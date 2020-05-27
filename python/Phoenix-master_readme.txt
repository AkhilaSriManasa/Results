=========================
wxPython Project Phoenix
=========================

.. image:: demo/bitmaps/splash.png
   :align: center


Introduction
------------

Welcome to wxPython's Project Phoenix! Phoenix is the improved next-generation
wxPython, "better, stronger, faster than he was before." This new
implementation is focused on improving speed, maintainability and
extensibility. Just like "Classic" wxPython, Phoenix wraps the wxWidgets C++
toolkit and provides access to the user interface portions of the wxWidgets
API, enabling Python applications to have a native GUI on Windows, Macs or
Unix systems, with a native look and feel and requiring very little (if any)
platform specific code.

.. note:: 
    This document is primarily intended for those who will be working on
    wxPython, or at least building with the source code fetched directly from
    GitHub. If that's not you then please refer to the instructions at the
    `wxPython website <https://wxpython.org/pages/downloads/>`_ about how to get
    the current release of wxPython for your platform and chosen Python
    environment.

.. contents:: **Contents**


How to build wxPython Phoenix
-----------------------------

First of all, this README is intended primarily for those who want to build
wxPython from a workspace checked out from the wxPython Phoenix repository. If
you are not making changes to wxPython, or needing to build it for some
unsupported compiler or some other hardware architecture, then you probably do
not need to put yourself through the pain for building in this way. It's a
complicated build, and can sometimes be confusing even for the experts.
Instead, if the binaries available at PyPI are not what you need then you can
use pip to build from the released source archives, or from the source archives
created in the pre-release snapshot builds. See the notes about it at: 

* https://wxpython.org/pages/downloads/
* https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip


Next, review the section below about prerequisites.

All aspects of the wxPython Phoenix build are managed through a series of
commands provided by the build.py script. There is also a setup.py script
available for those who are used to the standard distutils or setuptools types
of builds. The setup.py script assumes that all of the code generation steps
have already been performed, and so it is suitable for use when building from
a source snapshot tarball or when using easy_install or pip. The setup.py
script will delegate to build.py for the actual build, and build.py will
delegate to setup.py when doing setuptoolsy things like performing an install
or building a wheel.

Using the build.py script allows for greater control over the build process
than setup.py does, including commands for performing the various
code-generation steps. So developers working on Phoenix itself or building
from a Git checkout, instead of a source snapshot tarball, should be using
the build.py script. The build.py script provides a fairly simple
command-line interface consisting of commands and options. To see the full
list run ``python build.py --help``. The most important commands are listed
below.

**Windows Users NOTE:** If you are building Phoenix on Windows and have a
non-English language installation of Microsoft Visual Studio then you may
need to set the code page in your console window in order to avoid Unicode
decoding errors. For example::

    chcp 1252
    python build.py <build commands>...

In addition, some tasks within the build currently expect to be able to use
Cygwin on Windows (https://www.cygwin.com/) to do its work. If you have
Cygwin installed in one of the default locations (c:\\cygwin or c:\\cygwin64)
then all is well. If you have it installed somewhere else then you can set
CYGWIN_BASE in the environment and the build tool will use that for the base
dir.

On the other hand, if you just want to do a standard setuptools-style build
using setup.py and are using a full source tarball, then you can stop reading
at this point. If you want to build from a source repository checkout, or
need to make changes and/or to regenerate some of the generated source files,
then please continue reading.


Building wxWidgets
------------------

Since build.py will, by default, build both wxWidgets and Phoenix you will
need the wxWidgets code as well. The source tarballs already include both
wxWidgets and the Phoenix source code, so if you are getting your copy of the
source code that way then you are all set. If you are fetching it from GitHub
you will need to do an additional step. The git repository is set up to bring
in the wxWidgets code as a git "submodule" so after cloning the Phoenix
repository, you can get the wxWidgets source with these commands::

  $ git submodule update --init --recursive

This will clone the wxWidgets repo into: ``Phoenix/ext/wxWidgets``. Once the
submodule is updated, the build script should be able to build wxWidgets.

If you would rather use an already built and installed wxWidgets then that is
possible as well by changing some options, see ``python build.py --help`` for
details. However be aware that doing so will require a wxWidgets that is
**very** close to the same age as the Phoenix code, at least for the
unreleased preview snapshots. In other words, the wxWidgets build should use
code from the wxWidgets source repository within a few days of when the
Phoenix code was checked out. Currently the master branch of Phoenix is
tracking the master branch of wxWidgets.

On the other hand, it is probably best to just let wxPython build and bundle
wxWidgets. The build tools will by default build wxWidgets in a way that
allows it to be bundled with the wxPython extension modules as part of the
wxPython package, meaning it can peacefully coexist with any wxWidgets
libraries you may already have installed. This bundling of the wx shared
libraries works on Windows, OSX and Linux, and probably any other unix-like
system using shared libraries based on the ELF standard. The libraries are
built in such a way that they are relocatable, meaning that they do not have
to be in a fixed location on the filesystem in order to be found by the
wxPython extension modules. This also means that you can do things like use
``pip`` to install a wxPython wheel in one or more virtual environments, move
the wx package to a versioned folder, or even move it into your own project
if desired, all without needing to rebuild the binaries. (Assuming that
compatible Pythons are being used in all cases of course.)

The build phase of the build.py script will copy the results of the wxWidgets
and Phoenix builds into the wx folder in the Phoenix source tree. This will
allow you to run and test Phoenix directly from the source tree without
installing it, if desired. You just need to set ``PYTHONPATH`` appropriately,
or you can use ``python setup.py develop`` or ``pip install -e .`` to install
an .egg-link file in your current Python site-packages folder that will point
to the folder where you built wxPython Phoenix. When you are finished testing
you can then use the install or one of the bdist commands like you normally
would for other Python packages.



Important build.py commands
---------------------------

The following ``build.py`` commands are required to be able to build Phoenix
from scratch. In other words, from a pristine source tree with none of the
generated code present yet. They can be run individually or you can specify
all of them on a single command line, in the order given. Once a command has
succeeded in one run of build.py there is no need to run that command again in
a later run, unless you've changed something which that command has the
responsibility to process. Many of the commands require the results of the
earlier commands, so at least the first time you run the build you will need
to use all 4 of the commands (or their equivalents for composite commands) in
the given order.

* **dox**: Builds the XML files from the wxWidgets documentation source,
  which will be used as input for the etg command.

* **etg**: Extracts information from the dox XML files, runs hand-written
  tweaker code on the extracted data structures, and runs various generators
  on the result to produce code for the next steps. The code being run for
  each item in this step is located in the etg folder in the Phoenix source
  tree.

* **sip**: This command processes the files generated in the etg command
  and produces the C++ code that will become the Python extension modules for
  wxPython Phoenix.

* **build**: Build both wxWidgets and wxPython. There are additional
  commands if you want to build just one or the other. The results will be
  put in the Phoenix/wx folder, and can be used from there without
  installation if desired, by setting PYTHONPATH so the Phoenix/wx package
  dir is found by Python.

Some other useful commands and options are:

* **clean**: Clean up the build products produced by prior runs of
  build.py. There are additional clean commands that will let you clean up
  just portions of the build if needed.

* **touch**: Updates the timestamp on all of the etg scripts, so they will
  be forced to be run in the next build. This is useful when a change has
  been made to the wxWidgets documentation that needs to be propagated
  through the build since the etg command doesn't yet do full dependency
  checking of the input.

* **M.N**: This is the Major.Minor version number of the Python that the
  extension modules will be built for, such as "3.3". This allows you to run
  build.py with a different Python than what you are building for, which is
  handy for things like buildbots running in a virtualenv for one Python
  that need to be able to run builds for other versions too.

  If build.py is not able to find the correct Python given the M.N on the
  command line then you can specify the full path to the python executable you
  want to use with the ``--python`` option.

* **test**: Runs all of Phoenix's unittests.

* **--nodoc**: This option turns off the sphinx generator when running the
  etg scripts. If you don't plan on generating the documentation then this
  will speed up the processing of the etg command.

Please see the output of ``python build.py --help`` for information about
commands and options not mentioned here. And, as always, if there is any
discrepancy between this document and the source code in the build.py script,
then the source code is correct. ;-)

The build.py script will download doxygen, sip and waf for your platform as
needed if they are not already in your Phoenix/bin folder. If prebuilt
versions of these tools are not available for your platform then build.py
will bail out with an error message. To continue with the build you will need
to acquire copies of the tool that will work on your platform and can then
tell build.py where to find it using an environment variable, as described in
the error message.


Example build command-lines
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To do a complete build from a totally clean git workspace, you will
need to use several of the commands listed above.  For example::

    python build.py dox etg --nodoc sip build

Subsequent builds can leave out some of the commands if there were no
changes which would require those commands to be run again.  For
example, if you wanted to just rebuild the Phoenix extension modules
you could do this::

    python build.py build_py

If you've changed one of the etg files and need to regenerate and
rebuild the source affected by that change, then you can use a command
like this::

    python build.py etg --nodoc sip build build_py



Project directory structure
---------------------------

There are a lot of subfolders in this directory, here is a brief
explanation to help a newbie find their way around.

* **build**: Intermediate files produced by the build process are stored
  here. This folder should not be committed to a source repository.

* **buildtools**: This is a Python package containing modules that are used
  from build.py and setup.py and which assist with configuring and running
  the build.

* **etg**: This is where the "Extractor-Tweaker-Generator" scripts are stored.
  These scripts are invoked by the build and they will read the XML files
  produced by Doxygen and will produce interface definition files for SIP.

* **etgtools**: This Python package contains modules which assist with the
  parsing of the XML files, tweaking the collection of objects produced by
  the parser, and also the backend generation of code or documentation.

* **ext**: This folder holds the source for external projects used by
  Phoenix, (currently just wxWidgets) as git submodules. This allows Phoenix
  to use a specific revision of the code in the other projects and not depend
  on the developer fetching the correct version of the code on their own.

  When you first checkout the Phoenix source using git you will need to tell
  git to also fetch the submodules, like this::

    cd Phoenix
    git submodule init
    git submodule update --recursively

* **sip/gen**: The code (.sip files) produced by the ETG scripts is placed
  in this folder.

* **sip/cpp**: The code produced when running SIP is put in this folder. It
  will be C++ source and header files, and also some extra files with
  information about the source files produced, so the build knows what files
  to compile.

* **sip/siplib**: This is a copy of the SIP runtime library. We have our
  own copy so it can be included with the wxPython build as an extension
  module with a unique name (``wx.siplib``) and to not require a runtime
  dependency on SIP being installed on the target system. 3rd party
  extensions that want to integrate with wxPython should ensure that the
  sip.h they ``#include`` is the one in this folder.

* **src**: This folder is for any other source code (SIP, C++, Python, or
  anything else) that is edited by hand instead of being generated by some
  tool.

* **wx**: This is the top of the wxPython package. For an in-place build the
  extension modules and any associated files will be put into this folder.
  Subfolders contain pure-python subpackages of the wx package, such as
  wx.lib, etc.



Naming of files
---------------

To help keep things a little easier when looking for things that need to be
worked on, the file names in the Phoenix project will mirror the names of the
files in the wxWidgets interface headers folder. For example, if there is a
``interface/wx/FOO.h`` and we are processing the XML produced for that file
then the ETG script for the classes and other items will be named
``etg/FOO.py`` and it will produce ``sip/gen/FOO.sip``, unit tests will be in
``unittests/test_FOO.py``, and so on.

