Building Silence
================

Basics
------

Silence uses [Gradle](http://gradle.org) to build the project and to maintain
dependencies.

Building Silence
----------------

The following steps should help you (re)build Silence from the command line.

1. Checkout the source somewhere on your filesystem with

        git clone --recursive https://git.silence.dev/Silence/Silence-Android.git

2. Make sure you have the [Android SDK](https://developer.android.com/sdk/index.html) installed somewhere on your system.
3. Ensure that the following packages are installed from the Android SDK manager:
    * Android SDK Build Tools
    * SDK Platform
    * Android Support Repository
    * Google Repository
4. Create a local.properties file at the root of your source checkout and add an sdk.dir entry to it.

        sdk.dir=\<path to your sdk installation\>

5. (Optional) Build [Gradle-Witness](https://git.silence.dev/Silence/gradle-witness)

        ./scripts/build-witness.sh

6. Execute Gradle:

        ./gradlew assembleDebug

If you get a `Configuration with name 'default' not found.`, please update submodules:

        git submodule init && git submodule update

Visual assets
-------------

Sample command for generating our audio placeholder image:

```bash
pngs_from_svg.py ic_audio.svg /path/to/Silence/res/ 150 --color #000 --opacity 0.54 --suffix _light
pngs_from_svg.py ic_audio.svg /path/to/Silence/res/ 150 --color #fff --opacity 1.00 --suffix _light
```


Translations
------------

Translations are available on [Weblate](https://translate.silence.dev) and automatically updated in the source code. Make sure you run on the latest `master` revision.

Setting up a development environment
------------------------------------

[Android Studio](https://developer.android.com/sdk/installing/studio.html) is the recommended development environment.

1. Install Android Studio.
2. Make sure the "Android Support Repository" is installed in the Android Studio SDK.
3. Make sure the latest "Android SDK build-tools" is installed in the Android Studio SDK.
4. Create a new Android Studio project. from the Quickstart pannel (use File > Close Project to see it), choose "Checkout from Version Control" then "git".
5. Paste the URL for the Silence project when prompted (https://github.com/SilenceIM/Silence.git).
6. Android studio should detect the presence of a project file and ask you whether to open it. Click "yes".
7. Default config options should be good enough.
8. Project initialisation and build should proceed.

Contributing code
-----------------

Code contributions should be sent via GitLab as merge requests, from feature branches.
# Silence Changelog

### [0.15.16] - 2019-08-28
- Improved local encryption
- Fixed duplicated MMS settings
- Added notifications channels
- Updated translations

### [0.15.15] - 2019-08-23
- Fixed infinite loop when sending MMS messages
- Fixed crash when receiving encrypted MMS message
- Updated translations

### [0.15.14] - 2019-08-17
- Improved MMS support and quality of scaled images
- Added Android Auto support
- Added UI fixes on failed messages
- Added selective permissions
- Improved welcome screen
- Added option to always ask for the SIM card to use to send a message
- Updated translations

### [0.15.13] - 2018-03-23
- Fixed logs sending
- Added option to share key fingerprint
- Minor UI fixes
- Updated translations

### [0.15.12] - 2018-02-19
- Added option to hide "new message" separator
- Updated APNs with fix for Free Mobile (FR)
- Switched to a new way to receive encrypted messages (started in v0.15.9)
- Updated translations

### [0.15.11] - 2018-01-04
- Fixed persistent crash when downloading some MMS messages
- Updated translations

### [0.15.10] - 2017-11-30
- Fixed crash on some devices when exporting data
- Added fallback to ROM's emojis
- Updated translations

### [0.15.9] - 2017-11-20
- Switched to a new way to send encrypted messages
- Updated translations

### [0.15.8] - 2017-10-05
- Updated emojis to Android O
- Improved build reproducibility
- Fixed crash on malformed messages
- Enabled incognito keyboard mode by default
- Removed cleartext password that may leak
- Enabled Czech and Portuguese (Brazil) languages
- Updated translations

### [0.15.7] - 2017-04-21
- Fixed crash on malformed encrypted messages
- Updated translations

### [0.15.6] - 2017-03-29
- Moved from Axolotl to Signal protocol
- Fixed crash when opening a conversation
- Added fallback to legacy MMS API on failure
- Added minor UI improvements
- Fixed minor bugs
- Removed dead code
- Updated translations

### [0.15.5] - 2017-03-16
- Fixed glitch with "Secure session ended" items
- Updated translations

### [0.15.4] - 2017-03-14
- Fixed build
- Updated translations

### [0.15.3] - 2017-03-14
- Added link to our Privacy policy in Settings
- Added "New messages" divider
- Linkified geo: and xmpp: URIs
- Fixed occasional crash on Android 7 quick reply
- Updated translations

### [0.15.2] - 2017-02-22
- Fixed button to download MMS messages
- Updated translations

### [0.15.1] - 2017-02-19
- Fixed build

### [0.15.0] - 2017-02-18
- Added missing emojis flags
- Added widget with unread messages count
- Added support for image keyboard
- Added Android N bundled notifications and quick reply
- Added support for direct share targets
- Added sticky date headers
- Added scroll-to-bottom button
- Updated translations
- Minor bugs fixes

### [0.14.8] - 2016-12-30
- Fixed emoji's support with Android <= 6.1
- Updated emojis, added flags
- Updated translations

### [0.14.7] - 2016-12-28
- Fixed issues with vibration of notifications when Silence is unlocked
- Added button to send drafts from main screen
- Updated emojis
- Updated translations

### [0.14.6] - 2016-12-06
- Fixed notifications when Silence is locked

### [0.14.5] - 2016-12-04
- Fixed notification lights with encrypted messages
- Updated translations

### [0.14.4] - 2016-11-29
- Fixed notifications with Android N
- Prepared for upcoming XMPP transport
- Added reminder to enable delivery reports
- Fixed privacy settings with Android < 5
- Fixed SMS characters calculation
- Updated APN database
- Updated translations
- Fixed lots of minor bugs

### [0.14.3] - 2016-05-14
- Fixed blocked MMS download

### [0.14.2] - 2016-05-13
- Fixed MMS issues with Android 4.x
- Updated translations

### [0.14.1] - 2016-04-25
- Fixed APN issues
- Updated translations

### [0.14.0] - 2016-04-23
- SMSSecure is now Silence
- Added new emojis
- Added support for multi-SIM phones
- Added encrypted backups
- Fixed strings
- Updated APN database
- Updated translations

### [0.13.2] - 2016-02-07
- Fixed keyboard/focus regressions
- Fixed debug logs
- Fixed click interception on failed messages
- Fixed silent in-thread notification
- Fixed notification LED and sound
- Fixed contact sorting
- Fixed crash on invalid image
- Fixed database migration from 0.12.3 to 0.13.1
- Updated APN database
- Added Esperanto translation
- Updated translations

### [0.13.1] - 2016-01-20
- Fixed crash on Gingerbread
- Fixed some issues with RTL languages
- Updated translations

### [0.13.0] - 2015-12-23
- Added support for archive actions
- Improved UI
- Improved MMS support for Android 5+
- Fixed lots of bugs

### [0.12.3] - 2015-10-08
- Improved settings
- Fixed bugs
- Updated translations

### [0.12.1] - 2015-10-07
- Added MMS download controls
- Improved MMS requests
- Fixed bugs
- Updated translations

### [0.11.3] - 2015-09-23
- Fixed bugs
- Updated translations

### [0.11.0] - 2015-09-15
- Added GIF support
- Added new options
- Fixed bugs
- Updated translations

### [0.10.1] - 2015-07-16
- Added a new, more "material" UI
- Added support for per-contact options
- Fixed bugs
- Updated translations

### [0.9.0] - 2015-06-02
- Added support for direct photo capture
- Fixed ANR on certain devices
- Updated emoji set
- Fixed bugs
- Updated translations

### [0.8.1] - 2015-05-13
- Fixed manual key exchange completion
- Fixed occasional generated avatar mis-sizing in conversation
- Updated translations

### [0.8.0] - 2015-05-12
- Added a generated avatar for contacts without pictures
- Fixed emoji drawer bugs
- Fixed crash in AppCompat

### [0.7.0] - 2015-05-07
- Added support for Android Wear
- Added support for Lollipop-style notifications
- Improved encrypted message detection (for using as non-default SMS app)
- Fixed bugs

### [0.6.0] - 2015-04-14
- Fixed key exchanges being blue while pending
- Fixed crash when username was null in MMS auth
- Improved handling of requests to end non-existing sessions
- Updated translations

### [0.5.4] - 2015-04-09
- Removed `READ_CALL_LOG` permission
- Fixed Norwegian localization issues
- Fixed problem with upgrading the database

### [0.5.3] - 2015-04-07
- Fixed crash on upgrading

### [0.5.2] - 2015-04-05
- Fixed bugs

### [0.5.1] - 2015-04-02
- Removed more push-related code
- Fixed MMS crash

### [0.4.2] - 2015-03-31
- Added ability to import TextSecure backups

### [0.4.1] - 2015-03-31
- Added new icon

### [0.4.0] - 2015-03-30
- Fixed bugs
- Removed TextSecure push-related code and strings

### [0.3.3] - 2015-03-22
- Renamed project to SMSSecure at the request of Moxie (TextSecure dev)

### [0.3.2] - 2015-03-21
- Fixed crash

### [0.3.1] - 2015-03-20
- Added the ability to install SecuredText alongside TextSecure

### [0.3.0] - 2015-03-19
- Fixed bugs

### [0.2.0] - 2015-03-19
- Initial fork
- Changed app name
- Removed non-free libraries

 [0.15.16]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.15...v0.15.16
 [0.15.15]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.14...v0.15.15
 [0.15.14]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.13...v0.15.14
 [0.15.13]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.12...v0.15.13
 [0.15.12]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.11...v0.15.12
 [0.15.11]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.10...v0.15.11
 [0.15.10]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.9...v0.15.10
 [0.15.9]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.8...v0.15.9
 [0.15.8]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.7...v0.15.8
 [0.15.7]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.6...v0.15.7
 [0.15.6]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.5...v0.15.6
 [0.15.5]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.4...v0.15.5
 [0.15.4]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.3...v0.15.4
 [0.15.3]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.2...v0.15.3
 [0.15.2]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.1...v0.15.2
 [0.15.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.15.0...v0.15.1
 [0.15.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.8...v0.15.0
 [0.14.8]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.7...v0.14.8
 [0.14.7]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.6...v0.14.7
 [0.14.6]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.5...v0.14.6
 [0.14.5]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.4...v0.14.5
 [0.14.4]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.3...v0.14.4
 [0.14.3]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.2...v0.14.3
 [0.14.2]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.1...v0.14.2
 [0.14.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.14.0...v0.14.1
 [0.14.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.13.2...v0.14.0
 [0.13.2]: https://git.silence.dev/Silence/Silence-Android/compare/v0.13.1...v0.13.2
 [0.13.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.13.0...v0.13.1
 [0.13.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.12.3...v0.13.0
 [0.12.3]: https://git.silence.dev/Silence/Silence-Android/compare/v0.12.1...v0.12.3
 [0.12.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.11.3...v0.12.1
 [0.11.3]: https://git.silence.dev/Silence/Silence-Android/compare/v0.11.1...v0.11.3
 [0.11.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.10.1...v0.11.1
 [0.10.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.9.0...v0.10.1
 [0.9.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.8.1...v0.9.0
 [0.8.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.8.0...v0.8.1
 [0.8.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.7.0...v0.8.0
 [0.7.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.6.0...v0.7.0
 [0.6.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.5.4...v0.6.0
 [0.5.4]: https://git.silence.dev/Silence/Silence-Android/compare/v0.5.3...v0.5.4
 [0.5.3]: https://git.silence.dev/Silence/Silence-Android/compare/v0.5.2...v0.5.3
 [0.5.2]: https://git.silence.dev/Silence/Silence-Android/compare/v0.5.1...v0.5.2
 [0.5.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.4.2...v0.5.1
 [0.4.2]: https://git.silence.dev/Silence/Silence-Android/compare/v0.4.1...v0.4.2
 [0.4.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.4.0...v0.4.1
 [0.4.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.3.3...v0.4.0
 [0.3.3]: https://git.silence.dev/Silence/Silence-Android/compare/v0.3.2...v0.3.3
 [0.3.2]: https://git.silence.dev/Silence/Silence-Android/compare/v0.3.1...v0.3.2
 [0.3.1]: https://git.silence.dev/Silence/Silence-Android/compare/v0.3.0...v0.3.1
 [0.3.0]: https://git.silence.dev/Silence/Silence-Android/compare/v0.2.0...v0.3.0
 [0.2.0]: https://git.silence.dev/Silence/Silence-Android/compare/ac92fa6f5e1f86da833b38aa5955b685e1959846...v0.2.0
## Translations

Please do not submit issues or pull requests for translation fixes. Anyone can update the translations in [Weblate](https://translate.silence.dev).
Please submit your corrections there.


## Submitting bug reports

1. Search our issues first to make sure this is not a duplicate.
2. (Optional) Search [Signal's issues](https://github.com/WhisperSystems/Signal-Android/issues).
3. Open an issue and follow the template carefully. If you can't get a debug log from Settings, you can use ADB to grab it: `adb logcat | grep $(adb shell ps | grep org.smssecure.smssecure | tr -s " " | cut -d " " -f2)`.

## Submitting merge requests

All useful MRs are accepted. Please respect [our template](https://git.silence.dev/Silence/Silence-Android/blob/master/.gitlab/merge_request_templates/Merge Request.md) and ask to merge your commits in `unstable` (PRs in `master` will be closed).
                    GNU GENERAL PUBLIC LICENSE
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
# Silence [![Build Status](https://travis-ci.org/SilenceIM/Silence.svg?branch=master)](https://travis-ci.org/SilenceIM/Silence)

[Silence](https://silence.im) (formerly SMSSecure) is an SMS/MMS application that allows you to protect your privacy while communicating with friends.

Using Silence, you can send SMS messages and share media or attachments with complete privacy.

[![Get it on F-Droid](https://silence.im/images/fdroid-github.png)](https://f-droid.org/app/org.smssecure.smssecure)
[![Get it on Google Play](https://silence.im/images/play-github.png)](https://play.google.com/store/apps/details?id=org.smssecure.smssecure)

Features:
* Easy. Silence works like any other SMS application. There's nothing to sign up for and no new service your friends need to join.
* Reliable. Silence communicates using encrypted SMS messages. No servers or internet connection required.
* Private. Silence uses the Signal encryption protocol to provide privacy for every message, every time.
* Safe. All messages are encrypted locally, so if your phone is lost or stolen, your messages are protected.
* Open Source. Silence is Free and Open Source, enabling anyone to verify its security by auditing the code.


## Project goals

This is a fork of [TextSecure](https://github.com/WhisperSystems/TextSecure) (now Signal) that aims to keep the SMS encryption that TextSecure removed [for a variety of reasons](https://whispersystems.org/blog/goodbye-encrypted-sms/).

Silence focuses on SMS and MMS. This fork aims to:

* Keep SMS/MMS encryption
* Drop Google services dependencies (push messages are not available in Silence)
* Integrate upstream bugfixes and patches from TextSecure

# Contributing

See [CONTRIBUTING.md](https://git.silence.dev/Silence/Silence-Android/blob/master/CONTRIBUTING.md) for how to contribute code, translations, or bug reports.

Instructions on how to setup a development environment and build Silence can be found in [BUILDING.md](https://git.silence.dev/Silence/Silence-Android/blob/master/BUILDING.md).

# Donate

We accept Bitcoin donations. This will help us to pay various costs (web hosting, domain name, etc.). Our Bitcoin address is:

```
1LoKZXg3bx6kfwAhEFQqS9pgeCE1CFMEJb
```

# Help
## Documentation
Looking for documentation? Check out the wiki of the original project:

https://github.com/WhisperSystems/TextSecure/wiki

## Chat
Have a question? Want to help out? Join us on Mattermost on [chat.silence.dev](https://chat.silence.dev/), or follow [@SilenceIM](https://twitter.com/SilenceIM) on Twitter or [@silence@mastodon.social](https://mastodon.social/@silence) on Mastodon.

# Legal
## Cryptography Notice

This distribution includes cryptographic software. The country in which you currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software.
BEFORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted.
See <http://www.wassenaar.org/> for more information.

## License

Licensed under the GPLv3: http://www.gnu.org/licenses/gpl-3.0.html
### Bug description
<!--
A detailed description of the bug. More information is better.
Be sure to include any extra information about your device that could be a factor.
Also include the value of any relevant preferences you have set in the app.
-->

### How to reproduce
- using hyphens as bullet points
- list the steps
- that reproduce the bug.

**Actual result:** Describe here what happens after you run the steps above (i.e. the buggy behaviour)
**Expected result:** Describe here what should happen after you run the steps above (i.e. what would be the correct behaviour)

### Screenshots
<!-- You can drag and drop images here -->

### Device info
- Device:
- Android version:
- Silence version:

### Link to debug log
<!--
Immediately after the bug has happened capture a debug log via Settings -> Advanced -> Submit log and paste the link here.
If you can't access the menu, you can use ADB to grab the debug log: `adb logcat | grep $(adb shell ps | grep org.smssecure.smssecure | tr -s " " | cut -d " " -f2)`.
If your debug log contains sensitive data, you can censor it (please don't remove any relevant data) or send it to support@silence.im instead
-->
<!-- Please ensure that:
- You are requesting `unstable` as base branch
- You have followed the Code Style Guidelines: https://github.com/WhisperSystems/Signal-Android/wiki/Code-Style-Guidelines
- Your contribution is ready to be merged as is
-->

### Description
<!--
Describe briefly what your pull request proposes to fix. Especially if you have more than one commit, it is helpful to give a summary of what your contribution as a whole is trying to solve. You can also use the `fixes #1234` syntax to refer to specific issues either here or in your commit message.
Also, please describe shortly how you tested that your fix actually works and the devices you tested it on.
-->
- Fixed crash on upgrading
- Removed `READ_CALL_LOG` permission
- Fixed Norwegian localization issues
- Fixed problem with upgrading the database
- Fixed key exchanges being blue while pending
- Fixed crash when username was null in MMS auth
- Improved handling of requests to end non-existing sessions
- Updated translations
- Added support for Android Wear
- Added support for Lollipop-style notifications
- Improved encrypted message detection (for using as non-default SMS app)
- Fixed bugs
- Added a generated avatar for contacts without pictures
- Fixed emoji drawer bugs
- Fixed crash in AppCompat
- Fixed manual key exchange completion
- Fixed occasional generated avatar mis-sizing in conversation
- Updated translations
- Added support for direct photo capture
- Fixed ANR on certain devices
- Updated emoji set
- Fixed bugs
- Updated translations
- Added a new, more "material" UI
- Added support for per-contact options
- Fixed bugs
- Updated translations
- Added GIF support
- Added new options
- Fixed bugs
- Updated translations
- Removed more push-related code
- Fixed MMS crash
- Fixed bugs
- Updated translations
- Added MMS download controls
- Improved MMS requests
- Fixed bugs
- Updated translations
- Improved settings
- Fixed bugs
- Updated translations
- Added support for archive actions
- Improved UI
- Improved MMS support for Android 5+
- Fixed lots of bugs
- Fixed crash on Gingerbread
- Fixed some issues with RTL languages
- Updated translations
- Fixed keyboard/focus regressions
- Fixed debug logs
- Fixed click interception on failed messages
- Fixed silent in-thread notification
- Fixed notification LED and sound
- Fixed contact sorting
- Fixed crash on invalid image
- Fixed database migration from 0.12.3 to 0.13.1
- Updated APN database
- Added Esperanto translation
- Updated translations
- Fixed bugs
- SMSSecure is now Silence
- Added new emojis
- Added support for multi-SIM phones
- Added encrypted backups
- Fixed strings
- Updated APN database
- Updated translations
- Fixed APN issues
- Updated translations
- Fixed MMS issues with Android 4.x
- Updated translations
- Fixed blocked MMS download
- Fixed notifications with Android N
- Prepared for upcoming XMPP transport
- Added reminder to enable delivery reports
- Fixed privacy settings with Android < 5
- Fixed SMS characters calculation
- Updated APN database
- Updated translations
- Fixed lots of minor bugs
- Fixed notification lights with encrypted messages
- Updated translations
- Fixed notifications when Silence is locked
- Fixed issues with vibration of notifications when Silence is unlocked
- Added button to send drafts from main screen
- Updated emojis
- Updated translations
- Added missing emojis flags
- Added widget with unread messages count
- Added support for image keyboard
- Added Android N bundled notifications and quick reply
- Added support for direct share targets
- Added sticky date headers
- Added scroll-to-bottom button
- Updated translations
- Minor bugs fixes
- Fixed build
- Fixed button to download MMS messages
- Updated translations
- Added link to our Privacy policy in Settings
- Added "New messages" divider
- Linkified geo: and xmpp: URIs
- Fixed occasional crash on Android 7 quick reply
- Updated translations
- Fixed build
- Updated translations
- Fixed glitch with "Secure session ended" items
- Updated translations
- Moved from Axolotl to Signal protocol
- Fixed crash when opening a conversation
- Added fallback to legacy MMS API on failure
- Added minor UI improvements
- Fixed minor bugs
- Removed dead code
- Updated translations
- Fixed crash on malformed encrypted messages
- Updated translations
- Updated emojis to Android O
- Improved build reproducibility
- Fixed crash on malformed messages
- Enabled incognito keyboard mode by default
- Removed cleartext password that may leak
- Enabled Czech and Portuguese (Brazil) languages
- Updated translations
- Switched to a new way to send encrypted messages
- Updated translations
- Fixed crash on some devices when exporting data
- Added fallback to ROM's emojis
- Updated translations
- Fixed persistent crash when downloading some MMS messages
- Updated translations
- Added option to hide "new message" separator
- Updated APNs with fix for Free Mobile (FR)
- Switched to a new way to receive encrypted messages (started in v0.15.9)
- Updated translations
- Fixed logs sending
- Added option to share key fingerprint
- Minor UI fixes
- Updated translations
- Improved MMS support and quality of scaled images
- Added Android Auto support
- Added UI fixes on failed messages
- Added selective permissions
- Improved welcome screen
- Added option to always ask for the SIM card to use to send a message
- Updated translations
- Fixed infinite loop when sending MMS messages
- Fixed crash when receiving encrypted MMS message
- Updated translations
- Improved local encryption
- Fixed duplicated MMS settings
- Added notifications channels
- Updated translations
- Fixed bugs
- Removed TextSecure push-related code and strings
- Added new icon
- Added ability to import TextSecure backups
argparse>=1.2.1
lxml>=3.3.3
progressbar-latest>=2.4
# emoji-extractor

This bunch of scripts allows you to:

 * Extract emojis from `NotoColorEmoji.ttf` (can be found in Android Source Code)
 * Remove useless margins of extracted emojis
 * Generate sprites from `emoji-categories.xml` with extracted emojis

Note: `gen-sprite.py` will generate a list of emojis included in sprites. To get escaped strings for Java, run `native2ascii -encoding utf8 input.txt output.java.txt`
TTF/OTF tables data

name:							font metadata
cmap.cmap_format_12:					name <-> unicode
CBDT.strikedata.cbdt_format_18:				name <-> data
CBLC.strike.eblc_index_sub_table_1:			id <-> name
GSUB.LookupList.Lookup.LigatureSubst.LigatureSet:	name <-> components <-> glyph
