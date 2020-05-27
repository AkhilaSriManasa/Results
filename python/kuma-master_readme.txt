# Mozilla Community Participation Guidelines

This repository is governed by Mozilla's code of conduct and etiquette guidelines.
For more details, please read the
[Mozilla Community Participation Guidelines](https://www.mozilla.org/about/governance/policies/participation/).

## How to Report

For more information on how to report violations of the CPG, please read our
[How to Report](https://www.mozilla.org/en-US/about/governance/policies/participation/reporting/)
page.

## Project Specific Etiquette

See the [Contributing Guide][cg] for code standards, and the
[Bugzilla Developer Etiquette Guidelines](bdeg) for general tips for being a
helpful participant in an open source project.

[cg]: https://github.com/mdn/kuma/blob/master/CONTRIBUTING.md
[bdeg]: https://bugzilla.mozilla.org/page.cgi?id=etiquette.html
Things to know when contributing code
=====================================
* You agree to license your contributions under [MPL 2][MPL2].
* You agreed to follow the [Code of Conduct][coc].
* Discuss large changes in [Discourse][discourse] or on a
  [GitHub issue][bugs] before coding.
* We don't accept pull requests for translated strings (anything under
  ``locale/``). Please use [Pontoon][pontoon] instead.

[MPL2]: http://www.mozilla.org/MPL/2.0/
[coc]: https://github.com/mdn/kuma/blob/master/CODE_OF_CONDUCT.md
[discourse]: https://discourse.mozilla.org/c/mdn
[bugs]: https://github.com/mdn/kuma/issues
[pontoon]: https://pontoon.mozilla.org/projects/mdn/

What to work on
===============
The MDN platform is a mature product, which means there aren't always bugs that
are suitable for new contributors. We keep a list of starting mentored bugs on
the [MDN "Getting Involved" page][get-involved]. There are interesting
[MDN projects][mdn-projects] outside of writing Python for the platform, but
they may be harder to find. If you have questions about what to work on, you
can ask:

* In the #mdndev [IRC channel on irc.mozilla.org][irc-howto].
* In the [MDN Topic][discourse] in Discourse.

[get-involved]: https://wiki.mozilla.org/Webdev/GetInvolved/developer.mozilla.org#Mentored_Bugs
[irc-howto]: https://wiki.mozilla.org/Irc
[mdn-projects]: https://github.com/mdn

How to submit code
==================
The MDN development process is similar to [GitHub Flow][gh-flow]. The general
steps are:

1. [Install our development environment][install].
2. Create a branch for your bug.
3. Make your changes, and create one or more commits.
4. Push your branch to your fork.
5. Open a pull request (PR).
6. Fix any issues identified by [TravisCI][travisci], our automated testing
   provider.
7. Fix any issues identified by code review.

MDN staff will take a look at your PR in 1 to 2 business days, either to review
and give feedback, or to tell you when we plan to review it.

[gh-flow]: https://guides.github.com/introduction/flow/
[install]: https://kuma.readthedocs.io/en/latest/installation.html
[travisci]: https://travis-ci.org/mdn/kuma/pull_requests

Conventions
===========
Contributors should follow MDN conventions as much as possible. This maintains
code quality and makes it easier to research problems. At the same time, we
don't expect new contributors to be familiar with all the rules. Pull requests
will not be rejected just because they don't follow conventions. Depending on
your experience level, reviewers may ask you to bring your PR up to standards,
or may make the changes themselves before merging. As you become more
experienced, you will be expected to make these changes yourself.

Code
----
Python code style should follow [PEP8 standards][pep8]. The required subset
of PEP8 is checked by ``flake8`` (``make lint``). Other PEP8
and [PEP257][pep257] (docstring) conventions are encouraged but not yet
enforced.

In Python code, we prefer ``'single quotes'`` for code strings and
``"""triple double-quotes"""`` for docstrings. There are other style
conventions (such as import statement order and indenting) which can be
determined by reading existing code.

Similar standards are enforced for front-end assets like CSS and
JavaScript. Some are checked by tools, and other by code review.

[pep8]: http://www.python.org/dev/peps/pep-0008/
[pep257]: https://www.python.org/dev/peps/pep-0257/

Branches
--------
We prefer that branch names have a descriptive summary and the bug number. MDN
staff are working with multiple branches at a time, and this makes it easier
to remember which is which. ``noun-###`` or ``verb-noun-####`` are good
patterns to follow.  Some good branch names:

* ``cache-control-headers-1431259``
* ``update-requests-1399639``

Some bad branch names:

* ``bug973612`` - This name requires looking up bug details in Bugzilla.
* ``fix-973612`` - This still doesn't communicate what the branch changes.
* ``create-page`` - This doesn't include the bug number, which suggests the
  author isn't linking changes to a bug.
* ``1431259-cache-control-headers`` - Putting the bug number first makes it
  more difficult to use tab-completion.

Exceptions are branches used in the deployment process, such as
``stage-push`` and ``prod-push``, and submodule update branches, such as
``pre-push-2018-02-21``.

In general, we prefer branches are stored on a fork, rather than the origin
repository. There are exceptions, such as the ``stage-push`` and
the ``prod-push`` branches, when we want the branch to run on our continuous
integration server.

It is recommended and safe to delete branches after the pull request is closed.
GitHub will remember the code changes in the context of the pull request. Less
stale branches mean less clutter and confusion.

Commits
-------
We prefer one-commit pull requests that are small and focused.  Multiple commit
PRs are good when the solution naturally breaks into multiple steps. The test
suite should pass for each commit.

Once a pull request is open, we prefer changes as additional commits. This
makes it easier to review just the changes since the last review. Once a
pull request is approved, the commits can be "squashed" into a single commit
before merging. Squashing is usually decided by the reviewer, but feel free
to squash commits yourself, ask for commits to be squashed, or ask for them to
be kept separate.

All commit messages must start with ``bug NNNNNNN``. This format makes it
easier to consume the commit log and get back to the Bugzilla bug.  Bugzilla
is where proposed changes are discussed, where one or more related changes are
linked, and where regressions are tracked.  We sometimes omit a bug or bug
number for non-code commits such as merge commits, submodule updates, and
updating translatable strings.

``fix bug NNNNNNN`` can also be used. When these commits are merged, the bug is
marked RESOLVED: FIXED. ``fix bug`` can be used when merging will fix the
bug, such as documentation updates or build fixes. ``fix bug`` is discouraged
when the code needs to be deployed to production to fix the issue, or when
multiple PRs are expected.

The rules for a [great commit message](https://chris.beams.io/posts/git-commit/)
should be followed:

1. Separate the subject line from the body with a blank line.
2. Limit the subject line to 50 characters.
3. Capitalize the subject line.
4. Do not end the subject line with a period.
5. Use the imperative mood in the subject line.
6. Wrap the body at 72 characters.
7. Use the body to explain what and why versus how.

Here's an example of a decent commit message (which ends up much longer than
[the commit itself][crawl-delay-commit]!):

```
bug 1316610: Drop Crawl-delay, etc from robots.txt

Googlebot doesn't respect Crawl-delay, but instead watches to see how
fast it can index your site without breaking it.

Request-rate isn't known by Googlebot, and doesn't appear to be supported
by many crawlers.

MDN can be accessed faster than 5 pages per second, and we shouldn't
penalize scrapers that respect robots.txt.
```

[crawl-delay-commit]: https://github.com/mdn/kuma/commit/4ba37df42531589c4276ea2b4c44270ac1c49210

Testing
-------
MDN uses automated tests to prevent regressions and ensure that new code does
what it claims. Tests are required for new functionality, as measured by code
coverage tools, and all tests must pass before merging.

We use [TravisCI][travisci] to automatically run tests and quality checks when
a pull request is opened. If TravisCI identifies problems, we expect them to
be fixed before the code review starts.

It is a good idea to run the tests that apply to your change before opening a
pull request. It is useful to know [how to run the test suite][testing], and
how to run a subset of the tests.

Automated tests are in the process of being converted to [pytest][pytest], but
a lot of the old-style code remains. Contributors can write new tests in the
style of existing tests. They can also join MDN staff in converting to the new
style.  MDN staff is updating tests as we add or update functionality, so
seldom-updated code is more likely to have old-style tests. We expect a full
conversion to take a few more years.

We **avoid** old-style tests that use Django's
[TestCase testing classes][testcase], [fixture files][fixture_files] and
general-purpose factory functions like [get_user][get_user], [document][document],
and [revision][revision].

We **prefer** test functions, a small number of global
[pytest fixtures][pytest-fixtures] like [root_doc][root_doc] and
[wiki_user][wiki_user], adding application- and file-local fixtures
that customize the global fixtures, and using [assert][assert] for test
assertions.

[travisci]: https://travis-ci.org/mdn/kuma/pull_requests
[testing]: https://kuma.readthedocs.io/en/latest/tests.html#running-the-test-suite
[testcase]: https://docs.djangoproject.com/en/1.8/topics/testing/tools/#testcase
[fixture_files]: https://docs.djangoproject.com/en/1.8/topics/testing/tools/#fixture-loading
[eq]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/core/tests/__init__.py#L16
[ok]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/core/tests/__init__.py#L26
[get_user]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/core/tests/__init__.py#L36
[document]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/wiki/tests/__init__.py#L29
[revision]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/wiki/tests/__init__.py#L43
[pytest-fixtures]: https://docs.pytest.org/en/latest/fixture.html
[root_doc]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/conftest.py#L35
[wiki_user]: https://github.com/mdn/kuma/blob/6f31cbc22e72827e4832b3ed6ca542132bf41f83/kuma/conftest.py#L18
[assert]: https://docs.pytest.org/en/latest/assert.html
[pytest]: https://docs.pytest.org/en/latest/

We have a functional test suite that runs against a running MDN instance.
It can be challenging to run or alter these tests. A reviewer can determine if
changes are needed to functional tests, and if they need to be included in the
pull request or can be written (usually by staff) in a new PR.

Pull Requests
-------------
The author should include the bug number and a summary of the change as the
pull request title, and a description of the change as the pull request body.
A good commit message often makes a good PR message. An empty PR body is
rarely appropriate.

For bug fixes, it can be useful to include steps needed to reproduce the bug
in a development environment. It can also be useful to suggest manual tests
that a reviewer should try.

Do not double-submit a change as a patch in Bugzilla. If you like, you can
update the bug to link to your pull request and mark yourself as the assignee.

Code Reviews
------------
Code reviews help us maintain and improve code quality. It can also be
stressful to have your work criticized. Code reviewers should point out
good code as well as bad, be clear when changes are needed, and offer
suggestions for fixing code. Code authors should ask questions when a
suggestion is unclear, and ask for help if needed. On both sides, the review
should be about the code, not the person, and the [code of conduct][coc] must
be followed.

An MDN module [owner or peer][peers] must review and merge all pull requests.
Owner and peers are accountable for the quality of MDN code changes, and
often know when a change will have a wider than expected impact. In an
emergency, code may be merged without review, but a bug should be filed for a
follow-up review. There may also be exceptions for changes that don't impact
production.

[peers]: https://wiki.mozilla.org/Modules/All#MDN

Pull requests that modify the database must be reviewed by a module owner.
Changes to database tables are critical and may lead to loss of data. They are
also tricky to deploy, usually requiring multiple deployments.

Security changes should be reviewed outside of the public repository. They are
manually merged by a peer, and the commit should include a comment such as
``r=username`` to say who the reviewer was.

A reviewer may identify a "nit", which is a style preference that isn't
important enough to reject a pull request. Feel free to fix or ignore nits if
desired.

We use the following labels for pull requests:
* **manual merge**: This pull request is ready, but additional steps outside
  of code review are needed to merge it.
* **not ready**: The author says this pull request isn't ready to review. For
  example, it requires tests or documentation.

In general, the reviewer merges the pull request. When reviewing a PR from a
staff member, a reviewer may approve the PR with nits, and let the author
merge after fixing minor issues.

Deployment and Closing Bugs
---------------------------
MDN staff deploy new code one to three times a week. Deployments are announced
in the #mdndev IRC channel. Currently deployed code can be seen on the
[What's Deployed?](https://whatsdeployed.io/s-HC0) page.

Once a bug fix is in production, the bug can be marked as RESOLVED:FIXED.
Mozilla Public License Version 2.0
==================================

1. Definitions
--------------

1.1. "Contributor"
    means each individual or legal entity that creates, contributes to
    the creation of, or owns Covered Software.

1.2. "Contributor Version"
    means the combination of the Contributions of others (if any) used
    by a Contributor and that particular Contributor's Contribution.

1.3. "Contribution"
    means Covered Software of a particular Contributor.

1.4. "Covered Software"
    means Source Code Form to which the initial Contributor has attached
    the notice in Exhibit A, the Executable Form of such Source Code
    Form, and Modifications of such Source Code Form, in each case
    including portions thereof.

1.5. "Incompatible With Secondary Licenses"
    means

    (a) that the initial Contributor has attached the notice described
        in Exhibit B to the Covered Software; or

    (b) that the Covered Software was made available under the terms of
        version 1.1 or earlier of the License, but not also under the
        terms of a Secondary License.

1.6. "Executable Form"
    means any form of the work other than Source Code Form.

1.7. "Larger Work"
    means a work that combines Covered Software with other material, in 
    a separate file or files, that is not Covered Software.

1.8. "License"
    means this document.

1.9. "Licensable"
    means having the right to grant, to the maximum extent possible,
    whether at the time of the initial grant or subsequently, any and
    all of the rights conveyed by this License.

1.10. "Modifications"
    means any of the following:

    (a) any file in Source Code Form that results from an addition to,
        deletion from, or modification of the contents of Covered
        Software; or

    (b) any new file in Source Code Form that contains any Covered
        Software.

1.11. "Patent Claims" of a Contributor
    means any patent claim(s), including without limitation, method,
    process, and apparatus claims, in any patent Licensable by such
    Contributor that would be infringed, but for the grant of the
    License, by the making, using, selling, offering for sale, having
    made, import, or transfer of either its Contributions or its
    Contributor Version.

1.12. "Secondary License"
    means either the GNU General Public License, Version 2.0, the GNU
    Lesser General Public License, Version 2.1, the GNU Affero General
    Public License, Version 3.0, or any later versions of those
    licenses.

1.13. "Source Code Form"
    means the form of the work preferred for making modifications.

1.14. "You" (or "Your")
    means an individual or a legal entity exercising rights under this
    License. For legal entities, "You" includes any entity that
    controls, is controlled by, or is under common control with You. For
    purposes of this definition, "control" means (a) the power, direct
    or indirect, to cause the direction or management of such entity,
    whether by contract or otherwise, or (b) ownership of more than
    fifty percent (50%) of the outstanding shares or beneficial
    ownership of such entity.

2. License Grants and Conditions
--------------------------------

2.1. Grants

Each Contributor hereby grants You a world-wide, royalty-free,
non-exclusive license:

(a) under intellectual property rights (other than patent or trademark)
    Licensable by such Contributor to use, reproduce, make available,
    modify, display, perform, distribute, and otherwise exploit its
    Contributions, either on an unmodified basis, with Modifications, or
    as part of a Larger Work; and

(b) under Patent Claims of such Contributor to make, use, sell, offer
    for sale, have made, import, and otherwise transfer either its
    Contributions or its Contributor Version.

2.2. Effective Date

The licenses granted in Section 2.1 with respect to any Contribution
become effective for each Contribution on the date the Contributor first
distributes such Contribution.

2.3. Limitations on Grant Scope

The licenses granted in this Section 2 are the only rights granted under
this License. No additional rights or licenses will be implied from the
distribution or licensing of Covered Software under this License.
Notwithstanding Section 2.1(b) above, no patent license is granted by a
Contributor:

(a) for any code that a Contributor has removed from Covered Software;
    or

(b) for infringements caused by: (i) Your and any other third party's
    modifications of Covered Software, or (ii) the combination of its
    Contributions with other software (except as part of its Contributor
    Version); or

(c) under Patent Claims infringed by Covered Software in the absence of
    its Contributions.

This License does not grant any rights in the trademarks, service marks,
or logos of any Contributor (except as may be necessary to comply with
the notice requirements in Section 3.4).

2.4. Subsequent Licenses

No Contributor makes additional grants as a result of Your choice to
distribute the Covered Software under a subsequent version of this
License (see Section 10.2) or under the terms of a Secondary License (if
permitted under the terms of Section 3.3).

2.5. Representation

Each Contributor represents that the Contributor believes its
Contributions are its original creation(s) or it has sufficient rights
to grant the rights to its Contributions conveyed by this License.

2.6. Fair Use

This License is not intended to limit any rights You have under
applicable copyright doctrines of fair use, fair dealing, or other
equivalents.

2.7. Conditions

Sections 3.1, 3.2, 3.3, and 3.4 are conditions of the licenses granted
in Section 2.1.

3. Responsibilities
-------------------

3.1. Distribution of Source Form

All distribution of Covered Software in Source Code Form, including any
Modifications that You create or to which You contribute, must be under
the terms of this License. You must inform recipients that the Source
Code Form of the Covered Software is governed by the terms of this
License, and how they can obtain a copy of this License. You may not
attempt to alter or restrict the recipients' rights in the Source Code
Form.

3.2. Distribution of Executable Form

If You distribute Covered Software in Executable Form then:

(a) such Covered Software must also be made available in Source Code
    Form, as described in Section 3.1, and You must inform recipients of
    the Executable Form how they can obtain a copy of such Source Code
    Form by reasonable means in a timely manner, at a charge no more
    than the cost of distribution to the recipient; and

(b) You may distribute such Executable Form under the terms of this
    License, or sublicense it under different terms, provided that the
    license for the Executable Form does not attempt to limit or alter
    the recipients' rights in the Source Code Form under this License.

3.3. Distribution of a Larger Work

You may create and distribute a Larger Work under terms of Your choice,
provided that You also comply with the requirements of this License for
the Covered Software. If the Larger Work is a combination of Covered
Software with a work governed by one or more Secondary Licenses, and the
Covered Software is not Incompatible With Secondary Licenses, this
License permits You to additionally distribute such Covered Software
under the terms of such Secondary License(s), so that the recipient of
the Larger Work may, at their option, further distribute the Covered
Software under the terms of either this License or such Secondary
License(s).

3.4. Notices

You may not remove or alter the substance of any license notices
(including copyright notices, patent notices, disclaimers of warranty,
or limitations of liability) contained within the Source Code Form of
the Covered Software, except that You may alter any license notices to
the extent required to remedy known factual inaccuracies.

3.5. Application of Additional Terms

You may choose to offer, and to charge a fee for, warranty, support,
indemnity or liability obligations to one or more recipients of Covered
Software. However, You may do so only on Your own behalf, and not on
behalf of any Contributor. You must make it absolutely clear that any
such warranty, support, indemnity, or liability obligation is offered by
You alone, and You hereby agree to indemnify every Contributor for any
liability incurred by such Contributor as a result of warranty, support,
indemnity or liability terms You offer. You may include additional
disclaimers of warranty and limitations of liability specific to any
jurisdiction.

4. Inability to Comply Due to Statute or Regulation
---------------------------------------------------

If it is impossible for You to comply with any of the terms of this
License with respect to some or all of the Covered Software due to
statute, judicial order, or regulation then You must: (a) comply with
the terms of this License to the maximum extent possible; and (b)
describe the limitations and the code they affect. Such description must
be placed in a text file included with all distributions of the Covered
Software under this License. Except to the extent prohibited by statute
or regulation, such description must be sufficiently detailed for a
recipient of ordinary skill to be able to understand it.

5. Termination
--------------

5.1. The rights granted under this License will terminate automatically
if You fail to comply with any of its terms. However, if You become
compliant, then the rights granted under this License from a particular
Contributor are reinstated (a) provisionally, unless and until such
Contributor explicitly and finally terminates Your grants, and (b) on an
ongoing basis, if such Contributor fails to notify You of the
non-compliance by some reasonable means prior to 60 days after You have
come back into compliance. Moreover, Your grants from a particular
Contributor are reinstated on an ongoing basis if such Contributor
notifies You of the non-compliance by some reasonable means, this is the
first time You have received notice of non-compliance with this License
from such Contributor, and You become compliant prior to 30 days after
Your receipt of the notice.

5.2. If You initiate litigation against any entity by asserting a patent
infringement claim (excluding declaratory judgment actions,
counter-claims, and cross-claims) alleging that a Contributor Version
directly or indirectly infringes any patent, then the rights granted to
You by any and all Contributors for the Covered Software under Section
2.1 of this License shall terminate.

5.3. In the event of termination under Sections 5.1 or 5.2 above, all
end user license agreements (excluding distributors and resellers) which
have been validly granted by You or Your distributors under this License
prior to termination shall survive termination.

************************************************************************
*                                                                      *
*  6. Disclaimer of Warranty                                           *
*  -------------------------                                           *
*                                                                      *
*  Covered Software is provided under this License on an "as is"       *
*  basis, without warranty of any kind, either expressed, implied, or  *
*  statutory, including, without limitation, warranties that the       *
*  Covered Software is free of defects, merchantable, fit for a        *
*  particular purpose or non-infringing. The entire risk as to the     *
*  quality and performance of the Covered Software is with You.        *
*  Should any Covered Software prove defective in any respect, You     *
*  (not any Contributor) assume the cost of any necessary servicing,   *
*  repair, or correction. This disclaimer of warranty constitutes an   *
*  essential part of this License. No use of any Covered Software is   *
*  authorized under this License except under this disclaimer.         *
*                                                                      *
************************************************************************

************************************************************************
*                                                                      *
*  7. Limitation of Liability                                          *
*  --------------------------                                          *
*                                                                      *
*  Under no circumstances and under no legal theory, whether tort      *
*  (including negligence), contract, or otherwise, shall any           *
*  Contributor, or anyone who distributes Covered Software as          *
*  permitted above, be liable to You for any direct, indirect,         *
*  special, incidental, or consequential damages of any character      *
*  including, without limitation, damages for lost profits, loss of    *
*  goodwill, work stoppage, computer failure or malfunction, or any    *
*  and all other commercial damages or losses, even if such party      *
*  shall have been informed of the possibility of such damages. This   *
*  limitation of liability shall not apply to liability for death or   *
*  personal injury resulting from such party's negligence to the       *
*  extent applicable law prohibits such limitation. Some               *
*  jurisdictions do not allow the exclusion or limitation of           *
*  incidental or consequential damages, so this exclusion and          *
*  limitation may not apply to You.                                    *
*                                                                      *
************************************************************************

8. Litigation
-------------

Any litigation relating to this License may be brought only in the
courts of a jurisdiction where the defendant maintains its principal
place of business and such litigation shall be governed by laws of that
jurisdiction, without reference to its conflict-of-law provisions.
Nothing in this Section shall prevent a party's ability to bring
cross-claims or counter-claims.

9. Miscellaneous
----------------

This License represents the complete agreement concerning the subject
matter hereof. If any provision of this License is held to be
unenforceable, such provision shall be reformed only to the extent
necessary to make it enforceable. Any law or regulation which provides
that the language of a contract shall be construed against the drafter
shall not be used to construe this License against a Contributor.

10. Versions of the License
---------------------------

10.1. New Versions

Mozilla Foundation is the license steward. Except as provided in Section
10.3, no one other than the license steward has the right to modify or
publish new versions of this License. Each version will be given a
distinguishing version number.

10.2. Effect of New Versions

You may distribute the Covered Software under the terms of the version
of the License under which You originally received the Covered Software,
or under the terms of any subsequent version published by the license
steward.

10.3. Modified Versions

If you create software not governed by this License, and you want to
create a new license for such software, you may create and use a
modified version of this License if you rename the license and remove
any references to the name of the license steward (except to note that
such modified license differs from this License).

10.4. Distributing Source Code Form that is Incompatible With Secondary
Licenses

If You choose to distribute Source Code Form that is Incompatible With
Secondary Licenses under the terms of this version of the License, the
notice described in Exhibit B of this License must be attached.

Exhibit A - Source Code Form License Notice
-------------------------------------------

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

If it is not possible or desirable to put the notice in a particular
file, then You may include the notice in a location (such as a LICENSE
file in a relevant directory) where a recipient would be likely to look
for such a notice.

You may add additional accurate notices of copyright ownership.

Exhibit B - "Incompatible With Secondary Licenses" Notice
---------------------------------------------------------

  This Source Code Form is "Incompatible With Secondary Licenses", as
  defined by the Mozilla Public License, v. 2.0.
====
Kuma
====

.. image:: https://travis-ci.org/mdn/kuma.svg?branch=master
   :target: https://travis-ci.org/mdn/kuma
   :alt: Build Status

.. image:: https://codecov.io/github/mdn/kuma/coverage.svg?branch=master
   :target: https://codecov.io/github/mdn/kuma?branch=master
   :alt: Code Coverage Status

.. image:: https://requires.io/github/mdn/kuma/requirements.svg?branch=master
   :target: https://requires.io/github/mdn/kuma/requirements/?branch=master
   :alt: Requirements Status

.. image:: http://img.shields.io/badge/license-MPL2-blue.svg
   :target: https://raw.githubusercontent.com/mdn/kuma/master/LICENSE
   :alt: License

.. image:: https://img.shields.io/badge/whatsdeployed-stage,prod-green.svg
   :target: https://whatsdeployed.io/s/HC0/mdn/kuma
   :alt: What's deployed on stage,prod?

.. Omit badges from docs

Kuma is the platform that powers `MDN (developer.mozilla.org)
<https://developer.mozilla.org>`_

Development
===========

:Code:          https://github.com/mdn/kuma
:Issues:        `P1 Bugs`_ (to be fixed in current or next sprint_)

                `P2 Bugs`_ (to be fixed in 180 days)

                `All developer.mozilla.org bugs`_

                `Pull Request Queues`_
:Dev Docs:      https://kuma.readthedocs.io/en/latest/installation.html
:CI Server:     https://travis-ci.org/mdn/kuma
:Forum:         https://discourse.mozilla.org/c/mdn
:IRC:           irc://irc.mozilla.org/mdndev
:Servers:       `What's Deployed on MDN?`_

                https://developer.allizom.org/ (stage)

                https://developer.mozilla.org/ (prod)

.. _`P1 Bugs`: https://github.com/mdn/kuma/issues?q=is%3Aopen+is%3Aissue+label%3Ap1
.. _`P2 Bugs`: https://github.com/mdn/kuma/issues?q=is%3Aopen+is%3Aissue+label%3Ap2
.. _`All developer.mozilla.org bugs`: https://mzl.la/2onLvZ8
.. _`Pull Request Queues`: http://prs.mozilla.io/mdn:kuma,kumascript,infra,mdn-fiori
.. _`What's Deployed on MDN?`: https://whatsdeployed.io/s/HC0/mdn/kuma
.. _sprint: https://wiki.mozilla.org/Engagement/MDN_Durable_Team/Processes#Planning_Sprints


Getting started
===============

Want to help make MDN great? Our `contribution guide
<https://github.com/mdn/kuma/blob/master/CONTRIBUTING.md>`_ lists some good
first projects and offers direction on submitting code.
---
name: Bug report
about: Help us fix things that are broken
title: ''
labels: 'status: needs triage'
assignees: ''

---

**Summary**
_What is the problem?_


**Steps To Reproduce (STR)**
_How can we reproduce the problem?_

1. 
2. 
3. 


**Actual behavior**
_What actually happened?_


**Expected behavior**
_What did you expect to happen?_


**Additional context**
_Is there anything else we should know?_
---
name: Change request
about: Suggest a change to how MDN currently works
title: ''
labels: 'status: needs triage'
assignees: ''

---

**Summary**
_What should be changed? (Please provide a URL if applicable)_


**Rationale**
_What problems would this solve?_


**Audience**
_Who would use this changed feature?_


**Proposal**
_What would users see and do? What would happen as a result?_


**Additional context**
_Is there anything else we should know?_
---
name: Feature request
about: Suggest a new idea for MDN
title: ''
labels: 'status: needs triage'
assignees: ''

---

**Summary**
_What problem would this solve?_


**Audience**
_Who has this problem? Everyone? Article authors? Etc._


**Rationale**
_How do you know that people identified above actually have this problem?_


**Workaround**
_How are the people identified above currently handling this problem?_


**Proposal**
_Do you have suggestions for solving this problem?_


**Additional context**
_Is there anything else we should know?_
---
name: Support request
about: Request a support task from the MDN team.
title: ''
labels: 'status: needs triage'
assignees: ''

---

**Summary**
_What support task would you like completed by the team?_


**Rationale**
_What problems would this solve?_


**Due Date**
_When would you like this task completed by?_


**Additional context**
_Is there anything else we should know?_
Kuma Assets
===========
This folder contains front-end assets for developer.mozilla.org.

In production, they are collected to ``/static``, processed to add
a hash of the contents to the name, and served to users.
In development, some may be served from this folder, to speed up
development. See
[Building, collecting, and serving assets](https://kuma.readthedocs.io/en/latest/assets.html)
for the details.

Here are the subfolders:

* `build`: (TODO) Output of ``make compilejsi18n``, copied to
  ``static/build``.
* `ckeditor4`: The source and build folders for CKEditor 4.
  ``ckeditor4/build`` is copied to ``static/js/libs/ckeditor4/build``.
* `dist`: (TODO) Output of the ``webpack`` process, copied to ``static/dist``.
* `legacy`: These files are no longer served to users, and are candidates
  for deletion.
* `lib`: (TODO) Third-party libraries that are served to users.
* `pipeline`: (TODO) Input of the ``process:sass`` npm script. It should be possible to
  convert these to ``webpack`` some day.
* `reference`: These files are related to assets, but are not part of an
  automated build process, and are not served to users.
* `src`: (TODO) Input for the ``webpack`` process.
* `static`: These files are copied to ``/static``. Small files (under 32
  kilobytes) in a folder called `embed` (such as `static/img/embed`) may be
  inlined as ``data:`` by
  [django-pipeline](https://django-pipeline.readthedocs.io/en/latest/configuration.html#embedding-fonts-and-images).
CKEditor 4 Changelog
====================

## CKEditor 4.5.10

Fixed Issues:

* [#10750](http://dev.ckeditor.com/ticket/10750): Fixed: The editor does not escape the `font-style` family property correctly, removing quotes and whitespace from font names.
* [#14413](http://dev.ckeditor.com/ticket/14413): Fixed: The [Auto Grow](http://ckeditor.com/addon/autogrow) plugin with the [`config.autoGrow_onStartup`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-autoGrow_onStartup) option set to `true` does not work properly for an editor that is not visible.
* [#14451](http://dev.ckeditor.com/ticket/14451): Fixed: Numeric element ID not escaped properly. Thanks to [Jakub Chalupa](https://github.com/chaluja7)!
* [#14590](http://dev.ckeditor.com/ticket/14590): Fixed: Additional line break appearing after inline elements when switching modes. Thanks to [dpidcock](https://github.com/dpidcock)!
* [#14539](https://dev.ckeditor.com/ticket/14539): Fixed: JAWS reads "selected Blank" instead of "selected <widget name>" when selecting a widget.
* [#14701](http://dev.ckeditor.com/ticket/14701): Fixed: More precise labels for [Enhanced Image](http://ckeditor.com/addon/image2) and [Placeholder](http://ckeditor.com/addon/placeholder) widgets.
* [#14667](http://dev.ckeditor.com/ticket/14667): [IE] Fixed: Removing background color from selected text removes background color from the whole paragraph.
* [#14252](http://dev.ckeditor.com/ticket/14252): [IE] Fixed: Styles drop-down list does not always reflect the current style of the text line.
* [#14275](http://dev.ckeditor.com/ticket/14275): [IE9+] Fixed: `onerror` and `onload` events are not used in browsers it could have been used when loading scripts dynamically.


## CKEditor 4.5.9

Fixed Issues:

* [#10685](http://dev.ckeditor.com/ticket/10685): Fixed: Unreadable toolbar icons after updating to the new editor version. Fixed with [6876179](https://github.com/ckeditor/ckeditor-dev/commit/6876179db4ee97e786b07b8fd72e6b4120732185) in [ckeditor-dev](https://github.com/ckeditor/ckeditor-dev) and [6c9189f4](https://github.com/ckeditor/ckeditor-presets/commit/6c9189f46392d2c126854fe8889b820b8c76d291) in [ckeditor-presets](https://github.com/ckeditor/ckeditor-presets).
* [#14573](https://dev.ckeditor.com/ticket/14573): Fixed: Missing [Widget](http://ckeditor.com/addon/widget) drag handler CSS when there are multiple editor instances.
* [#14620](https://dev.ckeditor.com/ticket/14620): Fixed: Setting both the `min-height` style for the `<body>` element and the `height` style for the `<html>` element breaks the [Auto Grow](http://ckeditor.com/addon/autogrow) plugin.
* [#14538](http://dev.ckeditor.com/ticket/14538): Fixed: Keyboard focus goes into an embedded `<iframe>` element.
* [#14602](http://dev.ckeditor.com/ticket/14602): Fixed: The [`dom.element.removeAttribute()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-removeAttribute) method does not remove all attributes if no parameter is given.
* [#8679](http://dev.ckeditor.com/ticket/8679): Fixed: Better focus indication and ability to style the selected color in the [color picker dialog](http://ckeditor.com/addon/colordialog).
* [#11697](http://dev.ckeditor.com/ticket/11697): Fixed: Content is replaced ignoring the letter case setting in the [Find and Replace](http://ckeditor.com/addon/find) dialog window.
* [#13886](http://dev.ckeditor.com/ticket/13886): Fixed: Invalid handling of the [`CKEDITOR.style`](http://docs.ckeditor.com/#!/api/CKEDITOR.style) instance with the `styles` property by [`CKEDITOR.filter`](http://docs.ckeditor.com/#!/api/CKEDITOR.filter).
* [#14535](http://dev.ckeditor.com/ticket/14535): Fixed: CSS syntax corrections. Thanks to [mdjdenormandie](https://github.com/mdjdenormandie)!
* [#14312](http://dev.ckeditor.com/ticket/14312): [IE] Fixed: Artifact is visible after pasting any text.

## CKEditor 4.5.8

New Features:

* [#12440](http://dev.ckeditor.com/ticket/12440): Added the [`config.colorButton_enableAutomatic`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-colorButton_enableAutomatic) option to allow hiding the "Automatic" option in the [color picker](http://ckeditor.com/addon/colorbutton).

Fixed Issues:

* [#10448](http://dev.ckeditor.com/ticket/10448): Fixed: Lack of scrollbar in the [right-to-left text direction](http://ckeditor.com/addon/bidi).
* [#12707](http://dev.ckeditor.com/ticket/12707): Fixed: The order of table elements does not comply with the HTML specification.
* [#13756](http://dev.ckeditor.com/ticket/13756): [Edge] Fixed: Context menus are cut-off.

## CKEditor 4.5.7

New Features:

* [#14327](http://dev.ckeditor.com/ticket/14327): Added Swiss German localization. Thanks to [Miro Grenda](https://twitter.com/mirogrenda)!

Fixed Issues:

* [#13816](http://dev.ckeditor.com/ticket/13816): Introduced a new strategy for Filling Character handling to avoid changes in DOM. This fixes the following issues:
	* [#12727](http://dev.ckeditor.com/ticket/12727): [Blink] `IndexSizeError` when using the [Div Editing Area](http://ckeditor.com/addon/divarea) and [Content Templates](http://ckeditor.com/addon/templates) plugins.
	* [#13377](http://dev.ckeditor.com/ticket/13377): [Widget](http://ckeditor.com/addon/widget) plugin issue when typing in Korean.
	* [#13389](http://dev.ckeditor.com/ticket/13389): [Blink] [`editor.getData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getData) fails when the cursor is next to an `<hr>` tag.
	* [#13513](http://dev.ckeditor.com/ticket/13513): [Blink, WebKit] [Div Editing Area](http://ckeditor.com/addon/divarea) and [`editor.getData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getData) throw an error when an image is the only data in the editor.
* [#13884](http://dev.ckeditor.com/ticket/13884): [Firefox] Fixed: Copying and pasting a table results in just the first cell being pasted.
* [#14234](http://dev.ckeditor.com/ticket/14234): Fixed: URL input field is not marked as required in the [Media Embed](http://ckeditor.com/addon/embed) dialog.

## CKEditor 4.5.6

New Features:

* Introduced the [`CKEDITOR.tools.getCookie()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-getCookie) and [`CKEDITOR.tools.setCookie()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-setCookie) methods for accessing cookies.
* Introduced the [`CKEDITOR.tools.getCsrfToken()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-getCsrfToken) method. The CSRF token is now automatically sent by the [File Browser](http://ckeditor.com/addon/filebrowser) and [File Tools](http://ckeditor.com/addon/filetools) plugins during file uploads. The server-side upload handlers may check it and use it to additionally secure the communication.

Other Changes:

* Updated [SCAYT](http://ckeditor.com/addon/scayt) (Spell Check As You Type):
	- New features:
		- CKEditor [Language](http://ckeditor.com/addon/language) plugin support.
		- CKEditor [Placeholder](http://ckeditor.com/addon/placeholder) plugin support.
		- [Drag&Drop](http://sdk.ckeditor.com/samples/fileupload.html) support.
		- **Experimental** [GRAYT](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-grayt_autoStartup) (Grammar As You Type) functionality.
	- Fixed issues:
		* [#98](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/98): SCAYT affects dialog double-click. Fixed in SCAYT core.
		* [#102](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/102): SCAYT core performance enhancements.
		* [#104](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/104): SCAYT's spans leak into the clipboard and after pasting.
		* [#105](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/105): A JavaScript error fired in case of multiple instances of CKEditor on one page.
		* [#107](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/107): SCAYT should not check non-editable parts of content.
		* [#108](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/108): Latest SCAYT copies the ID of the editor element to the iframe.
		* SCAYT stops working when CKEditor [Undo plugin](http://ckeditor.com/addon/undo) not enabled.
		* Issue with pasting SCAYT markup in CKEditor.
		* SCAYT stops working after pressing the *Cancel* button in the WSC dialog.

## CKEditor 4.5.5

Fixed Issues:

* [#13887](https://dev.ckeditor.com/ticket/13887): Fixed: [Link](http://ckeditor.com/addon/link) plugin alters the `target` attribute value. Thanks to [SamZiemer](https://github.com/SamZiemer)!
* [#12189](http://dev.ckeditor.com/ticket/12189): Fixed: The [Link](http://ckeditor.com/addon/link) plugin dialog does not display the subject of email links if the subject parameter is not lowercase.
* [#9192](http://dev.ckeditor.com/ticket/9192): Fixed: An `undefined` string is appended to an email address added with the [Link](http://ckeditor.com/addon/link) plugin if subject and email body are empty and [`config.emailProtection`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-emailProtection) is set to `encode`.
* [#13790](https://dev.ckeditor.com/ticket/13790): Fixed: It is not possible to destroy the editor `<iframe>` after the editor was detached from DOM. Thanks to [Stefan Rijnhart](https://github.com/StefanRijnhart)!
* [#13803](https://dev.ckeditor.com/ticket/13803): Fixed: The editor cannot be destroyed before being fully initialized. Thanks to [Cyril Fluck](https://github.com/cyril-sf)!
* [#13867](http://dev.ckeditor.com/ticket/13867): Fixed: CKEditor does not work when the `classList` polyfill is used.
* [#13885](http://dev.ckeditor.com/ticket/13885): Fixed: [Enhanced Image](http://ckeditor.com/addon/image2) requires the [Link](http://ckeditor.com/addon/link) plugin to link an image.
* [#13883](http://dev.ckeditor.com/ticket/13883): Fixed: Copying a table using the context menu strips off styles.
* [#13872](http://dev.ckeditor.com/ticket/13872): Fixed: Cutting is possible in the [read-only](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-readOnly) mode.
* [#12848](http://dev.ckeditor.com/ticket/12848): [Blink] Fixed: Opening the [Find and Replace](http://ckeditor.com/addon/find) dialog window in the [read-only](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-readOnly) mode throws an exception.
* [#13879](http://dev.ckeditor.com/ticket/13879): Fixed: It is not possible to prevent the [`editor.drop`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-drop) event.
* [#13361](http://dev.ckeditor.com/ticket/13361): Fixed: Skin images fail when the site path includes parentheses because the `background-image` path needs single quotes around the URL value.
* [#13771](http://dev.ckeditor.com/ticket/13771): Fixed: The `contents.css` style is not used if the [IFrame Editing Area](http://ckeditor.com/addon/wysiwygarea) plugin is missing.
* [#13782](http://dev.ckeditor.com/ticket/13782): Fixed: Unclear log messages.
* [#13919](http://dev.ckeditor.com/ticket/13919): [Edge] Fixed: Browser window crashes when accessing the `isContentEditable` property of an `<input>` DOM element.

Other Changes:

* [#13859](http://dev.ckeditor.com/ticket/13859): Test cases created with `bender.tools.createTestsForEditors` will also receive editor bot as a second parameter.

## CKEditor 4.5.4

New Features:

* [#13632](http://dev.ckeditor.com/ticket/13632): Introduce error logging mechanism.
* [#13730](http://dev.ckeditor.com/ticket/13730): Switch to the new error logging mechanism.

Fixed Issues:

* [#9856](http://dev.ckeditor.com/ticket/9856): Fixed: Cannot use the native context menu together with the [Div Editing Area](http://ckeditor.com/addon/divarea) plugin. Thanks to [Mark Wade](https://github.com/mark-wade)!
* [#12733](http://dev.ckeditor.com/ticket/12733): [IE9+] Fixed: Radio button `onChange` does not work. Thanks to [Iliya Kostadinov](https://github.com/iliyakostadinov)!
* [#13142](http://dev.ckeditor.com/ticket/13142): [Edge] Fixed: *Ctrl+A* and then *Backspace* result in an empty `<div>` element.
* [#13599](http://dev.ckeditor.com/ticket/13599): Fixed: Cross-editor drag and drop of an inline widget results in error/artifacts.
* [#13640](http://dev.ckeditor.com/ticket/13640): [IE] Fixed: Dropping a widget outside the `<body>` element is not handled correctly.
* [#13533](http://dev.ckeditor.com/ticket/13533): Fixed: No progress during upload.
* [#13680](http://dev.ckeditor.com/ticket/13680): Fixed: The parser should allow the `<h1-6>` element to be a child of the `<summary>` element.
* [#11724](http://dev.ckeditor.com/ticket/11724): [Touch devices] Fixed: Drop-downs often hide right after opening them.
* [#13690](http://dev.ckeditor.com/ticket/13690): Fixed: Copying content from IE to Chrome adds an extra paragraph.
* [#13284](http://dev.ckeditor.com/ticket/13284): Fixed: Cannot drag and drop a widget if the text caret is placed just after the widget instance.
* [#13516](http://dev.ckeditor.com/ticket/13516): Fixed: CKEditor removes empty HTML5 anchors without the `name` attribute.
* [#13765](http://dev.ckeditor.com/ticket/13765): [Safari 9] Fixed: Problems with rendering samples.

Other Changes:

* [#11725](http://dev.ckeditor.com/ticket/11725): Marked [`CKEDITOR.env.mobile`](http://docs.ckeditor.com/#!/api/CKEDITOR.env-property-mobile) as deprecated. The reason is that it is no longer clear what "mobile" means.
* [#13737](http://dev.ckeditor.com/ticket/13737): Upgraded [Bender.js](https://github.com/benderjs/benderjs) to 0.4.1.

## CKEditor 4.5.3

New Features:

* [#13501](http://dev.ckeditor.com/ticket/13501): Added the [`config.fileTools_defaultFileName`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-fileTools_defaultFileName) option to allow setting a default file name for paste uploads.
* [#13603](http://dev.ckeditor.com/ticket/13603): Added support for uploading dropped BMP images.

Fixed Issues:

* [#13590](http://dev.ckeditor.com/ticket/13590): Fixed: Various issues related to the [Paste from Word](http://ckeditor.com/addon/pastefromword) feature. Fixes also:
  * [#11215](http://dev.ckeditor.com/ticket/11215),
  * [#8780](http://dev.ckeditor.com/ticket/8780),
  * [#12762](http://dev.ckeditor.com/ticket/12762).
* [#13386](http://dev.ckeditor.com/ticket/13386): [Edge] Fixed: Issues with selecting and editing images.
* [#13568](http://dev.ckeditor.com/ticket/13568): Fixed: The [`editor.getSelectedHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getSelectedHtml) method returns invalid results for entire content selection.
* [#13453](http://dev.ckeditor.com/ticket/13453): Fixed: Drag&drop of entire editor content throws an error.
* [#13465](http://dev.ckeditor.com/ticket/13465): Fixed: Error is thrown and the widget is lost on drag&drop if it is the only content of the editor.
* [#13414](http://dev.ckeditor.com/ticket/13414): Fixed: Content auto paragraphing in a nested editable despite editor configuration.
* [#13429](http://dev.ckeditor.com/ticket/13429): Fixed: Incorrect selection after content insertion by the [Auto Embed](http://ckeditor.com/addon/autoembed) plugin.
* [#13388](http://dev.ckeditor.com/ticket/13388): Fixed: [Table Resize](http://ckeditor.com/addon/tableresize) integration with [Undo](http://ckeditor.com/addon/undo) is broken.

Other Changes:

* [#13637](https://dev.ckeditor.com/ticket/13637): Several icons were refactored.
* Updated [Bender.js](https://github.com/benderjs/benderjs) to 0.3.0 and introduced the ability to run tests via HTTPs ([#13265](https://dev.ckeditor.com/ticket/13265)).

## CKEditor 4.5.2

Fixed Issues:

* [#13609](http://dev.ckeditor.com/ticket/13609): [Edge] Fixed: The browser crashes when switching to the source mode. Thanks to [Andrew Williams and Mark Smeed](http://webxsolution.com/)!
* [PR#201](https://github.com/ckeditor/ckeditor-dev/pull/201): Fixed: Buttons in the toolbar configurator cause form submission. Thanks to [colemanw](https://github.com/colemanw)!
* [#13422](http://dev.ckeditor.com/ticket/13422): Fixed: A monospaced font should be used in the `<textarea>` element storing editor configuration in the toolbar configurator.
* [#13494](http://dev.ckeditor.com/ticket/13494): Fixed: Error thrown in the toolbar configurator if plugin requirements are not met.
* [#13409](http://dev.ckeditor.com/ticket/13409): Fixed: List elements incorrectly merged when pressing *Backspace* or *Delete*.
* [#13434](http://dev.ckeditor.com/ticket/13434): Fixed: Dialog state indicator broken in Right–To–Left environments.
* [#13460](http://dev.ckeditor.com/ticket/13460): [IE8] Fixed: Copying inline widgets is broken when [Advanced Content Filter](http://docs.ckeditor.com/#!/guide/dev_acf) is disabled.
* [#13495](http://dev.ckeditor.com/ticket/13495): [Firefox, IE] Fixed: Text is not word-wrapped in the Paste dialog window.
* [#13528](http://dev.ckeditor.com/ticket/13528): [Firefox@Windows] Fixed: Content copied from Microsoft Word and other external applications is pasted as a plain text. Removed the `CKEDITOR.plugins.clipboard.isHtmlInExternalDataTransfer` property as the check must be dynamic.
* [#13583](http://dev.ckeditor.com/ticket/13583): Fixed: [`DataTransfer.getData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.clipboard.dataTransfer-method-getData) should work consistently in all browsers and should not strip valuable content. Fixed pasting tables from Microsoft Excel on Chrome.
* [#13468](http://dev.ckeditor.com/ticket/13468): [IE] Fixed: Binding drag&drop `dataTransfer` does not work if `text` data was set in the meantime.
* [#13451](http://dev.ckeditor.com/ticket/13451): [IE8-9] Fixed: One drag&drop operation may affect following ones.
* [#13184](http://dev.ckeditor.com/ticket/13184): Fixed: Web page reloaded after a drop on editor UI.
* [#13129](http://dev.ckeditor.com/ticket/13129) Fixed: Block widget blurred after a drop followed by an undo.
* [#13397](http://dev.ckeditor.com/ticket/13397): Fixed: Drag&drop of a widget inside its nested widget crashes the editor.
* [#13385](http://dev.ckeditor.com/ticket/13385): Fixed: [`editor.getSnapshot()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getSnapshot) may return a non-string value.
* [#13419](http://dev.ckeditor.com/ticket/13419): Fixed: The [Auto Link](http://ckeditor.com/addon/autolink) plugin does not encode double quotes in URLs.
* [#13420](http://dev.ckeditor.com/ticket/13420): Fixed: The [Auto Embed](http://ckeditor.com/addon/autoembed) plugin ignores encoded characters in URL parameters.
* [#13410](http://dev.ckeditor.com/ticket/13410): Fixed: Error thrown in the [Auto Embed](http://ckeditor.com/addon/autoembed) plugin when undoing right after pasting a link.
* [#13566](http://dev.ckeditor.com/ticket/13566): Fixed: Suppressed notifications in the [Media Embed Base](http://ckeditor.com/addon/embedbase) plugin.
* [#11616](http://dev.ckeditor.com/ticket/11616): [Chrome] Fixed: Resizing the editor while it is not displayed breaks the editable. Fixes also [#9160](http://dev.ckeditor.com/ticket/9160) and [#9715](http://dev.ckeditor.com/ticket/9715).
* [#11376](http://dev.ckeditor.com/ticket/11376): [IE11] Fixed: Loss of text when pasting bulleted lists from Microsoft Word.
* [#13143](http://dev.ckeditor.com/ticket/13143): [Edge] Fixed: Focus lost when opening the panel.
* [#13387](http://dev.ckeditor.com/ticket/13387): [Edge] Fixed: "Permission denied" error thrown when loading the editor with developer tools open.
* [#13574](http://dev.ckeditor.com/ticket/13574): [Edge] Fixed: "Permission denied" error thrown when opening editor dialog windows.
* [#13441](http://dev.ckeditor.com/ticket/13441): [Edge] Fixed: The [Clipboard](http://ckeditor.com/addon/clipboard) plugin breaks the state of [Undo](http://ckeditor.com/addon/undo) commands after a paste.
* [#13554](http://dev.ckeditor.com/ticket/13554): [Edge] Fixed: Paste dialog's iframe does not receive focus on show.
* [#13440](http://dev.ckeditor.com/ticket/13440): [Edge] Fixed: Unable to paste a widget.

Other Changes:

* [#13421](http://dev.ckeditor.com/ticket/13421): UX improvements to notifications in the [Auto Embed](http://ckeditor.com/addon/autoembed) plugin.

## CKEditor 4.5.1

Fixed Issues:

* [#13486](http://dev.ckeditor.com/ticket/13486): Fixed: The [Upload Image](http://ckeditor.com/addon/uploadimage) plugin should log an error, not throw an error when upload URL is not set.

## CKEditor 4.5

New Features:

* [#13304](http://dev.ckeditor.com/ticket/13304): Added support for passing DOM elements to [`config.sharedSpaces`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-sharedSpaces). Thanks to [Undergrounder](https://github.com/Undergrounder)!
* [#13215](http://dev.ckeditor.com/ticket/13215): Added ability to cancel fetching a resource by the Embed plugins.
* [#13213](http://dev.ckeditor.com/ticket/13213): Added the [`dialog#setState()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dialog-method-setState) method and used it in the [Embed](http://ckeditor.com/addon/embed) dialog to indicate that a resource is being loaded.
* [#13337](http://dev.ckeditor.com/ticket/13337): Added the [`repository.onWidget()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository-method-onWidget) method &mdash; a convenient way to listen to [widget](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget) events through the [repository](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository).
* [#13214](http://dev.ckeditor.com/ticket/13214): Added support for pasting links that convert into embeddable resources on the fly.

Fixed Issues:

* [#13334](http://dev.ckeditor.com/ticket/13334): Fixed: Error after nesting widgets and playing with undo/redo.
* [#13118](http://dev.ckeditor.com/ticket/13118): Fixed: The [`editor.getSelectedHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getSelectedHtml) method throws an error when called in the source mode.
* [#13158](http://dev.ckeditor.com/ticket/13158): Fixed: Error after canceling a dialog when creating a widget.
* [#13197](http://dev.ckeditor.com/ticket/13197): Fixed: Linked inline [Enhanced Image](http://ckeditor.com/addon/image2) alignment class is not transferred to the widget wrapper.
* [#13199](http://dev.ckeditor.com/ticket/13199): Fixed: [Semantic Embed](http://ckeditor.com/addon/embedsemantic) does not support widget classes.
* [#13003](http://dev.ckeditor.com/ticket/13003): Fixed: Anchors are uploaded when moving them by drag and drop.
* [#13032](http://dev.ckeditor.com/ticket/13032): Fixed: When upload is done, notification update should be marked as important.
* [#13300](http://dev.ckeditor.com/ticket/13300): Fixed: The `internalCommit` argument in the [Image](http://ckeditor.com/addon/image) dialog seems to be never used.
* [#13036](http://dev.ckeditor.com/ticket/13036): Fixed: Notifications are moved 10px to the right.
* [#13280](http://dev.ckeditor.com/ticket/13280): [IE8] Fixed: Undo after inline widget drag&drop throws an error.
* [#13186](http://dev.ckeditor.com/ticket/13186): Fixed: Content dropped into a nested editable is not filtered by [Advanced Content Filter](http://docs.ckeditor.com/#!/guide/dev_acf).
* [#13140](http://dev.ckeditor.com/ticket/13140): Fixed: Error thrown when dropping a block widget right after itself.
* [#13176](http://dev.ckeditor.com/ticket/13176): [IE8] Fixed: Errors on drag&drop of embed widgets.
* [#13015](http://dev.ckeditor.com/ticket/13015): Fixed: Dropping an image file on [Enhanced Image](http://ckeditor.com/addon/image2) causes a page reload.
* [#13080](http://dev.ckeditor.com/ticket/13080): Fixed: Ugly notification shown when the response contains HTML content.
* [#13011](http://dev.ckeditor.com/ticket/13011): [IE8] Fixed: Anchors are duplicated on drag&drop in specific locations.
* [#13105](http://dev.ckeditor.com/ticket/13105): Fixed: Various issues related to [`CKEDITOR.tools.htmlEncode()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-htmlEncode) and [`CKEDITOR.tools.htmlDecode()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-htmlDecode) methods.
* [#11976](http://dev.ckeditor.com/ticket/11976): [Chrome] Fixed: Copy&paste and drag&drop lists from Microsoft Word.
* [#13128](http://dev.ckeditor.com/ticket/13128): Fixed: Various issues with cloning element IDs:
  * Fixed the default behavior of [`range.cloneContents()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-cloneContents) and [`range.extractContents()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-extractContents) methods which now clone IDs similarly to their native counterparts.
  * Added `cloneId` arguments to the above methods, [`range.splitBlock()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-splitBlock) and [`element.breakParent()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-breakParent). Mind the default values and special behavior in the `extractContents()` method!
  * Fixed issues where IDs were lost on copy&paste and drag&drop.
* Toolbar configurators:
  * [#13185](http://dev.ckeditor.com/ticket/13185): Fixed: Wrong position of the suggestion box if there is not enough space below the caret.
  * [#13138](http://dev.ckeditor.com/ticket/13138): Fixed: The "Toggle empty elements" button label is unclear.
  * [#13136](http://dev.ckeditor.com/ticket/13136): Fixed: Autocompleter is far too intrusive.
  * [#13133](http://dev.ckeditor.com/ticket/13133): Fixed: Tab leaves the editor.
  * [#13173](http://dev.ckeditor.com/ticket/13173): Fixed: [`config.removeButtons`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-removeButtons) is ignored by the advanced toolbar configurator.

Other Changes:

* [#13119](http://dev.ckeditor.com/ticket/13119): Improved compatibility of editor skins ([Moono](http://ckeditor.com/addon/moono) and [Kama](http://ckeditor.com/addon/kama)) with external web page style sheets.
* Toolbar configurators:
  * [#13147](http://dev.ckeditor.com/ticket/13147): Added buttons to the sticky toolbar.
  * [#13207](http://dev.ckeditor.com/ticket/13207): Used modal window to display toolbar configurator help.
* [#13316](http://dev.ckeditor.com/ticket/13316): Made [`CKEDITOR.env.isCompatible`](http://docs.ckeditor.com/#!/api/CKEDITOR.env-property-isCompatible) a blacklist rather than a whitelist. More about the change in the [Browser Compatibility](http://docs.ckeditor.com/#!/guide/dev_browsers) guide.
* [#13398](http://dev.ckeditor.com/ticket/13398): Renamed `CKEDITOR.fileTools.UploadsRepository` to [`CKEDITOR.fileTools.UploadRepository`](http://docs.ckeditor.com/#!/api/CKEDITOR.fileTools.uploadRepository) and changed all related properties.
* [#13279](http://dev.ckeditor.com/ticket/13279): Reviewed CSS vendor prefixes.
* [#13454](http://dev.ckeditor.com/ticket/13454): Removed unused `lang.image.alertUrl` token from the [Image](http://ckeditor.com/addon/image) plugin.

## CKEditor 4.5 Beta

New Features:

* Clipboard (copy&paste, drag&drop) and file uploading features and improvements ([#11437](http://dev.ckeditor.com/ticket/11437)).

  * Major features:
    * Support for dropping and pasting files into the editor was introduced. Through a set of new facades for native APIs it is now possible to easily intercept and process inserted files.
    * [File upload tools](http://docs.ckeditor.com/#!/api/CKEDITOR.fileTools) were introduced in order to simplify controlling the loading, uploading and handling server response, properly handle [new upload configuration](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-uploadUrl) options, etc.
    * [Upload Image](http://ckeditor.com/addon/uploadimage) widget was introduced to upload dropped images. A base class for the [upload widget](http://docs.ckeditor.com/#!/api/CKEDITOR.fileTools.uploadWidgetDefinition) was exposed, too, to make it simple to create new types of upload widgets which can handle any type of dropped file, show the upload progress and update the content when the process is done. It also handles editing and undo/redo operations when a file is being uploaded and integrates with the [notification aggregator](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.notificationAggregator) to show progress and success or error.
    * All drag and drop operations were integrated with the editor. All dropped content is passed through the [`editor#paste`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-paste) event and a set of new editor events was introduced &mdash; [`dragstart`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-dragstart), [`drop`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-drop), [`dragend`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-dragend).
    * The [Data Transfer](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.clipboard.dataTransfer) facade was introduced to unify access to data in various types and files. [Data Transfer](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.clipboard.dataTransfer) is now always available in the [`editor#paste`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-paste) event.
    * Switched from the pastebin to using the native clipboard access whenever possible. This solved many issues related to pastebin such as unnecessary scrolling or data loss. Additionally, on copy and cut from the editor the clipboard data is set. Therefore, on paste the editor has access to clean data, undisturbed by the browsers.
    * Drag and drop of inline and block widgets was integrated with the standard clipboard APIs. By listening to drag events you will thus be notified about widgets, too. This opens a possibility to filter pasted and dropped widgets.
    * The [`editor#paste`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-paste) event can have the `range` parameter so it is possible to change the paste position in the listener or paste in the not selectable position. Also the [`editor.insertHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-insertHtml) method now accepts `range` as an additional parameter.
    * [#11621](http://dev.ckeditor.com/ticket/11621): A configurable [paste filter](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-pasteFilter) was introduced. The filter is by default turned to `'semantic-content'` on Webkit and Blink for all pasted content coming from external sources because of the low quality of HTML that these engines put into the clipboard. Internal and cross-editor paste is safe due to the change explained in the previous point.

  * Other changes and related fixes:
    * [#12095](http://dev.ckeditor.com/ticket/12095): On drag and copy of widgets [the same method](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getSelectedHtml) is used to get selected HTML as in the normal case. Thanks to that styles applied to inline widgets are not lost.
    * [#11219](http://dev.ckeditor.com/ticket/11219): Fixed: Dragging a [captioned image](http://ckeditor.com/addon/image2) does not fire the [`editor#paste`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-paste) event.
    * [#9554](http://dev.ckeditor.com/ticket/9554): [Webkit Mac] Fixed: Editor scrolls on paste.
    * [#9898](http://dev.ckeditor.com/ticket/9898): [Webkit&Divarea] Fixed: Pasting causes undesirable scrolling.
    * [#11993](http://dev.ckeditor.com/ticket/11993): [Chrome] Fixed: Pasting content scrolls the document.
    * [#12613](http://dev.ckeditor.com/ticket/12613): Show the user that they can not drop on editor UI (toolbar, bottom bar).
    * [#12851](http://dev.ckeditor.com/ticket/12851): [Blink/Webkit] Fixed: Formatting disappears when pasting content into cells.
    * [#12914](http://dev.ckeditor.com/ticket/12914): Fixed: Copy/Paste of table broken in `div`-based editor.

  * Browser support.<br>Browser support for related features varies significantly (see http://caniuse.com/clipboard).
    * File APIs needed to operate and file upload is not supported in Internet Explorer 9 and below.
    * Only Chrome and Safari on Mac OS support setting custom data items in the clipboard, so currently it is possible to recognize the origin of the copied content in these browsers only. All drag and drop operations can be identified thanks to the new Data Transfer facade.
    * No Internet Explorer browser supports the standard clipboard API which results in small glitches like where only plain text can be dropped from outside the editor. Thanks to the new Data Transfer facade, internal and cross-editor drag and drop supports the full range of data.
    * Direct access to clipboard could only be implemented in Chrome, Safari on Mac OS, Opera and Firefox. In other browsers the pastebin must still be used.

* [#12875](http://dev.ckeditor.com/ticket/12875): Samples and toolbar configuration tools.
  * The old set of samples shipped with every CKEditor package was replaced with a shiny new single-page sample. This change concluded a long term plan which started from introducing the [CKEditor SDK](http://sdk.ckeditor.com/) and [CKEditor Functionality Overview](http://docs.ckeditor.com/#!/guide/dev_features) section in the documentation which essentially redefined the old samples.
  * Toolbar configurators with live previews were introduced. They will be shipped with every CKEditor package and are meant to help in configuring toolbar layouts.

* [#10925](http://dev.ckeditor.com/ticket/10925): The [Media Embed](http://ckeditor.com/addon/embed) and [Semantic Media Embed](http://ckeditor.com/addon/embedsemantic) plugins were introduced. Read more about the new features in the [Embedding Content](http://docs.ckeditor.com/#!/guide/dev_media_embed) article.
* [#10931](http://dev.ckeditor.com/ticket/10931): Added support for nesting widgets. It is now possible to insert one widget into another widget's nested editable. Note that unless nested editable's [allowed content](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.nestedEditable.definition-property-allowedContent) is defined precisely, starting from CKEditor 4.5 some widget buttons may become enabled. This feature is not supported in IE8. Included issues:
  * [#12018](http://dev.ckeditor.com/ticket/12018): Fixed and reviewed: Nested widgets garbage collection.
  * [#12024](http://dev.ckeditor.com/ticket/12024): [Firefox] Fixed: Outline is extended to the left by unpositioned drag handlers.
  * [#12006](http://dev.ckeditor.com/ticket/12006): Fixed: Drag and drop of nested block widgets.
  * [#12008](http://dev.ckeditor.com/ticket/12008): Fixed various cases of inserting a single non-editable element using the [`editor.insertHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-insertHtml) method. Fixes pasting a widget with a nested editable inside another widget's nested editable.

* Notification system:
  * [#11580](http://dev.ckeditor.com/ticket/11580): Introduced the [notification system](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.notification).
  * [#12810](http://dev.ckeditor.com/ticket/12810): Introduced a [notification aggregator](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.notificationAggregator) for the [notification system](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.notification) which simplifies displaying progress of many concurrent tasks.
* [#11636](http://dev.ckeditor.com/ticket/11636): Introduced new, UX-focused, methods for getting selected HTML and deleting it &mdash; [`editor.getSelectedHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getSelectedHtml) and [`editor.deleteSelectedHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getSelectedHtml).
* [#12416](http://dev.ckeditor.com/ticket/12416): Added the [`widget.definition.upcastPriority`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.definition-property-upcastPriority) property which gives more control over widget upcasting order to the widget author.
* [#12036](http://dev.ckeditor.com/ticket/12036): Initialize the editor in [read-only](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-readOnly) mode when the `<textarea>` element has a `readonly` attribute.
* [#11905](http://dev.ckeditor.com/ticket/11905): The [`resize` event](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-resize) passes the current dimensions in its data.
* [#12126](http://dev.ckeditor.com/ticket/12126): Introduced [`config.image_prefillDimensions`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-image_prefillDimensions) and [`config.image2_prefillDimensions`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-image2_prefillDimensions) to make pre-filling `width` and `height` configurable for the [Enhanced Image](http://ckeditor.com/addon/image2).
* [#12746](http://dev.ckeditor.com/ticket/12746): Added a new configuration option to hide the [Enhanced Image](http://ckeditor.com/addon/image2) resizer.
* [#12150](http://dev.ckeditor.com/ticket/12150): Exposed the [`getNestedEditable()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-static-method-getNestedEditable) and `is*` [widget helper](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget) functions (see the static methods).
* [#12448](http://dev.ckeditor.com/ticket/12448): Introduced the [`editable.insertHtmlIntoRange`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-method-insertHtmlIntoRange) method.
* [#12143](http://dev.ckeditor.com/ticket/12143): Added the [`config.floatSpacePreferRight`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-floatSpacePreferRight) configuration option that switches the alignment of the floating toolbar. Thanks to [InvisibleBacon](http://github.com/InvisibleBacon)!
* [#10986](http://dev.ckeditor.com/ticket/10986): Added support for changing dialog input and textarea text directions by using the *Shift+Alt+Home/End* keystrokes. The direction is stored in the value of the input by prepending the [`\u202A`](http://unicode.org/cldr/utility/character.jsp?a=202A) or [`\u202B`](http://unicode.org/cldr/utility/character.jsp?a=202B) marker to it. Read more in the [documentation](http://docs.ckeditor.com/#!/api/CKEDITOR.dialog.definition.textInput-property-bidi). Thanks to [edithkk](https://github.com/edithkk)!
* [#12770](http://dev.ckeditor.com/ticket/12770): Added support for passing [widget](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget)'s startup data as a widget command's argument. Thanks to [Rebrov Boris](https://github.com/zipp3r) and [Tieme van Veen](https://github.com/tiemevanveen)!
* [#11583](http://dev.ckeditor.com/ticket/11583): Added support for the HTML5 `required` attribute in various form elements. Thanks to [Steven Busse](https://github.com/sbusse)!

Changes:

* [#12858](http://dev.ckeditor.com/ticket/12858): Basic [Spartan](http://blogs.windows.com/bloggingwindows/2015/03/30/introducing-project-spartan-the-new-browser-built-for-windows-10/) browser compatibility. Full compatibility will be introduced later, because at the moment Spartan is still too unstable to be used for tests and we see many changes from version to version.
* [#12948](http://dev.ckeditor.com/ticket/12948): The [`config.mathJaxLibrary`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-mathJaxLib) option does not default to the MathJax CDN any more. It needs to be configured to enable the [Mathematical Formulas](http://ckeditor.com/addon/mathjax) plugin now.
* [#13069](http://dev.ckeditor.com/ticket/13069): Fixed inconsistencies between [`editable.insertHtml()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-method-insertElement) and [`editable.insertElement()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-method-insertElement) when the `range` parameter is used. Now, the `editor.insertElement()` method works on a higher level, which means that it saves undo snapshots and sets the selection after insertion. Use the [`editable.insertElementIntoRange()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-method-insertElementIntoRange) method directly for the pre 4.5 behavior of `editable.insertElement()`.
* [#12870](http://dev.ckeditor.com/ticket/12870): Use [`editor.showNotification()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-showNotification) instead of `alert()` directly whenever possible. When the [Notification plugin](http://ckeditor.com/addon/notification) is loaded, the notification system is used automatically. Otherwise, the native `alert()` is displayed.
* [#8024](http://dev.ckeditor.com/ticket/8024): Swapped behavior of the Split Cell Vertically and Horizontally features of the [Table Tools](http://ckeditor.com/addon/tabletools) plugin to be more intuitive. Thanks to [kevinisagit](https://github.com/kevinisagit)!
* [#10903](http://dev.ckeditor.com/ticket/10903): Performance improvements for the [`dom.element.addClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-addClass), [`dom.element.removeClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-removeClass) and [`dom.element.hasClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-hasClass) methods. Note: The previous implementation allowed passing multiple classes to `addClass()` although it was only a side effect of that implementation. The new implementation does not allow this.
* [#11856](http://dev.ckeditor.com/ticket/11856): The jQuery adapter throws a meaningful error if CKEditor or jQuery are not loaded.

Fixed issues:

* [#11586](http://dev.ckeditor.com/ticket/11586): Fixed: [`range.cloneContents()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-cloneContents) should not change the DOM in order not to affect selection.
* [#12148](http://dev.ckeditor.com/ticket/12148): Fixed: [`dom.element.getChild()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-getChild) should not modify a passed array.
* [#12503](http://dev.ckeditor.com/ticket/12503): [Blink/Webkit] Fixed: Incorrect result of Select All and *Backspace* or *Delete*.
* [#13001](http://dev.ckeditor.com/ticket/13001): [Firefox] Fixed: The `<br />` filler is placed in the wrong position by the [`range.fixBlock()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-fixBlock) method due to quirky Firefox behavior.
* [#13101](http://dev.ckeditor.com/ticket/13101): [IE8] Fixed: Colons are prepended to HTML5 element names when cloning them.

## CKEditor 4.4.8

**Security Updates:**

* Fixed XSS vulnerability in the HTML parser reported by [Dheeraj Joshi](https://twitter.com/dheerajhere) and [Prem Kumar](https://twitter.com/iAmPr3m).

	Issue summary: It was possible to execute XSS inside CKEditor after persuading the victim to: (i) switch CKEditor to source mode, then (ii) paste a specially crafted HTML code, prepared by the attacker, into the opened CKEditor source area, and (iii) switch back to WYSIWYG mode.

**An upgrade is highly recommended!**

Fixed Issues:

* [#12899](http://dev.ckeditor.com/ticket/12899): Fixed: Corrected wrong tag ending for horizontal box definition in the [Dialog User Interface](http://ckeditor.com/addon/dialogui) plugin. Thanks to [mizafish](https://github.com/mizafish)!
* [#13254](http://dev.ckeditor.com/ticket/13254): Fixed: Cannot outdent block after indent when using the [Div Editing Area](http://ckeditor.com/addon/divarea) plugin. Thanks to [Jonathan Cottrill](https://github.com/jcttrll)!
* [#13268](http://dev.ckeditor.com/ticket/13268): Fixed: Documentation for [`CKEDITOR.dom.text`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.text) is incorrect. Thanks to [Ben Kiefer](https://github.com/benkiefer)!
* [#12739](http://dev.ckeditor.com/ticket/12739): Fixed: Link loses inline styles when edited without the [Advanced Tab for Dialogs](http://ckeditor.com/addon/dialogadvtab) plugin. Thanks to [Віталій Крутько](https://github.com/asmforce)!
* [#13292](http://dev.ckeditor.com/ticket/13292): Fixed: Protection pattern does not work in attribute in self-closing elements with no space before `/>`. Thanks to [Віталій Крутько](https://github.com/asmforce)!
* [PR#192](https://github.com/ckeditor/ckeditor-dev/pull/192): Fixed: Variable name typo in the [Dialog User Interface](http://ckeditor.com/addon/dialogui) plugin which caused [`CKEDITOR.ui.dialog.radio`](http://docs.ckeditor.com/#!/api/CKEDITOR.ui.dialog.radio) validation to not work. Thanks to [Florian Ludwig](https://github.com/FlorianLudwig)!
* [#13232](http://dev.ckeditor.com/ticket/13232): [Safari] Fixed: The [`element.appendText()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-appendText) method does not work properly for empty elements.
* [#13233](http://dev.ckeditor.com/ticket/13233): Fixed: [HTMLDataProcessor](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlDataProcessor) can process `foo:href` attributes.
* [#12796](http://dev.ckeditor.com/ticket/12796): Fixed: The [Indent List](http://ckeditor.com/addon/indentlist) plugin unwraps parent `<li>` elements. Thanks to [Andrew Stucki](https://github.com/andrewstucki)!
* [#12885](http://dev.ckeditor.com/ticket/12885): Added missing [`editor.getData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getData) parameter documentation.
* [#11982](http://dev.ckeditor.com/ticket/11982): Fixed: Bullet added in a wrong position after the *Enter* key is pressed in a nested list.
* [#13027](http://dev.ckeditor.com/ticket/13027): Fixed: Keyboard navigation in dialog windows with multiple tabs not following IBM CI 162 instructions or [ARIA Authoring Practices](http://www.w3.org/TR/2013/WD-wai-aria-practices-20130307/#tabpanel).
* [#12256](http://dev.ckeditor.com/ticket/12256): Fixed: Basic styles classes are lost when pasting from Microsoft Word if [basic styles](http://ckeditor.com/addon/basicstyles) were configured to use classes.
* [#12729](http://dev.ckeditor.com/ticket/12729): Fixed: Incorrect structure created when merging a block into a list item on *Backspace* and *Delete*.
* [#13031](http://dev.ckeditor.com/ticket/13031): [Firefox] Fixed: No more line breaks in source view since Firefox 36.
* [#13131](http://dev.ckeditor.com/ticket/13131): Fixed: The [Code Snippet](http://ckeditor.com/addon/codesnippet) plugin cannot be used without the [IFrame Editing Area](http://ckeditor.com/addon/wysiwygarea) plugin.
* [#9086](http://dev.ckeditor.com/ticket/9086): Fixed: Invalid ARIA property used on paste area `<iframe>`.
* [#13164](http://dev.ckeditor.com/ticket/13164): Fixed: Error when inserting a hidden field.
* [#13155](http://dev.ckeditor.com/ticket/13155): Fixed: Incorrect [Line Utilities](http://ckeditor.com/addon/lineutils) positioning when `<body>` has a margin.
* [#13351](http://dev.ckeditor.com/ticket/13351): Fixed: Link lost when editing a linked image with the Link tab disabled. This also fixed a bug when inserting an image into a fully selected link would throw an error ([#12847](https://dev.ckeditor.com/ticket/12847)).
* [#13344](http://dev.ckeditor.com/ticket/13344): [WebKit/Blink] Fixed: It is possible to remove or change editor content in [read-only mode](http://docs.ckeditor.com/#!/guide/dev_readonly).

Other Changes:

* [#12844](http://dev.ckeditor.com/ticket/12844) and [#13103](http://dev.ckeditor.com/ticket/13103): Upgraded the [testing environment](http://docs.ckeditor.com/#!/guide/dev_tests) to [Bender.js](https://github.com/benderjs/benderjs) `0.2.3`.
* [#12930](http://dev.ckeditor.com/ticket/12930): Because of licensing issues, `truncated-mathjax/` is now removed from the `tests/` directory. Now `bender.config.mathJaxLibPath` must be configured manually in order to run [Mathematical Formulas](http://ckeditor.com/addon/mathjax) plugin tests.
* [#13266](http://dev.ckeditor.com/ticket/13266): Added more shades of gray in the [Color Dialog](http://ckeditor.com/addon/colordialog) window. Thanks to [mizafish](https://github.com/mizafish)!


## CKEditor 4.4.7

Fixed Issues:

* [#12825](http://dev.ckeditor.com/ticket/12825): Fixed: Preventing the [Table Resize](http://ckeditor.com/addon/tableresize) plugin from operating on elements outside the editor. Thanks to [Paul Martin](https://github.com/Paul-Martin)!
* [#12157](http://dev.ckeditor.com/ticket/12157): Fixed: Lost text formatting on pressing *Tab* when the [`config.tabSpaces`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-tabSpaces) configuration option value was greater than zero.
* [#12777](http://dev.ckeditor.com/ticket/12777): Fixed: The `table-layout` CSS property should be reset by skins. Thanks to [vita10gy](https://github.com/vita10gy)!
* [#12812](http://dev.ckeditor.com/ticket/12812): Fixed: An uncaught security exception is thrown when [Line Utilities](http://ckeditor.com/addon/lineutils) are used in an inline editor loaded in a cross-domain `iframe`. Thanks to [Vitaliy Zurian](https://github.com/thecatontheflat)!
* [#12735](http://dev.ckeditor.com/ticket/12735): Fixed: [`config.fillEmptyBlocks`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-fillEmptyBlocks) should only apply when outputting data.
* [#10032](http://dev.ckeditor.com/ticket/10032): Fixed: [Paste from Word](http://ckeditor.com/addon/pastefromword) filter is executed for every paste after using the button.
* [#12597](http://dev.ckeditor.com/ticket/12597): [Blink/WebKit] Fixed: Multi-byte Japanese characters entry not working properly after *Shift+Enter*.
* [#12387](http://dev.ckeditor.com/ticket/12387): Fixed: An error is thrown if a skin does not have the [`chameleon`](http://docs.ckeditor.com/#!/api/CKEDITOR.skin-method-chameleon) property defined and [`config.uiColor`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-uiColor) is defined.
* [#12747](http://dev.ckeditor.com/ticket/12747): [IE8-10] Fixed: Opening a drop-down for a specific selection when the editor is maximized results in incorrect drop-down panel position.
* [#12850](http://dev.ckeditor.com/ticket/12850): [IEQM] Fixed: An error is thrown after focusing the editor.

## CKEditor 4.4.6

**Security Updates:**

* Fixed XSS vulnerability in the HTML parser reported by [Maco Cortes](https://www.facebook.com/Maaacoooo).

	Issue summary: It was possible to execute XSS inside CKEditor after persuading the victim to: (i) switch CKEditor to source mode, then (ii) paste a specially crafted HTML code, prepared by the attacker, into the opened CKEditor source area, and (iii) switch back to WYSIWYG mode.

**An upgrade is highly recommended!**

New Features:

* [#12501](http://dev.ckeditor.com/ticket/12501): Allowed dashes in element names in the [string format of allowed content rules](http://docs.ckeditor.com/#!/guide/dev_allowed_content_rules-section-string-format).
* [#12550](http://dev.ckeditor.com/ticket/12550): Added the `<main>` element to the [`CKEDITOR.dtd`](http://docs.ckeditor.com/#!/api/CKEDITOR.dtd).

Fixed Issues:

* [#12506](http://dev.ckeditor.com/ticket/12506): [Safari] Fixed: Cannot paste into inline editor if the page has `user-select: none` style. Thanks to [shaohua](https://github.com/shaohua)!
* [#12683](http://dev.ckeditor.com/ticket/12683): Fixed: [Filter](http://docs.ckeditor.com/#!/guide/dev_acf) fails to remove custom tags. Thanks to [timselier](https://github.com/timselier)!
* [#12489](http://dev.ckeditor.com/ticket/12489) and [#12491](http://dev.ckeditor.com/ticket/12491): Fixed: Various issues related to restoring the selection after performing operations on filler character. See the [fixed cases](http://dev.ckeditor.com/ticket/12491#comment:4).
* [#12621](http://dev.ckeditor.com/ticket/12621): Fixed: Cannot remove inline styles (bold, italic, etc.) in empty lines.
* [#12630](http://dev.ckeditor.com/ticket/12630): [Chrome] Fixed: Selection is placed outside the paragraph when the [New Page](http://ckeditor.com/addon/newpage) button is clicked. This patch significantly simplified the way how the initial selection (a selection after the content of the editable is overwritten) is being fixed. That might have fixed many related scenarios in all browsers.
* [#11647](http://dev.ckeditor.com/ticket/11647): Fixed: The [`editor.blur`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-blur) event is not fired on first blur after initializing the inline editor on an already focused element.
* [#12601](http://dev.ckeditor.com/ticket/12601): Fixed: [Strikethrough](http://ckeditor.com/addon/basicstyles) button tooltip spelling.
* [#12546](http://dev.ckeditor.com/ticket/12546): Fixed: The Preview tab in the [Document Properties](http://ckeditor.com/addon/docprops) dialog window is always disabled.
* [#12300](http://dev.ckeditor.com/ticket/12300): Fixed: The [`editor.change`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-change) event fired on first navigation key press after typing.
* [#12141](http://dev.ckeditor.com/ticket/12141): Fixed: List items are lost when indenting a list item with content wrapped with a block element.
* [#12515](http://dev.ckeditor.com/ticket/12515): Fixed: Cursor is in the wrong position when undoing after adding an image and typing some text.
* [#12484](http://dev.ckeditor.com/ticket/12484): [Blink/WebKit] Fixed: DOM is changed outside the editor area in a certain case.
* [#12688](http://dev.ckeditor.com/ticket/12688): Improved the tests of the [styles system](http://docs.ckeditor.com/#!/api/CKEDITOR.style) and fixed two minor issues.
* [#12403](http://dev.ckeditor.com/ticket/12403): Fixed: Changing the [font](http://ckeditor.com/addon/font) style should not lead to nesting it in the previous style element.
* [#12609](http://dev.ckeditor.com/ticket/12609): Fixed: Incorrect `config.magicline_putEverywhere` name used for a [Magic Line](http://ckeditor.com/addon/magicline) all-encompassing [`config.magicline_everywhere`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-magicline_everywhere) configuration option.


## CKEditor 4.4.5

New Features:

* [#12279](http://dev.ckeditor.com/ticket/12279): Added a possibility to pass a custom evaluator to [`node.getAscendant()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.node-method-getAscendant).

Fixed Issues:

* [#12423](http://dev.ckeditor.com/ticket/12423): [Safari7.1+] Fixed: *Enter* key moved cursor to a strange position.
* [#12381](http://dev.ckeditor.com/ticket/12381): [iOS] Fixed: Selection issue. Thanks to [Remiremi](https://github.com/Remiremi)!
* [#10804](http://dev.ckeditor.com/ticket/10804): Fixed: `CKEDITOR_GETURL` is not used with some plugins where it should be used. Thanks to [Thomas Andraschko](https://github.com/tandraschko)!
* [#9137](http://dev.ckeditor.com/ticket/9137): Fixed: The `<base>` tag is not created when `<head>` has an attribute. Thanks to [naoki.fujikawa](https://github.com/naoki-fujikawa)!
* [#12377](http://dev.ckeditor.com/ticket/12377): Fixed: Errors thrown in the [Image](http://ckeditor.com/addon/image) plugin when removing preview from the dialog window definition. Thanks to [Axinet](https://github.com/Axinet)!
* [#12162](http://dev.ckeditor.com/ticket/12162): Fixed: Auto paragraphing and *Enter* key in nested editables.
* [#12315](http://dev.ckeditor.com/ticket/12315): Fixed: Marked [`config.autoParagraph`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-autoParagraph) as deprecated.
* [#12113](http://dev.ckeditor.com/ticket/12113): Fixed: A [code snippet](http://ckeditor.com/addon/codesnippet) should be presented in the [elements path](http://ckeditor.com/addon/elementspath) as "code snippet" (translatable).
* [#12311](http://dev.ckeditor.com/ticket/12311): Fixed: [Remove Format](http://ckeditor.com/addon/removeformat) should also remove `<cite>` elements.
* [#12261](http://dev.ckeditor.com/ticket/12261): Fixed: Filter has to be destroyed and removed from [`CKEDITOR.filter.instances`](http://docs.ckeditor.com/#!/api/CKEDITOR.filter-static-property-instances) on editor destroy.
* [#12398](http://dev.ckeditor.com/ticket/12398): Fixed: [Maximize](http://ckeditor.com/addon/maximize) does not work on an instance without a [title](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-title).
* [#12097](http://dev.ckeditor.com/ticket/12097): Fixed: JAWS not reading the number of options correctly in the [Text Color and Background Color](http://ckeditor.com/addon/colorbutton) button menu.
* [#12411](http://dev.ckeditor.com/ticket/12411): Fixed: [Page Break](http://ckeditor.com/addon/pagebreak) used directly in the editable breaks the editor.
* [#12354](http://dev.ckeditor.com/ticket/12354): Fixed: Various issues in undo manager when holding keys.
* [#12324](http://dev.ckeditor.com/ticket/12324): [IE8] Fixed: Undo steps are not recorded when changing the caret position by clicking below the body.
* [#12332](http://dev.ckeditor.com/ticket/12332): Fixed: Lowered DOM events listeners' priorities in undo manager in order to avoid ambiguity.
* [#12402](http://dev.ckeditor.com/ticket/12402): [Blink] Fixed: Workaround for Blink bug with `document.title` which breaks updating title in the full HTML mode.
* [#12338](http://dev.ckeditor.com/ticket/12338): Fixed: The CKEditor package contains unoptimized images.


## CKEditor 4.4.4

Fixed Issues:

* [#12268](http://dev.ckeditor.com/ticket/12268): Cleanup of [UI Color](http://ckeditor.com/addon/uicolor) YUI styles. Thanks to [CasherWest](https://github.com/CasherWest)!
* [#12263](http://dev.ckeditor.com/ticket/12263): Fixed: [Paste from Word](http://ckeditor.com/addon/pastefromword) filter does not properly normalize semicolons style text. Thanks to [Alin Purcaru](https://github.com/mesmerizero)!
* [#12243](http://dev.ckeditor.com/ticket/12243): Fixed: Text formatting lost when pasting from Word. Thanks to [Alin Purcaru](https://github.com/mesmerizero)!
* [#111739](http://dev.ckeditor.com/ticket/11739): Fixed: `keypress` listeners should not be used in the undo manager. A complete rewrite of keyboard handling in the undo manager was made. Numerous smaller issues were fixed, among others:
  * [#10926](http://dev.ckeditor.com/ticket/10926): [Chrome@Android] Fixed: Typing does not record snapshots and does not fire the [`editor.change`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-change) event.
  * [#11611](http://dev.ckeditor.com/ticket/11611): [Firefox] Fixed: The [`editor.change`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-change) event is fired when pressing Arrow keys.
  * [#12219](http://dev.ckeditor.com/ticket/12219): [Safari] Fixed: Some modifications of the [`UndoManager.locked`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.undo.UndoManager-property-locked) property violate strict mode in the [Undo](http://ckeditor.com/addon/undo) plugin.
* [#10916](http://dev.ckeditor.com/ticket/10916): Fixed: [Magic Line](http://ckeditor.com/addon/magicline) icon in Right-To-Left environments.
* [#11970](http://dev.ckeditor.com/ticket/11970): [IE] Fixed: CKEditor `paste` event is not fired when pasting with *Shift+Ins*.
* [#12111](http://dev.ckeditor.com/ticket/12111): Fixed: Linked image attributes are not read when opening the image dialog window by doubleclicking.
* [#10030](http://dev.ckeditor.com/ticket/10030): [IE] Fixed: Prevented "Unspecified Error" thrown in various cases when IE8-9 does not allow access to `document.activeElement`.
* [#12273](http://dev.ckeditor.com/ticket/12273): Fixed: Applying block style in a description list breaks it.
* [#12218](http://dev.ckeditor.com/ticket/12218): Fixed: Minor syntax issue in CSS files.
* [#12178](http://dev.ckeditor.com/ticket/12178): [Blink/WebKit] Fixed: Iterator does not return the block if the selection is located at the end of it.
* [#12185](http://dev.ckeditor.com/ticket/12185): [IE9QM] Fixed: Error thrown when moving the mouse over focused editor's scrollbar.
* [#12215](http://dev.ckeditor.com/ticket/12215): Fixed: Basepath resolution does not recognize semicolon as a query separator.
* [#12135](http://dev.ckeditor.com/ticket/12135): Fixed: [Remove Format](http://ckeditor.com/addon/removeformat) does not work on widgets.
* [#12298](http://dev.ckeditor.com/ticket/12298): [IE11] Fixed: Clicking below `<body>` in Compatibility Mode will no longer reset selection to the first line.
* [#12204](http://dev.ckeditor.com/ticket/12204): Fixed: Editor's voice label is not affected by [`config.title`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-title).
* [#11915](http://dev.ckeditor.com/ticket/11915): Fixed: With [SCAYT](http://ckeditor.com/addon/scayt) enabled, cursor moves to the beginning of the first highlighted, misspelled word after typing or pasting into the editor.
* [SCAYT](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/69): Fixed: Error thrown in the console after enabling [SCAYT](http://ckeditor.com/addon/scayt) and trying to add a new image.


Other Changes:

* [#12296](http://dev.ckeditor.com/ticket/12296): Merged `benderjs-ckeditor` into the main CKEditor repository.

## CKEditor 4.4.3

**Security Updates:**

* Fixed XSS vulnerability in the Preview plugin reported by Mario Heiderich of [Cure53](https://cure53.de/).

**An upgrade is highly recommended!**

New Features:

* [#12164](http://dev.ckeditor.com/ticket/12164): Added the "Justify" option to the "Horizontal Alignment" drop-down in the Table Cell Properties dialog window.

Fixed Issues:

* [#12110](http://dev.ckeditor.com/ticket/12110): Fixed: Editor crash after deleting a table. Thanks to [Alin Purcaru](https://github.com/mesmerizero)!
* [#11897](http://dev.ckeditor.com/ticket/11897): Fixed: *Enter* key used in an empty list item creates a new line instead of breaking the list. Thanks to [noam-si](https://github.com/noam-si)!
* [#12140](http://dev.ckeditor.com/ticket/12140): Fixed: Double-clicking linked widgets opens two dialog windows.
* [#12132](http://dev.ckeditor.com/ticket/12132): Fixed: Image is inserted with `width` and `height` styles even when they are not allowed.
* [#9317](http://dev.ckeditor.com/ticket/9317): [IE] Fixed: [`config.disableObjectResizing`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-disableObjectResizing) does not work on IE. **Note**: We were not able to fix this issue on IE11+ because necessary events stopped working. See a [last resort workaround](http://dev.ckeditor.com/ticket/9317#comment:16) and make sure to [support our complaint to Microsoft](https://connect.microsoft.com/IE/feedback/details/742593/please-respect-execcommand-enableobjectresizing-in-contenteditable-elements).
* [#9638](http://dev.ckeditor.com/ticket/9638): Fixed: There should be no information about accessibility help available under the *Alt+0* keyboard shortcut if the [Accessibility Help](http://ckeditor.com/addon/a11yhelp) plugin is not available.
* [#8117](http://dev.ckeditor.com/ticket/8117) and [#9186](http://dev.ckeditor.com/ticket/9186): Fixed: In HTML5 `<meta>` tags should be allowed everywhere, including inside the `<body>` element.
* [#10422](http://dev.ckeditor.com/ticket/10422): Fixed: [`config.fillEmptyBlocks`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-fillEmptyBlocks) not working properly if a function is specified.

## CKEditor 4.4.2

Important Notes:

* The CKEditor testing environment is now publicly available. Read more about how to set up the environment and execute tests in the [CKEditor Testing Environment](http://docs.ckeditor.com/#!/guide/dev_tests) guide.
	Please note that the [`tests/`](https://github.com/ckeditor/ckeditor-dev/tree/master/tests) directory which contains editor tests is not available in release packages. It can only be found in the development version of CKEditor on [GitHub](https://github.com/ckeditor/ckeditor-dev/).

New Features:

* [#11909](http://dev.ckeditor.com/ticket/11909): Introduced a parameter to prevent the [`editor.setData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-setData) method from recording undo snapshots.

Fixed Issues:

* [#11757](http://dev.ckeditor.com/ticket/11757): Fixed: Imperfections in the [Moono](http://ckeditor.com/addon/moono) skin. Thanks to [danyaPostfactum](https://github.com/danyaPostfactum)!
* [#10091](http://dev.ckeditor.com/ticket/10091): Blockquote should be treated like an object by the styles system. Thanks to [dan-james-deeson](https://github.com/dan-james-deeson)!
* [#11478](http://dev.ckeditor.com/ticket/11478): Fixed: Issue with passing jQuery objects to [adapter](http://docs.ckeditor.com/#!/guide/dev_jquery) configuration.
* [#10867](http://dev.ckeditor.com/ticket/10867): Fixed: Issue with setting encoded URI as image link.
* [#11983](http://dev.ckeditor.com/ticket/11983): Fixed: Clicking a nested widget does not focus it. Additionally, performance of the [`widget.repository.getByElement()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository-method-getByElement) method was improved.
* [#12000](http://dev.ckeditor.com/ticket/12000): Fixed: Nested widgets should be initialized on [`editor.setData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-setData) and [`nestedEditable.setData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.nestedEditable-method-setData).
* [#12022](http://dev.ckeditor.com/ticket/12022): Fixed: Outer widget's drag handler is not created at all if it has any nested widgets inside.
* [#11960](http://dev.ckeditor.com/ticket/11960): [Blink/WebKit] Fixed: The caret should be scrolled into view on *Backspace* and *Delete* (covers only the merging blocks case).
* [#11306](http://dev.ckeditor.com/ticket/11306): [OSX][Blink/WebKit] Fixed: No widget entries in the context menu on widget right-click.
* [#11957](http://dev.ckeditor.com/ticket/11957): Fixed: Alignment labels in the [Enhanced Image](http://ckeditor.com/addon/image2) dialog window are not translated.
* [#11980](http://dev.ckeditor.com/ticket/11980): [Blink/WebKit] Fixed: `<span>` elements created when joining adjacent elements (non-collapsed selection).
* [#12009](http://dev.ckeditor.com/ticket/12009): [Nested widgets] Integration with the [Magic Line](http://ckeditor.com/addon/magicline) plugin.
* [#11387](http://dev.ckeditor.com/ticket/11387): Fixed: `role="radiogroup"` should be applied only to radio inputs' container.
* [#7975](http://dev.ckeditor.com/ticket/7975): [IE8] Fixed: Errors when trying to select an empty table cell.
* [#11947](http://dev.ckeditor.com/ticket/11947): [Firefox+IE11] Fixed: *Shift+Enter* in lists produces two line breaks.
* [#11972](http://dev.ckeditor.com/ticket/11972): Fixed: Feature detection in the [`element.setText()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-setText) method should not trigger the layout engine.
* [#7634](http://dev.ckeditor.com/ticket/7634): Fixed: The [Flash Dialog](http://ckeditor.com/addon/flash) plugin omits the `allowFullScreen` parameter in the editor data if set to `true`.
* [#11910](http://dev.ckeditor.com/ticket/11910): Fixed: [Enhanced Image](http://ckeditor.com/addon/image2) does not take [`config.baseHref`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-baseHref) into account when updating image dimensions.
* [#11753](http://dev.ckeditor.com/ticket/11753): Fixed: Wrong [`checkDirty()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-checkDirty) method value after focusing or blurring a widget.
* [#11830](http://dev.ckeditor.com/ticket/11830): Fixed: Impossible to pass some arguments to [CKBuilder](https://github.com/ckeditor/ckbuilder) when using the `/dev/builder/build.sh` script.
* [#11945](http://dev.ckeditor.com/ticket/11945): Fixed: [Form Elements](http://ckeditor.com/addon/forms) plugin should not change a core method.
* [#11384](http://dev.ckeditor.com/ticket/11384): [IE9+] Fixed: `IndexSizeError` thrown when pasting into a non-empty selection anchored in one text node.

## CKEditor 4.4.1

New Features:

* [#9661](http://dev.ckeditor.com/ticket/9661): Added the option to [configure](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-linkJavaScriptLinksAllowed) anchor tags with JavaScript code in the `href` attribute.

Fixed Issues:

* [#11861](http://dev.ckeditor.com/ticket/11861): [WebKit/Blink] Fixed: Span elements created while joining adjacent elements. **Note:** This patch only covers cases when *Backspace* or *Delete* is pressed on a collapsed (empty) selection. The remaining case, with a non-empty selection, will be fixed in the next release.
* [#10714](http://dev.ckeditor.com/ticket/10714): [iOS] Fixed: Selection and drop-downs are broken if a touch event listener is used due to a [WebKit bug](https://bugs.webkit.org/show_bug.cgi?id=128924). Thanks to [Arty Gus](https://github.com/artygus)!
* [#11911](http://dev.ckeditor.com/ticket/11911): Fixed setting the `dir` attribute for a preloaded language in [CKEDITOR.lang](http://docs.ckeditor.com/#!/api/CKEDITOR.lang). Thanks to [Akash Mohapatra](https://github.com/akashmohapatra)!
* [#11926](http://dev.ckeditor.com/ticket/11926): Fixed: [Code Snippet](http://ckeditor.com/addon/codesnippet) does not decode HTML entities when loading code from the `<code>` element.
* [#11223](http://dev.ckeditor.com/ticket/11223): Fixed: Issue when [Protected Source](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-protectedSource) was not working in the `<title>` element.
* [#11859](http://dev.ckeditor.com/ticket/11859): Fixed: Removed the [Source Dialog](http://ckeditor.com/addon/sourcedialog) plugin dependency from the [Code Snippet](http://ckeditor.com/addon/codesnippet) sample.
* [#11754](http://dev.ckeditor.com/ticket/11754): [Chrome] Fixed: Infinite loop when content includes not closed attributes.
* [#11848](http://dev.ckeditor.com/ticket/11848): [IE] Fixed: [`editor.insertElement()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-insertElement) throwing an exception when there was no selection in the editor.
* [#11801](http://dev.ckeditor.com/ticket/11801): Fixed: Editor anchors unavailable when linking the [Enhanced Image](http://ckeditor.com/addon/image2) widget.
* [#11626](http://dev.ckeditor.com/ticket/11626): Fixed: [Table Resize](http://ckeditor.com/addon/tableresize) sets invalid column width.
* [#11872](http://dev.ckeditor.com/ticket/11872): Made [`element.addClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-addClass) chainable symmetrically to [`element.removeClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-removeClass).
* [#11813](http://dev.ckeditor.com/ticket/11813): Fixed: Link lost while pasting a captioned image and restoring an undo snapshot ([Enhanced Image](http://ckeditor.com/addon/image2)).
* [#11814](http://dev.ckeditor.com/ticket/11814): Fixed: _Link_ and _Unlink_ entries persistently displayed in the [Enhanced Image](http://ckeditor.com/addon/image2) context menu.
* [#11839](http://dev.ckeditor.com/ticket/11839): [IE9] Fixed: The caret jumps out of the editable area when resizing the editor in the source mode.
* [#11822](http://dev.ckeditor.com/ticket/11822): [WebKit] Fixed: Editing anchors by double-click is broken in some cases.
* [#11823](http://dev.ckeditor.com/ticket/11823): [IE8] Fixed: [Table Resize](http://ckeditor.com/addon/tableresize) throws an error over scrollbar.
* [#11788](http://dev.ckeditor.com/ticket/11788): Fixed: It is not possible to change the language back to _Not set_ in the [Code Snippet](http://ckeditor.com/addon/codesnippet) dialog window.
* [#11788](http://dev.ckeditor.com/ticket/11788): Fixed: [Filter](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.filter) rules are not applied inside elements with the `contenteditable` attribute set to `true`.
* [#11798](http://dev.ckeditor.com/ticket/11798): Fixed: Inserting a non-editable element inside a table cell breaks the table.
* [#11793](http://dev.ckeditor.com/ticket/11793): Fixed: Drop-down is not "on" when clicking it while the editor is blurred.
* [#11850](http://dev.ckeditor.com/ticket/11850): Fixed: Fake objects with the `contenteditable` attribute set to `false` are not downcasted properly.
* [#11811](http://dev.ckeditor.com/ticket/11811): Fixed: Widget's data is not encoded correctly when passed to an attribute.
* [#11777](http://dev.ckeditor.com/ticket/11777): Fixed encoding ampersand in the [Mathematical Formulas](http://ckeditor.com/addon/mathjax) plugin.
* [#11880](http://dev.ckeditor.com/ticket/11880): [IE8-9] Fixed: Linked image has a default thick border.

Other Changes:

* [#11807](http://dev.ckeditor.com/ticket/11807): Updated jQuery version used in the sample to 1.11.0 and tested CKEditor jQuery Adapter with version 1.11.0 and 2.1.0.
* [#9504](http://dev.ckeditor.com/ticket/9504): Stopped using deprecated `attribute.specified` in all browsers except Internet Explorer.
* [#11809](http://dev.ckeditor.com/ticket/11809): Changed tab size in `<pre>` to 4 spaces.

## CKEditor 4.4

**Important Notes:**

* Marked the [`editor.beforePaste`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-beforePaste) event as deprecated.
* The default class of captioned images has changed to `image` (was: `caption`). Please note that once edited in CKEditor 4.4+, all existing images of the `caption` class (`<figure class="caption">`) will be [filtered out](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) unless the [`config.image2_captionedClass`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-image2_captionedClass) option is set to `caption`. For backward compatibility (i.e. when upgrading), it is highly recommended to use this setting, which also helps prevent CSS conflicts, etc. This does not apply to new CKEditor integrations.
* Widgets without defined buttons are no longer registered automatically to the [Advanced Content Filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter). Before CKEditor 4.4 widgets were registered to the ACF which was an incorrect behavior ([#11567](http://dev.ckeditor.com/ticket/11567)). This change should not have any impact on standard scenarios, but if your button does not execute the widget command, you need to set [`allowedContent`](http://docs.ckeditor.com/#!/api/CKEDITOR.feature-property-allowedContent) and [`requiredContent`](http://docs.ckeditor.com/#!/api/CKEDITOR.feature-property-requiredContent) properties for it manually, because the editor will not be able to find them.
* The [Show Borders](http://ckeditor.com/addon/showborders) plugin was added to the Standard installation package in order to ensure that unstyled tables are still visible for the user ([#11665](http://dev.ckeditor.com/ticket/11665)).
* Since CKEditor 4.4 the editor instance should be passed to [`CKEDITOR.style`](http://docs.ckeditor.com/#!/api/CKEDITOR.style) methods to ensure full compatibility with other features (e.g. applying styles to widgets requires that). We ensured backward compatibility though, so the [`CKEDITOR.style`](http://docs.ckeditor.com/#!/api/CKEDITOR.style) will work even when the editor instance is not provided.

New Features:

* [#11297](http://dev.ckeditor.com/ticket/11297): Styles can now be applied to widgets. The definition of a style which can be applied to a specific widget must contain two additional properties &mdash; `type` and `widget`. Read more in the [Widget Styles](http://docs.ckeditor.com/#!/guide/dev_styles-section-widget-styles) section of the "Syles Drop-down" guide. Note that by default, widgets support only classes and no other attributes or styles. Related changes and features:
  * Introduced the [`CKEDITOR.style.addCustomHandler()`](http://docs.ckeditor.com/#!/api/CKEDITOR.style-static-method-addCustomHandler) method for registering custom style handlers.
  * The [`CKEDITOR.style.apply()`](http://docs.ckeditor.com/#!/api/CKEDITOR.style-method-apply) and [`CKEDITOR.style.remove()`](http://docs.ckeditor.com/#!/api/CKEDITOR.style-method-remove) methods are now called with an editor instance instead of the document so they can be reused by the [`CKEDITOR.editor.applyStyle()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-applyStyle) and [`CKEDITOR.editor.removeStyle()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-removeStyle) methods. Backward compatibility was preserved, but from CKEditor 4.4 it is highly recommended to pass an editor instead of a document to these methods.
  * Many new methods and properties were introduced in the [Widget API](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget) to make the handling of styles by widgets fully customizable. See: [`widget.definition.styleableElements`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.definition-property-styleableElements), [`widget.definition.styleToAllowedContentRule`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.definition-property-styleToAllowedContentRules), [`widget.addClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-addClass), [`widget.removeClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-removeClass), [`widget.getClasses()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-getClasses), [`widget.hasClass()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-hasClass), [`widget.applyStyle()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-applyStyle), [`widget.removeStyle()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-removeStyle), [`widget.checkStyleActive()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-method-checkStyleActive).
  * Integration with the [Allowed Content Filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) required an introduction of the [`CKEDITOR.style.toAllowedContent()`](http://docs.ckeditor.com/#!/api/CKEDITOR.style-method-toAllowedContentRules) method which can be implemented by the custom style handler and if exists, it is used by the [`CKEDITOR.filter`](http://docs.ckeditor.com/#!/api/CKEDITOR.filter) to translate a style to [allowed content rules](http://docs.ckeditor.com/#!/api/CKEDITOR.filter.allowedContentRules).
* [#11300](http://dev.ckeditor.com/ticket/11300): Various changes in the [Enhanced Image](http://ckeditor.com/addon/image2) plugin:
  * Introduced the [`config.image2_captionedClass`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-image2_captionedClass) option to configure the class of captioned images.
  * Introduced the [`config.image2_alignClasses`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-image2_alignClasses) option to configure the way images are aligned with CSS classes.
  If this setting is defined, the editor produces classes instead of inline styles for aligned images.
  * Default image caption can be translated (customized) with the `editor.lang.image2.captionPlaceholder` string.
* [#11341](http://dev.ckeditor.com/ticket/11341): [Enhanced Image](http://ckeditor.com/addon/image2) plugin: It is now possible to add a link to any image type.
* [#10202](http://dev.ckeditor.com/ticket/10202): Introduced wildcard support in the [Allowed Content Rules](http://docs.ckeditor.com/#!/guide/dev_allowed_content_rules) format.
* [#10276](http://dev.ckeditor.com/ticket/10276): Introduced blacklisting in the [Allowed Content Filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter).
* [#10480](http://dev.ckeditor.com/ticket/10480): Introduced code snippets with code highlighting. There are two versions available so far &mdash; the default [Code Snippet](http://ckeditor.com/addon/codesnippet) which uses the [highlight.js](http://highlightjs.org) library and the [Code Snippet GeSHi](http://ckeditor.com/addon/codesnippetgeshi) which uses the [GeSHi](http://qbnz.com/highlighter/) library.
* [#11737](http://dev.ckeditor.com/ticket/11737): Introduced an option to prevent [filtering](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) of an element that matches custom criteria (see [`filter.addElementCallback()`](http://docs.ckeditor.com/#!/api/CKEDITOR.filter-method-addElementCallback)).
* [#11532](http://dev.ckeditor.com/ticket/11532): Introduced the [`editor.addContentsCss()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-addContentsCss) method that can be used for [adding custom CSS files](http://docs.ckeditor.com/#!/guide/plugin_sdk_styles).
* [#11536](http://dev.ckeditor.com/ticket/11536): Added the [`CKEDITOR.tools.htmlDecode()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-htmlDecode) method for decoding HTML entities.
* [#11225](http://dev.ckeditor.com/ticket/11225): Introduced the [`CKEDITOR.tools.transparentImageData`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-property-transparentImageData) property which contains transparent image data to be used in CSS or as image source.

Other Changes:

* [#11377](http://dev.ckeditor.com/ticket/11377): Unified internal representation of empty anchors using the [fake objects](http://ckeditor.com/addon/fakeobjects).
* [#11422](http://dev.ckeditor.com/ticket/11422): Removed Firefox 3.x, Internet Explorer 6 and Opera 12.x leftovers in code.
* [#5217](http://dev.ckeditor.com/ticket/5217): Setting data (including switching between modes) creates a new undo snapshot. Besides that:
  * Introduced the [`editable.status`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-property-status) property.
  * Introduced a new `forceUpdate` option for the [`editor.lockSnapshot`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-lockSnapshot) event.
  * Fixed: Selection not being unlocked in inline editor after setting data ([#11500](http://dev.ckeditor.com/ticket/11500)).
* The [WebSpellChecker](http://ckeditor.com/addon/wsc) plugin was updated to the latest version.

Fixed Issues:

* [#10190](http://dev.ckeditor.com/ticket/10190): Fixed: Removing block style with [`editor.removeStyle()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-removeStyle) should result in a paragraph and not a div.
* [#11727](http://dev.ckeditor.com/ticket/11727): Fixed: The editor tries to select a non-editable image which was clicked.

## CKEditor 4.3.5

New Features:

* Added new translation: Tatar.

Fixed Issues:

* [#11677](http://dev.ckeditor.com/ticket/11677): Fixed: Undo/Redo keystrokes are blocked in the source mode.
* [#11717](http://dev.ckeditor.com/ticket/11717): [Document Properties](http://ckeditor.com/addon/docprops) plugin requires the [Color Dialog](http://ckeditor.com/addon/colordialog) plugin to work.

## CKEditor 4.3.4

Fixed Issues:

* [#11597](http://dev.ckeditor.com/ticket/11597): [IE11] Fixed: Error thrown when trying to open the [preview](http://ckeditor.com/addon/preview) using the keyboard.
* [#11544](http://dev.ckeditor.com/ticket/11544): [Placeholders](http://ckeditor.com/addon/placeholder) will no longer be upcasted in parents not accepting `<span>` elements.
* [#8663](http://dev.ckeditor.com/ticket/8663): Fixed [`element.renameNode()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-renameNode) not clearing the [`element.getName()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.element-method-getName) cache.
* [#11574](http://dev.ckeditor.com/ticket/11574): Fixed: *Backspace* destroying the DOM structure if an inline editable is placed in a list item.
* [#11603](http://dev.ckeditor.com/ticket/11603): Fixed: [Table Resize](http://ckeditor.com/addon/tableresize) attaches to tables outside the editable.
* [#9205](http://dev.ckeditor.com/ticket/9205), [#7805](http://dev.ckeditor.com/ticket/7805), [#8216](http://dev.ckeditor.com/ticket/8216): Fixed: `{cke_protected_1}` appearing in data in various cases where HTML comments are placed next to `"` or `'`.
* [#11635](http://dev.ckeditor.com/ticket/11635): Fixed: Some attributes are not protected before the content is passed through the fix bin.
* [#11660](http://dev.ckeditor.com/ticket/11660): [IE] Fixed: Table content is lost when some extra markup is inside the table.
* [#11641](http://dev.ckeditor.com/ticket/11641): Fixed: Switching between modes in the classic editor removes content styles for the inline editor.
* [#11568](http://dev.ckeditor.com/ticket/11568): Fixed: [Styles](http://ckeditor.com/addon/stylescombo) drop-down list is not enabled on selection change.

## CKEditor 4.3.3

Fixed Issues:

* [#11500](http://dev.ckeditor.com/ticket/11500): [WebKit/Blink] Fixed: Selection lost when setting data in another inline editor. Additionally, [`selection.removeAllRanges()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.selection-method-removeAllRanges) is now scoped to selection's [root](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.selection-property-root).
* [#11104](http://dev.ckeditor.com/ticket/11104): [IE] Fixed: Various issues with scrolling and selection when focusing widgets.
* [#11487](http://dev.ckeditor.com/ticket/11487): Moving mouse over the [Enhanced Image](http://ckeditor.com/addon/image2) widget will no longer change the value returned by the [`editor.checkDirty()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-checkDirty) method.
* [#8673](http://dev.ckeditor.com/ticket/8673): [WebKit] Fixed: Cannot select and remove the [Page Break](http://ckeditor.com/addon/pagebreak).
* [#11413](http://dev.ckeditor.com/ticket/11413): Fixed: Incorrect [`editor.execCommand()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-execCommand) behavior.
* [#11438](http://dev.ckeditor.com/ticket/11438): Splitting table cells vertically is no longer changing table structure.
* [#8899](http://dev.ckeditor.com/ticket/8899): Fixed: Links in the [About CKEditor](http://ckeditor.com/addon/about) dialog window now open in a new browser window or tab.
* [#11490](http://dev.ckeditor.com/ticket/11490): Fixed: [Menu button](http://ckeditor.com/addon/menubutton) panel not showing in the source mode.
* [#11417](http://dev.ckeditor.com/ticket/11417): The [`widget.doubleclick`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget-event-doubleclick) event is not canceled anymore after editing was triggered.
* [#11253](http://dev.ckeditor.com/ticket/11253): [IE] Fixed: Clipped upload button in the [Enhanced Image](http://ckeditor.com/addon/image2) dialog window.
* [#11359](http://dev.ckeditor.com/ticket/11359): Standardized the way anchors are discovered by the [Link](http://ckeditor.com/addon/link) plugin.
* [#11058](http://dev.ckeditor.com/ticket/11058): [IE8] Fixed: Error when deleting a table row.
* [#11508](http://dev.ckeditor.com/ticket/11508): Fixed: [`htmlDataProcessor`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlDataProcessor) discovering protected attributes within other attributes' values.
* [#11533](http://dev.ckeditor.com/ticket/11533): Widgets: Avoid recurring upcasts if the DOM structure was modified during an upcast.
* [#11400](http://dev.ckeditor.com/ticket/11400): Fixed: The [`domObject.removeAllListeners()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.domObject-method-removeAllListeners) method does not remove custom listeners completely.
* [#11493](http://dev.ckeditor.com/ticket/11493): Fixed: The [`selection.getRanges()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.selection-method-getRanges) method does not override cached ranges when used with the `onlyEditables` argument.
* [#11390](http://dev.ckeditor.com/ticket/11390): [IE] All [XML](http://ckeditor.com/addon/xml) plugin [methods](http://docs.ckeditor.com/#!/api/CKEDITOR.xml) now work in IE10+.
* [#11542](http://dev.ckeditor.com/ticket/11542): [IE11] Fixed: Blurry toolbar icons when Right-to-Left UI language is set.
* [#11504](http://dev.ckeditor.com/ticket/11504): Fixed: When [`config.fullPage`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-fullPage) is set to `true`, entities are not encoded in editor output.
* [#11004](http://dev.ckeditor.com/ticket/11004): Integrated [Enhanced Image](http://ckeditor.com/addon/image2) dialog window with [Advanced Content Filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter).
* [#11439](http://dev.ckeditor.com/ticket/11439): Fixed: Properties get cloned in the Cell Properties dialog window if multiple cells are selected.

## CKEditor 4.3.2

Fixed Issues:

* [#11331](http://dev.ckeditor.com/ticket/11331): A menu button will have a changed label when selected instead of using the `aria-pressed` attribute.
* [#11177](http://dev.ckeditor.com/ticket/11177): Widget drag handler improvements:
  * [#11176](http://dev.ckeditor.com/ticket/11176): Fixed: Initial position is not updated when the widget data object is empty.
  * [#11001](http://dev.ckeditor.com/ticket/11001): Fixed: Multiple synchronous layout recalculations are caused by initial drag handler positioning causing performance issues.
  * [#11161](http://dev.ckeditor.com/ticket/11161): Fixed: Drag handler is not repositioned in various situations.
  * [#11281](http://dev.ckeditor.com/ticket/11281): Fixed: Drag handler and mask are duplicated after widget reinitialization.
* [#11207](http://dev.ckeditor.com/ticket/11207): [Firefox] Fixed: Misplaced [Enhanced Image](http://ckeditor.com/addon/image2) resizer in the inline editor.
* [#11102](http://dev.ckeditor.com/ticket/11102): `CKEDITOR.template` improvements:
  * [#11102](http://dev.ckeditor.com/ticket/11102): Added newline character support.
  * [#11216](http://dev.ckeditor.com/ticket/11216): Added "\\'" substring support.
* [#11121](http://dev.ckeditor.com/ticket/11121): [Firefox] Fixed: High Contrast mode is enabled when the editor is loaded in a hidden iframe.
* [#11350](http://dev.ckeditor.com/ticket/11350): The default value of [`config.contentsCss`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-contentsCss) is affected by [`CKEDITOR.getUrl()`](http://docs.ckeditor.com/#!/api/CKEDITOR-method-getUrl).
* [#11097](http://dev.ckeditor.com/ticket/11097): Improved the [Autogrow](http://ckeditor.com/addon/autogrow) plugin performance when dealing with very big tables.
* [#11290](http://dev.ckeditor.com/ticket/11290): Removed redundant code in the [Source Dialog](http://ckeditor.com/addon/sourcedialog) plugin.
* [#11133](http://dev.ckeditor.com/ticket/11133): [Page Break](http://ckeditor.com/addon/pagebreak) becomes editable if pasted.
* [#11126](http://dev.ckeditor.com/ticket/11126): Fixed: Native Undo executed once the bottom of the snapshot stack is reached.
* [#11131](http://dev.ckeditor.com/ticket/11131): [Div Editing Area](http://ckeditor.com/addon/divarea): Fixed: Error thrown when switching to source mode if the selection was in widget's nested editable.
* [#11139](http://dev.ckeditor.com/ticket/11139): [Div Editing Area](http://ckeditor.com/addon/divarea): Fixed: Elements Path is not cleared after switching to source mode.
* [#10778](http://dev.ckeditor.com/ticket/10778): Fixed a bug with range enlargement. The range no longer expands to visible whitespace.
* [#11146](http://dev.ckeditor.com/ticket/11146): [IE] Fixed: Preview window switches Internet Explorer to Quirks Mode.
* [#10762](http://dev.ckeditor.com/ticket/10762): [IE] Fixed: JavaScript code displayed in preview window's URL bar.
* [#11186](http://dev.ckeditor.com/ticket/11186): Introduced the [`widgets.repository.addUpcastCallback()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository-method-addUpcastCallback) method that allows to block upcasting given element to a widget.
* [#11307](http://dev.ckeditor.com/ticket/11307): Fixed: Paste as Plain Text conflict with the [MooTools](http://mootools.net) library.
* [#11140](http://dev.ckeditor.com/ticket/11140): [IE11] Fixed: Anchors are not draggable.
* [#11379](http://dev.ckeditor.com/ticket/11379): Changed default contents `line-height` to unitless values to avoid huge text overlapping (like in [#9696](http://dev.ckeditor.com/ticket/9696)).
* [#10787](http://dev.ckeditor.com/ticket/10787): [Firefox] Fixed: Broken replacement of text while pasting into `div`-based editor.
* [#10884](http://dev.ckeditor.com/ticket/10884): Widgets integration with the [Show Blocks](http://ckeditor.com/addon/showblocks) plugin.
* [#11021](http://dev.ckeditor.com/ticket/11021): Fixed: An error thrown when selecting entire editable contents while fake selection is on.
* [#11086](http://dev.ckeditor.com/ticket/11086): [IE8] Re-enable inline widgets drag&drop in Internet Explorer 8.
* [#11372](http://dev.ckeditor.com/ticket/11372): Widgets: Special characters encoded twice in nested editables.
* [#10068](http://dev.ckeditor.com/ticket/10068): Fixed: Support for protocol-relative URLs.
* [#11283](http://dev.ckeditor.com/ticket/11283): [Enhanced Image](http://ckeditor.com/addon/image2): A `<div>` element with `text-align: center` and an image inside is not recognised correctly.
* [#11196](http://dev.ckeditor.com/ticket/11196): [Accessibility Instructions](http://ckeditor.com/addon/a11yhelp): Allowed additional keyboard button labels to be translated in the dialog window.

## CKEditor 4.3.1

**Important Notes:**

* To match the naming convention, the `language` button is now `Language` ([#11201](http://dev.ckeditor.com/ticket/11201)).
* [Enhanced Image](http://ckeditor.com/addon/image2) button, context menu, command, and icon names match those of the [Image](http://ckeditor.com/addon/image) plugin ([#11222](http://dev.ckeditor.com/ticket/11222)).

Fixed Issues:

* [#11244](http://dev.ckeditor.com/ticket/11244): Changed: The [`widget.repository.checkWidgets()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository-method-checkWidgets) method now fires the [`widget.repository.checkWidgets`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository-event-checkWidgets) event, so from CKEditor 4.3.1 it is preferred to use the method rather than fire the event.
* [#11171](http://dev.ckeditor.com/ticket/11171): Fixed: [`editor.insertElement()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-insertElement) and [`editor.insertText()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-insertText) methods do not call the [`widget.repository.checkWidgets()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.repository-method-checkWidgets) method.
* [#11085](http://dev.ckeditor.com/ticket/11085): [IE8] Replaced preview generated by the [Mathematical Formulas](http://ckeditor.com/addon/mathjax) widget with a placeholder.
* [#11044](http://dev.ckeditor.com/ticket/11044): Enhanced WAI-ARIA support for the [Language](http://ckeditor.com/addon/language) plugin drop-down menu.
* [#11075](http://dev.ckeditor.com/ticket/11075): With drop-down menu button focused, pressing the *Down Arrow* key will now open the menu and focus its first option.
* [#11165](http://dev.ckeditor.com/ticket/11165): Fixed: The [File Browser](http://ckeditor.com/addon/filebrowser) plugin cannot be removed from the editor.
* [#11159](http://dev.ckeditor.com/ticket/11159): [IE9-10] [Enhanced Image](http://ckeditor.com/addon/image2): Fixed buggy discovery of image dimensions.
* [#11101](http://dev.ckeditor.com/ticket/11101): Drop-down lists no longer break when given double quotes.
* [#11077](http://dev.ckeditor.com/ticket/11077): [Enhanced Image](http://ckeditor.com/addon/image2): Empty undo step recorded when resizing the image.
* [#10853](http://dev.ckeditor.com/ticket/10853): [Enhanced Image](http://ckeditor.com/addon/image2): Widget has paragraph wrapper when de-captioning unaligned image.
* [#11198](http://dev.ckeditor.com/ticket/11198): Widgets: Drag handler is not fully visible when an inline widget is in a heading.
* [#11132](http://dev.ckeditor.com/ticket/11132): [Firefox] Fixed: Caret is lost after drag and drop of an inline widget.
* [#11182](http://dev.ckeditor.com/ticket/11182): [IE10-11] Fixed: Editor crashes (IE11) or works with minor issues (IE10) if a page is loaded in Quirks Mode. See [`env.quirks`](http://docs.ckeditor.com/#!/api/CKEDITOR.env-property-quirks) for more details.
* [#11204](http://dev.ckeditor.com/ticket/11204): Added `figure` and `figcaption` styles to the `contents.css` file so [Enhanced Image](http://ckeditor.com/addon/image2) looks nicer.
* [#11202](http://dev.ckeditor.com/ticket/11202): Fixed: No newline in [BBCode](http://ckeditor.com/addon/bbcode) mode.
* [#10890](http://dev.ckeditor.com/ticket/10890): Fixed: Error thrown when pressing the *Delete* key in a list item.
* [#10055](http://dev.ckeditor.com/ticket/10055): [IE8-10] Fixed: *Delete* pressed on a selected image causes the browser to go back.
* [#11183](http://dev.ckeditor.com/ticket/11183): Fixed: Inserting a horizontal rule or a table in multiple row selection causes a browser crash. Additionally, the [`editor.insertElement()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-insertElement) method does not insert the element into every range of a selection any more.
* [#11042](http://dev.ckeditor.com/ticket/11042): Fixed: Selection made on an element containing a non-editable element was not auto faked.
* [#11125](http://dev.ckeditor.com/ticket/11125): Fixed: Keyboard navigation through menu and drop-down items will now cycle.
* [#11011](http://dev.ckeditor.com/ticket/11011): Fixed: The [`editor.applyStyle()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-applyStyle) method removes attributes from nested elements.
* [#11179](http://dev.ckeditor.com/ticket/11179): Fixed: [`editor.destroy()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-destroy) does not cleanup content generated by the [Table Resize](http://ckeditor.com/addon/tableresize) plugin for inline editors.
* [#11237](http://dev.ckeditor.com/ticket/11237): Fixed: Table border attribute value is deleted when pasting content from Microsoft Word.
* [#11250](http://dev.ckeditor.com/ticket/11250): Fixed: HTML entities inside the `<textarea>` element are not encoded.
* [#11260](http://dev.ckeditor.com/ticket/11260): Fixed: Initially disabled buttons are not read by JAWS as disabled.
* [#11200](http://dev.ckeditor.com/ticket/11200):  Added [Clipboard](http://ckeditor.com/addon/clipboard) plugin as a dependency for [Widget](http://ckeditor.com/addon/widget) to fix drag and drop.

## CKEditor 4.3

New Features:

* [#10612](http://dev.ckeditor.com/ticket/10612): Internet Explorer 11 support.
* [#10869](http://dev.ckeditor.com/ticket/10869): Widgets: Added better integration with the [Elements Path](http://ckeditor.com/addon/elementspath) plugin.
* [#10886](http://dev.ckeditor.com/ticket/10886): Widgets: Added tooltip to the drag handle.
* [#10933](http://dev.ckeditor.com/ticket/10933): Widgets: Introduced drag and drop of block widgets with the [Line Utilities](http://ckeditor.com/addon/lineutils) plugin.
* [#10936](http://dev.ckeditor.com/ticket/10936): Widget System changes for easier integration with other dialog systems.
* [#10895](http://dev.ckeditor.com/ticket/10895): [Enhanced Image](http://ckeditor.com/addon/image2): Added file browser integration.
* [#11002](http://dev.ckeditor.com/ticket/11002): Added the [`draggable`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget.definition-property-draggable) option to disable drag and drop support for widgets.
* [#10937](http://dev.ckeditor.com/ticket/10937): [Mathematical Formulas](http://ckeditor.com/addon/mathjax) widget improvements:
  * loading indicator ([#10948](http://dev.ckeditor.com/ticket/10948)),
  * applying paragraph changes (like font color change) to iframe ([#10841](http://dev.ckeditor.com/ticket/10841)),
  * Firefox and IE9 clipboard fixes ([#10857](http://dev.ckeditor.com/ticket/10857)),
  * fixing same origin policy issue ([#10840](http://dev.ckeditor.com/ticket/10840)),
  * fixing undo bugs ([#10842](http://dev.ckeditor.com/ticket/10842), [#10930](http://dev.ckeditor.com/ticket/10930)),
  * fixing other minor bugs.
* [#10862](http://dev.ckeditor.com/ticket/10862): [Placeholder](http://ckeditor.com/addon/placeholder) plugin was rewritten as a widget.
* [#10822](http://dev.ckeditor.com/ticket/10822): Added styles system integration with non-editable elements (for example widgets) and their nested editables. Styles cannot change non-editable content and are applied in nested editable only if allowed by its type and content filter.
* [#10856](http://dev.ckeditor.com/ticket/10856): Menu buttons will now toggle the visibility of their panels when clicked multiple times. [Language](http://ckeditor.com/addon/language) plugin fixes: Added active language highlighting, added an option to remove the language.
* [#10028](http://dev.ckeditor.com/ticket/10028): New [`config.dialog_noConfirmCancel`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-dialog_noConfirmCancel) configuration option that eliminates the need to confirm closing of a dialog window when the user changed any of its fields.
* [#10848](http://dev.ckeditor.com/ticket/10848): Integrate remaining plugins ([Styles](http://ckeditor.com/addon/stylescombo), [Format](http://ckeditor.com/addon/format), [Font](http://ckeditor.com/addon/font), [Color Button](http://ckeditor.com/addon/colorbutton), [Language](http://ckeditor.com/addon/language) and [Indent](http://ckeditor.com/addon/indent)) with [active filter](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-activeFilter).
* [#10855](http://dev.ckeditor.com/ticket/10855): Change the extension of emoticons in the [BBCode](http://ckeditor.com/addon/bbcode) sample from GIF to PNG.

Fixed Issues:

* [#10831](http://dev.ckeditor.com/ticket/10831): [Enhanced Image](http://ckeditor.com/addon/image2): Merged `image2inline` and `image2block` into one `image2` widget.
* [#10835](http://dev.ckeditor.com/ticket/10835): [Enhanced Image](http://ckeditor.com/addon/image2): Improved visibility of the resize handle.
* [#10836](http://dev.ckeditor.com/ticket/10836): [Enhanced Image](http://ckeditor.com/addon/image2): Preserve custom mouse cursor while resizing the image.
* [#10939](http://dev.ckeditor.com/ticket/10939): [Firefox] [Enhanced Image](http://ckeditor.com/addon/image2): hovering the image causes it to change.
* [#10866](http://dev.ckeditor.com/ticket/10866): Fixed: Broken *Tab* key navigation in the [Enhanced Image](http://ckeditor.com/addon/image2) dialog window.
* [#10833](http://dev.ckeditor.com/ticket/10833): Fixed: *Lock ratio* option should be on by default in the [Enhanced Image](http://ckeditor.com/addon/image2) dialog window.
* [#10881](http://dev.ckeditor.com/ticket/10881): Various improvements to *Enter* key behavior in nested editables.
* [#10879](http://dev.ckeditor.com/ticket/10879): [Remove Format](http://ckeditor.com/addon/removeformat) should not leak from a nested editable.
* [#10877](http://dev.ckeditor.com/ticket/10877): Fixed: [WebSpellChecker](http://ckeditor.com/addon/wsc) fails to apply changes if a nested editable was focused.
* [#10877](http://dev.ckeditor.com/ticket/10877): Fixed: [SCAYT](http://ckeditor.com/addon/wsc) blocks typing in nested editables.
* [#11079](http://dev.ckeditor.com/ticket/11079): Add button icons to the [Placeholder](http://ckeditor.com/addon/placeholder) sample.
* [#10870](http://dev.ckeditor.com/ticket/10870): The `paste` command is no longer being disabled when the clipboard is empty.
* [#10854](http://dev.ckeditor.com/ticket/10854): Fixed: Firefox prepends `<br>` to `<body>`, so it is stripped by the HTML data processor.
* [#10823](http://dev.ckeditor.com/ticket/10823): Fixed: [Link](http://ckeditor.com/addon/link) plugin does not work with non-editable content.
* [#10828](http://dev.ckeditor.com/ticket/10828): [Magic Line](http://ckeditor.com/addon/magicline) integration with the Widget System.
* [#10865](http://dev.ckeditor.com/ticket/10865): Improved hiding copybin, so copying widgets works smoothly.
* [#11066](http://dev.ckeditor.com/ticket/11066): Widget's private parts use CSS reset.
* [#11027](http://dev.ckeditor.com/ticket/11027): Fixed: Block commands break on widgets; added the [`contentDomInvalidated`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-contentDomInvalidated) event.
* [#10430](http://dev.ckeditor.com/ticket/10430): Resolve dependence of the [Image](http://ckeditor.com/addon/image) plugin on the [Form Elements](http://ckeditor.com/addon/forms) plugin.
* [#10911](http://dev.ckeditor.com/ticket/10911): Fixed: Browser *Alt* hotkeys will no longer be blocked while a widget is focused.
* [#11082](http://dev.ckeditor.com/ticket/11082): Fixed: Selected widget is not copied or cut when using toolbar buttons or context menu.
* [#11083](http://dev.ckeditor.com/ticket/11083): Fixed list and div element application to block widgets.
* [#10887](http://dev.ckeditor.com/ticket/10887): Internet Explorer 8 compatibility issues related to the Widget System.
* [#11074](http://dev.ckeditor.com/ticket/11074): Temporarily disabled inline widget drag and drop, because of seriously buggy native `range#moveToPoint` method.
* [#11098](http://dev.ckeditor.com/ticket/11098): Fixed: Wrong selection position after undoing widget drag and drop.
* [#11110](http://dev.ckeditor.com/ticket/11110): Fixed: IFrame and Flash objects are being incorrectly pasted in certain conditions.
* [#11129](http://dev.ckeditor.com/ticket/11129): Page break is lost when loading data.
* [#11123](http://dev.ckeditor.com/ticket/11123): [Firefox] Widget is destroyed after being dragged outside of `<body>`.
* [#11124](http://dev.ckeditor.com/ticket/11124): Fixed the [Elements Path](http://ckeditor.com/addon/elementspath) in an editor using the [Div Editing Area](http://ckeditor.com/addon/divarea).

## CKEditor 4.3 Beta

New Features:

* [#9764](http://dev.ckeditor.com/ticket/9764): Widget System.
  * [Widget plugin](http://ckeditor.com/addon/widget) introducing the [Widget API](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.widget).
  * New [`editor.enterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-enterMode) and [`editor.shiftEnterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-shiftEnterMode) properties &ndash; normalized versions of [`config.enterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-enterMode) and [`config.shiftEnterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-shiftEnterMode).
  * Dynamic editor settings. Starting from CKEditor 4.3 Beta, *Enter* mode values and [content filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) instances may be changed dynamically (for example when the caret was placed in an element in which editor features should be adjusted). When you are implementing a new editor feature, you should base its behavior on [dynamic](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-activeEnterMode) or [static](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-enterMode) *Enter* mode values depending on whether this feature works in selection context or globally on editor content.
      * Dynamic *Enter* mode values &ndash; [`editor.setActiveEnterMode()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-setActiveEnterMode) method, [`editor.activeEnterModeChange`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-activeEnterModeChange) event, and two properties: [`editor.activeEnterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-activeEnterMode) and [`editor.activeShiftEnterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-activeShiftEnterMode).
      * Dynamic content filter instances &ndash; [`editor.setActiveFilter()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-setActiveFilter) method, [`editor.activeFilterChange`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-activeFilterChange) event, and [`editor.activeFilter`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-activeFilter) property.
  * "Fake" selection was introduced. It makes it possible to virtually select any element when the real selection remains hidden. See the  [`selection.fake()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.selection-method-fake) method.
  * Default [`htmlParser.filter`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.filter) rules are not applied to non-editable elements (elements with `contenteditable` attribute set to `false` and their descendants) anymore. To add a rule which will be applied to all elements you need to pass an additional argument to the [`filter.addRules()`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.filter-method-addRules) method.
  * Dozens of new methods were introduced &ndash; most interesting ones:
      * [`document.find()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.document-method-find),
      * [`document.findOne()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.document-method-findOne),
      * [`editable.insertElementIntoRange()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-method-insertElementIntoRange),
      * [`range.moveToClosestEditablePosition()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-moveToClosestEditablePosition),
      * New methods for [`htmlParser.node`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.node) and [`htmlParser.element`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.element).
* [#10659](http://dev.ckeditor.com/ticket/10659): New [Enhanced Image](http://ckeditor.com/addon/image2) plugin that introduces a widget with integrated image captions, an option to center images, and dynamic "click and drag" resizing.
* [#10664](http://dev.ckeditor.com/ticket/10664): New [Mathematical Formulas](http://ckeditor.com/addon/mathjax) plugin that introduces the MathJax widget.
* [#7987](https://dev.ckeditor.com/ticket/7987): New [Language](http://ckeditor.com/addon/language) plugin that implements Language toolbar button to support [WCAG 3.1.2 Language of Parts](http://www.w3.org/TR/UNDERSTANDING-WCAG20/meaning-other-lang-id.html).
* [#10708](http://dev.ckeditor.com/ticket/10708): New [smileys](http://ckeditor.com/addon/smiley).

## CKEditor 4.2.3

Fixed Issues:

* [#10994](http://dev.ckeditor.com/ticket/10994): Fixed: Loading external jQuery library when opening the [jQuery Adapter](http://docs.ckeditor.com/#!/guide/dev_jquery) sample directly from file.
* [#10975](http://dev.ckeditor.com/ticket/10975): [IE] Fixed: Error thrown while opening the color palette.
* [#9929](http://dev.ckeditor.com/ticket/9929): [Blink/WebKit] Fixed: A non-breaking space is created once a character is deleted and a regular space is typed.
* [#10963](http://dev.ckeditor.com/ticket/10963): Fixed: JAWS issue with the keyboard shortcut for [Magic Line](http://ckeditor.com/addon/magicline).
* [#11096](http://dev.ckeditor.com/ticket/11096): Fixed: TypeError: Object has no method 'is'.

## CKEditor 4.2.2

Fixed Issues:

* [#9314](http://dev.ckeditor.com/ticket/9314): Fixed: Incorrect error message on closing a dialog window without saving changs.
* [#10308](http://dev.ckeditor.com/ticket/10308): [IE10] Fixed: Unspecified error when deleting a row.
* [#10945](http://dev.ckeditor.com/ticket/10945): [Chrome] Fixed: Clicking with a mouse inside the editor does not show the caret.
* [#10912](http://dev.ckeditor.com/ticket/10912): Prevent default action when content of a non-editable link is clicked.
* [#10913](http://dev.ckeditor.com/ticket/10913): Fixed [`CKEDITOR.plugins.addExternal()`](http://docs.ckeditor.com/#!/api/CKEDITOR.resourceManager-method-addExternal) not handling paths including file name specified.
* [#10666](http://dev.ckeditor.com/ticket/10666): Fixed [`CKEDITOR.tools.isArray()`](http://docs.ckeditor.com/#!/api/CKEDITOR.tools-method-isArray) not working cross frame.
* [#10910](http://dev.ckeditor.com/ticket/10910): [IE9] Fixed JavaScript error thrown in Compatibility Mode when clicking and/or typing in the editing area.
* [#10868](http://dev.ckeditor.com/ticket/10868): [IE8] Prevent the browser from crashing when applying the Inline Quotation style.
* [#10915](http://dev.ckeditor.com/ticket/10915): Fixed: Invalid CSS filter in the Kama skin.
* [#10914](http://dev.ckeditor.com/ticket/10914): Plugins [Indent List](http://ckeditor.com/addon/indentlist) and [Indent Block](http://ckeditor.com/addon/indentblock) are now included in the build configuration.
* [#10812](http://dev.ckeditor.com/ticket/10812): Fixed [`range.createBookmark2()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dom.range-method-createBookmark2) incorrectly normalizing offsets. This bug was causing many issues: [#10850](http://dev.ckeditor.com/ticket/10850), [#10842](http://dev.ckeditor.com/ticket/10842).
* [#10951](http://dev.ckeditor.com/ticket/10951): Reviewed and optimized focus handling on panels (combo, menu buttons, color buttons, and context menu) to enhance accessibility. Fixed [#10705](http://dev.ckeditor.com/ticket/10705), [#10706](http://dev.ckeditor.com/ticket/10706) and [#10707](http://dev.ckeditor.com/ticket/10707).
* [#10704](http://dev.ckeditor.com/ticket/10704): Fixed a JAWS issue with the Select Color dialog window title not being announced.
* [#10753](http://dev.ckeditor.com/ticket/10753): The floating toolbar in inline instances now has a dedicated accessibility label.

## CKEditor 4.2.1

Fixed Issues:

* [#10301](http://dev.ckeditor.com/ticket/10301): [IE9-10] Undo fails after 3+ consecutive paste actions with a JavaScript error.
* [#10689](http://dev.ckeditor.com/ticket/10689): Save toolbar button saves only the first editor instance.
* [#10368](http://dev.ckeditor.com/ticket/10368): Move language reading direction definition (`dir`) from main language file to core.
* [#9330](http://dev.ckeditor.com/ticket/9330): Fixed pasting anchors from MS Word.
* [#8103](http://dev.ckeditor.com/ticket/8103): Fixed pasting nested lists from MS Word.
* [#9958](http://dev.ckeditor.com/ticket/9958): [IE9] Pressing the "OK" button will trigger the `onbeforeunload` event in the popup dialog.
* [#10662](http://dev.ckeditor.com/ticket/10662): Fixed styles from the Styles drop-down list not registering to the ACF in case when the [Shared Spaces plugin](http://ckeditor.com/addon/sharedspace) is used.
* [#9654](http://dev.ckeditor.com/ticket/9654): Problems with Internet Explorer 10 Quirks Mode.
* [#9816](http://dev.ckeditor.com/ticket/9816): Floating toolbar does not reposition vertically in several cases.
* [#10646](http://dev.ckeditor.com/ticket/10646): Removing a selected sublist or nested table with *Backspace/Delete* removes the parent element.
* [#10623](http://dev.ckeditor.com/ticket/10623): [WebKit] Page is scrolled when opening a drop-down list.
* [#10004](http://dev.ckeditor.com/ticket/10004): [ChromeVox] Button names are not announced.
* [#10731](http://dev.ckeditor.com/ticket/10731): [WebSpellChecker](http://ckeditor.com/addon/wsc) plugin breaks cloning of editor configuration.
* It is now possible to set per instance [WebSpellChecker](http://ckeditor.com/addon/wsc) plugin configuration instead of setting the configuration globally.

## CKEditor 4.2

**Important Notes:**

* Dropped compatibility support for Internet Explorer 7 and Firefox 3.6.

* Both the Basic and the Standard distribution packages will not contain the new [Indent Block](http://ckeditor.com/addon/indentblock) plugin. Because of this the [Advanced Content Filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) might remove block indentations from existing contents. If you want to prevent this, either [add an appropriate ACF rule to your filter](http://docs.ckeditor.com/#!/guide/dev_allowed_content_rules) or create a custom build based on the Basic/Standard package and add the Indent Block plugin in [CKBuilder](http://ckeditor.com/builder).

New Features:

* [#10027](http://dev.ckeditor.com/ticket/10027): Separated list and block indentation into two plugins: [Indent List](http://ckeditor.com/addon/indentlist) and [Indent Block](http://ckeditor.com/addon/indentblock).
* [#8244](http://dev.ckeditor.com/ticket/8244): Use *(Shift+)Tab* to indent and outdent lists.
* [#10281](http://dev.ckeditor.com/ticket/10281): The [jQuery Adapter](http://docs.ckeditor.com/#!/guide/dev_jquery) is now available. Several jQuery-related issues fixed: [#8261](http://dev.ckeditor.com/ticket/8261), [#9077](http://dev.ckeditor.com/ticket/9077), [#8710](http://dev.ckeditor.com/ticket/8710), [#8530](http://dev.ckeditor.com/ticket/8530), [#9019](http://dev.ckeditor.com/ticket/9019), [#6181](http://dev.ckeditor.com/ticket/6181), [#7876](http://dev.ckeditor.com/ticket/7876), [#6906](http://dev.ckeditor.com/ticket/6906).
* [#10042](http://dev.ckeditor.com/ticket/10042): Introduced [`config.title`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-title) setting to change the human-readable title of the editor.
* [#9794](http://dev.ckeditor.com/ticket/9794): Added [`editor.change`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-change) event.
* [#9923](http://dev.ckeditor.com/ticket/9923): HiDPI support in the editor UI. HiDPI icons for [Moono skin](http://ckeditor.com/addon/moono) added.
* [#8031](http://dev.ckeditor.com/ticket/8031): Handle `required` attributes on `<textarea>` elements &mdash; introduced [`editor.required`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-required) event.
* [#10280](http://dev.ckeditor.com/ticket/10280): Ability to replace `<textarea>` elements with the inline editor.

Fixed Issues:

* [#10599](http://dev.ckeditor.com/ticket/10599): [Indent](http://ckeditor.com/addon/indent) plugin is no longer required by the [List](http://ckeditor.com/addon/list) plugin.
* [#10370](http://dev.ckeditor.com/ticket/10370): Inconsistency in data events between framed and inline editors.
* [#10438](http://dev.ckeditor.com/ticket/10438): [FF, IE] No selection is done on an editable element on executing [`editor.setData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-setData).

## CKEditor 4.1.3

New Features:

* Added new translation: Indonesian.

Fixed Issues:

* [#10644](http://dev.ckeditor.com/ticket/10644): Fixed a critical bug when pasting plain text in Blink-based browsers.
* [#5189](http://dev.ckeditor.com/ticket/5189): [Find/Replace](http://ckeditor.com/addon/find) dialog window: rename "Cancel" button to "Close".
* [#10562](http://dev.ckeditor.com/ticket/10562): [Housekeeping] Unified CSS gradient filter formats in the [Moono](http://ckeditor.com/addon/moono) skin.
* [#10537](http://dev.ckeditor.com/ticket/10537): Advanced Content Filter should register a default rule for [`config.shiftEnterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-shiftEnterMode).
* [#10610](http://dev.ckeditor.com/ticket/10610): [`CKEDITOR.dialog.addIframe()`](http://docs.ckeditor.com/#!/api/CKEDITOR.dialog-static-method-addIframe) incorrectly sets the iframe size in dialog windows.

## CKEditor 4.1.2

New Features:

* Added new translation: Sinhala.

Fixed Issues:

* [#10339](http://dev.ckeditor.com/ticket/10339): Fixed: Error thrown when inserted data was totally stripped out after filtering and processing.
* [#10298](http://dev.ckeditor.com/ticket/10298): Fixed: Data processor breaks attributes containing protected parts.
* [#10367](http://dev.ckeditor.com/ticket/10367): Fixed: [`editable.insertText()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editable-method-insertText) loses characters when `RegExp` replace controls are being inserted.
* [#10165](http://dev.ckeditor.com/ticket/10165): [IE] Access denied error when `document.domain` has been altered.
* [#9761](http://dev.ckeditor.com/ticket/9761): Update the *Backspace* key state in [`keystrokeHandler.blockedKeystrokes`](http://docs.ckeditor.com/#!/api/CKEDITOR.keystrokeHandler-property-blockedKeystrokes) when calling [`editor.setReadOnly()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-setReadOnly).
* [#6504](http://dev.ckeditor.com/ticket/6504): Fixed: Race condition while loading several [`config.customConfig`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-customConfig) files.
* [#10146](http://dev.ckeditor.com/ticket/10146): [Firefox] Empty lines are being removed while [`config.enterMode`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-enterMode) is [`CKEDITOR.ENTER_BR`](http://docs.ckeditor.com/#!/api/CKEDITOR-property-ENTER_BR).
* [#10360](http://dev.ckeditor.com/ticket/10360): Fixed: ARIA `role="application"` should not be used for dialog windows.
* [#10361](http://dev.ckeditor.com/ticket/10361): Fixed: ARIA `role="application"` should not be used for floating panels.
* [#10510](http://dev.ckeditor.com/ticket/10510): Introduced unique voice labels to differentiate between different editor instances.
* [#9945](http://dev.ckeditor.com/ticket/9945): [iOS] Scrolling not possible on iPad.
* [#10389](http://dev.ckeditor.com/ticket/10389): Fixed: Invalid HTML in the "Text and Table" template.
* [WebSpellChecker](http://ckeditor.com/addon/wsc) plugin user interface was changed to match CKEditor 4 style.

## CKEditor 4.1.1

New Features:

* Added new translation: Albanian.

Fixed Issues:

* [#10172](http://dev.ckeditor.com/ticket/10172): Pressing *Delete* or *Backspace* in an empty table cell moves the cursor to the next/previous cell.
* [#10219](http://dev.ckeditor.com/ticket/10219): Error thrown when destroying an editor instance in parallel with a `mouseup` event.
* [#10265](http://dev.ckeditor.com/ticket/10265): Wrong loop type in the [File Browser](http://ckeditor.com/addon/filebrowser) plugin.
* [#10249](http://dev.ckeditor.com/ticket/10249): Wrong undo/redo states at start.
* [#10268](http://dev.ckeditor.com/ticket/10268): [Show Blocks](http://ckeditor.com/addon/showblocks) does not recover after switching to Source view.
* [#9995](http://dev.ckeditor.com/ticket/9995): HTML code in the `<textarea>` should not be modified by the [`htmlDataProcessor`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlDataProcessor).
* [#10320](http://dev.ckeditor.com/ticket/10320): [Justify](http://ckeditor.com/addon/justify) plugin should add elements to Advanced Content Filter based on current [Enter mode](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-enterMode).
* [#10260](http://dev.ckeditor.com/ticket/10260): Fixed: Advanced Content Filter blocks [`tabSpaces`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-tabSpaces). Unified `data-cke-*` attributes filtering.
* [#10315](http://dev.ckeditor.com/ticket/10315): [WebKit] [Undo manager](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.undo.UndoManager) should not record snapshots after a filling character was added/removed.
* [#10291](http://dev.ckeditor.com/ticket/10291): [WebKit] Space after a filling character should be secured.
* [#10330](http://dev.ckeditor.com/ticket/10330): [WebKit] The filling character is not removed on `keydown` in specific cases.
* [#10285](http://dev.ckeditor.com/ticket/10285): Fixed: Styled text pasted from MS Word causes an infinite loop.
* [#10131](http://dev.ckeditor.com/ticket/10131): Fixed: [`undoManager.update()`](http://docs.ckeditor.com/#!/api/CKEDITOR.plugins.undo.UndoManager-method-update) does not refresh the command state.
* [#10337](http://dev.ckeditor.com/ticket/10337): Fixed: Unable to remove `<s>` using [Remove Format](http://ckeditor.com/addon/removeformat).

## CKEditor 4.1

Fixed Issues:

* [#10192](http://dev.ckeditor.com/ticket/10192): Closing lists with the *Enter* key does not work with [Advanced Content Filter](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) in several cases.
* [#10191](http://dev.ckeditor.com/ticket/10191): Fixed allowed content rules unification, so the [`filter.allowedContent`](http://docs.ckeditor.com/#!/api/CKEDITOR.filter-property-allowedContent) property always contains rules in the same format.
* [#10224](http://dev.ckeditor.com/ticket/10224): Advanced Content Filter does not remove non-empty `<a>` elements anymore.
* Minor issues in plugin integration with Advanced Content Filter:
  * [#10166](http://dev.ckeditor.com/ticket/10166): Added transformation from the `align` attribute to `float` style to preserve backward compatibility after the introduction of Advanced Content Filter.
  * [#10195](http://dev.ckeditor.com/ticket/10195): [Image](http://ckeditor.com/addon/image) plugin no longer registers rules for links to Advanced Content Filter.
  * [#10213](http://dev.ckeditor.com/ticket/10213): [Justify](http://ckeditor.com/addon/justify) plugin is now correctly registering rules to Advanced Content Filter when [`config.justifyClasses`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-justifyClasses) is defined.

## CKEditor 4.1 RC

New Features:

* [#9829](http://dev.ckeditor.com/ticket/9829): Advanced Content Filter - data and features activation based on editor configuration.

  Brand new data filtering system that works in 2 modes:

  * Based on loaded features (toolbar items, plugins) - the data will be filtered according to what the editor in its
  current configuration can handle.
  * Based on [`config.allowedContent`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-allowedContent) rules - the data
  will be filtered and the editor features (toolbar items, commands, keystrokes) will be enabled if they are allowed.

  See the `datafiltering.html` sample, [guides](http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter) and [`CKEDITOR.filter` API documentation](http://docs.ckeditor.com/#!/api/CKEDITOR.filter).
* [#9387](http://dev.ckeditor.com/ticket/9387): Reintroduced [Shared Spaces](http://ckeditor.com/addon/sharedspace) - the ability to display toolbar and bottom editor space in selected locations and to share them by different editor instances.
* [#9907](http://dev.ckeditor.com/ticket/9907): Added the [`contentPreview`](http://docs.ckeditor.com/#!/api/CKEDITOR-event-contentPreview) event for preview data manipulation.
* [#9713](http://dev.ckeditor.com/ticket/9713): Introduced the [Source Dialog](http://ckeditor.com/addon/sourcedialog) plugin that brings raw HTML editing for inline editor instances.
* Included in [#9829](http://dev.ckeditor.com/ticket/9829): Introduced new events, [`toHtml`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-toHtml) and [`toDataFormat`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-toDataFormat), allowing for better integration with data processing.
* [#9981](http://dev.ckeditor.com/ticket/9981): Added ability to filter [`htmlParser.fragment`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.fragment), [`htmlParser.element`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.element) etc. by many [`htmlParser.filter`](http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.filter)s before writing structure to an HTML string.
* Included in [#10103](http://dev.ckeditor.com/ticket/10103):
  * Introduced the [`editor.status`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-status) property to make it easier to check the current status of the editor.
  * Default [`command`](http://docs.ckeditor.com/#!/api/CKEDITOR.command) state is now [`CKEDITOR.TRISTATE_DISABLE`](http://docs.ckeditor.com/#!/api/CKEDITOR-property-TRISTATE_DISABLED). It will be activated on [`editor.instanceReady`](http://docs.ckeditor.com/#!/api/CKEDITOR-event-instanceReady) or immediately after being added if the editor is already initialized.
* [#9796](http://dev.ckeditor.com/ticket/9796): Introduced `<s>` as a default tag for strikethrough, which replaces obsolete `<strike>` in HTML5.

## CKEditor 4.0.3

Fixed Issues:

* [#10196](http://dev.ckeditor.com/ticket/10196): Fixed context menus not opening with keyboard shortcuts when [Autogrow](http://ckeditor.com/addon/autogrow) is enabled.
* [#10212](http://dev.ckeditor.com/ticket/10212): [IE7-10] Undo command throws errors after multiple switches between Source and WYSIWYG view.
* [#10219](http://dev.ckeditor.com/ticket/10219): [Inline editor] Error thrown after calling [`editor.destroy()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-destroy).

## CKEditor 4.0.2

Fixed Issues:

* [#9779](http://dev.ckeditor.com/ticket/9779): Fixed overriding [`CKEDITOR.getUrl()`](http://docs.ckeditor.com/#!/api/CKEDITOR-method-getUrl) with `CKEDITOR_GETURL`.
* [#9772](http://dev.ckeditor.com/ticket/9772): Custom buttons in the dialog window footer have different look and size ([Moono](http://ckeditor.com/addon/moono), [Kama](http://ckeditor.com/addon/kama) skins).
* [#9029](http://dev.ckeditor.com/ticket/9029): Custom styles added with the [`stylesSet.add()`](http://docs.ckeditor.com/#!/api/CKEDITOR.stylesSet-method-add) are displayed in the wrong order.
* [#9887](http://dev.ckeditor.com/ticket/9887): Disable [Magic Line](http://ckeditor.com/addon/magicline) when [`editor.readOnly`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-property-readOnly) is set.
* [#9882](http://dev.ckeditor.com/ticket/9882): Fixed empty document title on [`editor.getData()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-getData) if set via the Document Properties dialog window.
* [#9773](http://dev.ckeditor.com/ticket/9773): Fixed rendering problems with selection fields in the Kama skin.
* [#9851](http://dev.ckeditor.com/ticket/9851): The [`selectionChange`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-event-selectionChange) event is not fired when mouse selection ended outside editable.
* [#9903](http://dev.ckeditor.com/ticket/9903): [Inline editor] Bad positioning of floating space with page horizontal scroll.
* [#9872](http://dev.ckeditor.com/ticket/9872): [`editor.checkDirty()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-checkDirty) returns `true` when called onload. Removed the obsolete `editor.mayBeDirty` flag.
* [#9893](http://dev.ckeditor.com/ticket/9893): [IE] Fixed broken toolbar when editing mixed direction content in Quirks mode.
* [#9845](http://dev.ckeditor.com/ticket/9845): Fixed TAB navigation in the [Link](http://ckeditor.com/addon/link) dialog window when the Anchor option is used and no anchors are available.
* [#9883](http://dev.ckeditor.com/ticket/9883): Maximizing was making the entire page editable with [divarea](http://ckeditor.com/addon/divarea)-based editors.
* [#9940](http://dev.ckeditor.com/ticket/9940): [Firefox] Navigating back to a page with the editor was making the entire page editable.
* [#9966](http://dev.ckeditor.com/ticket/9966): Fixed: Unable to type square brackets with French keyboard layout. Changed [Magic Line](http://ckeditor.com/addon/magicline) keystrokes.
* [#9507](http://dev.ckeditor.com/ticket/9507): [Firefox] Selection is moved before editable position when the editor is focused for the first time.
* [#9947](http://dev.ckeditor.com/ticket/9947): [WebKit] Editor overflows parent container in some edge cases.
* [#10105](http://dev.ckeditor.com/ticket/10105): Fixed: Broken [sourcearea](http://ckeditor.com/addon/sourcearea) view when an RTL language is set.
* [#10123](http://dev.ckeditor.com/ticket/10123): [WebKit] Fixed: Several dialog windows have broken layout since the latest WebKit release.
* [#10152](http://dev.ckeditor.com/ticket/10152): Fixed: Invalid ARIA property used on menu items.

## CKEditor 4.0.1.1

Fixed Issues:

* Security update: Added protection against XSS attack and possible path disclosure in the PHP sample.

## CKEditor 4.0.1

Fixed Issues:

* [#9655](http://dev.ckeditor.com/ticket/9655): Support for IE Quirks Mode in the new [Moono skin](http://ckeditor.com/addon/moono).
* Accessibility issues (mainly in inline editor): [#9364](http://dev.ckeditor.com/ticket/9364), [#9368](http://dev.ckeditor.com/ticket/9368), [#9369](http://dev.ckeditor.com/ticket/9369), [#9370](http://dev.ckeditor.com/ticket/9370), [#9541](http://dev.ckeditor.com/ticket/9541), [#9543](http://dev.ckeditor.com/ticket/9543), [#9841](http://dev.ckeditor.com/ticket/9841), [#9844](http://dev.ckeditor.com/ticket/9844).
* [Magic Line](http://ckeditor.com/addon/magicline) plugin:
    * [#9481](http://dev.ckeditor.com/ticket/9481): Added accessibility support for Magic Line.
    * [#9509](http://dev.ckeditor.com/ticket/9509): Added Magic Line support for forms.
    * [#9573](http://dev.ckeditor.com/ticket/9573): Magic Line does not disappear on `mouseout` in a specific case.
* [#9754](http://dev.ckeditor.com/ticket/9754): [WebKit] Cutting & pasting simple unformatted text generates an inline wrapper in WebKit browsers.
* [#9456](http://dev.ckeditor.com/ticket/9456): [Chrome] Properly paste bullet list style from MS Word.
* [#9699](http://dev.ckeditor.com/ticket/9699), [#9758](http://dev.ckeditor.com/ticket/9758): Improved selection locking when selecting by dragging.
* Context menu:
    * [#9712](http://dev.ckeditor.com/ticket/9712): Opening the context menu destroys editor focus.
    * [#9366](http://dev.ckeditor.com/ticket/9366): Context menu should be displayed over the floating toolbar.
    * [#9706](http://dev.ckeditor.com/ticket/9706): Context menu generates a JavaScript error in inline mode when the editor is attached to a header element.
* [#9800](http://dev.ckeditor.com/ticket/9800): Hide float panel when resizing the window.
* [#9721](http://dev.ckeditor.com/ticket/9721): Padding in content of div-based editor puts the editing area under the bottom UI space.
* [#9528](http://dev.ckeditor.com/ticket/9528): Host page `box-sizing` style should not influence the editor UI elements.
* [#9503](http://dev.ckeditor.com/ticket/9503): [Form Elements](http://ckeditor.com/addon/forms) plugin adds context menu listeners only on supported input types. Added support for `tel`, `email`, `search` and `url` input types.
* [#9769](http://dev.ckeditor.com/ticket/9769): Improved floating toolbar positioning in a narrow window.
* [#9875](http://dev.ckeditor.com/ticket/9875): Table dialog window does not populate width correctly.
* [#8675](http://dev.ckeditor.com/ticket/8675): Deleting cells in a nested table removes the outer table cell.
* [#9815](http://dev.ckeditor.com/ticket/9815): Cannot edit dialog window fields in an editor initialized in the jQuery UI modal dialog.
* [#8888](http://dev.ckeditor.com/ticket/8888): CKEditor dialog windows do not show completely in a small window.
* [#9360](http://dev.ckeditor.com/ticket/9360): [Inline editor] Blocks shown for a `<div>` element stay permanently even after the user exits editing the `<div>`.
* [#9531](http://dev.ckeditor.com/ticket/9531): [Firefox & Inline editor] Toolbar is lost when closing the Format drop-down list by clicking its button.
* [#9553](http://dev.ckeditor.com/ticket/9553): Table width incorrectly set when the `border-width` style is specified.
* [#9594](http://dev.ckeditor.com/ticket/9594): Cannot tab past CKEditor when it is in read-only mode.
* [#9658](http://dev.ckeditor.com/ticket/9658): [IE9] Justify not working on selected images.
* [#9686](http://dev.ckeditor.com/ticket/9686): Added missing contents styles for `<pre>` elements.
* [#9709](http://dev.ckeditor.com/ticket/9709): [Paste from Word](http://ckeditor.com/addon/pastefromword) should not depend on configuration from other styles.
* [#9726](http://dev.ckeditor.com/ticket/9726): Removed [Color Dialog](http://ckeditor.com/addon/colordialog) plugin dependency from [Table Tools](http://ckeditor.com/addon/tabletools).
* [#9765](http://dev.ckeditor.com/ticket/9765): Toolbar Collapse command documented incorrectly in the [Accessibility Instructions](http://ckeditor.com/addon/a11yhelp) dialog window.
* [#9771](http://dev.ckeditor.com/ticket/9771): [WebKit & Opera] Fixed scrolling issues when pasting.
* [#9787](http://dev.ckeditor.com/ticket/9787): [IE9] `onChange` is not fired for checkboxes in dialogs.
* [#9842](http://dev.ckeditor.com/ticket/9842): [Firefox 17] When opening a toolbar menu for the first time and pressing the *Down Arrow* key, focus goes to the next toolbar button instead of the menu options.
* [#9847](http://dev.ckeditor.com/ticket/9847): [Elements Path](http://ckeditor.com/addon/elementspath) should not be initialized in the inline editor.
* [#9853](http://dev.ckeditor.com/ticket/9853): [`editor.addRemoveFormatFilter()`](http://docs.ckeditor.com/#!/api/CKEDITOR.editor-method-addRemoveFormatFilter) is exposed before it really works.
* [#8893](http://dev.ckeditor.com/ticket/8893): Value of the [`pasteFromWordCleanupFile`](http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-pasteFromWordCleanupFile) configuration option is now taken from the instance configuration.
* [#9693](http://dev.ckeditor.com/ticket/9693): Removed "Live Preview" checkbox from UI color picker.


## CKEditor 4.0

The first stable release of the new CKEditor 4 code line.

The CKEditor JavaScript API has been kept compatible with CKEditor 4, whenever
possible. The list of relevant changes can be found in the [API Changes page of
the CKEditor 4 documentation][1].

[1]: http://docs.ckeditor.com/#!/guide/dev_api_changes "API Changes"
Software License Agreement
==========================

CKEditor - The text editor for Internet - http://ckeditor.com
Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your
choice:

 - GNU General Public License Version 2 or later (the "GPL")
   http://www.gnu.org/licenses/gpl.html
   (See Appendix A)

 - GNU Lesser General Public License Version 2.1 or later (the "LGPL")
   http://www.gnu.org/licenses/lgpl.html
   (See Appendix B)

 - Mozilla Public License Version 1.1 or later (the "MPL")
   http://www.mozilla.org/MPL/MPL-1.1.html
   (See Appendix C)

You are not required to, but if you want to explicitly declare the
license you have chosen to be bound to when using, reproducing,
modifying and distributing this software, just include a text file
titled "legal.txt" in your version of this software, indicating your
license choice. In any case, your choice will not restrict any
recipient of your version of this software to use, reproduce, modify
and distribute this software under any of the above licenses.

Sources of Intellectual Property Included in CKEditor
-----------------------------------------------------

Where not otherwise indicated, all CKEditor content is authored by
CKSource engineers and consists of CKSource-owned intellectual
property. In some specific instances, CKEditor will incorporate work
done by developers outside of CKSource with their express permission.

The following libraries are included in CKEditor under the MIT license (see Appendix D):

* CKSource Samples Framework (included in the samples) - Copyright (c) 2014-2016, CKSource - Frederico Knabben.
* PicoModal (included in `samples/js/sf.js`) - Copyright (c) 2012 James Frasca.
* CodeMirror (included in the samples) - Copyright (C) 2014 by Marijn Haverbeke <marijnh@gmail.com> and others.

Parts of code taken from the following libraries are included in CKEditor under the MIT license (see Appendix D):

* jQuery (inspired the domReady function, ckeditor_base.js) - Copyright (c) 2011 John Resig, http://jquery.com/

The following libraries are included in CKEditor under the SIL Open Font License, Version 1.1 (see Appendix E):

* Font Awesome (included in the toolbar configurator) - Copyright (C) 2012 by Dave Gandy.

The following libraries are included in CKEditor under the BSD-3 License (see Appendix F):

* highlight.js (included in the `codesnippet` plugin) - Copyright (c) 2006, Ivan Sagalaev.
* YUI Library (included in the `uicolor` plugin) - Copyright (c) 2009, Yahoo! Inc.


Trademarks
----------

CKEditor is a trademark of CKSource - Frederico Knabben. All other brand
and product names are trademarks, registered trademarks or service
marks of their respective holders.

---

Appendix A: The GPL License
---------------------------

```
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
software-to make sure the software is free for all its users.  This
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
```

Appendix B: The LGPL License
----------------------------

```
GNU LESSER GENERAL PUBLIC LICENSE
Version 2.1, February 1999

 Copyright (C) 1991, 1999 Free Software Foundation, Inc.
     59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

[This is the first released version of the Lesser GPL.  It also counts
 as the successor of the GNU Library Public License, version 2, hence
 the version number 2.1.]

Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
Licenses are intended to guarantee your freedom to share and change
free software-to make sure the software is free for all its users.

  This license, the Lesser General Public License, applies to some
specially designated software packages-typically libraries-of the
Free Software Foundation and other authors who decide to use it.  You
can use it too, but we suggest you first think carefully about whether
this license or the ordinary General Public License is the better
strategy to use in any particular case, based on the explanations below.

  When we speak of free software, we are referring to freedom of use,
not price.  Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and charge
for this service if you wish); that you receive source code or can get
it if you want it; that you can change the software and use pieces of
it in new free programs; and that you are informed that you can do
these things.

  To protect your rights, we need to make restrictions that forbid
distributors to deny you these rights or to ask you to surrender these
rights.  These restrictions translate to certain responsibilities for
you if you distribute copies of the library or if you modify it.

  For example, if you distribute copies of the library, whether gratis
or for a fee, you must give the recipients all the rights that we gave
you.  You must make sure that they, too, receive or can get the source
code.  If you link other code with the library, you must provide
complete object files to the recipients, so that they can relink them
with the library after making changes to the library and recompiling
it.  And you must show them these terms so they know their rights.

  We protect your rights with a two-step method: (1) we copyright the
library, and (2) we offer you this license, which gives you legal
permission to copy, distribute and/or modify the library.

  To protect each distributor, we want to make it very clear that
there is no warranty for the free library.  Also, if the library is
modified by someone else and passed on, the recipients should know
that what they have is not the original version, so that the original
author's reputation will not be affected by problems that might be
introduced by others.

  Finally, software patents pose a constant threat to the existence of
any free program.  We wish to make sure that a company cannot
effectively restrict the users of a free program by obtaining a
restrictive license from a patent holder.  Therefore, we insist that
any patent license obtained for a version of the library must be
consistent with the full freedom of use specified in this license.

  Most GNU software, including some libraries, is covered by the
ordinary GNU General Public License.  This license, the GNU Lesser
General Public License, applies to certain designated libraries, and
is quite different from the ordinary General Public License.  We use
this license for certain libraries in order to permit linking those
libraries into non-free programs.

  When a program is linked with a library, whether statically or using
a shared library, the combination of the two is legally speaking a
combined work, a derivative of the original library.  The ordinary
General Public License therefore permits such linking only if the
entire combination fits its criteria of freedom.  The Lesser General
Public License permits more lax criteria for linking other code with
the library.

  We call this license the "Lesser" General Public License because it
does Less to protect the user's freedom than the ordinary General
Public License.  It also provides other free software developers Less
of an advantage over competing non-free programs.  These disadvantages
are the reason we use the ordinary General Public License for many
libraries.  However, the Lesser license provides advantages in certain
special circumstances.

  For example, on rare occasions, there may be a special need to
encourage the widest possible use of a certain library, so that it becomes
a de-facto standard.  To achieve this, non-free programs must be
allowed to use the library.  A more frequent case is that a free
library does the same job as widely used non-free libraries.  In this
case, there is little to gain by limiting the free library to free
software only, so we use the Lesser General Public License.

  In other cases, permission to use a particular library in non-free
programs enables a greater number of people to use a large body of
free software.  For example, permission to use the GNU C Library in
non-free programs enables many more people to use the whole GNU
operating system, as well as its variant, the GNU/Linux operating
system.

  Although the Lesser General Public License is Less protective of the
users' freedom, it does ensure that the user of a program that is
linked with the Library has the freedom and the wherewithal to run
that program using a modified version of the Library.

  The precise terms and conditions for copying, distribution and
modification follow.  Pay close attention to the difference between a
"work based on the library" and a "work that uses the library".  The
former contains code derived from the library, whereas the latter must
be combined with the library in order to run.

GNU LESSER GENERAL PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License Agreement applies to any software library or other
program which contains a notice placed by the copyright holder or
other authorized party saying it may be distributed under the terms of
this Lesser General Public License (also called "this License").
Each licensee is addressed as "you".

  A "library" means a collection of software functions and/or data
prepared so as to be conveniently linked with application programs
(which use some of those functions and data) to form executables.

  The "Library", below, refers to any such software library or work
which has been distributed under these terms.  A "work based on the
Library" means either the Library or any derivative work under
copyright law: that is to say, a work containing the Library or a
portion of it, either verbatim or with modifications and/or translated
straightforwardly into another language.  (Hereinafter, translation is
included without limitation in the term "modification".)

  "Source code" for a work means the preferred form of the work for
making modifications to it.  For a library, complete source code means
all the source code for all modules it contains, plus any associated
interface definition files, plus the scripts used to control compilation
and installation of the library.

  Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running a program using the Library is not restricted, and output from
such a program is covered only if its contents constitute a work based
on the Library (independent of the use of the Library in a tool for
writing it).  Whether that is true depends on what the Library does
and what the program that uses the Library does.

  1. You may copy and distribute verbatim copies of the Library's
complete source code as you receive it, in any medium, provided that
you conspicuously and appropriately publish on each copy an
appropriate copyright notice and disclaimer of warranty; keep intact
all the notices that refer to this License and to the absence of any
warranty; and distribute a copy of this License along with the
Library.

  You may charge a fee for the physical act of transferring a copy,
and you may at your option offer warranty protection in exchange for a
fee.

  2. You may modify your copy or copies of the Library or any portion
of it, thus forming a work based on the Library, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) The modified work must itself be a software library.

    b) You must cause the files modified to carry prominent notices
    stating that you changed the files and the date of any change.

    c) You must cause the whole of the work to be licensed at no
    charge to all third parties under the terms of this License.

    d) If a facility in the modified Library refers to a function or a
    table of data to be supplied by an application program that uses
    the facility, other than as an argument passed when the facility
    is invoked, then you must make a good faith effort to ensure that,
    in the event an application does not supply such function or
    table, the facility still operates, and performs whatever part of
    its purpose remains meaningful.

    (For example, a function in a library to compute square roots has
    a purpose that is entirely well-defined independent of the
    application.  Therefore, Subsection 2d requires that any
    application-supplied function or table used by this function must
    be optional: if the application does not supply it, the square
    root function must still compute square roots.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Library,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Library, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote
it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Library.

In addition, mere aggregation of another work not based on the Library
with the Library (or with a work based on the Library) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may opt to apply the terms of the ordinary GNU General Public
License instead of this License to a given copy of the Library.  To do
this, you must alter all the notices that refer to this License, so
that they refer to the ordinary GNU General Public License, version 2,
instead of to this License.  (If a newer version than version 2 of the
ordinary GNU General Public License has appeared, then you can specify
that version instead if you wish.)  Do not make any other change in
these notices.

  Once this change is made in a given copy, it is irreversible for
that copy, so the ordinary GNU General Public License applies to all
subsequent copies and derivative works made from that copy.

  This option is useful when you wish to copy part of the code of
the Library into a program that is not a library.

  4. You may copy and distribute the Library (or a portion or
derivative of it, under Section 2) in object code or executable form
under the terms of Sections 1 and 2 above provided that you accompany
it with the complete corresponding machine-readable source code, which
must be distributed under the terms of Sections 1 and 2 above on a
medium customarily used for software interchange.

  If distribution of object code is made by offering access to copy
from a designated place, then offering equivalent access to copy the
source code from the same place satisfies the requirement to
distribute the source code, even though third parties are not
compelled to copy the source along with the object code.

  5. A program that contains no derivative of any portion of the
Library, but is designed to work with the Library by being compiled or
linked with it, is called a "work that uses the Library".  Such a
work, in isolation, is not a derivative work of the Library, and
therefore falls outside the scope of this License.

  However, linking a "work that uses the Library" with the Library
creates an executable that is a derivative of the Library (because it
contains portions of the Library), rather than a "work that uses the
library".  The executable is therefore covered by this License.
Section 6 states terms for distribution of such executables.

  When a "work that uses the Library" uses material from a header file
that is part of the Library, the object code for the work may be a
derivative work of the Library even though the source code is not.
Whether this is true is especially significant if the work can be
linked without the Library, or if the work is itself a library.  The
threshold for this to be true is not precisely defined by law.

  If such an object file uses only numerical parameters, data
structure layouts and accessors, and small macros and small inline
functions (ten lines or less in length), then the use of the object
file is unrestricted, regardless of whether it is legally a derivative
work.  (Executables containing this object code plus portions of the
Library will still fall under Section 6.)

  Otherwise, if the work is a derivative of the Library, you may
distribute the object code for the work under the terms of Section 6.
Any executables containing that work also fall under Section 6,
whether or not they are linked directly with the Library itself.

  6. As an exception to the Sections above, you may also combine or
link a "work that uses the Library" with the Library to produce a
work containing portions of the Library, and distribute that work
under terms of your choice, provided that the terms permit
modification of the work for the customer's own use and reverse
engineering for debugging such modifications.

  You must give prominent notice with each copy of the work that the
Library is used in it and that the Library and its use are covered by
this License.  You must supply a copy of this License.  If the work
during execution displays copyright notices, you must include the
copyright notice for the Library among them, as well as a reference
directing the user to the copy of this License.  Also, you must do one
of these things:

    a) Accompany the work with the complete corresponding
    machine-readable source code for the Library including whatever
    changes were used in the work (which must be distributed under
    Sections 1 and 2 above); and, if the work is an executable linked
    with the Library, with the complete machine-readable "work that
    uses the Library", as object code and/or source code, so that the
    user can modify the Library and then relink to produce a modified
    executable containing the modified Library.  (It is understood
    that the user who changes the contents of definitions files in the
    Library will not necessarily be able to recompile the application
    to use the modified definitions.)

    b) Use a suitable shared library mechanism for linking with the
    Library.  A suitable mechanism is one that (1) uses at run time a
    copy of the library already present on the user's computer system,
    rather than copying library functions into the executable, and (2)
    will operate properly with a modified version of the library, if
    the user installs one, as long as the modified version is
    interface-compatible with the version that the work was made with.

    c) Accompany the work with a written offer, valid for at
    least three years, to give the same user the materials
    specified in Subsection 6a, above, for a charge no more
    than the cost of performing this distribution.

    d) If distribution of the work is made by offering access to copy
    from a designated place, offer equivalent access to copy the above
    specified materials from the same place.

    e) Verify that the user has already received a copy of these
    materials or that you have already sent this user a copy.

  For an executable, the required form of the "work that uses the
Library" must include any data and utility programs needed for
reproducing the executable from it.  However, as a special exception,
the materials to be distributed need not include anything that is
normally distributed (in either source or binary form) with the major
components (compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself accompanies
the executable.

  It may happen that this requirement contradicts the license
restrictions of other proprietary libraries that do not normally
accompany the operating system.  Such a contradiction means you cannot
use both them and the Library together in an executable that you
distribute.

  7. You may place library facilities that are a work based on the
Library side-by-side in a single library together with other library
facilities not covered by this License, and distribute such a combined
library, provided that the separate distribution of the work based on
the Library and of the other library facilities is otherwise
permitted, and provided that you do these two things:

    a) Accompany the combined library with a copy of the same work
    based on the Library, uncombined with any other library
    facilities.  This must be distributed under the terms of the
    Sections above.

    b) Give prominent notice with the combined library of the fact
    that part of it is a work based on the Library, and explaining
    where to find the accompanying uncombined form of the same work.

  8. You may not copy, modify, sublicense, link with, or distribute
the Library except as expressly provided under this License.  Any
attempt otherwise to copy, modify, sublicense, link with, or
distribute the Library is void, and will automatically terminate your
rights under this License.  However, parties who have received copies,
or rights, from you under this License will not have their licenses
terminated so long as such parties remain in full compliance.

  9. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Library or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Library (or any work based on the
Library), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Library or works based on it.

  10. Each time you redistribute the Library (or any work based on the
Library), the recipient automatically receives a license from the
original licensor to copy, distribute, link with or modify the Library
subject to these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties with
this License.

  11. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Library at all.  For example, if a patent
license would not permit royalty-free redistribution of the Library by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Library.

If any portion of this section is held invalid or unenforceable under any
particular circumstance, the balance of the section is intended to apply,
and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  12. If the distribution and/or use of the Library is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Library under this License may add
an explicit geographical distribution limitation excluding those countries,
so that distribution is permitted only in or among countries not thus
excluded.  In such case, this License incorporates the limitation as if
written in the body of this License.

  13. The Free Software Foundation may publish revised and/or new
versions of the Lesser General Public License from time to time.
Such new versions will be similar in spirit to the present version,
but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number.  If the Library
specifies a version number of this License which applies to it and
"any later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation.  If the Library does not specify a
license version number, you may choose any version ever published by
the Free Software Foundation.

  14. If you wish to incorporate parts of the Library into other free
programs whose distribution conditions are incompatible with these,
write to the author to ask for permission.  For software which is
copyrighted by the Free Software Foundation, write to the Free
Software Foundation; we sometimes make exceptions for this.  Our
decision will be guided by the two goals of preserving the free status
of all derivatives of our free software and of promoting the sharing
and reuse of software generally.

NO WARRANTY

  15. BECAUSE THE LIBRARY IS LICENSED FREE OF CHARGE, THERE IS NO
WARRANTY FOR THE LIBRARY, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE LIBRARY "AS IS" WITHOUT WARRANTY OF ANY
KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
LIBRARY IS WITH YOU.  SHOULD THE LIBRARY PROVE DEFECTIVE, YOU ASSUME
THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN
WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
AND/OR REDISTRIBUTE THE LIBRARY AS PERMITTED ABOVE, BE LIABLE TO YOU
FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
LIBRARY (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A
FAILURE OF THE LIBRARY TO OPERATE WITH ANY OTHER SOFTWARE), EVEN IF
SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.

END OF TERMS AND CONDITIONS
```

Appendix C: The MPL License
---------------------------

```
MOZILLA PUBLIC LICENSE
Version 1.1

1. Definitions.

     1.0.1. "Commercial Use" means distribution or otherwise making the
     Covered Code available to a third party.

     1.1. "Contributor" means each entity that creates or contributes to
     the creation of Modifications.

     1.2. "Contributor Version" means the combination of the Original
     Code, prior Modifications used by a Contributor, and the Modifications
     made by that particular Contributor.

     1.3. "Covered Code" means the Original Code or Modifications or the
     combination of the Original Code and Modifications, in each case
     including portions thereof.

     1.4. "Electronic Distribution Mechanism" means a mechanism generally
     accepted in the software development community for the electronic
     transfer of data.

     1.5. "Executable" means Covered Code in any form other than Source
     Code.

     1.6. "Initial Developer" means the individual or entity identified
     as the Initial Developer in the Source Code notice required by Exhibit
     A.

     1.7. "Larger Work" means a work which combines Covered Code or
     portions thereof with code not governed by the terms of this License.

     1.8. "License" means this document.

     1.8.1. "Licensable" means having the right to grant, to the maximum
     extent possible, whether at the time of the initial grant or
     subsequently acquired, any and all of the rights conveyed herein.

     1.9. "Modifications" means any addition to or deletion from the
     substance or structure of either the Original Code or any previous
     Modifications. When Covered Code is released as a series of files, a
     Modification is:
          A. Any addition to or deletion from the contents of a file
          containing Original Code or previous Modifications.

          B. Any new file that contains any part of the Original Code or
          previous Modifications.

     1.10. "Original Code" means Source Code of computer software code
     which is described in the Source Code notice required by Exhibit A as
     Original Code, and which, at the time of its release under this
     License is not already Covered Code governed by this License.

     1.10.1. "Patent Claims" means any patent claim(s), now owned or
     hereafter acquired, including without limitation,  method, process,
     and apparatus claims, in any patent Licensable by grantor.

     1.11. "Source Code" means the preferred form of the Covered Code for
     making modifications to it, including all modules it contains, plus
     any associated interface definition files, scripts used to control
     compilation and installation of an Executable, or source code
     differential comparisons against either the Original Code or another
     well known, available Covered Code of the Contributor's choice. The
     Source Code can be in a compressed or archival form, provided the
     appropriate decompression or de-archiving software is widely available
     for no charge.

     1.12. "You" (or "Your")  means an individual or a legal entity
     exercising rights under, and complying with all of the terms of, this
     License or a future version of this License issued under Section 6.1.
     For legal entities, "You" includes any entity which controls, is
     controlled by, or is under common control with You. For purposes of
     this definition, "control" means (a) the power, direct or indirect,
     to cause the direction or management of such entity, whether by
     contract or otherwise, or (b) ownership of more than fifty percent
     (50%) of the outstanding shares or beneficial ownership of such
     entity.

2. Source Code License.

     2.1. The Initial Developer Grant.
     The Initial Developer hereby grants You a world-wide, royalty-free,
     non-exclusive license, subject to third party intellectual property
     claims:
          (a)  under intellectual property rights (other than patent or
          trademark) Licensable by Initial Developer to use, reproduce,
          modify, display, perform, sublicense and distribute the Original
          Code (or portions thereof) with or without Modifications, and/or
          as part of a Larger Work; and

          (b) under Patents Claims infringed by the making, using or
          selling of Original Code, to make, have made, use, practice,
          sell, and offer for sale, and/or otherwise dispose of the
          Original Code (or portions thereof).

          (c) the licenses granted in this Section 2.1(a) and (b) are
          effective on the date Initial Developer first distributes
          Original Code under the terms of this License.

          (d) Notwithstanding Section 2.1(b) above, no patent license is
          granted: 1) for code that You delete from the Original Code; 2)
          separate from the Original Code;  or 3) for infringements caused
          by: i) the modification of the Original Code or ii) the
          combination of the Original Code with other software or devices.

     2.2. Contributor Grant.
     Subject to third party intellectual property claims, each Contributor
     hereby grants You a world-wide, royalty-free, non-exclusive license

          (a)  under intellectual property rights (other than patent or
          trademark) Licensable by Contributor, to use, reproduce, modify,
          display, perform, sublicense and distribute the Modifications
          created by such Contributor (or portions thereof) either on an
          unmodified basis, with other Modifications, as Covered Code
          and/or as part of a Larger Work; and

          (b) under Patent Claims infringed by the making, using, or
          selling of  Modifications made by that Contributor either alone
          and/or in combination with its Contributor Version (or portions
          of such combination), to make, use, sell, offer for sale, have
          made, and/or otherwise dispose of: 1) Modifications made by that
          Contributor (or portions thereof); and 2) the combination of
          Modifications made by that Contributor with its Contributor
          Version (or portions of such combination).

          (c) the licenses granted in Sections 2.2(a) and 2.2(b) are
          effective on the date Contributor first makes Commercial Use of
          the Covered Code.

          (d)    Notwithstanding Section 2.2(b) above, no patent license is
          granted: 1) for any code that Contributor has deleted from the
          Contributor Version; 2)  separate from the Contributor Version;
          3)  for infringements caused by: i) third party modifications of
          Contributor Version or ii)  the combination of Modifications made
          by that Contributor with other software  (except as part of the
          Contributor Version) or other devices; or 4) under Patent Claims
          infringed by Covered Code in the absence of Modifications made by
          that Contributor.

3. Distribution Obligations.

     3.1. Application of License.
     The Modifications which You create or to which You contribute are
     governed by the terms of this License, including without limitation
     Section 2.2. The Source Code version of Covered Code may be
     distributed only under the terms of this License or a future version
     of this License released under Section 6.1, and You must include a
     copy of this License with every copy of the Source Code You
     distribute. You may not offer or impose any terms on any Source Code
     version that alters or restricts the applicable version of this
     License or the recipients' rights hereunder. However, You may include
     an additional document offering the additional rights described in
     Section 3.5.

     3.2. Availability of Source Code.
     Any Modification which You create or to which You contribute must be
     made available in Source Code form under the terms of this License
     either on the same media as an Executable version or via an accepted
     Electronic Distribution Mechanism to anyone to whom you made an
     Executable version available; and if made available via Electronic
     Distribution Mechanism, must remain available for at least twelve (12)
     months after the date it initially became available, or at least six
     (6) months after a subsequent version of that particular Modification
     has been made available to such recipients. You are responsible for
     ensuring that the Source Code version remains available even if the
     Electronic Distribution Mechanism is maintained by a third party.

     3.3. Description of Modifications.
     You must cause all Covered Code to which You contribute to contain a
     file documenting the changes You made to create that Covered Code and
     the date of any change. You must include a prominent statement that
     the Modification is derived, directly or indirectly, from Original
     Code provided by the Initial Developer and including the name of the
     Initial Developer in (a) the Source Code, and (b) in any notice in an
     Executable version or related documentation in which You describe the
     origin or ownership of the Covered Code.

     3.4. Intellectual Property Matters
          (a) Third Party Claims.
          If Contributor has knowledge that a license under a third party's
          intellectual property rights is required to exercise the rights
          granted by such Contributor under Sections 2.1 or 2.2,
          Contributor must include a text file with the Source Code
          distribution titled "LEGAL" which describes the claim and the
          party making the claim in sufficient detail that a recipient will
          know whom to contact. If Contributor obtains such knowledge after
          the Modification is made available as described in Section 3.2,
          Contributor shall promptly modify the LEGAL file in all copies
          Contributor makes available thereafter and shall take other steps
          (such as notifying appropriate mailing lists or newsgroups)
          reasonably calculated to inform those who received the Covered
          Code that new knowledge has been obtained.

          (b) Contributor APIs.
          If Contributor's Modifications include an application programming
          interface and Contributor has knowledge of patent licenses which
          are reasonably necessary to implement that API, Contributor must
          also include this information in the LEGAL file.

               (c)    Representations.
          Contributor represents that, except as disclosed pursuant to
          Section 3.4(a) above, Contributor believes that Contributor's
          Modifications are Contributor's original creation(s) and/or
          Contributor has sufficient rights to grant the rights conveyed by
          this License.

     3.5. Required Notices.
     You must duplicate the notice in Exhibit A in each file of the Source
     Code.  If it is not possible to put such notice in a particular Source
     Code file due to its structure, then You must include such notice in a
     location (such as a relevant directory) where a user would be likely
     to look for such a notice.  If You created one or more Modification(s)
     You may add your name as a Contributor to the notice described in
     Exhibit A.  You must also duplicate this License in any documentation
     for the Source Code where You describe recipients' rights or ownership
     rights relating to Covered Code.  You may choose to offer, and to
     charge a fee for, warranty, support, indemnity or liability
     obligations to one or more recipients of Covered Code. However, You
     may do so only on Your own behalf, and not on behalf of the Initial
     Developer or any Contributor. You must make it absolutely clear than
     any such warranty, support, indemnity or liability obligation is
     offered by You alone, and You hereby agree to indemnify the Initial
     Developer and every Contributor for any liability incurred by the
     Initial Developer or such Contributor as a result of warranty,
     support, indemnity or liability terms You offer.

     3.6. Distribution of Executable Versions.
     You may distribute Covered Code in Executable form only if the
     requirements of Section 3.1-3.5 have been met for that Covered Code,
     and if You include a notice stating that the Source Code version of
     the Covered Code is available under the terms of this License,
     including a description of how and where You have fulfilled the
     obligations of Section 3.2. The notice must be conspicuously included
     in any notice in an Executable version, related documentation or
     collateral in which You describe recipients' rights relating to the
     Covered Code. You may distribute the Executable version of Covered
     Code or ownership rights under a license of Your choice, which may
     contain terms different from this License, provided that You are in
     compliance with the terms of this License and that the license for the
     Executable version does not attempt to limit or alter the recipient's
     rights in the Source Code version from the rights set forth in this
     License. If You distribute the Executable version under a different
     license You must make it absolutely clear that any terms which differ
     from this License are offered by You alone, not by the Initial
     Developer or any Contributor. You hereby agree to indemnify the
     Initial Developer and every Contributor for any liability incurred by
     the Initial Developer or such Contributor as a result of any such
     terms You offer.

     3.7. Larger Works.
     You may create a Larger Work by combining Covered Code with other code
     not governed by the terms of this License and distribute the Larger
     Work as a single product. In such a case, You must make sure the
     requirements of this License are fulfilled for the Covered Code.

4. Inability to Comply Due to Statute or Regulation.

     If it is impossible for You to comply with any of the terms of this
     License with respect to some or all of the Covered Code due to
     statute, judicial order, or regulation then You must: (a) comply with
     the terms of this License to the maximum extent possible; and (b)
     describe the limitations and the code they affect. Such description
     must be included in the LEGAL file described in Section 3.4 and must
     be included with all distributions of the Source Code. Except to the
     extent prohibited by statute or regulation, such description must be
     sufficiently detailed for a recipient of ordinary skill to be able to
     understand it.

5. Application of this License.

     This License applies to code to which the Initial Developer has
     attached the notice in Exhibit A and to related Covered Code.

6. Versions of the License.

     6.1. New Versions.
     Netscape Communications Corporation ("Netscape") may publish revised
     and/or new versions of the License from time to time. Each version
     will be given a distinguishing version number.

     6.2. Effect of New Versions.
     Once Covered Code has been published under a particular version of the
     License, You may always continue to use it under the terms of that
     version. You may also choose to use such Covered Code under the terms
     of any subsequent version of the License published by Netscape. No one
     other than Netscape has the right to modify the terms applicable to
     Covered Code created under this License.

     6.3. Derivative Works.
     If You create or use a modified version of this License (which you may
     only do in order to apply it to code which is not already Covered Code
     governed by this License), You must (a) rename Your license so that
     the phrases "Mozilla", "MOZILLAPL", "MOZPL", "Netscape",
     "MPL", "NPL" or any confusingly similar phrase do not appear in your
     license (except to note that your license differs from this License)
     and (b) otherwise make it clear that Your version of the license
     contains terms which differ from the Mozilla Public License and
     Netscape Public License. (Filling in the name of the Initial
     Developer, Original Code or Contributor in the notice described in
     Exhibit A shall not of themselves be deemed to be modifications of
     this License.)

7. DISCLAIMER OF WARRANTY.

     COVERED CODE IS PROVIDED UNDER THIS LICENSE ON AN "AS IS" BASIS,
     WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING,
     WITHOUT LIMITATION, WARRANTIES THAT THE COVERED CODE IS FREE OF
     DEFECTS, MERCHANTABLE, FIT FOR A PARTICULAR PURPOSE OR NON-INFRINGING.
     THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE COVERED CODE
     IS WITH YOU. SHOULD ANY COVERED CODE PROVE DEFECTIVE IN ANY RESPECT,
     YOU (NOT THE INITIAL DEVELOPER OR ANY OTHER CONTRIBUTOR) ASSUME THE
     COST OF ANY NECESSARY SERVICING, REPAIR OR CORRECTION. THIS DISCLAIMER
     OF WARRANTY CONSTITUTES AN ESSENTIAL PART OF THIS LICENSE. NO USE OF
     ANY COVERED CODE IS AUTHORIZED HEREUNDER EXCEPT UNDER THIS DISCLAIMER.

8. TERMINATION.

     8.1.  This License and the rights granted hereunder will terminate
     automatically if You fail to comply with terms herein and fail to cure
     such breach within 30 days of becoming aware of the breach. All
     sublicenses to the Covered Code which are properly granted shall
     survive any termination of this License. Provisions which, by their
     nature, must remain in effect beyond the termination of this License
     shall survive.

     8.2.  If You initiate litigation by asserting a patent infringement
     claim (excluding declatory judgment actions) against Initial Developer
     or a Contributor (the Initial Developer or Contributor against whom
     You file such action is referred to as "Participant")  alleging that:

     (a)  such Participant's Contributor Version directly or indirectly
     infringes any patent, then any and all rights granted by such
     Participant to You under Sections 2.1 and/or 2.2 of this License
     shall, upon 60 days notice from Participant terminate prospectively,
     unless if within 60 days after receipt of notice You either: (i)
     agree in writing to pay Participant a mutually agreeable reasonable
     royalty for Your past and future use of Modifications made by such
     Participant, or (ii) withdraw Your litigation claim with respect to
     the Contributor Version against such Participant.  If within 60 days
     of notice, a reasonable royalty and payment arrangement are not
     mutually agreed upon in writing by the parties or the litigation claim
     is not withdrawn, the rights granted by Participant to You under
     Sections 2.1 and/or 2.2 automatically terminate at the expiration of
     the 60 day notice period specified above.

     (b)  any software, hardware, or device, other than such Participant's
     Contributor Version, directly or indirectly infringes any patent, then
     any rights granted to You by such Participant under Sections 2.1(b)
     and 2.2(b) are revoked effective as of the date You first made, used,
     sold, distributed, or had made, Modifications made by that
     Participant.

     8.3.  If You assert a patent infringement claim against Participant
     alleging that such Participant's Contributor Version directly or
     indirectly infringes any patent where such claim is resolved (such as
     by license or settlement) prior to the initiation of patent
     infringement litigation, then the reasonable value of the licenses
     granted by such Participant under Sections 2.1 or 2.2 shall be taken
     into account in determining the amount or value of any payment or
     license.

     8.4.  In the event of termination under Sections 8.1 or 8.2 above,
     all end user license agreements (excluding distributors and resellers)
     which have been validly granted by You or any distributor hereunder
     prior to termination shall survive termination.

9. LIMITATION OF LIABILITY.

     UNDER NO CIRCUMSTANCES AND UNDER NO LEGAL THEORY, WHETHER TORT
     (INCLUDING NEGLIGENCE), CONTRACT, OR OTHERWISE, SHALL YOU, THE INITIAL
     DEVELOPER, ANY OTHER CONTRIBUTOR, OR ANY DISTRIBUTOR OF COVERED CODE,
     OR ANY SUPPLIER OF ANY OF SUCH PARTIES, BE LIABLE TO ANY PERSON FOR
     ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY
     CHARACTER INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF GOODWILL,
     WORK STOPPAGE, COMPUTER FAILURE OR MALFUNCTION, OR ANY AND ALL OTHER
     COMMERCIAL DAMAGES OR LOSSES, EVEN IF SUCH PARTY SHALL HAVE BEEN
     INFORMED OF THE POSSIBILITY OF SUCH DAMAGES. THIS LIMITATION OF
     LIABILITY SHALL NOT APPLY TO LIABILITY FOR DEATH OR PERSONAL INJURY
     RESULTING FROM SUCH PARTY'S NEGLIGENCE TO THE EXTENT APPLICABLE LAW
     PROHIBITS SUCH LIMITATION. SOME JURISDICTIONS DO NOT ALLOW THE
     EXCLUSION OR LIMITATION OF INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO
     THIS EXCLUSION AND LIMITATION MAY NOT APPLY TO YOU.

10. U.S. GOVERNMENT END USERS.

     The Covered Code is a "commercial item," as that term is defined in
     48 C.F.R. 2.101 (Oct. 1995), consisting of "commercial computer
     software" and "commercial computer software documentation," as such
     terms are used in 48 C.F.R. 12.212 (Sept. 1995). Consistent with 48
     C.F.R. 12.212 and 48 C.F.R. 227.7202-1 through 227.7202-4 (June 1995),
     all U.S. Government End Users acquire Covered Code with only those
     rights set forth herein.

11. MISCELLANEOUS.

     This License represents the complete agreement concerning subject
     matter hereof. If any provision of this License is held to be
     unenforceable, such provision shall be reformed only to the extent
     necessary to make it enforceable. This License shall be governed by
     California law provisions (except to the extent applicable law, if
     any, provides otherwise), excluding its conflict-of-law provisions.
     With respect to disputes in which at least one party is a citizen of,
     or an entity chartered or registered to do business in the United
     States of America, any litigation relating to this License shall be
     subject to the jurisdiction of the Federal Courts of the Northern
     District of California, with venue lying in Santa Clara County,
     California, with the losing party responsible for costs, including
     without limitation, court costs and reasonable attorneys' fees and
     expenses. The application of the United Nations Convention on
     Contracts for the International Sale of Goods is expressly excluded.
     Any law or regulation which provides that the language of a contract
     shall be construed against the drafter shall not apply to this
     License.

12. RESPONSIBILITY FOR CLAIMS.

     As between Initial Developer and the Contributors, each party is
     responsible for claims and damages arising, directly or indirectly,
     out of its utilization of rights under this License and You agree to
     work with Initial Developer and Contributors to distribute such
     responsibility on an equitable basis. Nothing herein is intended or
     shall be deemed to constitute any admission of liability.

13. MULTIPLE-LICENSED CODE.

     Initial Developer may designate portions of the Covered Code as
     "Multiple-Licensed".  "Multiple-Licensed" means that the Initial
     Developer permits you to utilize portions of the Covered Code under
     Your choice of the NPL or the alternative licenses, if any, specified
     by the Initial Developer in the file described in Exhibit A.

EXHIBIT A -Mozilla Public License.

     ``The contents of this file are subject to the Mozilla Public License
     Version 1.1 (the "License"); you may not use this file except in
     compliance with the License. You may obtain a copy of the License at
     http://www.mozilla.org/MPL/

     Software distributed under the License is distributed on an "AS IS"
     basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
     License for the specific language governing rights and limitations
     under the License.

     The Original Code is ______________________________________.

     The Initial Developer of the Original Code is ________________________.
     Portions created by ______________________ are Copyright (C) ______
     _______________________. All Rights Reserved.

     Contributor(s): ______________________________________.

     Alternatively, the contents of this file may be used under the terms
     of the _____ license (the  "[___] License"), in which case the
     provisions of [______] License are applicable instead of those
     above.  If you wish to allow use of your version of this file only
     under the terms of the [____] License and not to allow others to use
     your version of this file under the MPL, indicate your decision by
     deleting  the provisions above and replace  them with the notice and
     other provisions required by the [___] License.  If you do not delete
     the provisions above, a recipient may use your version of this file
     under either the MPL or the [___] License."

     [NOTE: The text of this Exhibit A may differ slightly from the text of
     the notices in the Source Code files of the Original Code. You should
     use the text of this Exhibit A rather than the text found in the
     Original Code Source Code for Your Modifications.]
```

Appendix D: The MIT License
---------------------------

```
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

Appendix E: The SIL Open Font License Version 1.1
---------------------------------------------

```
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
```

Appendix F: The BSD-3 License
-----------------------------

```
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.md or http://ckeditor.com/license

af.js      Found: 62 Missing: 4
ar.js      Found: 51 Missing: 15
bg.js      Found: 58 Missing: 8
bn.js      Found: 40 Missing: 26
bs.js      Found: 29 Missing: 37
ca.js      Found: 61 Missing: 5
cs.js      Found: 66 Missing: 0
cy.js      Found: 66 Missing: 0
da.js      Found: 66 Missing: 0
de.js      Found: 66 Missing: 0
el.js      Found: 59 Missing: 7
en-au.js   Found: 38 Missing: 28
en-ca.js   Found: 37 Missing: 29
en-gb.js   Found: 61 Missing: 5
eo.js      Found: 66 Missing: 0
es.js      Found: 66 Missing: 0
et.js      Found: 66 Missing: 0
eu.js      Found: 48 Missing: 18
fa.js      Found: 66 Missing: 0
fi.js      Found: 66 Missing: 0
fo.js      Found: 66 Missing: 0
fr-ca.js   Found: 42 Missing: 24
fr.js      Found: 66 Missing: 0
gl.js      Found: 40 Missing: 26
gu.js      Found: 66 Missing: 0
he.js      Found: 66 Missing: 0
hi.js      Found: 43 Missing: 23
hr.js      Found: 66 Missing: 0
hu.js      Found: 63 Missing: 3
is.js      Found: 41 Missing: 25
it.js      Found: 66 Missing: 0
ja.js      Found: 62 Missing: 4
ka.js      Found: 62 Missing: 4
km.js      Found: 40 Missing: 26
ko.js      Found: 40 Missing: 26
lt.js      Found: 66 Missing: 0
lv.js      Found: 40 Missing: 26
mk.js      Found: 0 Missing: 66
mn.js      Found: 40 Missing: 26
ms.js      Found: 39 Missing: 27
nb.js      Found: 66 Missing: 0
nl.js      Found: 65 Missing: 1
no.js      Found: 66 Missing: 0
pl.js      Found: 66 Missing: 0
pt-br.js   Found: 66 Missing: 0
pt.js      Found: 52 Missing: 14
ro.js      Found: 61 Missing: 5
ru.js      Found: 66 Missing: 0
sk.js      Found: 49 Missing: 17
sl.js      Found: 48 Missing: 18
sr-latn.js Found: 40 Missing: 26
sr.js      Found: 40 Missing: 26
sv.js      Found: 62 Missing: 4
th.js      Found: 40 Missing: 26
tr.js      Found: 66 Missing: 0
ug.js      Found: 66 Missing: 0
uk.js      Found: 66 Missing: 0
vi.js      Found: 66 Missing: 0
zh-cn.js   Found: 66 Missing: 0
zh.js      Found: 58 Missing: 8
CKEditor Accessibility Checker Changelog
========================================

[CKEditor Accessibility Checker](https://ckeditor.com/ckeditor-4/accessibility-checker/)

Copyright (c) 2014-2018, CKSource - Frederico Knabben. All rights reserved.

## Version 1.1.1

New Features:

* [#240](https://github.com/cksource/ckeditor-plugin-a11ychecker/pull/240): Added Brazilian Portuguese localization. Thanks to [Guilherme Alves](https://github.com/gsag)!
* [#247](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/247): Introduced the `process` event in the `Engine` type, allowing for adding custom issue types.

Fixed Issues:

* [#233](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/233): Fixed: Balloon classes are localized, causing issues of a different testability to look the same.

## Version 1.1.0

New Features:

* [#228](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/228): Added compatibility with the new default `moono-lisa` skin.

Fixed Issues:

* [#201](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/201): `imgShouldNotHaveTitle` Quick Fix - if the image has both `title` and `alt` attributes, the `alt` will be used as the default value.

* [#185](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/185): Added a more verbose error message when jQuery is missing in the built version of .
* [#185](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/185): Added a more verbose error message when jQuery is missing in the built version of Accessibility Checker.

## Version 1.0

A brand new CKEditor plugin that lets you inspect accessibility level of content created in CKEditor and immediately solve any issues that are found. For an overview of its features, see the [Accessibility Checker website](https://ckeditor.com/ckeditor-4/accessibility-checker/).

It is built upon three key elements:

* User Interface optimized for quick problem solving.
* Flexibility allowing you to use the accessibility checking engine of your choice (default: [Quail](http://quailjs.org/)).
* Quick Fix feature letting you fix common problems fully automatically!

All of this comes bundled with a tight integration with CKEditor.

The first release includes three language versions:

* English
* German (provided by Sebastian Peilicke of [Sopra Steria GmbH](http://www.soprasteria.de/de))
* Dutch (provided by [Dutch Government](https://www.government.nl/))
Software License Agreement
==========================

CKEditor Accessibility Checker Plugin
Copyright (c) 2014-2018, CKSource - Frederico Knabben. All rights reserved.

License under the terms of the GNU General Public License Version 2 or later (the "GPL") (Appendix A).

This license is not valid for integration within commercial
applications or applications whose license is not compatible
with the GPL.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Sources of Intellectual Property Included
-----------------------------------------

Where not otherwise indicated, all program code is authored by
CKSource engineers and consists of CKSource-owned intellectual
property. In some specific instances, the program will incorporate work
done by developers outside of CKSource with their express permission.

Third-party software included:

- QUAIL, Copyright (c) 2013 Kevin Miller (libs/quail)<br>
  https://github.com/quailjs/quail<br>
  License under the terms of the MIT license.
 

Parts of code taken from the following libraries are included in CKEditor Accessibility Checker:

- CKEditor, Copyright (c) 2003 CKSource - Frederico Knabben (quickfix/TableHeaders.js)<br>
  https://ckeditor.com/<br>
  License under the terms of the GNU General Public License Version 2 license.

Trademarks
----------

CKEditor, CKEditor Accessibility Checker and CKEditor A11y Checker are
trademarks of CKSource - Frederico Knabben. All other brand and product names
are trademarks, registered trademarks or service marks of their respective
holders.

---

Appendix A: The GPL License
---------------------------

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
software-to make sure the software is free for all its users.  This
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
Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.md or http://ckeditor.com/license

cs.js      Found: 30 Missing: 0
cy.js      Found: 30 Missing: 0
da.js      Found: 12 Missing: 18
de.js      Found: 30 Missing: 0
el.js      Found: 25 Missing: 5
eo.js      Found: 30 Missing: 0
fa.js      Found: 30 Missing: 0
fi.js      Found: 30 Missing: 0
fr.js      Found: 30 Missing: 0
gu.js      Found: 12 Missing: 18
he.js      Found: 30 Missing: 0
it.js      Found: 30 Missing: 0
mk.js      Found: 5 Missing: 25
nb.js      Found: 30 Missing: 0
nl.js      Found: 30 Missing: 0
no.js      Found: 30 Missing: 0
pt-br.js   Found: 30 Missing: 0
ro.js      Found: 6 Missing: 24
tr.js      Found: 30 Missing: 0
ug.js      Found: 27 Missing: 3
vi.js      Found: 6 Missing: 24
zh-cn.js   Found: 30 Missing: 0
This project is free software released under the MIT/X11 license:

Copyright (C) 2014 Piotr Koszulinski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
SCAYT plugin for CKEditor 4 Changelog
====================
### CKEditor 4.5.6

New Features:
* CKEditor [language addon](http://ckeditor.com/addon/language) support
* CKEditor [placeholder addon](http://ckeditor.com/addon/placeholder) support
* Drag and Drop support
* *Experimental* GRAYT functionality http://www.webspellchecker.net/samples/scayt-ckeditor-plugin.html#25

Fixed issues:
* [#98](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/98) SCAYT Affects Dialog Double Click. Fixed in SCAYT Core.
* [#102](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/102) SCAYT Core performance enhancements
* [#104](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/104) SCAYT's spans leak into the clipboard and after pasting
* [#105](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/105) Javascript error fired in case of multiple instances of CKEditor in one page
* [#107](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/107) SCAYT should not check non-editable parts of content
* [#108](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/108) Latest SCAYT copies id of editor element to the iframe
* SCAYT stops working when CKEditor Undo plug-in not enabled
* Issue with pasting SCAYT markup in CKEditor
* [#32](https://github.com/WebSpellChecker/ckeditor-plugin-wsc/issues/32) SCAYT stops working after pressing Cancel button in WSC dialog
Software License Agreement
==========================

**CKEditor SCAYT Plugin**
Copyright &copy; 2012, [CKSource](http://cksource.com) - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your choice:

*   GNU General Public License Version 2 or later (the "GPL"):
    http://www.gnu.org/licenses/gpl.html

*   GNU Lesser General Public License Version 2.1 or later (the "LGPL"):
    http://www.gnu.org/licenses/lgpl.html

*   Mozilla Public License Version 1.1 or later (the "MPL"):
    http://www.mozilla.org/MPL/MPL-1.1.html

You are not required to, but if you want to explicitly declare the license you have chosen to be bound to when using, reproducing, modifying and distributing this software, just include a text file titled "legal.txt" in your version of this software, indicating your license choice.

Sources of Intellectual Property Included in this plugin
--------------------------------------------------------

Where not otherwise indicated, all plugin content is authored by CKSource engineers and consists of CKSource-owned intellectual property. In some specific instances, the plugin will incorporate work done by developers outside of CKSource with their express permission.

Trademarks
----------

CKEditor is a trademark of CKSource - Frederico Knabben. All other brand and product names are trademarks, registered trademarks or service marks of their respective holders.
Software License Agreement
==========================

**CKEditor WSC Plugin**
Copyright &copy; 2012, [CKSource](http://cksource.com) - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your choice:

*   GNU General Public License Version 2 or later (the "GPL"):
    http://www.gnu.org/licenses/gpl.html

*   GNU Lesser General Public License Version 2.1 or later (the "LGPL"):
    http://www.gnu.org/licenses/lgpl.html

*   Mozilla Public License Version 1.1 or later (the "MPL"):
    http://www.mozilla.org/MPL/MPL-1.1.html

You are not required to, but if you want to explicitly declare the license you have chosen to be bound to when using, reproducing, modifying and distributing this software, just include a text file titled "legal.txt" in your version of this software, indicating your license choice.

Sources of Intellectual Property Included in this plugin
--------------------------------------------------------

Where not otherwise indicated, all plugin content is authored by CKSource engineers and consists of CKSource-owned intellectual property. In some specific instances, the plugin will incorporate work done by developers outside of CKSource with their express permission.

Trademarks
----------

CKEditor is a trademark of CKSource - Frederico Knabben. All other brand and product names are trademarks, registered trademarks or service marks of their respective holders.
Font license info


## Font Awesome

   Copyright (C) 2012 by Dave Gandy

   Author:    Dave Gandy
   License:   SIL ()
   Homepage:  http://fortawesome.github.com/Font-Awesome/
Copyright (C) 2014 by Marijn Haverbeke <marijnh@gmail.com> and others

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"Moono" Skin
====================

This skin has been chosen for the **default skin** of CKEditor 4.x, elected from the CKEditor
[skin contest](http://ckeditor.com/blog/new_ckeditor_4_skin) and further shaped by
the CKEditor team. "Moono" is maintained by the core developers.

For more information about skins, please check the [CKEditor Skin SDK](http://docs.cksource.com/CKEditor_4.x/Skin_SDK)
documentation.

Features
-------------------
"Moono" is a monochromatic skin, which offers a modern look coupled with gradients and transparency.
It comes with the following features:

- Chameleon feature with brightness,
- high-contrast compatibility,
- graphics source provided in SVG.

Directory Structure
-------------------

CSS parts:
- **editor.css**: the main CSS file. It's simply loading several other files, for easier maintenance,
- **mainui.css**: the file contains styles of entire editor outline structures,
- **toolbar.css**: the file contains styles of the editor toolbar space (top),
- **richcombo.css**: the file contains styles of the rich combo ui elements on toolbar,
- **panel.css**: the file contains styles of the rich combo drop-down, it's not loaded
until the first panel open up,
- **elementspath.css**: the file contains styles of the editor elements path bar (bottom),
- **menu.css**: the file contains styles of all editor menus including context menu and button drop-down,
it's not loaded until the first menu open up,
- **dialog.css**: the CSS files for the dialog UI, it's not loaded until the first dialog open,
- **reset.css**: the file defines the basis of style resets among all editor UI spaces,
- **preset.css**: the file defines the default styles of some UI elements reflecting the skin preference,
- **editor_XYZ.css** and **dialog_XYZ.css**: browser specific CSS hacks.

Other parts:
- **skin.js**: the only JavaScript part of the skin that registers the skin, its browser specific files and its icons and defines the Chameleon feature,
- **icons/**: contains all skin defined icons,
- **images/**: contains a fill general used images,
- **dev/**: contains SVG source of the skin icons.

License
-------

Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.

For licensing, see LICENSE.md or [http://ckeditor.com/license](http://ckeditor.com/license)
CKEditor Accessibility Checker Changelog
========================================

[CKEditor Accessibility Checker](https://ckeditor.com/ckeditor-4/accessibility-checker/)

Copyright (c) 2014-2018, CKSource - Frederico Knabben. All rights reserved.

## Version 1.1.1

New Features:

* [#240](https://github.com/cksource/ckeditor-plugin-a11ychecker/pull/240): Added Brazilian Portuguese localization. Thanks to [Guilherme Alves](https://github.com/gsag)!
* [#247](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/247): Introduced the `process` event in the `Engine` type, allowing for adding custom issue types.

Fixed Issues:

* [#233](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/233): Fixed: Balloon classes are localized, causing issues of a different testability to look the same.

## Version 1.1.0

New Features:

* [#228](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/228): Added compatibility with the new default `moono-lisa` skin.

Fixed Issues:

* [#201](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/201): `imgShouldNotHaveTitle` Quick Fix - if the image has both `title` and `alt` attributes, the `alt` will be used as the default value.

* [#185](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/185): Added a more verbose error message when jQuery is missing in the built version of .
* [#185](https://github.com/cksource/ckeditor-plugin-a11ychecker/issues/185): Added a more verbose error message when jQuery is missing in the built version of Accessibility Checker.

## Version 1.0

A brand new CKEditor plugin that lets you inspect accessibility level of content created in CKEditor and immediately solve any issues that are found. For an overview of its features, see the [Accessibility Checker website](https://ckeditor.com/ckeditor-4/accessibility-checker/).

It is built upon three key elements:

* User Interface optimized for quick problem solving.
* Flexibility allowing you to use the accessibility checking engine of your choice (default: [Quail](http://quailjs.org/)).
* Quick Fix feature letting you fix common problems fully automatically!

All of this comes bundled with a tight integration with CKEditor.

The first release includes three language versions:

* English
* German (provided by Sebastian Peilicke of [Sopra Steria GmbH](http://www.soprasteria.de/de))
* Dutch (provided by [Dutch Government](https://www.government.nl/))
Software License Agreement
==========================

CKEditor Accessibility Checker Plugin
Copyright (c) 2014-2018, CKSource - Frederico Knabben. All rights reserved.

License under the terms of the GNU General Public License Version 2 or later (the "GPL") (Appendix A).

This license is not valid for integration within commercial
applications or applications whose license is not compatible
with the GPL.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Sources of Intellectual Property Included
-----------------------------------------

Where not otherwise indicated, all program code is authored by
CKSource engineers and consists of CKSource-owned intellectual
property. In some specific instances, the program will incorporate work
done by developers outside of CKSource with their express permission.

Third-party software included:

- QUAIL, Copyright (c) 2013 Kevin Miller (libs/quail)<br>
  https://github.com/quailjs/quail<br>
  License under the terms of the MIT license.
 

Parts of code taken from the following libraries are included in CKEditor Accessibility Checker:

- CKEditor, Copyright (c) 2003 CKSource - Frederico Knabben (quickfix/TableHeaders.js)<br>
  https://ckeditor.com/<br>
  License under the terms of the GNU General Public License Version 2 license.

Trademarks
----------

CKEditor, CKEditor Accessibility Checker and CKEditor A11y Checker are
trademarks of CKSource - Frederico Knabben. All other brand and product names
are trademarks, registered trademarks or service marks of their respective
holders.

---

Appendix A: The GPL License
---------------------------

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
software-to make sure the software is free for all its users.  This
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
CKEditor Accessibility Checker
==================================================

# Overview

This package contains the distribution version of Accessibility Checker.

## Requirements

* CKEditor **4.3.0** or later.
* [Balloon Panel](https://ckeditor.com/cke4/addon/balloonpanel) plugin for CKEditor.
* jQuery **1.x** or later in order to run [Quail](http://quailjs.org/).

## Browser Support

Accessibility Checker has [the same browser compatibility as CKEditor](https://docs.ckeditor.com/ckeditor4/latest/guide/dev_browsers.html), with the following exceptions:

* Internet Explorer 8 is not supported.
* Internet Explorer 9 Quirks Mode is not supported.

## Installation

The recommended way to install Accessibility Checker is through [online builder](https://ckeditor.com/cke4/builder).

Select Accessibility Checker from the list of Available Plugins and add it to your editor build - CKBuilder will automatically resolve the dependencies for you and include all necessary plugins in your configuration.

### Limitations

**Running on local filesystem:** You cannot run Accessibility Checker on a local filesystem, since Quail uses an `XMLHttpRequest` for fetching its resources. This is not allowed when working with the `file://` scheme.

## License

Copyright (c) 2014-2018, CKSource - Frederico Knabben. All rights reserved.<br>
Licensed under the terms of the [GNU General Public License Version 2 or later (the "GPL")](http://www.gnu.org/licenses/gpl.html).

See LICENSE.md for more information.
This project is free software released under the MIT/X11 license:

Copyright (C) 2014 Piotr Koszulinski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.


Youtube Plugin for CKEditor 4
=============================

Copyright © 2013 Jonnas Fonini <contato@fonini.net>.
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.

This plugin allow you to insert Youtube videos using embed code or just the video URL.

## Installation

Follow these steps:

 1. Download the latest version of the plugin from Github.
 2. Extract the downloaded file into the CKEditor's **plugins** folder.
 3. Enable the plugin by changing or adding the extraPlugins line in your configuration (config.js):

config.extraPlugins = 'youtube';

## How to use
If everything is ok, a Youtube icon should appear on the CKEditor toolbar. Click it,
paste your embed code or video URL and the video will be inserted.


[![Licensed under the WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png "Licensed under the WTFPL")](http://www.wtfpl.net)
SCAYT plugin for CKEditor 4 Changelog
====================
### CKEditor 4.5.6

New Features:
* CKEditor [language addon](http://ckeditor.com/addon/language) support
* CKEditor [placeholder addon](http://ckeditor.com/addon/placeholder) support
* Drag and Drop support
* *Experimental* GRAYT functionality http://www.webspellchecker.net/samples/scayt-ckeditor-plugin.html#25

Fixed issues:
* [#98](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/98) SCAYT Affects Dialog Double Click. Fixed in SCAYT Core.
* [#102](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/102) SCAYT Core performance enhancements
* [#104](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/104) SCAYT's spans leak into the clipboard and after pasting
* [#105](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/105) Javascript error fired in case of multiple instances of CKEditor in one page
* [#107](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/107) SCAYT should not check non-editable parts of content
* [#108](https://github.com/WebSpellChecker/ckeditor-plugin-scayt/issues/108) Latest SCAYT copies id of editor element to the iframe
* SCAYT stops working when CKEditor Undo plug-in not enabled
* Issue with pasting SCAYT markup in CKEditor
* [#32](https://github.com/WebSpellChecker/ckeditor-plugin-wsc/issues/32) SCAYT stops working after pressing Cancel button in WSC dialog
Software License Agreement
==========================

**CKEditor SCAYT Plugin**
Copyright &copy; 2012, [CKSource](http://cksource.com) - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your choice:

*   GNU General Public License Version 2 or later (the "GPL"):
    http://www.gnu.org/licenses/gpl.html

*   GNU Lesser General Public License Version 2.1 or later (the "LGPL"):
    http://www.gnu.org/licenses/lgpl.html

*   Mozilla Public License Version 1.1 or later (the "MPL"):
    http://www.mozilla.org/MPL/MPL-1.1.html

You are not required to, but if you want to explicitly declare the license you have chosen to be bound to when using, reproducing, modifying and distributing this software, just include a text file titled "legal.txt" in your version of this software, indicating your license choice.

Sources of Intellectual Property Included in this plugin
--------------------------------------------------------

Where not otherwise indicated, all plugin content is authored by CKSource engineers and consists of CKSource-owned intellectual property. In some specific instances, the plugin will incorporate work done by developers outside of CKSource with their express permission.

Trademarks
----------

CKEditor is a trademark of CKSource - Frederico Knabben. All other brand and product names are trademarks, registered trademarks or service marks of their respective holders.
CKEditor SCAYT Plugin
=====================

This plugin brings Spell Check As You Type (SCAYT) into up to CKEditor 4+.

SCAYT is a "installation-less", using the web-services of [WebSpellChecker.net](http://www.webspellchecker.net/). It's an out of the box solution.

Installation
------------

1. Clone/copy this repository contents in a new "plugins/scayt" folder in your CKEditor installation.
2. Enable the "scayt" plugin in the CKEditor configuration file (config.js):

        config.extraPlugins = 'scayt';

That's all. SCAYT will appear on the editor toolbar and will be ready to use.

License
-------

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.

Developed in cooperation with [WebSpellChecker.net](http://www.webspellchecker.net/).
CKEditor-WordCount-Plugin
=========================

WordCount Plugin for CKEditor v4 (or above) that counts the words/characters an shows the word count and/or char count in the footer of the editor.

![Screenshot]
(http://www.watchersnet.de/Portals/0/screenshots/dnn/CKEditorWordCountPlugin.png)

####Demo

http://w8tcha.github.com/CKEditor-WordCount-Plugin/

DISCLAIMER: This is a forked Version, i can not find the original Author anymore if anyone knows the original Author please contact me and i can include the Author in the Copyright Notices. 

####License

Licensed under the terms of the MIT License.

####Installation

 If building a new editor using the CKBuilder from http://ckeditor.com/, there is no need to follow numbers steps below. If adding the Word Count & Char Count plugin to an already established CKEditor, follow the numbered steps below.

1.	Download the Word Count &  Char Count plugin from http://ckeditor.com/addon/wordcount or https://github.com/w8tcha/CKEditor-WordCount-Plugin. This will download a folder named **wordcount_*version*.zip** or **CKEditor-WordCount-Plugin-master.zip** to your Downloads folder.
2.	Download the Notification plugin from http://ckeditor.com/addon/notification. This will download a folder named **notification_*version*.zip** to your Downloads folder.
3.	Extract the .zip folders for both the Word Count & Char Count and Notification plugin. After extraction, you should have a folder named **wordcount** and a folder named **notification**.
4.	Move the wordcount folder to /web/server/root/ckeditor/plugins/.  Move the notification folder to /web/server/root/ckeditor/plugins/.
5.	Add the following line of text to the config.js file, which is located at /web/server/root/ckeditor/.

```javascript
config.extraPlugins = 'wordcount,notification'; 
```

Below is an example of what your config.js file might look like after adding config.extraPlugins = 'wordcount,notification';

```javascript
CKEDITOR.editorConfig = function( config ) {
  config.extraPlugins = 'wordcount,notification';
  config.toolbar [
  et cetera . . .
  ];
};
```

There now should be text in the bottom right-hand corner of your CKEditor which counts the number of Paragraphs and number of Words in your CKEditor.

![plugin example](http://www.trojanbot.com/uploads/ckeditor_paragraph_words.png)

To modify the behavior of the Word Count & Char Count text at the bottom right-hand corner of your CKEditor, add the following text to your config.js file located at /web/server/root/ckeditor/config.js.

````js
config.wordcount = {

    // Whether or not you want to show the Paragraphs Count
    showParagraphs: true,

    // Whether or not you want to show the Word Count
    showWordCount: true,

    // Whether or not you want to show the Char Count
    showCharCount: false,

    // Whether or not you want to count Spaces as Chars
    countSpacesAsChars: false,

    // Whether or not to include Html chars in the Char Count
    countHTML: false,
    
    // Maximum allowed Word Count, -1 is default for unlimited
    maxWordCount: -1,

    // Maximum allowed Char Count, -1 is default for unlimited
    maxCharCount: -1,

    // How long to show the 'paste' warning, 0 is default for not auto-closing the notification
    pasteWarningDuration: 0,
    

    // Add filter to add or remove element before counting (see CKEDITOR.htmlParser.filter), Default value : null (no filter)
    filter: new CKEDITOR.htmlParser.filter({
        elements: {
            div: function( element ) {
                if(element.attributes.class == 'mediaembed') {
                    return false;
                }
            }
        }
    })
};
````

**Note:** If you plan to change some of the JavaScript, you probably will not want to use the CKBuilder, because this will place the JavaScript of the Word Count & Char Count plugin in the ckeditor.js file located at /web/server/root/ckeditor/ckeditor.js. The JavaScript for the Word Count & Char Count plugin in the ckeditor.js file is different than the JavaScript used when manually adding the Word Count & Char Count plugin.  When manually adding the Word Count & Char Count plugin, the JavaScript will be in the plugin.js file located at 

Software License Agreement
==========================

**CKEditor WSC Plugin**
Copyright &copy; 2012, [CKSource](http://cksource.com) - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your choice:

*   GNU General Public License Version 2 or later (the "GPL"):
    http://www.gnu.org/licenses/gpl.html

*   GNU Lesser General Public License Version 2.1 or later (the "LGPL"):
    http://www.gnu.org/licenses/lgpl.html

*   Mozilla Public License Version 1.1 or later (the "MPL"):
    http://www.mozilla.org/MPL/MPL-1.1.html

You are not required to, but if you want to explicitly declare the license you have chosen to be bound to when using, reproducing, modifying and distributing this software, just include a text file titled "legal.txt" in your version of this software, indicating your license choice.

Sources of Intellectual Property Included in this plugin
--------------------------------------------------------

Where not otherwise indicated, all plugin content is authored by CKSource engineers and consists of CKSource-owned intellectual property. In some specific instances, the plugin will incorporate work done by developers outside of CKSource with their express permission.

Trademarks
----------

CKEditor is a trademark of CKSource - Frederico Knabben. All other brand and product names are trademarks, registered trademarks or service marks of their respective holders.
CKEditor WebSpellChecker Plugin
===============================

This plugin brings Web Spell Checker (WSC) into CKEditor.

WSC is "installation-less", using the web-services of [WebSpellChecker.net](http://www.webspellchecker.net/). It's an out of the box solution.

Installation
------------

1. Clone/copy this repository contents in a new "plugins/wsc" folder in your CKEditor installation.
2. Enable the "wsc" plugin in the CKEditor configuration file (config.js):

        config.extraPlugins = 'wsc';

That's all. WSC will appear on the editor toolbar and will be ready to use.

License
-------

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.

Developed in cooperation with [WebSpellChecker.net](http://www.webspellchecker.net/).
These assets are referenced by the MDN10 zone CSS.
These files are no longer served by developer.mozilla.org.

Subsets of the ZillaSlab fonts are served by MDN. These were created as
documented in ``latin-subset``.

mplus-2c-light-fulah-subset.woff appears to be an unused font for the
"ff" (Fulah) locale.
Retired Promos
==============
Assets from old promotions. We're often asked to run these again.

* `fx-dev-2018` - Firefox Developer Edition
  ([bug 1482538](https://bugzilla.mozilla.org/show_bug.cgi?id=1482538))
* `saucelabs-2017` - SauceLabs cross-browser testing
  ([bug 1330094](https://bugzilla.mozilla.org/show_bug.cgi?id=1330094))
kuma
----
The kuma Docker image builds on the kuma_base image, installing a kuma branch
and building the assets needed for running as a webservice.  The environment
can be customized for different deployments.

The image can be recreated locally with ``make build-kuma``.

The image tagged ``latest`` is used by default for development. It can be
created locally with ``make build-kuma VERSION=latest``. The official latest
image is created from the master branch in Jenkins__ and published to
DockerHub__.

.. __: https://ci.us-west-2.mdn.mozit.cloud/blue/organizations/jenkins/kuma/branches/
.. __: https://hub.docker.com/r/mdnwebdocs/kuma/
kuma_base
---------
The kuma_base Docker image contains the OS and libraries (C, Python, and
Node.js) that support the kuma project.  The kuma image extends this by
installing the kuma source and building assets needed for production.

The image can be recreated locally with ``make build-base``.

The image tagged ``latest`` is used by default for development. It can be
created locally with ``make build-base VERSION=latest``. The official
latest image is created from the master branch in Jenkins__ and published to
DockerHub__

.. __: https://ci.us-west-2.mdn.mozit.cloud/blue/organizations/jenkins/kuma/branches/
.. __: https://hub.docker.com/r/mdnwebdocs/kuma_base/
# This is a standalone requirements file for the documentation requirements
# used by ReadTheDocs to set up the documentation rendering environment

# These should stay synced with other requirements files
Babel==2.2.0
docutils==0.12
Jinja2==2.10.1
MarkupSafe==0.23
pytz==2018.5

# These requirements are unique to docs
Pygments==2.1.1
Sphinx==1.3.5
snowballstemmer==1.2.1
This folder will contain self-signed certificates for testing SSL.
# Needs to exist so we don't have outstanding migrations for
# django-soapbox.
# See https://github.com/ubernostrum/django-soapbox/issues/5
Authors ordered by first contribution
A list of current team members is available at http://jqueryui.com/about

Paul Bakaus <paul.bakaus@googlemail.com>
Richard Worth <rdworth@gmail.com>
Yehuda Katz <wycats@gmail.com>
Sean Catchpole <sean@sunsean.com>
John Resig <jeresig@gmail.com>
Tane Piper <piper.tane@gmail.com>
Dmitri Gaskin <dmitrig01@gmail.com>
Klaus Hartl <klaus.hartl@googlemail.com>
Stefan Petre <stefan.petre@gmail.com>
Gilles van den Hoven <gilles@webunity.nl>
Micheil Bryan Smith <micheil@brandedcode.com>
Jörn Zaefferer <joern.zaefferer@gmail.com>
Marc Grabanski <m@marcgrabanski.com>
Keith Wood <kbwood.au@gmail.com>
Brandon Aaron <brandon.aaron@gmail.com>
Scott González <scott.gonzalez@gmail.com>
Eduardo Lundgren <eduardolundgren@gmail.com>
Aaron Eisenberger <aaronchi@gmail.com>
Joan Piedra <theneojp@gmail.com>
Bruno Basto <b.basto@gmail.com>
Remy Sharp <remy@leftlogic.com>
Bohdan Ganicky <bohdan.ganicky@gmail.com>
David Bolter <david.bolter@gmail.com>
Chi Cheng <cloudream@gmail.com>
Ca-Phun Ung <pazu2k@gmail.com>
Ariel Flesler <aflesler@gmail.com>
Maggie Costello Wachs <fg.maggie@gmail.com>
Scott Jehl <scott@scottjehl.com>
Todd Parker <fg.todd@gmail.com>
Andrew Powell <powella@gmail.com>
Brant Burnett <btburnett3@gmail.com>
Douglas Neiner <doug@pixelgraphics.us>
Paul Irish <paul.irish@gmail.com>
Ralph Whitbeck <ralph.whitbeck@gmail.com>
Thibault Duplessis <thibault.duplessis@gmail.com>
Dominique Vincent <dominique.vincent@toitl.com>
Jack Hsu <jack.hsu@gmail.com>
Adam Sontag <ajpiano@ajpiano.com>
Carl Fürstenberg <carl@excito.com>
Kevin Dalman <development@allpro.net>
Alberto Fernández Capel <afcapel@gmail.com>
Jacek Jędrzejewski (http://jacek.jedrzejewski.name)
Ting Kuei <ting@kuei.com>
Samuel Cormier-Iijima <sam@chide.it>
Jon Palmer <jonspalmer@gmail.com>
Ben Hollis <bhollis@amazon.com>
Justin MacCarthy <Justin@Rubystars.biz>
Eyal Kobrigo <kobrigo@hotmail.com>
Tiago Freire <tiago.freire@gmail.com>
Diego Tres <diegotres@gmail.com>
Holger Rüprich <holger@rueprich.de>
Ziling Zhao <zizhao@cisco.com>
Mike Alsup <malsup@gmail.com>
Robson Braga Araujo <robsonbraga@gmail.com>
Pierre-Henri Ausseil <ph.ausseil@gmail.com>
Christopher McCulloh <cmcculloh@gmail.com>
Andrew Newcomb <ext.github@preceptsoftware.co.uk>
Lim Chee Aun <cheeaun@gmail.com>
Jorge Barreiro <yortx.barry@gmail.com>
Daniel Steigerwald <daniel@steigerwald.cz>
John Firebaugh <john_firebaugh@bigfix.com>
John Enters <github@darkdark.net>
Andrey Kapitcyn <ru.m157y@gmail.com>
Dmitry Petrov <dpetroff@gmail.com>
Eric Hynds <eric@hynds.net>
Chairat Sunthornwiphat <pipo@sixhead.com>
Josh Varner <josh.varner@gmail.com>
Stéphane Raimbault <stephane.raimbault@gmail.com>
Jay Merrifield <fracmak@gmail.com>
J. Ryan Stinnett <jryans@gmail.com>
Peter Heiberg <peter@heiberg.se>
Alex Dovenmuehle <adovenmuehle@gmail.com>
Jamie Gegerson <git@jamiegegerson.com>
Raymond Schwartz <skeetergraphics@gmail.com>
Phillip Barnes <philbar@gmail.com>
Kyle Wilkinson <kai@wikyd.org>
Khaled AlHourani <me@khaledalhourani.com>
Marian Rudzynski <mr@impaled.org>
Jean-Francois Remy <jfremy@virtuoz.com>
Doug Blood <dougblood@gmail.com>
Filippo Cavallarin <filippo.cavallarin@codseq.it>
Heiko Henning <h.henning@educa.ch>
Aliaksandr Rahalevich <saksmlz@gmail.com>
Mario Visic <mario@mariovisic.com>
Xavi Ramirez <xavi.rmz@gmail.com>
Max Schnur <max.schnur@gmail.com>
Saji Nediyanchath <saji89@gmail.com>
Corey Frang <gnarf@gnarf.net>
Aaron Peterson <aaronp123@yahoo.com>
Ivan Peters <ivan@ivanpeters.com>
Mohamed Cherif Bouchelaghem <cherifbouchelaghem@yahoo.fr>
Marcos Sousa <falecomigo@marcossousa.com>
Michael DellaNoce <mdellanoce@mailtrust.com>
George Marshall <echosx@gmail.com>
Tobias Brunner <tobias@strongswan.org>
Martin Solli <msolli@gmail.com>
David Petersen <public@petersendidit.com>
Dan Heberden <danheberden@gmail.com>
William Kevin Manire <williamkmanire@gmail.com>
Gilmore Davidson <gilmoreorless@gmail.com>
Michael Wu <michaelmwu@gmail.com>
Adam Parod <mystic414@gmail.com>
Guillaume Gautreau <guillaume+github@ghusse.com>
Marcel Toele <EleotleCram@gmail.com>
Dan Streetman <ddstreet@ieee.org>
Matt Hoskins <furlined@cat-basket.org>
Giovanni Giacobbi <giovanni@giacobbi.net>
Kyle Florence <kyle.florence@gmail.com>
Pavol Hluchý <lopo@losys.sk>
Hans Hillen <hans.hillen@gmail.com>
Mark Johnson <virgofx@live.com>
Trey Hunner <treyhunner@gmail.com>
Shane Whittet <whittet@gmail.com>
Edward A Faulkner <ef@alum.mit.edu>
Adam Baratz <adam@adambaratz.com>
Kato Kazuyoshi <kato.kazuyoshi@gmail.com>
Eike Send <eike.send@gmail.com>
Kris Borchers <kris.borchers@gmail.com>
Eddie Monge <eddie@eddiemonge.com>
Israel Tsadok <itsadok@gmail.com>
Carson McDonald <carson@ioncannon.net>
Jason Davies <jason@jasondavies.com>
Garrison Locke <gplocke@gmail.com>
David Murdoch <musicisair@yahoo.com>
Benjamin Scott Boyle <benjamins.boyle@gmail.com>
Jesse Baird <jebaird@gmail.com>
Jonathan Vingiano <jvingiano@gmail.com>
Dylan Just <dev@ephox.com>
Hiroshi Tomita <tomykaira@gmail.com>
Glenn Goodrich <glenn.goodrich@gmail.com>
Tarafder Ashek-E-Elahi <mail.ashek@gmail.com>
Ryan Neufeld <ryan@neufeldmail.com>
Marc Neuwirth <marc.neuwirth@gmail.com>
Philip Graham <philip.robert.graham@gmail.com>
Benjamin Sterling <benjamin.sterling@kenzomedia.com>
Wesley Walser <waw325@gmail.com>
Kouhei Sutou <kou@clear-code.com>
Karl Kirch <karlkrch@gmail.com>
Chris Kelly <ckdake@ckdake.com>
Jay Oster <jay@loyalize.com>
Alexander Polomoshnov <alex.polomoshnov@gmail.com>
David Leal <dgleal@gmail.com>
Igor Milla <igor.fsp.milla@gmail.com>
Dave Methvin <dave.methvin@gmail.com>
Florian Gutmann <f.gutmann@chronimo.com>
Marwan Al Jubeh <marwan.aljubeh@gmail.com>
Milan Broum <midlis@googlemail.com>
Sebastian Sauer <info@dynpages.de>
Gaëtan Muller <m.gaetan89@gmail.com>
Michel Weimerskirch <michel@weimerskirch.net>
William Griffiths <william@ycymro.com>
Stojce Slavkovski <stojce@gmail.com>
David Soms <david.soms@gmail.com>
David De Sloovere <david.desloovere@hotmail.com>
Michael P. Jung <michael.jung@terreon.de>
Shannon Pekary <spekary@gmail.com>
Matthew Edward Hutton <meh@corefiling.co.uk>
James Khoury <james@jameskhoury.com>
Rob Loach <robloach@gmail.com>
Alberto Monteiro <betimbrasil@gmail.com>
Alex Rhea <alex.rhea@gmail.com>
Krzysztof Rosiński <rozwell69@gmail.com>
Ryan Olton <oltonr@gmail.com>
Genie <386@mail.com>
Rick Waldron <waldron.rick@gmail.com>
Ian Simpson <spoonlikesham@gmail.com>
Lev Kitsis <spam4lev@gmail.com>
TJ VanToll <tj.vantoll@gmail.com>
Justin Domnitz <jdomnitz@gmail.com>
Douglas Cerna <douglascerna@yahoo.com>
Bert ter Heide <bertjh@hotmail.com>
Jasvir Nagra <jasvir@gmail.com>
Petr Hromadko <yuriy@tokyoscale.com>
Harri Kilpiö <harri.kilpio@gmail.com>
Lado Lomidze <lado.lomidze@gmail.com>
Amir E. Aharoni <amir.aharoni@mail.huji.ac.il>
Simon Sattes <simon.sattes@gmail.com>
Jo Liss <joliss42@gmail.com>
Guntupalli Karunakar <karunakarg@yahoo.com>
Shahyar Ghobadpour <shahyar@gmail.com>
Lukasz Lipinski <uzza17@gmail.com>
Timo Tijhof <krinklemail@gmail.com>
Jason Moon <jmoon@socialcast.com>
Martin Frost <martinf55@hotmail.com>
Eneko Illarramendi <eneko@illarra.com>
EungJun Yi <semtlenori@gmail.com>
Courtland Allen <courtlandallen@gmail.com>
Viktar Varvanovich <non4eg@gmail.com>
Danny Trunk <dtrunk90@gmail.com>
Pavel Stetina <pavel.stetina@nangu.tv>
Michael Stay <metaweta@gmail.com>
Steven Roussey <sroussey@gmail.com>
Michael Hollis <hollis21@gmail.com>
Lee Rowlands <lee.rowlands@previousnext.com.au>
Timmy Willison <timmywillisn@gmail.com>
Karl Swedberg <kswedberg@gmail.com>
Baoju Yuan <the_guy_1987@hotmail.com>
Maciej Mroziński <mrozik87@gmail.com>
Luis Dalmolin <luis.nh@gmail.com>
Mark Aaron Shirley <maspwr@gmail.com>
Martin Hoch <martin@fidion.de>
Jiayi Yang <tr870829@gmail.com>
Philipp Benjamin Köppchen <xgxtpbk@gws.ms>
Sindre Sorhus <sindresorhus@gmail.com>
Bernhard Sirlinger <bernhard.sirlinger@tele2.de>
Jared A. Scheel <jared@jaredscheel.com>
Rafael Xavier de Souza <rxaviers@gmail.com>
John Chen <zhang.z.chen@intel.com>
Dale Kocian <dale.kocian@gmail.com>
Mike Sherov <mike.sherov@gmail.com>
Andrew Couch <andy@couchand.com>
Marc-Andre Lafortune <github@marc-andre.ca>
Nate Eagle <nate.eagle@teamaol.com>
David Souther <davidsouther@gmail.com>
Mathias Stenbom <mathias@stenbom.com>
Sergey Kartashov <ebishkek@yandex.ru>
Avinash R <nashpapa@gmail.com>
Ethan Romba <ethanromba@gmail.com>
Cory Gackenheimer <cory.gack@gmail.com>
Juan Pablo Kaniefsky <jpkaniefsky@gmail.com>
Roman Salnikov <bardt.dz@gmail.com>
Anika Henke <anika@selfthinker.org>
Samuel Bovée <samycookie2000@yahoo.fr>
Fabrício Matté <ult_combo@hotmail.com>
Viktor Kojouharov <vkojouharov@gmail.com>
Pawel Maruszczyk <lord_t@o2.pl>
Pavel Selitskas <p.selitskas@gmail.com>
Bjørn Johansen <bjorn.johansen@metronet.no>
Matthieu Penant <thieum22@hotmail.com>
Dominic Barnes <dominic@dbarnes.info>
David Sullivan <david.sullivan@gmail.com>
Thomas Jaggi <thomas.jaggi@gmail.com>
Vahid Sohrabloo <vahid4134@gmail.com>
Travis Carden <travis.carden@gmail.com>
Bruno M. Custódio <bruno@brunomcustodio.com>
Nathanael Silverman <nathanael.silverman@gmail.com>
Christian Wenz <christian@wenz.org>
Steve Urmston <steve@urm.st>
Zaven Muradyan <megalivoithos@gmail.com>
Woody Gilk <shadowhand@deviantart.com>
Zbigniew Motyka <zbigniew.motyka@gmail.com>
Suhail Alkowaileet <xsoh.k7@gmail.com>
Copyright 2013 jQuery Foundation and other contributors,
http://jqueryui.com/

This software consists of voluntary contributions made by many
individuals (AUTHORS.txt, http://jqueryui.com/about) For exact
contribution history, see the revision history and logs, available
at http://jquery-ui.googlecode.com/svn/

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
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
[jQuery UI](http://jqueryui.com/) - Interactions and Widgets for the web
================================

jQuery UI provides interactions like Drag and Drop and widgets like Autocomplete, Tabs and Slider and makes these as easy to use as jQuery itself.

If you want to use jQuery UI, go to [jqueryui.com](http://jqueryui.com) to get started. Or visit the [Using jQuery UI Forum](http://forum.jquery.com/using-jquery-ui) for discussions and questions.

If you are interested in helping develop jQuery UI, you are in the right place.
To discuss development with team members and the community, visit the [Developing jQuery UI Forum](http://forum.jquery.com/developing-jquery-ui) or in #jquery on irc.freednode.net.


For contributors
---

If you want to help and provide a patch for a bugfix or new feature, please take
a few minutes and look at [our Getting Involved guide](http://wiki.jqueryui.com/w/page/35263114/Getting-Involved).
In particular check out the [Coding standards](http://wiki.jqueryui.com/w/page/12137737/Coding-standards)
and [Commit Message Style Guide](http://wiki.jqueryui.com/w/page/25941597/Commit-Message-Style-Guide).

In general, fork the project, create a branch for a specific change and send a
pull request for that branch. Don't mix unrelated changes. You can use the commit
message as the description for the pull request.


Running the Unit Tests
---

Run the unit tests with a local server that supports PHP. No database is required. Pre-configured php local servers are available for Windows and Mac. Here are some options:

- Windows: [WAMP download](http://www.wampserver.com/en/)
- Mac: [MAMP download](http://www.mamp.info/en/index.html)
- Linux: [Setting up LAMP](https://www.linux.com/learn/tutorials/288158-easy-lamp-server-installation)
- [Mongoose (most platforms)](http://code.google.com/p/mongoose/)


Building jQuery UI
---

jQuery UI uses the [grunt](http://github.com/cowboy/grunt) build system. Building jQuery UI requires node.js and a command line zip program.

Install grunt.

`npm install grunt -g`

Clone the jQuery UI git repo.

`git clone git://github.com/jquery/jquery-ui.git`

`cd jquery-ui`

Install node modules.

`npm install`

Run grunt.

`grunt build`

There are many other tasks that can be run through grunt. For a list of all tasks:

`grunt --help`


For committers
---

When looking at pull requests, first check for [proper commit messages](http://wiki.jqueryui.com/w/page/12137724/Bug-Fixing-Guide).

Do not merge pull requests directly through GitHub's interface.
Most pull requests are a single commit; cherry-picking will avoid creating a merge commit.
It's also common for contributors to make minor fixes in an additional one or two commits.
These should be squashed before landing in master.

**Make sure the author has a valid name and email address associated with the commit.**

Fetch the remote first:

    git fetch [their-fork.git] [their-branch]

Then cherry-pick the commit(s):

	git cherry-pick [sha-of-commit]

If you need to edit the commit message:

    git cherry-pick -e [sha-of-commit]

If you need to edit the changes:

	git cherry-pick -n [sha-of-commit]
	# make changes
	git commit --author="[author-name-and-email]"

If it should go to the stable brach, cherry-pick it to stable:

    git checkout 1-8-stable
    git cherry-pick -x [sha-of-commit-from-master]

*NOTE: Do not cherry-pick into 1-8-stable until you have pushed the commit from master upstream.*
{% trans site_name=current_site.name, user_display=user_display(user) %}User {{ user_display }} at {{ site_name }} has given this as an email address.

To confirm this is correct, go to {{ activate_url }}
{% endtrans %}
{% include "account/email/email_confirmation_message.txt" %}
{% include "account/email/email_confirmation_subject.txt" %}
{% trans %}Confirm Email Address{% endtrans %}
{% trans site_domain=site.domain, username=user.username %}You're receiving this e-mail because you or someone else has requested a password for your user account at {{ site_domain }}.
It can be safely ignored if you did not request a password reset. Click the link below to reset your password.

{{ password_reset_url }}

In case you forgot, your username is {{ username }}.

Thanks for using our site!
{% endtrans %}
{% trans %}Password Reset E-mail{% endtrans %}
{% trans email=email %}You cannot remove your primary email address ({{email}}).{% endtrans %}
{% trans email=email %}Confirmation email sent to {{ email }}.{% endtrans %}
{% trans email=email %}You have confirmed {{ email }}.{% endtrans %}
{% trans email=email %}Removed email address {{ email }}.{% endtrans %}
{% trans name=user_display(user) %}Successfully signed in as {{ name }}.{% endtrans %}
{% trans %}You have signed out.{% endtrans %}
{% trans %}Password successfully changed.{% endtrans %}

{% trans %}Password successfully set.{% endtrans %}

{% trans %}Primary email address set.{% endtrans %}
{% trans %}Your primary email address must be confirmed.{% endtrans %}
{% trans %}Account successfully connected.{% endtrans %}
{% trans %}This account is already connected to a different profile.{% endtrans %}
{% trans %}Account successfully disconnected.{% endtrans %}
{% trans %}Could not find profile matching that account.{% endtrans %}