In most cases more than one ETG/SIP file will be used to create a single
Python extension module. In those cases there will be one ETG script used to
bring all the others together into the single extension module (by using the
back-end generator's include feature for example.) The names of those scripts
will have a leading underscore, such as ``etg/_core.py``, and all the scripts
that are intended to be included in that extension module should specify that
name in their MODULE variable.


Prerequisites
-------------

The following are some tips about what is required to build Phoenix for
yourself. There are likely some other things that may not have been mentioned
here, if you find something else that should be mentioned then please submit
a PR for updating this document.


**Windows**

All the source code needed for wxWidgets and wxPython Phoenix are
included in the wxWidgets and Phoenix source trees. In addition to a
stock Python installation you will also need a copy of Visual Studio 2008
(for Python2.7 compatibility) or Visual Studio 2015 (for Python 3.x
support). It should also be possible to build using Mingw32, but there
will need to be some changes made to the build scripts to support that.

You may also want to get a copy of the MS SDK in order to have newer
definitions of the Windows API. I typically use 7.0 or 7.1 with Visual
Studio 2008.

Unfortunately Microsoft no longer distributes Visual Studio 2008. But don't
panic! They have recently made available a "Microsoft Visual C++ Compiler for
Python 2.7" package, which can also be used for building Phoenix for Python
2.7. Plus it's free! You can get it at:
http://www.microsoft.com/en-us/download/details.aspx?id=44266

If you want to build Phoenix with debug info then you will need to first
build a debug version of Python, and then use that Python (python_d.exe) to
build Phoenix.


**Linux**

On Ubuntu the following development packages and their dependencies
should be installed in order to build Phoenix. Other debian-like distros
will probably also have these or similarly named packages available.
Extrapolate other package names accordingly for other linux distributions
or other unixes.

* dpkg-dev
* build-essential
* python3.7-dev and libpython3.7-dev  # use appropriate Python version here
* freeglut3-dev 
* libgl1-mesa-dev 
* libglu1-mesa-dev 
* libgstreamer-plugins-base1.0-dev 
* libgtk-3-dev 
* libjpeg-dev 
* libnotify-dev 
* libpng-dev
* libsdl2-dev 
* libsm-dev 
* libtiff-dev 
* libwebkit2gtk-4.0-dev 
* libxtst-dev

If you are building for GTK2 then you'll also need these packages and
their dependencies:

* libgtk2.0-dev
* libwebkitgtk-dev


If You use a custom built python in a non standard location, You need to
compile python with the --enable-shared option.

**Mac OSX**

Like the Windows platform all the source and libs you need for building
Phoenix on OSX are included in the wxWidgets and Phoenix source trees, or
by default on the system. In addition you will need to get the Xcode
compiler and SDKs, if you don't already have it, from
https://developer.apple.com/ (free registration required). You should
also install the command line tools for your version of Xcode and OSX.
This can usually be done from within Xcode or via a separate installer
package.

Also like on Windows, using the same or similar compiler that was used to
build Python usually helps things to work better and have a better chance
for success. For example, the stock Python 2.7 will try to use "gcc-4.2"
when building extensions, but newer versions of Xcode may not have that
command available. I am currently using Xcode 7.1.1.

If all else fails it is not too hard to build Python yourself using
whatever Xcode you have installed, and then use that Python when building
Phoenix.


Help and Helping
----------------

Most discussions about Phoenix happen on the wxPython-dev google group
(a.k.a. the wxPython-dev mail list.) If you have questions or would like to
get involved please subscribe to the group at
https://groups.google.com/forum/#!forum/wxpython-dev and join in.


Latest Snapshot Builds
----------------------

You can find snapshots of the latest wxPython Phoenix build files,
including source snapshots, wheels files for Windows and Mac, and etc. at:
https://wxpython.org/Phoenix/snapshot-builds/.  These files are built at most
once per day, on any day that has had a commit to the master branch.


.. image:: docs/phoenix-fire-md.png
   :width: 100%
-r requirements/devel.txt
<!-- For bugs or other problems please provide the following details in addition to
     your issue report, if applicable. See also https://wxpython.org/pages/how-to-submit-issue/

     For issues about building on Linux, please read this page before reporting it here:
     https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/
-->

**Operating system**:
**wxPython version & source**:          <!-- pypi, self-built, etc. -->
**Python version & source**:            <!-- stock, anaconda, EDM, distro, self-built, etc. -->

**Description of the problem**:

<!-- if possible please include a small runnable application that demonstrates the problem -->

```python
# Put code sample here
```
<!-- Be sure to set the issue number that this PR fixes or implements below, and give
     a good description. If this PR is for a new feature or enhancement, then it's
     okay to remove the "Fixes #..." below, but be sure to give an even better
     description of the PR in that case.

     See also https://wxpython.org/pages/contributor-guide/  -->

Fixes #NNNN

Buildbot Master Config
----------------------

The master.cfg file in this folder is the configuration file for Project
Phoenix's buildbot, running at http://buildbot.wxpython.org:8011/ This file
is the master copy and is kept here in order to keep it under revision
control. It is *NOT* automatically copied to the build master when it is
updated and committed and must be copied manually. This is to help avoid
security issues or problems resulting from DSM's by somebody who has commit
access to the source repository but does not know what they are doing with
Buildbot.

Developers with the proper SSH keys can copy the file and reconfigure the
server with these commands:

scp buildbot/master.cfg  wxpybb@buildbot.wxpython.org:/home/wxpybb/bb2
ssh wxpybb@buildbot.wxpython.org "cd /home/wxpybb/bb2 && ./reconfig"

To run the main demo in this directory, execute demo.py.  In other
words, one of the following commands should do it:

       demo.py
       python demo.py
       pythonw demo.py

Name	Type	Platform	Location	Availability	Description
WebReuser	Development	Windows 95, Windows NT, HPUX 9.05 and 10.2, Solaris 2.4 and 2.5	http://www.stablesoft.com	Evaluation	WebReuser is a re-use tool from Hitachi Europe Limited. WebReuser is a tool that simplifies software reuse. Its ability to track, schematize and search documents makes it the ideal way to understand C++ code. These features also make WebReuser an ideal tool to classify any Web resource. WebReuser can even be used for more general documentation management tasks.
MacAnova	Development	Windows, Motif, Mac	http://www.stat.umn.edu/~gary/macanova/macanova.home.html	Free	A large statistical application from the School of Statistics, University of Minnesota. It is based on a modified version of wxWindows 1.65.
Hardy	Development	Win 3.1, WIN32, Motif (Sun only)	http://www.aiai.ed.ac.uk/~hardy/	Freeware for personal and academic use	A hypertext-based diagramming and knowledge-based system development tool, with NASA's CLIPS built-in. It is a superset of wxCLIPS.
wxCLIPS	Development	Win 3.1, WIN32, Motif, XView	http://web.ukonline.co.uk/julian.smart/wxclips	Freeware	A GUI development environment for CLIPS applications.
wxPython	Development	wxWindows 2 for the new version	http://alldunn.com/wxPython/	Freeware	Python/wxWindows combination by Robin Dunn and Harri Pasanen. Python is an elegant object-oriented, interpreted language that runs on many platforms.
MrEd	Development	Win 3.1, WIN32, Motif, XView	http://www.cs.rice.edu/CS/PLT/packages/mred/	Freeware	MrEd is a combined editor and Scheme development environment by Matthew Flatt.
WXLisp	Development	Win 3.1, WIN32, Motif, XView	http://www.cadlab.de/~lipuser/wxlisp/wxlisp.html	Freeware	A combination of wxWindows and XLisp.
Scriptum	Development	Motif	http://www.isoft.com.ar/eng/products/system/scriptum.html	Freeware	Graphical editor with visual highlighting, navigation/browsing, undo, class browser for C++ and Java, source code management, file locking, remote editing using ftp, configurable.
WipeOut	Development	XView/Linux	http://www.softwarebuero.de/wipeout-eng.html	Giftware	WipeOut is an integrated development environment for C++ projects, available for Linux/XView. The authors are working on versions for SunOS/Solaris. Source is available for porting to other platforms.
OPL	Development	Win 3.1, WIN32, Motif, XView	http://www.ozemail.com.au/~adavison/	Freeware	Object Prolog is a portable implementation of Prolog by Andrew Davison, with object-oriented extensions, entirely written in C++. In the initial version, a binding to wxWindows is available. In the revamped version, this binding has not been written yet.
Dataplore	Graphics and sound	Windows, other?	http://www.datan.de/dataplore	Commercial	Data visualisation tool, from Datan
VCG Tool	Graphics and sound	Win 3.1, WIN32, Motif, XView	http://www.cs.uni-sb.de:80/RW/users/sander/html/gsvcg1.html	Freeware	A graph layout tool similar to GraphPlace, but with extensions. Very nice indeed!
Y.E.S.	Graphics and sound	Win 3.1, WIN32, XView (Linux)	ftp://ftp.musik.uni-essen.de/pub/EsAC/program/	Shareware	Monophonic notation program.
JAZZ	Graphics and sound	XView (Linux)	http://rokke.aug.hiagder.no/per/jazz.html	Freeware	A MIDI sequencer for Linux.
ISP	Graphics and sound	Win 3.1, WIN32, Motif, XView	ftp://www.remstar.com/pub/wxwin/contrib/isp-100/	Freeware	Image and sound player educational tool.
ClockWorks	Graphics and sound	Win 3.1, WIN32, Motif, XView	http://web.ukonline.co.uk/Members/julian.smart/freesoft.html#clockworks	Freeware	A configurable analogue clock, with a collection of 'fine art' faces. By Julian Smart.
M	Miscellaneous	Windows 95, Windows NT, Linux	http://www.phy.hw.ac.uk/~karsten/M/index.html	GPL	M is a cross-platform e-mail application. It will be available for X11/Unix and Windows platforms, supporting a wide range of e-mail transfer protocols as well as including full MIME support. M's wealth of features and ease of use make it one of the most powerful MUAs available, providing a consistent and intuitive interface across all platforms.
Boolean	Miscellaneous	Windows 95, Windows NT, Solaris	http://www.xs4all.nl/~kholwerd/bool.html	Freeware	A GDSII CAD file format viewer, and program to perform boolean operations on sets of 2D polygons. By Klaas Holwerda.
TimeMan	Miscellaneous	wxGTK, Unix	http://www.bgif.no/neureka/TimeMan/	Freeware	A time manager, written using wxGTK
Forty Thieves	Miscellaneous	Motif, Windows	apps/forty/forty.htm	Freeware	A fiendish patience game, by Chris Breeze. A nice demo of what's possible with wxWindows.
Lean Integration Platform	Miscellaneous	Windows NT, various flavours of UNIX	http://www.c-lab.de/~lipuser/lip	To be decided	LIP is a workflow-oriented tool integration system which uses wxLisp (and thus wxWindows) as an implementation basis. Lisp combined with the wxWindows bindings make up the compatible extension language platform of the system.
wxWeb	Miscellaneous	Win 3.1, WIN32, Motif	ftp://www.remstar.com/pub/wxwin/contrib/wxweb	Freeware	Andrew Davison's Web browser, with SimSock portable socket library and wxHtml canvas. Includes an http server for UNIX and Windows.
SANTIS	Miscellaneous	Win 3.1, Windows 95, Linux, Solaris OpenLook and Motif, Silicon Graphics	http://www.physiology.rwth-aachen.de/bs/santis/	Free for non-commercial use	SANTIS is a software tool designed for the analysis of signals and time series data of any kind, in particular for scientific purposes. It was developed at the Laboratory of Biomedical Systems Analysis, Institute of Physiology at the University of Aachen, Germany.
Xbaies	Miscellaneous	Win 3.1, WIN32, Motif, XView	xbaies.htm	Freeware	A shell for building Bayesian network models, by Robert Cowell.
wxTinyBB	Miscellaneous	Win 3.1, WIN32, Motif, XView	ftp://www.remstar.com/pub/wxwin/contrib/wxtinybb	Freeware/commercial	A tiny blackboard shell demo showing an embedded (commercial) Prolog engine. Demo written by Arvindra Sehmi. A good example of a nice interface using wxWindows.
Gambit	Miscellaneous	Win 3.1, WIN32, Motif, XView	http://www.hss.caltech.edu/~gambit/Gambit.html	Freeware	A large wxWindows application with source, and features such as a table control with printing.
Tex2RTF	Miscellaneous	Win 3.1, WIN32, Motif, XView	http://web.ukonline.co.uk/julian.smart/tex2rtf	Freeware	Converts subset of LaTeX syntax to WinHelp, wordprocessor RTF, HTML, and wxHelp. As used for wxWindows documentation.
wxPoem	Miscellaneous	Win 3.1, WIN32, Motif, XView	none.htm	Freeware	A poetry display program for wxWindows. Included as a sample in the wxWindows distribution.
Sonar tracking software	Miscellaneous	See Web site	http://www.desertstar.com	Demonstration	Miscellaneous sonar tracking software from Desert Star Systems, who use wxWindows for all their Windows-based software.
Name	Research software	Platform	Location	Availability	Description
DisCo	Research software	N/A	http://www.cs.tut.fi/laitos/DisCo/tool.fm.html	N/A	A tool for specification of reactive systems.
CAFE	Research software	N/A	cafe.htm	N/A	Cellular Analysis of Fire and Extinction
CODA	Research software	See Web site	http://www.ozemail.com.au/~mbedward/coda/coda.html	See Web site	CODA assists in the design of networks of nature reserves or protected areas. It has been used for major reserve planning studies, as a teaching resource and for research into conservation planning methods.
EGRESS	Research software	N/A	http://www.aiai.ed.ac.uk/~jimd/Egress2/projInfo_contents.html	N/A	An evacuation decision model.
ACT	Research software	N/A	none.htm	N/A	A general process and tracker and automator being built at NASA.
Rectangular nesting program	Research software	N/A	http://www.elec-eng.leeds.ac.uk/een5mpd/research.html	N/A	Optimized layout of rectangles on a page.
Finite element post processor	Research software	N/A	http://www.ime.auc.dk/afd3/odessy/manuals/index.htm	N/A	Finite element postprocessor, produced at Aalborg University in Denmark by John Rasmussen and Erik Lund.
__          __ _____  _____
\ \        / /|_   _||  __ \
 \ \  /\  / /   | |  | |__) | ____
  \ \/  \/ /    | |  |  ___/ |_  /
   \  /\  /    _| |_ | |      / /
    \/  \/    |_____||_|     /___|
WIPz Phoenix Demos Checklist
"""
[X] Demo Works! Woot :)
[ ] Demo Still NEEDS work, has missing libs, other. :(
"""
When all done, this checklist.txt can be discarded.

Frames and Dialogs Demos
========================
[X] AUI_DockingWindowMgr
[X] AUI_MDI
        TODO
        Not working properly
[X] Dialog
[X] Frame
[X] MDIWindows
[X] MiniFrame
[X] Wizard

Common Dialogs Demos
====================
[X] AboutBox
[X] ColourDialog
[X] DirDialog
[X] FileDialog
[X] FindReplaceDialog
[X] FontDialog
[X] MessageDialog
[X] MultiChoiceDialog
[X] PageSetupDialog
[X] PrintDialog
[X] ProgressDialog
[X] SingleChoiceDialog
[X] TextEntryDialog

More Dialogs Demos
==================
[X] ImageBrowser
[X] ScrolledMessageDialog

Core Windows/Controls Demos
===========================
[X] BitmapButton
[X] Button
[X] CheckBox
[X] CheckListBox
[X] Choice
[X] ComboBox
[X] CommandLinkButton
[X] DVC_CustomRenderer
[X] DVC_DataViewModel
[X] DVC_IndexListModel
[X] DVC_ListCtrl
[X] DVC_TreeCtrl
[X] Gauge
[X] Grid
[X] Grid_MegaExample
[X] GridLabelRenderer
[X] ListBox
[X] ListCtrl
[X] ListCtrl_virtual
[X] ListCtrl_edit
[X] Menu
[X] PopupMenu
[X] PopupWindow
[X] RadioBox
[X] RadioButton
[X] SashWindow
[X] ScrolledWindow
[X] SearchCtrl
[X] Slider
[X] SpinButton
[X] SpinCtrl
[X] SpinCtrlDouble
[X] SplitterWindow
[X] StaticBitmap
[X] StaticBox
[X] StaticText
[X] StatusBar
[X] StockButtons
[X] TextCtrl
[X] ToggleButton
[X] ToolBar
[X] TreeCtrl
[X] Validator

"Book" Controls Demos
=====================
[X] AUI_Notebook
        TODO
        Not working properly
[X] Choicebook
[X] FlatNotebook
[X] Listbook
[X] Notebook
[X] Toolbook
[X] Treebook

Custom Controls Demos
=====================
[X] AnalogClock
[X] ColourSelect
[X] ComboTreeBox
[X] Editor
[X] GenericButtons
[X] GenericDirCtrl
[X] ItemsPicker
[ ] LEDNumberCtrl
[X] MultiSash
[X] PlateButton
[X] PopupControl
[X] PyColourChooser
[X] TreeListCtrl
        TODO
        still need to adjust for selected image: smiley

AGW Demos
=========
[X] AdvancedSplash
[X] AquaButton
[X] AUI
[X] BalloonTip
[X] ButtonPanel
[X] CubeColourDialog
[X] CustomTreeCtrl
[ ] FlatMenu
        TODO
        Crashes on opening menu
[X] FlatNotebook
[X] FloatSpin
[X] FoldPanelBar
[X] FourWaySplitter
[X] GenericMessageDialog
[X] GradientButton
[X] HyperLinkCtrl
[X] HyperTreeList
[X] AGWInfoBar
[X] KnobCtrl
[X] LabelBook
[X] MultiDirDialog
[X] PeakMeter
[X] PersistentControls
[X] PieCtrl
[X] PyBusyInfo
[X] PyCollapsiblePane
[X] PyGauge
[X] PyProgress
        TODO
        Also cancel button doesn't work
[X] RibbonBar
[X] RulerCtrl
[X] ShapedButton
[X] ShortcutEditor
[X] SpeedMeter
        TODO
        Traceback (most recent call last):
[X] SuperToolTip
[X] ThumbnailCtrl
[X] ToasterBox
        TODO
        is crashing on/after toasty
[X] UltimateListCtrl
[X] XLSGrid
[X] ZoomBar

More Windows/Controls Demos
===========================
[X] ActiveX_FlashWindow
[X] ActiveX_IEHtmlWindow
[X] ActiveX_PDFWindow
[X] BitmapComboBox
[X] Calendar
[X] CalendarCtrl
        TODO
        could use some work/cleanup
[X] CheckListCtrlMixin
[X] CollapsiblePane
[X] ComboCtrl
[X] ContextHelp
        TODO
        ContextHelp doesn't seem to be working yet tho...
