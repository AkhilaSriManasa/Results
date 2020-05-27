####################### CMakeLists.txt (libopenshot) #########################
# @brief CMake build file for libopenshot (used to generate makefiles)
# @author Jonathan Thomas <jonathan@openshot.org>
#
# @section LICENSE
#
# Copyright (c) 2008-2019 OpenShot Studios, LLC
# <http://www.openshotstudios.com/>. This file is part of
# OpenShot Library (libopenshot), an open-source project dedicated to
# delivering high quality video editing and animation solutions to the
# world. For more information visit <http://www.openshot.org/>.
#
# OpenShot Library (libopenshot) is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenShot Library (libopenshot) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenShot Library. If not, see <http://www.gnu.org/licenses/>.
################################################################################

cmake_minimum_required(VERSION 3.2...3.14 FATAL_ERROR)

message("\
-----------------------------------------------------------------
          Welcome to the OpenShot Build System!

CMake will now check libopenshot's build dependencies and inform
you of any missing files or other issues.

For more information, please visit <http://www.openshot.org/>.
-----------------------------------------------------------------")

################ ADD CMAKE MODULES ##################
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/Modules")

################ PROJECT VERSION ####################
set(PROJECT_VERSION_FULL "0.2.4-dev1")
set(PROJECT_SO_VERSION 18)

# Remove the dash and anything following, to get the #.#.# version for project()
STRING(REGEX REPLACE "\-.*$" "" VERSION_NUM "${PROJECT_VERSION_FULL}")

################### SETUP PROJECT ###################
# This will define the following variables
# PROJECT_NAME
# PROJECT_VERSION, libopenshot_VERSION
# PROJECT_VERSION_MAJOR, libopenshot_VERSION_MAJOR
# PROJECT_VERSION_MINOR, libopenshot_VERSION_MINOR
# PROJECT_VERSION_PATCH, libopenshot_VERSION_PATCH
PROJECT(libopenshot LANGUAGES C CXX VERSION ${VERSION_NUM})

message("
Generating build files for OpenShot with CMake ${CMAKE_VERSION}
  Building ${PROJECT_NAME} (version ${PROJECT_VERSION})
  SO/API/ABI Version: ${PROJECT_SO_VERSION}
")

# Define install paths according to system conventions
# XXX: This must be AFTER THE PROJECT() COMMAND w/ languages enabled,
#      in order to properly configure CMAKE_INSTALL_LIBDIR path
include(GNUInstallDirs)

# Collect and display summary of options/dependencies
include(FeatureSummary)

################ OPTIONS ##################
# Optional build settings for libopenshot
option(USE_SYSTEM_JSONCPP "Use system installed JsonCpp, if found" ON)
option(DISABLE_BUNDLED_JSONCPP "Don't fall back to bundled JsonCpp" OFF)
option(DISABLE_TESTS "Don't build unit tests" OFF)
option(ENABLE_IWYU "Enable 'Include What You Use' scanner (CMake 3.3+)" OFF)
option(ENABLE_COVERAGE "Enable coverage reporting" OFF)

########## Configure Version.h header ##############
configure_file(include/OpenShotVersion.h.in include/OpenShotVersion.h @ONLY)
# We'll want that installed later
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/include/OpenShotVersion.h
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/libopenshot)

#### Enable C++11 (for std::shared_ptr support)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

IF (WIN32)
	SET_PROPERTY(GLOBAL PROPERTY WIN32 "WIN32")
ENDIF(WIN32)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}/include
  ${CMAKE_CURRENT_BINARY_DIR}/include)

############## Code Coverage #########################
if (DISABLE_TESTS AND ENABLE_COVERAGE)
  message(WARNING "ENABLE_COVERAGE requires tests, overriding DISABLE_TESTS")
  set(DISABLE_TESTS OFF CACHE BOOL "Don't build unit tests" FORCE)
endif()

if (ENABLE_COVERAGE)
  if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug")
    message(STATUS "Coverage enabled, setting build type to Debug")
  endif()
  include(CodeCoverage)
  APPEND_COVERAGE_COMPILER_FLAGS()
endif()
add_feature_info("Coverage" ENABLE_COVERAGE "analyze test coverage and generate report")

############## PROCESS src/ DIRECTORIES ##############
add_subdirectory(src)

################### DOCUMENTATION ###################
# Find Doxygen (used for documentation)
include(cmake/Modules/UseDoxygen.cmake)

# Doxygen was found
if (TARGET doc)
	message(STATUS "Doxygen found, documentation target enabled")
	message("\nTo compile documentation in doc/html, run: 'make doc'")

  # Install docs, if the user builds them with `make doc`
  install(CODE "MESSAGE(\"Checking for documentation files to install...\")")
  install(CODE "MESSAGE(\"(Compile with 'make doc' command, requires Doxygen)\")")

  install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/doc/html/
          DESTINATION ${CMAKE_INSTALL_DOCDIR}/API
          MESSAGE_NEVER # Don't spew about file copies
          OPTIONAL )    # No error if the docs aren't found
endif()

############# PROCESS tests/ DIRECTORY ##############
if(NOT DISABLE_TESTS)
  add_subdirectory(tests)
endif()

############## COVERAGE REPORTING #################
if (ENABLE_COVERAGE)
  setup_target_for_coverage_lcov(
    NAME coverage
    LCOV_ARGS "--no-external"
    EXECUTABLE openshot-test
    DEPENDENCIES openshot-test)
    message("Generate coverage report with 'make coverage'")
endif()

########### PRINT FEATURE SUMMARY ##############
feature_summary(WHAT ALL
    INCLUDE_QUIET_PACKAGES
    FATAL_ON_MISSING_REQUIRED_PACKAGES
    DESCRIPTION "Displaying feature summary\n\nBuild configuration:")
## Detailed Install Instructions

Operating system specific install instructions are located in:

* doc/INSTALL-LINUX.md
* doc/INSTALL-MAC.md
* doc/INSTALL-WINDOWS.md

## Getting Started

The best way to get started with libopenshot, is to learn about our build system, obtain all the source code, 
install a development IDE and tools, and better understand our dependencies. So, please read through the 
following sections, and follow the instructions. And keep in mind, that your computer is likely different 
than the one used when writing these instructions. Your file paths and versions of applications might be 
slightly different, so keep an eye out for subtle file path differences in the commands you type.

## Build Tools

CMake is the backbone of our build system.  It is a cross-platform build system, which checks for dependencies, 
locates header files and libraries, generates makefiles, and supports the cross-platform compiling of 
libopenshot and libopenshot-audio.  CMake uses an out-of-source build concept, where all temporary build 
files, such as makefiles, object files, and even the final binaries, are created outside of the source 
code folder, inside a /build/ sub-folder.  This prevents the build process from cluttering up the source 
code.  These instructions have only been tested with the GNU compiler (including MSYS2/MinGW for Windows).

## Dependencies

The following libraries are required to build libopenshot.  Instructions on how to install these 
dependencies vary for each operating system.  Libraries and Executables have been labeled in the 
list below to help distinguish between them.

* ### FFmpeg (libavformat, libavcodec, libavutil, libavdevice, libavresample, libswscale)
  * http://www.ffmpeg.org/ `(Library)`
  * This library is used to decode and encode video, audio, and image files.  It is also used to obtain information about media files, such as frame rate, sample rate, aspect ratio, and other common attributes.

* ### ImageMagick++ (libMagick++, libMagickWand, libMagickCore)
  * http://www.imagemagick.org/script/magick++.php `(Library)`
  * This library is **optional**, and used to decode and encode images.

* ### OpenShot Audio Library (libopenshot-audio)
  * https://github.com/OpenShot/libopenshot-audio/ `(Library)`
  * This library is used to mix, resample, host plug-ins, and play audio. It is based on the JUCE project, which is an outstanding audio library used by many different applications

* ### Qt 5 (libqt5)
  * http://www.qt.io/qt5/ `(Library)`
  * Qt5 is used to display video, store image data, composite images, apply image effects, and many other utility functions, such as file system manipulation, high resolution timers, etc...

* ### CMake (cmake)
  * http://www.cmake.org/ `(Executable)`
  * This executable is used to automate the generation of Makefiles, check for dependencies, and is the backbone of libopenshot’s cross-platform build process.

* ### SWIG (swig)
  * http://www.swig.org/ `(Executable)`
  * This executable is used to generate the Python and Ruby bindings for libopenshot. It is a simple and powerful wrapper for C++ libraries, and supports many languages.

* ### Python 3 (libpython)
  * http://www.python.org/ `(Executable and Library)`
  * This library is used by swig to create the Python (version 3+) bindings for libopenshot. This is also the official language used by OpenShot Video Editor (a graphical interface to libopenshot).

* ### Doxygen (doxygen)
  * http://www.stack.nl/~dimitri/doxygen/ `(Executable)`
  * This executable is used to auto-generate the documentation used by libopenshot.

* ### UnitTest++ (libunittest++)
  * https://github.com/unittest-cpp/ `(Library)`
  * This library is used to execute unit tests for libopenshot.  It contains many macros used to keep our unit testing code very clean and simple.

* ### ZeroMQ (libzmq)
  * http://zeromq.org/ `(Library)`
  * This library is used to communicate between libopenshot and other applications (publisher / subscriber). Primarily used to send debug data from libopenshot.

* ### OpenMP (-fopenmp)
  * http://openmp.org/wp/ `(Compiler Flag)`
  * If your compiler supports this flag (GCC, Clang, and most other compilers), it provides libopenshot with easy methods of using parallel programming techniques to improve performance and take advantage of multi-core processors.

## CMake Flags (Optional)
There are many different build flags that can be passed to cmake to adjust how libopenshot is compiled. Some of these flags might be required when compiling on certain OSes, just depending on how your build environment is setup. To add a build flag, follow this general syntax:  $ cmake -DMAGICKCORE_HDRI_ENABLE=1 -DENABLE_TESTS=1 ../

* MAGICKCORE_HDRI_ENABLE (default 0)
* MAGICKCORE_QUANTUM_DEPTH (default 0)
* OPENSHOT_IMAGEMAGICK_COMPATIBILITY (default 0)
* DISABLE_TESTS (default 0)
* CMAKE_PREFIX_PATH (`/location/to/missing/library/`)
* PYTHON_INCLUDE_DIR (`/location/to/python/include/`)
* PYTHON_LIBRARY (`/location/to/python/lib.a`)
* PYTHON_FRAMEWORKS (`/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/`)
* CMAKE_CXX_COMPILER (`/location/to/mingw/g++`)
* CMAKE_C_COMPILER (`/location/to/mingw/gcc`)

## Obtaining Source Code

