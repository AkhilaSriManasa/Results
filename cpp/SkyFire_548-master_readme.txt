# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# Set projectname (must be done AFTER setting configurationtypes)
project(Project_Skyfire)

if( UNIX )
  cmake_minimum_required(VERSION 3.10.2)
else()
  cmake_minimum_required(VERSION 3.15.1)
endif()

# CMake policies (can not be handled elsewhere)
cmake_policy(SET CMP0005 OLD)

# add this options before PROJECT keyword
set(CMAKE_DISABLE_SOURCE_CHANGES ON)
set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)

# Set RPATH-handing (CMake parameters)
set(CMAKE_SKIP_BUILD_RPATH 0)
set(CMAKE_BUILD_WITH_INSTALL_RPATH 0)
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH 1)
	   
# set macro-directory
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/macros")

# Set a default build type if none was specified
if( NOT CMAKE_BUILD_TYPE )
  message(STATUS "Setting build type to 'Release' as none was specified.")
  set(CMAKE_BUILD_TYPE "Release")
endif()

include(CheckCXXSourceRuns)
include(CheckIncludeFiles)

# set default buildoptions and print them
include(cmake/options.cmake)

# turn off PCH totally if enabled (hidden setting, mainly for devs)
if( NOPCH )
  set(USE_COREPCH 0)
  set(USE_SCRIPTPCH 0)
endif()

include(CheckPlatform)

set(OPENSSL_EXPECTED_VERSION 1.1.1)
set(ACE_EXPECTED_VERSION 6.4.5)

find_package(PCHSupport)
find_package(ACE REQUIRED)
find_package(OpenSSL REQUIRED)
find_package(Threads REQUIRED)
find_package(MySQL REQUIRED)

if( UNIX )
  find_package(Readline)
  find_package(ZLIB)
  find_package(BZip2)
endif()

if(NOT WITHOUT_GIT)
  find_package(Git)
endif()

# Find revision ID and hash of the sourcetree
include(cmake/genrev.cmake)

# print out the results before continuing
include(cmake/showoptions.cmake)

# add dependencies
add_subdirectory(dep)

# add core sources
add_subdirectory(src)
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.
<!--- (**********************************)
      (** Fill in the following fields **)
      (**********************************) --->

**Description:**

CHANGEME Description of the problem or issue here.

**Current behaviour:**