[X] DatePickerCtrl
[ ] DynamicSashWindow
[X] EditableListBox
[X] ExpandoTextCtrl
        TODO
        Traceback (most recent call last):
          File "ExpandoTextCtrl.py", line 82, in OnSetMaxHeight
            dlg = wx.NumberEntryDialog(self, "", "Enter new max height:",
        AttributeError: 'module' object has no attribute 'NumberEntryDialog'
[X] FancyText
[X] FileBrowseButton
[X] FloatBar
[X] FloatCanvas
[X] HtmlWindow
        TODO
        Traceback (most recent call last):
          File "HtmlWindow.py", line 177, in OnViewSource
            source = self.html.GetParser().GetSource()
        AttributeError: 'MyHtmlWindow' object has no attribute 'GetParser'
[X] HTML2_WebView
[X] InfoBar
[X] IntCtrl
[X] MVCTree
[X] MaskedEditControls
[X] MaskedNumCtrl
[X] MediaCtrl
[X] MultiSplitterWindow
[X] OwnerDrawnComboBox
[X] Pickers
[ ] PropertyGrid
[X] PyCrust
[X] PyPlot
[X] PyShell
[X] ResizeWidget
[X] RichTextCtrl
[X] ScrolledPanel
[ ] SplitTree
[X] StyledTextCtrl_1
[X] StyledTextCtrl_2
[X] TablePrint
[X] Throbber
[X] Ticker
[X] TimeCtrl
[X] TreeMixin
[X] VListBox

Window Layout Demos
===================
[X] GridBagSizer
[X] LayoutAnchors
[X] LayoutConstraints
[X] Layoutf
[X] RowColSizer
[X] ScrolledPanel
[X] SizedControls
[X] Sizers
[X] WrapSizer
[X] XmlResource
[X] XmlResourceHandler
[X] XmlResourceSubclass

Process and Events Demos
[X] DelayedResult
[X] EventManager
[X] KeyEvents
[X] Process
[X] PythonEvents
[X] Threads
[X] Timer
[ ] #'infoframe    # needs better explanation and some fixing

Clipboard and DnD Demos
=======================
[X] CustomDragAndDrop
        TODO
        DoodleDrop isn't showing upon drop
[X] DragAndDrop
        TODO
        TypeError: Invalid result type upon drops
[X] URLDragAndDrop

Using Images Demos
==================
[X] AdjustChannels
[X] AlphaDrawing
[X] AnimateCtrl
[X] ArtProvider
[X] BitmapFromBuffer
[X] Cursor
[X] DragImage
[X] Image
[X] ImageAlpha
[X] ImageFromStream
[X] Img2PyArtProvider
[X] Mask
[X] RawBitmapAccess
[X] Throbber

Miscellaneous Demos
===================
[X] AlphaDrawing
[X] Cairo
[X] Cairo_Snippets
[X] ColourDB
[ ] #'DialogUnits   # needs more explanations
[X] DragScroller
[X] DrawXXXList
[X] FileHistory
[X] FontEnumerator
[X] GraphicsContext
[X] GraphicsGradient
[X] GLCanvas
        TODO
        Cone not working
[X] I18N
[X] Joystick
        TODO
        Needs more work and tested with a joystick. I dont have one.
[X] MimeTypesManager
[X] MouseGestures
[X] OGL
[X] PDFViewer
[X] PenAndBrushStyles
[X] PrintFramework
[X] PseudoDC
[X] RendererNative
[X] ShapedWindow
[X] Sound
[X] StandardPaths
[X] SystemSettings
[X] UIActionSimulator
[X] Unicode
EMANCIPATION PROCLAMATION:
By the President of the United States of America:
A PROCLAMATION

  Whereas on the 22nd day of September, A.D. 1862, a proclamation
was issued by the President of the United States, containing,
among other things, the following, to wit:

  "That on the 1st day of January, A.D. 1863, all persons held as
slaves within any State or designated part of a State the people
whereof shall then be in rebellion against the United States shall
be then, thenceforward, and forever free; and the executive
government of the United States, including the military and naval
authority thereof, will recognize and maintain the freedom of such
persons and will do no act or acts to repress such persons, or any
of them, in any efforts they may make for their actual freedom.

  "That the executive will on the 1st day of January aforesaid,
by proclamation, designate the States and parts of States, if any,
in which the people thereof, respectively, shall then be in
rebellion against the United States; and the fact that any State
or the people thereof shall on that day be in good faith
represented in the Congress of the United States by members
chosen thereto at elections wherein a majority of the qualified
voters of such States shall have participated shall, in the
absence of strong countervailing testimony, be deemed conclusive
evidence that such State and the people thereof are not then
in rebellion against the United States."

  Now, therefore, I, Abraham Lincoln, President of the United
States, by virtue of the power in me vested as Commander-In-Chief
of the Army and Navy of the United States in time of actual armed
rebellion against the authority and government of the United States,
and as a fit and necessary war measure for supressing said
rebellion, do, on this 1st day of January, A.D. 1863, and in
accordance with my purpose so to do, publicly proclaimed for the
full period of one hundred days from the first day above mentioned,
order and designate as the States and parts of States wherein the
people thereof, respectively, are this day in rebellion against
the United States the following, to wit:

  Arkansas, Texas, Louisiana (except the parishes of St. Bernard,
Palquemines, Jefferson, St. John, St. Charles, St. James, Ascension,
Assumption, Terrebone, Lafourche, St. Mary, St. Martin, and Orleans,
including the city of New Orleans), Mississippi, Alabama, Florida,
Georgia, South Carolina, North Carolina, and Virginia (except the
forty-eight counties designated as West Virginia, and also the
counties of Berkeley, Accomac, Morthhampton, Elizabeth City, York,
Princess Anne, and Norfolk, including the cities of Norfolk and
Portsmouth), and which excepted parts are for the present left
precisely as if this proclamation were not issued.

  And by virtue of the power and for the purpose aforesaid, I do
order and declare that all persons held as slaves within said
designated States and parts of States are, and henceforward shall
be, free; and that the Executive Government of the United States,
including the military and naval authorities thereof, will
recognize and maintain the freedom of said persons.

  And I hereby enjoin upon the people so declared to be free to
abstain from all violence, unless in necessary self-defence; and
I recommend to them that, in all case when allowed, they labor
faithfully for reasonable wages.

  And I further declare and make known that such persons of
suitable condition will be received into the armed service of
the United States to garrison forts, positions, stations, and
other places, and to man vessels of all sorts in said service.

  And upon this act, sincerely believed to be an act of justice,
warranted by the Constitution upon military necessity, I invoke
the considerate judgment of mankind and the gracious favor
of Almighty God.

(signed)
ABRAHAM LINCOLN
-------------------------------------

On Jan. 1, 1863, U.S. President Abraham Lincoln declared free
all slaves residing in territory in rebellion against the federal
government. This Emancipation Proclamation actually freed few
people. It did not apply to slaves in border states fighting on
the Union side; nor did it affect slaves in southern areas already
under Union control. Naturally, the states in rebellion did not
act on Lincoln's order. But the proclamation did show Americans--
and the world--that the civil war was now being fought to end slavery.

Lincoln had been reluctant to come to this position. A believer
in white supremacy, he initially viewed the war only in terms of
preserving the Union. As pressure for abolition mounted in
Congress and the country, however, Lincoln became more sympathetic
to the idea. On Sept. 22, 1862, he issued a preliminary proclamation
announcing that emancipation would become effective on Jan. 1, 1863,
in those states still in rebellion. Although the Emancipation
Proclamation did not end slavery in America--this was achieved
by the passage of the 13TH Amendment to the Constitution on Dec.
18, 1865--it did make that accomplishment a basic war goal and
a virtual certainty.

DOUGLAS T. MILLER

Bibliography: Commager, Henry Steele, The Great Proclamation
(1960); Donovan, Frank, Mr. Lincoln's Proclamation (1964);
Franklin, John Hope, ed., The Emancipation Proclamation (1964).

-------------------------------------

Prepared by Gerald Murphy (The Cleveland Free-Net - aa300)
Distributed by the Cybercasting Services Division of the
  National Public Telecomputing Network (NPTN).

Permission is hereby granted to download, reprint, and/or otherwise
  redistribute this file, provided appropriate point of origin
  credit is given to the preparer(s) and the National Public
  Telecomputing Network.
This license applies to the "SourceCodePro-Regular.ttf" file.
Font Source: https://github.com/adobe-fonts/source-code-pro
-------------------------------------------------------------

Copyright 2010, 2012 Adobe Systems Incorporated (http://www.adobe.com/), with Reserved Font Name 'Source'. All Rights Reserved. Source is a trademark of Adobe Systems Incorporated in the United States and/or other countries.

This Font Software is licensed under the SIL Open Font License, Version 1.1.

This license is copied below, and is also available with a FAQ at: http://scripts.sil.org/OFL


-----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
-----------------------------------------------------------

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded, 
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting -- in part or in whole -- any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are
not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.
Name	Type	Platform	Location	Availability	Description
WebReuser	Development	Windows 95, Windows NT, HPUX 9.05 and 10.2, Solaris 2.4 and 2.5	http://www.stablesoft.com	Evaluation	WebReuser is a re-use tool from Hitachi Europe Limited. WebReuser is a tool that simplifies software reuse. Its ability to track, schematize and search documents makes it the ideal way to understand C++ code. These features also make WebReuser an ideal tool to classify any Web resource. WebReuser can even be used for more general documentation management tasks.
MacAnova	Development	Windows, Motif, Mac	http://www.stat.umn.edu/~gary/macanova/macanova.home.html	Free	A large statistical application from the School of Statistics, University of Minnesota. It is based on a modified version of wxWindows 1.65.
Hardy	Development	Win 3.1, WIN32, Motif (Sun only)	http://www.aiai.ed.ac.uk/~hardy/	Freeware for personal and academic use	A hypertext-based diagramming and knowledge-based system development tool, with NASA's CLIPS built-in. It is a superset of wxCLIPS.
wxCLIPS	Development	Win 3.1, WIN32, Motif, XView	http://web.ukonline.co.uk/julian.smart/wxclips	Freeware	A GUI development environment for CLIPS applications.
wxPython	Development	wxWindows 2 for the new version	http://alldunn.com/wxPython/	Freeware	Python/wxWindows combination by Robin Dunn and Harri Pasanen. Python is an elegant object-oriented, interpreted language that runs on many platforms.
MrEd	Development	Win 3.1, WIN32, Motif, XView	http://www.cs.rice.edu/CS/PLT/packages/mred/	Freeware	MrEd is a combined editor and Scheme development environment by Matthew Flatt.
WXLisp	Development	Win 3.1, WIN32, Motif, XView	http://www.cadlab.de/~lipuser/wxlisp/wxlisp.html	Freeware	A combination of wxWindows and XLisp.
Scriptum	Development	Motif	http://www.isoft.com.ar/eng/products/system/scriptum.html	Freeware	Graphical editor with visual highlighting, navigation/browsing, undo, class browser for C++ and Java, source code management, file locking, remote editing using ftp, configurable.
WipeOut	Development	XView/Linux	http://www.softwarebuero.de/wipeout-eng.html	Giftware	WipeOut is an integrated development environment for C++ projects, available for Linux/XView. The authors are working on versions for SunOS/Solaris. Source is available for porting to other platforms.
OPL	Development	Win 3.1, WIN32, Motif, XView	http://www.ozemail.com.au/~adavison/	Freeware	Object Prolog is a portable implementation of Prolog by Andrew Davison, with object-oriented extensions, entirely written in C++. In the initial version, a binding to wxWindows is available. In the revamped version, this binding has not been written yet.
Dataplore	Graphics and sound	Windows, other?	http://www.datan.de/dataplore	Commercial	Data visualisation tool, from Datan
VCG Tool	Graphics and sound	Win 3.1, WIN32, Motif, XView	http://www.cs.uni-sb.de:80/RW/users/sander/html/gsvcg1.html	Freeware	A graph layout tool similar to GraphPlace, but with extensions. Very nice indeed!
Y.E.S.	Graphics and sound	Win 3.1, WIN32, XView (Linux)	ftp://ftp.musik.uni-essen.de/pub/EsAC/program/	Shareware	Monophonic notation program.
JAZZ	Graphics and sound	XView (Linux)	http://rokke.aug.hiagder.no/per/jazz.html	Freeware	A MIDI sequencer for Linux.
ISP	Graphics and sound	Win 3.1, WIN32, Motif, XView	ftp://www.remstar.com/pub/wxwin/contrib/isp-100/	Freeware	Image and sound player educational tool.
ClockWorks	Graphics and sound	Win 3.1, WIN32, Motif, XView	http://web.ukonline.co.uk/Members/julian.smart/freesoft.html#clockworks	Freeware	A configurable analogue clock, with a collection of 'fine art' faces. By Julian Smart.
M	Miscellaneous	Windows 95, Windows NT, Linux	http://www.phy.hw.ac.uk/~karsten/M/index.html	GPL	M is a cross-platform e-mail application. It will be available for X11/Unix and Windows platforms, supporting a wide range of e-mail transfer protocols as well as including full MIME support. M's wealth of features and ease of use make it one of the most powerful MUAs available, providing a consistent and intuitive interface across all platforms.
Boolean	Miscellaneous	Windows 95, Windows NT, Solaris	http://www.xs4all.nl/~kholwerd/bool.html	Freeware	A GDSII CAD file format viewer, and program to perform boolean operations on sets of 2D polygons. By Klaas Holwerda.
TimeMan	Miscellaneous	wxGTK, Unix	http://www.bgif.no/neureka/TimeMan/	Freeware	A time manager, written using wxGTK
Forty Thieves	Miscellaneous	Motif, Windows	apps/forty/forty.htm	Freeware	A fiendish patience game, by Chris Breeze. A nice demo of what's possible with wxWindows.
Lean Integration Platform	Miscellaneous	Windows NT, various flavours of UNIX	http://www.c-lab.de/~lipuser/lip	To be decided	LIP is a workflow-oriented tool integration system which uses wxLisp (and thus wxWindows) as an implementation basis. Lisp combined with the wxWindows bindings make up the compatible extension language platform of the system.
wxWeb	Miscellaneous	Win 3.1, WIN32, Motif	ftp://www.remstar.com/pub/wxwin/contrib/wxweb	Freeware	Andrew Davison's Web browser, with SimSock portable socket library and wxHtml canvas. Includes an http server for UNIX and Windows.
SANTIS	Miscellaneous	Win 3.1, Windows 95, Linux, Solaris OpenLook and Motif, Silicon Graphics	http://www.physiology.rwth-aachen.de/bs/santis/	Free for non-commercial use	SANTIS is a software tool designed for the analysis of signals and time series data of any kind, in particular for scientific purposes. It was developed at the Laboratory of Biomedical Systems Analysis, Institute of Physiology at the University of Aachen, Germany.
Xbaies	Miscellaneous	Win 3.1, WIN32, Motif, XView	xbaies.htm	Freeware	A shell for building Bayesian network models, by Robert Cowell.
wxTinyBB	Miscellaneous	Win 3.1, WIN32, Motif, XView	ftp://www.remstar.com/pub/wxwin/contrib/wxtinybb	Freeware/commercial	A tiny blackboard shell demo showing an embedded (commercial) Prolog engine. Demo written by Arvindra Sehmi. A good example of a nice interface using wxWindows.
Gambit	Miscellaneous	Win 3.1, WIN32, Motif, XView	http://www.hss.caltech.edu/~gambit/Gambit.html	Freeware	A large wxWindows application with source, and features such as a table control with printing.
Tex2RTF	Miscellaneous	Win 3.1, WIN32, Motif, XView	http://web.ukonline.co.uk/julian.smart/tex2rtf	Freeware	Converts subset of LaTeX syntax to WinHelp, wordprocessor RTF, HTML, and wxHelp. As used for wxWindows documentation.
wxPoem	Miscellaneous	Win 3.1, WIN32, Motif, XView	none.htm	Freeware	A poetry display program for wxWindows. Included as a sample in the wxWindows distribution.
Sonar tracking software	Miscellaneous	See Web site	http://www.desertstar.com	Demonstration	Miscellaneous sonar tracking software from Desert Star Systems, who use wxWindows for all their Windows-based software.
Name	Research software	Platform	Location	Availability	Description
DisCo	Research software	N/A	http://www.cs.tut.fi/laitos/DisCo/tool.fm.html	N/A	A tool for specification of reactive systems.
CAFE	Research software	N/A	cafe.htm	N/A	Cellular Analysis of Fire and Extinction
CODA	Research software	See Web site	http://www.ozemail.com.au/~mbedward/coda/coda.html	See Web site	CODA assists in the design of networks of nature reserves or protected areas. It has been used for major reserve planning studies, as a teaching resource and for research into conservation planning methods.
EGRESS	Research software	N/A	http://www.aiai.ed.ac.uk/~jimd/Egress2/projInfo_contents.html	N/A	An evacuation decision model.
ACT	Research software	N/A	none.htm	N/A	A general process and tracker and automator being built at NASA.
Rectangular nesting program	Research software	N/A	http://www.elec-eng.leeds.ac.uk/een5mpd/research.html	N/A	Optimized layout of rectangles on a page.
Finite element post processor	Research software	N/A	http://www.ime.auc.dk/afd3/odessy/manuals/index.htm	N/A	Finite element postprocessor, produced at Aalborg University in Denmark by John Rasmussen and Erik Lund.
Each of the leaf items in the tree is a separate demo.  Click and learn!
Use the source Luke!
Many of the demos have some helpful overview text associated with them.  Simply click on the first tab in the notebook control after selecting the demo.  You can switch back and forth to the demo page as often as you like.
You can also view the source code for each demo by clicking on the second notebook tab.
This demo is a teaching tool.  The source code for each sample can be modified and you can see the results immediately!
Be sure to subscribe to the mail list.  Go to http://wxpython.org/maillist.php today!
The wxPyWiki is a place where wxPython users can help other users, and is a colaborative documentation system.  See http://wiki.wxpython.org.
You shouldn't pee on an electric fence!
The whole world is a tuxedo and you are a pair of brown shoes.
Cold hands, no gloves.
Learn to pause -- or nothing worthwhile can catch up to you.
Don't kiss an elephant on the lips today.
Grief can take care of itself; but to get the full value of a joy you must have somebody to divide it with. -- Mark Twain
Stay away from hurricanes for a while.
Beware of a dark-haired man with a loud tie.
Don't ask Robin what these quotes mean, he doesn't remember.
Your lucky number has been disconnected.
You single-handedly fought your way into this hopeless mess.
A few hours grace before the madness begins again.
Your fly might be open (but don't check it just now).
Never commit yourself!  Let someone else commit you.
Noise proves nothing.  Often a hen who has merely laid an egg cackles as if she laid an asteroid.   -- Mark Twain
The very ink with which all history is written is merely fluid prejudice.   -- Mark Twain
Excellent time to become a missing person.
Stay away from flying saucers today.
Look afar and see the end from the beginning.
Tomorrow, this will be part of the unchangeable past but fortunately, it can still be changed today.
It has long been an axiom of mine that the little things are infinitely the most important.  -- Sir Arthur Conan Doyle
I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve.  -- J. R. R. Tolkien
You are only young once, but you can stay immature indefinitely.
You look like a million dollars.  All green and wrinkled.
The difference between the right word and the almost right word is the difference between lightning and the lightning bug.  -- Mark Twain
The countdown had stalled at 'T' minus 69 seconds when Desiree, the first female ape to go up in space, winked at me slyly and pouted her thick, rubbery lips unmistakably -- the first of many such advances during what would prove to be the longest, and most memorable, space voyage of my career.                -- Winning sentence, 1985 Bulwer-Lytton bad fiction contest.
Q: Why haven't you graduated yet?  A: Well, Dad, I could have finished years ago, but I wanted my dissertation to rhyme.
You are scrupulously honest, frank, and straightforward.  Therefore you have few friends.
Don't you wish you had more energy... or less ambition?
Are you making all this up as you go along?  I am.
Kindness is a language which the deaf can hear and the blind can read.                -- Mark Twain
Don't let your mind wander -- it's too little to be let out alone.
Change your thoughts and you change your world.
Don't you feel more like you do now than you did when you came in?
Today is the tomorrow you worried about yesterday.
Caution: breathing may be hazardous to your health.
You will soon forget this.
Go not to the elves for counsel, for they will say both yes and no.                -- J.R.R. Tolkien
Today is the first day of the rest of your life.
Cheer Up!  Things are getting worse at a slower rate.
You are the only person to ever get this message.
You're almost as happy as you think you are.
Ships are safe in harbor, but they were never meant to stay there.
I must have a prodigious quantity of mind; it takes me as much as a week sometimes to make it up.                -- Mark Twain
If you stand on your head, you will get footprints in your hair.
All generalizations are false, including this one.                -- Mark Twain
You have the body of a 19 year old.  Please return it before it gets wrinkled.
Your ignorance cramps my conversation.
The brain is a wonderful organ; it starts working the moment you get up in the morning and does not stop until you get into the office. -- Robert Frost
By working faithfully eight hours a day, you may get to be a boss and work twelve hours a day.  -- Robert Frost
In three words I can sum up everything I've learned about life: it goes on. -- Robert Frost
If we get involved in a nuclear war, would the electromagnetic pulses from exploding bombs damage my videotapes?
The earth? Oh the earth will be gone in a few seconds...I'm going to blow it up. It's obstructing my view of Venus.  -- Marvin the Martian
There's that word again, 'heavy'. Why are things so heavy in the future? Is there a problem with the earth's gravitational pull? -- Dr Emmet Brown, "Back To The Future"
I'm Luke Skywalker, I'm here to rescue you.
It is good to have an end to journey towards; but it is the journey that matters, in the end.     -- Ursula K. Le Guin, "The Left Hand of Darkness"
I was ready for everything -- except what actually happened.
Flying is simple. You just throw yourself at the ground and miss. -- Douglas Adams, "So Long, and Thanks for the Fish"
Man has always assumed that he is more intelligent than dolphins because he has achieved so much--the wheel, New York, wars and so on -- while all the dolphins had ever done was muck about in the water having a good time. But, conversely, the dolphins had always believed that they were far more intelligent than man -- for precisely the same reasons. -- Douglas Adams, "So Long, and Thanks for the Fish"
I think animal testing is a terrible idea; they get all nervous and give the wrong answers. --A Bit of Fry and Laurie
All right, brain. You don't like me and I don't like you, but let's just do this and I can get back to killing you with beer. -- Homer Simpson
The most exciting phrase to hear in science, the one that heralds new discoveries, is not 'Eureka!' (I found it!) but 'That's funny ...' --Isaac Asimov
Always listen to experts. They'll tell you what can't be done and why. Then do it. --Robert Heinlein
Still waters run deep.
Premature optimization is the root of all evil.  -- Donald Knuth
If at first you don't succeed, you must be a programmer.
Building wxPython4 with Docker
==============================

Introduction
------------

Docker is a relatively lightweight system for deploying containers with a
specified set of software running within them. A Docker container is less than a
virtual machine, but more than a chroot, and will typically be much more
performant than a VM, (sub-second startup time, less resource hungry, etc.)
Typically they would be used for deploying "containerized applications", but a
docker image can easily be created with all that's needed for building software
too.

The files and folders in this subtree provide the Dockerfiles and scripts needed
to build the Docker images, as well as for using those images to build wxPython
wheels for various Linux distributions. A current set of images are available on
Docker Hub at https://hub.docker.com/r/wxpython4/build. There is an image there
tagged with the same names as those in the ./build folder. For example, as of
this writing you can pull images with these names and tags:

    wxpython4/build:centos-7
    wxpython4/build:debian-9
    wxpython4/build:debian-10
    wxpython4/build:fedora-29
    wxpython4/build:fedora-30
    wxpython4/build:ubuntu-14.04
    wxpython4/build:ubuntu-16.04
    wxpython4/build:ubuntu-18.04


Building Images
---------------

Since images are available on DockerHub there shouldn't be much need for
building them yourself, but just in case, here is how to do it. All images
can be built with a simple command like this::

    inv build-images 

And one or more specific images can be built like this::

    inv build-images -i debian-10 -i ubuntu-18.04

The ``inv`` command comes from the ``invoke`` package, which can be downloaded
and installed from PyPI. It loads a set of tasks from the ``tasks.py`` file in
this folder, and provides a command line interface for running those tasks.


Building wxPython
-----------------

To perform a build there must be one (and only one) wxPython source tarball
located in the ``../dist`` folder. This source archive can either be generated
with the ``build.py dox etg sip sdist`` command, or it can be downloaded from a
wxPython release on PyPI, or it can come from the wxPython snapshots server for
prerelease versions of the software.

With that source archive in place then a build for a specific distro can be done
like this (see the paragraph about ``invoke`` above)::

    inv build-wxpython -i ubuntu-18.04

That will do a build for all Pythons that are set up in the image, and both gtk2
and gtk3 if the image supports gtk2 (some don't.) To narrow the build down to
just one Python and one port, a command like this can be used::

    inv build-wxpython -i ubuntu-18.04 -p gtk3 -v Py37

And a bare ``inv build-wxpython`` will cause a build to be done for all distros,
all supported Pythons, and all supported ports. This will take a little while to
accomplish. Go binge-watch something on Netflix while you're waiting...

When the build(s) are finished the results will be placed in the
``../dist/linux`` folder, using the same folder structure for distros and ports
as is used on https://extras.wxpython.org/wxPython4/extras/linux/

PNG

   
IHDR             IDATxڥ3A۶m۶m۶-m۶l}oΞWdS_c7~;LջDѹ}K&d/e'UZZ g!(epAHQHi!H$$OjrH/`ЮڿB+ |.BrJ*7lC~}ۏU  G鮥[QI7k[dA7F3 5Y9$ro$^Wf9 thbR2b=<<)mbo@Nc郅/^U =" 37a>7pDaV*%R$ v`4Tj,xCINͤ$AM@kJOJjҎT'@sOfMN,4WzP	]_{S WϜ){T!pXǧDπ$bB"I~>I = _"!&gBf`@3LFi87 `0
zqBYC1 @ !tb05r|~ϻbߒ}CWF74;I%11<~(\xaa֓}V5 Am@@K+BW"sxNx6+ĄˠV|uXKoO3v໣6v*(qL~Rxx ߒ,wI`	/K+3ɈHi_+?nA^$<
5\wn'gR 0_\k 	sRxZ
 Jp `XEh]x% /DK/Ꞅ0kӪJ:>#tbX-l{<2 = }~=[?n>_!:ڒMCPqtk~,̹f@Oϭ R,^cirKڠ$ׅ'~÷a
ɪkt\[+!+7(0gl7SN<z`6 hJ
q{gQŸN n9 ~Ig a|1ݸj0;+Hsiӱj[ 	Qtd $b(Q3 Ǝ:j奱Mӟ7= R}9)Ϧ|?~AÚp7G1`䭧 O ~C{b,1PǔmNjt    IENDB`Extractor, Tweaker, Generator Scripts
=====================================

What is this stuff?
-------------------

This directory contains Extractor-Tweaker-Generator (ETG) scripts which are
used to drive the process of converting the wxWidgets Doxygen XML files into
the files that will be fed to the bindings generator tool (SIP).

They are each standalone Python scripts (although some refer to others) which
process the incoming XML for one or more wxWidgets classes, (that is the
"extractor" part). That XML data is converted to a hierarchy of objects that
describe the various components of the API (classes, methods, parameters,
etc.)

Since C++ and Python are different then there are some things which do not
match perfectly when implementing wrappers of API elements, and we need to do
some adaptation of the API to make things work. This is the "tweaker" part of
these scripts, and is typically the bulk of the content of the scripts.  The
objects created by the extractor have methods that help facilitate these
tweaks, and it is also possible to add new elements as well, when appropriate.

The last thing these scripts do is hand off the tweaked objects to the active
generators which will traverse the object tree and generate code as needed.


Checklist for all new etg files
-------------------------------

    * Use the bin/make-new-etg-file.py script to create a new boilerplate etg
      and unittest files for you. In simplest cases all you'll do after that is
      add the class names to be processed, and add some unittest code for it.

    * Use a filename that matches the wxWidgets/interface/wx file name
      that the classes and other stuff is being loaded from.  This
      means that there will be lots of very small files in etg, but it
      will help to find the interface header source to compare what is
      being declared there with what is being generated, and to better
      understand what may need tweaked in the etg script file.

    * Read the corresponding interface file and ensure that all classes
      declared in it are listed in the ITEMS list in the etg file,
      unless the class should not be wrapped for some reason.  Other
      items from the interface file will be included automatically.

    * Do not list classes from other interface files in the etg file.

    * Check for any extras added to each class in Classic wxPython and
      evaluate whether the same extras should be added to the Phoenix
      version.  For example, there may be additional methods added
      on to the class with %extend or %pythoncode that need to be
      carried over to Phoenix, such as __nonzero__, etc.  Also look
      for methods where Classic indicates that ownership should be
      transferred, or other special directives.

    * Check for backwards compatibility issues with Classic wxPython
      and document in the MigrationGuide. Compatibility issues
      resulting from not renaming all the overloads can probably be
      left undocumented, we'll probably be adding some of them back as
      deprecated methods eventually, and the programmers should be
      able to figure out the rest once they've started porting some
      code.

    * For window classes check if there are other virtual methods
      besides those added in addWindowVirtuals() that should be
      unignored.

    * UNITTESTS!  Create a unit test script in the unittests folder
      using the same base file name.  It should at least check that
      every non-abstract class can be constructed, and should also
      have tests for things that are added or tweaked in the etg
      script.  Other things that needed no tweaks are ok to be left
      untested for the time being, although porting over some of the
      the old unittest code from Classic would also be a good idea, but
      priority should be given to testing those things that had to be
      tweaked or added.

What is this?
=============

This folder holds the source for external projects used by Phoenix, (currently
just wxWidgets) as git submodules.  This allows Phoenix to use a specific
revision of the code in the other projects and not depend on the developer
fetching the correct version of the code on their own.

When you first check out the Phoenix source using git you will need to tell git
to also fetch the submodules, like this:

    cd Phoenix
    git submodule init
    git submodule update

To learn more about git submodules, please see the following:

    http://git-scm.com/book/en/v2/Git-Tools-Submodules
    http://blogs.atlassian.com/2013/03/git-submodules-workflows-tips/
    http://www.speirs.org/blog/2009/5/11/understanding-git-submodules.html


Notes to self
=============

 * To clone repositories with submodules:

       git clone <repourl>
       cd <repo>
       git submodule init
       git submodule update

 * To update an existing submodule from its upstream:

       git submodule update --remote <submodule>

   Or you can go into the submodule's folder and use normal git
   fetch/merge or pull operations to update the files in the
   submodule's workspace.  Commit the change in the main repo.

 * To set the submodule to track a specific branch from upstream:

       git config -f .gitmodules submodule.<name>.branch <branch name>

 * To use a different repo URL for a submodule than what others will
   see (in order to make and test local changes to the submodule that
   may be pushed to a different URL) then you can set that with a
   command like:

       git config submodule.MODULE_NAME.url PRIVATE_URL


[[ send to:
   wxpython-users@googlegroups.com
   wxpython-dev@googlegroups.com
   wx-users@googlegroups.com
   wx-announce@googlegroups.com
   Python-Announce-List@Python.Org
   ]]



Announcing wxPython 4.0.7
=========================

PyPI:   https://pypi.org/project/wxPython/4.0.7
Extras: https://extras.wxPython.org/wxPython4/extras/
Pip:    ``pip install wxPython==4.0.7``

This release is comprised mostly of fixes and minor features which have been
back-ported from the master branch. This release is likely the last release of
the 4.0.x release series, and is certainly the last 4.0.x release that will
support Python 2.7. It may still continue to build for Python 2.7 for some time, 
but no extra effort will be expended to keep it compatible.

Support for building for Python 3.8 has been added, as well as 3.8 binaries on
PyPI for Windows and MacOS.

This release provides the following changes:

* Bug fixes in wx.lib.calendar: key navigation across month boundaries is now 
  possible; key navigation now sets the date and fires the EVT_CALENDAR event; 
  setter APIs now set the date correctly (#1230).

* Switch to using a wx.Overlay in the Widget Inspection Tool to highlight
  widgets when running on a GTK3 port.

* Fixed issue in wx.lib.agw.customtreectrl where label editor could remain
  stuck forever (#1235).

* Fix a sometimes crash when using a wx.Overlay by letting the wx.DCOverlay hold
  a reference to the DC, to ensure that the DCOverlay is destroyed first.
  (PR#1301)
  
* Ported the embedding sample from Classic, which shows how to use wxPython from
  a C++ wxWidgets application that embeds Python. (PR #1353)

* Fixed wx.GetApp() to use wxWidgets' global wxApp instance instead of 
  maintaining its own pointer. This way, if the wxApp is created by C++ code
  wxPython will still be able to get access to it. (#1126)
  
* Several other PRs have been backported from the master branch (which will 
  become wxPython 4.1.0), the full list can be seen here: 
  https://github.com/wxWidgets/Phoenix/pull/1357



What is wxPython?
-----------------

wxPython is a cross-platform GUI toolkit for the Python programming
language.  It allows Python programmers to create programs with a
robust, highly functional graphical user interface, simply and
easily. It is implemented as a set of Python extension modules that
wrap the GUI components of the popular wxWidgets cross platform
library, which is written in C++. Supported platforms are Microsoft
Windows, Mac OS X and macOS, and Linux or other unix-like systems with
GTK2 or GTK3 libraries. In most cases the native widgets are used on
each platform to provide a 100% native look and feel for the
application.


What is wxPython Phoenix?
-------------------------

wxPython's Project Phoenix is a new from-the-ground-up implementation
of wxPython, created with the intent of making wxPython “better,
stronger, faster than he was before.” In other words, this new
implementation is focused on improving speed, maintainability and
extensibility of wxPython, as well as removing most of the cruft that
had accumulated over the long life of Classic wxPython.

The project has been in development off and on, mostly behind the
scenes, for many years. For the past few years automated snapshot
builds have been available for those adventurous enough to try it, and
many people eventually started using the snapshots in their projects,
even for production releases.  While there are still some things on
the periphery that need to be completed, the core of the new wxPython
extension modules which wrap the wxWidgets code has been stable for a
long time now.

Due to some things being cleaned up, reorganized, simplified and
dehackified wxPython Phoenix is not completely backwards compatible
with wxPython Classic.  This is intended. In general, however, the API
differences tend to be minor and some applications can use Phoenix
with slight, or even with no modifications.  In some other cases the
correct way to do things was also available in Classic and it's only
the wrong way that has been removed from Phoenix.  For more
information there is a Migration Guide document available at:
https://docs.wxpython.org/MigrationGuide.html

The new wxPython API reference documentation, including all
Python-specific additions and customizations, and docs for the wx.lib
package, is located at: https://docs.wxpython.org/

How to use the Phoenix snapshot build
=====================================

Hello, and welcome to the Phoenix snapshot build. If you are not
interested in Phoenix or do not know what Phoenix is, you may want to
exit the plane now and find a ticketing agent to help you get to the
correct package.

This tarball is basically a dump of the 'wx' package after a build has
been done, probably by one of the buildbot's build slaves. To use it
instead of Classic wxPython you will need to do a little tweaking to
your environment, which we will describe here. There are likely other
solutions that would work just as well, feel free to use something
else if you prefer.


Virtualenv
----------

One of the easiest ways to try out new Python modules without
impacting those that are already installed for other projects is to
use the virtualenv (or similar) tool to create a new stock python
environment with only the additional packages that you need, plus this
Phoenix test snapshot.  We highly recommend the use of such a tool to
avoid unexpected interactions with other packages.


Help Python find Phoenix
------------------------

All the usual suspects apply here.  You can simply add this folder to
your PYTHONPATH environment variable.  Or you can add a phoenix.pth
file to someplace already on the sys.path which contains the path to
this folder.  Or you can even copy the wx folder into the
site-packages folder in your virtualenv.


Help Phoenix find wxWidgets
---------------------------

The Phoenix extension modules need to load the dynamic libraries that contain
the wxWidgets code for the platform. In most cases the extension modules in
this snapshot already know to look in the same folder for the wxWidgets
shared libraries. This will work for Windows and Mac, and should also work
for any unix-like system based on ELF binaries, and if the expected objdump
utility was found on the build system.

For those cases where the build was not able to perform the neccesary magic
required to be able to make and use relocatable shared libraries, you may
need to do a little extra to help wxPython find the wxWidgets libraries.
Check your platform's documentation for details, but it may be as simple as
setting the LD_LIBRARY_PATH variable in the environment. For example if
you're in the folder where this README is located, then you can do something
like this::

    export LD_LIBRARY_PATH=`pwd`/wx

Auxiliary wxPython Release Files
================================

The source and binary extension modules for wxPython are located at PyPI where
they can be downloaded either manually or automatically via the pip tool.  See
https://pypi.python.org/pypi/wxPython

The files in this folder are the extras that are not uploaded to PyPI,
including the documentation, demo and samples, and also debugger information
files (.pdb) for Visual Studio.

================
wxPython Phoenix
================


Introduction
============

Phoenix is a new implementation of wxPython focused on improving speed,
maintainability and extensibility. Just like wxPython it wraps the wxWidgets
C++ toolkit and provides access to the UI portions of the wx API, enabling
Python applications to have a GUI on Windows, Macs or Unix systems with a
native look and feel and requiring very little (if any) platform specific code.



More to be written...


wxPython Demo and Samples
=========================

This archive contains a copy of the wxPython Phoenix demo, and also a
collection of small sample applications.

Once you have installed wxPython Phoenix you can run the demo by launching it
from a command line like this::

    cd demo
    python demo.py

Each of the folders in the samples folder contains one or more standalone
applications demonstrating how to use certain features of wxPython.  Examine
the source code in each sample folder to see how to run them and what they do.

wxPython Phoenix Snapshot Builds
================================

This directory contains a set of snapshot builds for the wxPython Phoenix
project. Each time there is a successful daily build from the buildbot the
results are uploaded here, in addition to the source and documentation
tarballs. Currently binaries for Windows and OSX are included, for a few
versions of Python. The source tarball can be used to build wxPython Phoenix
for other platforms. See Phoenix/README.rst in the source tarball for more
information.

If you are wanting to install an official release build of wxPython this is
not the place to be. You should go to PyPI instead, or use pip with the
default server address.

    https://pypi.python.org/pypi/wxPython


File naming conventions:
------------------------

 - Files with the "*.whl" extension are binary wheel files
   (https://wheel.readthedocs.org/en/latest/). See below for more info.

 - Files with the "*.tar.gz" extension are compressed tar archives of the
   Phoenix and wxWidgets source code.

 - The "*-docs-*.tar.gz" files are compressed archives of the documentation.

 - The bulk of the filename follows the conventions for naming wheels
   (https://www.python.org/dev/peps/pep-0427/#file-name-convention). For
   example:

      wxPython-4.0.0a2.dev2973+5ff6be7-cp35-cp35m-macosx_10_6_intel.whl

   means:

   - This is the "wxPython" package

   - It is version 4.0.0a2.dev2973+5ff6be7 (a development version, with
     the build number derived from the source control system.)

   - It is built for CPython version 3.5

   - "cp35m" indicates the name of the Application Binary Interface (ABI) that
     this package is compatible with.  Pip matches this with the ABI of the
     Python being used to run pip to know if the wxPython wheel is compatible
     with the target Python.

   - It is built for the macosx operating system

   - It is built for OSX version 10.6 or greater

   - It is built for Intel processors.


Installing Wheels
-----------------

The *.whl binaries in this directory are provided using Python's "wheel"
format, which is an archive format with some extra meta-data that can
be used by some Python tools to track installs, do uninstalls, etc.
In addition to the tools provided by the wheel package, the commonly
used pip command can also be used to install, upgrade and uninstall
wheels.  It can also be used to automatically download the correct
version of a wheel for you from PyPi, and then install it.  With a
little extra help it can do the same for prerelease versions of
software wheels like what is available here, with a command like
this:

    pip install -U --pre \
        -f https://wxpython.org/Phoenix/snapshot-builds/ \
        wxPython

NOTE: if there isn't a binary here for the latest version of Phoenix
that matches your Python version, then the command above will download
the latest version of the source and will try to build Phoenix for
you.  This will not be successful if you do not have appropriate
development tools and dependent libraries installed.

To install a specific binary from this site you can append the version
number to the command, like this:

    pip install -U --pre \
        -f https://wxpython.org/Phoenix/snapshot-builds/ \
        wxPython==4.0.0a2.dev2973+5ff6be7

There are also snapshot builds available for a few of the common Linux
distributions, located under the following folder:

    https://wxpython.org/Phoenix/snapshot-builds/linux/


Wheels for Linux
----------------

Since there are various options for distro and wx port (GTK2 or GTK3) then the
files can not all be located in the same folder like we can do for the Windows
and OSX builds.  This just simply means that you'll need to drill down a
little further to find the URL to give to pip.  For example, to get the GTK3
Phoenix builds for Ubuntu 16.04 (and 16.10, LinuxMint 18, and probably others)
you can use a pip command like this:

    pip install -U --pre \
        -f https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/ubuntu-16.04 \
        wxPython


Getting Pip
-----------

If you don't already have pip then you can install it with commands
like this:

    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py

See https://pip.pypa.io/en/latest/index.html for more info.


Happy Hacking!
Robin
This folder contains Cairo header files and DLLs for Windows, which enable
building Cairo support in wxWidgets on Windows, (in wx.GraphicsContext) as
well as using Cairo directly from Python, integrated with wxPython using the
wx.lib.wxcairo package. These DLLs will be included by default in the binary
builds for Windows.

These files were originally extracted from a zip file available from the
following location:

    https://github.com/preshing/cairo-windows

Note that the projects represented by these DLLs are released under the LGPL
or similar licenses. The DLLs are able to be included with wxPython because
they are not statically linked, and because end users are able to replace them
with newer or rebuilt versions if desired so long as they use a compatible
API/ABI, (for example a replacement libcairo would need to be compatible with
Cairo 1.15.12).  Source code is available at their respective project pages.
# Python packages needed for building and testing wxPython Phoenix
-r install.txt
appdirs
setuptools
wheel
twine
requests
requests[security]
cython
pytest
pytest-xdist
pytest-forked
pytest-timeout

sphinx==2.2.0 ; python_version >= '3.0'
sphinx==1.8.5 ; python_version < '3.0'
doc2dash==2.3.0
beautifulsoup4
# Runtime dependencies needed when using wxPython Phoenix
numpy < 1.17 ; python_version <= '2.7'
numpy ; python_version >= '3.0'
pillow
six
Recent changes for the SuperDoodle application
==============================================

This is not a real change-log, but rather serves as an example that goes
along with SuperDoodle's example of self-updating functionality. To see it
in action download and unzip either the Windows or Mac version of
SuperDoodle 1.0.0 from http://wxPython.org/software-update-test/. When you
run the 1.0.0 version there will be a "Check for Updates..." item on the
help menu that you can use to see how the self-updating UI works. The
application will download the latest version available, install it, and
will restart SuperDoodle for you. Be sure to check the version numbers in
the About dialog before and after the update so you can see that it is
changing. (That is the only real change in each of the application
updates.)

And now we return you to the totally fake change log, already in
progress...


Version 1.0.3
-------------
    * A little of this, a little of that.
    * Fixed the foozlehopper.
    * Added a whatsamagigit
    * There's a wocket in my pocket.
    
    
Version 1.0.2
-------------
    * "I don't believe there's a power in the 'verse that can stop Kaylee
      from being cheerful."
      
    * "Ten percent of nuthin' is...let me do the math here...nuthin' into
      nuthin'...carry the nuthin'..."
      
    * "Well, what about you, Shepherd? How come you're flying about with us
      brigands? I mean, shouldn't you be off bringing religiosity to the
      Fuzzie-Wuzzies or some such?"
      
    * "Do you know what the chain of command is here? It's the chain I go
      get and beat you with to show you who's in command."
      
    * "A man walks down the street in that hat, people know he's not afraid
      of anything."
      
    

Version 1.0.1
-------------
    * "Time is an illusion. Lunchtime doubly so."
    
    * "The ships hung in the sky in much the same way that bricks don't."
    
    * "Forty-two."
    
    * "Reality is frequently inaccurate."
    
    
Version 1.0.0
-------------
    * Initial release.
Doodle
------

This little sample is a doodle application.  It shows you how to draw
on a canvas, deal with mouse events, popup menus, update UI events,
and much more.

    doodle.py	    A class for the main drawing window.  You can also
                    run it directly to see just this window.


    superdoodle.py  Takes the DoodleWindow from doodle.py and puts it
                    in a more full featured application with a control
                    panel, and the ability to save and load doodles.

    setup.py        This sample also shows you how to make your
                    applications automatically self-update when new
		    releases are available.  There is a bit of code in
                    the superdoodle module to use the softwareupdate
                    module from the library, but the real magic
                    happens here in the distutils setup module.

This sample is an example of using wxPython from within a wxWidgets C++
application that embeds Python. Most things you'll need to know are documented
in the source code in embedded.cpp. THE BROTHERS GRIMM
FAIRY TALES



THE GOLDEN BIRD

A certain king had a beautiful garden, and in the garden stood a tree
which bore golden apples. These apples were always counted, and about
the time when they began to grow ripe it was found that every night
one of them was gone. The king became very angry at this, and ordered
the gardener to keep watch all night under the tree. The gardener set
his eldest son to watch; but about twelve o'clock he fell asleep, and
in the morning another of the apples was missing. Then the second son
was ordered to watch; and at midnight he too fell asleep, and in the
morning another apple was gone. Then the third son offered to keep
watch; but the gardener at first would not let him, for fear some harm
should come to him: however, at last he consented, and the young man
laid himself under the tree to watch. As the clock struck twelve he
heard a rustling noise in the air, and a bird came flying that was of
pure gold; and as it was snapping at one of the apples with its beak,
the gardener's son jumped up and shot an arrow at it. But the arrow
did the bird no harm; only it dropped a golden feather from its tail,
and then flew away. The golden feather was brought to the king in the
morning, and all the council was called together. Everyone agreed that
it was worth more than all the wealth of the kingdom: but the king
said, 'One feather is of no use to me, I must have the whole bird.'

Then the gardener's eldest son set out and thought to find the golden
bird very easily; and when he had gone but a little way, he came to a
wood, and by the side of the wood he saw a fox sitting; so he took his
bow and made ready to shoot at it. Then the fox said, 'Do not shoot
me, for I will give you good counsel; I know what your business is,
and that you want to find the golden bird. You will reach a village in
the evening; and when you get there, you will see two inns opposite to
each other, one of which is very pleasant and beautiful to look at: go
not in there, but rest for the night in the other, though it may
appear to you to be very poor and mean.' But the son thought to
himself, 'What can such a beast as this know about the matter?' So he
shot his arrow at the fox; but he missed it, and it set up its tail
above its back and ran into the wood. Then he went his way, and in the
evening came to the village where the two inns were; and in one of
these were people singing, and dancing, and feasting; but the other
looked very dirty, and poor. 'I should be very silly,' said he, 'if I
went to that shabby house, and left this charming place'; so he went
into the smart house, and ate and drank at his ease, and forgot the
bird, and his country too.

Time passed on; and as the eldest son did not come back, and no
tidings were heard of him, the second son set out, and the same thing
happened to him. He met the fox, who gave him the good advice: but
when he came to the two inns, his eldest brother was standing at the
window where the merrymaking was, and called to him to come in; and he
could not withstand the temptation, but went in, and forgot the golden
bird and his country in the same manner.

Time passed on again, and the youngest son too wished to set out into
the wide world to seek for the golden bird; but his father would not
listen to it for a long while, for he was very fond of his son, and
was afraid that some ill luck might happen to him also, and prevent
his coming back. However, at last it was agreed he should go, for he
would not rest at home; and as he came to the wood, he met the fox,
and heard the same good counsel. But he was thankful to the fox, and
did not attempt his life as his brothers had done; so the fox said,
'Sit upon my tail, and you will travel faster.' So he sat down, and
the fox began to run, and away they went over stock and stone so quick
that their hair whistled in the wind.

When they came to the village, the son followed the fox's counsel, and
without looking about him went to the shabby inn and rested there all
night at his ease. In the morning came the fox again and met him as he
was beginning his journey, and said, 'Go straight forward, till you
come to a castle, before which lie a whole troop of soldiers fast
asleep and snoring: take no notice of them, but go into the castle and
pass on and on till you come to a room, where the golden bird sits in
a wooden cage; close by it stands a beautiful golden cage; but do not
try to take the bird out of the shabby cage and put it into the
handsome one, otherwise you will repent it.' Then the fox stretched
out his tail again, and the young man sat himself down, and away they
went over stock and stone till their hair whistled in the wind.

Before the castle gate all was as the fox had said: so the son went in
and found the chamber where the golden bird hung in a wooden cage, and
below stood the golden cage, and the three golden apples that had been
lost were lying close by it. Then thought he to himself, 'It will be a
very droll thing to bring away such a fine bird in this shabby cage';
so he opened the door and took hold of it and put it into the golden
cage. But the bird set up such a loud scream that all the soldiers
awoke, and they took him prisoner and carried him before the king. The
next morning the court sat to judge him; and when all was heard, it
sentenced him to die, unless he should bring the king the golden horse
which could run as swiftly as the wind; and if he did this, he was to
have the golden bird given him for his own.

So he set out once more on his journey, sighing, and in great despair,
when on a sudden his friend the fox met him, and said, 'You see now
what has happened on account of your not listening to my counsel. I
will still, however, tell you how to find the golden horse, if you
will do as I bid you. You must go straight on till you come to the
castle where the horse stands in his stall: by his side will lie the
groom fast asleep and snoring: take away the horse quietly, but be
sure to put the old leathern saddle upon him, and not the golden one
that is close by it.' Then the son sat down on the fox's tail, and
away they went over stock and stone till their hair whistled in the
wind.

All went right, and the groom lay snoring with his hand upon the
golden saddle. But when the son looked at the horse, he thought it a
great pity to put the leathern saddle upon it. 'I will give him the
good one,' said he; 'I am sure he deserves it.' As he took up the
golden saddle the groom awoke and cried out so loud, that all the
guards ran in and took him prisoner, and in the morning he was again
brought before the court to be judged, and was sentenced to die. But
it was agreed, that, if he could bring thither the beautiful princess,
he should live, and have the bird and the horse given him for his own.

Then he went his way very sorrowful; but the old fox came and said,
'Why did not you listen to me? If you had, you would have carried away
both the bird and the horse; yet will I once more give you counsel. Go
straight on, and in the evening you will arrive at a castle. At twelve
o'clock at night the princess goes to the bathing-house: go up to her
and give her a kiss, and she will let you lead her away; but take care
you do not suffer her to go and take leave of her father and mother.'
Then the fox stretched out his tail, and so away they went over stock
and stone till their hair whistled again.

As they came to the castle, all was as the fox had said, and at twelve
o'clock the young man met the princes going to the bath and gave her
the kiss, and she agreed to run away with him, but begged with many
tears that he would let her take leave of her father. At first he
refused, but she wept still more and more, and fell at his feet, till
at last he consented; but the moment she came to her father's house
the guards awoke and he was taken prisoner again.

Then he was brought before the king, and the king said, 'You shall
never have my daughter unless in eight days you dig away the hill that
stops the view from my window.' Now this hill was so big that the
whole world could not take it away: and when he had worked for seven
days, and had done very little, the fox came and said. 'Lie down and
go to sleep; I will work for you.' And in the morning he awoke and the
hill was gone; so he went merrily to the king, and told him that now
that it was removed he must give him the princess.

Then the king was obliged to keep his word, and away went the young
man and the princess; and the fox came and said to him, 'We will have
all three, the princess, the horse, and the bird.' 'Ah!' said the
young man, 'that would be a great thing, but how can you contrive it?'

'If you will only listen,' said the fox, 'it can be done. When you
come to the king, and he asks for the beautiful princess, you must
say, "Here she is!" Then he will be very joyful; and you will mount
the golden horse that they are to give you, and put out your hand to
take leave of them; but shake hands with the princess last. Then lift
her quickly on to the horse behind you; clap your spurs to his side,
and gallop away as fast as you can.'

All went right: then the fox said, 'When you come to the castle where
the bird is, I will stay with the princess at the door, and you will
ride in and speak to the king; and when he sees that it is the right
horse, he will bring out the bird; but you must sit still, and say
that you want to look at it, to see whether it is the true golden
bird; and when you get it into your hand, ride away.'

This, too, happened as the fox said; they carried off the bird, the
princess mounted again, and they rode on to a great wood. Then the fox
came, and said, 'Pray kill me, and cut off my head and my feet.' But
the young man refused to do it: so the fox said, 'I will at any rate
give you good counsel: beware of two things; ransom no one from the
gallows, and sit down by the side of no river.' Then away he went.
'Well,' thought the young man, 'it is no hard matter to keep that
advice.'

He rode on with the princess, till at last he came to the village
where he had left his two brothers. And there he heard a great noise
and uproar; and when he asked what was the matter, the people said,
'Two men are going to be hanged.' As he came nearer, he saw that the
two men were his brothers, who had turned robbers; so he said, 'Cannot
they in any way be saved?' But the people said 'No,' unless he would
bestow all his money upon the rascals and buy their liberty. Then he
did not stay to think about the matter, but paid what was asked, and
his brothers were given up, and went on with him towards their home.

And as they came to the wood where the fox first met them, it was so
cool and pleasant that the two brothers said, 'Let us sit down by the
side of the river, and rest a while, to eat and drink.' So he said,
'Yes,' and forgot the fox's counsel, and sat down on the side of the
river; and while he suspected nothing, they came behind, and threw him
down the bank, and took the princess, the horse, and the bird, and
went home to the king their master, and said. 'All this have we won by
our labour.' Then there was great rejoicing made; but the horse would
not eat, the bird would not sing, and the princess wept.

The youngest son fell to the bottom of the river's bed: luckily it was
nearly dry, but his bones were almost broken, and the bank was so
steep that he could find no way to get out. Then the old fox came once
more, and scolded him for not following his advice; otherwise no evil
would have befallen him: 'Yet,' said he, 'I cannot leave you here, so
lay hold of my tail and hold fast.' Then he pulled him out of the
river, and said to him, as he got upon the bank, 'Your brothers have
set watch to kill you, if they find you in the kingdom.' So he dressed
himself as a poor man, and came secretly to the king's court, and was
scarcely within the doors when the horse began to eat, and the bird to
sing, and princess left off weeping. Then he went to the king, and
told him all his brothers' roguery; and they were seized and punished,
and he had the princess given to him again; and after the king's death
he was heir to his kingdom.

A long while after, he went to walk one day in the wood, and the old
fox met him, and besought him with tears in his eyes to kill him, and
cut off his head and feet. And at last he did so, and in a moment the
fox was changed into a man, and turned out to be the brother of the
princess, who had been lost a great many many years.

This folder is where the ouput of SIP is placed. These will be the C++ source
and header files, as well as a file for each module that specifies what files
were generated for that module (which is used by the build scripts.)

Currently these files are not committed to the SVN repository, but
they should be included in any source tarballs that are distributed.
This directory is where wxPython's ETG scripts will deposit the
wrapper generator files which describe the wxWidgets APIs that
wxPython wraps. These files will be fed to SIP to procude the C++ code
for the extension modules.

Currently these files are not committed to the SVN repository, but
they should be included in any source tarballs that are distributed.
RIVERBANK COMPUTING LIMITED LICENSE AGREEMENT FOR SIP

1. This LICENSE AGREEMENT is between Riverbank Computing Limited ("Riverbank"),
and the Individual or Organization ("Licensee") accessing and otherwise using
SIP software in source or binary form and its associated documentation.  SIP
comprises a software tool for generating Python bindings for software C and C++
libraries, and a Python extension module used at runtime by those generated
bindings.

2. Subject to the terms and conditions of this License Agreement, Riverbank
hereby grants Licensee a nonexclusive, royalty-free, world-wide license to
reproduce, analyze, test, perform and/or display publicly, prepare derivative
works, distribute, and otherwise use SIP alone or in any derivative version,
provided, however, that Riverbank's License Agreement and Riverbank's notice of
copyright, e.g., "Copyright (c) 2015 Riverbank Computing Limited; All Rights
Reserved" are retained in SIP alone or in any derivative version prepared by
Licensee.

3. In the event Licensee prepares a derivative work that is based on or
incorporates SIP or any part thereof, and wants to make the derivative work
available to others as provided herein, then Licensee hereby agrees to include
in any such work a brief summary of the changes made to SIP.

4. Licensee may not use SIP to generate Python bindings for any C or C++
library for which bindings are already provided by Riverbank.

5. Riverbank is making SIP available to Licensee on an "AS IS" basis.
RIVERBANK MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY
OF EXAMPLE, BUT NOT LIMITATION, RIVERBANK MAKES NO AND DISCLAIMS ANY
REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR
PURPOSE OR THAT THE USE OF SIP WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

6. RIVERBANK SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF SIP FOR ANY
INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF MODIFYING,
DISTRIBUTING, OR OTHERWISE USING SIP, OR ANY DERIVATIVE THEREOF, EVEN IF
ADVISED OF THE POSSIBILITY THEREOF.

7. This License Agreement will automatically terminate upon a material breach
of its terms and conditions.

8. Nothing in this License Agreement shall be deemed to create any relationship
of agency, partnership, or joint venture between Riverbank and Licensee.  This
License Agreement does not grant permission to use Riverbank trademarks or
trade name in a trademark sense to endorse or promote products or services of
Licensee, or any third party.

9. By copying, installing or otherwise using SIP, Licensee agrees to be bound
by the terms and conditions of this License Agreement.
This folder contains a copy of the SIP runtime library code.  It is
here so we can make it part of the wxPython build instead of needing
to have a dependency upon SIP already being installed on user
machines.

3rd party extension modules that need to use or interact with wxPython
types or other items will need to ensure that they #include the sip.h
located in this folder so they will know the proper module name to
import to find this version of the runtime library.  This feature was
added in SIP 4.12.

This directory holds source code that is not generated by any of the tools,
but is edited by hand instead. It may include C/C++, SIP or Python code as
needed.
Here is a tip from a text file.  See test_tipdlg.py
wxEditor component
------------------

The wxEditor class implements a simple text editor using wxPython.  You
can create a custom editor by subclassing wxEditor.  Even though much of
the editor is implemented in Python, it runs surprisingly smoothly on
normal hardware with small files.


Keys
----
Keys are similar to Windows-based editors:

Tab:                 1 to 4 spaces (to next tab stop)
Cursor movement:     Arrow keys
Beginning of line:   Home
End of line:         End
Beginning of buffer: Control-Home
End of the buffer:   Control-End
Select text:         Hold down Shift while moving the cursor
Copy:                Shift-Insert,   Control-C
Cut:                 Shift-Delete,   Control-X
Paste:               Control-Insert, Control-V

How to use it
-------------
The demo code (demo/wxEditor.py) shows how to use it as a simple text
box. Use the SetText() and GetText() methods to set or get text from
the component; these both return a list of strings.

The samples/FrogEdit directory has an example of a simple text editor
application that uses the wxEditor component.

Subclassing
-----------
To add or change functionality, you can subclass this
component. One example of this might be to change the key
Alt key commands. In that case you would (for example) override the
SetAltFuncs() method.

History
-------
The original author of this component was Dirk Holtwic. It originally
had limited support for syntax highlighting, but was not a usable text
editor, as it didn't implement select (with keys or mouse), or any of
the usual key sequences you'd expect in an editor. Robin Dunn did some
refactoring work to make it more usable. Steve Howell and Adam Feuer
did a lot of refactoring, and added some functionality, including
keyboard and mouse select, properly working scrollbars, and
overridable keys. Adam and Steve also removed support for
syntax-highlighting while refactoring the code.

To do
-----
Alt/Ctrl Arrow keys move by word
Descriptive help text for keys
Speed improvements
Different fonts/colors


Authors
-------
Steve Howell, Adam Feuer, Dirk Holtwic, Robin Dunn


Contact
-------
You can find the latest code for wxEditor here:
http://www.pobox.com/~adamf/software/

We're not actively maintaining this code, but we can answer
questions about it. You can email us at:

Adam Feuer <adamf at pobox dot com>
Steve Howell <showell at zipcon dot net>

29 November 2001
Free Icons by Axialis Software
http://www.axialis.com

Here is a library of icons that you can freely use in your projects. All
the icons are licensed under the Creative Commons Attribution License
(http://creativecommons.org/licenses/by/2.5/). It means that you can use
them in any project or website, commercially or not.

The icons have been created by Axialis IconWorkshop, the professional
icon authoring tool for Windows. For more info visit this page:
http://www.axialis.com/iconworkshop

TERMS OF USE
The only restrictions are: (a) you must keep the credits of the authors:
"Axialis Team", even if you modify them; (b) link to us if you use them
on your website (see below).

LINK TO US
If you use the icons in your website, you must add the following link on
EACH PAGE containing the icons (at the bottom of the page for example).
The HTML code for this link is:

  <a href="http://www.axialis.com/free/icons">Icons</a> by <a href="http://www.axialis.com">Axialis Team</a>





# wx.lib.plot Changelog

This is a log of the changes made to this package in reverse chronological
order.

Attempts were made to maintain previous contributors' attributions, but some
things may have been lost in transition. If a mistake is found, please
submit a PR to correct it.

The `wx.lib.plot` code used to be a module. Conversion to a package began
on 2016-07-05 and finished on [insert date here].


## 2016-07-05 (Start) - Douglas Thor (doug.thor@gmail.com) (PR #)
+ Converted module to package.
+ Separated out changelog and readme to separate files.
+ Changed cursors to use the built-ins rather than PyEmbeddedImage.
+ Moved PlotCanvas class to separate plotcanvas.py module
+ Moved demo to examples/demo; added simple_example.py
+ package now callable via `python -m wx.lib.plot`: runs demo.
+ Moved PendingDeprecation, TempSytle to utils.py
+ Renamed `BoxPlot` to `PolyBoxPlot`.


## 2016-06-14 (Start) - Douglas Thor (doug.thor@gmail.com) (PR #98)
+ Refactored PolyBars and PolyHistogram to PolyBarsBase class
+ Replaced `SaveBrush` et. al., with more generic `TempStyle` combination
  Context Manager and Decorator.
+ Removed `eval` in PolyMarkers._drawmarkers
+ Refactored EnableAxes, EnableAxesValues, and EnableTicks, as they all used
  the same core logic.
+ Replaced some instances of dc.DrawText with dc.DrawTextList
+ Various cleanups of math, line character limits, and PEP8-ing
+ Updated/Added a bunch of Sphinx-compatible documentation
+ NaN is now handled (ignored) in BoxPlot.


## 2016-05-27 - Douglas Thor (doug.thor@gmail.com) (PR #91)
+ Added PolyBars and PolyHistogram classes
+ General Cleanup
+ Added demos for PolyBars and PolyHistogram
+ updated plotNN menu items status-bar text to be descriptive.
+ increased default size of demo
+ updated xSpec and ySpec to accept a list or tuple of (min, max) values.


## 2015-08-20 - Douglas Thor (doug.thor@gmail.com) (PR #26)
+ Implemented a drawstyle option to PolyLine that mimics matplotlib's
  Line2dD.drawstyle option.
+ Added significant customization options to PlotCanvas
  - Gridlines, Axes, Centerline, diagonal, and ticks can now have
    their Pen (color, width, and linestyle) set independently.
  - Ticks, Axes, and AxesValues can now be turned on/off for each side.
+ Added properties to replace getters/setters.
+ All getters and setters now have deprecation warnings
+ Fixed python3 FutureWarning for instances of 'x == None' (replaced with
  'x is None')
+ Documentation updates
+ Added Box Plot
+ Added context manager and decorator that gets and resets the pen before
  and after a function call
+ updated demo for new features
+ Most items are now allow custom pens (color, width, linestyle)
+ Added 'drawstyle' option to PolyLine that mimics MatPlotLib's
  Line2dD.drawstyle option.


## 2009-06-22 - Florian Hoech (florian.hoech@gmx.de)
+ Fixed exception when drawing empty plots on Mac OS X
+ Fixed exception when trying to draw point labels on Mac OS X (Mac OS X
  point label drawing code is still slow and only supports wx.COPY)
+ Moved label positions away from axis lines a bit
+ Added PolySpline class and modified demo 1 and 2 to use it
+ Added center and diagonal lines option (Set/GetEnableCenterLines,
  Set/GetEnableDiagonals)
+ Added anti-aliasing option with optional high-resolution mode
  (Set/GetEnableAntiAliasing, Set/GetEnableHiRes) and demo
+ Added option to specify exact number of tick marks to use for each axis
  (SetXSpec(<number>, SetYSpec(<number>) -- work like 'min', but with
  <number> tick marks)
+ Added support for background and foreground colours (enabled via
  SetBackgroundColour/SetForegroundColour on a PlotCanvas instance)
+ Changed PlotCanvas printing initialization from occuring in __init__ to
  occur on access. This will postpone any IPP and / or CUPS warnings
  which appear on stderr on some Linux systems until printing
  functionality is actually used.


## 2004-08-15 - Gordon Williams (g_will@cyberus.ca)
+ Imported modules given leading underscore to name.
+ Added Cursor Line Tracking and User Point Labels.
+ Demo for Cursor Line Tracking and Point Labels.
+ Size of plot preview frame adjusted to show page better.
+ Added helper functions PositionUserToScreen and PositionScreenToUser
  in PlotCanvas.
+ Added functions GetClosestPoints (all curves) and GetClosestPoint (only
  closest curve) can be in either user coords or screen coords.


## 2004-08-06 - Gordon Williams (g_will@cyberus.ca)
+ Added bar graph demo
+ Modified line end shape from round to square.
+ Removed FloatDCWrapper for conversion to ints and ints in arguments


## 2003-12-18 - Jeff Grimmett (grimmtooth@softhome.net)
+ wxScrolledMessageDialog -> ScrolledMessageDialog


## 2003-12-15 - Jeff Grimmett (grimmtooth@softhome.net)
+ 2.5 compatability update.
+ Renamed to plot.py in the wx.lib directory.
+ Reworked test frame to work with wx demo framework. This saves a bit
  of tedious cut and paste, and the test app is excellent.


## 2003-02-?? - Gordon Williams (g_will@cyberus.ca)
+ More style options
+ Zooming using mouse "rubber band"
+ Scroll left, right
+ Grid(graticule)
+ Printing, preview, and page set up (margins)
+ Axis and title labels
+ Cursor xy axis values
+ Doc strings and lots of comments
+ Optimizations for large number of points
+ Legends
+ Did a lot of work here to speed markers up. Only a factor of 4
  improvement though. Lines are much faster than markers, especially
  filled markers.  Stay away from circles and triangles unless you
  only have a few thousand points.

  ```
  +--------------------------------------------+
  | Times for 25,000 points                    |
  +============================================+
  | Line                             | 0.078 s |
  +----------------------------------+---------+
  | Markers: Square                  | 0.22 s  |
  +----------------------------------+---------+
  | Markers: dot                     | 0.10    |
  +----------------------------------+---------+
  | Markers: circle                  | 0.87    |
  +----------------------------------+---------+
  | Markers: cross, plus             | 0.28    |
  +----------------------------------+---------+
  | Markers: triangle, triangle_down | 0.90    |
  +----------------------------------+---------+
  ```
+ Thanks to Chris Barker for getting this version working on Linux.
# wx.lib.plot

A simple, light-weight plotting package for wxPython Phoenix.

Based on wxPlotCanvas
Written by K. Hinsen, R. Srinivasan;
Ported to wxPython: Harm van der Heijden, Feb 1999

This is a simple, light weight plotting module that can be used with
Boa or easily integrated into your own wxPython application. The
emphasis is on small size and fast plotting for large data sets. It
has a reasonable number of features to do line and scatter graphs
easily as well as simple bar graphs. It is not as sophisticated or
as powerful as SciPy Plt or Chaco. Both of these are great packages
but consume huge amounts of computer resources for simple plots.
They can be found at http://scipy.com
Copyright (c) since 2006, Oliver Schoenborn
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# this file gets copied to wx/lib/pubsub folder when release to wxPython

For wxPython users:

The code in this wx/lib/pubsub folder is taken verbatim from the PyPubSub
project on SourceForge.net. Pubsub originated as a wxPython lib, but it is now
a standalone project on SourceForge. It is included as part of wxPython
distribution for convenience to wxPython users, but pubsub can also be installed
standalone (see installation notes at http://pypubsub.sourceforge.net), or you
can also overwrite the version in this folder with the standalone version or
put an SVN checkout of pubsub in this folder, etc.

Note that the source distribution on SF.net tends to be updated more often than
the copy in wx/lib/pubsub. If you wish to install pubsub standalone, there are
instructions on the Install page of http://pypubsub.sourceforge.net.

There is extensive documentation for pubsub at http://pypubsub.sourceforge.net,
and some examples are in wx/lib/pubsub/examples. The WxPython wiki also discusses
usage of pubsub in wxPython.

Oliver Schoenborn
December 2013
For PyPubSub v3.3.0
^^^^^^^^^^^^^^^^^^^^^

* cleanup low-level API: exception classes, moved some out of pub module that did not 
  belong there (clutter), move couple modules, 
* completed the reference documentation
* support installation via pip
* follow some guidelines in some PEPs such as PEP 396 and PEP 8
* support Python 2.6, 2.7, and 3.2 to 3.4a4 but drop support for Python <= 2.5

For PyPubSub v3.2.0
^^^^^^^^^^^^^^^^^^^

This is a minor release for small improvements made (see docs/CHANGELOG.txt) 
based on feedback from user community. In particular an XML reader for 
topic specification contributed by Josh English. Also cleaned up the 
documentation, updated the examples folder (available in source distribution
as well as `online`_). 

.. _online: https://sourceforge.net/p/pubsub/code/HEAD/tree/

Only 3 changes to API (function names): 

* renamed pub.getDefaultRootAllTopics to pub.getDefaultTopicTreeRoot
* removed pub.importTopicTree: use pub.addTopicDefnProvider(source, format)
* renamed pub.exportTopicTree to pub.exportTopicTreeSpec

Oliver Schoenborn
September 2013


PyPubSub 3.1.2
^^^^^^^^^^^^^^^^

This is a minor release for small improvements made (see docs/CHANGELOG.txt) 
based on feedback from user community. Also extended the documentation. See 
pubsub.sourceforge.net for installation and usage. See the examples folder for 
some useful examples. 

Oliver Schoenborn
Nov 2011


PyPubSub 3.1.1b1
^^^^^^^^^^^^^^^^^^

Docs updated. 

Oliver Schoenborn
May 2010


For PyPubSub v3.1.0b1
^^^^^^^^^^^^^^^^^^^^^^

Major cleanup of the API since 3.0 and better support 
for the legacy wxPython code. Defining a topic tree 
via a text file has been improved drastically, making it
simpler to document topic messages and payload data
required or optional. More examples have been added, 
and the messaging protocols clarified. 

The included docs are not yet updated, that's what I'm 
working on now and will lead to the 3.1.1b1 release. 
I'm also working on an add-on module that would allow 
two applications to communicate over the network using 
pubsub-type messaging (with topics, etc). The design 
is almost complete. 

Oliver Schoenborn
Jan 20100.9.7.9 (9/8/09)
-------------------
Finalized the naming convention so that references to shell in the new "slices"
shell are renamed to "sliceshell" (likewise, Shell becomes SlicesShell)

Also, renamed the file "slices.py" to "sliceshell.py".
Since my goal is to keep PySlices.py as the equivalent to PyCrust.py,
   I think this new convention makes the most sense...

Now (Finally):
  shell.py contains the classes: Shell, ShellFacade, and ShellFrame
  sliceshell.py contains the classes: SlicesShell, SlicesShellFacade,
                                      and SlicesShellFrame
  crust.py contains: Crust and CrustFrame
  crustslices.py contains: CrustSlices and CrustSlicesFrame
  PyShell.py and PySlicesShell.py are the respective standalone shell apps
  PyCrust.py and PySlices.py are the respective apps that also include Filling

  frame.py etc. still continue to service both PyCrust and PySlices.

0.9.7.8 (9/8/09)
-------------------
Added open/save abilities to PySlices (PyCrust remains the same).
  This uses a special format with extension .pyslices.
  A file, *.pyslices will contain a text header and
    also a line denoting the beginning of each new slice,
    naming the type of slice as well (grouping, input, output)
  All output is commented with a single '#' which is removed upon loading.
  This ensures that a well contstucted .pyslices file is also
    a valid python script!

Added the ability to load an entire python file into a new Input slice
    with Ctrl-L
Added the ability to load pyslices files from the command line.

Split the functionality of crust.py (functioning for both PyCrust and PySlices)
  into crust.py (only PyCrust) and crustslices.py (only for PySlices).

After revising the naming conventions:
  shell.py contains the classes: Shell, ShellFacade, and ShellFrame
  slice.py contains the classes: Shell, ShellFacade, and ShellFrame
  crust.py contains: Crust and CrustFrame
  crustslices.py contains: CrustSlices and CrustSlicesFrame
  PyShell.py and PySlicesShell.py are the respective standalone shell apps
  PyCrust.py and PySlices.py are the respective apps that also include Filling

  frame.py etc. still continue to service both PyCrust and PySlices.

0.9.7.7 (8/25/2009) (Current--Still Need to SVNAdd the new file PySlicesShell.py)
-------------------
Added code to introspect.py to check for Enthought's "Traits" attributes.
Added PySlicesShell.py.  PySlices shell is PySlices without Filling
  and other crust attributes.
Fixed a bug with Output_BG

0.9.7.6 (7/18/2009)
-------------------
Made output have a slight-blue background
Added a tutorial that can be disabled in Options->Startup.
Added "Shell Mode" which uses >>> and ... markers for input slices and uses two returns for command execution
Changed manual completion keybindings.
Cleaned up keybinding help.
Made Items in Options->Startup menu automatically save to the config file (since they don't affect anything until startup)
Major code cleanup, removal of much dead code, shortening of very long lines, etc...

0.9.6.9 (7/9/2009)
-------------------
Fixed Undo marker issues and a bug in selection overwrite.

0.9.6.8 (7/1/2009)
-------------------
Merged changes with SVN trunk.

0.9.6.4 thru 0.9.6.6  (10/22/2008-4/27/2009)
-------------------
Added magic.py to handle some very simple "magic" commands:

Now the command:
"f 1"
will be re-interpreted as:
"f(1)"

The command:
"f 1,2,3,4"
will be interpreted as:
f(1,2,3,4)

Special commands "ls","cd", and "pwd" are interpreted separately

Works with slices.py and shell.py

Also fixed auto-indent magic.

0.9.6.1 thru 0.9.6.3 (10/21/2008)
---------------------------------
Added PySlices (slices.py and PySlices.py), a modified version of PyCrust.
PySlices is a "notebook interface" multi-line shell, ala Sage or Mathematica.
It uses Scintilla markers extensively, with red for input and blue for output.

Modified crust.py to use a switch so it can load either a Shell or a Slices_Shell

0.9.5 (12/23/2005)
------------------

Applied a series of enhancments by Franz Steinaeusler, Adi Sieker, and
Sebastian Haase, up until their 7-31-2005 version.  (Their next
version broke some existing functionality, and added some confusing
hacks, and I didn't feel that the incremental gains were worth the
loss at that point so I stopped at 7-31-2005.)

Their changes include the following:

* The Autocomplete and Calltip windows can now be opened manually with
  Ctrl-Space and Ctrl-Shift-Space.

* In the stand alone PyCrust app the various option settings, window
  size and position, and etc. are saved and restored at the next run.

* Added a help dialog bound to the F1 key that shows the key bindings.

* Added a new text completion function that suggests words from the
  history.  Bound to Shift-Return.

* F11 will toggle the maximized state of the frame.

* switched to Bind() from wx.EVT_*().

* Display of line numbers can be toggled.

* F12 toggles a "free edit" mode of the shell buffer.  This mode is
  useful, for example, if you would like to remove some output or
  errors or etc. from the buffer before doing a copy/paste.  The free
  edit mode is designated by the use of a red, non-flashing caret.

* Ctrl-Shift-F will fold/unfold (hide/show) the selected lines.



On top of these changes I (Robin Dunn) added the following:

* General code cleanup and fixes.

* Use wx.StandardPaths to determine the location of the config files.

* Remove Orbtech attributions from the UI, they've been there long
  enough.

* Use wx.SP_LIVE_UPDATE on crust and filling windows.

* Extended the saving of the config info and other new features to the
  PyShell app too.  Additionally, other apps that embed a PyCrust or a
  PyShell can pass their own wx.Config object and have the Py code
  save/restore its settings to/from there.

* All of the classes with config info get an opportunity to save/load
  their own settings instead of putting all the save/load code in one
  place that then has to reach all over the place to do anything.

* Enable editing of the startup python code, which will either be the
  file pointed to by PYTHONSTARTUP or a file in the config dir if
  PYTHONSTARTUP is not set in the environment.

* Added an option to skip the running of the startup code when
  PyShell or PyCrust starts.

* PyCrust adds a pp(item) function to the shell's namespace that
  pretty prints the item in the Display tab of the notebook.  Added
  code to raise that tab when pp() is called.

* Added an option for whether to insert text for function parameters
  when popping up the call tip.

* Added Find and Find-Next functions that use the wx.FindReplaceDialog.






0.9.4 (1/25/2004 to //2004)
------------------------------

Removed wxd decorators in favor of new SWIG-generated docstrings.

Removed docs tabs from crust interface:
* wxPython Docs
* wxSTC Docs

Fixed Calltip tab refresh problem on Windows.

shell.autoCompleteAutoHide added with default of False.

Changed default namespace of Shell to __main__.__dict__, instead of an
empty dictionary.


0.9.3 (9/25/2003 to 1/24/2004)
------------------------------

Fun and games with dynamic renaming.  Details of any other changes
were lost in the confusion.  I'll try to do better in the future.


0.9.2 (5/3/2003 to 9/25/2003)
-----------------------------

Changed to the new prefix-less "wx" package::

    import wx

instead of::

    from wxPython import wx

Fixed typo in ``PyWrap.py``::

    if __name__ == '__main__':
        main(sys.argv)

should have been::

    if __name__ == '__main__':
        main()

Added pretty-print Display tab to Crust, based on suggestion from
Jason Whitlark.

Improved ``Can*`` checks in ``EditWindow``, since STC is too lenient,
particularly when it is set to read-only but returns True for
CanPaste() (seems like an STC bug to me)::

    def CanCopy(self):
        """Return True if text is selected and can be copied."""
        return self.GetSelectionStart() != self.GetSelectionEnd()

    def CanCut(self):
        """Return True if text is selected and can be cut."""
        return self.CanCopy() and self.CanEdit()

    def CanEdit(self):
        """Return True if editing should succeed."""
        return not self.GetReadOnly()

    def CanPaste(self):
        """Return True if pasting should succeed."""
        return stc.StyledTextCtrl.CanPaste(self) and self.CanEdit()


0.9.1 (3/21/2003 to 5/2/2003)
-----------------------------

PyCrust is dead!  Long live Py!

* Renamed ``PyCrust`` package to ``py``.
* Moved code to wxPython's CVS repository.

Fixed bug in ``introspect.py`` on introspecting objects occurring
immediately after a secondary prompt, like this::

    >>> l = [1, 2, 3]
    >>> for n in range(3):
    ...     l.  <-- failed to popup autocomplete list

Added documentation files:

* PyManual.txt
* wxPythonManual.txt
* wxPythonPackage.txt
* wxPythonExamples.txt

Added PyAlaMode and PyAlaCarte code editors.

Major refactoring to support ``editor`` and ``shell`` from the same
base.

Renamed program files:

* ``PyCrustApp.py`` to ``PyCrust.py``
* ``PyFillingApp.py`` to ``PyFilling.py``
* ``PyShellApp.py`` to ``PyShell.py``
* ``wrap.py`` to ``PyWrap.py``

Removed disabling of autocomplete for lists of 2000 items or more.
The current implementation of wxSTC can now handle lists this big.

Improved handling of ``sys.path`` to mimic the standard Python shell.


0.9 (2/27/2003 to 3/20/2003)
----------------------------

Added fontIncrease, fontDecrease, fontDefault signals, receivers and
keybindings::

    Ctrl+]            Increase font size.
    Ctrl+[            Decrease font size.
    Ctrl+=            Default font size.

Continued enhancement of the decorator capability to provide better
documentation and docstrings for wxPython classes and functions.

Introduced new tabbed interface:

* Namespace
* Calltip
* Session
* Dispatcher
* wxPython Docs
* wxSTC Docs

``Filling.tree`` now expands tuples as well as lists.  (It should have
done this all along, I just never noticed this omission before.)

Added this True/False test to all modules::

    try:
        True
    except NameError:
        True = 1==1
        False = 1==0

Added ``wxd`` directory with decoration classes.


0.8.2 (1/5/2003 to 2/26/2003)
-----------------------------

Wrapped ``sys.ps1``, ``sys.ps2``, and ``sys.ps3`` in ``str()``.
(Thanks, Kieran Holland.)

Fixed minor things found by PyChecker.

Changed locals to use ``__main__.__dict__`` and added code to clean up
the namespace, making it as close to the regular Python environment as
possible.  This solves the problem of pickling and unpickling
instances of classes defined in the shell.

Made ``shell.PasteAndRun()`` a little more forgiving when it finds a
ps2 prompt line with no trailing space, such when you copy code from a
web page.

Improved autocomplete behavior by adding these to shell::

    self.AutoCompSetAutoHide(False)
    self.AutoCompStops(' .,;:([)]}\'"\\<>%^&+-=*/|`')

Added ``decor`` directory, ``decorator.py``, ``stcDecor.py``, and
``stcConstants.py``.  These all serve the purpose of adding docstrings
to existing wxPython classes, in particular the ``wxStyledTextCtrl``.

Added ``wrap.py``, a command line utility for running a wxPython app
with additional runtime-tools loaded, such as PyCrust (the only tool
at this point).

Flushed the clipboard Cut/Copy operations so that selections will
exist in the clipboard even after PyCrust has been closed.

Improved the suppression of docstrings for simple data types appearing
in the namespace viewer.

Better handling of autocompletion with numeric types; no
autocompletion when typing a dot after an integer.  If the
autocompletion is desired, type a space before the dot::

    func = 3 .

More Filling!!! The namespace tree is now dynamically updated.


0.8.1 (12/20/2002 to 12/25/2002)
--------------------------------

Improved keyboard handling with Autocomplete active.  You can now use
Enter as well as Tab to select an item from the list.

Disabled autocomplete for lists of 2000 items or more.  The current
implementation of wxSTC can't handle lists this big.

Changed ``filling`` to always display docstrings for objects.  This is
useful for objects whose docstrings have been decorated, rather than
coming directly from the source code.  (Hmmm.  Sounds like someone is
doing some decorating.  I wonder where that would be helpful? <wink>)

Fixed handling of icon.  Added ``images.py`` file.


0.8 (10/29/2002 to 12/16/2002)
------------------------------

Added "help" to startup banner info.

Made all ``wx`` and ``stc`` imports explicit.  No more ``import *``.

Replaced use of the ``wx`` module's ``true`` and ``false`` with
Python's ``True`` and ``False``.

Changed ``introspect.getRoot()`` to use ``tokenize`` module.  This
does a slightly better job than the previous parsing routine and the
code is clearer.

Improved handling of whitespace and empty types during introspection.

Fixed cut/copy clipboard problem under Linux.  (Robin Dunn rocks!!!)

Added shell.about() which works like this::

    >>> shell.about()
    PyCrust Version: 0.8
    Shell Revision: 1.80
    Interpreter Revision: 1.15
    Python Version: 2.2.2
    wxPython Version: 2.3.3.1
    Platform: linux2

Added copy plus and paste plus to shell menu.

Moved shell menu from ``shell.py`` to ``shellmenu.py``.

Added ``sys.stdin.readlines()`` support.

Added ``time.sleep()`` in ``readline()`` and ``OnIdle()`` event
handler to free up the CPU.


0.7.2 (2/22/2002 to 8/27/2002)
------------------------------

Tweaked ``getAttributeNames()`` to pick up a few more attributes::

    '__bases__', '__class__', '__dict__', '__name__', 'func_closure',
    'func_code', 'func_defaults', 'func_dict', 'func_doc',
    'func_globals', 'func_name'

Added a tests directory and unit tests.

Improved support for empty types in the shell: ``[]``, ``()`` and
``{}`` as far as when call tips and autocompletion are available.

Added support for the other triple string - ``''''''``.

Refactored ``introspect.py`` to improve testability.

Improved call tips for unbound methods by leaving the "self"
parameter, since unbound methods require an instance be passed.

Fixed call tip bug where a tip was displayed when a "(" was typed
after an object that wasn't callable.

Fixed ``getAllAttributeNames`` when ``str(object)`` fails.

Added brace highlighting.  (Thank you, Kevin Altis.)

Fixed problem displaying unicode objects in ``PyFilling``.

Changed how ``filling.py`` checks for expandable objects.  Lists are
now expandable objects.

Made the key handling more robust when there is an active text
selection that includes text prior to the last primary prompt.  Thanks
to Raul Cota for pointing this out.

Fixed wxSTC problem with brace highlighting and non-us keyboards.
(Thank you for the patch, Jean-Michel Fauth.)

Added ``busy = wxBusyCursor()`` to key points in ``shell`` and
``filling``.

Added ``OnCloseWindow`` handler to ``ShellFrame`` and ``CrustFrame``.

Default to ``SetWrapMode(1)`` for shell and namespace viewer.

Added ``shell.wrap()`` and ``shell.zoom()``.

Added autoCompleteKeys hooks for Raul Cota.

Cleaned up various little key handling bugs.

Changed input methods to get values from shell, rather than dialog
boxes.  Renamed ``readIn`` to ``readline`` and ``readRaw`` to
``raw_input``.


0.7.1 (12/12/2001 to 2/21/2002)
-------------------------------

Fixed ``OnChar()`` issues effecting European keyboards, as reported by
Jean-Michel Fauth.

Fixed ``introspect.py`` issue with xmlrpc objects reported by Kevin
Altis.

Fixed some introspect/PyFilling issues with regard to Python 2.2.

Fixed font background color as reported by Keith J. Farmer.  (Thanks)

Fixed problem with call tips and autocompletion inside multiline
commands as report by Kevin Altis.

Improved ``OnKeyDown`` handling of cut/copy/paste operations based on
feedback from Syver Enstad.  (Thanks)

Added a ``shell.help()`` method to display some help info.

Changed sort of items in the namespace viewer to case insensitive.

Changed ``attributes.sort(lambda x, y: cmp(x.upper(), y.upper()))`` in
advance of an upcoming fix to an autocompletion matching bug in wxSTC.

Improved support for ZODB by allowing namespace drilldown into BTrees.

Added ``shell.PasteAndRun()`` to support pasting multiple commands into
the shell from the clipboard.  Ctrl+Shift+V or v.

Enter now always processes a command (or copies down a previous one.)
To insert a line break, press Ctrl+Enter.

Escape key clears the current, unexecuted command.

History retrieval changed to replace current command.  Added new keys
to insert from history - Shift+Up and Shift+Down.

Better call tips on objects with ``__call__`` methods.

Improved call tip positioning calculation.


0.7 (10/15/2001 to 12/11/2001)
------------------------------

Changed how command history retrieval functions work.  Added Alt-P,
Alt-N as keybindings for Retrieve-Previous, Retrieve-Next.

Added full support for multi-line commands, similar to IDLE.

Changed ``introspect.getAttributeNames()`` to do a case insensitive
sort.

Changed Cut/Copy/Paste to deal with prompts intelligently.  Cut and
Copy remove all prompts.  Paste can handle prompted or not-prompted
text.

Added ``CopyWithPrompts()`` method attached to Ctrl-Shift-C for those
times when you really do want all the prompts left intact.

Improved handling of the shell's read-only zone.

Changed ``CrustFrame.__init__`` parameter spec to include all
parameters allowed by a ``wxFrame``.

Changed ``FillingText`` to be read-only.

Renamed ``PyCrust.py`` to ``PyCrustApp.py`` to eliminate
package/module name conflicts that kept you from doing ``from PyCrust
import shell`` inside files located in the ``PyCrust`` directory.

Renamed ``PyFilling.py`` to ``PyFillingApp.py`` and ``PyShell.py`` to
``PyShellApp.py`` to maintain consistency.

Removed the ``__date__`` property from all modules.

Fixed bug in ``introspect.getCallTip()``, reported by Kevin Altis.


0.6.1 (9/19/2001 to 10/12/2001)
-------------------------------

Changed ``Shell.run()`` to always position to the end of existing
text, as suggested by Raul Cota.

Changed ``introspect.getAllAttributeNames()`` to break circular
references in ``object.__class__``, which occurs in Zope/ZODB
extension classes.

Changed ``filling.FillingTree.getChildren()`` to introspect extension
classes.

Fixed minor bugs in ``introspect.getCallTip()`` that were interfering
with call tips for Zope/ZODB extension class methods.

In preparation for wxPython 2.3.2, added code to fix a font sizing
problem.  Versions of wxPython prior to 2.3.2 had a sizing bug on Win
platform where the font was 2 points larger than what was specified.

Added a hack to ``introspect.getAllAttributeNames()`` to "wake up"
ZODB objects that are asleep - in a "ghost" state.  Otherwise it
returns incomplete info.


0.6 (8/21/2001 to 9/12/2001)
----------------------------

Added ``PyFilling.py`` and ``filling.py``.

``PyShell.py`` and ``PyFilling.py`` can now be run standalone, as well
as ``PyCrust.py``.

Added ``crust.py`` and moved some code from ``PyCrust.py`` to it.

Added command history retrieval features submitted by Richie Hindle.

Changed ``shell.write()`` to replace line endings with OS-specific
endings.  Changed ``shell.py`` and ``interpreter.py`` to use
``os.linesep`` in strings having hardcoded line endings.

Added ``shell.redirectStdin()``, ``shell.redirectStdout()`` and
``shell.redirectStderr()`` to allow the surrounding app to toggle
requests that the specified ``sys.std*`` be redirected to the shell.
These can also be run from within the shell itself, of course.

The shell now adds the current working directory "." to the search
path::

    sys.path.insert(0, os.curdir)

Added support for distutils installations.


0.5.4 (8/17/2001 to 8/20/2001)
------------------------------

Changed default font size under Linux to::

    'size'   : 12,
    'lnsize' : 10,

Changed ``Shell`` to expect a parameter referencing an Interpreter
class, rather than an intepreter instance, to facilitate subclassing
of Interpreter, which effectively broke when the Editor class was
eliminated.

Fixed ``PyCrustAlaCarte.py``, which had been broken by previous
changes.

Created ``InterpreterAlaCarte`` class as an example for use in the
demo.

Split ``PyCrust.py`` into ``PyCrust.py`` and ``PyShell.py`` in
anticipation of ``PyFilling.py``.


0.5.3 (8/16/2001)
-----------------

Added patch to ``PyCrust.py`` to fix wxPython bug::

    wxID_SELECTALL = NewId() # This *should* be defined by wxPython.


0.5.2 (8/14/2001 to 8/15/2001)
------------------------------

Shortened module names by dropping "PyCrust" as a prefix.

Changed ``version`` to ``VERSION`` in ``version`` module.

Added Options menu to PyCrust application.

Eliminated the Editor class (and editor module) by merging with Shell.
This means that Shell "is a" wxStyledTextCtrl rather than "has a".
There just wasn't enough non-gui code to justify the separation.
Plus, Shell will be much easier for gui toolkits/designers to deal
with now.


0.5.1 (8/10/2001 to 8/14/2001)
------------------------------

Added ``introspect`` module.

Moved some functionality from ``PyCrustInterp`` to ``introspect``.

Changed ``introspect.getRoot()`` to no longer remove whitespace from
the command.  This was a remnant of a previous approach that, when
left as part of the current approach, turned out to be a really bad
thing.

Changed ``introspect.getRoot()`` to allow commands of ``''``, ``""``,
``""""""``, ``[]``, ``()``, and ``{}`` to pass through.  This allows
you to type them, followed by a dot, and get autocomplete options on
them.

Changed ``introspect.getRoot()`` to identify some situations where
strings shouldn't be considered roots.  For example::

    >>> import PyCrust  # To illustrate the potential problem.
    >>> len('PyCrust.py')

Typing the dot at the end of "PyCrust" in the second line above should
NOT result in an autocompletion list because "PyCrust" is part of a
string in this context, not a reference to the PyCrust module object.
Similar reasoning applies to call tips.  For example::

    >>> len('dir(')

Typing the left paren at the end of "dir" should NOT result in a call
tip.

Both features now behave properly in the examples given.  However,
there is still the case where whitespace precedes the potential root
and that is NOT handled properly.  For example::

    >>> len('this is a dir(')

and::

    >>> len('This is PyCrust.py')

More code needs to be written to handle more complex situations.

Added ``locals=None`` parameter to ``Shell.__init__()``.

Added support for magic attribute retrieval.  Users can change this
with::

    >>> shell.editor.autoCompleteIncludeMagic = 0

Added the ability to set filters on auto completion to exclude
attributes prefixed with a single or double underscore.  Users can
exclude one or the other or both with::

    >>> shell.editor.autoCompleteExcludeSingle = 1
    >>> shell.editor.autoCompleteExcludeDouble = 1


0.5 (8/8/2001)
--------------

Mostly just a final version change before creating a release.


0.4 (8/4/2001 to 8/7/2001)
--------------------------

Changed version/revision handling.

Fixed bugs.


0.3 (8/2/2001 to 8/3/2001)
--------------------------

Removed lots of cruft.

Added lots of docstrings.

Imported to CVS repository at SourceForge.

Added call tips.


0.2 (7/30/2001 to 8/2/2001)
---------------------------

Renamed several files.

Added command autocompletion.

Added menus to PyCrust.py: File, Edit and Help.

Added sample applications: ``PyCrustAlaCarte.py``,
``PyCrustAlaMode.py``, and ``PyCrustMinimus.py``.


0.1 (7/1/2001 to 7/19/2001)
---------------------------

Added basic syntax coloring much like Boa.

Added read-only logging much like IDLE.

Can retrieve a previous command by putting the cursor back on that
line and hitting enter.

Stdin and raw_input operate properly so you can now do ``help()`` and
``license()`` without hanging.

Redefined "quit", "exit", and "close" to display a better-than-nothing
response.

Home key honors the prompt.

Created SourceForge account, but nothing was posted.


In the beginning, there was pie... (7/1/2001)
---------------------------------------------

Blame it all on IDLE, Boa and PythonWin.  I was using all three, got
frustrated with their dissimilarities, and began to let everyone know
how I felt.  At the same time, Scintilla looked like an interesting
tool to build a shell around.  And while I didn't receive much in the
way of positive feedback, let alone encouragement, I just couldn't let
go of the idea of a Scintilla-based Python shell.  Then the PythonCard
project got to the point where they were talking about including a
shell in their development environment.  That was all the incentive I
needed.  PyCrust had to happen...
=====================================
 PyCrust - The Flakiest Python Shell
=====================================

Half-baked by Patrick K. O'Brien (pobrien@orbtech.com)

Orbtech - "Your source for Python programming expertise."
Sample all our half-baked Python goods at www.orbtech.com.


What is PyCrust?
----------------

PyCrust is an interactive Python environment written in Python.
PyCrust components can run standalone or be integrated into other
development environments and/or other Python applications.

PyCrust comes with an interactive Python shell (PyShell), an
interactive namespace/object tree control (PyFilling) and an
integrated, split-window combination of the two (PyCrust).


What is PyCrust good for?
-------------------------

Have you ever tried to bake a pie without one? Well, you shouldn't
build a Python program without a PyCrust either.


What else do I need to use PyCrust?
-----------------------------------

PyCrust requires Python 2.2 or later, and wxPython 2.4 or later.
PyCrust uses wxPython and the Scintilla wrapper (wxStyledTextCtrl).
Python is available at http://www.python.org/.  wxPython is available
at http://www.wxpython.org/.


Where can I get the latest version of PyCrust?
----------------------------------------------

The latest production version ships with wxPython.  The latest
developer version is available in the wxWindows CVS at:
http://cvs.wxwindows.org/viewcvs.cgi/


Where is the PyCrust project hosted?
------------------------------------

The old answer was "At SourceForge, of course." The SourceForge
summary page is still available at:
http://sourceforge.net/projects/pycrust/

The new answer is that there is no longer a need for a separate
project.  Simply install wxPython and you'll have everything you need.


I found a bug in PyCrust, what do I do with it?
-----------------------------------------------

You can send it to me at pobrien@orbtech.com.


I want a new feature added to PyCrust. Will you do it?
------------------------------------------------------

Flattery and money will get you anything. Short of that, you can send
me a request and I'll see what I can do.


Does PyCrust have a mailing list full of wonderful people?
----------------------------------------------------------

As a matter of fact, we do. Join the PyCrust mailing lists at:
http://sourceforge.net/mail/?group_id=31263