The first step in installing libopenshot is to obtain the most recent source code. The source code is available on [GitHub](https://github.com/OpenShot/libopenshot). Use the following command to obtain the latest libopenshot source code.

```
git clone https://github.com/OpenShot/libopenshot.git
git clone https://github.com/OpenShot/libopenshot-audio.git
```

## Folder Structure (libopenshot)

The source code is divided up into the following folders.

* ### build/
   * This folder needs to be manually created, and is used by cmake to store the temporary build files, such as makefiles, as well as the final binaries (library and test executables).

* ### cmake/
   * This folder contains custom modules not included by default in cmake, used to find dependency libraries and headers and determine if these libraries are installed.

* ### doc/
   * This folder contains documentation and related files, such as logos and images required by the doxygen auto-generated documentation.

* ### include/
   * This folder contains all headers (*.h) used by libopenshot.

* ### src/
   * This folder contains all source code (*.cpp) used by libopenshot.

* ### tests/
   * This folder contains all unit test code.  Each class has it’s own test file (*.cpp), and uses UnitTest++ macros to keep the test code simple and manageable.

* ### thirdparty/
   * This folder contains code not written by the OpenShot team. For example, jsoncpp, an open-source JSON parser.

## Linux Build Instructions (libopenshot-audio)
To compile libopenshot-audio, we need to go through a few additional steps to manually build and install it. Launch a terminal and enter:

```
cd [libopenshot-audio repo folder]
mkdir build
cd build
cmake ../
make
make install
./src/openshot-audio-test-sound  (This should play a test sound)
```

## Linux Build Instructions (libopenshot)
Run the following commands to compile libopenshot:

```
cd [libopenshot repo directory]
mkdir -p build
cd build
cmake ../
make
make install
```

For more detailed instructions, please see:

* doc/INSTALL-LINUX.md
* doc/INSTALL-MAC.md
* doc/INSTALL-WINDOWS.md
OpenShot Video Library (libopenshot) is a free, open-source C++ library dedicated to
delivering high quality video editing, animation, and playback solutions to the 
world.

## Build Status

[![Build Status](https://img.shields.io/travis/OpenShot/libopenshot/develop.svg?label=libopenshot)](https://travis-ci.org/OpenShot/libopenshot) [![Build Status](https://img.shields.io/travis/OpenShot/libopenshot-audio/develop.svg?label=libopenshot-audio)](https://travis-ci.org/OpenShot/libopenshot-audio)

## Features

* Cross-Platform (Linux, Mac, and Windows)
* Multi-Layer Compositing
* Video and Audio Effects (Chroma Key, Color Adjustment, Grayscale, etc…)
* Animation Curves (Bézier, Linear, Constant)
* Time Mapping (Curve-based Slow Down, Speed Up, Reverse)
* Audio Mixing & Resampling (Curve-based)
* Audio Plug-ins (VST & AU)
* Audio Drivers (ASIO, WASAPI, DirectSound, CoreAudio, iPhone Audio, ALSA, JACK, and Android)
* Telecine and Inverse Telecine (Film to TV, TV to Film)
* Frame Rate Conversions
* Multi-Processor Support (Performance)
* Python and Ruby Bindings (All Features Supported)
* Qt Video Player Included (Ability to display video on any QWidget)
* Unit Tests (Stability)
* All FFmpeg Formats and Codecs Supported (Images, Videos, and Audio files)
* Full Documentation with Examples (Doxygen Generated)

## Install

Detailed instructions for building libopenshot and libopenshot-audio for each OS. These instructions
are also available in the /docs/ source folder.

   * [Linux](https://github.com/OpenShot/libopenshot/wiki/Linux-Build-Instructions)
   * [Mac](https://github.com/OpenShot/libopenshot/wiki/Mac-Build-Instructions)
   * [Windows](https://github.com/OpenShot/libopenshot/wiki/Windows-Build-Instructions)

## Hardware Acceleration

OpenShot now supports experimental hardware acceleration, both for encoding and
decoding videos. When enabled, this can either speed up those operations or slow
them down, depending on the power and features supported by your graphics card.
Please see [doc/HW-ACCELL.md](doc/HW-ACCEL.md) for more information.

## Documentation

Beautiful HTML documentation can be generated using Doxygen.
```
make doc
```
(Also available online: http://openshot.org/files/libopenshot/)

## Developers

Are you interested in becoming more involved in the development of 
OpenShot? Build exciting new features, fix bugs, make friends, and become a hero! 
Please read the [step-by-step](https://github.com/OpenShot/openshot-qt/wiki/Become-a-Developer) 
instructions for getting source code, configuring dependencies, and building OpenShot.

## Report a bug

You can report a new libopenshot issue directly on GitHub:

https://github.com/OpenShot/libopenshot/issues

## Websites

- https://www.openshot.org/  (Official website and blog)
- https://github.com/OpenShot/libopenshot/ (source code and issue tracker)
- https://github.com/OpenShot/libopenshot-audio/ (source code for audio library)
- https://github.com/OpenShot/openshot-qt/ (source code for Qt client)
- https://launchpad.net/openshot/

### License

Copyright (c) 2008-2019 OpenShot Studios, LLC.

OpenShot Library (libopenshot) is free software: you can redistribute it
and/or modify it under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

OpenShot Library (libopenshot) is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with OpenShot Library. If not, see http://www.gnu.org/licenses/.

To release a closed-source product which uses libopenshot (i.e. video
editing and playback), commercial licenses are also available: contact
sales@openshot.org for more information.
cmake_minimum_required(VERSION 2.8.1)
project(UnitTest++)

# get the main sources
file(GLOB SRCS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/*.cpp src/*.h)
source_group("" FILES ${SRCS})

# get platform specific sources
if (WIN32)
    set(PLAT_DIR Win32)
else()
    set(PLAT_DIR Posix)
endif(WIN32)
file(GLOB PLAT_SRCS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/${PLAT_DIR}/*.cpp src/${PLAT_DIR}/*.h)
source_group(${PLAT_DIR} FILES ${PLAT_SRCS})

# create the lib
add_library(UnitTestPP SHARED ${SRCS} ${PLAT_SRCS})
set_target_properties(UnitTestPP PROPERTIES OUTPUT_NAME UnitTest++)
include_directories(src)

# build the test runner
file(GLOB TEST_SRCS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/tests/*.cpp src/tests/*.h)
source_group( "" FILES ${TEST_SRCS})
add_executable(TestUnitTestPP ${TEST_SRCS})
set_target_properties(TestUnitTestPP PROPERTIES OUTPUT_NAME TestUnitTest++)
target_link_libraries(TestUnitTestPP UnitTestPP)

# turn on testing
enable_testing()
add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND} -V)

# add the test runner as a test
add_test(NAME TestUnitTestPP COMMAND TestUnitTest++ ${CONFIG_PATH} ${CONFIG_TASKS_PATH} ${SOUND_LOG_PATH})
add_dependencies(check TestUnitTestPP)
## Hardware Acceleration

OpenShot now has experimental support for hardware acceleration, which uses 1 (or more)
graphics cards to offload some of the work for both decoding and encoding. This is
very new and experimental (as of May 2019), but we look forward to "accelerating"
our support for this in the future!

The following table summarizes our current level of support:

|                    |  Linux Decode   | Linux Encode   | Mac Decode |    Mac Encode  | Windows Decode | Windows Encode | Notes            |
|--------------------|:---------------:|:--------------:|:----------:|:--------------:|:--------------:|:--------------:|------------------|
| VA-API             |   ✔️ &nbsp;      |    ✔️ &nbsp;    |      -     |        -       |       -        |        -       | *Linux Only*     |
| VDPAU              | ✔️ <sup>1</sup>  | ✅ <sup>2</sup> |      -    |        -       |       -        |        -       | *Linux Only*     |
| CUDA (NVDEC/NVENC) | ❌ <sup>3</sup> |   ✔️ &nbsp;     |      -     |        -       |       -        |    ✔️ &nbsp;    | *Cross Platform* |
| VideoToolBox       |           -     |         -      |  ✔️ &nbsp;  | ❌ <sup>4</sup> |      -        |       -         | *Mac Only*       |
| DXVA2              |           -     |         -      |      -     |        -       | ❌ <sup>3</sup> |      -         | *Windows Only*   |
| D3D11VA            |           -     |         -      |      -     |        -       | ❌ <sup>3</sup> |      -         | *Windows Only*   |
| QSV                | ❌ <sup>3</sup> |   ❌ &nbsp;   |  ❌ &nbsp; |   ❌ &nbsp;    |   ❌ &nbsp;     |    ❌ &nbsp;   | *Cross Platform* |

#### Notes

1.  VDPAU for some reason needs a card number one higher than it really is
2.  VDPAU is a decoder only
3.  Green frames (pixel data not correctly tranferred back to system memory)
4.  Crashes and burns

## Supported FFmpeg Versions

* HW accel is supported from FFmpeg version 3.2 (3.3 for nVidia drivers)
* HW accel was removed for nVidia drivers in Ubuntu for FFmpeg 4+

**Notice:** The FFmpeg versions of Ubuntu and PPAs for Ubuntu show the
same behaviour. FFmpeg 3 has working nVidia hardware acceleration while
FFmpeg 4+ has no support for nVidia hardware acceleration
included.

## OpenShot Settings

The following settings are use by libopenshot to enable, disable, and control
the various hardware acceleration features.

```{cpp}
/// Use video codec for faster video decoding (if supported)
int HARDWARE_DECODER = 0;

/* 0 - No acceleration
   1 - Linux VA-API
   2 - nVidia NVDEC
   3 - Windows D3D9
   4 - Windows D3D11
   5 - MacOS / VideoToolBox
   6 - Linux VDPAU
   7 - Intel QSV */

/// Number of threads of OpenMP
int OMP_THREADS = 12;

/// Number of threads that FFmpeg uses
int FF_THREADS = 8;

/// Maximum rows that hardware decode can handle
int DE_LIMIT_HEIGHT_MAX = 1100;

/// Maximum columns that hardware decode can handle
int DE_LIMIT_WIDTH_MAX = 1950;

/// Which GPU to use to decode (0 is the first, LINUX ONLY)
int HW_DE_DEVICE_SET = 0;

/// Which GPU to use to encode (0 is the first, LINUX ONLY)
int HW_EN_DEVICE_SET = 0;
```

## Libva / VA-API (Video Acceleration API)

The correct version of libva is needed (libva in Ubuntu 16.04 or libva2
in Ubuntu 18.04) for the AppImage to work with hardware acceleration.
An AppImage that works on both systems (supporting libva and libva2),
might be possible when no libva is included in the AppImage.

*  vaapi is working for intel and AMD
*  vaapi is working for decode only for nouveau
*  nVidia driver is working for export only

## AMD Graphics Cards (RadeonOpenCompute/ROCm)

Decoding and encoding on the (AMD) GPU is possible with the default drivers.
On systems where ROCm is installed and run a future use for GPU acceleration
of effects could be implemented (contributions welcome).

## Multiple Graphics Cards

If the computer has multiple graphics cards installed, you can choose which
should be used by libopenshot. Also, you can optionally use one card for
decoding and the other for encoding (if both cards support acceleration).
This is currently only supported on Linux, due to the device name FFmpeg
expects (i.e. **/dev/dri/render128**). Contributions welcome if anyone can
determine what string format to pass for Windows and Mac.

## Help Us Improve Hardware Support

This information might be wrong, and we would love to continue improving
our support for hardware acceleration in OpenShot. Please help us update
this document if you find an error or discover new and/or useful information.

**FFmpeg 4 + nVidia** The manual at:
https://www.tal.org/tutorials/ffmpeg_nvidia_encode
works pretty well. We could compile and install a version of FFmpeg 4.1.3
on Mint 19.1 that supports the GPU on nVidia cards. A version of openshot
with hardware support using these libraries could use the nVidia GPU.

**BUG:** Hardware supported decoding still has some bugs (as you can see from
the chart above). Also, the speed gains with decoding are not as great
as with encoding. Currently, if hardware decoding fails, there is no
fallback (you either get green frames or an "invalid file" error in OpenShot).
This needs to be improved to successfully fall-back to software decoding.

**Needed:**
  * A way to get options and limits of the GPU, such as
 supported dimensions (width and height).
  *  A way to list the actual Graphic Cards available to FFmpeg (for the
  user to choose which card for decoding and encoding, as opposed
  to "Graphics Card X")

**Further improvement:** Right now the frame can be decoded on the GPU, but the
frame is then copied to CPU memory for modifications. It is then copied back to
GPU memory for encoding. Using the GPU for both decoding and modifications
will make it possible to do away with these two copies. A possible solution would
be to use Vulkan compute which would be available on Linux and Windows natively
and on MacOS via MoltenVK.

## Credit

A big thanks to Peter M (https://github.com/eisneinechse) for all his work
on integrating hardware acceleration into libopenshot! The community thanks
you for this major contribution!
# Building libopenshot for Linux

## Getting Started

The best way to get started with libopenshot, is to learn about our build system, obtain all the source code, 
install a development IDE and tools, and better understand our dependencies. So, please read through the 
following sections, and follow the instructions. And keep in mind, that your computer is likely different 
than the one used when writing these instructions. Your file paths and versions of applications might be 
slightly different, so keep an eye out for subtle file path differences in the commands you type.

## Build Tools

CMake is the backbone of our build system.  It is a cross-platform build system, which checks for 
dependencies, locates header files and libraries, generates makefiles, and supports the cross-platform 
compiling of libopenshot and libopenshot-audio.  CMake uses an out-of-source build concept, where 
all temporary build files, such as makefiles, object files, and even the final binaries, are created 
outside of the source code folder, inside a /build/ sub-folder.  This prevents the build process 
from cluttering up the source code.  These instructions have only been tested with the GNU compiler 
(including MSYS2/MinGW for Windows).

## Dependencies

The following libraries are required to build libopenshot.  Instructions on how to install these 
dependencies vary for each operating system.  Libraries and Executables have been labeled in the 
list below to help distinguish between them.

### FFmpeg (libavformat, libavcodec, libavutil, libavdevice, libavresample, libswscale)
  * http://www.ffmpeg.org/ `(Library)`
  * This library is used to decode and encode video, audio, and image files.  It is also used to obtain information about media files, such as frame rate, sample rate, aspect ratio, and other common attributes.

### ImageMagick++ (libMagick++, libMagickWand, libMagickCore)
  * http://www.imagemagick.org/script/magick++.php `(Library)`
  * This library is **optional**, and used to decode and encode images.

### OpenShot Audio Library (libopenshot-audio)
  * https://github.com/OpenShot/libopenshot-audio/ `(Library)`
  * This library is used to mix, resample, host plug-ins, and play audio. It is based on the JUCE project, which is an outstanding audio library used by many different applications

### Qt 5 (libqt5)
  * http://www.qt.io/qt5/ `(Library)`
  * Qt5 is used to display video, store image data, composite images, apply image effects, and many other utility functions, such as file system manipulation, high resolution timers, etc...

### CMake (cmake)
  * http://www.cmake.org/ `(Executable)`
  * This executable is used to automate the generation of Makefiles, check for dependencies, and is the backbone of libopenshot’s cross-platform build process.

### SWIG (swig)
  * http://www.swig.org/ `(Executable)`
  * This executable is used to generate the Python and Ruby bindings for libopenshot. It is a simple and powerful wrapper for C++ libraries, and supports many languages.

### Python 3 (libpython)
  * http://www.python.org/ `(Executable and Library)`
  * This library is used by swig to create the Python (version 3+) bindings for libopenshot. This is also the official language used by OpenShot Video Editor (a graphical interface to libopenshot).

### Doxygen (doxygen)
  * http://www.stack.nl/~dimitri/doxygen/ `(Executable)`
  * This executable is used to auto-generate the documentation used by libopenshot.

### UnitTest++ (libunittest++)
  * https://github.com/unittest-cpp/ `(Library)`
  * This library is used to execute unit tests for libopenshot.  It contains many macros used to keep our unit testing code very clean and simple.

### ZeroMQ (libzmq)
  * http://zeromq.org/ `(Library)`
  * This library is used to communicate between libopenshot and other applications (publisher / subscriber). Primarily used to send debug data from libopenshot.

### OpenMP (-fopenmp)
  * http://openmp.org/wp/ `(Compiler Flag)`
  * If your compiler supports this flag (GCC, Clang, and most other compilers), it provides libopenshot with easy methods of using parallel programming techniques to improve performance and take advantage of multi-core processors.


## CMake Flags (Optional)
There are many different build flags that can be passed to cmake to adjust how libopenshot is 
compiled. Some of these flags might be required when compiling on certain OSes, just depending 
on how your build environment is setup. To add a build flag, follow this general syntax: 
`cmake -DMAGICKCORE_HDRI_ENABLE=1 -DENABLE_TESTS=1 ../`

* MAGICKCORE_HDRI_ENABLE (default 0)
* MAGICKCORE_QUANTUM_DEPTH (default 0)
* OPENSHOT_IMAGEMAGICK_COMPATIBILITY (default 0)
* DISABLE_TESTS (default 0)
* CMAKE_PREFIX_PATH (`/location/to/missing/library/`)
* PYTHON_INCLUDE_DIR (`/location/to/python/include/`)
* PYTHON_LIBRARY (`/location/to/python/lib.a`)
* PYTHON_FRAMEWORKS (`/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/`)
* CMAKE_CXX_COMPILER (`/location/to/mingw/g++`)
* CMAKE_C_COMPILER (`/location/to/mingw/gcc`)

## Obtaining Source Code

The first step in installing libopenshot is to obtain the most recent source code. The source code is 
available on [GitHub](https://github.com/OpenShot/libopenshot). Use the following command 
to obtain the latest libopenshot source code.

```
git clone https://github.com/OpenShot/libopenshot.git
git clone https://github.com/OpenShot/libopenshot-audio.git
```

## Folder Structure (libopenshot)

The source code is divided up into the following folders.

### build/
   * This folder needs to be manually created, and is used by cmake to store the temporary build files, such as makefiles, as well as the final binaries (library and test executables).

### cmake/
   * This folder contains custom modules not included by default in cmake, used to find dependency libraries and headers and determine if these libraries are installed.

### doc/
   * This folder contains documentation and related files, such as logos and images required by the doxygen auto-generated documentation.

### include/
   * This folder contains all headers (*.h) used by libopenshot.

### src/
   * This folder contains all source code (*.cpp) used by libopenshot.

### tests/
   * This folder contains all unit test code.  Each class has it’s own test file (*.cpp), and uses UnitTest++ macros to keep the test code simple and manageable.

### thirdparty/
   * This folder contains code not written by the OpenShot team. For example, jsoncpp, an open-source JSON parser.

## Install Dependencies

In order to actually compile libopenshot, we need to install some dependencies on your system. The easiest 
way to accomplish this is with our Daily PPA. A PPA is an unofficial Ubuntu repository, which has our 
software packages available to download and install.

```
   sudo add-apt-repository ppa:openshot.developers/libopenshot-daily
   sudo apt-get update
   sudo apt-get install openshot-qt \
                        cmake \
                        libx11-dev \
                        libasound2-dev \
                        libavcodec-dev \
                        libavdevice-dev \
                        libavfilter-dev \
                        libavformat-dev \
                        libavresample-dev \
                        libavutil-dev \
                        libfdk-aac-dev \
                        libfreetype6-dev \
                        libjsoncpp-dev \
                        libmagick++-dev \
                        libopenshot-audio-dev \
                        libswscale-dev \
                        libunittest++-dev \
                        libxcursor-dev \
                        libxinerama-dev \
                        libxrandr-dev \
                        libzmq3-dev \
                        pkg-config \
                        python3-dev \
                        qtbase5-dev \
                        qtmultimedia5-dev \
                        swig
```

## Linux Build Instructions (libopenshot-audio)
To compile libopenshot-audio, we need to go through a few additional steps to manually build and 
install it. Launch a terminal and enter:

```
cd [libopenshot-audio repo folder]
mkdir build
cd build
cmake ../
make
make install
./src/openshot-audio-test-sound  (This should play a test sound)
```

## Linux Build Instructions (libopenshot)
Run the following commands to compile libopenshot:

```
cd [libopenshot repo directory]
mkdir -p build
cd build
cmake ../
make
```

If you are missing any dependencies for libopenshot, you might receive error messages at this point. 
Just install the missing packages (usually with a -dev suffix), and run the above commands again. 
Repeat until no error messages are displayed, and the build process completes. Also, if you manually
install Qt 5, you might need to specify the location for cmake:

```
cmake -DCMAKE_PREFIX_PATH=/qt5_path/qt5/5.2.0/ ../
```

To run all unit tests (and verify everything is working correctly), launch a terminal, and enter:

```
make test
```

To auto-generate documentation for libopenshot, launch a terminal, and enter:

```
make doc
```

This will use doxygen to generate a folder of HTML files, with all classes and methods documented. The 
folder is located at **build/doc/html/**. Once libopenshot has been successfully built, we need to 
install it (i.e. copy it to the correct folder, so other libraries can find it).

```
make install
```

This will copy the binary files to /usr/local/lib/, and the header files to /usr/local/include/openshot/... 
This is where other projects will look for the libopenshot files when building. Python 3 bindings are 
also installed at this point. let's verify the python bindings work:

```
python3
>>> import openshot
```

If no errors are displayed, you have successfully compiled and installed libopenshot on your system. 
Congratulations and be sure to read our wiki on [Becoming an OpenShot Developer](https://github.com/OpenShot/openshot-qt/wiki/Become-a-Developer)! 
Welcome to the OpenShot developer community! We look forward to meeting you!
# Building libopenshot for MacOS

## Getting Started

The best way to get started with libopenshot, is to learn about our build system, obtain all the source code, 
install a development IDE and tools, and better understand our dependencies. So, please read through the 
following sections, and follow the instructions. And keep in mind, that your computer is likely different 
than the one used when writing these instructions. Your file paths and versions of applications might be 
slightly different, so keep an eye out for subtle file path differences in the commands you type.

## Build Tools

CMake is the backbone of our build system.  It is a cross-platform build system, which checks for 
dependencies, locates header files and libraries, generates makefiles, and supports the cross-platform 
compiling of libopenshot and libopenshot-audio.  CMake uses an out-of-source build concept, where 
all temporary build files, such as makefiles, object files, and even the final binaries, are created 
outside of the source code folder, inside a /build/ sub-folder.  This prevents the build process 
from cluttering up the source code.  These instructions have only been tested with the GNU compiler 
(including MSYS2/MinGW for Windows).

## Dependencies

The following libraries are required to build libopenshot.  Instructions on how to install these 
dependencies vary for each operating system.  Libraries and Executables have been labeled in the 
list below to help distinguish between them.

### FFmpeg (libavformat, libavcodec, libavutil, libavdevice, libavresample, libswscale)
  * http://www.ffmpeg.org/ `(Library)`
  * This library is used to decode and encode video, audio, and image files.  It is also used to obtain information about media files, such as frame rate, sample rate, aspect ratio, and other common attributes.

### ImageMagick++ (libMagick++, libMagickWand, libMagickCore)
  * http://www.imagemagick.org/script/magick++.php `(Library)`
  * This library is **optional**, and used to decode and encode images.

### OpenShot Audio Library (libopenshot-audio)
  * https://github.com/OpenShot/libopenshot-audio/ `(Library)`
  * This library is used to mix, resample, host plug-ins, and play audio. It is based on the JUCE project, which is an outstanding audio library used by many different applications

### Qt 5 (libqt5)
  * http://www.qt.io/qt5/ `(Library)`
  * Qt5 is used to display video, store image data, composite images, apply image effects, and many other utility functions, such as file system manipulation, high resolution timers, etc...

### CMake (cmake)
  * http://www.cmake.org/ `(Executable)`
  * This executable is used to automate the generation of Makefiles, check for dependencies, and is the backbone of libopenshot’s cross-platform build process.

### SWIG (swig)
  * http://www.swig.org/ `(Executable)`
  * This executable is used to generate the Python and Ruby bindings for libopenshot. It is a simple and powerful wrapper for C++ libraries, and supports many languages.

### Python 3 (libpython)
  * http://www.python.org/ `(Executable and Library)`
  * This library is used by swig to create the Python (version 3+) bindings for libopenshot. This is also the official language used by OpenShot Video Editor (a graphical interface to libopenshot).

### Doxygen (doxygen)
  * http://www.stack.nl/~dimitri/doxygen/ `(Executable)`
  * This executable is used to auto-generate the documentation used by libopenshot.

### UnitTest++ (libunittest++)
  * https://github.com/unittest-cpp/ `(Library)`
  * This library is used to execute unit tests for libopenshot.  It contains many macros used to keep our unit testing code very clean and simple.

### ZeroMQ (libzmq)
  * http://zeromq.org/ `(Library)`
  * This library is used to communicate between libopenshot and other applications (publisher / subscriber). Primarily used to send debug data from libopenshot.

### OpenMP (-fopenmp)
  * http://openmp.org/wp/ `(Compiler Flag)`
  * If your compiler supports this flag (GCC, Clang, and most other compilers), it provides libopenshot with easy methods of using parallel programming techniques to improve performance and take advantage of multi-core processors.

## CMake Flags (Optional)
There are many different build flags that can be passed to cmake to adjust how libopenshot is compiled. 
Some of these flags might be required when compiling on certain OSes, just depending on how your build 
environment is setup. To add a build flag, follow this general syntax: 
`cmake -DMAGICKCORE_HDRI_ENABLE=1 -DENABLE_TESTS=1 ../`

* MAGICKCORE_HDRI_ENABLE (default 0)
* MAGICKCORE_QUANTUM_DEPTH (default 0)
* OPENSHOT_IMAGEMAGICK_COMPATIBILITY (default 0)
* DISABLE_TESTS (default 0)
* CMAKE_PREFIX_PATH (`/location/to/missing/library/`)
* PYTHON_INCLUDE_DIR (`/location/to/python/include/`)
* PYTHON_LIBRARY (`/location/to/python/lib.a`)
* PYTHON_FRAMEWORKS (`/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/`)
* CMAKE_CXX_COMPILER (`/location/to/mingw/g++`)
* CMAKE_C_COMPILER (`/location/to/mingw/gcc`)

## Obtaining Source Code

The first step in installing libopenshot is to obtain the most recent source code. The source code 
is available on [GitHub](https://github.com/OpenShot/libopenshot). Use the following command to 
obtain the latest libopenshot source code.

```
git clone https://github.com/OpenShot/libopenshot.git
git clone https://github.com/OpenShot/libopenshot-audio.git
```

## Folder Structure (libopenshot)

The source code is divided up into the following folders.

### build/
   * This folder needs to be manually created, and is used by cmake to store the temporary build files, such as makefiles, as well as the final binaries (library and test executables).

### cmake/
   * This folder contains custom modules not included by default in cmake, used to find dependency libraries and headers and determine if these libraries are installed.

### doc/
   * This folder contains documentation and related files, such as logos and images required by the doxygen auto-generated documentation.

### include/
   * This folder contains all headers (*.h) used by libopenshot.

### src/
   * This folder contains all source code (*.cpp) used by libopenshot.

### tests/
   * This folder contains all unit test code.  Each class has it’s own test file (*.cpp), and uses UnitTest++ macros to keep the test code simple and manageable.

### thirdparty/
   * This folder contains code not written by the OpenShot team. For example, jsoncpp, an open-source JSON parser.

## Install Dependencies

In order to actually compile libopenshot and libopenshot-audio, we need to install some dependencies on 
your system. Most packages needed by libopenshot can be installed easily with Homebrew. However, first 
install Xcode with the following options ("UNIX Development", "System Tools", "Command Line Tools", or 
"Command Line Support"). Be sure to refresh your list of Homebrew packages with the “brew update” command.

**NOTE:** Homebrew seems to work much better for most users (compared to MacPorts), so I am going to 
focus on brew for this guide.

Install the following packages using the Homebrew package installer (http://brew.sh/). Pay close attention 
to any warnings or errors during these brew installs. NOTE: You might have some conflicting libraries in 
your /usr/local/ folders, so follow the directions from brew if these are detected.

```
brew install gcc48 --enable-all-languages
brew install ffmpeg
brew install librsvg
brew install swig
brew install doxygen
brew install unittest-cpp --cc=gcc-4.8. You must specify the c++ compiler with the --cc flag to be 4.7 or 4.8.
brew install qt5
brew install cmake
brew install zeromq
```

## Mac Build Instructions (libopenshot-audio)
Since libopenshot-audio is not available in a Homebrew or MacPorts package, we need to go through a 
few additional steps to manually build and install it. Launch a terminal and enter:

```
cd [libopenshot-audio repo folder]
mkdir build
cd build
cmake -d -G "Unix Makefiles" -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang ../   (CLang must be used due to GNU incompatible Objective-C code in some of the Apple frameworks)
make
make install
./src/openshot-audio-test-sound  (This should play a test sound)
```

## Mac Build Instructions (libopenshot)
Run the following commands to build libopenshot:

```
$ cd [libopenshot repo folder]
$ mkdir build
$ cd build
$ cmake -G "Unix Makefiles"  -DCMAKE_CXX_COMPILER=/usr/local/opt/gcc48/bin/g++-4.8 -DCMAKE_C_COMPILER=/usr/local/opt/gcc48/bin/gcc-4.8 -DCMAKE_PREFIX_PATH=/usr/local/Cellar/qt5/5.4.2/ -DPYTHON_INCLUDE_DIR=/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/include/python3.3m/ -DPYTHON_LIBRARY=/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/libpython3.3.dylib -DPython_FRAMEWORKS=/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/ ../ -D"CMAKE_BUILD_TYPE:STRING=Debug"
```

The extra arguments on the cmake command make sure the compiler will be gcc4.8 and that cmake 
knows where to look for the Qt header files and Python library. Double check these file paths, 
as yours will likely be different.

```
make
```

If you are missing any dependencies for libopenshot, you will receive error messages at this point. 
Just install the missing dependencies, and run the above commands again. Repeat until no error 
messages are displayed and the build process completes.

Also, if you are having trouble building, please see the CMake Flags section above, as it might 
provide a solution for finding a missing folder path, missing Python 3 library, etc...

To run all unit tests (and verify everything is working correctly), launch a terminal, and enter:

```
make test
```

To auto-generate the documentation for libopenshot, launch a terminal, and enter:

```
make doc
```

This will use doxygen to generate a folder of HTML files, with all classes and methods documented. 
The folder is located at build/doc/html/. Once libopenshot has been successfully built, we need 
to install it (i.e. copy it to the correct folder, so other libraries can find it).

```
make install
```

This should copy the binary files to /usr/local/lib/, and the header files to /usr/local/include/openshot/... 
This is where other projects will look for the libopenshot files when building. Python 3 bindings are 
also installed at this point. let's verify the python bindings work:

```
python3 (or python)
>>> import openshot
```

If no errors are displayed, you have successfully compiled and installed libopenshot on your 
system. Congratulations and be sure to read our wiki on [Becoming an OpenShot Developer](https://github.com/OpenShot/openshot-qt/wiki/Become-a-Developer)! 
Welcome to the OpenShot developer community! We look forward to meeting you!
# Building libopenshot for Windows

## Getting Started

The best way to get started with libopenshot, is to learn about our build system, obtain all the 
source code, install a development IDE and tools, and better understand our dependencies. So, 
please read through the following sections, and follow the instructions. And keep in mind, 
that your computer is likely different than the one used when writing these instructions. 
Your file paths and versions of applications might be slightly different, so keep an eye out 
for subtle file path differences in the commands you type.

## Build Tools

CMake is the backbone of our build system.  It is a cross-platform build system, which 
checks for dependencies, locates header files and libraries, generates makefiles, and 
supports the cross-platform compiling of libopenshot and libopenshot-audio.  CMake uses 
an out-of-source build concept, where all temporary build files, such as makefiles, 
object files, and even the final binaries, are created outside of the source code 
folder, inside a /build/ sub-folder.  This prevents the build process from cluttering 
up the source code.  These instructions have only been tested with the GNU compiler 
(including MSYS2/MinGW for Windows).

## Dependencies

The following libraries are required to build libopenshot.  Instructions on how to 
install these dependencies vary for each operating system.  Libraries and Executables 
have been labeled in the list below to help distinguish between them.

### FFmpeg (libavformat, libavcodec, libavutil, libavdevice, libavresample, libswscale)
  * http://www.ffmpeg.org/ `(Library)`
  * This library is used to decode and encode video, audio, and image files.  It is also used to obtain information about media files, such as frame rate, sample rate, aspect ratio, and other common attributes.

### ImageMagick++ (libMagick++, libMagickWand, libMagickCore)
  * http://www.imagemagick.org/script/magick++.php `(Library)`
  * This library is **optional**, and used to decode and encode images.

### OpenShot Audio Library (libopenshot-audio)
  * https://github.com/OpenShot/libopenshot-audio/ `(Library)`
  * This library is used to mix, resample, host plug-ins, and play audio. It is based on the JUCE project, which is an outstanding audio library used by many different applications

### Qt 5 (libqt5)
  * http://www.qt.io/qt5/ `(Library)`
  * Qt5 is used to display video, store image data, composite images, apply image effects, and many other utility functions, such as file system manipulation, high resolution timers, etc...

### CMake (cmake)
  * http://www.cmake.org/ `(Executable)`
  * This executable is used to automate the generation of Makefiles, check for dependencies, and is the backbone of libopenshot’s cross-platform build process.

### SWIG (swig)
  * http://www.swig.org/ `(Executable)`
  * This executable is used to generate the Python and Ruby bindings for libopenshot. It is a simple and powerful wrapper for C++ libraries, and supports many languages.

### Python 3 (libpython)
  * http://www.python.org/ `(Executable and Library)`
  * This library is used by swig to create the Python (version 3+) bindings for libopenshot. This is also the official language used by OpenShot Video Editor (a graphical interface to libopenshot).

### Doxygen (doxygen)
  * http://www.stack.nl/~dimitri/doxygen/ `(Executable)`
  * This executable is used to auto-generate the documentation used by libopenshot.

### UnitTest++ (libunittest++)
  * https://github.com/unittest-cpp/ `(Library)`
  * This library is used to execute unit tests for libopenshot.  It contains many macros used to keep our unit testing code very clean and simple.

### ZeroMQ (libzmq)
  * http://zeromq.org/ `(Library)`
  * This library is used to communicate between libopenshot and other applications (publisher / subscriber). Primarily used to send debug data from libopenshot.

### OpenMP (-fopenmp)
  * http://openmp.org/wp/ `(Compiler Flag)`
  * If your compiler supports this flag (GCC, Clang, and most other compilers), it provides libopenshot with easy methods of using parallel programming techniques to improve performance and take advantage of multi-core processors.

## CMake Flags (Optional)
There are many different build flags that can be passed to cmake to adjust how libopenshot 
is compiled. Some of these flags might be required when compiling on certain OSes, just 
depending on how your build environment is setup. To add a build flag, follow this general 
syntax: `cmake -DMAGICKCORE_HDRI_ENABLE=1 -DENABLE_TESTS=1 ../`

* MAGICKCORE_HDRI_ENABLE (default 0)
* MAGICKCORE_QUANTUM_DEPTH (default 0)
* OPENSHOT_IMAGEMAGICK_COMPATIBILITY (default 0)
* DISABLE_TESTS (default 0)
* CMAKE_PREFIX_PATH (`/location/to/missing/library/`)
* PYTHON_INCLUDE_DIR (`/location/to/python/include/`)
* PYTHON_LIBRARY (`/location/to/python/lib.a`)
* PYTHON_FRAMEWORKS (`/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/`)
* CMAKE_CXX_COMPILER (`/location/to/mingw/g++`)
* CMAKE_C_COMPILER (`/location/to/mingw/gcc`)

## Environment Variables

Many environment variables will need to be set during this Windows installation guide. 
The command line will need to be closed and re-launched after any changes to your environment 
variables. Also, dependency libraries will not be found during linking or execution without 
being found in the PATH environment variable. So, if you get errors related to missing 
commands or libraries, double check the PATH variable.

The following environment variables need to be added to your “System Variables”.  Be sure to 
check each folder path for accuracy, as your paths will likely be different than this list.

### Example Variables

* DL_DIR (`C:\libdl`)
* DXSDK_DIR (`C:\Program Files\Microsoft DirectX SDK (June 2010)\`)
* FFMPEGDIR (`C:\ffmpeg-git-95f163b-win32-dev`)
* FREETYPE_DIR (`C:\Program Files\GnuWin32`)
* HOME (`C:\msys\1.0\home`)
* LIBOPENSHOT_AUDIO_DIR (`C:\Program Files\libopenshot-audio`)
* QTDIR (`C:\qt5`)
* SNDFILE_DIR (`C:\Program Files\libsndfile`)
* UNITTEST_DIR (`C:\UnitTest++`)
* ZMQDIR (`C:\msys2\usr\local\`)
* PATH (`The following paths are an example`)
   * `C:\Qt5\bin; C:\Qt5\MinGW\bin\; C:\msys\1.0\local\lib; C:\Program Files\CMake 2.8\bin; C:\UnitTest++\build; C:\libopenshot\build\src; C:\Program Files\doxygen\bin; C:\ffmpeg-git-95f163b-win32-dev\lib; C:\swigwin-2.0.4; C:\Python33; C:\Program Files\Project\lib; C:\msys2\usr\local\`





## Obtaining Source Code

The first step in installing libopenshot is to obtain the most recent source code. The source code 
is available on [GitHub](https://github.com/OpenShot/libopenshot). Use the following command to 
obtain the latest libopenshot source code.

```
git clone https://github.com/OpenShot/libopenshot.git
git clone https://github.com/OpenShot/libopenshot-audio.git
```

## Folder Structure (libopenshot)

The source code is divided up into the following folders.

### build/
   * This folder needs to be manually created, and is used by cmake to store the temporary 
   build files, such as makefiles, as well as the final binaries (library and test executables).

### cmake/
   * This folder contains custom modules not included by default in cmake, used to find 
   dependency libraries and headers and determine if these libraries are installed.

### doc/
   * This folder contains documentation and related files, such as logos and images 
   required by the doxygen auto-generated documentation.

### include/
   * This folder contains all headers (*.h) used by libopenshot.

### src/
   * This folder contains all source code (*.cpp) used by libopenshot.

### tests/
   * This folder contains all unit test code.  Each class has it’s own test file (*.cpp), and 
   uses UnitTest++ macros to keep the test code simple and manageable.

### thirdparty/
   * This folder contains code not written by the OpenShot team. For example, jsoncpp, an 
   open-source JSON parser.

## Install MSYS2 Dependencies

Most Windows dependencies needed for libopenshot-audio, libopenshot, and openshot-qt
can be installed easily with MSYS2 and the pacman package manager. Follow these
directions to setup a Windows build environment for OpenShot.

1) Install MSYS2: http://www.msys2.org/

2) Run MSYS2 command prompt (for example: `C:\msys64\msys2_shell.cmd`)

3) Append PATH (so MSYS2 can find executables and libraries):

```
PATH=$PATH:/c/msys64/mingw64/bin:/c/msys64/mingw64/lib     (64-bit PATH)
  or 
PATH=$PATH:/c/msys32/mingw32/bin:/c/msys32/mingw32/lib     (32-bit PATH)
```

4) Update and upgrade all packages

```
pacman -Syu
```

5a) Install the following packages (**64-Bit**)

```
pacman -S --needed base-devel mingw-w64-x86_64-toolchain
pacman -S mingw64/mingw-w64-x86_64-ffmpeg
pacman -S mingw64/mingw-w64-x86_64-python3-pyqt5
pacman -S mingw64/mingw-w64-x86_64-swig
pacman -S mingw64/mingw-w64-x86_64-cmake
pacman -S mingw64/mingw-w64-x86_64-doxygen
pacman -S mingw64/mingw-w64-x86_64-python3-pip
pacman -S mingw32/mingw-w64-i686-zeromq
pacman -S mingw64/mingw-w64-x86_64-python3-pyzmq
pacman -S mingw64/mingw-w64-x86_64-python3-cx_Freeze
pacman -S git

# Install ImageMagick if needed (OPTIONAL and NOT NEEDED)
pacman -S mingw64/mingw-w64-x86_64-imagemagick
```
  
5b) **Or** Install the following packages (**32-Bit**)

```
pacman -S --needed base-devel mingw32/mingw-w64-i686-toolchain
pacman -S mingw32/mingw-w64-i686-ffmpeg
pacman -S mingw32/mingw-w64-i686-python3-pyqt5
pacman -S mingw32/mingw-w64-i686-swig
pacman -S mingw32/mingw-w64-i686-cmake
pacman -S mingw32/mingw-w64-i686-doxygen
pacman -S mingw32/mingw-w64-i686-python3-pip
pacman -S mingw32/mingw-w64-i686-zeromq
pacman -S mingw32/mingw-w64-i686-python3-pyzmq
pacman -S mingw32/mingw-w64-i686-python3-cx_Freeze
pacman -S git

# Install ImageMagick if needed (OPTIONAL and NOT NEEDED)
pacman -S mingw32/mingw-w32-x86_32-imagemagick
```

6) Install Python PIP Dependencies
 
```
pip3 install httplib2
pip3 install slacker
pip3 install tinys3
pip3 install github3.py
pip3 install requests
```  

7) Download Unittest++ (https://github.com/unittest-cpp/unittest-cpp) into /MSYS2/[USER]/unittest-cpp-master/

``` 
cmake -G "MSYS Makefiles" ../ -DCMAKE_MAKE_PROGRAM=mingw32-make -DCMAKE_INSTALL_PREFIX:PATH=/usr
mingw32-make install
```

8) ZMQ++ Header (This might not be needed anymore)
  NOTE: Download and copy zmq.hpp into the /c/msys64/mingw64/include/ folder

## Manual Dependencies

### DLfcn
   * https://github.com/dlfcn-win32/dlfcn-win32
   * Download and Extract the Win32 Static (.tar.bz2) archive to a local folder: `C:\libdl\`
   * Create an environment variable called DL_DIR and set the value to `C:\libdl\`. This environment variable will be used by CMake to find the binary and header file.

### DirectX SDK / Windows SDK
   * Windows 7: (DirectX SDK) http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=6812
   * Windows 8: (Windows SDK)
   * https://msdn.microsoft.com/en-us/windows/desktop/aa904949
   * Download and Install the SDK Setup program.  This is needed for the JUCE library to play audio on Windows.
Create an environment variable called DXSDK_DIR and set the value to `C:\Program Files\Microsoft DirectX SDK (June 2010)\` (your path might be different). This environment variable will be used by CMake to find the binaries and header files.

### libSndFile
   * http://www.mega-nerd.com/libsndfile/#Download
   * Download and Install the Win32 Setup program.
   * Create an environment variable called SNDFILE_DIR and set the value to `C:\Program Files\libsndfile`. This environment variable will be used by CMake to find the binary and header files.

### libzmq
   * http://zeromq.org/intro:get-the-software
   * Download source code (zip)
   * Follow their instructions, and build with mingw
   * Create an environment variable called ZMQDIR and set the value to `C:\libzmq\build\` (the location of the compiled version). This environment variable will be used by CMake to find the binary and header files.

## Windows Build Instructions (libopenshot-audio)
In order to compile libopenshot-audio, launch a command prompt and enter the following commands. This does not require the MSYS2 prompt, but it should work in both the Windows command prompt and the MSYS2 prompt.

```
cd [libopenshot-audio repo folder]
mkdir build
cd build
cmake -G “MinGW Makefiles” ../
mingw32-make
mingw32-make install
openshot-audio-test-sound  (This should play a test sound)
```

## Windows Build Instructions (libopenshot)
Run the following commands to build libopenshot:

```
cd [libopenshot repo folder]
mkdir build
cd build
cmake -G "MinGW Makefiles" -DPYTHON_INCLUDE_DIR="C:/Python34/include/" -DPYTHON_LIBRARY="C:/Python34/libs/libpython34.a" ../
mingw32-make
```

If you are missing any dependencies for libopenshot, you will receive error messages at this point. 
Just install the missing dependencies, and run the above commands again. Repeat until no error 
messages are displayed and the build process completes.

Also, if you are having trouble building, please see the CMake Flags section above, as 
it might provide a solution for finding a missing folder path, missing Python 3 library, etc...

To run all unit tests (and verify everything is working correctly), launch a terminal, and enter:

```
mingw32-make test
```

To auto-generate the documentation for libopenshot, launch a terminal, and enter:

```
mingw32-make doc
```

This will use doxygen to generate a folder of HTML files, with all classes and methods 
documented. The folder is located at build/doc/html/. Once libopenshot has been successfully 
built, we need to install it (i.e. copy it to the correct folder, so other libraries can find it).

```
mingw32-make install
```

This should copy the binary files to `C:\Program Files\openshot\lib\`, and the header 
files to `C:\Program Files\openshot\include\...`  This is where other projects will 
look for the libopenshot files when building.. Python 3 bindings are also installed 
at this point. let's verify the python bindings work:

```
python3
>>> import openshot
```

If no errors are displayed, you have successfully compiled and installed libopenshot on 
your system. Congratulations and be sure to read our wiki on [Becoming an OpenShot Developer](https://github.com/OpenShot/openshot-qt/wiki/Become-a-Developer)! 
Welcome to the OpenShot developer community! We look forward to meeting you!
####################### CMakeLists.txt (libopenshot) #########################
# @brief CMake build file for libopenshot (used to generate makefiles)
# @author Jonathan Thomas <jonathan@openshot.org>
#
# @section LICENSE
#
# Copyright (c) 2008-2019 OpenShot Studios, LLC
# <http://www.openshotstudios.com/>. This file is part of
# OpenShot Library (libopenshot), an open-source project dedicated to
# delivering high quality video editing and animation solutions to the
# world. For more information visit <http://www.openshot.org/>.
#
# OpenShot Library (libopenshot) is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenShot Library (libopenshot) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenShot Library. If not, see <http://www.gnu.org/licenses/>.
################################################################################

# Collect and display summary of options/dependencies
include(FeatureSummary)

# Automatically process Qt classes with meta-object compiler
set(CMAKE_AUTOMOC True)

################ WINDOWS ##################
# Set some compiler options for Windows
# required for libopenshot-audio headers
IF (WIN32)
	add_definitions( -DIGNORE_JUCE_HYPOT=1 )
	SET(CMAKE_CXX_FLAGS " ${CMAKE_CXX_FLAGS} -include cmath")
ENDIF(WIN32)
IF (APPLE)
	# If you still get errors compiling with GCC 4.8, mac headers need to be patched: http://hamelot.co.uk/programming/osx-gcc-dispatch_block_t-has-not-been-declared-invalid-typedef/
	SET_PROPERTY(GLOBAL PROPERTY JUCE_MAC "JUCE_MAC")
	ADD_DEFINITIONS(-DNDEBUG)
	SET(EXTENSION "mm")

	SET(JUCE_PLATFORM_SPECIFIC_DIR build/macosx/platform_specific_code)
	SET(JUCE_PLATFORM_SPECIFIC_LIBRARIES "-framework Carbon -framework Cocoa -framework CoreFoundation -framework CoreAudio -framework CoreMidi -framework IOKit -framework AGL -framework AudioToolbox -framework QuartzCore -lobjc -framework Accelerate")
ENDIF(APPLE)

################ IMAGE MAGICK ##################
# Set the Quantum Depth that ImageMagick was built with (default to 16 bits)
IF (MAGICKCORE_QUANTUM_DEPTH)
	add_definitions( -DMAGICKCORE_QUANTUM_DEPTH=${MAGICKCORE_QUANTUM_DEPTH} )
ELSE (MAGICKCORE_QUANTUM_DEPTH)
	add_definitions( -DMAGICKCORE_QUANTUM_DEPTH=16 )
ENDIF (MAGICKCORE_QUANTUM_DEPTH)
IF (MAGICKCORE_HDRI_ENABLE)
	add_definitions( -DMAGICKCORE_HDRI_ENABLE=${MAGICKCORE_HDRI_ENABLE} )
ELSE (MAGICKCORE_HDRI_ENABLE)
	add_definitions( -DMAGICKCORE_HDRI_ENABLE=0 )
ENDIF (MAGICKCORE_HDRI_ENABLE)
IF (OPENSHOT_IMAGEMAGICK_COMPATIBILITY)
	add_definitions( -DOPENSHOT_IMAGEMAGICK_COMPATIBILITY=${OPENSHOT_IMAGEMAGICK_COMPATIBILITY} )
ELSE (OPENSHOT_IMAGEMAGICK_COMPATIBILITY)
	add_definitions( -DOPENSHOT_IMAGEMAGICK_COMPATIBILITY=0 )
ENDIF (OPENSHOT_IMAGEMAGICK_COMPATIBILITY)

# Find the ImageMagick++ library
FIND_PACKAGE(ImageMagick COMPONENTS Magick++ MagickWand MagickCore)
IF (ImageMagick_FOUND)
	# Include ImageMagick++ headers (needed for compile)
	include_directories(${ImageMagick_INCLUDE_DIRS})

	# define a global var (used in the C++)
	add_definitions( -DUSE_IMAGEMAGICK=1 )
	SET(CMAKE_SWIG_FLAGS "-DUSE_IMAGEMAGICK=1")

ENDIF (ImageMagick_FOUND)

################# LIBOPENSHOT-AUDIO ###################
# Find JUCE-based openshot Audio libraries
FIND_PACKAGE(OpenShotAudio 0.1.9 REQUIRED)

# Include Juce headers (needed for compile)
include_directories(${LIBOPENSHOT_AUDIO_INCLUDE_DIRS})

################# BLACKMAGIC DECKLINK ###################
# Find BlackMagic DeckLinkAPI libraries
IF (ENABLE_BLACKMAGIC)
	FIND_PACKAGE(BlackMagic)

	IF (BLACKMAGIC_FOUND)
		# Include Blackmagic headers (needed for compile)
		include_directories(${BLACKMAGIC_INCLUDE_DIR})

		# define a global var (used in the C++)
		add_definitions( -DUSE_BLACKMAGIC=1 )
		SET(CMAKE_SWIG_FLAGS "-DUSE_BLACKMAGIC=1")

	ENDIF (BLACKMAGIC_FOUND)
ENDIF (ENABLE_BLACKMAGIC)

###############  PROFILING  #################
#set(PROFILER "/usr/lib/libprofiler.so.0.3.2")
#set(PROFILER "/usr/lib/libtcmalloc.so.4")

if(CMAKE_VERSION VERSION_LESS 3.3)
  # IWYU wasn't supported internally in 3.2
  set(ENABLE_IWYU FALSE)
endif()

if(ENABLE_IWYU)
	find_program(IWYU_PATH NAMES "iwyu"
		DOC "include-what-you-use source code scanner executable")
	if(IWYU_PATH)
		if(IWYU_OPTS)
			separate_arguments(IWYU_OPTS)
			list(APPEND _iwyu_opts "-Xiwyu" ${IWYU_OPTS})
		endif()
		set(CMAKE_CXX_INCLUDE_WHAT_YOU_USE ${IWYU_PATH} ${_iwyu_opts})
	else()
		set(ENABLE_IWYU FALSE)
	endif()
endif()
add_feature_info("IWYU (include-what-you-use)" ENABLE_IWYU "Scan all source files with 'iwyu'")

# Main library sources
set(OPENSHOT_SOURCES
  AudioBufferSource.cpp
  AudioReaderSource.cpp
  AudioResampler.cpp
  CacheBase.cpp
  CacheDisk.cpp
  CacheMemory.cpp
  ChunkReader.cpp
  ChunkWriter.cpp
  Color.cpp
  Clip.cpp
  ClipBase.cpp
  Coordinate.cpp
  CrashHandler.cpp
  DummyReader.cpp
  ReaderBase.cpp
  RendererBase.cpp
  WriterBase.cpp
  EffectBase.cpp
  EffectInfo.cpp
  FFmpegReader.cpp
  FFmpegWriter.cpp
  Fraction.cpp
  Frame.cpp
  FrameMapper.cpp
  KeyFrame.cpp
  OpenShotVersion.cpp
  ZmqLogger.cpp
  PlayerBase.cpp
  Point.cpp
  Profiles.cpp
  QtHtmlReader.cpp
  QtImageReader.cpp
  QtPlayer.cpp
  QtTextReader.cpp
  Settings.cpp
  Timeline.cpp)

# Video effects
set(EFFECTS_SOURCES
  effects/Bars.cpp
  effects/Blur.cpp
  effects/Brightness.cpp
  effects/ChromaKey.cpp
  effects/ColorShift.cpp
  effects/Crop.cpp
  effects/Deinterlace.cpp
  effects/Hue.cpp
  effects/Mask.cpp
  effects/Negate.cpp
  effects/Pixelate.cpp
  effects/Saturation.cpp
  effects/Shift.cpp
  effects/Wave.cpp)

# Qt video player components
set(QT_PLAYER_SOURCES
  Qt/AudioPlaybackThread.cpp
  Qt/PlayerDemo.cpp
  Qt/PlayerPrivate.cpp
  Qt/VideoCacheThread.cpp
  Qt/VideoPlaybackThread.cpp
  Qt/VideoRenderer.cpp
  Qt/VideoRenderWidget.cpp)


# Get list of headers
file(GLOB_RECURSE headers ${CMAKE_SOURCE_DIR}/include/*.h)

# Disable RPATH
SET(CMAKE_MACOSX_RPATH 0)

############### CREATE LIBRARY #################
# Create shared openshot library
add_library(openshot SHARED)

target_sources(openshot
  PRIVATE
    ${OPENSHOT_SOURCES} ${EFFECTS_SOURCES} ${QT_PLAYER_SOURCES}
  PUBLIC
    ${headers})

# Set SONAME and other library properties
set_target_properties(openshot
		PROPERTIES
		VERSION ${PROJECT_VERSION}
		SOVERSION ${PROJECT_SO_VERSION}
		INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
		)

# Add optional ImageMagic-dependent sources
if(ImageMagick_FOUND)
	target_sources(openshot PRIVATE
    ImageReader.cpp
    ImageWriter.cpp
    TextReader.cpp)
endif()

# BlackMagic related files
if(BLACKMAGIC_FOUND)
  target_sources(openshot PRIVATE
    DecklinkInput.cpp
    DecklinkReader.cpp
    DecklinkOutput.cpp
    DecklinkWriter.cpp)
endif()

# Location of our includes, both internally and when installed
target_include_directories(openshot
  PRIVATE
    ${CMAKE_SOURCE_DIR}/include
    ${CMAKE_BINARY_DIR}/include
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
    $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/libopenshot>)


################### JSONCPP #####################
# Include jsoncpp headers (needed for JSON parsing)
if (USE_SYSTEM_JSONCPP)
	message(STATUS "Looking for system JsonCpp")
	find_package(JsonCpp)
	if (JSONCPP_FOUND AND NOT TARGET jsoncpp_lib)
		# Create the expected target, for older installs that don't
		add_library(jsoncpp_lib INTERFACE)
		target_include_directories(jsoncpp_lib INTERFACE
			${JSONCPP_INCLUDE_DIRS})
		target_link_libraries(jsoncpp_lib INTERFACE ${JSONCPP_LIBRARY})
	endif ()
endif ()

if (NOT JSONCPP_FOUND AND NOT DISABLE_BUNDLED_JSONCPP)
  message(STATUS "Using embedded JsonCpp (not found or USE_SYSTEM_JSONCPP disabled)")
  if (NOT TARGET jsoncpp_lib)
    add_library(jsoncpp_lib INTERFACE)
    target_include_directories(jsoncpp_lib INTERFACE
      "${PROJECT_SOURCE_DIR}/thirdparty/jsoncpp")
    target_sources(jsoncpp_lib INTERFACE "${PROJECT_SOURCE_DIR}/thirdparty/jsoncpp/jsoncpp.cpp")
    # Because this satisfies the requirement, an installed JsonCpp is optional
    set_package_properties(JsonCpp PROPERTIES TYPE OPTIONAL)
  endif ()
  add_feature_info("JsonCpp (embedded)" TRUE "JsonCpp will be compiled from the bundled sources")
endif ()

if (JSONCPP_FOUND)
  # JsonCpp is actually required, even though we probe for it optionally
  # (This tells feature_summary() to bail if it's not found, later)
  set_package_properties(JsonCpp PROPERTIES TYPE REQUIRED)
endif ()

# If we found any usable JsonCpp, use it. Otherwise, bail.
if (TARGET jsoncpp_lib)
  target_link_libraries(openshot PUBLIC jsoncpp_lib)
endif ()

################# QT5 ###################
# Find QT5 libraries
set(_qt_components Widgets Core Gui Multimedia MultimediaWidgets)
find_package(Qt5 COMPONENTS ${_qt_components} REQUIRED)

foreach(_qt_comp IN LISTS _qt_components)
  if(TARGET Qt5::${_qt_comp})
    target_link_libraries(openshot PUBLIC Qt5::${_qt_comp})
  endif()
endforeach()

################### FFMPEG #####################
# Find FFmpeg libraries (used for video encoding / decoding)
FIND_PACKAGE(FFmpeg REQUIRED COMPONENTS avcodec avdevice avformat avutil swscale)

foreach(ff_comp avcodec avdevice avformat avfilter avutil postproc swscale swresample avresample)
  if(TARGET FFmpeg::${ff_comp})
		target_link_libraries(openshot PUBLIC FFmpeg::${ff_comp})
  endif()
endforeach()

################### Threads ####################
# Threading library -- uses IMPORTED target Threads::Threads (since CMake 3.1)
set(CMAKE_THREAD_PREFER_PTHREAD TRUE)
set(THREADS_PREFER_PTHREAD_FLAG TRUE)
find_package(Threads REQUIRED)
target_link_libraries(openshot PUBLIC Threads::Threads)

################### OPENMP #####################
# Check for OpenMP (used for multi-core processing)

# OpenMP is required by FFmpegReader/Writer
find_package(OpenMP REQUIRED)

if(NOT TARGET OpenMP::OpenMP_CXX)
    # Older CMake versions (< 3.9) don't create find targets.
    add_library(OpenMP_TARGET INTERFACE)
    add_library(OpenMP::OpenMP_CXX ALIAS OpenMP_TARGET)
    target_compile_options(OpenMP_TARGET INTERFACE ${OpenMP_CXX_FLAGS})
    target_link_libraries(OpenMP_TARGET INTERFACE Threads::Threads)
    target_link_libraries(OpenMP_TARGET INTERFACE ${OpenMP_CXX_FLAGS})
endif()

target_link_libraries(openshot PUBLIC OpenMP::OpenMP_CXX)

################### ZEROMQ #####################
# Find ZeroMQ library (used for socket communication & logging)
find_package(ZeroMQ REQUIRED) # Creates libzmq target

# Some platforms package the header-only cppzmq C++ bindings separately,
# others (Ubuntu) bundle them in with libzmq itself
find_package(cppzmq QUIET) # Creates cppzmq target

# Link ZeroMQ library
if (TARGET libzmq)
	target_link_libraries(openshot PUBLIC libzmq)
endif()
# Include cppzmq headers, if not bundled into libzmq
if (TARGET cppzmq)
  target_link_libraries(openshot PUBLIC cppzmq)
endif()

################### RESVG #####################
# Migrate some legacy variable names
if(DEFINED RESVGDIR AND NOT DEFINED RESVG_ROOT)
  set(RESVG_ROOT ${RESVGDIR})
endif()
if(DEFINED ENV{RESVGDIR} AND NOT DEFINED RESVG_ROOT)
  set(RESVG_ROOT $ENV{RESVGDIR})
endif()

# Find resvg library (used for rendering svg files)
FIND_PACKAGE(RESVG)

# Include resvg headers (optional SVG library)
if (TARGET RESVG::resvg)
  #include_directories(${RESVG_INCLUDE_DIRS})
  target_link_libraries(openshot PUBLIC RESVG::resvg)

  target_compile_definitions(openshot PUBLIC "-DUSE_RESVG=1")
  set(CMAKE_SWIG_FLAGS "-DUSE_RESVG=1")
endif()

###############  LINK LIBRARY  #################
# Link remaining dependency libraries
target_link_libraries(openshot PUBLIC
	${LIBOPENSHOT_AUDIO_LIBRARIES}
  ${PROFILER})

if(ImageMagick_FOUND)
  target_link_libraries(openshot PUBLIC ${ImageMagick_LIBRARIES})
endif()

if(BLACKMAGIC_FOUND)
  target_link_libraries(openshot PUBLIC ${BLACKMAGIC_LIBRARY_DIR})
endif()

if(WIN32)
	# Required for exception handling on Windows
	target_link_libraries(openshot PUBLIC "imagehlp" "dbghelp" )
endif()


############### CLI EXECUTABLES ################
# Create test executable
add_executable(openshot-example examples/Example.cpp)

# Define path to test input files
SET(TEST_MEDIA_PATH "${PROJECT_SOURCE_DIR}/src/examples/")
IF (WIN32)
        STRING(REPLACE "/" "\\\\" TEST_MEDIA_PATH TEST_MEDIA_PATH)
ENDIF(WIN32)
target_compile_definitions(openshot-example PRIVATE
	-DTEST_MEDIA_PATH="${TEST_MEDIA_PATH}" )

# Link test executable to the new library
target_link_libraries(openshot-example openshot)

add_executable(openshot-html-test examples/ExampleHtml.cpp)
target_link_libraries(openshot-html-test openshot Qt5::Gui)

############### PLAYER EXECUTABLE ################
# Create test executable
add_executable(openshot-player Qt/demo/main.cpp)

# Link test executable to the new library
target_link_libraries(openshot-player openshot)

############### TEST BLACKMAGIC CAPTURE APP ################
IF (BLACKMAGIC_FOUND)
	# Create test executable
	add_executable(openshot-blackmagic
			examples/ExampleBlackmagic.cpp)

	# Link test executable to the new library
	target_link_libraries(openshot-blackmagic openshot)
ENDIF (BLACKMAGIC_FOUND)

############### INCLUDE SWIG BINDINGS ################
add_subdirectory(bindings)

############### INSTALL HEADERS & LIBRARY ################
set(LIB_INSTALL_DIR lib${LIB_SUFFIX}) # determine correct lib folder

# Install primary library
INSTALL(TARGETS openshot
		ARCHIVE DESTINATION ${LIB_INSTALL_DIR}
		LIBRARY DESTINATION ${LIB_INSTALL_DIR}
		RUNTIME DESTINATION ${LIB_INSTALL_DIR}
		COMPONENT library )

INSTALL(DIRECTORY ${CMAKE_SOURCE_DIR}/include/
		DESTINATION ${CMAKE_INSTALL_PREFIX}/include/libopenshot
		FILES_MATCHING PATTERN "*.h")

############### CPACK PACKAGING ##############
IF(MINGW)
	SET(CPACK_GENERATOR "NSIS")
ENDIF(MINGW)
IF(UNIX AND NOT APPLE)
	SET(CPACK_GENERATOR "DEB")
ENDIF(UNIX AND NOT APPLE)
#IF(UNIX AND APPLE)
#	SET(CPACK_GENERATOR "DragNDrop")
#ENDIF(UNIX AND APPLE)
SET(CPACK_DEBIAN_PACKAGE_MAINTAINER "Jonathan Thomas") #required

INCLUDE(CPack)
####################### CMakeLists.txt (libopenshot) #########################
# @brief CMake build file for libopenshot (used to generate makefiles)
# @author Jonathan Thomas <jonathan@openshot.org>
#
# @section LICENSE
#
# Copyright (c) 2008-2019 OpenShot Studios, LLC
# <http://www.openshotstudios.com/>. This file is part of
# OpenShot Library (libopenshot), an open-source project dedicated to 
# delivering high quality video editing and animation solutions to the 
# world. For more information visit <http://www.openshot.org/>.
#
# OpenShot Library (libopenshot) is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenShot Library (libopenshot) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenShot Library. If not, see <http://www.gnu.org/licenses/>.
################################################################################

IF(NOT DEFINED ENABLE_PYTHON)
    SET(ENABLE_PYTHON 1)
ENDIF()

IF(NOT DEFINED ENABLE_RUBY)
    SET(ENABLE_RUBY 1)
ENDIF()

############### INCLUDE EACH LANGUAGE BINDING ################
IF (ENABLE_PYTHON)
    add_subdirectory(python)
ENDIF (ENABLE_PYTHON)

IF (ENABLE_RUBY)
    add_subdirectory(ruby)
ENDIF (ENABLE_RUBY)

####################### CMakeLists.txt (libopenshot) #########################
# @brief CMake build file for libopenshot (used to generate Python SWIG bindings)
# @author Jonathan Thomas <jonathan@openshot.org>
#
# @section LICENSE
#
# Copyright (c) 2008-2019 OpenShot Studios, LLC
# <http://www.openshotstudios.com/>. This file is part of
# OpenShot Library (libopenshot), an open-source project dedicated to
# delivering high quality video editing and animation solutions to the
# world. For more information visit <http://www.openshot.org/>.
#
# OpenShot Library (libopenshot) is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenShot Library (libopenshot) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenShot Library. If not, see <http://www.gnu.org/licenses/>.
################################################################################


############### SWIG PYTHON BINDINGS ################
FIND_PACKAGE(SWIG 3.0 REQUIRED)
INCLUDE(${SWIG_USE_FILE})

### Enable some legacy SWIG behaviors, in newer CMAKEs
if (POLICY CMP0078)
	cmake_policy(SET CMP0078 OLD)
endif()
if (POLICY CMP0086)
	cmake_policy(SET CMP0086 OLD)
endif()

FIND_PACKAGE(PythonInterp 3)
FIND_PACKAGE(PythonLibs 3)
if (PYTHONLIBS_FOUND AND PYTHONINTERP_FOUND)

	### Include Python header files
	INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
	INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})

	### Enable C++ support in SWIG
	set_property(SOURCE openshot.i PROPERTY CPLUSPLUS ON)
	set_property(SOURCE openshot.i PROPERTY SWIG_MODULE_NAME openshot)

	### Suppress a ton of warnings in the generated SWIG C++ code
	set(SWIG_CXX_FLAGS "-Wno-unused-variable -Wno-unused-function -Wno-deprecated-copy -Wno-class-memaccess -Wno-cast-function-type \
-Wno-unused-parameter -Wno-catch-value -Wno-sign-compare -Wno-ignored-qualifiers")
	separate_arguments(sw_flags UNIX_COMMAND ${SWIG_CXX_FLAGS})
	set_property(SOURCE openshot.i PROPERTY GENERATED_COMPILE_OPTIONS ${sw_flags})

  ### Take include dirs from target, automatically if possible
  if (CMAKE_VERSION VERSION_GREATER 3.13)
    set_property(SOURCE openshot.i PROPERTY USE_TARGET_INCLUDE_DIRECTORIES True)
  else ()
    set_property(SOURCE openshot.i PROPERTY INCLUDE_DIRECTORIES $<TARGET_PROPERTY:openshot,INCLUDE_DIRECTORIES>)
  endif ()

	### Add the SWIG interface file (which defines all the SWIG methods)
	if (CMAKE_VERSION VERSION_LESS 3.8.0)
		swig_add_module(pyopenshot python openshot.i)
	else()
		swig_add_library(pyopenshot LANGUAGE python SOURCES openshot.i)
	endif()

	### Set output name of target
	set_target_properties(${SWIG_MODULE_pyopenshot_REAL_NAME} PROPERTIES
	                      PREFIX "_" OUTPUT_NAME "openshot")

	### Link the new python wrapper library with libopenshot
	target_link_libraries(${SWIG_MODULE_pyopenshot_REAL_NAME}
                        PUBLIC ${PYTHON_LIBRARIES} openshot)

	### Check if the following Debian-friendly python module path exists
	SET(PYTHON_MODULE_PATH "${CMAKE_INSTALL_PREFIX}/lib/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/dist-packages")
	if (NOT EXISTS ${PYTHON_MODULE_PATH})

		### Calculate the python module path (using distutils)
		execute_process ( COMMAND ${PYTHON_EXECUTABLE} -c "\
from distutils.sysconfig import get_python_lib; \
print( get_python_lib( plat_specific=True, prefix='${CMAKE_INSTALL_PREFIX}' ) )"
			OUTPUT_VARIABLE _ABS_PYTHON_MODULE_PATH
			OUTPUT_STRIP_TRAILING_WHITESPACE )

		GET_FILENAME_COMPONENT(_ABS_PYTHON_MODULE_PATH
				"${_ABS_PYTHON_MODULE_PATH}" ABSOLUTE)
		FILE(RELATIVE_PATH _REL_PYTHON_MODULE_PATH
				${CMAKE_INSTALL_PREFIX} ${_ABS_PYTHON_MODULE_PATH})
		SET(PYTHON_MODULE_PATH ${_ABS_PYTHON_MODULE_PATH})
	endif()
	message("PYTHON_MODULE_PATH: ${PYTHON_MODULE_PATH}")

	############### INSTALL HEADERS & LIBRARY ################
	### Install Python bindings
	INSTALL(TARGETS ${SWIG_MODULE_pyopenshot_REAL_NAME}
	        LIBRARY DESTINATION ${PYTHON_MODULE_PATH} )
	INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/openshot.py
	        DESTINATION ${PYTHON_MODULE_PATH} )

endif ()
####################### CMakeLists.txt (libopenshot) #########################
# @brief CMake build file for libopenshot (used to generate Ruby SWIG bindings)
# @author Jonathan Thomas <jonathan@openshot.org>
#
# @section LICENSE
#
# Copyright (c) 2008-2019 OpenShot Studios, LLC
# <http://www.openshotstudios.com/>. This file is part of
# OpenShot Library (libopenshot), an open-source project dedicated to
# delivering high quality video editing and animation solutions to the
# world. For more information visit <http://www.openshot.org/>.
#
# OpenShot Library (libopenshot) is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenShot Library (libopenshot) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenShot Library. If not, see <http://www.gnu.org/licenses/>.
################################################################################

############### RUBY BINDINGS ################
FIND_PACKAGE(SWIG 3.0 REQUIRED)
INCLUDE(${SWIG_USE_FILE})

### Enable some legacy SWIG behaviors, in newer CMAKEs
if (POLICY CMP0078)
	cmake_policy(SET CMP0078 OLD)
endif()
if (POLICY CMP0086)
	cmake_policy(SET CMP0086 OLD)
endif()

FIND_PACKAGE(Ruby)
IF (RUBY_FOUND)

	### Include the Ruby header files
	INCLUDE_DIRECTORIES(${RUBY_INCLUDE_DIRS})
	INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})

	### Enable C++ in SWIG
	set_property(SOURCE openshot.i PROPERTY CPLUSPLUS ON)
	set_property(SOURCE openshot.i PROPERTY SWIG_MODULE_NAME openshot)

	### Suppress a ton of warnings in the generated SWIG C++ code
	set(SWIG_CXX_FLAGS "-Wno-unused-variable -Wno-unused-function -Wno-deprecated-copy -Wno-class-memaccess -Wno-cast-function-type \
-Wno-unused-parameter -Wno-catch-value -Wno-sign-compare -Wno-ignored-qualifiers")
	separate_arguments(sw_flags UNIX_COMMAND ${SWIG_CXX_FLAGS})
	set_property(SOURCE openshot.i PROPERTY GENERATED_COMPILE_OPTIONS ${sw_flags})

	### Take include dirs from target, automatically if possible
	if (CMAKE_VERSION VERSION_GREATER 3.13)
		set_property(SOURCE openshot.i PROPERTY USE_TARGET_INCLUDE_DIRECTORIES True)
	else ()
		set_property(SOURCE openshot.i PROPERTY INCLUDE_DIRECTORIES $<TARGET_PROPERTY:openshot,INCLUDE_DIRECTORIES>)
	endif ()

	### Add the SWIG interface file (which defines all the SWIG methods)
	if (CMAKE_VERSION VERSION_LESS 3.8.0)
		swig_add_module(rbopenshot ruby openshot.i)
	else()
		swig_add_library(rbopenshot LANGUAGE ruby SOURCES openshot.i)
	endif()

	### Set name of target (with no prefix, since Ruby does not like that)
	SET_TARGET_PROPERTIES(${SWIG_MODULE_rbopenshot_REAL_NAME} PROPERTIES
	                      PREFIX "" OUTPUT_NAME "openshot")

	### Link the new Ruby wrapper library with libopenshot
	target_link_libraries(${SWIG_MODULE_rbopenshot_REAL_NAME}
	                      ${RUBY_LIBRARY} openshot)

	### FIND THE RUBY INTERPRETER (AND THE LOAD_PATH FOLDER)
	EXECUTE_PROCESS(COMMAND ${RUBY_EXECUTABLE}
	                -r rbconfig -e "print RbConfig::CONFIG['vendorarchdir']"
	                OUTPUT_VARIABLE RUBY_VENDOR_ARCH_DIR)
	MESSAGE(STATUS "Ruby executable: ${RUBY_EXECUTABLE}")
	MESSAGE(STATUS "Ruby vendor arch dir: ${RUBY_VENDOR_ARCH_DIR}")
	MESSAGE(STATUS "Ruby include path: ${RUBY_INCLUDE_PATH}")

	############### INSTALL HEADERS & LIBRARY ################
	# Install Ruby bindings
	install(TARGETS ${SWIG_MODULE_rbopenshot_REAL_NAME}
	        LIBRARY DESTINATION ${RUBY_VENDOR_ARCH_DIR} )

ENDIF (RUBY_FOUND)
##################### tests/CMakeLists.txt (libopenshot) ######################
# @brief CMake build file for libopenshot (used to generate makefiles)
# @author Jonathan Thomas <jonathan@openshot.org>
#
# @section LICENSE
#
# Copyright (c) 2008-2019 OpenShot Studios, LLC
# <http://www.openshotstudios.com/>. This file is part of
# OpenShot Library (libopenshot), an open-source project dedicated to
# delivering high quality video editing and animation solutions to the
# world. For more information visit <http://www.openshot.org/>.
#
# OpenShot Library (libopenshot) is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenShot Library (libopenshot) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenShot Library. If not, see <http://www.gnu.org/licenses/>.
################################################################################

SET(TEST_MEDIA_PATH "${PROJECT_SOURCE_DIR}/src/examples/")

################ WINDOWS ##################
# Set some compiler options for Windows
# required for libopenshot-audio headers
IF (WIN32)
	STRING(REPLACE "/" "\\\\" TEST_MEDIA_PATH TEST_MEDIA_PATH)
	add_definitions( -DIGNORE_JUCE_HYPOT=1 )
	SET(CMAKE_CXX_FLAGS " ${CMAKE_CXX_FLAGS} -include cmath")
ENDIF(WIN32)

add_definitions( -DTEST_MEDIA_PATH="${TEST_MEDIA_PATH}" )

################### UNITTEST++ #####################
# Find UnitTest++ libraries (used for unit testing)
FIND_PACKAGE(UnitTest++ REQUIRED)

# Include UnitTest++ headers (needed for compile)
include_directories(${UNITTEST++_INCLUDE_DIR})

################ IMAGE MAGICK ##################
# Set the Quantum Depth that ImageMagick was built with (default to 16 bits)
IF (MAGICKCORE_QUANTUM_DEPTH)
	add_definitions( -DMAGICKCORE_QUANTUM_DEPTH=${MAGICKCORE_QUANTUM_DEPTH} )
ELSE (MAGICKCORE_QUANTUM_DEPTH)
	add_definitions( -DMAGICKCORE_QUANTUM_DEPTH=16 )
ENDIF (MAGICKCORE_QUANTUM_DEPTH)
IF (MAGICKCORE_HDRI_ENABLE)
	add_definitions( -DMAGICKCORE_HDRI_ENABLE=${MAGICKCORE_HDRI_ENABLE} )
ELSE (MAGICKCORE_HDRI_ENABLE)
	add_definitions( -DMAGICKCORE_HDRI_ENABLE=0 )
ENDIF (MAGICKCORE_HDRI_ENABLE)
IF (OPENSHOT_IMAGEMAGICK_COMPATIBILITY)
	add_definitions( -DOPENSHOT_IMAGEMAGICK_COMPATIBILITY=${OPENSHOT_IMAGEMAGICK_COMPATIBILITY} )
ELSE (OPENSHOT_IMAGEMAGICK_COMPATIBILITY)
	add_definitions( -DOPENSHOT_IMAGEMAGICK_COMPATIBILITY=0 )
ENDIF (OPENSHOT_IMAGEMAGICK_COMPATIBILITY)

# Find the ImageMagick++ library
FIND_PACKAGE(ImageMagick COMPONENTS Magick++ MagickWand MagickCore)
IF (ImageMagick_FOUND)
	# Include ImageMagick++ headers (needed for compile)
	include_directories(${ImageMagick_INCLUDE_DIRS})

	# define a global var (used in the C++)
	add_definitions( -DUSE_IMAGEMAGICK=1 )
	SET(CMAKE_SWIG_FLAGS "-DUSE_IMAGEMAGICK=1")

ENDIF (ImageMagick_FOUND)

################# LIBOPENSHOT-AUDIO ###################
# Find JUCE-based openshot Audio libraries
FIND_PACKAGE(OpenShotAudio 0.1.9 REQUIRED)

# Include Juce headers (needed for compile)
include_directories(${LIBOPENSHOT_AUDIO_INCLUDE_DIRS})


################# BLACKMAGIC DECKLINK ###################
IF (ENABLE_BLACKMAGIC)
	# Find BlackMagic DeckLinkAPI libraries
	FIND_PACKAGE(BlackMagic)

	IF (BLACKMAGIC_FOUND)
		# Include Blackmagic headers (needed for compile)
		include_directories(${BLACKMAGIC_INCLUDE_DIR})
	ENDIF (BLACKMAGIC_FOUND)
ENDIF (ENABLE_BLACKMAGIC)


###############  SET TEST SOURCE FILES  #################
SET ( OPENSHOT_TEST_FILES
	   Cache_Tests.cpp
	   Clip_Tests.cpp
	   Color_Tests.cpp
	   Coordinate_Tests.cpp
	   ReaderBase_Tests.cpp
	   ImageWriter_Tests.cpp
	   FFmpegReader_Tests.cpp
	   FFmpegWriter_Tests.cpp
	   Fraction_Tests.cpp
     Frame_Tests.cpp
	   FrameMapper_Tests.cpp
	   KeyFrame_Tests.cpp
	   Point_Tests.cpp
	   Settings_Tests.cpp
	   Timeline_Tests.cpp )

################ TESTER EXECUTABLE #################
# Create unit test executable (openshot-test)
message (STATUS "Tests enabled, test executable will be built as tests/openshot-test")
add_executable(openshot-test
			   tests.cpp
			   ${OPENSHOT_TEST_FILES} )

# Link libraries to the new executable
target_link_libraries(openshot-test openshot ${UNITTEST++_LIBRARY})

##### RUNNING TESTS (make os_test / make test) #####
# Hook up the 'make os_test' target to the 'openshot-test' executable
ADD_CUSTOM_TARGET(os_test COMMAND openshot-test)
list(APPEND OS_TEST_CMDS "'make os_test'")

# Also hook up 'make test', if possible
# This requires CMake 3.11+, where the CMP0037 policy
# configured to 'NEW' mode will not reserve target names
# unless the corresponding feature is actually used
if (POLICY CMP0037)
	cmake_policy(SET CMP0037 NEW)
endif()
if (CMAKE_VERSION VERSION_GREATER 3.11)
	message(STATUS "Cmake 3.11+ detected, enabling 'test' target")
	add_custom_target(test COMMAND openshot-test)
	list(APPEND OS_TEST_CMDS " or " "'make test'")
endif()

string(CONCAT t ${OS_TEST_CMDS})
message("\nTo run unit tests, use: ${t}")
The JsonCpp library's source code, including accompanying documentation, 
tests and demonstration applications, are licensed under the following
conditions...

Baptiste Lepilleur and The JsonCpp Authors explicitly disclaim copyright in all 
jurisdictions which recognize such a disclaimer. In such jurisdictions, 
this software is released into the Public Domain.

In jurisdictions which do not recognize Public Domain property (e.g. Germany as of
2010), this software is Copyright (c) 2007-2010 by Baptiste Lepilleur and
The JsonCpp Authors, and is released under the terms of the MIT License (see below).

In jurisdictions which recognize Public Domain property, the user of this 
software may choose to accept it either as 1) Public Domain, 2) under the 
conditions of the MIT License (see below), or 3) under the terms of dual 
Public Domain/MIT License conditions described here, as they choose.

The MIT License is about as close to Public Domain as a license can get, and is
described in clear, concise terms at:

   http://en.wikipedia.org/wiki/MIT_License
   
The full text of the MIT License follows:

========================================================================
Copyright (c) 2007-2010 Baptiste Lepilleur and The JsonCpp Authors

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
========================================================================
(END LICENSE TEXT)

The MIT license is compatible with both the GPL and commercial
software, affording one all of the rights of Public Domain with the
minor nuisance of being required to keep the above copyright notice
and license text in the source code. Note also that by accepting the
Public Domain "license" you can re-license your copy using whatever
license you like.