CHANGEME Tell us what happens.
If this is a crash, post the crashlog (upload to https://gist.github.com/).

**Expected behaviour:**

CHANGEME Tell us what should happen instead.

**Steps to reproduce the problem:**

1. CHANGEME Step 1 include entries of affected creatures / items / quests with a link to the relevant wowhead page.  
2. Step 2
3. Step 3

**SF rev. hash/commit:** 

CHANGEME Copy the first line of the `worldserver`, `authserver` or `bnetserver` startup.
For example: Skyfire rev. 0000000000 2000-01-09 11:31:41 +0100 (my branch) (Win64, RelWithDebInfo, Static) (bnetserver)

**SFDB version:**  CHANGEME Version of the Skyfire database

**Operating system:** CHANGEME OS


<!--- Notes
- This template is for problem reports. For other types of report, edit it accordingly.
- For fixes containing C++ changes, create a Pull Request.
--->[![Stories in Ready](https://badge.waffle.io/ProjectSkyfire/SkyFire.548.png?label=ready&title=Ready)](https://waffle.io/ProjectSkyfire/SkyFire.548) [![Insight.io](https://insight.io/repoBadge/github.com/ProjectSkyfire/SkyFire.548)](https://insight.io/github.com/ProjectSkyfire/SkyFire.548)

# ![logo](https://abload.de/img/15_14_skyfire_logoqyj68.png)

## Project Information
SkyFire is a *MMORPG* Framework based mostly on C++.

SkyFireEMU is a MMORPG Framework based mostly on C++. It is completely 
open-source, and is community supported. It is derived
from CactusEmu, TrinityCore, and MaNGOS, the Massive Network Game Object Servers, 
and is based on the code of there projects with extensive changes over time to optimize, 
improve and cleanup the code base at the same time as improving the in game mechanics
and functionality.

It is completely open source; community involvement is highly encouraged.

If you wish to contribute ideas or code please visit our site linked below or
make pull requests to our 
[Github repository](https://github.com/ProjectSkyfire/SkyFire.548).

For further information on the SkyFire project, please visit our project website at 
[projectskyfire.org](http://www.projectskyfire.org).

## Supported Client Version
**MoP 5.4.8 Build 18414**

## Client Patch
[SkyFire-Community-Tools](https://github.com/ProjectSkyfire/SkyFire-Community-Tools).

## Build Status
# [![Build Status](https://travis-ci.org/ProjectSkyfire/SkyFire_548.png)](https://travis-ci.org/ProjectSkyfire/SkyFire_548)

## Requirements
+ Platform/Architecture:
  + Canonical:
    + Ubuntu 18.04 LTS: x86_32, x86_64
  + Debian:
    + Debian GNU/Linux 10: x86_32, x86_64
  + Windows / Windows Server:
    + Windows 10:               x86_64
    + Windows 8.1:              x86_64
    + Windows 2016 Server:      x86_64
    + Windows 2012 Server R2:   x86_64
+ Processor with SSE2 support
+ ACE = 6.4.5  (Linux only)
+ MySQL = 8.0 (Windows / Linux)
+ CMake = 3.13.1/3.10.2 (Windows / Linux)
+ OpenSSL = 1.1.1 (Windows / Linux)
+ GCC = 9.2.1 (Linux only)
+ MS Visual Studio = 16 (2019) (Windows only)

## Install
Detailed installation guides are available in the wiki for

[Windows](http://wiki.projectskyfire.org/index.php?title=Installation_Windows),
[Linux](http://wiki.projectskyfire.org/index.php?title=Installation_Linux) and
[Mac OSX](http://wiki.projectskyfire.org/index.php?title=Installation_Mac_OS_X).


## Reporting issues
Please use the search function before you report issues.
[SkyFire Issue Tracker](https://github.com/ProjectSkyfire/SkyFire.548/issues).

## Submitting fixes
Fixes are submitted as pull requests via Github.

[SkyFire Pull Request](https://github.com/ProjectSkyfire/SkyFire.548/pulls)

## Copyright
License: GPL 3.0

Read file [COPYING](COPYING.md)

## Authors &amp; Contributors
Read file [THANKS](THANKS.md)

## To-Do List
Read File [TO-DO](TODO.md)

## Links
Forum [https://forum.projectskyfire.org/](https://forum.projectskyfire.org/)

Database [https://forum.projectskyfire.org/index.php?/files/](https://forum.projectskyfire.org/index.php?/files/)

Wiki [http://wiki.projectskyfire.org](http://wiki.projectskyfire.org)
= Project SkyFire -- Thanks/credits file =

Project SkyFire is a derivation/rewrite of MaNGOS & TrinityCore, which was originally written
by Team Python and the WoW Daemon Team. Many people further helped Trinity Core
by submitting bug reports, code patches, and suggestions. Thanks to the
community!

Special thanks should go out to the WowwoW team. We have gained help from
them many times in the creation of this project. Keep up the good work guys.

Thanks to the ScriptDev2 team (http://www.scriptdev2.com) for scripts.

Thanks to the WCell team (especially Ralek) for research on realm reconnect
sequence, item scaling stats algorithm, gameobject rotation issues.

Thanks go out to the following people for various patches/code (listed in the
order they were added) (there may be duplicates or invalid names, most of them
were extracted from commits):

- _manuel_
- `win 
- 0xFuture 
- 123qwe 
- 19Maxx83 
- 3kids 
- 4m1g0 
- aai 
- Abdollah Hasan 
- adrycasillo 
- aerione_alt 
- AFROM 
- Akama 
- Albis 
- Albrecht de Endrau 
- Alestaan 
- Alex
- Alex Bolotsin 
- alex_1983 
- Alexander 
- alexbolotsin
- AlexDereka 
- alexsot 
- Alez 
- AliveShiro 
- AlterEgo 
- Alternative 
- Alyen
- Ambal 
- Amit 
- Amit86 
- amnell 
- Amok 
- amsjunior123
- AniRB 
- announce 
- antihrists 
- Anubisss 
- Aokromes 
- ApoC
- aqs999 
- arcanzic 
- arclite 
- ArcticDevil 
- arcx 
- arez 
- AriDEV 
- Aristoo 
- armano2 
- Arthas 
- Arthorius 
- arthurcik 
- ArticDevil 
- Asael 
- Astellar 
- Athor 
- Authorius 
- aven_coda 
- Aviram 
- Az@zel 
- Azazel
- Azrael
- Azuritus 
- Bagsac 
- balrok 
- Beaste 
- Bezo 
- Big 
- bigjohnson4 
- Biglad 
- BioHazard 
- Bizzy 
- bkhorizon 
- BlackCat0110 
- blackmanos 
- BlackOne
- BlackYoghurt 
- Bladex 
- Blaymoira 
- blub 
- BlueSteel 
- bobaz 
- Bodeguero 
- bodompelle 
- bogie 
- BombermaG 
- Boogie 
- boom
- Bootz 
- Brats 
- breakerfly
- Brian 
- BroodWyrm 
- Brueggus 
- BudIcePenguin 
- bufferoverflow 
- Bulkin 
- burnham
- bytewaior 
- caffeine239 
- Cass 
- cca220v 
- cccyril 
- CDawg 
- CeIa 
- Ceris 
- Cha0S2 
- Chaplain 
- Charlie 
- Charlie2025 
- Chaz Brown
- Chesterfield 
- Chipsi 
- Christyan 
- ckegg 
- Cleave 
- clement.roussel 
- click
- clotza 
- Cnillidan 
- Coldblooded
- cookta2012 
- Corfen 
- crackm 
- Craker 
- CRAZyBUg 
- Cron 
- cryingcloud 
- CrYser 
- Curuad 
- cyberbrest 
- Cybrax 
- D_Skywalk 
- D3VIL 
- DaGNU 
- Dakeyras 
- Dani 
- danik 
- Dark0r 
- darkEvil 
- DarkRabbit 
- Darkshines
- darkstalker 
- DarkXuan 
- DasBlub 
- daveh 
- David Klepáček 
- Deafboy 
- DearScorpion
- death420 
- defacer
- deicide 
- DemiDroL
- Demonx 
- Den 
- DEN_North 
- denyde 
- DerDyddye 
- dereka
- Derex
- derex_tri 
- Destalker
- destros 
- Dimitro 
- disassebler
- Disassembler 
- Discover 
- Discovered 
- DiSlord 
- domingo
- DonTomika
- dr.skull 
- dr.tenma 
- draco 
- dracula70 
- DragonHunter 
- Drahy 
- Drake Fish 
- Drethek 
- Drevi 
- DrTenma 
- duckman 
- durotar 
- dythzer 
- E. van Harten 
- e@cacaw.net 
- e000 
- Ebrithil 
- ebx 
- Edder 
- edrinn 
- EdwinDW 
- EIFEL 
- eL
- elecyb 
- EleGoS
- Elminster 
- Elron 
- elron103 
- Emo Norfik 
- emsy 
- EnderGT 
- enjoi 
- Enril 
- Epsik 
- erimioa 
- Erocoloco
- et2012 
- eumario 
- evilstar 
- Exodius 
- Exordian 
- exul182 
- F636y623 
- Fabian 
- False 
- faq 
- faq_ 
- Farah 
- faramir118 
- FaTe753 
- Feanordev 
- FearX 
- Fest 
- fgenesis 
- filip.havlicek 
- fisherman
- Fog 
- Foks 
- footman 
- Forgiven 
- Frankir 
- Frca 
- fredi
- Fredi Machado 
- freeganja 
- fregh 
- freghar 
- FrenchW 
- frozenarmor 
- FrozenDB 
- fukifat 
- furion 
- Furion89 
- Gacko 
- gadge 
- ge0rg 
- gecko32 
- Geekotron
- Genars 
- Gendalph 
- Geodar 
- ghost 
- Gigatotem 
- gildor 
- Giuseppe Montesanto 
- glkrlos 
- Go6o 
- GodsdoG 
- Gomez 
- Gommes 
- Google 
- Greymane
- GriffonHeart 
- Grobi 
- guenex 
- gvcoman 
- GWRde 
- Gyullo 
- Gyx 
- hacknowledge 
- Havenard 
- Hawthorne 
- hectolight 
- Heisenberg 
- Helias 
- hexa 
- Hexit
- HiZed 
- horn 
- horogandris 
- hoshie
- HP1 
- Hunteee 
- hunuza 
- hyriuu 
- iadus3 
- idostyle@zoit 
- Ille 
- Ille000 
- imbecile 
- Imprtat 
- IncoGnito 
- Infinity 
- Insider 
- insider42 
- irish 
- Iskander 
- Itch 
- j4r0d
- Jackpoz 
- Jeniczek
- Jesper Meyer 
- Jildor 
- Joeri Thissen 
- John Holiver 
- johnholiver 
- jojo 
- Jolan 
- Jon 
- JoN0 
- Joni
- Jorge 
- Joro 
- jorooo 
- joschiwald 
- Joshh 
- joshwhedon
- jotapdiez 
- jrkpote
- JuliuSZS 
- jurkovic.nikola 
- Ka0z 
- Kaelima
- kaell
- Kaldorei 
- kamir86 
- kancaras 
- Kandera 
- KAPATEJIb 
- Kapoeira 
- kaxap 
- kb_z 
- KerchumA222 
- Kezo90 
- Kiddie 
- Kierkegaard 
- KingPin 
- Kinzcool 
- Kipe
- Kiper 
- KiriX
- Klaimmore 
- Koani 
- Koord 
- kozelo 
- Kretol 
- krz 
- Kudlaty 
- Kuteur 
- L30m4nc3r 
- laise 
- laly 
- Larva 
- LaserJet 
- laviniu 
- Lazzalf 
- Leak 
- Liberate 
- Lightguard 
- LihO 
- LiMCrosS 
- linencloth 
- liszt 
- lobuz 
- loop69 
- Lopin 
- Lorac 
- LordJZ 
- lost-illusion 
- Lucy 
- Lukaasm 
- Luniz2k1 
- Lutik 
- Lynx3d 
- m.ax 
- maanuel 
- Machiavelli 
- MacWaior 
- MadJack 
- maikash 
- make_the_king 
- Malcrom 
- mansemino
- manuel
- Manuel Caasco 
- Mark07 
- Martin Weinelt
- MaS0n 
- Matthew Goff 
- maxdestroyer 
- MaXiMiUS 
- Maxxie
- McBitter 
- McLovin 
- MeanMachine
- Medwise 
- megamage 
- Meldanor 
- Menia 
- menke
- Merlin2010 
- MetaphysicalDrama 
- miebaik 
- Mik43l
- mike753 
- miranda.conrado 
- mknjc 
- mns 
- Moandor 
- mobel 
- Molius 
- moriquendu 
- Morpheux 
- mrbungle 
- mrquickfx 
- MrSmite 
- MrTux 
- Mufik 
- Muhaha 
- multiplexer 
- Multivitamin 
- mweinelt 
- Myran2 
- n0n4m3 
- n4ndo 
- n4rk0 
- Nafsih 
- Naga
- Naicisum 
- nanouniko 
- Naturamen 
- Nay 
- Nayre 
- NeatElves 
- Necro 
- Necroo 
- nelegalno 
- Nemesis 
- neo0608 
- Neo2003 
- NeoLithicX 
- Ner'zhul 
- nesocip 
- netoya 
- NetSky 
- neuro_999 
- neurorulez
- Nevan 
- new001 
- Nexflame 
- Nezemnoy 
- nihal 
- nissen
- Nivelo 
- NNN666 
- NoFantasy 
- Northstrider
- nos4r2zod 
- Ntsc 
- NTX 
- nucleartux 
- nugu100
- Nui 
- oc_redfox 
- Oculus 
- Odyssey 
- ogeraisi 
- oiler2112
- oMadMano 
- onkelz28 
- Opterman
- Ottowayne 
- Ouden 
- p.alexej 
- p0wer
- PainKiller
- Palabola 
- panaut0lordv 
- Paradox 
- pasdVn 
- Patro 
- Payn 
- Paytheo 
- peaceman 
- pek2011 
- peldor 
- pendragon 
- Per Wilhelmsen 
- Pesthuf 
- Phacops 
- Pitcrawler 
- PKX 
- Prince 
- PrinceCreed
- Projectcore
- Proofzor 
- PSZ 
- QAston 
- qaywsx
- QuaLiT1 
- qubix 
- raczman 
- raftom 
- RammboNr5 
- Ramses_II 
- Ramus 
- Ramusik 
- Rastik 
- rastikzzz 
- Rat 
- raven_coda 
- Rawaho 
- rechapa79 
- redcore
- RedSonja 
- reno 
- retriman 
- Reve 
- Riccardo 
- riddick 
- rilex 
- rj686 
- Rochet2 
- rockzOr 
- Rognar 
- Roland 
- runningnak3d 
- rvnth 
- Saeba 
- Santiago 
- Sarjuuk 
- Sawiner 
- scarymovie87 
- Scazzato88
- Sebastián Orellana 
- seirge 
- Seizerkiller 
- Seline 
- Sephiroth1984
- Seraphim 
- SeT 
- Sethoso 
- SeTM 
- Shauren 
- shax
- Shendor 
- ShinDarth 
- shlomi1515 
- Shocker 
- SignFinder 
- Silinoron 
- silver1ce 
- SilverIce
- simak 
- simon 
- SimonDMII 
- Sisif 
- Skystar 
- SLG 
- Smakapotatis 
- smellbee 
- SnakeIce 
- Socolin 
- sohrab 
- sombre88 
- Sony 
- Sorken 
- Sorya 
- Souler
- SoulForge 
- Sovak 
- sparc
- spgm 
- Splinter 
- Spp 
- srounet 
- Stalker_Riddick 
- Stalker-Riddick 
- StarJoker 
- Stefo 
- stfx 
- Stokrotka 
- StormByte 
- Stryker 
- Studioworks 
- subhuman_bob 
- Subv 
- Sundark
- sunwell 
- SupaBad 
- svannon 
- Syntec 
- SyRiOCoP
- Taliesin 
- Tanatos 
- Tartalo 
- Taser 
- Tassader 
- TCKiper 
- teacher 
- teacher4 
- tehmarto 
- telsamat 
- teorbringer 
- Tequila 
- teyrnon 
- tharaca 
- The Game 
- The_Game_Master 
- Them 
- Themris 
- thenecromancer 
- thesensei 
- thmarth
- thomas33 
- Thraxx 
- throneinc
- thumsoul 
- thymuswisewood 
- Thyros 
- tibbi 
- Tidus 
- timmit 
- Tiretunderl 
- tlexii
- tobmaps 
- toilet1 
- TOM_RUS
- Tomas 
- Tome 
- Tommassino
- toshik 
- totoro 
- Trazom 
- Trazom62 
- tREAk 
- trickerer 
- Triply 
- Trista
- Trogvar
- Trojan 
- Troy 
- TrullyONE 
- Turk3y 
- Turok 
- Tux`Volant 
- Tuxity 
- tvaroh 
- Typhoon 
- unholy
- unknown
- Uruviel 
- vagoth 
- Valcorb
- Various 
- Vaughner 
- vcrx6 
- Velorien 
- Venugh 
- Veras 
- Vicos 
- Vincent-Michael
- Vinolentus 
- Visagalis 
- Vlad 
- vlad852 
- VladimirMangos 
- Vladmim�r Lipt�k 
- vladonix 
- w12x 
- w1sht0l1v3
- waiorpoetex 
- WarHead 
- Warpten 
- weclub
- Wilds 
- wilibald09 
- Willian Krueger 
- Win32 
- WishToDie 
- Wispeckt 
- Wizz 
- wonopon 
- Wormheart 
- wowgargamel 
- Wowka321 
- Wyk3d 
- Xanadu 
- Xanvial 
- Xees 
- Xeptor 
- XEQT 
- xILOSWag 
- xK1 
- Xlybriem 
- X-Savior 
- XTElite1 
- XTZGZoReX 
- yad02 
- Yaki Khadafi 
- yavi 
- Yelvann 
- Zalito12 
- Zcuron 
- Zerg2000
- zergtmn 
- zhanhang03
- zhenya 
- zoidmann 
- zori 
- zorix 
- zthoreen 
- zwerg 
- zxbiohazardzx 
==== PHP merger (index.php + merge.php) ====

This is a PHP script for merging a new .dist file with your existing .conf file (worldserver.conf.dist and authserver.conf.dist)
It should also work with mangos dist/conf files as well.

It uses sessions so it is multi user safe, it adds any options that are removed to the bottom of the file,
commented out, just in case it removes something it shouldn't,
and, if you add all of your custom patch configs below "# Custom" they will be copied exactly as they are.

==== Perl merger (tc-conf-merger.pl) ====

Perl based command line merger script. This script feeds a .conf.dist file with variables that exist in an old .conf file,
comments and custom options are ignored.
The included crashreport.gdb allows for semiautomated hunting of 
crashes. The crashlog-file will be named backtrace.log and contains all 
the commands required to partially automate a crashlog-creation with the 
proper information.

Usage: gdb -x crashreport.gdb <executable file>

For creating an efficient backtrace, use -DCMAKE_BUILD_TYPE=Debug as a 
parameter to CMake during configuration - this increases the filesize, 
but includes all the needed information for a decent and efficient 
crashreport.

-- Good luck, and happy crashhunting.
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

if( CMAKE_COMPILER_IS_GNUCXX )
  add_definitions(--no-warnings)
elseif( MSVC )
  add_definitions(/W0)
endif()

if(CMAKE_SYSTEM_NAME MATCHES "Linux")
  if(SERVERS AND NOT NOJEM)
    add_subdirectory(jemalloc)  
  endif()
endif()

if(CMAKE_SYSTEM_NAME MATCHES "Windows")
  add_subdirectory(acelite)
  if(TOOLS)
    add_subdirectory(bzip2)
  endif()
endif()

add_subdirectory(zlib)
add_subdirectory(g3dlite)
add_subdirectory(recastnavigation)

if(SERVERS)
  add_subdirectory(gsoap)
endif()

if(TOOLS)
  add_subdirectory(StormLib)
endif()
SkyFire uses (parts of or in whole) the following opensource software :

ACE (ADAPTIVE Communication Environment)
  http://www.cs.wustl.edu/~schmidt/ACE.html
  Version: 6.1.4

bzip2 (a freely available, patent free, high-quality data compressor)
  http://www.bzip.org/
  Version: 1.0.6

G3D (a commercial-grade C++ 3D engine available as Open Source (BSD License)
  http://g3d.sourceforge.net/
  Version: 8.01-Release

jemalloc (a general-purpose scalable concurrent malloc-implementation)
  http://www.canonware.com/jemalloc/
  Version: 3.3.1
 
SFMT (SIMD-oriented Fast Mersenne Twister)
  Based on http://agner.org/random/
  Version: 2010-Aug-03

utf8-cpp (UTF-8 with C++ in a Portable Way)
  http://utfcpp.sourceforge.net/
  Version: 2.3.4

zlib (A Massively Spiffy Yet Delicately Unobtrusive Compression Library)
  http://www.zlib.net/
  Version: 1.2.7

gSOAP (a portable development toolkit for C and C++ XML Web services and XML data bindings)
  http://gsoap2.sourceforge.net/
  Version: 2.8.10

recastnavigation (Recast is state of the art navigation mesh construction toolset for games)
  http://code.google.com/p/recastnavigation/
  Version: 1.4

StormLib (a pack of modules, written in C++, which are able to read and also to write files from/to the MPQ archives)
  http://www.zezula.net/en/mpq/stormlib.html
  Version: 8.04
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

add_subdirectory(ace)
This document is also available at the following URL:

http://www.dre.vanderbilt.edu/~schmidt/ACE.html

All software and documentation is available via both anonymous ftp and
http.

THE ADAPTIVE COMMUNICATION ENVIRONMENT (ACE)

An Object-Oriented Network Programming Toolkit

----------------------------------------

Overview of ACE

The ADAPTIVE Communication Environment (ACE) is an object-oriented
(OO) toolkit that implements fundamental design patterns for
communication software.  ACE provides a rich set of reusable C++
wrappers and frameworks that perform common communication software
tasks across a range of OS platforms, including Win32/Win64, most
versions of UNIX (e.g., SunOS, HP-UX , AIX, Linux, NetBSD, and FreeBSD),
real-time operating systems (e.g., VxWorks, Chorus, LynxOS, and QNX),
OpenVMS, and MVS OpenEdition.  A single source tree is used for all
these platforms and porting ACE to other platforms is relatively easy.

The communication software components provided by ACE include event
demultiplexing and event handler dispatching, service initialization,
interprocess communication, shared memory management, message routing,
dynamic (re)configuration of distributed services, multi-threading,
and concurrency control.  There are both C++ and Java versions of ACE
available.

ACE is targeted for developers of high-performance and real-time
communication services and applications on UNIX, POSIX, and Win32
platforms.  ACE simplifies the development of OO network applications
and services that utilize interprocess communication, event
demultiplexing, explicit dynamic linking, and concurrency.  ACE
automates system configuration and reconfiguration by dynamically
linking services into applications at run-time and executing these
services in one or more processes or threads.

ACE is currently used in commercial projects and products by dozens of
companies including Ericsson, Bellcore, Siemens, Motorola, Kodak,
Boeing, Lucent, DEC, Lockheed Martin, and SAIC.  Commercial support
for ACE is available from several companies as listed at
http://www.dre.vanderbilt.edu/~schmidt/commercial-support.html

----------------------------------------

C++ Wrappers for OS Interfaces

The lower-level portions of ACE provide a set of portable and
type-secure C++ wrappers that encapsulate the following C language OS
interfaces:

. IPC mechanisms
  -- e.g., Internet- and UNIX-domain sockets, TLI, Named
      Pipes (for UNIX and Win32) and STREAM pipes;

. Event demultiplexing
  -- e.g., select(), poll(), and Win32
      WaitForMultipleObjects and I/O completion ports;

. Multi-threading and synchronization
  -- e.g., Solaris threads, POSIX Pthreads, and Win32
      threads;

. Explicit dynamic linking
  -- e.g., dlopen/dlsym on UNIX and LoadLibrary/GetProc
      on Win32;

. Memory-mapped files and shared memory management
  -- e.g., BSD mmap(), SYSV shared memory, and Win32
      shared memory;

. System V IPC
  -- e.g., shared memory, semaphores, message queues.

The OS Adaptation Layer shields the upper levels of ACE from platform
dependencies associated with the underlying OS interfaces.

----------------------------------------

Frameworks and Class Categories

ACE also contains a higher-level network programming framework that
integrates and enhances the lower-level C++ wrappers.  This framework
supports the dynamic configuration of concurrent distributed services
into applications.  The framework portion of ACE contains the
following class categories:

. The Reactor
  -- Supports both Reactive and Proactive I/O;

. The Service Configurator
  -- Support dynamic (re)configuration of objects;

. The ADAPTIVE Service Executive
  -- A user-level implementation of System V STREAMS,
      that supports modular integration of
      hierarchically-related communication services;

. Concurrency
  -- Various types of higher-level concurrency
      control and synchronization patterns (such as
      Polymorphic Futures and Active Objects);

. Shared Malloc
  -- Components for managing dynamically allocation
      of shared and local memory;

----------------------------------------

Distributed Services and Components

Finally, ACE provides a standard library of distributed services that
are packaged as components.  These service components play two roles
in ACE:

1. They provide reusable components for common distributed
    system tasks such as logging, naming, locking, and time
    synchronization.

2. They illustrate how to utilize ACE features such as the
    Reactor, Service Configurator, Service Initialization,
    Concurrency, and IPC components.

----------------------------------------

Middleware Applications

ACE has been used in research and development projects at many
universities and companies.  For instance, it has been used to build
avionics systems at Boeing, telecommunication systems at Bellcore,
Ericsson, Motorola, and Lucent; medical imaging systems at Siemens and
Kodak; and many academic research projects.  Two example middleware
applications provided with the ACE release include:

1. The ACE ORB (TAO) -- TAO is a real-time implementation of
    CORBA built using the framework components and patterns
    provided by ACE.

2. JAWS -- JAWS is a high-performance, adaptive Web server
    built using the components in ACE.

----------------------------------------

OBTAINING ACE

ACE may be obtained electronically from
http://download.dre.vanderbilt.edu.  This release contains the source
code, test drivers, and example applications (including JAWS) for C++
wrapper libraries and the higher-level ACE network programming
framework developed as part of the ADAPTIVE project at the University
of California, Irvine, Washington University, St. Louis, and
Vanderbilt University.

You can get The ACE ORB (TAO) in a companion release at the same URL.

----------------------------------------

ACE DOCUMENTATION AND TUTORIALS

Many of the C++ wrappers and higher-level components have been
described in issues of the C++ Report, as well as in proceedings of
many journals, conferences, and workshops.

A collection of white papers and tutorial handouts are included at

http://www.dre.vanderbilt.edu/~schmidt/ACE-papers.html

This page contains PDF versions of various papers that describe
different aspects of ACE.

This material is also available available via the WWW at URL:

http://www.dre.vanderbilt.edu/~schmidt/ACE.html

----------------------------------------

ACE MAILING LIST AND NEWSGROUP

A mailing list, ace-users@list.isis.vanderbilt.edu, is available for
discussing bug fixes, enhancements, and porting issues regarding ACE.
Please send mail to me at the
ace-users-request@list.isis.vanderbilt.edu if you'd like to join the
mailing list.  There is also a USENET newsgroup called
comp.soft-sys.ace. Please see
http://www.dre.vanderbilt.edu/~schmidt/ACE-mail.html for details on
how to subscribe to the mailing list.

----------------------------------------

BUILDING AND INSTALLING ACE

Please refer to the $ACE_ROOT/ACE-INSTALL.html file for
information on how to build and test the ACE wrappers.  The
BIBLIOGRAPHY file contains information on where to obtain articles
that describe the ACE wrappers and the ADAPTIVE system in more detail.

The current release has been tested extensively, but if you find any
bugs, please report them to the ACE mailing list
ace-users@list.isis.vanderbilt.edu using the
$ACE_ROOT/PROBLEM-REPORT-FORM.  Please use the same form to submit
questions, comments, etc.  To ensure that you see responses, please do
one of the following:

1) Subscribe to the ace-users mail list, by sending email with
    contents "subscribe ace-users" to
    ace-users-request@list.isis.vanderbilt.edu.

2) Or, monitor the comp.soft-sys.ace newsgroup for responses.

----------------------------------------

ACKNOWLEDGEMENTS

Please see the file `$ACE_ROOT/THANKS' for a list of the thousands of
people who've contributed to ACE and TAO over the years.
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# NOTE: Do not use glob here, it would include files we don't want
set(ace_STAT_SRCS
  Abstract_Timer_Queue.cpp
  Acceptor.cpp
  ACE.cpp
  ACE_crc_ccitt.cpp
  ACE_crc32.cpp
  ace_wchar.cpp
  Activation_Queue.cpp
  Active_Map_Manager.cpp
  Active_Map_Manager_T.cpp
  Addr.cpp
  Arg_Shifter.cpp
  ARGV.cpp
  Argv_Type_Converter.cpp
  Array_Base.cpp
  Array_Map.cpp
  Assert.cpp
  Asynch_Acceptor.cpp
  Asynch_Connector.cpp
  Asynch_IO.cpp
  Asynch_IO_Impl.cpp
  Asynch_Pseudo_Task.cpp
  ATM_Acceptor.cpp
  ATM_Addr.cpp
  ATM_Connector.cpp
  ATM_Params.cpp
  ATM_QoS.cpp
  ATM_Stream.cpp
  Atomic_Op.cpp
  Atomic_Op_GCC_T.cpp
  Atomic_Op_Sparc.c
  Atomic_Op_T.cpp
  Auto_Event.cpp
  Auto_Functor.cpp
  Auto_IncDec_T.cpp
  Auto_Ptr.cpp
  Barrier.cpp
  Base_Thread_Adapter.cpp
  Based_Pointer_Repository.cpp
  Based_Pointer_T.cpp
  Basic_Stats.cpp
  Basic_Types.cpp
  Bound_Ptr.cpp
  Cache_Map_Manager_T.cpp
  Cached_Connect_Strategy_T.cpp
  Caching_Strategies_T.cpp
  Caching_Utility_T.cpp
  Capabilities.cpp
  CDR_Base.cpp
  CDR_Size.cpp
  CDR_Stream.cpp
  CE_Screen_Output.cpp
  Cleanup.cpp
  Cleanup_Strategies_T.cpp
  Codecs.cpp
  Codeset_IBM1047.cpp
  Codeset_Registry.cpp
  Codeset_Registry_db.cpp
  Condition_Attributes.cpp
  Condition_Recursive_Thread_Mutex.cpp
  Condition_T.cpp
  Condition_Thread_Mutex.cpp
  Configuration.cpp
  Configuration_Import_Export.cpp
  Connection_Recycling_Strategy.cpp
  Connector.cpp
  Containers.cpp
  Containers_T.cpp
  Copy_Disabled.cpp
  Countdown_Time_T.cpp
  Date_Time.cpp
  DEV.cpp
  DEV_Addr.cpp
  DEV_Connector.cpp
  DEV_IO.cpp
  Dev_Poll_Reactor.cpp
  Dirent.cpp
  Dirent_Selector.cpp
  DLL.cpp
  DLL_Manager.cpp
  Dump.cpp
  Dump_T.cpp
  Dynamic.cpp
  Dynamic_Message_Strategy.cpp
  Dynamic_Service.cpp
  Dynamic_Service_Base.cpp
  Dynamic_Service_Dependency.cpp
  Encoding_Converter.cpp
  Encoding_Converter_Factory.cpp
  Env_Value_T.cpp
  Event.cpp
  Event_Base.cpp
  Event_Handler.cpp
  Event_Handler_Handle_Timeout_Upcall.cpp
  Event_Handler_T.cpp
  FIFO.cpp
  FIFO_Recv.cpp
  FIFO_Recv_Msg.cpp
  FIFO_Send.cpp
  FIFO_Send_Msg.cpp
  FILE.cpp
  FILE_Addr.cpp
  FILE_Connector.cpp
  FILE_IO.cpp
  File_Lock.cpp
  Filecache.cpp
  Flag_Manip.cpp
  Framework_Component.cpp
  Framework_Component_T.cpp
  Free_List.cpp
  Functor.cpp
  Functor_String.cpp
  Functor_T.cpp
  Future.cpp
  Future_Set.cpp
  Get_Opt.cpp
  Guard_T.cpp
  Handle_Ops.cpp
  Handle_Set.cpp
  Hash_Cache_Map_Manager_T.cpp
  Hash_Map_Manager_T.cpp
  Hash_Map_With_Allocator_T.cpp
  Hash_Multi_Map_Manager_T.cpp
  Hashable.cpp
  High_Res_Timer.cpp
  ICMP_Socket.cpp
  INET_Addr.cpp
  Init_ACE.cpp
  Intrusive_Auto_Ptr.cpp
  Intrusive_List.cpp
  Intrusive_List_Node.cpp
  IO_Cntl_Msg.cpp
  IO_SAP.cpp
  IOStream.cpp
  IOStream_T.cpp
  IPC_SAP
  Lib_Find.cpp
  Local_Memory_Pool.cpp
  Local_Name_Space.cpp
  Local_Name_Space_T.cpp
  Local_Tokens.cpp
  Lock.cpp
  Lock_Adapter_T.cpp
  LOCK_SOCK_Acceptor.cpp
  Log_Category.cpp
  Log_Msg.cpp
  Log_Msg_Backend.cpp
  Log_Msg_Callback.cpp
  Log_Msg_IPC.cpp
  Log_Msg_NT_Event_Log.cpp
  Log_Msg_UNIX_Syslog.cpp
  Log_Record.cpp
  Logging_Strategy.cpp
  LSOCK.cpp
  LSOCK_Acceptor.cpp
  LSOCK_CODgram.cpp
  LSOCK_Connector.cpp
  LSOCK_Dgram.cpp
  LSOCK_Stream.cpp
  Malloc.cpp
  Malloc_Allocator.cpp
  Malloc_T.cpp
  Managed_Object.cpp
  Manual_Event.cpp
  Map_Manager.cpp
  Map_T.cpp
  MEM_Acceptor.cpp
  MEM_Addr.cpp
  MEM_Connector.cpp
  MEM_IO.cpp
  Mem_Map.cpp
  MEM_SAP.cpp
  MEM_Stream.cpp
  Message_Block.cpp
  Message_Block_T.cpp
  Message_Queue.cpp
  Message_Queue_NT.cpp
  Message_Queue_T.cpp
  Message_Queue_Vx.cpp
  Method_Request.cpp
  Metrics_Cache_T.cpp
  MMAP_Memory_Pool.cpp
  Module.cpp
  Monitor_Admin.cpp
  Monitor_Admin_Manager.cpp
  Monitor_Base.cpp
  Monitor_Control_Action.cpp
  Monitor_Control_Types.cpp
  Monitor_Point_Registry.cpp
  Monitor_Size.cpp
  Monotonic_Time_Policy.cpp
  Msg_WFMO_Reactor.cpp
  Multihomed_INET_Addr.cpp
  Mutex.cpp
  Name_Proxy.cpp
  Name_Request_Reply.cpp
  Name_Space.cpp
  Naming_Context.cpp
  Netlink_Addr.cpp
  Node.cpp
  Notification_Queue.cpp
  Notification_Strategy.cpp
  NT_Service.cpp
  Null_Mutex.cpp
  Obchunk.cpp
  Object_Manager.cpp
  Object_Manager_Base.cpp
  Obstack.cpp
  Obstack_T.cpp
  OS_Errno.cpp
  OS_Log_Msg_Attributes.cpp
  OS_main.cpp
  OS_NS_arpa_inet.cpp
  OS_NS_ctype.cpp
  OS_NS_devctl.cpp
  OS_NS_dirent.cpp
  OS_NS_dlfcn.cpp
  OS_NS_errno.cpp
  OS_NS_fcntl.cpp
  OS_NS_math.cpp
  OS_NS_netdb.cpp
  OS_NS_poll.cpp
  OS_NS_pwd.cpp
  OS_NS_regex.cpp
  OS_NS_signal.cpp
  OS_NS_stdio.cpp
  OS_NS_stdlib.cpp
  OS_NS_string.cpp
  OS_NS_strings.cpp
  OS_NS_stropts.cpp
  OS_NS_sys_mman.cpp
  OS_NS_sys_msg.cpp
  OS_NS_sys_resource.cpp
  OS_NS_sys_select.cpp
  OS_NS_sys_sendfile.cpp
  OS_NS_sys_shm.cpp
  OS_NS_sys_socket.cpp
  OS_NS_sys_stat.cpp
  OS_NS_sys_time.cpp
  OS_NS_sys_uio.cpp
  OS_NS_sys_utsname.cpp
  OS_NS_sys_wait.cpp
  OS_NS_Thread.cpp
  OS_NS_time.cpp
  OS_NS_unistd.cpp
  OS_NS_wchar.cpp
  OS_NS_wctype.cpp
  OS_QoS.cpp
  OS_Thread_Adapter.cpp
  OS_TLI.cpp
  Pagefile_Memory_Pool.cpp
  Pair_T.cpp
  Parse_Node.cpp
  PI_Malloc.cpp
  Ping_Socket.cpp
  Pipe.cpp
  POSIX_Asynch_IO.cpp
  POSIX_CB_Proactor.cpp
  POSIX_Proactor.cpp
  Priority_Reactor.cpp
  Proactor.cpp
  Proactor_Impl.cpp
  Process.cpp
  Process_Manager.cpp
  Process_Mutex.cpp
  Process_Semaphore.cpp
  Profile_Timer.cpp
  RB_Tree.cpp
  Reactor.cpp
  Reactor_Impl.cpp
  Reactor_Notification_Strategy.cpp
  Reactor_Timer_Interface.cpp
  Read_Buffer.cpp
  Recursive_Thread_Mutex.cpp
  Recyclable.cpp
  Refcountable_T.cpp
  Refcounted_Auto_Ptr.cpp
  Registry.cpp
  Registry_Name_Space.cpp
  Remote_Name_Space.cpp
  Remote_Tokens.cpp
  Reverse_Lock_T.cpp
  Rtems_init.c
  RW_Mutex.cpp
  RW_Process_Mutex.cpp
  RW_Thread_Mutex.cpp
  Sample_History.cpp
  Sbrk_Memory_Pool.cpp
  Sched_Params.cpp
  Select_Reactor_Base.cpp
  Select_Reactor_T.cpp
  Semaphore.cpp
  Service_Config.cpp
  Service_Gestalt.cpp
  Service_Manager.cpp
  Service_Object.cpp
  Service_Repository.cpp
  Service_Types.cpp
  Shared_Memory.cpp
  Shared_Memory_MM.cpp
  Shared_Memory_Pool.cpp
  Shared_Memory_SV.cpp
  Shared_Object.cpp
  Sig_Adapter.cpp
  Sig_Handler.cpp
  Signal.cpp
  Singleton.cpp
  SOCK.cpp
  SOCK_Acceptor.cpp
  SOCK_CODgram.cpp
  Sock_Connect.cpp
  SOCK_Connector.cpp
  SOCK_Dgram.cpp
  SOCK_Dgram_Bcast.cpp
  SOCK_IO.cpp
  SOCK_Netlink.cpp
  SOCK_SEQPACK_Acceptor.cpp
  SOCK_SEQPACK_Association.cpp
  SOCK_SEQPACK_Connector.cpp
  SOCK_Stream.cpp
  SPIPE.cpp
  SPIPE_Acceptor.cpp
  SPIPE_Addr.cpp
  SPIPE_Connector.cpp
  SPIPE_Stream.cpp
  SString.cpp
  Stack_Trace.cpp
  Stats.cpp
  Strategies_T.cpp
  Stream.cpp
  Stream_Modules.cpp
  String_Base.cpp
  String_Base_Const.cpp
  SUN_Proactor.cpp
  SV_Message.cpp
  SV_Message_Queue.cpp
  SV_Semaphore_Complex.cpp
  SV_Semaphore_Simple.cpp
  SV_Shared_Memory.cpp
  Svc_Conf_Lexer.cpp
  Svc_Conf_y.cpp
  Svc_Handler.cpp
  Synch_Options.cpp
  System_Time.cpp
  Task.cpp
  Task_Ex_T.cpp
  Task_T.cpp
  Test_and_Set.cpp
  Thread.cpp
  Thread_Adapter.cpp
  Thread_Control.cpp
  Thread_Exit.cpp
  Thread_Hook.cpp
  Thread_Manager.cpp
  Thread_Mutex.cpp
  Thread_Semaphore.cpp
  Throughput_Stats.cpp
  Time_Policy.cpp
  Time_Policy_T.cpp
  Time_Value.cpp
  Time_Value_T.cpp
  Timeprobe.cpp
  Timeprobe_T.cpp
  Timer_Hash_T.cpp
  Timer_Heap_T.cpp
  Timer_List_T.cpp
  Timer_Queue_Adapters.cpp
  Timer_Queue_Iterator.cpp
  Timer_Queue_T.cpp
  Timer_Wheel_T.cpp
  TLI.cpp
  TLI_Acceptor.cpp
  TLI_Connector.cpp
  TLI_Stream.cpp
  Token.cpp
  Token_Collection.cpp
  Token_Invariants.cpp
  Token_Manager.cpp
  Token_Request_Reply.cpp
  Tokenizer_T.cpp
  TP_Reactor.cpp
  Trace.cpp
  TSS_Adapter.cpp
  TSS_T.cpp
  TTY_IO.cpp
  Typed_SV_Message.cpp
  Typed_SV_Message_Queue.cpp
  Unbounded_Queue.cpp
  Unbounded_Set.cpp
  Unbounded_Set_Ex.cpp
  UNIX_Addr.cpp
  UPIPE_Acceptor.cpp
  UPIPE_Connector.cpp
  UPIPE_Stream.cpp
  UTF8_Encoding_Converter.cpp
  UTF16_Encoding_Converter.cpp
  UTF32_Encoding_Converter.cpp
  UUID.cpp
  Vector_T.cpp
  WFMO_Reactor.cpp
  WIN32_Asynch_IO.cpp
  WIN32_Proactor.cpp
  XML_Svc_Conf.cpp
  XTI_ATM_Mcast.cpp
)

if (USE_COREPCH)
  set(ace_PCH_HDR PrecompiledHeaders/WinAcePCH.h)
  set(ace_PCH_SRC PrecompiledHeaders/WinAcePCH.cpp)
endif()

include_directories(
  ${CMAKE_SOURCE_DIR}/dep/acelite
  ${CMAKE_CURRENT_SOURCE_DIR}/Compression
  ${CMAKE_CURRENT_SOURCE_DIR}/Compression/rle
  ${CMAKE_CURRENT_SOURCE_DIR}/ETCL
  ${CMAKE_CURRENT_SOURCE_DIR}/FIReactor
  ${CMAKE_CURRENT_SOURCE_DIR}/FoxReactor
  ${CMAKE_CURRENT_SOURCE_DIR}/Monitor_Control
  ${CMAKE_CURRENT_SOURCE_DIR}/ETCL
  ${CMAKE_CURRENT_SOURCE_DIR}/PrecompiledHeaders
  ${CMAKE_CURRENT_SOURCE_DIR}/QoS
  ${CMAKE_CURRENT_SOURCE_DIR}/QtReactor
  ${CMAKE_CURRENT_SOURCE_DIR}/SSL
  ${CMAKE_CURRENT_SOURCE_DIR}/TkReactor
  ${CMAKE_CURRENT_SOURCE_DIR}/XML_Utils
  ${CMAKE_CURRENT_SOURCE_DIR}/XtReactor
  ${CMAKE_SOURCE_DIR}/dep/zlib
)

# Needed for PCH support
set_source_files_properties(Atomic_Op_Sparc.c Rtems_init.c PROPERTIES LANGUAGE CXX)

add_definitions(-DACE_BUILD_DLL)

add_library(ace SHARED
  ${ace_STAT_SRCS}
  ${ace_PCH_SRC}
)

if (MINGW) # GCC ignores "#prama comment"
  target_link_libraries(ace ws2_32 iphlpapi netapi32 mswsock)
endif()

# Generate precompiled header
if( USE_COREPCH )
  add_cxx_pch(ace ${ace_PCH_HDR} ${ace_PCH_SRC})
endif()

install(TARGETS ace RUNTIME DESTINATION "${CMAKE_INSTALL_PREFIX}")
ACE Portability Macros
----------------------

The following describes the meaning of the C++ compiler macros that
can be set in the config*.h file.  When you port ACE to a new platform
and/or C++ compiler, make sure that you check to see which of these
need to be defined.  It's helpful to check the various config*.h files
in this directory to see what's already been defined.  If you need to
add new macros, please send them to me and I'll add them to this file.

Eventually, most of this information should be auto-discovered via GNU
autoconf, which is currently available in the ACE distribution.

Macro                                   Description
-----                                   -----------

ACE_HAS_DUMP                            Used to enable the dump()
                                        method bodies.  If not
                                        defined, the bodies are ifdef
                                        out in order to reduce
                                        footprint.  By default, it is
                                        not defined.
ACE_CAST_CONST                          Used to work around broken
                                        SunCC ANSI casts that require
                                        an extra const.
ACE_DEFINES_DEFAULT_WIN32_SECURITY_ATTRIBUTES
                                        Win32 only.  Users want to use
                                        a predefined security
                                        attributes defined in
                                        ACE_OS::default_win32_security_attributes
                                        as the default security
                                        object.
ACE_DISABLE_MKTEMP                      Disable availability of
                                        ACE_OS::mktemp().
ACE_DISABLE_TEMPNAM                     Disable availability of
                                        ACE_OS::tempnam().
ACE_DISABLE_DEBUG_DLL_CHECK             Define this if you don't want
                                        debug version ACE search for
                                        debug version DLLs first
                                        before looking for the DLL
                                        names specified.
ACE_DOESNT_INSTANTIATE_NONSTATIC_OBJECT_MANAGER
                                        Application will allocate its
                                        own object manager.  This
                                        implicitly defines
                                        ACE_HAS_NONSTATIC_OBJECT_MANAGER.
                                        Usually used with MFC
                                        applications.
ACE_GETNAME_RETURNS_RANDOM_SIN_ZERO     Platform does not initialize
                                        sockaddr_in::sin_zero field in
                                        calls to getpeername() and
                                        getsockname().  As a result,
                                        memcmp()-based equality
                                        comparison can fail despite
                                        the fact two sockaddr_in
                                        instances refer to the same
                                        addr characteristics.
ACE_MAIN                                Renames "main (int, char *[])",
                                        for platforms such as g++/VxWorks
                                        that don't allow "main".  Requires
                                        the use of
                                        ACE_HAS_NONSTATIC_OBJECT_MANAGER.
ACE_MKDIR_LACKS_MODE                    This platform has a mkdir function with
                                        a mode argument
ACE_MT_SAFE                             Compile using multi-thread libraries
ACE_NDEBUG                              Turns off debugging features
ACE_NEW_THROWS_EXCEPTIONS               Compiler's 'new' throws exception on
                                        failure (ANSI C++ behavior).
ACE_NLOGGING                            Turns off the LM_DEBUG and
                                        LM_ERROR logging macros...
ACE_NTRACE                              Turns off the tracing feature when = 1.
ACE_HAS_TRACE                           Defined when ACE_NTRACE=0 to
                                        help support tracing.  Can
                                        also be defined by users who
                                        implement their own tracing
                                        macros based on
                                        ACE_TRACE_IMPL.  Not defining
                                        it helps reduce footprint by
                                        not requiring applications to
                                        link in Trace.o.
ACE_PAGE_SIZE                           Defines the page size of the
                                        system (not used on Win32 or
                                        with ACE_HAS_GETPAGESIZE).
ACE_REDEFINES_XTI_FUNCTIONS             Platform redefines the t_... names (UnixWare)
ACE_TEMPLATES_REQUIRE_PRAGMA            Compiler's template mechanism
                                        must use a pragma This is used
                                        for AIX's C++ compiler.
ACE_TEMPLATES_REQUIRE_SOURCE            Compiler's template mechanim
                                        must see source code (i.e.,
                                        .cpp files).  This is used for
                                        GNU G++.
ACE_TIMEPROBE_ASSERTS_FIXED_SIZE        If enabled then ACE_Timeprobe_Ex<>::timeprobe()
                                        will assert if the end of the
                                        buffer is reached.  If disabled, the
                                        counter wraps around to start
                                        at the beginning of the buffer.
ACE_TIMER_SKEW                          If a timed ::select () can return
                                        early, then ACE_TIMER_SKEW is the
                                        maximum adjustment, in microseconds,
                                        that ACE_Timer_Queue uses to
                                        compensate for the early return.
ACE_TLI_TCP_DEVICE                      Device the platform uses for TCP on
                                        TLI.  Only needed if not /dev/tcp.
ACE_USE_POLL                            The OS platform supports the
                                        poll() event demultiplexor
ACE_USES_ASM_SYMBOL_IN_DLSYM            Platform uses assembly symbols
                                        instead of C symbols in
                                        dlsym()
ACE_USES_STATIC_MFC                     When linking MFC as a static library is desired
ACE_USES_STD_NAMESPACE_FOR_STDCPP_LIB   Platform has its standard c++
                                        library in the namespace std.
ACE_USES_EXPLICIT_STD_NAMESPACE         Set this when ::fclose doesn't
                                        work and you have to
                                        explicitly specify the std
                                        namespace.   This is needed
                                        with the Borland 6 and earlier
                                        compilers.
ACE_USES_GPROF                          ACE calls getitimer before spawning
                                        a new thread and setitimer
                                        after spawning the thread in
                                        order to overcome the problems
                                        of gprof with multithreaded
                                        applications. It uses the idea from
                                        http://sam.zoy.org/writings/programming/gprof.html
ACE_USES_FIFO_SEM                       Directs ACE to use FIFO based semaphores on
                                        platforms that support this (not having full
                                        POSIX semaphore support, supporting mkfifo, select
                                        and fcntl).
ACE_WSOCK_VERSION                       A parameter list indicating
                                        the version of WinSock (e.g.,
                                        "1, 1" is version 1.1).
ACE_HAS_AIO_CALLS                       Platform supports POSIX aio* calls.
                                        Corresponds to _POSIX_ASYNCHRONOUS_IO
                                        constant in <unistd.h>.
ACE_HAS_ALT_CUSERID                     Use ACE's alternate cuserid()
                                        implementation since a system
                                        cuserid() may not exist, or it
                                        is not desirable to use it.
                                        The implementation requires
                                        ACE_LACKS_PWD_FUNCTIONS to be
                                        undefined and that the
                                        geteuid() system call exists.
ACE_HAS_DINKUM_STL                      Using the Dinkum STL library
ACE_HAS_HEADER_ALLOCATED_CLASS_STATIC_CONST_INT_STOREAGE
                                        Non-C++ Complient compilers that automatically
                                        provide storeage for class static const int
                                        when their declaration is seen. I.e. they object
                                        to explicit definitions being seen in the .cpp
                                        file.
ACE_DEFAULT_THREAD_KEYS                 Number of TSS keys, with
                                        ACE_HAS_TSS_EMULATION _only_.
                                        Defaults to 64.
ACE_DEFAULT_THREAD_STACKSIZE            Default stack size specified for the
                                        ACE thread spawning methods. Defaults
                                        to 0, which defers to OS defaults.
ACE_DEFAULT_LD_SEARCH_PATH              Specify the platform default search
                                        paths.  This macro should only be
                                        defined on platforms that don't
                                        support environment variables at all
                                        (i.e., Windows CE.)
ACE_THREADS_DONT_INHERIT_LOG_MSG        Specify this if you don't want
                                        threads to inherit parent
                                        thread's ACE_Log_Msg
                                        properties.
ACE_THREAD_MANAGER_USES_SAFE_SPAWN      Disable the "check before lock" feature
                                        in ACE_Thread_Manager.  Defining this
                                        macro avoids a potential race condition
                                        on platforms with aggressive read/write
                                        reordering.
ACE_HAS_CPU_SET_T                       Platform delivers cpu_set_t.
ACE_HAS_PRIOCNTL                        OS has priocntl (2).
ACE_HAS_RECURSIVE_MUTEXES               Mutexes are inherently recursive
                                        (e.g., Win32)
ACE_HAS_NONRECURSIVE_MUTEXES            In addition to recursive mutexes,
                                        platform has non-recursive ones also.
ACE_HAS_RECV_TIMEDWAIT                  Platform has the MIT pthreads
                                        APIs for
ACE_HAS_RLIMIT_RESOURCE_ENUM            Platform has enum instead of
                                        int for first argument to
                                        ::{get,set}rlimit ().  The
                                        value of this macro is the
                                        enum definition, e.g., enum
                                        __rlimit_resource, for Linux
                                        glibc 2.0.
ACE_HAS_RUSAGE_WHO_ENUM                 Platform has enum instead of
                                        int for first argument to
                                        ::getrusage ().  The value of
                                        this macro is the enum
                                        definition, e.g., enum
                                        __rusage_who, for Linux glibc
                                        2.0.
ACE_HAS_SCANDIR                         Platform has a native scandir()
                                        function. Without any other scandir-
                                        related settings, it's assumed that
                                        the selector and comparator functions
                                        accept const ACE_DIRENT pointers.
ACE_SCANDIR_CMP_USES_VOIDPTR            The OS's scandir() comparator function
                                        is int (*compare)(void*, void*).
ACE_SCANDIR_CMP_USES_CONST_VOIDPTR      The OS's scandir() comparator function
                                        is int (*compare)(const void*,
                                                          const void*).
ACE_SCANDIR_SEL_LACKS_CONST             The OS's scandir() selector function
                                        is int (*selector)(ACE_DIRENT*)
ACE_HAS_STDARG_THR_DEST                 Platform has void (*)(...)
                                        prototype for
                                        pthread_key_create()
                                        destructor (e.g., LynxOS).
ACE_HAS_WIN32_STRUCTURAL_EXCEPTIONS     Platform/compiler supports
                                        Win32 structural exceptions
ACE_HAS_4_4BSD_SENDMSG_RECVMSG          Platform has BSD 4.4
                                        sendmsg()/recvmsg() APIs.
ACE_HAS_P_READ_WRITE                    Platform has pread() and
                                        pwrite() support
ACE_HAS_AIX_BROKEN_SOCKET_HEADER        Platform, such as AIX4, needs
                                        to wrap #include of
                                        sys/socket.h with
                                        #undef/#define of
                                        __cplusplus.
ACE_HAS_AIX_HI_RES_TIMER                Platform has AIX4
                                        ::read_real_time ()
ACE_HAS_ALLOCA                          Compiler/platform supports
                                        alloca()
ACE_HAS_ALLOCA_H                        Compiler/platform has
                                        <alloca.h>
ACE_HAS_ALPHA_TIMER                     CPU is an Alpha, with the rpcc
                                        instruction to read the tick timer.
                                        Limited to 32 bits, so not recommended.
ACE_HAS_AUTOMATIC_INIT_FINI             Compiler/platform correctly
                                        calls init()/fini() for shared
                                        libraries
ACE_HAS_BIG_FD_SET                      Compiler/platform has typedef
                                        u_long fdmask (e.g., Linux and
                                        SCO).
ACE_HAS_WORKING_EXPLICIT_TEMPLATE_DESTRUCTOR
                                        Compiler handles explicit calling of
                                        template destructor correctly. See
                                        "ace/OS.h" for details.
ACE_HAS_BROKEN_ACCEPT_ADDR              Platform can't correctly deal
                                        with a NULL addr to accept()
                                        (e.g, VxWorks < 6.9).
ACE_HAS_BROKEN_DGRAM_SENDV              Platform sendv() does not work
                                        properly with datagrams,
                                        i.e. it fails when the iovec
                                        size is IOV_MAX.
ACE_HAS_BROKEN_MAP_FAILED               Platform doesn't cast MAP_FAILED
                                        to a void *.
ACE_HAS_BROKEN_MSG_H                    Platform headers don't support
                                        <msg.h> prototypes
ACE_HAS_BROKEN_MMAP_H                   HP/UX does not wrap the
                                        mmap(2) header files with
                                        extern "C".
ACE_HAS_BROKEN_NESTED_TEMPLATES         MSVC has trouble with defining
                                        STL containers for nested
                                        structs and classes
ACE_HAS_BROKEN_POSIX_TIME               Platform defines struct
                                        timespec in <sys/timers.h>
ACE_HAS_BROKEN_T_ERROR                  Compiler/platform has the wrong
                                        prototype for t_error(), i.e.,
                                        t_error(char *) rather than
                                        t_error(const char *).
ACE_HAS_BSTRING                         Platform has <bstring.h>
                                        (which contains bzero()
                                        prototype)
ACE_HAS_BYTESEX_H                       Platform has <bytesex.h>.
ACE_HAS_CANCEL_IO                       Platform supports the Win32
                                        CancelIO() function (WinNT 4.0
                                        and beyond).
ACE_HAS_CHARPTR_DL                      OS/platform uses char * for
                                        dlopen/dlsym args, rather than
                                        const char *.
ACE_HAS_CHARPTR_SOCKOPT                 OS/platform uses char * for
                                        sockopt, rather than const
                                        char *
ACE_HAS_CLOCK_GETTIME                   Platform supports POSIX.1b
                                        clock_gettime () at least for clock-id CLOCK_REALTIME
ACE_HAS_CLOCK_GETTIME_MONOTONIC         Platform supports POSIX.1b
                                        clock_gettime () with the clock-id CLOCK_MONOTONIC
ACE_HAS_CLOCK_SETTIME                   Platform supports POSIX.1b
                                        clock_settime ()
ACE_HAS_CONFLICTING_XTI_MACROS          OS's XTI header file defines some
                                        TCP-related macros that netinet/tcp.h
                                        also defines, but they conflict
                                        (only seen on HP-UX 11).
ACE_HAS_CONSISTENT_SIGNAL_PROTOTYPES    Prototypes for both signal()
                                        and struct sigaction are
                                        consistent.
ACE_HAS_CPLUSPLUS_HEADERS               Compiler/platform has
                                        correctly prototyped header
                                        files
ACE_HAS_DIRENT                          Compiler/platform has Dirent
                                        iterator functions
ACE_HAS_DLL                             Build ACE using the frigging
                                        PC DLL nonsense...
ACE_HAS_EBCDIC                          Compile in the ACE code set classes
                                        that support EBCDIC.
ACE_HAS_EXCEPTIONS                      Compiler supports C++
                                        exception handling
ACE_HAS_EXPLICIT_TEMPLATE_INSTANTIATION_EXPORT  When a base-class is a
                                        specialization of a class template
                                        then this class template must be
                                        explicitly exported
ACE_HAS_EXPLICIT_STATIC_TEMPLATE_MEMBER_INSTANTIATION  For the GCC compiler
                                        on AIX, HPUX and VxWorks we have to
                                        explicitly instantiate static template
                                        members else we get multiple instances
                                        of the same static.
ACE_HAS_GETPAGESIZE                     Platform supports
                                        getpagesize() call (otherwise,
                                        ACE_PAGE_SIZE must be defined,
                                        except on Win32)
ACE_HAS_GETRUSAGE                       Platform supports the
                                        getrusage() system call.
ACE_HAS_GETRUSAGE_PROTOTYPE             Platform has a getrusage ()
                                        prototype in sys/resource.h
                                        that differs from the one in
                                        ace/OS.i.
ACE_HAS_GPERF                           The GPERF utility is compiled
                                        for this platform
ACE_HAS_GETIFADDRS                      This platform has ifaddrs.h and
                                        the getifaddrs() function.  This
                                        is used in preference to
                                        the SIOCGIFCONF ioctl call, since
                                        it is much simpler and supports
                                        IPv6 and non-IP interfaces better.
ACE_HAS_HANDLE_SET_OPTIMIZED_FOR_SELECT Optimize
                                        ACE_Handle_Set::count_bits for
                                        select() operations (common
                                        case)
ACE_HAS_LLSEEK                          Platform supports llseek.
ACE_HAS_HI_RES_TIMER                    Compiler/platform supports
                                        SunOS high resolution timers
ACE_HAS_IDTYPE_T                        Compiler/platform supports
                                        idtype_t.
ACE_HAS_INLINED_OSCALLS                 Inline all the static class OS
                                        methods to remove call
                                        overhead
ACE_HAS_INT_SWAB                        Platform's swab function has length
                                        argument of type int, not ssize_t.
ACE_HAS_IP_MULTICAST                    Platform supports IP multicast
ACE_HAS_IPV6                            Platform supports IPv6.
ACE_HAS_BROKEN_GETHOSTBYADDR_V4MAPPED   gethostbyaddr does not handle
                                        IPv6-mapped-IPv4 addresses
ACE_USES_IPV4_IPV6_MIGRATION            Enable IPv6 support in ACE on
                                        platforms that don't have IPv6
                                        turned on by default.
ACE_HAS_NONSTATIC_OBJECT_MANAGER        Causes the ACE_Object_Manager
                                        instance to be created in main
                                        (int, char *[]), instead of as
                                        a static (global) instance.
ACE_HAS_THR_KEYDELETE                   Platform supports
                                        thr_keydelete (e.g,. UNIXWARE)
ACE_HAS_THR_MINSTACK                    Platform calls thr_minstack()
                                        rather than thr_min_stack()
                                        (e.g., Tandem).
ACE_HAS_LIMITED_RUSAGE_T                The rusage_t structure has
                                        only two fields.
ACE_HAS_LINUX_NPTL                      Linux platform (with kernel >= 2.6.x)
                                        with GLibc including new NPTL (Native
                                        POSIX Thread Library).
                                        This triggers extended POSIX checks
                                        since the NPTL library is (almost) fully
                                        POSIX compliant.
ACE_HAS_LOG_MSG_NT_EVENT_LOG            Platform supports Windows NT event
                                        log so we can create an
                                        ACE_Log_Msg_Backend to log to it.
ACE_HAS_LONG_MAP_FAILED                 Platform defines MAP_FAILED as
                                        a long constant.
ACE_HAS_MALLOC_STATS                    Enabled malloc statistics
                                        collection.
ACE_HAS_MEMCHR                          Use native implementation of memchr.
ACE_HAS_MINIMAL_ACE_OS                  Disables some #includes in ace/OS.*.
ACE_HAS_MFC                             Platform supports Microsoft
                                        Foundation Classes
ACE_HAS_MSG                             Platform supports recvmsg and
                                        sendmsg
ACE_HAS_MT_SAFE_MKTIME                  Platform supports MT safe
                                        mktime() call (do any of
                                        them?)
ACE_HAS_MUTEX_TIMEOUTS                  Compiler supports timed mutex
                                        acquisitions
                                        (e.g. pthread_mutex_timedlock()).
ACE_HAS_NEW_NOTHROW                     Compiler offers new (nothrow).
ACE_HAS_NONCONST_CHDIR                  Platform uses non-const char *
                                        in call to chdir
ACE_HAS_NONCONST_CLOCK_SETTIME          Platform uses non-const
                                        struct timespec * in call to
                                        clock_settime
ACE_HAS_NONCONST_OPENDIR                Platform uses non-const char *
                                        in call to opendir
ACE_HAS_NONCONST_UNLINK                 Platform uses non-const char *
                                        in call to unlink
ACE_HAS_NONCONST_GETBY                  Platform uses non-const char *
                                        in calls to gethostbyaddr,
                                        gethostbyname, getservbyname
ACE_HAS_NONCONST_MSGSND                 Platform has a non-const
                                        parameter to msgsend() (e.g.,
                                        SCO).
ACE_HAS_NONCONST_READV                  Platform omits const qualifier from
                                        iovec parameter in readv() prototype.
ACE_HAS_NONCONST_SELECT_TIMEVAL         Platform's select() uses
                                        non-const timeval* (only found
                                        on Linux right now)
ACE_HAS_NONCONST_SENDMSG                Platform omits const qualifier
                                        from msghdr parameter in sendmsg()
                                        prototype.
ACE_HAS_NONCONST_SETRLIMIT              Platform omits const qualifier
                                        from rlimit parameter in setrlimit()
                                        prototype.
ACE_HAS_NONCONST_STAT                   Platform's stat function has non const
                                        name argument
ACE_HAS_NONCONST_SWAB                   Platform's swab function has non
                                        const src argument
ACE_HAS_NONCONST_WRITEV                 Platform omits const qualifier from
                                        iovec parameter in writev() prototype.
ACE_HAS_OLD_MALLOC                      Compiler/platform uses old
                                        malloc()/free() prototypes
                                        (ugh)
ACE_HAS_ONLY_SCHED_FIFO                 Platform, e.g., HP NonStop OSS,
                                        only supports SCHED_FIFO
                                        POSIX scheduling policy.
ACE_HAS_ONLY_SCHED_OTHER                Platform, e.g., Solaris 2.5,
                                        only supports SCHED_OTHER
                                        POSIX scheduling policy.
ACE_HAS_2_PARAM_ASCTIME_R_AND_CTIME_R   Uses ctime_r & asctime_r with
                                        only two parameters
                                        vs. three.
ACE_HAS_OSF_TIMOD_H                     Platform supports the OSF TLI
                                        timod STREAMS module
ACE_HAS_3_PARAM_WCSTOK                  Platform has 3-parameter version
                                        of wcstok(), which was added in
                                        1994 in the ISO C standard Normative
                                        Addendum 1.  Other standards like XPG4
                                        define a 2 parameter wcstok().
ACE_HAS_PENTIUM                         Platform is an Intel Pentium
                                        microprocessor.
ACE_HAS_POLL                            Platform contains <poll.h>
ACE_HAS_POSITION_INDEPENDENT_POINTERS   Platform supports
                                        "position-independent" features
                                        provided by ACE_Based_Pointer<>.
ACE_HAS_POSIX_MESSAGE_PASSING           Platform supports POSIX message queues.
                                        Corresponds to _POSIX_MESSAGE_PASSING
                                        constant in <unistd.h>.
ACE_HAS_POSIX_NONBLOCK                  Platform supports POSIX
                                        O_NONBLOCK semantics
ACE_HAS_POSIX_REALTIME_SIGNALS          Platform supports POSIX RT signals.
                                        Corresponds to _POSIX_REALTIME_SIGNALS
                                        constant in <unistd.h>.
ACE_HAS_POSIX_SEM                       Platform supports POSIX
                                        real-time semaphores (e.g.,
                                        VxWorks and Solaris).  Corresponds
                                        to _POSIX_SEMAPHORES constant
                                        in <unistd.h>
ACE_HAS_POSIX_SEM_TIMEOUT               Platform supports timed wait operation
                                        on POSIX realtime semaphores.
ACE_HAS_POSIX_TIME                      Platform supports the POSIX
                                        struct timespec type
ACE_HAS_PROC_FS                         Platform supports the /proc
                                        file system and defines tid_t
                                        in <sys/procfs.h>
ACE_HAS_POWERPC_TIMER                   Platform supports PowerPC
                                        time-base register.
ACE_HAS_PRUSAGE_T                       Platform supports the
                                        prusage_t struct
ACE_HAS_PTHREADS                        Platform supports POSIX
                                        Pthreads, of one form or
                                        another.  This macro says the
                                        platform has a pthreads
                                        variety - should also define
                                        one of the below to say which
                                        one.  Also may need some
                                        ACE_HAS_... thing for
                                        extensions.
ACE_HAS_PTHREADS_UNIX98_EXT             Platform has the UNIX98 extensions to
                                        Pthreads (rwlocks)
ACE_HAS_PTHREAD_ATTR_SETCREATESUSPEND_NP  Platform has
                                        pthread_attr_setcreatesuspend_np().
ACE_HAS_PTHREAD_CONDATTR_SETKIND_NP     Platform has pthread_condattr_setkind_np().
ACE_HAS_PTHREAD_MUTEXATTR_SETKIND_NP    Platform has
                                        pthread_mutexattr_setkind_np().
ACE_HAS_PTHREAD_GETCONCURRENCY          Platform has pthread_getconcurrency().
ACE_HAS_PTHREAD_SETCONCURRENCY          Platform has pthread_setconcurrency().
ACE_HAS_PTHREAD_PROCESS_ENUM            pthread.h declares an enum with
                                        PTHREAD_PROCESS_PRIVATE and
                                        PTHREAD_PROCESS_SHARED values.
ACE_HAS_PTHREAD_SETSTACK                Platform has pthread_attr_setstack().
ACE_HAS_PTHREAD_NP_H                    Platform has <pthread_np.h>  FreeBSD
                                        declares non-portable (*_np) pthread
                                        functions in this header.
ACE_HAS_PURIFY                          Purify'ing.  Set by wrapper_macros.GNU.
ACE_HAS_QUANTIFY                        Quantify'ing.  Set by wrapper_macros.GNU.
ACE_HAS_RECURSIVE_THR_EXIT_SEMANTICS    Platform will recurse
                                        infinitely on thread exits
                                        from TSS cleanup routines
                                        (e.g., AIX).
ACE_HAS_REENTRANT_FUNCTIONS             Platform supports reentrant
                                        functions (i.e., all the POSIX
                                        *_r functions).
ACE_HAS_XPG4_MULTIBYTE_CHAR             Platform has support for
                                        multi-byte character support
                                        compliant with the XPG4
                                        Worldwide Portability
                                        Interface wide-character
                                        classification.
ACE_HAS_REGEX                           Platform supports the POSIX
                                        regular expression library
ACE_HAS_DLSYM_SEGFAULT_ON_INVALID_HANDLE For OpenBSD: The dlsym call
                                        segfaults when passed an invalid
                                        handle.  Other platforms handle
                                        this more gracefully.
ACE_HAS_SELECT_H                        Platform has special header for select().
ACE_USE_SELECT_REACTOR_FOR_REACTOR_IMPL For Win32: Use Select_Reactor
                                        as default implementation of
                                        Reactor instead of
                                        WFMO_Reactor.
ACE_HAS_SEMUN                           Compiler/platform defines a
                                        union semun for SysV shared
                                        memory
ACE_HAS_SET_T_ERRNO                     Platform has a function to set
                                        t_errno (e.g., Tandem).
ACE_HAS_SIGACTION_CONSTP2               Platform's sigaction() function takes
                                        const sigaction* as 2nd parameter.
ACE_HAS_SIGINFO_T                       Platform supports SVR4
                                        extended signals
ACE_HAS_SIGSUSPEND                      Platform supports sigsuspend()
ACE_HAS_SIGISMEMBER_BUG                 Platform has bug with
                                        sigismember() (HP/UX 11).
ACE_HAS_SIGNAL_OBJECT_AND_WAIT          Platform supports the Win32
                                        SignalObjectAndWait() function
                                        (WinNT 4.0 and beyond).
ACE_HAS_SIGWAIT                         Platform/compiler has the
                                        sigwait(2) prototype
ACE_HAS_SIG_ATOMIC_T                    Compiler/platform defines the
                                        sig_atomic_t typedef
ACE_HAS_SIG_C_FUNC                      Compiler requires extern "C"
                                        functions for signals.
ACE_HAS_SIZET_SOCKET_LEN                OS/compiler uses size_t *
                                        rather than int * for socket
                                        lengths
ACE_HAS_SOCKADDR_IN_SIN_LEN             Platform has sin_len member in struct
                                        sockaddr_in.
ACE_HAS_SOCKADDR_IN6_SIN_LEN            Platform has sin6_len member in struct
                                        sockaddr_in6.
ACE_HAS_SOCKADDR_MSG_NAME               Platform requires (struct
                                        sockaddr *) for msg_name field
                                        of struct msghdr.
ACE_HAS_SOCKLEN_T                       Platform provides socklen_t
                                        type, such as Linux with
                                        glibc2.
ACE_HAS_SOCK_BUF_SIZE_MAX               Platform limits the maximum socket
                                        message size.
ACE_HAS_SPARCWORKS_401_SIGNALS          Compiler has brain-damaged
                                        SPARCwork SunOS 4.x signal
                                        prototype...
ACE_HAS_SSIZE_T                         Compiler supports the ssize_t
                                        typedef
ACE_HAS_STHREADS                        Platform supports Solaris
                                        threads
ACE_HAS_STANDARD_CPP_LIBRARY            Platform/compiler supports
                                        Standard C++ Library
ACE_HAS_STDCPP_STL_INCLUDES             Standard C++ headers can be
                                        included in the standard way.
                                        e.g. #include <vector>
ACE_HAS_STRBUF_T                        Compiler/platform supports
                                        struct strbuf
ACE_HAS_STRDUP_EMULATION                Use ACE's strdup() emulation (even
                                        if platform has a native strdup()).
                                        This is useful if you need control
                                        over what memory allocator is used.
ACE_HAS_WCSDUP_EMULATION                Use ACE's wcsdup() emulation (even
                                        if platform has a native wcsdup()).
                                        This is useful if you need control
                                        over what memory allocator is used.
ACE_HAS_STRNLEN                         Platform supports strnlen(3).
ACE_HAS_STREAMS                         Platform supports STREAMS
ACE_HAS_STREAM_PIPES                    Platform supports STREAM pipes
ACE_HAS_STRICT                          Use the STRICT compilation mode on Win32.
ACE_HAS_STRING_CLASS                    Platform/Compiler supports a
                                        String class (e.g., GNU or
                                        Win32).
ACE_HAS_STRUCT_NETDB_DATA               Compiler/platform has strange
                                        hostent API for socket *_r()
                                        calls
ACE_HAS_SUNOS4_SIGNAL_T                 Compiler has horrible SunOS
                                        4.x signal handlers...
ACE_HAS_SVR4_DYNAMIC_LINKING            Compiler/platform supports
                                        SVR4 dynamic linking semantics
ACE_HAS_SVR4_GETTIMEOFDAY               Compiler/platform supports
                                        SVR4 gettimeofday() prototype
ACE_HAS_SVR4_SIGNAL_T                   Compiler/platform supports
                                        SVR4 signal typedef
ACE_HAS_SVR4_TLI                        Compiler/platform supports
                                        SVR4 TLI; that is, TLI with extensions
                                        like t_getname(). This is sometimes
                                        used as a pseudonym for TLI on SunOS4.
                                        This is a modifier to ACE_HAS_TLI and
                                        isn't used if ACE_HAS_XTI is set.
ACE_HAS_SYSCALL_GETRUSAGE               HP/UX has an undefined syscall
                                        for GETRUSAGE...
ACE_HAS_SYSENT_H                        Platform provides <sysent.h>
                                        header
ACE_HAS_SYSV_SYSINFO                    Platform supports system
                                        configuration information
ACE_HAS_SYSV_IPC                        Platform supports System V IPC
                                        (most versions of UNIX, but
                                        not Win32)
ACE_HAS_SYS_FILIO_H                     Platform provides
                                        <sys/filio.h> header
ACE_HAS_SYS_LOADAVG_H                   Compiler/platform contains the
                                        <sys/loadavg.h> file.
ACE_HAS_SYS_PSTAT_H                     Compiler/platform contains the
                                        <sys/pstat.h> file.
ACE_HAS_SYS_SOCKIO_H                    Compiler/platform provides the
                                        sockio.h file
ACE_HAS_SYS_SYSCALL_H                   Compiler/platform contains the
                                        <sys/syscall.h> file.
ACE_HAS_TEMPLATE_INSTANTIATION_PRAGMA   Compiler's template
                                        instantiation mechanism
                                        supports the use of "#pragma
                                        instantiate".  Edison Design
                                        Group compilers, e.g., SGI C++
                                        and Green Hills 1.8.8 and
                                        later, support this.
ACE_HAS_TEMPLATE_TYPEDEFS               Compiler implements templates
                                        that support typedefs inside
                                        of classes used as formal
                                        arguments to a template
                                        class.
ACE_HAS_TERMIO                          Platform has terminal ioctl
                                        flags like TCGETS and TCSETS and
                                        termio struct.
ACE_HAS_TERMIOS                         Platform has POSIX terminal
                                        interface and termios struct.
ACE_HAS_LAZY_MAP_MANAGER                ACE supports lazy Map Managers
                                        that allow deletion of entries
                                        during active iteration.
ACE_HAS_THREADS                         Platform supports threads
ACE_HAS_THREAD_SAFE_ACCEPT              Platform allows multiple
                                        threads to call accept() on
                                        the same port (e.g., WinNT).
ACE_HAS_THREAD_SELF                     Platform has thread_self()
                                        rather than pthread_self()
                                        (e.g., DCETHREADS and AIX)
ACE_HAS_THREAD_SPECIFIC_STORAGE         Compiler/platform has
                                        thread-specific storage
ACE_HAS_THR_C_DEST                      The pthread_keycreate()
                                        routine *must* take extern C
                                        functions.
ACE_HAS_THR_C_FUNC                      The pthread_create() routine
                                        *must* take extern C
                                        functions.
ACE_HAS_TIMEZONE                        Platform/compiler supports
                                        global "timezone" variable.
ACE_HAS_TIMEZONE_GETTIMEOFDAY           Platform/compiler supports
                                        timezone * as second parameter
                                        to gettimeofday()
ACE_HAS_TIMOD_H                         Platform supports TLI timod
                                        STREAMS module
ACE_HAS_TIUSER_H                        Platform provides TLI tiuser.h
                                        header file.
ACE_HAS_TLI                             Platform supports TLI.  Also
                                        see ACE_TLI_TCP_DEVICE. If the
                                        platform supports XTI, set ACE_HAS_XTI
                                        instead of this.
ACE_HAS_TLI_PROTOTYPES                  Platform provides TLI function
                                        prototypes
ACE_HAS_TR24731_2005_CRT                The platform provides an implementation
                                        of C99 draft TR24731 (October 2005),
                                        C run-time with more secure parameters.
ACE_HAS_TSS_EMULATION                   ACE provides TSS emulation.
                                        See also
                                        ACE_DEFAULT_THREAD_KEYS.
ACE_HAS_UALARM                          Platform supports ualarm()
ACE_HAS_UCONTEXT_T                      Platform supports ucontext_t
                                        (which is used in the extended
                                        signal API).
ACE_HAS_UNION_WAIT                      The wait() system call takes a
                                        (union wait *) rather than int
                                        *
ACE_HAS_VALGRIND                        Running with valgrind
ACE_HAS_VERBOSE_NOTSUP                  Prints out console message in
                                        ACE_NOTSUP.  Useful for
                                        tracking down origin of
                                        ACE_NOTSUP.
ACE_HAS_VERSIONED_NAMESPACE             Wrap all library code within a
                                        "versioned namespace" to
                                        prevent symbol conflicts with
                                        other versions of ACE shared
                                        libraries in third party
                                        libraries.  Default namespace
                                        name may be overridden by
                                        defining preprocessor symbol
                                        ACE_VERSIONED_NAMESPACE_NAME
                                        to desired name.
ACE_LACKS_INTMAX_T                      Platform lacks the intmax_t type
ACE_LACKS_UINTMAX_T                     Platform lacks the uintmax_t type.
ACE_LACKS_INTPTR_T                      Platform lacks the intptr_t type
ACE_LACKS_UINTPTR_T                     Platform lacks the uintptr_t type.

ACE_HAS_INT8_T                          Platform provides the int8_t type.
ACE_HAS_INT16_T                         Platform provides the int16_t type.
ACE_HAS_INT32_T                         Platform provides the int32_t type.
ACE_HAS_INT64_T                         Platform provides the int64_t type.
ACE_HAS_UINT8_T                         Platform provides the uint8_t type.
ACE_HAS_UINT16_T                        Platform provides the uint16_t type.
ACE_HAS_UINT32_T                        Platform provides the uint32_t type.
ACE_HAS_UINT64_T                        Platform provides the uint64_t type.

ACE_INT8_TYPE                           Specific type to use for ACE_INT8.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_INT16_TYPE                          Specific type to use for ACE_INT16.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_INT32_TYPE                          Specific type to use for ACE_INT32.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_INT64_TYPE                          Specific type to use for ACE_INT64.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_UINT8_TYPE                          Specific type to use for ACE_UINT8.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_UINT16_TYPE                         Specific type to use for ACE_UINT16.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_UINT32_TYPE                         Specific type to use for ACE_UINT32.
                                        If not defined, ACE will attempt to
                                        determine the correct type.
ACE_UINT64_TYPE                         Specific type to use for ACE_UINT64.
                                        If not defined, ACE will attempt to
                                        determine the correct type.

ACE_INT8_FORMAT_SPECIFIER               String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_INT8 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_INT16_FORMAT_SPECIFIER              String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_INT16 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_INT32_FORMAT_SPECIFIER              String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_INT32 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_INT64_FORMAT_SPECIFIER              String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_INT64 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_UINT8_FORMAT_SPECIFIER              String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_UINT8 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_UINT16_FORMAT_SPECIFIER             String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_UINT16 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_UINT32_FORMAT_SPECIFIER             String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_UINT32 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.
ACE_UINT64_FORMAT_SPECIFIER             String literal containing *printf
                                        format specifier (including the '%')
                                        to be used for ACE_UINT64 values.  If
                                        not defined, ACE will attempt to
                                        determine the correct setting.

ACE_HAS_VOIDPTR_GETTIMEOFDAY            Platform/compiler supports
                                        void * as second parameter
                                        to gettimeofday
ACE_HAS_VOIDPTR_MMAP                    Platform requires void * for
                                        mmap().
ACE_HAS_VOIDPTR_SOCKOPT                 OS/compiler uses void * arg 4
                                        setsockopt() rather than const
                                        char *
ACE_HAS_WCSNLEN                         Platform supports wcsnlen(3).
ACE_HAS_WIN32_OVERLAPPED_IO             Platform has Windows overlapped I/O;
                                        requires I/O completion ports.
ACE_HAS_WIN32_TRYLOCK                   The Win32 platform support
                                        TryEnterCriticalSection()
                                        (WinNT 4.0 and beyond)
ACE_HAS_WINSOCK2                        The Win32 platform supports
                                        WinSock 2.0
ACE_HAS_XLI                             Platform has the XLI version
                                        of TLI
ACE_HAS_XTI                             Platform has XTI
                                        (X/Open-standardized superset
                                        of TLI).  Implies ACE_HAS_TLI
                                        but uses a different header
                                        file.
ACE_INITIALIZE_MEMORY_BEFORE_USE        Memory is explicitly initialized before
                                        use. Useful when using a profiler like
                                        purify or valgrind
ACE_HRTIME_T_IS_BASIC_TYPE              ACE_hrtime_t is a basic type that
                                        doesn't require ACE_U64_TO_U32
                                        conversion
ACE_LACKS_ACCESS                        Platform lacks access() (e.g.,
                                        VxWorks and Chorus)
ACE_LACKS_ACE_IOSTREAM                  Platform can not build
                                        ace/IOStream{,_T}.cpp.  This
                                        does not necessarily mean that
                                        the platform does not support
                                        iostreams.
ACE_LACKS_AUTO_MMAP_REPLACEMENT         No system support for replacing any
                                        previous mappings.
ACE_LACKS_BSEARCH                       Compiler/platform lacks the
                                        standard C library bsearch()
                                        function
ACE_LACKS_CLOSEDIR                      Platform lacks closedir and the closedir
                                        emulation must be used
ACE_LACKS_OPENDIR                       Platform lacks opendir and the opendir
                                        emulation must be used
ACE_LACKS_READDIR                       Platform lacks readdir and the readdir
                                        emulation must be used
ACE_LACKS_COND_TIMEDWAIT_RESET          pthread_cond_timedwait does
                                        *not* reset the time argument
                                        when the lock is acquired.
ACE_LACKS_CONST_STRBUF_PTR              Platform uses struct strbuf *
                                        rather than const struct
                                        strbuf * (e.g., HP/UX 10.x)
ACE_LACKS_CONST_TIMESPEC_PTR            Platform forgot const in
                                        cond_timewait (e.g., HP/UX).
ACE_LACKS_COND_T                        Platform lacks condition
                                        variables (e.g., Win32 and
                                        VxWorks)
ACE_LACKS_CONDATTR_PSHARED              Platform has no implementation
                                        of
                                        pthread_condattr_setpshared(),
                                        even though it supports
                                        pthreads!
ACE_LACKS_DIFFTIME                      Platform lacks difftime() implementation
ACE_LACKS_DUP2                          Platform lacks dup2().
ACE_LACKS_FCNTL                         Platform lacks POSIX-style fcntl ().
ACE_LACKS_FSYNC                         Platform lacks fsync().
ACE_LACKS_INLINE_FUNCTIONS              Platform can't handle "inline"
                                        keyword correctly.
ACE_LACKS_EXEC                          Platform lacks the exec()
                                        family of system calls (e.g.,
                                        Win32, VxWorks, Chorus)
ACE_LACKS_FILELOCKS                     Platform lacks file locking
                                        mechanism
ACE_LACKS_FLOATING_POINT                Platform does not support
                                        floating point operations
                                        (e.g., certain Chorus hardware
                                        platforms)
ACE_LACKS_FORK                          Platform lacks the fork()
                                        system call (e.g., Win32,
                                        VxWorks, Chorus)
ACE_LACKS_GETOPT_PROTOTYPE              Platform lacks the getopt()
                                        prototype (e.g., LynxOS)
ACE_LACKS_GETPGID                       Platform lacks getpgid() call
                                        (e.g., Win32, Chorus, and
                                        FreeBSD).
ACE_LACKS_GETSERVBYNAME                 Platforms lacks
                                        getservbyname() (e.g., VxWorks
                                        and Chorus).
ACE_LACKS_GETIPNODEBYADDR               Platform lacks getipnodebyaddr().
ACE_LACKS_GETIPNODEBYNAME               Platform lacks getipnodebyname().
ACE_LACKS_INET_ATON                     Platform lacks the inet_aton()
                                        function.
ACE_LACKS_INET_ATON_PROTOTYPE           Platform/compiler lacks the
                                        inet_aton() prototype (e.g.,
                                        LynxOS)
ACE_LACKS_IOSTREAM_FX                   iostream header does not
                                        declare ipfx (), opfx (),
                                        etc.
ACE_LACKS_KEY_T                         Platform lacks key_t (e.g.,
                                        Chorus, VxWorks, Win32)
ACE_LACKS_LINEBUFFERED_STREAMBUF        Platform lacks streambuf
                                        "linebuffered ()".
ACE_LACKS_LONGLONG_T                    Compiler/platform does not
                                        support the signed or unsigned long
                                        long datatype.
ACE_LACKS_LSTAT                         Platform lacks the lstat() function.
ACE_LACKS_MADVISE                       Platform lacks madvise()
                                        (e.g., Linux)
ACE_LACKS_MALLOC_H                      Platform lacks malloc.h
ACE_LACKS_MEMORY_H                      Platform lacks memory.h (e.g.,
                                        VxWorks and Chorus)
ACE_LACKS_MKFIFO                        Platform lacks mkfifo() e.g.,
                                        VxWorks, Chorus, pSoS, and WinNT.
ACE_LACKS_MKTEMP                        Platform lacks the mktemp() function.
ACE_LACKS_MKTEMP_PROTOTYPE              Platform/compiler lacks the
                                        mktemp() prototype (e.g.,
                                        LynxOS)
ACE_LACKS_MKSTEMP      Platform lacks the mkstemp() function.
ACE_LACKS_MKSTEMP_PROTOTYPE             Platform/compiler lacks the
                                        mkstemp() prototype (e.g.,
                                        LynxOS)
ACE_LACKS_MMAP                          The platform doesn't have
                                        mmap(2) (e.g., SCO UNIX).
ACE_LACKS_MODE_MASKS                    Platform/compiler doesn't have
                                        open() mode masks.
ACE_LACKS_MPROTECT                      The platform doesn't have
                                        mprotect(2) (e.g., EPLX real
                                        time OS from CDC (based on
                                        LYNX))
ACE_LACKS_MSG_ACCRIGHTS                 Platform defines ACE_HAS_MSG,
                                        but lacks msg_accrights{,len}.
ACE_LACKS_MSG_WFMO                      Platform lacks
                                        MsgWaitForMultipleObjects
                                        (only needs to be defined when
                                        ACE_WIN32 is also defined).
ACE_LACKS_MSYNC                         Platform lacks msync() (e.g.,
                                        Linux)
ACE_LACKS_MUTEXATTR_PSHARED             Platform lacks
                                        pthread_mutexattr_setpshared().
ACE_LACKS_NAMED_POSIX_SEM               Platform lacks named POSIX
                                        semaphores (e.g., Chorus)
ACE_LACKS_NETDB_REENTRANT_FUNCTIONS     Platform does not support
                                        reentrant netdb functions
                                        (getprotobyname_r,
                                        getprotobynumber_r,
                                        gethostbyaddr_r,
                                        gethostbyname_r,
                                        getservbyname_r).
ACE_LACKS_NEW_H                         OS doesn't have, or we don't want to
                                        use, new.h.
ACE_LACKS_NULL_PTHREAD_STATUS           OS requires non-null status pointer
                                        for ::pthread_join ().
ACE_LACKS_NUMERIC_LIMITS    Platform lacks std::numeric_limits<>.
ACE_LACKS_PERFECT_MULTICAST_FILTERING   Platform lacks IGMPv3 "perfect" filtering
                                        of multicast dgrams at the socket level.
                                        If == 1, ACE_SOCK_Dgram_Mcast will bind
                                        the first joined multicast group to the
                                        socket, and all future joins on that
                                        socket will fail with an error.
ACE_LACKS_PRAGMA_ONCE                   Compiler complains about #pragma once
ACE_LACKS_PRI_T                         Platform lacks pri_t (e.g.,
                                        Tandem NonStop UNIX).
ACE_LACKS_PTHREAD_CANCEL                Platform lacks
                                        pthread_cancel().
ACE_LACKS_PTHREAD_SCOPE_PROCESS         Platform lacks support for
                                        PTHREAD_SCOPE_PROCESS
ACE_LACKS_PTHREAD_SIGMASK               Platform lacks pthread_sigmask ().
ACE_LACKS_PTHREAD_THR_SIGSETMASK        Platform lacks
                                        pthread_thr_sigsetmask (e.g.,
                                        MVS, HP/UX, and OSF/1 3.2)
ACE_LACKS_PUTENV_PROTOTYPE              Platform/compiler lacks the
                                        putenv() prototype (e.g.,
                                        LynxOS)
ACE_LACKS_PWD_REENTRANT_FUNCTIONS       Platform lacks getpwnam_r()
                                        methods (e.g., SGI 6.2).
ACE_LACKS_QSORT                         Compiler/platform lacks the
                                        standard C library qsort()
                                        function
ACE_LACKS_READLINK                      Platform lacks the readlink() function.
ACE_LACKS_READV                         Platform doesn't define readv,
                                        so use our own
ACE_LACKS_RENAME                        Platform lacks rename().
ACE_LACKS_RLIMIT                        Platform/compiler lacks
                                        {get,set}rlimit() function
                                        (e.g., VxWorks, Chorus, and
                                        SCO UNIX)
ACE_LACKS_RLIMIT_PROTOTYPE              Platform/compiler lacks
                                        {get,set}rlimit() prototypes
                                        (e.g., Tandem)
ACE_LACKS_READDIR_R                     Platform uses ACE_HAS_DIRENT
                                        but does not have readdir_r
                                        ().
ACE_LACKS_REALPATH                      Platform/compiler lacks
                                        realpath () function (e.g.,
                                        LynxOS)
ACE_LACKS_RECVMSG                       Platform lacks recvmsg()
                                        (e.g., Linux)
ACE_LACKS_RWLOCK_T                      Platform lacks readers/writer
                                        locks.
ACE_LACKS_RWLOCKATTR_PSHARED            Platform lacks
                                        pthread_rwlockattr_setpshared().
ACE_LACKS_SBRK                          Platform lacks a working
                                        sbrk() (e.g., Win32 and
                                        VxWorks)
ACE_LACKS_SCANDIR_PROTOTYPE             Platform/compiler lacks
                                        scandir() prototype
                                        (e.g., LynxOS)
ACE_LACKS_SEEKDIR                       Platform uses ACE_HAS_DIRENT
                                        but does not have seekdir ().
ACE_LACKS_SEMBUF_T                      Platform lacks struct sembuf
                                        (e.g., Win32 and VxWorks)
ACE_LACKS_SETDETACH                     Platform lacks
                                        pthread_attr_setdetachstate()
                                        (e.g., HP/UX 10.x)
ACE_LACKS_SETSCHED                      Platform lacks
                                        pthread_attr_setsched()
                                        (e.g. MVS)
ACE_LACKS_SIGACTION                     Platform lacks struct
                                        sigaction (e.g., Win32 and
                                        Chorus)
ACE_LACKS_SIGNED_CHAR                   Platform lacks "signed char"
                                        type (broken!)
ACE_LACKS_SIGSET                        Platform lacks signal sets
                                        (e.g., Chorus and Win32)
ACE_LACKS_STRPTIME                      Platform/compiler lacks the strptime()
                                        function.
ACE_LACKS_WCSCHR                        Platform/compiler lacks wcschr()
ACE_LACKS_STRDUP                        Platform/compiler lacks strdup()
ACE_LACKS_WCSDUP                        Platform/compiler lacks wcsdup()
ACE_LACKS_STRRCHR                       Platform/compiler lacks strrchr()
ACE_LACKS_WCSRCHR                       Platform/compiler lacks wcsrchr()
ACE_LACKS_SWAB                          Platform/compiler lacks
                                        swab () function.
ACE_LACKS_SYS_MSG_H                     Platform lacks sys/msg.h
                                        (e.g., Chorus and VxWorks)
ACE_LACKS_SYS_PARAM_H                   Platform lacks <sys/param.h>
                                        (e.g., MVS)
ACE_LACKS_SENDMSG                       Platform lacks sendmsg()
                                        (e.g., Linux)
ACE_LACKS_SI_ADDR                       Platform lacks the si_addr
                                        field of siginfo_t (e.g.,
                                        VxWorks and HP/UX 10.x)
ACE_LACKS_SYMLINKS                      Platform lacks symbolic links
ACE_LACKS_SYSV_SHMEM                    Platform lacks System V shared
                                        memory (e.g., Win32 and
                                        VxWorks)
ACE_LACKS_SIGINFO_H                     Platform lacks the siginfo.h
                                        include file (e.g., MVS)
ACE_LACKS_SOCKET_BUFSIZ                 Platform doesn't support
                                        SO_SNDBUF/SO_RCVBUF
ACE_LACKS_SOCKETPAIR                    Platform lacks the
                                        socketpair() call (e.g., SCO
                                        UNIX)
ACE_LACKS_STATIC_DATA_MEMBER_TEMPLATES  Compiler doesn't support
                                        static data member templates
ACE_LACKS_STRCASECMP                    Compiler/platform lacks
                                        strcasecmp() (e.g., DG/UX,
                                        UNIXWARE, VXWORKS)
ACE_LACKS_STRCASECMP_PROTOTYPE          Platform/compiler lacks the
                                        strcasecmp() prototype (e.g.,
                                        LynxOS)
ACE_LACKS_STRNCASECMP_PROTOTYPE         Platform/compiler lacks the
                                        strncasecmp() prototype (e.g.,
                                        LynxOS)
ACE_LACKS_STRRECVFD                     Platform doesn't define struct
                                        strrecvfd.
ACE_LACKS_SYSCALL                       Platform doesn't have
                                        syscall() prototype
ACE_LACKS_T_ERRNO                       Header files lack t_errno for
                                        TLI
ACE_LACKS_TCP_NODELAY                   OS does not support TCP_NODELAY.
ACE_LACKS_TELLDIR                       Platform uses ACE_HAS_DIRENT
                                        but does not have telldir ().
ACE_LACKS_THREAD_STACK_SIZE             Platform lacks
                                        pthread_attr_setstacksize()
                                        (e.g., Linux pthreads)
ACE_LACKS_THR_CONCURRENCY_FUNCS    (ONLY APPLIES TO SOLARIS)
                                        Platform does not support
                                        thr_getconcurrency/thr_setconcurrency
                                        functions, or their implementation
                                        is effectively a "no-op".  This
                                        notably applies for Solaris >= 5.9.
                                        Note that if you build on Solaris 8
                                        and run on Solaris 9+, you can
                                        encounter thread creation errors
                                        unless you rebuild on the target
                                        platform.
ACE_LACKS_TIMEDWAIT_PROTOTYPES          MIT pthreads platform lacks
                                        the timedwait prototypes
ACE_LACKS_TIMESPEC_T                    Platform does not define
                                        timepec_t as a typedef for
                                        struct timespec.
ACE_LACKS_TRUNCATE                      Platform doesn't have truncate()
                                        (e.g., vxworks)
ACE_LACKS_U_LONGLONG_T                  Platform does not have
                                        u_longlong_t typedef, and
                                        "sun" is defined.
ACE_LACKS_UALARM_PROTOTYPE              Platform/compiler lacks the
                                        ualarm() prototype (e.g.,
                                        Solaris)
ACE_LACKS_CHAR_RIGHT_SHIFTS             Compiler does not have any istream
                                        operator>> for chars, u_chars, or
                                        signed chars.
ACE_LACKS_CHAR_STAR_RIGHT_SHIFTS        Compiler does not have
                                        operator>> (istream &, u_char *) or
                                        operator>> (istream &, signed char *)
ACE_LACKS_UCONTEXT_H                    Platform lacks the ucontext.h
                                        file
ACE_LACKS_UMASK                         Platform lacks umask function
ACE_LACKS_UNBUFFERED_STREAMBUF          Platform lacks streambuf
                                        "unbuffered ()".
ACE_LACKS_UNISTD_H                      Platform lacks the unistd.h
                                        file (e.g., VxWorks and Win32)
ACE_LACKS_UNIX_DOMAIN_SOCKETS           ACE platform has no UNIX
                                        domain sockets
ACE_LACKS_UNIX_SIGNALS                  Platform lacks full signal
                                        support (e.g., Win32 and
                                        Chorus).
ACE_LACKS_UNSIGNEDLONGLONG_T            Compiler/platform does not
                                        support the unsigned long
                                        long datatype.
ACE_LACKS_UTSNAME_T                     Platform lacks struct utsname
                                        (e.g., Win32 and VxWorks)
ACE_LACKS_UNAME                         Platform lacks uname calls
ACE_LACKS_WAIT                          The platform lacks wait
ACE_LACKS_WIN32_GETPROCESSTIMES         The Windows platform doesn't have
                                        GetProcessTimes().
ACE_LACKS_WIN32_MOVEFILEEX              The Windows platform doesn't have
                                        MoveFileEx().
ACE_LACKS_WIN32_SECURITY_DESCRIPTORS    The Windows platform doesn't have
                                        security descriptor support.
ACE_LACKS_WRITEV                        Platform doesn't define
                                        writev, so use our own

ACE_LEGACY_MODE                         When defined, it will enable
                                        some code that is used to
                                        provide some support for
                                        backwards compatibility.

ACE_NEEDS_DEV_IO_CONVERSION             Necessary with some compilers
                                        to pass ACE_TTY_IO as
                                        parameter to DEV_Connector.
ACE_NEEDS_FUNC_DEFINITIONS              Compiler requires a definition
                                        for a "hidden" function, e.g.,
                                        a private, unimplemented copy
                                        constructor or assignment
                                        operator.  The SGI C++
                                        compiler needs this, in
                                        template classes, with
                                        ACE_HAS_TEMPLATE_INSTANTIATION_PRAGMA.
ACE_NEEDS_HUGE_THREAD_STACKSIZE         Required by platforms with
                                        small default stacks.
ACE_NEEDS_LWP_PRIO_SET                  OS has LWPs, and when the
                                        priority of a bound thread is
                                        set, then the LWP priority
                                        must be set also.
ACE_NEEDS_SCHED_H                       Platform needs to #include
                                        <sched.h>
                                        to get thread scheduling
                                        defs.

ACE_NO_WIN32_LEAN_AND_MEAN              If this is set, then ACE does not
                                        define WIN32_LEAN_AND_MEAN before
                                        including <windows.h>. Needed for
                                        code that uses non-lean Win32
                                        facilities such as COM.

ACE_ONLY_LATEST_AND_GREATEST            A macro that indicates that
                                        the "latest and greatest"
                                        features of ACE/TAO should be
                                        turned on.  It has been
                                        replaced by ACE_LEGACY_MODE,
                                        which has the opposite meaning
                                        but serves the same purpose.

ACE_SHM_OPEN_REQUIRES_ONE_SLASH         The path specified on shm_open() must
                                        have a leading, single slash and not
                                        have any other slashes.

ACE_WSTRING_HAS_USHORT_SUPPORT          If a platform has wchar_t as a
                                        separate type, then
                                        ACE_WString doesn't have a
                                        constructor that understands
                                        an ACE_USHORT16 string.  So
                                        this macro enables
                                        one. (mostly used my ACE Name
                                        Space).

ACE_HAS_BROKEN_PREALLOCATED_OBJECTS_AFTER_FORK
                                        Under QNX/RTP the objects preallocated
                                        in ACE_OS_Object_Manager cannot be
                                        destroyed after a fork() call.
                                        Since these objects are only destroyed
                                        at application shutdown we take the
                                        simpler approach of not destroying
                                        them at all.
                                        Both QNX/RTP and LynxOS suffer from
                                        this problem.

ACE_LACKS_MEMBER_TEMPLATES              Compiler does not support
                                        member template feature.

ACE_LACKS_DEPRECATED_MACROS             When this define is set, macros which
                                        are deprecated are not defined. Usefull
                                        to check whether deprecated macros are
                                        not used anymore.

ACE_DONT_INIT_WINSOCK                   This definition defines whether or not
                                        to explicitly initialize Winsock during
                                        ACE::init() (i.e., whether WSAStartup()
                                        is called). Some Win32 platforms have
                                        dependent characteristics between
                                        ACE initialization and
                                        network initialization.

----------------------------------------

The following macros determine the svc.conf file format ACE uses.

Macro                                   Description
-----                                   -----------
ACE_HAS_CLASSIC_SVC_CONF                This macro forces ACE to use
                                        the classic svc.conf format.

ACE_HAS_XML_SVC_CONF                    This macro forces ACE to use the XML
                                        svc.conf format.

ACE_USES_CLASSIC_SVC_CONF               This macro should be defined
                                        as 0 or 1, depending on the
                                        preferred svc.conf file
                                        format.  Defining this macro
                                        to 0 means ACE will use XML
                                        svc.conf file format.
                                        Defining it to 1 will force
                                        ACE to use the classic
                                        svc.conf format.
                                        ** This macro takes precedence
                                        ** over previous two macros.

----------------------------------------
The following is a partial list of where some of these macros are used
in the code.  This list was originally compiled by Jam Hamidi
(jh1@core01.osi.com).  It is now hopelessly out of date.  Hopefully,
someone will come along and update it....

ACE_HAS_ALLOCA:
---------------

  Used in:
     libsrc/IPC_SAP/SOCK_SAP/SOCK_Connect.C
        for allocation of iovp
A
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE_Msg.C
        for alocation of iovp

  In solaris:
     alloca() allocates size bytes of space in the stack frame of
     the  caller,  and  returns a pointer to the allocated block.
     This temporary space is automatically freed when the  caller
     returns.  Note: if the allocated block is beyond the current
     stack limit, the resulting behavior is undefined.

  In HPUX:
     no equivalent.

  Notes:
     in HPUX it has to do new and delete. Affects performance.


ACE_HAS_AUTOMATIC_INIT_FINI:
----------------------------

  Used in:
     libsrc/Service_Configurator/Service_Repository.i
     libsrc/Service_Configurator/Parse_Node.i
     include/Parse_Node.i
     include/Service_Repository.i

  In solaris:
     _init() initializes a loadable module. It is  called  before
     any other routine in a loadable module.
     _info()  returns  information  about  a   loadable   module.
     _fini() should return the return value from mod_remove(9F).
     This flag if set, doesn't do anything.  If not set, forces
     _init() and _fini() to be executed as is:
       dlsym ((char *) handle, "_fini").

  In HPUX:
     don't set.
     Maybe have to look into shl_load( ), shl_definesym( ),
     shl_findsym( ), shl_gethandle( ), shl_getsymbols( ),
     shl_unload( ), shl_get( )(3X) - explicit load of shared libraries
     Means Service Configurator won't be available.
     TBA.


ACE_HAS_CPLUSPLUS_HEADERS:
--------------------------

  Used In:
     ace/OS.h

  HPUX:
     set it.

  Notes:
     If this is not defined, libc.h and osfcn.h get included.
     Only needed for older compiler/OS platforms that don't
     provide standard C++ header files in /usr/include.

ACE_HAS_HI_RES_TIMER:
---------------------

  Used In:
     libsrc/Misc/High_Res_Timer.h
     libsrc/Misc/High_Res_Timer.C
     include/High_Res_Timer.h

  In Solaris,
     C++ wrapper around gethrtime(), which returns a long long.
         gethrtime() returns the current high-resolution  real  time.
     Time  is  expressed as nanoseconds since some arbitrary time
     in the past; it is not correlated in any way to the time  of
     day,  and  thus  is not subject to resetting, drifting, etc.

  In HPUX
     look into: getclock(), reltimer(), getitimer()
     maybe even vtimes structure vm_utime, vm_stime ?

  Notes:
     TBA


ACE_LACKS_T_ERRNO:
-------------------

  Used In:
     ace/OS.h

  HPUX:
     set it.

  Notes:
     if set, adds:
     extern int t_errno;


ACE_HAS_POSIX_NONBLOCK:
-----------------------

  Used in:
     ace/OS.h

  HPUX:
     set it.

  Notes:
     if defined, sets ACE_NONBLOCK and O_NONBLOCK
     O_NONBLOCK is used in libsrc/Misc/misc.C to do a
       fcntl (fd, F_SETFL, opt)
     ACE_NONBLOCK is used in libsrc/IPC_SAP/FIFO_SAP/FIFO_Recv.C in the
       disable member function and options passed to the open function
       in libsrc/IPC_SAP/FIFO_SAP/FIFO.C


ACE_HAS_PROC_FS:
----------------

  Used in:
     ace/OS.h
     libsrc/Misc/Profile_Timer.i

  Notes:
     if set, includes <sys/procfs.h>
     the PIOCUSAGE define is used in Profile_Timer.

  Solaris:
     procfs.h defines things for the prpsinfo structure (basically to
     do a "ps" from inside a program).

  HPUX:
     don't set: obviously a different mechanism.
     Look into /usr/include/sys/proc.h.  The structure is proc.  The
     pointer to the kernel's proc table may be obtained by
     extern  struct  proc *proc, *procNPROC;
     extern  int nproc;


ACE_HAS_PRUSAGE_T:
------------------

  Used in:
     libsrc/Misc/Profile_Timer.h
     libsrc/Misc/Profile_Timer.C

  Notes:
     If defined, declares the Profile_Timer class that does start(),
     stop() and basically gets real_time, user_time, system_time for
     an interval.
     This stuff is highly non-portable.

  HPUX:
     don't set


ACE_HAS_SEMUN:
--------------

  Used in:
     libsrc/Semaphores/Semaphore_Simple.h

  Notes:
     if not defined, defines semun as:
     union semun {
           int          val;    /* value for SETVAL */
           struct semid_ds      *buf;   /* buffer for IPC_STAT & IPC_SET */
           ushort               *array; /* array for GETALL & SETALL */
     };

  HPUX:
     don't set.
     in /usr/include/sem.h:
     /* The fourth argument to semctl() varies depending on the value of
       its first argument.  If desired, "union semun" can be declared
       by the user, but this is not necessary since the individual
       member can just be passed as the argument. */


ACE_HAS_SIG_ATOMIC_T:
---------------------

  Used in:
     ace/OS.h

  Notes:
     if not defined, does a:
     typedef int sig_atomic_t;
     This is used in the Reactor and service configurator.

  HPUX:
     set it.
     in /usr/include/sys/signal.h:
     typedef unsigned int sig_atomic_t;


ACE_HAS_SSIZE_T:
----------------

  Used in:
     ace/OS.h

  Notes:
     if not defined, does a
     typedef int ssize_t;
     used mostly in IPC_SAP.  (don't confuse with size_t).

  HPUX:
     set it.
     in /usr/include/sys/types.h


ACE_HAS_STRBUF_T:
-----------------

  Used in:
     include/Str_Buf.h

  Notes:
     if not defined, declares the strbuf structure as:
     struct strbuf
     {
       int      maxlen;                 /* no. of bytes in buffer */
       int      len;                    /* no. of bytes returned */
       void     *buf;                   /* pointer to data */
     };

  Solaris:
     defined in /usr/include/sys/stropts.h
     Sys V.4 Streams.
     uses strbuf as parameter to putmsg, putpmsg:
     int putmsg(int fildes, const struct strbuf *ctlptr,
          const struct strbuf *dataptr, int flags);

  HPUX:
     don't set.
     no SYS V.4 streams.


ACE_HAS_STREAMS:
----------------

  Used In:
     ace/OS.h
     libsrc/IPC_SAP/SOCK_SAP/LSOCK.C

  Notes:
     if defined, includes <stropts.h>

  HPUX:
     don't set.
     no SYS V.4 streams.


ACE_HAS_STREAM_PIPES:
---------------------

  Used in:
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE_Msg.h
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE_Msg.C
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE_Listener.h
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE_Listener.C
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE.h
     libsrc/IPC_SAP/SPIPE_SAP/SPIPE.C
     libsrc/IPC_SAP/FIFO_SAP/FIFO_Send_Msg.h
     libsrc/IPC_SAP/FIFO_SAP/FIFO_Send_Msg.C
     libsrc/IPC_SAP/FIFO_SAP/FIFO_Send_Msg.i
     libsrc/IPC_SAP/FIFO_SAP/FIFO_Recv_Msg.h
     libsrc/IPC_SAP/FIFO_SAP/FIFO_Recv_Msg.C
     libsrc/IPC_SAP/FIFO_SAP/FIFO_Recv_Msg.i

  Notes:
     if not set, won't be able to use the SPIPE class (IPC_SAP) with
     rendezvous handles.

  HPUX:
     don't set.
     No sysV.4 streams.


ACE_HAS_SVR4_DYNAMIC_LINKING:
-----------------------------

  Used in:
     ace/OS.h
     tests/Service_Configurator/CCM_App.C

  Notes:
     if defined, includes <dlfcn.h>
     with dlopen(), dlsym(), etc..

  HPUX:
     don't set.
     has its own:
     shl_findsym( ), shl_gethandle( ), shl_getsymbols( ),
     shl_unload( ), shl_get( )(3X) - explicit load of shared libraries


ACE_HAS_SVR4_GETTIMEOFDAY:
--------------------------

  Used in:
     ace/OS.h
     libsrc/Reactor/Timer_Queue.i

  Notes:
     has to do with gettimeofday ().

  Solaris:
     gettimeofday (struct timeval *tp)

  HPUX:
     don't set.
     it has gettimeofday (struct timeval *tp, struct timezone *tzp);
     most calls do a:
     #if defined (ACE_HAS_SVR4_GETTIMEOFDAY)
      ::gettimeofday (&cur_time);
     #else
      ::gettimeofday (&cur_time, 0);
     #endif /* ACE_HAS_SVR4_GETTIMEOFDAY */


ACE_HAS_POLL:
------------
  Used in:
     ace/OS.h

  Notes:
     #if defined (ACE_HAS_POLL)
     #include /**/ <poll.h>
     #endif /* ACE_HAS_POLL */

ACE_USE_POLL_IMPLEMENTATION:
------------------

  Used in:
     ace/OS.h

  Notes:
    Use the poll() event demultiplexor rather than select().

  HPUX:
     set it.


ACE_HAS_SVR4_SIGNAL_T:
----------------------

  Used in:
     ace/OS.h

  Notes:
     #if defined (ACE_HAS_SVR4_SIGNAL_T)
     typedef void (*SignalHandler)(int);
     typedef void (*SignalHandlerV)(void);
     #elif defined (ACE_HAS_SIGNALHANDLERV_INT_ARG)
     typedef void (*SignalHandler)(int);
     typedef void (*SignalHandlerV)(int);
     #else
     #define SignalHandler SIG_PF
     typedef void (*SignalHandlerV)(...);
     #endif /* ACE_HAS_SVR4_SIGNAL_T */

  HPUX:
     set it.


ACE_HAS_SVR4_TLI:
-----------------

  Used in:
     libsrc/IPC_SAP/TLI_SAP/TLI.C
     libsrc/IPC_SAP/TLI_SAP/TLI.h
     libsrc/IPC_SAP/TLI_SAP/TLI_Stream.C

  Notes:
     TLI is the transport layer calls as in: t_bind(), t_open(), t_unbind(),
     t_optmgmt(), ... in SunOS and Solaris.

  HPUX:
     don't set.
     Not supported.


ACE_HAS_SYS_FILIO_H:
--------------------

  Used in:
     ace/OS.h

  Notes:
     if not defined, includes <sys/filio.h>.
     didn't find any reference to anything in this file in the ACE code.

  Solaris:
     filio.h defines FIOCLEX, FIOASYNC, ... as _IO('f', 1), ..
     for FIOLFS,.. solaris has this to say:
     /*
      * ioctl's for Online: DiskSuite.
      * WARNING - the support for these ioctls may be withdrawn
      * in the future OS releases.
      */

  HPUX:
     <sys/ioctl.h> defines FIOASYNC and some other ones,
     <sgtty.h> defines some like FIOCLEX.
     some are never defined.
     use #ifdef HP-UX to modify sysincludes.h


ACE_HAS_TEMPLATE_TYPEDEFS:
--------------------------

  Used in:
     libsrc/ASX/*.[Chi]

  Notes:
     cfront-based C++ compilers don't implement templates that support
     classes with typedefs of other types as formal arguments.  This
     typedef uses the C++ preprocessor to work around this problem.

ACE_HAS_THREADS:
----------------

  Used in:
     libsrc/Service_Configurator/Svc_Conf.y.C
     libsrc/Service_Configurator/Thread_Spawn.i
     libsrc/Threads/Synch.C
     libsrc/Threads/Synch.i
     libsrc/Threads/Thr_Manager.i
     libsrc/ASX/STREAM.C
     libsrc/ASX/Queue.C
     libsrc/ASX/Module.C
     libsrc/ASX/Stream_Modules.C
     libsrc/ASX/Multiplexor.C
     libsrc/ASX/Message_List.C
     include/Message_List.h
     include/Module.h
     include/Multiplexor.h
     include/Queue.h
     include/STREAM.h
     include/Stream_Modules.h
     include/Service_Types.h
     include/Thread_Spawn.h
     include/Synch.h
     include/Thr_Manager.h

  Notes:
     We use Message_List.h even in a non-threaded environment.
     our XOMessageList.h does this by #ifdefs around Threaded things.

  HPUX:
     not until 10.0.


ACE_HAS_TIMOD_H:
----------------

  Used in:
     ace/OS.h

  Notes:
     if defined, include <sys/timod.h>

  Solaris:
     timod is a STREAMS module for use with the Transport  Inter-
     face  (TI)  functions  of the Network Services library.  The
     timod module converts a set of ioctl(2) calls  into  STREAMS
     messages  that  may be consumed by a transport protocol pro-
     vider that supports the Transport Interface.  This allows  a
     user to initiate certain TI functions as atomic operations.

  HPUX:
     don't set.


ACE_HAS_TIUSER_H:
-----------------

  Used in:
     ace/OS.h

  Notes:
     if set, includes <tiuser.h>

  Solaris:
     in conjunction with t_bind, t_accept, etc.. transport layer.

  HPUX:
     don't set.


ACE_USE_POLL_IMPLEMENTATION:
----------------------------

  Used in:
     libsrc/Reactor/Reactor.i
     include/Event_Handler.h
     ace/OS.h
     include/Reactor.h

  Notes:
     in the reactor, use poll instead of select.  In general,
     good thing to have set.

ACE_USES_GPROF:
----------------------------
  Used in:
    ace/Base_Thread_Adapter.h
    ace/Base_Thread_Adapter.inl
    ace/Base_Thread_Adapter.cpp

  Notes:
    When using gprof mainly on Linux, #define ACE_USES_GPROF
    will add calls to getitimer/setitimer in order to initialize profile
    timer and overcome the problem of gprof with multithreaded applications.

ACE_QTREACTOR_CLEAR_PENDING_EVENTS:
----------------------------
  Used in:
    ace/QtReactor.cpp:
    QtReactor by default does not clear qt events pending for
    activated socket. Clearing costs much, at least 2 hash accesses
    in ACE, and 2 another in Qt. It is also better to not clear
    pending events as some side effects are unknown. However,
    when events are not clear, then some user applications may be
    confused by handle_input/output/exception called without any
    data eg. in ACE_Acceptor::make_svc_handler. This swithc is
    intended to quickly fix user application which does not
    follow some reactor rules.
 Linux:
   It seems linux::qt does not queue pending events. Do not define
   this switch.
 Windows:
   Windows::qt queues pending events. If user application has handle_*
   methods which cannot be called without data, then turn on this switch
   to quickly fix the bug. However, one should seriously fix the
   application then.


ACE QoS API (AQoSA)
===================

This directory contains the implementation for the ACE QoS API (AQoSA).

BUILD REQUIREMENTS
==================
WIN2K :

AQoSA makes use of the GQOS API under Windows 2000.  The minimum
requirements are:

1. June98 Platform SDK or later.
2. Link with ws2_32.lib

More information about GQOS is available from the MSDN website:
http://msdn.microsoft.com/msdn-files/026/002/258/Search.asp

-------------------------------------------------------------------------------

UNIX :

AQoSA makes use of the RSVP API (RAPI) under UNIX.
RAPI can be obtained from: ftp://ftp.isi.edu/rsvp/release/.
rsvpd.rel4.2a4-1 may require patches in order to compile
under current versions of Linux.  Contact Craig Rodrigues <crodrigu@bbn.com>
to obtain these patches.

The following lines should be added to your platform_macros.GNU file
before building AQoSA:

PLATFORM_RAPI_CPPFLAGS += -I[path to RAPI header files]
PLATFORM_RAPI_LIBS += -lrsvp
PLATFORM_RAPI_LDFLAGS += -L[path to RAPI library files]

1. Compile AQoSA with

   make rapi=1

More information about RAPI can be found at:

http://www.opengroup.org/onlinepubs/9619099/toc.htm
http://www.cs.wustl.edu/~vishal/qos.html
http://www.sun.com/software/bandwidth/rsvp/docs/
http://www.tru64unix.compaq.com/faqs/publications/base_doc/DOCUMENTATION/V51_HTML/ARH9UCTE/TOC.HTM#RSVPCHXX

-------------------------------------------------------------------------------

TEST
====

The test for AQoSA is located in $ACE_ROOT/examples/QOS

# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB sources *.c)

set(bzip2_STAT_SRCS
  ${sources}
)

include_directories(
  ${CMAKE_SOURCE_DIR}/dep/zlib
  ${CMAKE_CURRENT_SOURCE_DIR}
)

add_library(bzip2 STATIC ${bzip2_STAT_SRCS})

--------------------------------------------------------------------------

This program, "bzip2", the associated library "libbzip2", and all
documentation, are copyright (C) 1996-2010 Julian R Seward.  All
rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. The origin of this software must not be misrepresented; you must 
   not claim that you wrote the original software.  If you use this 
   software in a product, an acknowledgment in the product 
   documentation would be appreciated but is not required.

3. Altered source versions must be plainly marked as such, and must
   not be misrepresented as being the original software.

4. The name of the author may not be used to endorse or promote 
   products derived from this software without specific prior written 
   permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Julian Seward, jseward@bzip.org
bzip2/libbzip2 version 1.0.6 of 6 September 2010

--------------------------------------------------------------------------

This is the README for bzip2/libzip2.
This version is fully compatible with the previous public releases.

------------------------------------------------------------------
This file is part of bzip2/libbzip2, a program and library for
lossless, block-sorting data compression.

bzip2/libbzip2 version 1.0.6 of 6 September 2010
Copyright (C) 1996-2010 Julian Seward <jseward@bzip.org>

Please read the WARNING, DISCLAIMER and PATENTS sections in this file.

This program is released under the terms of the license contained
in the file LICENSE.
------------------------------------------------------------------

Complete documentation is available in Postscript form (manual.ps),
PDF (manual.pdf) or html (manual.html).  A plain-text version of the
manual page is available as bzip2.txt.


HOW TO BUILD -- UNIX

Type 'make'.  This builds the library libbz2.a and then the programs
bzip2 and bzip2recover.  Six self-tests are run.  If the self-tests
complete ok, carry on to installation:

To install in /usr/local/bin, /usr/local/lib, /usr/local/man and
/usr/local/include, type

   make install

To install somewhere else, eg, /xxx/yyy/{bin,lib,man,include}, type

   make install PREFIX=/xxx/yyy

If you are (justifiably) paranoid and want to see what 'make install'
is going to do, you can first do

   make -n install                      or
   make -n install PREFIX=/xxx/yyy      respectively.

The -n instructs make to show the commands it would execute, but not
actually execute them.


HOW TO BUILD -- UNIX, shared library libbz2.so.

Do 'make -f Makefile-libbz2_so'.  This Makefile seems to work for
Linux-ELF (RedHat 7.2 on an x86 box), with gcc.  I make no claims
that it works for any other platform, though I suspect it probably
will work for most platforms employing both ELF and gcc.

bzip2-shared, a client of the shared library, is also built, but not
self-tested.  So I suggest you also build using the normal Makefile,
since that conducts a self-test.  A second reason to prefer the
version statically linked to the library is that, on x86 platforms,
building shared objects makes a valuable register (%ebx) unavailable
to gcc, resulting in a slowdown of 10%-20%, at least for bzip2.

Important note for people upgrading .so's from 0.9.0/0.9.5 to version
1.0.X.  All the functions in the library have been renamed, from (eg)
bzCompress to BZ2_bzCompress, to avoid namespace pollution.
Unfortunately this means that the libbz2.so created by
Makefile-libbz2_so will not work with any program which used an older
version of the library.  I do encourage library clients to make the
effort to upgrade to use version 1.0, since it is both faster and more
robust than previous versions.


HOW TO BUILD -- Windows 95, NT, DOS, Mac, etc.

It's difficult for me to support compilation on all these platforms.
My approach is to collect binaries for these platforms, and put them
on the master web site (http://www.bzip.org).  Look there.  However
(FWIW), bzip2-1.0.X is very standard ANSI C and should compile
unmodified with MS Visual C.  If you have difficulties building, you
might want to read README.COMPILATION.PROBLEMS.

At least using MS Visual C++ 6, you can build from the unmodified
sources by issuing, in a command shell: 

   nmake -f makefile.msc

(you may need to first run the MSVC-provided script VCVARS32.BAT
 so as to set up paths to the MSVC tools correctly).


VALIDATION

Correct operation, in the sense that a compressed file can always be
decompressed to reproduce the original, is obviously of paramount
importance.  To validate bzip2, I used a modified version of Mark
Nelson's churn program.  Churn is an automated test driver which
recursively traverses a directory structure, using bzip2 to compress
and then decompress each file it encounters, and checking that the
decompressed data is the same as the original.



Please read and be aware of the following:

WARNING:

   This program and library (attempts to) compress data by 
   performing several non-trivial transformations on it.  
   Unless you are 100% familiar with *all* the algorithms 
   contained herein, and with the consequences of modifying them, 
   you should NOT meddle with the compression or decompression 
   machinery.  Incorrect changes can and very likely *will* 
   lead to disastrous loss of data.


DISCLAIMER:

   I TAKE NO RESPONSIBILITY FOR ANY LOSS OF DATA ARISING FROM THE
   USE OF THIS PROGRAM/LIBRARY, HOWSOEVER CAUSED.

   Every compression of a file implies an assumption that the
   compressed file can be decompressed to reproduce the original.
   Great efforts in design, coding and testing have been made to
   ensure that this program works correctly.  However, the complexity
   of the algorithms, and, in particular, the presence of various
   special cases in the code which occur with very low but non-zero
   probability make it impossible to rule out the possibility of bugs
   remaining in the program.  DO NOT COMPRESS ANY DATA WITH THIS
   PROGRAM UNLESS YOU ARE PREPARED TO ACCEPT THE POSSIBILITY, HOWEVER
   SMALL, THAT THE DATA WILL NOT BE RECOVERABLE.

   That is not to say this program is inherently unreliable.  
   Indeed, I very much hope the opposite is true.  bzip2/libbzip2 
   has been carefully constructed and extensively tested.


PATENTS:

   To the best of my knowledge, bzip2/libbzip2 does not use any 
   patented algorithms.  However, I do not have the resources 
   to carry out a patent search.  Therefore I cannot give any 
   guarantee of the above statement.



WHAT'S NEW IN 0.9.0 (as compared to 0.1pl2) ?

   * Approx 10% faster compression, 30% faster decompression
   * -t (test mode) is a lot quicker
   * Can decompress concatenated compressed files
   * Programming interface, so programs can directly read/write .bz2 files
   * Less restrictive (BSD-style) licensing
   * Flag handling more compatible with GNU gzip
   * Much more documentation, i.e., a proper user manual
   * Hopefully, improved portability (at least of the library)

WHAT'S NEW IN 0.9.5 ?

   * Compression speed is much less sensitive to the input
     data than in previous versions.  Specifically, the very
     slow performance caused by repetitive data is fixed.
   * Many small improvements in file and flag handling.
   * A Y2K statement.

WHAT'S NEW IN 1.0.0 ?

   See the CHANGES file.

WHAT'S NEW IN 1.0.2 ?

   See the CHANGES file.

WHAT'S NEW IN 1.0.3 ?

   See the CHANGES file.

WHAT'S NEW IN 1.0.4 ?

   See the CHANGES file.

WHAT'S NEW IN 1.0.5 ?

   See the CHANGES file.

WHAT'S NEW IN 1.0.6 ?

   See the CHANGES file.


I hope you find bzip2 useful.  Feel free to contact me at
   jseward@bzip.org
if you have any suggestions or queries.  Many people mailed me with
comments, suggestions and patches after the releases of bzip-0.15,
bzip-0.21, and bzip2 versions 0.1pl2, 0.9.0, 0.9.5, 1.0.0, 1.0.1,
1.0.2 and 1.0.3, and the changes in bzip2 are largely a result of this
feedback.  I thank you for your comments.

bzip2's "home" is http://www.bzip.org/

Julian Seward
jseward@bzip.org
Cambridge, UK.

18     July 1996 (version 0.15)
25   August 1996 (version 0.21)
 7   August 1997 (bzip2, version 0.1)
29   August 1997 (bzip2, version 0.1pl2)
23   August 1998 (bzip2, version 0.9.0)
 8     June 1999 (bzip2, version 0.9.5)
 4     Sept 1999 (bzip2, version 0.9.5d)
 5      May 2000 (bzip2, version 1.0pre8)
30 December 2001 (bzip2, version 1.0.2pre1)
15 February 2005 (bzip2, version 1.0.3)
20 December 2006 (bzip2, version 1.0.4)
10 December 2007 (bzip2, version 1.0.5)
 6     Sept 2010 (bzip2, version 1.0.6)
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(g3dlib_STAT_SRCS
  source/AABox.cpp
  source/Any.cpp
  source/AnyTableReader.cpp
  source/BinaryFormat.cpp
  source/BinaryInput.cpp
  source/BinaryOutput.cpp
  source/Box.cpp
  source/Capsule.cpp
  source/CollisionDetection.cpp
  source/CoordinateFrame.cpp
  source/Crypto.cpp
  source/Cylinder.cpp
  source/debugAssert.cpp
  source/FileSystem.cpp
  source/fileutils.cpp
  source/format.cpp
  source/g3dfnmatch.cpp
  source/g3dmath.cpp
  source/GThread.cpp
  source/Line.cpp
  source/LineSegment.cpp
  source/Log.cpp
  source/Matrix3.cpp
  source/Matrix4.cpp
  source/MemoryManager.cpp
  source/PhysicsFrame.cpp
  source/Plane.cpp
  source/prompt.cpp
  source/Quat.cpp
  source/Random.cpp
  source/Ray.cpp
  source/RegistryUtil.cpp
  source/Sphere.cpp
  source/stringutils.cpp
  source/System.cpp
  source/TextInput.cpp
  source/TextOutput.cpp
  source/Triangle.cpp
  source/uint128.cpp
  source/UprightFrame.cpp
  source/Vector2.cpp
  source/Vector3.cpp
  source/Vector4.cpp
)

if(WIN32)
  include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_SOURCE_DIR}/dep/zlib
  )
else()
  include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
  )
endif()

add_library(g3dlib STATIC ${g3dlib_STAT_SRCS})

target_link_libraries(g3dlib
  ${ZLIB_LIBRARIES}
  ${CMAKE_THREAD_LIBS_INIT}
)
 Due to issues with G3D normally requiring X11 and the ZIP-library, the library version in this sourcetree contains a modified version.
The applied patches are added as .diff-files to the repository for future reference (knowing what was changed is quite handy).

G3D-v8.0_hotfix1.diff - 2010-08-27 - remove dependency on zip/z11 libraries, add support for 64-bit arch
G3D-v8.0_hotfix2.diff - 2012-01-14 - fix typo in isNaN(float x)
G3D-v8.0_hotfix3.diff - 2012-08-26 - fix compilation on Fedora Linux
G3D-v8.0_hotfix4.diff - 2012-11-09 - fix compilation on OSX
G3D-v8.0_hotfix5.diff - 2013-02-27 - fix compilation in cygwin environments
G3D-v8.0_hotfix6.diff - 2013-03-08 - fix compilation in mingw
G3D-v8.0_hotfix7.diff - 2013-08-31 - fix typo in Matrix4 == operator
G3D-v8.0_hotfix8.diff - 2013-09-01 - fix typo in Vector3int32 += operator
G3D-v8.0_hotfix9.diff - 2014-06-01 - only VS < 10 don't ship inttypes.h
G3D-v9.0 hotfix1.diff - 2014-08-22 - updated to G3D9, reapplied previous patches and removed unneeded changes
G3D-v9.0 hotfix2.diff - 2014-08-23 - fix some -Wconversion warnings
G3D-v9.0 hotfix3.diff - 2015-06-28 - fix some warnings
G3D-v9.0 hotfix4.diff - 2015-07-02 - backport G3D10 fix
G3D-v9.0 hotfix5.diff - 2015-07-31 - fix MSVC 2015 warning: dep/g3dlite/include/G3D/Quat.h(352): warning C4458: declaration of 'x' hides class member
G3D-v9.0 hotfix6.diff - 2015-11-04 - fix adding std::shared_ptr, std::weak_ptr, std::dynamic_pointer_cast, std::static_pointer_cast and std::enable_shared_from_this to global namespace
G3D-v9.0 hotfix7.diff - 2016-10-10 - fix warning on clang 3.8 backported from G3D 10
/**
 @file license.cpp
 
 @author Morgan McGuire, graphics3d.com
 
 @created 2004-04-15
 @edited  2004-04-15
*/

#include "G3D/format.h"
#include <string>

namespace G3D {

std::string license() {
    return format(

"This software is based in part on the PNG Reference Library which is\n"
"Copyright (c) 2004 Glenn Randers-Pehrson\n\n"
"This software is based in part on the work of the Independent JPEG Group.\n\n"
"This software is based on part on the FFmpeg libavformat and libavcodec libraries\n" 
"(\"FFmpeg\", http://ffmpeg.mplayerhq.hu), which are included under the terms of the\n" 
"GNU Lesser General Public License (LGPL), (http://www.gnu.org/copyleft/lesser.html).\n\n"
"%s"
"This program uses the G3D Library (http://g3d.sf.net), which\n"
"is licensed under the \"Modified BSD\" Open Source license.  The G3D library\n"
"source code is Copyright  2000-2011, Morgan McGuire, All rights reserved.\n"
"This program uses The OpenGL Extension Wrangler Library, which \n"
"is licensed under the \"Modified BSD\" Open Source license.  \n"
"The OpenGL Extension Wrangler Library source code is\n"
"Copyright (C) 2002-2008, Milan Ikits <milan ikits[]ieee org>\n"
"Copyright (C) 2002-2008, Marcelo E. Magallon <mmagallo[]debian org>\n"
"Copyright (C) 2002, Lev Povalahev\n"
"All rights reserved.\n\n"
"The Modified BSD license is below, and requires the following statement:\n"
"\n"
"Redistribution and use in source and binary forms, with or without \n"
"modification, are permitted provided that the following conditions are met:\n"
"\n"
"* Redistributions of source code must retain the above copyright notice, \n"
"  this list of conditions and the following disclaimer.\n"
"* Redistributions in binary form must reproduce the above copyright notice, \n"
"  this list of conditions and the following disclaimer in the documentation \n"
"  and/or other materials provided with the distribution.\n"
"* The name of the author may be used to endorse or promote products \n"
"  derived from this software without specific prior written permission.\n"
"\n"
"THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" \n"
"AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE \n"
"IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n"
"ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE \n"
"LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR \n"
"CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF \n"
"SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS\n"
"INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN\n"
"CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)\n"
"ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF\n"
"THE POSSIBILITY OF SUCH DAMAGE.\n"
"\n\n"
"G3D VERSION %d\n", 

#ifdef G3D_WINDOWS
    "" // Win32 doesn't use SDL
#else
    "This software uses the Simple DirectMedia Layer library (\"SDL\",\n"
    "http://www.libsdl.org), which is included under the terms of the\n"
    "GNU Lesser General Public License, (http://www.gnu.org/copyleft/lesser.html).\n\n"
#endif
,
G3D_VER);
}

}
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB sources *.cpp *.h)

set(gsoap_STAT_SRCS
   ${sources}
)

include_directories(
   ${CMAKE_CURRENT_SOURCE_DIR}
)

# Little fix for MSVC / Windows platforms
add_definitions(-D_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES=0)

add_library(gsoap STATIC ${gsoap_STAT_SRCS})

set_target_properties(gsoap PROPERTIES LINKER_LANGUAGE CXX)
* Generate new headers based on TrinityCore soap-services stub:
gsoap/bin/linux386/soapcpp2 -1 -S -L -w -x -y soap.stub

* Copy the following files from the gsoap package:
gsoap/stdsoap2.h
gsoap/stdsoap2.cpp

* Remove the following files after generation:
ns1.nsmap
soapObject.h

* Test compile and see if SOAP works...
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# We need to generate the jemalloc_def.h header based on platform-specific settings
if (PLATFORM EQUAL 32)
  set(JEM_SIZEDEF 2)
  set(JEM_TLSMODEL)
else()
  set(JEM_SIZEDEF 3)
  set(JEM_TLSMODEL "__attribute__\(\(tls_model\(\"initial-exec\"\)\)\)")
endif()

# Create the header, so we can use it
configure_file(
  "${CMAKE_SOURCE_DIR}/dep/jemalloc/jemalloc_defs.h.in.cmake"
  "${BUILDDIR}/jemalloc_defs.h"
  @ONLY
)

# Done, let's continue
set(jemalloc_STAT_SRC
  ${CMAKE_CURRENT_SOURCE_DIR}/src/arena.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/atomic.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/base.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/bitmap.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/chunk.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/chunk_dss.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/chunk_mmap.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/ckh.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/ctl.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/extent.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/hash.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/huge.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/jemalloc.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/mb.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/mutex.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/prof.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/quarantine.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/rtree.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/stats.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/tcache.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/tsd.c
  ${CMAKE_CURRENT_SOURCE_DIR}/src/util.c
)

include_directories(
  ${BUILDDIR}/
  ${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_definitions(-D_GNU_SOURCE -D_REENTRANT)

add_library(jemalloc STATIC ${jemalloc_STAT_SRC})
jemalloc is a general-purpose scalable concurrent malloc(3) implementation.
This distribution is a "portable" implementation that currently targets
FreeBSD, Linux, Apple OS X, and MinGW.  jemalloc is included as the default
allocator in the FreeBSD and NetBSD operating systems, and it is used by the
Mozilla Firefox web browser on Microsoft Windows-related platforms.  Depending
on your needs, one of the other divergent versions may suit your needs better
than this distribution.

The COPYING file contains copyright and licensing information.

The INSTALL file contains information on how to configure, build, and install
jemalloc.

The ChangeLog file contains a brief summary of changes for each release.

URL: http://www.canonware.com/jemalloc/
*** THIS FILE CONTAINS INFORMATION ABOUT CHANGES DONE TO THE JEMALLOC LIBRARY FILES ***
Removed from archive, as OSX does not use jemalloc:
  src/zone.c
  include/jemalloc/internal/zone.h
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 
 if (NOT MYSQL_FOUND)
	  message(FATAL_ERROR "MySQL wasn't found on your system but it's required to build the servers!")
	endif()
	
	add_library(mysql STATIC IMPORTED GLOBAL)
	
	set_target_properties(mysql
	  PROPERTIES
	    IMPORTED_LOCATION
	      "${MYSQL_LIBRARY}"
	    INTERFACE_INCLUDE_DIRECTORIES
	      "${MYSQL_INCLUDE_DIR}")# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
add_subdirectory(Detour)
add_subdirectory(Recast)
Copyright (c) 2009 Mikko Mononen memon@inside.org

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


Recast & Detour Version 1.4


Recast

Recast is state of the art navigation mesh construction toolset for games.

    * It is automatic, which means that you can throw any level geometry
      at it and you will get robust mesh out
    * It is fast which means swift turnaround times for level designers
    * It is open source so it comes with full source and you can
      customize it to your hearts content. 

The Recast process starts with constructing a voxel mold from a level geometry 
and then casting a navigation mesh over it. The process consists of three steps, 
building the voxel mold, partitioning the mold into simple regions, peeling off 
the regions as simple polygons.

   1. The voxel mold is build from the input triangle mesh by rasterizing 
      the triangles into a multi-layer heightfield. Some simple filters are 
      then applied to the mold to prune out locations where the character 
      would not be able to move.
   2. The walkable areas described by the mold are divided into simple 
      overlayed 2D regions. The resulting regions have only one non-overlapping 
      contour, which simplifies the final step of the process tremendously.
   3. The navigation polygons are peeled off from the regions by first tracing 
      the boundaries and then simplifying them. The resulting polygons are 
      finally converted to convex polygons which makes them perfect for 
      pathfinding and spatial reasoning about the level. 

The toolset code is located in the Recast folder and demo application using the Recast
toolset is located in the RecastDemo folder.

The project files with this distribution can be compiled with Microsoft Visual C++ 2008
(you can download it for free) and XCode 3.1.


Detour

Recast is accompanied with Detour, path-finding and spatial reasoning toolkit. You can use any navigation mesh with Detour, but of course the data generated with Recast fits perfectly.

Detour offers simple static navigation mesh which is suitable for many simple cases, as well as tiled navigation mesh which allows you to plug in and out pieces of the mesh. The tiled mesh allows to create systems where you stream new navigation data in and out as the player progresses the level, or you may regenerate tiles as the world changes. 


Latest code available at http://code.google.com/p/recastnavigation/


--

Release Notes

----------------
* Recast 1.4
  Released August 24th, 2009

- Added detail height mesh generation (RecastDetailMesh.cpp) for single,
  tiled statmeshes as well as tilemesh.
- Added feature to contour tracing which detects extra vertices along
  tile edges which should be removed later.
- Changed the tiled stat mesh preprocess, so that it first generated
  polymeshes per tile and finally combines them.
- Fixed bug in the GUI code where invisible buttons could be pressed.

----------------
* Recast 1.31
  Released July 24th, 2009

- Better cost and heuristic functions.
- Fixed tile navmesh raycast on tile borders.

----------------
* Recast 1.3
  Released July 14th, 2009

- Added dtTileNavMesh which allows to dynamically add and remove navmesh pieces at runtime.
- Renamed stat navmesh types to dtStat* (i.e. dtPoly is now dtStatPoly).
- Moved common code used by tile and stat navmesh to DetourNode.h/cpp and DetourCommon.h/cpp.
- Refactores the demo code.

----------------
* Recast 1.2
  Released June 17th, 2009

- Added tiled mesh generation. The tiled generation allows to generate navigation for
  much larger worlds, it removes some of the artifacts that comes from distance fields
  in open areas, and allows later streaming and dynamic runtime generation
- Improved and added some debug draw modes
- API change: The helper function rcBuildNavMesh does not exists anymore,
  had to change few internal things to cope with the tiled processing,
  similar API functionality will be added later once the tiled process matures
- The demo is getting way too complicated, need to split demos
- Fixed several filtering functions so that the mesh is tighter to the geometry,
  sometimes there could be up error up to tow voxel units close to walls,
  now it should be just one.

----------------
* Recast 1.1
  Released April 11th, 2009

This is the first release of Detour.

----------------
* Recast 1.0
  Released March 29th, 2009

This is the first release of Recast.

The process is not always as robust as I would wish. The watershed phase sometimes swallows tiny islands
which are close to edges. These droppings are handled in rcBuildContours, but the code is not
particularly robust either.

Another non-robust case is when portal contours (contours shared between two regions) are always
assumed to be straight. That can lead to overlapping contours specially when the level has
large open areas.



Mikko Mononen
memon@inside.org
TODO/Roadmap

Summer/Autumn 2009

- Off mesh links (jump links)
- Area annotations
- Embed extra data per polygon
- Height conforming navmesh


Autumn/Winter 2009/2010

- Detour path following
- More dynamic example with tile navmesh
- Faster small tile process


More info at http://digestingduck.blogspot.com/2009/07/recast-and-detour-roadmap.html

-
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(Detour_STAT_SRCS
    DetourAlloc.cpp 
    DetourCommon.cpp 
    DetourNavMesh.cpp 
    DetourNavMeshBuilder.cpp 
    DetourNavMeshQuery.cpp 
    DetourNode.cpp 
)

if(WIN32)
  include_directories(
    ${CMAKE_SOURCE_DIR}/dep/zlib
  )
endif()

add_library(Detour STATIC ${Detour_STAT_SRCS})

target_link_libraries(Detour ${ZLIB_LIBRARIES})
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(Recast_STAT_SRCS
    Recast.cpp 
    RecastAlloc.cpp 
    RecastArea.cpp 
    RecastContour.cpp 
    RecastFilter.cpp 
    RecastLayers.cpp 
    RecastMesh.cpp 
    RecastMeshDetail.cpp 
    RecastRasterization.cpp 
    RecastRegion.cpp 
)

if(WIN32)
  include_directories(
    ${CMAKE_SOURCE_DIR}/dep/zlib
  )
endif()

add_library(Recast STATIC ${Recast_STAT_SRCS})

target_link_libraries(Recast ${ZLIB_LIBRARIES})# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(SRC_FILES
           src/adpcm/adpcm.cpp
           src/huffman/huff.cpp
           src/jenkins/lookup3.c
           src/lzma/C/LzFind.c
           src/lzma/C/LzmaDec.c
           src/lzma/C/LzmaEnc.c
           src/pklib/explode.c
           src/pklib/implode.c
           src/sparse/sparse.cpp
           src/FileStream.cpp
           src/SBaseCommon.cpp
           src/SBaseFileTable.cpp
           src/SCompression.cpp
           src/SFileAddFile.cpp
           src/SFileAttributes.cpp
           src/SFileCompactArchive.cpp
           src/SFileCreateArchive.cpp
           src/SFileExtractFile.cpp
           src/SFileFindFile.cpp
           src/SFileListFile.cpp
           src/SFileOpenArchive.cpp
           src/SFileOpenFileEx.cpp
           src/SFilePatchArchives.cpp
           src/SFileReadFile.cpp
           src/SFileVerify.cpp
)

set(TOMCRYPT_FILES
           src/libtomcrypt/src/hashes/hash_memory.c
           src/libtomcrypt/src/hashes/md5.c
           src/libtomcrypt/src/hashes/sha1.c
           src/libtomcrypt/src/math/ltm_desc.c
           src/libtomcrypt/src/math/multi.c
           src/libtomcrypt/src/math/rand_prime.c
           src/libtomcrypt/src/misc/base64_decode.c
           src/libtomcrypt/src/misc/crypt_argchk.c
           src/libtomcrypt/src/misc/crypt_find_hash.c
           src/libtomcrypt/src/misc/crypt_find_prng.c
           src/libtomcrypt/src/misc/crypt_hash_descriptor.c
           src/libtomcrypt/src/misc/crypt_hash_is_valid.c
           src/libtomcrypt/src/misc/crypt_libc.c
           src/libtomcrypt/src/misc/crypt_ltc_mp_descriptor.c
           src/libtomcrypt/src/misc/crypt_prng_descriptor.c
           src/libtomcrypt/src/misc/crypt_prng_is_valid.c
           src/libtomcrypt/src/misc/crypt_register_hash.c
           src/libtomcrypt/src/misc/crypt_register_prng.c
           src/libtomcrypt/src/misc/zeromem.c
           src/libtomcrypt/src/pk/asn1/der_decode_bit_string.c
           src/libtomcrypt/src/pk/asn1/der_decode_boolean.c
           src/libtomcrypt/src/pk/asn1/der_decode_choice.c
           src/libtomcrypt/src/pk/asn1/der_decode_ia5_string.c
           src/libtomcrypt/src/pk/asn1/der_decode_integer.c
           src/libtomcrypt/src/pk/asn1/der_decode_object_identifier.c
           src/libtomcrypt/src/pk/asn1/der_decode_octet_string.c
           src/libtomcrypt/src/pk/asn1/der_decode_printable_string.c
           src/libtomcrypt/src/pk/asn1/der_decode_sequence_ex.c
           src/libtomcrypt/src/pk/asn1/der_decode_sequence_flexi.c
           src/libtomcrypt/src/pk/asn1/der_decode_sequence_multi.c
           src/libtomcrypt/src/pk/asn1/der_decode_short_integer.c
           src/libtomcrypt/src/pk/asn1/der_decode_utctime.c
           src/libtomcrypt/src/pk/asn1/der_decode_utf8_string.c
           src/libtomcrypt/src/pk/asn1/der_length_bit_string.c
           src/libtomcrypt/src/pk/asn1/der_length_boolean.c
           src/libtomcrypt/src/pk/asn1/der_length_ia5_string.c
           src/libtomcrypt/src/pk/asn1/der_length_integer.c
           src/libtomcrypt/src/pk/asn1/der_length_object_identifier.c
           src/libtomcrypt/src/pk/asn1/der_length_octet_string.c
           src/libtomcrypt/src/pk/asn1/der_length_printable_string.c
           src/libtomcrypt/src/pk/asn1/der_length_sequence.c
           src/libtomcrypt/src/pk/asn1/der_length_utctime.c
           src/libtomcrypt/src/pk/asn1/der_sequence_free.c
           src/libtomcrypt/src/pk/asn1/der_length_utf8_string.c
           src/libtomcrypt/src/pk/asn1/der_length_short_integer.c
           src/libtomcrypt/src/pk/ecc/ltc_ecc_map.c
           src/libtomcrypt/src/pk/ecc/ltc_ecc_mul2add.c
           src/libtomcrypt/src/pk/ecc/ltc_ecc_mulmod.c
           src/libtomcrypt/src/pk/ecc/ltc_ecc_points.c
           src/libtomcrypt/src/pk/ecc/ltc_ecc_projective_add_point.c
           src/libtomcrypt/src/pk/ecc/ltc_ecc_projective_dbl_point.c
           src/libtomcrypt/src/pk/pkcs1/pkcs_1_mgf1.c
           src/libtomcrypt/src/pk/pkcs1/pkcs_1_oaep_decode.c
           src/libtomcrypt/src/pk/pkcs1/pkcs_1_pss_decode.c
           src/libtomcrypt/src/pk/pkcs1/pkcs_1_v1_5_decode.c
           src/libtomcrypt/src/pk/rsa/rsa_exptmod.c
           src/libtomcrypt/src/pk/rsa/rsa_free.c
           src/libtomcrypt/src/pk/rsa/rsa_import.c
           src/libtomcrypt/src/pk/rsa/rsa_make_key.c
           src/libtomcrypt/src/pk/rsa/rsa_verify_hash.c
           src/libtomcrypt/src/pk/rsa/rsa_verify_simple.c
)

set(TOMMATH_FILES
           src/libtommath/bncore.c
           src/libtommath/bn_fast_mp_invmod.c
           src/libtommath/bn_fast_mp_montgomery_reduce.c
           src/libtommath/bn_fast_s_mp_mul_digs.c
           src/libtommath/bn_fast_s_mp_mul_high_digs.c
           src/libtommath/bn_fast_s_mp_sqr.c
           src/libtommath/bn_mp_2expt.c
           src/libtommath/bn_mp_abs.c
           src/libtommath/bn_mp_add.c
           src/libtommath/bn_mp_addmod.c
           src/libtommath/bn_mp_add_d.c
           src/libtommath/bn_mp_and.c
           src/libtommath/bn_mp_clamp.c
           src/libtommath/bn_mp_clear.c
           src/libtommath/bn_mp_clear_multi.c
           src/libtommath/bn_mp_cmp.c
           src/libtommath/bn_mp_cmp_d.c
           src/libtommath/bn_mp_cmp_mag.c
           src/libtommath/bn_mp_cnt_lsb.c
           src/libtommath/bn_mp_copy.c
           src/libtommath/bn_mp_count_bits.c
           src/libtommath/bn_mp_div.c
           src/libtommath/bn_mp_div_2.c
           src/libtommath/bn_mp_div_2d.c
           src/libtommath/bn_mp_div_3.c
           src/libtommath/bn_mp_div_d.c
           src/libtommath/bn_mp_dr_is_modulus.c
           src/libtommath/bn_mp_dr_reduce.c
           src/libtommath/bn_mp_dr_setup.c
           src/libtommath/bn_mp_exch.c
           src/libtommath/bn_mp_exptmod.c
           src/libtommath/bn_mp_exptmod_fast.c
           src/libtommath/bn_mp_expt_d.c
           src/libtommath/bn_mp_exteuclid.c
           src/libtommath/bn_mp_fread.c
           src/libtommath/bn_mp_fwrite.c
           src/libtommath/bn_mp_gcd.c
           src/libtommath/bn_mp_get_int.c
           src/libtommath/bn_mp_grow.c
           src/libtommath/bn_mp_init.c
           src/libtommath/bn_mp_init_copy.c
           src/libtommath/bn_mp_init_multi.c
           src/libtommath/bn_mp_init_set.c
           src/libtommath/bn_mp_init_set_int.c
           src/libtommath/bn_mp_init_size.c
           src/libtommath/bn_mp_invmod.c
           src/libtommath/bn_mp_invmod_slow.c
           src/libtommath/bn_mp_is_square.c
           src/libtommath/bn_mp_jacobi.c
           src/libtommath/bn_mp_karatsuba_mul.c
           src/libtommath/bn_mp_karatsuba_sqr.c
           src/libtommath/bn_mp_lcm.c
           src/libtommath/bn_mp_lshd.c
           src/libtommath/bn_mp_mod.c
           src/libtommath/bn_mp_mod_2d.c
           src/libtommath/bn_mp_mod_d.c
           src/libtommath/bn_mp_montgomery_calc_normalization.c
           src/libtommath/bn_mp_montgomery_reduce.c
           src/libtommath/bn_mp_montgomery_setup.c
           src/libtommath/bn_mp_mul.c
           src/libtommath/bn_mp_mulmod.c
           src/libtommath/bn_mp_mul_2.c
           src/libtommath/bn_mp_mul_2d.c
           src/libtommath/bn_mp_mul_d.c
           src/libtommath/bn_mp_neg.c
           src/libtommath/bn_mp_n_root.c
           src/libtommath/bn_mp_or.c
           src/libtommath/bn_mp_prime_fermat.c
           src/libtommath/bn_mp_prime_is_divisible.c
           src/libtommath/bn_mp_prime_is_prime.c
           src/libtommath/bn_mp_prime_miller_rabin.c
           src/libtommath/bn_mp_prime_next_prime.c
           src/libtommath/bn_mp_prime_rabin_miller_trials.c
           src/libtommath/bn_mp_prime_random_ex.c
           src/libtommath/bn_mp_radix_size.c
           src/libtommath/bn_mp_radix_smap.c
           src/libtommath/bn_mp_rand.c
           src/libtommath/bn_mp_read_radix.c
           src/libtommath/bn_mp_read_signed_bin.c
           src/libtommath/bn_mp_read_unsigned_bin.c
           src/libtommath/bn_mp_reduce.c
           src/libtommath/bn_mp_reduce_2k.c
           src/libtommath/bn_mp_reduce_2k_l.c
           src/libtommath/bn_mp_reduce_2k_setup.c
           src/libtommath/bn_mp_reduce_2k_setup_l.c
           src/libtommath/bn_mp_reduce_is_2k.c
           src/libtommath/bn_mp_reduce_is_2k_l.c
           src/libtommath/bn_mp_reduce_setup.c
           src/libtommath/bn_mp_rshd.c
           src/libtommath/bn_mp_set.c
           src/libtommath/bn_mp_set_int.c
           src/libtommath/bn_mp_shrink.c
           src/libtommath/bn_mp_signed_bin_size.c
           src/libtommath/bn_mp_sqr.c
           src/libtommath/bn_mp_sqrmod.c
           src/libtommath/bn_mp_sqrt.c
           src/libtommath/bn_mp_sub.c
           src/libtommath/bn_mp_submod.c
           src/libtommath/bn_mp_sub_d.c
           src/libtommath/bn_mp_toom_mul.c
           src/libtommath/bn_mp_toom_sqr.c
           src/libtommath/bn_mp_toradix.c
           src/libtommath/bn_mp_toradix_n.c
           src/libtommath/bn_mp_to_signed_bin.c
           src/libtommath/bn_mp_to_signed_bin_n.c
           src/libtommath/bn_mp_to_unsigned_bin.c
           src/libtommath/bn_mp_to_unsigned_bin_n.c
           src/libtommath/bn_mp_unsigned_bin_size.c
           src/libtommath/bn_mp_xor.c
           src/libtommath/bn_mp_zero.c
           src/libtommath/bn_prime_tab.c
           src/libtommath/bn_reverse.c
           src/libtommath/bn_s_mp_add.c
           src/libtommath/bn_s_mp_exptmod.c
           src/libtommath/bn_s_mp_mul_digs.c
           src/libtommath/bn_s_mp_mul_high_digs.c
           src/libtommath/bn_s_mp_sqr.c
           src/libtommath/bn_s_mp_sub.c
)

set(ZLIB_BZIP2_FILES
           src/bzip2/blocksort.c
           src/bzip2/bzlib.c
           src/bzip2/compress.c
           src/bzip2/crctable.c
           src/bzip2/decompress.c
           src/bzip2/huffman.c
           src/bzip2/randtable.c
           src/zlib/adler32.c
           src/zlib/compress2.c
           src/zlib/crc32.c
           src/zlib/deflate.c
           src/zlib/inffast.c
           src/zlib/inflate.c
           src/zlib/inftrees.c
           src/zlib/trees.c
           src/zlib/zutil.c
)

set(TEST_SRC_FILES
           test/Test.cpp
)

add_definitions(-D_7ZIP_ST -DBZ_STRICT_ANSI)

if(WIN32)
    if(MSVC)
        add_definitions(-D_7ZIP_ST -DWIN32)
    endif()
    set(SRC_ADDITIONAL_FILES ${ZLIB_BZIP2_FILES} ${TOMCRYPT_FILES} ${TOMMATH_FILES})
    set(LINK_LIBS wininet)
endif()

if(APPLE)
    set(LINK_LIBS z bz2)
    set(SRC_ADDITIONAL_FILES ${TOMCRYPT_FILES} ${TOMMATH_FILES})
endif()

if (${CMAKE_SYSTEM_NAME} STREQUAL Linux)
    option(WITH_LIBTOMCRYPT "Use system LibTomCrypt library" OFF)
    if(WITH_LIBTOMCRYPT)
        set(LINK_LIBS z bz2 tomcrypt)
    else()
        set(LINK_LIBS z bz2)
        set(SRC_ADDITIONAL_FILES ${TOMCRYPT_FILES} ${TOMMATH_FILES})
    endif()
endif()

add_library(storm STATIC ${SRC_FILES} ${SRC_ADDITIONAL_FILES})
target_link_libraries(storm ${LINK_LIBS})

if(UNIX)
    set_target_properties(storm PROPERTIES SOVERSION 0)
endif()

# On Win32, build StormLib.dll since we don't want to clash with Storm.dll
if(WIN32)
    set_target_properties(storm PROPERTIES OUTPUT_NAME StormLib)
endif()
UCMXF6EJY352EFH4XFRXCFH2XC9MQRZKMMKVHY48RP7WXP4GHYBQ7SL9J9UNPHBP8MXLWHQ7VGGLTZ9MQZQSFDCLJYET3CPPEJ2R5TM6XFE2GUNG5QDGHKQ9UAKPWZSZPBGFBE42Z6LNK65UGJQ3WZVMCLP4HQQTX7SEJJS9TSGCW5P28EBSC47AJPEY8VU25KVBQA8VYE6XRY3DLGC5ZDE4XS4P7YA2478JD2K56EVNVVY4XX8TDWYT5B8KB2548TS4VNFQRZTN6YWHE9CHVDH9NVWD474ALJ52Z32DF4LZ4ZJJXVKK3AZQA6GABLJBK6BDHY2ECUE2545YKNLBJPVYWHE7XYAG6VWCQTN8V3ZZMRUCZXV8A8CGUX2TAA8Hhttp://dist.blizzard.com/mediakey/d3-authenticationcode-deDE.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-enGB.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-enSG.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-enUS.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-esES.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-esMX.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-frFR.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-itIT.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-koKR.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-plPL.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-ptBR.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-ruRU.txt  <====
http://dist.blizzard.com/mediakey/d3-authenticationcode-zhTW.txt
http://dist.blizzard.com/mediakey/d3-authenticationcode-zhCN.txt  <==== 

  StormLib history
  ================

 Version 8.02

 - Support for UNICODE encoding for on-disk files
 - Optimized file deleting

 Version 8.01

 - SFileFindFirstFile and SFileFindNextFile no longer find files that have
   patch file in the oldest MPQ in the patch chain
 - Write support for MPQs version 4

 Version 8.00

 - Updated support for protected maps from Warcraft III

 Version 7.11
 
 - Support for MPQs v 3.0 (WOW-Cataclysm BETA)
 - StormLib now deals properly with files that have MPQ_SECTOR_CHECKSUM missing,
   but have sector checksum entry present in the sector offset table

 Version 7.10
 
 - Support for partial MPQs ("interface.MPQ.part")
 - The only operation that is externally allowed to do with internal files
   ("(listfile)", "(attributes)" and "(signature)") is reading. Attempt to modify any of the file
   fails and GetLastError returns ERROR_INTERNAL_FILE
 - Fixed memory leak that has occured when writing more than one sector to the file at once

 Version 7.01
 
 - Support for adding files from memory
 - Fixed improper validation of handles to MPQ file and MPQ archive
 - Fixed bug where StormLib didn't save CRC32 of the file when added to archive

 Version 7.00

 - Properly deals with MPQs protected by w3xMaster
 - Major rewrite
 - Fixed support for (attributes)
 - Added file verification
 - Added MPQ signature verification

 Version 6.22

 - Properly deals with MPQs protected by w3xMaster

 Version 6.21

 - SFileRenameFile now properly re-crypts the file if necessary.
 - SFileFindFirstFile correctly deals with deleted files

 Version 6.20

 - Fixed lots of bugs when processing files with same names but different locales
 - Fixed bugs when repeately extracts the same file with MPQ_FILE_SINGLE_UNIT flag
 - Added SFileFlushArchive
 - Fixed issue opening AVI files renamed to MPQ using SFileCreateArchiveEx

    After sector offset table
    =========================

FileSize    CmpSize   DWORDs
00007588    000075A4  0x01
0000A9EA    000095EC  0x01
0000E51D    0000E20D  0x02
00015C00    00015C40  0x02
0001C578    000186C4  0x02
0002A9D4    0002A9EA  0x04
00037BAC    00037A42  0x06
0003C3C1    00034084  0x06
0003D224    0003B30F  0x06
00045105    0004195A  0x07
00045D9C    0003D87D  0x07     
0004AAB8    0004860A  0x08
0004D18E    00048E0C  0x07
00056B4C    00056BDD  0x09
0005DC08    00059426  0x09
00061EC0    00057711  0x0A
0006CEC4    00062561  0x0B
000778EE    00066736  0x0C
000AD0CB    0007F32E  0x11
00327EAC    00303395  0x53
THE MOPAQ ARCHIVE FORMAT
v0.9 (Thursday, June 30, 2005)
by Justin Olbrantz(Quantam)

Distribution and reproduction of this specification are allowed without limitation, as long as it is not altered. Quoting
in other works is freely allowed, as long as the source and author of the quote is stated.

TABLE OF CONTENTS
1. Introduction to the MoPaQ Format
2. The MoPaQ Format
	2.1 General Archive Layout
	2.2 Archive Header
	2.3 Block Table
	2.4 Hash Table
	2.5 File Data
	2.6 Listfile
	2.7 Extended Attributes
	2.8 Weak (Old) Digital Signature
	2.9 Strong (New) Digital Signature
3. Algorithm Source Code
	3.1 Encryption/Decryption
	3.2 Hashing
	3.3 Conversion of FILETIME and time_t

1. INTRODUCTION TO THE MOPAQ FORMAT
The MoPaQ (or MPQ) format is an archive file format designed by Mike O'Brien (hence the name Mike O'brien PaCK) at Blizzard
Entertainment. The format has been used in all Blizzard games since (and including) Diablo. It is heavily optimized to be
a read-only game archive format, and excels at this role. 

The Blizzard MoPaQ-reading functions are contained in the Storm module, which my be either statically or dynamically linked.
The Blizzard MoPaQ-writing functions are contained in the MPQAPI module, which is always statically linked.

2. THE MOPAQ FORMAT
All numbers in the MoPaQ format are in little endian. Data types are listed either as int (integer, the number of bits specified),
byte (8 bits), and char (bytes which contain ASCII characters). All sizes and offsets are in bytes, unless specified otherwise.
Structure members are listed in the following general form:
offset from the beginning of the structure: data type(array size) member name : member description

2.1 GENERAL ARCHIVE LAYOUT
- Archive Header
- File Data
- File Data - Special Files
- Hash Table
- Block Table
- Strong Digital signature

This is the usual archive format, and is not absolutely essential. Some archives have been observed placing the hash table
and file table after the archive header, and before the file data.

2.2 ARCHIVE HEADER
00h: char(4) Magic : Indicates that the file is a MoPaQ archive. Must be ASCII "MPQ" 1Ah.
04h: int32 HeaderSize : Size of the archive header. Should be 32.
08h: int32 ArchiveSize : Size of the whole archive, including the header. Does not include the strong digital signature, if present.
This size is used, among other things, for determining the region to hash in computing the digital signature.
0Ch: int16 Unknown : Unknown
0Eh: int8 SectorSizeShift : Power of two exponent specifying the number of 512-byte disk sectors in each logical sector
in the archive. The size of each logical sector the archive is 512 * 2^SectorSizeShift. Bugs in the Storm library dictate
that this should always be 3 (4096 byte sectors).
10h: int32 HashTableOffset : Offset to the beginning of the hash table, relative to the beginning of the archive.
14h: int32 BlockTableOffset : Offset to the beginning of the block table, relative to the beginning of the archive.
18h: int32 HashTableEntries : Number of entries in the hash table. Must be a power of two, and must be less than 2^16.
1Ch: int32 BlockTableEntries : Number of entries in the block table.

The archive header is the first structure in the archive, at archive offset 0, but the archive does not need to be at offset
0 of the containing file. The offset of the archive in the file is referred to here as ArchiveOffset. If the archive is not
at the beginning of the file, it must begin at a disk sector boundary (512 bytes). Early versions of Storm require that the
archive be at the end of the containing file (ArchiveOffset + ArchiveSize = file size), but this is not required in newer
versions (due to the strong digital signature not being considered a part of the archive).

2.3 BLOCK TABLE
The block table contains entries for each region in the archive. Regions may be either files or empty space, which may be
overwritten by new files (typically this space is from deleted file data). The block table is encrypted, using the hash
of "(block table)" as the key. Each entry is structured as follows:

00h: int32 BlockOffset : Offset of the beginning of the block, relative to the beginning of the archive. Meaningless if the block size is 0.
04h: int32 BlockSize : Size of the block in the archive.
08h: int32 FileSize : Size of the file data stored in the block. Only valid if the block is a file, otherwise meaningless, and should be 0. If the file is compressed, this is the size of the uncompressed file data.
0Ch: int32 Flags : Bit mask of the flags for the block. The following values are conclusively identified:
	80000000h: Block is a file, and follows the file data format; otherwise, block is free space, and may be overwritten. If the block is not a file, all other flags should be cleared.
	01000000h: File is stored as a single unit, rather than split into sectors.
	00020000h: The file's encryption key is adjusted by the block offset and file size (explained in detail in the File Data section). File must be encrypted.
	00010000h: File is encrypted.
	00000200h: File is compressed. Mutually exclusive to file imploded.
	00000100h: File is imploded. Mutually exclusive to file compressed.

2.4 HASH TABLE
Instead of storing file names, for quick access MoPaQs use a fixed, power of two-size hash table of files in the archive. A file is uniquely identified by its file path, its language, and its platform. The home entry for a file in the hash table is computed as a hash of the file path. In the event of a collision (the home entry is occupied by another file), progressive overflow is used, and the file is placed in the next available hash table entry. Searches for a desired file in the hash table proceed from the home entry for the file until either the file is found, the entire hash table is searched, or an empty hash table entry (FileBlockIndex of FFFFFFFFh) is encountered. The hash table is encrypted using the hash of "(hash table)" as the key. Each entry is structured as follows:

00h: int32 FilePathHashA : The hash of the file path, using method A.
04h: int32 FilePathHashB : The hash of the file path, using method B.
08h: int16 Language : The language of the file. This is a Windows LANGID data type, and uses the same values. 0 indicates the default language (American English), or that the file is language-neutral.
0Ah: int8 Platform : The platform the file is used for. 0 indicates the default platform. No other values have been observed.
0Ch: int32 FileBlockIndex : If the hash table entry is valid, this is the index into the block table of the file. Otherwise, one of the following two values:
	FFFFFFFFh: Hash table entry is empty, and has always been empty. Terminates searches for a given file.
	FFFFFFFEh: Hash table entry is empty, but was valid at some point (in other words, the file was deleted). Does not terminate searches for a given file.

2.5 FILE DATA
00h: int32(SectorsInFile + 1) SectorOffsetTable : Offsets to the start of each sector's data, relative to the beginning of the file data. Not present if this information is calculatable (see details below).
immediately following SectorOffsetTable: SectorData : Data of each sector in the file, packed end to end (see details below).

Normally, file data is split up into sectors, for simple streaming. All sectors, save for the last, will contain as many bytes of file data as specified in the archive header's SectorSizeShift; the last sector may be smaller than this, depending on the size of the file data. This sector size is the size of the raw file data; if the file is compressed, the compressed sector will be smaller or the same size as the uncompressed sector size. Individual sectors in a compressed file may be stored uncompressed; this occurs if and only if the sector could not be compressed by the algorithm used (if the compressed sector size was greater than or equal to the size of the raw data), and is indicated by the sector's compressed size in SectorOffsetTable being equal to the uncompressed size of the sector (which may be calculated from the FileSize).

If the sector is compressed (but not imploded), a bit mask byte of the compression algorithm(s) used to compress the sector is appended to the beginning of the compressed sector data. This additional byte counts towards the total size of the sector; if the size of the sector (including this byte) exceeds or matches the uncompressed size of the sector data, the sector will be stored uncompressed, and this byte omitted. Multiple compression algorithms may be used on the same sector; in this case, successive compression occurs in the order the algorithms are listed below, and decompression occurs in the opposite order. For implimentations of all of these algorithms, see StormLib.
	40h: IMA ADPCM mono
	80h: IMA ADPCM stereo
	01h: Huffman encoded
	02h: Deflated (see ZLib)
	08h: Imploded (see PKWare Data Compression Library)
	10h: BZip2 compressed (see BZip2)

If the file is stored as a single unit (indicated in the file's Flags), there is effectively only a single sector, which
contains the entire file.

If the file is encrypted, each sector (after compression and appendage of the compression type byte, if applicable)
is encrypted with the file's key. The base key for a file is determined by a hash of the file name stripped of the
directory (i.e. the key for a file named "directory\file" would be computed as the hash of "file"). If this key is
adjusted, as indicated in the file's Flags, the final key is calculated as ((base key + BlockOffset - ArchiveOffset)
XOR FileSize) (StormLib - an open-source implementation of the MoPaQ reading and writing functions,
by Ladislav Zezula - incorrectly uses an AND in place of the XOR). Each sector is encrypted using the key + the
0-based index of the sector in the file. The SectorOffsetTable, if present, is encrypted using the key - 1.

The SectorOffsetTable is omitted when the sizes and offsets of all sectors in the file are calculatable from the FileSize.
This can happen in several circumstances. If the file is not compressed/imploded, then the size and offset of all sectors
is known, based on the archive's SectorSizeShift. If the file is stored as a single unit compressed/imploded, then the
SectorOffsetTable is omitted, as the single file "sector" corresponds to BlockSize and FileSize, as mentioned previously.
Note that the SectorOffsetTable will always be present if the file is compressed/imploded and the file is not stored as
a single unit, even if there is only a single sector in the file (the size of the file is less than or equal to the
archive's sector size).

2.6 LISTFILE
The listfile is a very simple extension to the MoPaQ format that contains the file paths of (most) files in the archive.
The languages and platforms of the files are not stored in the listfile. The listfile is contained in the file "(listfile)",
and is simply a non-Unix-style text file with one file path on each line, lines terminated with the bytes 0Dh 0Ah. The file
"(listfile)" may not be listed in the listfile.

2.7 EXTENDED ATTRIBUTES
The extended attributes are optional file attributes for files in the block table. These attributes were added at times after
the MoPaQ format was already finalized, and it is not necessary for every archive to have all (or any) of the extended attributes.
If an archive contains a given attribute, there will be an instance of that attribute for every block in the block table, although
the attribute will be meaningless if the block is not a file. The order of the attributes for blocks correspond to the order of the
blocks in the block table, and are of the same number. The attributes are stored in parallel arrays in the "(attributes)" file,
in the archive. The attributes corresponding to this file need not be valid (and logically cannot be). Unlike all the other
structures in the MoPaQ format, entries in the extended attributes are NOT guaranteed to be aligned. Also note that in some
archives, malicious zeroing of the attributes has been observed, perhaps with the intent of breaking archive viewers. This
file is structured as follows:

00h: int32 Version : Specifies the extended attributes format version. For now, must be 100.
04h: int32 AttributesPresent : Bit mask of the extended attributes present in the archive:
	00000001h: File CRC32s.
	00000002h: File timestamps.
	00000004h: File MD5s.
08h: int32(BlockTableEntries) CRC32s : CRC32s of the (uncompressed) file data for each block in the archive. Omitted if the
archive does not have CRC32s. immediately after CRC32s: FILETIME(BlockTableEntries) Timestamps : Timestamps for each block
in the archive. The format is that of the Windows FILETIME structure. Omitted if the archive does not have timestamps.
immediately after Timestamps: MD5(BlockTableEntries) MD5s : MD5s of the (uncompressed) file data for each block in the archive.
Omitted if the archive does not have MD5s.

2.8 WEAK DIGITAL SIGNATURE
The weak digital signature is a digital signature using Microsoft CryptoAPI. It is an implimentation of the RSASSA-PKCS1-v1_5
digital signature protocol, using the MD5 hashing algorithm and a 512-bit (weak) RSA key (for more information about this
protocol, see the RSA Labs PKCS1 specification). The public key and exponent are stored in a resource in Storm. The signature
is stored uncompressed, unencrypted in the file "(signature)" in the archive. The archive is hashed from the beginning of the
archive (ArchiveOffset in the containing file) to the end of the archive (the length indicated by ArchiveSize); the signature
file is added to the archive before signing, and the space occupied by the file is considered to be all binary 0s during
signing/verification. This file is structured as follows:

00h: int32 Unknown : Must be 0.
04h: int32 Unknown : must be 0.
08h: int512 Signature : The digital signature. Like all other numbers in the MoPaQ format, this is stored in little-endian order.

2.9 STRONG DIGITAL SIGNATURE
The strong digital signature uses a simple proprietary implementation of RSA signing, using the SHA-1 hashing algorithm and
a 2048-bit (strong) RSA key. The default public key and exponent are stored in Storm, but other keys may be used as well.
The strong digital signature is stored immediately after the archive, in the containing file; the entire archive (ArchiveSize
bytes, starting at ArchiveOffset in the containing file) is hashed as a single block. The signature has the following format:

00h: char(4) Magic : Indicates the presence of a digital signature. Must be "NGIS" ("SIGN" backwards).
04h: int2048 Signature : The digital signature, stored in little-endian format.

When the Signature field is decrypted with the public key and exponent, and the result stored in little-endian order, it is structured as follows:

00h: byte Padding : Must be 0Bh.
01h: byte(235) Padding : Must be BBh.
ECh: byte(20) SHA-1 : SHA-1 hash of the archive, in standard SHA-1 format.

3. ALGORITHM SOURCE CODE
3.1 ENCRYPTION/DECRYPTION
I believe this was derived at some point from code in StormLib. Assumes the long type to be 32 bits, and the machine to be little endian order.

unsigned long dwCryptTable[0x500];

void InitializeCryptTable()
{
    unsigned long seed   = 0x00100001;
    unsigned long index1 = 0;
    unsigned long index2 = 0;
    int   i;

    for (index1 = 0; index1 < 0x100; index1++)
    {
        for (index2 = index1, i = 0; i < 5; i++, index2 += 0x100)
        {
            unsigned long temp1, temp2;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp1 = (seed & 0xFFFF) << 0x10;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp2 = (seed & 0xFFFF);

            dwCryptTable[index2] = (temp1 | temp2);
        }
    }
}

void EncryptData(void *lpbyBuffer, unsigned long dwLength, unsigned long dwKey)
{
    unsigned long *lpdwBuffer = (unsigned long *)lpbyBuffer;
    unsigned long seed = 0xEEEEEEEE;
    unsigned long ch;

	assert(lpbyBuffer);

    dwLength /= sizeof(unsigned long);

    while(dwLength-- > 0)
    {
        seed += dwCryptTable[0x400 + (dwKey & 0xFF)];
        ch = *lpdwBuffer ^ (dwKey + seed);

        dwKey = ((~dwKey << 0x15) + 0x11111111) | (dwKey >> 0x0B);
        seed = *lpdwBuffer + seed + (seed << 5) + 3;

		*lpdwBuffer++ = ch;
    }
}

void DecryptData(void *lpbyBuffer, unsigned long dwLength, unsigned long dwKey)
{
	unsigned long *lpdwBuffer = (unsigned long *)lpbyBuffer;
    unsigned long seed = 0xEEEEEEEE;
    unsigned long ch;

	assert(lpbyBuffer);

    dwLength /= sizeof(unsigned long);

    while(dwLength-- > 0)
    {
        seed += dwCryptTable[0x400 + (dwKey & 0xFF)];
        ch = *lpdwBuffer ^ (dwKey + seed);

        dwKey = ((~dwKey << 0x15) + 0x11111111) | (dwKey >> 0x0B);
        seed = ch + seed + (seed << 5) + 3;

		*lpdwBuffer++ = ch;
    }
}

3.2 HASHING
Based on code from StormLib.

// Different types of hashes to make with HashString
#define MPQ_HASH_TABLE_OFFSET	0
#define MPQ_HASH_NAME_A	1
#define MPQ_HASH_NAME_B	2
#define MPQ_HASH_FILE_KEY	3

unsigned long HashString(const char *lpszString, unsigned long dwHashType)
{
    unsigned long  seed1 = 0x7FED7FED;
    unsigned long  seed2 = 0xEEEEEEEE;
    int    ch;

    while (*lpszString != 0)
    {
        ch = toupper(*lpszString++);

        seed1 = dwCryptTable[(dwHashType * 0xFF) + ch] ^ (seed1 + seed2);
        seed2 = ch + seed1 + seed2 + (seed2 << 5) + 3;
    }
    return seed1;
}

3.3 CONVERSION OF FILETIME AND time_t

#define EPOCH_OFFSET 116444736000000000ULL	// Number of 100 ns units between 01/01/1601 and 01/01/1970

bool GetTimeFromFileTime(FILETIME &fileTime, time_t &time)
{
	// The FILETIME represents a 64-bit integer: the number of 100 ns units since January 1, 1601
	unsigned long long nTime = ((unsigned long long)fileTime.dwHighDateTime << 32) + fileTime.dwLowDateTime;

	if (nTime < EPOCH_OFFSET)
		return false;

	nTime -= EPOCH_OFFSET;	// Convert the time base from 01/01/1601 to 01/01/1970
	nTime /= 10000000ULL;	// Convert 100 ns to sec

	time = (time_t)nTime;

	// Test for overflow (FILETIME is 64 bits, time_t is 32 bits)
	if ((nTime - (unsigned long long)time) > 0)
		return false;

	return true;
}

void GetFileTimeFromTime(time_t &time, FILETIME &fileTime)
{
	unsigned long long nTime = (unsigned long long)time;

	nTime *= 10000000ULL;
	nTime += EPOCH_OFFSET;

	fileTime.dwLowDateTime = (DWORD)nTime;
	fileTime.dwHighDateTime = (DWORD)(nTime >> 32);
}
THE MOPAQ ARCHIVE FORMAT
v1.0 (Friday, September 1, 2006)
by Justin Olbrantz(Quantam)

Distribution and reproduction of this specification are allowed without limitation, as long as it is not altered. Quotation in other works is freely allowed, as long as the source and author of the quote are stated.

TABLE OF CONTENTS
1. Introduction to the MoPaQ Format
2. The MoPaQ Format
	2.1 General Archive Layout
	2.2 Archive Header
	2.3 Block Table
	2.4 Extended Block Table
	2.5 Hash Table
	2.6 File Data
	2.7 Listfile
	2.8 Extended Attributes
	2.9 Weak (Old) Digital Signature
	2.10 Strong (New) Digital Signature
3. Algorithm Source Code
	3.1 Encryption/Decryption
	3.2 Hashing and File Key Computation
	3.3 Finding Files
	3.4 Deleting Files
	3.5 Conversion of FILETIME and time_t
	3.6 Forming a 64-bit Large Archive Offset from 32-bit and 16-bit Components
4. Revision History

1. INTRODUCTION TO THE MOPAQ FORMAT
The MoPaQ (or MPQ) format is an archive file format designed by Mike O'Brien (hence the name Mike O'brien PaCK) at Blizzard Entertainment. The format has been used in all Blizzard games since (and including) Diablo. It is heavily optimized to be a read-only game archive format, and excels at this role. 

The Blizzard MoPaQ-reading functions are contained in the Storm module, which my be either statically or dynamically linked. The Blizzard MoPaQ-writing functions are contained in the MPQAPI module, which is always statically linked.

StormLib - mentioned several times in this specification - is an open-source MoPaQ reading and writing library written by Ladislav Zezula (no affiliation with Blizzard Entertainment). While it's a bit dated, and does not support all of the newer MoPaQ features, it contains source code to the more exotic compression methods used by MoPaQ, such as the PKWare implode algorithm, MoPaQ's huffman compression algorithm, and the IMA ADPCM compression used by MoPaQ.

2. THE MOPAQ FORMAT
All numbers in the MoPaQ format are in little endian byte order; signed numbers use the two's complement system. Data types are listed either as int (integer, the number of bits specified), byte (8 bits), or char (bytes which contain ASCII characters). All sizes and offsets are in bytes, unless specified otherwise. Structure members are listed in the following general form:
offset from the beginning of the structure: data type(array size) member name : member description

2.1 GENERAL ARCHIVE LAYOUT
- Archive Header
- File Data
- File Data - Special Files
- Hash Table
- Block Table
- Extended Block Table
- Strong Digital signature

This is the usual archive format, but it is not mandatory. Some archives have been observed placing the hash table and file table after the archive header, and before the file data.

2.2 ARCHIVE HEADER
00h: char(4) Magic : Indicates that the file is a MoPaQ archive. Must be ASCII "MPQ" 1Ah.
04h: int32 HeaderSize : Size of the archive header.
08h: int32 ArchiveSize : Size of the whole archive, including the header. Does not include the strong digital signature, if present. This size is used, among other things, for determining the region to hash in computing the digital signature. This field is deprecated in the Burning Crusade MoPaQ format, and the size of the archive is calculated as the size from the beginning of the archive to the end of the hash table, block table, or extended block table (whichever is largest).
0Ch: int16 FormatVersion : MoPaQ format version. MPQAPI will not open archives where this is negative. Known versions:
	0000h: Original format. HeaderSize should be 20h, and large archives are not supported.
	0001h: Burning Crusade format. Header size should be 2Ch, and large archives are supported.
0Eh: int8 SectorSizeShift : Power of two exponent specifying the number of 512-byte disk sectors in each logical sector in the archive. The size of each logical sector in the archive is 512 * 2^SectorSizeShift. Bugs in the Storm library dictate that this should always be 3 (4096 byte sectors).
10h: int32 HashTableOffset : Offset to the beginning of the hash table, relative to the beginning of the archive.
14h: int32 BlockTableOffset : Offset to the beginning of the block table, relative to the beginning of the archive.
18h: int32 HashTableEntries : Number of entries in the hash table. Must be a power of two, and must be less than 2^16 for the original MoPaQ format, or less than 2^20 for the Burning Crusade format.
1Ch: int32 BlockTableEntries : Number of entries in the block table.
Fields only present in the Burning Crusade format and later:
20h: int64 ExtendedBlockTableOffset : Offset to the beginning of the extended block table, relative to the beginning of the archive.
28h: int16 HashTableOffsetHigh : High 16 bits of the hash table offset for large archives.
2Ah: int16 BlockTableOffsetHigh : High 16 bits of the block table offset for large archives.

The archive header is the first structure in the archive, at archive offset 0; however, the archive does not need to be at offset 0 of the containing file. The offset of the archive in the file is referred to here as ArchiveOffset. If the archive is not at the beginning of the file, it must begin at a disk sector boundary (512 bytes). Early versions of Storm require that the archive be at the end of the containing file (ArchiveOffset + ArchiveSize = file size), but this is not required in newer versions (due to the strong digital signature not being considered a part of the archive).

2.3 BLOCK TABLE
The block table contains entries for each region in the archive. Regions may be either files, empty space, which may be overwritten by new files (typically this space is from deleted file data), or unused block table entries. Empty space entries should have BlockOffset and BlockSize nonzero, and FileSize and Flags zero; unused block table entries should have BlockSize, FileSize, and Flags zero. The block table is encrypted, using the hash of "(block table)" as the key. Each entry is structured as follows:

00h: int32 BlockOffset : Offset of the beginning of the block, relative to the beginning of the archive.
04h: int32 BlockSize : Size of the block in the archive.
08h: int32 FileSize : Size of the file data stored in the block. Only valid if the block is a file; otherwise meaningless, and should be 0. If the file is compressed, this is the size of the uncompressed file data.
0Ch: int32 Flags : Bit mask of the flags for the block. The following values are conclusively identified:
	80000000h: Block is a file, and follows the file data format; otherwise, block is free space or unused. If the block is not a file, all other flags should be cleared, and FileSize should be 0.
	01000000h: File is stored as a single unit, rather than split into sectors.
	00020000h: The file's encryption key is adjusted by the block offset and file size (explained in detail in the File Data section). File must be encrypted.
	00010000h: File is encrypted.
	00000200h: File is compressed. File cannot be imploded.
	00000100h: File is imploded. File cannot be compressed.

2.4 EXTENDED BLOCK TABLE
The extended block table was added to support archives larger than 4 gigabytes (2^32 bytes). The table contains the upper bits of the archive offsets for each block in the block table. It is simply an array of int16s, which become bits 32-47 of the archive offsets for each block, with bits 48-63 being zero. Individual blocks in the archive are still limited to 4 gigabytes in size. This table is only present in Burning Crusade format archives that exceed 4 gigabytes size.

As of the Burning Crusade Friends and Family beta, this table is not encrypted.

2.5 HASH TABLE
Instead of storing file names, for quick access MoPaQs use a fixed, power of two-size hash table of files in the archive. A file is uniquely identified by its file path, its language, and its platform. The home entry for a file in the hash table is computed as a hash of the file path. In the event of a collision (the home entry is occupied by another file), progressive overflow is used, and the file is placed in the next available hash table entry. Searches for a desired file in the hash table proceed from the home entry for the file until either the file is found, the entire hash table is searched, or an empty hash table entry (FileBlockIndex of FFFFFFFFh) is encountered. The hash table is encrypted using the hash of "(hash table)" as the key. Each entry is structured as follows:

00h: int32 FilePathHashA : The hash of the file path, using method A.
04h: int32 FilePathHashB : The hash of the file path, using method B.
08h: int16 Language : The language of the file. This is a Windows LANGID data type, and uses the same values. 0 indicates the default language (American English), or that the file is language-neutral.
0Ah: int8 Platform : The platform the file is used for. 0 indicates the default platform. No other values have been observed.
0Ch: int32 FileBlockIndex : If the hash table entry is valid, this is the index into the block table of the file. Otherwise, one of the following two values:
	FFFFFFFFh: Hash table entry is empty, and has always been empty. Terminates searches for a given file.
	FFFFFFFEh: Hash table entry is empty, but was valid at some point (in other words, the file was deleted). Does not terminate searches for a given file.

2.6 FILE DATA
The data for each file is composed of the following structure:
00h: int32(SectorsInFile + 1) SectorOffsetTable : Offsets to the start of each sector, relative to the beginning of the file data. The last entry contains the file size, making it possible to easily calculate the size of any given sector. This table is not present if this information can be calculated (see details below).
immediately following SectorOffsetTable: SECTOR Sectors(SectorsInFile) : Data of each sector in the file, packed end to end (see details below).

Normally, file data is split up into sectors, for simple streaming. All sectors, save for the last, will contain as many bytes of file data as specified in the archive header's SectorSizeShift; the last sector may contain less than this, depending on the size of the entire file's data. If the file is compressed or imploded, the sector will be smaller or the same size as the file data it contains. Individual sectors in a compressed or imploded file may be stored uncompressed; this occurs if and only if the file data the sector contains could not be compressed by the algorithm(s) used (if the compressed sector size was greater than or equal to the size of the file data), and is indicated by the sector's size in SectorOffsetTable being equal to the size of the file data in the sector (which may be calculated from the FileSize). 

The format of each sector depends on the kind of sector it is. Uncompressed sectors are simply the the raw file data contained in the sector. Imploded sectors are the raw compressed data following compression with the implode algorithm (these sectors can only be in imploded files). Compressed sectors (only found in compressed - not imploded - files) are compressed with one or more compression algorithms, and have the following structure:
00h: byte CompressionMask : Mask of the compression types applied to this sector. If multiple compression types are used, they are applied in the order listed below, and decompression is performed in the opposite order. This byte counts towards the total sector size, meaning that the sector will be stored uncompressed if the data cannot be compressed by at least two bytes; as well, this byte is encrypted with the sector data, if applicable. The following compression types are defined (for implementations of these algorithms, see StormLib):
	40h: IMA ADPCM mono
	80h: IMA ADPCM stereo
	01h: Huffman encoded
	02h: Deflated (see ZLib)
	08h: Imploded (see PKWare Data Compression Library)
	10h: BZip2 compressed (see BZip2)
01h: byte(SectorSize - 1) SectorData : The compressed data for the sector.

If the file is stored as a single unit (indicated in the file's Flags), there is effectively only a single sector, which contains the entire file data.

If the file is encrypted, each sector (after compression/implosion, if applicable) is encrypted with the file's key. The base key for a file is determined by a hash of the file name stripped of the directory (i.e. the key for a file named "directory\file" would be computed as the hash of "file"). If this key is adjusted, as indicated in the file's Flags, the final key is calculated as ((base key + BlockOffset - ArchiveOffset) XOR FileSize) (StormLib incorrectly uses an AND in place of the XOR). Each sector is encrypted using the key + the 0-based index of the sector in the file. The SectorOffsetTable, if present, is encrypted using the key - 1.

The SectorOffsetTable is omitted when the sizes and offsets of all sectors in the file are calculatable from the FileSize. This can happen in several circumstances. If the file is not compressed/imploded, then the size and offset of all sectors is known, based on the archive's SectorSizeShift. If the file is stored as a single unit compressed/imploded, then the SectorOffsetTable is omitted, as the single file "sector" corresponds to BlockSize and FileSize, as mentioned previously. However, the SectorOffsetTable will be present if the file is compressed/imploded and the file is not stored as a single unit, even if there is only a single sector in the file (the size of the file is less than or equal to the archive's sector size).

2.7 LISTFILE
The listfile is a very simple extension to the MoPaQ format that contains the file paths of (most) files in the archive. The languages and platforms of the files are not stored in the listfile. The listfile is contained in the file "(listfile)" (default language and platform), and is simply a text file with file paths separated by ';', 0Dh, 0Ah, or some combination of these. The file "(listfile)" may not be listed in the listfile.

2.8 EXTENDED ATTRIBUTES
The extended attributes are optional file attributes for files in the block table. These attributes were added at times after the MoPaQ format was already finalized, and it is not necessary for every archive to have all (or any) of the extended attributes. If an archive contains a given attribute, there will be an instance of that attribute for every block in the block table, although the attribute will be meaningless if the block is not a file. The order of the attributes for blocks correspond to the order of the blocks in the block table, and are of the same number. The attributes are stored in parallel arrays in the "(attributes)" file (default language and platform), in the archive. The attributes corresponding to this file need not be valid (and logically cannot be). Unlike all the other structures in the MoPaQ format, entries in the extended attributes are NOT guaranteed to be aligned. Also note that in some archives, malicious zeroing of the attributes has been observed, perhaps with the intent of breaking archive viewers. This file is structured as follows:

00h: int32 Version : Specifies the extended attributes format version. For now, must be 100.
04h: int32 AttributesPresent : Bit mask of the extended attributes present in the archive:
	00000001h: File CRC32s.
	00000002h: File timestamps.
	00000004h: File MD5s.
08h: int32(BlockTableEntries) CRC32s : CRC32s of the (uncompressed) file data for each block in the archive. Omitted if the archive does not have CRC32s.
immediately after CRC32s: FILETIME(BlockTableEntries) Timestamps : Timestamps for each block in the archive. The format is that of the Windows FILETIME structure. Omitted if the archive does not have timestamps.
immediately after Timestamps: MD5(BlockTableEntries) MD5s : MD5s of the (uncompressed) file data for each block in the archive. Omitted if the archive does not have MD5s.

2.9 WEAK DIGITAL SIGNATURE
The weak digital signature is a digital signature using Microsoft CryptoAPI. It is an implimentation
of the RSASSA-PKCS1-v1_5 digital signature protocol, using the MD5 hashing algorithm and a 512-bit (weak)
RSA key (for more information about this protocol, see the RSA Labs PKCS1 specification). The public key
and exponent are stored in a resource in Storm, the private key is stored in a separate file, whose filename
is passed to MPQAPI (the private key is not stored in MPQAPI). The signature is stored uncompressed,
unencrypted in the file "(signature)" (default language and platform) in the archive. The archive
is hashed from the beginning of the archive (ArchiveOffset in the containing file) to the end of
the archive (the length indicated by ArchiveSize, or calculated in the Burning Crusade MoPaQ format);
the signature file is added to the archive before signing, and the space occupied by the file is considered
to be all binary 0s during signing/verification. This file is structured as follows:

00h: int32 Unknown : Must be 0.
04h: int32 Unknown : Must be 0.
08h: int512 Signature : The digital signature. Like all other numbers in the MoPaQ format, this is stored
in little-endian order. The structure of this, when decrypted, follows the RSASSA-PKCS1-v1_5 specification;
this format is rather icky to work with (I wrote a program to verify this signature using nothing but an MD5
function and huge integer functions; it wasn't pleasant), and best left to an encryption library such as Cryto++.

2.10 STRONG DIGITAL SIGNATURE
The strong digital signature uses a simple proprietary implementation of RSA signing, using the SHA-1 hashing algorithm and a 2048-bit (strong) RSA key. The default public key and exponent are stored in Storm, but other keys may be used as well. The strong digital signature is stored immediately after the archive, in the containing file; the entire archive (ArchiveSize bytes, starting at ArchiveOffset in the containing file) is hashed as a single block. The signature has the following format:

00h: char(4) Magic : Indicates the presence of a digital signature. Must be "NGIS" ("SIGN" backwards).
04h: int2048 Signature : The digital signature, stored in little-endian format.

When the Signature field is decrypted with the public key and exponent, and the resulting large integer is stored in little-endian order, it is structured as follows:

00h: byte Padding : Must be 0Bh.
01h: byte(235) Padding : Must be BBh.
ECh: byte(20) SHA-1 : SHA-1 hash of the archive, in standard SHA-1 byte order.

3. ALGORITHM SOURCE CODE
All of the sample code here assumes little endian machine byte order, that the short type is 16 bits, that the long type is 32 bits, and that the long long type is 64 bits. Adjustments must be made if these assumptions are not correct on a given platform. All code not credited otherwise was written by myself in the writing of this specification.

3.1 ENCRYPTION/DECRYPTION
Based on code from StormLib.

unsigned long dwCryptTable[0x500];

// The encryption and hashing functions use a number table in their procedures. This table must be initialized before the functions are called the first time.
void InitializeCryptTable()
{
    unsigned long seed   = 0x00100001;
    unsigned long index1 = 0;
    unsigned long index2 = 0;
    int   i;

    for (index1 = 0; index1 < 0x100; index1++)
    {
        for (index2 = index1, i = 0; i < 5; i++, index2 += 0x100)
        {
            unsigned long temp1, temp2;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp1 = (seed & 0xFFFF) << 0x10;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp2 = (seed & 0xFFFF);

            dwCryptTable[index2] = (temp1 | temp2);
        }
    }
}

void EncryptData(void *lpbyBuffer, unsigned long dwLength, unsigned long dwKey)
{
    assert(lpbyBuffer);

    unsigned long *lpdwBuffer = (unsigned long *)lpbyBuffer;
    unsigned long seed = 0xEEEEEEEE;
    unsigned long ch;

    dwLength /= sizeof(unsigned long);

    while(dwLength-- > 0)
    {
        seed += dwCryptTable[0x400 + (dwKey & 0xFF)];
        ch = *lpdwBuffer ^ (dwKey + seed);

        dwKey = ((~dwKey << 0x15) + 0x11111111) | (dwKey >> 0x0B);
        seed = *lpdwBuffer + seed + (seed << 5) + 3;

		*lpdwBuffer++ = ch;
    }
}

void DecryptData(void *lpbyBuffer, unsigned long dwLength, unsigned long dwKey)
{
    assert(lpbyBuffer);

    unsigned long *lpdwBuffer = (unsigned long *)lpbyBuffer;
    unsigned long seed = 0xEEEEEEEEL;
    unsigned long ch;

    dwLength /= sizeof(unsigned long);

    while(dwLength-- > 0)
    {
        seed += dwCryptTable[0x400 + (dwKey & 0xFF)];
        ch = *lpdwBuffer ^ (dwKey + seed);

        dwKey = ((~dwKey << 0x15) + 0x11111111L) | (dwKey >> 0x0B);
        seed = ch + seed + (seed << 5) + 3;

		*lpdwBuffer++ = ch;
    }
}

3.2 HASHING AND FILE KEY COMPUTATION
These functions may have been derived from StormLib code at some point in the very distant past. It was so long ago that I don't remember for certain.

// Different types of hashes to make with HashString
#define MPQ_HASH_TABLE_OFFSET	0
#define MPQ_HASH_NAME_A	1
#define MPQ_HASH_NAME_B	2
#define MPQ_HASH_FILE_KEY	3

// Based on code from StormLib.
unsigned long HashString(const char *lpszString, unsigned long dwHashType)
{
    assert(lpszString);
    assert(dwHashType <= MPQ_HASH_FILE_KEY);
    
    unsigned long  seed1 = 0x7FED7FEDL;
    unsigned long  seed2 = 0xEEEEEEEEL;
    int    ch;

    while (*lpszString != 0)
    {
        ch = toupper(*lpszString++);

        seed1 = dwCryptTable[(dwHashType * 0x100) + ch] ^ (seed1 + seed2);
        seed2 = ch + seed1 + seed2 + (seed2 << 5) + 3;
    }
    return seed1;
}

#define BLOCK_OFFSET_ADJUSTED_KEY 0x00020000L

unsigned long ComputeFileKey(const char *lpszFilePath, const BlockTableEntry &blockEntry, unsigned long nArchiveOffset)
{
	assert(lpszFilePath);
	
	// Find the file name part of the path
	const char *lpszFileName = strrchr(lpszFilePath, '\\');
	if (lpszFileName)
		lpszFileName++;	// Skip the \
	else
		lpszFileName = lpszFilePath;
		
	// Hash the name to get the base key
	unsigned long nFileKey = HashString(lpszFileName, MPQ_HASH_FILE_KEY);
	
	// Offset-adjust the key if necessary
	if (blockEntry.Flags & BLOCK_OFFSET_ADJUSTED_KEY)
		nFileKey = (nFileKey + blockEntry.BlockOffset) ^ blockEntry.FileSize;
		
	return nFileKey;
}

3.3 FINDING FILES

#define MPQ_HASH_ENTRY_EMPTY 0xFFFFFFFFL
#define MPQ_HASH_ENTRY_DELETED 0xFFFFFFFEL

bool FindFileInHashTable(const HashTableEntry *lpHashTable, unsigned long nHashTableSize, const char *lpszFilePath, unsigned short nLang, unsigned char nPlatform, unsigned long &iFileHashEntry)
{
	assert(lpHashTable);
	assert(nHashTableSize);
	assert(lpszFilePath);
	
	// Find the home entry in the hash table for the file
	unsigned long iInitEntry = HashString(lpszFilePath, MPQ_HASH_TABLE_OFFSET) & (nHashTableSize - 1);
		
	// Is there anything there at all?
	if (lpHashTable[iInitEntry].FileBlockIndex == MPQ_HASH_ENTRY_EMPTY)
		return false;
		
	// Compute the hashes to compare the hash table entry against
	unsigned long nNameHashA = HashString(lpszFilePath, MPQ_HASH_NAME_A),
		nNameHashB = HashString(lpszFilePath, MPQ_HASH_NAME_B),
		iCurEntry = iInitEntry;
		
	// Check each entry in the hash table till a termination point is reached
	do
	{
		if (lpHashTable[iCurEntry].FileBlockIndex != MPQ_HASH_ENTRY_DELETED)
		{
			if (lpHashTable[iCurEntry].FilePathHashA == nNameHashA 
				&& lpHashTable[iCurEntry].FilePathHashB == nNameHashB
				&& lpHashTable[iCurEntry].Language == nLang
				&& lpHashTable[iCurEntry].Platform == nPlatform)
			{
				iFileHashEntry = iCurEntry;
				
				return true;
			}
		}
			
		iCurEntry = (iCurEntry + 1) & (nHashTableSize - 1);
	} while (iCurEntry != iInitEntry && lpHashTable[iCurEntry].FileBlockIndex != MPQ_HASH_ENTRY_EMPTY);
	
	return false;
}

3.4 DELETING FILES

bool DeleteFile(HashTableEntry *lpHashTable, unsigned long nHashTableSize, BlockTableEntry *lpBlockTable, const char *lpszFilePath, unsigned short nLang, unsigned char nPlatform)
{
	assert(lpHashTable);
	assert(nHashTableSize);
	assert(lpBlockTable);
	
	// Find the file in the hash table
	unsigned long iFileHashEntry;
	
	if (!FindFileInHashTable(lpHashTable, nHashTableSize, lpszFilePath, nLang, nPlatform, iFileHashEntry))
		return false;
	
	// Get the block table index before we nuke the hash table entry
	unsigned long iFileBlockEntry = lpHashTable[iFileHashEntry].FileBlockIndex;
	
	// Delete the file's entry in the hash table
	memset(&lpHashTable[iFileHashEntry], 0xFF, sizeof(HashTableEntry));
	
	// If the next entry is empty, mark this one as empty; otherwise, mark this as deleted.
	if (lpHashTable[(iFileHashEntry + 1) & (nHashTableSize - 1)].FileBlockIndex == MPQ_HASH_ENTRY_EMPTY)
		lpHashTable[iFileHashEntry].FileBlockIndex = MPQ_HASH_ENTRY_EMPTY;
	else
		lpHashTable[iFileHashEntry].FileBlockIndex = MPQ_HASH_ENTRY_DELETED;
	
	// If the block occupies space, mark the block as free space; otherwise, clear the block table entry.
	if (lpBlockTable[iFileBlockEntry].BlockSize > 0)
	{
		lpBlockTable[iFileBlockEntry].FileSize = 0;
		lpBlockTable[iFileBlockEntry].Flags = 0;
	}
	else
		memset(&lpBlockTable[iFileBlockEntry], 0, sizeof(BlockTableEntry);
		
	return true;
}

3.5 CONVERSION OF FILETIME AND time_t
This code assumes that the base ("zero") date for time_t is 01/01/1970. This is true on Windows, Unix System V systems, and Mac OS X. It is unknown whether this is true on all other platforms. You'll need to research this yourself, if you plan on porting it somewhere else.

#define EPOCH_OFFSET 116444736000000000ULL	// Number of 100 ns units between 01/01/1601 and 01/01/1970

bool GetTimeFromFileTime(const FILETIME &fileTime, time_t &time)
{
	// The FILETIME represents a 64-bit integer: the number of 100 ns units since January 1, 1601
	unsigned long long nTime = ((unsigned long long)fileTime.dwHighDateTime << 32) + fileTime.dwLowDateTime;

	if (nTime < EPOCH_OFFSET)
		return false;

	nTime -= EPOCH_OFFSET;	// Convert the time base from 01/01/1601 to 01/01/1970
	nTime /= 10000000ULL;	// Convert 100 ns to sec

	time = (time_t)nTime;

	// Test for overflow (FILETIME is 64 bits, time_t is 32 bits)
	if ((nTime - (unsigned long long)time) > 0)
		return false;

	return true;
}

void GetFileTimeFromTime(const time_t &time, FILETIME &fileTime)
{
	unsigned long long nTime = (unsigned long long)time;

	nTime *= 10000000ULL;
	nTime += EPOCH_OFFSET;

	fileTime.dwLowDateTime = (DWORD)nTime;
	fileTime.dwHighDateTime = (DWORD)(nTime >> 32);
}

3.6 FORMING A 64-BIT LARGE ARCHIVE OFFSET FROM 32-BIT AND 16-BIT COMPONENTS
unsigned long long MakeLargeArchiveOffset(unsigned long nOffsetLow, unsigned short nOffsetHigh)
{
	return ((unsigned long long)nOffsetHigh << 32) + (unsigned long long)nOffsetLow;
}

4. REVISION HISTORY
1.0
	- Updated to include most of the changes found in the Burning Crusade Friends and Family beta

0.91.
	- Updated several structure member descriptions
	- Listed the full set of characters that can separate list file entries
	- Noted that (attributes), (listfile), and (signature) use the default language and platform codes
	- Redid part of the file data specs to clarify the format of sectors
	- Enhanced descriptions of the different kinds of block table entries
	- Added ComputeFileKey, FindFileInHashTable, and DeleteFile sourceTaken from LZMA SDK v 9.11# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

if(UNIX)
  # Look for an installed zlib on unix
  find_package(ZLIB REQUIRED)

  add_library(zlib SHARED IMPORTED GLOBAL)

  set_target_properties(zlib
    PROPERTIES
      IMPORTED_LOCATION
        "${ZLIB_LIBRARIES}"
      INTERFACE_INCLUDE_DIRECTORIES
        "${ZLIB_INCLUDE_DIRS}")
else()
  # Use the bundled source on windows
  SET(zlib_STAT_SRCS
    adler32.c
    compress.c
    crc32.c
    deflate.c
    infback.c
    inffast.c
    inflate.c
    inftrees.c
    trees.c
    uncompr.c
    zutil.c
  )

  add_library(zlib STATIC
    ${zlib_STAT_SRCS})

  target_include_directories(zlib
    PUBLIC
      ${CMAKE_CURRENT_SOURCE_DIR})

  set_target_properties(zlib
      PROPERTIES
        FOLDER
          "dep")
endif()
 The purpose of the CharacterDB cleanup routines is to remove old, non- 
existent and erranous/defunct skills, talents, spells, and achievements 
from characters in the database.

 To achieve this, add an entry (number) in the worldstate-table 
(id:20004), combining the following arguments (bitmasked):

    CLEANING_FLAG_ACHIEVEMENT_PROGRESS  = 0x1
    CLEANING_FLAG_SKILLS                = 0x2
    CLEANING_FLAG_SPELLS                = 0x4
    CLEANING_FLAG_TALENTS               = 0x8
    CLEANING_FLAG_QUESTSTATUS           = 0x10

Example:
 We want to clean up old talents, spells and skills, but leave 
achivements alone - ie. NOT touching those. We'd then need to combine 
the numbers from each of the above fields:

  CLEANING_FLAG_SKILLS + CLEANING_FLAG_SPELLS + CLEANING_FLAG_TALENTS

This comes out as 2+4+8 => 14, and we now put an entry in for this in 
the worldstate table (this is done on the CHARACTERS database) :

  UPDATE worldstates SET value=14 WHERE entry=20004;

This will then (when the core is restarting) clean up old and missing
skills, spells and talents.

Please note that we are not responsible for any issues that might come 
from this, and that you are (as the owner of the database), responsible 
for doing proper backups prior to doing the above in case of anything 
going wrong.

-- The TrinityCore developer team
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.Coding and Pull Requests
-----------

* We generally follow the Sun/Oracle coding standards.
* No tabs; use 4 spaces instead.
* No trailing whitespaces.
* No CRLF line endings, LF only, put your gits 'core.autocrlf' on 'true'.
* The number of commits in a pull request should be kept to a minimum (squish them into one most of the time - use common sense!).
* No merges should be included in pull requests unless the pull request's purpose is a merge.
* Pull requests should be tested (does it compile? AND does it work?) before submission.
* Any major additions should have documentation ready and provided if applicable (this is usually the case).
* Try to follow test driven development where applicable.

-----------
Useful Links
-----------
squashing commits -- http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html/*
 * Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/> 
 * Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
 * Copyright (C) 2005-2019 MaNGOS <http://getmangos.com/>
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 3 of the License, or (at your
 * option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */                     GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
** HOW TO SCRIPT IN C++ **

=========================================================
WARNING: THIS DOCUMENTATION IS NOT ALWAYS UP TO DATE.
FOR MORE UP-TO-DATE INFORMATION, CHECK THE TRINITY WIKI.
=========================================================

1 - create a file myscript.cpp in the scripts/custom folder.
2 - Find the appropriate examples script in the scripts/examples folder and copy its contents.
    Don't forget to rename the classes as appropriate!
3 - Rename the AddSC functions as appropriate.
4 - Make sure to change the initializations in the AddSC function to the appropriate script names!
5 - Under ScriptLoader.cpp, add your AddSC function near the top and in AddCustomScripts(), call it.
6 - Add your myscript.cpp file to the scripts CMakeLists.txt: under: set(scripts_STAT_SRCS add: Custom/myscript.cpp
7 - Redefine the virtual functions you want to override in your script.
8 - If the script you are writing is database bound, add the scriptname to the appropriate location in the database.
9 - Recompile and restart the server, and your script should be up and running.
Logging system "log4j-like"

--- LOGGERS AND APPENDERS ---

Logging system has two components: loggers and appenders. These types of
components enable users to log messages according to message type and level and
control at runtime where they are reported.

LOGGERS

The first and foremost advantage of this system resided in the ability to
disable certain log statements while allowing others to print unhindered.
This capability assumes that the loggers are categorized according to some
developer-chosen criteria.

Loggers are named entitites. Logger names are case-sensitive and they follow
the hierarchical naming rule:

    A Logger is said to be an ancestor of another logger if its name followed
    by a dot is a prefix of the descendant logger name. A logger is salid to be
    a parent of a child logger if there are no ancestors between itself and the
    descendant logger.

For example, the logger named "entities.player" is a parent of the logger named
"entities.player.character". Similarly, "entities" is a parent of "entities.player"
and an ancestor of "entities.player.character".

Loggers may be assigned levels. The set of possible levels are TRACE, DEBUG,
INFO, WARN, ERROR AND FATAL, or be disabled using level DISABLED.

By definition the printing method determines the level of a logging request.
For example, TC_LOG_INFO(...) is a logging request of level INFO.

A logging request is said to be enabled if its level is higher than or equal to
the level of its logger. Otherwise, the request is said to be disabled. A logger
without an assigned level will inherit one from the hierarchy

Example
Logger Name        Assigned Level      Inherited Level
root               Proot               Proot
server             None                Proot

As "server" is not defined, it uses the root logger and it's log level.
TRACE < DEBUG < INFO < WARN < ERROR < FATAL.


APPENDERS

The ability to selectively enable of dissable logging request based on their
loggers is only part of the picture. This system allows logging requests to
print to multiple destinations. An output destination is called an appender.
Current system defines appenders for Console, files and Database, but can be
easily extended to remote socket server, NT event loggers, syslog daemons or
any other system.

More than one appender can be attached to one logger. Each enabled logging
request for a given logger will be forwarded to all the appenders in that
logger


CONFIGURATION

System will read all config elements with prefix "Logger." and "Appender."
and configure the logging system. If "root" can not be properly configured the core
will remove all loggers and appenders and create a default set:
- Logger "root" with log level Error
- Logger "server" with log level Info
- Appender "Console" to log to console


Appender config line follows the format:

    Type,LogLevel,Flags,optional1,optional2

Its a list of elements separated by comma where each element has its own meaning
    Type: Type of the appender
        1 - (Console)
        2 - (File)
        3 - (DB)
    LogLevel: Log level
        0 - (Disabled)
        1 - (Trace)
        2 - (Debug)
        3 - (Info)
        4 - (Warn)
        5 - (Error)
        6 - (Fatal)
    Flags: Define some extra modifications to do to logging message
        1 - Prefix Timestamp to the text
        2 - Prefix Log Level to the text
        4 - Prefix Log Filter type to the text
        8 - Append timestamp to the log file name. Format: YYYY-MM-DD_HH-MM-SS
            (Only used with Type = 2)
       16 - Make a backup of existing file before overwrite
            (Only used with Mode = w)

Depending on the type, elements optional1 and optional2 will take different

    Colors (read as optional1 if Type = Console)
        Format: "fatal error warn info debug trace"
        0 - BLACK
        1 - RED
        2 - GREEN
        3 - BROWN
        4 - BLUE
        5 - MAGENTA
        6 - CYAN
        7 - GREY
        8 - YELLOW
        9 - LRED
       10 - LGREEN
       11 - LBLUE
       12 - LMAGENTA
       13 - LCYAN
       14 - WHITE
        Example: "13 11 9 5 3 1"

    File: Name of the file (read as optional1 if Type = File)
        Allows to use one "%u" to create dynamic files

    Mode: Mode to open the file (read as optional2 if Type = File)
        a - (Append)
        w - (Overwrite)

Example:
    Appender.Console1=1,2,6

    Creates new appender to log to console any message with log level DEBUG
    or higher and prefixes log type and level to the message.

    Appender.Console2=1,5,1,13 11 9 5 3 1

    Creates new appender to log to console any message with log level ERROR
    or higher and prefixes timestamp to the message using colored text.

    Appender.File=2,2,7,Auth.log,w

    Creates new appender to log to file "Auth.log" any message with log level
    DEBUG or higher and prefixes timestamp, type and level to message

In the example, having two different loggers to log to console is perfectly
legal but redundant.

Once we have the list of loggers to read, system will try to configure a new
logger from its config line. Logger config line follows the format:

    LogLevel,AppenderList

Its a list of elements separated by comma where each element has its own meaning
    LogLevel
        0 - (Disabled)
        1 - (Trace)
        2 - (Debug)
        3 - (Info)
        4 - (Warn)
        5 - (Error)
        6 - (Fatal)
    AppenderList: List of appenders linked to logger
    (Using spaces as separator).

--- EXAMPLES ---

EXAMPLE 1

Log errors to console and a file called server.log that only contain
logs for this server run. File should prefix timestamp, type and log level to
the messages. Console should prefix type and log level.

    Appender.Console=1,5,6
    Appender.Server=2,5,7,Server.log,w
    Logger.root=5,Console Server

Lets trace how system will log two different messages:
    1) TC_LOG_ERROR(LOG_FILTER_GUILD, "Guild 1 created");
    System will try to find logger of type GUILD, as no logger is configured
    for GUILD it will use Root logger. As message Log Level is equal or higher
    than the Log level of logger the message is sent to the Appenders
    configured in the Logger. "Console" and "Server".
    Console will write: "ERROR [GUILD     ] Guild 1 created"
    Server will write to file "2012-08-15 ERROR [GUILD     ] Guild 1 created"

    2) TC_LOG_INFO(LOG_FILTER_CHARACTER, "Player Name Logged in");
    System will try to find logger of type CHARACTER, as no logger is
    configured for CHARACTER it will use Root logger. As message Log Level is
    not equal or higher than the Log level of logger the message its discarted.

EXAMPLE 2

Same example that above, but now i want to see all messages of level INFO on
file and server file should add timestamp on creation.

    Appender.Console=1,5,6
    Appender.Server=2,4,15,Server.log
    Logger.root=4,Console Server

Lets trace how system will log two different messages:
    1) TC_LOG_ERROR(LOG_FILTER_GUILD, "Guild 1 created");
    Performs exactly as example 1.
    2) TC_LOG_INFO(LOG_FILTER_CHARACTER, "Player Name Logged in");
    System will try to find logger of type CHARACTER, as no logger is
    configured for CHARACTER it will use Root logger. As message Log Level is
    equal or higher than the Log level of logger the message is sent to the
    Appenders configured in the Logger. "Console" and "Server".
    Console will discard msg as Log Level is not higher or equal to this
    appender
    Server will write to file
    "2012-08-15 INFO [CHARACTER ] Player Name Logged in"

EXAMPLE 3
As a dev, i may be interested in logging just a particular part of the core
while i'm trying to fix something. So... i want to debug GUILDS to maximum
and also some CHARACTER events to some point. Also im checking some Waypoints
so i want SQLDEV to be logged to file without prefixes. All other messages
should only be logged to console, GUILD to TRACE and CHARACTER to INFO

    Appender.Console=1,1
    Appender.SQLDev=2,2,0,SQLDev.log
    Logger.guild=1,Console
    Logger.entities.player.character=3,Console
    Logger.sql.dev=3,SQLDev

With this config, any message logger with a Log type different to GUILD,
CHARACTER or SQLDEV will be ignored, as we didn't define a logger Root and
system created a default Root disabled. Appender Console, log level should be
defined to allow all possible messages of its loggers, in this case GUILD uses
TRACE (1), so Appender should allow it. Logger Characters will limit it's own
messages to INFO (3)
= TrinityCore -- Linux installation =
Copyright (C) 2008-2013 TrinityCore (http://www.trinitycore.org)

=========================================================
WARNING: THIS DOCUMENTATION IS NOT ALWAYS UP TO DATE.
FOR MORE UP-TO-DATE INFORMATION, CHECK THE TRINITY WIKI.
=========================================================

CHECK http://www.trinitycore.info/How-to:Linux FOR FURTHER HELP

These are instructions for installation in a Linux environment, if you are
using Windows refer to http://www.trinitycore.info/How-to:Win

Installing TrinityCore is fairly simple on a Linux machine, assuming you 
have all required applications

The most important ones are:

    g++
    gcc version 4.3.x or greater
    make
    cmake version 2.6.x or greater
    libmysql++-dev
    git (for checking out the core and database)
    openssl
    libssl-dev
    zlib1g-dev
    libtool
    libmysqlclient15-dev
    patch
    build-essential
    mysql-client
    
Most of these are included on common Linux distros, others you may have 
to install by your self. Please check your distro's repos.

Make a directory to build in, you can call it anything you want like 
build or bin etc, then go into the directory and cmake and make. E.G. 
you created a dir named build ad want to have your finalcompiled product 
installed in /home/trinity/server, an example sequence of commands can 
be :

    cmake ../ -DPREFIX=/home/trinity/server -DTOOLS=1 -DWITH_WARNINGS=1
    make
    make install
    
Thats just about all thats needed. You can however tweak more settings 
than where to install using flags built into our cmake files. Just open 
up CMakeLists.txt in the main folder and take a look at some of the 
flags like

    SERVERS             Build worldserver and authserver
    SCRIPTS             Build core with scripts included
    TOOLS               Build map/vmap extraction/assembler tools
    USE_SCRIPTPCH       Use precompiled headers when compiling scripts
    USE_COREPCH         Use precompiled headers when compiling servers
    WITH_WARNINGS       Show all warnings during compile
    WITH_COREDEBUG      Include additional debug-code in core
    PREFIX              Set installation directory
    NOJEM               Do not build with jemalloc (advanced users only)
    CONF_DIR            Set path as default configuration directory
    LIBSDIR             Set path as default library directory
    CMAKE_C_FLAGS       Set C_FLAGS for compile (advanced users only)
    CMAKE_CXX_FLAGS     Set CXX_FLAGS for compile (advanced users only)
    CMAKE_BUILD_TYPE    Set buildtype - the supported modes are :
                        Release, MinSizeRel, RelWithDebInfo, Debug

Of course, replace the paths in PREFIX, CONF_DIR and LIBSDIR with the
directories you wish to install TrinityCore to. The datadir is where maps,
DBCs, and SQLs are stored. The sysconfdir is where configuration files are stored.

Once TrinityCore is installed you will need to apply database updates 
where necessary. Furthermore, you must configure your installation by 
editing the config files in the sysconfdir.
auth Updates.characters Updates.World Updates.# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

add_subdirectory(genrev)
add_subdirectory(server)

if(TOOLS)
  add_subdirectory(tools)
endif(TOOLS)

# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# Need to pass old ${CMAKE_BINARY_DIR} as param because its different at build stage
add_custom_target(revision.h ALL
  COMMAND ${CMAKE_COMMAND} -DNO_GIT=${WITHOUT_GIT} -DGIT_EXEC=${GIT_EXECUTABLE} -DBUILDDIR=${CMAKE_BINARY_DIR} -P ${CMAKE_SOURCE_DIR}/cmake/genrev.cmake
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

if(CMAKE_COMPILER_IS_GNUCXX AND NOT MINGW)
  add_definitions(-fno-delete-null-pointer-checks)
endif()

if( SERVERS )
  set(sources_windows_Debugging
    ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging/WheatyExceptionReport.cpp
    ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging/WheatyExceptionReport.h
  )
  add_subdirectory(shared)
  add_subdirectory(game)
  add_subdirectory(collision)
  add_subdirectory(authserver)
  add_subdirectory(scripts)
  add_subdirectory(worldserver)
else()
  if( TOOLS )
    add_subdirectory(shared)
    add_subdirectory(collision)
  endif()
endif()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

########### authserver ###############

file(GLOB_RECURSE sources_Authentication Authentication/*.cpp Authentication/*.h)
file(GLOB_RECURSE sources_Realms Realms/*.cpp Realms/*.h)
file(GLOB_RECURSE sources_Server Server/*.cpp Server/*.h)
file(GLOB sources_Localdir *.cpp *.h)

source_group(CMake FILES CMakeLists.txt)
source_group(Authentication FILES ${sources_Authentication})
source_group(Realms FILES ${sources_Realms})
source_group(Server FILES ${sources_Server})
source_group(localdir FILES ${sources_Localdir})

if (USE_COREPCH)
  set(authserver_PCH_HDR PrecompiledHeaders/authPCH.h)
  set(authserver_PCH_SRC PrecompiledHeaders/authPCH.cpp)
endif()

set(authserver_SRCS
  ${authserver_SRCS}
  ${sources_Authentication}
  ${sources_Realms}
  ${sources_Server}
  ${sources_Localdir}
)

if( WIN32 )
  set(authserver_SRCS
    ${authserver_SRCS}
    ${sources_windows_Debugging}
  )
  if ( MSVC )
    set(authserver_SRCS
      ${authserver_SRCS}
      authserver.rc
    )
  endif ()
endif()

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Database
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Packets
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography/Authentication
  ${CMAKE_SOURCE_DIR}/src/server/shared/Logging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Threading
  ${CMAKE_SOURCE_DIR}/src/server/shared/Utilities
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/Authentication
  ${CMAKE_CURRENT_SOURCE_DIR}/Realms
  ${CMAKE_CURRENT_SOURCE_DIR}/Server
  ${ACE_INCLUDE_DIR}
  ${MYSQL_INCLUDE_DIR}
  ${OPENSSL_INCLUDE_DIR}
)

add_executable(authserver
  ${authserver_SRCS}
  ${authserver_PCH_SRC}
)

add_dependencies(authserver revision.h)

if( NOT WIN32 )
  set_target_properties(authserver PROPERTIES
    COMPILE_DEFINITIONS _SKYFIRE_REALM_CONFIG="${CONF_DIR}/authserver.conf"
  )
endif()

target_link_libraries(authserver
  shared
  ${MYSQL_LIBRARY}
  ${OPENSSL_LIBRARIES}
  ${CMAKE_THREAD_LIBS_INIT}
  ${ACE_LIBRARY}
)

if( WIN32 )
  if ( MSVC )
    add_custom_command(TARGET authserver
      POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/authserver.conf.dist ${CMAKE_BINARY_DIR}/bin/$(ConfigurationName)/
    )
  elseif ( MINGW )
    add_custom_command(TARGET authserver
      POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/authserver.conf.dist ${CMAKE_BINARY_DIR}/bin/
    )
  endif()
endif()

if( UNIX )
  install(TARGETS authserver DESTINATION bin)
  install(FILES  authserver.conf.dist DESTINATION ${CONF_DIR})
elseif( WIN32 )
  install(TARGETS authserver DESTINATION "${CMAKE_INSTALL_PREFIX}")
  install(FILES authserver.conf.dist DESTINATION "${CMAKE_INSTALL_PREFIX}")
endif()

# Generate precompiled header
if (USE_COREPCH)
  add_cxx_pch(authserver ${authserver_PCH_HDR} ${authserver_PCH_SRC})
endif()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

if( USE_COREPCH )
  include_directories(${CMAKE_CURRENT_BINARY_DIR})
endif()

file(GLOB_RECURSE sources_Management Management/*.cpp Management/*.h)
file(GLOB_RECURSE sources_Maps Maps/*.cpp Maps/*.h)
file(GLOB_RECURSE sources_Models Models/*.cpp Models/*.h)
file(GLOB sources_localdir *.cpp *.h)

if (USE_COREPCH)
  set(collision_STAT_PCH_HDR PrecompiledHeaders/collisionPCH.h)
  set(collision_STAT_PCH_SRC PrecompiledHeaders/collisionPCH.cpp)
endif ()

set(collision_STAT_SRCS
  ${collision_STAT_SRCS}
  ${sources_Management}
  ${sources_Maps}
  ${sources_Models}
  ${sources_localdir}
)

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_SOURCE_DIR}/dep/g3dlite/include
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Detour
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Configuration
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Database
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic/LinkedReference
  ${CMAKE_SOURCE_DIR}/src/server/shared/Logging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Threading
  ${CMAKE_SOURCE_DIR}/src/server/shared/Packets
  ${CMAKE_SOURCE_DIR}/src/server/shared/Utilities
  ${CMAKE_SOURCE_DIR}/src/server/shared/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/game/Addons
  ${CMAKE_SOURCE_DIR}/src/server/game/Conditions
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Item
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/GameObject
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Creature
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object/Updates
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Unit
  ${CMAKE_SOURCE_DIR}/src/server/game/Combat
  ${CMAKE_SOURCE_DIR}/src/server/game/Loot
  ${CMAKE_SOURCE_DIR}/src/server/game/Miscellaneous
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids/Cells
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids/Notifiers
  ${CMAKE_SOURCE_DIR}/src/server/game/Maps
  ${CMAKE_SOURCE_DIR}/src/server/game/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/Waypoints
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/Spline
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement
  ${CMAKE_SOURCE_DIR}/src/server/game/Server
  ${CMAKE_SOURCE_DIR}/src/server/game/Server/Protocol
  ${CMAKE_SOURCE_DIR}/src/server/game/World
  ${CMAKE_SOURCE_DIR}/src/server/game/Spells
  ${CMAKE_SOURCE_DIR}/src/server/game/Spells/Auras
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/Management
  ${CMAKE_CURRENT_SOURCE_DIR}/Maps
  ${CMAKE_CURRENT_SOURCE_DIR}/Models
  ${ACE_INCLUDE_DIR}
  ${MYSQL_INCLUDE_DIR}
)

add_library(collision STATIC
  ${collision_STAT_SRCS}
  ${collision_STAT_PCH_SRC}
)

target_link_libraries(collision
  shared
)

# Generate precompiled header
if (USE_COREPCH)
  add_cxx_pch(collision ${collision_STAT_PCH_HDR} ${collision_STAT_PCH_SRC})
endif ()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB_RECURSE sources_Accounts Accounts/*.cpp Accounts/*.h)
file(GLOB_RECURSE sources_Achievements Achievements/*.cpp Achievements/*.h)
file(GLOB_RECURSE sources_Addons Addons/*.cpp Addons/*.h)
file(GLOB_RECURSE sources_AI AI/*.cpp AI/*.h)
file(GLOB_RECURSE sources_AuctionHouse AuctionHouse/*.cpp AuctionHouse/*.h)
file(GLOB_RECURSE sources_Battlefield Battlefield/*.cpp Battlefield/*.h)
file(GLOB_RECURSE sources_Battlegrounds Battlegrounds/*.cpp Battlegrounds/*.h)
file(GLOB_RECURSE sources_BattlePet BattlePet/*.cpp BattlePet/*.h)
file(GLOB_RECURSE sources_Boost Boost/*.cpp Boost/*.h)
file(GLOB_RECURSE sources_BlackMarket BlackMarket/*.cpp BlackMarket/*.h)
file(GLOB_RECURSE sources_Calendar Calendar/*.cpp Calendar/*.h)
file(GLOB_RECURSE sources_Chat Chat/*.cpp Chat/*.h)
file(GLOB_RECURSE sources_Combat Combat/*.cpp Combat/*.h)
file(GLOB_RECURSE sources_Conditions Conditions/*.cpp Conditions/*.h)
file(GLOB_RECURSE sources_DataStores DataStores/*.cpp DataStores/*.h)
file(GLOB_RECURSE sources_DungeonFinding DungeonFinding/*.cpp DungeonFinding/*.h)
file(GLOB_RECURSE sources_Entities Entities/*.cpp Entities/*.h)
file(GLOB_RECURSE sources_Events Events/*.cpp Events/*.h)
file(GLOB_RECURSE sources_Globals Globals/*.cpp Globals/*.h)
file(GLOB_RECURSE sources_Grids Grids/*.cpp Grids/*.h)
file(GLOB_RECURSE sources_Groups Groups/*.cpp Groups/*.h)
file(GLOB_RECURSE sources_Guilds Guilds/*.cpp Guilds/*.h)
file(GLOB_RECURSE sources_Handlers Handlers/*.cpp Handlers/*.h)
file(GLOB_RECURSE sources_Instances Instances/*.cpp Instances/*.h)
file(GLOB_RECURSE sources_Loot Loot/*.cpp Loot/*.h)
file(GLOB_RECURSE sources_Mails Mails/*.cpp Mails/*.h)
file(GLOB_RECURSE sources_Maps Maps/*.cpp Maps/*.h)
file(GLOB_RECURSE sources_Miscellaneous Miscellaneous/*.cpp Miscellaneous/*.h)
file(GLOB_RECURSE sources_Movement Movement/*.cpp Movement/*.h)
file(GLOB_RECURSE sources_OutdoorPvP OutdoorPvP/*.cpp OutdoorPvP/*.h)
file(GLOB_RECURSE sources_Pools Pools/*.cpp Pools/*.h)
file(GLOB_RECURSE sources_Quests Quests/*.cpp Quests/*.h)
file(GLOB_RECURSE sources_Reputation Reputation/*.cpp Reputation/*.h)
file(GLOB_RECURSE sources_Scripting Scripting/*.cpp Scripting/*.h)
file(GLOB_RECURSE sources_Server Server/*.cpp Server/*.h)
file(GLOB_RECURSE sources_Skills Skills/*.cpp Skills/*.h)
file(GLOB_RECURSE sources_Spells Spells/*.cpp Spells/*.h)
file(GLOB_RECURSE sources_Texts Texts/*.cpp Texts/*.h)
file(GLOB_RECURSE sources_Tools Tools/*.cpp Tools/*.h)
file(GLOB_RECURSE sources_Tickets Tickets/*.cpp Tickets/*.h)
file(GLOB_RECURSE sources_Warden Warden/*.cpp Warden/*.h)
file(GLOB_RECURSE sources_Weather Weather/*.cpp Weather/*.h)
file(GLOB_RECURSE sources_World World/*.cpp World/*.h)

source_group(CMake FILES CMakeLists.txt)
source_group(Accounts FILES ${sources_Accounts})
source_group(Achievements FILES ${sources_Achievements})
source_group(Addons FILES ${sources_Addons})
source_group(AI FILES ${sources_AI})
source_group(AuctionHouse FILES ${sources_AuctionHouse})
source_group(Battlefield FILES ${sources_Battlefield})
source_group(Battlegrounds FILES ${sources_Battlegrounds})
source_group(BattlePet FILES ${sources_BattlePet})
source_group(Boost FILES ${sources_Boost})
source_group(BlackMarket FILES ${sources_BlackMarket})
source_group(Calendar FILES ${sources_Calendar})
source_group(Chat FILES ${sources_Chat})
source_group(Combat FILES ${sources_Combat})
source_group(Conditions FILES ${sources_Conditions})
source_group(DataStores FILES ${sources_DataStores})
source_group(DungeonFinding FILES ${sources_DungeonFinding})
source_group(Entities FILES ${sources_Entities})
source_group(Events FILES ${sources_Events})
source_group(Globals FILES ${sources_Globals})
source_group(Grids FILES ${sources_Grids})
source_group(Groups FILES ${sources_Groups})
source_group(Guilds FILES ${sources_Guilds})
source_group(Handlers FILES ${sources_Handlers})
source_group(Instances FILES ${sources_Instances})
source_group(Loot FILES ${sources_Loot})
source_group(Mails FILES ${sources_Mails})
source_group(Maps FILES ${sources_Maps})
source_group(Miscellaneous FILES ${sources_Miscellaneous})
source_group(Movement FILES ${sources_Movement})
source_group(OutdoorPvP FILES ${sources_OutdoorPvP})
source_group(Pools FILES ${sources_Pools})
source_group(Quests FILES ${sources_Quests})
source_group(Reputation FILES ${sources_Reputation})
source_group(Scripting FILES ${sources_Scripting})
source_group(Server FILES ${sources_Server})
source_group(Skills FILES ${sources_Skills})
source_group(Spells FILES ${sources_Spells})
source_group(Texts FILES ${sources_Texts})
source_group(Tools FILES ${sources_Tools})
source_group(Tickets FILES ${sources_Tickets})
source_group(Warden FILES ${sources_Warden})
source_group(Weather FILES ${sources_Weather})
source_group(World FILES ${sources_World})
# Create game-libary

if (USE_COREPCH)
  set(game_STAT_PCH_HDR PrecompiledHeaders/gamePCH.h)
  set(game_STAT_PCH_SRC PrecompiledHeaders/gamePCH.cpp)
endif ()

set(game_STAT_SRCS
  ${game_STAT_SRCS}
  ${sources_Accounts}
  ${sources_Achievements}
  ${sources_Addons}
  ${sources_AI}
  ${sources_AuctionHouse}
  ${sources_Battlefield}
  ${sources_Battlegrounds}
  ${sources_BattlePet}
  ${sources_Boost}
  ${sources_BlackMarket}
  ${sources_Calendar}
  ${sources_Chat}
  ${sources_Combat}
  ${sources_Conditions}
  ${sources_DataStores}
  ${sources_DungeonFinding}
  ${sources_Entities}
  ${sources_Events}
  ${sources_Globals}
  ${sources_Grids}
  ${sources_Groups}
  ${sources_Guilds}
  ${sources_Handlers}
  ${sources_Instances}
  ${sources_Loot}
  ${sources_Mails}
  ${sources_Maps}
  ${sources_Miscellaneous}
  ${sources_Movement}
  ${sources_OutdoorPvP}
  ${sources_Pools}
  ${sources_Quests}
  ${sources_Reputation}
  ${sources_Scripting}
  ${sources_Server}
  ${sources_Skills}
  ${sources_Spells}
  ${sources_Texts}
  ${sources_Tools}
  ${sources_Tickets}
  ${sources_Warden}
  ${sources_Weather}
  ${sources_World}
)

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Detour
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Recast
  ${CMAKE_SOURCE_DIR}/dep/g3dlite/include
  ${CMAKE_SOURCE_DIR}/dep/SFMT
  ${CMAKE_SOURCE_DIR}/dep/zlib
  ${CMAKE_SOURCE_DIR}/src/server/collision
  ${CMAKE_SOURCE_DIR}/src/server/collision/Management
  ${CMAKE_SOURCE_DIR}/src/server/collision/Models
  ${CMAKE_SOURCE_DIR}/src/server/collision/Maps
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Configuration
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography/Authentication
  ${CMAKE_SOURCE_DIR}/src/server/shared/Database
  ${CMAKE_SOURCE_DIR}/src/server/shared/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic/LinkedReference
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic
  ${CMAKE_SOURCE_DIR}/src/server/shared/Logging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Packets
  ${CMAKE_SOURCE_DIR}/src/server/shared/Threading
  ${CMAKE_SOURCE_DIR}/src/server/shared/Utilities
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/Accounts
  ${CMAKE_CURRENT_SOURCE_DIR}/Achievements
  ${CMAKE_CURRENT_SOURCE_DIR}/Addons
  ${CMAKE_CURRENT_SOURCE_DIR}/AI
  ${CMAKE_CURRENT_SOURCE_DIR}/AI/CoreAI
  ${CMAKE_CURRENT_SOURCE_DIR}/AI/ScriptedAI
  ${CMAKE_CURRENT_SOURCE_DIR}/AI/SmartScripts
  ${CMAKE_CURRENT_SOURCE_DIR}/AuctionHouse
  ${CMAKE_CURRENT_SOURCE_DIR}/Battlefield
  ${CMAKE_CURRENT_SOURCE_DIR}/Battlefield/Zones
  ${CMAKE_CURRENT_SOURCE_DIR}/Battlegrounds
  ${CMAKE_CURRENT_SOURCE_DIR}/Battlegrounds/Zones
  ${CMAKE_CURRENT_SOURCE_DIR}/BattlePet
  ${CMAKE_CURRENT_SOURCE_DIR}/Boost
  ${CMAKE_CURRENT_SOURCE_DIR}/BlackMarket
  ${CMAKE_CURRENT_SOURCE_DIR}/Calendar
  ${CMAKE_CURRENT_SOURCE_DIR}/Chat
  ${CMAKE_CURRENT_SOURCE_DIR}/Chat/Channels
  ${CMAKE_CURRENT_SOURCE_DIR}/Combat
  ${CMAKE_CURRENT_SOURCE_DIR}/Conditions
  ${CMAKE_CURRENT_SOURCE_DIR}/DataStores
  ${CMAKE_CURRENT_SOURCE_DIR}/DungeonFinding
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/AreaTrigger
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Creature
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Corpse
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/DynamicObject
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/GameObject
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Item
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Item/Container
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Object
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Object/Updates
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Pet
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Player
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Totem
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Unit
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Vehicle
  ${CMAKE_CURRENT_SOURCE_DIR}/Entities/Transport
  ${CMAKE_CURRENT_SOURCE_DIR}/Events
  ${CMAKE_CURRENT_SOURCE_DIR}/Globals
  ${CMAKE_CURRENT_SOURCE_DIR}/Grids/Cells
  ${CMAKE_CURRENT_SOURCE_DIR}/Grids/Notifiers
  ${CMAKE_CURRENT_SOURCE_DIR}/Grids
  ${CMAKE_CURRENT_SOURCE_DIR}/Groups
  ${CMAKE_CURRENT_SOURCE_DIR}/Guilds
  ${CMAKE_CURRENT_SOURCE_DIR}/Handlers
  ${CMAKE_CURRENT_SOURCE_DIR}/Instances
  ${CMAKE_CURRENT_SOURCE_DIR}/Loot
  ${CMAKE_CURRENT_SOURCE_DIR}/Mails
  ${CMAKE_CURRENT_SOURCE_DIR}/Maps
  ${CMAKE_CURRENT_SOURCE_DIR}/Miscellaneous
  ${CMAKE_CURRENT_SOURCE_DIR}/Movement
  ${CMAKE_CURRENT_SOURCE_DIR}/Movement/Spline
  ${CMAKE_CURRENT_SOURCE_DIR}/Movement/MovementGenerators
  ${CMAKE_CURRENT_SOURCE_DIR}/Movement/Waypoints
  ${CMAKE_CURRENT_SOURCE_DIR}/OutdoorPvP
  ${CMAKE_CURRENT_SOURCE_DIR}/Pools
  ${CMAKE_CURRENT_SOURCE_DIR}/PrecompiledHeaders
  ${CMAKE_CURRENT_SOURCE_DIR}/Quests
  ${CMAKE_CURRENT_SOURCE_DIR}/Reputation
  ${CMAKE_CURRENT_SOURCE_DIR}/Scripting
  ${CMAKE_CURRENT_SOURCE_DIR}/Server/Protocol
  ${CMAKE_CURRENT_SOURCE_DIR}/Server
  ${CMAKE_CURRENT_SOURCE_DIR}/Skills
  ${CMAKE_CURRENT_SOURCE_DIR}/Spells
  ${CMAKE_CURRENT_SOURCE_DIR}/Spells/Auras
  ${CMAKE_CURRENT_SOURCE_DIR}/Texts
  ${CMAKE_CURRENT_SOURCE_DIR}/Tools
  ${CMAKE_CURRENT_SOURCE_DIR}/Tickets
  ${CMAKE_CURRENT_SOURCE_DIR}/Warden
  ${CMAKE_CURRENT_SOURCE_DIR}/Warden/Modules
  ${CMAKE_CURRENT_SOURCE_DIR}/Weather
  ${CMAKE_CURRENT_SOURCE_DIR}/World
  ${ACE_INCLUDE_DIR}
  ${MYSQL_INCLUDE_DIR}
  ${OPENSSL_INCLUDE_DIR}
)

add_library(game STATIC
  ${game_STAT_SRCS}
  ${game_STAT_PCH_SRC}
)

add_dependencies(game revision.h)

# Generate precompiled header
if (USE_COREPCH)
  add_cxx_pch(game ${game_STAT_PCH_HDR} ${game_STAT_PCH_SRC})
endif ()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# Enable precompiled headers when using the GCC compiler.

if (USE_SCRIPTPCH)
  set(scripts_STAT_PCH_HDR PrecompiledHeaders/ScriptPCH.h)
  set(scripts_STAT_PCH_SRC PrecompiledHeaders/ScriptPCH.cpp)
endif ()

file(GLOB_RECURSE sources_Commands Commands/*.cpp Commands/*.h)
file(GLOB_RECURSE sources_Spells Spells/*.cpp Spells/*.h)

if(SCRIPTS)
  file(GLOB_RECURSE sources_Custom Custom/*.cpp Custom/*.h)
  file(GLOB_RECURSE sources_EasternKingdoms EasternKingdoms/*.cpp EasternKingdoms/*.h)
  file(GLOB_RECURSE sources_Events Events/*.cpp Events/*.h)
  file(GLOB_RECURSE sources_Kalimdor Kalimdor/*.cpp Kalimdor/*.h)
  file(GLOB_RECURSE sources_Maelstrom Maelstrom/*.cpp Maelstrom/*.h)
  file(GLOB_RECURSE sources_Northrend Northrend/*.cpp Northrend/*.h)
  file(GLOB_RECURSE sources_OutdoorPvP OutdoorPvP/*.cpp OutdoorPvP/*.h)
  file(GLOB_RECURSE sources_Outland Outland/*.cpp Outland/*.h)
  file(GLOB_RECURSE sources_Pet Pet/*.cpp Pet/*.h)
  file(GLOB_RECURSE sources_World World/*.cpp World/*.h)
endif()

source_group(Commands FILES ${sources_Commands})
source_group(Spells FILES ${sources_Spells})

if(SCRIPTS)
  source_group(EasternKingdoms FILES ${sources_EasternKingdoms})
  source_group(Events FILES ${sources_Events})
  source_group(Kalimdor FILES ${sources_Kalimdor})
  source_group(Maelstrom FILES ${sources_Maelstrom})
  source_group(Northrend FILES ${sources_Northrend})
  source_group(OutdoorPvP FILES ${sources_OutdoorPvP})
  source_group(Outland FILES ${sources_Outland})
  source_group(Pet FILES ${sources_Pet})
  source_group(World FILES ${sources_World})
endif()

message(STATUS "SCRIPT PREPARATIONS")

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  ../game/AI/ScriptedAI/ScriptedEscortAI.cpp
  ../game/AI/ScriptedAI/ScriptedCreature.cpp
  ../game/AI/ScriptedAI/ScriptedFollowerAI.cpp
)

include(Commands/CMakeLists.txt)
include(Spells/CMakeLists.txt)

if(SCRIPTS)
  include(Custom/CMakeLists.txt)
  include(EasternKingdoms/CMakeLists.txt)
  include(Events/CMakeLists.txt)
  include(Kalimdor/CMakeLists.txt)
  include(Maelstrom/CMakeLists.txt)
  include(Northrend/CMakeLists.txt)
  include(OutdoorPvP/CMakeLists.txt)
  include(Outland/CMakeLists.txt)
  include(Pet/CMakeLists.txt)
  include(World/CMakeLists.txt)
endif()

message(STATUS "SCRIPT PREPARATION COMPLETE")
message("")

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Detour
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Recast
  ${CMAKE_SOURCE_DIR}/dep/g3dlite/include
  ${CMAKE_SOURCE_DIR}/dep/SFMT
  ${CMAKE_SOURCE_DIR}/dep/zlib
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Configuration
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography
  ${CMAKE_SOURCE_DIR}/src/server/shared/Database
  ${CMAKE_SOURCE_DIR}/src/server/shared/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic/LinkedReference
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic
  ${CMAKE_SOURCE_DIR}/src/server/shared/Logging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Packets
  ${CMAKE_SOURCE_DIR}/src/server/shared/Threading
  ${CMAKE_SOURCE_DIR}/src/server/shared/Utilities
  ${CMAKE_SOURCE_DIR}/src/server/collision
  ${CMAKE_SOURCE_DIR}/src/server/collision/Management
  ${CMAKE_SOURCE_DIR}/src/server/collision/Models
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Database
  ${CMAKE_SOURCE_DIR}/src/server/game/Accounts
  ${CMAKE_SOURCE_DIR}/src/server/game/Achievements
  ${CMAKE_SOURCE_DIR}/src/server/game/Addons
  ${CMAKE_SOURCE_DIR}/src/server/game/AI
  ${CMAKE_SOURCE_DIR}/src/server/game/AI/CoreAI
  ${CMAKE_SOURCE_DIR}/src/server/game/AI/ScriptedAI
  ${CMAKE_SOURCE_DIR}/src/server/game/AI/SmartScripts
  ${CMAKE_SOURCE_DIR}/src/server/game/AuctionHouse
  ${CMAKE_SOURCE_DIR}/src/server/game/Battlefield
  ${CMAKE_SOURCE_DIR}/src/server/game/Battlefield/Zones
  ${CMAKE_SOURCE_DIR}/src/server/game/Battlegrounds
  ${CMAKE_SOURCE_DIR}/src/server/game/Battlegrounds/Zones
  ${CMAKE_SOURCE_DIR}/src/server/game/BlackMarket
  ${CMAKE_SOURCE_DIR}/src/server/game/Calendar
  ${CMAKE_SOURCE_DIR}/src/server/game/Chat
  ${CMAKE_SOURCE_DIR}/src/server/game/Chat/Channels
  ${CMAKE_SOURCE_DIR}/src/server/game/Conditions
  ${CMAKE_SOURCE_DIR}/src/server/shared/Configuration
  ${CMAKE_SOURCE_DIR}/src/server/game/Combat
  ${CMAKE_SOURCE_DIR}/src/server/game/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/game/DungeonFinding
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/AreaTrigger
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Corpse
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Creature
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/DynamicObject
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Item
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Item/Container
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/GameObject
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object/Updates
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Pet
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Player
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Transport
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Unit
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Vehicle
  ${CMAKE_SOURCE_DIR}/src/server/game/Events
  ${CMAKE_SOURCE_DIR}/src/server/game/Globals
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids/Cells
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids/Notifiers
  ${CMAKE_SOURCE_DIR}/src/server/game/Groups
  ${CMAKE_SOURCE_DIR}/src/server/game/Guilds
  ${CMAKE_SOURCE_DIR}/src/server/game/Handlers
  ${CMAKE_SOURCE_DIR}/src/server/game/Instances
  ${CMAKE_SOURCE_DIR}/src/server/game/LookingForGroup
  ${CMAKE_SOURCE_DIR}/src/server/game/Loot
  ${CMAKE_SOURCE_DIR}/src/server/game/Mails
  ${CMAKE_SOURCE_DIR}/src/server/game/Miscellaneous
  ${CMAKE_SOURCE_DIR}/src/server/game/Maps
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/MovementGenerators
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/Spline
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/Waypoints
  ${CMAKE_SOURCE_DIR}/src/server/game/Opcodes
  ${CMAKE_SOURCE_DIR}/src/server/game/OutdoorPvP
  ${CMAKE_SOURCE_DIR}/src/server/game/Pools
  ${CMAKE_SOURCE_DIR}/src/server/game/PrecompiledHeaders
  ${CMAKE_SOURCE_DIR}/src/server/game/Quests
  ${CMAKE_SOURCE_DIR}/src/server/game/Reputation
  ${CMAKE_SOURCE_DIR}/src/server/game/Scripting
  ${CMAKE_SOURCE_DIR}/src/server/game/Server
  ${CMAKE_SOURCE_DIR}/src/server/game/Server/Protocol
  ${CMAKE_SOURCE_DIR}/src/server/game/Skills
  ${CMAKE_SOURCE_DIR}/src/server/game/Spells
  ${CMAKE_SOURCE_DIR}/src/server/game/Spells/Auras
  ${CMAKE_SOURCE_DIR}/src/server/game/Texts
  ${CMAKE_SOURCE_DIR}/src/server/game/Tickets
  ${CMAKE_SOURCE_DIR}/src/server/game/Tools
  ${CMAKE_SOURCE_DIR}/src/server/game/Warden
  ${CMAKE_SOURCE_DIR}/src/server/game/Warden/Modules
  ${CMAKE_SOURCE_DIR}/src/server/game/Weather
  ${CMAKE_SOURCE_DIR}/src/server/game/World
  ${ACE_INCLUDE_DIR}
  ${MYSQL_INCLUDE_DIR}
)

add_library(scripts STATIC
  ${scripts_STAT_SRCS}
  ${scripts_STAT_PCH_SRC}
)

add_dependencies(scripts revision.h)

# Generate precompiled header
if (USE_SCRIPTPCH)
  add_cxx_pch(scripts ${scripts_STAT_PCH_HDR} ${scripts_STAT_PCH_SRC})
endif()
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB_RECURSE sources_Commands Commands/*.cpp Commands/*.h)

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  ${sources_Commands}
)

message("  -> Prepared: Commands")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
)

message("  -> Prepared: Custom")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  EasternKingdoms/zone_ghostlands.cpp
  EasternKingdoms/zone_eversong_woods.cpp
  EasternKingdoms/zone_elwynn_forest.cpp
  EasternKingdoms/AlteracValley/boss_galvangar.cpp
  EasternKingdoms/AlteracValley/boss_balinda.cpp
  EasternKingdoms/AlteracValley/boss_drekthar.cpp
  EasternKingdoms/AlteracValley/boss_vanndar.cpp
  EasternKingdoms/AlteracValley/alterac_valley.cpp
  EasternKingdoms/BaradinHold/boss_alizabal.cpp
  EasternKingdoms/BaradinHold/boss_occuthar.cpp
  EasternKingdoms/BaradinHold/boss_pit_lord_argaloth.cpp
  EasternKingdoms/BaradinHold/instance_baradin_hold.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_high_interrogator_gerstahn.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_gorosh_the_dervish.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/blackrock_depths.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_anubshiah.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_tomb_of_seven.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_general_angerforge.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_grizzle.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_ambassador_flamelash.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/instance_blackrock_depths.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_moira_bronzebeard.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/blackrock_depths.h
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_emperor_dagran_thaurissan.cpp
  EasternKingdoms/BlackrockMountain/BlackrockDepths/boss_magmus.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_chromaggus.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_razorgore.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_firemaw.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_broodlord_lashlayer.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_ebonroc.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/instance_blackwing_lair.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_vaelastrasz.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_nefarian.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/boss_flamegor.cpp
  EasternKingdoms/BlackrockMountain/BlackwingLair/blackwing_lair.h
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_pyroguard_emberseer.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_drakkisath.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_warmaster_voone.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_mother_smolderweb.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_quartermaster_zigris.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_halycon.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_overlord_wyrmthalak.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_shadow_hunter_voshgajin.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_gyth.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_rend_blackhand.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_highlord_omokk.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_the_beast.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_gizrul_the_slavener.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_urok_doomhowl.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/boss_lord_valthalak.cpp
  EasternKingdoms/BlackrockMountain/BlackrockSpire/blackrock_spire.h
  EasternKingdoms/BlackrockMountain/BlackrockSpire/instance_blackrock_spire.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_gehennas.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_lucifron.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_golemagg.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_majordomo_executus.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_baron_geddon.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_ragnaros.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_garr.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/molten_core.h
  EasternKingdoms/BlackrockMountain/MoltenCore/instance_molten_core.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_sulfuron_harbinger.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_magmadar.cpp
  EasternKingdoms/BlackrockMountain/MoltenCore/boss_shazzrah.cpp
  #REWORKED IN PANDARIA
  #EasternKingdoms/Scholomance/boss_the_ravenian.cpp
  #EasternKingdoms/Scholomance/boss_instructor_malicia.cpp
  #EasternKingdoms/Scholomance/boss_death_knight_darkreaver.cpp
  #EasternKingdoms/Scholomance/boss_illucia_barov.cpp
  #EasternKingdoms/Scholomance/scholomance.h
  #EasternKingdoms/Scholomance/boss_vectus.cpp
  #EasternKingdoms/Scholomance/boss_jandice_barov.cpp
  #EasternKingdoms/Scholomance/boss_kormok.cpp
  #EasternKingdoms/Scholomance/boss_lord_alexei_barov.cpp
  #EasternKingdoms/Scholomance/boss_doctor_theolen_krastinov.cpp
  #EasternKingdoms/Scholomance/boss_darkmaster_gandling.cpp
  #EasternKingdoms/Scholomance/instance_scholomance.cpp
  #EasternKingdoms/Scholomance/boss_lorekeeper_polkelt.cpp
  #EasternKingdoms/Scholomance/boss_ras_frostwhisper.cpp
  #EasternKingdoms/Scholomance/boss_kirtonos_the_herald.cpp
  EasternKingdoms/zone_isle_of_queldanas.cpp
  EasternKingdoms/ZulGurub/boss_grilek.cpp
  EasternKingdoms/ZulGurub/boss_hazzarah.cpp
  EasternKingdoms/ZulGurub/boss_jindo_the_godbreaker.cpp
  EasternKingdoms/ZulGurub/boss_kilnara.cpp
  EasternKingdoms/ZulGurub/boss_mandokir.cpp
  EasternKingdoms/ZulGurub/boss_renataki.cpp
  EasternKingdoms/ZulGurub/boss_venoxis.cpp
  EasternKingdoms/ZulGurub/boss_wushoolay.cpp
  EasternKingdoms/ZulGurub/boss_zanzil.cpp
  EasternKingdoms/ZulGurub/instance_zulgurub.cpp
  EasternKingdoms/zone_arathi_highlands.cpp
  EasternKingdoms/Gnomeregan/instance_gnomeregan.cpp
  EasternKingdoms/Gnomeregan/gnomeregan.cpp
  EasternKingdoms/Gnomeregan/gnomeregan.h
  EasternKingdoms/ScarletEnclave/chapter2.cpp
  EasternKingdoms/ScarletEnclave/chapter5.cpp
  EasternKingdoms/ScarletEnclave/chapter1.cpp
  EasternKingdoms/ScarletEnclave/zone_the_scarlet_enclave.cpp
  EasternKingdoms/zone_eastern_plaguelands.cpp
  EasternKingdoms/Stratholme/boss_baroness_anastari.cpp
  EasternKingdoms/Stratholme/boss_nerubenkan.cpp
  EasternKingdoms/Stratholme/instance_stratholme.cpp
  EasternKingdoms/Stratholme/boss_dathrohan_balnazzar.cpp
  EasternKingdoms/Stratholme/boss_timmy_the_cruel.cpp
  EasternKingdoms/Stratholme/boss_baron_rivendare.cpp
  EasternKingdoms/Stratholme/boss_magistrate_barthilas.cpp
  EasternKingdoms/Stratholme/boss_order_of_silver_hand.cpp
  EasternKingdoms/Stratholme/boss_ramstein_the_gorger.cpp
  EasternKingdoms/Stratholme/boss_cannon_master_willey.cpp
  EasternKingdoms/Stratholme/boss_maleki_the_pallid.cpp
  EasternKingdoms/Stratholme/boss_postmaster_malown.cpp
  EasternKingdoms/Stratholme/stratholme.h
  EasternKingdoms/Stratholme/stratholme.cpp
  #REWORKED IN CATACLYSM
  #EasternKingdoms/SunkenTemple/sunken_temple.cpp
  #EasternKingdoms/SunkenTemple/sunken_temple.h
  #EasternKingdoms/SunkenTemple/instance_sunken_temple.cpp
  EasternKingdoms/MagistersTerrace/boss_felblood_kaelthas.cpp
  EasternKingdoms/MagistersTerrace/magisters_terrace.h
  EasternKingdoms/MagistersTerrace/boss_priestess_delrissa.cpp
  EasternKingdoms/MagistersTerrace/instance_magisters_terrace.cpp
  EasternKingdoms/MagistersTerrace/boss_selin_fireheart.cpp
  EasternKingdoms/MagistersTerrace/boss_vexallus.cpp
  EasternKingdoms/MagistersTerrace/magisters_terrace.cpp
  #REWORKED IN CATACLYSM
  #EasternKingdoms/Uldaman/uldaman.cpp
  #EasternKingdoms/Uldaman/boss_ironaya.cpp
  #EasternKingdoms/Uldaman/uldaman.h
  #EasternKingdoms/Uldaman/instance_uldaman.cpp
  #EasternKingdoms/Uldaman/boss_archaedas.cpp
  EasternKingdoms/SunwellPlateau/boss_eredar_twins.cpp
  EasternKingdoms/SunwellPlateau/boss_kiljaeden.cpp
  EasternKingdoms/SunwellPlateau/sunwell_plateau.h
  EasternKingdoms/SunwellPlateau/boss_muru.cpp
  EasternKingdoms/SunwellPlateau/instance_sunwell_plateau.cpp
  EasternKingdoms/SunwellPlateau/boss_kalecgos.cpp
  EasternKingdoms/SunwellPlateau/boss_brutallus.cpp
  EasternKingdoms/SunwellPlateau/sunwell_plateau.cpp
  EasternKingdoms/SunwellPlateau/boss_felmyst.cpp
  EasternKingdoms/zone_stranglethorn_vale.cpp
  #REWORKED IN CATACLYSM
  #EasternKingdoms/Deadmines/deadmines.h
  #EasternKingdoms/Deadmines/deadmines.cpp
  #EasternKingdoms/Deadmines/boss_mr_smite.cpp
  #EasternKingdoms/Deadmines/instance_deadmines.cpp
  #REWORKED IN PANDARIA
  #EasternKingdoms/ScarletMonastery/boss_azshir_the_sleepless.cpp
  #EasternKingdoms/ScarletMonastery/boss_mograine_and_whitemane.cpp
  #EasternKingdoms/ScarletMonastery/boss_bloodmage_thalnos.cpp
  #EasternKingdoms/ScarletMonastery/boss_interrogator_vishas.cpp
  #EasternKingdoms/ScarletMonastery/boss_headless_horseman.cpp
  #EasternKingdoms/ScarletMonastery/instance_scarlet_monastery.cpp
  #EasternKingdoms/ScarletMonastery/boss_houndmaster_loksey.cpp
  #EasternKingdoms/ScarletMonastery/scarlet_monastery.h
  #EasternKingdoms/ScarletMonastery/boss_high_inquisitor_fairbanks.cpp
  #EasternKingdoms/ScarletMonastery/boss_arcanist_doan.cpp
  #EasternKingdoms/ScarletMonastery/boss_herod.cpp
  #EasternKingdoms/ScarletMonastery/boss_scorn.cpp
  EasternKingdoms/zone_undercity.cpp
  #REWORKED IN CATACLYSM
  #EasternKingdoms/ShadowfangKeep/shadowfang_keep.cpp
  #EasternKingdoms/ShadowfangKeep/instance_shadowfang_keep.cpp
  #EasternKingdoms/ShadowfangKeep/shadowfang_keep.h
  EasternKingdoms/zone_blasted_lands.cpp
  #REWORKED IN CATACLYSM
  #EasternKingdoms/ZulAman/boss_halazzi.cpp
  #EasternKingdoms/ZulAman/boss_hexlord.cpp
  #EasternKingdoms/ZulAman/boss_daakara.cpp
  #EasternKingdoms/ZulAman/boss_akilzon.cpp
  #EasternKingdoms/ZulAman/instance_zulaman.cpp
  #EasternKingdoms/ZulAman/boss_janalai.cpp
  #EasternKingdoms/ZulAman/boss_nalorakk.cpp
  #EasternKingdoms/ZulAman/zulaman.cpp
  #EasternKingdoms/ZulAman/zulaman.h
  EasternKingdoms/zone_hinterlands.cpp
  EasternKingdoms/zone_silverpine_forest.cpp
  EasternKingdoms/Karazhan/instance_karazhan.cpp
  EasternKingdoms/Karazhan/boss_nightbane.cpp
  EasternKingdoms/Karazhan/karazhan.cpp
  EasternKingdoms/Karazhan/boss_curator.cpp
  EasternKingdoms/Karazhan/boss_shade_of_aran.cpp
  EasternKingdoms/Karazhan/boss_netherspite.cpp
  EasternKingdoms/Karazhan/boss_maiden_of_virtue.cpp
  EasternKingdoms/Karazhan/boss_midnight.cpp
  EasternKingdoms/Karazhan/boss_prince_malchezaar.cpp
  EasternKingdoms/Karazhan/bosses_opera.cpp
  EasternKingdoms/Karazhan/boss_moroes.cpp
  EasternKingdoms/Karazhan/boss_terestian_illhoof.cpp
  EasternKingdoms/Karazhan/karazhan.h
  #REWORKED IN CATACLYSM
  #EasternKingdoms/TheStockade/instance_the_stockade.cpp
)

message("  -> Prepared: Eastern Kingdoms")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Events/childrens_week.cpp
)

message("  -> Prepared: Events")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Examples/example_misc.cpp
  Examples/example_gossip_codebox.cpp
  Examples/example_escort.cpp
  Examples/example_creature.cpp
  Examples/example_spell.cpp
  Examples/example_commandscript.cpp
)

message("  -> Prepared: Examples")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Kalimdor/zone_silithus.cpp
  Kalimdor/zone_moonglade.cpp
  Kalimdor/RazorfenDowns/razorfen_downs.cpp
  Kalimdor/RazorfenDowns/instance_razorfen_downs.cpp
  Kalimdor/RazorfenDowns/boss_amnennar_the_coldbringer.cpp
  Kalimdor/RazorfenDowns/razorfen_downs.h
  #REWORKED IN CATACLYSM
  #Kalimdor/ZulFarrak/zulfarrak.h
  #Kalimdor/ZulFarrak/zulfarrak.cpp
  #Kalimdor/ZulFarrak/instance_zulfarrak.cpp
  #Kalimdor/ZulFarrak/boss_zum_rah.cpp
  Kalimdor/CavernsOfTime/EscapeFromDurnholdeKeep/boss_epoch_hunter.cpp
  Kalimdor/CavernsOfTime/EscapeFromDurnholdeKeep/old_hillsbrad.h
  Kalimdor/CavernsOfTime/EscapeFromDurnholdeKeep/boss_leutenant_drake.cpp
  Kalimdor/CavernsOfTime/EscapeFromDurnholdeKeep/old_hillsbrad.cpp
  Kalimdor/CavernsOfTime/EscapeFromDurnholdeKeep/instance_old_hillsbrad.cpp
  Kalimdor/CavernsOfTime/EscapeFromDurnholdeKeep/boss_captain_skarloc.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/boss_archimonde.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/hyjalAI.h
  Kalimdor/CavernsOfTime/BattleForMountHyjal/hyjal_trash.h
  Kalimdor/CavernsOfTime/BattleForMountHyjal/boss_kazrogal.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/hyjal_trash.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/hyjal.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/hyjalAI.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/instance_hyjal.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/boss_rage_winterchill.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/hyjal.h
  Kalimdor/CavernsOfTime/BattleForMountHyjal/boss_azgalor.cpp
  Kalimdor/CavernsOfTime/BattleForMountHyjal/boss_anetheron.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/boss_infinite_corruptor.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/boss_salramm_the_fleshcrafter.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/boss_meathook.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/boss_mal_ganis.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/boss_chrono_lord_epoch.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/culling_of_stratholme.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/instance_culling_of_stratholme.cpp
  Kalimdor/CavernsOfTime/CullingOfStratholme/culling_of_stratholme.h
  Kalimdor/CavernsOfTime/TheBlackMorass/the_black_morass.h
  Kalimdor/CavernsOfTime/TheBlackMorass/instance_the_black_morass.cpp
  Kalimdor/CavernsOfTime/TheBlackMorass/boss_chrono_lord_deja.cpp
  Kalimdor/CavernsOfTime/TheBlackMorass/the_black_morass.cpp
  Kalimdor/CavernsOfTime/TheBlackMorass/boss_aeonus.cpp
  Kalimdor/CavernsOfTime/TheBlackMorass/boss_temporus.cpp
  Kalimdor/BlackfathomDeeps/boss_kelris.cpp
  Kalimdor/BlackfathomDeeps/instance_blackfathom_deeps.cpp
  Kalimdor/BlackfathomDeeps/boss_gelihast.cpp
  Kalimdor/BlackfathomDeeps/blackfathom_deeps.cpp
  Kalimdor/BlackfathomDeeps/boss_aku_mai.cpp
  Kalimdor/BlackfathomDeeps/blackfathom_deeps.h
  Kalimdor/zone_azuremyst_isle.cpp
  Kalimdor/zone_desolace.cpp
  #REWORKED IN CATACLYSM
  #Kalimdor/Maraudon/boss_princess_theradras.cpp
  #Kalimdor/Maraudon/boss_landslide.cpp
  #Kalimdor/Maraudon/boss_celebras_the_cursed.cpp
  #Kalimdor/Maraudon/boss_noxxion.cpp
  #Kalimdor/Maraudon/instance_maraudon.cpp
  Kalimdor/TempleOfAhnQiraj/boss_fankriss.cpp
  Kalimdor/TempleOfAhnQiraj/boss_huhuran.cpp
  Kalimdor/TempleOfAhnQiraj/instance_temple_of_ahnqiraj.cpp
  Kalimdor/TempleOfAhnQiraj/mob_anubisath_sentinel.cpp
  Kalimdor/TempleOfAhnQiraj/boss_viscidus.cpp
  Kalimdor/TempleOfAhnQiraj/boss_twinemperors.cpp
  Kalimdor/TempleOfAhnQiraj/boss_sartura.cpp
  Kalimdor/TempleOfAhnQiraj/boss_cthun.cpp
  Kalimdor/TempleOfAhnQiraj/temple_of_ahnqiraj.h
  Kalimdor/TempleOfAhnQiraj/boss_skeram.cpp
  Kalimdor/TempleOfAhnQiraj/boss_ouro.cpp
  Kalimdor/TempleOfAhnQiraj/boss_bug_trio.cpp
  Kalimdor/RuinsOfAhnQiraj/boss_buru.cpp
  Kalimdor/RuinsOfAhnQiraj/instance_ruins_of_ahnqiraj.cpp
  Kalimdor/RuinsOfAhnQiraj/boss_rajaxx.cpp
  Kalimdor/RuinsOfAhnQiraj/boss_ossirian.cpp
  Kalimdor/RuinsOfAhnQiraj/boss_ayamiss.cpp
  Kalimdor/RuinsOfAhnQiraj/boss_moam.cpp
  Kalimdor/RuinsOfAhnQiraj/ruins_of_ahnqiraj.h
  Kalimdor/RuinsOfAhnQiraj/boss_kurinnaxx.cpp
  Kalimdor/zone_mulgore.cpp
  Kalimdor/zone_bloodmyst_isle.cpp
  Kalimdor/zone_thunder_bluff.cpp
  Kalimdor/RazorfenKraul/razorfen_kraul.h
  Kalimdor/RazorfenKraul/instance_razorfen_kraul.cpp
  Kalimdor/RazorfenKraul/razorfen_kraul.cpp
  Kalimdor/zone_the_barrens.cpp
  #REWORKED IN CATACLYSM
  #Kalimdor/WailingCaverns/wailing_caverns.h
  #Kalimdor/WailingCaverns/instance_wailing_caverns.cpp
  #Kalimdor/WailingCaverns/wailing_caverns.cpp
  Kalimdor/zone_durotar.cpp
  #Kalimdor/boss_azuregos.cpp
  Kalimdor/zone_tanaris.cpp
  Kalimdor/zone_dustwallow_marsh.cpp
  Kalimdor/zone_winterspring.cpp
  Kalimdor/zone_ashenvale.cpp
  Kalimdor/zone_teldrassil.cpp
  Kalimdor/OnyxiasLair/boss_onyxia.cpp
  Kalimdor/OnyxiasLair/onyxias_lair.h
  Kalimdor/OnyxiasLair/instance_onyxias_lair.cpp
  #REWORKED IN PANDARIA
  #Kalimdor/RagefireChasm/instance_ragefire_chasm.cpp
  Kalimdor/DireMaul/instance_dire_maul.cpp
  Kalimdor/HallsOfOrigination/halls_of_origination.h
  Kalimdor/HallsOfOrigination/instance_halls_of_origination.cpp
  Kalimdor/HallsOfOrigination/boss_temple_guardian_anhuur.cpp
  Kalimdor/HallsOfOrigination/boss_earthrager_ptah.cpp
  Kalimdor/HallsOfOrigination/boss_anraphet.cpp
  Kalimdor/Firelands/instance_firelands.cpp
  Kalimdor/Firelands/firelands.h
  Kalimdor/Firelands/boss_alysrazor.cpp
)

message("  -> Prepared: Kalimdor")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Maelstrom/kezan.cpp
)

message("  -> Prepared: The Maelstrom")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Northrend/zone_wintergrasp.cpp
  Northrend/isle_of_conquest.cpp
  Northrend/zone_storm_peaks.cpp
  Northrend/Ulduar/HallsOfLightning/instance_halls_of_lightning.cpp
  Northrend/Ulduar/HallsOfLightning/boss_bjarngrim.cpp
  Northrend/Ulduar/HallsOfLightning/halls_of_lightning.h
  Northrend/Ulduar/HallsOfLightning/boss_ionar.cpp
  Northrend/Ulduar/HallsOfLightning/boss_volkhan.cpp
  Northrend/Ulduar/HallsOfLightning/boss_loken.cpp
  Northrend/Ulduar/Ulduar/boss_general_vezax.cpp
  Northrend/Ulduar/Ulduar/ulduar_teleporter.cpp
  Northrend/Ulduar/Ulduar/boss_thorim.cpp
  Northrend/Ulduar/Ulduar/boss_ignis.cpp
  Northrend/Ulduar/Ulduar/boss_algalon_the_observer.cpp
  Northrend/Ulduar/Ulduar/instance_ulduar.cpp
  Northrend/Ulduar/Ulduar/boss_auriaya.cpp
  Northrend/Ulduar/Ulduar/boss_yogg_saron.cpp
  Northrend/Ulduar/Ulduar/boss_hodir.cpp
  Northrend/Ulduar/Ulduar/boss_assembly_of_iron.cpp
  Northrend/Ulduar/Ulduar/boss_flame_leviathan.cpp
  Northrend/Ulduar/Ulduar/boss_xt002.cpp
  Northrend/Ulduar/Ulduar/boss_mimiron.cpp
  Northrend/Ulduar/Ulduar/ulduar.h
  Northrend/Ulduar/Ulduar/boss_freya.cpp
  Northrend/Ulduar/Ulduar/boss_razorscale.cpp
  Northrend/Ulduar/Ulduar/boss_kologarn.cpp
  Northrend/Ulduar/HallsOfStone/boss_krystallus.cpp
  Northrend/Ulduar/HallsOfStone/halls_of_stone.h
  Northrend/Ulduar/HallsOfStone/instance_halls_of_stone.cpp
  Northrend/Ulduar/HallsOfStone/boss_maiden_of_grief.cpp
  Northrend/Ulduar/HallsOfStone/boss_sjonnir.cpp
  Northrend/Ulduar/HallsOfStone/halls_of_stone.cpp
  Northrend/ChamberOfAspects/ObsidianSanctum/instance_obsidian_sanctum.cpp
  Northrend/ChamberOfAspects/ObsidianSanctum/obsidian_sanctum.h
  Northrend/ChamberOfAspects/ObsidianSanctum/boss_sartharion.cpp
  Northrend/ChamberOfAspects/RubySanctum/instance_ruby_sanctum.cpp
  Northrend/ChamberOfAspects/RubySanctum/ruby_sanctum.h
  Northrend/ChamberOfAspects/RubySanctum/ruby_sanctum.cpp
  Northrend/ChamberOfAspects/RubySanctum/boss_baltharus_the_warborn.cpp
  Northrend/ChamberOfAspects/RubySanctum/boss_saviana_ragefire.cpp
  Northrend/ChamberOfAspects/RubySanctum/boss_general_zarithrian.cpp
  Northrend/ChamberOfAspects/RubySanctum/boss_halion.cpp
  Northrend/FrozenHalls/HallsOfReflection/halls_of_reflection.h
  Northrend/FrozenHalls/HallsOfReflection/boss_falric.cpp
  Northrend/FrozenHalls/HallsOfReflection/instance_halls_of_reflection.cpp
  Northrend/FrozenHalls/HallsOfReflection/halls_of_reflection.cpp
  Northrend/FrozenHalls/HallsOfReflection/boss_marwyn.cpp
  Northrend/FrozenHalls/PitOfSaron/boss_forgemaster_garfrost.cpp
  Northrend/FrozenHalls/PitOfSaron/boss_krickandick.cpp
  Northrend/FrozenHalls/PitOfSaron/pit_of_saron.cpp
  Northrend/FrozenHalls/PitOfSaron/boss_scourgelord_tyrannus.cpp
  Northrend/FrozenHalls/PitOfSaron/pit_of_saron.h
  Northrend/FrozenHalls/PitOfSaron/instance_pit_of_saron.cpp
  Northrend/FrozenHalls/ForgeOfSouls/forge_of_souls.cpp
  Northrend/FrozenHalls/ForgeOfSouls/boss_bronjahm.cpp
  Northrend/FrozenHalls/ForgeOfSouls/instance_forge_of_souls.cpp
  Northrend/FrozenHalls/ForgeOfSouls/boss_devourer_of_souls.cpp
  Northrend/FrozenHalls/ForgeOfSouls/forge_of_souls.h
  Northrend/Nexus/EyeOfEternity/boss_malygos.cpp
  Northrend/Nexus/EyeOfEternity/instance_eye_of_eternity.cpp
  Northrend/Nexus/EyeOfEternity/eye_of_eternity.h
  Northrend/Nexus/Oculus/boss_eregos.cpp
  Northrend/Nexus/Oculus/boss_drakos.cpp
  Northrend/Nexus/Oculus/oculus.h
  Northrend/Nexus/Oculus/boss_varos.cpp
  Northrend/Nexus/Oculus/boss_urom.cpp
  Northrend/Nexus/Oculus/oculus.cpp
  Northrend/Nexus/Oculus/instance_oculus.cpp
  Northrend/Nexus/Nexus/boss_commander_kolurg.cpp
  Northrend/Nexus/Nexus/boss_commander_stoutbeard.cpp
  Northrend/Nexus/Nexus/boss_ormorok.cpp
  Northrend/Nexus/Nexus/boss_magus_telestra.cpp
  Northrend/Nexus/Nexus/instance_nexus.cpp
  Northrend/Nexus/Nexus/boss_keristrasza.cpp
  Northrend/Nexus/Nexus/boss_anomalus.cpp
  Northrend/Nexus/Nexus/nexus.h
  Northrend/CrusadersColiseum/TrialOfTheCrusader/boss_anubarak_trial.cpp
  Northrend/CrusadersColiseum/TrialOfTheCrusader/boss_faction_champions.cpp
  Northrend/CrusadersColiseum/TrialOfTheCrusader/boss_lord_jaraxxus.cpp
  Northrend/CrusadersColiseum/TrialOfTheCrusader/trial_of_the_crusader.h
  Northrend/CrusadersColiseum/TrialOfTheCrusader/boss_northrend_beasts.cpp
  Northrend/CrusadersColiseum/TrialOfTheCrusader/trial_of_the_crusader.cpp
  Northrend/CrusadersColiseum/TrialOfTheCrusader/boss_twin_valkyr.cpp
  Northrend/CrusadersColiseum/TrialOfTheCrusader/instance_trial_of_the_crusader.cpp
  Northrend/CrusadersColiseum/TrialOfTheChampion/trial_of_the_champion.h
  Northrend/CrusadersColiseum/TrialOfTheChampion/trial_of_the_champion.cpp
  Northrend/CrusadersColiseum/TrialOfTheChampion/boss_grand_champions.cpp
  Northrend/CrusadersColiseum/TrialOfTheChampion/boss_black_knight.cpp
  Northrend/CrusadersColiseum/TrialOfTheChampion/instance_trial_of_the_champion.cpp
  Northrend/CrusadersColiseum/TrialOfTheChampion/boss_argent_challenge.cpp
  Northrend/Naxxramas/boss_loatheb.cpp
  Northrend/Naxxramas/boss_anubrekhan.cpp
  Northrend/Naxxramas/boss_maexxna.cpp
  Northrend/Naxxramas/boss_patchwerk.cpp
  Northrend/Naxxramas/boss_gothik.cpp
  Northrend/Naxxramas/boss_faerlina.cpp
  Northrend/Naxxramas/boss_gluth.cpp
  Northrend/Naxxramas/boss_four_horsemen.cpp
  Northrend/Naxxramas/naxxramas.h
  Northrend/Naxxramas/boss_kelthuzad.cpp
  Northrend/Naxxramas/boss_heigan.cpp
  Northrend/Naxxramas/boss_thaddius.cpp
  Northrend/Naxxramas/boss_razuvious.cpp
  Northrend/Naxxramas/boss_sapphiron.cpp
  Northrend/Naxxramas/instance_naxxramas.cpp
  Northrend/Naxxramas/boss_grobbulus.cpp
  Northrend/Naxxramas/boss_noth.cpp
  Northrend/zone_crystalsong_forest.cpp
  Northrend/VaultOfArchavon/boss_archavon.cpp
  Northrend/VaultOfArchavon/boss_koralon.cpp
  Northrend/VaultOfArchavon/vault_of_archavon.h
  Northrend/VaultOfArchavon/instance_vault_of_archavon.cpp
  Northrend/VaultOfArchavon/boss_emalon.cpp
  Northrend/VaultOfArchavon/boss_toravon.cpp
  Northrend/zone_sholazar_basin.cpp
  Northrend/UtgardeKeep/UtgardePinnacle/boss_svala.cpp
  Northrend/UtgardeKeep/UtgardePinnacle/boss_palehoof.cpp
  Northrend/UtgardeKeep/UtgardePinnacle/boss_skadi.cpp
  Northrend/UtgardeKeep/UtgardePinnacle/boss_ymiron.cpp
  Northrend/UtgardeKeep/UtgardePinnacle/instance_utgarde_pinnacle.cpp
  Northrend/UtgardeKeep/UtgardePinnacle/utgarde_pinnacle.h
  Northrend/UtgardeKeep/UtgardeKeep/boss_ingvar_the_plunderer.cpp
  Northrend/UtgardeKeep/UtgardeKeep/boss_skarvald_dalronn.cpp
  Northrend/UtgardeKeep/UtgardeKeep/utgarde_keep.h
  Northrend/UtgardeKeep/UtgardeKeep/instance_utgarde_keep.cpp
  Northrend/UtgardeKeep/UtgardeKeep/boss_keleseth.cpp
  Northrend/UtgardeKeep/UtgardeKeep/utgarde_keep.cpp
  Northrend/zone_dragonblight.cpp
  Northrend/zone_grizzly_hills.cpp
  Northrend/AzjolNerub/AzjolNerub/azjol_nerub.h
  Northrend/AzjolNerub/AzjolNerub/instance_azjol_nerub.cpp
  Northrend/AzjolNerub/AzjolNerub/boss_krikthir_the_gatewatcher.cpp
  Northrend/AzjolNerub/AzjolNerub/boss_hadronox.cpp
  Northrend/AzjolNerub/AzjolNerub/boss_anubarak.cpp
  Northrend/AzjolNerub/Ahnkahet/boss_herald_volazj.cpp
  Northrend/AzjolNerub/Ahnkahet/boss_prince_taldaram.cpp
  Northrend/AzjolNerub/Ahnkahet/instance_ahnkahet.cpp
  Northrend/AzjolNerub/Ahnkahet/boss_jedoga_shadowseeker.cpp
  Northrend/AzjolNerub/Ahnkahet/boss_elder_nadox.cpp
  Northrend/AzjolNerub/Ahnkahet/boss_amanitar.cpp
  Northrend/AzjolNerub/Ahnkahet/ahnkahet.h
  Northrend/VioletHold/boss_zuramat.cpp
  Northrend/VioletHold/instance_violet_hold.cpp
  Northrend/VioletHold/boss_lavanthor.cpp
  Northrend/VioletHold/boss_cyanigosa.cpp
  Northrend/VioletHold/violet_hold.h
  Northrend/VioletHold/boss_ichoron.cpp
  Northrend/VioletHold/boss_moragg.cpp
  Northrend/VioletHold/boss_xevozz.cpp
  Northrend/VioletHold/boss_erekem.cpp
  Northrend/VioletHold/violet_hold.cpp
  Northrend/IcecrownCitadel/instance_icecrown_citadel.cpp
  Northrend/IcecrownCitadel/icecrown_citadel.cpp
  Northrend/IcecrownCitadel/icecrown_citadel.h
  Northrend/IcecrownCitadel/icecrown_citadel_teleport.cpp
  Northrend/IcecrownCitadel/boss_lord_marrowgar.cpp
  Northrend/IcecrownCitadel/boss_lady_deathwhisper.cpp
  Northrend/IcecrownCitadel/boss_deathbringer_saurfang.cpp
  Northrend/IcecrownCitadel/boss_festergut.cpp
  Northrend/IcecrownCitadel/boss_rotface.cpp
  Northrend/IcecrownCitadel/boss_professor_putricide.cpp
  Northrend/IcecrownCitadel/boss_blood_prince_council.cpp
  Northrend/IcecrownCitadel/boss_blood_queen_lana_thel.cpp
  Northrend/IcecrownCitadel/boss_valithria_dreamwalker.cpp
  Northrend/IcecrownCitadel/boss_sindragosa.cpp
  Northrend/IcecrownCitadel/boss_the_lich_king.cpp
  Northrend/zone_zuldrak.cpp
  Northrend/zone_icecrown.cpp
  Northrend/Gundrak/boss_slad_ran.cpp
  Northrend/Gundrak/instance_gundrak.cpp
  Northrend/Gundrak/boss_drakkari_colossus.cpp
  Northrend/Gundrak/gundrak.h
  Northrend/Gundrak/boss_gal_darah.cpp
  Northrend/Gundrak/boss_moorabi.cpp
  Northrend/Gundrak/boss_eck.cpp
  Northrend/zone_borean_tundra.cpp
  Northrend/zone_howling_fjord.cpp
  Northrend/zone_dalaran.cpp
  Northrend/DraktharonKeep/boss_trollgore.cpp
  Northrend/DraktharonKeep/instance_drak_tharon_keep.cpp
  Northrend/DraktharonKeep/boss_novos.cpp
  Northrend/DraktharonKeep/drak_tharon_keep.h
  Northrend/DraktharonKeep/boss_tharon_ja.cpp
  Northrend/DraktharonKeep/boss_king_dred.cpp
)

message("  -> Prepared: Northrend")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  OutdoorPvP/OutdoorPvPTF.cpp
  OutdoorPvP/OutdoorPvPSI.cpp
  OutdoorPvP/OutdoorPvPSI.h
  OutdoorPvP/OutdoorPvPZM.cpp
  OutdoorPvP/OutdoorPvPNA.cpp
  OutdoorPvP/OutdoorPvPHP.cpp
  OutdoorPvP/OutdoorPvPTF.h
  OutdoorPvP/OutdoorPvPHP.h
  OutdoorPvP/OutdoorPvPZM.h
  OutdoorPvP/OutdoorPvPNA.h
)

message("  -> Prepared: Outdoor PVP Zones")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Outland/zone_nagrand.cpp
  Outland/HellfireCitadel/MagtheridonsLair/magtheridons_lair.h
  Outland/HellfireCitadel/MagtheridonsLair/instance_magtheridons_lair.cpp
  Outland/HellfireCitadel/MagtheridonsLair/boss_magtheridon.cpp
  Outland/HellfireCitadel/HellfireRamparts/instance_hellfire_ramparts.cpp
  Outland/HellfireCitadel/HellfireRamparts/boss_omor_the_unscarred.cpp
  Outland/HellfireCitadel/HellfireRamparts/boss_watchkeeper_gargolmar.cpp
  Outland/HellfireCitadel/HellfireRamparts/boss_vazruden_the_herald.cpp
  Outland/HellfireCitadel/HellfireRamparts/hellfire_ramparts.h
  Outland/HellfireCitadel/BloodFurnace/boss_the_maker.cpp
  Outland/HellfireCitadel/BloodFurnace/boss_kelidan_the_breaker.cpp
  Outland/HellfireCitadel/BloodFurnace/blood_furnace.h
  Outland/HellfireCitadel/BloodFurnace/instance_blood_furnace.cpp
  Outland/HellfireCitadel/BloodFurnace/boss_broggok.cpp
  Outland/HellfireCitadel/ShatteredHalls/shattered_halls.h
  Outland/HellfireCitadel/ShatteredHalls/boss_warchief_kargath_bladefist.cpp
  Outland/HellfireCitadel/ShatteredHalls/boss_nethekurse.cpp
  Outland/HellfireCitadel/ShatteredHalls/instance_shattered_halls.cpp
  Outland/HellfireCitadel/ShatteredHalls/boss_warbringer_omrogg.cpp
  Outland/CoilfangReservoir/SteamVault/boss_mekgineer_steamrigger.cpp
  Outland/CoilfangReservoir/SteamVault/instance_steam_vault.cpp
  Outland/CoilfangReservoir/SteamVault/boss_hydromancer_thespia.cpp
  Outland/CoilfangReservoir/SteamVault/boss_warlord_kalithresh.cpp
  Outland/CoilfangReservoir/SteamVault/steam_vault.h
  Outland/CoilfangReservoir/SerpentShrine/boss_hydross_the_unstable.cpp
  Outland/CoilfangReservoir/SerpentShrine/boss_fathomlord_karathress.cpp
  Outland/CoilfangReservoir/SerpentShrine/instance_serpent_shrine.cpp
  Outland/CoilfangReservoir/SerpentShrine/serpent_shrine.h
  Outland/CoilfangReservoir/SerpentShrine/boss_lady_vashj.cpp
  Outland/CoilfangReservoir/SerpentShrine/boss_leotheras_the_blind.cpp
  Outland/CoilfangReservoir/SerpentShrine/boss_lurker_below.cpp
  Outland/CoilfangReservoir/SerpentShrine/boss_morogrim_tidewalker.cpp
  Outland/CoilfangReservoir/TheSlavePens/instance_the_slave_pens.cpp
  Outland/CoilfangReservoir/TheUnderbog/boss_hungarfen.cpp
  Outland/CoilfangReservoir/TheUnderbog/boss_the_black_stalker.cpp
  Outland/CoilfangReservoir/TheUnderbog/instance_the_underbog.cpp
  Outland/zone_shattrath_city.cpp
  Outland/TempestKeep/Mechanar/boss_mechano_lord_capacitus.cpp
  Outland/TempestKeep/Mechanar/boss_pathaleon_the_calculator.cpp
  Outland/TempestKeep/Mechanar/boss_nethermancer_sepethrea.cpp
  Outland/TempestKeep/Mechanar/mechanar.h
  Outland/TempestKeep/Mechanar/boss_gatewatcher_gyrokill.cpp
  Outland/TempestKeep/Mechanar/instance_mechanar.cpp
  Outland/TempestKeep/Mechanar/boss_gatewatcher_ironhand.cpp
  Outland/TempestKeep/Eye/the_eye.h
  Outland/TempestKeep/Eye/instance_the_eye.cpp
  Outland/TempestKeep/Eye/boss_void_reaver.cpp
  Outland/TempestKeep/Eye/boss_astromancer.cpp
  Outland/TempestKeep/Eye/boss_alar.cpp
  Outland/TempestKeep/Eye/boss_kaelthas.cpp
  Outland/TempestKeep/Eye/the_eye.cpp
  Outland/TempestKeep/botanica/the_botanica.h
  Outland/TempestKeep/botanica/instance_the_botanica.cpp
  Outland/TempestKeep/botanica/boss_commander_sarannis.cpp
  Outland/TempestKeep/botanica/boss_thorngrin_the_tender.cpp
  Outland/TempestKeep/botanica/boss_high_botanist_freywinn.cpp
  Outland/TempestKeep/botanica/boss_warp_splinter.cpp
  Outland/TempestKeep/botanica/boss_laj.cpp
  Outland/TempestKeep/arcatraz/boss_harbinger_skyriss.cpp
  Outland/TempestKeep/arcatraz/instance_arcatraz.cpp
  Outland/TempestKeep/arcatraz/arcatraz.h
  Outland/TempestKeep/arcatraz/arcatraz.cpp
  Outland/Auchindoun/AuchenaiCrypts/boss_shirrak_the_dead_watcher.cpp
  Outland/Auchindoun/AuchenaiCrypts/boss_exarch_maladaar.cpp
  Outland/Auchindoun/AuchenaiCrypts/instance_auchenai_crypts.cpp
  Outland/Auchindoun/AuchenaiCrypts/auchenai_crypts.h
  Outland/Auchindoun/ManaTombs/boss_pandemonius.cpp
  Outland/Auchindoun/ManaTombs/boss_nexusprince_shaffar.cpp
  Outland/Auchindoun/ManaTombs/instance_mana_tombs.cpp
  Outland/Auchindoun/ManaTombs/mana_tombs.h
  Outland/Auchindoun/SethekkHalls/boss_darkweaver_syth.cpp
  Outland/Auchindoun/SethekkHalls/boss_tailonking_ikiss.cpp
  Outland/Auchindoun/SethekkHalls/boss_anzu.cpp
  Outland/Auchindoun/SethekkHalls/instance_sethekk_halls.cpp
  Outland/Auchindoun/SethekkHalls/sethekk_halls.h
  Outland/Auchindoun/ShadowLabyrinth/boss_ambassador_hellmaw.cpp
  Outland/Auchindoun/ShadowLabyrinth/boss_blackheart_the_inciter.cpp
  Outland/Auchindoun/ShadowLabyrinth/boss_grandmaster_vorpil.cpp
  Outland/Auchindoun/ShadowLabyrinth/boss_murmur.cpp
  Outland/Auchindoun/ShadowLabyrinth/instance_shadow_labyrinth.cpp
  Outland/Auchindoun/ShadowLabyrinth/shadow_labyrinth.h
  Outland/boss_doomwalker.cpp
  Outland/zone_terokkar_forest.cpp
  Outland/zone_hellfire_peninsula.cpp
  Outland/boss_doomlord_kazzak.cpp
  Outland/BlackTemple/boss_teron_gorefiend.cpp
  Outland/BlackTemple/black_temple.h
  Outland/BlackTemple/illidari_council.cpp
  Outland/BlackTemple/boss_shade_of_akama.cpp
  Outland/BlackTemple/boss_supremus.cpp
  Outland/BlackTemple/black_temple.cpp
  Outland/BlackTemple/boss_mother_shahraz.cpp
  Outland/BlackTemple/instance_black_temple.cpp
  Outland/BlackTemple/boss_reliquary_of_souls.cpp
  Outland/BlackTemple/boss_warlord_najentus.cpp
  Outland/BlackTemple/boss_bloodboil.cpp
  Outland/BlackTemple/boss_illidan.cpp
  Outland/zone_shadowmoon_valley.cpp
  Outland/zone_blades_edge_mountains.cpp
  Outland/GruulsLair/boss_high_king_maulgar.cpp
  Outland/GruulsLair/boss_gruul.cpp
  Outland/GruulsLair/gruuls_lair.h
  Outland/GruulsLair/instance_gruuls_lair.cpp
  Outland/zone_netherstorm.cpp
  Outland/zone_zangarmarsh.cpp
)

message("  -> Prepared: Outland")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Pet/pet_dk.cpp
  Pet/pet_generic.cpp
  Pet/pet_hunter.cpp
  Pet/pet_mage.cpp
  #Pet/pet_monk.cpp
  Pet/pet_priest.cpp
  Pet/pet_shaman.cpp
  #Pet/pet_warlock.cpp
)

message("  -> Prepared: Pet")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  Spells/spell_shaman.cpp
  Spells/spell_hunter.cpp
  Spells/spell_rogue.cpp
  Spells/spell_druid.cpp
  Spells/spell_dk.cpp
  Spells/spell_quest.cpp
  Spells/spell_warrior.cpp
  Spells/spell_generic.cpp
  Spells/spell_warlock.cpp
  Spells/spell_priest.cpp
  Spells/spell_mage.cpp
  #Spells/spell_monk.cpp
  Spells/spell_mastery.cpp
  Spells/spell_paladin.cpp
  Spells/spell_item.cpp
  Spells/spell_holiday.cpp
  Spells/spell_pet.cpp
)

message("  -> Prepared: Spells")
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

set(scripts_STAT_SRCS
  ${scripts_STAT_SRCS}
  World/achievement_scripts.cpp
  World/areatrigger_scripts.cpp
  World/chat_log.cpp
  World/go_scripts.cpp
  World/guards.cpp
  World/item_scripts.cpp
  World/mob_generic_creature.cpp
  World/npc_innkeeper.cpp
  World/npc_professions.cpp
  World/npc_taxi.cpp
  World/npcs_special.cpp
)

message("  -> Prepared: World")
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

if( USE_COREPCH )
  include_directories(${CMAKE_CURRENT_BINARY_DIR})
endif()

file(GLOB_RECURSE sources_Configuration Configuration/*.cpp Configuration/*.h)
file(GLOB_RECURSE sources_Cryptography Cryptography/*.cpp Cryptography/*.h)
file(GLOB_RECURSE sources_Database Database/*.cpp Database/*.h)
file(GLOB_RECURSE sources_DataStores DataStores/*.cpp DataStores/*.h)
file(GLOB_RECURSE sources_Dynamic Dynamic/*.cpp Dynamic/*.h)
file(GLOB_RECURSE sources_Logging Logging/*.cpp Logging/*.h)
file(GLOB_RECURSE sources_Packets Packets/*.cpp Packets/*.h)
file(GLOB_RECURSE sources_Threading Threading/*.cpp Threading/*.h)
file(GLOB_RECURSE sources_Utilities Utilities/*.cpp Utilities/*.h)
file(GLOB sources_localdir *.cpp *.h)

source_group(CMake FILES CMakeLists.txt)
source_group(Configuration FILES ${sources_Configuration})
source_group(Cryptography FILES ${sources_Cryptography})
source_group(Database FILES ${sources_Database})
source_group(DataStores FILES ${sources_DataStores})
source_group(Dynamic FILES ${sources_Dynamic})
source_group(Logging FILES ${sources_Logging})
source_group(Packets FILES ${sources_Packets})
source_group(Threading FILES ${sources_Threading})
source_group(Utilities FILES ${sources_Utilities})
source_group(localdir FILES ${sources_localdir})

# Manually set sources for Debugging directory as we don't want to include WheatyExceptionReport in shared project
# It needs to be included both in authserver and worldserver for the static global variable to be properly initialized
# and to handle crash logs on windows
set(sources_Debugging Debugging/Errors.cpp Debugging/Errors.h)

#
# Build shared sourcelist
#

if (USE_COREPCH)
  set(shared_STAT_PCH_HDR PrecompiledHeaders/sharedPCH.h)
  set(shared_STAT_PCH_SRC PrecompiledHeaders/sharedPCH.cpp)
endif()

set(shared_STAT_SRCS
  ${shared_STAT_SRCS}
  ${sources_Configuration}
  ${sources_Cryptography}
  ${sources_Database}
  ${sources_DataStores}
  ${sources_Debugging}
  ${sources_Dynamic}
  ${sources_Logging}
  ${sources_Packets}
  ${sources_Threading}
  ${sources_Utilities}
  ${sources_localdir}
)

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Detour
  ${CMAKE_SOURCE_DIR}/dep/SFMT
  ${CMAKE_SOURCE_DIR}/dep/sockets/include
  ${CMAKE_SOURCE_DIR}/dep/utf8cpp
  ${CMAKE_SOURCE_DIR}/src/server
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/Configuration
  ${CMAKE_CURRENT_SOURCE_DIR}/Cryptography
  ${CMAKE_CURRENT_SOURCE_DIR}/Database
  ${CMAKE_CURRENT_SOURCE_DIR}/DataStores
  ${CMAKE_CURRENT_SOURCE_DIR}/Debugging
  ${CMAKE_CURRENT_SOURCE_DIR}/Dynamic
  ${CMAKE_CURRENT_SOURCE_DIR}/Logging
  ${CMAKE_CURRENT_SOURCE_DIR}/Packets
  ${CMAKE_CURRENT_SOURCE_DIR}/Threading
  ${CMAKE_CURRENT_SOURCE_DIR}/Utilities
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object
  ${ACE_INCLUDE_DIR}
  ${MYSQL_INCLUDE_DIR}
  ${OPENSSL_INCLUDE_DIR}
)

add_library(shared STATIC
  ${shared_STAT_SRCS}
  ${shared_STAT_PCH_SRC}
)

target_link_libraries(shared
  ${ACE_LIBRARY}
)

# Generate precompiled header
if (USE_COREPCH)
  add_cxx_pch(shared ${shared_STAT_PCH_HDR} ${shared_STAT_PCH_SRC})
endif ()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB_RECURSE sources_CommandLine CommandLine/*.cpp CommandLine/*.h)
file(GLOB_RECURSE sources_RemoteAccess RemoteAccess/*.cpp RemoteAccess/*.h)
file(GLOB_RECURSE sources_SFSoap SFSoap/*.cpp SFSoap/*.h)
file(GLOB_RECURSE sources_WorldThread WorldThread/*.cpp WorldThread/*.h)
file(GLOB sources_localdir *.cpp *.h)

source_group(CMake FILES CMakeLists.txt)
source_group(CommandLine FILES ${sources_CommandLine})
source_group(RemoteAcces FILES ${sources_RemoteAccess})
source_group(SFSoap FILES ${sources_SFSoap})
source_group(WorldThread FILES ${sources_WorldThread})
source_group(localdir FILES ${sources_localdir})

if (USE_COREPCH)
  set(worldserver_PCH_HDR PrecompiledHeaders/worldPCH.h)
  set(worldserver_PCH_SRC PrecompiledHeaders/worldPCH.cpp)
endif()

set(worldserver_SRCS
  ${worldserver_SRCS}
  ${sources_CommandLine}
  ${sources_RemoteAccess}
  ${sources_SFSoap}
  ${sources_WorldThread}
  ${sources_localdir}
)

if( WIN32 )
  set(worldserver_SRCS
    ${worldserver_SRCS}
    ${sources_windows_Debugging}
  )
  if ( MSVC )
    set(worldserver_SRCS
      ${worldserver_SRCS}
      worldserver.rc
    )
  endif()
endif()

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_SOURCE_DIR}/dep/g3dlite/include
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Detour
  ${CMAKE_SOURCE_DIR}/dep/gsoap
  ${CMAKE_SOURCE_DIR}/dep/sockets/include
  ${CMAKE_SOURCE_DIR}/dep/SFMT
  ${CMAKE_SOURCE_DIR}/src/server/collision
  ${CMAKE_SOURCE_DIR}/src/server/collision/Management
  ${CMAKE_SOURCE_DIR}/src/server/collision/Models
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Configuration
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography
  ${CMAKE_SOURCE_DIR}/src/server/shared/Cryptography/Authentication
  ${CMAKE_SOURCE_DIR}/src/server/shared/Database
  ${CMAKE_SOURCE_DIR}/src/server/shared/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic/LinkedReference
  ${CMAKE_SOURCE_DIR}/src/server/shared/Dynamic
  ${CMAKE_SOURCE_DIR}/src/server/shared/Logging
  ${CMAKE_SOURCE_DIR}/src/server/shared/Packets
  ${CMAKE_SOURCE_DIR}/src/server/shared/Threading
  ${CMAKE_SOURCE_DIR}/src/server/shared/Utilities
  ${CMAKE_SOURCE_DIR}/src/server/game
  ${CMAKE_SOURCE_DIR}/src/server/game/Accounts
  ${CMAKE_SOURCE_DIR}/src/server/game/Achievements
  ${CMAKE_SOURCE_DIR}/src/server/game/Addons
  ${CMAKE_SOURCE_DIR}/src/server/game/AI
  ${CMAKE_SOURCE_DIR}/src/server/game/AI/CoreAI
  ${CMAKE_SOURCE_DIR}/src/server/game/AI/ScriptedAI
  ${CMAKE_SOURCE_DIR}/src/server/game/AI/SmartScripts
  ${CMAKE_SOURCE_DIR}/src/server/game/AuctionHouse
  ${CMAKE_SOURCE_DIR}/src/server/game/AuctionHouse/AuctionHouseBot
  ${CMAKE_SOURCE_DIR}/src/server/game/Battlegrounds
  ${CMAKE_SOURCE_DIR}/src/server/game/Battlegrounds/Zones
  ${CMAKE_SOURCE_DIR}/src/server/game/Boost
  ${CMAKE_SOURCE_DIR}/src/server/game/Calendar
  ${CMAKE_SOURCE_DIR}/src/server/game/Chat
  ${CMAKE_SOURCE_DIR}/src/server/game/Chat/Channels
  ${CMAKE_SOURCE_DIR}/src/server/game/Combat
  ${CMAKE_SOURCE_DIR}/src/server/game/Conditions
  ${CMAKE_SOURCE_DIR}/src/server/game/DataStores
  ${CMAKE_SOURCE_DIR}/src/server/game/DungeonFinding
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/AreaTrigger
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Creature
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Corpse
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/DynamicObject
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/GameObject
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Item
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Item/Container
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Object/Updates
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Pet
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Player
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Totem
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Unit
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Vehicle
  ${CMAKE_SOURCE_DIR}/src/server/game/Entities/Transport
  ${CMAKE_SOURCE_DIR}/src/server/game/Events
  ${CMAKE_SOURCE_DIR}/src/server/game/Globals
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids/Cells
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids/Notifiers
  ${CMAKE_SOURCE_DIR}/src/server/game/Grids
  ${CMAKE_SOURCE_DIR}/src/server/game/Groups
  ${CMAKE_SOURCE_DIR}/src/server/game/Guilds
  ${CMAKE_SOURCE_DIR}/src/server/game/Handlers
  ${CMAKE_SOURCE_DIR}/src/server/game/Instances
  ${CMAKE_SOURCE_DIR}/src/server/game/Loot
  ${CMAKE_SOURCE_DIR}/src/server/game/Mails
  ${CMAKE_SOURCE_DIR}/src/server/game/Maps
  ${CMAKE_SOURCE_DIR}/src/server/game/Miscellaneous
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/MovementGenerators
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/Spline
  ${CMAKE_SOURCE_DIR}/src/server/game/Movement/Waypoints
  ${CMAKE_SOURCE_DIR}/src/server/game/OutdoorPvP
  ${CMAKE_SOURCE_DIR}/src/server/game/Pools
  ${CMAKE_SOURCE_DIR}/src/server/game/Quests
  ${CMAKE_SOURCE_DIR}/src/server/game/Reputation
  ${CMAKE_SOURCE_DIR}/src/server/game/Scripting
  ${CMAKE_SOURCE_DIR}/src/server/game/Server/Protocol
  ${CMAKE_SOURCE_DIR}/src/server/game/Server
  ${CMAKE_SOURCE_DIR}/src/server/game/Skills
  ${CMAKE_SOURCE_DIR}/src/server/game/Spells
  ${CMAKE_SOURCE_DIR}/src/server/game/Spells/Auras
  ${CMAKE_SOURCE_DIR}/src/server/game/Tools
  ${CMAKE_SOURCE_DIR}/src/server/game/Warden
  ${CMAKE_SOURCE_DIR}/src/server/game/Warden/Modules
  ${CMAKE_SOURCE_DIR}/src/server/game/Weather
  ${CMAKE_SOURCE_DIR}/src/server/game/World
  ${CMAKE_SOURCE_DIR}/src/server/authserver/Server
  ${CMAKE_SOURCE_DIR}/src/server/authserver/Realms
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/CommandLine
  ${CMAKE_CURRENT_SOURCE_DIR}/RemoteAccess
  ${CMAKE_CURRENT_SOURCE_DIR}/SFSoap
  ${CMAKE_CURRENT_SOURCE_DIR}/WorldThread
  ${ACE_INCLUDE_DIR}
  ${MYSQL_INCLUDE_DIR}
  ${OPENSSL_INCLUDE_DIR}
)

add_executable(worldserver
  ${worldserver_SRCS}
  ${worldserver_PCH_SRC}
)

if( NOT WIN32 )
  set_target_properties(worldserver PROPERTIES
    COMPILE_DEFINITIONS _SKYFIRE_CORE_CONFIG="${CONF_DIR}/worldserver.conf"
  )
endif()

add_dependencies(worldserver revision.h)

if( UNIX AND NOT NOJEM )
  set(worldserver_LINK_FLAGS "-pthread -lncurses ${worldserver_LINK_FLAGS}")
endif()

set_target_properties(worldserver PROPERTIES LINK_FLAGS "${worldserver_LINK_FLAGS}")

target_link_libraries(worldserver
  game
  shared
  scripts
  collision
  g3dlib
  gsoap
  Detour
  ${JEMALLOC_LIBRARY}
  ${READLINE_LIBRARY}
  ${TERMCAP_LIBRARY}
  ${ACE_LIBRARY}
  ${MYSQL_LIBRARY}
  ${OPENSSL_LIBRARIES}
  ${ZLIB_LIBRARIES}
  ${CMAKE_THREAD_LIBS_INIT}
)

if( WIN32 )
  if ( MSVC )
    add_custom_command(TARGET worldserver
      POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/worldserver.conf.dist ${CMAKE_BINARY_DIR}/bin/$(ConfigurationName)/
    )
  elseif ( MINGW )
    add_custom_command(TARGET worldserver
      POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/worldserver.conf.dist ${CMAKE_BINARY_DIR}/bin/
    )
  endif()
endif()

if( UNIX )
  install(TARGETS worldserver DESTINATION bin)
  install(FILES worldserver.conf.dist DESTINATION ${CONF_DIR})
elseif( WIN32 )
  install(TARGETS worldserver DESTINATION "${CMAKE_INSTALL_PREFIX}")
  install(FILES worldserver.conf.dist DESTINATION "${CMAKE_INSTALL_PREFIX}")
endif()

# Generate precompiled header
if( USE_COREPCH )
  add_cxx_pch(worldserver ${worldserver_PCH_HDR} ${worldserver_PCH_SRC})
endif()
# Copyright (C) 2011-2019 Project SkyFire <http://www.projectskyfire.org/
# Copyright (C) 2008-2019 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


add_subdirectory(map_extractor)
add_subdirectory(mmaps_generator)
add_subdirectory(vmap4_assembler)
add_subdirectory(vmap4_extractor)
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB_RECURSE sources *.cpp *.h)

include_directories (
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/dep/StormLib/src
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/loadlib
)

include_directories(${include_Dirs})

add_executable(mapextractor
  ${sources}
)

target_link_libraries(mapextractor
  ${BZIP2_LIBRARIES}
  ${ZLIB_LIBRARIES}
  storm
)

add_dependencies(mapextractor storm)

if( UNIX )
  install(TARGETS mapextractor DESTINATION bin)
elseif( WIN32 )
  install(TARGETS mapextractor DESTINATION "${CMAKE_INSTALL_PREFIX}")
endif()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB_RECURSE mmap_gen_sources *.cpp *.h)

set(mmap_gen_Includes
  ${CMAKE_BINARY_DIR}
  ${ACE_INCLUDE_DIR}
  ${CMAKE_SOURCE_DIR}/dep/libmpq
  ${CMAKE_SOURCE_DIR}/dep/zlib
  ${CMAKE_SOURCE_DIR}/dep/bzip2
  ${CMAKE_SOURCE_DIR}/dep/g3dlite/include
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Recast
  ${CMAKE_SOURCE_DIR}/dep/recastnavigation/Detour
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/game/Conditions
  ${CMAKE_SOURCE_DIR}/src/server/collision
  ${CMAKE_SOURCE_DIR}/src/server/collision/Management
  ${CMAKE_SOURCE_DIR}/src/server/collision/Maps
  ${CMAKE_SOURCE_DIR}/src/server/collision/Models
)

if( WIN32 )
  set(mmap_gen_Includes
    ${mmap_gen_Includes}
    ${CMAKE_SOURCE_DIR}/dep/libmpq/win
    )
endif()

include_directories(${mmap_gen_Includes})

add_executable(mmaps_generator ${mmap_gen_sources})

target_link_libraries(mmaps_generator
  collision
  g3dlib
  Recast
  Detour
  ${ACE_LIBRARY}
  ${BZIP2_LIBRARIES}
  ${ZLIB_LIBRARIES}
)

if( UNIX )
  install(TARGETS mmaps_generator DESTINATION bin)
elseif( WIN32 )
  install(TARGETS mmaps_generator DESTINATION "${CMAKE_INSTALL_PREFIX}")
endif()
Generator command line args

--threads           [#]             Max number of threads used by the generator
                                    Default: 3

--offMeshInput      [file.*]        Path to file containing off mesh connections data.
                                    Format must be: (see offmesh_example.txt)
                                    "map_id tile_x,tile_y (start_x start_y start_z) (end_x end_y end_z) size  //optional comments"
                                    Single mesh connection per line.

--silent            []              Make us script friendly. Do not wait for user input
                                    on error or completion.

--bigBaseUnit       [true|false]    Generate tile/map using bigger basic unit.
                                    Use this option only if you have unexpected gaps.

                                    false: use normal metrics (default)

--maxAngle          [#]             Max walkable inclination angle

                                    float between 45 and 90 degrees (default 60)

--skipLiquid        [true|false]    extract liquid data for maps

                                    false: include liquid data (default)

--skipContinents    [true|false]    continents are maps 0 (Eastern Kingdoms),
                                    1 (Kalimdor), 530 (Outlands), 571 (Northrend)

                                    false: build continents (default)

--skipJunkMaps      [true|false]    junk maps include some unused
                                    maps, transport maps, and some other

                                    true: skip junk maps (default)

--skipBattlegrounds [true|false]    does not include PVP arenas

                                    false: skip battlegrounds (default)

--debugOutput       [true|false]    create debugging files for use with RecastDemo
                                    if you are only creating mmaps for use with MaNGOS,
                                    you don't want debugging files

                                    false: don't create debugging files (default)

--tile              [#,#]           Build the specified tile
                                    seperate number with a comma ','
                                    must specify a map number (see below)
                                    if this option is not used, all tiles are built

                    [#]             Build only the map specified by #
                                    this command will build the map regardless of --skip* option settings
                                    if you do not specify a map number, builds all maps that pass the filters specified by --skip* options


examples:

movement_extractor
builds maps using the default settings (see above for defaults)

movement_extractor --skipContinents true
builds the default maps, except continents

movement_extractor 0
builds all tiles of map 0

movement_extractor 0 --tile 34,46
builds only tile 34,46 of map 0 (this is the southern face of blackrock mountain)
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

include_directories(
  ${CMAKE_SOURCE_DIR}/dep/g3dlite/include
  ${CMAKE_SOURCE_DIR}/src/server/shared
  ${CMAKE_SOURCE_DIR}/src/server/shared/Debugging
  ${CMAKE_SOURCE_DIR}/src/server/collision
  ${CMAKE_SOURCE_DIR}/src/server/collision/Maps
  ${CMAKE_SOURCE_DIR}/src/server/collision/Models
  ${ACE_INCLUDE_DIR}
  ${ZLIB_INCLUDE_DIR}
)

add_executable(vmap4assembler VMapAssembler.cpp)
add_dependencies(vmap4assembler storm)

target_link_libraries(vmap4assembler
  collision
  g3dlib
  ${ZLIB_LIBRARIES}
)

if( UNIX )
  install(TARGETS vmap4assembler DESTINATION bin)
elseif( WIN32 )
  install(TARGETS vmap4assembler DESTINATION "${CMAKE_INSTALL_PREFIX}")
endif()
# Copyright (C) 2011-2020 Project SkyFire <http://www.projectskyfire.org/>
# Copyright (C) 2008-2020 TrinityCore <http://www.trinitycore.org/>
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

file(GLOB_RECURSE sources *.cpp *.h)

# uncomment next line to disable debug mode
add_definitions("-DIOMAP_DEBUG")

# build setup currently only supports libmpq 0.4.x
if( NOT MSVC )
  add_definitions("-Wall")
  add_definitions("-ggdb")
  add_definitions("-O3")
endif()

include_directories(
  ${CMAKE_SOURCE_DIR}/dep/StormLib/src
)

add_executable(vmap4extractor ${sources})

target_link_libraries(vmap4extractor
  ${BZIP2_LIBRARIES}
  ${ZLIB_LIBRARIES}
  storm
)

add_dependencies(vmap4extractor storm)

if( UNIX )
  install(TARGETS vmap4extractor DESTINATION bin)
elseif( WIN32 )
  install(TARGETS vmap4extractor DESTINATION "${CMAKE_INSTALL_PREFIX}")
endif()
