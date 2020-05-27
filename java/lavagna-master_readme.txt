# Changelog

## 1.1.4

 - Update dependencies (see https://github.com/digitalfondue/lavagna/pull/126, thank you @ejouvin)

## 1.1.3 (2019-11-22)

 - Update login with google (see https://github.com/digitalfondue/lavagna/commit/eae861ce972c89f6f74189d14440066a99a28264)
 - Update dependencies

## 1.1.2 (2018-07-20)

 - Fix download export for Firefox (see https://github.com/digitalfondue/lavagna/issues/107)
 - Add the possibility to configure lavagna from properties/file (see https://github.com/digitalfondue/lavagna/issues/108)

## 1.1.1 (2018-06-17)

 - Update dependencies
 - Fix html email issue (see https://github.com/digitalfondue/lavagna/issues/103)
 - Fix card d&d with the role only defined at the project level (see https://github.com/digitalfondue/lavagna/issues/105)

## 1.1 (2018-04-09)

 - Cleanup documentation. Stable release.

## 1.1-M8 (2018-02-20)

 - Remove the HSTS filter (see https://github.com/digitalfondue/lavagna/issues/97#issuecomment-366937891), updated dependencies.

## 1.1-M7 (2017-08-16)

 - Fix the "email to card" feature, updated dependencies.

## 1.1-M6 (2017-07-03)

 - Fixes, updated dependencies, add a more complete "create new card" functionality
 
## 1.0.7.4 (2017-07-03)

 - Updated dependencies, fix for tomcat

## 1.1-M5 (2017-04-05)

 - Fixes, improvements in the "email to card" feature.

## 1.1-M4 (2017-04-03)

 - Fixes, UI/UX improvements and "email to card" feature.

## 1.0.7.3 (2017-03-06)

 - Fix check ldap functionality and print more diagnostic information in the ui

## 1.1-M3 (2017-02-20)

 - Update the pre-release. Fixes and updates.

## 1.1-M2 (2017-02-09)

 - Update the pre-release. Multiple fixes and improvements.

## 1.1-M1 (2016-10-06)

 - Update the pre-release: ui/ux fixes.

## 1.0.7.2 (2016-10-06)

 - fix java7 compatibility

## 1.1-M0 (2016-10-02)

 - first pre-release of the 1.1 version. The user interface and experience has been completely revisited

## 1.0.7.1 (2016-10-02)

 - fix clone card issue (duplicated comments)
 - update dependencies

## 1.0.7 (2016-08-28)

 - better performance when handling boards with many custom labels or more than 200 cards
 - export an entire project to Excel
 - reworked the milestones in order to improve their usefulness 
   - milestone's detail page
   - improved cards list with "Column" and "Assigned to" columns
   - export a milestone to Excel 

## 1.0.6.2 (2016-03-28)

 - fix unsubscribe mechanism in stomp-client wrapper

## 1.0.6.1 (2016-03-25)

 - clone card functionality
 - milestones can have a release date
 - misc. minor UI/UX improvements
 - improved performances
 - updated libraries

(note: the 1.0.6 release has been skipped due to an error in the dependencies).

## 1.0.5.2 (2016-01-12)

 - fix file upload issue when a user don't have a global READ role.
 - misc minor UI/UX improvements

## 1.0.5.1 (2015-11-16)

 - Fix XSS issue in the file upload section (require an authenticated user)

## 1.0.5 (2015-11-07)

 - UI/UX improvements
   - change due date color based on the current date
   - card label: on mouse hover, show a tooltip with the card name
   - email notification: now the user can choose to receive only changes made by other users

## 1.0.4.1 (2015-10-19)

 - update dependencies ([spring framework](https://spring.io/blog/2015/10/15/spring-framework-4-2-2-4-1-8-and-3-2-15-available-now) due to a possible security issue)

## 1.0.4 (2015-09-15)

 - [#8](https://github.com/digitalfondue/lavagna/issues/8) implement gitlab support for gitlab.com and self hosted instances
 - updates some libraries
 - refactor part of the login system

## 1.0.3 (2015-09-01)

 - fix issue [#13](https://github.com/digitalfondue/lavagna/issues/13)
 - iCalendar feed support
 - update to spring 4.2.x
 - switch connection pool to hikaricp (simplify configuration)
 - use the browser locale for showing the correct first day of the week in the calendar (sunday or monday)

## 1.0.2 (2015-08-14)

 - Tomcat 7/8 fix as found in issue [#12](https://github.com/digitalfondue/lavagna/issues/12)

## 1.0.1 (2015-08-14)

 - IE related fix [1e4980e](https://github.com/digitalfondue/lavagna/commit/1e4980e9c3ef4a7a84dafe9a0088be361d90a1b1)
 - Update the search result after closing a card [1dfdb3e](https://github.com/digitalfondue/lavagna/commit/1dfdb3e5b02afad349b987099ac923038f7ed901)
 - Define the correct content types for the fonts [10d6e66](https://github.com/digitalfondue/lavagna/commit/10d6e66f9707093122d82b28ef54e6e87c85ae39)
 - Fix typo in doc [71b79be](https://github.com/digitalfondue/lavagna/commit/71b79bebafb62c0485a0870d96db0612d4297803)


## 1.0 (2015-08-05)

 - stable release
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
Lavagna
======

[![Build Status](https://travis-ci.org/digitalfondue/lavagna.svg?branch=master)](https://travis-ci.org/digitalfondue/lavagna)
[![Coverage Status](https://coveralls.io/repos/digitalfondue/lavagna/badge.svg?branch=master)](https://coveralls.io/r/digitalfondue/lavagna?branch=master)
[![Maven Central](https://img.shields.io/maven-central/v/io.lavagna/lavagna.svg)](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22lavagna%22)
[![Github All Releases](https://img.shields.io/github/downloads/digitalfondue/lavagna/total.svg)](https://github.com/digitalfondue/lavagna/releases)
[![Docker Status](https://img.shields.io/docker/pulls/digitalfondue/lavagna.svg)](https://registry.hub.docker.com/u/digitalfondue/lavagna/)
[![Docker Layers](https://images.microbadger.com/badges/image/digitalfondue/lavagna.svg)](https://microbadger.com/images/digitalfondue/lavagna)

# Latest stable release is 1.1.4 (2019-12-31) #

## About ##

[Lavagna](http://lavagna.io) is a small and easy to use issue/project tracking software.

It requires Java 8 or better and optionally a database: MySQL, MariaDB or PostgreSQL. It can be deployed in a Java servlet container or as a self contained war.

See:

 - [roadmap](https://github.com/digitalfondue/lavagna/blob/master/ROADMAP.md)
 - [changelog](https://github.com/digitalfondue/lavagna/blob/master/CHANGELOG.md)
 - [download](http://lavagna.io/download/)


## Install ##

Lavagna supports MySQL (at least 5.1), MariaDB (tested on 10.1), PostgreSQL (tested on 9.1) and HSQLDB (for small deploy).

It's distributed in 2 forms:

 - simple war for deploying in your preferred web container
 - self contained war with embedded jetty web server
 
See the documentation at http://help.lavagna.io

### For testing purposes ###

If you want to test it locally, you can download the self contained war and run:

```
wget https://repo1.maven.org/maven2/io/lavagna/lavagna/1.1.4/lavagna-1.1.4-distribution.zip
unzip lavagna-1.1.4-distribution.zip
./lavagna-1.1.4/bin/lavagna.sh
```

Go to http://localhost:8080 and login with "user" (password "user").

See the README in the archive and the documentation at http://help.lavagna.io if you want to customize the scripts and set lavagna in production mode.

### Docker ###

Lavagna is also available as a Docker image so you can try it on the fly:

```
https://registry.hub.docker.com/u/digitalfondue/lavagna/
```

## Develop ##

### Java and Kotlin ###

Lavagna runs on a Java 8 jvm.
Some parts of Lavagna are made with Kotlin.

### IDE Configuration ###

Use UTF-8 encoding and 120 characters as line width.
You will need a Java _and_ Kotlin aware IDE. (Currently tested with intellij and eclipse).

For eclipse: you will need to install the kotlin plugin and add the "Kotlin nature" to the project:
Right click on the project -> "Configure Kotlin" -> "Add Kotlin nature"

### Javascript

Install npm and run the following script to assure your code follows our guidelines

First ensure that all the dependencies are ok with `npm install`.

Then, for checking:

```
npm run-script lint
```

Fix any error or warning before opening a pull request

### Execute ###

Launch the Web Server:

```
mvn jetty:run
```

For launching Web Server + DB manager (HSQLDB only):

```
mvn jetty:run -DstartDBManager
```

for launching Web Server with the MySQL database (use the mysql profile):

```
mvn jetty:run -Pdev-mysql
```
```
mvn jetty:run -Pdev-pgsql
```
- go to http://localhost:8080
  if you have a 403 error, you must configure the application,
  go to http://localhost:8080/setup, select demo + insert user "user".

- enter
	username: user
	password: user

For debugging:

```
mvnDebug jetty:run
```

For running the test cases:

```
mvn test
```

For running the test cases with MySQL or PostgreSQL:

```
mvn test -Ddatasource.dialect=MYSQL
```
```
mvn test -Ddatasource.dialect=PGSQL
```

For running with jetty-runner:

```
mvn clean install
java -Ddatasource.dialect=HSQLDB -Ddatasource.url=jdbc:hsqldb:mem:lavagna -Ddatasource.username=sa -Ddatasource.password= -Dspring.profiles.active=dev -jar target/dependency/jetty-runner.jar --port 8080 target/*.war
```

When adding new file, remember to add the license header with:

```
mvn com.mycila:license-maven-plugin:format
```

### Angular perfs ###

Use the following stats for keeping an eye on the performances:

 - https://github.com/kentcdodds/ng-stats has a bookmarklet
 - https://github.com/mrdoob/stats.js/ has a bookrmarklet

### Documentation ###

The documentation is written using stampo (see https://github.com/digitalfondue/stampo).
It currently reside in src/main/stampo .

For building the doc:

```
mvn clean stampo:build
```

The output will be present in target/generated-docs

For testing the documentation run

```
mvn stampo:serve
```

And go to http://localhost:45001/

### Vagrant ###

In order to make it easier to tests on different databases we included 3 Vagrant VMs.
Make sure that you have installed Vagrant and VirtualBox before continuing.

#### Initialization ####

Fetch the submodules:

```
git submodule update --init
```

If you are under windows you need to ensure that the pgsql submodule is not in a broken state,
double check that the file puppet\modules\postgresql\files\validate_postgresql_connection.sh is using the
unix end of line (run dos2unix).

To run the tests with Vagrant boot the VMs with:

```
vagrant up [optionally use pgsql / mysql to boot only one VM]
```

Once that the VM is up and running run the tests:

```
mvn test -Ddatasource.dialect=PGSQL / MYSQL
```


#### Connecting manually: ####

PGSQL: localhost:5432/lavagna as postgres / password

MySQL: localhost:3306/lavagna as root

## Notes about databases ##

The application uses UTF-8 at every stage and on MySQL you will need to create a database with the collation set to utf8_bin:

```
CREATE DATABASE lavagna CHARACTER SET utf8 COLLATE utf8_bin;
```


### Code Coverage ###

Jacoco plugin is used.

```
mvn clean test jacoco:report
```

-> open target/site/jacoco/index.html with your browser


## About Database migration ##

Can be disabled using the following system property: datasource.disable.migration=true


## Check for updated dependencies ##

```
mvn versions:display-dependency-updates
```
```
mvn versions:display-plugin-updates
```

## Supported by ##

[![Alt text](misc/jetbrains.png)](https://www.jetbrains.com/?from=Lavagna)
A second war named lavagna-jetty-console.war will be built. Inside there is an embedded jetty.

You must provide the following properties:

- datasource.dialect=HSQLDB | MYSQL | PGSQL
- datasource.url= for example: jdbc:hsqldb:mem:lavagna | jdbc:mysql://localhost:3306/lavagna | jdbc:postgresql://localhost:5432/lavagna
- datasource.username=<username>
- datasource.password=<pwd> 
- spring.profile.active= dev | prod

For example:

>java -Ddatasource.dialect=HSQLDB -Ddatasource.url=jdbc:hsqldb:mem:lavagna -Ddatasource.username=sa -Ddatasource.password= -Dspring.profile.active=dev -jar lavagna-jetty-console.war


You can set port and others options too:

Options:
 --port n            - Create an HTTP listener on port n (default 8080)
 --bindAddress addr  - Accept connections only on address addr (default: accept on any address)
 --contextPath /path - Set context path (default: /)
 --help              - Print this help message
 --tmpDir /path      - Temporary directory, default is /tmp# Roadmap

This is a high level roadmap. Lavagna has currently:

 - a stable 1.0.x branch where small fixes and features will be added. Some of the work done in the master branch will be backported.
 - the current master (1.1) where the big features are developed

## Expected for 1.1 

 - improve the UI/UX [done]
 - webhooks support [wip]
 - support for internal password protected accounts
 - client side refactoring, porting to angular 1.5 [done]
 - support internal account handling [wip]
 - refactor the authentication manager: cleanup + simplification [done]
 - support gitlab oauth [done]
 - iCalendar feed support [done]
 - update to spring 4.2.x [done]
 - switch connection pool to hikaricp [done]
 
## Backlog

 - enable Content-Security-Policy
 - decent i18n
REST API return data

GET:
- success: data / failure: exception

DELETE:
- success: 1/0 / failure: exception

ADD (no duplicates):
- success: nothing / failure: exception

ADD (duplicates):
- success: IDs / failure: exception

UPDATE:
- success: nothing / failure: exception

this will affect the return types of the services/controllers.For google, you should enable the following apis:

- Google+ API 	
- Google+ Domains APIroute, try to follow the RoR convention:

http://guides.rubyonrails.org/routing.html#crud-verbs-and-actions (# 2.2 CRUD, Verbs, and Actions )


angular is taken from

https://ajax.googleapis.com/ajax/libs/angularjs/1.2.8/angular.js
https://ajax.googleapis.com/ajax/libs/angularjs/1.2.8/angular-sanitize.js


notes:
- http://blog.smartbear.com/open-source/how-to-turn-your-pile-of-code-into-an-open-source-project/

markdown parser:

- https://github.com/chjj/marked

hihglight

- http://highlightjs.org/
 
elastic text area

 - http://monospaced.github.io/angular-elastic/
   https://github.com/monospaced/angular-elastic
   https://github.com/monospaced/angular-elastic/releases v2.0.0
   
   
  
 sockjs:
 
 - taken from https://raw.github.com/rstoyanchev/spring-websocket-portfolio/master/src/main/webapp/assets/lib/sockjs/sockjs.min.js
 
 stomp:
 
 - taken from https://raw.github.com/rstoyanchev/spring-websocket-portfolio/master/src/main/webapp/assets/lib/stomp/dist/stomp.min.js
 
 spectrum: https://rawgithub.com/bgrins/spectrum/master/spectrum.css + js
 
 - taken from 

 how to center stuff with bootstrap:
 http://stackoverflow.com/a/18153551
 
 
 codemirror:
 
  - core + markdown + markdown-fold + placeholder v5.5 @ http://codemirror.net/doc/compress.html  _
 | |
 | |     __ ___   ____ _  __ _ _ __   __ _
 | |    / _` \ \ / / _` |/ _` | '_ \ / _` |
 | |___| (_| |\ V / (_| | (_| | | | | (_| |
 |______\__,_| \_/ \__,_|\__, |_| |_|\__,_|
                          __/ |
                         |___/

 Version: ${project.version}

 http://lavagna.io
===========================================

This archive contain:

 - /bin/* : shell script for launching lavagna. By default it will launch
            lavagna in dev mode. You will need to customize the scripts.

 - /lavagna/*.war : a simple war that can be deployed in your servlet
                    container (tomcat, ...) or an executable war
                    (which is launched by the scripts)

 - /LICENSE.txt: license file (GPL3)
 - /NOTICE.txt: third party licenses file


Running the application
-----------------------

For testing purpose you can launch bin/lavagna.sh, bin/lavagna.bat or bin/windows-service/lavagna.xml and go
to http://localhost:8080 (username: user password: user).

If you want to install it or configure it, you have two options:

- Self contained
- Deploy in a servlet container


Database configuration
----------------------

Lavagna require a utf8 environment.
Check that the database has a utf8 collation.

For ensuring a correct db creation with MySQL create it with:

CREATE DATABASE lavagna CHARACTER SET utf8 COLLATE utf8_bin;


Self contained:
---------------

See the bin/lavagna.sh, bin/lavagna.bat or bin/windows-service/lavagna.xml scripts and configure them.
It will launch the app using a self contained jetty server.


Servlet container:
------------------

You can deploy in any servlet 3.0 container. You will need to set the following
property to the JVM (see the scripts bin/lavagna.sh / bin/lavagna.bat):

 - datasource.dialect=HSQLDB | MYSQL | PGSQL
 - datasource.url= for example: jdbc:hsqldb:mem:lavagna | jdbc:mysql://localhost:3306/lavagna?useUnicode=true&characterEncoding=utf-8 | jdbc:postgresql://localhost:5432/lavagna
 - datasource.username=[username]
 - datasource.password=[pwd]
 - spring.profiles.active= dev | prod

Or

You can define them in an external file (like the bundled sample-conf.properties) and define the following property:

 - lavagna.config.location=file:/your/file/location.properties
{{#cards}}
## {{cardName}} ({{baseApplicationUrl}}{{cardFull.projectShortName}}/{{cardFull.boardShortName}}-{{cardFull.sequence}})

{{#cardEvents}}
{{.}}

{{/cardEvents}}


{{/cards}}Doc
---

This archetype is based on the "Responsive Side Menu" layout provided by the 
purecss framework at http://purecss.io/layouts/ .


Structure
---------

The documentation is written as markdown files in the doc/ directory.

The files are then included by content/index.html.peb for generating a 
multi page doc and by content/single.html.peb for a single page doc.

The style+js are in static/*# About

This help site contains the following sections:

* **<a href="{{relativeRootPath}}/02-install.html">Install</a>**: a step by step approach to install Lavagna. It covers database configuration, servlet container, and the initial application setup
* **<a href="{{relativeRootPath}}/03-use-lavagna.html">Use Lavagna</a>**: the everyday user guide, explaining how to manage projects and boards, and take advantage of all the cool features of Lavagna
* **<a href="{{relativeRootPath}}/04-administration.html">Administration</a>**: caters to administrators, going into details about managing users, login providers, and permissions
# Install

This section is divided in 3 steps: first preparing the database, second configuring the connection parameters of lavagna and third the setup phase.

For installing lavagna, the requirements are:

 - a jre (java runtime) >= 8
 - utf-8 environment (especially for the database)
# Use Lavagna
# Administration

To access the administration panel, click on the sidebar (the **<i class="fa fa-bars"></i>** icon in the top left position) and follow the **<i class="fa fa-cog"></i> Admin Panel** link in the side bar.

## Database

Lavagna support the following databases:

 - MySQL version 5.1 or later
 - MariaDB version 10.0 or later
 - PostgreSQL version 9.2 or later
 - embedded HSQLDB version 2.3.1
 
If it's not possible to use MySql or Postgresql and the full text search feature is not important, the HSQLDB backend can be used with a file backend. See the HSQLDB section below. 
 
### MySql

When using MySql, for ensuring a good full text search experience, it's advisable to set in the MySql configuration file:

```
[mysqld]
ft_min_word_len=3
ft_stopword_file = ""
``` 

The default minimal word length (4) and the stopwords can be problematic for searching acronyms or short words.

Additionally, when creating the database, it must ensured that utf-8 is used everywhere:

```sql
CREATE DATABASE lavagna CHARACTER SET utf8 COLLATE utf8_bin;
```

### MariaDB

Unit tests are run also on MariaDB and as a general rule everything that must be done for MySql must be done also for MariaDB.

### PostgreSQL

When using PostgreSQL, ensure that the database/schema is in utf-8.

For the full text search support, the unaccent extension must be present. In general it's already included in the PostgreSQL
installation. If it's not present, an error will be launched when running lavagna the first time.


### HSQLDB

It's the default development database. But it's possible to use it a persistent way: when configuring the jdbc url, the file backend can be used: `-Ddatasource.url=jdbc:hsqldb:file:lavagna `.
## Configuration

Lavagna can run as a standalone application or inside a servlet 3.0+ container.

### Self contained

As a standalone application, see the `bin/lavagna.sh`, `bin/lavagna.bat` or `bin/windows-service/lavagna.xml` scripts and configure them. It will launch the app using a self contained [jetty](https://www.eclipse.org/jetty/) server.

As a default, lavagna launch in dev mode, so check in the scripts that the spring.profiles.active property is set to **prod**.

### Servlet container

You can deploy in any servlet 3.0 container. You will need to set the following
property to the JVM (see the scripts bin/lavagna.sh / bin/lavagna.bat):

 - datasource.dialect=HSQLDB | MYSQL | PGSQL
 - datasource.url= for example: jdbc:hsqldb:mem:lavagna | jdbc:mysql://localhost:3306/lavagna?useUnicode=true&characterEncoding=utf-8 | jdbc:postgresql://localhost:5432/lavagna
 - datasource.username=[username]
 - datasource.password=[pwd]
 - spring.profiles.active= dev | prod

Or

You can define them in an external file (like the bundled sample-conf.properties) and define the following property:

 - lavagna.config.location=file:/your/file/location.properties
## Setup

### Step 1, Base url or import

After successfully launching the application, go to http://your-lavagna-install/setup .

The following page will be shown:

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_1.png" alt="First setup step">

 - If it's a new install, confirm that the base url is correct and click **Next** 
 - If it's an import, select the exported file and click **Import**. The import process can take a noticeable amount of time.
 
### Step 2, Login provider configuration

Lavagna does **not** store the user credentials by design: an external provider must be chosen. There are 3 possible choice:

 - password
 - demo (use for test purpose only)
 - ldap
 - oauth
 
#### Password provider

If you want to manage your accounts inside lavagna.

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_2_password.png" alt="Password provider">
 
#### Demo provider

The demo provider must **not** be selected in production, as the password **is** the username. It can be useful for a small test round for evaluating the product.

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_2_demo.png" alt="Demo provider">

#### Ldap provider

If the users are stored in a ldap directory (Active Directory is supported too), the ldap provider must be configured.

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_2_ldap.png" alt="Ldap provider">

It requires a user that can query the directory (the Manager DN and Manager Password). 

The query is composed by a base (Search base) and the filter (User search filter), where `{0}` is the placeholder for the username.

The configuration can be tested in the "Check ldap configuration" form.

#### Oauth provider

The application support the following external oauth providers: 

 - bitbucket 
 - gitlab.com
 - github
 - google
 - twitter
 
Additionally, self-hosted/others external gitlab instances can be configured in the Custom Oauth provider section.

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_2_oauth.png" alt="Oauth provider">

#### Preconfigured oauth providers

Select the oauth provider of the first account and provide the api key and secret. The provided callback url should be the correct one that must be provided.

See the documentation for:

 - [bitbucket](https://confluence.atlassian.com/display/BITBUCKET/OAuth+on+Bitbucket)
 - [gitlab](http://doc.gitlab.com/ce/integration/oauth_provider.html). Registration page is https://gitlab.com/profile/applications
 - [github](https://developer.github.com/v3/oauth/). Registration page is https://github.com/settings/applications/new
 - [google](https://developers.google.com/identity/protocols/OAuth2WebServer): the "Google+ API" must be enabled
 - [twitter](https://dev.twitter.com/web/sign-in/implementing)
 
#### Custom oauth providers

If you have a self-hosted (or others) gitlab instance, you can configure in the "Custom oauth providers" section.
Select the type, enter the name, the base url, api key and api secret.

Please note that if you are using **self signed certificates** you _must_ include them in the default keystore of your java virtual machine. See the [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html#keytool_option_importcert) documentation and this [stackoverflow post](http://stackoverflow.com/a/11617655). Lavagna will **not** provide a way to ignore untrusted certificates. 



### Step 3 Insert administator

In the third step, the administrator must be defined. Enter the username and click **Next**.

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_3.png" alt="Insert admin user">

### Step 4 Confirm

Check the validity of the configuration data. Click on **Activate**: the configuration will be saved and the browser will go to the root of the application. Enter the username (and password if required).

<img class="pure-img" src="{{relativeRootPath}}/images/en/c02_install_step_4.png" alt="Confirm">
## Project

### Create Project

To create a new project, press the plus button on the dashboard.

A dialog will appear. Enter a name, a unique short name, and a description, and press create.

<img class="pure-img" src="{{relativeRootPath}}/images/en/create-project-dialog.png" alt="Create new project dialog">

### Project settings

To manage a project, click on the cog icon in the project header bar

<img class="pure-img" src="{{relativeRootPath}}/images/en/project-header-bar.png" alt="Project header bar">

### Edit Project

To edit a project, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Project" tab.

A project can be renamed in this section, and its description modified.

Changing the project short name is not possible after it has been created.

### Archive Project

A project can be archived/unarchived using the checkbox in this page.

This may hide the project in the home page if the "Show Archived Projects" switch isn't active.

### Delete Project

Lavagna doesn't support yet the full deletion of a project. It is recommended to archive a project instead.

## Board

### Create Board

To create a new board, navigate to a project, and then press the plus button.

A dialog will appear. Enter a name, a unique short name, and a description, and press create.

<img class="pure-img" src="{{relativeRootPath}}/images/en/create-board-dialog.png" alt="Create new board dialog">

### Edit Board

To edit a board, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Board" tab.

Then, press the edit icon on the board panel.

<img class="pure-img" src="{{relativeRootPath}}/images/en/manage-board-edit.png" alt="Edit board">

### Archive Board

To archive, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Board" tab.

Then, press the archive icon on the board panel.

<img class="pure-img" src="{{relativeRootPath}}/images/en/manage-board-archive.png" alt="Archive board">

This may hide the board in the project home page if the "Show Archived Boards" switch isn't active.

### Delete Board

Lavagna doesn't support yet the full deletion of a boar. It is recommended to archive a board instead.
## Columns

Columns are used to define the current status of a card. This is done by combining two metadata:

* the name of the column
* the status assigned to the column, represented by the color in the header

<img class="pure-img" src="{{relativeRootPath}}/images/en/column.png" alt="Column">

There are four main statuses:

* OPEN: used for both new and in progress cards, without distinction
* CLOSED
* BACKLOG
* DEFERRED

The aggregate number of cards by status present in the board is then reflected in the main and project dashboard.

<img class="pure-img" src="{{relativeRootPath}}/images/en/dashboard-panel.png" alt="Dashboard panel">

### Create a new column

To create a new column, click on the <span class="icon icon-add-column"></span> icon in the board left side bar.

A new dialog will appear: enter the column name, select a status, and click add.

<img class="pure-img" src="{{relativeRootPath}}/images/en/add-column.png" alt="Add column">

### Special columns

Each board has three special column:

* **BACKLOG**: A more general backlog column to free up space in the board. Cards in this column are still taken into the board count.
* **ARCHIVE**: If cards have been closed for a while, then it is advised to move them to the archive. Cards moved here are not included in the board count anymore.
* **TRASH**: Cards that have been created by mistake can be put here to separate them from the archive. Cards moved here are not included in the board count anymore.

#### Access the backlog

To access the backlog, click on the <span class="icon icon-board-backlog"></span> icon in the board left side bar.

#### Access the archive

To access the archive, click on the <span class="icon icon-board-archive"></span> icon in the board left side bar.

#### Access the trash

To access the trash, click on the <span class="icon icon-board-trash"></span> icon in the board left side bar.

### Change the name of a column

To change the name of a column, click on the name itself to open the edit form.

### Column menu

To open the column menu, click on the <span class="icon icon-more-vert"></span> icon in the column header.

The available operations are:

* **Select all**: Select all cards in the column
* **Select none**: Deselect all cards in the column
* **Column status**: change the status assigned to the column
* **Move all cards to Archive**: archive all the cards that belong to the column, but keep the column in the board
* **Move all cards to Backlog**: move all the cards that belong to the column to the board backlog, but keep the column in the board
* **Move all cards to Trash**: move all the cards that belong to the column to the board trash bin, but keep the column in the board
* **Move column to Archive**: archive the column and all its cards. The column won't be available in the board anymore
* **Move column to Backlog**: move the column and all its cards to the board backlog. The column won't be available in the board anymore
* **Move column to Trash**: move the column and all its cards to the board trash bin. The column won't be available in the board anymore

### Change status color

To modify the color representing each status, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Project" tab.

There, use the color picker to select a different color for each status.

<img class="pure-img" src="{{relativeRootPath}}/images/en/status-color.png" alt="Status color">


## Card

### Create a new card

To add a new card to a column, click on the <span class="icon icon-add-card"></span> icon in the column header.

A new dialog will open: enter at least the card name and the target column, preselected to the current one, then click Create.

In addition to the card name, the following fields are available when creating a new card:

* **Labels** 
* **Description**
* **Milestone**
* **Due Date**
* **Assigned Users**

### Access the card menu in a board

To access the card menu, hover on the card and click the <span class="icon icon-more-vert"></span> icon.

The card menu will open, providing the following actions:

* **Move card to column**: Move the card to a column of choice
* **Clone**: Clone the card to a different board, including all its data
* **Move to backlog**: Move the card to the board backlog
* **Move to archive**: Move the card to the board archive
* **Move to trash**: Move the card to the board trash
* **Take**: Add the current users to the list of assigned users
* **Watch**: Add the current user to the list of watchers

### Work with a card

This section provides information about operations that can be performed on the card screen.

#### Change the card title

To change the card title, click on the current title and modify it.

#### Change the card description

To change the card description, click on the <span class="icon icon-edit"></span> icon in the main panel, 

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-edit-description.png" alt="Edit card description">

#### Add a label

To add a label, click the plus icon under the card title.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-add-label.png" alt="Add label">

[Learn more about Labels.](/03-use-lavagna/03-05-labels.html)

#### Move the card

To change the current column, access the status menu and select a new column.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-metadata.png" alt="Card metadata">

[Read more about columns.](/03-use-lavagna/03-03-columns.html)

#### Change the card due date

To set the date a card is due, click on the calendar icon in the Due By section.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-due-date.png" alt="Set card due date">

#### Assign the card to a milestone

To assign the card to a milestone, click on the <span class="icon icon-edit"></span> under the Milestone section.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-set-milestone.png" alt="Set card milestone">

[Read more about milestones.](/03-use-lavagna/03-06-milestone.html)

#### Work with people

##### Assign the card to a user

To assign the card to a user, star to type the user details in the box below, select the desired user, and the press Assign.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-assign-user.png" alt="Assign a user">

##### Personal operations

You can also assign the card to yourself, or start watching it, by using the shortcuts in the People panel header.

#### Work with action lists

Action lists are a good way to keep track on small tasks within a card.

To create an action list, look for the Action List form at the bottom of the card.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-add-action-list.png" alt="Add action list">

Multiple action lists can be added to a single card.

Both entire action lists and single action items can be moved around by dragging from the <span class="icon icon-drag"></span> handle.

If a list or item is deleted by mistake, is possible to revert the operation by clicking on the UNDO button on the notification. If the notification is acknowledged however, the restore operation is not possible anymore.

#### Attachments

File can be uploaded to a card, either by selecting them from the file system, or dropping them in the attachment panel.

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-attachments.png" alt="Card attachments">

#### Activity

Activity contains both comments and all operations performed on a card. By default, only the last 10 comments are displayed.
By scrolling down, more comments will be loaded.
## Labels

Labels are a powerful way to create custom data to tag cards, providing both an easy visual feedback and a powerful search tool.

Labels are defined for each project. There are no global labels.

Each label has a type, with the following possibilities: 

* **Name only**: a simple label
* **Text**: a custom text can be set by the user
* **Date**: a date can be defined
* **Number**: a number can be specified
* **Card**: a card can be referenced (useful for a label like: "Duplicate of:")
* **User**: a user can be referenced (useful for a label like: "Review:")
* **List**: a value specified in a ordered list can be selected.

In addition, it can be specified if a label can be unique per card.

### Use labels

Labels are very powerful search criteria. [Learn more about search](/03-use-lavagna/03-07-search)

### Manage labels

To manage labels, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Labels" tab.

#### Create a label

Press the plus button to open the create label dialog.

Enter the name, color, and type, and press create.

For adding a new label, the following form must be used:

<img class="pure-img" src="{{relativeRootPath}}/images/en/labels-manage-create.png" alt="New label">

The name (unique in the context of a project), the type, the color and whether the label must be unique in card must be specified.

In case of a label of type **list**, the values must be specified later, see the the [Edit section](#edit-label).

#### Edit a label

To edit a label, click on the <span class="icon icon-edit"></span> icon.

A dialog will appear:

<img class="pure-img" src="{{relativeRootPath}}/images/en/labels-manage-edit.png" alt="Edit label">

**NOTE**: list values that are still in use can't be deleted.

#### Delete a label

To delete a label, click on the <span class="icon icon-delete"></span> icon.

**NOTE**: labels that are still in use can't be deleted.
## Milestones

### Use milestones

Milestones are unique per project. Access milestones from the "Milestones" tab.

<img class="pure-img" src="{{relativeRootPath}}/images/en/milestone-panel.png" alt="Milestone">

#### Close a milestone

To close a milestone, click on the <span class="icon icon-milestone-open"></span> icon.

### Manage milestones

To manage labels, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Milestones" tab.

<img class="pure-img" src="{{relativeRootPath}}/images/en/milestones-manage.png" alt="Milestones">

Milestones can be reordered using the appropriate icons.

#### Create a new milestone

To create a new milestone, click the plus button, enter the name, and click create.

#### Edit a milestone

* <span class="icon icon-edit"></span>: edit milestone name
* <span class="icon icon-calendar"></span>: set due date
* <span class="icon icon-milestone-open"></span>: close a milestone
* <span class="icon icon-delete"></span>: delete a milestone

**NOTE**: a milestone that is still in use, meaning that it still has cards assigned, can't be deleted.
## Search

The search bar at the top is context sensitive. The context are:

 - global search: when the user is in the Dashboard
 - project specific search: when the user is in a project
 - board filter: when the user is in the board view
 
Currently the search only support implicitly the "AND" operator. Each search term is part of the list of filters that *must* match.

### Filters

In both the global/project and board filter the following filters can be defined. For most filters, only a single value can be specified. The filters that receive dates as a parameter can receive two dates for defining a time interval.

#### label

A label filter begin with the hash symbol: '#'.

When entering # in the search bar, a list of possible label is displayed. For example:

<img class="pure-img" src="{{relativeRootPath}}/images/en/search-label-criteria.png" alt="Label suggestions">

When confirming the filter, the search will be done. In this case all the cards with the label "Priority" are shown, regardless of the associated value.

<img class="pure-img" src="{{relativeRootPath}}/images/en/search-label-only.png" alt="Label only search">

For searching the associated value, the complete syntax is : #LABEL: ASSOCIATED_VALUE, in the screenshot below it can be seen in action:

<img class="pure-img" src="{{relativeRootPath}}/images/en/search-label-value.png" alt="Label with value">

#### to

For searching the cards assigned (or not) to a specific user, the "to: " filter must be used.

The following values are permitted:

 - **to:me**
 - **to:unassigned**
 - **to:LOGIN_PROVIDER:USERNAME**
 
The "to:me" show the cards assigned to the current user.

The "to:unassiged" show all the cards without an assigned user.

The "to:LOGIN_PROVIDER:USERNAME" show the cards assigned to a specific user. For example: "to:demo:user1".

#### by

"by" search all the cards created by the specified user.

The following values are permitted:

 - **by:me**
 - **by:LOGIN_PROVIDER:USERNAME**

Like the "to" filter, the "by:me" search the cards created by the current user and "by:LOGIN_PROVIDER:USERNAME" show the ones created by the specified user.

#### created

"created" show all the cards created in the specified time interval.

The supported values are:

 - **created:DATE**
 - **created:DATE1..DATE2**
 - **created:late**
 - **created:today**
 - **created:this week**
 - **created:this month**
 - **created:previous week**
 - **created:previous month**
 - **created:last week**
 - **created:last month**
 
The supported DATE format is yyyy-mm-dd. For searching an interval, add ".." between the two dates, for example: "created:2015-02-01..2015-10-01"

"created:late" will show all the cards created in the past.

#### watched

"watched" search all the cards watched (or notd) by a specific user.

The permitted values are:

 - **watched:me**
 - **watched:unassigned**
 - **watched:LOGIN_PROVIDER:USERNAME**
 
Like the "to" filter, the "watched:me" search all the cards watched by the current user, **watched:unassigned** search the one without watcher and finally "watched:LOGIN_PROVIDER:USERNAME" show the cards with the specified user.

#### updated

The "updated" filter show all the cards that have been updated in the specified time interval.

The following values are supported:

 - **updated:DATE**
 - **updated:DATE1..DATE2**
 - **updated:late**
 - **updated:today**
 - **updated:this week**
 - **updated:this month**
 - **updated:previous week**
 - **updated:previous month**
 - **updated:last week**
 - **updated:last month**

It follow exactly the same behaviour as the ["created"](#created) filter.

#### due

The "due" filter search all the cards that have the due date specified.

The following values are supported:

 - **due:DATE**
 - **due:DATE1..DATE2**
 - **due:late**
 - **due:today**
 - **due:this week**
 - **due:this month**
 - **due:previous week**
 - **due:previous month**
 - **due:next week**
 - **due:next month**
 - **due:last week**
 - **due:last month**

It follow exactly the same behaviour as the ["created"](#created) filter, in addition "next week" and "next month" are available as a shortcut. 

#### updated by

"updated_by" search all the cards updated by a specific user.

The following values are permitted:

 - **updated_by:me**
 - **updated_by:LOGIN_PROVIDER:USERNAME**

Like the "by" filter, the "updated_by:me" search the cards updated by the current user and "updated_by:LOGIN_PROVIDER:USERNAME" show the ones updated by the selected user.

#### milestone

For searching the cards that are assigned (or not) to a specific milestones, the **"milestone:"** filter must be used.

The accepted values are:

 - **milestone:unassigned**
 - **milestone:MILESTONE_NAME**

The "milestone:unassigned" search all the cards without an assigned milestone.

#### status

The **status:** filter allow to search the cards that are in a specific status (OPEN, CLOSED, BACKLOG, DEFERRED).

The following values are valid:

 - **status:OPEN**
 - **status:CLOSED**
 - **status:BACKLOG**
 - **status:DEFERRED** 

#### location

The **location:** filter search for the cards that are in a specific location (BOARD, ARCHIVE, BACKLOG, TRASH)

The following values are valid:

 - **location:BOARD**
 - **location:ARCHIVE**
 - **location:BACKLOG**
 - **location:TRASH** 

#### Free text search

All the text that don't fall in the others filters is considered a "free text search". At the moment it use the functions from the underlying DB. 


### Single board search

In the board view, the search bar generate a client side filter that is continuously applied when the cards are updated like the following screenshot:

Note: in this view, the "free text search" will only work on card names due to the search being performed client side.


### Global and project specific search

When the search is triggered in the home page, a global search is done in all the projects that the user has access to.

When the user is in the **project** page, a project specific search will be done.

Bulk operations will be available in this view. [Learn more](/03-use-lavagna/03-08-work-with-multiple-cards.html)
## Operations on multiple cards

On a board, is possible to select multiple cards and perform one or more operations in bulk.

### Select cards

To select a card, over on the card fragment and click on the check mark in the top left corner:

<img class="pure-img" src="{{relativeRootPath}}/images/en/card-fragment-select.png" alt="Select card">

Or use the select handle <span class="icon icon-bulk-select"></span> in the left sidebar to select or deselect all cards.

### Operations

* <span class="icon icon-bulk-move"></span> **Handle Move**: Move the selected cards to Archive, Backlog, or Trash
* <span class="icon icon-bulk-assign"></span> **Handle assigned users**: Assign, Reassign, or remove an assigned user from the selected cards
* <span class="icon icon-calendar"></span> **Handle due date**: Set or remove the due date of the selected cards
* <span class="icon icon-bulk-milestone"></span> **Handle milestone**: Set, update, or remove the milestone of the selected cards
* <span class="icon icon-bulk-label"></span> **Handle labels**: Add or remove a label from the selected cards
## Calendars

The global and project calendar take into consideration all due dates, set either on cards or milestones, and display them in a month by month view.

<img class="pure-img" src="{{relativeRootPath}}/images/en/calendar.png" alt="Calendar view">

Cards will be displayed by their short name and name.

Milestone will be displayed by their name and percentage of closed cards.
## Project Statistics

Statistics can be accessed from the statistics tab in a project.

### Filtering

Statistics can be filtered by individual boards, and specific periods.

### Basic statistics

* **Created this period**: cards created in the selected period
* **Closed this period**: cards closed in the selected period
* **Most active card**: card with the most activity in the selected period
* **Open**: cards currently open
* **Closed**: cards currently closed
* **Deferred**: cards currently deferred
* **Backlog**: cards currently in the backlog
* **Total cards**: total cards
* **Active users**: users that have performed at least one operation
* **Average cards per user**: average number of cards assigned to a user
* **Average users per card**: average assigned users per card

### Chart statistics

**Created vs closed**: created and closed cards per day

<img class="pure-img" src="{{relativeRootPath}}/images/en/statistics-created-vs-closed.png" alt="Created vs closed">

**Cards history**: evolution of open, closed, backlog, and deferred cards

<img class="pure-img" src="{{relativeRootPath}}/images/en/statistics-cards-history.png" alt="Cards history">

**Cards by label**: how many cards for each label

<img class="pure-img" src="{{relativeRootPath}}/images/en/statistics-cards-by-label.png" alt="Cards by label">
## Import data from external sources

To access the data import feature, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Import" tab.

### Trello

#### Requirements

Configure a Trello API Key in the [Configuration Parameters](/04-administration/04-01-config-parameters.html).

#### Import data

First, click "Load Trello Connector".

If the load is successful, the button will change to "Connect to Trello".

You will be required to allow Lavagna read-only access to your Trello account.

Once done, you will get a list of boards you can select to import.

When a board is selected, a short name will be automatically generated.

As a final option, you can select whether or not to import archived cards.

<img class="pure-img" src="{{relativeRootPath}}/images/en/import-from-trello.png" alt="Trello import">

When at least one board is selected, with a valid short name, the import process can start.

**Note**: Lavagna does not keep track of which boards have been imported.  That means you'll be able to import a board a second time, as long as a different short name is provided.
## Create tickets via E-mail

Lavagna supports creating cards via E-mail.

### Manage ticket E-mail configuration

To manage mail ticket, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Mail Ticket" tab.

<img class="pure-img" src="{{relativeRootPath}}/images/en/project-mail-ticket.png" alt="Mail ticket">

#### Create mail configuration

To add a new mail configuration, click on the plus button.

Fill the dialog with the following information:

* **Name**: A name identifying the configuration

* **Inbound Config**: The E-mail account Lavagna reads from.
  - **Protocol**: Mail server protocol. One from: IMAP, IMAPS, POP3, POP3S. We recommend using IMAPS.
  - **Host**: Mail server address
  - **Port**: Mail server port
  - **User**: Mail account username
  - **Password**: Mail account password
  - **Properties**: Properties for the Java Mail client. One property per line.
  
* **Outbound Config**: The E-mail account Lavagna uses to notify the user a new ticket has been created.
  - **Protocol**: Mail server protocol. One from: SMTP, SMTPS.
  - **Host**: Mail server address
  - **Port**: Mail server port
  - **User**: Mail account username
  - **Password**: Mail account password
  - **From**: What to send the E-Mail as.
  - **Properties**: Properties for the Java Mail client. One property per line.
    
* **Notification E-Mail**: The content of the notification E-Mail sent to the user.
  - **Subject**: The subject of the notification E-Mail. Use the {{card}} identifier to reference the created card.
  - **Body**: The content of the notification E-Mail. Supports markdown. Use {{name}} to reference the display name or address of the user creating the ticket, and {{card}} to reference the created card.

Then click Save.

#### Add ticket configuration

Once a mail configuration is added, click "Add Ticket Config". A dialog will appear.

<img class="pure-img" src="{{relativeRootPath}}/images/en/project-mail-ticket-config-dialog.png" alt="Add ticket config dialog">

* **Name**: A name identifying the ticket configuration
* **Alias**: The address this configuration should read E-Mails from. If no alias is configured on the E-Mail account, use the address.
* **Send mail as alias**: Whether to send the notification E-Mail using the configured alias.
* **Create card in**: Configure where the card is created.
  - **Board**: Select a board
  - **Column**: Select a column in the selected board
* **Notification E-Mail**: The content of the notification E-Mail sent to the user.
  - **Override Mail Config Template**: Override the subject and body configured in the Mail Config
  - **Subject**: The subject of the notification E-Mail. Use the {{card}} identifier to reference the created card.
  - **Body**: The content of the notification E-Mail. Supports markdown. Use {{name}} to reference the display name or address of the user creating the ticket, and {{card}} to reference the created card.
  
Then click "Save".

#### Edit configurations

Use <span class="icon icon-edit"></span> to edit both mail configuration and ticket configuration. See the previous section to find details about each parameter.

#### Enable/Disable configuration

Single ticket configuration can be enabled or disabled, or entire mail configuration. When a mail configuration is disabled, no ticket configuration will be processed.

To enable, click <span class="icon icon-enable-ticket"></span>.

To disable, click <span class="icon icon-disable-ticket"></span>.

#### Delete configuration

To delete a configuration, click <span class="icon icon-delete"></span>.

**NOTE**: mail configuration with one or more ticket configuration can't be deleted.

### Support localized E-Mail notifications

By taking advantage of the possibility to override notification templates for a specific alias, it's possible
to create a more customized experience for users in different language regions.

An organization can have a generic Mail Config (e.g. support@organization.com) with a english notification template.

A default ticket configuration using support@organization.com as alias, with "Override Mail Config Template" left unchecked will cover international users.

Then, a set of aliases (e.g. support-es@organization.com, support-fr@organization.com) can share the same mail account (support@organization.com),
but by using different aliases can send localized mail notification, while still creating cards in the same column as any other ticket config.

While this solution requires the duplication of some configuration, in our opinion it improves the experience of the end users.
## Manage profile

To access the user profile, click on the <span class="icon icon-bulk-assign"></span> icon on the header bar.

### Profile

<img class="pure-img" src="{{relativeRootPath}}/images/en/profile-manage.png" alt="Manage profile">

* **Display name**: overrides the username across the application
* **Email**: used to send notifications
* **Enable email notifications**: enable sending notifications to the configured email
* **Do not notify my own actions**: avoid sending emails for own actions
* **Clear all tokens**: clear all access token (remember me)

### Calendar access

This is the calendar link you can use to import the Lavagna calendar to your preferred application.

<img class="pure-img" src="{{relativeRootPath}}/images/en/profile-calendar.png" alt="Manage calendar access">

The calendar feed can be disabled, or the URL generated once again if you suspect it has been leaked.

### Change password

**Note**: only available for password auth provider. [Learn more](/04-administration/04-02-login.html)

Change the account password: requires the current password. 

<img class="pure-img" src="{{relativeRootPath}}/images/en/profile-password.png" alt="Change password">

Password reset without the current password can only be performed by an administrator. [Learn more](/04-administration/04-03-users.html)
## Configuration parameters

The configuration parameters section provides the list of the currently configured parameters in the application, e.g.: smtp configuration, authentication configuration, and the possibility to change a few.

The following parameters can be configured in this page:

* **Email notification interval**: In seconds. How often to check for new events and send email notifications. If not configured, the default value is 30
* **Max upload file size**: Size in bytes. Limit the dimensions of the uploaded files. If not configured, no limit will be considered
* **Trello API Key**: Trello api key to import boards, can be found at https://trello.com/app-key

To modify a parameter, enter the new value and click **Save**. 

To delete and revert to the default value, leave the field empty and click **Save**.
## Login

The login section provide the configuration space for:

 - anonymous user access
 - login providers
 
 
### Anonymous user access

Anonymous access allows read-only access to the entire application. Users will be able to navigate projects, boards, and cards without the need to login in.

By default, the access for anonymous user is disabled.

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-login-anon.png" alt="Anonymous user access control">

Once enabled, it's possible to configure further settings:

* **Global Access**: give access to all project, regardless of each project anonymous access policy
* **Enable Search**: enable search for anonymous users

If only one of few projects should be accessible without login, enable anonymous access for each one individually.

To do that, access the "Anonymous Access" tab in the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings).

### Login providers

Lavagna support multiple providers at the same time. In this section they can be enabled and configured.

#### Demo

The Demo provider is used for development and internal testing. Users belonging to the demo provider have their password automatically set as their username, without the possibility to change it.

<div class="alert-box"><b>ALERT</b>: don't use this provider for any purpose other than develpment or testing</div>

#### Password (internal provider)

The internal password provider is used for deployments that have no ability to connect to an external authentication provider, and enforce security via other means (e.g. access via VPN only).

Simply enable the password provider to start using it.

<div class="info-box"><b>NOTICE</b>: the Lavagna team still recomends to use a more secure provider, with features like two-factor authentication.</div>

#### Ldap

If the users are stored in a ldap directory (Active Directory is supported too), the ldap provider must be configured.

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-login-ldap.png" alt="Ldap provider">

It requires a user that can query the directory (the Manager DN and Manager Password). 

The query is composed by a base (Search base) and the filter (User search filter), where `{0}` is the placeholder for the username.

The configuration can be tested in the "Verify" form.

By checking "Enable automatic account creation", Lavagna will automatically create missing users, with DEFAULT role, if the LDAP authentication succeeds, but the user is not found internally.

#### Oauth 

The application support the following external oauth providers:
 
  - [bitbucket](https://bitbucket.org)
  - [gitlab](https://about.gitlab.com/gitlab-com/)
  - [github](https://github.com)
  - [google](https://google.com)
  - [twitter](https://twitter.com)
  
#### Preconfigured oauth providers

Select the oauth provider of the first account and provide the api key and secret. The provided callback url should be the correct one that must be provided.

See the documentation for:

 - [bitbucket](https://confluence.atlassian.com/display/BITBUCKET/OAuth+on+Bitbucket)
 - [gitlab](http://doc.gitlab.com/ce/integration/oauth_provider.html). Registration page is https://gitlab.com/profile/applications
 - [github](https://developer.github.com/v3/oauth/). Registration page is https://github.com/settings/applications/new
 - [google](https://developers.google.com/identity/protocols/OAuth2WebServer): the "Google+ API" must be enabled
 - [twitter](https://dev.twitter.com/web/sign-in/implementing)

#### Configurable oauth providers

Self-hosted gitlab instances can be configured with the "Add new provider" functionality.

Please note that if you are using **self signed certificates** you _must_ include them in the default keystore of your java virtual machine. See the [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html#keytool_option_importcert) documentation and this [stackoverflow post](http://stackoverflow.com/a/11617655). Lavagna will **not** provide a way to ignore untrusted certificates.

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-login-new-oauth.png" alt="New Oauth provider">

The new providers will appear in the section "Configurable OAuth providers".
## Users

Users are displayed ordered by provider and username. 

It's possible to filter users by status (Active, Inactive, Both) and by free text search (includes all fields).

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-users.png" alt="Manage users">

### Add User

To create a user, click on the plus button, and then select "Add user".

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-users-add.png" alt="Add user">

Based on the selected provider, enter the required configuration:

* **Username**: the unique username, also used to log in in case of demo and password providers
* **Password**: Password provider only
* **Email**: address used to send notifications
* **Display Name**: name to display across the application instead of the username
* **Roles**: one or more roles to assign to the user
* **Active**: whether the user is active or not

### Import users from a file

It is also possible to save time and import a large set of user from a JSON formatted file.

The format has to be:
<pre>
[
    {
        "provider" : "",
        "username" : "",
        "displayName" : "",
        "email" : "",
        "enabled" : true|false,
        "roles" : []
    },
    ...
]
</pre>

Only provider and username are mandatory, with password mandatory in case the internal provider is used.

To then import the file, click on the plus button, then "Import".

Select a file, then click "Import".

A notification will appear in the lower left corner with the result of the operation.

### User actions

* <span class="icon icon-password"></span>: reset the user's password
* <span class="icon icon-edit"></span>: edit e-mail address and display name
* <span class="icon icon-info"></span>: show roles assigned to the user
## Access control

### Global and Project Roles

Lavagna supports two types of roles:

* **Global roles**: roles defined by the administrators. Those roles applies to every project.
* **Project roles**: roles defined by the project administrator. Those roles only apply to the project they belong.

#### Default roles

By default, Lavagna comes with two pre-defined roles:

* **ADMIN**: administration role, with all permissions, can't be deleted.
* **DEFAULT**: default user role, with no management permissions, can't be deleted.

#### Use roles for effective access control

The best way to prevent unwanted access to projects is to set up the roles on project level.

However, it is also good to keep in mind that the permissions for a few operations, like update profile and search, are defined in global roles.

To address that, create a global role that only allows search and update profile access.

Assign all users without administration rights to that role.

Then, ask the project administrators to set up their desired roles. Users won't be able to access a project until the project administrator assign them a role.

### Permissions

To each role belongs a list of permissions, describe in details in this section.

Global application permissions are:

* **Application Administration**: access the administration panel, and gives the ability to create new projects
* **Update user profile**: modify own user profile
* **Search**: access the search bar, and the search feature
* **Global API hook access**: API hook access for all the application
* **Project API hooks access**: API hook access limited to the project

Project permissions are:

* **Project_Administration**: access the project administration panel,and the ability to create new boards

Board permissions are:

* **Board access**: access boards in read only mode

Columns permissions are:

* **Create column**: create a new columns within a board
* **Move column**: ability to move a column around the board, including move the column to the archive, backlog, and trash
* **Rename column**: change the column name, and the status associated with the column

Card permissions are:

* **Create card**: create a new card
* **Update card**: change the card title, description, due date, milestone, watchers, and assigned users
* **Move card**: ability to move a card around the board, including to the ability to move the card to the archive, backlog, and trash
* **Create comment**: create a comment. In case of user own comment, it's also possible to update and delete
* **Update comment**: update another user comment
* **Delete comment**: delete another user comment
* **Action lists**: ability to create, modify, and delete action lists. This also applies to the action items within a list
* **Upload file**: upload a file
* **Update file**: not used in this version of lavagna, but reserved for future use cases
* **Delete file**: delete a file
* **Labels**: Add or remove labels on a card

### Manage roles

#### Add a new role

To add a role, click on the plus button, enter the role name, and click "Add".

By default, roles have no permissions associated.

#### Edit a role

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-manage-role.png" alt="Manage role">

To edit a role, click on the <span class="icon icon-edit"></span> icon.

A dialog with the list of available permissions will open. Select the desired one, and click "Update".

#### Delete a role

A role can be deleted when there are no users assigned to it.

To delete a role, click on the <span class="icon icon-delete"></span> icon.

#### Edit project role

To edit project roles, go to the [Project Settings](/03-use-lavagna/03-01-project.html#project-settings), and then the "Roles" tab.

Click the <span class="icon icon-edit"></span> icon on the role: the role's permissions dialog will open. Select the desired permissions, and press "Update".

<img class="pure-img" src="{{relativeRootPath}}/images/en/manage-project-edit-role.png" alt="Edit project role">
## Mail notifications

For sending email notifications, a smtp server must be available and accessible.

Click on the toggle for displaying and enabling the smtp configuration form:

<img class="pure-img" src="{{relativeRootPath}}/images/en/admin-smtp.png" alt="SMTP configuration">

Consult https://javamail.java.net/nonav/docs/api/com/sun/mail/smtp/package-summary.html if there is a need to add additional properties.

Fields description, with a [mailgun](https://www.mailgun.com/) configuration as an example:

 - **Host**: the smtp host. Example: `smtp.mailgun.org`
 - **Port**: the smtp port. Example: 465
 - **Protocol**: smtp or smtps. Example: smtps
 - **Username**: smtp username. Example: example@example.com
 - **Password**: smtp password.
 - **From E-Mail**: the "from" value when lavagna send the email. Example: no-reply@dev.lavagna.io

You can test your configuration by clicking "send test email"
## Import/Export data

For creating a backup of lavagna, exporting the dabase (with [mysqdump](https://dev.mysql.com/doc/refman/5.1/en/mysqldump.html) or [pg_dump](http://www.postgresql.org/docs/9.4/static/app-pgdump.html)) is the recommended method.

The import/export data functionality provided by lavagna has some serious drawback, but it can be used as a backup method and/or transport data to a different database (e.g.: from mysql to pgsql).

The drawbacks are: 

 - if a project with the same short name already exists in the target system, the whole project will not be imported  
 - it's possible that some part of the history cannot be rebuilt
 
### Exporting

For exporting click the export button. The process will take some time, especially if there are uploaded files.

The resulting file is a zip archive named lavagna-YEAR-MONTH-DAY.zip.

### Importing

First select the archive to import.

When importing the file, by default, the current configuration is preserved. For using the configuration from the zip archive, check the checkbox. 

Click the "Import" button for launching the import procedure. The import will take some time and can use a sizeable amount of memory on the database, as the operation is done in a single transaction. 
## External integrations

You can add customized javascript programs to react on application events.

It can be useful for example to notify an external system, like a slack channel.


### Script creation

To create a new integration, press the plus button. It will open the following modal window:

<img class="pure-img" src="{{relativeRootPath}}/images/en/integration-create.png" alt="create new integration modal window">

Insert the name, a description, configuration parameters (will be available in the global `configuration` variable) and the script.

The script receive the following global variables:

 - `log`: an instance of a Logger
 - `GSON`: an instance of Gson
 - `restTemplate`: an instance of a RestTemplate
 - `eventName`: a string with the current triggered event. See below the values
 - `project`: the project name (string)
 - `user`: an instance of io.lavagna.model.apihook.User: the user that triggered the event
 - `configuration`: a map containing configuration values
 - `data`: a map containing additional values

#### Supported events

 - CREATE_PROJECT
 - UPDATE_PROJECT
 - CREATE_BOARD, additional global variables:
    - `board`: short name of the board (string)
 - UPDATE_BOARD, additional global variables:
    - `board`: short name of the board (string)
 - CREATE_COLUMN, additional global variables:
    - `board`: short name of the board (string)
    - `columnName`: column name (string)
 - UPDATE_COLUMN, additional global variables:
    - `board`: short name of the board (string)
    - `previous`: previous column (io.lavagna.model.apihook.Column)
    - `updated`: current column (io.lavagna.model.apihook.Column)
 - CREATE_CARD, additional global variables:
    - `board`: short name of the board (string)
    - `card`: newly created card (io.lavagna.model.apihook.Card)
 - UPDATE_CARD, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `previous`: previous name (string)
    - `updated`: current name (string)
 - UPDATE_CARD_POSITION, additional global variables:
    - `board`: short name of the board (string)
    - `affectedCards`: the cards that are moved (list of io.lavagna.model.apihook.Card)
    - `from`: the source column (io.lavagna.model.apihook.Column)
    - `to`: the destination column (io.lavagna.model.apihook.Column)
 - UPDATE_DESCRIPTION, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `previous`: previous card data (io.lavagna.model.apihook.Card)
    - `updated`: current card data (io.lavagna.model.apihook.Card) 
 - CREATE_COMMENT, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `comment`: the comment (io.lavagna.model.apihook.CardData)
 - UPDATE_COMMENT, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `previous`: previous comment (io.lavagna.model.apihook.CardData)
    - `updated`: current comment (io.lavagna.model.apihook.CardData)
 - DELETE_COMMENT, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `comment`: the deleted comment (io.lavagna.model.apihook.CardData)
 - UNDO_DELETE_COMMENT, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `comment`: the undeleted comment (io.lavagna.model.apihook.CardData)
 - CREATE_ACTION_LIST, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
 - DELETE_ACTION_LIST, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
 - UNDO_DELETE_ACTION_LIST, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
 - UPDATE_ACTION_LIST, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `previous`: previous name of the list (string)
    - `updated`: current name of the list (string)
 - CREATE_ACTION_ITEM, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
    - `actionItem`: the text of the item (string)
 - DELETE_ACTION_ITEM, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
    - `actionItem`: the text of the item (string)
 - UNDO_DELETE_ACTION_ITEM, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
    - `actionItem`: the text of the item (string)
 - TOGGLE_ACTION_ITEM, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
    - `actionItem`: the text of the item (string)
    - `toggled`: the state of the action item (boolean) 
 - UPDATE_ACTION_ITEM, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionList`: the name of the action list (string)
    - `previous`: previous text (string)
    - `updated`: current text (string)
 - MOVE_ACTION_ITEM, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `actionItem`: the text of the item (string)
    - `from`: the name of the action list (string)
    - `to`:  the name of the action list (string)
 - CREATE_FILE, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `files`: the list of uploaded files (list of string)
 - DELETE_FILE, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `file`: the deleted file (string)
 - UNDO_DELETE_FILE, additional global variables:
    - `board`: short name of the board (string)
    - `card`: the card (io.lavagna.model.apihook.Card)
    - `file`: the undeleted file (string)
 - ADD_LABEL_VALUE_TO_CARD, additional global variables:
    - `board`: short name of the board (string)
    - `label`: the label (io.lavagna.model.apihook.Label)
    - `affectedCards`: the cards (list of io.lavagna.model.apihook.Card)
 - UPDATE_LABEL_VALUE, additional global variables:
    - `board`: short name of the board (string)
    - `label`: the label (io.lavagna.model.apihook.Label)
    - `affectedCards`: the cards (list of io.lavagna.model.apihook.Card)
 - REMOVE_LABEL_VALUE, additional global variables:
    - `board`: short name of the board (string)
    - `label`: the label (io.lavagna.model.apihook.Label)
    - `affectedCards`: the cards (list of io.lavagna.model.apihook.Card)

### Script example

The following script create post on a slack channel:

```
log.warn("eventName: " + eventName + ", project: " + project + ", 
    data: " + GSON.toJson(data));
var userName = user.displayName || user.username;

function formatCard(card) {
  return card.boardShortName + '-' + card.sequence + ' "' + card.name + '" ' + card.url;
}

function formatColumn(column) {
  return column.name;
}

var supportedEvents = {
  CREATE_CARD: function() {
    return {text: 'User "' + userName+'" has created the card: ' + formatCard(data.card)};
  },
  UPDATE_CARD_POSITION: function() {
    var moreThanOne = data.affectedCards.length > 1;
    var cardText = 'card'+(moreThanOne ? 's' : '');
    for(var i = 0; i < data.affectedCards.length; i++) {
      cardText += ' '+formatCard(data.affectedCards[i]);
    }
    return {text: 'User "' + userName+'" moved the ' + cardText + 
        ' from column ' + formatColumn(data.from) + ' to column ' + formatColumn(data.to)};
  },
  CREATE_COMMENT: function() {
    return {text: 'User "' + userName+'" has posted the comment: ' 
        +   data.comment.content  + ' in the card ' + formatCard(data.card)};
  },
  UPDATE_COMMENT: function() {
    return {text: 'User "' + userName+'" has updated a comment to' 
        + data.updated +' in the card ' + formatCard(data.card)}
  },
  UPDATE_DESCRIPTION: function() {
    return {text: 'User "' + userName+'" has updated the card description to ' 
        + data.updated.content +' in the card ' + formatCard(data.card)}
  }
};

if(supportedEvents[eventName]) {
  var payload = supportedEvents[eventName]();
  if(payload) {
    restTemplate.postForLocation('https://hooks.slack.com/services/.../.../...', payload);
  }
}
```

We check if the event is handled by our script by using a map of string, functions. 
If the event is present in the map, we execute the function.


### Manage the integration

All the integrations will be listed as shown below.


<img class="pure-img" src="{{relativeRootPath}}/images/en/integration-manage.png" alt="manage integrations">

Clicking on the <span class="icon icon-disable-sync"></span> button, will disable the script, for re-enable it, click on <span class="icon icon-enable-sync"></span>.

You can edit (<span class="icon icon-edit"></span>) and delete (<span class="icon icon-delete"></span>) the integration too.
.lvg-about-license__content {
	margin-left:10%;
	margin-right:10%;
	overflow: auto;
}<md-card class="lvg-content__row-item">
	<md-card-title>
		<md-card-title-text>
			<span>
				<span data-translate>about.lavagna-version</span>
				<span data-translate>build.version</span>
			</span>
		</md-card-title-text>
	</md-card-title>
	<md-card-content>
		<pre ng-bind="$ctrl.license" class="lvg-about-license__content"></pre>
	</md-card-content>
</md-card>
(function () {
    'use strict';

    angular.module('lavagna.components').component('lvgAboutLicense', {
        templateUrl: 'app/components/about/license/license.html',
        controller: ['$http', LicenseController]
    });

    function LicenseController($http) {
        var ctrl = this;

        ctrl.$onInit = function init() {
            $http.get('about/LICENSE-GPLv3.txt').then(function (res) {
                ctrl.license = res.data;
            });
        };
    }
}());
.lvg-about-licenses__content {
	overflow:hidden;
}<md-card class="lvg-content__row-item">
	<md-card-content>
		<pre data-ng-bind="$ctrl.thirdParty" class="lvg-about-licenses__content"></pre>
	</md-card-content>
</md-card>(function () {
    'use strict';

    angular.module('lavagna.components').component('lvgAboutLicenses', {
        templateUrl: 'app/components/about/licenses/licenses.html',
        controller: ['$http', LicensesController]
    });

    function LicensesController($http) {
        var ctrl = this;

        ctrl.$onInit = function init() {
            $http.get('about/THIRD-PARTY.txt').then(function (res) {
                ctrl.thirdParty = res.data;
            });
        };
    }
}());
