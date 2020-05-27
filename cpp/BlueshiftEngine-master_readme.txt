Build Sample Program
--------------------

## Prerequisite

* [How to Build Engine Runtime Libraries](https://github.com/PolygonTek/BlueshiftEngine/wiki/How-to-Build-Engine-Runtime-Libraries)

## Game Build Test

Download the file [BlueshiftExamples-master.zip](https://github.com/PolygonTek/BlueshiftExamples/archive/master.zip),
extract `Simple` to the `~/Documents/Simple` folder

Run `BlueshiftEditor` (`BlueshiftEngine/Engine/Bin/Win64/Release/BlueshiftEditor.exe`),
select the `~/Documents/Simple` folder from the `File/Open Project` menu
and select the `~/Documents/Simple/Contents/Maps/main.map` from the `File/Open Map` menu.


Select the platform from the `Project/Build Settings...` menu,
set build folder  to `~/Documents/Simple1And` (`SimpleIOS, SimpleWin, ...`).

When the build is complete, the project folder opens automatically within the build folder `~/Documents/SimpleAnd`.

## See also

* [Building iOS Sample Program](https://github.com/PolygonTek/BlueshiftDocument/blob/master/Build%20iOS.pdf)


Version History
---------------

### 0.6.0
- Refined PBR shaders
- Added support for environment probes for indirect lighting
- Added support for various HDR tonemapping operators
- Added support for integration [Google Analytics](https://analytics.google.com/) into the player
- Added support for integration three ad formats of [Google AdMob](https://www.google.com/admob/) into the player
- Added support for Unicode (UTF-8) almost everywhere
- Updated Bullet physics library to 2.88
- Fixed an issue where sRGB rendering on Android was incorrect
- Improved speed of project loading in editor

### 0.5.0
- Added support for GPU instancing for static/skinned meshes
- Added support for static batching
- Added support for calculation tangent vectors using MikkTSpace
- Added support for calculation normals with area and anglular weights
- Added support for vehicle physics
- Added support for slider/wheel joint components
- Added support for copy & paste component values in editor
- Changed engine unit from centi-meters to meters
- Changed FBX importing process to support hierarchical mesh in editor
- Fixed an issue where rolling friction was not working correctly
- Fixed an issue where inspector updating in play mode would slow down the game 

### 0.4.0
- Added support for LuaJIT (Windows / macOS)
- Added support for debugging Lua script in [ZeroBrane Studio](https://studio.zerobrane.com/)
- Reimplemented Android build from scratch
- Added support for Google reward based video ad (Android)
- Various minor improvements and bug fixes

### 0.3.0
- Improved property system
- Added support for editing multiple selected entities simultaneously
- Added support for undo/redo in play mode
- Added support for Google reward based video ad (iOS)
- Added component icons in editor for each component widgets
- New dock widgets
- Fixed a potential crash when using undo/redo

### 0.2.2
- Fixed crashes for Android player
- Various minor bug fixes

### 0.2.0
- Added support for physically based lighting
- Added support for particle system
- Improved material editor
- Added support for six sided skybox rendering
- Added support for conversion between equirectangular spherical image and cube image
- Various minor improvements and bug fixes

### 0.1.3
- Fixed bug to deploy target iOS/macOS

### 0.1.0
- First release################################################################################
# Top-level CMakeLists.txt file for Blueshift Engine
################################################################################
cmake_minimum_required(VERSION 3.1)

if (COMMAND cmake_policy)
    if (POLICY CMP0025)
        # Compiler id for Apple Clang is now AppleClang.
        cmake_policy(SET CMP0025 NEW)
    endif ()
endif ()

set(CMAKE_OBJECT_PATH_MAX 512)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/CMake)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(CMakeDependentOption)
include(BlueshiftCommon)

option(BUILD_RUNTIME "Build Blueshift Runtime libraies" OFF)
option(BUILD_PLAYER "Build Blueshift Player executable" OFF)
option(BUILD_EDITOR "Build Blueshift Editor executable" OFF)
option(BUILD_TEST "Build test projects" OFF)

if (BUILD_RUNTIME)
    set(ROOT_PROJECT_NAME Blueshift)

    set(ENGINE_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Source CACHE STRING "engine include directory")
    set(ENGINE_LIBRARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Library CACHE STRING "engine library directory")
elseif (BUILD_PLAYER)
    set(ROOT_PROJECT_NAME BlueshiftPlayer)
else ()
    message(FATAL_ERROR "Neither BUILD_RUNTIME nor BUILD_PLAYER are set")
endif ()

project(${ROOT_PROJECT_NAME})

cmake_dependent_option(USE_LUAJIT "Use LuaJIT" ON "NOT IOS AND NOT ANDROID" OFF)

# Check platform
if (ANDROID)
    set(PLATFORM_ANDROID TRUE)
elseif (WIN32)
    set(PLATFORM_WINDOWS TRUE)
elseif (APPLE AND IOS)
    set(PLATFORM_IOS TRUE)
elseif (APPLE AND ${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(PLATFORM_MACOS TRUE)
elseif (UNIX)
    set(PLATFORM_LINUX TRUE)
endif ()

if (CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(ENGINE_64BIT TRUE)
endif ()

if (CMAKE_CROSSCOMPILING)
    if (IOS)
        set(ENGINE_ARCH ${IOS_ARCH})
    elseif (ANDROID)
        set(ENGINE_ARCH ${CMAKE_ANDROID_ARCH})

        include_directories(${ANDROID_SYSROOT}/usr/include/${ANDROID_HEADER_TRIPLE})
    endif ()
else ()
    if (ENGINE_64BIT)
        set(ENGINE_ARCH x86_64)
    else ()
        set(ENGINE_ARCH i386)
    endif ()
endif ()

set(VERSION_MAJOR 0 CACHE INTERNAL "Project major version number.")
set(VERSION_MINOR 6 CACHE INTERNAL "Project minor version number.")
set(VERSION_PATCH 0 CACHE INTERNAL "Project patch version number.")

string(TIMESTAMP NOW "%Y-%m-%d %H:%M:%S")
set(VERSION_DATE ${NOW} CACHE INTERNAL "Project version date")

# Advanced variables will not be displayed in any of the cmake GUIs unless the show advanced option is on.
mark_as_advanced(VERSION_MAJOR VERSION_MINOR VERSION_PATCH VERSION_DATE)

message(STATUS "Running from ${CMAKE_CURRENT_SOURCE_DIR}")

message(STATUS "Version: ${CMAKE_VERSION}")
message(STATUS "Generator: ${CMAKE_GENERATOR}")
message(STATUS "System: ${CMAKE_SYSTEM_NAME} ${CMAKE_SYSTEM_VERSION} ${CMAKE_SYSTEM_PROCESSOR}") 
message(STATUS "C Compiler: ${CMAKE_C_COMPILER}")
message(STATUS "CXX Compiler: ${CMAKE_CXX_COMPILER}")

set(CMAKE_CONFIGURATION_TYPES Debug Release Development)

# Set this variable to specify a common place where CMake should put all executable files
set(RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/Bin/${CMAKE_GENERATOR})

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set_property(GLOBAL PROPERTY PREDEFINED_TARGETS_FOLDER "")

# Add DEBUG, _DEBUG definition to compiler in debug build
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DDEBUG -D_DEBUG")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG -D_DEBUG")

# Add DEVELOPMENT, _DEVELOPMENT definition to compiler in development build
set(CMAKE_C_FLAGS_DEVELOPMENT "${CMAKE_C_FLAGS_RELEASE} -DDEVELOPMENT -D_DEVELOPMENT")
set(CMAKE_CXX_FLAGS_DEVELOPMENT "${CMAKE_CXX_FLAGS_RELEASE} -DDEVELOPMENT -D_DEVELOPMENT")

set(CMAKE_EXE_LINKER_FLAGS_DEVELOPMENT ${CMAKE_EXE_LINKER_FLAGS_RELEASE})

################################################################################

if (NOT CMAKE_CROSSCOMPILING)
    set(USE_DESKTOP_EGL FALSE CACHE INTERNAL "Force to use EGL on desktop platform")
endif ()

if (USE_DESKTOP_EGL)
    add_definitions(-DUSE_DESKTOP_EGL)
endif ()

if (WIN32)
    # Settings for Windows
    add_definitions(-D_UNICODE -DUNICODE)
    
    set(USE_WINDOWS_OPENAL FALSE CACHE INTERNAL "Force to use OpenAL on Windows")

    if (USE_WINDOWS_OPENAL)
        add_definitions(-DUSE_WINDOWS_OPENAL)
    endif ()

    if (MSVC)
        # Enable Function-Level Linking
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /Gy")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Gy")
    
        # Force Synchronous PDB Writes
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /FS")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /FS")
    
        # Remove RTTI
        string(REGEX REPLACE "/GR-?" "" CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")

        #set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /LTCG")
        #set(CMAKE_STATIC_LINKER_FLAGS_RELEASE "${CMAKE_STATIC_LINKER_FLAGS_RELEASE} /LTCG")
        #set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /LTCG")

        # Suppress warnings when linking with release library
        set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} /NODEFAULTLIB:\"msvcrt.lib\"")
    endif ()
elseif (APPLE) 
    # Settings for macOS, iOS
    #set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu99")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -stdlib=libc++")

    add_compile_options("-Wno-unused-parameter")
    add_compile_options("-Wno-unused-variable")
    add_compile_options("-Wno-unused-local-typedef")
    add_compile_options("-Wno-unused-function")
    add_compile_options("-Wno-reorder")
    add_compile_options("-Wno-inconsistent-missing-override")
    add_compile_options("-Wno-tautological-undefined-compare")

    if (IOS)
        add_compile_options("-DIOS")

        set(IOS_DEPLOYMENT_TARGET 9.0)
   else ()
        set(CMAKE_OSX_SYSROOT "macosx")
        set(CMAKE_OSX_DEPLOYMENT_TARGET "10.9") # 10.9 Mavericks
        #set(CMAKE_OSX_ARCHITECTURES "$(ARCHS_STANDARD_64_BIT)")
    endif ()
elseif (ANDROID)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
    #set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++14 -fno-exceptions -fno-rtti")

    # Settings for Android
    add_compile_options("-DANDROID")

    add_compile_options("-Wno-unused-parameter")
    add_compile_options("-Wno-unused-variable")
    add_compile_options("-Wno-unused-local-typedef")
    add_compile_options("-Wno-unused-function")
    add_compile_options("-Wno-unused-private-field")
    add_compile_options("-Wno-reorder")
    add_compile_options("-Wno-inconsistent-missing-override")
    add_compile_options("-Wparentheses-equality")
    add_compile_options("-Wlogical-not-parentheses")
    add_compile_options("-Wshift-overflow")
    add_compile_options("-Wno-tautological-undefined-compare")
endif ()

################################################################################

if (XAMARIN)
    if (MSVC)
        set(ENGINE_BUILD_PLATFORM_DIR "XamarinWin64")
    endif ()

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -D__XAMARIN__")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D__XAMARIN__")
else ()
    if (MSVC)
        set(ENGINE_BUILD_PLATFORM_DIR "Win64")
    elseif (ANDROID)
        set(ENGINE_BUILD_PLATFORM_DIR "Android/${CMAKE_BUILD_TYPE}/${ANDROID_ABI}")
    elseif (APPLE)
        if (IOS)
            set(ENGINE_BUILD_PLATFORM_DIR "iOS$(EFFECTIVE_PLATFORM_NAME)")
        else ()
            set(ENGINE_BUILD_PLATFORM_DIR "macOS")
        endif ()
    else ()
        set(ENGINE_BUILD_PLATFORM_DIR ${CMAKE_GENERATOR})
    endif ()
endif ()

if (USE_LUAJIT)
    add_definitions(-DUSE_LUAJIT=1)
else ()
    add_definitions(-DUSE_LUAJIT=0)
endif ()

################################################################################
# Print C/CXX FLAGS
################################################################################

set(FLAGS
    CMAKE_C_FLAGS
    CMAKE_C_FLAGS_DEBUG
    CMAKE_C_FLAGS_RELEASE
    CMAKE_C_FLAGS_RELWITHDEBINFO
    CMAKE_CXX_FLAGS
    CMAKE_CXX_FLAGS_DEBUG
    CMAKE_CXX_FLAGS_RELEASE
    CMAKE_CXX_FLAGS_RELWITHDEBINFO
)

foreach(FLAG ${FLAGS})
    message(STATUS "${FLAG}: ${${FLAG}}")
endforeach()

################################################################################
# Sub projects
################################################################################
if (BUILD_RUNTIME)
    # Override subdirectory options
    set(JSONCPP_WITH_TESTS OFF CACHE "" INTERNAL FORCE)
    set(JSONCPP_WITH_POST_BUILD_UNITTEST OFF CACHE "" INTERNAL FORCE)
    set(JSONCPP_WITH_PKGCONFIG_SUPPORT OFF CACHE "" INTERNAL FORCE)

    add_subdirectory(Source/ThirdParty/zlib)
    add_subdirectory(Source/ThirdParty/minizip)
    add_subdirectory(Source/ThirdParty/libjpeg)
    add_subdirectory(Source/ThirdParty/libpng)
    add_subdirectory(Source/ThirdParty/libpvrt)
    add_subdirectory(Source/ThirdParty/etcpack)
    add_subdirectory(Source/ThirdParty/etc2comp)
    add_subdirectory(Source/ThirdParty/freetype)
    add_subdirectory(Source/ThirdParty/libogg)
    add_subdirectory(Source/ThirdParty/libvorbis)
    add_subdirectory(Source/ThirdParty/jsoncpp)
    add_subdirectory(Source/ThirdParty/tinyxml2)
    add_subdirectory(Source/ThirdParty/NvTriStrip)
    add_subdirectory(Source/ThirdParty/Bullet)
    add_subdirectory(Source/ThirdParty/HACD)
 
    if (USE_LUAJIT)
        add_subdirectory(Source/ThirdParty/luaJIT)
    else ()
        add_subdirectory(Source/ThirdParty/lua)
    endif ()
  
    add_subdirectory(Source/ThirdParty/luasocket)
    add_subdirectory(Source/ThirdParty/LuaCpp)
  
    add_subdirectory(Source/Runtime)

    add_subdirectory(Shaders)
endif ()

if (BUILD_PLAYER)
    add_subdirectory(Source/Player)
endif ()

if (BUILD_EDITOR)
    add_subdirectory(Source/ThirdParty/mikktspace)
    add_subdirectory(Source/ThirdParty/ToolWindowManager)
    add_subdirectory(Source/Editor)
endif ()

if (BUILD_TEST)
    if (NOT ANDROID)
        add_subdirectory(Source/TestBase)
    endif ()
    add_subdirectory(Source/TestRenderer)
endif ()

if (MSVC)
    if (BUILD_EDITOR)
        set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT BlueshiftEditor)
    elseif (BUILD_PLAYER)
        set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT BlueshiftPlayer)
    endif ()
endif ()

Bug reports, feature requests or code contributions are always very welcome.
To make things easier, here are a few tips:

Reporting bugs, requesting features
-----------------------------------

*   Best way to report bugs and request new features is to use GitHub
    [issues](https://github.com/PolygonTek/BlueshiftEngine/issues), but you can contact me
    also any other way.

Code contribution
-----------------

*   Follow the project coding guidelines. In short -- try to match style of the
    surrounding code and avoid any trailing whitespace.

*   Best way to contribute is by using GitHub [pull requests](https://github.com/PolygonTek/BlueshiftEngine/pulls)
    -- fork the repository and make pull request from feature branch. You can
    also send patches via e-mail or contact me any other way.

*   All your code will be released under license of the project (see [LICENSE](LICENSE.md)
    file for details), so make sure you have no problems with it. If you create new files, don't forget to add
    license header (verbatim copied from other files)
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
Blueshift Game Engine
=======================

[![License](https://img.shields.io/badge/Licence-Apache2.0-blue.svg)](LICENSE)
[![LoC](https://tokei.rs/b1/github/PolygonTek/BlueshiftEngine)](https://github.com/PolygonTek/BlueshiftEngine)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/586e8c52b0c847a9ac1bc7632c65e79c)](https://app.codacy.com/app/juhl/BlueshiftEngine?utm_source=github.com&utm_medium=referral&utm_content=PolygonTek/BlueshiftEngine&utm_campaign=Badge_Grade_Dashboard)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/9m56bx55uxe88rgs/branch/master?svg=true)](https://ci.appveyor.com/project/juhl48312/blueshiftengine/branch/master)

Blueshift is a cross-platform 3D game engine implemented in C++. it's free, open-source, and works on Windows, macOS, iOS, and Android.
The project is currently in an early stage of development.

For more information about the changes, see the [change log](CHANGELOG.md).

<a href='https://ko-fi.com/V7V66PEJ' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi1.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

Features
-------------------

  * Cross-platform (Windows, macOS, iOS and Android)
  * OpenGL 3.2+, OpenGL ES 3.0 rendering
  * Component based scene objects
  * Skeletal (with hardware skinning) animation
  * GPU instancing with skinned mesh
  * Parametric animation blending
  * Directional, spot, point lights
  * Environment probes
  * Shadow mapping (cascaded shadow map, omni directional shadow map, projected shadow map)
  * Particle system
  * HDR rendering and filmic tone mapping
  * Post-processing
  * PBR rendering
  * Environment probes
  * Physics using [Bullet](http://www.bulletphysics.org/)
  * Vehicle physics
  * Scripting using [Lua](https://www.lua.org/) and [LuaJIT](https://luajit.org/)
  * 2D and 3D audio playback using DirectSound, [OpenAL](https://www.openal.org/) and OpenSLES
  * TrueType font rendering using [FreeType](https://www.freetype.org/)
  * Unicode string support
  * 3D mesh/animation import from FBX
  * Supported IDEs: Visual Studio, Xcode, Android Studio
  * Playable WYSIWYG editor using [Qt](https://www.qt.io/) with undo & redo capabilities

Downloads
-------------------

Blueshift editor binaries are downloadable [here](https://github.com/PolygonTek/BlueshiftEngine/releases).

Examples
-------------------

Example projects are downloadable [here](https://github.com/PolygonTek/BlueshiftExamples/archive/master.zip).

Screenshots
-------------------

![Screenshot1](Screenshots/screenshot1.png)
![Screenshot2](Screenshots/screenshot2.png)
![Screenshot3](Screenshots/screenshot3.png)
![Screenshot4](Screenshots/screenshot4.png)

Documentation
-------------------

* [How to Build Engine Runtime Libraries](https://github.com/PolygonTek/BlueshiftEngine/wiki/How-to-Build-Engine-Runtime-Libraries)
* [Lua Debugging with ZeroBrane Studio](https://github.com/PolygonTek/BlueshiftEngine/wiki/Lua-Debugging-with-ZeroBrane-Studio)

License
-------------------

The Blueshift game engine source code is released under the Apache 2.0 license. Please see [LICENSE.md](LICENSE.md) for complete licensing information.

How To Contribute
-------------------

Contributions are always welcome, either reporting issues/bugs or forking the repository and then issuing pull requests when you have completed some additional coding that you feel will be beneficial to the main project. If you are interested in contributing in a more dedicated capacity, then please contact me.

See also
-------------------

[Blueshift Document](https://github.com/PolygonTek/BlueshiftDocument/blob/master/README.md)

Ld Build/xcode-ios/Source/Player/Debug-iphonesimulator/Player.app/Player normal x86_64
    cd /Users/sjpark/nvidiasample/Pyramid
    export IPHONEOS_DEPLOYMENT_TARGET=8.2
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch x86_64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator8.3.sdk -L/Users/sjpark/nvidiasample/Pyramid/Build/xcode-ios/Source/Player/Debug-iphonesimulator -F/Users/sjpark/nvidiasample/Pyramid/Build/xcode-ios/Source/Player/Debug-iphonesimulator -filelist /Users/sjpark/nvidiasample/Pyramid/Build/xcode-ios/Source/Player/BlueshiftPlayer.build/Debug-iphonesimulator/Player.build/Objects-normal/x86_64/Player.LinkFileList -Xlinker -objc_abi_version -Xlinker 2 -Wl,-search_paths_first -Wl,-headerpad_max_install_names -framework Foundation -framework UIKit -framework OpenGLES -framework CoreGraphics -framework QuartzCore 
	/Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/zlib_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/minizip_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/libjpeg_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/libpng_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/libpvrt_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/rg_etc1_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/freetype_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/jsoncpp_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/Bullet_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/HACD_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/BLib_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/Renderer_d.a /Users/sjpark/nvidiasample/Pyramid/Library/iOS/Debug/Core_d.a -stdlib=libc++ -Xlinker -no_implicit_dylibs -fobjc-arc -fobjc-link-runtime -mios-simulator-version-min=8.2 -Xlinker -dependency_info -Xlinker /Users/sjpark/nvidiasample/Pyramid/Build/xcode-ios/Source/Player/BlueshiftPlayer.build/Debug-iphonesimulator/Player.build/Objects-normal/x86_64/Player_dependency_info.dat -o /Users/sjpark/nvidiasample/Pyramid/Build/xcode-ios/Source/Player/Debug-iphonesimulator/Player.app/Player



BLib;minizip;zlib;Core;# To enable ProGuard in your project, edit project.properties
# to define the proguard.config property as described in that file.
#
# Add project specific ProGuard rules here.
# By default, the flags in this file are appended to flags specified
# in ${sdk.dir}/tools/proguard/proguard-android.txt
# You can edit the include path and order by changing the ProGuard
# include property in project.properties.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# Add any project specific keep options here:

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}
Output Directory: ..\..\..\Build\Android\$(Platform)\$(Configuration)\
Intermidiate Directory: ..\..\..\Build\Android\$(ProjectName)\$(Platform)\$(Configuration)\
Min Android API Level : Android 5.0 (android-21)
Target Android API Level : Android 5.0 (android-21)
Additional Include Directory: ..\..\..\Source\Dependencies\jsoncpp\include
Preprocesson Definition: JSON_USE_EXCEPTION=0



cmake_minimum_required(VERSION 2.8.12)

project(Bullet)

set(SRC_FILES
"btBulletCollisionCommon.h"  "btBulletDynamicsCommon.h"  "Bullet-C-Api.h"  "BulletCollision\BroadphaseCollision\btAxisSweep3.h"  "BulletCollision\BroadphaseCollision\btBroadphaseInterface.h"  "BulletCollision\BroadphaseCollision\btBroadphaseProxy.h"  
"BulletCollision\BroadphaseCollision\btCollisionAlgorithm.h"  "BulletCollision\BroadphaseCollision\btDbvt.h"  "BulletCollision\BroadphaseCollision\btDbvtBroadphase.h"  "BulletCollision\BroadphaseCollision\btDispatcher.h"  
"BulletCollision\BroadphaseCollision\btMultiSapBroadphase.h"  "BulletCollision\BroadphaseCollision\btOverlappingPairCache.h"  "BulletCollision\BroadphaseCollision\btOverlappingPairCallback.h"  "BulletCollision\BroadphaseCollision\btQuantizedBvh.h"
"BulletCollision\BroadphaseCollision\btSimpleBroadphase.h"  "BulletCollision\BroadphaseCollision\btAxisSweep3.cpp"  "BulletCollision\BroadphaseCollision\btBroadphaseProxy.cpp"  "BulletCollision\BroadphaseCollision\btCollisionAlgorithm.cpp"  
"BulletCollision\BroadphaseCollision\btDbvt.cpp"  "BulletCollision\BroadphaseCollision\btDbvtBroadphase.cpp"  "BulletCollision\BroadphaseCollision\btDispatcher.cpp"  "BulletCollision\BroadphaseCollision\btMultiSapBroadphase.cpp"  
"BulletCollision\BroadphaseCollision\btOverlappingPairCache.cpp"  "BulletCollision\BroadphaseCollision\btQuantizedBvh.cpp"  "BulletCollision\BroadphaseCollision\btSimpleBroadphase.cpp"  
"BulletCollision\CollisionDispatch\btActivatingCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btBoxBoxCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btBox2dBox2dCollisionAlgorithm.h" 
"BulletCollision\CollisionDispatch\btBoxBoxDetector.h"  "BulletCollision\CollisionDispatch\btCollisionConfiguration.h"  "BulletCollision\CollisionDispatch\btCollisionCreateFunc.h"  
"BulletCollision\CollisionDispatch\btCollisionDispatcher.h"  "BulletCollision\CollisionDispatch\btCollisionObject.h"  "BulletCollision\CollisionDispatch\btCollisionObjectWrapper.h"  "BulletCollision\CollisionDispatch\btCollisionWorld.h" 
"BulletCollision\CollisionDispatch\btCompoundCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btCompoundCompoundCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btConvexConcaveCollisionAlgorithm.h"  
"BulletCollision\CollisionDispatch\btConvexConvexAlgorithm.h"  "BulletCollision\CollisionDispatch\btConvex2dConvex2dAlgorithm.h"  "BulletCollision\CollisionDispatch\btConvexPlaneCollisionAlgorithm.h"  
"BulletCollision\CollisionDispatch\btDefaultCollisionConfiguration.h"  "BulletCollision\CollisionDispatch\btEmptyCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btGhostObject.h" 
"BulletCollision\CollisionDispatch\btHashedSimplePairCache.h"  "BulletCollision\CollisionDispatch\btManifoldResult.h"  "BulletCollision\CollisionDispatch\btSimulationIslandManager.h" 
"BulletCollision\CollisionDispatch\btSphereBoxCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btSphereSphereCollisionAlgorithm.h"  "BulletCollision\CollisionDispatch\btSphereTriangleCollisionAlgorithm.h"
"BulletCollision\CollisionDispatch\btUnionFind.h"  "BulletCollision\CollisionDispatch\SphereTriangleDetector.h"  "BulletCollision\CollisionDispatch\btActivatingCollisionAlgorithm.cpp" 
"BulletCollision\CollisionDispatch\btBoxBoxCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btBox2dBox2dCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btBoxBoxDetector.cpp" 
"BulletCollision\CollisionDispatch\btCollisionDispatcher.cpp"  "BulletCollision\CollisionDispatch\btCollisionObject.cpp"  "BulletCollision\CollisionDispatch\btCollisionWorld.cpp"  "BulletCollision\CollisionDispatch\btCompoundCollisionAlgorithm.cpp" 
"BulletCollision\CollisionDispatch\btCompoundCompoundCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btConvexConcaveCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btConvexConvexAlgorithm.cpp"  
"BulletCollision\CollisionDispatch\btConvexPlaneCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btConvex2dConvex2dAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btDefaultCollisionConfiguration.cpp"  
"BulletCollision\CollisionDispatch\btEmptyCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btGhostObject.cpp"  "BulletCollision\CollisionDispatch\btHashedSimplePairCache.cpp"  "BulletCollision\CollisionDispatch\btInternalEdgeUtility.cpp"  
"BulletCollision\CollisionDispatch\btInternalEdgeUtility.h"  "BulletCollision\CollisionDispatch\btManifoldResult.cpp"  "BulletCollision\CollisionDispatch\btSimulationIslandManager.cpp"  "BulletCollision\CollisionDispatch\btSphereBoxCollisionAlgorithm.cpp"  
"BulletCollision\CollisionDispatch\btSphereSphereCollisionAlgorithm.cpp"  "BulletCollision\CollisionDispatch\btSphereTriangleCollisionAlgorithm.cpp"
 
"BulletCollision\CollisionDispatch\btUnionFind.cpp" "BulletCollision\CollisionDispatch\SphereTriangleDetector.cpp" "BulletCollision\CollisionShapes\btBoxShape.h" "BulletCollision\CollisionShapes\btBox2dShape.h" 
"BulletCollision\CollisionShapes\btBvhTriangleMeshShape.h" "BulletCollision\CollisionShapes\btCapsuleShape.h" "BulletCollision\CollisionShapes\btCollisionMargin.h" "BulletCollision\CollisionShapes\btCollisionShape.h" 
"BulletCollision\CollisionShapes\btCompoundShape.h" "BulletCollision\CollisionShapes\btConcaveShape.h" "BulletCollision\CollisionShapes\btConeShape.h" "BulletCollision\CollisionShapes\btConvexHullShape.h" 
"BulletCollision\CollisionShapes\btConvexInternalShape.h" "BulletCollision\CollisionShapes\btConvexPointCloudShape.h" "BulletCollision\CollisionShapes\btConvexPolyhedron.h" "BulletCollision\CollisionShapes\btConvexShape.h" 
"BulletCollision\CollisionShapes\btConvex2dShape.h" "BulletCollision\CollisionShapes\btConvexTriangleMeshShape.h" "BulletCollision\CollisionShapes\btCylinderShape.h" "BulletCollision\CollisionShapes\btEmptyShape.h" 
"BulletCollision\CollisionShapes\btHeightfieldTerrainShape.h" "BulletCollision\CollisionShapes\btMaterial.h" "BulletCollision\CollisionShapes\btMinkowskiSumShape.h" "BulletCollision\CollisionShapes\btMultimaterialTriangleMeshShape.h" 
"BulletCollision\CollisionShapes\btMultiSphereShape.h" "BulletCollision\CollisionShapes\btOptimizedBvh.h" "BulletCollision\CollisionShapes\btPolyhedralConvexShape.h" "BulletCollision\CollisionShapes\btScaledBvhTriangleMeshShape.h" 
"BulletCollision\CollisionShapes\btShapeHull.h" "BulletCollision\CollisionShapes\btSphereShape.h" "BulletCollision\CollisionShapes\btStaticPlaneShape.h" "BulletCollision\CollisionShapes\btStridingMeshInterface.h" 
"BulletCollision\CollisionShapes\btTetrahedronShape.h" "BulletCollision\CollisionShapes\btTriangleBuffer.h" "BulletCollision\CollisionShapes\btTriangleCallback.h" "BulletCollision\CollisionShapes\btTriangleIndexVertexArray.h"
"BulletCollision\CollisionShapes\btTriangleIndexVertexMaterialArray.h" "BulletCollision\CollisionShapes\btTriangleInfoMap.h" "BulletCollision\CollisionShapes\btTriangleMesh.h" "BulletCollision\CollisionShapes\btTriangleMeshShape.h"
"BulletCollision\CollisionShapes\btTriangleShape.h" "BulletCollision\CollisionShapes\btUniformScalingShape.h" "BulletCollision\CollisionShapes\btBoxShape.cpp" "BulletCollision\CollisionShapes\btBox2dShape.cpp" 
"BulletCollision\CollisionShapes\btBvhTriangleMeshShape.cpp" "BulletCollision\CollisionShapes\btCapsuleShape.cpp" "BulletCollision\CollisionShapes\btCollisionShape.cpp" "BulletCollision\CollisionShapes\btCompoundShape.cpp" 
"BulletCollision\CollisionShapes\btConcaveShape.cpp" "BulletCollision\CollisionShapes\btConeShape.cpp" "BulletCollision\CollisionShapes\btConvexHullShape.cpp" "BulletCollision\CollisionShapes\btConvexInternalShape.cpp" 
"BulletCollision\CollisionShapes\btConvexPointCloudShape.cpp" "BulletCollision\CollisionShapes\btConvexPolyhedron.cpp" "BulletCollision\CollisionShapes\btConvexShape.cpp" "BulletCollision\CollisionShapes\btConvex2dShape.cpp" 
"BulletCollision\CollisionShapes\btConvexTriangleMeshShape.cpp" "BulletCollision\CollisionShapes\btCylinderShape.cpp" "BulletCollision\CollisionShapes\btEmptyShape.cpp" "BulletCollision\CollisionShapes\btHeightfieldTerrainShape.cpp" 
"BulletCollision\CollisionShapes\btMinkowskiSumShape.cpp" "BulletCollision\CollisionShapes\btMultimaterialTriangleMeshShape.cpp" "BulletCollision\CollisionShapes\btMultiSphereShape.cpp" "BulletCollision\CollisionShapes\btOptimizedBvh.cpp" 
"BulletCollision\CollisionShapes\btPolyhedralConvexShape.cpp" "BulletCollision\CollisionShapes\btScaledBvhTriangleMeshShape.cpp" "BulletCollision\CollisionShapes\btShapeHull.cpp" "BulletCollision\CollisionShapes\btSphereShape.cpp" 
"BulletCollision\CollisionShapes\btStaticPlaneShape.cpp" "BulletCollision\CollisionShapes\btStridingMeshInterface.cpp" "BulletCollision\CollisionShapes\btTetrahedronShape.cpp" "BulletCollision\CollisionShapes\btTriangleBuffer.cpp" 
"BulletCollision\CollisionShapes\btTriangleCallback.cpp" "BulletCollision\CollisionShapes\btTriangleIndexVertexArray.cpp" "BulletCollision\CollisionShapes\btTriangleIndexVertexMaterialArray.cpp" "BulletCollision\CollisionShapes\btTriangleMesh.cpp" 

"BulletCollision\CollisionShapes\btTriangleMeshShape.cpp" "BulletCollision\CollisionShapes\btUniformScalingShape.cpp" "BulletCollision\Gimpact\btBoxCollision.h" "BulletCollision\Gimpact\btClipPolygon.h" "BulletCollision\Gimpact\btContactProcessing.h" 
"BulletCollision\Gimpact\btGenericPoolAllocator.h" "BulletCollision\Gimpact\btGeometryOperations.h" "BulletCollision\Gimpact\btGImpactBvh.h" "BulletCollision\Gimpact\btGImpactCollisionAlgorithm.h" "BulletCollision\Gimpact\btGImpactMassUtil.h" 
"BulletCollision\Gimpact\btGImpactQuantizedBvh.h" "BulletCollision\Gimpact\btGImpactShape.h" "BulletCollision\Gimpact\btQuantization.h" "BulletCollision\Gimpact\btTriangleShapeEx.h" "BulletCollision\Gimpact\gim_array.h" 
"BulletCollision\Gimpact\gim_basic_geometry_operations.h" "BulletCollision\Gimpact\gim_bitset.h" "BulletCollision\Gimpact\gim_box_collision.h" "BulletCollision\Gimpact\gim_box_set.h" "BulletCollision\Gimpact\gim_clip_polygon.h" 
"BulletCollision\Gimpact\gim_contact.h" "BulletCollision\Gimpact\gim_geom_types.h" "BulletCollision\Gimpact\gim_geometry.h" "BulletCollision\Gimpact\gim_hash_table.h" "BulletCollision\Gimpact\gim_linear_math.h" "BulletCollision\Gimpact\gim_math.h" 
"BulletCollision\Gimpact\gim_memory.h" "BulletCollision\Gimpact\gim_radixsort.h" "BulletCollision\Gimpact\gim_tri_collision.h" "BulletCollision\Gimpact\btContactProcessing.cpp" "BulletCollision\Gimpact\btGenericPoolAllocator.cpp" 
"BulletCollision\Gimpact\btGImpactBvh.cpp" "BulletCollision\Gimpact\btGImpactCollisionAlgorithm.cpp" "BulletCollision\Gimpact\btGImpactQuantizedBvh.cpp" "BulletCollision\Gimpact\btGImpactShape.cpp" "BulletCollision\Gimpact\btTriangleShapeEx.cpp" 
"BulletCollision\Gimpact\gim_box_set.cpp" "BulletCollision\Gimpact\gim_contact.cpp" "BulletCollision\Gimpact\gim_memory.cpp" "BulletCollision\Gimpact\gim_tri_collision.cpp" "BulletCollision\NarrowPhaseCollision\btContinuousConvexCollision.h" 
"BulletCollision\NarrowPhaseCollision\btConvexCast.h" "BulletCollision\NarrowPhaseCollision\btConvexPenetrationDepthSolver.h" "BulletCollision\NarrowPhaseCollision\btDiscreteCollisionDetectorInterface.h" "BulletCollision\NarrowPhaseCollision\btGjkConvexCast.h" 
"BulletCollision\NarrowPhaseCollision\btGjkEpa2.h" "BulletCollision\NarrowPhaseCollision\btGjkEpaPenetrationDepthSolver.h" "BulletCollision\NarrowPhaseCollision\btGjkPairDetector.h" "BulletCollision\NarrowPhaseCollision\btManifoldPoint.h" 
"BulletCollision\NarrowPhaseCollision\btMinkowskiPenetrationDepthSolver.h" "BulletCollision\NarrowPhaseCollision\btPersistentManifold.h" "BulletCollision\NarrowPhaseCollision\btPointCollector.h" "BulletCollision\NarrowPhaseCollision\btRaycastCallback.h" 
"BulletCollision\NarrowPhaseCollision\btSimplexSolverInterface.h" "BulletCollision\NarrowPhaseCollision\btSubSimplexConvexCast.h" "BulletCollision\NarrowPhaseCollision\btVoronoiSimplexSolver.h" 
"BulletCollision\NarrowPhaseCollision\btPolyhedralContactClipping.h" "BulletCollision\NarrowPhaseCollision\btContinuousConvexCollision.cpp" "BulletCollision\NarrowPhaseCollision\btConvexCast.cpp" "BulletCollision\NarrowPhaseCollision\btGjkConvexCast.cpp" 
"BulletCollision\NarrowPhaseCollision\btGjkEpa2.cpp" "BulletCollision\NarrowPhaseCollision\btGjkEpaPenetrationDepthSolver.cpp" "BulletCollision\NarrowPhaseCollision\btGjkPairDetector.cpp" 
"BulletCollision\NarrowPhaseCollision\btMinkowskiPenetrationDepthSolver.cpp" "BulletCollision\NarrowPhaseCollision\btPersistentManifold.cpp" "BulletCollision\NarrowPhaseCollision\btRaycastCallback.cpp" 
"BulletCollision\NarrowPhaseCollision\btSubSimplexConvexCast.cpp" "BulletCollision\NarrowPhaseCollision\btVoronoiSimplexSolver.cpp" "BulletCollision\NarrowPhaseCollision\btPolyhedralContactClipping.cpp" 
"BulletDynamics\Character\btCharacterControllerInterface.h" "BulletDynamics\Character\btKinematicCharacterController.h" "BulletDynamics\Character\btKinematicCharacterController.cpp" "BulletDynamics\ConstraintSolver\btConeTwistConstraint.h" 
"BulletDynamics\ConstraintSolver\btConstraintSolver.h" "BulletDynamics\ConstraintSolver\btContactConstraint.h" "BulletDynamics\ConstraintSolver\btContactSolverInfo.h" "BulletDynamics\ConstraintSolver\btFixedConstraint.h" 
"BulletDynamics\ConstraintSolver\btGearConstraint.h" "BulletDynamics\ConstraintSolver\btGeneric6DofConstraint.h" "BulletDynamics\ConstraintSolver\btGeneric6DofSpringConstraint.h" "BulletDynamics\ConstraintSolver\btHinge2Constraint.h" 
"BulletDynamics\ConstraintSolver\btHingeConstraint.h" "BulletDynamics\ConstraintSolver\btJacobianEntry.h" "BulletDynamics\ConstraintSolver\btPoint2PointConstraint.h" "BulletDynamics\ConstraintSolver\btSequentialImpulseConstraintSolver.h" 
"BulletDynamics\ConstraintSolver\btSliderConstraint.h" "BulletDynamics\ConstraintSolver\btSolve2LinearConstraint.h" "BulletDynamics\ConstraintSolver\btSolverBody.h" "BulletDynamics\ConstraintSolver\btSolverConstraint.h"
"BulletDynamics\ConstraintSolver\btTypedConstraint.h" "BulletDynamics\ConstraintSolver\btUniversalConstraint.h" "BulletDynamics\ConstraintSolver\btConeTwistConstraint.cpp" "BulletDynamics\ConstraintSolver\btContactConstraint.cpp" 
"BulletDynamics\ConstraintSolver\btFixedConstraint.cpp" "BulletDynamics\ConstraintSolver\btGearConstraint.cpp" "BulletDynamics\ConstraintSolver\btGeneric6DofConstraint.cpp" "BulletDynamics\ConstraintSolver\btGeneric6DofSpringConstraint.cpp"
"BulletDynamics\ConstraintSolver\btHinge2Constraint.cpp" "BulletDynamics\ConstraintSolver\btHingeConstraint.cpp" "BulletDynamics\ConstraintSolver\btPoint2PointConstraint.cpp" "BulletDynamics\ConstraintSolver\btSequentialImpulseConstraintSolver.cpp" 
"BulletDynamics\ConstraintSolver\btSliderConstraint.cpp" "BulletDynamics\ConstraintSolver\btSolve2LinearConstraint.cpp" "BulletDynamics\ConstraintSolver\btTypedConstraint.cpp" "BulletDynamics\ConstraintSolver\btUniversalConstraint.cpp" 
"BulletDynamics\Dynamics\btActionInterface.h" "BulletDynamics\Dynamics\btDiscreteDynamicsWorld.h" "BulletDynamics\Dynamics\btDynamicsWorld.h" "BulletDynamics\Dynamics\btSimpleDynamicsWorld.h" "BulletDynamics\Dynamics\btRigidBody.h" 
"BulletDynamics\Dynamics\btDiscreteDynamicsWorld.cpp" "BulletDynamics\Dynamics\btRigidBody.cpp" "BulletDynamics\Dynamics\btSimpleDynamicsWorld.cpp" "BulletDynamics\Dynamics\Bullet"-"C"-"API.cpp" "BulletDynamics\Vehicle\btRaycastVehicle.h" 
"BulletDynamics\Vehicle\btVehicleRaycaster.h" "BulletDynamics\Vehicle\btWheelInfo.h" "BulletDynamics\Vehicle\btRaycastVehicle.cpp" "BulletDynamics\Vehicle\btWheelInfo.cpp" "BulletDynamics\Featherstone\btMultiBody.h" 
"BulletDynamics\Featherstone\btMultiBodyConstraintSolver.h" "BulletDynamics\Featherstone\btMultiBodyDynamicsWorld.h" "BulletDynamics\Featherstone\btMultiBodyLink.h" "BulletDynamics\Featherstone\btMultiBodyLinkCollider.h" 
"BulletDynamics\Featherstone\btMultiBodySolverConstraint.h" "BulletDynamics\Featherstone\btMultiBodyConstraint.h" "BulletDynamics\Featherstone\btMultiBodyJointLimitConstraint.h" "BulletDynamics\Featherstone\btMultiBodyConstraint.h"
"BulletDynamics\Featherstone\btMultiBodyPoint2Point.h" "BulletDynamics\Featherstone\btMultiBodyJointMotor.h" "BulletDynamics\Featherstone\btMultiBody.cpp" "BulletDynamics\Featherstone\btMultiBodyConstraintSolver.cpp" 
"BulletDynamics\Featherstone\btMultiBodyDynamicsWorld.cpp" "BulletDynamics\Featherstone\btMultiBodyJointLimitConstraint.cpp" "BulletDynamics\Featherstone\btMultiBodyConstraint.cpp" "BulletDynamics\Featherstone\btMultiBodyPoint2Point.cpp" 
"BulletDynamics\Featherstone\btMultiBodyJointMotor.cpp" "BulletDynamics\MLCPSolvers\btDantzigLCP.h" "BulletDynamics\MLCPSolvers\btDantzigSolver.h" "BulletDynamics\MLCPSolvers\btMLCPSolver.h" "BulletDynamics\MLCPSolvers\btMLCPSolverInterface.h" 
"BulletDynamics\MLCPSolvers\btPATHSolver.h" "BulletDynamics\MLCPSolvers\btSolveProjectedGaussSeidel.h" "BulletDynamics\MLCPSolvers\btDantzigLCP.cpp" "BulletDynamics\MLCPSolvers\btMLCPSolver.cpp" "BulletSoftBody\btSoftBody.h" 
"BulletSoftBody\btSoftBodyData.h" "BulletSoftBody\btSoftBodyConcaveCollisionAlgorithm.h" "BulletSoftBody\btSoftBodyHelpers.h" "BulletSoftBody\btSoftBodyRigidBodyCollisionConfiguration.h" "BulletSoftBody\btSoftRigidCollisionAlgorithm.h" 
"BulletSoftBody\btSoftRigidDynamicsWorld.h" "BulletSoftBody\btSoftSoftCollisionAlgorithm.h" "BulletSoftBody\btSparseSDF.h" "BulletSoftBody\btSoftBodySolvers.h" "BulletSoftBody\btDefaultSoftBodySolver.h" "BulletSoftBody\btSoftBodySolverVertexBuffer.h" 
"BulletSoftBody\btSoftBody.cpp" "BulletSoftBody\btSoftBodyConcaveCollisionAlgorithm.cpp" "BulletSoftBody\btSoftBodyHelpers.cpp" "BulletSoftBody\btSoftBodyRigidBodyCollisionConfiguration.cpp" "BulletSoftBody\btSoftRigidCollisionAlgorithm.cpp"
"BulletSoftBody\btSoftRigidDynamicsWorld.cpp" "BulletSoftBody\btSoftSoftCollisionAlgorithm.cpp" "BulletSoftBody\btDefaultSoftBodySolver.cpp" "LinearMath\btAabbUtil2.h" "LinearMath\btAlignedAllocator.h" "LinearMath\btAlignedObjectArray.h" 
"LinearMath\btConvexHull.h" "LinearMath\btConvexHullComputer.h" "LinearMath\btDefaultMotionState.h" "LinearMath\btGeometryUtil.h" "LinearMath\btGrahamScan2dConvexHull.h" "LinearMath\btHashMap.h" "LinearMath\btIDebugDraw.h" "LinearMath\btList.h" 
"LinearMath\btMatrix3x3.h" "LinearMath\btMinMax.h" "LinearMath\btMotionState.h" "LinearMath\btPolarDecomposition.h" "LinearMath\btPoolAllocator.h" "LinearMath\btQuadWord.h" "LinearMath\btQuaternion.h" "LinearMath\btQuickprof.h" "LinearMath\btRandom.h"
"LinearMath\btScalar.h" "LinearMath\btSerializer.h" "LinearMath\btStackAlloc.h" "LinearMath\btTransform.h" "LinearMath\btTransformUtil.h" "LinearMath\btVector3.h" "LinearMath\btAlignedAllocator.cpp" "LinearMath\btConvexHull.cpp" 
"LinearMath\btConvexHullComputer.cpp" "LinearMath\btGeometryUtil.cpp" "LinearMath\btPolarDecomposition.cpp" "LinearMath\btQuickprof.cpp" "LinearMath\btSerializer.cpp" "LinearMath\btVector3.cpp" "ConvexDecomposition\ConvexDecomposition.h" 
"ConvexDecomposition\cd_vector.h" "ConvexDecomposition\concavity.h" "ConvexDecomposition\bestfitobb.h" "ConvexDecomposition\ConvexBuilder.h" "ConvexDecomposition\cd_wavefront.h" "ConvexDecomposition\fitsphere.h" "ConvexDecomposition\meshvolume.h"
"ConvexDecomposition\raytri.h" "ConvexDecomposition\vlookup.h" "ConvexDecomposition\bestfit.h" "ConvexDecomposition\cd_hull.h" "ConvexDecomposition\bestfitobb.cpp" "ConvexDecomposition\ConvexBuilder.cpp" "ConvexDecomposition\cd_wavefront.cpp"
"ConvexDecomposition\fitsphere.cpp" "ConvexDecomposition\meshvolume.cpp" "ConvexDecomposition\raytri.cpp" "ConvexDecomposition\vlookup.cpp" "ConvexDecomposition\bestfit.cpp" "ConvexDecomposition\cd_hull.cpp" "ConvexDecomposition\ConvexDecomposition.cpp"
"ConvexDecomposition\concavity.cpp" "ConvexDecomposition\float_math.cpp" "ConvexDecomposition\planetri.cpp" "ConvexDecomposition\splitplane.cpp" 
)

include_directories(
	${PROJECT_SOURCE_DIR}
)

auto_source_group(${SRC_FILES})

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_include_directories(${PROJECT_NAME}
	PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
)

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
Output Directory: ..\..\..\Build\Android\$(Platform)\$(Configuration)\
Intermidiate Directory: ..\..\..\Build\Android\$(ProjectName)\$(Platform)\$(Configuration)\
Min Android API Level : Android 5.0 (android-21)
Target Android API Level : Android 5.0 (android-21)
Additional Include Directory: ..\..\..\Source\Dependencies\freetype\include
Preprocesson Definition: FT2_BUILD_LIBRARY
Find what:[ \t]+([^ \t\r\n]+)
Replace with:    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\$1" />


cmake_minimum_required(VERSION 2.8.12)

project(freetype)

set(VERSION_MAJOR "2")
set(VERSION_MINOR "5")
set(VERSION_PATCH "5")
set(PROJECT_VERSION ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH})

# Compiler definitions for building the library
add_definitions(-DFT2_BUILD_LIBRARY)

# Specify library include directories
include_directories("${PROJECT_SOURCE_DIR}\include")

file(GLOB PUBLIC_HEADERS "include\*.h")
file(GLOB PUBLIC_CONFIG_HEADERS "include\config\*.h")
file(GLOB PRIVATE_HEADERS "include\internal\*.h")

set(BASE_SRCS
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\autofit\autofit.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftadvanc.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftbbox.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftbdf.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftbitmap.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftcalc.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftcid.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftdbgmem.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftdebug.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftfstype.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftgasp.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftgloadr.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftglyph.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftgxval.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftinit.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftlcdfil.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftmm.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftobjs.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftotval.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftoutln.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftpatent.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftpfr.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftrfork.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftsnames.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftstream.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftstroke.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftsynth.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftsystem.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\fttrigon.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\fttype1.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftutil.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftwinfnt.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\base\ftxf86.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\bdf\bdf.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\bzip2\ftbzip2.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\cache\ftcache.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\cff\cff.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\cid\type1cid.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\gzip\ftgzip.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\lzw\ftlzw.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\pcf\pcf.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\pfr\pfr.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\psaux\psaux.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\pshinter\pshinter.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\psnames\psmodule.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\raster\raster.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\sfnt\sfnt.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\smooth\smooth.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\truetype\truetype.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\type1\type1.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\type42\type42.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\freetype\src\winfonts\winfnt.c" />
)

set(ALL_FILES ${PUBLIC_HEADERS}
  ${PUBLIC_CONFIG_HEADERS}
  ${PRIVATE_HEADERS}
  ${BASE_SRCS}
)

source_group("Public Headers" FILES ${PUBLIC_HEADERS})
source_group("Public Config Headers" FILES ${PUBLIC_CONFIG_HEADERS})
source_group("Private Headers" FILES ${PRIVATE_HEADERS})
auto_source_group(${BASE_SRCS})

include_directories("src\truetype")
include_directories("src\sfnt")
include_directories("src\autofit")
include_directories("src\smooth")
include_directories("src\raster")
include_directories("src\psaux")
include_directories("src\psnames")

add_library(${PROJECT_NAME} STATIC ${ALL_FILES})

target_include_directories(${PROJECT_NAME} 
	PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}\include>
)

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})Output Directory: ..\..\..\Build\Android\$(Platform)\$(Configuration)\
Intermidiate Directory: ..\..\..\Build\Android\$(ProjectName)\$(Platform)\$(Configuration)\
Min Android API Level : Android 5.0 (android-21)
Target Android API Level : Android 5.0 (android-21)
Additional Include Directory: ..\..\..\Source\Dependencies\HACD
Preprocesson Definition: 

cmake_minimum_required(VERSION 2.8.12)

project(HACD)

set(SRC_FILES
	hacdCircularList.h
	hacdGraph.h
	hacdHACD.h
	hacdICHull.h
	hacdManifoldMesh.h
	hacdVector.h
	hacdVersion.h
	hacdCircularList.inl
	hacdVector.inl
	hacdGraph.cpp
	hacdHACD.cpp
	hacdICHull.cpp
	hacdManifoldMesh.cpp
)

auto_source_group(${SRC_FILES})

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})Output Directory: ..\..\..\Build\Android\$(Platform)\$(Configuration)\
Intermidiate Directory: ..\..\..\Build\Android\$(ProjectName)\$(Platform)\$(Configuration)\
Min Android API Level : Android 5.0 (android-21)
Target Android API Level : Android 5.0 (android-21)
Additional Include Directory: ..\..\..\Source\Dependencies\jsoncpp\include
Preprocesson Definition: JSON_USE_EXCEPTION=0



CMAKE_MINIMUM_REQUIRED(VERSION 2.8.5)

PROJECT(jsoncpp)

SET(LIB_SUFFIX "" CACHE STRING "Optional arch-dependent suffix for the library installation directory")

# Set variable named ${VAR_NAME} to value ${VALUE}
FUNCTION(set_using_dynamic_name VAR_NAME VALUE)
    SET( "${VAR_NAME}" "${VALUE}" PARENT_SCOPE)
ENDFUNCTION(set_using_dynamic_name)

# Extract major, minor, patch from version text
# Parse a version string "X.Y.Z" and outputs
# version parts in ${OUPUT_PREFIX}_MAJOR, _MINOR, _PATCH.
# If parse succeeds then ${OUPUT_PREFIX}_FOUND is TRUE.
MACRO(jsoncpp_parse_version VERSION_TEXT OUPUT_PREFIX)
    SET(VERSION_REGEX "[0-9]+\\.[0-9]+\\.[0-9]+(-[a-zA-Z0-9_]+)?")
    IF( ${VERSION_TEXT} MATCHES ${VERSION_REGEX} )
        STRING(REGEX MATCHALL "[0-9]+|-([A-Za-z0-9_]+)" VERSION_PARTS ${VERSION_TEXT})
        LIST(GET VERSION_PARTS 0 ${OUPUT_PREFIX}_MAJOR)
        LIST(GET VERSION_PARTS 1 ${OUPUT_PREFIX}_MINOR)
        LIST(GET VERSION_PARTS 2 ${OUPUT_PREFIX}_PATCH)
        set_using_dynamic_name( "${OUPUT_PREFIX}_FOUND" TRUE )
    ELSE( ${VERSION_TEXT} MATCHES ${VERSION_REGEX} )
        set_using_dynamic_name( "${OUPUT_PREFIX}_FOUND" FALSE )
    ENDIF( ${VERSION_TEXT} MATCHES ${VERSION_REGEX} )
ENDMACRO(jsoncpp_parse_version)

# Read out version from "version" file
FILE(STRINGS "version" JSONCPP_VERSION)

jsoncpp_parse_version( ${JSONCPP_VERSION} JSONCPP_VERSION )
IF(NOT JSONCPP_VERSION_FOUND)
    MESSAGE(FATAL_ERROR "Failed to parse version string properly. Expect X.Y.Z")
ENDIF(NOT JSONCPP_VERSION_FOUND)

MESSAGE(STATUS "JsonCpp Version: ${JSONCPP_VERSION_MAJOR}.${JSONCPP_VERSION_MINOR}.${JSONCPP_VERSION_PATCH}")
# File version.h is only regenerated on CMake configure step
CONFIGURE_FILE( "${PROJECT_SOURCE_DIR}/src/lib_json/version.h.in"
                "${PROJECT_SOURCE_DIR}/include/json/version.h" )

# Include our configuration header
INCLUDE_DIRECTORIES( ${PROJECT_SOURCE_DIR}/include )

if ( MSVC )
    # Only enabled in debug because some old versions of VS STL generate
    # unreachable code warning when compiled in release configuration.
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /W4 ")
endif( MSVC )

# Build the different applications
ADD_SUBDIRECTORY( src/lib_json )
Output Directory: ..\..\..\Build\Android\$(Platform)\$(Configuration)\
Intermidiate Directory: ..\..\..\Build\Android\$(ProjectName)\$(Platform)\$(Configuration)\
Min Android API Level : Android 5.0 (android-21)
Target Android API Level : Android 5.0 (android-21)
Additional Include Directory: ..\..\..\Source\Dependencies\libjpeg
Preprocesson Definition: 
Find what:[ \t]+([^ \t\r\n]+)
Replace with:    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\$1" />


cmake_minimum_required(VERSION 2.8.12)

project(libjpeg)

set(SRC_FILES
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\cderror.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcinit.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdapimin.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdinput.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jfdctflt.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jmorecfg.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\cdjpeg.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcmainct.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdapistd.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdmainct.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jfdctfst.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jpegint.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jaricom.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcmarker.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdarith.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdmarker.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jfdctint.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jpeglib.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcapimin.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcmaster.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdatadst.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdmaster.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jidctflt.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jquant1.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcapistd.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcomapi.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdatasrc.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdmerge.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jidctfst.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jquant2.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcarith.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jconfig.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdcoefct.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdpostct.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jidctint.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jutils.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jccoefct.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcparam.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdcolor.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdsample.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jinclude.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jversion.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jccolor.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcprepct.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdct.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdtrans.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jmemmgr.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\transupp.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcdctmgr.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jcsample.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jddctmgr.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jerror.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jmemnobs.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\transupp.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jchuff.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jctrans.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jdhuff.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jerror.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libjpeg\jmemsys.h" />
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
Output Directory: ..\..\..\Build\Android\$(Platform)\$(Configuration)\
Intermidiate Directory: ..\..\..\Build\Android\$(ProjectName)\$(Platform)\$(Configuration)\
Min Android API Level : Android 5.0 (android-21)
Target Android API Level : Android 5.0 (android-21)
Additional Include Directory: ..\..\..\Source\Dependencies\freetype\include
Preprocesson Definition: 
Find what:[ \t]+([^ \t\r\n]+\.c\w*)
Replace with:    <ClCompile Include="..\..\..\Source\Dependencies\libpng\$1" />


cmake_minimum_required(VERSION 2.8.12)

project(libpng)

set(SRC_FILES
  png.h
  pngconf.h
  pnglibconf.h
  pngdebug.h
  pnginfo.h
  pngpriv.h
  pngstruct.h
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\png.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngerror.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngget.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngmem.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngpread.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngread.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngrio.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngrtran.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngrutil.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngset.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngtrans.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngwio.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngwrite.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngwtran.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\pngwutil.c" />
)

if (IOS_PLATFORM)
  list(APPEND SRC_FILES
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\arm\arm_init.c" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpng\arm\filter_neon_intrinsics.c" />
    #arm\filter_neon.S
  )
endif ()

add_library(${PROJECT_NAME} STATIC ${SRC_FILES} ${ARM_FILES})

target_link_libraries(${PROJECT_NAME} zlib)

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}\Library\${ENGINE_BUILD_PLATFORM_DIR})Find what:[ \t]+([^ \t\r\n]+)
Replace with:    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\$1" />


cmake_minimum_required(VERSION 2.8.12)

project(libpvrt)

set(SRC_FILES
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTArray.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTError.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTGlobal.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTMap.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTMemoryFileSystem.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTResourceFile.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTString.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTTexture.h" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTError.cpp" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTResourceFile.cpp" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTString.cpp" />
    <ClCompile Include="..\..\..\Source\Dependencies\libpvrt\PVRTTexture.cpp" />
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})cmake_minimum_required(VERSION 2.8.12)

project(minizip)

set(SRC_FILES
  ioapi.h
  unzip.h
  zip.h
  "ioapi.c"   "unzip.c"   "zip.c"
)

add_definitions(-DUSE_FILE32API)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_link_libraries(${PROJECT_NAME} zlib)

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})C:\Users\Seongjae\Documents\blueshift\Engine\Source\Dependencies\zlib


cmake_minimum_required(VERSION 2.4.4)
set(CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS ON)

project(zlib C)

set(VERSION "1.2.8")

option(ASM686 "Enable building i686 assembly implementation")
option(AMD64 "Enable building amd64 assembly implementation")

include(CheckTypeSize)
include(CheckFunctionExists)
include(CheckIncludeFile)
include(CheckCSourceCompiles)
enable_testing()

check_include_file(sys/types.h HAVE_SYS_TYPES_H)
check_include_file(stdint.h    HAVE_STDINT_H)
check_include_file(stddef.h    HAVE_STDDEF_H)

#
# Check to see if we have large file support
#
set(CMAKE_REQUIRED_DEFINITIONS -D_LARGEFILE64_SOURCE=1)
# We add these other definitions here because CheckTypeSize.cmake
# in CMake 2.4.x does not automatically do so and we want
# compatibility with CMake 2.4.x.
if(HAVE_SYS_TYPES_H)
    list(APPEND CMAKE_REQUIRED_DEFINITIONS -DHAVE_SYS_TYPES_H)
endif()
if(HAVE_STDINT_H)
    list(APPEND CMAKE_REQUIRED_DEFINITIONS -DHAVE_STDINT_H)
endif()
if(HAVE_STDDEF_H)
    list(APPEND CMAKE_REQUIRED_DEFINITIONS -DHAVE_STDDEF_H)
endif()

check_type_size(off64_t OFF64_T)
if(HAVE_OFF64_T)
   add_definitions(-D_LARGEFILE64_SOURCE=1)
endif()
set(CMAKE_REQUIRED_DEFINITIONS) # clear variable

#
# Check for fseeko
#
check_function_exists(fseeko HAVE_FSEEKO)
if(NOT HAVE_FSEEKO)
    add_definitions(-DNO_FSEEKO)
endif()

#
# Check for unistd.h
#
check_include_file(unistd.h Z_HAVE_UNISTD_H)

# Force to add definition Z_HAVE_UNISTD_H for iOS
if (DEFINED IOS_PLATFORM)
  add_definitions(-DZ_HAVE_UNISTD_H=1)
endif ()

if(MSVC)
    add_definitions(-D_CRT_SECURE_NO_DEPRECATE)
    add_definitions(-D_CRT_NONSTDC_NO_DEPRECATE)
    include_directories(${CMAKE_CURRENT_SOURCE_DIR})
endif()

if(NOT CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_CURRENT_BINARY_DIR)
    # If we're doing an out of source build and the user has a zconf.h
    # in their source tree...
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h)
        message(STATUS "Renaming")
        message(STATUS "    ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h")
        message(STATUS "to 'zconf.h.included' because this file is included with zlib")
        message(STATUS "but CMake generates it automatically in the build directory.")
        file(RENAME ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h.included)
  endif()
endif()

set(ZLIB_PC ${CMAKE_CURRENT_BINARY_DIR}/zlib.pc)

configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/zlib.pc.cmakein ${ZLIB_PC} @ONLY)
configure_file(	${CMAKE_CURRENT_SOURCE_DIR}/zconf.h.cmakein ${CMAKE_CURRENT_BINARY_DIR}/zconf.h @ONLY)

include_directories(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_SOURCE_DIR})


#============================================================================
# zlib
#============================================================================

set(ZLIB_PUBLIC_HDRS
    ${CMAKE_CURRENT_BINARY_DIR}/zconf.h
    zlib.h
)
set(ZLIB_PRIVATE_HDRS
    crc32.h
    deflate.h
    gzguts.h
    inffast.h
    inffixed.h
    inflate.h
    inftrees.h
    trees.h
    zutil.h
)
set(ZLIB_SRCS
    "adler32.c" "compress.c"     "crc32.c"    "deflate.c"    "gzclose.c"    "gzlib.c"    "gzread.c"    "gzwrite.c"    "inflate.c"
    "infback.c"   "inftrees.c"    "inffast.c"    "trees.c"    "uncompr.c"    "zutil.c"
)

if(NOT MINGW)
    set(ZLIB_DLL_SRCS
        win32/zlib1.rc # If present will override custom build rule below.
    )
endif()

if(CMAKE_COMPILER_IS_GNUCC)
    if(ASM686)
        set(ZLIB_ASMS contrib/asm686/match.S)
    elseif (AMD64)
        set(ZLIB_ASMS contrib/amd64/amd64-match.S)
    endif ()

	if(ZLIB_ASMS)
		add_definitions(-DASMV)
		set_source_files_properties(${ZLIB_ASMS} PROPERTIES LANGUAGE C COMPILE_FLAGS -DNO_UNDERLINE)
	endif()
endif()

if(MSVC)
    if(ASM686)
		ENABLE_LANGUAGE(ASM_MASM)
        set(ZLIB_ASMS
			contrib/masmx86/inffas32.asm
			contrib/masmx86/match686.asm
		)
    elseif (AMD64)
		ENABLE_LANGUAGE(ASM_MASM)
        set(ZLIB_ASMS
			contrib/masmx64/gvmat64.asm
			contrib/masmx64/inffasx64.asm
		)
    endif()

	if(ZLIB_ASMS)
		add_definitions(-DASMV -DASMINF)
	endif()
endif()

# parse the full version number from zlib.h and include in ZLIB_FULL_VERSION
file(READ ${CMAKE_CURRENT_SOURCE_DIR}/zlib.h _zlib_h_contents)
string(REGEX REPLACE ".*#define[ \t]+ZLIB_VERSION[ \t]+\"([-0-9A-Za-z.]+)\".*"
    "\\1" ZLIB_FULL_VERSION ${_zlib_h_contents})

if(MINGW)
    # This gets us DLL resource information when compiling on MinGW.
    if(NOT CMAKE_RC_COMPILER)
        set(CMAKE_RC_COMPILER windres.exe)
    endif()

    add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/zlib1rc.obj
                       COMMAND ${CMAKE_RC_COMPILER}
                            -D GCC_WINDRES
                            -I ${CMAKE_CURRENT_SOURCE_DIR}
                            -I ${CMAKE_CURRENT_BINARY_DIR}
                            -o ${CMAKE_CURRENT_BINARY_DIR}/zlib1rc.obj
                            -i ${CMAKE_CURRENT_SOURCE_DIR}/win32/zlib1.rc)
    set(ZLIB_DLL_SRCS ${CMAKE_CURRENT_BINARY_DIR}/zlib1rc.obj)
endif(MINGW)

add_library(${PROJECT_NAME} STATIC ${ZLIB_SRCS} ${ZLIB_ASMS} ${ZLIB_PUBLIC_HDRS} ${ZLIB_PRIVATE_HDRS})

if(UNIX)
    # On unix-like platforms the library is almost always called libz
   set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME z)
endif()

target_include_directories(${PROJECT_NAME} 
	PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
	PUBLIC $<BUILD_INTERFACE:${PROJECT_BINARY_DIR}>
)

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Dependencies)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

LD_LIBRARY_PATH: %USERPROFILE%\Documents\android;

AndroidPlayerLibrary/PostBuildEvent:
	copy $(IntermediateOutputPath)libAndroidPlayer.so %USERPROFILE%\Documents\androidcopy C:\ProgramData\Microsoft\AndroidNDK\android-ndk-r11c\prebuilt\android-arm\gdbserver\gdbserver  %USERPROFILE%\Documents\blueshift\Engine\Project\XamarinAndroid\XamarinPlayer/libs/armeabi-v7a/gdbserver
XamarinPlayer/libs/armeabi-v7a/libsangeles.so/Build Action:AndroidNativeLibrary
XamarinPlayer/libs/armeabi-v7a/gdbserver/Build Action:AndroidNativeLibrary
XamarinPlayerLibrary/PostBuildEvent:
#	copy $(IntermediateOutputPath)libXamarinPlayer.so %USERPROFILE%\Documents\android
	echo copy $(IntermediateOutputPath)libXamarinPlayer.so ..\XamarinPlayer\bin\$(Configuration)
	copy $(IntermediateOutputPath)libXamarinPlayer.so ..\XamarinPlayer\bin\$(Configuration)
	echo copy $(OutputPath)libXamarinPlayer.so ..\XamarinPlayer\libs\armeabi-v7a
	copy $(OutputPath)libXamarinPlayer.so ..\XamarinPlayer\libs\armeabi-v7a


LD_LIBRARY_PATH: %USERPROFILE%\Documents\android;


Android ndk debug
=========================

mkdir %USERPROFILE%\Documents\android
cd %USERPROFILE%\Documents\android
adb shell ls -l /system/bin/app_process
adb pull /system/bin/app_process  
adb pull /system/bin/linker  


SanAngele Project > Properties > Android Options > Debugging optoins > Xamarin
adb shell "ps | grep SanAngeles"
adb> su
adb> cat /proc/21223/cmdline
adb forward tcp:5039 localfilesystem:/data/data/SanAngeles.SanAngeles/debug-pipe
adb shell run-as SanAngeles.SanAngeles /data/data/SanAngeles.SanAngeles/lib/gdbserver +debug-pipe --attach 23467 
cd C:\NVPACK\android-ndk-r10e\toolchains\arm-linux-androideabi-4.9\prebuilt\windows-x86_64\bin
arm-linux-androideabi-gdb %USERPROFILE%\Documents\android\app_process 
gdb> target remote :5039
# gdb> set solib-search-path ~/Documents/android;~/Documents/android/system_lib:~/Documents/android/vendor_lib
gdb> info sharedlibrary 



Mono San Angeles sample port
============================

This is a port of Android NDK sample (sanangeles).
http://developer.android.com/tools/sdk/ndk/index.html#Samples


This library sample is easily ported because there is no dependency on
any jobject instances or JNIEnv instance in C code.

There are **TWO** versions available:


1) C++ for Visual Studio 2015 (SanAngeles_NativeDebug)
---

Complete C++ source is built as part of the solution, which means you can debug the C++ code while running the Xamarin.Android project using **Visual Studio 2015**.



2) Pre-compiled (SanAngeles_NDK)
-----

The project contains pre-compiled libsanangeles.so under libs directory
(armeabi, armeabi-v7a and x86 are supported). You'll only debug the Xamarin.Android C# code with this example.




S
Images, layout descriptions, binary blobs and string dictionaries can be included 
in your application as resource files.  Various Android APIs are designed to 
operate on the resource IDs instead of dealing with images, strings or binary blobs 
directly.

For example, a sample Android app that contains a user interface layout (main.axml),
an internationalization string table (strings.xml) and some icons (drawable-XXX/icon.png) 
would keep its resources in the "Resources" directory of the application:

Resources/
    drawable/
        icon.png

    layout/
        main.axml

    values/
        strings.xml

In order to get the build system to recognize Android resources, set the build action to
"AndroidResource".  The native Android APIs do not operate directly with filenames, but 
instead operate on resource IDs.  When you compile an Android application that uses resources, 
the build system will package the resources for distribution and generate a class called "R" 
(this is an Android convention) that contains the tokens for each one of the resources 
included. For example, for the above Resources layout, this is what the R class would expose:

public class R {
    public class drawable {
        public const int icon = 0x123;
    }

    public class layout {
        public const int main = 0x456;
    }

    public class strings {
        public const int first_string = 0xabc;
        public const int second_string = 0xbcd;
    }
}

You would then use R.drawable.icon to reference the drawable/icon.png file, or R.layout.main 
to reference the layout/main.axml file, or R.strings.first_string to reference the first 
string in the dictionary file values/strings.xml.
libControl 32 bit 빌드
XamarinControl 실행

==========================

libControl > Project option > General > Output Directory > ..\..\..\Bin\$(Platform)\$(Configuration)\
XamrinContorl > Project option > Build > Output path > ..\..\..\Bin\Win32\Debug\
========================================================================
    DYNAMIC LINK LIBRARY : ConsoleDll Project Overview
========================================================================

AppWizard has created this ConsoleDll DLL for you.

This file contains a summary of what you will find in each of the files that
make up your ConsoleDll application.


ConsoleDll.vcxproj
    This is the main project file for VC++ projects generated using an Application Wizard.
    It contains information about the version of Visual C++ that generated the file, and
    information about the platforms, configurations, and project features selected with the
    Application Wizard.

ConsoleDll.vcxproj.filters
    This is the filters file for VC++ projects generated using an Application Wizard. 
    It contains information about the association between the files in your project 
    and the filters. This association is used in the IDE to show grouping of files with
    similar extensions under a specific node (for e.g. ".cpp" files are associated with the
    "Source Files" filter).

ConsoleDll.cpp
    This is the main DLL source file.

	When created, this DLL does not export any symbols. As a result, it
	will not produce a .lib file when it is built. If you wish this project
	to be a project dependency of some other project, you will either need to
	add code to export some symbols from the DLL so that an export library
	will be produced, or you can set the Ignore Input Library property to Yes
	on the General propert page of the Linker folder in the project's Property
	Pages dialog box.

/////////////////////////////////////////////////////////////////////////////
Other standard files:

StdAfx.h, StdAfx.cpp
    These files are used to build a precompiled header (PCH) file
    named ConsoleDll.pch and a precompiled types file named StdAfx.obj.

/////////////////////////////////////////////////////////////////////////////
Other notes:

AppWizard uses "TODO:" comments to indicate parts of the source code you
should add to or customize.

/////////////////////////////////////////////////////////////////////////////
cmake_minimum_required(VERSION 2.8.12)

project(Shaders)

file(GLOB_RECURSE ALL_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/**)

auto_source_group(${ALL_FILES})

add_custom_target(${PROJECT_NAME} SOURCES ${ALL_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Blueshift)
cmake_minimum_required(VERSION 2.8.12)

project(libControl)

if (WIN32)
  include(FindOpenAL)
endif ()

set(ALL_FILES
  PreCompiled.h
  PreCompiled.cpp
  Protocol.h
  Client.h
  Client.cpp
  Control.cpp
)

auto_source_group(${ALL_FILES})

if (WIN32)
  include_directories(${OPENAL_INCLUDE_DIR})
endif ()

include_directories(
  ${PROJECT_SOURCE_DIR}
  ${ENGINE_INCLUDE_DIR}/Engine/Public
  ${ENGINE_INCLUDE_DIR}/ThirdParty
  ${ENGINE_INCLUDE_DIR}/ThirdParty/asio/include
)

enable_precompiled_header(Precompiled.h Precompiled.cpp CORE_FILES)

add_library(${PROJECT_NAME} SHARED ${ALL_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Blueshift)
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
set_target_properties(${PROJECT_NAME} PROPERTIES MACOSX_RPATH 1)
#set_target_properties(${PROJECT_NAME} PROPERTIES INSTALL_NAME_DIR "@loader_path")

if (WIN32)
	  target_link_libraries(${PROJECT_NAME} winmm.lib imm32.lib)

	  find_package(OpenGL REQUIRED)
	  target_link_libraries(${PROJECT_NAME} ${OPENGL_LIBRARIES})
elseif (APPLE)
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "gnu++0x")
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LIBRARY "libc++")
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_CLANG_MODULES_AUTOLINK "NO")
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC "YES")
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_GCC_C_LANGUAGE_STANDARD "gnu99")
  #set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS NO)
  #set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS[variant=Debug] YES)
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_COPY_PHASE_STRIP YES)
  set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_COPY_PHASE_STRIP[variant=Debug] NO)
  #set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_GCC_PREFIX_HEADER ${CMAKE_CURRENT_LIST_DIR}/Precompiled.h)
  #set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_GCC_PRECOMPILE_PREFIX_HEADER "YES")

	    add_framework(${PROJECT_NAME} Foundation)
	    add_framework(${PROJECT_NAME} AppKit)
	    add_framework(${PROJECT_NAME} Carbon)
	    add_framework(${PROJECT_NAME} OpenGL)
	    add_framework(${PROJECT_NAME} CoreGraphics)
	    add_framework(${PROJECT_NAME} CoreVideo)
	    add_framework(${PROJECT_NAME} OpenAL)
	    add_framework(${PROJECT_NAME} AudioToolbox)
	    add_framework(${PROJECT_NAME} AVFoundation)
## OSX

endif ()

target_link_libraries(${PROJECT_NAME} 
	    zlib
	    minizip
	    libjpeg
	    libpng
	    libpvrt
	    rg_etc1
	    freetype
	    jsoncpp
	    Bullet
	    HACD
	    BlueshiftEngine
)
cmake_minimum_required(VERSION 2.8.12)

# Variables are given by Blueshift Editor
set(BS_APP_NAME "Blueshift Player" CACHE STRING "BS_APP_NAME variable defaulting")
set(BS_APP_IDENTIFIER "com.polygontek.BlueshiftPlayer" CACHE STRING "BS_APP_IDENTIFIER variable defaulting")
set(BS_APP_VERSION "1.0" CACHE STRING "BS_APP_VERSION variable defaulting")
set(BS_PRODUCT_NAME "BlueshiftPlayer" CACHE STRING "BS_PRODUCT_NAME variable defaulting")
set(BS_TARGET_DEVICE "1,2" CACHE STRING "BS_TARGET_DEVICE variable defaulting")
set(BS_ORIENTATION "<string>UIInterfaceOrientationPortrait</string>" CACHE STRING "BS_ORIENTATION variable defaulting")
set(BS_USE_ANALYTICS FALSE CACHE BOOL "BS_USE_ANALYTICS variable defaulting")
set(BS_USE_ADMOB FALSE CACHE BOOL "BS_USE_ADMOB variable defaulting")

project(BlueshiftPlayer)

set(COMMON_SOURCE_FILES
    Precompiled.h
    Precompiled.cpp
    Application.h
    Application.cpp)

set(WINDOWS_SOURCE_FILES
    WinMain.cpp
    WinResource.h
    Manifest.xml
    WinRes/player.rc
    WinRes/player.ico)

set(MACOS_SOURCE_FILES
    macOSMain.mm
    macOSMainMenu.xib)

set(ANDROID_SOURCE_FILES
    android_native_app_glue.h
    android_native_app_glue.c
    AndroidMain.cpp
    AndroidAnalytics.h
    AndroidAnalytics.cpp
    AndroidAdMob.h
    AndroidAdMob.cpp)

set(IOS_SOURCE_FILES
    iOSMain.mm
    iOSLaunchScreen.xib
    Assets.xcassets
    iOSAnalytics.h
    iOSAnalytics.mm
    iOSAdMob.h
    iOSAdMob.mm)

if (NOT PLATFORM_WINDOWS)
    list(APPEND COMPILING_DISABLED_SOURCES ${WINDOWS_SOURCE_FILES})
endif ()

if (NOT PLATFORM_MACOS)
    list(APPEND COMPILING_DISABLED_SOURCES ${MACOS_SOURCE_FILES})
endif ()

if (NOT PLATFORM_ANDROID)
    list(APPEND COMPILING_DISABLED_SOURCES ${ANDROID_SOURCE_FILES})
endif ()

if (NOT PLATFORM_IOS)
    list(APPEND COMPILING_DISABLED_SOURCES ${IOS_SOURCE_FILES})
endif ()

set_source_files_properties(${COMPILING_DISABLED_SOURCES} PROPERTIES HEADER_FILE_ONLY TRUE)

if (PLATFORM_WINDOWS)
    set_source_files_properties(${WINDOWS_SOURCE_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)
elseif (PLATFORM_MACOS)
    set_source_files_properties(${MACOS_SOURCE_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)
elseif (PLATFORM_ANDROID)
    set_source_files_properties(${ANDROID_SOURCE_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)

    if (NOT BS_USE_ANALYTICS)
        set_source_files_properties(AndroidAnalytics.h AndroidAnalytics.cpp PROPERTIES HEADER_FILE_ONLY TRUE)
    endif ()

    if (NOT BS_USE_ADMOB)
        set_source_files_properties(AndroidAdMob.h AndroidAdMob.cpp PROPERTIES HEADER_FILE_ONLY TRUE)
    endif ()
elseif (PLATFORM_IOS)
    set_source_files_properties(${IOS_SOURCE_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)

    if (NOT BS_USE_ANALYTICS)
        set_source_files_properties(iOSAnalytics.h iOSAnalytics.mm PROPERTIES HEADER_FILE_ONLY TRUE)
    endif ()

    if (NOT BS_USE_ADMOB)
        set_source_files_properties(iOSAdMob.h iOSAdMob.mm PROPERTIES HEADER_FILE_ONLY TRUE)
    endif ()
endif ()

set(ALL_FILES
    ${COMMON_SOURCE_FILES}
    ${WINDOWS_SOURCE_FILES}
    ${MACOS_SOURCE_FILES}
    ${ANDROID_SOURCE_FILES}
    ${IOS_SOURCE_FILES})

auto_source_group(${ALL_FILES})

include_directories(
    ${PROJECT_SOURCE_DIR}
    ${ENGINE_INCLUDE_DIR}/Runtime/Public
    ${ENGINE_INCLUDE_DIR}/ThirdParty)

enable_precompiled_header(Precompiled.h Precompiled.cpp ALL_FILES)

if (XAMARIN)
    add_library(${PROJECT_NAME} STATIC ${ALL_FILES})

    set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Blueshift)
    set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
    set_target_properties(${PROJECT_NAME} PROPERTIES DEBUG_POSTFIX "_d")
    set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
    set_target_properties(${PROJECT_NAME} PROPERTIES ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
    set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

    target_link_libraries(${PROJECT_NAME} 
        zlib
        minizip
        libjpeg
        libpng
        libpvrt
        etcpack_lib
        Etc2CompLib
        libogg
        libvorbis
        freetype
        jsoncpp
        Bullet
        HACD
        lua
        luasocket
        LuaCpp
        BlueshiftRuntime
    )
	if (ANDROID)
	    target_link_libraries(${PROJECT_NAME} nvidia)
	endif ()
else ()
    if (ANDROID)
        # Export ANativeActivity_onCreate(),
        # Refer to: https://github.com/android-ndk/ndk/issues/381.
        set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -u ANativeActivity_onCreate")

        add_library(${PROJECT_NAME} SHARED ${ALL_FILES})
    elseif (APPLE)
        if (USE_LUAJIT AND NOT IOS)
            set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pagezero_size 10000 -image_base 100000000")
        endif ()

        add_executable(${PROJECT_NAME} MACOSX_BUNDLE ${ALL_FILES})
    elseif (WIN32)
        add_executable(${PROJECT_NAME} WIN32 ${ALL_FILES})
    endif ()

    if (ANDROID OR IOS)
        if (BS_USE_ANALYTICS)
            add_definitions(-DUSE_ANALYTICS=1)
        endif ()

        if (BS_USE_ADMOB)
            add_definitions(-DUSE_ADMOB=1)
        endif ()
    else ()
        set_target_properties(${PROJECT_NAME} PROPERTIES
            PREFIX ""
            #DEBUG_POSTFIX "_d"
            OUTPUT_NAME ${PROJECT_NAME}
            RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Bin/${ENGINE_BUILD_PLATFORM_DIR})
    endif ()

    if (APPLE)
        # App name
        set(CMAKEVAR_APP_NAME ${BS_APP_NAME})
        # App version
        set(CMAKEVAR_BUNDLE_SHORT_VERSION_STRING ${BS_APP_VERSION})
        # Bundle version
        set(CMAKEVAR_BUNDLE_VERSION "1")
        # Orientation
        set(CMAKEVAR_ORIENTATION "${BS_ORIENTATION}")

        set_target_properties(${PROJECT_NAME} PROPERTIES 
            XCODE_ATTRIBUTE_PRODUCT_NAME ${BS_PRODUCT_NAME}
            XCODE_ATTRIBUTE_PRODUCT_BUNDLE_IDENTIFIER ${BS_APP_IDENTIFIER}
            XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "gnu++0x"
            XCODE_ATTRIBUTE_CLANG_CXX_LIBRARY "libc++"
            XCODE_ATTRIBUTE_CLANG_MODULES_AUTOLINK "NO"
            XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC "YES"
            XCODE_ATTRIBUTE_GCC_C_LANGUAGE_STANDARD "gnu99"
            #XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS NO
            #XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS[variant=Debug] YES
            XCODE_ATTRIBUTE_COPY_PHASE_STRIP YES
            XCODE_ATTRIBUTE_COPY_PHASE_STRIP[variant=Debug] NO
            XCODE_ATTRIBUTE_GCC_PREFIX_HEADER "${PROJECT_SOURCE_DIR}/Precompiled.h"
            XCODE_ATTRIBUTE_GCC_PRECOMPILE_PREFIX_HEADER "YES"
            XCODE_ATTRIBUTE_INSTALL_PATH "/Applications"
            XCODE_ATTRIBUTE_SKIP_INSTALL "NO")

        if (IOS)
            set_target_properties(${PROJECT_NAME} PROPERTIES 
                XCODE_ATTRIBUTE_IPHONEOS_DEPLOYMENT_TARGET ${IOS_DEPLOYMENT_TARGET}
                XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY ${BS_TARGET_DEVICE}
                XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "iPhone Developer"
                #XCODE_ATTRIBUTE_DEVELOPMENT_TEAM XXX
                XCODE_ATTRIBUTE_ASSETCATALOG_COMPILER_APPICON_NAME "AppIcon"
                MACOSX_BUNDLE_INFO_PLIST ${CMAKE_CURRENT_LIST_DIR}/iOSplist.in)

            set_source_files_properties(iOSLaunchScreen.xib Assets.xcassets PROPERTIES MACOSX_PACKAGE_LOCATION Resources)

            add_framework(${PROJECT_NAME} Foundation)
            add_framework(${PROJECT_NAME} UIKit)
            add_framework(${PROJECT_NAME} OpenGLES)
            add_framework(${PROJECT_NAME} CoreGraphics)
            add_framework(${PROJECT_NAME} QuartzCore)
            add_framework(${PROJECT_NAME} OpenAL)
            add_framework(${PROJECT_NAME} AudioToolbox)
            add_framework(${PROJECT_NAME} AVFoundation)

            if (BS_USE_ANALYTICS)
                set(GoogleAnalyticsServices ${ENGINE_INCLUDE_DIR}/ThirdParty/GoogleAnalyticsServices)

                if (${GoogleAnalyticsServices} STREQUAL GoogleAnalyticsServices-NOTFOUND)
                    message(ERROR ": GoogleAnalyticsServices folder not found")
                else ()
                    target_link_libraries(${PROJECT_NAME} ${GoogleAnalyticsServices}/libGoogleAnalyticsServices.a)

                    target_include_directories(${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${GoogleAnalyticsServices}/GoogleAnalytics/Library>)
                endif ()

                find_package(ZLIB REQUIRED)
                target_link_libraries(${PROJECT_NAME} ${ZLIB_LIBRARIES})

                find_library(SQLITE3_LIBRARY NAMES sqlite3)
                target_link_libraries(${PROJECT_NAME} ${SQLITE3_LIBRARY})

                add_framework(${PROJECT_NAME} CoreData)
                add_framework(${PROJECT_NAME} SystemConfiguration)
            endif ()
            
            if (BS_USE_ADMOB)
                set(GoogleMobileAds ${ENGINE_INCLUDE_DIR}/ThirdParty/GoogleMobileAds/GoogleMobileAds)

                if (${GoogleMobileAds} STREQUAL GoogleMobileAds-NOTFOUND)
                    message(ERROR ": Framework GoogleMobileAds not found")
                else ()
                    target_link_libraries(${PROJECT_NAME} ${GoogleMobileAds}.framework)

                    target_include_directories(${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${GoogleMobileAds}.framework/Headers>)
                endif ()

                add_framework(${PROJECT_NAME} AdSupport)
                add_framework(${PROJECT_NAME} CFNetwork)
                add_framework(${PROJECT_NAME} CoreMedia)
                add_framework(${PROJECT_NAME} CoreMotion)
                add_framework(${PROJECT_NAME} CoreTelephony)
                add_framework(${PROJECT_NAME} CoreVideo)
                add_framework(${PROJECT_NAME} GLKit)
                add_framework(${PROJECT_NAME} MessageUI)
                add_framework(${PROJECT_NAME} MediaPlayer)
                add_framework(${PROJECT_NAME} MobileCoreServices)
                add_framework(${PROJECT_NAME} Security)
                add_framework(${PROJECT_NAME} StoreKit)
                add_framework(${PROJECT_NAME} SystemConfiguration)
            endif ()
        else () # macOS
            set(CMAKEVAR_COPYRIGHT "Copyright (c) 2014 PolygonTek. All rights reserved.")

            set_target_properties(${PROJECT_NAME} PROPERTIES MACOSX_BUNDLE_INFO_PLIST ${CMAKE_CURRENT_LIST_DIR}/macOSplist.in)

            set_source_files_properties(macOSMainMenu.xib PROPERTIES MACOSX_PACKAGE_LOCATION Resources)

            add_framework(${PROJECT_NAME} Foundation)
            add_framework(${PROJECT_NAME} AppKit)
            add_framework(${PROJECT_NAME} Carbon)
            add_framework(${PROJECT_NAME} OpenGL)
            add_framework(${PROJECT_NAME} CoreGraphics)
            add_framework(${PROJECT_NAME} CoreVideo)
            add_framework(${PROJECT_NAME} OpenAL)
            add_framework(${PROJECT_NAME} AudioToolbox)
            add_framework(${PROJECT_NAME} AVFoundation)
        endif ()
    elseif (WIN32)
        find_package(OpenGL REQUIRED)
        target_link_libraries(${PROJECT_NAME} ${OPENGL_LIBRARIES} winmm.lib imm32.lib dxguid.lib dsound.lib ws2_32.lib)

        if (MSVC)
            set_target_properties(${PROJECT_NAME} PROPERTIES WIN32_EXECUTABLE YES)

            add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND "mt.exe" -nologo -manifest "${PROJECT_SOURCE_DIR}\\Manifest.xml" -outputresource:"$<TARGET_FILE:${PROJECT_NAME}>\;1"
                COMMENT "Adding manifest...")
        endif ()
    endif ()

    if (BUILD_RUNTIME)
        set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Blueshift)

        target_link_libraries(${PROJECT_NAME} BlueshiftRuntime)
    elseif (BUILD_PLAYER)
        set(THIRDPARTY_LIB_FILES
            zlib
            minizip
            libjpeg
            libpng
            libpvrt
            etcpack_lib
            Etc2CompLib
            libogg
            libvorbis
            freetype
            jsoncpp
            Bullet
            HACD
            LuaCpp
            luasocket)

        if (USE_LUAJIT)
            include(FindLuaJIT)
            target_link_libraries(${PROJECT_NAME} ${LUAJIT_LIBRARY})

            include_directories(${PROJECT_NAME} ${ENGINE_INCLUDE_DIR}/ThirdParty/luaJIT/src)
        else ()
            list(APPEND THIRDPARTY_LIB_FILES lua)

            include_directories(${PROJECT_NAME} ${ENGINE_INCLUDE_DIR}/ThirdParty/lua)
        endif ()

        set(IMPORTED_LIB_FILES ${THIRDPARTY_LIB_FILES} BlueshiftRuntime)

        if (ANDROID)
            target_link_libraries(${PROJECT_NAME} 
                android
                atomic
                log
                EGL
                GLESv3
                OpenSLES)

            foreach (FILE ${IMPORTED_LIB_FILES})
                add_library(${FILE} STATIC IMPORTED)

                set_target_properties(${FILE} PROPERTIES
                    IMPORTED_LOCATION ${ENGINE_LIBRARY_DIR}/${ENGINE_BUILD_PLATFORM_DIR}/${FILE}${CMAKE_STATIC_LIBRARY_SUFFIX})
            endforeach ()
        else ()
            foreach (FILE ${IMPORTED_LIB_FILES})
                add_library(${FILE} STATIC IMPORTED)

                message(STATUS ${ENGINE_LIBRARY_DIR}/${ENGINE_BUILD_PLATFORM_DIR}/Debug/${FILE}${CMAKE_STATIC_LIBRARY_SUFFIX})

                set_target_properties(${FILE} PROPERTIES
                    IMPORTED_LOCATION_DEBUG   ${ENGINE_LIBRARY_DIR}/${ENGINE_BUILD_PLATFORM_DIR}/Debug/${FILE}${CMAKE_STATIC_LIBRARY_SUFFIX}
                    IMPORTED_LOCATION_RELEASE ${ENGINE_LIBRARY_DIR}/${ENGINE_BUILD_PLATFORM_DIR}/Release/${FILE}${CMAKE_STATIC_LIBRARY_SUFFIX})
            endforeach ()
        endif ()
 
        if (APPLE)
            add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                #COMMAND rm -rf "\"$(TARGET_BUILD_DIR)/$(PRODUCT_NAME).app/Data\""
                COMMAND mkdir -p "\"$(PROJECT_DIR)/Scripts\""
                COMMAND cp -Rf "\"$(PROJECT_DIR)/Data\"" "\"$(TARGET_BUILD_DIR)/$(PRODUCT_NAME).app\""
                COMMAND cp -Rf "\"$(PROJECT_DIR)/Config\"" "\"$(TARGET_BUILD_DIR)/$(PRODUCT_NAME).app\""
                COMMENT "Copying data files"
                USES_TERMINAL)
        endif ()

        set_property(TARGET minizip PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES zlib)
        set_property(TARGET libpng PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES zlib)
        set_property(TARGET libvorbis PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES libogg)
        set_property(TARGET BlueshiftRuntime PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES ${THIRDPARTY_LIB_FILES})

        target_link_libraries(${PROJECT_NAME} ${THIRDPARTY_LIB_FILES} BlueshiftRuntime)
    endif ()
endif ()
cmake_minimum_required(VERSION 2.8.12)

project(BlueshiftRuntime)

configure_file(
    "${PROJECT_SOURCE_DIR}/Version.h.in"
    "${PROJECT_SOURCE_DIR}/Version.h")

set(COMMON_ENGINE_FILES
    Precompiled.h
    Precompiled.cpp

    Public/BlueshiftEngine.h

    Public/Core/Allocator.h
    Public/Core/BinSearch.h
    Public/Core/Checksum_CRC32.h
    Public/Core/Checksum_MD5.h
    Public/Core/Heap.h
    Public/Core/Range.h
    Public/Core/UTF.h
    Public/Core/Str.h
    Public/Core/Variant.h
    Public/Core/VariantArg.h
    Public/Core/Guid.h
    Public/Core/ByteOrder.h
    Public/Core/CmdArgs.h
    Public/Core/Cmds.h
    Public/Core/CVars.h
    Public/Core/Timespan.h
    Public/Core/DateTime.h
    Public/Core/MinMaxCurve.h
    Public/Core/Dict.h
    Public/Core/Expr.h
    Public/Core/Lexer.h
    Public/Core/Task.h
    Public/Core/Event.h
    Public/Core/Object.h
    Public/Core/Property.h
    Public/Core/ScopeLock.h
    Public/Core/Serializable.h
    Public/Core/Signal.h
    Public/Core/SignalObject.h
    Public/Core/DynamicAABBTree.h
    Public/Core/JointPose.h
    Public/Core/StrColor.h
    Public/Core/Vec4Color.h
    Public/Core/Vertex.h 

    Public/Containers/StaticArray.h
    Public/Containers/HashIndex.h
    Public/Containers/HashMap.h
    Public/Containers/HashTable.h
    Public/Containers/Hierarchy.h
    Public/Containers/LinkList.h
    Public/Containers/Array.h
    Public/Containers/Pair.h
    Public/Containers/Stack.h
    Public/Containers/Queue.h 
    Public/Containers/StrArray.h
    Public/Containers/StrPool.h
    Public/Containers/LinkedList.h

    Public/Image/Image.h 
    Public/Image/DxtCodec.h
    Public/Image/DxtDecoder.h
    Public/Image/DxtEncoder.h

    Public/Math/AABB.h
    Public/Math/Angles.h
    Public/Math/Complex.h
    Public/Math/Color.h
    Public/Math/Color3.h
    Public/Math/Color4.h
    Public/Math/CQuaternion.h
    Public/Math/Curve.h
    Public/Math/Hermite.h
    Public/Math/Cylinder.h
    Public/Math/FloatConverter.h
    Public/Math/Frustum.h
    Public/Math/Half.h
    Public/Math/Hammersley.h
    Public/Math/Math.h
    Public/Math/MathCommon.h
    Public/Math/Matrix.h
    Public/Math/Matrix2.h
    Public/Math/Matrix3.h
    Public/Math/Matrix3x4.h
    Public/Math/Matrix4.h
    Public/Math/OBB.h
    Public/Math/Plane.h
    Public/Math/Pluecker.h
    Public/Math/Point.h
    Public/Math/Quaternion.h
    Public/Math/Random.h
    Public/Math/Ray.h
    Public/Math/Rect.h
    Public/Math/RGBE9995.h
    Public/Math/Rotation.h
    Public/Math/Sphere.h
    Public/Math/SphericalHarmonics.h
    Public/Math/Vector.h
    Public/Math/Vector2.h
    Public/Math/Vector3.h
    Public/Math/Vector4.h

    Public/Simd/Simd.h
    Public/Simd/Simd_AVX.h
    Public/Simd/Simd_Generic.h
    Public/Simd/Simd_SSE4.h
    Public/Simd/smmintrin_emu.h
    Public/Simd/immintrin_emu.h
    Public/Simd/AVX/avx.h
    Public/Simd/AVX/avxb.h
    Public/Simd/AVX/avxf.h
    Public/Simd/AVX/avxi.h
    Public/Simd/SSE/sse.h
    Public/Simd/SSE/sseb.h
    Public/Simd/SSE/ssef.h
    Public/Simd/SSE/ssei.h

    Public/Platform/cpuid.h
    Public/Platform/Intrinsics.h
    Public/Platform/PlatformAtomic.h
    Public/Platform/PlatformProcess.h
    Public/Platform/PlatformFile.h
    Public/Platform/PlatformThread.h
    Public/Platform/PlatformTLS.h
    Public/Platform/PlatformTime.h
    Public/Platform/PlatformSystem.h

    Public/File/File.h
    Public/File/FileSystem.h
    Public/File/ZipArchiver.h
  
    Public/RHI/RHI.h
    Public/RHI/RHIOpenGL.h

    Public/Engine/Common.h
    Public/Engine/GameClient.h
    Public/Engine/Console.h
    Public/Engine/Engine.h

    Public/Asset/Asset.h
    Public/Asset/AssetImporter.h
    Public/Asset/GuidMapper.h

    Public/AnimController/AnimBlendTree.h
    Public/AnimController/AnimClip.h
    Public/AnimController/AnimLayer.h
    Public/AnimController/AnimState.h
    Public/AnimController/AnimController.h

    Public/Animator/Animator.h
    Public/Animator/AnimStateBlender.h

    Public/Components/ComAnimation.h
    Public/Components/ComAnimator.h
    Public/Components/ComAudioListener.h
    Public/Components/ComAudioSource.h
    Public/Components/ComBoxCollider.h
    Public/Components/ComCamera.h
    Public/Components/ComCapsuleCollider.h
    Public/Components/ComCharacterController.h
    Public/Components/ComCharacterJoint.h
    Public/Components/ComCollider.h
    Public/Components/ComConeCollider.h
    Public/Components/ComConstantForce.h
    Public/Components/ComCylinderCollider.h
    Public/Components/ComFixedJoint.h
    Public/Components/ComHingeJoint.h
    Public/Components/ComJoint.h
    Public/Components/ComLight.h
    Public/Components/ComEnvironmentProbe.h
    Public/Components/ComLogic.h
    Public/Components/ComScript.h
    Public/Components/ComMeshCollider.h
    Public/Components/ComMeshRenderer.h
    Public/Components/ComTextRenderer.h
    Public/Components/Component.h
    Public/Components/ComParticleSystem.h
    Public/Components/ComRenderable.h
    Public/Components/ComRigidBody.h
    Public/Components/ComSensor.h
    Public/Components/ComSkinnedMeshRenderer.h
    Public/Components/ComSliderJoint.h
    Public/Components/ComSocketJoint.h
    Public/Components/ComSphereCollider.h
    Public/Components/ComSpline.h
    Public/Components/ComSpringJoint.h
    Public/Components/ComStaticMeshRenderer.h
    Public/Components/ComTransform.h
    Public/Components/ComWheelJoint.h
    Public/Components/ComVehicleWheel.h

    Public/Game/Entity.h
    Public/Game/Prefab.h
    Public/Game/MapRenderSettings.h
    Public/Game/GameWorld.h
    Public/Game/CastResult.h
    Public/Game/GameSettings.h
    Public/Game/TagLayerSettings.h
    Public/Game/PhysicsSettings.h
    Public/Game/PlayerSettings.h

    Public/StaticBatching/StaticBatch.h
    
    Public/Physics/Collider.h
    Public/Physics/Physics.h
    Public/Physics/PhysicsCollidable.h
    Public/Physics/PhysicsCollisionListener.h
    Public/Physics/PhysicsConstraint.h
    Public/Physics/PhysicsGenericConstraint.h
    Public/Physics/PhysicsGenericSpringConstraint.h
    Public/Physics/PhysicsHingeConstraint.h
    Public/Physics/PhysicsP2PConstraint.h
    Public/Physics/PhysicsSliderConstraint.h
    Public/Physics/PhysicsRigidBody.h
    Public/Physics/PhysicsSensor.h
    Public/Physics/PhysicsSystem.h
    Public/Physics/PhysicsVehicle.h
    Public/Physics/PhysicsWorld.h

    Public/Sound/Pcm.h
    Public/Sound/SoundSystem.h

    Public/Render/Anim.h
    Public/Render/BufferCache.h
    Public/Render/SkinningJointCache.h
    Public/Render/Font.h
    Public/Render/ParticleMesh.h
    Public/Render/GuiMesh.h
    Public/Render/Material.h
    Public/Render/Mesh.h
    Public/Render/Render.h
    Public/Render/RenderSystem.h
    Public/Render/RenderContext.h  
    Public/Render/ParticleSystem.h
    Public/Render/EnvProbe.h
    Public/Render/RenderObject.h
    Public/Render/RenderLight.h
    Public/Render/RenderCamera.h
    Public/Render/RenderWorld.h
    Public/Render/Shader.h
    Public/Render/Skeleton.h
    Public/Render/Skin.h
    Public/Render/SubMesh.h
    Public/Render/Texture.h

    Public/Platform/Platform.h

    Public/Input/InputSystem.h
    Public/Input/KeyCmd.h
    Public/Input/KeyCodes.h

    Public/Scripting/LuaVM.h

    Public/Profiler/Profiler.h

    Private/Core/Checksum_CRC32.cpp
    Private/Core/Checksum_MD5.cpp
    Private/Core/Heap.cpp
    Private/Core/UTF8.cpp
    Private/Core/UTF16.cpp
    Private/Core/Str.cpp
    Private/Core/Guid.cpp
    Private/Core/ByteOrder.cpp
    Private/Core/CmdArgs.cpp
    Private/Core/Cmds.cpp
    Private/Core/CVars.cpp
    Private/Core/Timespan.cpp
    Private/Core/DateTime.cpp
    Private/Core/Dict.cpp
    Private/Core/Expr.cpp
    Private/Core/MinMaxCurve.cpp
    Private/Core/Lexer.cpp
    Private/Core/Task.cpp
    Private/Core/Variant.cpp
    Private/Core/DynamicAABBTree.cpp
    Private/Core/Vec4Color.cpp

    Private/Containers/HashIndex.cpp

    Private/Image/ImageInternal.h
    Private/Image/Image.cpp
    Private/Image/ImageColorSpace.cpp
    Private/Image/ImageConvert.cpp
    Private/Image/ImageCompressDXT.cpp
    Private/Image/ImageCompressETC.cpp
    Private/Image/ImageDecompressDXT.cpp
    Private/Image/ImageDecompressPVRTC.cpp
    Private/Image/ImageDecompressETC.cpp
    Private/Image/ImageFile.cpp
    Private/Image/ImageFileBMP.cpp
    Private/Image/ImageFileDDS.cpp
    Private/Image/ImageFilePVR.cpp
    Private/Image/ImageFileHDR.cpp
    Private/Image/ImageFileJPG.cpp
    Private/Image/ImageFilePCX.cpp
    Private/Image/ImageFilePNG.cpp
    Private/Image/ImageFileTGA.cpp
    Private/Image/ImageFormat.cpp
    Private/Image/ImageProcess.cpp
    Private/Image/ImageResize.cpp
    Private/Image/DXTDecoder.cpp
    Private/Image/DXTEncoder.cpp

    Private/Math/Vector3.cpp
    Private/Math/Vector4.cpp
    Private/Math/Color3.cpp
    Private/Math/Color4.cpp
    Private/Math/RGBE9995.cpp
    Private/Math/AABB.cpp
    Private/Math/Frustum.cpp
    Private/Math/Matrix4.cpp
    Private/Math/Quaternion.cpp
    Private/Math/Angles.cpp
    Private/Math/Half.cpp
    Private/Math/OBB.cpp
    Private/Math/Ray.cpp
    Private/Math/Rect.cpp
    Private/Math/CQuaternion.cpp
    Private/Math/SphericalHarmonics.cpp
    Private/Math/Math.cpp
    Private/Math/Plane.cpp
    Private/Math/Rotation.cpp
    Private/Math/Complex.cpp
    Private/Math/Matrix2.cpp
    Private/Math/Matrix3x4.cpp
    Private/Math/Pluecker.cpp
    Private/Math/Sphere.cpp
    Private/Math/Cylinder.cpp
    Private/Math/Matrix3.cpp
    Private/Math/Point.cpp
    Private/Math/Vector2.cpp

    Private/SIMD/Simd.cpp
    Private/SIMD/Simd_AVX.cpp
    Private/SIMD/Simd_Generic.cpp
    Private/SIMD/Simd_SSE4.cpp

    Private/Platform/cpuid.cpp
    Private/Platform/PlatformBaseProcess.cpp
    Private/Platform/PlatformBaseFile.cpp
    Private/Platform/PlatformBaseThread.cpp
    Private/Platform/PlatformBaseTLS.cpp
    Private/Platform/PlatformBaseTime.cpp
    Private/Platform/PlatformBaseSystem.cpp

    Private/File/File.cpp
    Private/File/FileSystem.cpp
    Private/File/ZipArchiver.cpp

    Private/RHIOpenGL/OpenGL/OpenGL.h
    Private/RHIOpenGL/OpenGL/OpenGL.cpp
    Private/RHIOpenGL/RGLInternal.h
    Private/RHIOpenGL/RGLBuffer.cpp
    Private/RHIOpenGL/RGLCommon.cpp
    Private/RHIOpenGL/RGLQuery.cpp
    Private/RHIOpenGL/RGLRenderTarget.cpp
    Private/RHIOpenGL/RGLShader.cpp
    Private/RHIOpenGL/RGLState.cpp
    Private/RHIOpenGL/RGLSync.cpp
    Private/RHIOpenGL/RGLTexture.cpp
    Private/RHIOpenGL/RGLVertexFormat.cpp

    Private/Engine/Common.cpp
    Private/Engine/GameClient.cpp
    Private/Engine/Console.cpp
    Private/Engine/Engine.cpp

    Private/Asset/Asset.cpp
    Private/Asset/FolderAsset.cpp
    Private/Asset/FbxAsset.cpp
    Private/Asset/TextureAsset.cpp
    Private/Asset/ShaderAsset.cpp
    Private/Asset/MaterialAsset.cpp
    Private/Asset/FontAsset.cpp
    Private/Asset/MeshAsset.cpp
    Private/Asset/ParticleSystemAsset.cpp
    Private/Asset/SkeletonAsset.cpp
    Private/Asset/AnimAsset.cpp
    Private/Asset/JointMaskAsset.cpp
    Private/Asset/AnimControllerAsset.cpp
    Private/Asset/ScriptAsset.cpp
    Private/Asset/PrefabAsset.cpp
    Private/Asset/SoundAsset.cpp
    Private/Asset/MapAsset.cpp
    Private/Asset/AssetImporter.cpp
    Private/Asset/GuidMapper.cpp
  
    Private/AnimController/AnimBlendTree.cpp
    Private/AnimController/AnimClip.cpp
    Private/AnimController/AnimLayer.cpp
    Private/AnimController/AnimState.cpp
    Private/AnimController/AnimController.cpp

    Private/Animator/Animator.cpp
    Private/Animator/AnimStateBlender.cpp
  
    Private/Components/ComAnimation.cpp
    Private/Components/ComAnimator.cpp
    Private/Components/ComAudioListener.cpp
    Private/Components/ComAudioSource.cpp
    Private/Components/ComBoxCollider.cpp  
    Private/Components/ComCamera.cpp
    Private/Components/ComCapsuleCollider.cpp
    Private/Components/ComCharacterController.cpp
    Private/Components/ComCharacterJoint.cpp
    Private/Components/ComCollider.cpp
    Private/Components/ComConeCollider.cpp
    Private/Components/ComConstantForce.cpp
    Private/Components/ComCylinderCollider.cpp
    Private/Components/ComFixedJoint.cpp
    Private/Components/ComHingeJoint.cpp
    Private/Components/ComJoint.cpp
    Private/Components/ComLight.cpp
    Private/Components/ComEnvironmentProbe.cpp
    Private/Components/ComLogic.cpp
    Private/Components/ComScript.cpp
    Private/Components/ComMeshCollider.cpp
    Private/Components/ComMeshRenderer.cpp
    Private/Components/ComTextRenderer.cpp
    Private/Components/Component.cpp
    Private/Components/ComParticleSystem.cpp
    Private/Components/ComRenderable.cpp
    Private/Components/ComRigidBody.cpp
    Private/Components/ComSensor.cpp
    Private/Components/ComSkinnedMeshRenderer.cpp
    Private/Components/ComSliderJoint.cpp
    Private/Components/ComSocketJoint.cpp
    Private/Components/ComSphereCollider.cpp
    Private/Components/ComSpline.cpp
    Private/Components/ComSpringJoint.cpp
    Private/Components/ComStaticMeshRenderer.cpp
    Private/Components/ComTransform.cpp
    Private/Components/ComWheelJoint.cpp
    Private/Components/ComVehicleWheel.cpp

    Private/Game/Entity.cpp
    Private/Game/Prefab.cpp
    Private/Game/PrefabManager.cpp
    Private/Game/MapRenderSettings.cpp
    Private/Game/GameWorld.cpp
    Private/Game/CastResult.cpp  
    Private/Game/GameSettings.cpp
    Private/Game/TagLayerSettings.cpp
    Private/Game/PhysicsSettings.cpp
    Private/Game/PlayerSettings.cpp

    Private/StaticBatching/MeshCombiner.h
    Private/StaticBatching/MeshCombiner.cpp
    Private/StaticBatching/StaticBatch.cpp

    Private/Core/Event.cpp
    Private/Core/Object.cpp
    Private/Core/Serializable.cpp
    Private/Core/Signal.cpp
    Private/Core/SignalObject.cpp

    Private/Physics/ColliderInternal.h
    Private/Physics/PhysicsCVars.h
    Private/Physics/PhysicsInternal.h
    Private/Physics/Collider.cpp
    Private/Physics/ColliderManager.cpp
    Private/Physics/PhysicsCollidable.cpp
    Private/Physics/PhysicsCollisionListener.cpp
    Private/Physics/PhysicsConstraint.cpp
    Private/Physics/PhysicsCVars.cpp
    Private/Physics/PhysicsDebugDraw.cpp
    Private/Physics/PhysicsGenericConstraint.cpp
    Private/Physics/PhysicsGenericSpringConstraint.cpp
    Private/Physics/PhysicsHingeConstraint.cpp
    Private/Physics/PhysicsP2PConstraint.cpp
    Private/Physics/PhysicsSliderConstraint.cpp
    Private/Physics/PhysicsRigidBody.cpp
    Private/Physics/PhysicsSensor.cpp
    Private/Physics/PhysicsSystem.cpp
    Private/Physics/PhysicsVehicle.cpp
    Private/Physics/PhysicsWorld.cpp

    Private/Sound/Pcm.cpp
    Private/Sound/Pcm_DecodeWav.cpp
    Private/Sound/Pcm_DecodeOgg.cpp
    Private/Sound/Sound.cpp
    Private/Sound/SoundSystem.cpp

    Private/Render/BModel.h
    Private/Render/Anim.cpp
    Private/Render/Anim_banim.cpp
    Private/Render/Anim_optimize.cpp
    Private/Render/AnimManager.cpp
    Private/Render/BufferCache.cpp
    Private/Render/SkinningJointCache.cpp
    Private/Render/ParticleMesh.cpp
    Private/Render/GuiMesh.cpp
    Private/Render/Material.cpp
    Private/Render/MaterialManager.cpp
    Private/Render/Mesh.cpp
    Private/Render/Mesh_bmesh.cpp
    Private/Render/Mesh_CreateMesh.cpp
    Private/Render/Mesh_SortAndMerge.cpp
    Private/Render/MeshManager.cpp
    Private/Render/RenderSystem.cpp
    Private/Render/RenderContext.cpp
    Private/Render/ParticleSystem.cpp
    Private/Render/ParticleSystemManager.cpp
    Private/Render/EnvProbe.cpp
    Private/Render/RenderObject.cpp
    Private/Render/RenderLight.cpp
    Private/Render/RenderCamera.cpp
    Private/Render/RenderWorld.cpp
    Private/Render/RenderWorldDrawCamera.cpp
    Private/Render/RenderWorldDebugTools.cpp
    Private/Render/Shader.cpp
    Private/Render/ShaderManager.cpp
    Private/Render/Skeleton.cpp
    Private/Render/SkeletonManager.cpp
    Private/Render/Skin.cpp
    Private/Render/SkinManager.cpp
    Private/Render/SubMesh.cpp
    Private/Render/Texture.cpp
    Private/Render/TextureManager.cpp
    Private/Render/FontFace.h
    Private/Render/Font.cpp
    Private/Render/FontManager.cpp
    Private/Render/FontFaceBitmap.cpp
    Private/Render/FontFaceFreeType.cpp
    Private/Render/DrawSurf.h
    Private/Render/FrameData.h
    Private/Render/RBackEnd.h
    Private/Render/RenderCmd.h
    Private/Render/RenderCVars.h
    Private/Render/RenderInternal.h
    Private/Render/RenderPostProcess.h
    Private/Render/RenderTarget.h
    Private/Render/RenderUtils.h
    Private/Render/Simplex.h
    Private/Render/VertexFormat.h
    Private/Render/FrameData.cpp
    Private/Render/RB_DebugTools.cpp
    Private/Render/RB_DrawSimple.cpp
    Private/Render/RB_Main.cpp
    Private/Render/RB_GenericPass.cpp
    Private/Render/RB_ShadowPass.cpp
    Private/Render/RB_ForwardBasePass.cpp
    Private/Render/RB_ForwardAdditivePass.cpp
    Private/Render/RB_PostProcess.cpp
    Private/Render/RB_Batch.cpp
    Private/Render/RB_BatchRender.cpp
    Private/Render/RenderCVars.cpp
    Private/Render/RenderPostProcess.cpp
    Private/Render/RenderTarget.cpp
    Private/Render/RenderUtils.cpp
    Private/Render/VertexFormat.cpp  

    Private/Platform/Platform.cpp
    Private/Platform/PlatformGeneric.h
    Private/Platform/PlatformGeneric.cpp

    Private/Input/InputSystem.cpp
    Private/Input/KeyCmd.cpp

    Private/Scripting/LuaVM.cpp
    Private/Scripting/Math/LuaModule_Math.cpp
    Private/Scripting/Math/LuaModule_Complex.cpp
    Private/Scripting/Math/LuaModule_Vec2.cpp
    Private/Scripting/Math/LuaModule_Vec3.cpp
    Private/Scripting/Math/LuaModule_Vec4.cpp
    Private/Scripting/Math/LuaModule_Color3.cpp
    Private/Scripting/Math/LuaModule_Color4.cpp
    Private/Scripting/Math/LuaModule_Mat2.cpp
    Private/Scripting/Math/LuaModule_Mat3.cpp
    Private/Scripting/Math/LuaModule_Mat3x4.cpp
    Private/Scripting/Math/LuaModule_Mat4.cpp
    Private/Scripting/Math/LuaModule_Quaternion.cpp
    Private/Scripting/Math/LuaModule_Angles.cpp
    Private/Scripting/Math/LuaModule_Rotation.cpp
    Private/Scripting/Math/LuaModule_Plane.cpp
    Private/Scripting/Math/LuaModule_Sphere.cpp
    Private/Scripting/Math/LuaModule_Cylinder.cpp
    Private/Scripting/Math/LuaModule_AABB.cpp
    Private/Scripting/Math/LuaModule_OBB.cpp
    Private/Scripting/Math/LuaModule_Frustum.cpp
    Private/Scripting/Math/LuaModule_Ray.cpp
    Private/Scripting/Math/LuaModule_Point.cpp
    Private/Scripting/Math/LuaModule_Rect.cpp
    Private/Scripting/Engine/LuaModule_Common.cpp
    Private/Scripting/Input/LuaModule_InputSystem.cpp
    Private/Scripting/Screen/LuaModule_Screen.cpp
    Private/Scripting/Physics/LuaModule_Physics.cpp
    Private/Scripting/Core/LuaModule_Str.cpp
    Private/Scripting/Core/LuaModule_Guid.cpp
    Private/Scripting/Core/LuaModule_Object.cpp
    Private/Scripting/File/LuaModule_FileSystem.cpp
    Private/Scripting/File/LuaModule_File.cpp
    Private/Scripting/Asset/LuaModule_Asset.cpp
    Private/Scripting/Asset/LuaModule_TextureAsset.cpp
    Private/Scripting/Asset/LuaModule_ShaderAsset.cpp
    Private/Scripting/Asset/LuaModule_MaterialAsset.cpp
    Private/Scripting/Asset/LuaModule_SkeletonAsset.cpp
    Private/Scripting/Asset/LuaModule_MeshAsset.cpp
    Private/Scripting/Asset/LuaModule_AnimAsset.cpp
    Private/Scripting/Asset/LuaModule_AnimControllerAsset.cpp
    Private/Scripting/Asset/LuaModule_SoundAsset.cpp
    Private/Scripting/Asset/LuaModule_MapAsset.cpp
    Private/Scripting/Asset/LuaModule_PrefabAsset.cpp
    Private/Scripting/Components/LuaModule_Component.cpp
    Private/Scripting/Components/LuaModule_ComTransform.cpp
    Private/Scripting/Components/LuaModule_ComCollider.cpp
    Private/Scripting/Components/LuaModule_ComBoxCollider.cpp
    Private/Scripting/Components/LuaModule_ComSphereCollider.cpp
    Private/Scripting/Components/LuaModule_ComCylinderCollider.cpp
    Private/Scripting/Components/LuaModule_ComCapsuleCollider.cpp
    Private/Scripting/Components/LuaModule_ComMeshCollider.cpp
    Private/Scripting/Components/LuaModule_ComRigidBody.cpp
    Private/Scripting/Components/LuaModule_ComSensor.cpp
    Private/Scripting/Components/LuaModule_ComJoint.cpp
    Private/Scripting/Components/LuaModule_ComFixedJoint.cpp
    Private/Scripting/Components/LuaModule_ComHingeJoint.cpp
    Private/Scripting/Components/LuaModule_ComSocketJoint.cpp
    Private/Scripting/Components/LuaModule_ComSliderJoint.cpp
    Private/Scripting/Components/LuaModule_ComSpringJoint.cpp
    Private/Scripting/Components/LuaModule_ComWheelJoint.cpp
    Private/Scripting/Components/LuaModule_ComCharacterJoint.cpp
    Private/Scripting/Components/LuaModule_ComConstantForce.cpp
    Private/Scripting/Components/LuaModule_ComCharacterController.cpp
    Private/Scripting/Components/LuaModule_ComRenderable.cpp
    Private/Scripting/Components/LuaModule_ComMeshRenderer.cpp
    Private/Scripting/Components/LuaModule_ComStaticMeshRenderer.cpp
    Private/Scripting/Components/LuaModule_ComSkinnedMeshRenderer.cpp
    Private/Scripting/Components/LuaModule_ComAnimation.cpp
    Private/Scripting/Components/LuaModule_ComAnimator.cpp
    Private/Scripting/Components/LuaModule_ComTextRenderer.cpp
    Private/Scripting/Components/LuaModule_ComParticleSystem.cpp
    Private/Scripting/Components/LuaModule_ComLight.cpp
    Private/Scripting/Components/LuaModule_ComCamera.cpp
    Private/Scripting/Components/LuaModule_ComAudioListener.cpp
    Private/Scripting/Components/LuaModule_ComAudioSource.cpp
    Private/Scripting/Components/LuaModule_ComSpline.cpp
    Private/Scripting/Components/LuaModule_ComScript.cpp
    Private/Scripting/Components/LuaModule_ComVehicleWheel.cpp
    Private/Scripting/Game/LuaModule_Entity.cpp
    Private/Scripting/Game/LuaModule_GameWorld.cpp

    Private/Profiler/Profiler.cpp)

set(WINDOWS_ENGINE_FILES
    Public/Platform/Windows/PlatformWinProcess.h
    Public/Platform/Windows/PlatformWinFile.h
    Public/Platform/Windows/PlatformWinThread.h
    Public/Platform/Windows/PlatformWinTLS.h
    Public/Platform/Windows/PlatformWinTime.h
    Public/Platform/Windows/PlatformWinSystem.h
    Public/Platform/Windows/PlatformWinUtils.h

    Private/Platform/Windows/PlatformWinProcess.cpp
    Private/Platform/Windows/PlatformWinFile.cpp
    Private/Platform/Windows/PlatformWinThread.cpp
    Private/Platform/Windows/PlatformWinTLS.cpp
    Private/Platform/Windows/PlatformWinTime.cpp
    Private/Platform/Windows/PlatformWinSystem.cpp
    Private/Platform/Windows/PlatformWinUtils.cpp

    Private/Platform/PlatformWin.h
    Private/Platform/PlatformWin.cpp

    Public/Network/Socket.h
    Public/Network/Packet.h
    Private/Network/Socket.cpp
    Private/Network/Packet.cpp

    Private/Sound/SoundSystemAL.cpp
    Private/Sound/SoundBufferAL.cpp
    Private/Sound/SoundSourceAL.cpp
    
    Private/Sound/SoundSystemDS.cpp
    Private/Sound/SoundBufferDS.cpp
    Private/Sound/SoundSourceDS.cpp)

set(ANDROID_ENGINE_FILES
    Public/Platform/Posix/PlatformPosixProcess.h
    Public/Platform/Posix/PlatformPosixTLS.h
    Public/Platform/Posix/PlatformPosixTime.h
    Public/Platform/Linux/PlatformLinuxProcess.h
    Public/Platform/Linux/PlatformLinuxTime.h
    Public/Platform/Android/PlatformAndroidProcess.h
    Public/Platform/Android/PlatformAndroidSystem.h
    Public/Platform/Android/PlatformAndroidThread.h
    Public/Platform/Android/PlatformAndroidFile.h

    Private/Platform/Posix/PlatformPosixProcess.cpp
    Private/Platform/Posix/PlatformPosixTLS.cpp
    Private/Platform/Posix/PlatformPosixTime.cpp
    Private/Platform/Linux/PlatformLinuxProcess.cpp
    Private/Platform/Linux/PlatformLinuxTime.cpp
    Private/Platform/Android/PlatformAndroidProcess.cpp 
    Private/Platform/Android/PlatformAndroidSystem.cpp 
    Private/Platform/Android/PlatformAndroidThread.cpp
    Private/Platform/Android/PlatformAndroidFile.cpp
    Private/Platform/PlatformAndroid.h
    Private/Platform/PlatformAndroid.cpp

    Public/PlatformUtils/Android/AndroidJNI.h
    Public/PlatformUtils/Android/AndroidGPUInfo.h

    Private/PlatformUtils/Android/AndroidJNI.cpp
    Private/PlatformUtils/Android/AndroidGPUInfo.cpp

    Private/Sound/SoundSystemSLES.cpp
    Private/Sound/SoundBufferSLES.cpp
    Private/Sound/SoundSourceSLES.cpp)

set(UNIX_ENGINE_FILES
    Public/Platform/Posix/PlatformPosixProcess.h
    Public/Platform/Posix/PlatformPosixFile.h
    Public/Platform/Posix/PlatformPosixThread.h
    Public/Platform/Posix/PlatformPosixTLS.h
    Public/Platform/Posix/PlatformPosixTime.h
    Public/Platform/Posix/PlatformPosixSystem.h

    Private/Platform/Posix/PlatformPosixProcess.cpp
    Private/Platform/Posix/PlatformPosixFile.cpp
    Private/Platform/Posix/PlatformPosixThread.cpp
    Private/Platform/Posix/PlatformPosixTLS.cpp
    Private/Platform/Posix/PlatformPosixTime.cpp
    Private/Platform/Posix/PlatformPosixSystem.cpp

    Private/Sound/SoundSystemAL.cpp
    Private/Sound/SoundBufferAL.cpp
    Private/Sound/SoundSourceAL.cpp)

set(LINUX_ENGINE_FILES
    ${UNIX_ENGINE_FILES}
    Public/Platform/Linux/PlatformLinuxProcess.h
    Public/Platform/Linux/PlatformLinuxThread.h
    Private/Platform/Linux/PlatformLinuxProcess.cpp
    Private/Platform/Linux/PlatformLinuxThread.cpp)

set(APPLE_ENGINE_FILES
    ${UNIX_ENGINE_FILES}
    Public/Platform/Apple/PlatformAppleTime.h
    Public/Platform/Apple/PlatformAppleProcess.h
    Public/Platform/Apple/PlatformAppleSystem.h
    Public/Platform/Apple/PlatformAppleThread.h

    Private/Platform/Apple/PlatformAppleTime.cpp
    Private/Platform/Apple/PlatformAppleProcess.mm
    Private/Platform/Apple/PlatformAppleSystem.mm
    Private/Platform/Apple/PlatformAppleThread.cpp)
    
set(IOS_ENGINE_FILES
    ${APPLE_ENGINE_FILES}
    Public/Platform/IOS/PlatformIOSFile.h
    Public/Platform/IOS/PlatformIOSProcess.h
    Public/Platform/IOS/PlatformIOSSystem.h

    Private/Platform/IOS/PlatformIOSFile.mm
    Private/Platform/IOS/PlatformIOSProcess.mm
    Private/Platform/IOS/PlatformIOSSystem.mm
    Private/Platform/PlatformIOS.h
    Private/Platform/PlatformIOS.mm

    Public/PlatformUtils/iOS/iOSDevice.h
    Private/PlatformUtils/iOS/iOSDevice.mm)

set(MACOS_ENGINE_FILES
    ${APPLE_ENGINE_FILES}
    Public/Platform/MacOS/PlatformMacOSProcess.h
    Public/Platform/MacOS/PlatformMacOSSystem.h

    Private/Platform/MacOS/PlatformMacOSProcess.mm
    Private/Platform/MacOS/PlatformMacOSSystem.mm
    Private/Platform/PlatformMacOS.h
    Private/Platform/PlatformMacOS.mm

    Public/Network/Socket.h
    Public/Network/Packet.h
    Private/Network/Socket.cpp
    Private/Network/Packet.cpp)

set(WINDOWS_RENDERER_FILES
    Private/RHIOpenGL/OpenGL/GGL/gglcore32.c
    Private/RHIOpenGL/OpenGL/GGL/gglcore32.h
    Private/RHIOpenGL/OpenGL/GGL/gwgl.c
    Private/RHIOpenGL/OpenGL/GGL/gwgl.h
    Private/RHIOpenGL/OpenGL/OpenGL3.h
    Private/RHIOpenGL/OpenGL/OpenGL3.cpp
    Private/RHIOpenGL/OpenGL/OpenGL4.h
    Private/RHIOpenGL/OpenGL/OpenGL4.cpp
    Private/RHIOpenGL/OpenGL/WinOpenGL.h
    Private/RHIOpenGL/RGLPlatformWin.cpp)

set(ANDROID_RENDERER_FILES
    Private/RHIOpenGL/OpenGL/GGL/ggles3.c
    Private/RHIOpenGL/OpenGL/GGL/ggles3.h
    Private/RHIOpenGL/OpenGL/GGL/gegl.c
    Private/RHIOpenGL/OpenGL/GGL/gegl.h
    Private/RHIOpenGL/OpenGL/OpenGLES3.h
    Private/RHIOpenGL/OpenGL/OpenGLES3.cpp
    Private/RHIOpenGL/OpenGL/AndroidOpenGL.h
    Private/RHIOpenGL/OpenGL/AndroidOpenGL.cpp
    Private/RHIOpenGL/RGLPlatformAndroid.cpp)

set(IOS_RENDERER_FILES
    Private/RHIOpenGL/OpenGL/GGL/ggles3.c
    Private/RHIOpenGL/OpenGL/GGL/ggles3.h
    Private/RHIOpenGL/OpenGL/OpenGLES3.h
    Private/RHIOpenGL/OpenGL/OpenGLES3.cpp
    Private/RHIOpenGL/OpenGL/IOSOpenGL.h
    Private/RHIOpenGL/OpenGL/IOSOpenGL.mm
    Private/RHIOpenGL/RGLPlatformIOS.mm)

set(MACOS_RENDERER_FILES
    Private/RHIOpenGL/OpenGL/GGL/gglcore32.c
    Private/RHIOpenGL/OpenGL/GGL/gglcore32.h
    Private/RHIOpenGL/OpenGL/OpenGL3.h
    Private/RHIOpenGL/OpenGL/OpenGL3.cpp
    Private/RHIOpenGL/OpenGL/MacOSOpenGL.h
    Private/RHIOpenGL/RGLPlatformMacOS.mm)

if (NOT PLATFORM_WINDOWS)
    list(APPEND COMPILING_DISABLED_SOURCES ${WINDOWS_ENGINE_FILES} ${WINDOWS_RENDERER_FILES})
endif ()

if (NOT PLATFORM_MACOS)
    list(APPEND COMPILING_DISABLED_SOURCES ${MACOS_ENGINE_FILES} ${MACOS_RENDERER_FILES})
endif ()

if (NOT PLATFORM_LINUX)
    list(APPEND COMPILING_DISABLED_SOURCES ${LINUX_ENGINE_FILES})
endif ()

if (NOT PLATFORM_ANDROID)
    list(APPEND COMPILING_DISABLED_SOURCES ${ANDROID_ENGINE_FILES} ${ANDROID_RENDERER_FILES})
endif ()

if (NOT PLATFORM_IOS)
    list(APPEND COMPILING_DISABLED_SOURCES ${IOS_ENGINE_FILES} ${IOS_RENDERER_FILES})
endif ()

set_source_files_properties(${COMPILING_DISABLED_SOURCES} PROPERTIES HEADER_FILE_ONLY TRUE)

if (PLATFORM_WINDOWS)
    set_source_files_properties(${WINDOWS_ENGINE_FILES} ${WINDOWS_RENDERER_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)

    if (NOT USE_WINDOWS_OPENAL)
        set_source_files_properties(
            Private/Sound/SoundSystemAL.cpp 
            Private/Sound/SoundBufferAL.cpp
            Private/Sound/SoundSourceAL.cpp PROPERTIES HEADER_FILE_ONLY TRUE)
    else ()
        set_source_files_properties(
            Private/Sound/SoundSystemDS.cpp
            Private/Sound/SoundBufferDS.cpp
            Private/Sound/SoundSourceDS.cpp PROPERTIES HEADER_FILE_ONLY TRUE)
    endif ()
elseif (PLATFORM_MACOS)
    set_source_files_properties(${MACOS_ENGINE_FILES} ${MACOS_RENDERER_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)
elseif (PLATFORM_LINUX)
    set_source_files_properties(${LINUX_ENGINE_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)
elseif (PLATFORM_ANDROID)
    set_source_files_properties(${ANDROID_ENGINE_FILES} ${ANDROID_RENDERER_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)
elseif (PLATFORM_IOS)
    set_source_files_properties(${IOS_ENGINE_FILES} ${IOS_RENDERER_FILES} PROPERTIES HEADER_FILE_ONLY FALSE)
endif ()

set(ENGINE_FILES
    ${COMMON_ENGINE_FILES}
    ${WINDOWS_ENGINE_FILES}
    ${ANDROID_ENGINE_FILES}
    ${LINUX_ENGINE_FILES}
    ${MACOS_ENGINE_FILES}
    ${IOS_ENGINE_FILES})

set(RENDERER_FILES
    ${WINDOWS_RENDERER_FILES}
    ${ANDROID_RENDERER_FILES}
    ${IOS_RENDERER_FILES}
    ${MACOS_RENDERER_FILES})

set(ALL_FILES
    ${ENGINE_FILES}
    ${RENDERER_FILES})

auto_source_group(${ALL_FILES})

include_directories(
    ${PROJECT_SOURCE_DIR}
    ${ENGINE_INCLUDE_DIR}/Runtime/Public
    ${ENGINE_INCLUDE_DIR}/ThirdParty
    ${ENGINE_INCLUDE_DIR}/ThirdParty/asio/include)

enable_precompiled_header(Precompiled.h Precompiled.cpp ENGINE_FILES)

if (PLATFORM_ANDROID)
    include_directories(${ANDROID_NDK}/sources/android/cpufeatures)
    set(CPU_FEATURES_FILE ${ANDROID_NDK}/sources/android/cpufeatures/cpu-features.c)

    add_library(${PROJECT_NAME} STATIC ${ALL_FILES} ${CPU_FEATURES_FILE})

    target_link_libraries(${PROJECT_NAME}
        android
        atomic
        log
        EGL
        GLESv3
        OpenSLES)
else ()
    add_library(${PROJECT_NAME} STATIC ${ALL_FILES})
endif ()

if (APPLE)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "gnu++0x"
        XCODE_ATTRIBUTE_CLANG_CXX_LIBRARY "libc++"
        XCODE_ATTRIBUTE_CLANG_MODULES_AUTOLINK "NO"
        XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC "YES"
        #XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS NO
        #XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS[variant=Debug] YES
        #XCODE_ATTRIBUTE_GCC_PREFIX_HEADER ${CMAKE_CURRENT_LIST_DIR}/Precompiled.h
        #XCODE_ATTRIBUTE_GCC_PRECOMPILE_PREFIX_HEADER "YES"
        XCODE_ATTRIBUTE_GCC_C_LANGUAGE_STANDARD "gnu99") 

    if (WITHDEBUG)
        set_target_properties(${PROJECT_NAME} PROPERTIES XCODE_ATTRIBUTE_COPY_PHASE_STRIP NO)
    else ()
        set_target_properties(${PROJECT_NAME} PROPERTIES
            XCODE_ATTRIBUTE_COPY_PHASE_STRIP YES
            XCODE_ATTRIBUTE_COPY_PHASE_STRIP[variant=Debug] NO)
    endif ()

    if (IOS)
        include_directories(${ENGINE_INCLUDE_DIR}/ThirdParty/OpenGL/include)

        set_target_properties(${PROJECT_NAME} PROPERTIES
            XCODE_ATTRIBUTE_IPHONEOS_DEPLOYMENT_TARGET ${IOS_DEPLOYMENT_TARGET}
            XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2") # Universal (iPad + iPhone)

        add_framework(${PROJECT_NAME} Foundation)
        add_framework(${PROJECT_NAME} UIKit)
        add_framework(${PROJECT_NAME} OpenGLES)
        add_framework(${PROJECT_NAME} CoreGraphics)
        add_framework(${PROJECT_NAME} QuartzCore)
    elseif (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
        add_framework(${PROJECT_NAME} Carbon)
        add_framework(${PROJECT_NAME} Foundation)
        add_framework(${PROJECT_NAME} AppKit)
        add_framework(${PROJECT_NAME} OpenGL)
        add_framework(${PROJECT_NAME} CoreGraphics)
        add_framework(${PROJECT_NAME} CoreVideo)
    endif ()

    add_framework(${PROJECT_NAME} OpenAL)
elseif (WIN32)
    target_link_libraries(${PROJECT_NAME} ws2_32)

    if (USE_DESKTOP_EGL)
        include(FindOpenGLES3)
        include(FindEGL)

        include_directories(${ENGINE_INCLUDE_DIR}/ThirdParty/OpenGL/include)

        find_library(OPENGLES3_LIBRARY GLESv2)
        find_library(EGL_LIBRARY EGL)

        target_link_libraries(${PROJECT_NAME} ${EGL_LIBRARY} ${OPENGLES3_LIBRARY})
    else ()
        find_package(OpenGL REQUIRED)

        target_link_libraries(${PROJECT_NAME} ${OPENGL_LIBRARIES})
    endif ()

    if (USE_WINDOWS_OPENAL)
        include(FindOpenAL)
    
        target_include_directories(${PROJECT_NAME} PUBLIC ${OPENAL_INCLUDE_DIR})
        target_link_libraries(${PROJECT_NAME} ${OPENAL_LIBRARY})
    else ()
        target_link_libraries(${PROJECT_NAME} dxguid dsound)
    endif ()
endif ()

target_link_libraries(${PROJECT_NAME} 
    zlib
    minizip
    libjpeg
    libpng
    libpvrt
    etcpack_lib
    Etc2CompLib
    libogg
    libvorbis
    jsoncpp
    tinyxml2
    freetype
    Bullet
    HACD
    luasocket
    LuaCpp
    NvTriStrip)

if (USE_LUAJIT)
    target_include_directories(${PROJECT_NAME} PUBLIC ${ENGINE_INCLUDE_DIR}/ThirdParty/luaJIT/src)

    include(FindLuaJIT)
    target_link_libraries(${PROJECT_NAME} ${LUAJIT_LIBRARY})
else ()
    target_include_directories(${PROJECT_NAME} PUBLIC ${ENGINE_INCLUDE_DIR}/ThirdParty/lua)

    target_link_libraries(${PROJECT_NAME} lua)
endif ()

set_target_properties(${PROJECT_NAME} PROPERTIES
    FOLDER "Blueshift"
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

project(TestBase)

set(ALL_FILES
    Main.cpp
    TestContainer.h
    TestContainer.cpp
    TestMath.h
    TestMath.cpp
    TestSIMD.h
    TestSIMD.cpp
    TestCUDA.h
    TestCUDA.cpp
    TestLua.h
    TestLua.cpp)

auto_source_group(${ALL_FILES})

include_directories(
    ${PROJECT_SOURCE_DIR}
    ${ENGINE_INCLUDE_DIR}/Runtime/Public
    ${ENGINE_INCLUDE_DIR}/ThirdParty
)

if (ANDROID)
    # Export ANativeActivity_onCreate(),
    # Refer to: https://github.com/android-ndk/ndk/issues/381.
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -u ANativeActivity_onCreate")

    add_library(${PROJECT_NAME} SHARED ${ALL_FILES})
else ()
    add_executable(${PROJECT_NAME} ${ALL_FILES})
endif ()

target_link_libraries(${PROJECT_NAME} BlueshiftRuntime LuaCpp)

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Test)

if (USE_LUAJIT)
    if (APPLE AND NOT IOS)
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pagezero_size 10000 -image_base 100000000")
    endif ()
endif ()

if (NOT IOS)
    set_target_properties(${PROJECT_NAME} PROPERTIES 
        PREFIX ""
        #DEBUG_POSTFIX "_d"
        OUTPUT_NAME ${PROJECT_NAME}
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Bin/${ENGINE_BUILD_PLATFORM_DIR})
endif ()

if (WIN32)
    target_link_libraries(${PROJECT_NAME} winmm.lib)
endif ()
cmake_minimum_required(VERSION 2.8.12)

project(TestRenderer)

set(ALL_FILES
    Precompiled.h
    Precompiled.cpp
    Application.h
    Application.cpp)

if (ANDROID)
    list(APPEND ALL_FILES
        android_native_app_glue.h
        android_native_app_glue.c
        AndroidMain.cpp)
elseif (APPLE)
    if (IOS)
        list(APPEND ALL_FILES
            iOSMain.mm
            iOSLaunchScreen.xib)
    else ()
        list(APPEND ALL_FILES
            macOSMain.mm
            macOSMainMenu.xib)
    endif ()
elseif (WIN32)
    list(APPEND ALL_FILES
        WinMain.cpp
        WinResource.h
        WinRes/small.ico
        WinRes/TestRenderer.ico
        WinRes/TestRenderer.rc)
endif ()

auto_source_group(${ALL_FILES})

include_directories(
    ${PROJECT_SOURCE_DIR}
    ${ENGINE_INCLUDE_DIR}/Runtime/Public
    ${ENGINE_INCLUDE_DIR}/ThirdParty)

enable_precompiled_header(Precompiled.h Precompiled.cpp ALL_FILES)

if (ANDROID)
    # Export ANativeActivity_onCreate(),
    # Refer to: https://github.com/android-ndk/ndk/issues/381.
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -u ANativeActivity_onCreate")

    add_library(${PROJECT_NAME} SHARED ${ALL_FILES})
elseif (APPLE)
    add_executable(${PROJECT_NAME} MACOSX_BUNDLE ${ALL_FILES})
elseif (WIN32)
    add_executable(${PROJECT_NAME} WIN32 ${ALL_FILES})
endif ()

if (NOT ANDROID AND NOT IOS)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        PREFIX ""
        #DEBUG_POSTFIX "_d"
        OUTPUT_NAME ${PROJECT_NAME}
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Bin/${ENGINE_BUILD_PLATFORM_DIR})
endif ()

if (ANDROID)
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E remove_directory "\"${CMAKE_SOURCE_DIR}/Bin/Android/Assets\""
        COMMAND ${CMAKE_COMMAND} -E copy_directory "\"${CMAKE_SOURCE_DIR}/Data\"" "\"${CMAKE_SOURCE_DIR}/Bin/Android/Assets/Data\""
        COMMENT Copying asset files)
elseif (APPLE)
    # App name
    set(CMAKEVAR_APP_NAME "Test Renderer")
    # App version
    set(CMAKEVAR_BUNDLE_SHORT_VERSION_STRING "1.0")
    # Bundle version
    set(CMAKEVAR_BUNDLE_VERSION "1")

    set_target_properties(${PROJECT_NAME} PROPERTIES 
        XCODE_ATTRIBUTE_PRODUCT_NAME "TestRenderer"
        XCODE_ATTRIBUTE_PRODUCT_BUNDLE_IDENTIFIER "com.polygontek.TestRenderer"
        XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "gnu++0x"
        XCODE_ATTRIBUTE_CLANG_CXX_LIBRARY "libc++"
        XCODE_ATTRIBUTE_CLANG_MODULES_AUTOLINK "NO"
        XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC "YES"
        XCODE_ATTRIBUTE_GCC_C_LANGUAGE_STANDARD "gnu99"
        #XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS NO
        #XCODE_ATTRIBUTE_GCC_GENERATE_DEBUGGING_SYMBOLS[variant=Debug] YES
        XCODE_ATTRIBUTE_COPY_PHASE_STRIP YES
        XCODE_ATTRIBUTE_COPY_PHASE_STRIP[variant=Debug] NO
        #XCODE_ATTRIBUTE_GCC_PREFIX_HEADER ${CMAKE_CURRENT_LIST_DIR}/Precompiled.h
        #XCODE_ATTRIBUTE_GCC_PRECOMPILE_PREFIX_HEADER "YES"
        XCODE_ATTRIBUTE_INSTALL_PATH "/Applications"
        XCODE_ATTRIBUTE_SKIP_INSTALL "NO")

    if (IOS)
        set_target_properties(${PROJECT_NAME} PROPERTIES 
            XCODE_ATTRIBUTE_IPHONEOS_DEPLOYMENT_TARGET ${IOS_DEPLOYMENT_TARGET}
            XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2" # Universal (iPad + iPhone)
            XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "iPhone Developer"
            MACOSX_BUNDLE_INFO_PLIST ${CMAKE_CURRENT_LIST_DIR}/iOSplist.in)

        add_framework(${PROJECT_NAME} Foundation)
        add_framework(${PROJECT_NAME} UIKit)
    else ()
        set(CMAKEVAR_COPYRIGHT "Copyright (c) 2014 PolygonTek. All rights reserved.")

        set_target_properties(${PROJECT_NAME} PROPERTIES MACOSX_BUNDLE_INFO_PLIST ${CMAKE_CURRENT_LIST_DIR}/macOSplist.in)

        set_source_files_properties(macOSMainMenu.xib PROPERTIES MACOSX_PACKAGE_LOCATION Resources)

        add_framework(${PROJECT_NAME} Foundation)
        add_framework(${PROJECT_NAME} AppKit)
    endif ()

    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND rm -rf "\"$(TARGET_BUILD_DIR)/$(PRODUCT_NAME).app/Data\""
        COMMAND cp -Rf "\"$(PROJECT_DIR)/Data\"" "\"$(TARGET_BUILD_DIR)/$(PRODUCT_NAME).app/Data\""
        COMMENT Copying data files)
elseif (WIN32)
    target_link_libraries(${PROJECT_NAME} winmm.lib)

    if (MSVC)
        set_target_properties(${PROJECT_NAME} PROPERTIES WIN32_EXECUTABLE YES)
    endif ()
endif ()

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER Test)

target_link_libraries(${PROJECT_NAME} BlueshiftRuntime)
http://think-async.com/Asio/

asio-1.10.6cmake_minimum_required(VERSION 2.8.12)

project(Bullet)

if (MSVC)
    option(USE_MSVC_FAST_FLOATINGPOINT "Use MSVC /fp:fast option"	ON)
    if (USE_MSVC_FAST_FLOATINGPOINT)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /fp:fast")
    endif()
ENDIF()

if (WIN32)
    ADD_DEFINITIONS(-D_CRT_SECURE_NO_WARNINGS)
    ADD_DEFINITIONS(-D_CRT_SECURE_NO_DEPRECATE)
    ADD_DEFINITIONS(-D_SCL_SECURE_NO_WARNINGS)
endif()

set(SRC_FILES
    src/btBulletCollisionCommon.h
    src/btBulletDynamicsCommon.h

    src/BulletCollision/BroadphaseCollision/btAxisSweep3.h
    src/BulletCollision/BroadphaseCollision/btAxisSweep3.cpp
    src/BulletCollision/BroadphaseCollision/btAxisSweep3Internal.h
    src/BulletCollision/BroadphaseCollision/btBroadphaseInterface.h
    src/BulletCollision/BroadphaseCollision/btBroadphaseProxy.h
    src/BulletCollision/BroadphaseCollision/btBroadphaseProxy.cpp
    src/BulletCollision/BroadphaseCollision/btCollisionAlgorithm.h
    src/BulletCollision/BroadphaseCollision/btCollisionAlgorithm.cpp
    src/BulletCollision/BroadphaseCollision/btDbvt.h
    src/BulletCollision/BroadphaseCollision/btDbvt.cpp
    src/BulletCollision/BroadphaseCollision/btDbvtBroadphase.h
    src/BulletCollision/BroadphaseCollision/btDbvtBroadphase.cpp
    src/BulletCollision/BroadphaseCollision/btDispatcher.h
    src/BulletCollision/BroadphaseCollision/btDispatcher.cpp
    src/BulletCollision/BroadphaseCollision/btOverlappingPairCache.h
    src/BulletCollision/BroadphaseCollision/btOverlappingPairCache.cpp
    src/BulletCollision/BroadphaseCollision/btOverlappingPairCallback.h
    src/BulletCollision/BroadphaseCollision/btQuantizedBvh.h
    src/BulletCollision/BroadphaseCollision/btQuantizedBvh.cpp
    src/BulletCollision/BroadphaseCollision/btSimpleBroadphase.h
    src/BulletCollision/BroadphaseCollision/btSimpleBroadphase.cpp

    src/BulletCollision/CollisionDispatch/btActivatingCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btActivatingCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btBox2dBox2dCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btBox2dBox2dCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btBoxBoxCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btBoxBoxCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btBoxBoxDetector.h
    src/BulletCollision/CollisionDispatch/btBoxBoxDetector.cpp
    src/BulletCollision/CollisionDispatch/btCollisionConfiguration.h
    src/BulletCollision/CollisionDispatch/btCollisionCreateFunc.h
    src/BulletCollision/CollisionDispatch/btCollisionDispatcher.h
    src/BulletCollision/CollisionDispatch/btCollisionDispatcher.cpp
    src/BulletCollision/CollisionDispatch/btCollisionDispatcherMt.h
    src/BulletCollision/CollisionDispatch/btCollisionDispatcherMt.cpp
    src/BulletCollision/CollisionDispatch/btCollisionObject.h
    src/BulletCollision/CollisionDispatch/btCollisionObject.cpp
    src/BulletCollision/CollisionDispatch/btCollisionObjectWrapper.h
    src/BulletCollision/CollisionDispatch/btCollisionWorld.h
    src/BulletCollision/CollisionDispatch/btCollisionWorld.cpp
    src/BulletCollision/CollisionDispatch/btCollisionWorldImporter.cpp
    src/BulletCollision/CollisionDispatch/btCompoundCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btCompoundCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btCompoundCompoundCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btCompoundCompoundCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btConvex2dConvex2dAlgorithm.h
    src/BulletCollision/CollisionDispatch/btConvex2dConvex2dAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btConvexConcaveCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btConvexConcaveCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btConvexConvexAlgorithm.h
    src/BulletCollision/CollisionDispatch/btConvexConvexAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btConvexPlaneCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btConvexPlaneCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btDefaultCollisionConfiguration.h
    src/BulletCollision/CollisionDispatch/btDefaultCollisionConfiguration.cpp
    src/BulletCollision/CollisionDispatch/btEmptyCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btEmptyCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btGhostObject.h
    src/BulletCollision/CollisionDispatch/btGhostObject.cpp
    src/BulletCollision/CollisionDispatch/btHashedSimplePairCache.h
    src/BulletCollision/CollisionDispatch/btHashedSimplePairCache.cpp
    src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.h
    src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.cpp
    src/BulletCollision/CollisionDispatch/btManifoldResult.h
    src/BulletCollision/CollisionDispatch/btManifoldResult.cpp
    src/BulletCollision/CollisionDispatch/btSimulationIslandManager.h
    src/BulletCollision/CollisionDispatch/btSimulationIslandManager.cpp
    src/BulletCollision/CollisionDispatch/btSphereBoxCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btSphereBoxCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btSphereSphereCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btSphereSphereCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btSphereTriangleCollisionAlgorithm.h
    src/BulletCollision/CollisionDispatch/btSphereTriangleCollisionAlgorithm.cpp
    src/BulletCollision/CollisionDispatch/btUnionFind.h
    src/BulletCollision/CollisionDispatch/btUnionFind.cpp
    src/BulletCollision/CollisionDispatch/SphereTriangleDetector.h
    src/BulletCollision/CollisionDispatch/SphereTriangleDetector.cpp

    src/BulletCollision/CollisionShapes/btBox2dShape.h
    src/BulletCollision/CollisionShapes/btBox2dShape.cpp
    src/BulletCollision/CollisionShapes/btBoxShape.h
    src/BulletCollision/CollisionShapes/btBoxShape.cpp
    src/BulletCollision/CollisionShapes/btBvhTriangleMeshShape.h
    src/BulletCollision/CollisionShapes/btBvhTriangleMeshShape.cpp
    src/BulletCollision/CollisionShapes/btCapsuleShape.h
    src/BulletCollision/CollisionShapes/btCapsuleShape.cpp
    src/BulletCollision/CollisionShapes/btCollisionMargin.h
    src/BulletCollision/CollisionShapes/btCollisionShape.h
    src/BulletCollision/CollisionShapes/btCollisionShape.cpp
    src/BulletCollision/CollisionShapes/btCompoundShape.h
    src/BulletCollision/CollisionShapes/btCompoundShape.cpp
    src/BulletCollision/CollisionShapes/btConcaveShape.h
    src/BulletCollision/CollisionShapes/btConcaveShape.cpp
    src/BulletCollision/CollisionShapes/btConeShape.h
    src/BulletCollision/CollisionShapes/btConeShape.cpp
    src/BulletCollision/CollisionShapes/btConvex2dShape.h
    src/BulletCollision/CollisionShapes/btConvex2dShape.cpp
    src/BulletCollision/CollisionShapes/btConvexHullShape.h
    src/BulletCollision/CollisionShapes/btConvexHullShape.cpp
    src/BulletCollision/CollisionShapes/btConvexInternalShape.h
    src/BulletCollision/CollisionShapes/btConvexInternalShape.cpp
    src/BulletCollision/CollisionShapes/btConvexPointCloudShape.h
    src/BulletCollision/CollisionShapes/btConvexPointCloudShape.cpp
    src/BulletCollision/CollisionShapes/btConvexPolyhedron.h
    src/BulletCollision/CollisionShapes/btConvexPolyhedron.cpp
    src/BulletCollision/CollisionShapes/btConvexShape.h
    src/BulletCollision/CollisionShapes/btConvexShape.cpp
    src/BulletCollision/CollisionShapes/btConvexTriangleMeshShape.h
    src/BulletCollision/CollisionShapes/btConvexTriangleMeshShape.cpp
    src/BulletCollision/CollisionShapes/btCylinderShape.h
    src/BulletCollision/CollisionShapes/btCylinderShape.cpp
    src/BulletCollision/CollisionShapes/btEmptyShape.h
    src/BulletCollision/CollisionShapes/btEmptyShape.cpp
    src/BulletCollision/CollisionShapes/btHeightfieldTerrainShape.h
    src/BulletCollision/CollisionShapes/btHeightfieldTerrainShape.cpp
    src/BulletCollision/CollisionShapes/btMaterial.h
    src/BulletCollision/CollisionShapes/btMiniSDF.h
    src/BulletCollision/CollisionShapes/btMiniSDF.cpp
    src/BulletCollision/CollisionShapes/btMinkowskiSumShape.h
    src/BulletCollision/CollisionShapes/btMinkowskiSumShape.cpp
    src/BulletCollision/CollisionShapes/btMultimaterialTriangleMeshShape.h
    src/BulletCollision/CollisionShapes/btMultimaterialTriangleMeshShape.cpp
    src/BulletCollision/CollisionShapes/btMultiSphereShape.h
    src/BulletCollision/CollisionShapes/btMultiSphereShape.cpp
    src/BulletCollision/CollisionShapes/btOptimizedBvh.h
    src/BulletCollision/CollisionShapes/btOptimizedBvh.cpp
    src/BulletCollision/CollisionShapes/btPolyhedralConvexShape.h
    src/BulletCollision/CollisionShapes/btPolyhedralConvexShape.cpp
    src/BulletCollision/CollisionShapes/btScaledBvhTriangleMeshShape.h
    src/BulletCollision/CollisionShapes/btScaledBvhTriangleMeshShape.cpp
    src/BulletCollision/CollisionShapes/btSdfCollisionShape.h
    src/BulletCollision/CollisionShapes/btSdfCollisionShape.cpp
    src/BulletCollision/CollisionShapes/btShapeHull.h
    src/BulletCollision/CollisionShapes/btShapeHull.cpp
    src/BulletCollision/CollisionShapes/btSphereShape.h
    src/BulletCollision/CollisionShapes/btSphereShape.cpp
    src/BulletCollision/CollisionShapes/btStaticPlaneShape.h
    src/BulletCollision/CollisionShapes/btStaticPlaneShape.cpp
    src/BulletCollision/CollisionShapes/btStridingMeshInterface.h
    src/BulletCollision/CollisionShapes/btStridingMeshInterface.cpp
    src/BulletCollision/CollisionShapes/btTetrahedronShape.h
    src/BulletCollision/CollisionShapes/btTetrahedronShape.cpp
    src/BulletCollision/CollisionShapes/btTriangleBuffer.h
    src/BulletCollision/CollisionShapes/btTriangleBuffer.cpp
    src/BulletCollision/CollisionShapes/btTriangleCallback.h
    src/BulletCollision/CollisionShapes/btTriangleCallback.cpp
    src/BulletCollision/CollisionShapes/btTriangleIndexVertexArray.h
    src/BulletCollision/CollisionShapes/btTriangleIndexVertexArray.cpp
    src/BulletCollision/CollisionShapes/btTriangleIndexVertexMaterialArray.h
    src/BulletCollision/CollisionShapes/btTriangleIndexVertexMaterialArray.cpp
    src/BulletCollision/CollisionShapes/btTriangleInfoMap.h
    src/BulletCollision/CollisionShapes/btTriangleMesh.h
    src/BulletCollision/CollisionShapes/btTriangleMesh.cpp
    src/BulletCollision/CollisionShapes/btTriangleMeshShape.h
    src/BulletCollision/CollisionShapes/btTriangleMeshShape.cpp
    src/BulletCollision/CollisionShapes/btTriangleShape.h
    src/BulletCollision/CollisionShapes/btUniformScalingShape.cpp
    src/BulletCollision/CollisionShapes/btUniformScalingShape.h

    src/BulletCollision/Gimpact/btBoxCollision.h
    src/BulletCollision/Gimpact/btClipPolygon.h
    src/BulletCollision/Gimpact/btCompoundFromGimpact.h
    src/BulletCollision/Gimpact/btContactProcessing.h
    src/BulletCollision/Gimpact/btContactProcessing.cpp
    src/BulletCollision/Gimpact/btContactProcessingStructs.h
    src/BulletCollision/Gimpact/btGenericPoolAllocator.h
    src/BulletCollision/Gimpact/btGenericPoolAllocator.cpp
    src/BulletCollision/Gimpact/btGeometryOperations.h
    src/BulletCollision/Gimpact/btGImpactBvh.h
    src/BulletCollision/Gimpact/btGImpactBvh.cpp
    src/BulletCollision/Gimpact/btGImpactCollisionAlgorithm.h
    src/BulletCollision/Gimpact/btGImpactCollisionAlgorithm.cpp
    src/BulletCollision/Gimpact/btGImpactMassUtil.h
    src/BulletCollision/Gimpact/btGImpactQuantizedBvh.h
    src/BulletCollision/Gimpact/btGImpactQuantizedBvh.cpp
    src/BulletCollision/Gimpact/btGImpactQuantizedBvhStructs.h
    src/BulletCollision/Gimpact/btGImpactShape.h
    src/BulletCollision/Gimpact/btGImpactShape.cpp
    src/BulletCollision/Gimpact/btQuantization.h
    src/BulletCollision/Gimpact/btTriangleShapeEx.h
    src/BulletCollision/Gimpact/btTriangleShapeEx.cpp
    src/BulletCollision/Gimpact/gim_array.h
    src/BulletCollision/Gimpact/gim_basic_geometry_operations.h
    src/BulletCollision/Gimpact/gim_bitset.h
    src/BulletCollision/Gimpact/gim_box_collision.h
    src/BulletCollision/Gimpact/gim_box_set.h
    src/BulletCollision/Gimpact/gim_box_set.cpp
    src/BulletCollision/Gimpact/gim_clip_polygon.h
    src/BulletCollision/Gimpact/gim_contact.h
    src/BulletCollision/Gimpact/gim_contact.cpp
    src/BulletCollision/Gimpact/gim_geom_types.h
    src/BulletCollision/Gimpact/gim_geometry.h
    src/BulletCollision/Gimpact/gim_hash_table.h
    src/BulletCollision/Gimpact/gim_linear_math.h
    src/BulletCollision/Gimpact/gim_math.h
    src/BulletCollision/Gimpact/gim_memory.h
    src/BulletCollision/Gimpact/gim_memory.cpp
    src/BulletCollision/Gimpact/gim_radixsort.h
    src/BulletCollision/Gimpact/gim_tri_collision.h
    src/BulletCollision/Gimpact/gim_tri_collision.cpp

    src/BulletCollision/NarrowPhaseCollision/btComputeGjkEpaPenetration.h
    src/BulletCollision/NarrowPhaseCollision/btContinuousConvexCollision.h
    src/BulletCollision/NarrowPhaseCollision/btContinuousConvexCollision.cpp
    src/BulletCollision/NarrowPhaseCollision/btConvexCast.h
    src/BulletCollision/NarrowPhaseCollision/btConvexCast.cpp
    src/BulletCollision/NarrowPhaseCollision/btConvexPenetrationDepthSolver.h
    src/BulletCollision/NarrowPhaseCollision/btDiscreteCollisionDetectorInterface.h
    src/BulletCollision/NarrowPhaseCollision/btGjkCollisionDescription.h
    src/BulletCollision/NarrowPhaseCollision/btGjkConvexCast.h
    src/BulletCollision/NarrowPhaseCollision/btGjkConvexCast.cpp
    src/BulletCollision/NarrowPhaseCollision/btGjkEpa2.h
    src/BulletCollision/NarrowPhaseCollision/btGjkEpa2.cpp
    src/BulletCollision/NarrowPhaseCollision/btGjkEpa3.h
    src/BulletCollision/NarrowPhaseCollision/btGjkEpaPenetrationDepthSolver.h
    src/BulletCollision/NarrowPhaseCollision/btGjkEpaPenetrationDepthSolver.cpp
    src/BulletCollision/NarrowPhaseCollision/btGjkPairDetector.h
    src/BulletCollision/NarrowPhaseCollision/btGjkPairDetector.cpp
    src/BulletCollision/NarrowPhaseCollision/btManifoldPoint.h
    src/BulletCollision/NarrowPhaseCollision/btMinkowskiPenetrationDepthSolver.h
    src/BulletCollision/NarrowPhaseCollision/btMinkowskiPenetrationDepthSolver.cpp
    src/BulletCollision/NarrowPhaseCollision/btPersistentManifold.h
    src/BulletCollision/NarrowPhaseCollision/btPersistentManifold.cpp
    src/BulletCollision/NarrowPhaseCollision/btPointCollector.h
    src/BulletCollision/NarrowPhaseCollision/btPolyhedralContactClipping.h
    src/BulletCollision/NarrowPhaseCollision/btPolyhedralContactClipping.cpp
    src/BulletCollision/NarrowPhaseCollision/btRaycastCallback.h
    src/BulletCollision/NarrowPhaseCollision/btRaycastCallback.cpp
    src/BulletCollision/NarrowPhaseCollision/btSimplexSolverInterface.h
    src/BulletCollision/NarrowPhaseCollision/btSubSimplexConvexCast.h
    src/BulletCollision/NarrowPhaseCollision/btSubSimplexConvexCast.cpp
    src/BulletCollision/NarrowPhaseCollision/btVoronoiSimplexSolver.h
    src/BulletCollision/NarrowPhaseCollision/btVoronoiSimplexSolver.cpp

    src/BulletDynamics/Character/btCharacterControllerInterface.h
    src/BulletDynamics/Character/btKinematicCharacterController.h
    src/BulletDynamics/Character/btKinematicCharacterController.cpp

    src/BulletDynamics/ConstraintSolver/btBatchedConstraints.h
    src/BulletDynamics/ConstraintSolver/btBatchedConstraints.cpp
    src/BulletDynamics/ConstraintSolver/btConeTwistConstraint.h
    src/BulletDynamics/ConstraintSolver/btConeTwistConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btConstraintSolver.h
    src/BulletDynamics/ConstraintSolver/btContactConstraint.h
    src/BulletDynamics/ConstraintSolver/btContactConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btContactSolverInfo.h
    src/BulletDynamics/ConstraintSolver/btFixedConstraint.h
    src/BulletDynamics/ConstraintSolver/btFixedConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btGearConstraint.h
    src/BulletDynamics/ConstraintSolver/btGearConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btGeneric6DofConstraint.h
    src/BulletDynamics/ConstraintSolver/btGeneric6DofConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btGeneric6DofSpring2Constraint.h
    src/BulletDynamics/ConstraintSolver/btGeneric6DofSpring2Constraint.cpp
    src/BulletDynamics/ConstraintSolver/btGeneric6DofSpringConstraint.h
    src/BulletDynamics/ConstraintSolver/btGeneric6DofSpringConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btHinge2Constraint.h
    src/BulletDynamics/ConstraintSolver/btHinge2Constraint.cpp
    src/BulletDynamics/ConstraintSolver/btHingeConstraint.h
    src/BulletDynamics/ConstraintSolver/btHingeConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btJacobianEntry.h
    src/BulletDynamics/ConstraintSolver/btNNCGConstraintSolver.h
    src/BulletDynamics/ConstraintSolver/btNNCGConstraintSolver.cpp
    src/BulletDynamics/ConstraintSolver/btPoint2PointConstraint.h
    src/BulletDynamics/ConstraintSolver/btPoint2PointConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btSequentialImpulseConstraintSolver.h
    src/BulletDynamics/ConstraintSolver/btSequentialImpulseConstraintSolver.cpp
    src/BulletDynamics/ConstraintSolver/btSequentialImpulseConstraintSolverMt.h
    src/BulletDynamics/ConstraintSolver/btSequentialImpulseConstraintSolverMt.cpp
    src/BulletDynamics/ConstraintSolver/btSliderConstraint.h
    src/BulletDynamics/ConstraintSolver/btSliderConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btSolve2LinearConstraint.h
    src/BulletDynamics/ConstraintSolver/btSolve2LinearConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btSolverBody.h
    src/BulletDynamics/ConstraintSolver/btSolverConstraint.h
    src/BulletDynamics/ConstraintSolver/btTypedConstraint.h
    src/BulletDynamics/ConstraintSolver/btTypedConstraint.cpp
    src/BulletDynamics/ConstraintSolver/btUniversalConstraint.h
    src/BulletDynamics/ConstraintSolver/btUniversalConstraint.cpp

    src/BulletDynamics/Dynamics/btActionInterface.h
    src/BulletDynamics/Dynamics/btDiscreteDynamicsWorld.h
    src/BulletDynamics/Dynamics/btDiscreteDynamicsWorld.cpp
    src/BulletDynamics/Dynamics/btDiscreteDynamicsWorldMt.h
    src/BulletDynamics/Dynamics/btDiscreteDynamicsWorldMt.cpp
    src/BulletDynamics/Dynamics/btDynamicsWorld.h
    src/BulletDynamics/Dynamics/btRigidBody.h
    src/BulletDynamics/Dynamics/btRigidBody.cpp
    src/BulletDynamics/Dynamics/btSimpleDynamicsWorld.h
    src/BulletDynamics/Dynamics/btSimpleDynamicsWorld.cpp
    src/BulletDynamics/Dynamics/btSimulationIslandManagerMt.h
    src/BulletDynamics/Dynamics/btSimulationIslandManagerMt.cpp
    
    src/BulletDynamics/Featherstone/btMultiBody.h
    src/BulletDynamics/Featherstone/btMultiBody.cpp
    src/BulletDynamics/Featherstone/btMultiBodyConstraint.h
    src/BulletDynamics/Featherstone/btMultiBodyConstraint.cpp
    src/BulletDynamics/Featherstone/btMultiBodyConstraintSolver.h
    src/BulletDynamics/Featherstone/btMultiBodyConstraintSolver.cpp
    src/BulletDynamics/Featherstone/btMultiBodyDynamicsWorld.h
    src/BulletDynamics/Featherstone/btMultiBodyDynamicsWorld.cpp
    src/BulletDynamics/Featherstone/btMultiBodyFixedConstraint.h
    src/BulletDynamics/Featherstone/btMultiBodyFixedConstraint.cpp
    src/BulletDynamics/Featherstone/btMultiBodyGearConstraint.h
    src/BulletDynamics/Featherstone/btMultiBodyGearConstraint.cpp
    src/BulletDynamics/Featherstone/btMultiBodyJointFeedback.h
    src/BulletDynamics/Featherstone/btMultiBodyJointLimitConstraint.h
    src/BulletDynamics/Featherstone/btMultiBodyJointLimitConstraint.cpp
    src/BulletDynamics/Featherstone/btMultiBodyJointMotor.h
    src/BulletDynamics/Featherstone/btMultiBodyJointMotor.cpp
    src/BulletDynamics/Featherstone/btMultiBodyLink.h
    src/BulletDynamics/Featherstone/btMultiBodyLinkCollider.h
    src/BulletDynamics/Featherstone/btMultiBodyMLCPConstraintSolver.h
    src/BulletDynamics/Featherstone/btMultiBodyMLCPConstraintSolver.cpp
    src/BulletDynamics/Featherstone/btMultiBodyPoint2Point.h
    src/BulletDynamics/Featherstone/btMultiBodyPoint2Point.cpp
    src/BulletDynamics/Featherstone/btMultiBodySliderConstraint.h
    src/BulletDynamics/Featherstone/btMultiBodySliderConstraint.cpp
    src/BulletDynamics/Featherstone/btMultiBodySolverConstraint.h
    src/BulletDynamics/Featherstone/btMultiBodySphericalJointMotor.h
    src/BulletDynamics/Featherstone/btMultiBodySphericalJointMotor.cpp

    src/BulletDynamics/MLCPSolvers/btDantzigLCP.h
    src/BulletDynamics/MLCPSolvers/btDantzigLCP.cpp
    src/BulletDynamics/MLCPSolvers/btDantzigSolver.h
    src/BulletDynamics/MLCPSolvers/btLemkeAlgorithm.h
    src/BulletDynamics/MLCPSolvers/btLemkeAlgorithm.cpp
    src/BulletDynamics/MLCPSolvers/btLemkeSolver.h
    src/BulletDynamics/MLCPSolvers/btMLCPSolver.h
    src/BulletDynamics/MLCPSolvers/btMLCPSolver.cpp
    src/BulletDynamics/MLCPSolvers/btMLCPSolverInterface.h
    src/BulletDynamics/MLCPSolvers/btPATHSolver.h
    src/BulletDynamics/MLCPSolvers/btSolveProjectedGaussSeidel.h

    src/BulletDynamics/Vehicle/btRaycastVehicle.h
    src/BulletDynamics/Vehicle/btRaycastVehicle.cpp
    src/BulletDynamics/Vehicle/btVehicleRaycaster.h
    src/BulletDynamics/Vehicle/btWheelInfo.h    
    src/BulletDynamics/Vehicle/btWheelInfo.cpp

    src/BulletInverseDynamics/details/IDEigenInterface.hpp
    src/BulletInverseDynamics/details/IDLinearMathInterface.hpp
    src/BulletInverseDynamics/details/IDMatVec.hpp
    src/BulletInverseDynamics/details/MultiBodyTreeImpl.hpp
    src/BulletInverseDynamics/details/MultiBodyTreeImpl.cpp
    src/BulletInverseDynamics/details/MultiBodyTreeInitCache.hpp
    src/BulletInverseDynamics/details/MultiBodyTreeInitCache.cpp
    src/BulletInverseDynamics/IDConfig.hpp
    src/BulletInverseDynamics/IDConfigBuiltin.hpp
    src/BulletInverseDynamics/IDConfigEigen.hpp
    src/BulletInverseDynamics/IDErrorMessages.hpp
    src/BulletInverseDynamics/IDMath.hpp
    src/BulletInverseDynamics/IDMath.cpp
    src/BulletInverseDynamics/MultiBodyTree.hpp
    src/BulletInverseDynamics/MultiBodyTree.cpp

    src/BulletSoftBody/btDefaultSoftBodySolver.h
    src/BulletSoftBody/btDefaultSoftBodySolver.cpp
    src/BulletSoftBody/btSoftBody.h
    src/BulletSoftBody/btSoftBody.cpp
    src/BulletSoftBody/btSoftBodyConcaveCollisionAlgorithm.h
    src/BulletSoftBody/btSoftBodyConcaveCollisionAlgorithm.cpp
    src/BulletSoftBody/btSoftBodyData.h
    src/BulletSoftBody/btSoftBodyHelpers.h
    src/BulletSoftBody/btSoftBodyHelpers.cpp
    src/BulletSoftBody/btSoftBodyInternals.h
    src/BulletSoftBody/btSoftMultiBodyDynamicsWorld.h
    src/BulletSoftBody/btSoftMultiBodyDynamicsWorld.cpp
    src/BulletSoftBody/btSoftBodyRigidBodyCollisionConfiguration.h
    src/BulletSoftBody/btSoftBodyRigidBodyCollisionConfiguration.cpp
    src/BulletSoftBody/btSoftBodySolvers.h
    src/BulletSoftBody/btSoftBodySolverVertexBuffer.h
    src/BulletSoftBody/btSoftRigidCollisionAlgorithm.h
    src/BulletSoftBody/btSoftRigidCollisionAlgorithm.cpp
    src/BulletSoftBody/btSoftRigidDynamicsWorld.h
    src/BulletSoftBody/btSoftRigidDynamicsWorld.cpp
    src/BulletSoftBody/btSoftSoftCollisionAlgorithm.h
    src/BulletSoftBody/btSoftSoftCollisionAlgorithm.cpp
    src/BulletSoftBody/btSparseSDF.h

    src/LinearMath/btAabbUtil2.h
    src/LinearMath/btAlignedAllocator.h
    src/LinearMath/btAlignedAllocator.cpp
    src/LinearMath/btAlignedObjectArray.h
    src/LinearMath/btConvexHull.h
    src/LinearMath/btConvexHull.cpp
    src/LinearMath/btConvexHullComputer.h
    src/LinearMath/btConvexHullComputer.cpp
    src/LinearMath/btCpuFeatureUtility.h
    src/LinearMath/btDefaultMotionState.h
    src/LinearMath/btGeometryUtil.h
    src/LinearMath/btGeometryUtil.cpp
    src/LinearMath/btGrahamScan2dConvexHull.h
    src/LinearMath/btHashMap.h
    src/LinearMath/btIDebugDraw.h
    src/LinearMath/btList.h
    src/LinearMath/btMatrix3x3.h
    src/LinearMath/btMatrixX.h
    src/LinearMath/btMinMax.h
    src/LinearMath/btMotionState.h
    src/LinearMath/btPolarDecomposition.h
    src/LinearMath/btPolarDecomposition.cpp
    src/LinearMath/btPoolAllocator.h
    src/LinearMath/btQuadWord.h
    src/LinearMath/btQuaternion.h
    src/LinearMath/btQuickprof.h
    src/LinearMath/btQuickprof.cpp
    src/LinearMath/btRandom.h
    src/LinearMath/btScalar.h
    src/LinearMath/btSerializer.h
    src/LinearMath/btSerializer.cpp
    src/LinearMath/btSerializer64.cpp
    src/LinearMath/btSpatialAlgebra.h
    src/LinearMath/btStackAlloc.h
    src/LinearMath/btTransform.h
    src/LinearMath/btTransformUtil.h
    src/LinearMath/btThreads.h
    src/LinearMath/btThreads.cpp
    src/LinearMath/btVector3.h
    src/LinearMath/btVector3.cpp

    Extras/ConvexDecomposition/bestfit.h
    Extras/ConvexDecomposition/bestfit.cpp
    Extras/ConvexDecomposition/bestfitobb.h
    Extras/ConvexDecomposition/bestfitobb.cpp
    Extras/ConvexDecomposition/cd_hull.h
    Extras/ConvexDecomposition/cd_hull.cpp
    Extras/ConvexDecomposition/cd_vector.h
    Extras/ConvexDecomposition/cd_wavefront.h
    Extras/ConvexDecomposition/cd_wavefront.cpp
    Extras/ConvexDecomposition/concavity.h
    Extras/ConvexDecomposition/concavity.cpp
    Extras/ConvexDecomposition/ConvexBuilder.h
    Extras/ConvexDecomposition/ConvexBuilder.cpp
    Extras/ConvexDecomposition/ConvexDecomposition.h
    Extras/ConvexDecomposition/ConvexDecomposition.cpp
    Extras/ConvexDecomposition/fitsphere.h
    Extras/ConvexDecomposition/fitsphere.cpp
    Extras/ConvexDecomposition/float_math.h
    Extras/ConvexDecomposition/float_math.cpp
    Extras/ConvexDecomposition/meshvolume.h
    Extras/ConvexDecomposition/meshvolume.cpp
    Extras/ConvexDecomposition/planetri.h
    Extras/ConvexDecomposition/planetri.cpp
    Extras/ConvexDecomposition/raytri.h
    Extras/ConvexDecomposition/raytri.cpp
    Extras/ConvexDecomposition/splitplane.h
    Extras/ConvexDecomposition/splitplane.cpp
    Extras/ConvexDecomposition/vlookup.h
    Extras/ConvexDecomposition/vlookup.cpp

    Extras/GIMPACTUtils/btGImpactConvexDecompositionShape.h
    Extras/GIMPACTUtils/btGImpactConvexDecompositionShape.cpp
)

include_directories(
    ${PROJECT_SOURCE_DIR}
)

auto_source_group(${SRC_FILES})

include_directories("${PROJECT_SOURCE_DIR}/src")
include_directories("${PROJECT_SOURCE_DIR}/Extras")
include_directories("${PROJECT_SOURCE_DIR}/Extras/ConvexDecomposition")

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_include_directories(${PROJECT_NAME}
    PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/src>
)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
Eigen is primarily MPL2 licensed. See COPYING.MPL2 and these links:
  http://www.mozilla.org/MPL/2.0/
  http://www.mozilla.org/MPL/2.0/FAQ.html

Some files contain third-party code under BSD or LGPL licenses, whence the other
COPYING.* files here.

All the LGPL code is either LGPL 2.1-only, or LGPL 2.1-or-later.
For this reason, the COPYING.LGPL file contains the LGPL 2.1 text.

If you want to guarantee that the Eigen code that you are #including is licensed
under the MPL2 and possibly more permissive licenses (like BSD), #define this
preprocessor symbol:
  EIGEN_MPL2_ONLY
For example, with most compilers, you could add this to your project CXXFLAGS:
  -DEIGEN_MPL2_ONLY
This will cause a compilation error to be generated if you #include any code that is
LGPL licensed.

project(EigenBlas CXX)

include("../cmake/language_support.cmake")

workaround_9220(Fortran EIGEN_Fortran_COMPILER_WORKS)

if(EIGEN_Fortran_COMPILER_WORKS)
  enable_language(Fortran OPTIONAL)
  if(NOT CMAKE_Fortran_COMPILER)
    set(EIGEN_Fortran_COMPILER_WORKS OFF)
  endif()
endif()

add_custom_target(blas)

set(EigenBlas_SRCS single.cpp double.cpp complex_single.cpp complex_double.cpp xerbla.cpp)

if(EIGEN_Fortran_COMPILER_WORKS)

set(EigenBlas_SRCS ${EigenBlas_SRCS}
    complexdots.f
    srotm.f srotmg.f drotm.f drotmg.f
    lsame.f  dspmv.f ssbmv.f
    chbmv.f  sspmv.f
    zhbmv.f  chpmv.f dsbmv.f
    zhpmv.f
    dtbmv.f stbmv.f ctbmv.f ztbmv.f
)
else()

message(WARNING " No fortran compiler has been detected, the blas build will be incomplete.")

endif()

add_library(eigen_blas_static ${EigenBlas_SRCS})
add_library(eigen_blas SHARED ${EigenBlas_SRCS})

if(EIGEN_STANDARD_LIBRARIES_TO_LINK_TO)
  target_link_libraries(eigen_blas_static ${EIGEN_STANDARD_LIBRARIES_TO_LINK_TO})
  target_link_libraries(eigen_blas        ${EIGEN_STANDARD_LIBRARIES_TO_LINK_TO})
endif()

add_dependencies(blas eigen_blas eigen_blas_static)

install(TARGETS eigen_blas eigen_blas_static
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

if(EIGEN_Fortran_COMPILER_WORKS)

if(EIGEN_LEAVE_TEST_IN_ALL_TARGET)
  add_subdirectory(testing) # can't do EXCLUDE_FROM_ALL here, breaks CTest
else()
  add_subdirectory(testing EXCLUDE_FROM_ALL)
endif()

endif()


This directory contains a BLAS library built on top of Eigen.

This module is not built by default. In order to compile it, you need to
type 'make blas' from within your build dir.


macro(ei_add_blas_test testname)

  set(targetname ${testname})

  set(filename ${testname}.f)
  add_executable(${targetname} ${filename})

  target_link_libraries(${targetname} eigen_blas)

  if(EIGEN_STANDARD_LIBRARIES_TO_LINK_TO)
    target_link_libraries(${targetname} ${EIGEN_STANDARD_LIBRARIES_TO_LINK_TO})
  endif()

  target_link_libraries(${targetname} ${EXTERNAL_LIBS})

  add_test(${testname} "${Eigen_SOURCE_DIR}/blas/testing/runblastest.sh" "${testname}" "${Eigen_SOURCE_DIR}/blas/testing/${testname}.dat")
  add_dependencies(buildtests ${targetname})
  
endmacro(ei_add_blas_test)

ei_add_blas_test(sblat1)
ei_add_blas_test(sblat2)
ei_add_blas_test(sblat3)

ei_add_blas_test(dblat1)
ei_add_blas_test(dblat2)
ei_add_blas_test(dblat3)

ei_add_blas_test(cblat1)
ei_add_blas_test(cblat2)
ei_add_blas_test(cblat3)

ei_add_blas_test(zblat1)
ei_add_blas_test(zblat2)
ei_add_blas_test(zblat3)

# add_custom_target(level1)
# add_dependencies(level1 sblat1)

include(RegexUtils)
test_escape_string_as_regex()

file(GLOB Eigen_directory_files "*")

escape_string_as_regex(ESCAPED_CMAKE_CURRENT_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

foreach(f ${Eigen_directory_files})
  if(NOT f MATCHES "\\.txt" AND NOT f MATCHES "${ESCAPED_CMAKE_CURRENT_SOURCE_DIR}/[.].+" AND NOT f MATCHES "${ESCAPED_CMAKE_CURRENT_SOURCE_DIR}/src")
    list(APPEND Eigen_directory_files_to_install ${f})
  endif()
endforeach(f ${Eigen_directory_files})

install(FILES
  ${Eigen_directory_files_to_install}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen COMPONENT Devel
  )

add_subdirectory(src)
file(GLOB Eigen_src_subdirectories "*")
escape_string_as_regex(ESCAPED_CMAKE_CURRENT_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
foreach(f ${Eigen_src_subdirectories})
  if(NOT f MATCHES "\\.txt" AND NOT f MATCHES "${ESCAPED_CMAKE_CURRENT_SOURCE_DIR}/[.].+" )
    add_subdirectory(${f})
  endif()
endforeach()
FILE(GLOB Eigen_Cholesky_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Cholesky_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Cholesky COMPONENT Devel
  )
FILE(GLOB Eigen_CholmodSupport_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_CholmodSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/CholmodSupport COMPONENT Devel
  )
FILE(GLOB Eigen_Core_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Core_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core COMPONENT Devel
  )

ADD_SUBDIRECTORY(products)
ADD_SUBDIRECTORY(util)
ADD_SUBDIRECTORY(arch)
ADD_SUBDIRECTORY(SSE)
ADD_SUBDIRECTORY(AltiVec)
ADD_SUBDIRECTORY(NEON)
ADD_SUBDIRECTORY(Default)
FILE(GLOB Eigen_Core_arch_AltiVec_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Core_arch_AltiVec_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core/arch/AltiVec COMPONENT Devel
)
FILE(GLOB Eigen_Core_arch_Default_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Core_arch_Default_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core/arch/Default COMPONENT Devel
)
FILE(GLOB Eigen_Core_arch_NEON_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Core_arch_NEON_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core/arch/NEON COMPONENT Devel
)
FILE(GLOB Eigen_Core_arch_SSE_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Core_arch_SSE_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core/arch/SSE COMPONENT Devel
)
FILE(GLOB Eigen_Core_Product_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Core_Product_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core/products COMPONENT Devel
  )
FILE(GLOB Eigen_Core_util_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_Core_util_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Core/util COMPONENT Devel
  )
FILE(GLOB Eigen_Eigen2Support_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Eigen2Support_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Eigen2Support COMPONENT Devel
  )

ADD_SUBDIRECTORY(Geometry)FILE(GLOB Eigen_Eigen2Support_Geometry_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Eigen2Support_Geometry_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Eigen2Support/Geometry
  )
FILE(GLOB Eigen_EIGENVALUES_SRCS "*.h")

INSTALL(FILES
  ${Eigen_EIGENVALUES_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Eigenvalues COMPONENT Devel
  )
FILE(GLOB Eigen_Geometry_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Geometry_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Geometry COMPONENT Devel
  )

ADD_SUBDIRECTORY(arch)
FILE(GLOB Eigen_Geometry_arch_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Geometry_arch_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Geometry/arch COMPONENT Devel
  )
FILE(GLOB Eigen_Householder_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Householder_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Householder COMPONENT Devel
  )
FILE(GLOB Eigen_IterativeLinearSolvers_SRCS "*.h")

INSTALL(FILES
  ${Eigen_IterativeLinearSolvers_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/IterativeLinearSolvers COMPONENT Devel
  )
FILE(GLOB Eigen_Jacobi_SRCS "*.h")

INSTALL(FILES
  ${Eigen_Jacobi_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/Jacobi COMPONENT Devel
  )
FILE(GLOB Eigen_LU_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_LU_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/LU COMPONENT Devel
  )

ADD_SUBDIRECTORY(arch)
FILE(GLOB Eigen_LU_arch_SRCS "*.h")

INSTALL(FILES
  ${Eigen_LU_arch_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/LU/arch COMPONENT Devel
  )
FILE(GLOB Eigen_MetisSupport_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_MetisSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/MetisSupport COMPONENT Devel
  )
FILE(GLOB Eigen_misc_SRCS "*.h")

INSTALL(FILES
  ${Eigen_misc_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/misc COMPONENT Devel
  )
FILE(GLOB Eigen_OrderingMethods_SRCS "*.h")

INSTALL(FILES
  ${Eigen_OrderingMethods_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/OrderingMethods COMPONENT Devel
  )
FILE(GLOB Eigen_PardisoSupport_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_PardisoSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/PardisoSupport COMPONENT Devel
  )
FILE(GLOB Eigen_PastixSupport_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_PastixSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/PaStiXSupport COMPONENT Devel
  )
FILE(GLOB Eigen_plugins_SRCS "*.h")

INSTALL(FILES
  ${Eigen_plugins_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/plugins COMPONENT Devel
  )
FILE(GLOB Eigen_QR_SRCS "*.h")

INSTALL(FILES
  ${Eigen_QR_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/QR COMPONENT Devel
  )
FILE(GLOB Eigen_SparseCholesky_SRCS "*.h")

INSTALL(FILES
  ${Eigen_SparseCholesky_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SparseCholesky COMPONENT Devel
  )
FILE(GLOB Eigen_SparseCore_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_SparseCore_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SparseCore COMPONENT Devel
  )
FILE(GLOB Eigen_SparseLU_SRCS "*.h")

INSTALL(FILES
  ${Eigen_SparseLU_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SparseLU COMPONENT Devel
  )
FILE(GLOB Eigen_SparseQR_SRCS "*.h")

INSTALL(FILES
  ${Eigen_SparseQR_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SparseQR/ COMPONENT Devel
  )
FILE(GLOB Eigen_SPQRSupport_SRCS "*.h")

INSTALL(FILES
  ${Eigen_SPQRSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SPQRSupport/ COMPONENT Devel
  )
FILE(GLOB Eigen_StlSupport_SRCS "*.h")

INSTALL(FILES
  ${Eigen_StlSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/StlSupport COMPONENT Devel
  )
FILE(GLOB Eigen_SuperLUSupport_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_SuperLUSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SuperLUSupport COMPONENT Devel
  )
FILE(GLOB Eigen_SVD_SRCS "*.h")

INSTALL(FILES
  ${Eigen_SVD_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/SVD COMPONENT Devel
  )
FILE(GLOB Eigen_UmfPackSupport_SRCS "*.h")

INSTALL(FILES 
  ${Eigen_UmfPackSupport_SRCS}
  DESTINATION ${INCLUDE_INSTALL_DIR}/Eigen/src/UmfPackSupport COMPONENT Devel
  )

project(EigenLapack CXX)

include("../cmake/language_support.cmake")

workaround_9220(Fortran EIGEN_Fortran_COMPILER_WORKS)

if(EIGEN_Fortran_COMPILER_WORKS)
  enable_language(Fortran OPTIONAL)
  if(NOT CMAKE_Fortran_COMPILER)
    set(EIGEN_Fortran_COMPILER_WORKS OFF)
  endif()
endif()

add_custom_target(lapack)
include_directories(../blas)

set(EigenLapack_SRCS
single.cpp double.cpp complex_single.cpp complex_double.cpp ../blas/xerbla.cpp
)

if(EIGEN_Fortran_COMPILER_WORKS)

set(EigenLapack_SRCS  ${EigenLapack_SRCS}
  slarft.f  dlarft.f  clarft.f  zlarft.f
  slarfb.f  dlarfb.f  clarfb.f  zlarfb.f
  slarfg.f  dlarfg.f  clarfg.f  zlarfg.f
  slarf.f   dlarf.f   clarf.f   zlarf.f
  sladiv.f  dladiv.f  cladiv.f  zladiv.f
  ilaslr.f  iladlr.f  ilaclr.f  ilazlr.f
  ilaslc.f  iladlc.f  ilaclc.f  ilazlc.f
  dlapy2.f  dlapy3.f  slapy2.f  slapy3.f
  clacgv.f  zlacgv.f
  slamch.f  dlamch.f
  second_NONE.f dsecnd_NONE.f
)

option(EIGEN_ENABLE_LAPACK_TESTS OFF "Enbale the Lapack unit tests")

if(EIGEN_ENABLE_LAPACK_TESTS)

  get_filename_component(eigen_full_path_to_reference_lapack "./reference/" ABSOLUTE)
  if(NOT EXISTS ${eigen_full_path_to_reference_lapack})
    # Download lapack and install sources and testing at the right place
    message(STATUS "Download lapack_addons_3.4.1.tgz...")
    
    file(DOWNLOAD "http://downloads.tuxfamily.org/eigen/lapack_addons_3.4.1.tgz"
                  "${CMAKE_CURRENT_SOURCE_DIR}/lapack_addons_3.4.1.tgz"
                  INACTIVITY_TIMEOUT 15
                  TIMEOUT 240
                  STATUS download_status
                  EXPECTED_MD5 5758ce55afcf79da98de8b9de1615ad5
                  SHOW_PROGRESS)
                  
    message(STATUS ${download_status})
    list(GET download_status 0 download_status_num)
    set(download_status_num 0)
    if(download_status_num EQUAL 0)
      message(STATUS "Setup lapack reference and lapack unit tests")
      execute_process(COMMAND tar xzf  "lapack_addons_3.4.1.tgz" WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
    else()
      message(STATUS "Download of lapack_addons_3.4.1.tgz failed, LAPACK unit tests wont be enabled")
      set(EIGEN_ENABLE_LAPACK_TESTS false)
    endif()
                  
  endif()
  
  get_filename_component(eigen_full_path_to_reference_lapack "./reference/" ABSOLUTE)
  if(EXISTS ${eigen_full_path_to_reference_lapack})
    set(EigenLapack_funcfilenames
        ssyev.f   dsyev.f   csyev.f   zsyev.f
        spotrf.f  dpotrf.f  cpotrf.f  zpotrf.f
        spotrs.f  dpotrs.f  cpotrs.f  zpotrs.f
        sgetrf.f  dgetrf.f  cgetrf.f  zgetrf.f
        sgetrs.f  dgetrs.f  cgetrs.f  zgetrs.f)
    
    FILE(GLOB ReferenceLapack_SRCS0 RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "reference/*.f")
    foreach(filename1 IN LISTS ReferenceLapack_SRCS0)
      string(REPLACE "reference/" "" filename ${filename1})
      list(FIND EigenLapack_SRCS ${filename} id1)
      list(FIND EigenLapack_funcfilenames ${filename} id2)
      if((id1 EQUAL -1) AND (id2 EQUAL -1))
        set(ReferenceLapack_SRCS ${ReferenceLapack_SRCS} reference/${filename})
      endif()
    endforeach()
  endif()
  
  
endif(EIGEN_ENABLE_LAPACK_TESTS)

endif(EIGEN_Fortran_COMPILER_WORKS)

add_library(eigen_lapack_static ${EigenLapack_SRCS} ${ReferenceLapack_SRCS})
add_library(eigen_lapack SHARED ${EigenLapack_SRCS})

target_link_libraries(eigen_lapack  eigen_blas)

if(EIGEN_STANDARD_LIBRARIES_TO_LINK_TO)
  target_link_libraries(eigen_lapack_static ${EIGEN_STANDARD_LIBRARIES_TO_LINK_TO})
  target_link_libraries(eigen_lapack        ${EIGEN_STANDARD_LIBRARIES_TO_LINK_TO})
endif()

add_dependencies(lapack eigen_lapack eigen_lapack_static)

install(TARGETS eigen_lapack eigen_lapack_static
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

        
        
get_filename_component(eigen_full_path_to_testing_lapack "./testing/" ABSOLUTE)
if(EXISTS ${eigen_full_path_to_testing_lapack})
  
  # The following comes from lapack/TESTING/CMakeLists.txt
  # Get Python
  find_package(PythonInterp)
  message(STATUS "Looking for Python found - ${PYTHONINTERP_FOUND}")
  if (PYTHONINTERP_FOUND)
    message(STATUS "Using Python version ${PYTHON_VERSION_STRING}")
  endif()

  set(LAPACK_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
  set(LAPACK_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})
  set(BUILD_SINGLE      true)
  set(BUILD_DOUBLE      true)
  set(BUILD_COMPLEX     true)
  set(BUILD_COMPLEX16E  true)
  
  if(MSVC_VERSION)
#  string(REPLACE "/STACK:10000000" "/STACK:900000000000000000"
#    CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
  string(REGEX REPLACE "(.*)/STACK:(.*) (.*)" "\\1/STACK:900000000000000000 \\3"
    CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
  endif()
  add_subdirectory(testing/MATGEN)
  add_subdirectory(testing/LIN)
  add_subdirectory(testing/EIG)
  macro(add_lapack_test output input target)
    set(TEST_INPUT "${LAPACK_SOURCE_DIR}/testing/${input}")
    set(TEST_OUTPUT "${LAPACK_BINARY_DIR}/testing/${output}")
    get_target_property(TEST_LOC ${target} LOCATION)
    string(REPLACE "." "_" input_name ${input})
    set(testName "${target}_${input_name}")
    if(EXISTS "${TEST_INPUT}")
      add_test(LAPACK-${testName} "${CMAKE_COMMAND}"
        -DTEST=${TEST_LOC}
        -DINPUT=${TEST_INPUT} 
        -DOUTPUT=${TEST_OUTPUT} 
        -DINTDIR=${CMAKE_CFG_INTDIR}
        -P "${LAPACK_SOURCE_DIR}/testing/runtest.cmake")
    endif()
  endmacro(add_lapack_test)

  if (BUILD_SINGLE)
  add_lapack_test(stest.out stest.in xlintsts)
  #
  # ======== SINGLE RFP LIN TESTS ========================
  add_lapack_test(stest_rfp.out stest_rfp.in xlintstrfs)
  #
  #
  # ======== SINGLE EIG TESTS ===========================
  #

  add_lapack_test(snep.out nep.in xeigtsts)


  add_lapack_test(ssep.out sep.in xeigtsts)


  add_lapack_test(ssvd.out svd.in xeigtsts)


  add_lapack_test(sec.out sec.in xeigtsts)


  add_lapack_test(sed.out sed.in xeigtsts)


  add_lapack_test(sgg.out sgg.in xeigtsts)


  add_lapack_test(sgd.out sgd.in xeigtsts)


  add_lapack_test(ssb.out ssb.in xeigtsts)


  add_lapack_test(ssg.out ssg.in xeigtsts)


  add_lapack_test(sbal.out sbal.in xeigtsts)


  add_lapack_test(sbak.out sbak.in xeigtsts)


  add_lapack_test(sgbal.out sgbal.in xeigtsts)


  add_lapack_test(sgbak.out sgbak.in xeigtsts)


  add_lapack_test(sbb.out sbb.in xeigtsts)


  add_lapack_test(sglm.out glm.in xeigtsts)


  add_lapack_test(sgqr.out gqr.in xeigtsts)


  add_lapack_test(sgsv.out gsv.in xeigtsts)


  add_lapack_test(scsd.out csd.in xeigtsts)


  add_lapack_test(slse.out lse.in xeigtsts)
  endif()

  if (BUILD_DOUBLE)
  #
  # ======== DOUBLE LIN TESTS ===========================
  add_lapack_test(dtest.out dtest.in xlintstd)
  #
  # ======== DOUBLE RFP LIN TESTS ========================
  add_lapack_test(dtest_rfp.out dtest_rfp.in xlintstrfd)
  #
  # ======== DOUBLE EIG TESTS ===========================

  add_lapack_test(dnep.out nep.in xeigtstd)


  add_lapack_test(dsep.out sep.in xeigtstd)


  add_lapack_test(dsvd.out svd.in xeigtstd)


  add_lapack_test(dec.out dec.in xeigtstd)


  add_lapack_test(ded.out ded.in xeigtstd)


  add_lapack_test(dgg.out dgg.in xeigtstd)


  add_lapack_test(dgd.out dgd.in xeigtstd)


  add_lapack_test(dsb.out dsb.in xeigtstd)


  add_lapack_test(dsg.out dsg.in xeigtstd)


  add_lapack_test(dbal.out dbal.in xeigtstd)


  add_lapack_test(dbak.out dbak.in xeigtstd)


  add_lapack_test(dgbal.out dgbal.in xeigtstd)


  add_lapack_test(dgbak.out dgbak.in xeigtstd)


  add_lapack_test(dbb.out dbb.in xeigtstd)


  add_lapack_test(dglm.out glm.in xeigtstd)


  add_lapack_test(dgqr.out gqr.in xeigtstd)


  add_lapack_test(dgsv.out gsv.in xeigtstd)


  add_lapack_test(dcsd.out csd.in xeigtstd)


  add_lapack_test(dlse.out lse.in xeigtstd)
  endif()

  if (BUILD_COMPLEX)
  add_lapack_test(ctest.out ctest.in xlintstc)
  #
  # ======== COMPLEX RFP LIN TESTS ========================
  add_lapack_test(ctest_rfp.out ctest_rfp.in xlintstrfc)
  #
  # ======== COMPLEX EIG TESTS ===========================

  add_lapack_test(cnep.out nep.in xeigtstc)


  add_lapack_test(csep.out sep.in xeigtstc)


  add_lapack_test(csvd.out svd.in xeigtstc)


  add_lapack_test(cec.out cec.in xeigtstc)


  add_lapack_test(ced.out ced.in xeigtstc)


  add_lapack_test(cgg.out cgg.in xeigtstc)


  add_lapack_test(cgd.out cgd.in xeigtstc)


  add_lapack_test(csb.out csb.in xeigtstc)


  add_lapack_test(csg.out csg.in xeigtstc)


  add_lapack_test(cbal.out cbal.in xeigtstc)


  add_lapack_test(cbak.out cbak.in xeigtstc)


  add_lapack_test(cgbal.out cgbal.in xeigtstc)


  add_lapack_test(cgbak.out cgbak.in xeigtstc)


  add_lapack_test(cbb.out cbb.in xeigtstc)


  add_lapack_test(cglm.out glm.in xeigtstc)


  add_lapack_test(cgqr.out gqr.in xeigtstc)


  add_lapack_test(cgsv.out gsv.in xeigtstc)


  add_lapack_test(ccsd.out csd.in xeigtstc)


  add_lapack_test(clse.out lse.in xeigtstc)
  endif()

  if (BUILD_COMPLEX16)
  #
  # ======== COMPLEX16 LIN TESTS ========================
  add_lapack_test(ztest.out ztest.in xlintstz)
  #
  # ======== COMPLEX16 RFP LIN TESTS ========================
  add_lapack_test(ztest_rfp.out ztest_rfp.in xlintstrfz)
  #
  # ======== COMPLEX16 EIG TESTS ===========================

  add_lapack_test(znep.out nep.in xeigtstz)


  add_lapack_test(zsep.out sep.in xeigtstz)


  add_lapack_test(zsvd.out svd.in xeigtstz)


  add_lapack_test(zec.out zec.in xeigtstz)


  add_lapack_test(zed.out zed.in xeigtstz)


  add_lapack_test(zgg.out zgg.in xeigtstz)


  add_lapack_test(zgd.out zgd.in xeigtstz)


  add_lapack_test(zsb.out zsb.in xeigtstz)


  add_lapack_test(zsg.out zsg.in xeigtstz)


  add_lapack_test(zbal.out zbal.in xeigtstz)


  add_lapack_test(zbak.out zbak.in xeigtstz)


  add_lapack_test(zgbal.out zgbal.in xeigtstz)


  add_lapack_test(zgbak.out zgbak.in xeigtstz)


  add_lapack_test(zbb.out zbb.in xeigtstz)


  add_lapack_test(zglm.out glm.in xeigtstz)


  add_lapack_test(zgqr.out gqr.in xeigtstz)


  add_lapack_test(zgsv.out gsv.in xeigtstz)


  add_lapack_test(zcsd.out csd.in xeigtstz)


  add_lapack_test(zlse.out lse.in xeigtstz)
  endif()


  if (BUILD_SIMPLE)
      if (BUILD_DOUBLE)
  #
  # ======== SINGLE-DOUBLE PROTO LIN TESTS ==============
          add_lapack_test(dstest.out dstest.in xlintstds)
      endif()
  endif()


  if (BUILD_COMPLEX)
      if (BUILD_COMPLEX16)
  #
  # ======== COMPLEX-COMPLEX16 LIN TESTS ========================
          add_lapack_test(zctest.out zctest.in xlintstzc)
      endif()
  endif()

  # ==============================================================================

  execute_process(COMMAND ${CMAKE_COMMAND} -E copy ${LAPACK_SOURCE_DIR}/testing/lapack_testing.py ${LAPACK_BINARY_DIR})
  add_test(
    NAME LAPACK_Test_Summary
    WORKING_DIRECTORY ${LAPACK_BINARY_DIR}
    COMMAND ${PYTHON_EXECUTABLE} "lapack_testing.py"
  )

endif()

# Copyright 2015 Etc2Comp Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cmake_minimum_required(VERSION 2.8.9)
project(Etc2Comp)

set (CMAKE_CXX_STANDARD 11)

#IF (APPLE)
#	set (CMAKE_CXX_FLAGS "-I/usr/include/i386-linux-gnu/c++/4.8 -I/usr/include/c++/4.8 -std=c++11 -g3 -Wall -O3")
#ELSE ()
#	IF (WIN32)
#		set (CMAKE_CXX_FLAGS "-I/usr/include/i386-linux-gnu/c++/4.8 -I/usr/include/c++/4.8 -W4 /EHsc")
#	ELSE()
#		set (CMAKE_CXX_FLAGS "-I/usr/include/i386-linux-gnu/c++/4.8 -I/usr/include/c++/4.8 -std=c++11 -pthread -g3 -Wall -O2")
#	ENDIF()
#ENDIF ()

ADD_SUBDIRECTORY(EtcLib)
#ADD_SUBDIRECTORY(EtcTool)
# Contributing | Etc2Comp

Thank you for contributing to the Etc2Comp community!

 - [Have a usage question?](#question)
 - [Think you found a bug?](#issue)
 - [Have a feature request?](#feature)
 - [Want to submit a pull request?](#submit)
 - [Small print](#smallprint)

## <a name="question"></a> Have a usage question?

 - Review the README.md to make sure you're building the binary correctly.
 - Execute the binary with -h to show the usage help.
 - Search through [old issues](https://github.com/google/etc2comp/issues)
 for an answer to your question.
 - If you still haven't found an answer to your question, [open a new issue](https://github.com/google/etc2comp/issues/new).
Please use the provided bug report template and include a minimal repro.

## <a name="issue"></a> Think you found a bug?

The library is experimental so that's highly likely. Follow the same
procedure above for questions. If you are up to the challenge,
[submit a Pull Request](#submit) with a fix!

## <a name="feature"></a> Have a feature request?

Great! Make sure the feature request isn't already listed in 
[existing issues](https://github.com/google/etc2comp/issues),
then go ahead and [open a new issue](https://github.com/google/etc2comp/issues/new).
Remove the default template information and specify what you are requesting
technically, as well as, specifying what use cases it supports.

## <a name="submit"></a> Want to submit a pull request?

Sweet, we'd love to accept your contribution! [Open a new pull request](https://github.com/google/etc2comp/compare).

If you want to implement a new feature, please open an issue with a
proposal first to discuss the change.

You will need to sign our [Contributor License Agreement](https://cla.developers.google.com/about/google-individual)
before we can accept your pull request.

## <a name="smallprint"></a> The small print
Contributions made by corporations are covered by a different
agreement than the one above, the
[Software Grant and Corporate Contributor License Agreement]
(https://cla.developers.google.com/about/google-corporate).
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
# Etc2Comp - Texture to ETC2 compressor

Etc2Comp is a command line tool that converts textures (e.g. bitmaps)
into the [ETC2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression)
format. The tool is built with a focus on encoding performance
to reduce the amount of time required to compile asset heavy applications as
well as reduce overall application size.

This repo provides source code that can be compiled into a binary. The
binary can then be used to convert textures to the ETC2 format.

Important: This is not an official Google product. It is an experimental
library published as-is. Please see the CONTRIBUTORS.md file for information
about questions or issues.

## Setup
This project uses [CMake](https://cmake.org/) to generate platform-specific
build files:
 - Linux: make files
 - OS X: Xcode workspace files
 - Microsoft Windows: Visual Studio solution files
 - Note: CMake supports other formats, but this doc only provides steps for
 one of each platform for brevity.

Refer to each platform's setup section to setup your environment and build
an Etc2Comp binary. Then skip to the usage section of this page for examples
of how to use the library.

### Setup for OS X
 build tested on this config:
  OS X 10.9.5 i7 16GB RAM
  Xcode 5.1.1
  cmake 3.2.3
  
Start by downloading and installing the following components if they are not
already installed on your development machine.
 - *Xcode* version 5.1.1, or greater
 - [CMake](https://cmake.org/download/) version 3.2.3, or greater

To build the Etc2Comp binary:
 1. Open a *Terminal* window and navigate to the project directory.
 1. Run `mkdir build_xcode`
 1. Run `cd build_xcode`
 1. Run `cmake -G Xcode ../`
 1. Open *Xcode* and import the `build_xcode/EtcTest.xcodeproj` file.
 1. Open the Product menu and choose Build For -> Running.
 1. Once the build succeeds the binary located at `build_xcode/EtcTool/Debug/EtcTool`
can be executed.

Optional
Xcode EtcTool ‘Run’ preferences
note: if the build_xcode/EtcTest.xcodeproj is manually deleted then some Xcode preferences 
will need to be set by hand after cmake is run (these prefs are retained across 
cmake updates if the .xcodeproj is not deleted/removed)

1. Set the active scheme to ‘EtcTool’
1. Edit the scheme
1. Select option ‘Run EtcTool’, then tab ‘Arguments’. 
Add this launch argument: ‘-argfile ../../EtcTool/args.txt’
1. Select tab ‘Options’ and set a custom working directory to: ‘$(SRCROOT)/Build_Xcode/EtcTool’

### SetUp for Windows

1. Open a *Terminal* window and navigate to the project directory.
1. Run `mkdir build_vs`
1. Run `cd build_vs`
1. Run CMAKE, noting what build version you need, and pointing to the parent directory as the source root; 
  For VS 2013 : `cmake -G "Visual Studio 12 2013 Win64" ../`
  For VS 2015 : `cmake -G "Visual Studio 14 2015 Win64" ../`
  NOTE: To see what supported Visual Studio outputs there are, run `cmake -G`
1. open the 'EtcTest' solution
1. make the 'EtcTool' project the start up project 
1. (optional) in the project properties, under 'Debugging ->command arguments' 
add the argfile textfile thats included in the EtcTool directory. 
example: -argfile C:\etc2\EtcTool\Args.txt

### Setup For Linux
The Linux build was tested on this config:
  Ubuntu desktop 14.04
  gcc/g++ 4.8
  cmake 2.8.12.2

1. Verify linux has cmake and C++-11 capable g++ installed
1. Open shell
1. Run `mkdir build_linux`
1. Run `cd build_linux`
1. Run `cmake ../`
1. Run `make`
1. navigate to the newly created EtcTool directory `cd EtcTool`
1. run the executable: `./EtcTool -argfile ../../EtcTool/args.txt`

Skip to the <a href="#usage">Usage</a> section for more information about using the
tool.

## Usage

### Command Line Usage
EtcTool can be run from the command line with the following usage:
    etctool.exe source_image [options ...] -output encoded_image

The encoder will use an array of RGBA floats read from the source_image to create 
an ETC1 or ETC2 encoded image in encoded_image.  The RGBA floats should be in the 
range [0:1].

Options:

    -analyze <analysis_folder>
    -argfile <arg_file>           additional command line arguments read from a file
    -blockAtHV <H V>              encodes a single block that contains the
                                  pixel specified by the H V coordinates
    -compare <comparison_image>   compares source_image to comparison_image
    -effort <amount>              number between 0 and 100 to specify the encoding quality 
                                  (100 is the highest quality)
    -errormetric <error_metric>   specify the error metric, the options are
                                  rgba, rgbx, rec709, numeric and normalxyz
    -format <etc_format>          ETC1, RGB8, SRGB8, RGBA8, SRGB8, RGB8A1,
                                  SRGB8A1 or R11
    -help                         prints this message
    -jobs or -j <thread_count>    specifies the number of threads (default=1)
    -normalizexyz                 normalize RGB to have a length of 1
    -verbose or -v                shows status information during the encoding
                                  process
	-mipmaps or -m <mip_count>    sets the maximum number of mipaps to generate (default=1)
	-mipwrap or -w <x|y|xy>       sets the mipmap filter wrap mode (default=clamp)

* -analyze will run an analysis of the encoding and place it in folder 
"analysis_folder" (e.g. ../analysis/kodim05).  within the analysis_folder, a folder 
will be created with a name of the current date/time (e.g. 20151204_153306).  this 
date/time folder is used to compare encodings of the same texture over time.  
within the date/time folder is a text file with several encoding stats and a 2x png 
image showing the encoding mode for each 4x4 block.

* -argfile allows additional command line arguments to be placed in a text file

* -blockAtHV selects the 4x4 pixel subset of the source image at position (H,V).  
This is mainly used for debugging

* -compare compares the source image to the created encoded image. The encoding
will dictate what error analysis is used in the comparison.

* -effort uses an "amount" between 0 and 100 to determine how much additional effort 
to apply during the encoding.

* -errormetric selects the fitting algorithm used by the encoder.  "rgba" calculates 
RMS error using RGB components that are weighted by A.  "rgbx" calculates RMS error 
using RGBA components, where A is treated as an additional data channel, instead of 
as alpha.  "rec709" is similar to "rgba", except the RGB components are also weighted 
according to Rec709.  "numeric" calculates RMS error using unweighted RGBA components.  
"normalize" calculates error based on dot product and vector length for RGB and RMS 
error for A.

* -help prints out the usage message

* -jobs enables multi-threading to speed up image encoding

* -normalizexyz normalizes the source RGB to have a length of 1.

* -verbose shows information on the current encoding process. It will then display the 
PSNR and time time it took to encode the image.

* -mipmaps takes an argument that specifies how many mipmaps to generate from the 
source image.  The mipmaps are generated with a lanczos3 filter using edge clamping.
If the mipmaps option is not specified no mipmaps are created.

* -mipwrap takes an argument that specifies the mipmap filter wrap mode.  The options 
are "x", "y" and "xy" which specify wrapping in x only, y only or x and y respectively.
The default options are clamping in both x and y.

Note: Path names can use slashes or backslashes.  The tool will convert the 
slashes to the appropriate polarity for the current platform.


## API

The library supports two different APIs - a C-like API that is not heavily 
class-based and a class-based API.

main() in EtcTool.cpp contains an example of both APIs.

The Encode() method now returns an EncodingStatus that contains bit flags for
reporting various warnings and flags encountered when encoding.


## Copyright
Copyright 2015 Etc2Comp Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# Copyright 2015 The Etc2Comp Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

project(Etc2CompLib)

include_directories(./Etc)
include_directories(./EtcCodec)

file(GLOB SOURCES
	${PROJECT_SOURCE_DIR}/Etc/*.h
	${PROJECT_SOURCE_DIR}/EtcCodec/*.h
	${PROJECT_SOURCE_DIR}/Etc/*.cpp
	${PROJECT_SOURCE_DIR}/EtcCodec/*.cpp)

add_library(${PROJECT_NAME} STATIC ${SOURCES})

target_include_directories(${PROJECT_NAME} 
	PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/EtcCodec>
)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
C:\Users\BSI\Desktop\etc2comp\googleTest.png
-format RGB8
-errormetric rgba
-output ../../EncodedImages/googleTest.ktx
-analyze ../../Analysis/googleTest
-verbose
-effort 0
# Copyright 2015 The Etc2Comp Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

project(EtcTool)
include_directories(../EtcLib/Etc)
include_directories(../EtcLib/EtcCodec)
include_directories(../third_party/lodepng)

file(GLOB SOURCES
	${PROJECT_SOURCE_DIR}/*.h
	${PROJECT_SOURCE_DIR}/*.cpp
	../third_party/lodepng/*.h
	../third_party/lodepng/*.cpp)
add_executable(EtcTool ${SOURCES})

target_link_libraries (EtcTool EtcLib)

LodePNG version 20160124

Copyright (c) 2005-2016 Lode Vandevenne

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

    1. The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software
    in a product, an acknowledgment in the product documentation would be
    appreciated but is not required.

    2. Altered source versions must be plainly marked as such, and must not be
    misrepresented as being the original software.

    3. This notice may not be removed or altered from any source
    distribution.

The manual and changelog are in the header file "lodepng.h"
Rename this file to lodepng.cpp to use it for C++, or to lodepng.c to use it for C.
cmake_minimum_required(VERSION 2.8.12)

project(etcpack_lib)

set(SRC_FILES
  etcpack_lib.h
  etcdec.cxx
  etcpack.cxx
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
Software License Agreement

PLEASE REVIEW THE FOLLOWING TERMS AND CONDITIONS PRIOR TO USING THE
ERICSSON TEXTURE COMPRESSION CODEC SOFTWARE (THE "SOFTWARE"). THE USE
OF THE SOFTWARE IS SUBJECT TO THE TERMS AND CONDITIONS OF THE
FOLLOWING SOFTWARE LICENSE AGREEMENT (THE "SLA"). IF YOU DO NOT ACCEPT
SUCH TERMS AND CONDITIONS YOU MAY NOT USE THE SOFTWARE.

Subject to the terms and conditions of the SLA, the licensee of the
Software (the "Licensee") hereby, receives a non-exclusive,
non-transferable, limited, free-of-charge, perpetual and worldwide
license, to copy, use, distribute and modify the Software, but only
for the purpose of developing, manufacturing, selling, using and
distributing products including the Software in binary form, which
products are used for compression and/or decompression according to
the Khronos standard specifications OpenGL, OpenGL ES and
WebGL. Notwithstanding anything of the above, Licensee may distribute
[etcdec.cxx] in source code form provided (i) it is in unmodified
form; and (ii) it is included in software owned by Licensee.

If Licensee institutes, or threatens to institute, patent litigation
against Ericsson or Ericsson's affiliates for using the Software for
developing, having developed, manufacturing, having manufactured,
selling, offer for sale, importing, using, leasing, operating,
repairing and/or distributing products (i) within the scope of the
Khronos framework; or (ii) using software or other intellectual
property rights owned by Ericsson or its affiliates and provided under
the Khronos framework, Ericsson shall have the right to terminate this
SLA with immediate effect. Moreover, if Licensee institutes, or
threatens to institute, patent litigation against any other licensee
of the Software for using the Software in products within the scope of
the Khronos framework, Ericsson shall have the right to terminate this
SLA with immediate effect. However, should Licensee institute, or
threaten to institute, patent litigation against any other licensee of
the Software based on such other licensee's use of any other software
together with the Software, then Ericsson shall have no right to
terminate this SLA.

This SLA does not transfer to Licensee any ownership to any Ericsson
or third party intellectual property rights. All rights not expressly
granted by Ericsson under this SLA are hereby expressly
reserved. Furthermore, nothing in this SLA shall be construed as a
right to use or sell products in a manner which conveys or purports to
convey whether explicitly, by principles of implied license, or
otherwise, any rights to any third party, under any patent of Ericsson
or of Ericsson's affiliates covering or relating to any combination of
the Software with any other software or product (not licensed
hereunder) where the right applies specifically to the combination and
not to the software or product itself.

THE SOFTWARE IS PROVIDED "AS IS". ERICSSON MAKES NO REPRESENTATIONS OF
ANY KIND, EXTENDS NO WARRANTIES OR CONDITIONS OF ANY KIND, EITHER
EXPRESS, IMPLIED OR STATUTORY; INCLUDING, BUT NOT LIMITED TO, EXPRESS,
IMPLIED OR STATUTORY WARRANTIES OR CONDITIONS OF TITLE,
MERCHANTABILITY, SATISFACTORY QUALITY, SUITABILITY, AND FITNESS FOR A
PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE
OF THE SOFTWARE IS WITH THE LICENSEE. SHOULD THE SOFTWARE PROVE
DEFECTIVE, THE LICENSEE ASSUMES THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION. ERICSSON MAKES NO WARRANTY THAT THE MANUFACTURE,
SALE, OFFERING FOR SALE, DISTRIBUTION, LEASE, USE OR IMPORTATION UNDER
THE SLA WILL BE FREE FROM INFRINGEMENT OF PATENTS, COPYRIGHTS OR OTHER
INTELLECTUAL PROPERTY RIGHTS OF OTHERS, AND THE VALIDITY OF THE
LICENSE AND THE SLA ARE SUBJECT TO LICENSEE'S SOLE RESPONSIBILITY TO
MAKE SUCH DETERMINATION AND ACQUIRE SUCH LICENSES AS MAY BE NECESSARY
WITH RESPECT TO PATENTS, COPYRIGHT AND OTHER INTELLECTUAL PROPERTY OF
THIRD PARTIES.

THE LICENSEE ACKNOWLEDGES AND ACCEPTS THAT THE SOFTWARE (I) IS NOT
LICENSED FOR; (II) IS NOT DESIGNED FOR OR INTENDED FOR; AND (III) MAY
NOT BE USED FOR; ANY MISSION CRITICAL APPLICATIONS SUCH AS, BUT NOT
LIMITED TO OPERATION OF NUCLEAR OR HEALTHCARE COMPUTER SYSTEMS AND/OR
NETWORKS, AIRCRAFT OR TRAIN CONTROL AND/OR COMMUNICATION SYSTEMS OR
ANY OTHER COMPUTER SYSTEMS AND/OR NETWORKS OR CONTROL AND/OR
COMMUNICATION SYSTEMS ALL IN WHICH CASE THE FAILURE OF THE SOFTWARE
COULD LEAD TO DEATH, PERSONAL INJURY, OR SEVERE PHYSICAL, MATERIAL OR
ENVIRONMENTAL DAMAGE. LICENSEE'S RIGHTS UNDER THIS LICENSE WILL
TERMINATE AUTOMATICALLY AND IMMEDIATELY WITHOUT NOTICE IF LICENSEE
FAILS TO COMPLY WITH THIS PARAGRAPH.

IN NO EVENT SHALL ERICSSON BE LIABLE FOR ANY DAMAGES WHATSOEVER,
INCLUDING BUT NOT LIMITED TO PERSONAL INJURY, ANY GENERAL, SPECIAL,
INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES, ARISING OUT OF OR IN
CONNECTION WITH THE USE OR INABILITY TO USE THE SOFTWARE (INCLUDING
BUT NOT LIMITED TO LOSS OF PROFITS, BUSINESS INTERUPTIONS, OR ANY
OTHER COMMERCIAL DAMAGES OR LOSSES, LOSS OF DATA OR DATA BEING
RENDERED INACCURATE OR LOSSES SUSTAINED BY THE LICENSEE OR THIRD
PARTIES OR A FAILURE OF THE SOFTWARE TO OPERATE WITH ANY OTHER
SOFTWARE) REGARDLESS OF THE THEORY OF LIABILITY (CONTRACT, TORT, OR
OTHERWISE), EVEN IF THE LICENSEE OR ANY OTHER PARTY HAS BEEN ADVISED
OF THE POSSIBILITY OF SUCH DAMAGES.

Licensee acknowledges that "ERICSSON ///" is the corporate trademark
of Telefonaktiebolaget LM Ericsson and that both "Ericsson" and the
figure "///" are important features of the trade names of
Telefonaktiebolaget LM Ericsson. Nothing contained in these terms and
conditions shall be deemed to grant Licensee any right, title or
interest in the word "Ericsson" or the figure "///". No delay or
omission by Ericsson to exercise any right or power shall impair any
such right or power to be construed to be a waiver thereof. Consent by
Ericsson to, or waiver of, a breach by the Licensee shall not
constitute consent to, waiver of, or excuse for any other different or
subsequent breach.

This SLA shall be governed by the substantive law of Sweden. Any
dispute, controversy or claim arising out of or in connection with
this SLA, or the breach, termination or invalidity thereof, shall be
submitted to the exclusive jurisdiction of the Swedish Courts.

# ETCPACK

Ericsson has developed a texture compression system called "Ericsson Texture Compression". The software for compressing images and textures to that format is called ETCPACK.

The latest version of this software includes the possibility to compress images to the new formats introduced as mandatory in the Khronos standards OpenGL ES 3.0 and OpenGL 4.3. We call this package the ETC2-package of codecs, where ETC stands for Ericsson Texture Compression. For instance the new RGB8 ETC2 codec allows higher-quality compression than ETC1. It is also backward compatible; an old ETC1 texture can be decoded using ETC2-capable handsets. There are also new formats for RGBA textures and single-channel (R) and double-channel (RG) textures. For a complete list of codecs, see Appendix C in the OpenGL ES 3.0 standard. The new software also compresses old ETC1 textures. The software can be used by independent hardware vendors who want to include ETC2-package-compression in the tool chains that they give or sell to game developers. It can also be used directly by game developers who want to create games for OpenGL ES 3.0 capable handsets. The software includes source code for the command-line-program etcpack.Windows:
========
After compiling, you can validate your build by compressing a number
of images and comparing to what you should get:

1. Start a command line prompt (Start-menu, type cmd, press enter)
2. cd the "testing" directory
3. run the program testvectors.bat (type testvectors.bat, hit enter)

The system will now compress a number of images and store them in the
"compressed" directory. Now type

validate.bat > logfile.txt

This will compare the two directories "testvectors_correct" and "testvectors". The directory "testvectors_correct" contains the correctly compressed and uncompressed versions and "testvectors" is the output from your build.

Now examine your logfile.txt. If there are no errors, all file comparisons will show "FC: no differences encountered"

If you have errors, some parts of your output will contain

000003EC: F9 CD
000003ED: DC BD
000003EE: BA AE
000003EF: 91 40
000003F2: 08 00
000003F3: 88 04
0000048C: 06 64
0000048D: 21 5C

and your build was not successful. 

If you have cygwin installed, you can replace step 4 by

4. diff -r testvectors testvectors_correct

If your build is correct there should be no output from the above command.


Cygwin
======
After compiling, you can validate your build by compressing a number
of images and comparing to what you should get:

1. Start cygwin
2. cd the "testing" directory
3. run the program testvectors_cygwin.sh (type ./testvectors_cygwin.sh, hit enter)

The system will now compress a number of images and store them in the
"compressed" directory.

4. type diff -r testvectors testvectors_correct

This will compare the two directories "testvectors_correct" and "testvectors". The directory "testvectors_correct" contains the correctly compressed and uncompressed versions and "testvectors" is the output from your build.

If there are no differences between the two directories, diff will not print anything, and your build is correct.

cmake_minimum_required(VERSION 2.8.12)

project(freetype)

set(VERSION_MAJOR "2")
set(VERSION_MINOR "5")
set(VERSION_PATCH "5")
set(PROJECT_VERSION ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH})

# Compiler definitions for building the library
add_definitions(-DFT2_BUILD_LIBRARY)

# Specify library include directories
include_directories("${PROJECT_SOURCE_DIR}/include")

file(GLOB PUBLIC_HEADERS "include/*.h")
file(GLOB PUBLIC_CONFIG_HEADERS "include/config/*.h")
file(GLOB PRIVATE_HEADERS "include/internal/*.h")

set(BASE_SRCS
  src/autofit/autofit.c
  src/base/ftadvanc.c
  src/base/ftbbox.c
  src/base/ftbdf.c
  src/base/ftbitmap.c
  src/base/ftcalc.c
  src/base/ftcid.c
  src/base/ftdbgmem.c
  src/base/ftdebug.c
  src/base/ftfstype.c
  src/base/ftgasp.c
  src/base/ftgloadr.c
  src/base/ftglyph.c
  src/base/ftgxval.c
  src/base/ftinit.c
  src/base/ftlcdfil.c
  src/base/ftmm.c
  src/base/ftobjs.c
  src/base/ftotval.c
  src/base/ftoutln.c
  src/base/ftpatent.c
  src/base/ftpfr.c
  src/base/ftrfork.c
  src/base/ftsnames.c
  src/base/ftstream.c
  src/base/ftstroke.c
  src/base/ftsynth.c
  src/base/ftsystem.c
  src/base/fttrigon.c
  src/base/fttype1.c
  src/base/ftutil.c
  src/base/ftwinfnt.c
  src/base/ftxf86.c
  src/bdf/bdf.c
  src/bzip2/ftbzip2.c
  src/cache/ftcache.c
  src/cff/cff.c
  src/cid/type1cid.c
  src/gzip/ftgzip.c
  src/lzw/ftlzw.c
  src/pcf/pcf.c
  src/pfr/pfr.c
  src/psaux/psaux.c
  src/pshinter/pshinter.c
  src/psnames/psmodule.c
  src/raster/raster.c
  src/sfnt/sfnt.c
  src/smooth/smooth.c
  src/truetype/truetype.c
  src/type1/type1.c
  src/type42/type42.c
  src/winfonts/winfnt.c
)

set(ALL_FILES ${PUBLIC_HEADERS}
  ${PUBLIC_CONFIG_HEADERS}
  ${PRIVATE_HEADERS}
  ${BASE_SRCS}
)

source_group("Public Headers" FILES ${PUBLIC_HEADERS})
source_group("Public Config Headers" FILES ${PUBLIC_CONFIG_HEADERS})
source_group("Private Headers" FILES ${PRIVATE_HEADERS})
auto_source_group(${BASE_SRCS})

include_directories("src/truetype")
include_directories("src/sfnt")
include_directories("src/autofit")
include_directories("src/smooth")
include_directories("src/raster")
include_directories("src/psaux")
include_directories("src/psnames")

add_library(${PROJECT_NAME} STATIC ${ALL_FILES})

target_include_directories(${PROJECT_NAME} 
    PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
  FreeType 2.5.5
  ==============

  Homepage: http://www.freetype.org

  FreeType is a freely available software library to render fonts.

  It  is  written  in  C,  designed to  be  small,  efficient,  highly
  customizable, and  portable while capable of  producing high-quality
  output  (glyph  images) of  most  vector  and bitmap  font  formats.

  Please   read   the  docs/CHANGES   file,   it  contains   IMPORTANT
  INFORMATION.

  Read the  files `docs/INSTALL*'  for installation  instructions; see
  the file `docs/LICENSE.TXT' for the available licenses.

  The FreeType 2 API reference is located in `docs/reference'; use the
  file   `ft2-toc.html'   as   the   top  entry   point.    Additional
  documentation is available as a separate package from our sites.  Go
  to

    http://download.savannah.gnu.org/releases/freetype/

  and download one of the following files.

    freetype-doc-2.5.5.tar.bz2
    freetype-doc-2.5.5.tar.gz
    ftdoc255.zip

  To view the documentation online, go to

    http://www.freetype.org/freetype2/documentation.html


  Mailing Lists
  =============

  The preferred way  of communication with the FreeType  team is using
  e-mail lists.

    general use and discussion:      freetype@nongnu.org
    engine internals, porting, etc.: freetype-devel@nongnu.org
    announcements:                   freetype-announce@nongnu.org

  The lists are moderated; see

    http://www.freetype.org/contact.html

  how to subscribe.


  Bugs
  ====

  Please submit bug reports at

    https://savannah.nongnu.org/bugs/?group=freetype

  Alternatively,    you   might    report    bugs    by   e-mail    to
  `freetype-devel@nongnu.org'.   Don't  forget   to  send  a  detailed
  explanation of the problem --  there is nothing worse than receiving
  a terse message that only says `it doesn't work'.


  Enjoy!


    The FreeType Team

----------------------------------------------------------------------

Copyright 2006-2014 by
David Turner, Robert Wilhelm, and Werner Lemberg.

This  file is  part of  the FreeType  project, and  may only  be used,
modified,  and distributed  under the  terms of  the  FreeType project
license,  LICENSE.TXT.  By  continuing to  use, modify,  or distribute
this file you  indicate that you have read  the license and understand
and accept it fully.


--- end of README ---
The git  archive doesn't  contain pre-built configuration  scripts for
UNIXish platforms.  To generate them say

  sh autogen.sh

which in turn depends on the following packages:

  automake (1.10.1)
  libtool (2.2.4)
  autoconf (2.62)

The versions given  in parentheses are known to  work.  Newer versions
should work too, of course.   Note that autogen.sh also sets up proper
file permissions for the `configure' and auxiliary scripts.

The autogen.sh script  now checks the version of  above three packages
whether they match the numbers  above.  Otherwise it will complain and
suggest either upgrading or using  an environment variable to point to
a more recent version of the required tool(s).

Note that  `aclocal' is provided  by the `automake' package  on Linux,
and that `libtoolize' is called `glibtoolize' on Darwin (OS X).


For static builds which  don't use platform specific optimizations, no
configure script is necessary at all; saying

  make setup ansi
  make

should work on all platforms which have GNU make (or makepp).


Similarly, a  build with  `cmake' can  be done  directly from  the git
repository.


----------------------------------------------------------------------

Copyright 2005-2010, 2013 by
David Turner, Robert Wilhelm, and Werner Lemberg.

This  file is  part of  the FreeType  project, and  may only  be used,
modified,  and distributed  under the  terms of  the  FreeType project
license,  LICENSE.TXT.  By  continuing to  use, modify,  or distribute
this file you  indicate that you have read  the license and understand
and accept it fully.


--- end of README.git ---
                  FreeType font driver for BDF fonts

                       Francesco Zappa Nardelli
                  <francesco.zappa.nardelli@ens.fr>


Introduction
************

BDF (Bitmap Distribution Format) is a bitmap font format defined by Adobe,
which is intended to be easily understood by both humans and computers.
This code implements a BDF driver for the FreeType library, following the
Adobe Specification V 2.2.  The specification of the BDF font format is
available from Adobe's web site:

  http://partners.adobe.com/public/developer/en/font/5005.BDF_Spec.pdf

Many good bitmap fonts in bdf format come with XFree86 (www.XFree86.org).
They do not define vertical metrics, because the X Consortium BDF
specification has removed them.


Encodings
*********

The variety of encodings that accompanies bdf fonts appears to encompass the
small set defined in freetype.h.  On the other hand, two properties that
specify encoding and registry are usually defined in bdf fonts.

I decided to make these two properties directly accessible, leaving to the
client application the work of interpreting them.  For instance:


  #include FT_INTERNAL_BDF_TYPES_H

  FT_Face          face;
  BDF_Public_Face  bdfface;


  FT_New_Face( library, ..., &face );

  bdfface = (BDF_Public_Face)face;

  if ( ( bdfface->charset_registry == "ISO10646" ) &&
       ( bdfface->charset_encoding == "1" )        )
    [..]


Thus the driver always exports `ft_encoding_none' as face->charmap.encoding.
FT_Get_Char_Index's behavior is unmodified, that is, it converts the ULong
value given as argument into the corresponding glyph number.

If the two properties are not available, Adobe Standard Encoding should be
assumed.


Anti-Aliased Bitmaps
********************

The driver supports an extension to the BDF format as used in Mark Leisher's
xmbdfed bitmap font editor.  Microsoft's SBIT tool expects bitmap fonts in
that format for adding anti-aliased them to TrueType fonts.  It introduces a
fourth field to the `SIZE' keyword which gives the bpp value (bits per
pixel) of the glyph data in the font.  Possible values are 1 (the default),
2 (four gray levels), 4 (16 gray levels), and 8 (256 gray levels).  The
driver returns either a bitmap with 1 bit per pixel or a pixmap with 8bits
per pixel (using 4, 16, and 256 gray levels, respectively).


Known problems
**************

- A font is entirely loaded into memory.  Obviously, this is not the Right
  Thing(TM).  If you have big fonts I suggest you convert them into PCF
  format (using the bdftopcf utility): the PCF font drive of FreeType can
  perform incremental glyph loading.

When I have some time, I will implement on-demand glyph parsing.

- Except for encodings properties, client applications have no visibility of
  the PCF_Face object.  This means that applications cannot directly access
  font tables and must trust FreeType.

- Currently, glyph names are ignored.

  I plan to give full visibility of the BDF_Face object in an upcoming
  revision of the driver, thus implementing also glyph names.

- As I have never seen a BDF font that defines vertical metrics, vertical
  metrics are (parsed and) discarded.  If you own a BDF font that defines
  vertical metrics, please let me know (I will implement them in 5-10
  minutes).


License
*******

Copyright (C) 2001-2002 by Francesco Zappa Nardelli

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*** Portions of the driver (that is, bdflib.c and bdf.h):

Copyright 2000 Computing Research Labs, New Mexico State University
Copyright 2001-2002, 2011 Francesco Zappa Nardelli

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
THE COMPUTING RESEARCH LAB OR NEW MEXICO STATE UNIVERSITY BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Credits
*******

This driver is based on excellent Mark Leisher's bdf library.  If you
find something good in this driver you should probably thank him, not
me.
gxvalid: TrueType GX validator
==============================


1. What is this
---------------

  `gxvalid' is a module to  validate TrueType GX tables: a collection of
  additional tables  in TrueType  font which are  used by  `QuickDraw GX
  Text',  Apple Advanced  Typography  (AAT).  In  addition, gxvalid  can
  validates `kern'  tables which have  been extended for AAT.   Like the
  otvalid  module,   gxvalid  uses  Freetype   2's  validator  framework
  (ftvalid).

  You can link gxvalid with your program; before running your own layout
  engine, gxvalid validates a font  file.  As the result, you can remove
  error-checking code  from the layout  engine.  It is also  possible to
  use  gxvalid  as a  stand-alone  font  validator;  the `ftvalid'  test
  program  included  in the  ft2demo  bundle  calls gxvalid  internally.
  A stand-alone font validator may be useful for font developers.

  This documents documents the following issues.

  - supported TrueType GX tables
  - fundamental validation limitations
  - permissive error handling of broken GX tables
  - `kern' table issue.


2. Supported tables
-------------------

  The following GX tables are currently supported.

    bsln
    feat
    just
    kern(*)
    lcar
    mort
    morx
    opbd
    prop
    trak

  The following GX tables are currently unsupported.

    cvar
    fdsc
    fmtx
    fvar
    gvar
    Zapf

  The following GX tables won't be supported.

    acnt(**)
    hsty(***)

  The following undocumented tables in TrueType fonts designed for Apple
  platform aren't handled either.

    addg
    CVTM
    TPNM
    umif


  *)   The `kern'  validator handles both  the classic and the  new kern
       formats;  the former  is supported  on both  Microsoft  and Apple
       platforms, while the latter is supported on Apple platforms.

  **)  `acnt' tables are not supported by currently available Apple font
       tools.

  ***) There  is  one more  Apple  extension,  `hsty',  but  it  is  for
       Newton-OS, not GX  (Newton-OS is a platform by  Apple, but it can
       use  sfnt- housed bitmap  fonts only).   Therefore, it  should be
       excluded  from  `Apple  platform'  in the  context  of  TrueType.
       gxvalid ignores it as Apple font tools do so.


  We have  checked 183  fonts bundled with  MacOS 9.1, MacOS  9.2, MacOS
  10.0, MacOS X 10.1, MSIE  for MacOS, and AppleWorks 6.0.  In addition,
  we have  checked 67 Dynalab fonts  (designed for MacOS)  and 189 Ricoh
  fonts (designed for Windows and  MacOS dual platforms).  The number of
  fonts including TrueType GX tables are as follows.

    bsln:  76
    feat: 191
    just:  84
    kern:  59
    lcar:   4
    mort: 326
    morx:  19
    opbd:   4
    prop: 114
    trak:  16

  Dynalab  and Ricoh fonts  don't have  GX tables  except of  `feat' and
  `mort'.


3. Fundamental validation limitations
-------------------------------------

  TrueType  GX  provides  layout   information  to  libraries  for  font
  rasterizers  and text layout.   gxvalid can  check whether  the layout
  data in  a font is conformant  to the TrueType GX  format specified by
  Apple.  But gxvalid cannot check  a how QuickDraw GX/AAT renderer uses
  the stored information.

  3-1. Validation of State Machine activity
  -----------------------------------------

    QuickDraw GX/AAT uses a `State Machine' to provide `stateful' layout
    features,  and TrueType GX  stores the  state transition  diagram of
    this `State  Machine' in a  `StateTable' data structure.   While the
    State  Machine receives  a series  of glyph  IDs, the  State Machine
    starts with `start  of text' state, walks around  various states and
    generates various  layout information  to the  renderer, and finally
    reaches the `end of text' state.

    gxvalid can check essential errors like:

      - possibility of state transitions to undefined states
      - existence of glyph  IDs that the State Machine  doesn't know how
        to handle
      - the  State Machine  cannot compute  the layout  information from
        given diagram

    These errors  can be  checked within finite  steps, and  without the
    State Machine itself, because these are `expression' errors of state
    transition diagram.

    There  is no  limitation  about  how long  the  State Machine  walks
    around,  so validation  of  the algorithm  in  the state  transition
    diagram requires infinite  steps, even if we had  a State Machine in
    gxvalid.   Therefore, the  following errors  and problems  cannot be
    checked.

      - existence of states which the State Machine never transits to
      - the  possibility that the  State Machine  never reaches  `end of
        text'
      - the possibility of stack underflow/overflow in the State Machine
        (in  ligature  and  contextual  glyph substitutions,  the  State
        Machine can store 16 glyphs onto its stack)

    In addition, gxvalid doesn't check `temporary glyph IDs' used in the
    chained State Machines  (in `mort' and `morx' tables).   If a layout
    feature  is  implemented by  a  single  State  Machine, a  glyph  ID
    converted by the State Machine is passed to the glyph renderer, thus
    it  should not  point to  an undefined  glyph ID.   But if  a layout
    feature is implemented by  chained State Machines, a component State
    Machine  (if it  is  not the  final  one) is  permitted to  generate
    undefined glyph IDs for temporary use, because it is handled by next
    component State Machine and not  by the glyph renderer.  To validate
    such temporary glyph IDs, gxvalid must stack all undefined glyph IDs
    which  can occur in  the output  of the  previous State  Machine and
    search  them in  the  `ClassTable' structure  of  the current  State
    Machine.  It is too complex to  list all possible glyph IDs from the
    StateTable, especially from a ligature substitution table.

  3-2. Validation of relationship between multiple layout features
  ----------------------------------------------------------------

    gxvalid does  not validate the relationship  between multiple layout
    features at all.

    If  multiple layout  features  are defined  in  TrueType GX  tables,
    possible  interactions,  overrides,  and  conflicts  between  layout
    features are implicitly  given in the font too.   For example, there
    are several predefined spacing control features:

      - Text Spacing          (Proportional/Monospace/Half-width/Normal)
      - Number Spacing        (Monospaced-numbers/Proportional-numbers)
      - Kana Spacing          (Full-width/Proportional)
      - Ideographic Spacing   (Full-width/Proportional)
      - CJK Roman Spacing     (Half-width/Proportional/Default-roman
                               /Full-width-roman/Proportional)

    If all  layout features are  independently managed, we  can activate
    inconsistent  typographic rules  like  `Text Spacing=Monospace'  and
    `Ideographic Spacing=Proportional' at the same time.

    The combinations  of layout features  is managed by a  32bit integer
    (one bit each for selector  setting), so we can define relationships
    between  up  to 32  features,  theoretically.   But  if one  feature
    setting  affects  another   feature  setting,  we  need  typographic
    priority  rules to  validate the  relationship.   Unfortunately, the
    TrueType GX format specification does not give such information even
    for predefined features.


4. Permissive error handling of broken GX tables
------------------------------------------------

  When  Apple's font  rendering system  finds an  inconsistency,  like a
  specification  violation or  an  unspecified value  in  a TrueType  GX
  table, it does not always  return error.  In most cases, the rendering
  engine silently  ignores such wrong  values or even whole  tables.  In
  fact, MacOS is shipped with  fonts including broken GX/AAT tables, but
  no harmful  effects due to  `officially broken' fonts are  observed by
  end-users.

  gxvalid  is designed  to continue  the validation  process as  long as
  possible.  When gxvalid find wrong  values, gxvalid warns it at least,
  and takes  a fallback procedure  if possible.  The  fallback procedure
  depends on the debug level.

  We used the following three tools to investigate Apple's error handling.

    - FontValidator  (for MacOS 8.5 - 9.2)  resource fork font
    - ftxvalidator   (for MacOS X 10.1 -)   dfont or naked-sfnt
    - ftxdumperfuser (for MacOS X 10.1 -)   dfont or naked-sfnt

  However, all tests were done on a PowerPC based Macintosh; at present,
  we have not checked those tools on a m68k-based Macintosh.

  In total, we checked 183 fonts  bundled to MacOS 9.1, MacOS 9.2, MacOS
  10.0, MacOS X  10.1, MSIE for MacOS, and  AppleWorks 6.0.  These fonts
  are distributed  officially, but many broken GX/AAT  tables were found
  by Apple's font tools.  In the following, we list typical violation of
  the GX specification, in fonts officially distributed with those Apple
  systems.

  4-1. broken BinSrchHeader (19/183)
  ----------------------------------

    `BinSrchHeader' is  a header of a  data array for  m68k platforms to
    access memory efficiently.  Although  there are only two independent
    parameters  for real  (`unitSize' and  `nUnits'),  BinSrchHeader has
    three additional parameters which  can be calculated from `unitSize'
    and  `nUnits',  for  fast  setup.   Apple  font  tools  ignore  them
    silently, so gxvalid warns if it finds and inconsistency, and always
    continues  validation.    The  additional  parameters   are  ignored
    regardless of the consistency.

      19  fonts include  such  inconsistencies; all  breaks  are in  the
      BinSrchHeader structure of the `kern' table.

  4-2. too-short LookupTable (5/183)
  ----------------------------------

    LookupTable format 0  is a simple array to get a  value from a given
    GID (glyph  ID); the index of  this array is a  GID too.  Therefore,
    the length  of the array is expected  to be same as  the maximum GID
    value defined  in the `maxp' table,  but there are  some fonts whose
    LookupTable format 0 is too  short to cover all GIDs.  FontValidator
    ignores  this error silently,  ftxvalidator and  ftxdumperfuser both
    warn and continue.  Similar problems are found in format 3 subtables
    of `kern'.  gxvalid  warns always and abort if  the validation level
    is set to FT_VALIDATE_PARANOID.

      5 fonts include too-short kern format 0 subtables.
      1 font includes too-short kern format 3 subtable.

  4-3. broken LookupTable format 2 (1/183)
  ----------------------------------------

    LookupTable  format  2,  subformat  4  covers the  GID  space  by  a
    collection  of  segments which  are  specified  by `firstGlyph'  and
    `lastGlyph'.   Some  fonts  store  `firstGlyph' and  `lastGlyph'  in
    reverse order,  so the segment specification is  broken.  Apple font
    tools ignore this error silently;  a broken segment is ignored as if
    it  did not  exist.   gxvalid  warns and  normalize  the segment  at
    FT_VALIDATE_DEFAULT, or ignore  the segment at FT_VALIDATE_TIGHT, or
    abort at FT_VALIDATE_PARANOID.

      1 font includes broken LookupTable format 2, in the `just' table.

    *) It seems  that all fonts manufactured by  ITC for AppleWorks have
       this error.

  4-4. bad bracketing in glyph property (14/183)
  ----------------------------------------------

    GX/AAT defines a  `bracketing' property of the glyphs  in the `prop'
    table,  to control layout  features of  strings enclosed  inside and
    outside  of   brackets.   Some  fonts   give  inappropriate  bracket
    properties  to glyphs.   Apple  font tools  warn  about this  error;
    gxvalid warns too and aborts at FT_VALIDATE_PARANOID.

      14 fonts include wrong bracket properties.


  4-5. invalid feature number (117/183)
  -------------------------------------

    The GX/AAT extension can  include 255 different layout features, but
    popular      layout      features      are      predefined      (see
    http://developer.apple.com/fonts/Registry/index.html).   Some  fonts
    include feature  numbers which are incompatible  with the predefined
    feature registry.

    In our survey, there are 140 fonts including `feat' table.

    a) 67 fonts use a feature number which should not be used.
    b) 117 fonts set the wrong feature range (nSetting).  This is mostly
       found in the `mort' and `morx' tables.

    Apple  font tools give  no warning,  although they  cannot recognize
    what  the feature  is.   At FT_VALIDATE_DEFAULT,  gxvalid warns  but
    continues in both cases (a, b).  At FT_VALIDATE_TIGHT, gxvalid warns
    and aborts for (a), but continues for (b).  At FT_VALIDATE_PARANOID,
    gxvalid warns and aborts in both cases (a, b).

  4-6. invalid prop version (10/183)
  ----------------------------------

    As most TrueType GX tables, the `prop' table must start with a 32bit
    version identifier: 0x00010000,  0x00020000 or 0x00030000.  But some
    fonts  store nonsense binary  data instead.   When Apple  font tools
    find them, they abort the processing immediately, and the data which
    follows is unhandled.  gxvalid does the same.

      10 fonts include broken `prop' version.

    All  of these  fonts are  classic  TrueType fonts  for the  Japanese
    script, manufactured by Apple.

  4-7. unknown resource name (2/183)
  ------------------------------------

    NOTE: THIS IS NOT A TRUETYPE GX ERROR.

    If  a TrueType  font is  stored  in the  resource fork  or in  dfont
    format, the data must be tagged as `sfnt' in the resource fork index
    to invoke TrueType font handler for the data.  But the TrueType font
    data  in   `Keyboard.dfont'  is  tagged   as  `kbd',  and   that  in
    `LastResort.dfont' is tagged as  `lst'.  Apple font tools can detect
    that the data is in  TrueType format and successfully validate them.
    Maybe  this is possible  because they  are known  to be  dfont.  The
    current  implementation  of the  resource  fork  driver of  FreeType
    cannot do that, thus gxvalid cannot validate them.

      2 fonts use an unknown tag for the TrueType font resource.

5. `kern' table issues
----------------------

  In common terminology of TrueType, `kern' is classified as a basic and
  platform-independent table.  But there are Apple extensions of `kern',
  and  there is  an  extension which  requires  a GX  state machine  for
  contextual kerning.   Therefore, gxvalid includes  a special validator
  for  `kern' tables.   Unfortunately, there  is no  exact  algorithm to
  check Apple's extension, so  gxvalid includes a heuristic algorithm to
  find  the proper validation  routines for  all possible  data formats,
  including    the   data    format   for    Microsoft.     By   calling
  classic_kern_validate() instead of gxv_validate(), you can specify the
  `kern' format  explicitly.  However, current  FreeType2 uses Microsoft
  `kern' format  only, others  are ignored (and  should be handled  in a
  library one level higher than FreeType).

  5-1. History
  ------------

    The original  16bit version of `kern'  was designed by  Apple in the
    pre-GX  era, and  it was  also approved  by  Microsoft.  Afterwards,
    Apple designed a  new 32bit version of the  `kern' table.  According
    to  the documentation, the  difference between  the 16bit  and 32bit
    version is only the size of  variables in the `kern' header.  In the
    following,  we call  the original  16bit version  as  `classic', and
    32bit version as `new'.

  5-2. Versions and dialects which should be differentiated
  ---------------------------------------------------------

    The `kern' table  consists of a table header  and several subtables.
    The version number  which identifies a `classic' or  a `new' version
    is  explicitly   written  in  the   table  header,  but   there  are
    undocumented  differences between  Microsoft's and  Apple's formats.
    It is  called a `dialect' in  the following.  There  are three cases
    which  should  be  handled:   the  new  Apple-dialect,  the  classic
    Apple-dialect,  and the classic  Microsoft-dialect.  An  analysis of
    the formats and the auto detection algorithm of gxvalid is described
    in the following.

    5-2-1. Version detection: classic and new kern
    ----------------------------------------------

      According  to Apple  TrueType  specification, there  are only  two
      differences between the classic and the new:

        - The `kern' table header starts with the version number.
          The classic version starts with 0x0000 (16bit),
          the new version starts with 0x00010000 (32bit).

        - In the  `kern' table header,  the number of  subtables follows
          the version number.
          In the classic version, it is stored as a 16bit value.
          In the new version, it is stored as a 32bit value.

      From Apple font tool's output (DumpKERN is also tested in addition
      to  the  three  Apple  font  tools in  above),  there  is  another
      undocumented difference.  In the  new version, the subtable header
      includes a 16bit variable  named `tupleIndex' which does not exist
      in the classic version.

      The new version  can store all subtable formats (0,  1, 2, and 3),
      but the Apple TrueType specification does not mention the subtable
      formats available in the classic version.

    5-2-2. Available subtable formats in classic version
    ----------------------------------------------------

      Although the  Apple TrueType  specification recommends to  use the
      classic version in  the case if the font is  designed for both the
      Apple and Microsoft platforms,  it does not document the available
      subtable formats in the classic version.

      According  to the Microsoft  TrueType specification,  the subtable
      format  assured for  Windows  and OS/2  support  is only  subtable
      format  0.  The  Microsoft TrueType  specification  also describes
      subtable format  2, but does  not mention which  platforms support
      it.  Aubtable formats 1, 3,  and higher are documented as reserved
      for future use.  Therefore, the classic version can store subtable
      formats 0 and 2, at least.  `ttfdump.exe', a font tool provided by
      Microsoft,  ignores the  subtable format  written in  the subtable
      header, and parses the table as if all subtables are in format 0.

      `kern'  subtable format  1  uses  a StateTable,  so  it cannot  be
      utilized without a GX  State Machine.  Therefore, it is reasonable
      to assume  that format 1 (and  3) were introduced  after Apple had
      introduced GX and moved to the new 32bit version.

    5-2-3. Apple and Microsoft dialects
    -----------------------------------

      The  `kern' subtable  has  a 16bit  `coverage'  field to  describe
      kerning attributes, but bit interpretations by Apple and Microsoft
      are different:  For example, Apple  uses bits 0-7 to  identify the
      subtable, while Microsoft uses bits 8-15.

      In  addition, due  to the  output of  DumpKERN  and FontValidator,
      Apple's bit interpretations of coverage in classic and new version
      are  incompatible also.   In  summary, there  are three  dialects:
      classic Apple  dialect, classic  Microsoft dialect, and  new Apple
      dialect.  The classic Microsoft  dialect and the new Apple dialect
      are documented  by each vendors' TrueType  font specification, but
      the documentation for classic Apple dialect is not available.

      For example,  in the  new Apple dialect,  bit 15 is  documented as
      `set to  1 if  the kerning  is vertical'.  On  the other  hand, in
      classic Microsoft dialect, bit 1 is documented as `set to 1 if the
      kerning  is  horizontal'.   From   the  outputs  of  DumpKERN  and
      FontValidator, classic  Apple dialect recognizes  15 as `set  to 1
      when  the kerning  is horizontal'.   From the  results  of similar
      experiments, classic Apple dialect  seems to be the Endian reverse
      of the classic Microsoft dialect.

      As a  conclusion it must be  noted that no font  tool can identify
      classic Apple dialect or classic Microsoft dialect automatically.

    5-2-4. gxvalid auto dialect detection algorithm
    -----------------------------------------------

      The first 16  bits of the `kern' table are  enough to identify the
      version:

        - if  the first  16  bits are  0x0000,  the `kern'  table is  in
          classic Apple dialect or classic Microsoft dialect
        - if the first 16 bits are  0x0001, and next 16 bits are 0x0000,
          the kern table is in new Apple dialect.

      If the `kern'  table is a classic one,  the 16bit `coverage' field
      is checked next.   Firstly, the coverage bits are  decoded for the
      classic Apple dialect using the following bit masks (this is based
      on DumpKERN output):

        0x8000: 1=horizontal, 0=vertical
        0x4000: not used
        0x2000: 1=cross-stream, 0=normal
        0x1FF0: reserved
        0x000F: subtable format

      If  any  of  reserved  bits  are  set  or  the  subtable  bits  is
      interpreted as format 1 or 3, we take it as `impossible in classic
      Apple dialect' and retry, using the classic Microsoft dialect.

        The most popular coverage in new Apple-dialect:         0x8000,
        The most popular coverage in classic Apple-dialect:     0x0000,
        The most popular coverage in classic Microsoft dialect: 0x0001.

  5-3. Tested fonts
  -----------------

    We checked  59 fonts  bundled with MacOS  and 38 fonts  bundled with
    Windows, where all font include a `kern' table.

      - fonts bundled with MacOS
        * new Apple dialect
          format 0: 18
          format 2:  1
          format 3:  1
        * classic Apple dialect
          format 0: 14
        * classic Microsoft dialect
          format 0: 15

      - fonts bundled with Windows
        * classic Microsoft dialect
          format 0: 38

    It looks strange that classic Microsoft-dialect fonts are bundled to
    MacOS: they come from MSIE for MacOS, except of MarkerFelt.dfont.


  ACKNOWLEDGEMENT
  ---------------

  Some parts of gxvalid are  derived from both the `gxlayout' module and
  the `otvalid'  module.  Development of  gxlayout was supported  by the
  Information-technology Promotion Agency(IPA), Japan.

  The detailed analysis of undefined  glyph ID utilization in `mort' and
  `morx' tables is provided by George Williams.

------------------------------------------------------------------------

Copyright 2004, 2005, 2007 by
suzuki toshiya, Masatake YAMATO, Red hat K.K.,
David Turner, Robert Wilhelm, and Werner Lemberg.

This  file is  part  of the  FreeType  project, and  may  only be  used,
modified,  and  distributed under  the  terms  of  the FreeType  project
license, LICENSE.TXT.  By continuing  to use, modify, or distribute this
file  you indicate that  you have  read the  license and  understand and
accept it fully.


--- end of README ---
                  FreeType font driver for PCF fonts

                       Francesco Zappa Nardelli
                  <francesco.zappa.nardelli@ens.fr>


Introduction
************

PCF (Portable Compiled Format) is a binary bitmap font format, largely used
in X world. This code implements a PCF driver for the FreeType library.
Glyph images are loaded into memory only on demand, thus leading to a small
memory footprint.

Information on the PCF font format can only be worked out from
`pcfread.c', and `pcfwrite.c', to be found, for instance, in the XFree86
(www.xfree86.org) source tree (xc/lib/font/bitmap/).

Many good bitmap fonts in bdf format come with XFree86: they can be
compiled into the pcf format using the `bdftopcf' utility.


Supported hardware
******************

The driver has been tested on linux/x86 and sunos5.5/sparc.  In both
cases the compiler was gcc.  When back in Paris, I will test it also
on linux/alpha.


Encodings
*********

Use `FT_Get_BDF_Charset_ID' to access the encoding and registry.

The driver always exports `ft_encoding_none' as face->charmap.encoding.
FT_Get_Char_Index() behavior is unmodified, that is, it converts the ULong
value given as argument into the corresponding glyph number.


Known problems
**************

- dealing explicitly with encodings breaks the uniformity of freetype2
  api.

- except for encodings properties, client applications have no
  visibility of the PCF_Face object.  This means that applications
  cannot directly access font tables and are obliged to trust
  FreeType.

- currently, glyph names and ink_metrics are ignored.

I plan to give full visibility of the PCF_Face object in the next
release of the driver, thus implementing also glyph names and
ink_metrics.

- height is defined as (ascent - descent).  Is this correct?

- if unable to read size information from the font, PCF_Init_Face
  sets available_size->width and available_size->height to 12.

- too many english grammar errors in the readme file :-(


License
*******

Copyright (C) 2000 by Francesco Zappa Nardelli

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Credits
*******

Keith Packard wrote the pcf driver found in XFree86.  His work is at
the same time the specification and the sample implementation of the
PCF format.  Undoubtedly, this driver is inspired from his work.
ftrandom
--------

This program expects a set of directories containing good fonts, and a set
of extensions of fonts to be tested.  It will randomly pick a font, copy it,
introduce and error and then test it.

The FreeType tests are quite basic:

  For each erroneous font it
    forks off a new tester;
    initializes the library;
    opens each font in the file;
    loads each glyph;
      (optionally reviewing the contours of the glyph)
      (optionally rasterizing)
    closes the face.

If the tester exits with a signal, or takes longer than 20 seconds then
ftrandom saves the erroneous font and continues.  If the tester exits
normally or with an error, then the superstructure removes the test font and
continues.

Arguments are:

  --all                    Test every font in the directory(ies) no matter
                           what its extension (some CID-keyed fonts have no
                           extension).
  --check-outlines         Call FT_Outline_Decompose on each glyph.
  --dir <dir>              Append <dir> to the list of directories to search
                           for good fonts.
  --error-count <cnt>      Introduce <cnt> single-byte errors into the
                           erroneous fonts.
  --error-fraction <frac>  Multiply the file size of the font by <frac> and
                           introduce that many errors into the erroneous
                           font file.
  --ext <ext>              Add <ext> to the set of font types tested.  Known
                           extensions are `ttf', `otf', `ttc', `cid', `pfb',
                           `pfa', `bdf', `pcf', `pfr', `fon', `otb', and
                           `cff'.
  --help                   Print out this list of options.
  --nohints                Specify FT_LOAD_NO_HINTING when loading glyphs.
  --rasterize              Call FT_Render_Glyph as well as loading it.
  --result <dir>           This is the directory in which test files are
                           placed.
  --test <file>            Run a single test on a pre-generated testcase.
                           Done in the current process so it can be debugged
                           more easily.
This is a combined SDK that includes both the Google Analytics SDK
and the Google Tag Manager SDK.

The libGoogleAnalyticsServices.a library contains code for both.
Within the subdirectories, you can find header files and documentation
for each.

The libAdIdAccess.a library contains functions that call the AdSupport
framework. If you would like your application to access the identifier for
advertisers (IDFA) and tracking flag provided by that framework through the
Google Tag Manager SDK macros, you will also need to add this library to your
XCode project.
Google Analytics SDK for iOS Changelog
--------------------------------------------
Version: 3.17 (September 2016)
--------------------------------------------
* Fixed crash in GAITrackerModel on iOS 10.

--------------------------------------------
Version: 3.16 (July 2016)
--------------------------------------------
* Fixed bad memory access crash under rare conditions.

--------------------------------------------
Version: 3.15 (November 2015)
--------------------------------------------
* No change.

--------------------------------------------
Version: 3.14 (October 2015)
--------------------------------------------
* Added support for bitcode.

--------------------------------------------
Version: 3.13 (July 2015)
--------------------------------------------
* Fixed an issue which caused crashes when using setCampaignParametersFromUrl.

--------------------------------------------
Version: 3.12 (April 2015)
--------------------------------------------
* No change.

--------------------------------------------
Version: 3.11 (April 2015)
--------------------------------------------
* Report screen resolution using nativeBounds on iOS 8.0 and newer.
* Added support for click-related campaign parameters.
* Report iOS hardware model in addition to the device OS version.
* Report iAd install attribution on iOS 7.1 and newer. This requires the iAd framework.
* Added deprecation warning for the appview hit type.
* sqlite3 is now a required library.

--------------------------------------------
Version: 3.10 (November 2014)
--------------------------------------------
* Fixed an issue which prevented all beacons from being sent when dispatching
  beacons.
* Updated CuteAnimals sample application to demonstrate how to dispatch when
  the app goes into the background.
* Added support for additional Enhanced Ecommerce fields.
* Removed warning messages about GAIHit and GAIProperty classes missing when
  compiling against iOS SDK 8.0; those classes were removed.
* Dispatching beacons is now more efficient, with multiple beacons being
  dispatched in a single HTTPS request.
* Requests will be compressed to save on data plan usage under certain
  circumstances.

--------------------------------------------
Version: 3.09 (July 2014)
-------------------------------------------
* No change.

--------------------------------------------
Version: 3.08 (June 2014)
-------------------------------------------
* The SDK will now collect IDFA and the advertiser tracking enabled flag if the
  library libAdIdAccess.a (provided as part of the SDK) is included in the
  application and the allowIDFACollection property is set to true on the
  tracker.
* Enhanced Ecommerce support has been added.
* Added screenview hit type to replace appview hit type.
* A hit id parameter is now added to each hit.  It is changed every time an
  appview, screenview or pageview hit is generated.
* ClientId will now be reset every time the idfa value is changes.  This only
  happens when idfa is collected in a tracker.
* A new dispatchWithCompletionHandler method has been added to the GAI class.
* Fixed an issue where the SDK could send a beacon without a clientId or
  with an empty clientId.

--------------------------------------------
Version: 3.07 (May 2014)
-------------------------------------------
* Added User Id field.
* Fixed an issue so GTM users can use NSNumber for ecommerce data.

--------------------------------------------
Version: 3.06 (March 2014)
-------------------------------------------
* SDK will now populate the Application Id parameter (&aid) by default.

--------------------------------------------
Version: 3.03c (February 2014)
-------------------------------------------
* No change.

--------------------------------------------
Version: 3.03b (February 2014)
-------------------------------------------
* No change.

--------------------------------------------
Version: 3.03a (February 2014)
-------------------------------------------
* Removed need for Adsupport.framework.
* Removed unused code.

--------------------------------------------
Version: 3.03 (January 2014)
-------------------------------------------
* Support 64-bit iOS 7.0 SDK.
* Removed libGoogleAnalytics_debug.a, it’s part of the libGoogleAnalyticsServices.a
  library.
* Cleaned up CuteAnimals build file for Google Analytics.

--------------------------------------------
Version: 3.02 (October 2013)
-------------------------------------------
* Fixed conflict with protocol buffer SDK.
* Fixed linker error when code stripping was enabled.

--------------------------------------------
Version: 3.01 (September 2013)
-------------------------------------------
* Fixed link error when targeting iOS 7.0.

--------------------------------------------
Version: 3.00 (August 2013)
-------------------------------------------
* SDK API change to align with analytics.js. The track<hittype> and
  send<hittype> methods have been removed.  Use send and the
  GAIDictionaryBuilder construct methods instead.
* Most properties on the GAITracker protocol have been removed.  Use
  set on the various fields instead.
* All parameters set using the set method will be persisted.  Previously,
  several parameters would only be set for the next send/track call.
* GAILogger protocol is available for those wanting to implement their
  own custom logging for the SDK.
* Minimium system requirements have changed.  See Readme.txt for details.
* All SDK activity (database and network access) is now done on a separate
  thread.
* Clientid can now be read.  Call [tracker get:kGAIClientId].  Note that
  this call will block until the client id can be read from the database.
* SDK no longer uses POST unless the hit is larger than 2000 bytes.  It
  will use GET instead.
* SDK will no longer retry sending hits based off the HTTP response code.

--------------------------------------------
Version: 2.0beta4 Update (Jan 2013)
--------------------------------------------
* Change default appVersion to the value in CFBundleShortVersionString
    instead of CFBundleVersionKey.
* Use HTTPS as the default protocol instead of HTTP.
* Track methods changed to Send (e.g. trackView now called sendView).
* Some minor bug fixes.

--------------------------------------------
Version: 2.0beta3 iOS6 Update (Sep 2012)
--------------------------------------------
* Add armv7s architecture to libGoogleAnalytics.a.
* Remove armv6 architecture from libGoogleAnalytics.a.

--------------------------------------------
Version: 2.0beta3 (Aug 2012)
--------------------------------------------
* Third beta release.
* Added social tracking method to GAITracker:
    trackSocial:withAction:withTarget:
* Timing method signature changed to:
    trackTiming:withValue:withName:withLabel:
* Manual construction and dispatch methods added to GAITracker:
    set:value:
    get:
    send:params:
* Custom dimension setter methods added to GAITracker:
    setCustom:dimension:
    setCustom:metric:
* Architecture of data store refactored to prevent reported CoreData issues.

--------------------------------------------
Version: 2.0beta2 (Jun 2012)
--------------------------------------------
* Second beta release.
* Updated to latest wire format.
* sampleRate changed to double-precision float.
* Excessive tracking is throttled.
* Undispatched tracking information is deleted when opt-out is enabled.
* Undispatched tracking information older than 30 days will be deleted.
* Enhancements to hit dispatcher.
* Rather than periodically retry, the dispatcher will use the Reachability API
  when connectivity is lost to get notified when connectivity is reestablished.
* Updated example app.
* Other bugfixes and enhancements.

--------------------------------------------
Version: 2.0beta1 (May 2012)
--------------------------------------------
* Initial internal beta release.
* Added uncaught exception handling facility.
* Removed 'dispatchEnabled' property from GAI.
* Added 'defaultTracker' property to GAI.
* Added 'close' method to GAITracker.
* Added timing tracking method to GAITracker.
* Added trackView method to GAITracker which takes no argument.
* Transaction item field names updated.
* Updated to latest wire format.
* Event value is interpreted as a 64-bit integer.
* ARMV6 code generation switched from THUMB to ARM.

--------------------------------------------
Version: 2.0alpha1 (April 2012)
--------------------------------------------
* Initial internal alpha release.
Google Analytics iOS SDK version 3.17
Copyright 2009 - 2015 Google, Inc. All rights reserved.

================================================================================
DESCRIPTION:

This SDK provides developers with the capability to use Google Analytics
to track iOS application usage.

The SDK is packaged as a set of header files and a static library. Get started
by adding the header files from the Library subdirectory (GAI.h,
GAIDictionaryBuilder.h, etc.) and libGoogleAnalyticsServices.a to your XCode
project.  See below for a list of frameworks/libraries required by this SDK.

See the Examples/CuteAnimals application for an illustration of how to use
automatic screen tracking, event tracking, background dispatching, and uncaught
exception tracking.

You will need a Google Analytics tracking ID to track application usage with the
SDK. It is recommended to create an account for each set of applications that
are to be tracked together, and to use that account's tracking ID in each
application. To create a new tracking ID, go to your admin panel in Google
Analytics and select "New Account". Under "What would you like to track?",
choose "App" and complete the remainder of the form. When you are finished,
click "Get Tracking ID". The tracking ID will be of the form "UA-" followed by a
sequence of numbers and dashes.

You must indicate to your users, either in the app itself or in your terms of
service, that you reserve the right to anonymously track and report a user's
activity inside of your app.

If you wish to enable any Google Analytics features that require idfa
collection, you'll need to link in the additional library libAdIdAccess.a
(provided in this SDK) and add AdSupport.framework to your application.  In
addition, the linker flag:

   -force_load /path/to/libAdIdAccess.a

may be required, depending on your build settings. Finally, you need to set the
property allowIDFACollection to YES on each tracker that will collect idfa.

If you wish to enable iAd install attribution, you'll need to add iAd.framework
to your application.

Implementation Details:

Tracking information is stored in an SQLite database and dispatched to the
Google Analytics servers in a manner set by the developer: periodically at an
interval determined by the developer, immediately when tracking calls are made,
or manually. A battery efficient strategy may be to initiate a dispatch when the
application needs to access the network. Tracking information is dispatched
using HTTP or HTTPS requests to a Google Analytics server.

================================================================================
BUILD REQUIREMENTS:

Mac OS X 10.6 or later.
XCode 5.0 or later
iOS SDK 5.0 or later (6.0 or later for 64-bit).

================================================================================
RUNTIME REQUIREMENTS:

iOS 5.0 or later.

Your app must link the following frameworks:
  CoreData.framework
  SystemConfiguration.framework
  libz.dylib
  libsqlite3.dylib

================================================================================
PACKAGING LIST:

Library/ (contains header and library files to compile and link with)
  GAI.h
  GAIDictionaryBuilder.h
  GAIEcommerceFields.h
  GAIEcommerceProduct.h
  GAIEcommerceProductAction.h
  GAIEcommercePromotion.h
  GAIFields.h
  GAILogger.h
  GAITrackedViewController.h
  GAITracker.h
Examples/ (contains an example tracked application)
Documentation/ (contains documentation)

================================================================================
Google Tag Manager SDK for iOS Changelog
--------------------------------------------
Version: 3.17 (September 2016)
--------------------------------------------
* No Changes.

--------------------------------------------
Version: 3.16 (July 2016)
--------------------------------------------
* No Changes.

--------------------------------------------
Version: 3.15 (November 2015)
--------------------------------------------
* Removed UIViewController category implementation causing issues with Xcode 7 unit testing.

--------------------------------------------
Version: 3.14 (October 2015)
--------------------------------------------
* Added support for bitcode.

--------------------------------------------
Version: 3.13 (July 2015)
--------------------------------------------
* No Changes.

--------------------------------------------
Version: 3.12 (April 2015)
--------------------------------------------
* Fixed a class name conflict.

--------------------------------------------
Version: 3.11 (April 2015)
--------------------------------------------
* Fixed a nil string crash in TAGDispatcher.

--------------------------------------------
Version: 3.10 (November, 2014)
--------------------------------------------
* Deprecate TAGContainerFuture based openContainerWithId.  Using this
  API on iOS8 results in errors if the get is called during some phases
  of the UIAppDelegate lifecycle.
* Added support for custom metrics and custom dimensions to
  Enhanced Ecommerce for the Google Universal Analytics tag.
* Fixed a bug which required products for Enhanced Ecommerce
  actions that have optional products.
* Support Advertising ID Features for the Google Universal Analytics tag.
* Updated CuteAnimals sample application to demonstrate how to send data
  when the app is going into the background.

--------------------------------------------
Version: 3.09 (July, 2014)
--------------------------------------------
* Added support for Enhanced Ecommerce to Google Universal Analytics tag.
* Added dispatch: and dispatchWithCompletionHandler: method to TAGManager to
  support sending pending network traffic on demand.

--------------------------------------------
Version: 3.08 (June, 2014)
--------------------------------------------
* No Changes

--------------------------------------------
Version: 3.07 (May, 2014)
--------------------------------------------
* Fixed a bug in Id for Advertising Macro so that it can correctly
  return identifier for advertiser(IDFA) if available.
* Fixed an issue so users can use NSNumber for ecommerce data.

--------------------------------------------
Version: 3.06 (March, 2014)
--------------------------------------------
* Added support for Google Analytics Content Experiments Macro.

--------------------------------------------
Version: 3.03c (February, 2014)
--------------------------------------------
* Functions that call AdSupport.framework API are broken out into a separate
  library, libAdIdAccess.a. Apps need to link with that library to have access
  to the advertising identifier (IDFA) string and advertiser tracking enabled
  flag.

--------------------------------------------
Version: 3.03a (February, 2014)
--------------------------------------------
* No Changes.

--------------------------------------------
Version: 3.03 (January, 2014)
--------------------------------------------
* Added support for 64-bit iOS SDK 7.0.

--------------------------------------------
Version: 3.02 (October, 2013)
--------------------------------------------
* Fixed conflict with Google Games SDK and protocol buffer SDK.
* Fixed linker error when code stripping was enabled.
* Updated the example application to include new needed library libz.dylib.

--------------------------------------------
Version: 3.01 (September, 2013)
--------------------------------------------
* Fixed link error when targeting iOS 7.0

--------------------------------------------
Version: 3.0 (August 16, 2013)
--------------------------------------------
* Added support for AdWords Conversion Tracking Tag, AdWords Remarketing Tag,
  and Custom Image Tag.

* Added Advertising Enabled Macro, Application ID Macro, and ID for
  Advertising Macro.

* Pushing a link to the data layer as "gtm.url" will now cache the
  Click Referrer for AdWords Tags.

* Updated cuteAnimals sample app to demonstrate how to use Function Call Macro
  and Function Call Tag.

--------------------------------------------
Version: 3.0b1 (July 26, 2013)
--------------------------------------------
* libGoogleAnalyticsServices.a replaces libTagManager.a in the
  downloaded SDK. libGoogleAnalyticsServices.a includes all functions
  in libTagManager.a plus version 3 of the Google Analytics SDK.
  Note that an application can't include both libGoogleAnalyticsServices.a
  and the old libGoogleAnalytics.a or libTagManager.a file.
  An application that wants to use GTM and also do analytics tracking should
  either update their GA calls to use version 3 of the SDK, or replace GA
  calls with data layer push calls and add appropriate rules to their
  container to fire Universal Analytics hits.

* Added Tag support in SDK. There are 2 types of tags currently supported:
  Universal Analytics (beta) tag and Custom Function Tag.

* Added DataLayer support to hold generic information about the application.
  An app can obtain the DataLayer object by calling TagManager::dataLayer.

* Added 2 new macros: data layer variable macro and custom event macro.

* Added LogLevel support into Logger. This allows adjusting the threshold of
  what gets logged without having to write a new logger.

* Added preview exit link support to allow exiting preview mode of a container
  without killing the app.

* Fixed a bug that prevented developers from using both GTM and open-sourced
  proto buffer library.

* Modified the cuteAnimals example to show how to instrument an application
  by pushing events to the data layer. A sample container is provided that
  uses the pushed events to fire Google Universal Analytics tag.

--------------------------------------------
Version: 1.0b3 (June 26, 2013)
--------------------------------------------
* TagManager::openContainer no longer allows opening multiple containers with
  the same container ID.

* ContainerOpener no longer has the two methods
  openNonDefaultContainerWithId:tagManager:timeout:notifier and
  openFreshContainerWithId:tagManager:timeout:notifier:.
  Instead, there are now two openContainer methods:
  openContainerWithId:tagManager:openType:timeout: and
  openContainerWithId:tagManager:openType:timeout:notifier.
  The first returns a TAGContainerFuture, while the other takes a notifier.
  Both of these methods take a parameter specifying how the container should
  be opened (kTAGPreferNonDefault or kTAGPreferFresh).  This should reduce
  confusion as to how TAGContainerFutures and notifiers interact.

  These two new methods can be called more than once with the same
  container ID; if the container is already open, it'll be returned (via the
  future or notifier).

* In container preview mode, containers that are already open will be
  auto-updated (was just updating the container on the next open).

--------------------------------------------
Version: 1.0b2 (June 3, 2013)
--------------------------------------------
* Initial beta release.

--------------------------------------------
Version: 1.0b1
--------------------------------------------
* Unreleased internal version.

Google Tag Manager iOS SDK

Copyright 2013-2015 Google, Inc. All rights reserved.

================================================================================
DESCRIPTION:

This SDK provides developers with the capability to use Google Tag Manager
to do server-side rule-based customization of configuration variables.

The SDK is packaged as a zip file with a directory (Examples) containing
examples, a directory (Library) containing the headers and the static library,
the change history (CHANGELOG) and this file (README).

Details on how to use this SDK are available at:
  http://developers.google.com/tag-manager/ios

================================================================================
BUILD REQUIREMENTS:

Mac OS X 10.6 or later.
XCode 5.0 or later.
iOS SDK 5.0 or later (6.0 or later for 64-bit).

================================================================================
RUNTIME REQUIREMENTS:

iOS 5.0 or later

Your application must link to the following frameworks:
  CoreData.framework
  Foundation.framework
  SystemConfiguration.framework
  UIKit.framework
  libsqlite3.dylib
  libz.dylib

If you wish to have access to the advertising identifier (IDFA) string and
advertiser tracking enabled flag, the following are also required:
  AdSupport.framework
  libAdIdAccess.a (included)

In order to ensure that the libAdIdAccess.a code doesn't get dead-stripped
from your executable during linking, you'll need to either add the -all_load
or -ObjC flag to the "Other Linker Flags", or, for finer-grained control, add the
-force_load flag (followed by a full pathname to libAdIdAccess.a).

cmake_minimum_required(VERSION 2.8.12)

project(HACD)

set(SRC_FILES
	hacdCircularList.h
	hacdGraph.h
	hacdHACD.h
	hacdICHull.h
	hacdManifoldMesh.h
	hacdVector.h
	hacdVersion.h
	hacdCircularList.inl
	hacdVector.inl
	hacdGraph.cpp
	hacdHACD.cpp
	hacdICHull.cpp
	hacdManifoldMesh.cpp
)

auto_source_group(${SRC_FILES})

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
# vim: et ts=4 sts=4 sw=4 tw=0

CMAKE_MINIMUM_REQUIRED(VERSION 3.1)
PROJECT(jsoncpp)
ENABLE_TESTING()

OPTION(JSONCPP_WITH_TESTS "Compile and (for jsoncpp_check) run JsonCpp test executables" ON)
OPTION(JSONCPP_WITH_POST_BUILD_UNITTEST "Automatically run unit-tests as a post build step" ON)
OPTION(JSONCPP_WITH_WARNING_AS_ERROR "Force compilation to fail if a warning occurs" OFF)
OPTION(JSONCPP_WITH_STRICT_ISO "Issue all the warnings demanded by strict ISO C and ISO C++" ON)
OPTION(JSONCPP_WITH_PKGCONFIG_SUPPORT "Generate and install .pc files" ON)
OPTION(JSONCPP_WITH_CMAKE_PACKAGE "Generate and install cmake package files" OFF)
OPTION(BUILD_SHARED_LIBS "Build jsoncpp_lib as a shared library." OFF)
OPTION(BUILD_STATIC_LIBS "Build jsoncpp_lib static library." ON)

# Ensures that CMAKE_BUILD_TYPE is visible in cmake-gui on Unix
IF(NOT WIN32)
    IF(NOT CMAKE_BUILD_TYPE)
        SET(CMAKE_BUILD_TYPE Release CACHE STRING
            "Choose the type of build, options are: None Debug Release RelWithDebInfo MinSizeRel Coverage."
            FORCE)
    ENDIF()
ENDIF()

# Enable runtime search path support for dynamic libraries on OSX
IF(APPLE)
    SET(CMAKE_MACOSX_RPATH 1)
ENDIF()

# Adhere to GNU filesystem layout conventions
INCLUDE(GNUInstallDirs)

SET(DEBUG_LIBNAME_SUFFIX "" CACHE STRING "Optional suffix to append to the library name for a debug build")

# Set variable named ${VAR_NAME} to value ${VALUE}
FUNCTION(set_using_dynamic_name VAR_NAME VALUE)
    SET( "${VAR_NAME}" "${VALUE}" PARENT_SCOPE)
ENDFUNCTION()

# Extract major, minor, patch from version text
# Parse a version string "X.Y.Z" and outputs
# version parts in ${OUPUT_PREFIX}_MAJOR, _MINOR, _PATCH.
# If parse succeeds then ${OUPUT_PREFIX}_FOUND is TRUE.
MACRO(jsoncpp_parse_version VERSION_TEXT OUPUT_PREFIX)
    SET(VERSION_REGEX "[0-9]+\\.[0-9]+\\.[0-9]+(-[a-zA-Z0-9_]+)?")
    IF( ${VERSION_TEXT} MATCHES ${VERSION_REGEX} )
        STRING(REGEX MATCHALL "[0-9]+|-([A-Za-z0-9_]+)" VERSION_PARTS ${VERSION_TEXT})
        LIST(GET VERSION_PARTS 0 ${OUPUT_PREFIX}_MAJOR)
        LIST(GET VERSION_PARTS 1 ${OUPUT_PREFIX}_MINOR)
        LIST(GET VERSION_PARTS 2 ${OUPUT_PREFIX}_PATCH)
        set_using_dynamic_name( "${OUPUT_PREFIX}_FOUND" TRUE )
    ELSE( ${VERSION_TEXT} MATCHES ${VERSION_REGEX} )
        set_using_dynamic_name( "${OUPUT_PREFIX}_FOUND" FALSE )
    ENDIF()
ENDMACRO()

# Read out version from "version" file
#FILE(STRINGS "version" JSONCPP_VERSION)
#SET( JSONCPP_VERSION_MAJOR X )
#SET( JSONCPP_VERSION_MINOR Y )
#SET( JSONCPP_VERSION_PATCH Z )
SET( JSONCPP_VERSION 1.8.4 )
jsoncpp_parse_version( ${JSONCPP_VERSION} JSONCPP_VERSION )
#IF(NOT JSONCPP_VERSION_FOUND)
#    MESSAGE(FATAL_ERROR "Failed to parse version string properly. Expect X.Y.Z")
#ENDIF(NOT JSONCPP_VERSION_FOUND)
SET( JSONCPP_SOVERSION 19 )
SET( JSONCPP_USE_SECURE_MEMORY "0" CACHE STRING "-D...=1 to use memory-wiping allocator for STL" )

MESSAGE(STATUS "JsonCpp Version: ${JSONCPP_VERSION_MAJOR}.${JSONCPP_VERSION_MINOR}.${JSONCPP_VERSION_PATCH}")
# File version.h is only regenerated on CMake configure step
#CONFIGURE_FILE( "${PROJECT_SOURCE_DIR}/src/lib_json/version.h.in"
#                "${PROJECT_SOURCE_DIR}/include/json/version.h"
#                NEWLINE_STYLE UNIX )
#CONFIGURE_FILE( "${PROJECT_SOURCE_DIR}/version.in"
#                "${PROJECT_SOURCE_DIR}/version"
#                NEWLINE_STYLE UNIX )

MACRO(UseCompilationWarningAsError)
    IF(MSVC)
        # Only enabled in debug because some old versions of VS STL generate
        # warnings when compiled in release configuration.
        SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /WX ")
    ELSEIF(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")
        IF(JSONCPP_WITH_STRICT_ISO)
            SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pedantic-errors")
        ENDIF()
    ENDIF()
ENDMACRO()

# Include our configuration header
INCLUDE_DIRECTORIES( ${jsoncpp_SOURCE_DIR}/include )

IF(MSVC)
    # Only enabled in debug because some old versions of VS STL generate
    # unreachable code warning when compiled in release configuration.
    SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /W4 ")
ENDIF()

# Require C++11 support, prefer ISO C++ over GNU variants,
# as relying solely on ISO C++ is more portable.
SET(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)
SET(CMAKE_CXX_EXTENSIONS OFF)

IF(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # using regular Clang or AppleClang
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wconversion -Wshadow -Werror=conversion -Werror=sign-compare")
ELSEIF(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    # using GCC
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wconversion -Wshadow -Wextra")
    # not yet ready for -Wsign-conversion

    IF(JSONCPP_WITH_STRICT_ISO)
        SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pedantic")
    ENDIF()
    IF(JSONCPP_WITH_WARNING_AS_ERROR)
        SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror=conversion")
    ENDIF()
ELSEIF(CMAKE_CXX_COMPILER_ID STREQUAL "Intel")
    # using Intel compiler
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wconversion -Wshadow -Wextra -Werror=conversion")

    IF(JSONCPP_WITH_STRICT_ISO AND NOT JSONCPP_WITH_WARNING_AS_ERROR)
        SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pedantic")
    ENDIF()
ENDIF()

FIND_PROGRAM(CCACHE_FOUND ccache)
IF(CCACHE_FOUND)
    SET_PROPERTY(GLOBAL PROPERTY RULE_LAUNCH_COMPILE ccache)
    SET_PROPERTY(GLOBAL PROPERTY RULE_LAUNCH_LINK ccache)
ENDIF(CCACHE_FOUND)

IF(JSONCPP_WITH_WARNING_AS_ERROR)
    UseCompilationWarningAsError()
ENDIF()

IF(JSONCPP_WITH_PKGCONFIG_SUPPORT)
    CONFIGURE_FILE(
        "pkg-config/jsoncpp.pc.in"
        "pkg-config/jsoncpp.pc"
        @ONLY)
    INSTALL(FILES "${CMAKE_CURRENT_BINARY_DIR}/pkg-config/jsoncpp.pc"
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/pkgconfig")
ENDIF()

IF(JSONCPP_WITH_CMAKE_PACKAGE)
        INSTALL(EXPORT jsoncpp
                DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/jsoncpp
                FILE        jsoncppConfig.cmake)
ENDIF()

# Build the different applications
ADD_SUBDIRECTORY( src )

#install the includes
#ADD_SUBDIRECTORY( include )
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
# JsonCpp

[![badge](https://img.shields.io/badge/conan.io-jsoncpp%2F1.8.0-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/jsoncpp/1.8.0/theirix/ci)

[JSON][json-org] is a lightweight data-interchange format. It can represent
numbers, strings, ordered sequences of values, and collections of name/value
pairs.

[json-org]: http://json.org/

JsonCpp is a C++ library that allows manipulating JSON values, including
serialization and deserialization to and from strings. It can also preserve
existing comment in unserialization/serialization steps, making it a convenient
format to store user input files.


## Documentation

[JsonCpp documentation][JsonCpp-documentation] is generated using [Doxygen][].

[JsonCpp-documentation]: http://open-source-parsers.github.io/jsoncpp-docs/doxygen/index.html
[Doxygen]: http://www.doxygen.org


## A note on backward-compatibility

* `1.y.z` is built with C++11.
* `0.y.z` can be used with older compilers.
* Major versions maintain binary-compatibility.

## Contributing to JsonCpp

### Building and testing with Meson/Ninja
Thanks to David Seifert (@SoapGentoo), we (the maintainers) now use [meson](http://mesonbuild.com/) and [ninja](https://ninja-build.org/) to build for debugging, as well as for continuous integration (see [`travis.sh`](travis.sh) ). Other systems may work, but minor things like version strings might break.

First, install both meson (which requires Python3) and ninja.
If you wish to install to a directory other than /usr/local, set an environment variable called DESTDIR with the desired path:
    DESTDIR=/path/to/install/dir

Then,

    cd jsoncpp/
    BUILD_TYPE=debug
    #BUILD_TYPE=release
    LIB_TYPE=shared
    #LIB_TYPE=static
    meson --buildtype ${BUILD_TYPE} --default-library ${LIB_TYPE} . build-${LIB_TYPE}
    ninja -v -C build-${LIB_TYPE} test
    cd build-${LIB_TYPE}
    sudo ninja install

### Building and testing with other build systems
See https://github.com/open-source-parsers/jsoncpp/wiki/Building

### Running the tests manually

You need to run tests manually only if you are troubleshooting an issue.

In the instructions below, replace `path/to/jsontest` with the path of the
`jsontest` executable that was compiled on your platform.

    cd test
    # This will run the Reader/Writer tests
    python runjsontests.py path/to/jsontest

    # This will run the Reader/Writer tests, using JSONChecker test suite
    # (http://www.json.org/JSON_checker/).
    # Notes: not all tests pass: JsonCpp is too lenient (for example,
    # it allows an integer to start with '0'). The goal is to improve
    # strict mode parsing to get all tests to pass.
    python runjsontests.py --with-json-checker path/to/jsontest

    # This will run the unit tests (mostly Value)
    python rununittests.py path/to/test_lib_json

    # You can run the tests using valgrind:
    python rununittests.py --valgrind path/to/test_lib_json

### Building the documentation

Run the Python script `doxybuild.py` from the top directory:

    python doxybuild.py --doxygen=$(which doxygen) --open --with-dot

See `doxybuild.py --help` for options.

### Adding a reader/writer test

To add a test, you need to create two files in test/data:

* a `TESTNAME.json` file, that contains the input document in JSON format.
* a `TESTNAME.expected` file, that contains a flatened representation of the
  input document.

The `TESTNAME.expected` file format is as follows:

* Each line represents a JSON element of the element tree represented by the
  input document.
* Each line has two parts: the path to access the element separated from the
  element value by `=`. Array and object values are always empty (i.e.
  represented by either `[]` or `{}`).
* Element path `.` represents the root element, and is used to separate object
  members. `[N]` is used to specify the value of an array element at index `N`.

See the examples `test_complex_01.json` and `test_complex_01.expected` to better understand element paths.

### Understanding reader/writer test output

When a test is run, output files are generated beside the input test files. Below is a short description of the content of each file:

* `test_complex_01.json`: input JSON document.
* `test_complex_01.expected`: flattened JSON element tree used to check if
  parsing was corrected.
* `test_complex_01.actual`: flattened JSON element tree produced by `jsontest`
  from reading `test_complex_01.json`.
* `test_complex_01.rewrite`: JSON document written by `jsontest` using the
  `Json::Value` parsed from `test_complex_01.json` and serialized using
  `Json::StyledWritter`.
* `test_complex_01.actual-rewrite`: flattened JSON element tree produced by
  `jsontest` from reading `test_complex_01.rewrite`.
* `test_complex_01.process-output`: `jsontest` output, typically useful for
  understanding parsing errors.

## Using JsonCpp in your project

### Amalgamated source
https://github.com/open-source-parsers/jsoncpp/wiki/Amalgamated

### Other ways
If you have trouble, see the Wiki, or post a question as an Issue.

## License

See the `LICENSE` file for details. In summary, JsonCpp is licensed under the
MIT license, or public domain if desired and recognized in your jurisdiction.
FILE(GLOB INCLUDE_FILES "json/*.h")
INSTALL(FILES ${INCLUDE_FILES} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/json)
ADD_SUBDIRECTORY(lib_json)
IF(JSONCPP_WITH_TESTS)
    ADD_SUBDIRECTORY(jsontestrunner)
    ADD_SUBDIRECTORY(test_lib_json)
ENDIF()
IF( CMAKE_COMPILER_IS_GNUCXX )
    #Get compiler version.
    EXECUTE_PROCESS( COMMAND ${CMAKE_CXX_COMPILER} -dumpversion
                     OUTPUT_VARIABLE GNUCXX_VERSION )

    #-Werror=* was introduced -after- GCC 4.1.2
    IF( GNUCXX_VERSION VERSION_GREATER 4.1.2 )
        SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror=strict-aliasing")
    ENDIF()
ENDIF( CMAKE_COMPILER_IS_GNUCXX )

INCLUDE(CheckIncludeFileCXX)
INCLUDE(CheckTypeSize)
INCLUDE(CheckStructHasMember)
INCLUDE(CheckCXXSymbolExists)

check_include_file_cxx(clocale HAVE_CLOCALE)
check_cxx_symbol_exists(localeconv clocale HAVE_LOCALECONV)

IF(CMAKE_VERSION VERSION_LESS 3.0.0)
    # The "LANGUAGE CXX" parameter is not supported in CMake versions below 3,
    # so the C compiler and header has to be used.
    check_include_file(locale.h HAVE_LOCALE_H)
    SET(CMAKE_EXTRA_INCLUDE_FILES locale.h)
    check_type_size("struct lconv" LCONV_SIZE)
    UNSET(CMAKE_EXTRA_INCLUDE_FILES)
    check_struct_has_member("struct lconv" decimal_point locale.h HAVE_DECIMAL_POINT)
ELSE()
    SET(CMAKE_EXTRA_INCLUDE_FILES clocale)
    check_type_size(lconv LCONV_SIZE LANGUAGE CXX)
    UNSET(CMAKE_EXTRA_INCLUDE_FILES)
    check_struct_has_member(lconv decimal_point clocale HAVE_DECIMAL_POINT LANGUAGE CXX)
ENDIF()

IF(NOT (HAVE_CLOCALE AND HAVE_LCONV_SIZE AND HAVE_DECIMAL_POINT AND HAVE_LOCALECONV))
    MESSAGE(WARNING "Locale functionality is not supported")
    ADD_DEFINITIONS(-DJSONCPP_NO_LOCALE_SUPPORT)
ENDIF()

SET( JSONCPP_INCLUDE_DIR ../../include )

SET( PUBLIC_HEADERS
    ${JSONCPP_INCLUDE_DIR}/json/config.h
    ${JSONCPP_INCLUDE_DIR}/json/forwards.h
    ${JSONCPP_INCLUDE_DIR}/json/features.h
    ${JSONCPP_INCLUDE_DIR}/json/value.h
    ${JSONCPP_INCLUDE_DIR}/json/reader.h
    ${JSONCPP_INCLUDE_DIR}/json/writer.h
    ${JSONCPP_INCLUDE_DIR}/json/assertions.h
    ${JSONCPP_INCLUDE_DIR}/json/version.h
    )

SOURCE_GROUP( "Public API" FILES ${PUBLIC_HEADERS} )

SET(jsoncpp_sources
                json_tool.h
                json_reader.cpp
                json_valueiterator.inl
                json_value.cpp
                json_writer.cpp
                version.h.in)

IF(BUILD_STATIC_LIBS)
    ADD_LIBRARY(${PROJECT_NAME} STATIC ${PUBLIC_HEADERS} ${jsoncpp_sources})

    IF(NOT CMAKE_VERSION VERSION_LESS 2.8.11)
        TARGET_INCLUDE_DIRECTORIES( ${PROJECT_NAME} PUBLIC
                                #$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
                                $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/${JSONCPP_INCLUDE_DIR}>
                                )
    ENDIF()

    set_target_properties(${PROJECT_NAME} PROPERTIES 
        FOLDER ThirdParty
        PREFIX ""
        #DEBUG_POSTFIX "_d"
        OUTPUT_NAME ${PROJECT_NAME}
        ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
        LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
        VERSION ${JSONCPP_VERSION} SOVERSION ${JSONCPP_SOVERSION})
ENDIF()
cmake_minimum_required(VERSION 2.8.12)

project(libjpeg)

set(SRC_FILES
	cderror.h
	jcinit.c
	jdapimin.c
	jdinput.c
	jfdctflt.c
	jmorecfg.h
	cdjpeg.h
	jcmainct.c
	jdapistd.c
	jdmainct.c
	jfdctfst.c
	jpegint.h
	jaricom.c
	jcmarker.c
	jdarith.c
	jdmarker.c
	jfdctint.c
	jpeglib.h
	jcapimin.c
	jcmaster.c
	jdatadst.c
	jdmaster.c
	jidctflt.c
	jquant1.c
	jcapistd.c
	jcomapi.c
	jdatasrc.c
	jdmerge.c
	jidctfst.c
	jquant2.c
	jcarith.c
	jconfig.h
	jdcoefct.c
	jdpostct.c
	jidctint.c
	jutils.c
	jccoefct.c
	jcparam.c
	jdcolor.c
	jdsample.c
	jinclude.h
	jversion.h
	jccolor.c
	jcprepct.c
	jdct.h
	jdtrans.c
	jmemmgr.c
	transupp.c
	jcdctmgr.c
	jcsample.c
	jddctmgr.c
	jerror.c
	jmemnobs.c
	transupp.h
	jchuff.c
	jctrans.c
	jdhuff.c
	jerror.h
	jmemsys.h
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

project(libogg)

set(SRC_FILES
    include/ogg/ogg.h
    include/ogg/os_types.h
    src/bitwise.c
    src/framing.c  
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

target_include_directories(${PROJECT_NAME} 
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)cmake_minimum_required(VERSION 2.8.12)

project(libpng)

set(SRC_FILES
    png.h
    pngconf.h
    pnglibconf.h
    pngdebug.h
    pnginfo.h
    pngpriv.h
    pngstruct.h
    png.c
    pngerror.c
    pngget.c
    pngmem.c
    pngpread.c
    pngread.c
    pngrio.c
    pngrtran.c
    pngrutil.c
    pngset.c
    pngtrans.c
    pngwio.c
    pngwrite.c
    pngwtran.c
    pngwutil.c
)

if (IOS OR ANDROID)
    list(APPEND SRC_FILES
        arm/arm_init.c
        arm/filter_neon_intrinsics.c
        #arm/filter_neon.S
    )
endif ()

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_link_libraries(${PROJECT_NAME} zlib)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
libpng-manual.txt - A description on how to use and modify libpng

 libpng version 1.6.17 - March 26, 2015
 Updated and distributed by Glenn Randers-Pehrson
 <glennrp at users.sourceforge.net>
 Copyright (c) 1998-2015 Glenn Randers-Pehrson

 This document is released under the libpng license.
 For conditions of distribution and use, see the disclaimer
 and license in png.h

 Based on:

 libpng versions 0.97, January 1998, through 1.6.17 - March 26, 2015
 Updated and distributed by Glenn Randers-Pehrson
 Copyright (c) 1998-2015 Glenn Randers-Pehrson

 libpng 1.0 beta 6 - version 0.96 - May 28, 1997
 Updated and distributed by Andreas Dilger
 Copyright (c) 1996, 1997 Andreas Dilger

 libpng 1.0 beta 2 - version 0.88 - January 26, 1996
 For conditions of distribution and use, see copyright
 notice in png.h. Copyright (c) 1995, 1996 Guy Eric
 Schalnat, Group 42, Inc.

 Updated/rewritten per request in the libpng FAQ
 Copyright (c) 1995, 1996 Frank J. T. Wojcik
 December 18, 1995 & January 20, 1996

 TABLE OF CONTENTS

    I. Introduction
   II. Structures
  III. Reading
   IV. Writing
    V. Simplified API
   VI. Modifying/Customizing libpng
  VII. MNG support
 VIII. Changes to Libpng from version 0.88
   IX. Changes to Libpng from version 1.0.x to 1.2.x
    X. Changes to Libpng from version 1.0.x/1.2.x to 1.4.x
   XI. Changes to Libpng from version 1.4.x to 1.5.x
  XII. Changes to Libpng from version 1.5.x to 1.6.x
 XIII. Detecting libpng
  XIV. Source code repository
   XV. Coding style
  XVI. Y2K Compliance in libpng

I. Introduction

This file describes how to use and modify the PNG reference library
(known as libpng) for your own use.  In addition to this
file, example.c is a good starting point for using the library, as
it is heavily commented and should include everything most people
will need.  We assume that libpng is already installed; see the
INSTALL file for instructions on how to configure and install libpng.

For examples of libpng usage, see the files "example.c", "pngtest.c",
and the files in the "contrib" directory, all of which are included in
the libpng distribution.

Libpng was written as a companion to the PNG specification, as a way
of reducing the amount of time and effort it takes to support the PNG
file format in application programs.

The PNG specification (second edition), November 2003, is available as
a W3C Recommendation and as an ISO Standard (ISO/IEC 15948:2004 (E)) at
<http://www.w3.org/TR/2003/REC-PNG-20031110/
The W3C and ISO documents have identical technical content.

The PNG-1.2 specification is available at
<http://www.libpng.org/pub/png/documents/>.  It is technically equivalent
to the PNG specification (second edition) but has some additional material.

The PNG-1.0 specification is available
as RFC 2083 <http://www.libpng.org/pub/png/documents/> and as a
W3C Recommendation <http://www.w3.org/TR/REC.png.html>.

Some additional chunks are described in the special-purpose public chunks
documents at <http://www.libpng.org/pub/png/documents/>.

Other information
about PNG, and the latest version of libpng, can be found at the PNG home
page, <http://www.libpng.org/pub/png/>.

Most users will not have to modify the library significantly; advanced
users may want to modify it more.  All attempts were made to make it as
complete as possible, while keeping the code easy to understand.
Currently, this library only supports C.  Support for other languages
is being considered.

Libpng has been designed to handle multiple sessions at one time,
to be easily modifiable, to be portable to the vast majority of
machines (ANSI, K&R, 16-, 32-, and 64-bit) available, and to be easy
to use.  The ultimate goal of libpng is to promote the acceptance of
the PNG file format in whatever way possible.  While there is still
work to be done (see the TODO file), libpng should cover the
majority of the needs of its users.

Libpng uses zlib for its compression and decompression of PNG files.
Further information about zlib, and the latest version of zlib, can
be found at the zlib home page, <http://www.info-zip.org/pub/infozip/zlib/>.
The zlib compression utility is a general purpose utility that is
useful for more than PNG files, and can be used without libpng.
See the documentation delivered with zlib for more details.
You can usually find the source files for the zlib utility wherever you
find the libpng source files.

Libpng is thread safe, provided the threads are using different
instances of the structures.  Each thread should have its own
png_struct and png_info instances, and thus its own image.
Libpng does not protect itself against two threads using the
same instance of a structure.

II. Structures

There are two main structures that are important to libpng, png_struct
and png_info.  Both are internal structures that are no longer exposed
in the libpng interface (as of libpng 1.5.0).

The png_info structure is designed to provide information about the
PNG file.  At one time, the fields of png_info were intended to be
directly accessible to the user.  However, this tended to cause problems
with applications using dynamically loaded libraries, and as a result
a set of interface functions for png_info (the png_get_*() and png_set_*()
functions) was developed, and direct access to the png_info fields was
deprecated..

The png_struct structure is the object used by the library to decode a
single image.  As of 1.5.0 this structure is also not exposed.

Almost all libpng APIs require a pointer to a png_struct as the first argument.
Many (in particular the png_set and png_get APIs) also require a pointer
to png_info as the second argument.  Some application visible macros
defined in png.h designed for basic data access (reading and writing
integers in the PNG format) don't take a png_info pointer, but it's almost
always safe to assume that a (png_struct*) has to be passed to call an API
function.

You can have more than one png_info structure associated with an image,
as illustrated in pngtest.c, one for information valid prior to the
IDAT chunks and another (called "end_info" below) for things after them.

The png.h header file is an invaluable reference for programming with libpng.
And while I'm on the topic, make sure you include the libpng header file:

#include <png.h>

and also (as of libpng-1.5.0) the zlib header file, if you need it:

#include <zlib.h>

Types

The png.h header file defines a number of integral types used by the
APIs.  Most of these are fairly obvious; for example types corresponding
to integers of particular sizes and types for passing color values.

One exception is how non-integral numbers are handled.  For application
convenience most APIs that take such numbers have C (double) arguments;
however, internally PNG, and libpng, use 32 bit signed integers and encode
the value by multiplying by 100,000.  As of libpng 1.5.0 a convenience
macro PNG_FP_1 is defined in png.h along with a type (png_fixed_point)
which is simply (png_int_32).

All APIs that take (double) arguments also have a matching API that
takes the corresponding fixed point integer arguments.  The fixed point
API has the same name as the floating point one with "_fixed" appended.
The actual range of values permitted in the APIs is frequently less than
the full range of (png_fixed_point) (-21474 to +21474).  When APIs require
a non-negative argument the type is recorded as png_uint_32 above.  Consult
the header file and the text below for more information.

Special care must be take with sCAL chunk handling because the chunk itself
uses non-integral values encoded as strings containing decimal floating point
numbers.  See the comments in the header file.

Configuration

The main header file function declarations are frequently protected by C
preprocessing directives of the form:

    #ifdef PNG_feature_SUPPORTED
    declare-function
    #endif
    ...
    #ifdef PNG_feature_SUPPORTED
    use-function
    #endif

The library can be built without support for these APIs, although a
standard build will have all implemented APIs.  Application programs
should check the feature macros before using an API for maximum
portability.  From libpng 1.5.0 the feature macros set during the build
of libpng are recorded in the header file "pnglibconf.h" and this file
is always included by png.h.

If you don't need to change the library configuration from the default, skip to
the next section ("Reading").

Notice that some of the makefiles in the 'scripts' directory and (in 1.5.0) all
of the build project files in the 'projects' directory simply copy
scripts/pnglibconf.h.prebuilt to pnglibconf.h.  This means that these build
systems do not permit easy auto-configuration of the library - they only
support the default configuration.

The easiest way to make minor changes to the libpng configuration when
auto-configuration is supported is to add definitions to the command line
using (typically) CPPFLAGS.  For example:

CPPFLAGS=-DPNG_NO_FLOATING_ARITHMETIC

will change the internal libpng math implementation for gamma correction and
other arithmetic calculations to fixed point, avoiding the need for fast
floating point support.  The result can be seen in the generated pnglibconf.h -
make sure it contains the changed feature macro setting.

If you need to make more extensive configuration changes - more than one or two
feature macro settings - you can either add -DPNG_USER_CONFIG to the build
command line and put a list of feature macro settings in pngusr.h or you can set
DFA_XTRA (a makefile variable) to a file containing the same information in the
form of 'option' settings.

A. Changing pnglibconf.h

A variety of methods exist to build libpng.  Not all of these support
reconfiguration of pnglibconf.h.  To reconfigure pnglibconf.h it must either be
rebuilt from scripts/pnglibconf.dfa using awk or it must be edited by hand.

Hand editing is achieved by copying scripts/pnglibconf.h.prebuilt to
pnglibconf.h and changing the lines defining the supported features, paying
very close attention to the 'option' information in scripts/pnglibconf.dfa
that describes those features and their requirements.  This is easy to get
wrong.

B. Configuration using DFA_XTRA

Rebuilding from pnglibconf.dfa is easy if a functioning 'awk', or a later
variant such as 'nawk' or 'gawk', is available.  The configure build will
automatically find an appropriate awk and build pnglibconf.h.
The scripts/pnglibconf.mak file contains a set of make rules for doing the
same thing if configure is not used, and many of the makefiles in the scripts
directory use this approach.

When rebuilding simply write a new file containing changed options and set
DFA_XTRA to the name of this file.  This causes the build to append the new file
to the end of scripts/pnglibconf.dfa.  The pngusr.dfa file should contain lines
of the following forms:

everything = off

This turns all optional features off.  Include it at the start of pngusr.dfa to
make it easier to build a minimal configuration.  You will need to turn at least
some features on afterward to enable either reading or writing code, or both.

option feature on
option feature off

Enable or disable a single feature.  This will automatically enable other
features required by a feature that is turned on or disable other features that
require a feature which is turned off.  Conflicting settings will cause an error
message to be emitted by awk.

setting feature default value

Changes the default value of setting 'feature' to 'value'.  There are a small
number of settings listed at the top of pnglibconf.h, they are documented in the
source code.  Most of these values have performance implications for the library
but most of them have no visible effect on the API.  Some can also be overridden
from the API.

This method of building a customized pnglibconf.h is illustrated in
contrib/pngminim/*.  See the "$(PNGCONF):" target in the makefile and
pngusr.dfa in these directories.

C. Configuration using PNG_USER_CONFIG

If -DPNG_USER_CONFIG is added to the CPPFLAGS when pnglibconf.h is built,
the file pngusr.h will automatically be included before the options in
scripts/pnglibconf.dfa are processed.  Your pngusr.h file should contain only
macro definitions turning features on or off or setting settings.

Apart from the global setting "everything = off" all the options listed above
can be set using macros in pngusr.h:

#define PNG_feature_SUPPORTED

is equivalent to:

option feature on

#define PNG_NO_feature

is equivalent to:

option feature off

#define PNG_feature value

is equivalent to:

setting feature default value

Notice that in both cases, pngusr.dfa and pngusr.h, the contents of the
pngusr file you supply override the contents of scripts/pnglibconf.dfa

If confusing or incomprehensible behavior results it is possible to
examine the intermediate file pnglibconf.dfn to find the full set of
dependency information for each setting and option.  Simply locate the
feature in the file and read the C comments that precede it.

This method is also illustrated in the contrib/pngminim/* makefiles and
pngusr.h.

III. Reading

We'll now walk you through the possible functions to call when reading
in a PNG file sequentially, briefly explaining the syntax and purpose
of each one.  See example.c and png.h for more detail.  While
progressive reading is covered in the next section, you will still
need some of the functions discussed in this section to read a PNG
file.

Setup

You will want to do the I/O initialization(*) before you get into libpng,
so if it doesn't work, you don't have much to undo.  Of course, you
will also want to insure that you are, in fact, dealing with a PNG
file.  Libpng provides a simple check to see if a file is a PNG file.
To use it, pass in the first 1 to 8 bytes of the file to the function
png_sig_cmp(), and it will return 0 (false) if the bytes match the
corresponding bytes of the PNG signature, or nonzero (true) otherwise.
Of course, the more bytes you pass in, the greater the accuracy of the
prediction.

If you are intending to keep the file pointer open for use in libpng,
you must ensure you don't read more than 8 bytes from the beginning
of the file, and you also have to make a call to png_set_sig_bytes()
with the number of bytes you read from the beginning.  Libpng will
then only check the bytes (if any) that your program didn't read.

(*): If you are not using the standard I/O functions, you will need
to replace them with custom functions.  See the discussion under
Customizing libpng.

    FILE *fp = fopen(file_name, "rb");
    if (!fp)
    {
       return (ERROR);
    }

    if (fread(header, 1, number, fp) != number)
    {
       return (ERROR);
    }

    is_png = !png_sig_cmp(header, 0, number);
    if (!is_png)
    {
       return (NOT_PNG);
    }

Next, png_struct and png_info need to be allocated and initialized.  In
order to ensure that the size of these structures is correct even with a
dynamically linked libpng, there are functions to initialize and
allocate the structures.  We also pass the library version, optional
pointers to error handling functions, and a pointer to a data struct for
use by the error functions, if necessary (the pointer and functions can
be NULL if the default error handlers are to be used).  See the section
on Changes to Libpng below regarding the old initialization functions.
The structure allocation functions quietly return NULL if they fail to
create the structure, so your application should check for that.

    png_structp png_ptr = png_create_read_struct
        (PNG_LIBPNG_VER_STRING, (png_voidp)user_error_ptr,
        user_error_fn, user_warning_fn);

    if (!png_ptr)
       return (ERROR);

    png_infop info_ptr = png_create_info_struct(png_ptr);

    if (!info_ptr)
    {
       png_destroy_read_struct(&png_ptr,
           (png_infopp)NULL, (png_infopp)NULL);
       return (ERROR);
    }

If you want to use your own memory allocation routines,
use a libpng that was built with PNG_USER_MEM_SUPPORTED defined, and use
png_create_read_struct_2() instead of png_create_read_struct():

    png_structp png_ptr = png_create_read_struct_2
        (PNG_LIBPNG_VER_STRING, (png_voidp)user_error_ptr,
        user_error_fn, user_warning_fn, (png_voidp)
        user_mem_ptr, user_malloc_fn, user_free_fn);

The error handling routines passed to png_create_read_struct()
and the memory alloc/free routines passed to png_create_struct_2()
are only necessary if you are not using the libpng supplied error
handling and memory alloc/free functions.

When libpng encounters an error, it expects to longjmp back
to your routine.  Therefore, you will need to call setjmp and pass
your png_jmpbuf(png_ptr).  If you read the file from different
routines, you will need to update the longjmp buffer every time you enter
a new routine that will call a png_*() function.

See your documentation of setjmp/longjmp for your compiler for more
information on setjmp/longjmp.  See the discussion on libpng error
handling in the Customizing Libpng section below for more information
on the libpng error handling.  If an error occurs, and libpng longjmp's
back to your setjmp, you will want to call png_destroy_read_struct() to
free any memory.

    if (setjmp(png_jmpbuf(png_ptr)))
    {
       png_destroy_read_struct(&png_ptr, &info_ptr,
           &end_info);
       fclose(fp);
       return (ERROR);
    }

Pass (png_infopp)NULL instead of &end_info if you didn't create
an end_info structure.

If you would rather avoid the complexity of setjmp/longjmp issues,
you can compile libpng with PNG_NO_SETJMP, in which case
errors will result in a call to PNG_ABORT() which defaults to abort().

You can #define PNG_ABORT() to a function that does something
more useful than abort(), as long as your function does not
return.

Now you need to set up the input code.  The default for libpng is to
use the C function fread().  If you use this, you will need to pass a
valid FILE * in the function png_init_io().  Be sure that the file is
opened in binary mode.  If you wish to handle reading data in another
way, you need not call the png_init_io() function, but you must then
implement the libpng I/O methods discussed in the Customizing Libpng
section below.

    png_init_io(png_ptr, fp);

If you had previously opened the file and read any of the signature from
the beginning in order to see if this was a PNG file, you need to let
libpng know that there are some bytes missing from the start of the file.

    png_set_sig_bytes(png_ptr, number);

You can change the zlib compression buffer size to be used while
reading compressed data with

    png_set_compression_buffer_size(png_ptr, buffer_size);

where the default size is 8192 bytes.  Note that the buffer size
is changed immediately and the buffer is reallocated immediately,
instead of setting a flag to be acted upon later.

If you want CRC errors to be handled in a different manner than
the default, use

    png_set_crc_action(png_ptr, crit_action, ancil_action);

The values for png_set_crc_action() say how libpng is to handle CRC errors in
ancillary and critical chunks, and whether to use the data contained
therein.  Note that it is impossible to "discard" data in a critical
chunk.

Choices for (int) crit_action are
   PNG_CRC_DEFAULT      0  error/quit
   PNG_CRC_ERROR_QUIT   1  error/quit
   PNG_CRC_WARN_USE     3  warn/use data
   PNG_CRC_QUIET_USE    4  quiet/use data
   PNG_CRC_NO_CHANGE    5  use the current value

Choices for (int) ancil_action are
   PNG_CRC_DEFAULT      0  error/quit
   PNG_CRC_ERROR_QUIT   1  error/quit
   PNG_CRC_WARN_DISCARD 2  warn/discard data
   PNG_CRC_WARN_USE     3  warn/use data
   PNG_CRC_QUIET_USE    4  quiet/use data
   PNG_CRC_NO_CHANGE    5  use the current value

Setting up callback code

You can set up a callback function to handle any unknown chunks in the
input stream. You must supply the function

    read_chunk_callback(png_structp png_ptr,
         png_unknown_chunkp chunk);
    {
       /* The unknown chunk structure contains your
          chunk data, along with similar data for any other
          unknown chunks: */

           png_byte name[5];
           png_byte *data;
           png_size_t size;

       /* Note that libpng has already taken care of
          the CRC handling */

       /* put your code here.  Search for your chunk in the
          unknown chunk structure, process it, and return one
          of the following: */

       return (-n); /* chunk had an error */
       return (0); /* did not recognize */
       return (n); /* success */
    }

(You can give your function another name that you like instead of
"read_chunk_callback")

To inform libpng about your function, use

    png_set_read_user_chunk_fn(png_ptr, user_chunk_ptr,
        read_chunk_callback);

This names not only the callback function, but also a user pointer that
you can retrieve with

    png_get_user_chunk_ptr(png_ptr);

If you call the png_set_read_user_chunk_fn() function, then all unknown
chunks which the callback does not handle will be saved when read.  You can
cause them to be discarded by returning '1' ("handled") instead of '0'.  This
behavior will change in libpng 1.7 and the default handling set by the
png_set_keep_unknown_chunks() function, described below, will be used when the
callback returns 0.  If you want the existing behavior you should set the global
default to PNG_HANDLE_CHUNK_IF_SAFE now; this is compatible with all current
versions of libpng and with 1.7.  Libpng 1.6 issues a warning if you keep the
default, or PNG_HANDLE_CHUNK_NEVER, and the callback returns 0.

At this point, you can set up a callback function that will be
called after each row has been read, which you can use to control
a progress meter or the like.  It's demonstrated in pngtest.c.
You must supply a function

    void read_row_callback(png_structp png_ptr,
       png_uint_32 row, int pass);
    {
      /* put your code here */
    }

(You can give it another name that you like instead of "read_row_callback")

To inform libpng about your function, use

    png_set_read_status_fn(png_ptr, read_row_callback);

When this function is called the row has already been completely processed and
the 'row' and 'pass' refer to the next row to be handled.  For the
non-interlaced case the row that was just handled is simply one less than the
passed in row number, and pass will always be 0.  For the interlaced case the
same applies unless the row value is 0, in which case the row just handled was
the last one from one of the preceding passes.  Because interlacing may skip a
pass you cannot be sure that the preceding pass is just 'pass-1', if you really
need to know what the last pass is record (row,pass) from the callback and use
the last recorded value each time.

As with the user transform you can find the output row using the
PNG_ROW_FROM_PASS_ROW macro.

Unknown-chunk handling

Now you get to set the way the library processes unknown chunks in the
input PNG stream. Both known and unknown chunks will be read.  Normal
behavior is that known chunks will be parsed into information in
various info_ptr members while unknown chunks will be discarded. This
behavior can be wasteful if your application will never use some known
chunk types. To change this, you can call:

    png_set_keep_unknown_chunks(png_ptr, keep,
        chunk_list, num_chunks);

    keep       - 0: default unknown chunk handling
                 1: ignore; do not keep
                 2: keep only if safe-to-copy
                 3: keep even if unsafe-to-copy

               You can use these definitions:
                 PNG_HANDLE_CHUNK_AS_DEFAULT   0
                 PNG_HANDLE_CHUNK_NEVER        1
                 PNG_HANDLE_CHUNK_IF_SAFE      2
                 PNG_HANDLE_CHUNK_ALWAYS       3

    chunk_list - list of chunks affected (a byte string,
                 five bytes per chunk, NULL or '\0' if
                 num_chunks is positive; ignored if
                 numchunks <= 0).

    num_chunks - number of chunks affected; if 0, all
                 unknown chunks are affected.  If positive,
                 only the chunks in the list are affected,
                 and if negative all unknown chunks and
                 all known chunks except for the IHDR,
                 PLTE, tRNS, IDAT, and IEND chunks are
                 affected.

Unknown chunks declared in this way will be saved as raw data onto a
list of png_unknown_chunk structures.  If a chunk that is normally
known to libpng is named in the list, it will be handled as unknown,
according to the "keep" directive.  If a chunk is named in successive
instances of png_set_keep_unknown_chunks(), the final instance will
take precedence.  The IHDR and IEND chunks should not be named in
chunk_list; if they are, libpng will process them normally anyway.
If you know that your application will never make use of some particular
chunks, use PNG_HANDLE_CHUNK_NEVER (or 1) as demonstrated below.

Here is an example of the usage of png_set_keep_unknown_chunks(),
where the private "vpAg" chunk will later be processed by a user chunk
callback function:

    png_byte vpAg[5]={118, 112,  65, 103, (png_byte) '\0'};

    #if defined(PNG_UNKNOWN_CHUNKS_SUPPORTED)
      png_byte unused_chunks[]=
      {
        104,  73,  83,  84, (png_byte) '\0',   /* hIST */
        105,  84,  88, 116, (png_byte) '\0',   /* iTXt */
        112,  67,  65,  76, (png_byte) '\0',   /* pCAL */
        115,  67,  65,  76, (png_byte) '\0',   /* sCAL */
        115,  80,  76,  84, (png_byte) '\0',   /* sPLT */
        116,  73,  77,  69, (png_byte) '\0',   /* tIME */
      };
    #endif

    ...

    #if defined(PNG_UNKNOWN_CHUNKS_SUPPORTED)
      /* ignore all unknown chunks
       * (use global setting "2" for libpng16 and earlier):
       */
      png_set_keep_unknown_chunks(read_ptr, 2, NULL, 0);

      /* except for vpAg: */
      png_set_keep_unknown_chunks(read_ptr, 2, vpAg, 1);

      /* also ignore unused known chunks: */
      png_set_keep_unknown_chunks(read_ptr, 1, unused_chunks,
         (int)(sizeof unused_chunks)/5);
    #endif

User limits

The PNG specification allows the width and height of an image to be as
large as 2^31-1 (0x7fffffff), or about 2.147 billion rows and columns.
Larger images will be rejected immediately with a png_error() call. If
you wish to change these limits, you can use

   png_set_user_limits(png_ptr, width_max, height_max);

to set your own limits (libpng may reject some very wide images
anyway because of potential buffer overflow conditions).

You should put this statement after you create the PNG structure and
before calling png_read_info(), png_read_png(), or png_process_data().

When writing a PNG datastream, put this statement before calling
png_write_info() or png_write_png().

If you need to retrieve the limits that are being applied, use

   width_max = png_get_user_width_max(png_ptr);
   height_max = png_get_user_height_max(png_ptr);

The PNG specification sets no limit on the number of ancillary chunks
allowed in a PNG datastream.  You can impose a limit on the total number
of sPLT, tEXt, iTXt, zTXt, and unknown chunks that will be stored, with

   png_set_chunk_cache_max(png_ptr, user_chunk_cache_max);

where 0x7fffffffL means unlimited.  You can retrieve this limit with

   chunk_cache_max = png_get_chunk_cache_max(png_ptr);

You can also set a limit on the amount of memory that a compressed chunk
other than IDAT can occupy, with

   png_set_chunk_malloc_max(png_ptr, user_chunk_malloc_max);

and you can retrieve the limit with

   chunk_malloc_max = png_get_chunk_malloc_max(png_ptr);

Any chunks that would cause either of these limits to be exceeded will
be ignored.

Information about your system

If you intend to display the PNG or to incorporate it in other image data you
need to tell libpng information about your display or drawing surface so that
libpng can convert the values in the image to match the display.

From libpng-1.5.4 this information can be set before reading the PNG file
header.  In earlier versions png_set_gamma() existed but behaved incorrectly if
called before the PNG file header had been read and png_set_alpha_mode() did not
exist.

If you need to support versions prior to libpng-1.5.4 test the version number
as illustrated below using "PNG_LIBPNG_VER >= 10504" and follow the procedures
described in the appropriate manual page.

You give libpng the encoding expected by your system expressed as a 'gamma'
value.  You can also specify a default encoding for the PNG file in
case the required information is missing from the file.  By default libpng
assumes that the PNG data matches your system, to keep this default call:

   png_set_gamma(png_ptr, screen_gamma, output_gamma);

or you can use the fixed point equivalent:

   png_set_gamma_fixed(png_ptr, PNG_FP_1*screen_gamma,
      PNG_FP_1*output_gamma);

If you don't know the gamma for your system it is probably 2.2 - a good
approximation to the IEC standard for display systems (sRGB).  If images are
too contrasty or washed out you got the value wrong - check your system
documentation!

Many systems permit the system gamma to be changed via a lookup table in the
display driver, a few systems, including older Macs, change the response by
default.  As of 1.5.4 three special values are available to handle common
situations:

   PNG_DEFAULT_sRGB: Indicates that the system conforms to the
                     IEC 61966-2-1 standard.  This matches almost
                     all systems.
   PNG_GAMMA_MAC_18: Indicates that the system is an older
                     (pre Mac OS 10.6) Apple Macintosh system with
                     the default settings.
   PNG_GAMMA_LINEAR: Just the fixed point value for 1.0 - indicates
                     that the system expects data with no gamma
                     encoding.

You would use the linear (unencoded) value if you need to process the pixel
values further because this avoids the need to decode and re-encode each
component value whenever arithmetic is performed.  A lot of graphics software
uses linear values for this reason, often with higher precision component values
to preserve overall accuracy.


The output_gamma value expresses how to decode the output values, not how
they are encoded.  The values used correspond to the normal numbers used to
describe the overall gamma of a computer display system; for example 2.2 for
an sRGB conformant system.  The values are scaled by 100000 in the _fixed
version of the API (so 220000 for sRGB.)

The inverse of the value is always used to provide a default for the PNG file
encoding if it has no gAMA chunk and if png_set_gamma() has not been called
to override the PNG gamma information.

When the ALPHA_OPTIMIZED mode is selected the output gamma is used to encode
opaque pixels however pixels with lower alpha values are not encoded,
regardless of the output gamma setting.

When the standard Porter Duff handling is requested with mode 1 the output
encoding is set to be linear and the output_gamma value is only relevant
as a default for input data that has no gamma information.  The linear output
encoding will be overridden if png_set_gamma() is called - the results may be
highly unexpected!

The following numbers are derived from the sRGB standard and the research
behind it.  sRGB is defined to be approximated by a PNG gAMA chunk value of
0.45455 (1/2.2) for PNG.  The value implicitly includes any viewing
correction required to take account of any differences in the color
environment of the original scene and the intended display environment; the
value expresses how to *decode* the image for display, not how the original
data was *encoded*.

sRGB provides a peg for the PNG standard by defining a viewing environment.
sRGB itself, and earlier TV standards, actually use a more complex transform
(a linear portion then a gamma 2.4 power law) than PNG can express.  (PNG is
limited to simple power laws.)  By saying that an image for direct display on
an sRGB conformant system should be stored with a gAMA chunk value of 45455
(11.3.3.2 and 11.3.3.5 of the ISO PNG specification) the PNG specification
makes it possible to derive values for other display systems and
environments.

The Mac value is deduced from the sRGB based on an assumption that the actual
extra viewing correction used in early Mac display systems was implemented as
a power 1.45 lookup table.

Any system where a programmable lookup table is used or where the behavior of
the final display device characteristics can be changed requires system
specific code to obtain the current characteristic.  However this can be
difficult and most PNG gamma correction only requires an approximate value.

By default, if png_set_alpha_mode() is not called, libpng assumes that all
values are unencoded, linear, values and that the output device also has a
linear characteristic.  This is only very rarely correct - it is invariably
better to call png_set_alpha_mode() with PNG_DEFAULT_sRGB than rely on the
default if you don't know what the right answer is!

The special value PNG_GAMMA_MAC_18 indicates an older Mac system (pre Mac OS
10.6) which used a correction table to implement a somewhat lower gamma on an
otherwise sRGB system.

Both these values are reserved (not simple gamma values) in order to allow
more precise correction internally in the future.

NOTE: the values can be passed to either the fixed or floating
point APIs, but the floating point API will also accept floating point
values.

The second thing you may need to tell libpng about is how your system handles
alpha channel information.  Some, but not all, PNG files contain an alpha
channel.  To display these files correctly you need to compose the data onto a
suitable background, as described in the PNG specification.

Libpng only supports composing onto a single color (using png_set_background;
see below).  Otherwise you must do the composition yourself and, in this case,
you may need to call png_set_alpha_mode:

   #if PNG_LIBPNG_VER >= 10504
      png_set_alpha_mode(png_ptr, mode, screen_gamma);
   #else
      png_set_gamma(png_ptr, screen_gamma, 1.0/screen_gamma);
   #endif

The screen_gamma value is the same as the argument to png_set_gamma; however,
how it affects the output depends on the mode.  png_set_alpha_mode() sets the
file gamma default to 1/screen_gamma, so normally you don't need to call
png_set_gamma.  If you need different defaults call png_set_gamma() before
png_set_alpha_mode() - if you call it after it will override the settings made
by png_set_alpha_mode().

The mode is as follows:

    PNG_ALPHA_PNG: The data is encoded according to the PNG
specification.  Red, green and blue, or gray, components are
gamma encoded color values and are not premultiplied by the
alpha value.  The alpha value is a linear measure of the
contribution of the pixel to the corresponding final output pixel.

You should normally use this format if you intend to perform
color correction on the color values; most, maybe all, color
correction software has no handling for the alpha channel and,
anyway, the math to handle pre-multiplied component values is
unnecessarily complex.

Before you do any arithmetic on the component values you need
to remove the gamma encoding and multiply out the alpha
channel.  See the PNG specification for more detail.  It is
important to note that when an image with an alpha channel is
scaled, linear encoded, pre-multiplied component values must
be used!

The remaining modes assume you don't need to do any further color correction or
that if you do, your color correction software knows all about alpha (it
probably doesn't!).  They 'associate' the alpha with the color information by
storing color channel values that have been scaled by the alpha.  The
advantage is that the color channels can be resampled (the image can be
scaled) in this form.  The disadvantage is that normal practice is to store
linear, not (gamma) encoded, values and this requires 16-bit channels for
still images rather than the 8-bit channels that are just about sufficient if
gamma encoding is used.  In addition all non-transparent pixel values,
including completely opaque ones, must be gamma encoded to produce the final
image.  These are the 'STANDARD', 'ASSOCIATED' or 'PREMULTIPLIED' modes
described below (the latter being the two common names for associated alpha
color channels). Note that PNG files always contain non-associated color
channels; png_set_alpha_mode() with one of the modes causes the decoder to
convert the pixels to an associated form before returning them to your
application. 

Since it is not necessary to perform arithmetic on opaque color values so
long as they are not to be resampled and are in the final color space it is
possible to optimize the handling of alpha by storing the opaque pixels in
the PNG format (adjusted for the output color space) while storing partially
opaque pixels in the standard, linear, format.  The accuracy required for
standard alpha composition is relatively low, because the pixels are
isolated, therefore typically the accuracy loss in storing 8-bit linear
values is acceptable.  (This is not true if the alpha channel is used to
simulate transparency over large areas - use 16 bits or the PNG mode in
this case!)  This is the 'OPTIMIZED' mode.  For this mode a pixel is
treated as opaque only if the alpha value is equal to the maximum value.

    PNG_ALPHA_STANDARD:  The data libpng produces is encoded in the
standard way assumed by most correctly written graphics software.
The gamma encoding will be removed by libpng and the
linear component values will be pre-multiplied by the
alpha channel.

With this format the final image must be re-encoded to
match the display gamma before the image is displayed.
If your system doesn't do that, yet still seems to
perform arithmetic on the pixels without decoding them,
it is broken - check out the modes below.

With PNG_ALPHA_STANDARD libpng always produces linear
component values, whatever screen_gamma you supply.  The
screen_gamma value is, however, used as a default for
the file gamma if the PNG file has no gamma information.

If you call png_set_gamma() after png_set_alpha_mode() you
will override the linear encoding.  Instead the
pre-multiplied pixel values will be gamma encoded but
the alpha channel will still be linear.  This may
actually match the requirements of some broken software,
but it is unlikely.

While linear 8-bit data is often used it has
insufficient precision for any image with a reasonable
dynamic range.  To avoid problems, and if your software
supports it, use png_set_expand_16() to force all
components to 16 bits.

    PNG_ALPHA_OPTIMIZED: This mode is the same as PNG_ALPHA_STANDARD
except that completely opaque pixels are gamma encoded according to
the screen_gamma value.  Pixels with alpha less than 1.0
will still have linear components.

Use this format if you have control over your
compositing software and so don't do other arithmetic
(such as scaling) on the data you get from libpng.  Your
compositing software can simply copy opaque pixels to
the output but still has linear values for the
non-opaque pixels.

In normal compositing, where the alpha channel encodes
partial pixel coverage (as opposed to broad area
translucency), the inaccuracies of the 8-bit
representation of non-opaque pixels are irrelevant.

You can also try this format if your software is broken;
it might look better.

    PNG_ALPHA_BROKEN: This is PNG_ALPHA_STANDARD; however, all component
values, including the alpha channel are gamma encoded.  This is
broken because, in practice, no implementation that uses this choice
correctly undoes the encoding before handling alpha composition.  Use this
choice only if other serious errors in the software or hardware you use
mandate it.  In most cases of broken software or hardware the bug in the
final display manifests as a subtle halo around composited parts of the
image.  You may not even perceive this as a halo; the composited part of
the image may simply appear separate from the background, as though it had
been cut out of paper and pasted on afterward.

If you don't have to deal with bugs in software or hardware, or if you can fix
them, there are three recommended ways of using png_set_alpha_mode():

   png_set_alpha_mode(png_ptr, PNG_ALPHA_PNG,
       screen_gamma);

You can do color correction on the result (libpng does not currently
support color correction internally).  When you handle the alpha channel
you need to undo the gamma encoding and multiply out the alpha.

   png_set_alpha_mode(png_ptr, PNG_ALPHA_STANDARD,
       screen_gamma);
   png_set_expand_16(png_ptr);

If you are using the high level interface, don't call png_set_expand_16();
instead pass PNG_TRANSFORM_EXPAND_16 to the interface.

With this mode you can't do color correction, but you can do arithmetic,
including composition and scaling, on the data without further processing.

   png_set_alpha_mode(png_ptr, PNG_ALPHA_OPTIMIZED,
       screen_gamma);

You can avoid the expansion to 16-bit components with this mode, but you
lose the ability to scale the image or perform other linear arithmetic.
All you can do is compose the result onto a matching output.  Since this
mode is libpng-specific you also need to write your own composition
software.

The following are examples of calls to png_set_alpha_mode to achieve the
required overall gamma correction and, where necessary, alpha
premultiplication.

    png_set_alpha_mode(pp, PNG_ALPHA_PNG, PNG_DEFAULT_sRGB);

This is the default libpng handling of the alpha channel - it is not
pre-multiplied into the color components.  In addition the call states
that the output is for a sRGB system and causes all PNG files without gAMA
chunks to be assumed to be encoded using sRGB.

    png_set_alpha_mode(pp, PNG_ALPHA_PNG, PNG_GAMMA_MAC);

In this case the output is assumed to be something like an sRGB conformant
display preceeded by a power-law lookup table of power 1.45.  This is how
early Mac systems behaved.

    png_set_alpha_mode(pp, PNG_ALPHA_STANDARD, PNG_GAMMA_LINEAR);

This is the classic Jim Blinn approach and will work in academic
environments where everything is done by the book.  It has the shortcoming
of assuming that input PNG data with no gamma information is linear - this
is unlikely to be correct unless the PNG files where generated locally.
Most of the time the output precision will be so low as to show
significant banding in dark areas of the image.

    png_set_expand_16(pp);
    png_set_alpha_mode(pp, PNG_ALPHA_STANDARD, PNG_DEFAULT_sRGB);

This is a somewhat more realistic Jim Blinn inspired approach.  PNG files
are assumed to have the sRGB encoding if not marked with a gamma value and
the output is always 16 bits per component.  This permits accurate scaling
and processing of the data.  If you know that your input PNG files were
generated locally you might need to replace PNG_DEFAULT_sRGB with the
correct value for your system.

    png_set_alpha_mode(pp, PNG_ALPHA_OPTIMIZED, PNG_DEFAULT_sRGB);

If you just need to composite the PNG image onto an existing background
and if you control the code that does this you can use the optimization
setting.  In this case you just copy completely opaque pixels to the
output.  For pixels that are not completely transparent (you just skip
those) you do the composition math using png_composite or png_composite_16
below then encode the resultant 8-bit or 16-bit values to match the output
encoding.

    Other cases

If neither the PNG nor the standard linear encoding work for you because
of the software or hardware you use then you have a big problem.  The PNG
case will probably result in halos around the image.  The linear encoding
will probably result in a washed out, too bright, image (it's actually too
contrasty.)  Try the ALPHA_OPTIMIZED mode above - this will probably
substantially reduce the halos.  Alternatively try:

    png_set_alpha_mode(pp, PNG_ALPHA_BROKEN, PNG_DEFAULT_sRGB);

This option will also reduce the halos, but there will be slight dark
halos round the opaque parts of the image where the background is light.
In the OPTIMIZED mode the halos will be light halos where the background
is dark.  Take your pick - the halos are unavoidable unless you can get
your hardware/software fixed!  (The OPTIMIZED approach is slightly
faster.)

When the default gamma of PNG files doesn't match the output gamma.
If you have PNG files with no gamma information png_set_alpha_mode allows
you to provide a default gamma, but it also sets the ouput gamma to the
matching value.  If you know your PNG files have a gamma that doesn't
match the output you can take advantage of the fact that
png_set_alpha_mode always sets the output gamma but only sets the PNG
default if it is not already set:

    png_set_alpha_mode(pp, PNG_ALPHA_PNG, PNG_DEFAULT_sRGB);
    png_set_alpha_mode(pp, PNG_ALPHA_PNG, PNG_GAMMA_MAC);

The first call sets both the default and the output gamma values, the
second call overrides the output gamma without changing the default.  This
is easier than achieving the same effect with png_set_gamma.  You must use
PNG_ALPHA_PNG for the first call - internal checking in png_set_alpha will
fire if more than one call to png_set_alpha_mode and png_set_background is
made in the same read operation, however multiple calls with PNG_ALPHA_PNG
are ignored.

If you don't need, or can't handle, the alpha channel you can call
png_set_background() to remove it by compositing against a fixed color.  Don't
call png_set_strip_alpha() to do this - it will leave spurious pixel values in
transparent parts of this image.

   png_set_background(png_ptr, &background_color,
       PNG_BACKGROUND_GAMMA_SCREEN, 0, 1);

The background_color is an RGB or grayscale value according to the data format
libpng will produce for you.  Because you don't yet know the format of the PNG
file, if you call png_set_background at this point you must arrange for the
format produced by libpng to always have 8-bit or 16-bit components and then
store the color as an 8-bit or 16-bit color as appropriate.  The color contains
separate gray and RGB component values, so you can let libpng produce gray or
RGB output according to the input format, but low bit depth grayscale images
must always be converted to at least 8-bit format.  (Even though low bit depth
grayscale images can't have an alpha channel they can have a transparent
color!)

You set the transforms you need later, either as flags to the high level
interface or libpng API calls for the low level interface.  For reference the
settings and API calls required are:

8-bit values:
   PNG_TRANSFORM_SCALE_16 | PNG_EXPAND
   png_set_expand(png_ptr); png_set_scale_16(png_ptr);

   If you must get exactly the same inaccurate results
   produced by default in versions prior to libpng-1.5.4,
   use PNG_TRANSFORM_STRIP_16 and png_set_strip_16(png_ptr)
   instead.

16-bit values:
   PNG_TRANSFORM_EXPAND_16
   png_set_expand_16(png_ptr);

In either case palette image data will be expanded to RGB.  If you just want
color data you can add PNG_TRANSFORM_GRAY_TO_RGB or png_set_gray_to_rgb(png_ptr)
to the list.

Calling png_set_background before the PNG file header is read will not work
prior to libpng-1.5.4.  Because the failure may result in unexpected warnings or
errors it is therefore much safer to call png_set_background after the head has
been read.  Unfortunately this means that prior to libpng-1.5.4 it cannot be
used with the high level interface.

The high-level read interface

At this point there are two ways to proceed; through the high-level
read interface, or through a sequence of low-level read operations.
You can use the high-level interface if (a) you are willing to read
the entire image into memory, and (b) the input transformations
you want to do are limited to the following set:

    PNG_TRANSFORM_IDENTITY      No transformation
    PNG_TRANSFORM_SCALE_16      Strip 16-bit samples to
                                8-bit accurately
    PNG_TRANSFORM_STRIP_16      Chop 16-bit samples to
                                8-bit less accurately
    PNG_TRANSFORM_STRIP_ALPHA   Discard the alpha channel
    PNG_TRANSFORM_PACKING       Expand 1, 2 and 4-bit
                                samples to bytes
    PNG_TRANSFORM_PACKSWAP      Change order of packed
                                pixels to LSB first
    PNG_TRANSFORM_EXPAND        Perform set_expand()
    PNG_TRANSFORM_INVERT_MONO   Invert monochrome images
    PNG_TRANSFORM_SHIFT         Normalize pixels to the
                                sBIT depth
    PNG_TRANSFORM_BGR           Flip RGB to BGR, RGBA
                                to BGRA
    PNG_TRANSFORM_SWAP_ALPHA    Flip RGBA to ARGB or GA
                                to AG
    PNG_TRANSFORM_INVERT_ALPHA  Change alpha from opacity
                                to transparency
    PNG_TRANSFORM_SWAP_ENDIAN   Byte-swap 16-bit samples
    PNG_TRANSFORM_GRAY_TO_RGB   Expand grayscale samples
                                to RGB (or GA to RGBA)
    PNG_TRANSFORM_EXPAND_16     Expand samples to 16 bits

(This excludes setting a background color, doing gamma transformation,
quantizing, and setting filler.)  If this is the case, simply do this:

    png_read_png(png_ptr, info_ptr, png_transforms, NULL)

where png_transforms is an integer containing the bitwise OR of some
set of transformation flags.  This call is equivalent to png_read_info(),
followed the set of transformations indicated by the transform mask,
then png_read_image(), and finally png_read_end().

(The final parameter of this call is not yet used.  Someday it might point
to transformation parameters required by some future input transform.)

You must use png_transforms and not call any png_set_transform() functions
when you use png_read_png().

After you have called png_read_png(), you can retrieve the image data
with

   row_pointers = png_get_rows(png_ptr, info_ptr);

where row_pointers is an array of pointers to the pixel data for each row:

   png_bytep row_pointers[height];

If you know your image size and pixel size ahead of time, you can allocate
row_pointers prior to calling png_read_png() with

   if (height > PNG_UINT_32_MAX/(sizeof (png_byte)))
      png_error (png_ptr,
          "Image is too tall to process in memory");

   if (width > PNG_UINT_32_MAX/pixel_size)
      png_error (png_ptr,
          "Image is too wide to process in memory");

   row_pointers = png_malloc(png_ptr,
       height*(sizeof (png_bytep)));

   for (int i=0; i<height, i++)
      row_pointers[i]=NULL;  /* security precaution */

   for (int i=0; i<height, i++)
      row_pointers[i]=png_malloc(png_ptr,
          width*pixel_size);

   png_set_rows(png_ptr, info_ptr, &row_pointers);

Alternatively you could allocate your image in one big block and define
row_pointers[i] to point into the proper places in your block.

If you use png_set_rows(), the application is responsible for freeing
row_pointers (and row_pointers[i], if they were separately allocated).

If you don't allocate row_pointers ahead of time, png_read_png() will
do it, and it'll be free'ed by libpng when you call png_destroy_*().

The low-level read interface

If you are going the low-level route, you are now ready to read all
the file information up to the actual image data.  You do this with a
call to png_read_info().

    png_read_info(png_ptr, info_ptr);

This will process all chunks up to but not including the image data.

This also copies some of the data from the PNG file into the decode structure
for use in later transformations.  Important information copied in is:

1) The PNG file gamma from the gAMA chunk.  This overwrites the default value
provided by an earlier call to png_set_gamma or png_set_alpha_mode.

2) Prior to libpng-1.5.4 the background color from a bKGd chunk.  This
damages the information provided by an earlier call to png_set_background
resulting in unexpected behavior.  Libpng-1.5.4 no longer does this.

3) The number of significant bits in each component value.  Libpng uses this to
optimize gamma handling by reducing the internal lookup table sizes.

4) The transparent color information from a tRNS chunk.  This can be modified by
a later call to png_set_tRNS.

Querying the info structure

Functions are used to get the information from the info_ptr once it
has been read.  Note that these fields may not be completely filled
in until png_read_end() has read the chunk data following the image.

    png_get_IHDR(png_ptr, info_ptr, &width, &height,
       &bit_depth, &color_type, &interlace_type,
       &compression_type, &filter_method);

    width          - holds the width of the image
                     in pixels (up to 2^31).

    height         - holds the height of the image
                     in pixels (up to 2^31).

    bit_depth      - holds the bit depth of one of the
                     image channels.  (valid values are
                     1, 2, 4, 8, 16 and depend also on
                     the color_type.  See also
                     significant bits (sBIT) below).

    color_type     - describes which color/alpha channels
                         are present.
                     PNG_COLOR_TYPE_GRAY
                        (bit depths 1, 2, 4, 8, 16)
                     PNG_COLOR_TYPE_GRAY_ALPHA
                        (bit depths 8, 16)
                     PNG_COLOR_TYPE_PALETTE
                        (bit depths 1, 2, 4, 8)
                     PNG_COLOR_TYPE_RGB
                        (bit_depths 8, 16)
                     PNG_COLOR_TYPE_RGB_ALPHA
                        (bit_depths 8, 16)

                     PNG_COLOR_MASK_PALETTE
                     PNG_COLOR_MASK_COLOR
                     PNG_COLOR_MASK_ALPHA

    interlace_type - (PNG_INTERLACE_NONE or
                     PNG_INTERLACE_ADAM7)

    compression_type - (must be PNG_COMPRESSION_TYPE_BASE
                     for PNG 1.0)

    filter_method  - (must be PNG_FILTER_TYPE_BASE
                     for PNG 1.0, and can also be
                     PNG_INTRAPIXEL_DIFFERENCING if
                     the PNG datastream is embedded in
                     a MNG-1.0 datastream)

    Any of width, height, color_type, bit_depth,
    interlace_type, compression_type, or filter_method can
    be NULL if you are not interested in their values.

    Note that png_get_IHDR() returns 32-bit data into
    the application's width and height variables.
    This is an unsafe situation if these are not png_uint_32
    variables.  In such situations, the
    png_get_image_width() and png_get_image_height()
    functions described below are safer.

    width            = png_get_image_width(png_ptr,
                         info_ptr);

    height           = png_get_image_height(png_ptr,
                         info_ptr);

    bit_depth        = png_get_bit_depth(png_ptr,
                         info_ptr);

    color_type       = png_get_color_type(png_ptr,
                         info_ptr);

    interlace_type   = png_get_interlace_type(png_ptr,
                         info_ptr);

    compression_type = png_get_compression_type(png_ptr,
                         info_ptr);

    filter_method    = png_get_filter_type(png_ptr,
                         info_ptr);

    channels = png_get_channels(png_ptr, info_ptr);

    channels       - number of channels of info for the
                     color type (valid values are 1 (GRAY,
                     PALETTE), 2 (GRAY_ALPHA), 3 (RGB),
                     4 (RGB_ALPHA or RGB + filler byte))

    rowbytes = png_get_rowbytes(png_ptr, info_ptr);

    rowbytes       - number of bytes needed to hold a row

    signature = png_get_signature(png_ptr, info_ptr);

    signature      - holds the signature read from the
                     file (if any).  The data is kept in
                     the same offset it would be if the
                     whole signature were read (i.e. if an
                     application had already read in 4
                     bytes of signature before starting
                     libpng, the remaining 4 bytes would
                     be in signature[4] through signature[7]
                     (see png_set_sig_bytes())).

These are also important, but their validity depends on whether the chunk
has been read.  The png_get_valid(png_ptr, info_ptr, PNG_INFO_<chunk>) and
png_get_<chunk>(png_ptr, info_ptr, ...) functions return non-zero if the
data has been read, or zero if it is missing.  The parameters to the
png_get_<chunk> are set directly if they are simple data types, or a
pointer into the info_ptr is returned for any complex types.

The colorspace data from gAMA, cHRM, sRGB, iCCP, and sBIT chunks
is simply returned to give the application information about how the
image was encoded.  Libpng itself only does transformations using the file
gamma when combining semitransparent pixels with the background color, and,
since libpng-1.6.0, when converting between 8-bit sRGB and 16-bit linear pixels
within the simplified API.  Libpng also uses the file gamma when converting
RGB to gray, beginning with libpng-1.0.5, if the application calls
png_set_rgb_to_gray()).

    png_get_PLTE(png_ptr, info_ptr, &palette,
                     &num_palette);

    palette        - the palette for the file
                     (array of png_color)

    num_palette    - number of entries in the palette

    png_get_gAMA(png_ptr, info_ptr, &file_gamma);
    png_get_gAMA_fixed(png_ptr, info_ptr, &int_file_gamma);

    file_gamma     - the gamma at which the file is
                     written (PNG_INFO_gAMA)

    int_file_gamma - 100,000 times the gamma at which the
                     file is written

    png_get_cHRM(png_ptr, info_ptr,  &white_x, &white_y, &red_x,
                     &red_y, &green_x, &green_y, &blue_x, &blue_y)
    png_get_cHRM_XYZ(png_ptr, info_ptr, &red_X, &red_Y, &red_Z,
                     &green_X, &green_Y, &green_Z, &blue_X, &blue_Y,
                     &blue_Z)
    png_get_cHRM_fixed(png_ptr, info_ptr, &int_white_x,
                     &int_white_y, &int_red_x, &int_red_y,
                     &int_green_x, &int_green_y, &int_blue_x,
                     &int_blue_y)
    png_get_cHRM_XYZ_fixed(png_ptr, info_ptr, &int_red_X, &int_red_Y,
                     &int_red_Z, &int_green_X, &int_green_Y,
                     &int_green_Z, &int_blue_X, &int_blue_Y,
                     &int_blue_Z)

    {white,red,green,blue}_{x,y}
                     A color space encoding specified using the
                     chromaticities of the end points and the
                     white point. (PNG_INFO_cHRM)

    {red,green,blue}_{X,Y,Z}
                     A color space encoding specified using the
                     encoding end points - the CIE tristimulus
                     specification of the intended color of the red,
                     green and blue channels in the PNG RGB data.
                     The white point is simply the sum of the three
                     end points. (PNG_INFO_cHRM)

    png_get_sRGB(png_ptr, info_ptr, &srgb_intent);

    srgb_intent -    the rendering intent (PNG_INFO_sRGB)
                     The presence of the sRGB chunk
                     means that the pixel data is in the
                     sRGB color space.  This chunk also
                     implies specific values of gAMA and
                     cHRM.

    png_get_iCCP(png_ptr, info_ptr, &name,
       &compression_type, &profile, &proflen);

    name             - The profile name.

    compression_type - The compression type; always
                       PNG_COMPRESSION_TYPE_BASE for PNG 1.0.
                       You may give NULL to this argument to
                       ignore it.

    profile          - International Color Consortium color
                       profile data. May contain NULs.

    proflen          - length of profile data in bytes.

    png_get_sBIT(png_ptr, info_ptr, &sig_bit);

    sig_bit        - the number of significant bits for
                     (PNG_INFO_sBIT) each of the gray,
                     red, green, and blue channels,
                     whichever are appropriate for the
                     given color type (png_color_16)

    png_get_tRNS(png_ptr, info_ptr, &trans_alpha,
                     &num_trans, &trans_color);

    trans_alpha    - array of alpha (transparency)
                     entries for palette (PNG_INFO_tRNS)

    num_trans      - number of transparent entries
                     (PNG_INFO_tRNS)

    trans_color    - graylevel or color sample values of
                     the single transparent color for
                     non-paletted images (PNG_INFO_tRNS)

    png_get_hIST(png_ptr, info_ptr, &hist);
                     (PNG_INFO_hIST)

    hist           - histogram of palette (array of
                     png_uint_16)

    png_get_tIME(png_ptr, info_ptr, &mod_time);

    mod_time       - time image was last modified
                    (PNG_VALID_tIME)

    png_get_bKGD(png_ptr, info_ptr, &background);

    background     - background color (of type
                     png_color_16p) (PNG_VALID_bKGD)
                     valid 16-bit red, green and blue
                     values, regardless of color_type

    num_comments   = png_get_text(png_ptr, info_ptr,
                     &text_ptr, &num_text);

    num_comments   - number of comments

    text_ptr       - array of png_text holding image
                     comments

    text_ptr[i].compression - type of compression used
                 on "text" PNG_TEXT_COMPRESSION_NONE
                           PNG_TEXT_COMPRESSION_zTXt
                           PNG_ITXT_COMPRESSION_NONE
                           PNG_ITXT_COMPRESSION_zTXt

    text_ptr[i].key   - keyword for comment.  Must contain
                         1-79 characters.

    text_ptr[i].text  - text comments for current
                         keyword.  Can be empty.

    text_ptr[i].text_length - length of text string,
                 after decompression, 0 for iTXt

    text_ptr[i].itxt_length - length of itxt string,
                 after decompression, 0 for tEXt/zTXt

    text_ptr[i].lang  - language of comment (empty
                         string for unknown).

    text_ptr[i].lang_key  - keyword in UTF-8
                         (empty string for unknown).

    Note that the itxt_length, lang, and lang_key
    members of the text_ptr structure only exist when the
    library is built with iTXt chunk support.  Prior to
    libpng-1.4.0 the library was built by default without
    iTXt support. Also note that when iTXt is supported,
    they contain NULL pointers when the "compression"
    field contains PNG_TEXT_COMPRESSION_NONE or
    PNG_TEXT_COMPRESSION_zTXt.

    num_text       - number of comments (same as
                     num_comments; you can put NULL here
                     to avoid the duplication)

    Note while png_set_text() will accept text, language,
    and translated keywords that can be NULL pointers, the
    structure returned by png_get_text will always contain
    regular zero-terminated C strings.  They might be
    empty strings but they will never be NULL pointers.

    num_spalettes = png_get_sPLT(png_ptr, info_ptr,
       &palette_ptr);

    num_spalettes  - number of sPLT chunks read.

    palette_ptr    - array of palette structures holding
                     contents of one or more sPLT chunks
                     read.

    png_get_oFFs(png_ptr, info_ptr, &offset_x, &offset_y,
       &unit_type);

    offset_x       - positive offset from the left edge
                     of the screen (can be negative)

    offset_y       - positive offset from the top edge
                     of the screen (can be negative)

    unit_type      - PNG_OFFSET_PIXEL, PNG_OFFSET_MICROMETER

    png_get_pHYs(png_ptr, info_ptr, &res_x, &res_y,
       &unit_type);

    res_x          - pixels/unit physical resolution in
                     x direction

    res_y          - pixels/unit physical resolution in
                     x direction

    unit_type      - PNG_RESOLUTION_UNKNOWN,
                     PNG_RESOLUTION_METER

    png_get_sCAL(png_ptr, info_ptr, &unit, &width,
       &height)

    unit        - physical scale units (an integer)

    width       - width of a pixel in physical scale units

    height      - height of a pixel in physical scale units
                 (width and height are doubles)

    png_get_sCAL_s(png_ptr, info_ptr, &unit, &width,
       &height)

    unit        - physical scale units (an integer)

    width       - width of a pixel in physical scale units
                  (expressed as a string)

    height      - height of a pixel in physical scale units
                 (width and height are strings like "2.54")

    num_unknown_chunks = png_get_unknown_chunks(png_ptr,
       info_ptr, &unknowns)

    unknowns          - array of png_unknown_chunk
                        structures holding unknown chunks

    unknowns[i].name  - name of unknown chunk

    unknowns[i].data  - data of unknown chunk

    unknowns[i].size  - size of unknown chunk's data

    unknowns[i].location - position of chunk in file

    The value of "i" corresponds to the order in which the
    chunks were read from the PNG file or inserted with the
    png_set_unknown_chunks() function.

    The value of "location" is a bitwise "or" of

         PNG_HAVE_IHDR  (0x01)
         PNG_HAVE_PLTE  (0x02)
         PNG_AFTER_IDAT (0x08)

The data from the pHYs chunk can be retrieved in several convenient
forms:

    res_x = png_get_x_pixels_per_meter(png_ptr,
       info_ptr)

    res_y = png_get_y_pixels_per_meter(png_ptr,
       info_ptr)

    res_x_and_y = png_get_pixels_per_meter(png_ptr,
       info_ptr)

    res_x = png_get_x_pixels_per_inch(png_ptr,
       info_ptr)

    res_y = png_get_y_pixels_per_inch(png_ptr,
       info_ptr)

    res_x_and_y = png_get_pixels_per_inch(png_ptr,
       info_ptr)

    aspect_ratio = png_get_pixel_aspect_ratio(png_ptr,
       info_ptr)

    Each of these returns 0 [signifying "unknown"] if
       the data is not present or if res_x is 0;
       res_x_and_y is 0 if res_x != res_y

    Note that because of the way the resolutions are
       stored internally, the inch conversions won't
       come out to exactly even number.  For example,
       72 dpi is stored as 0.28346 pixels/meter, and
       when this is retrieved it is 71.9988 dpi, so
       be sure to round the returned value appropriately
       if you want to display a reasonable-looking result.

The data from the oFFs chunk can be retrieved in several convenient
forms:

    x_offset = png_get_x_offset_microns(png_ptr, info_ptr);

    y_offset = png_get_y_offset_microns(png_ptr, info_ptr);

    x_offset = png_get_x_offset_inches(png_ptr, info_ptr);

    y_offset = png_get_y_offset_inches(png_ptr, info_ptr);

    Each of these returns 0 [signifying "unknown" if both
       x and y are 0] if the data is not present or if the
       chunk is present but the unit is the pixel.  The
       remark about inexact inch conversions applies here
       as well, because a value in inches can't always be
       converted to microns and back without some loss
       of precision.

For more information, see the
PNG specification for chunk contents.  Be careful with trusting
rowbytes, as some of the transformations could increase the space
needed to hold a row (expand, filler, gray_to_rgb, etc.).
See png_read_update_info(), below.

A quick word about text_ptr and num_text.  PNG stores comments in
keyword/text pairs, one pair per chunk, with no limit on the number
of text chunks, and a 2^31 byte limit on their size.  While there are
suggested keywords, there is no requirement to restrict the use to these
strings.  It is strongly suggested that keywords and text be sensible
to humans (that's the point), so don't use abbreviations.  Non-printing
symbols are not allowed.  See the PNG specification for more details.
There is also no requirement to have text after the keyword.

Keywords should be limited to 79 Latin-1 characters without leading or
trailing spaces, but non-consecutive spaces are allowed within the
keyword.  It is possible to have the same keyword any number of times.
The text_ptr is an array of png_text structures, each holding a
pointer to a language string, a pointer to a keyword and a pointer to
a text string.  The text string, language code, and translated
keyword may be empty or NULL pointers.  The keyword/text
pairs are put into the array in the order that they are received.
However, some or all of the text chunks may be after the image, so, to
make sure you have read all the text chunks, don't mess with these
until after you read the stuff after the image.  This will be
mentioned again below in the discussion that goes with png_read_end().

Input transformations

After you've read the header information, you can set up the library
to handle any special transformations of the image data.  The various
ways to transform the data will be described in the order that they
should occur.  This is important, as some of these change the color
type and/or bit depth of the data, and some others only work on
certain color types and bit depths.

Transformations you request are ignored if they don't have any meaning for a
particular input data format.  However some transformations can have an effect
as a result of a previous transformation.  If you specify a contradictory set of
transformations, for example both adding and removing the alpha channel, you
cannot predict the final result.

The color used for the transparency values should be supplied in the same
format/depth as the current image data.  It is stored in the same format/depth
as the image data in a tRNS chunk, so this is what libpng expects for this data.

The color used for the background value depends on the need_expand argument as
described below.

Data will be decoded into the supplied row buffers packed into bytes
unless the library has been told to transform it into another format.
For example, 4 bit/pixel paletted or grayscale data will be returned
2 pixels/byte with the leftmost pixel in the high-order bits of the
byte, unless png_set_packing() is called.  8-bit RGB data will be stored
in RGB RGB RGB format unless png_set_filler() or png_set_add_alpha()
is called to insert filler bytes, either before or after each RGB triplet.
16-bit RGB data will be returned RRGGBB RRGGBB, with the most significant
byte of the color value first, unless png_set_scale_16() is called to
transform it to regular RGB RGB triplets, or png_set_filler() or
png_set_add alpha() is called to insert filler bytes, either before or
after each RRGGBB triplet.  Similarly, 8-bit or 16-bit grayscale data can
be modified with png_set_filler(), png_set_add_alpha(), png_set_strip_16(),
or png_set_scale_16().

The following code transforms grayscale images of less than 8 to 8 bits,
changes paletted images to RGB, and adds a full alpha channel if there is
transparency information in a tRNS chunk.  This is most useful on
grayscale images with bit depths of 2 or 4 or if there is a multiple-image
viewing application that wishes to treat all images in the same way.

    if (color_type == PNG_COLOR_TYPE_PALETTE)
        png_set_palette_to_rgb(png_ptr);

    if (png_get_valid(png_ptr, info_ptr,
        PNG_INFO_tRNS)) png_set_tRNS_to_alpha(png_ptr);

    if (color_type == PNG_COLOR_TYPE_GRAY &&
        bit_depth < 8) png_set_expand_gray_1_2_4_to_8(png_ptr);

The first two functions are actually aliases for png_set_expand(), added
in libpng version 1.0.4, with the function names expanded to improve code
readability.  In some future version they may actually do different
things.

As of libpng version 1.2.9, png_set_expand_gray_1_2_4_to_8() was
added.  It expands the sample depth without changing tRNS to alpha.

As of libpng version 1.5.2, png_set_expand_16() was added.  It behaves as
png_set_expand(); however, the resultant channels have 16 bits rather than 8.
Use this when the output color or gray channels are made linear to avoid fairly
severe accuracy loss.

   if (bit_depth < 16)
      png_set_expand_16(png_ptr);

PNG can have files with 16 bits per channel.  If you only can handle
8 bits per channel, this will strip the pixels down to 8-bit.

    if (bit_depth == 16)
#if PNG_LIBPNG_VER >= 10504
       png_set_scale_16(png_ptr);
#else
       png_set_strip_16(png_ptr);
#endif

(The more accurate "png_set_scale_16()" API became available in libpng version
1.5.4).

If you need to process the alpha channel on the image separately from the image
data (for example if you convert it to a bitmap mask) it is possible to have
libpng strip the channel leaving just RGB or gray data:

    if (color_type & PNG_COLOR_MASK_ALPHA)
       png_set_strip_alpha(png_ptr);

If you strip the alpha channel you need to find some other way of dealing with
the information.  If, instead, you want to convert the image to an opaque
version with no alpha channel use png_set_background; see below.

As of libpng version 1.5.2, almost all useful expansions are supported, the
major ommissions are conversion of grayscale to indexed images (which can be
done trivially in the application) and conversion of indexed to grayscale (which
can be done by a trivial manipulation of the palette.)

In the following table, the 01 means grayscale with depth<8, 31 means
indexed with depth<8, other numerals represent the color type, "T" means
the tRNS chunk is present, A means an alpha channel is present, and O
means tRNS or alpha is present but all pixels in the image are opaque.

  FROM  01  31   0  0T  0O   2  2T  2O   3  3T  3O  4A  4O  6A  6O
   TO
   01    -  [G]  -   -   -   -   -   -   -   -   -   -   -   -   -
   31   [Q]  Q  [Q] [Q] [Q]  Q   Q   Q   Q   Q   Q  [Q] [Q]  Q   Q
    0    1   G   +   .   .   G   G   G   G   G   G   B   B  GB  GB
   0T    lt  Gt  t   +   .   Gt  G   G   Gt  G   G   Bt  Bt GBt GBt
   0O    lt  Gt  t   .   +   Gt  Gt  G   Gt  Gt  G   Bt  Bt GBt GBt
    2    C   P   C   C   C   +   .   .   C   -   -  CB  CB   B   B
   2T    Ct  -   Ct  C   C   t   +   t   -   -   -  CBt CBt  Bt  Bt
   2O    Ct  -   Ct  C   C   t   t   +   -   -   -  CBt CBt  Bt  Bt
    3   [Q]  p  [Q] [Q] [Q]  Q   Q   Q   +   .   .  [Q] [Q]  Q   Q
   3T   [Qt] p  [Qt][Q] [Q]  Qt  Qt  Qt  t   +   t  [Qt][Qt] Qt  Qt
   3O   [Qt] p  [Qt][Q] [Q]  Qt  Qt  Qt  t   t   +  [Qt][Qt] Qt  Qt
   4A    lA  G   A   T   T   GA  GT  GT  GA  GT  GT  +   BA  G  GBA
   4O    lA GBA  A   T   T   GA  GT  GT  GA  GT  GT  BA  +  GBA  G
   6A    CA  PA  CA  C   C   A   T  tT   PA  P   P   C  CBA  +   BA
   6O    CA PBA  CA  C   C   A  tT   T   PA  P   P  CBA  C   BA  +

Within the matrix,
     "+" identifies entries where 'from' and 'to' are the same.
     "-" means the transformation is not supported.
     "." means nothing is necessary (a tRNS chunk can just be ignored).
     "t" means the transformation is obtained by png_set_tRNS.
     "A" means the transformation is obtained by png_set_add_alpha().
     "X" means the transformation is obtained by png_set_expand().
     "1" means the transformation is obtained by
         png_set_expand_gray_1_2_4_to_8() (and by png_set_expand()
         if there is no transparency in the original or the final
         format).
     "C" means the transformation is obtained by png_set_gray_to_rgb().
     "G" means the transformation is obtained by png_set_rgb_to_gray().
     "P" means the transformation is obtained by
         png_set_expand_palette_to_rgb().
     "p" means the transformation is obtained by png_set_packing().
     "Q" means the transformation is obtained by png_set_quantize().
     "T" means the transformation is obtained by
         png_set_tRNS_to_alpha().
     "B" means the transformation is obtained by
         png_set_background(), or png_strip_alpha().

When an entry has multiple transforms listed all are required to cause the
right overall transformation.  When two transforms are separated by a comma
either will do the job.  When transforms are enclosed in [] the transform should
do the job but this is currently unimplemented - a different format will result
if the suggested transformations are used.

In PNG files, the alpha channel in an image
is the level of opacity.  If you need the alpha channel in an image to
be the level of transparency instead of opacity, you can invert the
alpha channel (or the tRNS chunk data) after it's read, so that 0 is
fully opaque and 255 (in 8-bit or paletted images) or 65535 (in 16-bit
images) is fully transparent, with

    png_set_invert_alpha(png_ptr);

PNG files pack pixels of bit depths 1, 2, and 4 into bytes as small as
they can, resulting in, for example, 8 pixels per byte for 1 bit
files.  This code expands to 1 pixel per byte without changing the
values of the pixels:

    if (bit_depth < 8)
       png_set_packing(png_ptr);

PNG files have possible bit depths of 1, 2, 4, 8, and 16.  All pixels
stored in a PNG image have been "scaled" or "shifted" up to the next
higher possible bit depth (e.g. from 5 bits/sample in the range [0,31]
to 8 bits/sample in the range [0, 255]).  However, it is also possible
to convert the PNG pixel data back to the original bit depth of the
image.  This call reduces the pixels back down to the original bit depth:

    png_color_8p sig_bit;

    if (png_get_sBIT(png_ptr, info_ptr, &sig_bit))
       png_set_shift(png_ptr, sig_bit);

PNG files store 3-color pixels in red, green, blue order.  This code
changes the storage of the pixels to blue, green, red:

    if (color_type == PNG_COLOR_TYPE_RGB ||
        color_type == PNG_COLOR_TYPE_RGB_ALPHA)
       png_set_bgr(png_ptr);

PNG files store RGB pixels packed into 3 or 6 bytes. This code expands them
into 4 or 8 bytes for windowing systems that need them in this format:

    if (color_type == PNG_COLOR_TYPE_RGB)
       png_set_filler(png_ptr, filler, PNG_FILLER_BEFORE);

where "filler" is the 8 or 16-bit number to fill with, and the location is
either PNG_FILLER_BEFORE or PNG_FILLER_AFTER, depending upon whether
you want the filler before the RGB or after.  This transformation
does not affect images that already have full alpha channels.  To add an
opaque alpha channel, use filler=0xff or 0xffff and PNG_FILLER_AFTER which
will generate RGBA pixels.

Note that png_set_filler() does not change the color type.  If you want
to do that, you can add a true alpha channel with

    if (color_type == PNG_COLOR_TYPE_RGB ||
       color_type == PNG_COLOR_TYPE_GRAY)
       png_set_add_alpha(png_ptr, filler, PNG_FILLER_AFTER);

where "filler" contains the alpha value to assign to each pixel.
This function was added in libpng-1.2.7.

If you are reading an image with an alpha channel, and you need the
data as ARGB instead of the normal PNG format RGBA:

    if (color_type == PNG_COLOR_TYPE_RGB_ALPHA)
       png_set_swap_alpha(png_ptr);

For some uses, you may want a grayscale image to be represented as
RGB.  This code will do that conversion:

    if (color_type == PNG_COLOR_TYPE_GRAY ||
        color_type == PNG_COLOR_TYPE_GRAY_ALPHA)
       png_set_gray_to_rgb(png_ptr);

Conversely, you can convert an RGB or RGBA image to grayscale or grayscale
with alpha.

    if (color_type == PNG_COLOR_TYPE_RGB ||
        color_type == PNG_COLOR_TYPE_RGB_ALPHA)
       png_set_rgb_to_gray(png_ptr, error_action,
          double red_weight, double green_weight);

    error_action = 1: silently do the conversion

    error_action = 2: issue a warning if the original
                      image has any pixel where
                      red != green or red != blue

    error_action = 3: issue an error and abort the
                      conversion if the original
                      image has any pixel where
                      red != green or red != blue

    red_weight:       weight of red component

    green_weight:     weight of green component
                      If either weight is negative, default
                      weights are used.

In the corresponding fixed point API the red_weight and green_weight values are
simply scaled by 100,000:

    png_set_rgb_to_gray(png_ptr, error_action,
       png_fixed_point red_weight,
       png_fixed_point green_weight);

If you have set error_action = 1 or 2, you can
later check whether the image really was gray, after processing
the image rows, with the png_get_rgb_to_gray_status(png_ptr) function.
It will return a png_byte that is zero if the image was gray or
1 if there were any non-gray pixels.  Background and sBIT data
will be silently converted to grayscale, using the green channel
data for sBIT, regardless of the error_action setting.

The default values come from the PNG file cHRM chunk if present; otherwise, the
defaults correspond to the ITU-R recommendation 709, and also the sRGB color
space, as recommended in the Charles Poynton's Colour FAQ,
<http://www.poynton.com/>, in section 9:

   <http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html#RTFToC9>

    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B

Previous versions of this document, 1998 through 2002, recommended a slightly
different formula:

    Y = 0.212671 * R + 0.715160 * G + 0.072169 * B

Libpng uses an integer approximation:

    Y = (6968 * R + 23434 * G + 2366 * B)/32768

The calculation is done in a linear colorspace, if the image gamma
can be determined.

The png_set_background() function has been described already; it tells libpng to
composite images with alpha or simple transparency against the supplied
background color.  For compatibility with versions of libpng earlier than
libpng-1.5.4 it is recommended that you call the function after reading the file
header, even if you don't want to use the color in a bKGD chunk, if one exists.

If the PNG file contains a bKGD chunk (PNG_INFO_bKGD valid),
you may use this color, or supply another color more suitable for
the current display (e.g., the background color from a web page).  You
need to tell libpng how the color is represented, both the format of the
component values in the color (the number of bits) and the gamma encoding of the
color.  The function takes two arguments, background_gamma_mode and need_expand
to convey this information; however, only two combinations are likely to be
useful:

    png_color_16 my_background;
    png_color_16p image_background;

    if (png_get_bKGD(png_ptr, info_ptr, &image_background))
       png_set_background(png_ptr, image_background,
           PNG_BACKGROUND_GAMMA_FILE, 1/*needs to be expanded*/, 1);
    else
       png_set_background(png_ptr, &my_background,
           PNG_BACKGROUND_GAMMA_SCREEN, 0/*do not expand*/, 1);

The second call was described above - my_background is in the format of the
final, display, output produced by libpng.  Because you now know the format of
the PNG it is possible to avoid the need to choose either 8-bit or 16-bit
output and to retain palette images (the palette colors will be modified
appropriately and the tRNS chunk removed.)  However, if you are doing this,
take great care not to ask for transformations without checking first that
they apply!

In the first call the background color has the original bit depth and color type
of the PNG file.  So, for palette images the color is supplied as a palette
index and for low bit greyscale images the color is a reduced bit value in
image_background->gray.

If you didn't call png_set_gamma() before reading the file header, for example
if you need your code to remain compatible with older versions of libpng prior
to libpng-1.5.4, this is the place to call it.

Do not call it if you called png_set_alpha_mode(); doing so will damage the
settings put in place by png_set_alpha_mode().  (If png_set_alpha_mode() is
supported then you can certainly do png_set_gamma() before reading the PNG
header.)

This API unconditionally sets the screen and file gamma values, so it will
override the value in the PNG file unless it is called before the PNG file
reading starts.  For this reason you must always call it with the PNG file
value when you call it in this position:

   if (png_get_gAMA(png_ptr, info_ptr, &file_gamma))
      png_set_gamma(png_ptr, screen_gamma, file_gamma);

   else
      png_set_gamma(png_ptr, screen_gamma, 0.45455);

If you need to reduce an RGB file to a paletted file, or if a paletted
file has more entries than will fit on your screen, png_set_quantize()
will do that.  Note that this is a simple match quantization that merely
finds the closest color available.  This should work fairly well with
optimized palettes, but fairly badly with linear color cubes.  If you
pass a palette that is larger than maximum_colors, the file will
reduce the number of colors in the palette so it will fit into
maximum_colors.  If there is a histogram, libpng will use it to make
more intelligent choices when reducing the palette.  If there is no
histogram, it may not do as good a job.

   if (color_type & PNG_COLOR_MASK_COLOR)
   {
      if (png_get_valid(png_ptr, info_ptr,
          PNG_INFO_PLTE))
      {
         png_uint_16p histogram = NULL;

         png_get_hIST(png_ptr, info_ptr,
             &histogram);
         png_set_quantize(png_ptr, palette, num_palette,
            max_screen_colors, histogram, 1);
      }

      else
      {
         png_color std_color_cube[MAX_SCREEN_COLORS] =
            { ... colors ... };

         png_set_quantize(png_ptr, std_color_cube,
            MAX_SCREEN_COLORS, MAX_SCREEN_COLORS,
            NULL,0);
      }
   }

PNG files describe monochrome as black being zero and white being one.
The following code will reverse this (make black be one and white be
zero):

   if (bit_depth == 1 && color_type == PNG_COLOR_TYPE_GRAY)
      png_set_invert_mono(png_ptr);

This function can also be used to invert grayscale and gray-alpha images:

   if (color_type == PNG_COLOR_TYPE_GRAY ||
       color_type == PNG_COLOR_TYPE_GRAY_ALPHA)
      png_set_invert_mono(png_ptr);

PNG files store 16-bit pixels in network byte order (big-endian,
ie. most significant bits first).  This code changes the storage to the
other way (little-endian, i.e. least significant bits first, the
way PCs store them):

    if (bit_depth == 16)
       png_set_swap(png_ptr);

If you are using packed-pixel images (1, 2, or 4 bits/pixel), and you
need to change the order the pixels are packed into bytes, you can use:

    if (bit_depth < 8)
       png_set_packswap(png_ptr);

Finally, you can write your own transformation function if none of
the existing ones meets your needs.  This is done by setting a callback
with

    png_set_read_user_transform_fn(png_ptr,
        read_transform_fn);

You must supply the function

    void read_transform_fn(png_structp png_ptr, png_row_infop
        row_info, png_bytep data)

See pngtest.c for a working example.  Your function will be called
after all of the other transformations have been processed.  Take care with
interlaced images if you do the interlace yourself - the width of the row is the
width in 'row_info', not the overall image width.

If supported, libpng provides two information routines that you can use to find
where you are in processing the image:

   png_get_current_pass_number(png_structp png_ptr);
   png_get_current_row_number(png_structp png_ptr);

Don't try using these outside a transform callback - firstly they are only
supported if user transforms are supported, secondly they may well return
unexpected results unless the row is actually being processed at the moment they
are called.

With interlaced
images the value returned is the row in the input sub-image image.  Use
PNG_ROW_FROM_PASS_ROW(row, pass) and PNG_COL_FROM_PASS_COL(col, pass) to
find the output pixel (x,y) given an interlaced sub-image pixel (row,col,pass).

The discussion of interlace handling above contains more information on how to
use these values.

You can also set up a pointer to a user structure for use by your
callback function, and you can inform libpng that your transform
function will change the number of channels or bit depth with the
function

    png_set_user_transform_info(png_ptr, user_ptr,
        user_depth, user_channels);

The user's application, not libpng, is responsible for allocating and
freeing any memory required for the user structure.

You can retrieve the pointer via the function
png_get_user_transform_ptr().  For example:

    voidp read_user_transform_ptr =
        png_get_user_transform_ptr(png_ptr);

The last thing to handle is interlacing; this is covered in detail below,
but you must call the function here if you want libpng to handle expansion
of the interlaced image.

    number_of_passes = png_set_interlace_handling(png_ptr);

After setting the transformations, libpng can update your png_info
structure to reflect any transformations you've requested with this
call.

    png_read_update_info(png_ptr, info_ptr);

This is most useful to update the info structure's rowbytes
field so you can use it to allocate your image memory.  This function
will also update your palette with the correct screen_gamma and
background if these have been given with the calls above.  You may
only call png_read_update_info() once with a particular info_ptr.

After you call png_read_update_info(), you can allocate any
memory you need to hold the image.  The row data is simply
raw byte data for all forms of images.  As the actual allocation
varies among applications, no example will be given.  If you
are allocating one large chunk, you will need to build an
array of pointers to each row, as it will be needed for some
of the functions below.

Remember: Before you call png_read_update_info(), the png_get_*()
functions return the values corresponding to the original PNG image.
After you call png_read_update_info the values refer to the image
that libpng will output.  Consequently you must call all the png_set_
functions before you call png_read_update_info().  This is particularly
important for png_set_interlace_handling() - if you are going to call
png_read_update_info() you must call png_set_interlace_handling() before
it unless you want to receive interlaced output.

Reading image data

After you've allocated memory, you can read the image data.
The simplest way to do this is in one function call.  If you are
allocating enough memory to hold the whole image, you can just
call png_read_image() and libpng will read in all the image data
and put it in the memory area supplied.  You will need to pass in
an array of pointers to each row.

This function automatically handles interlacing, so you don't
need to call png_set_interlace_handling() (unless you call
png_read_update_info()) or call this function multiple times, or any
of that other stuff necessary with png_read_rows().

   png_read_image(png_ptr, row_pointers);

where row_pointers is:

   png_bytep row_pointers[height];

You can point to void or char or whatever you use for pixels.

If you don't want to read in the whole image at once, you can
use png_read_rows() instead.  If there is no interlacing (check
interlace_type == PNG_INTERLACE_NONE), this is simple:

    png_read_rows(png_ptr, row_pointers, NULL,
        number_of_rows);

where row_pointers is the same as in the png_read_image() call.

If you are doing this just one row at a time, you can do this with
a single row_pointer instead of an array of row_pointers:

    png_bytep row_pointer = row;
    png_read_row(png_ptr, row_pointer, NULL);

If the file is interlaced (interlace_type != 0 in the IHDR chunk), things
get somewhat harder.  The only current (PNG Specification version 1.2)
interlacing type for PNG is (interlace_type == PNG_INTERLACE_ADAM7);
a somewhat complicated 2D interlace scheme, known as Adam7, that
breaks down an image into seven smaller images of varying size, based
on an 8x8 grid.  This number is defined (from libpng 1.5) as
PNG_INTERLACE_ADAM7_PASSES in png.h

libpng can fill out those images or it can give them to you "as is".
It is almost always better to have libpng handle the interlacing for you.
If you want the images filled out, there are two ways to do that.  The one
mentioned in the PNG specification is to expand each pixel to cover
those pixels that have not been read yet (the "rectangle" method).
This results in a blocky image for the first pass, which gradually
smooths out as more pixels are read.  The other method is the "sparkle"
method, where pixels are drawn only in their final locations, with the
rest of the image remaining whatever colors they were initialized to
before the start of the read.  The first method usually looks better,
but tends to be slower, as there are more pixels to put in the rows.

If, as is likely, you want libpng to expand the images, call this before
calling png_start_read_image() or png_read_update_info():

    if (interlace_type == PNG_INTERLACE_ADAM7)
       number_of_passes
           = png_set_interlace_handling(png_ptr);

This will return the number of passes needed.  Currently, this is seven,
but may change if another interlace type is added.  This function can be
called even if the file is not interlaced, where it will return one pass.
You then need to read the whole image 'number_of_passes' times.  Each time
will distribute the pixels from the current pass to the correct place in
the output image, so you need to supply the same rows to png_read_rows in
each pass.

If you are not going to display the image after each pass, but are
going to wait until the entire image is read in, use the sparkle
effect.  This effect is faster and the end result of either method
is exactly the same.  If you are planning on displaying the image
after each pass, the "rectangle" effect is generally considered the
better looking one.

If you only want the "sparkle" effect, just call png_read_rows() as
normal, with the third parameter NULL.  Make sure you make pass over
the image number_of_passes times, and you don't change the data in the
rows between calls.  You can change the locations of the data, just
not the data.  Each pass only writes the pixels appropriate for that
pass, and assumes the data from previous passes is still valid.

    png_read_rows(png_ptr, row_pointers, NULL,
        number_of_rows);

If you only want the first effect (the rectangles), do the same as
before except pass the row buffer in the third parameter, and leave
the second parameter NULL.

    png_read_rows(png_ptr, NULL, row_pointers,
        number_of_rows);

If you don't want libpng to handle the interlacing details, just call
png_read_rows() PNG_INTERLACE_ADAM7_PASSES times to read in all the images.
Each of the images is a valid image by itself; however, you will almost
certainly need to distribute the pixels from each sub-image to the
correct place.  This is where everything gets very tricky.

If you want to retrieve the separate images you must pass the correct
number of rows to each successive call of png_read_rows().  The calculation
gets pretty complicated for small images, where some sub-images may
not even exist because either their width or height ends up zero.
libpng provides two macros to help you in 1.5 and later versions:

   png_uint_32 width = PNG_PASS_COLS(image_width, pass_number);
   png_uint_32 height = PNG_PASS_ROWS(image_height, pass_number);

Respectively these tell you the width and height of the sub-image
corresponding to the numbered pass.  'pass' is in in the range 0 to 6 -
this can be confusing because the specification refers to the same passes
as 1 to 7!  Be careful, you must check both the width and height before
calling png_read_rows() and not call it for that pass if either is zero.

You can, of course, read each sub-image row by row.  If you want to
produce optimal code to make a pixel-by-pixel transformation of an
interlaced image this is the best approach; read each row of each pass,
transform it, and write it out to a new interlaced image.

If you want to de-interlace the image yourself libpng provides further
macros to help that tell you where to place the pixels in the output image.
Because the interlacing scheme is rectangular - sub-image pixels are always
arranged on a rectangular grid - all you need to know for each pass is the
starting column and row in the output image of the first pixel plus the
spacing between each pixel.  As of libpng 1.5 there are four macros to
retrieve this information:

   png_uint_32 x = PNG_PASS_START_COL(pass);
   png_uint_32 y = PNG_PASS_START_ROW(pass);
   png_uint_32 xStep = 1U << PNG_PASS_COL_SHIFT(pass);
   png_uint_32 yStep = 1U << PNG_PASS_ROW_SHIFT(pass);

These allow you to write the obvious loop:

   png_uint_32 input_y = 0;
   png_uint_32 output_y = PNG_PASS_START_ROW(pass);

   while (output_y < output_image_height)
   {
      png_uint_32 input_x = 0;
      png_uint_32 output_x = PNG_PASS_START_COL(pass);

      while (output_x < output_image_width)
      {
         image[output_y][output_x] =
             subimage[pass][input_y][input_x++];

         output_x += xStep;
      }

      ++input_y;
      output_y += yStep;
   }

Notice that the steps between successive output rows and columns are
returned as shifts.  This is possible because the pixels in the subimages
are always a power of 2 apart - 1, 2, 4 or 8 pixels - in the original
image.  In practice you may need to directly calculate the output coordinate
given an input coordinate.  libpng provides two further macros for this
purpose:

   png_uint_32 output_x = PNG_COL_FROM_PASS_COL(input_x, pass);
   png_uint_32 output_y = PNG_ROW_FROM_PASS_ROW(input_y, pass);

Finally a pair of macros are provided to tell you if a particular image
row or column appears in a given pass:

   int col_in_pass = PNG_COL_IN_INTERLACE_PASS(output_x, pass);
   int row_in_pass = PNG_ROW_IN_INTERLACE_PASS(output_y, pass);

Bear in mind that you will probably also need to check the width and height
of the pass in addition to the above to be sure the pass even exists!

With any luck you are convinced by now that you don't want to do your own
interlace handling.  In reality normally the only good reason for doing this
is if you are processing PNG files on a pixel-by-pixel basis and don't want
to load the whole file into memory when it is interlaced.

libpng includes a test program, pngvalid, that illustrates reading and
writing of interlaced images.  If you can't get interlacing to work in your
code and don't want to leave it to libpng (the recommended approach), see
how pngvalid.c does it.

Finishing a sequential read

After you are finished reading the image through the
low-level interface, you can finish reading the file.

If you want to use a different crc action for handling CRC errors in
chunks after the image data, you can call png_set_crc_action()
again at this point.

If you are interested in comments or time, which may be stored either
before or after the image data, you should pass the separate png_info
struct if you want to keep the comments from before and after the image
separate.

    png_infop end_info = png_create_info_struct(png_ptr);

    if (!end_info)
    {
       png_destroy_read_struct(&png_ptr, &info_ptr,
           (png_infopp)NULL);
       return (ERROR);
    }

   png_read_end(png_ptr, end_info);

If you are not interested, you should still call png_read_end()
but you can pass NULL, avoiding the need to create an end_info structure.
If you do this, libpng will not process any chunks after IDAT other than
skipping over them and perhaps (depending on whether you have called
png_set_crc_action) checking their CRCs while looking for the IEND chunk.

   png_read_end(png_ptr, (png_infop)NULL);

If you don't call png_read_end(), then your file pointer will be
left pointing to the first chunk after the last IDAT, which is probably
not what you want if you expect to read something beyond the end of
the PNG datastream.

When you are done, you can free all memory allocated by libpng like this:

   png_destroy_read_struct(&png_ptr, &info_ptr,
       &end_info);

or, if you didn't create an end_info structure,

   png_destroy_read_struct(&png_ptr, &info_ptr,
       (png_infopp)NULL);

It is also possible to individually free the info_ptr members that
point to libpng-allocated storage with the following function:

    png_free_data(png_ptr, info_ptr, mask, seq)

    mask - identifies data to be freed, a mask
           containing the bitwise OR of one or
           more of
             PNG_FREE_PLTE, PNG_FREE_TRNS,
             PNG_FREE_HIST, PNG_FREE_ICCP,
             PNG_FREE_PCAL, PNG_FREE_ROWS,
             PNG_FREE_SCAL, PNG_FREE_SPLT,
             PNG_FREE_TEXT, PNG_FREE_UNKN,
           or simply PNG_FREE_ALL

    seq  - sequence number of item to be freed
           (-1 for all items)

This function may be safely called when the relevant storage has
already been freed, or has not yet been allocated, or was allocated
by the user and not by libpng,  and will in those cases do nothing.
The "seq" parameter is ignored if only one item of the selected data
type, such as PLTE, is allowed.  If "seq" is not -1, and multiple items
are allowed for the data type identified in the mask, such as text or
sPLT, only the n'th item in the structure is freed, where n is "seq".

The default behavior is only to free data that was allocated internally
by libpng.  This can be changed, so that libpng will not free the data,
or so that it will free data that was allocated by the user with png_malloc()
or png_calloc() and passed in via a png_set_*() function, with

    png_data_freer(png_ptr, info_ptr, freer, mask)

    freer  - one of
               PNG_DESTROY_WILL_FREE_DATA
               PNG_SET_WILL_FREE_DATA
               PNG_USER_WILL_FREE_DATA

    mask   - which data elements are affected
             same choices as in png_free_data()

This function only affects data that has already been allocated.
You can call this function after reading the PNG data but before calling
any png_set_*() functions, to control whether the user or the png_set_*()
function is responsible for freeing any existing data that might be present,
and again after the png_set_*() functions to control whether the user
or png_destroy_*() is supposed to free the data.  When the user assumes
responsibility for libpng-allocated data, the application must use
png_free() to free it, and when the user transfers responsibility to libpng
for data that the user has allocated, the user must have used png_malloc()
or png_calloc() to allocate it.

If you allocated your row_pointers in a single block, as suggested above in
the description of the high level read interface, you must not transfer
responsibility for freeing it to the png_set_rows or png_read_destroy function,
because they would also try to free the individual row_pointers[i].

If you allocated text_ptr.text, text_ptr.lang, and text_ptr.translated_keyword
separately, do not transfer responsibility for freeing text_ptr to libpng,
because when libpng fills a png_text structure it combines these members with
the key member, and png_free_data() will free only text_ptr.key.  Similarly,
if you transfer responsibility for free'ing text_ptr from libpng to your
application, your application must not separately free those members.

The png_free_data() function will turn off the "valid" flag for anything
it frees.  If you need to turn the flag off for a chunk that was freed by
your application instead of by libpng, you can use

    png_set_invalid(png_ptr, info_ptr, mask);

    mask - identifies the chunks to be made invalid,
           containing the bitwise OR of one or
           more of
             PNG_INFO_gAMA, PNG_INFO_sBIT,
             PNG_INFO_cHRM, PNG_INFO_PLTE,
             PNG_INFO_tRNS, PNG_INFO_bKGD,
             PNG_INFO_hIST, PNG_INFO_pHYs,
             PNG_INFO_oFFs, PNG_INFO_tIME,
             PNG_INFO_pCAL, PNG_INFO_sRGB,
             PNG_INFO_iCCP, PNG_INFO_sPLT,
             PNG_INFO_sCAL, PNG_INFO_IDAT

For a more compact example of reading a PNG image, see the file example.c.

Reading PNG files progressively

The progressive reader is slightly different from the non-progressive
reader.  Instead of calling png_read_info(), png_read_rows(), and
png_read_end(), you make one call to png_process_data(), which calls
callbacks when it has the info, a row, or the end of the image.  You
set up these callbacks with png_set_progressive_read_fn().  You don't
have to worry about the input/output functions of libpng, as you are
giving the library the data directly in png_process_data().  I will
assume that you have read the section on reading PNG files above,
so I will only highlight the differences (although I will show
all of the code).

png_structp png_ptr;
png_infop info_ptr;

 /*  An example code fragment of how you would
     initialize the progressive reader in your
     application. */
 int
 initialize_png_reader()
 {
    png_ptr = png_create_read_struct
        (PNG_LIBPNG_VER_STRING, (png_voidp)user_error_ptr,
         user_error_fn, user_warning_fn);

    if (!png_ptr)
        return (ERROR);

    info_ptr = png_create_info_struct(png_ptr);

    if (!info_ptr)
    {
       png_destroy_read_struct(&png_ptr,
          (png_infopp)NULL, (png_infopp)NULL);
       return (ERROR);
    }

    if (setjmp(png_jmpbuf(png_ptr)))
    {
       png_destroy_read_struct(&png_ptr, &info_ptr,
          (png_infopp)NULL);
       return (ERROR);
    }

    /* This one's new.  You can provide functions
       to be called when the header info is valid,
       when each row is completed, and when the image
       is finished.  If you aren't using all functions,
       you can specify NULL parameters.  Even when all
       three functions are NULL, you need to call
       png_set_progressive_read_fn().  You can use
       any struct as the user_ptr (cast to a void pointer
       for the function call), and retrieve the pointer
       from inside the callbacks using the function

          png_get_progressive_ptr(png_ptr);

       which will return a void pointer, which you have
       to cast appropriately.
     */
    png_set_progressive_read_fn(png_ptr, (void *)user_ptr,
        info_callback, row_callback, end_callback);

    return 0;
 }

 /* A code fragment that you call as you receive blocks
   of data */
 int
 process_data(png_bytep buffer, png_uint_32 length)
 {
    if (setjmp(png_jmpbuf(png_ptr)))
    {
       png_destroy_read_struct(&png_ptr, &info_ptr,
           (png_infopp)NULL);
       return (ERROR);
    }

    /* This one's new also.  Simply give it a chunk
       of data from the file stream (in order, of
       course).  On machines with segmented memory
       models machines, don't give it any more than
       64K.  The library seems to run fine with sizes
       of 4K. Although you can give it much less if
       necessary (I assume you can give it chunks of
       1 byte, I haven't tried less than 256 bytes
       yet).  When this function returns, you may
       want to display any rows that were generated
       in the row callback if you don't already do
       so there.
     */
    png_process_data(png_ptr, info_ptr, buffer, length);

    /* At this point you can call png_process_data_skip if
       you want to handle data the library will skip yourself;
       it simply returns the number of bytes to skip (and stops
       libpng skipping that number of bytes on the next
       png_process_data call).
    return 0;
 }

 /* This function is called (as set by
    png_set_progressive_read_fn() above) when enough data
    has been supplied so all of the header has been
    read.
 */
 void
 info_callback(png_structp png_ptr, png_infop info)
 {
    /* Do any setup here, including setting any of
       the transformations mentioned in the Reading
       PNG files section.  For now, you _must_ call
       either png_start_read_image() or
       png_read_update_info() after all the
       transformations are set (even if you don't set
       any).  You may start getting rows before
       png_process_data() returns, so this is your
       last chance to prepare for that.

       This is where you turn on interlace handling,
       assuming you don't want to do it yourself.

       If you need to you can stop the processing of
       your original input data at this point by calling
       png_process_data_pause.  This returns the number
       of unprocessed bytes from the last png_process_data
       call - it is up to you to ensure that the next call
       sees these bytes again.  If you don't want to bother
       with this you can get libpng to cache the unread
       bytes by setting the 'save' parameter (see png.h) but
       then libpng will have to copy the data internally.
     */
 }

 /* This function is called when each row of image
    data is complete */
 void
 row_callback(png_structp png_ptr, png_bytep new_row,
    png_uint_32 row_num, int pass)
 {
    /* If the image is interlaced, and you turned
       on the interlace handler, this function will
       be called for every row in every pass.  Some
       of these rows will not be changed from the
       previous pass.  When the row is not changed,
       the new_row variable will be NULL.  The rows
       and passes are called in order, so you don't
       really need the row_num and pass, but I'm
       supplying them because it may make your life
       easier.

       If you did not turn on interlace handling then
       the callback is called for each row of each
       sub-image when the image is interlaced.  In this
       case 'row_num' is the row in the sub-image, not
       the row in the output image as it is in all other
       cases.

       For the non-NULL rows of interlaced images when
       you have switched on libpng interlace handling,
       you must call png_progressive_combine_row()
       passing in the row and the old row.  You can
       call this function for NULL rows (it will just
       return) and for non-interlaced images (it just
       does the memcpy for you) if it will make the
       code easier.  Thus, you can just do this for
       all cases if you switch on interlace handling;
     */

        png_progressive_combine_row(png_ptr, old_row,
          new_row);

    /* where old_row is what was displayed
       previously for the row.  Note that the first
       pass (pass == 0, really) will completely cover
       the old row, so the rows do not have to be
       initialized.  After the first pass (and only
       for interlaced images), you will have to pass
       the current row, and the function will combine
       the old row and the new row.

       You can also call png_process_data_pause in this
       callback - see above.
    */
 }

 void
 end_callback(png_structp png_ptr, png_infop info)
 {
    /* This function is called after the whole image
       has been read, including any chunks after the
       image (up to and including the IEND).  You
       will usually have the same info chunk as you
       had in the header, although some data may have
       been added to the comments and time fields.

       Most people won't do much here, perhaps setting
       a flag that marks the image as finished.
     */
 }



IV. Writing

Much of this is very similar to reading.  However, everything of
importance is repeated here, so you won't have to constantly look
back up in the reading section to understand writing.

Setup

You will want to do the I/O initialization before you get into libpng,
so if it doesn't work, you don't have anything to undo. If you are not
using the standard I/O functions, you will need to replace them with
custom writing functions.  See the discussion under Customizing libpng.

    FILE *fp = fopen(file_name, "wb");

    if (!fp)
       return (ERROR);

Next, png_struct and png_info need to be allocated and initialized.
As these can be both relatively large, you may not want to store these
on the stack, unless you have stack space to spare.  Of course, you
will want to check if they return NULL.  If you are also reading,
you won't want to name your read structure and your write structure
both "png_ptr"; you can call them anything you like, such as
"read_ptr" and "write_ptr".  Look at pngtest.c, for example.

    png_structp png_ptr = png_create_write_struct
       (PNG_LIBPNG_VER_STRING, (png_voidp)user_error_ptr,
        user_error_fn, user_warning_fn);

    if (!png_ptr)
       return (ERROR);

    png_infop info_ptr = png_create_info_struct(png_ptr);
    if (!info_ptr)
    {
       png_destroy_write_struct(&png_ptr,
           (png_infopp)NULL);
       return (ERROR);
    }

If you want to use your own memory allocation routines,
define PNG_USER_MEM_SUPPORTED and use
png_create_write_struct_2() instead of png_create_write_struct():

    png_structp png_ptr = png_create_write_struct_2
       (PNG_LIBPNG_VER_STRING, (png_voidp)user_error_ptr,
        user_error_fn, user_warning_fn, (png_voidp)
        user_mem_ptr, user_malloc_fn, user_free_fn);

After you have these structures, you will need to set up the
error handling.  When libpng encounters an error, it expects to
longjmp() back to your routine.  Therefore, you will need to call
setjmp() and pass the png_jmpbuf(png_ptr).  If you
write the file from different routines, you will need to update
the png_jmpbuf(png_ptr) every time you enter a new routine that will
call a png_*() function.  See your documentation of setjmp/longjmp
for your compiler for more information on setjmp/longjmp.  See
the discussion on libpng error handling in the Customizing Libpng
section below for more information on the libpng error handling.

    if (setjmp(png_jmpbuf(png_ptr)))
    {
    png_destroy_write_struct(&png_ptr, &info_ptr);
       fclose(fp);
       return (ERROR);
    }
    ...
    return;

If you would rather avoid the complexity of setjmp/longjmp issues,
you can compile libpng with PNG_NO_SETJMP, in which case
errors will result in a call to PNG_ABORT() which defaults to abort().

You can #define PNG_ABORT() to a function that does something
more useful than abort(), as long as your function does not
return.

Checking for invalid palette index on write was added at libpng
1.5.10.  If a pixel contains an invalid (out-of-range) index libpng issues
a benign error.  This is enabled by default because this condition is an
error according to the PNG specification, Clause 11.3.2, but the error can
be ignored in each png_ptr with

   png_set_check_for_invalid_index(png_ptr, 0);

If the error is ignored, or if png_benign_error() treats it as a warning,
any invalid pixels are written as-is by the encoder, resulting in an
invalid PNG datastream as output.  In this case the application is
responsible for ensuring that the pixel indexes are in range when it writes
a PLTE chunk with fewer entries than the bit depth would allow.

Now you need to set up the output code.  The default for libpng is to
use the C function fwrite().  If you use this, you will need to pass a
valid FILE * in the function png_init_io().  Be sure that the file is
opened in binary mode.  Again, if you wish to handle writing data in
another way, see the discussion on libpng I/O handling in the Customizing
Libpng section below.

    png_init_io(png_ptr, fp);

If you are embedding your PNG into a datastream such as MNG, and don't
want libpng to write the 8-byte signature, or if you have already
written the signature in your application, use

    png_set_sig_bytes(png_ptr, 8);

to inform libpng that it should not write a signature.

Write callbacks

At this point, you can set up a callback function that will be
called after each row has been written, which you can use to control
a progress meter or the like.  It's demonstrated in pngtest.c.
You must supply a function

    void write_row_callback(png_structp png_ptr, png_uint_32 row,
       int pass);
    {
      /* put your code here */
    }

(You can give it another name that you like instead of "write_row_callback")

To inform libpng about your function, use

    png_set_write_status_fn(png_ptr, write_row_callback);

When this function is called the row has already been completely processed and
it has also been written out.  The 'row' and 'pass' refer to the next row to be
handled.  For the
non-interlaced case the row that was just handled is simply one less than the
passed in row number, and pass will always be 0.  For the interlaced case the
same applies unless the row value is 0, in which case the row just handled was
the last one from one of the preceding passes.  Because interlacing may skip a
pass you cannot be sure that the preceding pass is just 'pass-1', if you really
need to know what the last pass is record (row,pass) from the callback and use
the last recorded value each time.

As with the user transform you can find the output row using the
PNG_ROW_FROM_PASS_ROW macro.

You now have the option of modifying how the compression library will
run.  The following functions are mainly for testing, but may be useful
in some cases, like if you need to write PNG files extremely fast and
are willing to give up some compression, or if you want to get the
maximum possible compression at the expense of slower writing.  If you
have no special needs in this area, let the library do what it wants by
not calling this function at all, as it has been tuned to deliver a good
speed/compression ratio. The second parameter to png_set_filter() is
the filter method, for which the only valid values are 0 (as of the
July 1999 PNG specification, version 1.2) or 64 (if you are writing
a PNG datastream that is to be embedded in a MNG datastream).  The third
parameter is a flag that indicates which filter type(s) are to be tested
for each scanline.  See the PNG specification for details on the specific
filter types.


    /* turn on or off filtering, and/or choose
       specific filters.  You can use either a single
       PNG_FILTER_VALUE_NAME or the bitwise OR of one
       or more PNG_FILTER_NAME masks.
     */
    png_set_filter(png_ptr, 0,
       PNG_FILTER_NONE  | PNG_FILTER_VALUE_NONE |
       PNG_FILTER_SUB   | PNG_FILTER_VALUE_SUB  |
       PNG_FILTER_UP    | PNG_FILTER_VALUE_UP   |
       PNG_FILTER_AVG   | PNG_FILTER_VALUE_AVG  |
       PNG_FILTER_PAETH | PNG_FILTER_VALUE_PAETH|
       PNG_ALL_FILTERS);

If an application wants to start and stop using particular filters during
compression, it should start out with all of the filters (to ensure that
the previous row of pixels will be stored in case it's needed later),
and then add and remove them after the start of compression.

If you are writing a PNG datastream that is to be embedded in a MNG
datastream, the second parameter can be either 0 or 64.

The png_set_compression_*() functions interface to the zlib compression
library, and should mostly be ignored unless you really know what you are
doing.  The only generally useful call is png_set_compression_level()
which changes how much time zlib spends on trying to compress the image
data.  See the Compression Library (zlib.h and algorithm.txt, distributed
with zlib) for details on the compression levels.

    #include zlib.h

    /* Set the zlib compression level */
    png_set_compression_level(png_ptr,
        Z_BEST_COMPRESSION);

    /* Set other zlib parameters for compressing IDAT */
    png_set_compression_mem_level(png_ptr, 8);
    png_set_compression_strategy(png_ptr,
        Z_DEFAULT_STRATEGY);
    png_set_compression_window_bits(png_ptr, 15);
    png_set_compression_method(png_ptr, 8);
    png_set_compression_buffer_size(png_ptr, 8192)

    /* Set zlib parameters for text compression
     * If you don't call these, the parameters
     * fall back on those defined for IDAT chunks
     */
    png_set_text_compression_mem_level(png_ptr, 8);
    png_set_text_compression_strategy(png_ptr,
        Z_DEFAULT_STRATEGY);
    png_set_text_compression_window_bits(png_ptr, 15);
    png_set_text_compression_method(png_ptr, 8);

Setting the contents of info for output

You now need to fill in the png_info structure with all the data you
wish to write before the actual image.  Note that the only thing you
are allowed to write after the image is the text chunks and the time
chunk (as of PNG Specification 1.2, anyway).  See png_write_end() and
the latest PNG specification for more information on that.  If you
wish to write them before the image, fill them in now, and flag that
data as being valid.  If you want to wait until after the data, don't
fill them until png_write_end().  For all the fields in png_info and
their data types, see png.h.  For explanations of what the fields
contain, see the PNG specification.

Some of the more important parts of the png_info are:

    png_set_IHDR(png_ptr, info_ptr, width, height,
       bit_depth, color_type, interlace_type,
       compression_type, filter_method)

    width          - holds the width of the image
                     in pixels (up to 2^31).

    height         - holds the height of the image
                     in pixels (up to 2^31).

    bit_depth      - holds the bit depth of one of the
                     image channels.
                     (valid values are 1, 2, 4, 8, 16
                     and depend also on the
                     color_type.  See also significant
                     bits (sBIT) below).

    color_type     - describes which color/alpha
                     channels are present.
                     PNG_COLOR_TYPE_GRAY
                        (bit depths 1, 2, 4, 8, 16)
                     PNG_COLOR_TYPE_GRAY_ALPHA
                        (bit depths 8, 16)
                     PNG_COLOR_TYPE_PALETTE
                        (bit depths 1, 2, 4, 8)
                     PNG_COLOR_TYPE_RGB
                        (bit_depths 8, 16)
                     PNG_COLOR_TYPE_RGB_ALPHA
                        (bit_depths 8, 16)

                     PNG_COLOR_MASK_PALETTE
                     PNG_COLOR_MASK_COLOR
                     PNG_COLOR_MASK_ALPHA

    interlace_type - PNG_INTERLACE_NONE or
                     PNG_INTERLACE_ADAM7

    compression_type - (must be
                     PNG_COMPRESSION_TYPE_DEFAULT)

    filter_method  - (must be PNG_FILTER_TYPE_DEFAULT
                     or, if you are writing a PNG to
                     be embedded in a MNG datastream,
                     can also be
                     PNG_INTRAPIXEL_DIFFERENCING)

If you call png_set_IHDR(), the call must appear before any of the
other png_set_*() functions, because they might require access to some of
the IHDR settings.  The remaining png_set_*() functions can be called
in any order.

If you wish, you can reset the compression_type, interlace_type, or
filter_method later by calling png_set_IHDR() again; if you do this, the
width, height, bit_depth, and color_type must be the same in each call.

    png_set_PLTE(png_ptr, info_ptr, palette,
       num_palette);

    palette        - the palette for the file
                     (array of png_color)
    num_palette    - number of entries in the palette

    png_set_gAMA(png_ptr, info_ptr, file_gamma);
    png_set_gAMA_fixed(png_ptr, info_ptr, int_file_gamma);

    file_gamma     - the gamma at which the image was
                     created (PNG_INFO_gAMA)

    int_file_gamma - 100,000 times the gamma at which
                     the image was created

    png_set_cHRM(png_ptr, info_ptr,  white_x, white_y, red_x, red_y,
                     green_x, green_y, blue_x, blue_y)
    png_set_cHRM_XYZ(png_ptr, info_ptr, red_X, red_Y, red_Z, green_X,
                     green_Y, green_Z, blue_X, blue_Y, blue_Z)
    png_set_cHRM_fixed(png_ptr, info_ptr, int_white_x, int_white_y,
                     int_red_x, int_red_y, int_green_x, int_green_y,
                     int_blue_x, int_blue_y)
    png_set_cHRM_XYZ_fixed(png_ptr, info_ptr, int_red_X, int_red_Y,
                     int_red_Z, int_green_X, int_green_Y, int_green_Z,
                     int_blue_X, int_blue_Y, int_blue_Z)

    {white,red,green,blue}_{x,y}
                     A color space encoding specified using the chromaticities
                     of the end points and the white point.

    {red,green,blue}_{X,Y,Z}
                     A color space encoding specified using the encoding end
                     points - the CIE tristimulus specification of the intended
                     color of the red, green and blue channels in the PNG RGB
                     data.  The white point is simply the sum of the three end
                     points.

    png_set_sRGB(png_ptr, info_ptr, srgb_intent);

    srgb_intent    - the rendering intent
                     (PNG_INFO_sRGB) The presence of
                     the sRGB chunk means that the pixel
                     data is in the sRGB color space.
                     This chunk also implies specific
                     values of gAMA and cHRM.  Rendering
                     intent is the CSS-1 property that
                     has been defined by the International
                     Color Consortium
                     (http://www.color.org).
                     It can be one of
                     PNG_sRGB_INTENT_SATURATION,
                     PNG_sRGB_INTENT_PERCEPTUAL,
                     PNG_sRGB_INTENT_ABSOLUTE, or
                     PNG_sRGB_INTENT_RELATIVE.


    png_set_sRGB_gAMA_and_cHRM(png_ptr, info_ptr,
       srgb_intent);

    srgb_intent    - the rendering intent
                     (PNG_INFO_sRGB) The presence of the
                     sRGB chunk means that the pixel
                     data is in the sRGB color space.
                     This function also causes gAMA and
                     cHRM chunks with the specific values
                     that are consistent with sRGB to be
                     written.

    png_set_iCCP(png_ptr, info_ptr, name, compression_type,
                       profile, proflen);

    name             - The profile name.

    compression_type - The compression type; always
                       PNG_COMPRESSION_TYPE_BASE for PNG 1.0.
                       You may give NULL to this argument to
                       ignore it.

    profile          - International Color Consortium color
                       profile data. May contain NULs.

    proflen          - length of profile data in bytes.

    png_set_sBIT(png_ptr, info_ptr, sig_bit);

    sig_bit        - the number of significant bits for
                     (PNG_INFO_sBIT) each of the gray, red,
                     green, and blue channels, whichever are
                     appropriate for the given color type
                     (png_color_16)

    png_set_tRNS(png_ptr, info_ptr, trans_alpha,
       num_trans, trans_color);

    trans_alpha    - array of alpha (transparency)
                     entries for palette (PNG_INFO_tRNS)

    num_trans      - number of transparent entries
                     (PNG_INFO_tRNS)

    trans_color    - graylevel or color sample values
                     (in order red, green, blue) of the
                     single transparent color for
                     non-paletted images (PNG_INFO_tRNS)

    png_set_hIST(png_ptr, info_ptr, hist);

    hist           - histogram of palette (array of
                     png_uint_16) (PNG_INFO_hIST)

    png_set_tIME(png_ptr, info_ptr, mod_time);

    mod_time       - time image was last modified
                     (PNG_VALID_tIME)

    png_set_bKGD(png_ptr, info_ptr, background);

    background     - background color (of type
                     png_color_16p) (PNG_VALID_bKGD)

    png_set_text(png_ptr, info_ptr, text_ptr, num_text);

    text_ptr       - array of png_text holding image
                     comments

    text_ptr[i].compression - type of compression used
                 on "text" PNG_TEXT_COMPRESSION_NONE
                           PNG_TEXT_COMPRESSION_zTXt
                           PNG_ITXT_COMPRESSION_NONE
                           PNG_ITXT_COMPRESSION_zTXt
    text_ptr[i].key   - keyword for comment.  Must contain
                 1-79 characters.
    text_ptr[i].text  - text comments for current
                         keyword.  Can be NULL or empty.
    text_ptr[i].text_length - length of text string,
                 after decompression, 0 for iTXt
    text_ptr[i].itxt_length - length of itxt string,
                 after decompression, 0 for tEXt/zTXt
    text_ptr[i].lang  - language of comment (NULL or
                         empty for unknown).
    text_ptr[i].translated_keyword  - keyword in UTF-8 (NULL
                         or empty for unknown).

    Note that the itxt_length, lang, and lang_key
    members of the text_ptr structure only exist when the
    library is built with iTXt chunk support.  Prior to
    libpng-1.4.0 the library was built by default without
    iTXt support. Also note that when iTXt is supported,
    they contain NULL pointers when the "compression"
    field contains PNG_TEXT_COMPRESSION_NONE or
    PNG_TEXT_COMPRESSION_zTXt.

    num_text       - number of comments

    png_set_sPLT(png_ptr, info_ptr, &palette_ptr,
       num_spalettes);

    palette_ptr    - array of png_sPLT_struct structures
                     to be added to the list of palettes
                     in the info structure.
    num_spalettes  - number of palette structures to be
                     added.

    png_set_oFFs(png_ptr, info_ptr, offset_x, offset_y,
        unit_type);

    offset_x  - positive offset from the left
                     edge of the screen

    offset_y  - positive offset from the top
                     edge of the screen

    unit_type - PNG_OFFSET_PIXEL, PNG_OFFSET_MICROMETER

    png_set_pHYs(png_ptr, info_ptr, res_x, res_y,
        unit_type);

    res_x       - pixels/unit physical resolution
                  in x direction

    res_y       - pixels/unit physical resolution
                  in y direction

    unit_type   - PNG_RESOLUTION_UNKNOWN,
                  PNG_RESOLUTION_METER

    png_set_sCAL(png_ptr, info_ptr, unit, width, height)

    unit        - physical scale units (an integer)

    width       - width of a pixel in physical scale units

    height      - height of a pixel in physical scale units
                  (width and height are doubles)

    png_set_sCAL_s(png_ptr, info_ptr, unit, width, height)

    unit        - physical scale units (an integer)

    width       - width of a pixel in physical scale units
                  expressed as a string

    height      - height of a pixel in physical scale units
                 (width and height are strings like "2.54")

    png_set_unknown_chunks(png_ptr, info_ptr, &unknowns,
       num_unknowns)

    unknowns          - array of png_unknown_chunk
                        structures holding unknown chunks
    unknowns[i].name  - name of unknown chunk
    unknowns[i].data  - data of unknown chunk
    unknowns[i].size  - size of unknown chunk's data
    unknowns[i].location - position to write chunk in file
                           0: do not write chunk
                           PNG_HAVE_IHDR: before PLTE
                           PNG_HAVE_PLTE: before IDAT
                           PNG_AFTER_IDAT: after IDAT

The "location" member is set automatically according to
what part of the output file has already been written.
You can change its value after calling png_set_unknown_chunks()
as demonstrated in pngtest.c.  Within each of the "locations",
the chunks are sequenced according to their position in the
structure (that is, the value of "i", which is the order in which
the chunk was either read from the input file or defined with
png_set_unknown_chunks).

A quick word about text and num_text.  text is an array of png_text
structures.  num_text is the number of valid structures in the array.
Each png_text structure holds a language code, a keyword, a text value,
and a compression type.

The compression types have the same valid numbers as the compression
types of the image data.  Currently, the only valid number is zero.
However, you can store text either compressed or uncompressed, unlike
images, which always have to be compressed.  So if you don't want the
text compressed, set the compression type to PNG_TEXT_COMPRESSION_NONE.
Because tEXt and zTXt chunks don't have a language field, if you
specify PNG_TEXT_COMPRESSION_NONE or PNG_TEXT_COMPRESSION_zTXt
any language code or translated keyword will not be written out.

Until text gets around a few hundred bytes, it is not worth compressing it.
After the text has been written out to the file, the compression type
is set to PNG_TEXT_COMPRESSION_NONE_WR or PNG_TEXT_COMPRESSION_zTXt_WR,
so that it isn't written out again at the end (in case you are calling
png_write_end() with the same struct).

The keywords that are given in the PNG Specification are:

    Title            Short (one line) title or
                     caption for image

    Author           Name of image's creator

    Description      Description of image (possibly long)

    Copyright        Copyright notice

    Creation Time    Time of original image creation
                     (usually RFC 1123 format, see below)

    Software         Software used to create the image

    Disclaimer       Legal disclaimer

    Warning          Warning of nature of content

    Source           Device used to create the image

    Comment          Miscellaneous comment; conversion
                     from other image format

The keyword-text pairs work like this.  Keywords should be short
simple descriptions of what the comment is about.  Some typical
keywords are found in the PNG specification, as is some recommendations
on keywords.  You can repeat keywords in a file.  You can even write
some text before the image and some after.  For example, you may want
to put a description of the image before the image, but leave the
disclaimer until after, so viewers working over modem connections
don't have to wait for the disclaimer to go over the modem before
they start seeing the image.  Finally, keywords should be full
words, not abbreviations.  Keywords and text are in the ISO 8859-1
(Latin-1) character set (a superset of regular ASCII) and can not
contain NUL characters, and should not contain control or other
unprintable characters.  To make the comments widely readable, stick
with basic ASCII, and avoid machine specific character set extensions
like the IBM-PC character set.  The keyword must be present, but
you can leave off the text string on non-compressed pairs.
Compressed pairs must have a text string, as only the text string
is compressed anyway, so the compression would be meaningless.

PNG supports modification time via the png_time structure.  Two
conversion routines are provided, png_convert_from_time_t() for
time_t and png_convert_from_struct_tm() for struct tm.  The
time_t routine uses gmtime().  You don't have to use either of
these, but if you wish to fill in the png_time structure directly,
you should provide the time in universal time (GMT) if possible
instead of your local time.  Note that the year number is the full
year (e.g. 1998, rather than 98 - PNG is year 2000 compliant!), and
that months start with 1.

If you want to store the time of the original image creation, you should
use a plain tEXt chunk with the "Creation Time" keyword.  This is
necessary because the "creation time" of a PNG image is somewhat vague,
depending on whether you mean the PNG file, the time the image was
created in a non-PNG format, a still photo from which the image was
scanned, or possibly the subject matter itself.  In order to facilitate
machine-readable dates, it is recommended that the "Creation Time"
tEXt chunk use RFC 1123 format dates (e.g. "22 May 1997 18:07:10 GMT"),
although this isn't a requirement.  Unlike the tIME chunk, the
"Creation Time" tEXt chunk is not expected to be automatically changed
by the software.  To facilitate the use of RFC 1123 dates, a function
png_convert_to_rfc1123_buffer(buffer, png_timep) is provided to
convert from PNG time to an RFC 1123 format string.  The caller must provide
a writeable buffer of at least 29 bytes.

Writing unknown chunks

You can use the png_set_unknown_chunks function to queue up private chunks
for writing.  You give it a chunk name, location, raw data, and a size.  You
also must use png_set_keep_unknown_chunks() to ensure that libpng will
handle them.  That's all there is to it.  The chunks will be written by the
next following png_write_info_before_PLTE, png_write_info, or png_write_end
function, depending upon the specified location.  Any chunks previously
read into the info structure's unknown-chunk list will also be written out
in a sequence that satisfies the PNG specification's ordering rules.

Here is an example of writing two private chunks, prVt and miNE:

    #ifdef PNG_WRITE_UNKNOWN_CHUNKS_SUPPORTED
    /* Set unknown chunk data */
    png_unknown_chunk unk_chunk[2];
    strcpy((char *) unk_chunk[0].name, "prVt";
    unk_chunk[0].data = (unsigned char *) "PRIVATE DATA";
    unk_chunk[0].size = strlen(unk_chunk[0].data)+1;
    unk_chunk[0].location = PNG_HAVE_IHDR;
    strcpy((char *) unk_chunk[1].name, "miNE";
    unk_chunk[1].data = (unsigned char *) "MY CHUNK DATA";
    unk_chunk[1].size = strlen(unk_chunk[0].data)+1;
    unk_chunk[1].location = PNG_AFTER_IDAT;
    png_set_unknown_chunks(write_ptr, write_info_ptr,
        unk_chunk, 2);
    /* Needed because miNE is not safe-to-copy */
    png_set_keep_unknown_chunks(png, PNG_HANDLE_CHUNK_ALWAYS,
       (png_bytep) "miNE", 1);
    # if PNG_LIBPNG_VER < 10600
      /* Deal with unknown chunk location bug in 1.5.x and earlier */
      png_set_unknown_chunk_location(png, info, 0, PNG_HAVE_IHDR);
      png_set_unknown_chunk_location(png, info, 1, PNG_AFTER_IDAT);
    # endif
    # if PNG_LIBPNG_VER < 10500
      /* PNG_AFTER_IDAT writes two copies of the chunk prior to libpng-1.5.0,
       * one before IDAT and another after IDAT, so don't use it; only use
       * PNG_HAVE_IHDR location.  This call resets the location previously
       * set by assignment and png_set_unknown_chunk_location() for chunk 1.
       */
      png_set_unknown_chunk_location(png, info, 1, PNG_HAVE_IHDR);
    # endif
    #endif

The high-level write interface

At this point there are two ways to proceed; through the high-level
write interface, or through a sequence of low-level write operations.
You can use the high-level interface if your image data is present
in the info structure.  All defined output
transformations are permitted, enabled by the following masks.

    PNG_TRANSFORM_IDENTITY      No transformation
    PNG_TRANSFORM_PACKING       Pack 1, 2 and 4-bit samples
    PNG_TRANSFORM_PACKSWAP      Change order of packed
                                pixels to LSB first
    PNG_TRANSFORM_INVERT_MONO   Invert monochrome images
    PNG_TRANSFORM_SHIFT         Normalize pixels to the
                                sBIT depth
    PNG_TRANSFORM_BGR           Flip RGB to BGR, RGBA
                                to BGRA
    PNG_TRANSFORM_SWAP_ALPHA    Flip RGBA to ARGB or GA
                                to AG
    PNG_TRANSFORM_INVERT_ALPHA  Change alpha from opacity
                                to transparency
    PNG_TRANSFORM_SWAP_ENDIAN   Byte-swap 16-bit samples
    PNG_TRANSFORM_STRIP_FILLER        Strip out filler
                                      bytes (deprecated).
    PNG_TRANSFORM_STRIP_FILLER_BEFORE Strip out leading
                                      filler bytes
    PNG_TRANSFORM_STRIP_FILLER_AFTER  Strip out trailing
                                      filler bytes

If you have valid image data in the info structure (you can use
png_set_rows() to put image data in the info structure), simply do this:

    png_write_png(png_ptr, info_ptr, png_transforms, NULL)

where png_transforms is an integer containing the bitwise OR of some set of
transformation flags.  This call is equivalent to png_write_info(),
followed the set of transformations indicated by the transform mask,
then png_write_image(), and finally png_write_end().

(The final parameter of this call is not yet used.  Someday it might point
to transformation parameters required by some future output transform.)

You must use png_transforms and not call any png_set_transform() functions
when you use png_write_png().

The low-level write interface

If you are going the low-level route instead, you are now ready to
write all the file information up to the actual image data.  You do
this with a call to png_write_info().

    png_write_info(png_ptr, info_ptr);

Note that there is one transformation you may need to do before
png_write_info().  In PNG files, the alpha channel in an image is the
level of opacity.  If your data is supplied as a level of transparency,
you can invert the alpha channel before you write it, so that 0 is
fully transparent and 255 (in 8-bit or paletted images) or 65535
(in 16-bit images) is fully opaque, with

    png_set_invert_alpha(png_ptr);

This must appear before png_write_info() instead of later with the
other transformations because in the case of paletted images the tRNS
chunk data has to be inverted before the tRNS chunk is written.  If
your image is not a paletted image, the tRNS data (which in such cases
represents a single color to be rendered as transparent) won't need to
be changed, and you can safely do this transformation after your
png_write_info() call.

If you need to write a private chunk that you want to appear before
the PLTE chunk when PLTE is present, you can write the PNG info in
two steps, and insert code to write your own chunk between them:

    png_write_info_before_PLTE(png_ptr, info_ptr);
    png_set_unknown_chunks(png_ptr, info_ptr, ...);
    png_write_info(png_ptr, info_ptr);

After you've written the file information, you can set up the library
to handle any special transformations of the image data.  The various
ways to transform the data will be described in the order that they
should occur.  This is important, as some of these change the color
type and/or bit depth of the data, and some others only work on
certain color types and bit depths.  Even though each transformation
checks to see if it has data that it can do something with, you should
make sure to only enable a transformation if it will be valid for the
data.  For example, don't swap red and blue on grayscale data.

PNG files store RGB pixels packed into 3 or 6 bytes.  This code tells
the library to strip input data that has 4 or 8 bytes per pixel down
to 3 or 6 bytes (or strip 2 or 4-byte grayscale+filler data to 1 or 2
bytes per pixel).

    png_set_filler(png_ptr, 0, PNG_FILLER_BEFORE);

where the 0 is unused, and the location is either PNG_FILLER_BEFORE or
PNG_FILLER_AFTER, depending upon whether the filler byte in the pixel
is stored XRGB or RGBX.

PNG files pack pixels of bit depths 1, 2, and 4 into bytes as small as
they can, resulting in, for example, 8 pixels per byte for 1 bit files.
If the data is supplied at 1 pixel per byte, use this code, which will
correctly pack the pixels into a single byte:

    png_set_packing(png_ptr);

PNG files reduce possible bit depths to 1, 2, 4, 8, and 16.  If your
data is of another bit depth, you can write an sBIT chunk into the
file so that decoders can recover the original data if desired.

    /* Set the true bit depth of the image data */
    if (color_type & PNG_COLOR_MASK_COLOR)
    {
       sig_bit.red = true_bit_depth;
       sig_bit.green = true_bit_depth;
       sig_bit.blue = true_bit_depth;
    }

    else
    {
       sig_bit.gray = true_bit_depth;
    }

    if (color_type & PNG_COLOR_MASK_ALPHA)
    {
       sig_bit.alpha = true_bit_depth;
    }

    png_set_sBIT(png_ptr, info_ptr, &sig_bit);

If the data is stored in the row buffer in a bit depth other than
one supported by PNG (e.g. 3 bit data in the range 0-7 for a 4-bit PNG),
this will scale the values to appear to be the correct bit depth as
is required by PNG.

    png_set_shift(png_ptr, &sig_bit);

PNG files store 16-bit pixels in network byte order (big-endian,
ie. most significant bits first).  This code would be used if they are
supplied the other way (little-endian, i.e. least significant bits
first, the way PCs store them):

    if (bit_depth > 8)
       png_set_swap(png_ptr);

If you are using packed-pixel images (1, 2, or 4 bits/pixel), and you
need to change the order the pixels are packed into bytes, you can use:

    if (bit_depth < 8)
       png_set_packswap(png_ptr);

PNG files store 3 color pixels in red, green, blue order.  This code
would be used if they are supplied as blue, green, red:

    png_set_bgr(png_ptr);

PNG files describe monochrome as black being zero and white being
one. This code would be used if the pixels are supplied with this reversed
(black being one and white being zero):

    png_set_invert_mono(png_ptr);

Finally, you can write your own transformation function if none of
the existing ones meets your needs.  This is done by setting a callback
with

    png_set_write_user_transform_fn(png_ptr,
       write_transform_fn);

You must supply the function

    void write_transform_fn(png_structp png_ptr, png_row_infop
       row_info, png_bytep data)

See pngtest.c for a working example.  Your function will be called
before any of the other transformations are processed.  If supported
libpng also supplies an information routine that may be called from
your callback:

   png_get_current_row_number(png_ptr);
   png_get_current_pass_number(png_ptr);

This returns the current row passed to the transform.  With interlaced
images the value returned is the row in the input sub-image image.  Use
PNG_ROW_FROM_PASS_ROW(row, pass) and PNG_COL_FROM_PASS_COL(col, pass) to
find the output pixel (x,y) given an interlaced sub-image pixel (row,col,pass).

The discussion of interlace handling above contains more information on how to
use these values.

You can also set up a pointer to a user structure for use by your
callback function.

    png_set_user_transform_info(png_ptr, user_ptr, 0, 0);

The user_channels and user_depth parameters of this function are ignored
when writing; you can set them to zero as shown.

You can retrieve the pointer via the function png_get_user_transform_ptr().
For example:

    voidp write_user_transform_ptr =
       png_get_user_transform_ptr(png_ptr);

It is possible to have libpng flush any pending output, either manually,
or automatically after a certain number of lines have been written.  To
flush the output stream a single time call:

    png_write_flush(png_ptr);

and to have libpng flush the output stream periodically after a certain
number of scanlines have been written, call:

    png_set_flush(png_ptr, nrows);

Note that the distance between rows is from the last time png_write_flush()
was called, or the first row of the image if it has never been called.
So if you write 50 lines, and then png_set_flush 25, it will flush the
output on the next scanline, and every 25 lines thereafter, unless
png_write_flush() is called before 25 more lines have been written.
If nrows is too small (less than about 10 lines for a 640 pixel wide
RGB image) the image compression may decrease noticeably (although this
may be acceptable for real-time applications).  Infrequent flushing will
only degrade the compression performance by a few percent over images
that do not use flushing.

Writing the image data

That's it for the transformations.  Now you can write the image data.
The simplest way to do this is in one function call.  If you have the
whole image in memory, you can just call png_write_image() and libpng
will write the image.  You will need to pass in an array of pointers to
each row.  This function automatically handles interlacing, so you don't
need to call png_set_interlace_handling() or call this function multiple
times, or any of that other stuff necessary with png_write_rows().

    png_write_image(png_ptr, row_pointers);

where row_pointers is:

    png_byte *row_pointers[height];

You can point to void or char or whatever you use for pixels.

If you don't want to write the whole image at once, you can
use png_write_rows() instead.  If the file is not interlaced,
this is simple:

    png_write_rows(png_ptr, row_pointers,
       number_of_rows);

row_pointers is the same as in the png_write_image() call.

If you are just writing one row at a time, you can do this with
a single row_pointer instead of an array of row_pointers:

    png_bytep row_pointer = row;

    png_write_row(png_ptr, row_pointer);

When the file is interlaced, things can get a good deal more complicated.
The only currently (as of the PNG Specification version 1.2, dated July
1999) defined interlacing scheme for PNG files is the "Adam7" interlace
scheme, that breaks down an image into seven smaller images of varying
size.  libpng will build these images for you, or you can do them
yourself.  If you want to build them yourself, see the PNG specification
for details of which pixels to write when.

If you don't want libpng to handle the interlacing details, just
use png_set_interlace_handling() and call png_write_rows() the
correct number of times to write all the sub-images
(png_set_interlace_handling() returns the number of sub-images.)

If you want libpng to build the sub-images, call this before you start
writing any rows:

    number_of_passes = png_set_interlace_handling(png_ptr);

This will return the number of passes needed.  Currently, this is seven,
but may change if another interlace type is added.

Then write the complete image number_of_passes times.

    png_write_rows(png_ptr, row_pointers, number_of_rows);

Think carefully before you write an interlaced image.  Typically code that
reads such images reads all the image data into memory, uncompressed, before
doing any processing.  Only code that can display an image on the fly can
take advantage of the interlacing and even then the image has to be exactly
the correct size for the output device, because scaling an image requires
adjacent pixels and these are not available until all the passes have been
read.

If you do write an interlaced image you will hardly ever need to handle
the interlacing yourself.  Call png_set_interlace_handling() and use the
approach described above.

The only time it is conceivable that you will really need to write an
interlaced image pass-by-pass is when you have read one pass by pass and
made some pixel-by-pixel transformation to it, as described in the read
code above.  In this case use the PNG_PASS_ROWS and PNG_PASS_COLS macros
to determine the size of each sub-image in turn and simply write the rows
you obtained from the read code.

Finishing a sequential write

After you are finished writing the image, you should finish writing
the file.  If you are interested in writing comments or time, you should
pass an appropriately filled png_info pointer.  If you are not interested,
you can pass NULL.

    png_write_end(png_ptr, info_ptr);

When you are done, you can free all memory used by libpng like this:

    png_destroy_write_struct(&png_ptr, &info_ptr);

It is also possible to individually free the info_ptr members that
point to libpng-allocated storage with the following function:

    png_free_data(png_ptr, info_ptr, mask, seq)

    mask  - identifies data to be freed, a mask
            containing the bitwise OR of one or
            more of
              PNG_FREE_PLTE, PNG_FREE_TRNS,
              PNG_FREE_HIST, PNG_FREE_ICCP,
              PNG_FREE_PCAL, PNG_FREE_ROWS,
              PNG_FREE_SCAL, PNG_FREE_SPLT,
              PNG_FREE_TEXT, PNG_FREE_UNKN,
            or simply PNG_FREE_ALL

    seq   - sequence number of item to be freed
            (-1 for all items)

This function may be safely called when the relevant storage has
already been freed, or has not yet been allocated, or was allocated
by the user  and not by libpng,  and will in those cases do nothing.
The "seq" parameter is ignored if only one item of the selected data
type, such as PLTE, is allowed.  If "seq" is not -1, and multiple items
are allowed for the data type identified in the mask, such as text or
sPLT, only the n'th item in the structure is freed, where n is "seq".

If you allocated data such as a palette that you passed in to libpng
with png_set_*, you must not free it until just before the call to
png_destroy_write_struct().

The default behavior is only to free data that was allocated internally
by libpng.  This can be changed, so that libpng will not free the data,
or so that it will free data that was allocated by the user with png_malloc()
or png_calloc() and passed in via a png_set_*() function, with

    png_data_freer(png_ptr, info_ptr, freer, mask)

    freer  - one of
               PNG_DESTROY_WILL_FREE_DATA
               PNG_SET_WILL_FREE_DATA
               PNG_USER_WILL_FREE_DATA

    mask   - which data elements are affected
             same choices as in png_free_data()

For example, to transfer responsibility for some data from a read structure
to a write structure, you could use

    png_data_freer(read_ptr, read_info_ptr,
       PNG_USER_WILL_FREE_DATA,
       PNG_FREE_PLTE|PNG_FREE_tRNS|PNG_FREE_hIST)

    png_data_freer(write_ptr, write_info_ptr,
       PNG_DESTROY_WILL_FREE_DATA,
       PNG_FREE_PLTE|PNG_FREE_tRNS|PNG_FREE_hIST)

thereby briefly reassigning responsibility for freeing to the user but
immediately afterwards reassigning it once more to the write_destroy
function.  Having done this, it would then be safe to destroy the read
structure and continue to use the PLTE, tRNS, and hIST data in the write
structure.

This function only affects data that has already been allocated.
You can call this function before calling after the png_set_*() functions
to control whether the user or png_destroy_*() is supposed to free the data.
When the user assumes responsibility for libpng-allocated data, the
application must use
png_free() to free it, and when the user transfers responsibility to libpng
for data that the user has allocated, the user must have used png_malloc()
or png_calloc() to allocate it.

If you allocated text_ptr.text, text_ptr.lang, and text_ptr.translated_keyword
separately, do not transfer responsibility for freeing text_ptr to libpng,
because when libpng fills a png_text structure it combines these members with
the key member, and png_free_data() will free only text_ptr.key.  Similarly,
if you transfer responsibility for free'ing text_ptr from libpng to your
application, your application must not separately free those members.
For a more compact example of writing a PNG image, see the file example.c.

V. Simplified API

The simplified API, which became available in libpng-1.6.0, hides the details
of both libpng and the PNG file format itself.
It allows PNG files to be read into a very limited number of
in-memory bitmap formats or to be written from the same formats.  If these
formats do not accommodate your needs then you can, and should, use the more
sophisticated APIs above - these support a wide variety of in-memory formats
and a wide variety of sophisticated transformations to those formats as well
as a wide variety of APIs to manipulate ancilliary information.

To read a PNG file using the simplified API:

  1) Declare a 'png_image' structure (see below) on the
     stack and memset() it to all zero.

  2) Call the appropriate png_image_begin_read... function.

  3) Set the png_image 'format' member to the required
     format and allocate a buffer for the image.

  4) Call png_image_finish_read to read the image into
     your buffer.

There are no restrictions on the format of the PNG input itself; all valid
color types, bit depths, and interlace methods are acceptable, and the
input image is transformed as necessary to the requested in-memory format
during the png_image_finish_read() step.

To write a PNG file using the simplified API:

  1) Declare a 'png_image' structure on the stack and memset()
     it to all zero.

  2) Initialize the members of the structure that describe the
     image, setting the 'format' member to the format of the
     image in memory.

  3) Call the appropriate png_image_write... function with a
     pointer to the image to write the PNG data.

png_image is a structure that describes the in-memory format of an image
when it is being read or define the in-memory format of an image that you
need to write.  The "png_image" structure contains the following members:

   png_uint_32  version Set to PNG_IMAGE_VERSION
   png_uint_32  width   Image width in pixels (columns)
   png_uint_32  height  Image height in pixels (rows)
   png_uint_32  format  Image format as defined below
   png_uint_32  flags   A bit mask containing informational flags
   png_controlp opaque  Initialize to NULL, free with png_image_free
   png_uint_32  colormap_entries; Number of entries in the color-map
   png_uint_32  warning_or_error;
   char         message[64];

In the event of an error or warning the following field warning_or_error
field will be set to a non-zero value and the 'message' field will contain
a '\0' terminated string with the libpng error or warning message.  If both
warnings and an error were encountered, only the error is recorded.  If there
are multiple warnings, only the first one is recorded.

The upper 30 bits of this value are reserved; the low two bits contain
a two bit code such that a value more than 1 indicates a failure in the API
just called:

   0 - no warning or error
   1 - warning
   2 - error
   3 - error preceded by warning

The pixels (samples) of the image have one to four channels whose components
have original values in the range 0 to 1.0:

  1: A single gray or luminance channel (G).
  2: A gray/luminance channel and an alpha channel (GA).
  3: Three red, green, blue color channels (RGB).
  4: Three color channels and an alpha channel (RGBA).

The channels are encoded in one of two ways:

  a) As a small integer, value 0..255, contained in a single byte.  For the
alpha channel the original value is simply value/255.  For the color or
luminance channels the value is encoded according to the sRGB specification
and matches the 8-bit format expected by typical display devices.

The color/gray channels are not scaled (pre-multiplied) by the alpha
channel and are suitable for passing to color management software.

  b) As a value in the range 0..65535, contained in a 2-byte integer, in
the native byte order of the platform on which the application is running.
All channels can be converted to the original value by dividing by 65535; all
channels are linear.  Color channels use the RGB encoding (RGB end-points) of
the sRGB specification.  This encoding is identified by the
PNG_FORMAT_FLAG_LINEAR flag below.

When an alpha channel is present it is expected to denote pixel coverage
of the color or luminance channels and is returned as an associated alpha
channel: the color/gray channels are scaled (pre-multiplied) by the alpha
value.

When a color-mapped image is used as a result of calling
png_image_read_colormap or png_image_write_colormap the channels are encoded
in the color-map and the descriptions above apply to the color-map entries.
The image data is encoded as small integers, value 0..255, that index the
entries in the color-map.  One integer (one byte) is stored for each pixel.

PNG_FORMAT_*

The #defines to be used in png_image::format.  Each #define identifies a
particular layout of channel data and, if present, alpha values.  There are
separate defines for each of the two channel encodings.

A format is built up using single bit flag values.  Not all combinations are
valid: use the bit flag values below for testing a format returned by the
read APIs, but set formats from the derived values.

When reading or writing color-mapped images the format should be set to the
format of the entries in the color-map then png_image_{read,write}_colormap
called to read or write the color-map and set the format correctly for the
image data.  Do not set the PNG_FORMAT_FLAG_COLORMAP bit directly!

NOTE: libpng can be built with particular features disabled, if you see
compiler errors because the definition of one of the following flags has been
compiled out it is because libpng does not have the required support.  It is
possible, however, for the libpng configuration to enable the format on just
read or just write; in that case you may see an error at run time.  You can
guard against this by checking for the definition of:

   PNG_SIMPLIFIED_{READ,WRITE}_{BGR,AFIRST}_SUPPORTED

   PNG_FORMAT_FLAG_ALPHA    0x01 format with an alpha channel
   PNG_FORMAT_FLAG_COLOR    0x02 color format: otherwise grayscale
   PNG_FORMAT_FLAG_LINEAR   0x04 png_uint_16 channels else png_byte
   PNG_FORMAT_FLAG_COLORMAP 0x08 libpng use only
   PNG_FORMAT_FLAG_BGR      0x10 BGR colors, else order is RGB
   PNG_FORMAT_FLAG_AFIRST   0x20 alpha channel comes first

Supported formats are as follows.  Future versions of libpng may support more
formats; for compatibility with older versions simply check if the format
macro is defined using #ifdef.  These defines describe the in-memory layout
of the components of the pixels of the image.

First the single byte formats:

   PNG_FORMAT_GRAY 0
   PNG_FORMAT_GA   PNG_FORMAT_FLAG_ALPHA
   PNG_FORMAT_AG   (PNG_FORMAT_GA|PNG_FORMAT_FLAG_AFIRST)
   PNG_FORMAT_RGB  PNG_FORMAT_FLAG_COLOR
   PNG_FORMAT_BGR  (PNG_FORMAT_FLAG_COLOR|PNG_FORMAT_FLAG_BGR)
   PNG_FORMAT_RGBA (PNG_FORMAT_RGB|PNG_FORMAT_FLAG_ALPHA)
   PNG_FORMAT_ARGB (PNG_FORMAT_RGBA|PNG_FORMAT_FLAG_AFIRST)
   PNG_FORMAT_BGRA (PNG_FORMAT_BGR|PNG_FORMAT_FLAG_ALPHA)
   PNG_FORMAT_ABGR (PNG_FORMAT_BGRA|PNG_FORMAT_FLAG_AFIRST)

Then the linear 2-byte formats.  When naming these "Y" is used to
indicate a luminance (gray) channel.  The component order within the pixel
is always the same - there is no provision for swapping the order of the
components in the linear format.  The components are 16-bit integers in
the native byte order for your platform, and there is no provision for
swapping the bytes to a different endian condition.

   PNG_FORMAT_LINEAR_Y PNG_FORMAT_FLAG_LINEAR
   PNG_FORMAT_LINEAR_Y_ALPHA
      (PNG_FORMAT_FLAG_LINEAR|PNG_FORMAT_FLAG_ALPHA)
   PNG_FORMAT_LINEAR_RGB
      (PNG_FORMAT_FLAG_LINEAR|PNG_FORMAT_FLAG_COLOR)
   PNG_FORMAT_LINEAR_RGB_ALPHA
      (PNG_FORMAT_FLAG_LINEAR|PNG_FORMAT_FLAG_COLOR|
      PNG_FORMAT_FLAG_ALPHA)

Color-mapped formats are obtained by calling png_image_{read,write}_colormap,
as appropriate after setting png_image::format to the format of the color-map
to be read or written.  Applications may check the value of
PNG_FORMAT_FLAG_COLORMAP to see if they have called the colormap API.  The
format of the color-map may be extracted using the following macro.

   PNG_FORMAT_OF_COLORMAP(fmt) ((fmt) & ~PNG_FORMAT_FLAG_COLORMAP)

PNG_IMAGE macros

These are convenience macros to derive information from a png_image
structure.  The PNG_IMAGE_SAMPLE_ macros return values appropriate to the
actual image sample values - either the entries in the color-map or the
pixels in the image.  The PNG_IMAGE_PIXEL_ macros return corresponding values
for the pixels and will always return 1 after a call to
png_image_{read,write}_colormap.  The remaining macros return information
about the rows in the image and the complete image.

NOTE: All the macros that take a png_image::format parameter are compile time
constants if the format parameter is, itself, a constant.  Therefore these
macros can be used in array declarations and case labels where required.
Similarly the macros are also pre-processor constants (sizeof is not used) so
they can be used in #if tests.

First the information about the samples.

  PNG_IMAGE_SAMPLE_CHANNELS(fmt)
    Returns the total number of channels in a given format: 1..4

  PNG_IMAGE_SAMPLE_COMPONENT_SIZE(fmt)
    Returns the size in bytes of a single component of a pixel or color-map
    entry (as appropriate) in the image.

  PNG_IMAGE_SAMPLE_SIZE(fmt)
    This is the size of the sample data for one sample.  If the image is
    color-mapped it is the size of one color-map entry (and image pixels are
    one byte in size), otherwise it is the size of one image pixel.

  PNG_IMAGE_COLORMAP_SIZE(fmt)
   The size of the color-map required by the format; this is the size of the
   color-map buffer passed to the png_image_{read,write}_colormap APIs, it is
   a fixed number determined by the format so can easily be allocated on the
   stack if necessary.

#define PNG_IMAGE_MAXIMUM_COLORMAP_COMPONENTS(fmt)\
   (PNG_IMAGE_SAMPLE_CHANNELS(fmt) * 256)
   /* The maximum size of the color-map required by the format expressed in a
    * count of components.  This can be used to compile-time allocate a
    * color-map:
    *
    * png_uint_16 colormap[PNG_IMAGE_MAXIMUM_COLORMAP_COMPONENTS(linear_fmt)];
    *
    * png_byte colormap[PNG_IMAGE_MAXIMUM_COLORMAP_COMPONENTS(sRGB_fmt)];
    *
    * Alternatively, use the PNG_IMAGE_COLORMAP_SIZE macro below to use the
    * information from one of the png_image_begin_read_ APIs and dynamically
    * allocate the required memory.
    */


Corresponding information about the pixels

  PNG_IMAGE_PIXEL_(test,fmt)

  PNG_IMAGE_PIXEL_CHANNELS(fmt)
   The number of separate channels (components) in a pixel; 1 for a
   color-mapped image.

  PNG_IMAGE_PIXEL_COMPONENT_SIZE(fmt)\
   The size, in bytes, of each component in a pixel; 1 for a color-mapped
   image.

  PNG_IMAGE_PIXEL_SIZE(fmt)
   The size, in bytes, of a complete pixel; 1 for a color-mapped image.

Information about the whole row, or whole image

  PNG_IMAGE_ROW_STRIDE(image)
   Returns the total number of components in a single row of the image; this
   is the minimum 'row stride', the minimum count of components between each
   row.  For a color-mapped image this is the minimum number of bytes in a
   row.

   If you need the stride measured in bytes, row_stride_bytes is
   PNG_IMAGE_ROW_STRIDE(image) * PNG_IMAGE_PIXEL_COMPONENT_SIZE(fmt)
   plus any padding bytes that your application might need, for example
   to start the next row on a 4-byte boundary.

  PNG_IMAGE_BUFFER_SIZE(image, row_stride)
    Returns the size, in bytes, of an image buffer given a png_image and a row
    stride - the number of components to leave space for in each row.  This
    macro takes care of multiplying row_stride by PNG_IMAGE_PIXEL_COMONENT_SIZE
    when the image has 2-byte components.

  PNG_IMAGE_FLAG_COLORSPACE_NOT_sRGB == 0x01
    This indicates the the RGB values of the in-memory bitmap do not
    correspond to the red, green and blue end-points defined by sRGB.

  PNG_IMAGE_FLAG_COLORMAP == 0x02
    The PNG is color-mapped.  If this flag is set png_image_read_colormap
    can be used without further loss of image information.  If it is not set
    png_image_read_colormap will cause significant loss if the image has any

READ APIs

   The png_image passed to the read APIs must have been initialized by setting
   the png_controlp field 'opaque' to NULL (or, better, memset the whole thing.)

   int png_image_begin_read_from_file( png_imagep image,
     const char *file_name)

     The named file is opened for read and the image header
     is filled in from the PNG header in the file.

   int png_image_begin_read_from_stdio (png_imagep image,
     FILE* file)

      The PNG header is read from the stdio FILE object.

   int png_image_begin_read_from_memory(png_imagep image,
      png_const_voidp memory, png_size_t size)

      The PNG header is read from the given memory buffer.

   int png_image_finish_read(png_imagep image,
      png_colorp background, void *buffer,
      png_int_32 row_stride, void *colormap));

      Finish reading the image into the supplied buffer and
      clean up the png_image structure.

      row_stride is the step, in png_byte or png_uint_16 units
      as appropriate, between adjacent rows.  A positive stride
      indicates that the top-most row is first in the buffer -
      the normal top-down arrangement.  A negative stride
      indicates that the bottom-most row is first in the buffer.

      background need only be supplied if an alpha channel must
      be removed from a png_byte format and the removal is to be
      done by compositing on a solid color; otherwise it may be
      NULL and any composition will be done directly onto the
      buffer.  The value is an sRGB color to use for the
      background, for grayscale output the green channel is used.

      For linear output removing the alpha channel is always done
      by compositing on black.

   void png_image_free(png_imagep image)

      Free any data allocated by libpng in image->opaque,
      setting the pointer to NULL.  May be called at any time
      after the structure is initialized.

When the simplified API needs to convert between sRGB and linear colorspaces,
the actual sRGB transfer curve defined in the sRGB specification (see the
article at http://en.wikipedia.org/wiki/SRGB) is used, not the gamma=1/2.2
approximation used elsewhere in libpng.

WRITE APIS

For write you must initialize a png_image structure to describe the image to
be written:

   version: must be set to PNG_IMAGE_VERSION
   opaque: must be initialized to NULL
   width: image width in pixels
   height: image height in rows
   format: the format of the data you wish to write
   flags: set to 0 unless one of the defined flags applies; set
      PNG_IMAGE_FLAG_COLORSPACE_NOT_sRGB for color format images
      where the RGB values do not correspond to the colors in sRGB.
   colormap_entries: set to the number of entries in the color-map (0 to 256)

   int png_image_write_to_file, (png_imagep image,
      const char *file, int convert_to_8bit, const void *buffer,
      png_int_32 row_stride, const void *colormap));

      Write the image to the named file.

   int png_image_write_to_stdio(png_imagep image, FILE *file,
      int convert_to_8_bit, const void *buffer,
      png_int_32 row_stride, const void *colormap)

      Write the image to the given (FILE*).

With all write APIs if image is in one of the linear formats with
(png_uint_16) data then setting convert_to_8_bit will cause the output to be
a (png_byte) PNG gamma encoded according to the sRGB specification, otherwise
a 16-bit linear encoded PNG file is written.

With all APIs row_stride is handled as in the read APIs - it is the spacing
from one row to the next in component sized units (float) and if negative
indicates a bottom-up row layout in the buffer.

Note that the write API does not support interlacing, sub-8-bit pixels,
and indexed (paletted) images.

VI. Modifying/Customizing libpng

There are two issues here.  The first is changing how libpng does
standard things like memory allocation, input/output, and error handling.
The second deals with more complicated things like adding new chunks,
adding new transformations, and generally changing how libpng works.
Both of those are compile-time issues; that is, they are generally
determined at the time the code is written, and there is rarely a need
to provide the user with a means of changing them.

Memory allocation, input/output, and error handling

All of the memory allocation, input/output, and error handling in libpng
goes through callbacks that are user-settable.  The default routines are
in pngmem.c, pngrio.c, pngwio.c, and pngerror.c, respectively.  To change
these functions, call the appropriate png_set_*_fn() function.

Memory allocation is done through the functions png_malloc(), png_calloc(),
and png_free().  The png_malloc() and png_free() functions currently just
call the standard C functions and png_calloc() calls png_malloc() and then
clears the newly allocated memory to zero; note that png_calloc(png_ptr, size)
is not the same as the calloc(number, size) function provided by stdlib.h.
There is limited support for certain systems with segmented memory
architectures and the types of pointers declared by png.h match this; you
will have to use appropriate pointers in your application.  If you prefer
to use a different method of allocating and freeing data, you can use
png_create_read_struct_2() or png_create_write_struct_2() to register your
own functions as described above.  These functions also provide a void
pointer that can be retrieved via

    mem_ptr=png_get_mem_ptr(png_ptr);

Your replacement memory functions must have prototypes as follows:

    png_voidp malloc_fn(png_structp png_ptr,
       png_alloc_size_t size);

    void free_fn(png_structp png_ptr, png_voidp ptr);

Your malloc_fn() must return NULL in case of failure.  The png_malloc()
function will normally call png_error() if it receives a NULL from the
system memory allocator or from your replacement malloc_fn().

Your free_fn() will never be called with a NULL ptr, since libpng's
png_free() checks for NULL before calling free_fn().

Input/Output in libpng is done through png_read() and png_write(),
which currently just call fread() and fwrite().  The FILE * is stored in
png_struct and is initialized via png_init_io().  If you wish to change
the method of I/O, the library supplies callbacks that you can set
through the function png_set_read_fn() and png_set_write_fn() at run
time, instead of calling the png_init_io() function.  These functions
also provide a void pointer that can be retrieved via the function
png_get_io_ptr().  For example:

    png_set_read_fn(png_structp read_ptr,
        voidp read_io_ptr, png_rw_ptr read_data_fn)

    png_set_write_fn(png_structp write_ptr,
        voidp write_io_ptr, png_rw_ptr write_data_fn,
        png_flush_ptr output_flush_fn);

    voidp read_io_ptr = png_get_io_ptr(read_ptr);
    voidp write_io_ptr = png_get_io_ptr(write_ptr);

The replacement I/O functions must have prototypes as follows:

    void user_read_data(png_structp png_ptr,
        png_bytep data, png_size_t length);

    void user_write_data(png_structp png_ptr,
        png_bytep data, png_size_t length);

    void user_flush_data(png_structp png_ptr);

The user_read_data() function is responsible for detecting and
handling end-of-data errors.

Supplying NULL for the read, write, or flush functions sets them back
to using the default C stream functions, which expect the io_ptr to
point to a standard *FILE structure.  It is probably a mistake
to use NULL for one of write_data_fn and output_flush_fn but not both
of them, unless you have built libpng with PNG_NO_WRITE_FLUSH defined.
It is an error to read from a write stream, and vice versa.

Error handling in libpng is done through png_error() and png_warning().
Errors handled through png_error() are fatal, meaning that png_error()
should never return to its caller.  Currently, this is handled via
setjmp() and longjmp() (unless you have compiled libpng with
PNG_NO_SETJMP, in which case it is handled via PNG_ABORT()),
but you could change this to do things like exit() if you should wish,
as long as your function does not return.

On non-fatal errors, png_warning() is called
to print a warning message, and then control returns to the calling code.
By default png_error() and png_warning() print a message on stderr via
fprintf() unless the library is compiled with PNG_NO_CONSOLE_IO defined
(because you don't want the messages) or PNG_NO_STDIO defined (because
fprintf() isn't available).  If you wish to change the behavior of the error
functions, you will need to set up your own message callbacks.  These
functions are normally supplied at the time that the png_struct is created.
It is also possible to redirect errors and warnings to your own replacement
functions after png_create_*_struct() has been called by calling:

    png_set_error_fn(png_structp png_ptr,
        png_voidp error_ptr, png_error_ptr error_fn,
        png_error_ptr warning_fn);

    png_voidp error_ptr = png_get_error_ptr(png_ptr);

If NULL is supplied for either error_fn or warning_fn, then the libpng
default function will be used, calling fprintf() and/or longjmp() if a
problem is encountered.  The replacement error functions should have
parameters as follows:

    void user_error_fn(png_structp png_ptr,
        png_const_charp error_msg);

    void user_warning_fn(png_structp png_ptr,
        png_const_charp warning_msg);

The motivation behind using setjmp() and longjmp() is the C++ throw and
catch exception handling methods.  This makes the code much easier to write,
as there is no need to check every return code of every function call.
However, there are some uncertainties about the status of local variables
after a longjmp, so the user may want to be careful about doing anything
after setjmp returns non-zero besides returning itself.  Consult your
compiler documentation for more details.  For an alternative approach, you
may wish to use the "cexcept" facility (see http://cexcept.sourceforge.net),
which is illustrated in pngvalid.c and in contrib/visupng.

Beginning in libpng-1.4.0, the png_set_benign_errors() API became available.
You can use this to handle certain errors (normally handled as errors)
as warnings.

    png_set_benign_errors (png_ptr, int allowed);

    allowed: 0: treat png_benign_error() as an error.
             1: treat png_benign_error() as a warning.

As of libpng-1.6.0, the default condition is to treat benign errors as
warnings while reading and as errors while writing.

Custom chunks

If you need to read or write custom chunks, you may need to get deeper
into the libpng code.  The library now has mechanisms for storing
and writing chunks of unknown type; you can even declare callbacks
for custom chunks.  However, this may not be good enough if the
library code itself needs to know about interactions between your
chunk and existing `intrinsic' chunks.

If you need to write a new intrinsic chunk, first read the PNG
specification. Acquire a first level of understanding of how it works.
Pay particular attention to the sections that describe chunk names,
and look at how other chunks were designed, so you can do things
similarly.  Second, check out the sections of libpng that read and
write chunks.  Try to find a chunk that is similar to yours and use
it as a template.  More details can be found in the comments inside
the code.  It is best to handle private or unknown chunks in a generic method,
via callback functions, instead of by modifying libpng functions. This
is illustrated in pngtest.c, which uses a callback function to handle a
private "vpAg" chunk and the new "sTER" chunk, which are both unknown to
libpng.

If you wish to write your own transformation for the data, look through
the part of the code that does the transformations, and check out some of
the simpler ones to get an idea of how they work.  Try to find a similar
transformation to the one you want to add and copy off of it.  More details
can be found in the comments inside the code itself.

Configuring for gui/windowing platforms:

You will need to write new error and warning functions that use the GUI
interface, as described previously, and set them to be the error and
warning functions at the time that png_create_*_struct() is called,
in order to have them available during the structure initialization.
They can be changed later via png_set_error_fn().  On some compilers,
you may also have to change the memory allocators (png_malloc, etc.).

Configuring zlib:

There are special functions to configure the compression.  Perhaps the
most useful one changes the compression level, which currently uses
input compression values in the range 0 - 9.  The library normally
uses the default compression level (Z_DEFAULT_COMPRESSION = 6).  Tests
have shown that for a large majority of images, compression values in
the range 3-6 compress nearly as well as higher levels, and do so much
faster.  For online applications it may be desirable to have maximum speed
(Z_BEST_SPEED = 1).  With versions of zlib after v0.99, you can also
specify no compression (Z_NO_COMPRESSION = 0), but this would create
files larger than just storing the raw bitmap.  You can specify the
compression level by calling:

    #include zlib.h
    png_set_compression_level(png_ptr, level);

Another useful one is to reduce the memory level used by the library.
The memory level defaults to 8, but it can be lowered if you are
short on memory (running DOS, for example, where you only have 640K).
Note that the memory level does have an effect on compression; among
other things, lower levels will result in sections of incompressible
data being emitted in smaller stored blocks, with a correspondingly
larger relative overhead of up to 15% in the worst case.

    #include zlib.h
    png_set_compression_mem_level(png_ptr, level);

The other functions are for configuring zlib.  They are not recommended
for normal use and may result in writing an invalid PNG file.  See
zlib.h for more information on what these mean.

    #include zlib.h
    png_set_compression_strategy(png_ptr,
        strategy);

    png_set_compression_window_bits(png_ptr,
        window_bits);

    png_set_compression_method(png_ptr, method);

This controls the size of the IDAT chunks (default 8192):

    png_set_compression_buffer_size(png_ptr, size);

As of libpng version 1.5.4, additional APIs became
available to set these separately for non-IDAT
compressed chunks such as zTXt, iTXt, and iCCP:

    #include zlib.h
    #if PNG_LIBPNG_VER >= 10504
    png_set_text_compression_level(png_ptr, level);

    png_set_text_compression_mem_level(png_ptr, level);

    png_set_text_compression_strategy(png_ptr,
        strategy);

    png_set_text_compression_window_bits(png_ptr,
        window_bits);

    png_set_text_compression_method(png_ptr, method);
    #endif

Controlling row filtering

If you want to control whether libpng uses filtering or not, which
filters are used, and how it goes about picking row filters, you
can call one of these functions.  The selection and configuration
of row filters can have a significant impact on the size and
encoding speed and a somewhat lesser impact on the decoding speed
of an image.  Filtering is enabled by default for RGB and grayscale
images (with and without alpha), but not for paletted images nor
for any images with bit depths less than 8 bits/pixel.

The 'method' parameter sets the main filtering method, which is
currently only '0' in the PNG 1.2 specification.  The 'filters'
parameter sets which filter(s), if any, should be used for each
scanline.  Possible values are PNG_ALL_FILTERS and PNG_NO_FILTERS
to turn filtering on and off, respectively.

Individual filter types are PNG_FILTER_NONE, PNG_FILTER_SUB,
PNG_FILTER_UP, PNG_FILTER_AVG, PNG_FILTER_PAETH, which can be bitwise
ORed together with '|' to specify one or more filters to use.
These filters are described in more detail in the PNG specification.
If you intend to change the filter type during the course of writing
the image, you should start with flags set for all of the filters
you intend to use so that libpng can initialize its internal
structures appropriately for all of the filter types.  (Note that this
means the first row must always be adaptively filtered, because libpng
currently does not allocate the filter buffers until png_write_row()
is called for the first time.)

    filters = PNG_FILTER_NONE | PNG_FILTER_SUB
              PNG_FILTER_UP | PNG_FILTER_AVG |
              PNG_FILTER_PAETH | PNG_ALL_FILTERS;

    png_set_filter(png_ptr, PNG_FILTER_TYPE_BASE,
       filters);
              The second parameter can also be
              PNG_INTRAPIXEL_DIFFERENCING if you are
              writing a PNG to be embedded in a MNG
              datastream.  This parameter must be the
              same as the value of filter_method used
              in png_set_IHDR().

It is also possible to influence how libpng chooses from among the
available filters.  This is done in one or both of two ways - by
telling it how important it is to keep the same filter for successive
rows, and by telling it the relative computational costs of the filters.

    double weights[3] = {1.5, 1.3, 1.1},
       costs[PNG_FILTER_VALUE_LAST] =
       {1.0, 1.3, 1.3, 1.5, 1.7};

    png_set_filter_heuristics(png_ptr,
       PNG_FILTER_HEURISTIC_WEIGHTED, 3,
       weights, costs);

The weights are multiplying factors that indicate to libpng that the
row filter should be the same for successive rows unless another row filter
is that many times better than the previous filter.  In the above example,
if the previous 3 filters were SUB, SUB, NONE, the SUB filter could have a
"sum of absolute differences" 1.5 x 1.3 times higher than other filters
and still be chosen, while the NONE filter could have a sum 1.1 times
higher than other filters and still be chosen.  Unspecified weights are
taken to be 1.0, and the specified weights should probably be declining
like those above in order to emphasize recent filters over older filters.

The filter costs specify for each filter type a relative decoding cost
to be considered when selecting row filters.  This means that filters
with higher costs are less likely to be chosen over filters with lower
costs, unless their "sum of absolute differences" is that much smaller.
The costs do not necessarily reflect the exact computational speeds of
the various filters, since this would unduly influence the final image
size.

Note that the numbers above were invented purely for this example and
are given only to help explain the function usage.  Little testing has
been done to find optimum values for either the costs or the weights.

Requesting debug printout

The macro definition PNG_DEBUG can be used to request debugging
printout.  Set it to an integer value in the range 0 to 3.  Higher
numbers result in increasing amounts of debugging information.  The
information is printed to the "stderr" file, unless another file
name is specified in the PNG_DEBUG_FILE macro definition.

When PNG_DEBUG > 0, the following functions (macros) become available:

   png_debug(level, message)
   png_debug1(level, message, p1)
   png_debug2(level, message, p1, p2)

in which "level" is compared to PNG_DEBUG to decide whether to print
the message, "message" is the formatted string to be printed,
and p1 and p2 are parameters that are to be embedded in the string
according to printf-style formatting directives.  For example,

   png_debug1(2, "foo=%d", foo);

is expanded to

   if (PNG_DEBUG > 2)
      fprintf(PNG_DEBUG_FILE, "foo=%d\n", foo);

When PNG_DEBUG is defined but is zero, the macros aren't defined, but you
can still use PNG_DEBUG to control your own debugging:

   #ifdef PNG_DEBUG
       fprintf(stderr, ...
   #endif

When PNG_DEBUG = 1, the macros are defined, but only png_debug statements
having level = 0 will be printed.  There aren't any such statements in
this version of libpng, but if you insert some they will be printed.

VII.  MNG support

The MNG specification (available at http://www.libpng.org/pub/mng) allows
certain extensions to PNG for PNG images that are embedded in MNG datastreams.
Libpng can support some of these extensions.  To enable them, use the
png_permit_mng_features() function:

   feature_set = png_permit_mng_features(png_ptr, mask)

   mask is a png_uint_32 containing the bitwise OR of the
        features you want to enable.  These include
        PNG_FLAG_MNG_EMPTY_PLTE
        PNG_FLAG_MNG_FILTER_64
        PNG_ALL_MNG_FEATURES

   feature_set is a png_uint_32 that is the bitwise AND of
      your mask with the set of MNG features that is
      supported by the version of libpng that you are using.

It is an error to use this function when reading or writing a standalone
PNG file with the PNG 8-byte signature.  The PNG datastream must be wrapped
in a MNG datastream.  As a minimum, it must have the MNG 8-byte signature
and the MHDR and MEND chunks.  Libpng does not provide support for these
or any other MNG chunks; your application must provide its own support for
them.  You may wish to consider using libmng (available at
http://www.libmng.com) instead.

VIII.  Changes to Libpng from version 0.88

It should be noted that versions of libpng later than 0.96 are not
distributed by the original libpng author, Guy Schalnat, nor by
Andreas Dilger, who had taken over from Guy during 1996 and 1997, and
distributed versions 0.89 through 0.96, but rather by another member
of the original PNG Group, Glenn Randers-Pehrson.  Guy and Andreas are
still alive and well, but they have moved on to other things.

The old libpng functions png_read_init(), png_write_init(),
png_info_init(), png_read_destroy(), and png_write_destroy() have been
moved to PNG_INTERNAL in version 0.95 to discourage their use.  These
functions will be removed from libpng version 1.4.0.

The preferred method of creating and initializing the libpng structures is
via the png_create_read_struct(), png_create_write_struct(), and
png_create_info_struct() because they isolate the size of the structures
from the application, allow version error checking, and also allow the
use of custom error handling routines during the initialization, which
the old functions do not.  The functions png_read_destroy() and
png_write_destroy() do not actually free the memory that libpng
allocated for these structs, but just reset the data structures, so they
can be used instead of png_destroy_read_struct() and
png_destroy_write_struct() if you feel there is too much system overhead
allocating and freeing the png_struct for each image read.

Setting the error callbacks via png_set_message_fn() before
png_read_init() as was suggested in libpng-0.88 is no longer supported
because this caused applications that do not use custom error functions
to fail if the png_ptr was not initialized to zero.  It is still possible
to set the error callbacks AFTER png_read_init(), or to change them with
png_set_error_fn(), which is essentially the same function, but with a new
name to force compilation errors with applications that try to use the old
method.

Support for the sCAL, iCCP, iTXt, and sPLT chunks was added at libpng-1.0.6;
however, iTXt support was not enabled by default.

Starting with version 1.0.7, you can find out which version of the library
you are using at run-time:

   png_uint_32 libpng_vn = png_access_version_number();

The number libpng_vn is constructed from the major version, minor
version with leading zero, and release number with leading zero,
(e.g., libpng_vn for version 1.0.7 is 10007).

Note that this function does not take a png_ptr, so you can call it
before you've created one.

You can also check which version of png.h you used when compiling your
application:

   png_uint_32 application_vn = PNG_LIBPNG_VER;

IX.  Changes to Libpng from version 1.0.x to 1.2.x

Support for user memory management was enabled by default.  To
accomplish this, the functions png_create_read_struct_2(),
png_create_write_struct_2(), png_set_mem_fn(), png_get_mem_ptr(),
png_malloc_default(), and png_free_default() were added.

Support for the iTXt chunk has been enabled by default as of
version 1.2.41.

Support for certain MNG features was enabled.

Support for numbered error messages was added.  However, we never got
around to actually numbering the error messages.  The function
png_set_strip_error_numbers() was added (Note: the prototype for this
function was inadvertently removed from png.h in PNG_NO_ASSEMBLER_CODE
builds of libpng-1.2.15.  It was restored in libpng-1.2.36).

The png_malloc_warn() function was added at libpng-1.2.3.  This issues
a png_warning and returns NULL instead of aborting when it fails to
acquire the requested memory allocation.

Support for setting user limits on image width and height was enabled
by default.  The functions png_set_user_limits(), png_get_user_width_max(),
and png_get_user_height_max() were added at libpng-1.2.6.

The png_set_add_alpha() function was added at libpng-1.2.7.

The function png_set_expand_gray_1_2_4_to_8() was added at libpng-1.2.9.
Unlike png_set_gray_1_2_4_to_8(), the new function does not expand the
tRNS chunk to alpha. The png_set_gray_1_2_4_to_8() function is
deprecated.

A number of macro definitions in support of runtime selection of
assembler code features (especially Intel MMX code support) were
added at libpng-1.2.0:

    PNG_ASM_FLAG_MMX_SUPPORT_COMPILED
    PNG_ASM_FLAG_MMX_SUPPORT_IN_CPU
    PNG_ASM_FLAG_MMX_READ_COMBINE_ROW
    PNG_ASM_FLAG_MMX_READ_INTERLACE
    PNG_ASM_FLAG_MMX_READ_FILTER_SUB
    PNG_ASM_FLAG_MMX_READ_FILTER_UP
    PNG_ASM_FLAG_MMX_READ_FILTER_AVG
    PNG_ASM_FLAG_MMX_READ_FILTER_PAETH
    PNG_ASM_FLAGS_INITIALIZED
    PNG_MMX_READ_FLAGS
    PNG_MMX_FLAGS
    PNG_MMX_WRITE_FLAGS
    PNG_MMX_FLAGS

We added the following functions in support of runtime
selection of assembler code features:

    png_get_mmx_flagmask()
    png_set_mmx_thresholds()
    png_get_asm_flags()
    png_get_mmx_bitdepth_threshold()
    png_get_mmx_rowbytes_threshold()
    png_set_asm_flags()

We replaced all of these functions with simple stubs in libpng-1.2.20,
when the Intel assembler code was removed due to a licensing issue.

These macros are deprecated:

    PNG_READ_TRANSFORMS_NOT_SUPPORTED
    PNG_PROGRESSIVE_READ_NOT_SUPPORTED
    PNG_NO_SEQUENTIAL_READ_SUPPORTED
    PNG_WRITE_TRANSFORMS_NOT_SUPPORTED
    PNG_READ_ANCILLARY_CHUNKS_NOT_SUPPORTED
    PNG_WRITE_ANCILLARY_CHUNKS_NOT_SUPPORTED

They have been replaced, respectively, by:

    PNG_NO_READ_TRANSFORMS
    PNG_NO_PROGRESSIVE_READ
    PNG_NO_SEQUENTIAL_READ
    PNG_NO_WRITE_TRANSFORMS
    PNG_NO_READ_ANCILLARY_CHUNKS
    PNG_NO_WRITE_ANCILLARY_CHUNKS

PNG_MAX_UINT was replaced with PNG_UINT_31_MAX.  It has been
deprecated since libpng-1.0.16 and libpng-1.2.6.

The function
    png_check_sig(sig, num)
was replaced with
    !png_sig_cmp(sig, 0, num)
It has been deprecated since libpng-0.90.

The function
    png_set_gray_1_2_4_to_8()
which also expands tRNS to alpha was replaced with
    png_set_expand_gray_1_2_4_to_8()
which does not. It has been deprecated since libpng-1.0.18 and 1.2.9.

X.  Changes to Libpng from version 1.0.x/1.2.x to 1.4.x

Private libpng prototypes and macro definitions were moved from
png.h and pngconf.h into a new pngpriv.h header file.

Functions png_set_benign_errors(), png_benign_error(), and
png_chunk_benign_error() were added.

Support for setting the maximum amount of memory that the application
will allocate for reading chunks was added, as a security measure.
The functions png_set_chunk_cache_max() and png_get_chunk_cache_max()
were added to the library.

We implemented support for I/O states by adding png_ptr member io_state
and functions png_get_io_chunk_name() and png_get_io_state() in pngget.c

We added PNG_TRANSFORM_GRAY_TO_RGB to the available high-level
input transforms.

Checking for and reporting of errors in the IHDR chunk is more thorough.

Support for global arrays was removed, to improve thread safety.

Some obsolete/deprecated macros and functions have been removed.

Typecasted NULL definitions such as
   #define png_voidp_NULL            (png_voidp)NULL
were eliminated.  If you used these in your application, just use
NULL instead.

The png_struct and info_struct members "trans" and "trans_values" were
changed to "trans_alpha" and "trans_color", respectively.

The obsolete, unused pnggccrd.c and pngvcrd.c files and related makefiles
were removed.

The PNG_1_0_X and PNG_1_2_X macros were eliminated.

The PNG_LEGACY_SUPPORTED macro was eliminated.

Many WIN32_WCE #ifdefs were removed.

The functions png_read_init(info_ptr), png_write_init(info_ptr),
png_info_init(info_ptr), png_read_destroy(), and png_write_destroy()
have been removed.  They have been deprecated since libpng-0.95.

The png_permit_empty_plte() was removed. It has been deprecated
since libpng-1.0.9.  Use png_permit_mng_features() instead.

We removed the obsolete stub functions png_get_mmx_flagmask(),
png_set_mmx_thresholds(), png_get_asm_flags(),
png_get_mmx_bitdepth_threshold(), png_get_mmx_rowbytes_threshold(),
png_set_asm_flags(), and png_mmx_supported()

We removed the obsolete png_check_sig(), png_memcpy_check(), and
png_memset_check() functions.  Instead use !png_sig_cmp(), memcpy(),
and memset(), respectively.

The function png_set_gray_1_2_4_to_8() was removed. It has been
deprecated since libpng-1.0.18 and 1.2.9, when it was replaced with
png_set_expand_gray_1_2_4_to_8() because the former function also
expanded any tRNS chunk to an alpha channel.

Macros for png_get_uint_16, png_get_uint_32, and png_get_int_32
were added and are used by default instead of the corresponding
functions. Unfortunately,
from libpng-1.4.0 until 1.4.4, the png_get_uint_16 macro (but not the
function) incorrectly returned a value of type png_uint_32.

We changed the prototype for png_malloc() from
    png_malloc(png_structp png_ptr, png_uint_32 size)
to
    png_malloc(png_structp png_ptr, png_alloc_size_t size)

This also applies to the prototype for the user replacement malloc_fn().

The png_calloc() function was added and is used in place of
of "png_malloc(); memset();" except in the case in png_read_png()
where the array consists of pointers; in this case a "for" loop is used
after the png_malloc() to set the pointers to NULL, to give robust.
behavior in case the application runs out of memory part-way through
the process.

We changed the prototypes of png_get_compression_buffer_size() and
png_set_compression_buffer_size() to work with png_size_t instead of
png_uint_32.

Support for numbered error messages was removed by default, since we
never got around to actually numbering the error messages. The function
png_set_strip_error_numbers() was removed from the library by default.

The png_zalloc() and png_zfree() functions are no longer exported.
The png_zalloc() function no longer zeroes out the memory that it
allocates.  Applications that called png_zalloc(png_ptr, number, size)
can call png_calloc(png_ptr, number*size) instead, and can call
png_free() instead of png_zfree().

Support for dithering was disabled by default in libpng-1.4.0, because
it has not been well tested and doesn't actually "dither".
The code was not
removed, however, and could be enabled by building libpng with
PNG_READ_DITHER_SUPPORTED defined.  In libpng-1.4.2, this support
was re-enabled, but the function was renamed png_set_quantize() to
reflect more accurately what it actually does.  At the same time,
the PNG_DITHER_[RED,GREEN_BLUE]_BITS macros were also renamed to
PNG_QUANTIZE_[RED,GREEN,BLUE]_BITS, and PNG_READ_DITHER_SUPPORTED
was renamed to PNG_READ_QUANTIZE_SUPPORTED.

We removed the trailing '.' from the warning and error messages.

XI.  Changes to Libpng from version 1.4.x to 1.5.x

From libpng-1.4.0 until 1.4.4, the png_get_uint_16 macro (but not the
function) incorrectly returned a value of type png_uint_32.
The incorrect macro was removed from libpng-1.4.5.

Checking for invalid palette index on write was added at libpng
1.5.10.  If a pixel contains an invalid (out-of-range) index libpng issues
a benign error.  This is enabled by default because this condition is an
error according to the PNG specification, Clause 11.3.2, but the error can
be ignored in each png_ptr with

   png_set_check_for_invalid_index(png_ptr, allowed);

      allowed  - one of
                 0: disable benign error (accept the
                    invalid data without warning).
                 1: enable benign error (treat the
                    invalid data as an error or a
                    warning).

If the error is ignored, or if png_benign_error() treats it as a warning,
any invalid pixels are decoded as opaque black by the decoder and written
as-is by the encoder.

Retrieving the maximum palette index found was added at libpng-1.5.15.
This statement must appear after png_read_png() or png_read_image() while
reading, and after png_write_png() or png_write_image() while writing.

   int max_palette = png_get_palette_max(png_ptr, info_ptr);

This will return the maximum palette index found in the image, or "-1" if
the palette was not checked, or "0" if no palette was found.  Note that this
does not account for any palette index used by ancillary chunks such as the
bKGD chunk; you must check those separately to determine the maximum
palette index actually used.

There are no substantial API changes between the non-deprecated parts of
the 1.4.5 API and the 1.5.0 API; however, the ability to directly access
members of the main libpng control structures, png_struct and png_info,
deprecated in earlier versions of libpng, has been completely removed from
libpng 1.5.

We no longer include zlib.h in png.h.  The include statement has been moved
to pngstruct.h, where it is not accessible by applications. Applications that
need access to information in zlib.h will need to add the '#include "zlib.h"'
directive.  It does not matter whether this is placed prior to or after
the '"#include png.h"' directive.

The png_sprintf(), png_strcpy(), and png_strncpy() macros are no longer used
and were removed.

We moved the png_strlen(), png_memcpy(), png_memset(), and png_memcmp()
macros into a private header file (pngpriv.h) that is not accessible to
applications.

In png_get_iCCP, the type of "profile" was changed from png_charpp
to png_bytepp, and in png_set_iCCP, from png_charp to png_const_bytep.

There are changes of form in png.h, including new and changed macros to
declare parts of the API.  Some API functions with arguments that are
pointers to data not modified within the function have been corrected to
declare these arguments with PNG_CONST.

Much of the internal use of C macros to control the library build has also
changed and some of this is visible in the exported header files, in
particular the use of macros to control data and API elements visible
during application compilation may require significant revision to
application code.  (It is extremely rare for an application to do this.)

Any program that compiled against libpng 1.4 and did not use deprecated
features or access internal library structures should compile and work
against libpng 1.5, except for the change in the prototype for
png_get_iCCP() and png_set_iCCP() API functions mentioned above.

libpng 1.5.0 adds PNG_ PASS macros to help in the reading and writing of
interlaced images.  The macros return the number of rows and columns in
each pass and information that can be used to de-interlace and (if
absolutely necessary) interlace an image.

libpng 1.5.0 adds an API png_longjmp(png_ptr, value).  This API calls
the application-provided png_longjmp_ptr on the internal, but application
initialized, longjmp buffer.  It is provided as a convenience to avoid
the need to use the png_jmpbuf macro, which had the unnecessary side
effect of resetting the internal png_longjmp_ptr value.

libpng 1.5.0 includes a complete fixed point API.  By default this is
present along with the corresponding floating point API.  In general the
fixed point API is faster and smaller than the floating point one because
the PNG file format used fixed point, not floating point.  This applies
even if the library uses floating point in internal calculations.  A new
macro, PNG_FLOATING_ARITHMETIC_SUPPORTED, reveals whether the library
uses floating point arithmetic (the default) or fixed point arithmetic
internally for performance critical calculations such as gamma correction.
In some cases, the gamma calculations may produce slightly different
results.  This has changed the results in png_rgb_to_gray and in alpha
composition (png_set_background for example). This applies even if the
original image was already linear (gamma == 1.0) and, therefore, it is
not necessary to linearize the image.  This is because libpng has *not*
been changed to optimize that case correctly, yet.

Fixed point support for the sCAL chunk comes with an important caveat;
the sCAL specification uses a decimal encoding of floating point values
and the accuracy of PNG fixed point values is insufficient for
representation of these values. Consequently a "string" API
(png_get_sCAL_s and png_set_sCAL_s) is the only reliable way of reading
arbitrary sCAL chunks in the absence of either the floating point API or
internal floating point calculations.  Starting with libpng-1.5.0, both
of these functions are present when PNG_sCAL_SUPPORTED is defined.  Prior
to libpng-1.5.0, their presence also depended upon PNG_FIXED_POINT_SUPPORTED
being defined and PNG_FLOATING_POINT_SUPPORTED not being defined.

Applications no longer need to include the optional distribution header
file pngusr.h or define the corresponding macros during application
build in order to see the correct variant of the libpng API.  From 1.5.0
application code can check for the corresponding _SUPPORTED macro:

#ifdef PNG_INCH_CONVERSIONS_SUPPORTED
   /* code that uses the inch conversion APIs. */
#endif

This macro will only be defined if the inch conversion functions have been
compiled into libpng.  The full set of macros, and whether or not support
has been compiled in, are available in the header file pnglibconf.h.
This header file is specific to the libpng build.  Notice that prior to
1.5.0 the _SUPPORTED macros would always have the default definition unless
reset by pngusr.h or by explicit settings on the compiler command line.
These settings may produce compiler warnings or errors in 1.5.0 because
of macro redefinition.

Applications can now choose whether to use these macros or to call the
corresponding function by defining PNG_USE_READ_MACROS or
PNG_NO_USE_READ_MACROS before including png.h.  Notice that this is
only supported from 1.5.0; defining PNG_NO_USE_READ_MACROS prior to 1.5.0
will lead to a link failure.

Prior to libpng-1.5.4, the zlib compressor used the same set of parameters
when compressing the IDAT data and textual data such as zTXt and iCCP.
In libpng-1.5.4 we reinitialized the zlib stream for each type of data.
We added five png_set_text_*() functions for setting the parameters to
use with textual data.

Prior to libpng-1.5.4, the PNG_READ_16_TO_8_ACCURATE_SCALE_SUPPORTED
option was off by default, and slightly inaccurate scaling occurred.
This option can no longer be turned off, and the choice of accurate
or inaccurate 16-to-8 scaling is by using the new png_set_scale_16_to_8()
API for accurate scaling or the old png_set_strip_16_to_8() API for simple
chopping.  In libpng-1.5.4, the PNG_READ_16_TO_8_ACCURATE_SCALE_SUPPORTED
macro became PNG_READ_SCALE_16_TO_8_SUPPORTED, and the PNG_READ_16_TO_8
macro became PNG_READ_STRIP_16_TO_8_SUPPORTED, to enable the two
png_set_*_16_to_8() functions separately.

Prior to libpng-1.5.4, the png_set_user_limits() function could only be
used to reduce the width and height limits from the value of
PNG_USER_WIDTH_MAX and PNG_USER_HEIGHT_MAX, although this document said
that it could be used to override them.  Now this function will reduce or
increase the limits.

Starting in libpng-1.5.10, the user limits can be set en masse with the
configuration option PNG_SAFE_LIMITS_SUPPORTED.  If this option is enabled,
a set of "safe" limits is applied in pngpriv.h.  These can be overridden by
application calls to png_set_user_limits(), png_set_user_chunk_cache_max(),
and/or png_set_user_malloc_max() that increase or decrease the limits.  Also,
in libpng-1.5.10 the default width and height limits were increased
from 1,000,000 to 0x7ffffff (i.e., made unlimited).  Therefore, the
limits are now
                               default      safe
   png_user_width_max        0x7fffffff    1,000,000
   png_user_height_max       0x7fffffff    1,000,000
   png_user_chunk_cache_max  0 (unlimited)   128
   png_user_chunk_malloc_max 0 (unlimited) 8,000,000

The png_set_option() function (and the "options" member of the png struct) was
added to libpng-1.5.15.

The library now supports a complete fixed point implementation and can
thus be used on systems that have no floating point support or very
limited or slow support.  Previously gamma correction, an essential part
of complete PNG support, required reasonably fast floating point.

As part of this the choice of internal implementation has been made
independent of the choice of fixed versus floating point APIs and all the
missing fixed point APIs have been implemented.

The exact mechanism used to control attributes of API functions has
changed, as described in the INSTALL file.

A new test program, pngvalid, is provided in addition to pngtest.
pngvalid validates the arithmetic accuracy of the gamma correction
calculations and includes a number of validations of the file format.
A subset of the full range of tests is run when "make check" is done
(in the 'configure' build.)  pngvalid also allows total allocated memory
usage to be evaluated and performs additional memory overwrite validation.

Many changes to individual feature macros have been made. The following
are the changes most likely to be noticed by library builders who
configure libpng:

1) All feature macros now have consistent naming:

#define PNG_NO_feature turns the feature off
#define PNG_feature_SUPPORTED turns the feature on

pnglibconf.h contains one line for each feature macro which is either:

#define PNG_feature_SUPPORTED

if the feature is supported or:

/*#undef PNG_feature_SUPPORTED*/

if it is not.  Library code consistently checks for the 'SUPPORTED' macro.
It does not, and libpng applications should not, check for the 'NO' macro
which will not normally be defined even if the feature is not supported.
The 'NO' macros are only used internally for setting or not setting the
corresponding 'SUPPORTED' macros.

Compatibility with the old names is provided as follows:

PNG_INCH_CONVERSIONS turns on PNG_INCH_CONVERSIONS_SUPPORTED

And the following definitions disable the corresponding feature:

PNG_SETJMP_NOT_SUPPORTED disables SETJMP
PNG_READ_TRANSFORMS_NOT_SUPPORTED disables READ_TRANSFORMS
PNG_NO_READ_COMPOSITED_NODIV disables READ_COMPOSITE_NODIV
PNG_WRITE_TRANSFORMS_NOT_SUPPORTED disables WRITE_TRANSFORMS
PNG_READ_ANCILLARY_CHUNKS_NOT_SUPPORTED disables READ_ANCILLARY_CHUNKS
PNG_WRITE_ANCILLARY_CHUNKS_NOT_SUPPORTED disables WRITE_ANCILLARY_CHUNKS

Library builders should remove use of the above, inconsistent, names.

2) Warning and error message formatting was previously conditional on
the STDIO feature. The library has been changed to use the
CONSOLE_IO feature instead. This means that if CONSOLE_IO is disabled
the library no longer uses the printf(3) functions, even though the
default read/write implementations use (FILE) style stdio.h functions.

3) Three feature macros now control the fixed/floating point decisions:

PNG_FLOATING_POINT_SUPPORTED enables the floating point APIs

PNG_FIXED_POINT_SUPPORTED enables the fixed point APIs; however, in
practice these are normally required internally anyway (because the PNG
file format is fixed point), therefore in most cases PNG_NO_FIXED_POINT
merely stops the function from being exported.

PNG_FLOATING_ARITHMETIC_SUPPORTED chooses between the internal floating
point implementation or the fixed point one.  Typically the fixed point
implementation is larger and slower than the floating point implementation
on a system that supports floating point; however, it may be faster on a
system which lacks floating point hardware and therefore uses a software
emulation.

4) Added PNG_{READ,WRITE}_INT_FUNCTIONS_SUPPORTED.  This allows the
functions to read and write ints to be disabled independently of
PNG_USE_READ_MACROS, which allows libpng to be built with the functions
even though the default is to use the macros - this allows applications
to choose at app buildtime whether or not to use macros (previously
impossible because the functions weren't in the default build.)

XII.  Changes to Libpng from version 1.5.x to 1.6.x

A "simplified API" has been added (see documentation in png.h and a simple
example in contrib/examples/pngtopng.c).  The new publicly visible API
includes the following:

   macros:
     PNG_FORMAT_*
     PNG_IMAGE_*
   structures:
     png_control
     png_image
   read functions
     png_image_begin_read_from_file()
     png_image_begin_read_from_stdio()
     png_image_begin_read_from_memory()
     png_image_finish_read()
     png_image_free()
   write functions
     png_image_write_to_file()
     png_image_write_to_stdio()

Starting with libpng-1.6.0, you can configure libpng to prefix all exported
symbols, using the PNG_PREFIX macro.

We no longer include string.h in png.h.  The include statement has been moved
to pngpriv.h, where it is not accessible by applications.  Applications that
need access to information in string.h must add an '#include <string.h>'
directive.  It does not matter whether this is placed prior to or after
the '#include "png.h"' directive.

The following API are now DEPRECATED:
   png_info_init_3()
   png_convert_to_rfc1123() which has been replaced
     with png_convert_to_rfc1123_buffer()
   png_malloc_default()
   png_free_default()
   png_reset_zstream()

The following have been removed:
   png_get_io_chunk_name(), which has been replaced
     with png_get_io_chunk_type().  The new
     function returns a 32-bit integer instead of
     a string.
   The png_sizeof(), png_strlen(), png_memcpy(), png_memcmp(), and
     png_memset() macros are no longer used in the libpng sources and
     have been removed.  These had already been made invisible to applications
     (i.e., defined in the private pngpriv.h header file) since libpng-1.5.0.

The signatures of many exported functions were changed, such that
   png_structp became png_structrp or png_const_structrp
   png_infop became png_inforp or png_const_inforp
where "rp" indicates a "restricted pointer".

The support for FAR/far types has been eliminated and the definition of
png_alloc_size_t is now controlled by a flag so that 'small size_t' systems
can select it if necessary.

Error detection in some chunks has improved; in particular the iCCP chunk
reader now does pretty complete validation of the basic format.  Some bad
profiles that were previously accepted are now accepted with a warning or
rejected, depending upon the png_set_benign_errors() setting, in particular
the very old broken Microsoft/HP 3144-byte sRGB profile.  Starting with
libpng-1.6.11, recognizing and checking sRGB profiles can be avoided by
means of

    #if defined(PNG_SKIP_sRGB_CHECK_PROFILE) && \
        defined(PNG_SET_OPTION_SUPPORTED)
       png_set_option(png_ptr, PNG_SKIP_sRGB_CHECK_PROFILE,
           PNG_OPTION_ON);
    #endif

It's not a good idea to do this if you are using the "simplified API",
which needs to be able to recognize sRGB profiles conveyed via the iCCP
chunk.

The PNG spec requirement that only grayscale profiles may appear in images
with color type 0 or 4 and that even if the image only contains gray pixels,
only RGB profiles may appear in images with color type 2, 3, or 6, is now
enforced.  The sRGB chunk is allowed to appear in images with any color type
and is interpreted by libpng to convey a one-tracer-curve gray profile or a
three-tracer-curve RGB profile as appropriate.

Prior to libpng-1.6.0 a warning would be issued if the iTXt chunk contained
an empty language field or an empty translated keyword.  Both of these
are allowed by the PNG specification, so these warnings are no longer issued.

The library now issues an error if the application attempts to set a
transform after it calls png_read_update_info() or if it attempts to call
both png_read_update_info() and png_start_read_image() or to call either
of them more than once.

The default condition for benign_errors is now to treat benign errors as
warnings while reading and as errors while writing.

The library now issues a warning if both background processing and RGB to
gray are used when gamma correction happens. As with previous versions of
the library the results are numerically very incorrect in this case.

There are some minor arithmetic changes in some transforms such as
png_set_background(), that might be detected by certain regression tests.

Unknown chunk handling has been improved internally, without any API change.
This adds more correct option control of the unknown handling, corrects
a pre-existing bug where the per-chunk 'keep' setting is ignored, and makes
it possible to skip IDAT chunks in the sequential reader.

The machine-generated configure files are no longer included in branches
libpng16 and later of the GIT repository.  They continue to be included
in the tarball releases, however.

Libpng-1.6.0 through 1.6.2 used the CMF bytes at the beginning of the IDAT
stream to set the size of the sliding window for reading instead of using the
default 32-kbyte sliding window size.  It was discovered that there are
hundreds of PNG files in the wild that have incorrect CMF bytes that caused
zlib to issue the "invalid distance too far back" error and reject the file.
Libpng-1.6.3 and later calculate their own safe CMF from the image dimensions,
provide a way to revert to the libpng-1.5.x behavior (ignoring the CMF bytes
and using a 32-kbyte sliding window), by using

    png_set_option(png_ptr, PNG_MAXIMUM_INFLATE_WINDOW,
        PNG_OPTION_ON);

and provide a tool (contrib/tools/pngfix) for rewriting a PNG file while
optimizing the CMF bytes in its IDAT chunk correctly.

Libpng-1.6.0 and libpng-1.6.1 wrote uncompressed iTXt chunks with the wrong
length, which resulted in PNG files that cannot be read beyond the bad iTXt
chunk.  This error was fixed in libpng-1.6.3, and a tool (called
contrib/tools/png-fix-itxt) has been added to the libpng distribution.

XIII.  Detecting libpng

The png_get_io_ptr() function has been present since libpng-0.88, has never
changed, and is unaffected by conditional compilation macros.  It is the
best choice for use in configure scripts for detecting the presence of any
libpng version since 0.88.  In an autoconf "configure.in" you could use

    AC_CHECK_LIB(png, png_get_io_ptr, ...

XV. Source code repository

Since about February 2009, version 1.2.34, libpng has been under "git" source
control.  The git repository was built from old libpng-x.y.z.tar.gz files
going back to version 0.70.  You can access the git repository (read only)
at

    git://git.code.sf.net/p/libpng/code

or you can browse it with a web browser by selecting the "code" button at

    https://sourceforge.net/projects/libpng

Patches can be sent to glennrp at users.sourceforge.net or to
png-mng-implement at lists.sourceforge.net or you can upload them to
the libpng bug tracker at

    http://libpng.sourceforge.net

We also accept patches built from the tar or zip distributions, and
simple verbal discriptions of bug fixes, reported either to the
SourceForge bug tracker, to the png-mng-implement at lists.sf.net
mailing list, or directly to glennrp.

XV. Coding style

Our coding style is similar to the "Allman" style
(See http://en.wikipedia.org/wiki/Indent_style#Allman_style), with curly
braces on separate lines:

    if (condition)
    {
       action;
    }

    else if (another condition)
    {
       another action;
    }

The braces can be omitted from simple one-line actions:

    if (condition)
       return (0);

We use 3-space indentation, except for continued statements which
are usually indented the same as the first line of the statement
plus four more spaces.

For macro definitions we use 2-space indentation, always leaving the "#"
in the first column.

    #ifndef PNG_NO_FEATURE
    #  ifndef PNG_FEATURE_SUPPORTED
    #    define PNG_FEATURE_SUPPORTED
    #  endif
    #endif

Comments appear with the leading "/*" at the same indentation as
the statement that follows the comment:

    /* Single-line comment */
    statement;

    /* This is a multiple-line
     * comment.
     */
    statement;

Very short comments can be placed after the end of the statement
to which they pertain:

    statement;    /* comment */

We don't use C++ style ("//") comments. We have, however,
used them in the past in some now-abandoned MMX assembler
code.

Functions and their curly braces are not indented, and
exported functions are marked with PNGAPI:

 /* This is a public function that is visible to
  * application programmers. It does thus-and-so.
  */
 void PNGAPI
 png_exported_function(png_ptr, png_info, foo)
 {
    body;
 }

The return type and decorations are placed on a separate line
ahead of the function name, as illustrated above.

The prototypes for all exported functions appear in png.h,
above the comment that says

    /* Maintainer: Put new public prototypes here ... */

We mark all non-exported functions with "/* PRIVATE */"":

 void /* PRIVATE */
 png_non_exported_function(png_ptr, png_info, foo)
 {
    body;
 }

The prototypes for non-exported functions (except for those in
pngtest) appear in pngpriv.h above the comment that says

  /* Maintainer: Put new private prototypes here ^ */

To avoid polluting the global namespace, the names of all exported
functions and variables begin with "png_", and all publicly visible C
preprocessor macros begin with "PNG".  We request that applications that
use libpng *not* begin any of their own symbols with either of these strings.

We put a space after the "sizeof" operator and we omit the
optional parentheses around its argument when the argument
is an expression, not a type name, and we always enclose the
sizeof operator, with its argument, in parentheses:

  (sizeof (png_uint_32))
  (sizeof array)

Prior to libpng-1.6.0 we used a "png_sizeof()" macro, formatted as
though it were a function.

Control keywords if, for, while, and switch are always followed by a space
to distinguish them from function calls, which have no trailing space. 

We put a space after each comma and after each semicolon
in "for" statements, and we put spaces before and after each
C binary operator and after "for" or "while", and before
"?".  We don't put a space between a typecast and the expression
being cast, nor do we put one between a function name and the
left parenthesis that follows it:

    for (i = 2; i > 0; --i)
       y[i] = a(x) + (int)b;

We prefer #ifdef and #ifndef to #if defined() and #if !defined()
when there is only one macro being tested.  We always use parentheses
with "defined".

We prefer to express integers that are used as bit masks in hex format,
with an even number of lower-case hex digits (e.g., 0x00, 0xff, 0x0100).

We prefer to use underscores in variable names rather than camelCase, except
for a few type names that we inherit from zlib.h.

We prefer "if (something != 0)" and "if (something == 0)"
over "if (something)" and if "(!something)", respectively.

We do not use the TAB character for indentation in the C sources.

Lines do not exceed 80 characters.

Other rules can be inferred by inspecting the libpng source.

XVI. Y2K Compliance in libpng

March 26, 2015

Since the PNG Development group is an ad-hoc body, we can't make
an official declaration.

This is your unofficial assurance that libpng from version 0.71 and
upward through 1.6.17 are Y2K compliant.  It is my belief that earlier
versions were also Y2K compliant.

Libpng only has two year fields.  One is a 2-byte unsigned integer
that will hold years up to 65535.  The other, which is deprecated,
holds the date in text format, and will hold years up to 9999.

The integer is
    "png_uint_16 year" in png_time_struct.

The string is
    "char time_buffer[29]" in png_struct.  This is no longer used
in libpng-1.6.x and will be removed from libpng-1.7.0.

There are seven time-related functions:

    png_convert_to_rfc_1123_buffer() in png.c
      (formerly png_convert_to_rfc_1152() in error, and
      also formerly png_convert_to_rfc_1123())
    png_convert_from_struct_tm() in pngwrite.c, called
      in pngwrite.c
    png_convert_from_time_t() in pngwrite.c
    png_get_tIME() in pngget.c
    png_handle_tIME() in pngrutil.c, called in pngread.c
    png_set_tIME() in pngset.c
    png_write_tIME() in pngwutil.c, called in pngwrite.c

All appear to handle dates properly in a Y2K environment.  The
png_convert_from_time_t() function calls gmtime() to convert from system
clock time, which returns (year - 1900), which we properly convert to
the full 4-digit year.  There is a possibility that applications using
libpng are not passing 4-digit years into the png_convert_to_rfc_1123()
function, or that they are incorrectly passing only a 2-digit year
instead of "year - 1900" into the png_convert_from_struct_tm() function,
but this is not under our control.  The libpng documentation has always
stated that it works with 4-digit years, and the APIs have been
documented as such.

The tIME chunk itself is also Y2K compliant.  It uses a 2-byte unsigned
integer to hold the year, and can hold years as large as 65535.

zlib, upon which libpng depends, is also Y2K compliant.  It contains
no date-related code.


   Glenn Randers-Pehrson
   libpng maintainer
   PNG Development Group

This copy of the libpng notices is provided for your convenience.  In case of
any discrepancy between this copy and the notices in the file png.h that is
included in the libpng distribution, the latter shall prevail.

COPYRIGHT NOTICE, DISCLAIMER, and LICENSE:

If you modify libpng you may insert additional notices immediately following
this sentence.

This code is released under the libpng license.

libpng versions 1.2.6, August 15, 2004, through 1.6.17, March 26, 2015, are
Copyright (c) 2004, 2006-2015 Glenn Randers-Pehrson, and are
distributed according to the same disclaimer and license as libpng-1.2.5
with the following individual added to the list of Contributing Authors

   Cosmin Truta

libpng versions 1.0.7, July 1, 2000, through 1.2.5 - October 3, 2002, are
Copyright (c) 2000-2002 Glenn Randers-Pehrson, and are
distributed according to the same disclaimer and license as libpng-1.0.6
with the following individuals added to the list of Contributing Authors

   Simon-Pierre Cadieux
   Eric S. Raymond
   Gilles Vollant

and with the following additions to the disclaimer:

   There is no warranty against interference with your enjoyment of the
   library or against infringement.  There is no warranty that our
   efforts or the library will fulfill any of your particular purposes
   or needs.  This library is provided with all faults, and the entire
   risk of satisfactory quality, performance, accuracy, and effort is with
   the user.

libpng versions 0.97, January 1998, through 1.0.6, March 20, 2000, are
Copyright (c) 1998, 1999 Glenn Randers-Pehrson, and are
distributed according to the same disclaimer and license as libpng-0.96,
with the following individuals added to the list of Contributing Authors:

   Tom Lane
   Glenn Randers-Pehrson
   Willem van Schaik

libpng versions 0.89, June 1996, through 0.96, May 1997, are
Copyright (c) 1996, 1997 Andreas Dilger
Distributed according to the same disclaimer and license as libpng-0.88,
with the following individuals added to the list of Contributing Authors:

   John Bowler
   Kevin Bracey
   Sam Bushell
   Magnus Holmgren
   Greg Roelofs
   Tom Tanner

libpng versions 0.5, May 1995, through 0.88, January 1996, are
Copyright (c) 1995, 1996 Guy Eric Schalnat, Group 42, Inc.

For the purposes of this copyright and license, "Contributing Authors"
is defined as the following set of individuals:

   Andreas Dilger
   Dave Martindale
   Guy Eric Schalnat
   Paul Schmidt
   Tim Wegner

The PNG Reference Library is supplied "AS IS".  The Contributing Authors
and Group 42, Inc. disclaim all warranties, expressed or implied,
including, without limitation, the warranties of merchantability and of
fitness for any purpose.  The Contributing Authors and Group 42, Inc.
assume no liability for direct, indirect, incidental, special, exemplary,
or consequential damages, which may result from the use of the PNG
Reference Library, even if advised of the possibility of such damage.

Permission is hereby granted to use, copy, modify, and distribute this
source code, or portions hereof, for any purpose, without fee, subject
to the following restrictions:

1. The origin of this source code must not be misrepresented.

2. Altered versions must be plainly marked as such and must not
   be misrepresented as being the original source.

3. This Copyright notice may not be removed or altered from any
   source or altered source distribution.

The Contributing Authors and Group 42, Inc. specifically permit, without
fee, and encourage the use of this source code as a component to
supporting the PNG file format in commercial products.  If you use this
source code in a product, acknowledgment is not required but would be
appreciated.


A "png_get_copyright" function is available, for convenient use in "about"
boxes and the like:

   printf("%s",png_get_copyright(NULL));

Also, the PNG logo (in PNG format, of course) is supplied in the
files "pngbar.png" and "pngbar.jpg (88x31) and "pngnow.png" (98x31).

Libpng is OSI Certified Open Source Software.  OSI Certified Open Source is a
certification mark of the Open Source Initiative.

Glenn Randers-Pehrson
glennrp at users.sourceforge.net
March 26, 2015
README for libpng version 1.6.17 - March 26, 2015 (shared library 16.0)
See the note about version numbers near the top of png.h

See INSTALL for instructions on how to install libpng.

Libpng comes in several distribution formats.  Get libpng-*.tar.gz or
libpng-*.tar.xz or if you want UNIX-style line endings in the text files,
or lpng*.7z or lpng*.zip if you want DOS-style line endings.

Version 0.89 was the first official release of libpng.  Don't let the
fact that it's the first release fool you.  The libpng library has been in
extensive use and testing since mid-1995.  By late 1997 it had
finally gotten to the stage where there hadn't been significant
changes to the API in some time, and people have a bad feeling about
libraries with versions < 1.0.  Version 1.0.0 was released in
March 1998.

****
Note that some of the changes to the png_info structure render this
version of the library binary incompatible with libpng-0.89 or
earlier versions if you are using a shared library.  The type of the
"filler" parameter for png_set_filler() has changed from png_byte to
png_uint_32, which will affect shared-library applications that use
this function.

To avoid problems with changes to the internals of png info_struct,
new APIs have been made available in 0.95 to avoid direct application
access to info_ptr.  These functions are the png_set_<chunk> and
png_get_<chunk> functions.  These functions should be used when
accessing/storing the info_struct data, rather than manipulating it
directly, to avoid such problems in the future.

It is important to note that the APIs did not make current programs
that access the info struct directly incompatible with the new
library, through libpng-1.2.x.  In libpng-1.4.x, which was meant to
be a transitional release, members of the png_struct and the
info_struct can still be accessed, but the compiler will issue a
warning about deprecated usage.  Since libpng-1.5.0, direct access
to these structs is not allowed, and the definitions of the structs
reside in private pngstruct.h and pnginfo.h header files that are not
accessible to applications.  It is strongly suggested that new
programs use the new APIs (as shown in example.c and pngtest.c), and
older programs be converted to the new format, to facilitate upgrades
in the future.
****

Additions since 0.90 include the ability to compile libpng as a
Windows DLL, and new APIs for accessing data in the info struct.
Experimental functions include the ability to set weighting and cost
factors for row filter selection, direct reads of integers from buffers
on big-endian processors that support misaligned data access, faster
methods of doing alpha composition, and more accurate 16->8 bit color
conversion.

The additions since 0.89 include the ability to read from a PNG stream
which has had some (or all) of the signature bytes read by the calling
application.  This also allows the reading of embedded PNG streams that
do not have the PNG file signature.  As well, it is now possible to set
the library action on the detection of chunk CRC errors.  It is possible
to set different actions based on whether the CRC error occurred in a
critical or an ancillary chunk.

The changes made to the library, and bugs fixed are based on discussions
on the PNG-implement mailing list and not on material submitted
privately to Guy, Andreas, or Glenn.  They will forward any good
suggestions to the list.

For a detailed description on using libpng, read libpng-manual.txt.  For
examples of libpng in a program, see example.c and pngtest.c.  For usage
information and restrictions (what little they are) on libpng, see
png.h.  For a description on using zlib (the compression library used by
libpng) and zlib's restrictions, see zlib.h

I have included a general makefile, as well as several machine and
compiler specific ones, but you may have to modify one for your own needs.

You should use zlib 1.0.4 or later to run this, but it MAY work with
versions as old as zlib 0.95.  Even so, there are bugs in older zlib
versions which can cause the output of invalid compression streams for
some images.  You will definitely need zlib 1.0.4 or later if you are
taking advantage of the MS-DOS "far" structure allocation for the small
and medium memory models.  You should also note that zlib is a
compression library that is useful for more things than just PNG files.
You can use zlib as a drop-in replacement for fread() and fwrite() if
you are so inclined.

zlib should be available at the same place that libpng is, or at zlib.net.

You may also want a copy of the PNG specification.  It is available
as an RFC, a W3C Recommendation, and an ISO/IEC Standard.  You can find
these at http://www.libpng.org/pub/png/documents/

This code is currently being archived at libpng.sf.net in the
[DOWNLOAD] area, and at ftp://ftp.simplesystems.org.  If you can't find it
in any of those places, e-mail me, and I'll help you find it.

I am not a lawyer, but I believe that the Export Control Classification
Number (ECCN) for libpng is EAR99, which means not subject to export
controls or International Traffic in Arms Regulations (ITAR) because it
is open source, publicly available software, that does not contain any
encryption software.  See the EAR, paragraphs 734.3(b)(3) and 734.7(b).

If you have any code changes, requests, problems, etc., please e-mail
them to me.  Also, I'd appreciate any make files or project files,
and any modifications you needed to make to get libpng to compile,
along with a #define variable to tell what compiler/system you are on.
If you needed to add transformations to libpng, or wish libpng would
provide the image in a different way, drop me a note (and code, if
possible), so I can consider supporting the transformation.
Finally, if you get any warning messages when compiling libpng
(note: not zlib), and they are easy to fix, I'd appreciate the
fix.  Please mention "libpng" somewhere in the subject line.  Thanks.

This release was created and will be supported by myself (of course
based in a large way on Guy's and Andreas' earlier work), and the PNG
development group.

Send comments/corrections/commendations to png-mng-implement at
lists.sourceforge.net (subscription required; visit
https://lists.sourceforge.net/lists/listinfo/png-mng-implement
to subscribe) or to glennrp at users.sourceforge.net

You can't reach Guy, the original libpng author, at the addresses
given in previous versions of this document.  He and Andreas will
read mail addressed to the png-implement list, however.

Please do not send general questions about PNG.  Send them to
png-mng-misc at lists.sf.net (subscription required; visit
https://lists.sourceforge.net/lists/listinfo/png-mng-misc to
subscribe).  If you have a question about something
in the PNG specification that is related to using libpng, send it
to me.  Send me any questions that start with "I was using libpng,
and ...".  If in doubt, send questions to me.  I'll bounce them
to others, if necessary.

Please do not send suggestions on how to change PNG.  We have
been discussing PNG for nineteen years now, and it is official and
finished.  If you have suggestions for libpng, however, I'll
gladly listen.  Even if your suggestion is not used immediately,
it may be used later.

Files in this distribution:

      ANNOUNCE      =>  Announcement of this version, with recent changes
      CHANGES       =>  Description of changes between libpng versions
      KNOWNBUG      =>  List of known bugs and deficiencies
      LICENSE       =>  License to use and redistribute libpng
      README        =>  This file
      TODO          =>  Things not implemented in the current library
      Y2KINFO       =>  Statement of Y2K compliance
      example.c     =>  Example code for using libpng functions
      libpng.3      =>  manual page for libpng (includes libpng-manual.txt)
      libpng-manual.txt  =>  Description of libpng and its functions
      libpngpf.3    =>  manual page for libpng's private functions
      png.5         =>  manual page for the PNG format
      png.c         =>  Basic interface functions common to library
      png.h         =>  Library function and interface declarations (public)
      pngpriv.h     =>  Library function and interface declarations (private)
      pngconf.h     =>  System specific library configuration (public)
      pngstruct.h   =>  png_struct declaration (private)
      pnginfo.h     =>  png_info struct declaration (private)
      pngdebug.h    =>  debugging macros (private)
      pngerror.c    =>  Error/warning message I/O functions
      pngget.c      =>  Functions for retrieving info from struct
      pngmem.c      =>  Memory handling functions
      pngbar.png    =>  PNG logo, 88x31
      pngnow.png    =>  PNG logo, 98x31
      pngpread.c    =>  Progressive reading functions
      pngread.c     =>  Read data/helper high-level functions
      pngrio.c      =>  Lowest-level data read I/O functions
      pngrtran.c    =>  Read data transformation functions
      pngrutil.c    =>  Read data utility functions
      pngset.c      =>  Functions for storing data into the info_struct
      pngtest.c     =>  Library test program
      pngtest.png   =>  Library test sample image
      pngtrans.c    =>  Common data transformation functions
      pngwio.c      =>  Lowest-level write I/O functions
      pngwrite.c    =>  High-level write functions
      pngwtran.c    =>  Write data transformations
      pngwutil.c    =>  Write utility functions
      arm           =>  Contains optimized code for the ARM platform
      contrib       =>  Contributions
       examples         =>  Example programs
       gregbook         =>  source code for PNG reading and writing, from
                            Greg Roelofs' "PNG: The Definitive Guide",
                            O'Reilly, 1999
       libtests         =>  Test programs
       pngminim         =>  Minimal decoder, encoder, and progressive decoder
                            programs demonstrating use of pngusr.dfa
       pngminus         =>  Simple pnm2png and png2pnm programs
       pngsuite         =>  Test images
       tools            =>  Various tools
       visupng          =>  Contains a MSVC workspace for VisualPng
      projects      =>  Contains project files and workspaces for
                        building a DLL
       owatcom          =>  Contains a WATCOM project for building libpng
       visualc71        =>  Contains a Microsoft Visual C++ (MSVC)
                            workspace for building libpng and zlib
       vstudio          =>  Contains a Microsoft Visual C++ (MSVC)
                            workspace for building libpng and zlib
      scripts       =>  Directory containing scripts for building libpng:
                            (see scripts/README.txt for the list of scripts)

Good luck, and happy coding.

-Glenn Randers-Pehrson (current maintainer, since 1998)
 Internet: glennrp at users.sourceforge.net

-Andreas Eric Dilger (former maintainer, 1996-1997)
 Internet: adilger at enel.ucalgary.ca
 Web: http://www-mddsp.enel.ucalgary.ca/People/adilger/

-Guy Eric Schalnat (original author and former maintainer, 1995-1996)
 (formerly of Group 42, Inc)
 Internet: gschal at infinet.com
cmake_minimum_required(VERSION 2.8.12)

project(libpvrt)

set(SRC_FILES
    PVRTArray.h
    PVRTError.h
    PVRTGlobal.h
    PVRTMap.h
    PVRTMemoryFileSystem.h
    PVRTResourceFile.h
    PVRTString.h
    PVRTTexture.h
    PVRTError.cpp
    PVRTResourceFile.cpp
    PVRTString.cpp
    PVRTTexture.cpp
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

project(libvorbis)

set(SRC_FILES
    lib/analysis.c
    lib/bitrate.c
    lib/block.c
    lib/codebook.c
    lib/envelope.c
    lib/floor0.c
    lib/floor1.c
    lib/info.c
    lib/lookup.c
    lib/lpc.c
    lib/lsp.c
    lib/mapping0.c
    lib/mdct.c
    lib/psy.c
    lib/registry.c
    lib/res0.c
    lib/sharedbook.c
    lib/smallft.c
    lib/synthesis.c
    lib/vorbisenc.c
    lib/window.c  
    lib/backends.h
    lib/bitrate.h
    lib/codebook.h
    include/vorbis/codec.h
    lib/codec_internal.h
    lib/envelope.h
    lib/modes/floor_all.h
    lib/books/floor/floor_books.h
    lib/highlevel.h
    lib/lookup.h
    lib/lookup_data.h
    lib/lpc.h
    lib/lsp.h
    lib/masking.h
    lib/mdct.h
    lib/misc.h
    lib/os.h
    lib/psy.h
    lib/modes/psych_11.h
    lib/modes/psych_16.h
    lib/modes/psych_44.h
    lib/modes/psych_8.h
    lib/registry.h
    lib/books/coupled/res_books_stereo.h
    lib/books/uncoupled/res_books_uncoupled.h
    lib/modes/residue_16.h
    lib/modes/residue_44.h
    lib/modes/residue_44u.h
    lib/modes/residue_8.h
    lib/scales.h
    lib/modes/setup_11.h
    lib/modes/setup_16.h
    lib/modes/setup_22.h
    lib/modes/setup_32.h
    lib/modes/setup_44.h
    lib/modes/setup_44u.h
    lib/modes/setup_8.h
    lib/modes/setup_X.h
    lib/smallft.h
    include/vorbis/vorbisenc.h
    include/vorbis/vorbisfile.h
    lib/window.h
    lib/vorbisfile.c
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

include_directories(${PROJECT_SOURCE_DIR}/lib)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

target_include_directories(${PROJECT_NAME} 
  PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

target_link_libraries(${PROJECT_NAME} libogg)
cmake_minimum_required(VERSION 2.8.12)

project(lua)

set(SRC_FILES
    lapi.h
    lapi.c
    lauxlib.h
    lauxlib.c
    lbaselib.c
    lcode.h
    lcode.c
    ldblib.c
    ldebug.h
    ldebug.c
    ldo.h
    ldo.c
    ldump.c
    lfunc.c
    lfunc.h
    lgc.c
    lgc.h
    linit.c
    liolib.c
    llex.h
    llex.c
    llimits.h
    lmathlib.c
    lmem.c
    lmem.h
    loadlib.c
    lobject.c
    lobject.h
    lopcodes.c
    lopcodes.h
    loslib.c
    lparser.h
    lparser.c
    #lprefix.h
    lstate.h
    lstate.c
    lstring.h
    lstring.c
    lstrlib.c
    ltable.c
    ltable.h
    ltablib.c
    ltm.h
    ltm.c
    lua.h
    luaconf.h
    lualib.h
    lundump.h
    lundump.c
    #lutf8lib.c
    lvm.h
    lvm.c
    lzio.h
    lzio.c
)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

project(LuaCpp)

set(ALL_FILES
    LuaCpp.h
    BaseFunc.h
    Class.h
    ClassFunc.h
    Ctor.h
    Dtor.h
    ExceptionHandler.h
    ExceptionTypes.h
    Func.h
    function.h
    LuaRef.h
    MetatableRegistry.h
    Obj.h
    ObjFunc.h
    Searcher.h
    Module.h
    LuaStack.h
    Reference.h
    Pointer.h
    Registry.h
    ResourceHandler.h
    Selector.h
    State.h
    Traits.h  
    Tuple.h
    Util.h
    BaseFunc.cpp
    MetatableRegistry.cpp
    Selector.cpp
    State.cpp
    Util.cpp
)

auto_source_group(${ALL_FILES})

include_directories(${ENGINE_INCLUDE_DIR}/ThirdParty)

add_library(${PROJECT_NAME} STATIC ${ALL_FILES})

target_include_directories(${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)

if (USE_LUAJIT)
    include(FindLuaJIT)
    set(LUA_LIBRARY ${LUAJIT_LIBRARY})

    target_include_directories(${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${ENGINE_INCLUDE_DIR}/ThirdParty/luaJIT/src>)
else ()
    set(LUA_LIBRARY lua)

    target_include_directories(${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${ENGINE_INCLUDE_DIR}/ThirdParty/lua>)
endif ()

target_link_libraries(${PROJECT_NAME} ${LUA_LIBRARY})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

cmake_minimum_required(VERSION 2.8.12)

if (COMMAND cmake_policy)
    if (POLICY CMP0053)
        # Simplify variable reference and escape sequence evaluation.
        cmake_policy(SET CMP0053 OLD)
    endif ()
endif ()

project(LuaJIT)

include(FindLuaJIT)

file(GLOB_RECURSE ALL_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/lua*.h*)

auto_source_group(${ALL_FILES})

add_custom_target(${PROJECT_NAME} SOURCES ${ALL_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER ThirdParty)

# Skip LuaJIT compilation if library file already exists
if (NOT LUAJIT_FOUND)
    set(STATIC_LIB TRUE)

    if (APPLE)
        if (NOT IOS)
            set($ENV{MACOSX_DEPLOYMENT_TARGET} ${CMAKE_OSX_DEPLOYMENT_TARGET})
            set(LJLIBNAME libluajit.a)
            set(LJARCH x86_64)

            execute_process(COMMAND make clean
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)

            execute_process(COMMAND make "TARGET_FLAGS=-arch ${LJARCH}"
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)

            # Copy library and interpreter executable to lib folder
            file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../lib/${LUAJIT_LIBDIR})

            execute_process(COMMAND ${CMAKE_COMMAND} -E copy luajit ../lib/${LUAJIT_LIBDIR}/luajit
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)

            execute_process(COMMAND ${CMAKE_COMMAND} -E copy ${LJLIBNAME} ../lib/${LUAJIT_LIBDIR}/${LJLIBNAME}
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)

            # Clean 
            execute_process(COMMAND make clean
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)

            message(STATUS "Successfully built LuaJIT for MacOS/${LJARCH}")
        endif ()
    elseif (MSVC)
        set(LJCOMPILE cl /MD /nologo /c /O2 /W3 /D_CRT_SECURE_NO_DEPRECATE "/D_CRT_STDIO_INLINE=__declspec(dllexport)__inline") # NOTE: Add /MD because we need it !
        set(LJLINK link /nologo)
        set(LJMT mt /nologo)
        set(LJLIB lib /nologo /nodefaultlib)
        set(DASMDIR ../dynasm)
        set(DASM ${DASMDIR}/dynasm.lua)
        set(LJDLLNAME lua51.dll)
        set(LJLIBNAME lua51.lib)
        set(ALL_LIB lib_base.c lib_math.c lib_bit.c lib_string.c lib_table.c lib_io.c lib_os.c lib_package.c lib_debug.c lib_jit.c lib_ffi.c)

        if (DEFINED $ENV{VSWHERE})
            set(VSWHERE $ENV{VSWHERE})
        else ()
            set(VSWHERE "$ENV{ProgramFiles(x86)}\\Microsoft Visual Studio\\Installer\\vswhere.exe")
        endif ()
        
        execute_process(COMMAND ${VSWHERE} -latest -products * -requires Microsoft.Component.MSBuild -property installationPath
            OUTPUT_VARIABLE VSINSTALL_DIR OUTPUT_STRIP_TRAILING_WHITESPACE)

        if (DEFINED VSINSTALL_DIR)
            set(VCVARS64 "${VSINSTALL_DIR}\\VC\\Auxiliary\\Build\\vcvars64.bat")
            # Prevent vcvarsxx.bat call from changing the current working directory
            set(ENV{VSCMD_START_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/src)
        elseif (DEFINED ENV{VS140COMNTOOLS})
            set(VCVARS64 "$ENV{VS140COMNTOOLS}..\\..\\VC\\bin\\amd64\\vcvars64.bat")
        else ()
            message(FATAL_ERROR "Not found vcvars64.bat")
        endif ()

        # Compile minilua
        execute_process(COMMAND ${VCVARS64} && ${LJCOMPILE} host/minilua.c && ${LJLINK} /out:minilua.exe minilua.obj
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/src/minilua.exe.manifest")
            execute_process(COMMAND ${VCVARS64} && ${LJMT} -manifest minilua.exe.manifest -outputresource:minilua.exe
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)
        endif ()

        # Generate buildvm_arch.h using minilua
        set(DASMFLAGS -D WIN -D JIT -D FFI -D P64)
        set(LJARCH x64)

        execute_process(COMMAND minilua
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        execute_process(COMMAND minilua ${DASM} -LN ${DASMFLAGS} -o host/buildvm_arch.h vm_x86.dasc
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        # Compile buildvm
        execute_process(COMMAND ${VCVARS64} && ${LJCOMPILE} /I "." /I ${DASMDIR} host/buildvm*.c && ${LJLINK} /out:buildvm.exe buildvm*.obj
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/src/buildvm.exe.manifest")
            execute_process(COMMAND ${VCVARS64} && ${LJMT} -manifest buildvm.exe.manifest -outputresource:buildvm.exe
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)
        endif ()

        # Generate luaJIT header files using buildvm
        execute_process(COMMAND buildvm -m peobj -o lj_vm.obj
            COMMAND buildvm -m bcdef -o lj_bcdef.h ${ALL_LIB}
            COMMAND buildvm -m ffdef -o lj_ffdef.h ${ALL_LIB}
            COMMAND buildvm -m libdef -o lj_libdef.h ${ALL_LIB}
            COMMAND buildvm -m recdef -o lj_recdef.h ${ALL_LIB}
            COMMAND buildvm -m vmdef -o jit/vmdef.lua ${ALL_LIB}
            COMMAND buildvm -m folddef -o lj_folddef.h lj_opt_fold.c
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        # Compile library
        if (STATIC_LIB)
            set(LUAJIT_LIB_OPTIONS /OUT:${LJLIBNAME})
        else ()
            set(LUAJIT_COMPILE_OPTIONS /DLUA_BUILD_AS_DLL)
            set(LUAJIT_LIB_OPTIONS /DLL /OUT:${LJDLLNAME})
        endif ()

        execute_process(COMMAND ${VCVARS64} && ${LJCOMPILE} ${LUAJIT_COMPILE_OPTIONS} lj_*.c lib_*.c && ${LJLIB} ${LUAJIT_LIB_OPTIONS} lj_*.obj lib_*.obj
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        # Compile interpreter executable
        execute_process(COMMAND ${VCVARS64} && ${LJCOMPILE} luajit.c && ${LJLINK} /out:luajit.exe luajit.obj ${LJLIBNAME}
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/src/luajit.exe.manifest")
            execute_process(COMMAND ${VCVARS64} && ${LJMT} -manifest luajit.exe.manifest -outputresource:luajit.exe
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)
        endif ()

        # Remove intermediate files
        file(GLOB OBJ_FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.obj)
        file(GLOB EXP_FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.exp)
        file(GLOB MANIFEST_FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.manifest)
    
        execute_process(COMMAND ${CMAKE_COMMAND} -E remove ${OBJ_FILES} ${EXP_FILES} ${MANIFEST_FILES} minilua.exe buildvm.exe host/buildvm_arch.h lj_bcdef.h lj_ffdef.h lj_libdef.h lj_recdef.h lj_folddef.h jit/vmdef.lua
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        # Copy library and interpreter executable to lib folder
        file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../lib/${LUAJIT_LIBDIR})

        execute_process(COMMAND ${CMAKE_COMMAND} -E copy luajit.exe ../lib/${LUAJIT_LIBDIR}/luajit.exe
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
            RESULT_VARIABLE EXIT_CODE)

        if (STATIC_LIB)
            execute_process(COMMAND ${CMAKE_COMMAND} -E copy ${LJLIBNAME} ../lib/${LUAJIT_LIBDIR}/${LJLIBNAME}
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)
        else ()
            execute_process(COMMAND ${CMAKE_COMMAND} -E copy ${LJDLLNAME} ../lib/${LUAJIT_LIBDIR}/${LJDLLNAME}
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
                RESULT_VARIABLE EXIT_CODE)
        endif ()

        message(STATUS "Successfully built LuaJIT for Windows/${LJARCH}")
    endif ()
endif ()
README for LuaJIT 2.0.5
-----------------------

LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language.

Project Homepage: http://luajit.org/

LuaJIT is Copyright (C) 2005-2017 Mike Pall.
LuaJIT is free software, released under the MIT license.
See full Copyright Notice in the COPYRIGHT file or in luajit.h.

Documentation for LuaJIT is available in HTML format.
Please point your favorite browser to:

 doc/luajit.html

The files in this directory are only used during the build process of LuaJIT.
For cross-compilation, they must be executed on the host, not on the target.

These files should NOT be installed!
cmake_minimum_required(VERSION 2.8.12)

project(luasocket)

set(SRC_FILES
    luasocket.c
    luasocket.h
    timeout.c
    timeout.h
    buffer.c
    buffer.h
    io.c
    io.h
    auxiliar.c
    auxiliar.h
    compat.c
    compat.h
    options.c
    options.h
    inet.c
    inet.h
    except.c
    except.h
    select.c
    select.h
    tcp.c
    tcp.h
    udp.c
    udp.h
    mime.c
    mime.h
    socket.h
)

if (WIN32 AND NOT ANDROID)
    list(APPEND SRC_FILES
        wsocket.c
        wsocket.h)
elseif (UNIX)
    list(APPEND SRC_FILES
        usocket.c
        usocket.h
        unixstream.c
        unixstream.h
        unixdgram.c
        unixdgram.h
        unix.c
        unix.h
        #serial.c
        )
endif ()
    
if (USE_LUAJIT)
    include_directories(${ENGINE_INCLUDE_DIR}/ThirdParty/luaJIT/src)
else ()
    include_directories(${ENGINE_INCLUDE_DIR}/ThirdParty/lua)
endif ()

#set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DLUASOCKET_DEBUG")

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

if (WIN32 AND NOT ANDROID)
    target_link_libraries(${PROJECT_NAME} "wsock32")
elseif (APPLE)
    if (NOT IOS)
        target_link_libraries(${PROJECT_NAME} "-undefined dynamic_lookup")
    endif ()

    set_target_properties(${PROJECT_NAME} PROPERTIES 
        COMPILE_FLAGS "-fno-common")
    add_definitions("-DUNIX_HAS_SUN_LEN")
endif ()

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

project(mikktspace)

set(SRC_FILES
    mikktspace.h
    mikktspace.c)

auto_source_group(${SRC_FILES})

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

project(minizip)

set(SRC_FILES
  ioapi.h
  unzip.h
  zip.h
  ioapi.c
  unzip.c
  zip.c
)

add_definitions(-DUSE_FILE32API)

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_link_libraries(${PROJECT_NAME} zlib)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

MiniZip 1.1 was derrived from MiniZip at version 1.01f

Change in 1.0 (Okt 2009)
 - **TODO - Add history**

MiniZip - Copyright (c) 1998-2010 - by Gilles Vollant - version 1.1 64 bits from Mathias Svensson

Introduction
---------------------
MiniZip 1.1 is built from MiniZip 1.0 by Gilles Vollant ( http://www.winimage.com/zLibDll/minizip.html )

When adding ZIP64 support into minizip it would result into risk of breaking compatibility with minizip 1.0.
All possible work was done for compatibility.


Background
---------------------
When adding ZIP64 support Mathias Svensson found that Even Rouault have added ZIP64 
support for unzip.c into minizip for a open source project called gdal ( http://www.gdal.org/ )

That was used as a starting point. And after that ZIP64 support was added to zip.c
some refactoring and code cleanup was also done.


Changed from MiniZip 1.0 to MiniZip 1.1
---------------------------------------
* Added ZIP64 support for unzip ( by Even Rouault )
* Added ZIP64 support for zip ( by Mathias Svensson )
* Reverted some changed that Even Rouault did.
* Bunch of patches received from Gulles Vollant that he received for MiniZip from various users.
* Added unzip patch for BZIP Compression method (patch create by Daniel Borca)
* Added BZIP Compress method for zip
* Did some refactoring and code cleanup


Credits

 Gilles Vollant    - Original MiniZip author
 Even Rouault      - ZIP64 unzip Support
 Daniel Borca      - BZip Compression method support in unzip
 Mathias Svensson  - ZIP64 zip support
 Mathias Svensson  - BZip Compression method support in zip

 Resources

 ZipLayout   http://result42.com/projects/ZipFileLayout
             Command line tool for Windows that shows the layout and information of the headers in a zip archive.
             Used when debugging and validating the creation of zip files using MiniZip64


 ZIP App Note  http://www.pkware.com/documents/casestudies/APPNOTE.TXT
               Zip File specification


Notes.
 * To be able to use BZip compression method in zip64.c or unzip64.c the BZIP2 lib is needed and HAVE_BZIP2 need to be defined.

License
----------------------------------------------------------
   Condition of use and distribution are the same than zlib :

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

----------------------------------------------------------

cmake_minimum_required(VERSION 2.8.12)

project(NvTriStrip)

set(SRC_FILES
    include/NvTriStrip.h
    src/NvTriStrip/NvTriStrip.cpp
    src/NvTriStrip/NvTriStripObjects.h
    src/NvTriStrip/NvTriStripObjects.cpp
    src/NvTriStrip/VertexCache.h
    src/NvTriStrip/VertexCache.cpp
)

auto_source_group(${SRC_FILES})

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

target_include_directories(${PROJECT_NAME} 
    PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
README for NvTriStrip, library version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use: 
-#include "NvTriStrip.h"
-put nvtristrip.lib in your library path (the pragma in nvtristrip.h will automatically look for the library).

Check out NvTriStrip.h for the interface.

See the StripTest source code (in function LoadXFileStripped) for an example of using the library.

Features:
-generates strips from arbitrary geometry.
-flexibly optimizes for post TnL vertex caches (16 on GeForce1/2, 24 on GeForce3).
-can stitch together strips using degenerate triangles, or not.
-can output lists instead of strips.
-can optionally throw excessively small strips into a list instead.
-can remap indices to improve spatial locality in your vertex buffers.

On cache sizes:
Note that it's better to UNDERESTIMATE the cache size instead of OVERESTIMATING.
So, if you're targetting GeForce1, 2, and 3, be conservative and use the GeForce1_2 cache 
size, NOT the GeForce3 cache size.
This will make sure you don't "blow" the cache of the GeForce1 and 2.
Also note that the cache size you specify is the "actual" cache size, not the "effective"
cache size you may have heard about.  This is 16 for GeForce1 and 2, and 24 for GeForce3.

Credit goes to Curtis Beeson and Joe Demers for the basis for this stripifier and to Jason Regier and 
Jon Stone at Blizzard for providing a much cleaner version of CreateStrips().

Questions/comments email cem@nvidia.com

cmake_minimum_required(VERSION 2.8.12)

project(tinyxml2)

set(SRC_FILES
	tinyxml2.h
	tinyxml2.cpp
)

auto_source_group(${SRC_FILES})

add_library(${PROJECT_NAME} STATIC ${SRC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
cmake_minimum_required(VERSION 2.8.12)

if (DEFINED ENV{QT_DIR})
  set(ENV{PATH} "$ENV{PATH};$ENV{QT_DIR}/bin")
  set(CMAKE_PREFIX_PATH "$ENV{QT_DIR} ${CMAKE_PREFIX_PATH}")
endif()

project(ToolWindowManager)

set(SOURCES 
    ToolWindowManager.cpp
    ToolWindowManagerArea.cpp
    ToolWindowManagerSplitter.cpp
    ToolWindowManagerTabBar.cpp
    ToolWindowManagerWrapper.cpp
)

set(HEADERS
    ToolWindowManager.h
    ToolWindowManagerArea.h
    ToolWindowManagerSplitter.h
    ToolWindowManagerTabBar.h
    ToolWindowManagerWrapper.h
)

set(MOC_SOURCES ${HEADERS})

find_package(Qt5Core)
find_package(Qt5Widgets)

qt5_wrap_cpp(OUT_MOC_FILES ${MOC_SOURCES})

add_library(${PROJECT_NAME} STATIC ${SOURCES} ${HEADERS} ${OUT_MOC_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})

target_link_libraries(${PROJECT_NAME} Qt5::Core Qt5::Gui Qt5::Widgets)

target_include_directories(${PROJECT_NAME} 
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
)
cmake_minimum_required(VERSION 2.4.4)
set(CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS ON)

project(zlib C)

set(VERSION "1.2.8")

option(ASM686 "Enable building i686 assembly implementation")
option(AMD64 "Enable building amd64 assembly implementation")

include(CheckTypeSize)
include(CheckFunctionExists)
include(CheckIncludeFile)
include(CheckCSourceCompiles)
enable_testing()

check_include_file(sys/types.h HAVE_SYS_TYPES_H)
check_include_file(stdint.h    HAVE_STDINT_H)
check_include_file(stddef.h    HAVE_STDDEF_H)

#
# Check to see if we have large file support
#
set(CMAKE_REQUIRED_DEFINITIONS -D_LARGEFILE64_SOURCE=1)
# We add these other definitions here because CheckTypeSize.cmake
# in CMake 2.4.x does not automatically do so and we want
# compatibility with CMake 2.4.x.
if(HAVE_SYS_TYPES_H)
    list(APPEND CMAKE_REQUIRED_DEFINITIONS -DHAVE_SYS_TYPES_H)
endif()
if(HAVE_STDINT_H)
    list(APPEND CMAKE_REQUIRED_DEFINITIONS -DHAVE_STDINT_H)
endif()
if(HAVE_STDDEF_H)
    list(APPEND CMAKE_REQUIRED_DEFINITIONS -DHAVE_STDDEF_H)
endif()

check_type_size(off64_t OFF64_T)
if(HAVE_OFF64_T)
   add_definitions(-D_LARGEFILE64_SOURCE=1)
endif()
set(CMAKE_REQUIRED_DEFINITIONS) # clear variable

#
# Check for fseeko
#
check_function_exists(fseeko HAVE_FSEEKO)
if(NOT HAVE_FSEEKO)
    add_definitions(-DNO_FSEEKO)
endif()

#
# Check for unistd.h
#
check_include_file(unistd.h Z_HAVE_UNISTD_H)

# Force to add definition Z_HAVE_UNISTD_H for iOS
if (IOS)
  add_definitions(-DZ_HAVE_UNISTD_H=1)
endif ()

if(MSVC)
    add_definitions(-D_CRT_SECURE_NO_DEPRECATE)
    add_definitions(-D_CRT_NONSTDC_NO_DEPRECATE)
    include_directories(${CMAKE_CURRENT_SOURCE_DIR})
endif()

if(NOT CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_CURRENT_BINARY_DIR)
    # If we're doing an out of source build and the user has a zconf.h
    # in their source tree...
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h)
        message(STATUS "Renaming")
        message(STATUS "    ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h")
        message(STATUS "to 'zconf.h.included' because this file is included with zlib")
        message(STATUS "but CMake generates it automatically in the build directory.")
        file(RENAME ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h ${CMAKE_CURRENT_SOURCE_DIR}/zconf.h.included)
  endif()
endif()

set(ZLIB_PC ${CMAKE_CURRENT_BINARY_DIR}/zlib.pc)

configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/zlib.pc.cmakein ${ZLIB_PC} @ONLY)
configure_file(	${CMAKE_CURRENT_SOURCE_DIR}/zconf.h.cmakein ${CMAKE_CURRENT_BINARY_DIR}/zconf.h @ONLY)

include_directories(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_SOURCE_DIR})


#============================================================================
# zlib
#============================================================================

set(ZLIB_PUBLIC_HDRS
    ${CMAKE_CURRENT_BINARY_DIR}/zconf.h
    zlib.h
)
set(ZLIB_PRIVATE_HDRS
    crc32.h
    deflate.h
    gzguts.h
    inffast.h
    inffixed.h
    inflate.h
    inftrees.h
    trees.h
    zutil.h
)
set(ZLIB_SRCS
    adler32.c
    compress.c
    crc32.c
    deflate.c
    gzclose.c
    gzlib.c
    gzread.c
    gzwrite.c
    inflate.c
    infback.c
    inftrees.c
    inffast.c
    trees.c
    uncompr.c
    zutil.c
)

if(NOT MINGW)
    set(ZLIB_DLL_SRCS
        win32/zlib1.rc # If present will override custom build rule below.
    )
endif()

if(CMAKE_COMPILER_IS_GNUCC)
    if(ASM686)
        set(ZLIB_ASMS contrib/asm686/match.S)
    elseif (AMD64)
        set(ZLIB_ASMS contrib/amd64/amd64-match.S)
    endif ()

	if(ZLIB_ASMS)
		add_definitions(-DASMV)
		set_source_files_properties(${ZLIB_ASMS} PROPERTIES LANGUAGE C COMPILE_FLAGS -DNO_UNDERLINE)
	endif()
endif()

if(MSVC)
    if(ASM686)
		ENABLE_LANGUAGE(ASM_MASM)
        set(ZLIB_ASMS
			contrib/masmx86/inffas32.asm
			contrib/masmx86/match686.asm
		)
    elseif (AMD64)
		ENABLE_LANGUAGE(ASM_MASM)
        set(ZLIB_ASMS
			contrib/masmx64/gvmat64.asm
			contrib/masmx64/inffasx64.asm
		)
    endif()

	if(ZLIB_ASMS)
		add_definitions(-DASMV -DASMINF)
	endif()
endif()

# parse the full version number from zlib.h and include in ZLIB_FULL_VERSION
file(READ ${CMAKE_CURRENT_SOURCE_DIR}/zlib.h _zlib_h_contents)
string(REGEX REPLACE ".*#define[ \t]+ZLIB_VERSION[ \t]+\"([-0-9A-Za-z.]+)\".*"
    "\\1" ZLIB_FULL_VERSION ${_zlib_h_contents})

if(MINGW)
    # This gets us DLL resource information when compiling on MinGW.
    if(NOT CMAKE_RC_COMPILER)
        set(CMAKE_RC_COMPILER windres.exe)
    endif()

    add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/zlib1rc.obj
                       COMMAND ${CMAKE_RC_COMPILER}
                            -D GCC_WINDRES
                            -I ${CMAKE_CURRENT_SOURCE_DIR}
                            -I ${CMAKE_CURRENT_BINARY_DIR}
                            -o ${CMAKE_CURRENT_BINARY_DIR}/zlib1rc.obj
                            -i ${CMAKE_CURRENT_SOURCE_DIR}/win32/zlib1.rc)
    set(ZLIB_DLL_SRCS ${CMAKE_CURRENT_BINARY_DIR}/zlib1rc.obj)
endif(MINGW)

add_library(${PROJECT_NAME} STATIC ${ZLIB_SRCS} ${ZLIB_ASMS} ${ZLIB_PUBLIC_HDRS} ${ZLIB_PRIVATE_HDRS})

if(UNIX)
    # On unix-like platforms the library is almost always called libz
   set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME z)
endif()

target_include_directories(${PROJECT_NAME}
    PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
    PUBLIC $<BUILD_INTERFACE:${PROJECT_BINARY_DIR}>)

set_target_properties(${PROJECT_NAME} PROPERTIES 
    FOLDER ThirdParty
    PREFIX ""
    #DEBUG_POSTFIX "_d"
    OUTPUT_NAME ${PROJECT_NAME}
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Library/${ENGINE_BUILD_PLATFORM_DIR})
ZLIB DATA COMPRESSION LIBRARY

zlib 1.2.8 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://tools.ietf.org/html/rfc1950 (zlib format), rfc1951 (deflate format) and
rfc1952 (gzip format).

All functions of the compression library are documented in the file zlib.h
(volunteer to write man pages welcome, contact zlib@gzip.org).  A usage example
of the library is given in the file test/example.c which also tests that
the library is working correctly.  Another example is given in the file
test/minigzip.c.  The compression library itself is composed of all source
files in the root directory.

To compile all files and run the test program, follow the instructions given at
the top of Makefile.in.  In short "./configure; make test", and if that goes
well, "make install" should work for most flavors of Unix.  For Windows, use
one of the special makefiles in win32/ or contrib/vstudio/ .  For VMS, use
make_vms.com.

Questions about zlib should be sent to <zlib@gzip.org>, or to Gilles Vollant
<info@winimage.com> for the Windows DLL version.  The zlib home page is
http://zlib.net/ .  Before reporting a problem, please check this site to
verify that you have the latest version of zlib; otherwise get the latest
version and check whether the problem still exists or not.

PLEASE read the zlib FAQ http://zlib.net/zlib_faq.html before asking for help.

Mark Nelson <markn@ieee.org> wrote an article about zlib for the Jan.  1997
issue of Dr.  Dobb's Journal; a copy of the article is available at
http://marknelson.us/1997/01/01/zlib-engine/ .

The changes made in version 1.2.8 are documented in the file ChangeLog.

Unsupported third party contributions are provided in directory contrib/ .

zlib is available in Java using the java.util.zip package, documented at
http://java.sun.com/developer/technicalArticles/Programming/compression/ .

A Perl interface to zlib written by Paul Marquess <pmqs@cpan.org> is available
at CPAN (Comprehensive Perl Archive Network) sites, including
http://search.cpan.org/~pmqs/IO-Compress-Zlib/ .

A Python interface to zlib written by A.M. Kuchling <amk@amk.ca> is
available in Python 1.5 and later versions, see
http://docs.python.org/library/zlib.html .

zlib is built into tcl: http://wiki.tcl.tk/4610 .

An experimental package to read and write files in .zip format, written on top
of zlib by Gilles Vollant <info@winimage.com>, is available in the
contrib/minizip directory of zlib.


Notes for some targets:

- For Windows DLL versions, please see win32/DLL_FAQ.txt

- For 64-bit Irix, deflate.c must be compiled without any optimization. With
  -O, one libpng test fails. The test works in 32 bit mode (with the -n32
  compiler flag). The compiler bug has been reported to SGI.

- zlib doesn't work with gcc 2.6.3 on a DEC 3000/300LX under OSF/1 2.1 it works
  when compiled with cc.

- On Digital Unix 4.0D (formely OSF/1) on AlphaServer, the cc option -std1 is
  necessary to get gzprintf working correctly. This is done by configure.

- zlib doesn't work on HP-UX 9.05 with some versions of /bin/cc. It works with
  other compilers. Use "make test" to check your compiler.

- gzdopen is not supported on RISCOS or BEOS.

- For PalmOs, see http://palmzlib.sourceforge.net/


Acknowledgments:

  The deflate format used by zlib was defined by Phil Katz.  The deflate and
  zlib specifications were written by L.  Peter Deutsch.  Thanks to all the
  people who reported problems and suggested various improvements in zlib; they
  are too numerous to cite here.

Copyright notice:

 (C) 1995-2013 Jean-loup Gailly and Mark Adler

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  Jean-loup Gailly        Mark Adler
  jloup@gzip.org          madler@alumni.caltech.edu

If you use the zlib library in a product, we would appreciate *not* receiving
lengthy legal documents to sign.  The sources are provided for free but without
warranty of any kind.  The library has been entirely written by Jean-loup
Gailly and Mark Adler; it does not include third-party code.

If you redistribute modified sources, we would appreciate that you include in
the file ChangeLog history information documenting your changes.  Please read
the FAQ for more information on the distribution of modified source versions.
All files under this contrib directory are UNSUPPORTED. There were
provided by users of zlib and were not tested by the authors of zlib.
Use at your own risk. Please contact the authors of the contributions
for help about these, not the zlib authors. Thanks.


ada/        by Dmitriy Anisimkov <anisimkov@yahoo.com>
        Support for Ada
        See http://zlib-ada.sourceforge.net/

amd64/      by Mikhail Teterin <mi@ALDAN.algebra.com>
        asm code for AMD64
        See patch at http://www.freebsd.org/cgi/query-pr.cgi?pr=bin/96393

asm686/     by Brian Raiter <breadbox@muppetlabs.com>
        asm code for Pentium and PPro/PII, using the AT&T (GNU as) syntax
        See http://www.muppetlabs.com/~breadbox/software/assembly.html

blast/      by Mark Adler <madler@alumni.caltech.edu>
        Decompressor for output of PKWare Data Compression Library (DCL)

delphi/     by Cosmin Truta <cosmint@cs.ubbcluj.ro>
        Support for Delphi and C++ Builder

dotzlib/    by Henrik Ravn <henrik@ravn.com>
        Support for Microsoft .Net and Visual C++ .Net

gcc_gvmat64/by Gilles Vollant <info@winimage.com>
        GCC Version of x86 64-bit (AMD64 and Intel EM64t) code for x64
        assembler to replace longest_match() and inflate_fast()

infback9/   by Mark Adler <madler@alumni.caltech.edu>
        Unsupported diffs to infback to decode the deflate64 format

inflate86/  by Chris Anderson <christop@charm.net>
        Tuned x86 gcc asm code to replace inflate_fast()

iostream/   by Kevin Ruland <kevin@rodin.wustl.edu>
        A C++ I/O streams interface to the zlib gz* functions

iostream2/  by Tyge Lvset <Tyge.Lovset@cmr.no>
        Another C++ I/O streams interface

iostream3/  by Ludwig Schwardt <schwardt@sun.ac.za>
            and Kevin Ruland <kevin@rodin.wustl.edu>
        Yet another C++ I/O streams interface

masmx64/    by Gilles Vollant <info@winimage.com>
        x86 64-bit (AMD64 and Intel EM64t) code for x64 assembler to
        replace longest_match() and inflate_fast(),  also masm x86
        64-bits translation of Chris Anderson inflate_fast()

masmx86/    by Gilles Vollant <info@winimage.com>
        x86 asm code to replace longest_match() and inflate_fast(),
        for Visual C++ and MASM (32 bits).
        Based on Brian Raiter (asm686) and Chris Anderson (inflate86)

minizip/    by Gilles Vollant <info@winimage.com>
        Mini zip and unzip based on zlib
        Includes Zip64 support by Mathias Svensson <mathias@result42.com>
        See http://www.winimage.com/zLibDll/unzip.html

pascal/     by Bob Dellaca <bobdl@xtra.co.nz> et al.
        Support for Pascal

puff/       by Mark Adler <madler@alumni.caltech.edu>
        Small, low memory usage inflate.  Also serves to provide an
        unambiguous description of the deflate format.

testzlib/   by Gilles Vollant <info@winimage.com>
        Example of the use of zlib

untgz/      by Pedro A. Aranda Gutierrez <paag@tid.es>
        A very simple tar.gz file extractor using zlib

vstudio/    by Gilles Vollant <info@winimage.com>
        Building a minizip-enhanced zlib with Microsoft Visual Studio
        Includes vc11 from kreuzerkrieg and vc12 from davispuh
                        ZLib for Ada thick binding (ZLib.Ada)
                        Release 1.3

ZLib.Ada is a thick binding interface to the popular ZLib data
compression library, available at http://www.gzip.org/zlib/.
It provides Ada-style access to the ZLib C library.


        Here are the main changes since ZLib.Ada 1.2:

- Attension: ZLib.Read generic routine have a initialization requirement
  for Read_Last parameter now. It is a bit incompartible with previous version,
  but extends functionality, we could use new parameters Allow_Read_Some and
  Flush now.

- Added Is_Open routines to ZLib and ZLib.Streams packages.

- Add pragma Assert to check Stream_Element is 8 bit.

- Fix extraction to buffer with exact known decompressed size. Error reported by
  Steve Sangwine.

- Fix definition of ULong (changed to unsigned_long), fix regression on 64 bits
  computers. Patch provided by Pascal Obry.

- Add Status_Error exception definition.

- Add pragma Assertion that Ada.Streams.Stream_Element size is 8 bit.


        How to build ZLib.Ada under GNAT

You should have the ZLib library already build on your computer, before
building ZLib.Ada. Make the directory of ZLib.Ada sources current and
issue the command:

  gnatmake test -largs -L<directory where libz.a is> -lz

Or use the GNAT project file build for GNAT 3.15 or later:

  gnatmake -Pzlib.gpr -L<directory where libz.a is>


        How to build ZLib.Ada under Aonix ObjectAda for Win32 7.2.2

1. Make a project with all *.ads and *.adb files from the distribution.
2. Build the libz.a library from the ZLib C sources.
3. Rename libz.a to z.lib.
4. Add the library z.lib to the project.
5. Add the libc.lib library from the ObjectAda distribution to the project.
6. Build the executable using test.adb as a main procedure.


        How to use ZLib.Ada

The source files test.adb and read.adb are small demo programs that show
the main functionality of ZLib.Ada.

The routines from the package specifications are commented.


Homepage: http://zlib-ada.sourceforge.net/
Author: Dmitriy Anisimkov <anisimkov@yahoo.com>

Contributors: Pascal Obry <pascal@obry.org>, Steve Sangwine <sjs@essex.ac.uk>
This is a patched version of zlib, modified to use
Pentium-Pro-optimized assembly code in the deflation algorithm. The
files changed/added by this patch are:

README.686
match.S

The speedup that this patch provides varies, depending on whether the
compiler used to build the original version of zlib falls afoul of the
PPro's speed traps. My own tests show a speedup of around 10-20% at
the default compression level, and 20-30% using -9, against a version
compiled using gcc 2.7.2.3. Your mileage may vary.

Note that this code has been tailored for the PPro/PII in particular,
and will not perform particuarly well on a Pentium.

If you are using an assembler other than GNU as, you will have to
translate match.S to use your assembler's syntax. (Have fun.)

Brian Raiter
breadbox@muppetlabs.com
April, 1998


Added for zlib 1.1.3:

The patches come from
http://www.muppetlabs.com/~breadbox/software/assembly.html

To compile zlib with this asm file, copy match.S to the zlib directory
then do:

CFLAGS="-O3 -DASMV" ./configure
make OBJA=match.o


Update:

I've been ignoring these assembly routines for years, believing that
gcc's generated code had caught up with it sometime around gcc 2.95
and the major rearchitecting of the Pentium 4. However, I recently
learned that, despite what I believed, this code still has some life
in it. On the Pentium 4 and AMD64 chips, it continues to run about 8%
faster than the code produced by gcc 4.1.

In acknowledgement of its continuing usefulness, I've altered the
license to match that of the rest of zlib. Share and Enjoy!

Brian Raiter
breadbox@muppetlabs.com
April, 2007
Read blast.h for purpose and usage.

Mark Adler
madler@alumni.caltech.edu
AIAIAIAIAIAIA
Overview
========

This directory contains an update to the ZLib interface unit,
distributed by Borland as a Delphi supplemental component.

The original ZLib unit is Copyright (c) 1997,99 Borland Corp.,
and is based on zlib version 1.0.4.  There are a series of bugs
and security problems associated with that old zlib version, and
we recommend the users to update their ZLib unit.


Summary of modifications
========================

- Improved makefile, adapted to zlib version 1.2.1.

- Some field types from TZStreamRec are changed from Integer to
  Longint, for consistency with the zlib.h header, and for 64-bit
  readiness.

- The zlib_version constant is updated.

- The new Z_RLE strategy has its corresponding symbolic constant.

- The allocation and deallocation functions and function types
  (TAlloc, TFree, zlibAllocMem and zlibFreeMem) are now cdecl,
  and _malloc and _free are added as C RTL stubs.  As a result,
  the original C sources of zlib can be compiled out of the box,
  and linked to the ZLib unit.


Suggestions for improvements
============================

Currently, the ZLib unit provides only a limited wrapper around
the zlib library, and much of the original zlib functionality is
missing.  Handling compressed file formats like ZIP/GZIP or PNG
cannot be implemented without having this functionality.
Applications that handle these formats are either using their own,
duplicated code, or not using the ZLib unit at all.

Here are a few suggestions:

- Checksum class wrappers around adler32() and crc32(), similar
  to the Java classes that implement the java.util.zip.Checksum
  interface.

- The ability to read and write raw deflate streams, without the
  zlib stream header and trailer.  Raw deflate streams are used
  in the ZIP file format.

- The ability to read and write gzip streams, used in the GZIP
  file format, and normally produced by the gzip program.

- The ability to select a different compression strategy, useful
  to PNG and MNG image compression, and to multimedia compression
  in general.  Besides the compression level

    TCompressionLevel = (clNone, clFastest, clDefault, clMax);

  which, in fact, could have used the 'z' prefix and avoided
  TColor-like symbols

    TCompressionLevel = (zcNone, zcFastest, zcDefault, zcMax);

  there could be a compression strategy

    TCompressionStrategy = (zsDefault, zsFiltered, zsHuffmanOnly, zsRle);

- ZIP and GZIP stream handling via TStreams.


--
Cosmin Truta <cosmint@cs.ubbcluj.ro>
Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.This directory contains a .Net wrapper class library for the ZLib1.dll

The wrapper includes support for inflating/deflating memory buffers,
.Net streaming wrappers for the gz streams part of zlib, and wrappers
for the checksum parts of zlib. See DotZLib/UnitTests.cs for examples.

Directory structure:
--------------------

LICENSE_1_0.txt       - License file.
readme.txt            - This file.
DotZLib.chm           - Class library documentation
DotZLib.build         - NAnt build file
DotZLib.sln           - Microsoft Visual Studio 2003 solution file

DotZLib\*.cs          - Source files for the class library

Unit tests:
-----------
The file DotZLib/UnitTests.cs contains unit tests for use with NUnit 2.1 or higher.
To include unit tests in the build, define nunit before building.


Build instructions:
-------------------

1. Using Visual Studio.Net 2003:
   Open DotZLib.sln in VS.Net and build from there. Output file (DotZLib.dll)
   will be found ./DotZLib/bin/release or ./DotZLib/bin/debug, depending on
   you are building the release or debug version of the library. Check
   DotZLib/UnitTests.cs for instructions on how to include unit tests in the
   build.

2. Using NAnt:
   Open a command prompt with access to the build environment and run nant
   in the same directory as the DotZLib.build file.
   You can define 2 properties on the nant command-line to control the build:
   debug={true|false} to toggle between release/debug builds (default=true).
   nunit={true|false} to include or esclude unit tests (default=true).
   Also the target clean will remove binaries.
   Output file (DotZLib.dll) will be found in either ./DotZLib/bin/release
   or ./DotZLib/bin/debug, depending on whether you are building the release
   or debug version of the library.

   Examples:
     nant -D:debug=false -D:nunit=false
       will build a release mode version of the library without unit tests.
     nant
       will build a debug version of the library with unit tests
     nant clean
       will remove all previously built files.


---------------------------------
Copyright (c) Henrik Ravn 2004

Use, modification and distribution are subject to the Boost Software License, Version 1.0.
(See accompanying file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
See infback9.h for what this is and how to use it.
These classes provide a C++ stream interface to the zlib library. It allows you
to do things like:

  gzofstream outf("blah.gz");
  outf << "These go into the gzip file " << 123 << endl;

It does this by deriving a specialized stream buffer for gzipped files, which is
the way Stroustrup would have done it. :->

The gzifstream and gzofstream classes were originally written by Kevin Ruland
and made available in the zlib contrib/iostream directory. The older version still
compiles under gcc 2.xx, but not under gcc 3.xx, which sparked the development of
this version.

The new classes are as standard-compliant as possible, closely following the
approach of the standard library's fstream classes. It compiles under gcc versions
3.2 and 3.3, but not under gcc 2.xx. This is mainly due to changes in the standard
library naming scheme. The new version of gzifstream/gzofstream/gzfilebuf differs
from the previous one in the following respects:
- added showmanyc
- added setbuf, with support for unbuffered output via setbuf(0,0)
- a few bug fixes of stream behavior
- gzipped output file opened with default compression level instead of maximum level
- setcompressionlevel()/strategy() members replaced by single setcompression()

The code is provided "as is", with the permission to use, copy, modify, distribute
and sell it for any purpose without fee.

Ludwig Schwardt
<schwardt@sun.ac.za>

DSP Lab
Electrical & Electronic Engineering Department
University of Stellenbosch
South Africa
Summary
-------
This directory contains ASM implementations of the functions
longest_match() and inflate_fast(), for 64 bits x86 (both AMD64 and Intel EM64t),
for use with Microsoft Macro Assembler (x64) for AMD64 and Microsoft C++ 64 bits.

gvmat64.asm is written by Gilles Vollant (2005), by using Brian Raiter 686/32 bits
   assembly optimized version from Jean-loup Gailly original longest_match function

inffasx64.asm and inffas8664.c were written by Chris Anderson, by optimizing
   original function from Mark Adler

Use instructions
----------------
Assemble the .asm files using MASM and put the object files into the zlib source
directory.  You can also get object files here:

     http://www.winimage.com/zLibDll/zlib124_masm_obj.zip

define ASMV and ASMINF in your project. Include inffas8664.c in your source tree,
and inffasx64.obj and gvmat64.obj as object to link.


Build instructions
------------------
run bld_64.bat with Microsoft Macro Assembler (x64) for AMD64 (ml64.exe)

ml64.exe is given with Visual Studio 2005, Windows 2003 server DDK

You can get Windows 2003 server DDK with ml64 and cl for AMD64 from
  http://www.microsoft.com/whdc/devtools/ddk/default.mspx for low price)

Summary
-------
This directory contains ASM implementations of the functions
longest_match() and inflate_fast().


Use instructions
----------------
Assemble using MASM, and copy the object files into the zlib source
directory, then run the appropriate makefile, as suggested below.  You can
donwload MASM from here:

    http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7a1c9da0-0510-44a2-b042-7ef370530c64

You can also get objects files here:

    http://www.winimage.com/zLibDll/zlib124_masm_obj.zip

Build instructions
------------------
* With Microsoft C and MASM:
nmake -f win32/Makefile.msc LOC="-DASMV -DASMINF" OBJA="match686.obj inffas32.obj"

* With Borland C and TASM:
make -f win32/Makefile.bor LOCAL_ZLIB="-DASMV -DASMINF" OBJA="match686.obj inffas32.obj" OBJPA="+match686c.obj+match686.obj+inffas32.obj"


MiniZip 1.1 was derrived from MiniZip at version 1.01f

Change in 1.0 (Okt 2009)
 - **TODO - Add history**

MiniZip - Copyright (c) 1998-2010 - by Gilles Vollant - version 1.1 64 bits from Mathias Svensson

Introduction
---------------------
MiniZip 1.1 is built from MiniZip 1.0 by Gilles Vollant ( http://www.winimage.com/zLibDll/minizip.html )

When adding ZIP64 support into minizip it would result into risk of breaking compatibility with minizip 1.0.
All possible work was done for compatibility.


Background
---------------------
When adding ZIP64 support Mathias Svensson found that Even Rouault have added ZIP64 
support for unzip.c into minizip for a open source project called gdal ( http://www.gdal.org/ )

That was used as a starting point. And after that ZIP64 support was added to zip.c
some refactoring and code cleanup was also done.


Changed from MiniZip 1.0 to MiniZip 1.1
---------------------------------------
* Added ZIP64 support for unzip ( by Even Rouault )
* Added ZIP64 support for zip ( by Mathias Svensson )
* Reverted some changed that Even Rouault did.
* Bunch of patches received from Gulles Vollant that he received for MiniZip from various users.
* Added unzip patch for BZIP Compression method (patch create by Daniel Borca)
* Added BZIP Compress method for zip
* Did some refactoring and code cleanup


Credits

 Gilles Vollant    - Original MiniZip author
 Even Rouault      - ZIP64 unzip Support
 Daniel Borca      - BZip Compression method support in unzip
 Mathias Svensson  - ZIP64 zip support
 Mathias Svensson  - BZip Compression method support in zip

 Resources

 ZipLayout   http://result42.com/projects/ZipFileLayout
             Command line tool for Windows that shows the layout and information of the headers in a zip archive.
             Used when debugging and validating the creation of zip files using MiniZip64


 ZIP App Note  http://www.pkware.com/documents/casestudies/APPNOTE.TXT
               Zip File specification


Notes.
 * To be able to use BZip compression method in zip64.c or unzip64.c the BZIP2 lib is needed and HAVE_BZIP2 need to be defined.

License
----------------------------------------------------------
   Condition of use and distribution are the same than zlib :

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

----------------------------------------------------------


This directory contains a Pascal (Delphi, Kylix) interface to the
zlib data compression library.


Directory listing
=================

zlibd32.mak     makefile for Borland C++
example.pas     usage example of zlib
zlibpas.pas     the Pascal interface to zlib
readme.txt      this file


Compatibility notes
===================

- Although the name "zlib" would have been more normal for the
  zlibpas unit, this name is already taken by Borland's ZLib unit.
  This is somehow unfortunate, because that unit is not a genuine
  interface to the full-fledged zlib functionality, but a suite of
  class wrappers around zlib streams.  Other essential features,
  such as checksums, are missing.
  It would have been more appropriate for that unit to have a name
  like "ZStreams", or something similar.

- The C and zlib-supplied types int, uInt, long, uLong, etc. are
  translated directly into Pascal types of similar sizes (Integer,
  LongInt, etc.), to avoid namespace pollution.  In particular,
  there is no conversion of unsigned int into a Pascal unsigned
  integer.  The Word type is non-portable and has the same size
  (16 bits) both in a 16-bit and in a 32-bit environment, unlike
  Integer.  Even if there is a 32-bit Cardinal type, there is no
  real need for unsigned int in zlib under a 32-bit environment.

- Except for the callbacks, the zlib function interfaces are
  assuming the calling convention normally used in Pascal
  (__pascal for DOS and Windows16, __fastcall for Windows32).
  Since the cdecl keyword is used, the old Turbo Pascal does
  not work with this interface.

- The gz* function interfaces are not translated, to avoid
  interfacing problems with the C runtime library.  Besides,
    gzprintf(gzFile file, const char *format, ...)
  cannot be translated into Pascal.


Legal issues
============

The zlibpas interface is:
  Copyright (C) 1995-2003 Jean-loup Gailly and Mark Adler.
  Copyright (C) 1998 by Bob Dellaca.
  Copyright (C) 2003 by Cosmin Truta.

The example program is:
  Copyright (C) 1995-2003 by Jean-loup Gailly.
  Copyright (C) 1998,1999,2000 by Jacques Nomssi Nzali.
  Copyright (C) 2003 by Cosmin Truta.

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the author be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

Puff -- A Simple Inflate
3 Mar 2003
Mark Adler
madler@alumni.caltech.edu

What this is --

puff.c provides the routine puff() to decompress the deflate data format.  It
does so more slowly than zlib, but the code is about one-fifth the size of the
inflate code in zlib, and written to be very easy to read.

Why I wrote this --

puff.c was written to document the deflate format unambiguously, by virtue of
being working C code.  It is meant to supplement RFC 1951, which formally
describes the deflate format.  I have received many questions on details of the
deflate format, and I hope that reading this code will answer those questions.
puff.c is heavily commented with details of the deflate format, especially
those little nooks and cranies of the format that might not be obvious from a
specification.

puff.c may also be useful in applications where code size or memory usage is a
very limited resource, and speed is not as important.

How to use it --

Well, most likely you should just be reading puff.c and using zlib for actual
applications, but if you must ...

Include puff.h in your code, which provides this prototype:

int puff(unsigned char *dest,           /* pointer to destination pointer */
         unsigned long *destlen,        /* amount of output space */
         unsigned char *source,         /* pointer to source data pointer */
         unsigned long *sourcelen);     /* amount of input available */

Then you can call puff() to decompress a deflate stream that is in memory in
its entirety at source, to a sufficiently sized block of memory for the
decompressed data at dest.  puff() is the only external symbol in puff.c  The
only C library functions that puff.c needs are setjmp() and longjmp(), which
are used to simplify error checking in the code to improve readabilty.  puff.c
does no memory allocation, and uses less than 2K bytes off of the stack.

If destlen is not enough space for the uncompressed data, then inflate will
return an error without writing more than destlen bytes.  Note that this means
that in order to decompress the deflate data successfully, you need to know
the size of the uncompressed data ahead of time.

If needed, puff() can determine the size of the uncompressed data with no
output space.  This is done by passing dest equal to (unsigned char *)0.  Then
the initial value of *destlen is ignored and *destlen is set to the length of
the uncompressed data.  So if the size of the uncompressed data is not known,
then two passes of puff() can be used--first to determine the size, and second
to do the actual inflation after allocating the appropriate memory.  Not
pretty, but it works.  (This is one of the reasons you should be using zlib.)

The deflate format is self-terminating.  If the deflate stream does not end
in *sourcelen bytes, puff() will return an error without reading at or past
endsource.

On return, *sourcelen is updated to the amount of input data consumed, and
*destlen is updated to the size of the uncompressed data.  See the comments
in puff.c for the possible return codes for puff().
To build testzLib with Visual Studio 2005:

copy to a directory file from :
- root of zLib tree
- contrib/testzlib
- contrib/masmx86
- contrib/masmx64
- contrib/vstudio/vc7

and open testzlib8.slnBuilding instructions for the DLL versions of Zlib 1.2.8
========================================================

This directory contains projects that build zlib and minizip using
Microsoft Visual C++ 9.0/10.0.

You don't need to build these projects yourself. You can download the
binaries from:
  http://www.winimage.com/zLibDll

More information can be found at this site.





Build instructions for Visual Studio 2008 (32 bits or 64 bits)
--------------------------------------------------------------
- Uncompress current zlib, including all contrib/* files
- Compile assembly code (with Visual Studio Command Prompt) by running:
   bld_ml64.bat (in contrib\masmx64)
   bld_ml32.bat (in contrib\masmx86)
- Open contrib\vstudio\vc9\zlibvc.sln with Microsoft Visual C++ 2008
- Or run: vcbuild /rebuild contrib\vstudio\vc9\zlibvc.sln "Release|Win32"

Build instructions for Visual Studio 2010 (32 bits or 64 bits)
--------------------------------------------------------------
- Uncompress current zlib, including all contrib/* files
- Open contrib\vstudio\vc10\zlibvc.sln with Microsoft Visual C++ 2010

Build instructions for Visual Studio 2012 (32 bits or 64 bits)
--------------------------------------------------------------
- Uncompress current zlib, including all contrib/* files
- Open contrib\vstudio\vc11\zlibvc.sln with Microsoft Visual C++ 2012


Important
---------
- To use zlibwapi.dll in your application, you must define the
  macro ZLIB_WINAPI when compiling your application's source files.


Additional notes
----------------
- This DLL, named zlibwapi.dll, is compatible to the old zlib.dll built
  by Gilles Vollant from the zlib 1.1.x sources, and distributed at
    http://www.winimage.com/zLibDll
  It uses the WINAPI calling convention for the exported functions, and
  includes the minizip functionality. If your application needs that
  particular build of zlib.dll, you can rename zlibwapi.dll to zlib.dll.

- The new DLL was renamed because there exist several incompatible
  versions of zlib.dll on the Internet.

- There is also an official DLL build of zlib, named zlib1.dll. This one
  is exporting the functions using the CDECL convention. See the file
  win32\DLL_FAQ.txt found in this zlib distribution.

- There used to be a ZLIB_DLL macro in zlib 1.1.x, but now this symbol
  has a slightly different effect. To avoid compatibility problems, do
  not define it here.


Gilles Vollant
info@winimage.com
1. Compression algorithm (deflate)

The deflation algorithm used by gzip (also zip and zlib) is a variation of
LZ77 (Lempel-Ziv 1977, see reference below). It finds duplicated strings in
the input data.  The second occurrence of a string is replaced by a
pointer to the previous string, in the form of a pair (distance,
length).  Distances are limited to 32K bytes, and lengths are limited
to 258 bytes. When a string does not occur anywhere in the previous
32K bytes, it is emitted as a sequence of literal bytes.  (In this
description, `string' must be taken as an arbitrary sequence of bytes,
and is not restricted to printable characters.)

Literals or match lengths are compressed with one Huffman tree, and
match distances are compressed with another tree. The trees are stored
in a compact form at the start of each block. The blocks can have any
size (except that the compressed data for one block must fit in
available memory). A block is terminated when deflate() determines that
it would be useful to start another block with fresh trees. (This is
somewhat similar to the behavior of LZW-based _compress_.)

Duplicated strings are found using a hash table. All input strings of
length 3 are inserted in the hash table. A hash index is computed for
the next 3 bytes. If the hash chain for this index is not empty, all
strings in the chain are compared with the current input string, and
the longest match is selected.

The hash chains are searched starting with the most recent strings, to
favor small distances and thus take advantage of the Huffman encoding.
The hash chains are singly linked. There are no deletions from the
hash chains, the algorithm simply discards matches that are too old.

To avoid a worst-case situation, very long hash chains are arbitrarily
truncated at a certain length, determined by a runtime option (level
parameter of deflateInit). So deflate() does not always find the longest
possible match but generally finds a match which is long enough.

deflate() also defers the selection of matches with a lazy evaluation
mechanism. After a match of length N has been found, deflate() searches for
a longer match at the next input byte. If a longer match is found, the
previous match is truncated to a length of one (thus producing a single
literal byte) and the process of lazy evaluation begins again. Otherwise,
the original match is kept, and the next match search is attempted only N
steps later.

The lazy match evaluation is also subject to a runtime parameter. If
the current match is long enough, deflate() reduces the search for a longer
match, thus speeding up the whole process. If compression ratio is more
important than speed, deflate() attempts a complete second search even if
the first match is already long enough.

The lazy match evaluation is not performed for the fastest compression
modes (level parameter 1 to 3). For these fast modes, new strings
are inserted in the hash table only when no match was found, or
when the match is not too long. This degrades the compression ratio
but saves time since there are both fewer insertions and fewer searches.


2. Decompression algorithm (inflate)

2.1 Introduction

The key question is how to represent a Huffman code (or any prefix code) so
that you can decode fast.  The most important characteristic is that shorter
codes are much more common than longer codes, so pay attention to decoding the
short codes fast, and let the long codes take longer to decode.

inflate() sets up a first level table that covers some number of bits of
input less than the length of longest code.  It gets that many bits from the
stream, and looks it up in the table.  The table will tell if the next
code is that many bits or less and how many, and if it is, it will tell
the value, else it will point to the next level table for which inflate()
grabs more bits and tries to decode a longer code.

How many bits to make the first lookup is a tradeoff between the time it
takes to decode and the time it takes to build the table.  If building the
table took no time (and if you had infinite memory), then there would only
be a first level table to cover all the way to the longest code.  However,
building the table ends up taking a lot longer for more bits since short
codes are replicated many times in such a table.  What inflate() does is
simply to make the number of bits in the first table a variable, and  then
to set that variable for the maximum speed.

For inflate, which has 286 possible codes for the literal/length tree, the size
of the first table is nine bits.  Also the distance trees have 30 possible
values, and the size of the first table is six bits.  Note that for each of
those cases, the table ended up one bit longer than the ``average'' code
length, i.e. the code length of an approximately flat code which would be a
little more than eight bits for 286 symbols and a little less than five bits
for 30 symbols.


2.2 More details on the inflate table lookup

Ok, you want to know what this cleverly obfuscated inflate tree actually
looks like.  You are correct that it's not a Huffman tree.  It is simply a
lookup table for the first, let's say, nine bits of a Huffman symbol.  The
symbol could be as short as one bit or as long as 15 bits.  If a particular
symbol is shorter than nine bits, then that symbol's translation is duplicated
in all those entries that start with that symbol's bits.  For example, if the
symbol is four bits, then it's duplicated 32 times in a nine-bit table.  If a
symbol is nine bits long, it appears in the table once.

If the symbol is longer than nine bits, then that entry in the table points
to another similar table for the remaining bits.  Again, there are duplicated
entries as needed.  The idea is that most of the time the symbol will be short
and there will only be one table look up.  (That's whole idea behind data
compression in the first place.)  For the less frequent long symbols, there
will be two lookups.  If you had a compression method with really long
symbols, you could have as many levels of lookups as is efficient.  For
inflate, two is enough.

So a table entry either points to another table (in which case nine bits in
the above example are gobbled), or it contains the translation for the symbol
and the number of bits to gobble.  Then you start again with the next
ungobbled bit.

You may wonder: why not just have one lookup table for how ever many bits the
longest symbol is?  The reason is that if you do that, you end up spending
more time filling in duplicate symbol entries than you do actually decoding.
At least for deflate's output that generates new trees every several 10's of
kbytes.  You can imagine that filling in a 2^15 entry table for a 15-bit code
would take too long if you're only decoding several thousand symbols.  At the
other extreme, you could make a new table for every bit in the code.  In fact,
that's essentially a Huffman tree.  But then you spend too much time
traversing the tree while decoding, even for short symbols.

So the number of bits for the first lookup table is a trade of the time to
fill out the table vs. the time spent looking at the second level and above of
the table.

Here is an example, scaled down:

The code being decoded, with 10 symbols, from 1 to 6 bits long:

A: 0
B: 10
C: 1100
D: 11010
E: 11011
F: 11100
G: 11101
H: 11110
I: 111110
J: 111111

Let's make the first table three bits long (eight entries):

000: A,1
001: A,1
010: A,1
011: A,1
100: B,2
101: B,2
110: -> table X (gobble 3 bits)
111: -> table Y (gobble 3 bits)

Each entry is what the bits decode as and how many bits that is, i.e. how
many bits to gobble.  Or the entry points to another table, with the number of
bits to gobble implicit in the size of the table.

Table X is two bits long since the longest code starting with 110 is five bits
long:

00: C,1
01: C,1
10: D,2
11: E,2

Table Y is three bits long since the longest code starting with 111 is six
bits long:

000: F,2
001: F,2
010: G,2
011: G,2
100: H,2
101: H,2
110: I,3
111: J,3

So what we have here are three tables with a total of 20 entries that had to
be constructed.  That's compared to 64 entries for a single table.  Or
compared to 16 entries for a Huffman tree (six two entry tables and one four
entry table).  Assuming that the code ideally represents the probability of
the symbols, it takes on the average 1.25 lookups per symbol.  That's compared
to one lookup for the single table, or 1.66 lookups per symbol for the
Huffman tree.

There, I think that gives you a picture of what's going on.  For inflate, the
meaning of a particular symbol is often more than just a letter.  It can be a
byte (a "literal"), or it can be either a length or a distance which
indicates a base value and a number of bits to fetch after the code that is
added to the base value.  Or it might be the special end-of-block code.  The
data structures created in inftrees.c try to encode all that information
compactly in the tables.


Jean-loup Gailly        Mark Adler
jloup@gzip.org          madler@alumni.caltech.edu


References:

[LZ77] Ziv J., Lempel A., ``A Universal Algorithm for Sequential Data
Compression,'' IEEE Transactions on Information Theory, Vol. 23, No. 3,
pp. 337-343.

``DEFLATE Compressed Data Format Specification'' available in
http://tools.ietf.org/html/rfc1951






Network Working Group                                         P. Deutsch
Request for Comments: 1950                           Aladdin Enterprises
Category: Informational                                      J-L. Gailly
                                                                Info-ZIP
                                                                May 1996


         ZLIB Compressed Data Format Specification version 3.3

Status of This Memo

   This memo provides information for the Internet community.  This memo
   does not specify an Internet standard of any kind.  Distribution of
   this memo is unlimited.

IESG Note:

   The IESG takes no position on the validity of any Intellectual
   Property Rights statements contained in this document.

Notices

   Copyright (c) 1996 L. Peter Deutsch and Jean-Loup Gailly

   Permission is granted to copy and distribute this document for any
   purpose and without charge, including translations into other
   languages and incorporation into compilations, provided that the
   copyright notice and this notice are preserved, and that any
   substantive changes or deletions from the original are clearly
   marked.

   A pointer to the latest version of this and related documentation in
   HTML format can be found at the URL
   <ftp://ftp.uu.net/graphics/png/documents/zlib/zdoc-index.html>.

Abstract

   This specification defines a lossless compressed data format.  The
   data can be produced or consumed, even for an arbitrarily long
   sequentially presented input data stream, using only an a priori
   bounded amount of intermediate storage.  The format presently uses
   the DEFLATE compression method but can be easily extended to use
   other compression methods.  It can be implemented readily in a manner
   not covered by patents.  This specification also defines the ADLER-32
   checksum (an extension and improvement of the Fletcher checksum),
   used for detection of data corruption, and provides an algorithm for
   computing it.




Deutsch & Gailly             Informational                      [Page 1]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


Table of Contents

   1. Introduction ................................................... 2
      1.1. Purpose ................................................... 2
      1.2. Intended audience ......................................... 3
      1.3. Scope ..................................................... 3
      1.4. Compliance ................................................ 3
      1.5.  Definitions of terms and conventions used ................ 3
      1.6. Changes from previous versions ............................ 3
   2. Detailed specification ......................................... 3
      2.1. Overall conventions ....................................... 3
      2.2. Data format ............................................... 4
      2.3. Compliance ................................................ 7
   3. References ..................................................... 7
   4. Source code .................................................... 8
   5. Security Considerations ........................................ 8
   6. Acknowledgements ............................................... 8
   7. Authors' Addresses ............................................. 8
   8. Appendix: Rationale ............................................ 9
   9. Appendix: Sample code ..........................................10

1. Introduction

   1.1. Purpose

      The purpose of this specification is to define a lossless
      compressed data format that:

          * Is independent of CPU type, operating system, file system,
            and character set, and hence can be used for interchange;

          * Can be produced or consumed, even for an arbitrarily long
            sequentially presented input data stream, using only an a
            priori bounded amount of intermediate storage, and hence can
            be used in data communications or similar structures such as
            Unix filters;

          * Can use a number of different compression methods;

          * Can be implemented readily in a manner not covered by
            patents, and hence can be practiced freely.

      The data format defined by this specification does not attempt to
      allow random access to compressed data.







Deutsch & Gailly             Informational                      [Page 2]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


   1.2. Intended audience

      This specification is intended for use by implementors of software
      to compress data into zlib format and/or decompress data from zlib
      format.

      The text of the specification assumes a basic background in
      programming at the level of bits and other primitive data
      representations.

   1.3. Scope

      The specification specifies a compressed data format that can be
      used for in-memory compression of a sequence of arbitrary bytes.

   1.4. Compliance

      Unless otherwise indicated below, a compliant decompressor must be
      able to accept and decompress any data set that conforms to all
      the specifications presented here; a compliant compressor must
      produce data sets that conform to all the specifications presented
      here.

   1.5.  Definitions of terms and conventions used

      byte: 8 bits stored or transmitted as a unit (same as an octet).
      (For this specification, a byte is exactly 8 bits, even on
      machines which store a character on a number of bits different
      from 8.) See below, for the numbering of bits within a byte.

   1.6. Changes from previous versions

      Version 3.1 was the first public release of this specification.
      In version 3.2, some terminology was changed and the Adler-32
      sample code was rewritten for clarity.  In version 3.3, the
      support for a preset dictionary was introduced, and the
      specification was converted to RFC style.

2. Detailed specification

   2.1. Overall conventions

      In the diagrams below, a box like this:

         +---+
         |   | <-- the vertical bars might be missing
         +---+




Deutsch & Gailly             Informational                      [Page 3]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


      represents one byte; a box like this:

         +==============+
         |              |
         +==============+

      represents a variable number of bytes.

      Bytes stored within a computer do not have a "bit order", since
      they are always treated as a unit.  However, a byte considered as
      an integer between 0 and 255 does have a most- and least-
      significant bit, and since we write numbers with the most-
      significant digit on the left, we also write bytes with the most-
      significant bit on the left.  In the diagrams below, we number the
      bits of a byte so that bit 0 is the least-significant bit, i.e.,
      the bits are numbered:

         +--------+
         |76543210|
         +--------+

      Within a computer, a number may occupy multiple bytes.  All
      multi-byte numbers in the format described here are stored with
      the MOST-significant byte first (at the lower memory address).
      For example, the decimal number 520 is stored as:

             0     1
         +--------+--------+
         |00000010|00001000|
         +--------+--------+
          ^        ^
          |        |
          |        + less significant byte = 8
          + more significant byte = 2 x 256

   2.2. Data format

      A zlib stream has the following structure:

           0   1
         +---+---+
         |CMF|FLG|   (more-->)
         +---+---+








Deutsch & Gailly             Informational                      [Page 4]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


      (if FLG.FDICT set)

           0   1   2   3
         +---+---+---+---+
         |     DICTID    |   (more-->)
         +---+---+---+---+

         +=====================+---+---+---+---+
         |...compressed data...|    ADLER32    |
         +=====================+---+---+---+---+

      Any data which may appear after ADLER32 are not part of the zlib
      stream.

      CMF (Compression Method and flags)
         This byte is divided into a 4-bit compression method and a 4-
         bit information field depending on the compression method.

            bits 0 to 3  CM     Compression method
            bits 4 to 7  CINFO  Compression info

      CM (Compression method)
         This identifies the compression method used in the file. CM = 8
         denotes the "deflate" compression method with a window size up
         to 32K.  This is the method used by gzip and PNG (see
         references [1] and [2] in Chapter 3, below, for the reference
         documents).  CM = 15 is reserved.  It might be used in a future
         version of this specification to indicate the presence of an
         extra field before the compressed data.

      CINFO (Compression info)
         For CM = 8, CINFO is the base-2 logarithm of the LZ77 window
         size, minus eight (CINFO=7 indicates a 32K window size). Values
         of CINFO above 7 are not allowed in this version of the
         specification.  CINFO is not defined in this specification for
         CM not equal to 8.

      FLG (FLaGs)
         This flag byte is divided as follows:

            bits 0 to 4  FCHECK  (check bits for CMF and FLG)
            bit  5       FDICT   (preset dictionary)
            bits 6 to 7  FLEVEL  (compression level)

         The FCHECK value must be such that CMF and FLG, when viewed as
         a 16-bit unsigned integer stored in MSB order (CMF*256 + FLG),
         is a multiple of 31.




Deutsch & Gailly             Informational                      [Page 5]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


      FDICT (Preset dictionary)
         If FDICT is set, a DICT dictionary identifier is present
         immediately after the FLG byte. The dictionary is a sequence of
         bytes which are initially fed to the compressor without
         producing any compressed output. DICT is the Adler-32 checksum
         of this sequence of bytes (see the definition of ADLER32
         below).  The decompressor can use this identifier to determine
         which dictionary has been used by the compressor.

      FLEVEL (Compression level)
         These flags are available for use by specific compression
         methods.  The "deflate" method (CM = 8) sets these flags as
         follows:

            0 - compressor used fastest algorithm
            1 - compressor used fast algorithm
            2 - compressor used default algorithm
            3 - compressor used maximum compression, slowest algorithm

         The information in FLEVEL is not needed for decompression; it
         is there to indicate if recompression might be worthwhile.

      compressed data
         For compression method 8, the compressed data is stored in the
         deflate compressed data format as described in the document
         "DEFLATE Compressed Data Format Specification" by L. Peter
         Deutsch. (See reference [3] in Chapter 3, below)

         Other compressed data formats are not specified in this version
         of the zlib specification.

      ADLER32 (Adler-32 checksum)
         This contains a checksum value of the uncompressed data
         (excluding any dictionary data) computed according to Adler-32
         algorithm. This algorithm is a 32-bit extension and improvement
         of the Fletcher algorithm, used in the ITU-T X.224 / ISO 8073
         standard. See references [4] and [5] in Chapter 3, below)

         Adler-32 is composed of two sums accumulated per byte: s1 is
         the sum of all bytes, s2 is the sum of all s1 values. Both sums
         are done modulo 65521. s1 is initialized to 1, s2 to zero.  The
         Adler-32 checksum is stored as s2*65536 + s1 in most-
         significant-byte first (network) order.








Deutsch & Gailly             Informational                      [Page 6]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


   2.3. Compliance

      A compliant compressor must produce streams with correct CMF, FLG
      and ADLER32, but need not support preset dictionaries.  When the
      zlib data format is used as part of another standard data format,
      the compressor may use only preset dictionaries that are specified
      by this other data format.  If this other format does not use the
      preset dictionary feature, the compressor must not set the FDICT
      flag.

      A compliant decompressor must check CMF, FLG, and ADLER32, and
      provide an error indication if any of these have incorrect values.
      A compliant decompressor must give an error indication if CM is
      not one of the values defined in this specification (only the
      value 8 is permitted in this version), since another value could
      indicate the presence of new features that would cause subsequent
      data to be interpreted incorrectly.  A compliant decompressor must
      give an error indication if FDICT is set and DICTID is not the
      identifier of a known preset dictionary.  A decompressor may
      ignore FLEVEL and still be compliant.  When the zlib data format
      is being used as a part of another standard format, a compliant
      decompressor must support all the preset dictionaries specified by
      the other format. When the other format does not use the preset
      dictionary feature, a compliant decompressor must reject any
      stream in which the FDICT flag is set.

3. References

   [1] Deutsch, L.P.,"GZIP Compressed Data Format Specification",
       available in ftp://ftp.uu.net/pub/archiving/zip/doc/

   [2] Thomas Boutell, "PNG (Portable Network Graphics) specification",
       available in ftp://ftp.uu.net/graphics/png/documents/

   [3] Deutsch, L.P.,"DEFLATE Compressed Data Format Specification",
       available in ftp://ftp.uu.net/pub/archiving/zip/doc/

   [4] Fletcher, J. G., "An Arithmetic Checksum for Serial
       Transmissions," IEEE Transactions on Communications, Vol. COM-30,
       No. 1, January 1982, pp. 247-252.

   [5] ITU-T Recommendation X.224, Annex D, "Checksum Algorithms,"
       November, 1993, pp. 144, 145. (Available from
       gopher://info.itu.ch). ITU-T X.244 is also the same as ISO 8073.







Deutsch & Gailly             Informational                      [Page 7]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


4. Source code

   Source code for a C language implementation of a "zlib" compliant
   library is available at ftp://ftp.uu.net/pub/archiving/zip/zlib/.

5. Security Considerations

   A decoder that fails to check the ADLER32 checksum value may be
   subject to undetected data corruption.

6. Acknowledgements

   Trademarks cited in this document are the property of their
   respective owners.

   Jean-Loup Gailly and Mark Adler designed the zlib format and wrote
   the related software described in this specification.  Glenn
   Randers-Pehrson converted this document to RFC and HTML format.

7. Authors' Addresses

   L. Peter Deutsch
   Aladdin Enterprises
   203 Santa Margarita Ave.
   Menlo Park, CA 94025

   Phone: (415) 322-0103 (AM only)
   FAX:   (415) 322-1734
   EMail: <ghost@aladdin.com>


   Jean-Loup Gailly

   EMail: <gzip@prep.ai.mit.edu>

   Questions about the technical content of this specification can be
   sent by email to

   Jean-Loup Gailly <gzip@prep.ai.mit.edu> and
   Mark Adler <madler@alumni.caltech.edu>

   Editorial comments on this specification can be sent by email to

   L. Peter Deutsch <ghost@aladdin.com> and
   Glenn Randers-Pehrson <randeg@alumni.rpi.edu>






Deutsch & Gailly             Informational                      [Page 8]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


8. Appendix: Rationale

   8.1. Preset dictionaries

      A preset dictionary is specially useful to compress short input
      sequences. The compressor can take advantage of the dictionary
      context to encode the input in a more compact manner. The
      decompressor can be initialized with the appropriate context by
      virtually decompressing a compressed version of the dictionary
      without producing any output. However for certain compression
      algorithms such as the deflate algorithm this operation can be
      achieved without actually performing any decompression.

      The compressor and the decompressor must use exactly the same
      dictionary. The dictionary may be fixed or may be chosen among a
      certain number of predefined dictionaries, according to the kind
      of input data. The decompressor can determine which dictionary has
      been chosen by the compressor by checking the dictionary
      identifier. This document does not specify the contents of
      predefined dictionaries, since the optimal dictionaries are
      application specific. Standard data formats using this feature of
      the zlib specification must precisely define the allowed
      dictionaries.

   8.2. The Adler-32 algorithm

      The Adler-32 algorithm is much faster than the CRC32 algorithm yet
      still provides an extremely low probability of undetected errors.

      The modulo on unsigned long accumulators can be delayed for 5552
      bytes, so the modulo operation time is negligible.  If the bytes
      are a, b, c, the second sum is 3a + 2b + c + 3, and so is position
      and order sensitive, unlike the first sum, which is just a
      checksum.  That 65521 is prime is important to avoid a possible
      large class of two-byte errors that leave the check unchanged.
      (The Fletcher checksum uses 255, which is not prime and which also
      makes the Fletcher check insensitive to single byte changes 0 <->
      255.)

      The sum s1 is initialized to 1 instead of zero to make the length
      of the sequence part of s2, so that the length does not have to be
      checked separately. (Any sequence of zeroes has a Fletcher
      checksum of zero.)








Deutsch & Gailly             Informational                      [Page 9]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


9. Appendix: Sample code

   The following C code computes the Adler-32 checksum of a data buffer.
   It is written for clarity, not for speed.  The sample code is in the
   ANSI C programming language. Non C users may find it easier to read
   with these hints:

      &      Bitwise AND operator.
      >>     Bitwise right shift operator. When applied to an
             unsigned quantity, as here, right shift inserts zero bit(s)
             at the left.
      <<     Bitwise left shift operator. Left shift inserts zero
             bit(s) at the right.
      ++     "n++" increments the variable n.
      %      modulo operator: a % b is the remainder of a divided by b.

      #define BASE 65521 /* largest prime smaller than 65536 */

      /*
         Update a running Adler-32 checksum with the bytes buf[0..len-1]
       and return the updated checksum. The Adler-32 checksum should be
       initialized to 1.

       Usage example:

         unsigned long adler = 1L;

         while (read_buffer(buffer, length) != EOF) {
           adler = update_adler32(adler, buffer, length);
         }
         if (adler != original_adler) error();
      */
      unsigned long update_adler32(unsigned long adler,
         unsigned char *buf, int len)
      {
        unsigned long s1 = adler & 0xffff;
        unsigned long s2 = (adler >> 16) & 0xffff;
        int n;

        for (n = 0; n < len; n++) {
          s1 = (s1 + buf[n]) % BASE;
          s2 = (s2 + s1)     % BASE;
        }
        return (s2 << 16) + s1;
      }

      /* Return the adler32 of the bytes buf[0..len-1] */




Deutsch & Gailly             Informational                     [Page 10]

RFC 1950       ZLIB Compressed Data Format Specification        May 1996


      unsigned long adler32(unsigned char *buf, int len)
      {
        return update_adler32(1L, buf, len);
      }















































Deutsch & Gailly             Informational                     [Page 11]







Network Working Group                                         P. Deutsch
Request for Comments: 1951                           Aladdin Enterprises
Category: Informational                                         May 1996


        DEFLATE Compressed Data Format Specification version 1.3

Status of This Memo

   This memo provides information for the Internet community.  This memo
   does not specify an Internet standard of any kind.  Distribution of
   this memo is unlimited.

IESG Note:

   The IESG takes no position on the validity of any Intellectual
   Property Rights statements contained in this document.

Notices

   Copyright (c) 1996 L. Peter Deutsch

   Permission is granted to copy and distribute this document for any
   purpose and without charge, including translations into other
   languages and incorporation into compilations, provided that the
   copyright notice and this notice are preserved, and that any
   substantive changes or deletions from the original are clearly
   marked.

   A pointer to the latest version of this and related documentation in
   HTML format can be found at the URL
   <ftp://ftp.uu.net/graphics/png/documents/zlib/zdoc-index.html>.

Abstract

   This specification defines a lossless compressed data format that
   compresses data using a combination of the LZ77 algorithm and Huffman
   coding, with efficiency comparable to the best currently available
   general-purpose compression methods.  The data can be produced or
   consumed, even for an arbitrarily long sequentially presented input
   data stream, using only an a priori bounded amount of intermediate
   storage.  The format can be implemented readily in a manner not
   covered by patents.








Deutsch                      Informational                      [Page 1]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


Table of Contents

   1. Introduction ................................................... 2
      1.1. Purpose ................................................... 2
      1.2. Intended audience ......................................... 3
      1.3. Scope ..................................................... 3
      1.4. Compliance ................................................ 3
      1.5.  Definitions of terms and conventions used ................ 3
      1.6. Changes from previous versions ............................ 4
   2. Compressed representation overview ............................. 4
   3. Detailed specification ......................................... 5
      3.1. Overall conventions ....................................... 5
          3.1.1. Packing into bytes .................................. 5
      3.2. Compressed block format ................................... 6
          3.2.1. Synopsis of prefix and Huffman coding ............... 6
          3.2.2. Use of Huffman coding in the "deflate" format ....... 7
          3.2.3. Details of block format ............................. 9
          3.2.4. Non-compressed blocks (BTYPE=00) ................... 11
          3.2.5. Compressed blocks (length and distance codes) ...... 11
          3.2.6. Compression with fixed Huffman codes (BTYPE=01) .... 12
          3.2.7. Compression with dynamic Huffman codes (BTYPE=10) .. 13
      3.3. Compliance ............................................... 14
   4. Compression algorithm details ................................. 14
   5. References .................................................... 16
   6. Security Considerations ....................................... 16
   7. Source code ................................................... 16
   8. Acknowledgements .............................................. 16
   9. Author's Address .............................................. 17

1. Introduction

   1.1. Purpose

      The purpose of this specification is to define a lossless
      compressed data format that:
          * Is independent of CPU type, operating system, file system,
            and character set, and hence can be used for interchange;
          * Can be produced or consumed, even for an arbitrarily long
            sequentially presented input data stream, using only an a
            priori bounded amount of intermediate storage, and hence
            can be used in data communications or similar structures
            such as Unix filters;
          * Compresses data with efficiency comparable to the best
            currently available general-purpose compression methods,
            and in particular considerably better than the "compress"
            program;
          * Can be implemented readily in a manner not covered by
            patents, and hence can be practiced freely;



Deutsch                      Informational                      [Page 2]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


          * Is compatible with the file format produced by the current
            widely used gzip utility, in that conforming decompressors
            will be able to read data produced by the existing gzip
            compressor.

      The data format defined by this specification does not attempt to:

          * Allow random access to compressed data;
          * Compress specialized data (e.g., raster graphics) as well
            as the best currently available specialized algorithms.

      A simple counting argument shows that no lossless compression
      algorithm can compress every possible input data set.  For the
      format defined here, the worst case expansion is 5 bytes per 32K-
      byte block, i.e., a size increase of 0.015% for large data sets.
      English text usually compresses by a factor of 2.5 to 3;
      executable files usually compress somewhat less; graphical data
      such as raster images may compress much more.

   1.2. Intended audience

      This specification is intended for use by implementors of software
      to compress data into "deflate" format and/or decompress data from
      "deflate" format.

      The text of the specification assumes a basic background in
      programming at the level of bits and other primitive data
      representations.  Familiarity with the technique of Huffman coding
      is helpful but not required.

   1.3. Scope

      The specification specifies a method for representing a sequence
      of bytes as a (usually shorter) sequence of bits, and a method for
      packing the latter bit sequence into bytes.

   1.4. Compliance

      Unless otherwise indicated below, a compliant decompressor must be
      able to accept and decompress any data set that conforms to all
      the specifications presented here; a compliant compressor must
      produce data sets that conform to all the specifications presented
      here.

   1.5.  Definitions of terms and conventions used

      Byte: 8 bits stored or transmitted as a unit (same as an octet).
      For this specification, a byte is exactly 8 bits, even on machines



Deutsch                      Informational                      [Page 3]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


      which store a character on a number of bits different from eight.
      See below, for the numbering of bits within a byte.

      String: a sequence of arbitrary bytes.

   1.6. Changes from previous versions

      There have been no technical changes to the deflate format since
      version 1.1 of this specification.  In version 1.2, some
      terminology was changed.  Version 1.3 is a conversion of the
      specification to RFC style.

2. Compressed representation overview

   A compressed data set consists of a series of blocks, corresponding
   to successive blocks of input data.  The block sizes are arbitrary,
   except that non-compressible blocks are limited to 65,535 bytes.

   Each block is compressed using a combination of the LZ77 algorithm
   and Huffman coding. The Huffman trees for each block are independent
   of those for previous or subsequent blocks; the LZ77 algorithm may
   use a reference to a duplicated string occurring in a previous block,
   up to 32K input bytes before.

   Each block consists of two parts: a pair of Huffman code trees that
   describe the representation of the compressed data part, and a
   compressed data part.  (The Huffman trees themselves are compressed
   using Huffman encoding.)  The compressed data consists of a series of
   elements of two types: literal bytes (of strings that have not been
   detected as duplicated within the previous 32K input bytes), and
   pointers to duplicated strings, where a pointer is represented as a
   pair <length, backward distance>.  The representation used in the
   "deflate" format limits distances to 32K bytes and lengths to 258
   bytes, but does not limit the size of a block, except for
   uncompressible blocks, which are limited as noted above.

   Each type of value (literals, distances, and lengths) in the
   compressed data is represented using a Huffman code, using one code
   tree for literals and lengths and a separate code tree for distances.
   The code trees for each block appear in a compact form just before
   the compressed data for that block.










Deutsch                      Informational                      [Page 4]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


3. Detailed specification

   3.1. Overall conventions In the diagrams below, a box like this:

         +---+
         |   | <-- the vertical bars might be missing
         +---+

      represents one byte; a box like this:

         +==============+
         |              |
         +==============+

      represents a variable number of bytes.

      Bytes stored within a computer do not have a "bit order", since
      they are always treated as a unit.  However, a byte considered as
      an integer between 0 and 255 does have a most- and least-
      significant bit, and since we write numbers with the most-
      significant digit on the left, we also write bytes with the most-
      significant bit on the left.  In the diagrams below, we number the
      bits of a byte so that bit 0 is the least-significant bit, i.e.,
      the bits are numbered:

         +--------+
         |76543210|
         +--------+

      Within a computer, a number may occupy multiple bytes.  All
      multi-byte numbers in the format described here are stored with
      the least-significant byte first (at the lower memory address).
      For example, the decimal number 520 is stored as:

             0        1
         +--------+--------+
         |00001000|00000010|
         +--------+--------+
          ^        ^
          |        |
          |        + more significant byte = 2 x 256
          + less significant byte = 8

      3.1.1. Packing into bytes

         This document does not address the issue of the order in which
         bits of a byte are transmitted on a bit-sequential medium,
         since the final data format described here is byte- rather than



Deutsch                      Informational                      [Page 5]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


         bit-oriented.  However, we describe the compressed block format
         in below, as a sequence of data elements of various bit
         lengths, not a sequence of bytes.  We must therefore specify
         how to pack these data elements into bytes to form the final
         compressed byte sequence:

             * Data elements are packed into bytes in order of
               increasing bit number within the byte, i.e., starting
               with the least-significant bit of the byte.
             * Data elements other than Huffman codes are packed
               starting with the least-significant bit of the data
               element.
             * Huffman codes are packed starting with the most-
               significant bit of the code.

         In other words, if one were to print out the compressed data as
         a sequence of bytes, starting with the first byte at the
         *right* margin and proceeding to the *left*, with the most-
         significant bit of each byte on the left as usual, one would be
         able to parse the result from right to left, with fixed-width
         elements in the correct MSB-to-LSB order and Huffman codes in
         bit-reversed order (i.e., with the first bit of the code in the
         relative LSB position).

   3.2. Compressed block format

      3.2.1. Synopsis of prefix and Huffman coding

         Prefix coding represents symbols from an a priori known
         alphabet by bit sequences (codes), one code for each symbol, in
         a manner such that different symbols may be represented by bit
         sequences of different lengths, but a parser can always parse
         an encoded string unambiguously symbol-by-symbol.

         We define a prefix code in terms of a binary tree in which the
         two edges descending from each non-leaf node are labeled 0 and
         1 and in which the leaf nodes correspond one-for-one with (are
         labeled with) the symbols of the alphabet; then the code for a
         symbol is the sequence of 0's and 1's on the edges leading from
         the root to the leaf labeled with that symbol.  For example:











Deutsch                      Informational                      [Page 6]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


                          /\              Symbol    Code
                         0  1             ------    ----
                        /    \                A      00
                       /\     B               B       1
                      0  1                    C     011
                     /    \                   D     010
                    A     /\
                         0  1
                        /    \
                       D      C

         A parser can decode the next symbol from an encoded input
         stream by walking down the tree from the root, at each step
         choosing the edge corresponding to the next input bit.

         Given an alphabet with known symbol frequencies, the Huffman
         algorithm allows the construction of an optimal prefix code
         (one which represents strings with those symbol frequencies
         using the fewest bits of any possible prefix codes for that
         alphabet).  Such a code is called a Huffman code.  (See
         reference [1] in Chapter 5, references for additional
         information on Huffman codes.)

         Note that in the "deflate" format, the Huffman codes for the
         various alphabets must not exceed certain maximum code lengths.
         This constraint complicates the algorithm for computing code
         lengths from symbol frequencies.  Again, see Chapter 5,
         references for details.

      3.2.2. Use of Huffman coding in the "deflate" format

         The Huffman codes used for each alphabet in the "deflate"
         format have two additional rules:

             * All codes of a given bit length have lexicographically
               consecutive values, in the same order as the symbols
               they represent;

             * Shorter codes lexicographically precede longer codes.












Deutsch                      Informational                      [Page 7]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


         We could recode the example above to follow this rule as
         follows, assuming that the order of the alphabet is ABCD:

            Symbol  Code
            ------  ----
            A       10
            B       0
            C       110
            D       111

         I.e., 0 precedes 10 which precedes 11x, and 110 and 111 are
         lexicographically consecutive.

         Given this rule, we can define the Huffman code for an alphabet
         just by giving the bit lengths of the codes for each symbol of
         the alphabet in order; this is sufficient to determine the
         actual codes.  In our example, the code is completely defined
         by the sequence of bit lengths (2, 1, 3, 3).  The following
         algorithm generates the codes as integers, intended to be read
         from most- to least-significant bit.  The code lengths are
         initially in tree[I].Len; the codes are produced in
         tree[I].Code.

         1)  Count the number of codes for each code length.  Let
             bl_count[N] be the number of codes of length N, N >= 1.

         2)  Find the numerical value of the smallest code for each
             code length:

                code = 0;
                bl_count[0] = 0;
                for (bits = 1; bits <= MAX_BITS; bits++) {
                    code = (code + bl_count[bits-1]) << 1;
                    next_code[bits] = code;
                }

         3)  Assign numerical values to all codes, using consecutive
             values for all codes of the same length with the base
             values determined at step 2. Codes that are never used
             (which have a bit length of zero) must not be assigned a
             value.

                for (n = 0;  n <= max_code; n++) {
                    len = tree[n].Len;
                    if (len != 0) {
                        tree[n].Code = next_code[len];
                        next_code[len]++;
                    }



Deutsch                      Informational                      [Page 8]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


                }

         Example:

         Consider the alphabet ABCDEFGH, with bit lengths (3, 3, 3, 3,
         3, 2, 4, 4).  After step 1, we have:

            N      bl_count[N]
            -      -----------
            2      1
            3      5
            4      2

         Step 2 computes the following next_code values:

            N      next_code[N]
            -      ------------
            1      0
            2      0
            3      2
            4      14

         Step 3 produces the following code values:

            Symbol Length   Code
            ------ ------   ----
            A       3        010
            B       3        011
            C       3        100
            D       3        101
            E       3        110
            F       2         00
            G       4       1110
            H       4       1111

      3.2.3. Details of block format

         Each block of compressed data begins with 3 header bits
         containing the following data:

            first bit       BFINAL
            next 2 bits     BTYPE

         Note that the header bits do not necessarily begin on a byte
         boundary, since a block does not necessarily occupy an integral
         number of bytes.





Deutsch                      Informational                      [Page 9]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


         BFINAL is set if and only if this is the last block of the data
         set.

         BTYPE specifies how the data are compressed, as follows:

            00 - no compression
            01 - compressed with fixed Huffman codes
            10 - compressed with dynamic Huffman codes
            11 - reserved (error)

         The only difference between the two compressed cases is how the
         Huffman codes for the literal/length and distance alphabets are
         defined.

         In all cases, the decoding algorithm for the actual data is as
         follows:

            do
               read block header from input stream.
               if stored with no compression
                  skip any remaining bits in current partially
                     processed byte
                  read LEN and NLEN (see next section)
                  copy LEN bytes of data to output
               otherwise
                  if compressed with dynamic Huffman codes
                     read representation of code trees (see
                        subsection below)
                  loop (until end of block code recognized)
                     decode literal/length value from input stream
                     if value < 256
                        copy value (literal byte) to output stream
                     otherwise
                        if value = end of block (256)
                           break from loop
                        otherwise (value = 257..285)
                           decode distance from input stream

                           move backwards distance bytes in the output
                           stream, and copy length bytes from this
                           position to the output stream.
                  end loop
            while not last block

         Note that a duplicated string reference may refer to a string
         in a previous block; i.e., the backward distance may cross one
         or more block boundaries.  However a distance cannot refer past
         the beginning of the output stream.  (An application using a



Deutsch                      Informational                     [Page 10]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


         preset dictionary might discard part of the output stream; a
         distance can refer to that part of the output stream anyway)
         Note also that the referenced string may overlap the current
         position; for example, if the last 2 bytes decoded have values
         X and Y, a string reference with <length = 5, distance = 2>
         adds X,Y,X,Y,X to the output stream.

         We now specify each compression method in turn.

      3.2.4. Non-compressed blocks (BTYPE=00)

         Any bits of input up to the next byte boundary are ignored.
         The rest of the block consists of the following information:

              0   1   2   3   4...
            +---+---+---+---+================================+
            |  LEN  | NLEN  |... LEN bytes of literal data...|
            +---+---+---+---+================================+

         LEN is the number of data bytes in the block.  NLEN is the
         one's complement of LEN.

      3.2.5. Compressed blocks (length and distance codes)

         As noted above, encoded data blocks in the "deflate" format
         consist of sequences of symbols drawn from three conceptually
         distinct alphabets: either literal bytes, from the alphabet of
         byte values (0..255), or <length, backward distance> pairs,
         where the length is drawn from (3..258) and the distance is
         drawn from (1..32,768).  In fact, the literal and length
         alphabets are merged into a single alphabet (0..285), where
         values 0..255 represent literal bytes, the value 256 indicates
         end-of-block, and values 257..285 represent length codes
         (possibly in conjunction with extra bits following the symbol
         code) as follows:
















Deutsch                      Informational                     [Page 11]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


                 Extra               Extra               Extra
            Code Bits Length(s) Code Bits Lengths   Code Bits Length(s)
            ---- ---- ------     ---- ---- -------   ---- ---- -------
             257   0     3       267   1   15,16     277   4   67-82
             258   0     4       268   1   17,18     278   4   83-98
             259   0     5       269   2   19-22     279   4   99-114
             260   0     6       270   2   23-26     280   4  115-130
             261   0     7       271   2   27-30     281   5  131-162
             262   0     8       272   2   31-34     282   5  163-194
             263   0     9       273   3   35-42     283   5  195-226
             264   0    10       274   3   43-50     284   5  227-257
             265   1  11,12      275   3   51-58     285   0    258
             266   1  13,14      276   3   59-66

         The extra bits should be interpreted as a machine integer
         stored with the most-significant bit first, e.g., bits 1110
         represent the value 14.

                  Extra           Extra               Extra
             Code Bits Dist  Code Bits   Dist     Code Bits Distance
             ---- ---- ----  ---- ----  ------    ---- ---- --------
               0   0    1     10   4     33-48    20    9   1025-1536
               1   0    2     11   4     49-64    21    9   1537-2048
               2   0    3     12   5     65-96    22   10   2049-3072
               3   0    4     13   5     97-128   23   10   3073-4096
               4   1   5,6    14   6    129-192   24   11   4097-6144
               5   1   7,8    15   6    193-256   25   11   6145-8192
               6   2   9-12   16   7    257-384   26   12  8193-12288
               7   2  13-16   17   7    385-512   27   12 12289-16384
               8   3  17-24   18   8    513-768   28   13 16385-24576
               9   3  25-32   19   8   769-1024   29   13 24577-32768

      3.2.6. Compression with fixed Huffman codes (BTYPE=01)

         The Huffman codes for the two alphabets are fixed, and are not
         represented explicitly in the data.  The Huffman code lengths
         for the literal/length alphabet are:

                   Lit Value    Bits        Codes
                   ---------    ----        -----
                     0 - 143     8          00110000 through
                                            10111111
                   144 - 255     9          110010000 through
                                            111111111
                   256 - 279     7          0000000 through
                                            0010111
                   280 - 287     8          11000000 through
                                            11000111



Deutsch                      Informational                     [Page 12]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


         The code lengths are sufficient to generate the actual codes,
         as described above; we show the codes in the table for added
         clarity.  Literal/length values 286-287 will never actually
         occur in the compressed data, but participate in the code
         construction.

         Distance codes 0-31 are represented by (fixed-length) 5-bit
         codes, with possible additional bits as shown in the table
         shown in Paragraph 3.2.5, above.  Note that distance codes 30-
         31 will never actually occur in the compressed data.

      3.2.7. Compression with dynamic Huffman codes (BTYPE=10)

         The Huffman codes for the two alphabets appear in the block
         immediately after the header bits and before the actual
         compressed data, first the literal/length code and then the
         distance code.  Each code is defined by a sequence of code
         lengths, as discussed in Paragraph 3.2.2, above.  For even
         greater compactness, the code length sequences themselves are
         compressed using a Huffman code.  The alphabet for code lengths
         is as follows:

               0 - 15: Represent code lengths of 0 - 15
                   16: Copy the previous code length 3 - 6 times.
                       The next 2 bits indicate repeat length
                             (0 = 3, ... , 3 = 6)
                          Example:  Codes 8, 16 (+2 bits 11),
                                    16 (+2 bits 10) will expand to
                                    12 code lengths of 8 (1 + 6 + 5)
                   17: Repeat a code length of 0 for 3 - 10 times.
                       (3 bits of length)
                   18: Repeat a code length of 0 for 11 - 138 times
                       (7 bits of length)

         A code length of 0 indicates that the corresponding symbol in
         the literal/length or distance alphabet will not occur in the
         block, and should not participate in the Huffman code
         construction algorithm given earlier.  If only one distance
         code is used, it is encoded using one bit, not zero bits; in
         this case there is a single code length of one, with one unused
         code.  One distance code of zero bits means that there are no
         distance codes used at all (the data is all literals).

         We can now define the format of the block:

               5 Bits: HLIT, # of Literal/Length codes - 257 (257 - 286)
               5 Bits: HDIST, # of Distance codes - 1        (1 - 32)
               4 Bits: HCLEN, # of Code Length codes - 4     (4 - 19)



Deutsch                      Informational                     [Page 13]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


               (HCLEN + 4) x 3 bits: code lengths for the code length
                  alphabet given just above, in the order: 16, 17, 18,
                  0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15

                  These code lengths are interpreted as 3-bit integers
                  (0-7); as above, a code length of 0 means the
                  corresponding symbol (literal/length or distance code
                  length) is not used.

               HLIT + 257 code lengths for the literal/length alphabet,
                  encoded using the code length Huffman code

               HDIST + 1 code lengths for the distance alphabet,
                  encoded using the code length Huffman code

               The actual compressed data of the block,
                  encoded using the literal/length and distance Huffman
                  codes

               The literal/length symbol 256 (end of data),
                  encoded using the literal/length Huffman code

         The code length repeat codes can cross from HLIT + 257 to the
         HDIST + 1 code lengths.  In other words, all code lengths form
         a single sequence of HLIT + HDIST + 258 values.

   3.3. Compliance

      A compressor may limit further the ranges of values specified in
      the previous section and still be compliant; for example, it may
      limit the range of backward pointers to some value smaller than
      32K.  Similarly, a compressor may limit the size of blocks so that
      a compressible block fits in memory.

      A compliant decompressor must accept the full range of possible
      values defined in the previous section, and must accept blocks of
      arbitrary size.

4. Compression algorithm details

   While it is the intent of this document to define the "deflate"
   compressed data format without reference to any particular
   compression algorithm, the format is related to the compressed
   formats produced by LZ77 (Lempel-Ziv 1977, see reference [2] below);
   since many variations of LZ77 are patented, it is strongly
   recommended that the implementor of a compressor follow the general
   algorithm presented here, which is known not to be patented per se.
   The material in this section is not part of the definition of the



Deutsch                      Informational                     [Page 14]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


   specification per se, and a compressor need not follow it in order to
   be compliant.

   The compressor terminates a block when it determines that starting a
   new block with fresh trees would be useful, or when the block size
   fills up the compressor's block buffer.

   The compressor uses a chained hash table to find duplicated strings,
   using a hash function that operates on 3-byte sequences.  At any
   given point during compression, let XYZ be the next 3 input bytes to
   be examined (not necessarily all different, of course).  First, the
   compressor examines the hash chain for XYZ.  If the chain is empty,
   the compressor simply writes out X as a literal byte and advances one
   byte in the input.  If the hash chain is not empty, indicating that
   the sequence XYZ (or, if we are unlucky, some other 3 bytes with the
   same hash function value) has occurred recently, the compressor
   compares all strings on the XYZ hash chain with the actual input data
   sequence starting at the current point, and selects the longest
   match.

   The compressor searches the hash chains starting with the most recent
   strings, to favor small distances and thus take advantage of the
   Huffman encoding.  The hash chains are singly linked. There are no
   deletions from the hash chains; the algorithm simply discards matches
   that are too old.  To avoid a worst-case situation, very long hash
   chains are arbitrarily truncated at a certain length, determined by a
   run-time parameter.

   To improve overall compression, the compressor optionally defers the
   selection of matches ("lazy matching"): after a match of length N has
   been found, the compressor searches for a longer match starting at
   the next input byte.  If it finds a longer match, it truncates the
   previous match to a length of one (thus producing a single literal
   byte) and then emits the longer match.  Otherwise, it emits the
   original match, and, as described above, advances N bytes before
   continuing.

   Run-time parameters also control this "lazy match" procedure.  If
   compression ratio is most important, the compressor attempts a
   complete second search regardless of the length of the first match.
   In the normal case, if the current match is "long enough", the
   compressor reduces the search for a longer match, thus speeding up
   the process.  If speed is most important, the compressor inserts new
   strings in the hash table only when no match was found, or when the
   match is not "too long".  This degrades the compression ratio but
   saves time since there are both fewer insertions and fewer searches.





Deutsch                      Informational                     [Page 15]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


5. References

   [1] Huffman, D. A., "A Method for the Construction of Minimum
       Redundancy Codes", Proceedings of the Institute of Radio
       Engineers, September 1952, Volume 40, Number 9, pp. 1098-1101.

   [2] Ziv J., Lempel A., "A Universal Algorithm for Sequential Data
       Compression", IEEE Transactions on Information Theory, Vol. 23,
       No. 3, pp. 337-343.

   [3] Gailly, J.-L., and Adler, M., ZLIB documentation and sources,
       available in ftp://ftp.uu.net/pub/archiving/zip/doc/

   [4] Gailly, J.-L., and Adler, M., GZIP documentation and sources,
       available as gzip-*.tar in ftp://prep.ai.mit.edu/pub/gnu/

   [5] Schwartz, E. S., and Kallick, B. "Generating a canonical prefix
       encoding." Comm. ACM, 7,3 (Mar. 1964), pp. 166-169.

   [6] Hirschberg and Lelewer, "Efficient decoding of prefix codes,"
       Comm. ACM, 33,4, April 1990, pp. 449-459.

6. Security Considerations

   Any data compression method involves the reduction of redundancy in
   the data.  Consequently, any corruption of the data is likely to have
   severe effects and be difficult to correct.  Uncompressed text, on
   the other hand, will probably still be readable despite the presence
   of some corrupted bytes.

   It is recommended that systems using this data format provide some
   means of validating the integrity of the compressed data.  See
   reference [3], for example.

7. Source code

   Source code for a C language implementation of a "deflate" compliant
   compressor and decompressor is available within the zlib package at
   ftp://ftp.uu.net/pub/archiving/zip/zlib/.

8. Acknowledgements

   Trademarks cited in this document are the property of their
   respective owners.

   Phil Katz designed the deflate format.  Jean-Loup Gailly and Mark
   Adler wrote the related software described in this specification.
   Glenn Randers-Pehrson converted this document to RFC and HTML format.



Deutsch                      Informational                     [Page 16]

RFC 1951      DEFLATE Compressed Data Format Specification      May 1996


9. Author's Address

   L. Peter Deutsch
   Aladdin Enterprises
   203 Santa Margarita Ave.
   Menlo Park, CA 94025

   Phone: (415) 322-0103 (AM only)
   FAX:   (415) 322-1734
   EMail: <ghost@aladdin.com>

   Questions about the technical content of this specification can be
   sent by email to:

   Jean-Loup Gailly <gzip@prep.ai.mit.edu> and
   Mark Adler <madler@alumni.caltech.edu>

   Editorial comments on this specification can be sent by email to:

   L. Peter Deutsch <ghost@aladdin.com> and
   Glenn Randers-Pehrson <randeg@alumni.rpi.edu>






























Deutsch                      Informational                     [Page 17]







Network Working Group                                         P. Deutsch
Request for Comments: 1952                           Aladdin Enterprises
Category: Informational                                         May 1996


               GZIP file format specification version 4.3

Status of This Memo

   This memo provides information for the Internet community.  This memo
   does not specify an Internet standard of any kind.  Distribution of
   this memo is unlimited.

IESG Note:

   The IESG takes no position on the validity of any Intellectual
   Property Rights statements contained in this document.

Notices

   Copyright (c) 1996 L. Peter Deutsch

   Permission is granted to copy and distribute this document for any
   purpose and without charge, including translations into other
   languages and incorporation into compilations, provided that the
   copyright notice and this notice are preserved, and that any
   substantive changes or deletions from the original are clearly
   marked.

   A pointer to the latest version of this and related documentation in
   HTML format can be found at the URL
   <ftp://ftp.uu.net/graphics/png/documents/zlib/zdoc-index.html>.

Abstract

   This specification defines a lossless compressed data format that is
   compatible with the widely used GZIP utility.  The format includes a
   cyclic redundancy check value for detecting data corruption.  The
   format presently uses the DEFLATE method of compression but can be
   easily extended to use other compression methods.  The format can be
   implemented readily in a manner not covered by patents.










Deutsch                      Informational                      [Page 1]

RFC 1952             GZIP File Format Specification             May 1996


Table of Contents

   1. Introduction ................................................... 2
      1.1. Purpose ................................................... 2
      1.2. Intended audience ......................................... 3
      1.3. Scope ..................................................... 3
      1.4. Compliance ................................................ 3
      1.5. Definitions of terms and conventions used ................. 3
      1.6. Changes from previous versions ............................ 3
   2. Detailed specification ......................................... 4
      2.1. Overall conventions ....................................... 4
      2.2. File format ............................................... 5
      2.3. Member format ............................................. 5
          2.3.1. Member header and trailer ........................... 6
              2.3.1.1. Extra field ................................... 8
              2.3.1.2. Compliance .................................... 9
      3. References .................................................. 9
      4. Security Considerations .................................... 10
      5. Acknowledgements ........................................... 10
      6. Author's Address ........................................... 10
      7. Appendix: Jean-Loup Gailly's gzip utility .................. 11
      8. Appendix: Sample CRC Code .................................. 11

1. Introduction

   1.1. Purpose

      The purpose of this specification is to define a lossless
      compressed data format that:

          * Is independent of CPU type, operating system, file system,
            and character set, and hence can be used for interchange;
          * Can compress or decompress a data stream (as opposed to a
            randomly accessible file) to produce another data stream,
            using only an a priori bounded amount of intermediate
            storage, and hence can be used in data communications or
            similar structures such as Unix filters;
          * Compresses data with efficiency comparable to the best
            currently available general-purpose compression methods,
            and in particular considerably better than the "compress"
            program;
          * Can be implemented readily in a manner not covered by
            patents, and hence can be practiced freely;
          * Is compatible with the file format produced by the current
            widely used gzip utility, in that conforming decompressors
            will be able to read data produced by the existing gzip
            compressor.




Deutsch                      Informational                      [Page 2]

RFC 1952             GZIP File Format Specification             May 1996


      The data format defined by this specification does not attempt to:

          * Provide random access to compressed data;
          * Compress specialized data (e.g., raster graphics) as well as
            the best currently available specialized algorithms.

   1.2. Intended audience

      This specification is intended for use by implementors of software
      to compress data into gzip format and/or decompress data from gzip
      format.

      The text of the specification assumes a basic background in
      programming at the level of bits and other primitive data
      representations.

   1.3. Scope

      The specification specifies a compression method and a file format
      (the latter assuming only that a file can store a sequence of
      arbitrary bytes).  It does not specify any particular interface to
      a file system or anything about character sets or encodings
      (except for file names and comments, which are optional).

   1.4. Compliance

      Unless otherwise indicated below, a compliant decompressor must be
      able to accept and decompress any file that conforms to all the
      specifications presented here; a compliant compressor must produce
      files that conform to all the specifications presented here.  The
      material in the appendices is not part of the specification per se
      and is not relevant to compliance.

   1.5. Definitions of terms and conventions used

      byte: 8 bits stored or transmitted as a unit (same as an octet).
      (For this specification, a byte is exactly 8 bits, even on
      machines which store a character on a number of bits different
      from 8.)  See below for the numbering of bits within a byte.

   1.6. Changes from previous versions

      There have been no technical changes to the gzip format since
      version 4.1 of this specification.  In version 4.2, some
      terminology was changed, and the sample CRC code was rewritten for
      clarity and to eliminate the requirement for the caller to do pre-
      and post-conditioning.  Version 4.3 is a conversion of the
      specification to RFC style.



Deutsch                      Informational                      [Page 3]

RFC 1952             GZIP File Format Specification             May 1996


2. Detailed specification

   2.1. Overall conventions

      In the diagrams below, a box like this:

         +---+
         |   | <-- the vertical bars might be missing
         +---+

      represents one byte; a box like this:

         +==============+
         |              |
         +==============+

      represents a variable number of bytes.

      Bytes stored within a computer do not have a "bit order", since
      they are always treated as a unit.  However, a byte considered as
      an integer between 0 and 255 does have a most- and least-
      significant bit, and since we write numbers with the most-
      significant digit on the left, we also write bytes with the most-
      significant bit on the left.  In the diagrams below, we number the
      bits of a byte so that bit 0 is the least-significant bit, i.e.,
      the bits are numbered:

         +--------+
         |76543210|
         +--------+

      This document does not address the issue of the order in which
      bits of a byte are transmitted on a bit-sequential medium, since
      the data format described here is byte- rather than bit-oriented.

      Within a computer, a number may occupy multiple bytes.  All
      multi-byte numbers in the format described here are stored with
      the least-significant byte first (at the lower memory address).
      For example, the decimal number 520 is stored as:

             0        1
         +--------+--------+
         |00001000|00000010|
         +--------+--------+
          ^        ^
          |        |
          |        + more significant byte = 2 x 256
          + less significant byte = 8



Deutsch                      Informational                      [Page 4]

RFC 1952             GZIP File Format Specification             May 1996


   2.2. File format

      A gzip file consists of a series of "members" (compressed data
      sets).  The format of each member is specified in the following
      section.  The members simply appear one after another in the file,
      with no additional information before, between, or after them.

   2.3. Member format

      Each member has the following structure:

         +---+---+---+---+---+---+---+---+---+---+
         |ID1|ID2|CM |FLG|     MTIME     |XFL|OS | (more-->)
         +---+---+---+---+---+---+---+---+---+---+

      (if FLG.FEXTRA set)

         +---+---+=================================+
         | XLEN  |...XLEN bytes of "extra field"...| (more-->)
         +---+---+=================================+

      (if FLG.FNAME set)

         +=========================================+
         |...original file name, zero-terminated...| (more-->)
         +=========================================+

      (if FLG.FCOMMENT set)

         +===================================+
         |...file comment, zero-terminated...| (more-->)
         +===================================+

      (if FLG.FHCRC set)

         +---+---+
         | CRC16 |
         +---+---+

         +=======================+
         |...compressed blocks...| (more-->)
         +=======================+

           0   1   2   3   4   5   6   7
         +---+---+---+---+---+---+---+---+
         |     CRC32     |     ISIZE     |
         +---+---+---+---+---+---+---+---+




Deutsch                      Informational                      [Page 5]

RFC 1952             GZIP File Format Specification             May 1996


      2.3.1. Member header and trailer

         ID1 (IDentification 1)
         ID2 (IDentification 2)
            These have the fixed values ID1 = 31 (0x1f, \037), ID2 = 139
            (0x8b, \213), to identify the file as being in gzip format.

         CM (Compression Method)
            This identifies the compression method used in the file.  CM
            = 0-7 are reserved.  CM = 8 denotes the "deflate"
            compression method, which is the one customarily used by
            gzip and which is documented elsewhere.

         FLG (FLaGs)
            This flag byte is divided into individual bits as follows:

               bit 0   FTEXT
               bit 1   FHCRC
               bit 2   FEXTRA
               bit 3   FNAME
               bit 4   FCOMMENT
               bit 5   reserved
               bit 6   reserved
               bit 7   reserved

            If FTEXT is set, the file is probably ASCII text.  This is
            an optional indication, which the compressor may set by
            checking a small amount of the input data to see whether any
            non-ASCII characters are present.  In case of doubt, FTEXT
            is cleared, indicating binary data. For systems which have
            different file formats for ascii text and binary data, the
            decompressor can use FTEXT to choose the appropriate format.
            We deliberately do not specify the algorithm used to set
            this bit, since a compressor always has the option of
            leaving it cleared and a decompressor always has the option
            of ignoring it and letting some other program handle issues
            of data conversion.

            If FHCRC is set, a CRC16 for the gzip header is present,
            immediately before the compressed data. The CRC16 consists
            of the two least significant bytes of the CRC32 for all
            bytes of the gzip header up to and not including the CRC16.
            [The FHCRC bit was never set by versions of gzip up to
            1.2.4, even though it was documented with a different
            meaning in gzip 1.2.4.]

            If FEXTRA is set, optional extra fields are present, as
            described in a following section.



Deutsch                      Informational                      [Page 6]

RFC 1952             GZIP File Format Specification             May 1996


            If FNAME is set, an original file name is present,
            terminated by a zero byte.  The name must consist of ISO
            8859-1 (LATIN-1) characters; on operating systems using
            EBCDIC or any other character set for file names, the name
            must be translated to the ISO LATIN-1 character set.  This
            is the original name of the file being compressed, with any
            directory components removed, and, if the file being
            compressed is on a file system with case insensitive names,
            forced to lower case. There is no original file name if the
            data was compressed from a source other than a named file;
            for example, if the source was stdin on a Unix system, there
            is no file name.

            If FCOMMENT is set, a zero-terminated file comment is
            present.  This comment is not interpreted; it is only
            intended for human consumption.  The comment must consist of
            ISO 8859-1 (LATIN-1) characters.  Line breaks should be
            denoted by a single line feed character (10 decimal).

            Reserved FLG bits must be zero.

         MTIME (Modification TIME)
            This gives the most recent modification time of the original
            file being compressed.  The time is in Unix format, i.e.,
            seconds since 00:00:00 GMT, Jan.  1, 1970.  (Note that this
            may cause problems for MS-DOS and other systems that use
            local rather than Universal time.)  If the compressed data
            did not come from a file, MTIME is set to the time at which
            compression started.  MTIME = 0 means no time stamp is
            available.

         XFL (eXtra FLags)
            These flags are available for use by specific compression
            methods.  The "deflate" method (CM = 8) sets these flags as
            follows:

               XFL = 2 - compressor used maximum compression,
                         slowest algorithm
               XFL = 4 - compressor used fastest algorithm

         OS (Operating System)
            This identifies the type of file system on which compression
            took place.  This may be useful in determining end-of-line
            convention for text files.  The currently defined values are
            as follows:






Deutsch                      Informational                      [Page 7]

RFC 1952             GZIP File Format Specification             May 1996


                 0 - FAT filesystem (MS-DOS, OS/2, NT/Win32)
                 1 - Amiga
                 2 - VMS (or OpenVMS)
                 3 - Unix
                 4 - VM/CMS
                 5 - Atari TOS
                 6 - HPFS filesystem (OS/2, NT)
                 7 - Macintosh
                 8 - Z-System
                 9 - CP/M
                10 - TOPS-20
                11 - NTFS filesystem (NT)
                12 - QDOS
                13 - Acorn RISCOS
               255 - unknown

         XLEN (eXtra LENgth)
            If FLG.FEXTRA is set, this gives the length of the optional
            extra field.  See below for details.

         CRC32 (CRC-32)
            This contains a Cyclic Redundancy Check value of the
            uncompressed data computed according to CRC-32 algorithm
            used in the ISO 3309 standard and in section 8.1.1.6.2 of
            ITU-T recommendation V.42.  (See http://www.iso.ch for
            ordering ISO documents. See gopher://info.itu.ch for an
            online version of ITU-T V.42.)

         ISIZE (Input SIZE)
            This contains the size of the original (uncompressed) input
            data modulo 2^32.

      2.3.1.1. Extra field

         If the FLG.FEXTRA bit is set, an "extra field" is present in
         the header, with total length XLEN bytes.  It consists of a
         series of subfields, each of the form:

            +---+---+---+---+==================================+
            |SI1|SI2|  LEN  |... LEN bytes of subfield data ...|
            +---+---+---+---+==================================+

         SI1 and SI2 provide a subfield ID, typically two ASCII letters
         with some mnemonic value.  Jean-Loup Gailly
         <gzip@prep.ai.mit.edu> is maintaining a registry of subfield
         IDs; please send him any subfield ID you wish to use.  Subfield
         IDs with SI2 = 0 are reserved for future use.  The following
         IDs are currently defined:



Deutsch                      Informational                      [Page 8]

RFC 1952             GZIP File Format Specification             May 1996


            SI1         SI2         Data
            ----------  ----------  ----
            0x41 ('A')  0x70 ('P')  Apollo file type information

         LEN gives the length of the subfield data, excluding the 4
         initial bytes.

      2.3.1.2. Compliance

         A compliant compressor must produce files with correct ID1,
         ID2, CM, CRC32, and ISIZE, but may set all the other fields in
         the fixed-length part of the header to default values (255 for
         OS, 0 for all others).  The compressor must set all reserved
         bits to zero.

         A compliant decompressor must check ID1, ID2, and CM, and
         provide an error indication if any of these have incorrect
         values.  It must examine FEXTRA/XLEN, FNAME, FCOMMENT and FHCRC
         at least so it can skip over the optional fields if they are
         present.  It need not examine any other part of the header or
         trailer; in particular, a decompressor may ignore FTEXT and OS
         and always produce binary output, and still be compliant.  A
         compliant decompressor must give an error indication if any
         reserved bit is non-zero, since such a bit could indicate the
         presence of a new field that would cause subsequent data to be
         interpreted incorrectly.

3. References

   [1] "Information Processing - 8-bit single-byte coded graphic
       character sets - Part 1: Latin alphabet No.1" (ISO 8859-1:1987).
       The ISO 8859-1 (Latin-1) character set is a superset of 7-bit
       ASCII. Files defining this character set are available as
       iso_8859-1.* in ftp://ftp.uu.net/graphics/png/documents/

   [2] ISO 3309

   [3] ITU-T recommendation V.42

   [4] Deutsch, L.P.,"DEFLATE Compressed Data Format Specification",
       available in ftp://ftp.uu.net/pub/archiving/zip/doc/

   [5] Gailly, J.-L., GZIP documentation, available as gzip-*.tar in
       ftp://prep.ai.mit.edu/pub/gnu/

   [6] Sarwate, D.V., "Computation of Cyclic Redundancy Checks via Table
       Look-Up", Communications of the ACM, 31(8), pp.1008-1013.




Deutsch                      Informational                      [Page 9]

RFC 1952             GZIP File Format Specification             May 1996


   [7] Schwaderer, W.D., "CRC Calculation", April 85 PC Tech Journal,
       pp.118-133.

   [8] ftp://ftp.adelaide.edu.au/pub/rocksoft/papers/crc_v3.txt,
       describing the CRC concept.

4. Security Considerations

   Any data compression method involves the reduction of redundancy in
   the data.  Consequently, any corruption of the data is likely to have
   severe effects and be difficult to correct.  Uncompressed text, on
   the other hand, will probably still be readable despite the presence
   of some corrupted bytes.

   It is recommended that systems using this data format provide some
   means of validating the integrity of the compressed data, such as by
   setting and checking the CRC-32 check value.

5. Acknowledgements

   Trademarks cited in this document are the property of their
   respective owners.

   Jean-Loup Gailly designed the gzip format and wrote, with Mark Adler,
   the related software described in this specification.  Glenn
   Randers-Pehrson converted this document to RFC and HTML format.

6. Author's Address

   L. Peter Deutsch
   Aladdin Enterprises
   203 Santa Margarita Ave.
   Menlo Park, CA 94025

   Phone: (415) 322-0103 (AM only)
   FAX:   (415) 322-1734
   EMail: <ghost@aladdin.com>

   Questions about the technical content of this specification can be
   sent by email to:

   Jean-Loup Gailly <gzip@prep.ai.mit.edu> and
   Mark Adler <madler@alumni.caltech.edu>

   Editorial comments on this specification can be sent by email to:

   L. Peter Deutsch <ghost@aladdin.com> and
   Glenn Randers-Pehrson <randeg@alumni.rpi.edu>



Deutsch                      Informational                     [Page 10]

RFC 1952             GZIP File Format Specification             May 1996


7. Appendix: Jean-Loup Gailly's gzip utility

   The most widely used implementation of gzip compression, and the
   original documentation on which this specification is based, were
   created by Jean-Loup Gailly <gzip@prep.ai.mit.edu>.  Since this
   implementation is a de facto standard, we mention some more of its
   features here.  Again, the material in this section is not part of
   the specification per se, and implementations need not follow it to
   be compliant.

   When compressing or decompressing a file, gzip preserves the
   protection, ownership, and modification time attributes on the local
   file system, since there is no provision for representing protection
   attributes in the gzip file format itself.  Since the file format
   includes a modification time, the gzip decompressor provides a
   command line switch that assigns the modification time from the file,
   rather than the local modification time of the compressed input, to
   the decompressed output.

8. Appendix: Sample CRC Code

   The following sample code represents a practical implementation of
   the CRC (Cyclic Redundancy Check). (See also ISO 3309 and ITU-T V.42
   for a formal specification.)

   The sample code is in the ANSI C programming language. Non C users
   may find it easier to read with these hints:

      &      Bitwise AND operator.
      ^      Bitwise exclusive-OR operator.
      >>     Bitwise right shift operator. When applied to an
             unsigned quantity, as here, right shift inserts zero
             bit(s) at the left.
      !      Logical NOT operator.
      ++     "n++" increments the variable n.
      0xNNN  0x introduces a hexadecimal (base 16) constant.
             Suffix L indicates a long value (at least 32 bits).

      /* Table of CRCs of all 8-bit messages. */
      unsigned long crc_table[256];

      /* Flag: has the table been computed? Initially false. */
      int crc_table_computed = 0;

      /* Make the table for a fast CRC. */
      void make_crc_table(void)
      {
        unsigned long c;



Deutsch                      Informational                     [Page 11]

RFC 1952             GZIP File Format Specification             May 1996


        int n, k;
        for (n = 0; n < 256; n++) {
          c = (unsigned long) n;
          for (k = 0; k < 8; k++) {
            if (c & 1) {
              c = 0xedb88320L ^ (c >> 1);
            } else {
              c = c >> 1;
            }
          }
          crc_table[n] = c;
        }
        crc_table_computed = 1;
      }

      /*
         Update a running crc with the bytes buf[0..len-1] and return
       the updated crc. The crc should be initialized to zero. Pre- and
       post-conditioning (one's complement) is performed within this
       function so it shouldn't be done by the caller. Usage example:

         unsigned long crc = 0L;

         while (read_buffer(buffer, length) != EOF) {
           crc = update_crc(crc, buffer, length);
         }
         if (crc != original_crc) error();
      */
      unsigned long update_crc(unsigned long crc,
                      unsigned char *buf, int len)
      {
        unsigned long c = crc ^ 0xffffffffL;
        int n;

        if (!crc_table_computed)
          make_crc_table();
        for (n = 0; n < len; n++) {
          c = crc_table[(c ^ buf[n]) & 0xff] ^ (c >> 8);
        }
        return c ^ 0xffffffffL;
      }

      /* Return the CRC of the bytes buf[0..len-1]. */
      unsigned long crc(unsigned char *buf, int len)
      {
        return update_crc(0L, buf, len);
      }




Deutsch                      Informational                     [Page 12]

A Fast Method for Identifying Plain Text Files
==============================================


Introduction
------------

Given a file coming from an unknown source, it is sometimes desirable
to find out whether the format of that file is plain text.  Although
this may appear like a simple task, a fully accurate detection of the
file type requires heavy-duty semantic analysis on the file contents.
It is, however, possible to obtain satisfactory results by employing
various heuristics.

Previous versions of PKZip and other zip-compatible compression tools
were using a crude detection scheme: if more than 80% (4/5) of the bytes
found in a certain buffer are within the range [7..127], the file is
labeled as plain text, otherwise it is labeled as binary.  A prominent
limitation of this scheme is the restriction to Latin-based alphabets.
Other alphabets, like Greek, Cyrillic or Asian, make extensive use of
the bytes within the range [128..255], and texts using these alphabets
are most often misidentified by this scheme; in other words, the rate
of false negatives is sometimes too high, which means that the recall
is low.  Another weakness of this scheme is a reduced precision, due to
the false positives that may occur when binary files containing large
amounts of textual characters are misidentified as plain text.

In this article we propose a new, simple detection scheme that features
a much increased precision and a near-100% recall.  This scheme is
designed to work on ASCII, Unicode and other ASCII-derived alphabets,
and it handles single-byte encodings (ISO-8859, MacRoman, KOI8, etc.)
and variable-sized encodings (ISO-2022, UTF-8, etc.).  Wider encodings
(UCS-2/UTF-16 and UCS-4/UTF-32) are not handled, however.


The Algorithm
-------------

The algorithm works by dividing the set of bytecodes [0..255] into three
categories:
- The white list of textual bytecodes:
  9 (TAB), 10 (LF), 13 (CR), 32 (SPACE) to 255.
- The gray list of tolerated bytecodes:
  7 (BEL), 8 (BS), 11 (VT), 12 (FF), 26 (SUB), 27 (ESC).
- The black list of undesired, non-textual bytecodes:
  0 (NUL) to 6, 14 to 31.

If a file contains at least one byte that belongs to the white list and
no byte that belongs to the black list, then the file is categorized as
plain text; otherwise, it is categorized as binary.  (The boundary case,
when the file is empty, automatically falls into the latter category.)


Rationale
---------

The idea behind this algorithm relies on two observations.

The first observation is that, although the full range of 7-bit codes
[0..127] is properly specified by the ASCII standard, most control
characters in the range [0..31] are not used in practice.  The only
widely-used, almost universally-portable control codes are 9 (TAB),
10 (LF) and 13 (CR).  There are a few more control codes that are
recognized on a reduced range of platforms and text viewers/editors:
7 (BEL), 8 (BS), 11 (VT), 12 (FF), 26 (SUB) and 27 (ESC); but these
codes are rarely (if ever) used alone, without being accompanied by
some printable text.  Even the newer, portable text formats such as
XML avoid using control characters outside the list mentioned here.

The second observation is that most of the binary files tend to contain
control characters, especially 0 (NUL).  Even though the older text
detection schemes observe the presence of non-ASCII codes from the range
[128..255], the precision rarely has to suffer if this upper range is
labeled as textual, because the files that are genuinely binary tend to
contain both control characters and codes from the upper range.  On the
other hand, the upper range needs to be labeled as textual, because it
is used by virtually all ASCII extensions.  In particular, this range is
used for encoding non-Latin scripts.

Since there is no counting involved, other than simply observing the
presence or the absence of some byte values, the algorithm produces
consistent results, regardless what alphabet encoding is being used.
(If counting were involved, it could be possible to obtain different
results on a text encoded, say, using ISO-8859-16 versus UTF-8.)

There is an extra category of plain text files that are "polluted" with
one or more black-listed codes, either by mistake or by peculiar design
considerations.  In such cases, a scheme that tolerates a small fraction
of black-listed codes would provide an increased recall (i.e. more true
positives).  This, however, incurs a reduced precision overall, since
false positives are more likely to appear in binary files that contain
large chunks of textual data.  Furthermore, "polluted" plain text should
be regarded as binary by general-purpose text detection schemes, because
general-purpose text processing algorithms might not be applicable.
Under this premise, it is safe to say that our detection method provides
a near-100% recall.

Experiments have been run on many files coming from various platforms
and applications.  We tried plain text files, system logs, source code,
formatted office documents, compiled object code, etc.  The results
confirm the optimistic assumptions about the capabilities of this
algorithm.


--
Cosmin Truta
Last updated: 2006-May-28

            Frequently Asked Questions about ZLIB1.DLL


This document describes the design, the rationale, and the usage
of the official DLL build of zlib, named ZLIB1.DLL.  If you have
general questions about zlib, you should see the file "FAQ" found
in the zlib distribution, or at the following location:
  http://www.gzip.org/zlib/zlib_faq.html


 1. What is ZLIB1.DLL, and how can I get it?

  - ZLIB1.DLL is the official build of zlib as a DLL.
    (Please remark the character '1' in the name.)

    Pointers to a precompiled ZLIB1.DLL can be found in the zlib
    web site at:
      http://www.zlib.net/

    Applications that link to ZLIB1.DLL can rely on the following
    specification:

    * The exported symbols are exclusively defined in the source
      files "zlib.h" and "zlib.def", found in an official zlib
      source distribution.
    * The symbols are exported by name, not by ordinal.
    * The exported names are undecorated.
    * The calling convention of functions is "C" (CDECL).
    * The ZLIB1.DLL binary is linked to MSVCRT.DLL.

    The archive in which ZLIB1.DLL is bundled contains compiled
    test programs that must run with a valid build of ZLIB1.DLL.
    It is recommended to download the prebuilt DLL from the zlib
    web site, instead of building it yourself, to avoid potential
    incompatibilities that could be introduced by your compiler
    and build settings.  If you do build the DLL yourself, please
    make sure that it complies with all the above requirements,
    and it runs with the precompiled test programs, bundled with
    the original ZLIB1.DLL distribution.

    If, for any reason, you need to build an incompatible DLL,
    please use a different file name.


 2. Why did you change the name of the DLL to ZLIB1.DLL?
    What happened to the old ZLIB.DLL?

  - The old ZLIB.DLL, built from zlib-1.1.4 or earlier, required
    compilation settings that were incompatible to those used by
    a static build.  The DLL settings were supposed to be enabled
    by defining the macro ZLIB_DLL, before including "zlib.h".
    Incorrect handling of this macro was silently accepted at
    build time, resulting in two major problems:

    * ZLIB_DLL was missing from the old makefile.  When building
      the DLL, not all people added it to the build options.  In
      consequence, incompatible incarnations of ZLIB.DLL started
      to circulate around the net.

    * When switching from using the static library to using the
      DLL, applications had to define the ZLIB_DLL macro and
      to recompile all the sources that contained calls to zlib
      functions.  Failure to do so resulted in creating binaries
      that were unable to run with the official ZLIB.DLL build.

    The only possible solution that we could foresee was to make
    a binary-incompatible change in the DLL interface, in order to
    remove the dependency on the ZLIB_DLL macro, and to release
    the new DLL under a different name.

    We chose the name ZLIB1.DLL, where '1' indicates the major
    zlib version number.  We hope that we will not have to break
    the binary compatibility again, at least not as long as the
    zlib-1.x series will last.

    There is still a ZLIB_DLL macro, that can trigger a more
    efficient build and use of the DLL, but compatibility no
    longer dependents on it.


 3. Can I build ZLIB.DLL from the new zlib sources, and replace
    an old ZLIB.DLL, that was built from zlib-1.1.4 or earlier?

  - In principle, you can do it by assigning calling convention
    keywords to the macros ZEXPORT and ZEXPORTVA.  In practice,
    it depends on what you mean by "an old ZLIB.DLL", because the
    old DLL exists in several mutually-incompatible versions.
    You have to find out first what kind of calling convention is
    being used in your particular ZLIB.DLL build, and to use the
    same one in the new build.  If you don't know what this is all
    about, you might be better off if you would just leave the old
    DLL intact.


 4. Can I compile my application using the new zlib interface, and
    link it to an old ZLIB.DLL, that was built from zlib-1.1.4 or
    earlier?

  - The official answer is "no"; the real answer depends again on
    what kind of ZLIB.DLL you have.  Even if you are lucky, this
    course of action is unreliable.

    If you rebuild your application and you intend to use a newer
    version of zlib (post- 1.1.4), it is strongly recommended to
    link it to the new ZLIB1.DLL.


 5. Why are the zlib symbols exported by name, and not by ordinal?

  - Although exporting symbols by ordinal is a little faster, it
    is risky.  Any single glitch in the maintenance or use of the
    DEF file that contains the ordinals can result in incompatible
    builds and frustrating crashes.  Simply put, the benefits of
    exporting symbols by ordinal do not justify the risks.

    Technically, it should be possible to maintain ordinals in
    the DEF file, and still export the symbols by name.  Ordinals
    exist in every DLL, and even if the dynamic linking performed
    at the DLL startup is searching for names, ordinals serve as
    hints, for a faster name lookup.  However, if the DEF file
    contains ordinals, the Microsoft linker automatically builds
    an implib that will cause the executables linked to it to use
    those ordinals, and not the names.  It is interesting to
    notice that the GNU linker for Win32 does not suffer from this
    problem.

    It is possible to avoid the DEF file if the exported symbols
    are accompanied by a "__declspec(dllexport)" attribute in the
    source files.  You can do this in zlib by predefining the
    ZLIB_DLL macro.


 6. I see that the ZLIB1.DLL functions use the "C" (CDECL) calling
    convention.  Why not use the STDCALL convention?
    STDCALL is the standard convention in Win32, and I need it in
    my Visual Basic project!

    (For readability, we use CDECL to refer to the convention
     triggered by the "__cdecl" keyword, STDCALL to refer to
     the convention triggered by "__stdcall", and FASTCALL to
     refer to the convention triggered by "__fastcall".)

  - Most of the native Windows API functions (without varargs) use
    indeed the WINAPI convention (which translates to STDCALL in
    Win32), but the standard C functions use CDECL.  If a user
    application is intrinsically tied to the Windows API (e.g.
    it calls native Windows API functions such as CreateFile()),
    sometimes it makes sense to decorate its own functions with
    WINAPI.  But if ANSI C or POSIX portability is a goal (e.g.
    it calls standard C functions such as fopen()), it is not a
    sound decision to request the inclusion of <windows.h>, or to
    use non-ANSI constructs, for the sole purpose to make the user
    functions STDCALL-able.

    The functionality offered by zlib is not in the category of
    "Windows functionality", but is more like "C functionality".

    Technically, STDCALL is not bad; in fact, it is slightly
    faster than CDECL, and it works with variable-argument
    functions, just like CDECL.  It is unfortunate that, in spite
    of using STDCALL in the Windows API, it is not the default
    convention used by the C compilers that run under Windows.
    The roots of the problem reside deep inside the unsafety of
    the K&R-style function prototypes, where the argument types
    are not specified; but that is another story for another day.

    The remaining fact is that CDECL is the default convention.
    Even if an explicit convention is hard-coded into the function
    prototypes inside C headers, problems may appear.  The
    necessity to expose the convention in users' callbacks is one
    of these problems.

    The calling convention issues are also important when using
    zlib in other programming languages.  Some of them, like Ada
    (GNAT) and Fortran (GNU G77), have C bindings implemented
    initially on Unix, and relying on the C calling convention.
    On the other hand, the pre- .NET versions of Microsoft Visual
    Basic require STDCALL, while Borland Delphi prefers, although
    it does not require, FASTCALL.

    In fairness to all possible uses of zlib outside the C
    programming language, we choose the default "C" convention.
    Anyone interested in different bindings or conventions is
    encouraged to maintain specialized projects.  The "contrib/"
    directory from the zlib distribution already holds a couple
    of foreign bindings, such as Ada, C++, and Delphi.


 7. I need a DLL for my Visual Basic project.  What can I do?

  - Define the ZLIB_WINAPI macro before including "zlib.h", when
    building both the DLL and the user application (except that
    you don't need to define anything when using the DLL in Visual
    Basic).  The ZLIB_WINAPI macro will switch on the WINAPI
    (STDCALL) convention.  The name of this DLL must be different
    than the official ZLIB1.DLL.

    Gilles Vollant has contributed a build named ZLIBWAPI.DLL,
    with the ZLIB_WINAPI macro turned on, and with the minizip
    functionality built in.  For more information, please read
    the notes inside "contrib/vstudio/readme.txt", found in the
    zlib distribution.


 8. I need to use zlib in my Microsoft .NET project.  What can I
    do?

  - Henrik Ravn has contributed a .NET wrapper around zlib.  Look
    into contrib/dotzlib/, inside the zlib distribution.


 9. If my application uses ZLIB1.DLL, should I link it to
    MSVCRT.DLL?  Why?

  - It is not required, but it is recommended to link your
    application to MSVCRT.DLL, if it uses ZLIB1.DLL.

    The executables (.EXE, .DLL, etc.) that are involved in the
    same process and are using the C run-time library (i.e. they
    are calling standard C functions), must link to the same
    library.  There are several libraries in the Win32 system:
    CRTDLL.DLL, MSVCRT.DLL, the static C libraries, etc.
    Since ZLIB1.DLL is linked to MSVCRT.DLL, the executables that
    depend on it should also be linked to MSVCRT.DLL.


10. Why are you saying that ZLIB1.DLL and my application should
    be linked to the same C run-time (CRT) library?  I linked my
    application and my DLLs to different C libraries (e.g. my
    application to a static library, and my DLLs to MSVCRT.DLL),
    and everything works fine.

  - If a user library invokes only pure Win32 API (accessible via
    <windows.h> and the related headers), its DLL build will work
    in any context.  But if this library invokes standard C API,
    things get more complicated.

    There is a single Win32 library in a Win32 system.  Every
    function in this library resides in a single DLL module, that
    is safe to call from anywhere.  On the other hand, there are
    multiple versions of the C library, and each of them has its
    own separate internal state.  Standalone executables and user
    DLLs that call standard C functions must link to a C run-time
    (CRT) library, be it static or shared (DLL).  Intermixing
    occurs when an executable (not necessarily standalone) and a
    DLL are linked to different CRTs, and both are running in the
    same process.

    Intermixing multiple CRTs is possible, as long as their
    internal states are kept intact.  The Microsoft Knowledge Base
    articles KB94248 "HOWTO: Use the C Run-Time" and KB140584
    "HOWTO: Link with the Correct C Run-Time (CRT) Library"
    mention the potential problems raised by intermixing.

    If intermixing works for you, it's because your application
    and DLLs are avoiding the corruption of each of the CRTs'
    internal states, maybe by careful design, or maybe by fortune.

    Also note that linking ZLIB1.DLL to non-Microsoft CRTs, such
    as those provided by Borland, raises similar problems.


11. Why are you linking ZLIB1.DLL to MSVCRT.DLL?

  - MSVCRT.DLL exists on every Windows 95 with a new service pack
    installed, or with Microsoft Internet Explorer 4 or later, and
    on all other Windows 4.x or later (Windows 98, Windows NT 4,
    or later).  It is freely distributable; if not present in the
    system, it can be downloaded from Microsoft or from other
    software provider for free.

    The fact that MSVCRT.DLL does not exist on a virgin Windows 95
    is not so problematic.  Windows 95 is scarcely found nowadays,
    Microsoft ended its support a long time ago, and many recent
    applications from various vendors, including Microsoft, do not
    even run on it.  Furthermore, no serious user should run
    Windows 95 without a proper update installed.


12. Why are you not linking ZLIB1.DLL to
    <<my favorite C run-time library>> ?

  - We considered and abandoned the following alternatives:

    * Linking ZLIB1.DLL to a static C library (LIBC.LIB, or
      LIBCMT.LIB) is not a good option.  People are using the DLL
      mainly to save disk space.  If you are linking your program
      to a static C library, you may as well consider linking zlib
      in statically, too.

    * Linking ZLIB1.DLL to CRTDLL.DLL looks appealing, because
      CRTDLL.DLL is present on every Win32 installation.
      Unfortunately, it has a series of problems: it does not
      work properly with Microsoft's C++ libraries, it does not
      provide support for 64-bit file offsets, (and so on...),
      and Microsoft discontinued its support a long time ago.

    * Linking ZLIB1.DLL to MSVCR70.DLL or MSVCR71.DLL, supplied
      with the Microsoft .NET platform, and Visual C++ 7.0/7.1,
      raises problems related to the status of ZLIB1.DLL as a
      system component.  According to the Microsoft Knowledge Base
      article KB326922 "INFO: Redistribution of the Shared C
      Runtime Component in Visual C++ .NET", MSVCR70.DLL and
      MSVCR71.DLL are not supposed to function as system DLLs,
      because they may clash with MSVCRT.DLL.  Instead, the
      application's installer is supposed to put these DLLs
      (if needed) in the application's private directory.
      If ZLIB1.DLL depends on a non-system runtime, it cannot
      function as a redistributable system component.

    * Linking ZLIB1.DLL to non-Microsoft runtimes, such as
      Borland's, or Cygwin's, raises problems related to the
      reliable presence of these runtimes on Win32 systems.
      It's easier to let the DLL build of zlib up to the people
      who distribute these runtimes, and who may proceed as
      explained in the answer to Question 14.


13. If ZLIB1.DLL cannot be linked to MSVCR70.DLL or MSVCR71.DLL,
    how can I build/use ZLIB1.DLL in Microsoft Visual C++ 7.0
    (Visual Studio .NET) or newer?

  - Due to the problems explained in the Microsoft Knowledge Base
    article KB326922 (see the previous answer), the C runtime that
    comes with the VC7 environment is no longer considered a
    system component.  That is, it should not be assumed that this
    runtime exists, or may be installed in a system directory.
    Since ZLIB1.DLL is supposed to be a system component, it may
    not depend on a non-system component.

    In order to link ZLIB1.DLL and your application to MSVCRT.DLL
    in VC7, you need the library of Visual C++ 6.0 or older.  If
    you don't have this library at hand, it's probably best not to
    use ZLIB1.DLL.

    We are hoping that, in the future, Microsoft will provide a
    way to build applications linked to a proper system runtime,
    from the Visual C++ environment.  Until then, you have a
    couple of alternatives, such as linking zlib in statically.
    If your application requires dynamic linking, you may proceed
    as explained in the answer to Question 14.


14. I need to link my own DLL build to a CRT different than
    MSVCRT.DLL.  What can I do?

  - Feel free to rebuild the DLL from the zlib sources, and link
    it the way you want.  You should, however, clearly state that
    your build is unofficial.  You should give it a different file
    name, and/or install it in a private directory that can be
    accessed by your application only, and is not visible to the
    others (i.e. it's neither in the PATH, nor in the SYSTEM or
    SYSTEM32 directories).  Otherwise, your build may clash with
    applications that link to the official build.

    For example, in Cygwin, zlib is linked to the Cygwin runtime
    CYGWIN1.DLL, and it is distributed under the name CYGZ.DLL.


15. May I include additional pieces of code that I find useful,
    link them in ZLIB1.DLL, and export them?

  - No.  A legitimate build of ZLIB1.DLL must not include code
    that does not originate from the official zlib source code.
    But you can make your own private DLL build, under a different
    file name, as suggested in the previous answer.

    For example, zlib is a part of the VCL library, distributed
    with Borland Delphi and C++ Builder.  The DLL build of VCL
    is a redistributable file, named VCLxx.DLL.


16. May I remove some functionality out of ZLIB1.DLL, by enabling
    macros like NO_GZCOMPRESS or NO_GZIP at compile time?

  - No.  A legitimate build of ZLIB1.DLL must provide the complete
    zlib functionality, as implemented in the official zlib source
    code.  But you can make your own private DLL build, under a
    different file name, as suggested in the previous answer.


17. I made my own ZLIB1.DLL build.  Can I test it for compliance?

  - We prefer that you download the official DLL from the zlib
    web site.  If you need something peculiar from this DLL, you
    can send your suggestion to the zlib mailing list.

    However, in case you do rebuild the DLL yourself, you can run
    it with the test programs found in the DLL distribution.
    Running these test programs is not a guarantee of compliance,
    but a failure can imply a detected problem.

**

This document is written and maintained by
Cosmin Truta <cosmint@cs.ubbcluj.ro>
ZLIB DATA COMPRESSION LIBRARY

zlib 1.2.8 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://www.ietf.org/rfc/rfc1950.txt (zlib format), rfc1951.txt (deflate format)
and rfc1952.txt (gzip format).

All functions of the compression library are documented in the file zlib.h
(volunteer to write man pages welcome, contact zlib@gzip.org).  Two compiled
examples are distributed in this package, example and minigzip.  The example_d
and minigzip_d flavors validate that the zlib1.dll file is working correctly.

Questions about zlib should be sent to <zlib@gzip.org>.  The zlib home page
is http://zlib.net/ .  Before reporting a problem, please check this site to
verify that you have the latest version of zlib; otherwise get the latest
version and check whether the problem still exists or not.

PLEASE read DLL_FAQ.txt, and the the zlib FAQ http://zlib.net/zlib_faq.html
before asking for help.


Manifest:

The package zlib-1.2.8-win32-x86.zip will contain the following files:

  README-WIN32.txt This document
  ChangeLog        Changes since previous zlib packages
  DLL_FAQ.txt      Frequently asked questions about zlib1.dll
  zlib.3.pdf       Documentation of this library in Adobe Acrobat format

  example.exe      A statically-bound example (using zlib.lib, not the dll)
  example.pdb      Symbolic information for debugging example.exe

  example_d.exe    A zlib1.dll bound example (using zdll.lib)
  example_d.pdb    Symbolic information for debugging example_d.exe

  minigzip.exe     A statically-bound test program (using zlib.lib, not the dll)
  minigzip.pdb     Symbolic information for debugging minigzip.exe

  minigzip_d.exe   A zlib1.dll bound test program (using zdll.lib)
  minigzip_d.pdb   Symbolic information for debugging minigzip_d.exe

  zlib.h           Install these files into the compilers' INCLUDE path to
  zconf.h          compile programs which use zlib.lib or zdll.lib

  zdll.lib         Install these files into the compilers' LIB path if linking
  zdll.exp         a compiled program to the zlib1.dll binary

  zlib.lib         Install these files into the compilers' LIB path to link zlib
  zlib.pdb         into compiled programs, without zlib1.dll runtime dependency
                   (zlib.pdb provides debugging info to the compile time linker)

  zlib1.dll        Install this binary shared library into the system PATH, or
                   the program's runtime directory (where the .exe resides)
  zlib1.pdb        Install in the same directory as zlib1.dll, in order to debug
                   an application crash using WinDbg or similar tools.

All .pdb files above are entirely optional, but are very useful to a developer
attempting to diagnose program misbehavior or a crash.  Many additional
important files for developers can be found in the zlib127.zip source package
available from http://zlib.net/ - review that package's README file for details.


Acknowledgments:

The deflate format used by zlib was defined by Phil Katz.  The deflate and
zlib specifications were written by L.  Peter Deutsch.  Thanks to all the
people who reported problems and suggested various improvements in zlib; they
are too numerous to cite here.


Copyright notice:

  (C) 1995-2012 Jean-loup Gailly and Mark Adler

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  Jean-loup Gailly        Mark Adler
  jloup@gzip.org          madler@alumni.caltech.edu

If you use the zlib library in a product, we would appreciate *not* receiving
lengthy legal documents to sign.  The sources are provided for free but without
warranty of any kind.  The library has been entirely written by Jean-loup
Gailly and Mark Adler; it does not include third-party code.

If you redistribute modified sources, we would appreciate that you include in
the file ChangeLog history information documenting your changes.  Please read
the FAQ for more information on the distribution of modified source versions.

To build zlib using the Microsoft Visual C++ environment,
use the appropriate project from the projects/ directory.
