# Contributing to Eclipse SmartHome

Thanks for your interest in this project!

You can propose contributions by sending pull requests through GitHub.

And of course you can [report issues](https://github.com/eclipse/smarthome/issues).

## Legal considerations

Please read the [Eclipse Foundation policy on accepting contributions via Git](http://wiki.eclipse.org/Development_Resources/Contributing_via_Git).

Your contribution cannot be accepted unless you have an [Eclipse Contributor Agreement](https://www.eclipse.org/legal/ECA.php) in place.

Here is the checklist for contributions to be _acceptable_:

1. [create an account at Eclipse](https://dev.eclipse.org/site_login/createaccount.php), and
2. add your GitHub user name in your account settings, and
3. electronically sign the ["Eclipse Contributor Agreement"](https://accounts.eclipse.org/user/eca), and
4. ensure that you _sign-off_ your Git commits, and
5. ensure that you use the _same_ email address as your Eclipse Foundation in commits.

## Technical considerations

Again, check that your author email in commits is the same as your Eclipse Foundation account, and make sure that you sign-off every commit (`git commit -s`).

Do not make pull requests from your `master` branch, please use topic branches instead.

When submitting code, please make every effort to follow [our coding guidelines](https://www.eclipse.org/smarthome/documentation/development/guidelines.html) in order to keep the code as homogeneous as possible.

Please provide meaningful commit messages.

Here is a sample _good_ Git commit log message:

    [666999] Quick summary

    This is a discussion of the change with details on the impact, limitations, etc.

    Write just like if you were discussing with fellows :-)

    Also-By: Somebody who also contributed parts of this code <foo@bar.com>
    Signed-off-by: Yourself <baz@foobar.org>

Never `merge` changes from the `master` branch into your topic branch. Always use the `rebase` command to apply your changes on top of the current `master`.

Finally, a contribution is not a good contribution unless it comes with unit tests, integration tests and
documentation.

Once you have received review comments on your pull request, please address them in **additional** commits, do not amend your previous commits and squeeze it in there.
Several commits help to speed up reviews because it is easier to see the differences.
Thus, there is no need to squash any commits because that will be done by a commiter of the project once the pull request will finally be merged.

Eclipse Public License - v 2.0

    THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
    PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
    OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.

1. DEFINITIONS

"Contribution" means:

  a) in the case of the initial Contributor, the initial content
     Distributed under this Agreement, and

  b) in the case of each subsequent Contributor:
     i) changes to the Program, and
     ii) additions to the Program;
  where such changes and/or additions to the Program originate from
  and are Distributed by that particular Contributor. A Contribution
  "originates" from a Contributor if it was added to the Program by
  such Contributor itself or anyone acting on such Contributor's behalf.
  Contributions do not include changes or additions to the Program that
  are not Modified Works.

"Contributor" means any person or entity that Distributes the Program.

"Licensed Patents" mean patent claims licensable by a Contributor which
are necessarily infringed by the use or sale of its Contribution alone
or when combined with the Program.

"Program" means the Contributions Distributed in accordance with this
Agreement.

"Recipient" means anyone who receives the Program under this Agreement
or any Secondary License (as applicable), including Contributors.

"Derivative Works" shall mean any work, whether in Source Code or other
form, that is based on (or derived from) the Program and for which the
editorial revisions, annotations, elaborations, or other modifications
represent, as a whole, an original work of authorship.

"Modified Works" shall mean any work in Source Code or other form that
results from an addition to, deletion from, or modification of the
contents of the Program, including, for purposes of clarity any new file
in Source Code form that contains any contents of the Program. Modified
Works shall not include works that contain only declarations,
interfaces, types, classes, structures, or files of the Program solely
in each case in order to link to, bind by name, or subclass the Program
or Modified Works thereof.

"Distribute" means the acts of a) distributing or b) making available
in any manner that enables the transfer of a copy.

"Source Code" means the form of a Program preferred for making
modifications, including but not limited to software source code,
documentation source, and configuration files.

"Secondary License" means either the GNU General Public License,
Version 2.0, or any later versions of that license, including any
exceptions or additional permissions as identified by the initial
Contributor.

2. GRANT OF RIGHTS

  a) Subject to the terms of this Agreement, each Contributor hereby
  grants Recipient a non-exclusive, worldwide, royalty-free copyright
  license to reproduce, prepare Derivative Works of, publicly display,
  publicly perform, Distribute and sublicense the Contribution of such
  Contributor, if any, and such Derivative Works.

  b) Subject to the terms of this Agreement, each Contributor hereby
  grants Recipient a non-exclusive, worldwide, royalty-free patent
  license under Licensed Patents to make, use, sell, offer to sell,
  import and otherwise transfer the Contribution of such Contributor,
  if any, in Source Code or other form. This patent license shall
  apply to the combination of the Contribution and the Program if, at
  the time the Contribution is added by the Contributor, such addition
  of the Contribution causes such combination to be covered by the
  Licensed Patents. The patent license shall not apply to any other
  combinations which include the Contribution. No hardware per se is
  licensed hereunder.

  c) Recipient understands that although each Contributor grants the
  licenses to its Contributions set forth herein, no assurances are
  provided by any Contributor that the Program does not infringe the
  patent or other intellectual property rights of any other entity.
  Each Contributor disclaims any liability to Recipient for claims
  brought by any other entity based on infringement of intellectual
  property rights or otherwise. As a condition to exercising the
  rights and licenses granted hereunder, each Recipient hereby
  assumes sole responsibility to secure any other intellectual
  property rights needed, if any. For example, if a third party
  patent license is required to allow Recipient to Distribute the
  Program, it is Recipient's responsibility to acquire that license
  before distributing the Program.

  d) Each Contributor represents that to its knowledge it has
  sufficient copyright rights in its Contribution, if any, to grant
  the copyright license set forth in this Agreement.

  e) Notwithstanding the terms of any Secondary License, no
  Contributor makes additional grants to any Recipient (other than
  those set forth in this Agreement) as a result of such Recipient's
  receipt of the Program under the terms of a Secondary License
  (if permitted under the terms of Section 3).

3. REQUIREMENTS

3.1 If a Contributor Distributes the Program in any form, then:

  a) the Program must also be made available as Source Code, in
  accordance with section 3.2, and the Contributor must accompany
  the Program with a statement that the Source Code for the Program
  is available under this Agreement, and informs Recipients how to
  obtain it in a reasonable manner on or through a medium customarily
  used for software exchange; and

  b) the Contributor may Distribute the Program under a license
  different than this Agreement, provided that such license:
     i) effectively disclaims on behalf of all other Contributors all
     warranties and conditions, express and implied, including
     warranties or conditions of title and non-infringement, and
     implied warranties or conditions of merchantability and fitness
     for a particular purpose;

     ii) effectively excludes on behalf of all other Contributors all
     liability for damages, including direct, indirect, special,
     incidental and consequential damages, such as lost profits;

     iii) does not attempt to limit or alter the recipients' rights
     in the Source Code under section 3.2; and

     iv) requires any subsequent distribution of the Program by any
     party to be under a license that satisfies the requirements
     of this section 3.

3.2 When the Program is Distributed as Source Code:

  a) it must be made available under this Agreement, or if the
  Program (i) is combined with other material in a separate file or
  files made available under a Secondary License, and (ii) the initial
  Contributor attached to the Source Code the notice described in
  Exhibit A of this Agreement, then the Program may be made available
  under the terms of such Secondary Licenses, and

  b) a copy of this Agreement must be included with each copy of
  the Program.

3.3 Contributors may not remove or alter any copyright, patent,
trademark, attribution notices, disclaimers of warranty, or limitations
of liability ("notices") contained within the Program from any copy of
the Program which they Distribute, provided that Contributors may add
their own appropriate notices.

4. COMMERCIAL DISTRIBUTION

Commercial distributors of software may accept certain responsibilities
with respect to end users, business partners and the like. While this
license is intended to facilitate the commercial use of the Program,
the Contributor who includes the Program in a commercial product
offering should do so in a manner which does not create potential
liability for other Contributors. Therefore, if a Contributor includes
the Program in a commercial product offering, such Contributor
("Commercial Contributor") hereby agrees to defend and indemnify every
other Contributor ("Indemnified Contributor") against any losses,
damages and costs (collectively "Losses") arising from claims, lawsuits
and other legal actions brought by a third party against the Indemnified
Contributor to the extent caused by the acts or omissions of such
Commercial Contributor in connection with its distribution of the Program
in a commercial product offering. The obligations in this section do not
apply to any claims or Losses relating to any actual or alleged
intellectual property infringement. In order to qualify, an Indemnified
Contributor must: a) promptly notify the Commercial Contributor in
writing of such claim, and b) allow the Commercial Contributor to control,
and cooperate with the Commercial Contributor in, the defense and any
related settlement negotiations. The Indemnified Contributor may
participate in any such claim at its own expense.

For example, a Contributor might include the Program in a commercial
product offering, Product X. That Contributor is then a Commercial
Contributor. If that Commercial Contributor then makes performance
claims, or offers warranties related to Product X, those performance
claims and warranties are such Commercial Contributor's responsibility
alone. Under this section, the Commercial Contributor would have to
defend claims against the other Contributors related to those performance
claims and warranties, and if a court requires any other Contributor to
pay any damages as a result, the Commercial Contributor must pay
those damages.

5. NO WARRANTY

EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT
PERMITTED BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN "AS IS"
BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR
IMPLIED INCLUDING, WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF
TITLE, NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR
PURPOSE. Each Recipient is solely responsible for determining the
appropriateness of using and distributing the Program and assumes all
risks associated with its exercise of rights under this Agreement,
including but not limited to the risks and costs of program errors,
compliance with applicable laws, damage to or loss of data, programs
or equipment, and unavailability or interruption of operations.

6. DISCLAIMER OF LIABILITY

EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT
PERMITTED BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS
SHALL HAVE ANY LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST
PROFITS), HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE
EXERCISE OF ANY RIGHTS GRANTED HEREUNDER, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

7. GENERAL

If any provision of this Agreement is invalid or unenforceable under
applicable law, it shall not affect the validity or enforceability of
the remainder of the terms of this Agreement, and without further
action by the parties hereto, such provision shall be reformed to the
minimum extent necessary to make such provision valid and enforceable.

If Recipient institutes patent litigation against any entity
(including a cross-claim or counterclaim in a lawsuit) alleging that the
Program itself (excluding combinations of the Program with other software
or hardware) infringes such Recipient's patent(s), then such Recipient's
rights granted under Section 2(b) shall terminate as of the date such
litigation is filed.

All Recipient's rights under this Agreement shall terminate if it
fails to comply with any of the material terms or conditions of this
Agreement and does not cure such failure in a reasonable period of
time after becoming aware of such noncompliance. If all Recipient's
rights under this Agreement terminate, Recipient agrees to cease use
and distribution of the Program as soon as reasonably practicable.
However, Recipient's obligations under this Agreement and any licenses
granted by Recipient relating to the Program shall continue and survive.

Everyone is permitted to copy and distribute copies of this Agreement,
but in order to avoid inconsistency the Agreement is copyrighted and
may only be modified in the following manner. The Agreement Steward
reserves the right to publish new versions (including revisions) of
this Agreement from time to time. No one other than the Agreement
Steward has the right to modify this Agreement. The Eclipse Foundation
is the initial Agreement Steward. The Eclipse Foundation may assign the
responsibility to serve as the Agreement Steward to a suitable separate
entity. Each new version of the Agreement will be given a distinguishing
version number. The Program (including Contributions) may always be
Distributed subject to the version of the Agreement under which it was
received. In addition, after a new version of the Agreement is published,
Contributor may elect to Distribute the Program (including its
Contributions) under the new version.

Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
receives no rights or licenses to the intellectual property of any
Contributor under this Agreement, whether expressly, by implication,
estoppel or otherwise. All rights in the Program not expressly granted
under this Agreement are reserved. Nothing in this Agreement is intended
to be enforceable by any entity that is not a Contributor or Recipient.
No third-party beneficiary rights are created under this Agreement.

Exhibit A - Form of Secondary Licenses Notice

"This Source Code may also be made available under the following 
Secondary Licenses when the conditions for such availability set forth 
in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
version(s), and exceptions or additional permissions here}."

  Simply including a copy of this Agreement, including this Exhibit A
  is not sufficient to license the Source Code under Secondary Licenses.

  If it is not possible or desirable to put the notice in a particular
  file, then You may include the notice in a location (such as a LICENSE
  file in a relevant directory) where a recipient would be likely to
  look for such a notice.

  You may add additional accurate notices of copyright ownership.
# Eclipse SmartHome Build Instructions

Thanks for your interest in the Eclipse SmartHome project!

Building and running the project is fairly easy if you follow the steps detailed below.

Please note that Eclipse SmartHome is not a product itself, but a framework to build solutions on top.
This means that what you build is primarily an artifact repository of OSGi bundles that can be used within smart home products.
Besides this repository, a VSCode extension is available for editing configuration files with full IDE support.

1\. Prerequisites
=================

The build infrastructure is based on Maven in order to make it as easy as possible to get up to speed. 
If you know Maven already then there won't be any surprises for you. 
If you have not worked with Maven yet, just follow the instructions and everything will miraculously work ;-)

What you need before you start:
- Maven3 from http://maven.apache.org/download.html

Make sure that the "mvn" command is available on your path

2\. Checkout
============

Checkout the source code from GitHub, e.g. by running

git clone https://github.com/eclipse/smarthome.git

3\. Building with Maven
=======================

To build Eclipse SmartHome from the sources, Maven takes care of everything:
- set MAVEN_OPTS to "-Xms512m -Xmx1024m"
- change into the smarthome directory ("cd smarthome“)
- run "mvn clean install" to compile and package all sources

If there are tests that are failing occasionally on your local build, run `mvn -DskipTests=true clean install` instead to skip them.

The p2 repository that contains all bundles as a build result will be available in the folder `products/org.eclipse.smarthome.repo/target`.
This is a working bundle for demonstrating/ testing the Oauth2 client.
Passwords, secrets, etc have to be configured through config admin in order for it to work

Simply deploy it to the runtime; then smarthome oauth commands will be registered and ready to test.


# Example 1: (Using authorization code)

## Try these on the OSGI console:

```
smarthome oauth Code cleanupEverything
smarthome oauth Code create
smarthome oauth Code getClient <fill in handle from create step>
smarthome oauth Code getAuthorizationUrl
```

```
now open browser with the URL from above step, authenticate yourself
to a real oauth provider
if everything works properly, it should redirect you to your redirectURL
Read the code http parameter from the redirectURL
```

```
smarthome oauth Code getAccessTokenByCode <code from redirectURL parameter>
smarthome oauth Code getCachedAccessToken
smarthome oauth Code refresh
smarthome oauth Code close
```

# Example 2: (Using ResourceOwner credentials i.e. you have the user's username and password directly)

## Try these on the OSGI console:

```
smarthome oauth ResourceOwner create
smarthome oauth ResourceOwner getClient <fill in handle from create step>
smarthome oauth ResourceOwner getAccessTokenByResourceOwnerPassword
smarthome oauth ResourceOwner getCachedAccessToken
smarthome oauth ResourceOwner refresh
smarthome oauth ResourceOwner close
```

### load again, similar to reboot/restart

```
smarthome oauth ResourceOwner getClient <fill in handle from create step>
smarthome oauth ResourceOwner getCachedAccessToken
smarthome oauth ResourceOwner refresh
```

### Done playing, delete this service permanently

```
smarthome oauth ResourceOwner delete <fill in handle from create step>
```

### Verify this is deleted (will throw exception)

```
smarthome oauth ResourceOwner getCachedAccessToken 
```

### Cannot get the client after delete

```
smarthome oauth ResourceOwner getClient <fill in handle from create step>
```
# Action modules via annotated classes

Action modules can be defined by writing classes and annotating their methods with special annotations.
The framework offers two providers, namely `AnnotatedActionModuleTypeProvider` and `AnnotatedThingActionModuleTypeProvider`, which collect these annotated elements and dynamically create the according action modules.

## Types of annotated classes

There are three different ways to offer action modules via annotations:

### Service

If the goal is to provide an action which is independent of a specific `ThingHandler` and which should only exists as one single instance, it should be implemented as a service.
This service has to implement the `org.eclipse.smarthome.automation.AnnotatedActions` interface.
It can be configured like any other framework service via a `ConfigDescription`, however its category should be `RuleActions`.

### Multi Service

This case is similar to the one above, except for that it can be instantiated and thus configured multiple times.
The service also has to implement the `org.eclipse.smarthome.automation.AnnotatedActions` interface.
It makes use of the multi service infrastructure of the framework and the specified "Service context" becomes the identifier for the specific configuration.
Its category should also be `RuleActions`.

### Thing

For actions that need access to the logic of a `ThingHandler`, one has to implement a service which implements the `org.eclipse.smarthome.core.thing.binding.AnnotatedActionThingHandlerService` interface.
The `ThingHandler` has to override the `Collection<Class> getServices()` method from the `BaseThingHandler` and return the class of the aforementioned service.
The framework takes care of registering and un-registering of that service.

## Annotations

Service classes mentioned above should have the following annotations:

- `@ActionScope(name = "myScope")`: This annotation has to be on the class and `myScope` defines the first part of the ModuleType UID, for example `binding.myBindinName` or `twitter`.
- `@RuleAction(label = "@text/myLabel", description = "myDescription text")`: Each method that should be offered as an action has to have this annotation. The method name will be the second part of the ModuleType uid (after the scope, separated by a "."). There are more parameters available, basically all fields which are part of `org.eclipse.smarthome.automation.type.ActionType`. Translations are also possible if `@text/id` placeholders are used and the bundle providing the actions offers the corresponding files.
- `@ActionOutput(name = "output1", type = "java.lang.String")`: This annotation (or multiple of it) has to be on the return type of the method and specifies under which name and type a result will be available. Usually the type should be the fully qualified Java type, but in the future it will be extented to support further types.
- `@ActionInput(name = "input1")`: This annotation has to be before a parameter of the method to name the input for the module. If the annotation is omitted, the implicit name will be "pN", whereas "N" will be the position of the parameter, i.e. 0-n.

## Method definition

Each annotated method inside of such a service will be turned into an Action ModuleType, i.e. one can have multiple module type definitions per service if multiple methods are annotated.
In addition to the annotations the methods should have a proper name since it is used inside the ModuleType uid.
The return type of a method should be `Map<String, Object>`, because the automation engine uses this mapping between all its modules, or `void` if it does not provide any outputs.
However, there is one shortcut for simple dataypes like `boolean`, `String`, `int`, `double`, and `float`. Such return types will automatically be put into a map with the predefined keyword "result" for the following modules to process.
Within the implementation of the method, only those output names which are specified as `@ActionOutput` annotations should be used, i.e. the resulting map should only contain those which also appear in an `@ActionOutput` annotation.

## Examples

For examples, please see the package `org.eclipse.smarthome.magic.binding.internal.automation.modules` inside the `org.eclipse.smarthome.magic` bundle.
# Eclipse SmartHome Automation Java Demo #

## Description ##

The purpose of the demo is to give an example, of how to use the Eclipse SmartHome Automation Java API, for creating, adding and removing rules.
It implements a simple rule and adds the rule via the RuleRegistry interface.

The Structure of the rule is as follows.
Triggers:
ItemStateChangeTrigger which is configured to trigger the rule if state of DemoSwitch item is changed.

Actions:
ItemPostCommandAction which is configured to turn on the DemoDimmer item.

To trigger the rule provided by this demo You need to send a command to the DemoSwitch item.
Use smarthome send DemoSwitch <command># Eclipse SmartHome Automation Json Demo #

## Description ##

The purpose of the demo is to give an example, of how to define a rule in a .json file.
The Structure of the defined rule is as follows.
Triggers:
ItemStateChangeTrigger which is configured to trigger the rule if state of DemoSwitch item is changed.

Actions:
ItemPostCommandAction which is configured to turn on the DemoDimmer item.

To trigger the rule provided by this demo You need to send a command to the DemoSwitch item.
Use smarthome send DemoSwitch <command># Eclipse SmartHome Automation Module Type Demo #

## Description ##

The purpose of the demo is to give an example, of how to define a module types in .json files, how to create a handlers for them
and how to register a ModuleHandlerFactory that creates handlers for the defined module types.

Following module types are provided:
CompareCondition - it can perform a basic comparison on integer values.

ConsolePrintAction - it prints it input to the standard output

ConsoleTrigger - it is triggered from org.osgi.service.event.Event.

Example rule definition:

[  
   {  
      "uid":"DemoRule",
      "name":"Demo Rule",
      "triggers":[  
         {  
            "id":"RuleTrigger",
            "type":"ConsoleTrigger",
            "configuration":{  
               "eventTopic":"demo/topic",
               "keyName":"key"
            }
         }
      ],
      "conditions":[  
         {  
            "id":"RuleCondition",
            "type":"CompareCondition",
            "configuration":{  
               "operator":"=",
               "constraint":5
            },
            "inputs":{  
               "inputValue":"RuleTrigger.outputValue"
            }
         }
      ],
      "actions":[  
         {  
            "id":"RuleAction",
            "type":"ConsolePrintAction",
            "inputs":{  
               "inputValue":"RuleTrigger.outputValue"
            }
         }
      ]
   }
] 

To trigger this rule and satisfy rule's condition you need to type in the console:
atmdemo postEvent demo/topic key 5txt.default.pid:txt.property=txt.value
txt.service.pid:txt.property=txt.value
Bundle resources go in here!Bundle resources go in here!Bundle resources go in here!Bundle resources go in here!imageBundle resources go in here!Bundle resources go in here!Bundle resources go in here!FORMAT: 1A

# Eclipse SmartHome UI Logging Bundle

This Bundle provides a resource at the REST API to enable a consumer to fetch the set log levels.
It also receives log messages which will be logged to the server's log.
The last logged messages by this API can be requested to be displayed in UIs.

Meta: This document is in normal markdown format,
but also compatible to [Apiary](apiary.com) for automatic doc generation and API testing.

## Log levels [/rest/log/levels]

### Get enabled log levels [GET]

 This depends on the current log settings at the backend.


+ Response 200 (application/json)

        {
            "warn": true,
            "error": true,
            "debug": true,
            "info": true
        }


## Log [/rest/log]

### Send log message [POST]

+ Request (application/json)

    + Attributes
        + severity (enum[string], required) - The severity of the log message
            + Members
                + `error`
                + `warn`
                + `info`
                + `debug`

        + url (string, optional) - The URL where the log event ocurred.
        + message (string, optional) - The message to log.

    + Body

            {
                "severity" : "error",
                "url" : "http://exmple.org/",
                "message" : "A test message"
            }

+ Response 200

+ Response 403 (application/json)

    + Attributes
        + error (string)
        + severity (string)

    + Body

            {
                 "error": "Your log severity is not supported.",
                 "severity": "info"
            }


## Log [/rest/log/{limit}]    

### Get last log messages [GET]

Return the last log entries received by `/rest/log/`.


+ Parameters
    + limit (number, optional) - Limit the amount of messages.

        On invalid input, limit is set to it's default.

        + Default: 500

+ Response 200 (application/json)

    + Attributes
        + timestamp (number) - UTC milliseconds from the epoch.

            In JavaScript, you can use this value for constructing a `Date`.

        + severity (enum[string])
            + Members
                + `error`
                + `warn`
                + `info`
                + `debug`

        + url (string)
        + message (string)

    + Body

            [
              {
                "timestamp": 1450531459479,
                "severity": "error",
                "url": "http://example.com/page1",
                "message": "test 5"
              },
              {
                "timestamp": 1450531459655,
                "severity": "error",
                "url": "http://example.com/page1",
                "message": "test 6"
              },
              {
                "timestamp": 1450531460038,
                "severity": "error",
                "url": "http://example.com/page2",
                "message": "test 7"
              }
            ]        
# Magic Bundle

The Magic Bundle is a virtual device bundle which provides different Things, Channels and supporting functionality for easy UI testing.

Future plans:

* Simulate communication errors
* Provide REST API to update thing status from _outside_
* Provide REST API to temporarily create new Channels/Things

## Provided Things

* Magic Light - On/Off
* Magic Light - Dimmable
* Magic Light - Color
* Magic Sensor - Door/Window Contact
* Magic Location
* Magic Configurable Thing
* Magic Thermostat
* Magic Delayed Online Thing - goes online after some time
* Magic Firmware Updatable Thing - can be firmware updated, depending on the model


## Discovery

The Things provided by this bundle do not require discovery but can all be set up manually using PaperUI.

## Bundle Configuration

Right now Magic has no specific configuration. This may change when _Future plans_ are implemented.

## Thing Configuration

The provided Things need no parameters right now.

## Channels

Available channels:

* switch - the on/off toggle maps to a Switch item.
* brightness - the brightness value maps to a Dimmer item.
* color - the color maps to a Color item.
* alert - the alert function of the color light.
* contact - the contact of the door/window contact.
* location - the location of the magic location.
* temperature - the temperature of the magic thermostat.
* number - the delay in seconds for the delayed thing to go online.

## Full Example

*.things:

```
magic:onoff-light:mylight "Bright or Dark"
magic:dimmable-light:greys "Shades of light"
magic:color-light:rainbow "Rainbow"
```

*.items:

```
Switch Light1 "On/Off Light" { channel="magic:onoff-light:mylight:switch" }
Dimmer Light2 "Shades of light" { channel="magic:dimmable-light:greys:brightness" }
Color Rainbow "Rainbow" { channel="magic:color-light:rainbow:color" }
```

Bundle resources go in here!Bundle resources go in here!---
layout: documentation
---

{% include base.html %}

# Documentation Overview

As Eclipse SmartHome is not an end user product, but  a framework to build end user solutions on top, you will only find technical documentation here. If you are an end user, please rather check out any of the [offers that use Eclipse SmartHome](https://www.eclipse.org/smarthome/index.html#references).

The technical documentation is split into the following sections:

 - [Concepts](concepts/items.html): Here you will find information about the fundamental concepts of Eclipse SmartHome and the used vocabulary.
 - [Features](features/index.html): This section explains what features Eclipse SmartHome offers and how they are configured and used.
 - [Development](development/ide.html): Everything you need to know when you want to develop code - be it for the core platform or for your own extensions.
 - [Community](community/contributing.html): Learn how to get in touch with the community and how you can contribute back to the project.
  
## Background 

### Why Eclipse SmartHome?

Since the emergence of broadband internet connections, smartphones and tablets the smart home market shows a remarkable upsurge. This has led to a very fragmented market, which makes it difficult for customers to "bet on the right horse". In fact, there is not one system, protocol or standard that could possibly fulfill all potential requirements. There is hence a need for platforms that allow the integration of different systems, protocols or standards and that provide a uniform way of user interaction and higher level services.

### How does Eclipse SmartHome help?

The goals of the Eclipse SmartHome project can be summarized as:

* Provide a flexible framework for smart home and ambient assisted living (AAL) solutions. This framework focuses on the use cases of this domain, e.g. on easy automation and visualization aspects.
* Specify extension points for integration possibilities and higher-level services. Extending and thus customizing the solution must be as simple as possible and this requires concise and dedicated interfaces.
* Provide implementations of extensions for relevant systems, protocols or standards. Many of them can be useful to many smart home solutions, so this project will provide a set of extensions that can be included if desired. They can also be in the shape of a general Java library or an OSGi bundle, so that these implementations can be used independently of the rest of the project as well.
* Provide a development environment and tools to foster implementations of extensions. The right tooling can support the emergence of further extensions and thus stimulates future contributions to the project.
* Create a packaging and demo setups. Although the focus is on the framework, it needs to be shown how to package a real solution from it, which can be used as a starting point and for demo purposes.
Description
* The Eclipse SmartHome project is a framework that allows building smart home solutions that have a strong focus on heterogeneous environments, i.e. solutions that deal with the integration of different protocols or standards. Its purpose is to provide a uniform access to devices and information and to facilitate different kinds of interactions with them. This framework consists out of a set of OSGi bundles that can be deployed on an OSGi runtime and which defines OSGi services as extension points.

The stack is meant to be usable on any kind of system that can run an OSGi stack - be it a multi-core server, a residential gateway or a Raspberry Pi.

The project focuses on services and APIs for the following topics:

1. _Data Handling_: This includes a basic but extensible type system for smart home data and commands that provides a common ground for an abstracted data and device access as well as event mechanisms to send this information around. It is the most important topic for integrating with other systems, which is done through so called bindings, which are a special type of extension.
1. _Rule Engines_: A flexible rule engine that allows changing rules during runtime and which defines extension types that allow breaking down rules into smaller pieces like triggers, actions, logic modules and templates.
1. _Declarative User Interfaces_: A framework with extensions for describing user interface content in a declarative way. This includes widgets, icons, charts etc.
1. _Persistence Management_: Infrastructure that allows automatic data processing based on a simple and unified configuration. Persistence services are pluggable extensions, which can be anything from a log writer to an IoT cloud service.

Besides the runtime framework and implementation, the Eclipse SmartHome projects also provides different kinds of tools and samples:

* Language Server Protocol (LSP) support for content assist and syntax validation. This may be used by solutions to provide full IDE support for editing configuration models and rules.
* Maven archetypes to easily create skeletons for extensions
* Demo packaging with other Eclipse IoT projects
---
layout: documentation
---

{% include base.html %}

# How To Become Part of the Community

## Getting Involved

There are several ways of how to get in contact with the community in order to ask questions or discuss ideas:

## Discussion Forum

The forum is used to discuss ideas and to answer general questions. It is organized per topic, so you can easily decide what is of interest for you.

* [Discussion Forum](http://eclipse.org/forums/eclipse.smarthome)

## Issue Tracker

Like most GitHub hosted projects, we use GitHub Issues as an issue tracking system.

* [Eclipse SmartHome Issues](https://github.com/eclipse/smarthome/issues)

If you have found a bug or if you would like to propose a new feature, please feel free to enter an issue. But before creating a new issue, please first check that it does not already exist.

## Report a Security Vulnerability

Bugs which are crucial for the security of the project should be reported as a security vulnerability to the Eclipse Security Team:

* [Eclipse Security Team](https://eclipse.org/security)

### Issue Tracker Links

* [Create a new Issue](https://github.com/eclipse/smarthome/issues/new)
* [All Issues](https://github.com/eclipse/smarthome/issues?utf8=%E2%9C%93&q=is%3Aissue)
* [Open Bugs](https://github.com/eclipse/smarthome/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
* [Open Features](https://github.com/eclipse/smarthome/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Aenhancement+)
* [New/Unconfirmed Issues](https://github.com/eclipse/smarthome/issues?q=is%3Aopen+is%3Aissue+no%3Aassignee)
 
# Code Contributions

If you want to become a contributor to the project, please check our guidelines first. If you can't wait to get your hands dirty have a look at the open issues where we [need your help](https://github.com/eclipse/smarthome/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) or one of the [open bugs](https://github.com/eclipse/smarthome/issues?q=is%3Aissue+is%3Aopen+label%3Abug).
Be aware that you are required to sign the [Eclipse Contributor Agreement](https://www.eclipse.org/legal/ECA.php) in order for us to accept your contribution.

## Pull requests are always welcome

We are always thrilled to receive pull requests, and do our best to process them as fast as possible. Not sure if that typo is worth a pull request? Do it! We will appreciate it.

If your pull request is not accepted on the first try, don't be discouraged! If there's a problem with the implementation, hopefully you received feedback on what to improve.

We're trying very hard to keep Eclipse SmartHome lean and focused. We don't want it to do everything for everybody. This means that we might decide against incorporating a new feature. However, there might be a way to implement that feature on top of Eclipse SmartHome.

## Discuss your design in the discussion forum

We recommend discussing your plans in the [Discussion Forum](https://www.eclipse.org/forums/eclipse.smarthome) before starting to code - especially for more ambitious contributions. This gives other contributors a chance to point you in the right direction, give feedback on your design, and maybe point out if someone else is working on the same thing.

## Conventions for pull requests

* Submit unit tests for your changes. Eclipse SmartHome has a great test framework built in - use it! Take a look at existing tests for inspiration. Run the full test suite on your branch before submitting a pull request.
* Update the documentation when creating or modifying features. Test your documentation changes for clarity, concision and correctness, as well as a clean documentation build.
* Write clean code. Universally formatted code promotes ease of writing, reading and maintenance. Check our [Coding Guidelines](../development/guidelines.html).
* Pull requests' descriptions should be as clear as possible and include a reference to all the issues that they address.
* Pull requests must not contain commits from other users or branches.

The process to create a pull request is then the following:

1. Create an account at Eclipse if you do not have one yet.
1. Sign the [Eclipse Contributor Agreement (ECA)](https://www.eclipse.org/legal/ECA.php).
For legal reasons you are required to sign the ECA before we can accept your pull request.
1. Fork the sources of Eclipse SmartHome on GitHub.
1. Do the coding!
1. Make sure your code applies to the [Coding Guidelines](../development/guidelines.html).
1. Make sure there is a [GitHub issue](https://github.com/eclipse/smarthome/issues?utf8=%E2%9C%93&q=is%3Aissue) for your contribution. If it does not exist yet, [create one](https://github.com/eclipse/smarthome/issues/new).
1. Add a "Signed-off-by" line to every commit you do - see the [Eclipse wiki here](https://wiki.eclipse.org/Development_Resources/Contributing_via_Git#Signing_off_on_a_commit) and [here](https://wiki.eclipse.org/Development_Resources/Contributing_via_Git#via_GitHub) for details.
1. Create a pull request, referencing the GitHub issue number.
---
layout: documentation
---

{% include base.html %}

# Downloads

## Source Code

The source code of Eclipse SmartHome™ is available in our [GitHub repository](https://github.com/eclipse/smarthome).

## Binary Artifacts

Since Eclipse SmartHome™ is not a solution by itself, we do not offer any ready-to-run downloadable artifact. The binary build of Eclipse SmartHome [consists out of OSGi bundles](../features/index.html) that are provided through p2 and Maven repositories.

Besides the runtime bundles, Eclipse SmartHome comes with the "Designer", which is an Eclipse RCP application. The Designer is a tool for textual configuration of a runtime. You only need it, if your solution makes use of the [textual configuration support](../features/dsl.html) of Eclipse SmartHome.

### Releases

The *latest release of Eclipse SmartHome is 0.9*, released on December 6, 2017. For details, please check out the [Release Notes](https://projects.eclipse.org/projects/iot.smarthome/releases/0.9.0/plan). You can download it here:

| Maven repository | [https://repo.eclipse.org/content/repositories/smarthome-releases](https://repo.eclipse.org/content/repositories/smarthome-releases) |
| p2 repository | [http://download.eclipse.org/smarthome/updates-release/0.9.0/](http://download.eclipse.org/smarthome/updates-release/0.9.0/) (download as [zip](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.9.0/eclipsesmarthome-incubation-0.9.0-repo.zip)) |

Please note that the Designer has been deprecated is not part of the release anymore.

### Snapshots

You can find nightly snapshot builds of the Eclipse SmartHome features and bundles at [http://download.eclipse.org/smarthome/updates-nightly/](http://download.eclipse.org/smarthome/updates-nightly/). Every couple of days, we also provide a stable build, so if you want use snapshot builds, but a lower update frequency, go for [http://download.eclipse.org/smarthome/updates-stable/](http://download.eclipse.org/smarthome/updates-stable/).

### Archive

##### Eclipse SmartHome 0.8.0

The [0.8.0 release](https://projects.eclipse.org/projects/iot.smarthome/releases/0.8.0/plan) can be found here:

| Maven repository | [https://repo.eclipse.org/content/repositories/smarthome-releases](https://repo.eclipse.org/content/repositories/smarthome-releases) |
| p2 repository | [http://download.eclipse.org/smarthome/updates-release/0.8.0/](http://download.eclipse.org/smarthome/updates-release/0.8.0/) (download as [zip](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.8.0/eclipsesmarthome-incubation-0.8.0-repo.zip)) |

Designer downloads (platform-specific):

 - [Eclipse SmartHome Designer (Windows 32bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.8.0/eclipsesmarthome-incubation-0.8.0-designer-win.zip)
 - [Eclipse SmartHome Designer (Windows 64bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.8.0/eclipsesmarthome-incubation-0.8.0-designer-win64.zip)
 - [Eclipse SmartHome Designer (Mac OSX 64bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.8.0/eclipsesmarthome-incubation-0.8.0-designer-macosx64.zip)
 - [Eclipse SmartHome Designer (Linux 32bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.8.0/eclipsesmarthome-incubation-0.8.0-designer-linux.zip)
 - [Eclipse SmartHome Designer (Linux 64bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.8.0/eclipsesmarthome-incubation-0.8.0-designer-linux64.zip)

##### Eclipse SmartHome 0.7.0

The [0.7.0 release](https://projects.eclipse.org/projects/iot.smarthome/releases/0.7.0/plan) can be found here:

| Maven repository | [https://repo.eclipse.org/content/repositories/smarthome-releases](https://repo.eclipse.org/content/repositories/smarthome-releases) |
| p2 repository | [http://download.eclipse.org/smarthome/updates-release/0.7.0/](http://download.eclipse.org/smarthome/updates-release/0.7.0/) (download as [zip](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.7.0/eclipsesmarthome-incubation-0.7.0-repo.zip)) |

Designer downloads (platform-specific):

 - [Eclipse SmartHome Designer (Windows 32bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.7.0/eclipsesmarthome-incubation-0.7.0-designer-win.zip)
 - [Eclipse SmartHome Designer (Windows 64bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.7.0/eclipsesmarthome-incubation-0.7.0-designer-win64.zip)
 - [Eclipse SmartHome Designer (Mac OSX 64bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.7.0/eclipsesmarthome-incubation-0.7.0-designer-macosx64.zip)
 - [Eclipse SmartHome Designer (Linux 32bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.7.0/eclipsesmarthome-incubation-0.7.0-designer-linux.zip)
 - [Eclipse SmartHome Designer (Linux 64bit)](http://eclipse.org/downloads/download.php?file=/smarthome/releases/0.7.0/eclipsesmarthome-incubation-0.7.0-designer-linux64.zip)
	
---
layout: documentation
---

{% include base.html %}

# Audio & Voice

Audio and voice features are an important aspect of any smart home solution as it is a very natural way to interact with the user.

Eclipse SmartHome comes with a very modular architecture that enables all kinds of different use cases. 
At its core, there is the notion of an *audio stream*. 
Audio streams are provided by *audio sources* and consumed by *audio sinks*.  

![](images/audio.png)

- *Audio Streams* are essentially a byte stream with a given *audio format*. 
They do not need to be limited in size, i.e. it is also allowed to have continuous streams, e.g. the input from a microphone or from an Internet radio station.
- *Audio Formats* define the container (e.g. WAV), encoding, bit rate, sample frequency and depth and the bit order (little or big endian).
- *Audio Sources* are services that are capable of producing audio streams. 
They can support different formats and provide a stream in a requested format upon request. 
Typical audio source services are microphones. Typically, a continuous stream is expected from them.
- *Audio Sinks* are services that accept audio streams of certain formats. 
Typically, these are expected to play the audio stream, i.e. they are some kind of speaker or media device.
- *Text-to-Speech* (TTS) services are similar to audio sources with respect to the ability to create audio streams. 
The difference is that they take a string as an input and will synthesize this string to a spoken text using a given voice. 
TTS services can provide information about the voices that they support and the locale that those voices are associated with. 
Each voice supports exactly one locale.
- *Speech-to-Text* (STT) services are similar to audio sinks, but they do not simply play back the stream, but convert it to a plain string. 
They provide information about supported formats and locales.

As plain text from an STT service is often not very useful, there is additionally the concept of a *human language interpreter*:

![](images/hli.png)

A *Human Language Interpreter* takes a string as an input. 
It then derives actions from it (like sending commands to devices) and/or replies with a string, which opens the possibility to realize conversations. 
As such an interpreter is not directly linked to audio streams, but operates on strings only, this can be the basis for any kind of assistant, e.g. for chat bots using the console, XMPP, Twitter or other messaging services. 

Applications can dynamically choose which services to use, so that different sinks can be used for different use cases. 
Defaults can be set as a configuration for all those services in case an application does not ask for any specific service.
---
layout: documentation
---

{% include base.html %}

# Categories

Categories in Eclipse SmartHome are used to provide meta information about Things, Channels, etc. UIs can use this information to render specific icons or provide a search functionality to for example filter all Things for a certain category.

## Differences between categories

We separate the categories into `functional` and `visual`. 
Therefore we treat `Thing categories` as how the physical device **looks like** and `Channel categories` as something that describes the **functional purpose** of the Channel.

## Thing Categories

The Thing type definition allows to specify a category. 
User interfaces can parse this category to get an idea how to render this Thing. 
A Binding can classify each Thing into one of the existing categories. 
The list of all predefined categories can be found in our categories overview:

| Category        | Description | Icon Example |
|-----------------|-------------|{% for category in site.data.categories_thing %}
|{{category.name}}|{{category.description}}|![{{category.icon}}](../features/ui/iconset/classic/icons/{{category.icon}}){:height="36px" width="36px"}|{% endfor %}

### Channel Group Categories

Channel Groups can be seen as a kind of `sub-device` as they combine certain (physical) abilities of a `Thing` into one. For such `Group Channels` one can set a category from the `Thing` category list.

## Channel Categories

The Channel type definition allows to specify a category. 
A Binding should classify each Channel into one of the existing categories or leave the category blank, if there is no good match. 
There are different types of categories for Channels, which are listed below.

{% for category in site.data.categories %}
    {% assign typesStr = typesStr | append: category.type | append: ',' %}
{% endfor %}
{% assign types = typesStr | split: ',' | uniq %}

{% for type in types %}
#### {{ type }}

| Category        | Icon Example |
|-----------------|--------------|{% for category in site.data.categories %}{% if category.type == type %}
|{{category.name}}|![{{category.name | downcase}}](../features/ui/iconset/classic/icons/{{category.name | downcase }}.png){:height="36px" width="36px"}|{% endif %}{% endfor %}
{% endfor %}
---
layout: documentation
---

{% include base.html %}

# Thing Discovery

Many devices, technologies and systems can be automatically discovered on the network or browsed through some API. It therefore makes a lot of sense to use these features for a smart home solution.

In Eclipse SmartHome bindings therefore implement _Discovery Services_ for Things, which provide _Discovery Results_. All _Discovery Results_ are regarded as suggestions to the user and are put into the _inbox_.

### Background Discovery

A couple of discovery services support automatic discovery in the background, while for others a scan needs to be triggered manually.
Services that support background discovery usually have it enabled by default. 
It is possible to override this setting and deactivate background discovery for individual services by setting `discovery.<serviceid>:background=false`, where `serviceid` is usually identical to a binding id, e.g. the LIFX background discovery can be disabled through `discovery.lifx:background=false`.

## Inbox

The inbox holds a list of all discovered Things (`DiscoveryResult`) from all active discovery services. 
A discovery result represents a discovered Thing of a specific Thing type, that could be instantiated as a Thing. 
The result usually contains properties that identify the discovered Things further like IP address or a serial number. 
Each discovery result also has a timestamp when it was added to or updated in the inbox and it may also contain a time to live, indicating the time after which it is be automatically removed from the inbox. 

Discovery results can either be ignored or approved, where in the latter case a Thing is created for them and they become available in the application. 
If an entry is ignored, it will be hidden in the inbox without creating a Thing for it. 

Eclipse SmartHome offers a service to automatically ignore discovery results in the inbox, whenever a Thing is created manually, that represents the same Thing, as the respective discovery result would create. 
This Thing would either have the same Thing UID or the value of its representation property is equal to the representation property's value in the discovery result.
This service is enabled by default but can be disabled by setting `org.eclipse.smarthome.inbox:autoIgnore=false`. 

### Auto Approve

If the manual acceptance of discovery results by the user is not wished, it is possible to turn on the auto-approval feature of the inbox. 
In this case, every new entry gets automatically approved immediately (unless it has been marked as ignored as a duplicate).

The auto approval can be enabled by the setting `org.eclipse.smarthome.inbox:autoApprove=true`; the default is false.
---
layout: documentation
---

{% include base.html %}

# Concepts

When first thinking about your home automation system, it may be helpful to bear in mind that there are two ways of thinking about or viewing your system; the physical view and the functional view.

The physical view will be familiar to you.
This view focuses on the devices in your system, the connections between these devices (e.g. wires, Z-Wave, WiFi hardware), and other physical aspects of the system.

The functional view might be a new concept for you.
The functional view focuses on how information about the devices, connections, and so on, is represented in user interfaces.
The functional view includes focusing on how rules affect representations of physical devices in software.
 Perhaps most important to you, the functional view focuses on how an action in a user interface affects the software associated with the physical device it represents.

It is a bit of an over-simplification, but you can think of the physical view as being a view of the 'real world', and the functional view being a view of the 'software world'.

## Things, Channels, Bindings, Items and Links

**Things** are entities that can be physically added to a system.
Things may provide more than one function (for example, a Z-Wave multi-sensor may provide a motion detector and also measure room temperature).
Things do not have to be physical devices; they can also represent a web service or any other manageable source of information and functionality.

Things expose their capabilities through **Channels**.
Whether an installation takes advantage of a particular capability reflected by a Channel depends on whether it has been configured to do so.
When you configure your system, you do not necessarily have to use every capability offered by a Thing.
You can find out what Channels are available for a Thing by looking at the documentation of the Thing's Binding.

**Bindings** can be thought of as software adapters, making Things available to your home automation system.
They are add-ons that provide a way to link Items to physical devices.
They also abstract away the specific communications requirements of that device so that it may be treated more generically by the framework.

**Items** represent capabilities that can be used by applications, either in user interfaces or in automation logic.
Items have a **State** and they may receive commands.

The glue between Things and Items are **Links**.
A Link is an association between exactly one Channel and one Item.
If a Channel is linked to an Item, it is "enabled", which means that the capability the Item represents is accessible through that Channel.
Channels may be linked to multiple Items and Items may be linked to multiple Channels.

To illustrate these concepts, consider the example below of a two-channel actuator that controls two lights:

![](images/thing-devices-1.png)

The actuator is a Thing that might be installed in an electrical cabinet.
It has a physical address and it must be configured in order to be used (remember the physical view introduced at the beginning of this article).

In order for the user to control the two lights, he or she access the capability of the actuator Thing (turning on and off two separate lights) through two Channels, that are Linked to two switch Items presented to the user through a user interface.
---
layout: documentation
---

{% include base.html %}

# Items

Eclipse SmartHome has a strict separation between the physical world (the "Things", see below) and the application, which is built around the notion of "Items" (also called the virtual layer).

Items represent functionality that is used by the application (mainly user interfaces or automation logic).
Items have a state and are used through events.
  
The following Item types are currently available (alphabetical order):

| Item Name          | Description | Command Types |
|--------------------|-------------|---------------|
| Color              | Color information (RGB) | OnOff, IncreaseDecrease, Percent, HSB |
| Contact            | Item storing status of e.g. door/window contacts | OpenClosed |
| DateTime           | Stores date and time | - |
| Dimmer             | Item carrying a percentage value for dimmers | OnOff, IncreaseDecrease, Percent |
| Group              | Item to nest other Items / collect them in Groups | - |
| Image              | Holds the binary data of an image | - |
| Location           | Stores GPS coordinates | Point |
| Number             | Stores values in number format, takes an optional dimension suffix  | Decimal |
| Number:<dimension> | like Number, additional dimension information for unit support | Quantity |
| Player             | Allows to control players (e.g. audio players) | PlayPause, NextPrevious, RewindFastforward |
| Rollershutter      | Typically used for blinds | UpDown, StopMove, Percent |
| String             | Stores texts | String |
| Switch             | Typically used for lights (on/off) | OnOff |

## Group Items

Group Items collect other Items into Groups.
Group Items can themselves be members of other Group Items.
Cyclic membership is not forbidden but strongly not recommended.
User interfaces might display Group Items as single entries and provide navigation to its members.

Example for a Group Item as a simple collection of other Items:
```
    Group groundFloor
    Switch kitchenLight (groundFloor)
    Switch livingroomLight (groundFloor)
``` 

### Derive Group State from Member Items

Group Items can derive their own state from their member Items.
To derive a state the Group Item must be constructed using a base Item and a Group function.
When calculating the state, Group functions recursively traverse the Group's members and also take members of subgroups into account.
If a subgroup however defines a state on its own (having base Item & Group function set) traversal stops and the state of the subgroup member is taken. 

Available Group functions:

| Function           | Parameters                    | Base Item                                   | Description                                                                                                                                      |
|--------------------|-------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| EQUALITY           | -                             | \<all\>                                     | Sets the state of the members if all have equal state. Otherwise UNDEF is set. In the Item DSL `EQUALITY` is the default and may be omitted.     |
| AND, OR, NAND, NOR | <activeState>, <passiveState> | \<all\> (must match active & passive state) | Sets the \<activeState\>, if the member state \<activeState\> evaluates to `true` under the boolean term. Otherwise the \<passiveState\> is set. |
| SUM, AVG, MIN, MAX | -                             | Number                                      | Sets the state according to the arithmetic function over all member states.                                                                      |
| COUNT              | <regular expression>          | Number                                      | Sets the state to the number of members matching the given regular expression with their states.                                                 |
| LATEST, EARLIEST   | -                             | DateTime                                    | Sets the state to the latest/earliest date from all member states                                                                                |

Examples for derived states on Group Items when declared in the Item DSL:

- `Group:Number:COUNT(".*")` counts all members of the Group matching the given regular expression, here any character or state (simply count all members).
- `Group:Number:AVG` calculates the average value over all member states which can be interpreted as `DecimalTypes`.
- `Group:Switch:OR(ON,OFF)` sets the Group state to `ON` if any of its members has the state `ON`, `OFF` if all are off.    
- `Group:Switch:AND(ON,OFF)` sets the Group state to `ON` if all of its members have the state `ON`, `OFF` if any of the Group members has a different state than `ON`.
- `Group:DateTime:LATEST` sets the Group state to the latest date from all its members states.

## State and Command Type Formatting

### StringType

`StringType` objects store a simple Java String.

### DateTimeType

`DateTimeType` objects are parsed using Java's `SimpleDateFormat.parse()` using the first matching pattern:

1. `yyyy-MM-dd'T'HH:mm:ss.SSSZ`
2. `yyyy-MM-dd'T'HH:mm:ss.SSSz`
3. `yyyy-MM-dd'T'HH:mm:ss.SSSX`
4. `yyyy-MM-dd'T'HH:mm:ssz`
5. `yyyy-MM-dd'T'HH:mm:ss`

Literal | Standard | Example
--------|----------|--------
z | General time zone | Pacific Standard Time; PST; GMT-08:00
Z | RFC 822 time zone | -0800
X | ISO 8601 time zone | -08; -0800; -08:00

### DecimalType, PercentType

`DecimalType` and `PercentType` objects use Java's `BigDecimal` constructor for conversion.
`PercentType` values range from 0 to 100.

### QuantityType

A numerical type which carries a unit in addition to its value.
The framework is capable of automatic conversion between units depending on the users locale settings.
See the concept on [Units of Measurement](units-of-measurement.html) for more details.

### HSBType

HSB string values consist of three comma-separated values for hue (0-360°), saturation (0-100%), and value (0-100%) respectively, e.g. `240,100,100` for blue.

### PointType

`PointType` strings consist of three `DecimalType`s separated by commas, indicating latitude and longitude in degrees, and altitude in meters respectively.

### Enum Types

| Type                  | Supported Values        |
|-----------------------|-------------------------|
| IncreaseDecreaseType  | `INCREASE`, `DECREASE`  |
| NextPreviousType      | `NEXT`, `PREVIOUS`      |
| OnOffType             | `ON`, `OFF`             |
| OpenClosedType        | `OPEN`, `CLOSED`        |
| PlayPauseType         | `PLAY`, `PAUSE`         |
| RewindFastforwardType | `REWIND`, `FASTFORWARD` |
| StopMoveType          | `STOP`, `MOVE`          |
| UpDownType            | `UP`, `DOWN`            |

## A note on Items which accept multiple state data types

There are a number of Items which accept multiple state data types, for example `DimmerItem`, which accepts `OnOffType` and `PercentType`, `RollershutterItem`, which  accepts `PercentType` and `UpDownType`, or `ColorItem`, which accepts `HSBType`, `OnOffType` and `PercentType`.
Since an Item has a SINGLE state, these multiple data types can be considered different views to this state.
The data type carrying the most information about the state is usually used to keep the internal state for the Item, and other datatypes are converted from this main data type.
This main data type is normally the first element in the list returned by `Item.getAcceptedDataTypes()`.

Here is a short table demonstrating conversions for the examples above:

| Item Name     | Main Data Type | Additional Data Types Conversions                                                                                                                                             |
|---------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color         | `HSBType`      | &bull; `OnOffType` - `OFF` if the brightness level in the `HSBType` equals 0, `ON` otherwise <br/> &bull; `PercentType` - the value for the brightness level in the `HSBType` |
| Dimmer        | `PercentType`  | `OnOffType` - `OFF` if the brightness level indicated by the percent type equals 0, `ON` otherwise                                                                            |
| Rollershutter | `PercentType`  | `UpDownType` - `UP` if the shutter level indicated by the percent type equals 0, `DOWN` if it equals 100, and `UnDefType.UNDEF` for any other value                           |

## Item Metadata

Sometimes additional information is required to be attached to Items for certain use-cases. 
This could be an application which needs some hints in order to render the Items in a generic way, or an integration with voice controlled assistants, or any other services which access the Items and need to understand their "meaning".

Such metadata can be attached to Items using disjunct namespaces so they won't conflict with each other. 
Each metadata entry has a main value and optionally additional key/value pairs. 
There can be metadata attached to an Item for as many namespaces as desired, like in the following example: 

    Switch "My Fan" { homekit="Fan.v2", alexa="Fan" [ type="oscillating", speedSteps=3 ] }

The metadata can be maintained via a dedicated REST endpoint and is included in the `EnrichedItemDTO` responses.

Extensions which can infer some metadata automatically need to implement and register a `MetadataProvider` service in order to make them available to the system. 
They may provision them from any source they like and also dynamically remove or add data. 
They are also not restricted to a single namespace.

The `MetadataRegistry` provides access for all extensions which need to read the Item metadata programmatically. 
It is the central place where additional information about Items is kept.
---
layout: documentation
---

# Profiles

The communication between the framework and the Thing handlers is managed by the "Communication Manager", which in turn uses "Profiles"  to determined what exactly needs to be done. 
This provides some flexibility to influence these communication paths.

By their nature, profiles are correlated to links between Items and Channels (i.e. `ItemChannelLinks`). So if one Channel is linked to several Items it also will have several profile instances, each handling the communication to exactly one of these Items. 
The same applies for the situation where one Item is linked to multiple Channels. 

Profiles are created by ProfileFactories and are retained for the lifetime of their link. 
This means that they are allowed to retain a transient state, like e.g. the timestamp of the the last event or the last state. 
With this, it is possible to take into account the temporal dimension when calculating the appropriate action in any situation.

There exist two different kinds of profiles: state and trigger profiles.

### State Profiles

State profiles are responsible for communication between Items and their corresponding state Channels (`ChannelKind.STATE`). 
Their purpose is to forward state updates and commands to and from the Thing handlers.

### Trigger Profiles

Trigger Channels (`ChannelKind.TRIGGER`) by themselves do not maintain a state (as by their nature they only fire events). 
With the help of trigger profiles they can be linked to Items anyway. 
Hence the main purpose of a trigger profile is to calculate a state based on the fired events. 
This state then is forwarded to the linked Item by sending `ItemStateEvents`. 

Trigger profiles are powerful means to implement some immediate, straight-forward logic without the need to write any rules. 

Apart from that, they do not pass any commands or state updates to and from the Thing handler as by their nature trigger Channels are not capable of handling these.
---
layout: documentation
---

# Things

Things are the entities that can physically be added to a system and which can potentially provide many functionalities in one.
It is important to note that Things do not have to be devices, but they can also represent a web service or any other manageable source of information and functionality.
From a user perspective, they are relevant for the setup and configuration process, but not for the operation.

Things can have configuration properties, which can be optional or mandatory.
Such properties can be basic information like an IP address, an access token for a web service or a device specific configuration that alters its behavior.

### Channels

Things provide "Channels", which represent the different functions the Thing provides.
Where the Thing is the physical entity or source of information, the Channel is a concrete function from this Thing.
A physical light bulb might have a color temperature Channel and a color Channel, both providing functionality of the one light bulb Thing to the system.
For sources of information the Thing might be the local weather with information from a web service with different Channels like temperature, pressure and humidity.

Channels are linked to Items, where such links are the glue between the virtual and the physical layer.
Once such a link is established, a Thing reacts on events sent for an item that is linked to one of its Channels.
Likewise, it actively sends out events for Items linked to its Channels.

### Bridges

A special type of Thing is a "bridge".
Bridges are Things that need to be added to the system in order to gain access to other Things.
A typical example of a bridge is an IP gateway for some non-IP based home automation system or a web service configuration with authentication information which every Thing from this web service might need.

### Discovery

As many Things can be automatically discovered, there are special mechanisms available that deal with the handling of [automatically discovered Things](discovery.html).


## Thing Status

Each Thing has a status object, which helps to identify possible problems with the device or service.
The following table provides an overview of the different statuses:

| Status        | Description |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UNINITIALIZED | This is the initial status of a Thing, when it is added or the framework is being started. This status is also assigned, if the initializing process failed or the binding is not available. Commands, which are sent to Channels will not be processed.                                                                                                                                                                                                                                  |
| INITIALIZING  | This state is assigned while the binding initializes the Thing. It depends on the binding how long the initializing process takes. Commands, which are sent to Channels will not be processed.                                                                                                                                                                                                                                                                                            |
| UNKNOWN       | The handler is fully initialized but due to the nature of the represented device/service it cannot really tell yet whether the Thing is ONLINE or OFFLINE. Therefore the Thing potentially might be working correctly already and may or may not process commands. But the framework is allowed to send commands, because some radio-based devices may go ONLINE if a command is sent to them. The handler should take care to switch the Thing to ONLINE or OFFLINE as soon as possible. |
| ONLINE        | The device/service represented by a Thing is assumed to be working correctly and can process commands.                                                                                                                                                                                                                                                                                                                                                                                    |
| OFFLINE       | The device/service represented by a Thing is assumed to be not working correctly and may not process commands. But the framework is allowed to send commands, because some radio-based devices may go back to ONLINE, if a command is sent to them.                                                                                                                                                                                                                                       |
| REMOVING      | The device/service represented by a Thing should be removed, but the binding did not confirm the deletion yet. Some bindings need to communicate with the device to unpair it from the system. Thing is probably not working and commands can not be processed.                                                                                                                                                                                                                           |
| REMOVED       | This status indicates that the device/service represented by a Thing was removed from the external system after the REMOVING was initiated by the framework. Usually this status is an intermediate status because the Thing gets removed from the database after this status was assigned.                                                                                                                                                                                               |

The statuses UNINITIALIZED, INITIALIZING and REMOVING are set by the framework, where as the statuses UNKNOWN, ONLINE and OFFLINE are assigned from a binding.

Additionally, the REMOVED state is set by the binding to indicate that the removal process has been completed, i.e. the Thing must have been in REMOVING state before.

### Status Transitions

The following diagram shows the allowed status transitions:

![Status Transitions](diagrams/status_transitions.png)

The initial state of a Thing is UNINITIALIZED.
From UNINITIALIZED the Thing goes into INITIALIZING.
If the initialization fails, the Thing goes back to UNINITIALIZED.
If the initialization succeeds, the binding sets the status of the Thing to UNKNOWN, ONLINE or OFFLINE, which all mean that the Thing handler is fully initialized.
From one of this states the Thing can go back into UNINITIALIZED, REMOVING or REMOVED.
The statuses REMOVING and REMOVED can also be reached from any of the other states.

## Status Details

A status is detailed further with a status detail object.
The following table lists the different status details for each status:

<table>
<tr valign="top"><td rowspan="7">UNINITIALIZED</td><td>NONE</td><td>No further status details available.</td></tr>
<tr valign="top">                                  <td>HANDLER_MISSING_ERROR</td><td>The handler cannot be initialized, because the responsible binding is not available or started.</td></tr>
<tr valign="top">                                  <td>HANDLER_REGISTERING_ERROR</td><td>The handler failed in the service registration phase.</td></tr>
<tr valign="top">                                  <td>HANDLER_CONFIGURATION_PENDING</td><td>The handler is registered but can not be initialized caused by missing configuration parameters.</td></tr>
<tr valign="top">                                  <td>HANDLER_INITIALIZING_ERROR</td><td>The handler failed in the initialization phase.</td></tr>
<tr valign="top">                                  <td>BRIDGE_UNINITIALIZED</td><td>The bridge associated with this Thing is not initialized.</td></tr>
<tr valign="top">                                  <td>DISABLED</td><td>The thing was explicitly disabled.</td></tr>
<tr valign="top"><td>INITIALIZING</td>             <td>NONE</td><td>No further status details available.</td></tr>
<tr valign="top"><td>UNKNOWN</td>                  <td>NONE</td><td>No further status details available.</td></tr>
<tr valign="top"><td rowspan="2">ONLINE</td>       <td>NONE</td><td>No further status details available.</td></tr>
<tr valign="top">                                  <td>CONFIGURATION_PENDING</td><td>The Thing is waiting to transfer configuration information to a device. Some bindings need to communicate with the device to make sure the configuration is accepted.</td></tr>
<tr valign="top"><td rowspan="7">OFFLINE</td>      <td>NONE</td><td>No further status details available.</td></tr>
<tr valign="top">                                  <td>COMMUNICATION_ERROR</td><td>Error in communication with the device. This may also be only a temporary error.</td></tr>
<tr valign="top">                                  <td>CONFIGURATION_ERROR</td><td>An issue with the configuration of a Thing prevents the communication with the represented device or service. This issue might be solved by reconfiguring the Thing.</td></tr>
<tr valign="top">                                  <td>BRIDGE_OFFLINE</td><td>Assuming the Thing to be offline because the corresponding bridge is offline.</td></tr>
<tr valign="top">                                  <td>FIRMWARE_UPDATING</td><td>The Thing is currently operating a firmware update.</td></tr>
<tr valign="top">                                  <td>DUTY_CYCLE</td><td>The Thing is currently in DUTY_CYCLE state, which means it is blocked for further usage.</td></tr>
<tr valign="top">                                  <td>GONE</td><td>The Thing has been removed from the bridge or the network to which it belongs and is no longer available for use. The user can now remove the Thing from the system.</td></tr>
<tr valign="top"><td>REMOVING</td>                 <td>NONE</td><td>No further status details available.</td></tr>
<tr valign="top"><td>REMOVED</td>                  <td>NONE</td><td>No further status details available.</td></tr>
</table>

### Status Description 

To provide additional information about the current status a description is used.
The status description is to be specified by the binding.
This description can be used for debugging purposes and should not be presented to the user, as it might contain unreadable technical information (e.g. an HTTP status code, or any other protocol specific information, which helps to identify the current problem).

### Thing Status API

The Thing interface defines a method `getStatusInfo()` to retrieve the current status of the Thing.
The following code shows how to print the status of each Thing into the console:

```java
Collection<Thing> things = thingRegistry.getAll();
for (Thing thing : things) {
    ThingStatusInfo statusInfo = thing.getStatusInfo();
    switch (statusInfo.getStatus()) {
        case ONLINE:
            System.out.println("Thing is online");
            break;
        case OFFLINE:
            System.out.println("Thing is offline");
            break;
        default:
            System.out.println("Thing is in state " + statusInfo.getStatus());
            break;
    }
    System.out.println("Thing status detail: " + statusInfo.getStatusDetail());
    System.out.println("Thing status description: " + statusInfo.getDescription());
}
```
---
layout: documentation
---

{% include base.html %}

# Units Of Measurement

To express measured values in a scientific correct unit the framework supports units of measurement.
By using quantified decimal values in state updates and commands, the framework is able to automatically convert values to a desired unit which may be defined by the system locale or on a per-use-basis. 

## QuantityType 

Bindings use the `QuantityType` to post updates of sensor data with a quantifying unit. 
This way the framework and/or the user is able to convert the quantified value to other matching units:

A weather binding which reads temperature values in °C would use the `QuantityType` to indicate the unit as °C.
The framework is then able to convert the values to either °F or Kelvin according to the configuration of the system.
The default conversion the framework will use is locale based: 
Depended on the configured locale the framework tries to convert a `QuantityType` to the default unit of the matching measurement system. 
This is the imperial system for the United States (locale US) and Liberia (language tag "en-LR"). 
The metric system with SI units is used for the rest of the world. 
This conversion will convert the given `QuantityType` into a default unit for the specific dimension of the type. 
This is:

| Dimension     | default unit metric        | default unit imperial  |
|---------------|----------------------------|------------------------|
| Length        | Meter (m)                  | Inch (in)              |
| Temperature   | Celsius (°C)               | Fahrenheit (°F)        |
| Pressure      | Hectopascal (hPa)          | Inch of mercury (inHg) | 
| Speed         | Kilometers per hour (km/h) | Miles per hour (mph)   |
| Intensity     | Irradiance (W/m2)          | Irradiance (W/m2)      |
| Dimensionless | Abstract unit one (one)    | Abstract unit one (one)|
| Angle         | Degree (°)                 | Degree (°)             |

## NumberItem linked to QuantityType Channel

In addition to the automated conversion the `NumberItem` linked to a Channel delivering `QuantityTypes` can be configured to always have state updates converted to a specific unit. 
The unit given in the state description is parsed and then used for conversion (if necessary).
The framework assumes that the unit to parse is always the last token in the state description.
If the parsing failed the locale based default conversion takes place.

    Number:Temperature temperature "Outside [%.2f °F]" { channel="...:current#temperature" }
    
In the example the `NumberItem` is specified to bind to Channels which offer values from the dimension `Temperature`.
Without the dimension information the `NumberItem` only will receive updates of type `DecimalType` without a unit and any conversion.
The state description defines two decimal places for the value and the fix unit °F.
In case the state description should display the unit the binding delivers or the framework calculates through locale based conversion the pattern will look like this:
    
    "Outside [%.2f %unit%]"
    
The special placeholder `%unit%` will then be replaced by the actual unit symbol.
In addition the placeholder `%unit%` can be placed anywhere in the state description.
 
#### Defining ChannelTypes

In order to match `NumberItems` and Channels and define a default state description with unit placeholder the Channel also has to provide an Item type which includes the dimension information:


    <channel-type id="temperature">
        <item-type>Number:Temperature</item-type>
        <label>Temperature</label>
        <description>Current temperature</description>
        <state readOnly="true" pattern="%.1f %unit%" />
    </channel-type>

The state description pattern "%.1f %unit%" describes the value format as floating point with one decimal place and also the special placeholder for the unit.

## Implementing UoM
When creating QuantityType states the framework offers some useful packages and classes:
The `org.eclipse.smarthome.core.library.unit` package contains the classes `SIUnits`, `ImperialUnits` and `SmartHomeUnits` which provide units unique to either of the measurement systems and common units used in both systems.
The `MetricPrefix` class provides prefixes like MILLI, CENTI, HECTO, etc. which are wrappers to create derived units.
The `org.eclipse.smarthome.core.library.dimension` and `javax.measure.quantity` packages provide interfaces which are used to type the generic QuantityType and units. 

## List of Units

All units which are currently supported by default are listed in the tables below.


Imperial:

| Type        | Unit            | Symbol |
|-------------|-----------------|--------|
| Pressure    | Inch of Mercury | inHg   |
| Temperature | Fahrenheit      | °F     |
| Speed       | Miles per Hour  | mph    |
| Length      | Inch            | in     |
| Length      | Foot            | ft     |
| Length      | Yard            | yd     |
| Length      | Chain           | ch     |
| Length      | Furlong         | fur    |
| Length      | Mile            | mi     |
| Length      | League          | lea    |

SI:

| Type                   | Unit                    | Symbol |
|------------------------|-------------------------|--------|
| Acceleration           | Metre per square Second | m/s2   |
| AmountOfSubstance      | Mole                    | mol    |
| Angle                  | Radian                  | rad    |
| Angle                  | Degree                  | °      |
| Angle                  | Minute Angle            | '      |
| Angle                  | Second Angle            | ''     |
| Area                   | Square Metre            | m2     |
| ArealDensity           | Dobson Unit             | DU     |
| CatalyticActivity      | Katal                   | kat    |
| Dimensionless          | Percent                 | %      |
| Dimensionless          | Parts per Million       | ppm    |
| Dimensionless          | Decibel                 | dB     |
| ElectricPotential      | Volt                    | V      |
| ElectricCapacitance    | Farad                   | F      |
| ElectricCharge         | Coulomb                 | C      |
| ElectricConductance    | Siemens                 | S      |
| ElectricCurrent        | Ampere                  | A      |
| ElectricInductance     | Henry                   | H      |
| ElectricResistance     | Ohm                     | Ω      |
| Energy                 | Joule                   | J      |
| Energy                 | Watt Second             | Ws     |
| Energy                 | Watt Hour               | Wh     |
| Energy                 | KiloWatt Hour           | kWh    |
| Force                  | Newton                  | N      |
| Frequency              | Hertz                   | Hz     |
| Illuminance            | Lux                     | lx     |
| Intensity              | Irradiance              | W/m²   |
| Length                 | Metre                   | m      |
| Length                 | Kilometre               | km     |
| LuminousFlux           | Lumen                   | lm     |
| LuminousIntensity      | Candela                 | cd     |
| MagneticFlux           | Weber                   | Wb     |
| MagneticFluxDensity    | Tesla                   | T      |
| Mass                   | Kilogram                | kg     |
| Mass                   | Gram                    | g      |
| Power                  | Watt                    | W      |
| Pressure               | Pascal                  | Pa     |
| Pressure               | hectoPascal             | hPa    |
| Pressure               | Millimetre of Mercury   | mmHg   |
| Pressure               | Bar                     | bar    |
| Pressure               | milliBar                | mbar   |
| Radioactivity          | Becquerel               | Bq     |
| RadiationDoseAbsorbed  | Gray                    | Gy     |
| RadiationDoseEffective | Sievert                 | Sv     |
| SolidAngle             | Steradian               | sr     |
| Speed                  | Metre per Second        | m/s    |
| Speed                  | Kilometre per Hour      | km/h   |
| Speed                  | Knot                    | kn     |
| Temperature            | Kelvin                  | K      |
| Temperature            | Celsius                 | °C     |
| Time                   | Second                  | s      |
| Time                   | Minute                  | min    |
| Time                   | Hour                    | h      |
| Time                   | Day                     | d      |
| Time                   | Week                    | week   |
| Time                   | Year                    | y      |
| Volume                 | Cubic Metre             | m3     |

Prefixes:

| Name  | Symbol | Value |
|-------|--------|-------|
| Yotta | Y      | 10²⁴  |
| Zetta | Z      | 10²¹  |
| Exa   | E      | 10¹⁸  |
| Peta  | P      | 10¹⁵  |
| Tera  | T      | 10¹²  |
| Giga  | G      | 10⁹   |
| Mega  | M      | 10⁶   |
| Kilo  | k      | 10³   |
| Hecto | h      | 10²   |
| Deca  | da     | 10    |
| Deci  | d      | 10⁻¹  |
| Centi | c      | 10⁻²  |
| Milli | m      | 10⁻³  |
| Micro | µ      | 10⁻⁶  |
| Nano  | n      | 10⁻⁹  |
| Pico  | p      | 10⁻¹² |
| Femto | f      | 10⁻¹⁵ |
| Atto  | a      | 10⁻¹⁸ |
| Zepto | z      | 10⁻²¹ |
| Yocto | y      | 10⁻²⁴ |


To use the prefixes simply add the prefix to the unit symbol e.g.

Examples:
-milliAmpere - `mA`
-centiMetre - `cm`
-kiloWatt - `kW`
' State diagram for Thing Status Concept
@startuml
skinparam state {
  BackgroundColor White
  BorderColor Grey
  ArrowColor #01324D
  StartColor #01324D
  EndColor #01324D
}
[*] -up-> UNINITIALIZED
UNINITIALIZED -right-> INITIALIZING
INITIALIZING -left-> UNINITIALIZED
INITIALIZING -right-> initialized

state initialized {
 ONLINE -right-> OFFLINE
 ONLINE --> UNKNOWN
 OFFLINE -left-> ONLINE
 OFFLINE --> UNKNOWN
 UNKNOWN --> ONLINE
 UNKNOWN --> OFFLINE
}

initialized -left-> UNINITIALIZED

state removal {
 [*] --> REMOVING
 REMOVING --> REMOVED
 REMOVED --> [*]  
}
@enduml---
layout: documentation
---

{% include base.html %}

# Conventions

## Null Annotations

[Null annotations](https://wiki.eclipse.org/JDT_Core/Null_Analysis) are used from the Eclipse JDT project.
The intention of these annotations is to transfer a method's contract written in its JavaDoc into the code to be processed by tools.
These annotations can be used for **static** checks, but **not** at runtime.

Thus for publicly exposed methods that belong to the API and are (potentially) called by external callers, a `null` check cannot be omitted, although a method parameter is marked to be not `null` via an annotation.
There will be a warning in the IDE for this check, but that is fine.
For private methods or methods in an internal package the annotations are respected and additional `null` checks are omitted.

To use the annotations, every bundle must have an **optional** `Import-Package` dependency to `org.eclipse.jdt.annotation`.
Classes should be annotated with `@NonNullByDefault`:

```java
@NonNullByDefault
public class MyClass(){}
```

Return types, parameter types, generic types etc. are annotated with `@Nullable` only.
The annotation should be written in front of the type.

Fields should be annotated like this:

```java
private @Nullable MyType myField;
```

Methods should be annotated as follows:

```java
private @Nullable MyReturnType myMethod(){};
```

Fields that get a static and mandatory reference injected through OSGi Declarative Services can be annotated with

```java
private @NonNullByDefault({}) MyService injectedService;
```

to skip the nullevaluation for these fields.
Fields within `ThingHandler` classes that are initialized within the `initialize()` method may also be annotated like this, because the framework ensures that `initialize()` will be called before any other method.
However, please watch the scenario where the initialization of the handler fails, because fields might not have been initialized and using them should be prepended by a `null` check.

There is **no need** for a `@NonNull` annotation because it is set as default.
Test classes do not have to be annotated (the usage of `SuppressWarnings("null")` is allowed, too).

The transition of existing classes can be a longer process, but using nullness annotations in a class / interface requires to set the default for the whole class and annotations on all types that differ from the default.
---
layout: documentation
---

{% include base.html %}

# Coding Guidelines

The following guidelines apply to all code of the Eclipse SmartHome project.
They must be followed to ensure a consistent code base for easy readability and maintainability.
Exceptions can certainly be made, but they should be discussed and approved by a project committer upfront.

Note that this list also serves as a checklist for code reviews on pull requests.
To speed up the contribution process, we therefore advice to go through this checklist yourself before creating a pull request.

## A. Code Style

1. The [Java naming conventions](http://java.about.com/od/javasyntax/a/nameconventions.htm) should be used.
1. Every Java file must have a license header. You can run `mvn license:format` on the root of the repo to automatically add missing headers.
1. Every class, interface and enumeration should have JavaDoc describing its purpose and usage.
1. Every class, interface and enumeration must have an `@author` tag in its JavaDoc for every author that wrote a substantial part of the file.
1. Every constant, field and method with default, protected or public visibility should have JavaDoc (optional, but encouraged for private visibility as well).
1. Code must be formatted using the provided code formatter and clean up settings. They are set up automatically by the official [IDE setup](ide.html).
1. Generics must be used where applicable.
1. Code should not show any warnings. Warnings that cannot be circumvented should be suppressed by using the `@SuppressWarnings` annotation. 
1. For dependency injection, OSGi Declarative Services should be used.
1. OSGi Declarative Services should be declared using annotations. The IDE will take care of the service *.xml file creation. See the official OSGi documentation for an [example here](http://enroute.osgi.org/services/org.osgi.service.component.html). We always use `@Activate`, `@Deactivate` and `@Modified` if we define these methods, even if they exist in a super class, to make the code more readable.
1. Packages that contain classes that are not meant to be used by other bundles should have "internal" in their package name.
1. [Null annotations](https://wiki.eclipse.org/JDT_Core/Null_Analysis) are used from the Eclipse JDT project. `@NonNullByDefault` and `@Nullable` should be used, for details see [Null annotation conventions](conventions.html#null-annotations).

## B. OSGi Bundles

1. Every bundle must contain a Maven pom.xml with a version and artifact name that is in sync with the manifest entry. The pom.xml must reference the correct parent pom (which is usually in the parent folder).
1. Every bundle must contain a [NOTICE](https://www.eclipse.org/projects/handbook/#legaldoc) file, providing meta information about the bundle and license information about 3rd party content.
1. Every bundle must contain a build.properties file, which lists all resources that should end up in the binary under `bin.includes`.
1. The manifest must not contain any "Require-Bundle" entries. Instead, "Import-Package" must be used.
1. The manifest must not export any internal package.
1. The manifest must not have any version constraint on package imports, unless this is thoughtfully added. Note that Eclipse automatically adds these constraints based on the version in the target platform, which might be too high in many cases.
1. The manifest must include all services in the Service-Component entry. A good approach is to put OSGI-INF/*.xml in there.
1. Every exported package of a bundle must be imported by the bundle itself again.
1. Any 3rd party content has to be added thoughtfully and version/license information has to be given in the NOTICE file.

## C. Language Levels and Libraries

1. Eclipse SmartHome generally targets JavaSE 8 with the following restrictions:
 * To allow optimized JavaSE 8 runtimes, the set of Java packages to be used is furthermore restricted to [Compact Profile 2](http://www.oracle.com/technetwork/java/embedded/resources/tech/compact-profiles-overview-2157132.html)
 * Java 5 for org.eclipse.smarthome.protocols.enocean.*
1. The minimum OSGi framework version supported is [OSGi R4.2](http://www.osgi.org/Download/Release4V42), no newer features must be used.
1. For logging, slf4j (v1.7.2) is used.
1. A few common utility libraries are available that every Eclipse SmartHome based solution has to provide and which can be used throughout the code (and which are made available in the target platform):
 - Apache Commons IO (v2.2)
 - Apache Commons Lang (v2.6)
 - ~~Google Guava (v10.0.1)~~ (historically allowed, to be avoided in new contributions)

## D. Runtime Behavior

1. Overridden methods from abstract classes or interfaces are expected to return fast unless otherwise stated in their JavaDoc. Expensive operations should therefore rather be scheduled as a job.
1. Creation of threads must be avoided. Instead, resort into using existing schedulers which use pre-configured thread pools. If there is no suitable scheduler available, start a discussion in the forum about it rather than creating a thread by yourself. For periodically executed jobs that do not require a fixed rate [scheduleWithFixedDelay](http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html#scheduleWithFixedDelay(java.lang.Runnable,%20long,%20long,%20java.util.concurrent.TimeUnit)) should be preferred over [scheduleAtFixedRate](http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html#scheduleAtFixedRate(java.lang.Runnable,%20long,%20long,%20java.util.concurrent.TimeUnit)).
1. Bundles need to cleanly start and stop without throwing exceptions or malfunctioning. This can be tested by manually starting and stopping the bundle from the console (`stop <bundle-id>` resp. `start <bundle-id>`).
1. Bundles must not require any substantial CPU time. Test this e.g. using "top" or VisualVM and compare CPU utilization with your bundle stopped vs. started.

## E. Logging

1. As we are in a dynamic OSGi environment, loggers should be [non-static](http://slf4j.org/faq.html#declared_static), when ever possible and have the name `logger`.
1. Parametrized logging must be used (instead of string concatenation).
1. Where ever unchecked exceptions are caught and logged, the exception should be added as a last parameter to the logging. For checked exceptions, this is normally not recommended, unless it can be considered an error situation and the stacktrace would hold additional important information for the analysis.
1. Logging levels should focus on the system itself and describe its state. As every bundle is only one out of many, logging should be done very scarce. It should be up to the user to increase the logging level for specific bundles, packages or classes if necessary. This means in detail:
 - Most logging should be done in `debug` level. `trace` can be used for even more details, where necessary.
 - Only few important things should be logged in `info` level, e.g. a newly started component or a user file that has been loaded.
 - `warn` logging should only be used to inform the user that something seems to be wrong in his overall setup, but the system can nonetheless function as normal, while possibly ignoring some faulty configuration/situation. It can also be used in situations, where a code section is reached, which is not expected by the implementation under normal circumstances (while being able to automatically recover from it).
 - `error` logging should only be used to inform the user that something is tremendously wrong in his setup, the system cannot function normally anymore, and there is a need for immediate action. It should also be used if some code fails irrecoverably and the user should report it as a severe bug.
1. For bindings, you should NOT log errors, if e.g. connections are dropped - this is considered to be an external problem and from a system perspective to be a normal and expected situation. The correct way to inform users about such events is to update the Thing status accordingly. Note that all events (including Thing status events) are anyhow already logged.
1. Likewise, bundles that accept external requests (such as servlets) must not log errors or warnings if incoming requests are incorrect. Instead, appropriate error responses should be returned to the caller.

## Static Code Analysis

The Eclipse SmartHome Maven build includes [tooling for static code analysis](https://github.com/openhab/static-code-analysis) that will validate your code against the coding guidelines and some additional best practices. Information about the checks can be found [here](https://github.com/openhab/static-code-analysis/blob/master/docs/included-checks.md).

The tool will generate an individual report for each bundle that you can find in `path/to/bundle/target/code-analysis/report.html` file and a report for the whole build that contains links to the individual reports in the `target/summary_report.html`.
The tool categorizes the found issues by priority: 1(error),2(warning) or 3(info).
If any error is found within your code the Maven build will end with failure.
You will receive detailed information (path to the file, line and message) listing all problems with Priority 1 on the console.

Please fix all the priority 1 issues and all issues with priority 2 and 3 that are relevant (if you have any doubt don't hesitate to ask).
Re-run the build to confirm that the checks are passing.
---
layout: documentation
---

{% include base.html %}

# Setting Up a Development Environment

Please ensure that you have the following prerequisites installed on your machine:

1. [Git](https://git-scm.com/downloads)
1. [Maven 3.x](https://maven.apache.org/download.cgi)
1. [Oracle JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
1. [Python >=2.5](https://www.python.org/downloads/) (to build UIs with npm)

The Eclipse IDE is used for Eclipse SmartHome developments.
The Eclipse Installer automatically prepares the IDE so that it comes with all required plug-ins, the correct workspace encoding settings, pre-configured code formatters and more.
Simply follow these steps:

1. Download the [Eclipse Installer](https://wiki.eclipse.org/Eclipse_Installer)

2. Launch the Eclipse Installer and switch to „Advanced Mode“ in the top right menu:
![Step 0](images/ide0.png)

3. Choose the "Eclipse IDE for Java Developers" and select "Next":
![Step 1](images/ide1.png)

4. Expand the "SmartHome" entry, double click "Runtime" and select "Next":
![Step 2](images/ide2.png)

5. Now provide an installation folder (don't use spaces in the path on Windows!) and your Github id (used to push your changesets to) and select "Next":
![Step 3](images/ide3.png)

6. The installation will now begin when pressing "Finish".
![Step 4](images/ide4.png)

7. Once it is done, you will see the Eclipse Welcome Screen, which you can close by clicking "Workbench" on the top right.
You will see that the installer not only set up an Eclipse IDE instance for you, but also checked out the Eclipse SmartHome git repository and imported all projects into the workspace.
Don't worry that you still see error markers at that point, this will be addressed in the next steps.
![Step 5](images/ide5.png)

8. Wait until all automatic tasks have been finished (see status field bottom left). After that select "Help->Perform Setup Tasks..." from the menu and click "Finish":
![Step 6](images/ide6.png)

9. Your workspace should now fully compile and you can start the runtime by launching the "SmartHome Runtime" launch configuration:
![Step 8](images/ide8.png)

10. Note: The Paper UI and Basic UI have been built by "Perform Setup Tasks...". It could be necessary to repeat that step after code has been changed. Access the Paper UI at [http://localhost:8080/paperui/index.html](http://localhost:8080/paperui/index.html). For more information about Paper UI see [Paper UI Development](notes.html#paperui-development-jshtml). 

Note that you will find the sources in a subfolder called "git" within your selected installation folder. You can use any kind of git client here, if you do not want to use the git support from within the Eclipse IDE.
If you want to push changes, you need to do so to [your personal fork of the Eclipse SmartHome repository](https://github.com/eclipse/smarthome/fork) in order to create a pull request. You will find more details in the ["How to contribute"](../community/contributing.html) documentation.
---
layout: documentation
---

{% include base.html %}

# Notes
===
The following notes should collect some tips and tricks for the development for and with the Eclipse SmartHome framework.

## Maven Bundle Plugin
---

The Eclipse SmartHome framework follows the Manifest first approach and Tycho is been used to build eclipse-plugins using maven.
Sometimes it could be useful to use the maven-bundle-plugin (and so the bnd tools) to inspect a generated manifest file and compare this one with the one that is used by Tycho (e.g. to identify missing imports, etc.).
The manifest generation could be triggered by:

    mvn bundle:manifest -DniceManifest=true

The "nice manifest" option will add line breaks after every imported package.
Now you can have a look at the manifest that would be generated by the bndtool using:

    cat target/classes/META-INF/MANIFEST.MF

## Paper UI development (JS/HTML)
---

The initial setup of PaperUI can be done in two ways:

1. By running the maven build.
2. Running an `npm install` followed by `npm run build`.

The JS/HTML files of Paper UI are packaged using the 'Gulp' plugin. 
There are two important gulp tasks needed for development. 
For normal development you need to run the following command on console:

    npm start

This will automatically inject all the needed files to index.html and will launch a browsersync instance running on http://localhost:3000/ (default). 
The calls to rest end-point are also proxied by this gulp task. 
After running this, any changes made into the files of folder 'web-src' will be available in the browser after refreshing the page.
The distribution version of Paper UI can be seen using the command:

    npm run build

This will minify the files and copy all the sources to 'web' folder. 
The changes can be seen at 'http://localhost:8080/' (default port for smarthome web server).

### Paper UI Location Support

Paper UI supports the rendering for location configuration parameters as well as `LocationItem`s in a map view.
For licensing reasons the map component provided by the framework does _not_ render any map but defines the extension point `mapSourceService` which can be used to provide a map source.
Using the [OpenLayers API (v4.2.0)](https://openlayers.org/en/v4.2.0/apidoc/) a solution may provide an existing or even its own implementation of a map source.

This example configures the [OpenStreetMap map source](https://openlayers.org/en/v4.2.0/apidoc/ol.source.OSM.html) and provides it via the Paper UI extensions module:

```javascript
angular.module('PaperUI.extensions', []) //
.service('mapSourceService', function() {
    return {
        getMapSource : function() {
            return new ol.source.OSM()
        }
    }
})
```

---
layout: documentation
---

{% include base.html %}

Testing Eclipse SmartHome
===
There are two different kinds of approaches for testing Eclipse SmartHome. One is to use JUnit Plug-in tests with simple JUnit test classes. The other is to extend the test class from the `JavaOSGiTest` class and have the full OSGi environment available to test OSGi services and dynamic behaviour. Both approaches are supported through a simple infrastructure, which allows to easily write and execute tests.

Test fragment
---

In general tests are implemented in a separate fragment bundle, which host is the bundle that should be tested. The name of the test fragment bundle should be the same as the bundle to test with a ".test" suffix. The MANIFEST.MF file must contain a `Fragment-Host` entry pointing to the bundle under test. Fragment bundles inherit all imported packages from the host bundle. In addition the fragment bundle must import the `org.junit` package with a minimum version of 4.0.0 specified. The following code snippet shows the MANIFEST.MF file of the test fragment for the `org.eclipse.smarthome.core` bundle. This way all test dependencies are available in the test classes (JUnit, hamcrest, mockito).

    Manifest-Version: 1.0
    Bundle-ManifestVersion: 2
    Bundle-Name: Tests for the Eclipse SmartHome Core
    Bundle-SymbolicName: org.eclipse.smarthome.core.test
    Bundle-Version: 0.11.0.qualifier
    Bundle-Vendor: Eclipse.org/SmartHome
    Fragment-Host: org.eclipse.smarthome.core
    Bundle-RequiredExecutionEnvironment: JavaSE-1.8
    Import-Package: groovy.lang,
     org.codehaus.groovy.reflection,
     org.codehaus.groovy.runtime,
     org.codehaus.groovy.runtime.callsite,
     org.codehaus.groovy.runtime.typehandling,
     org.eclipse.smarthome.core.library.items,
     org.eclipse.smarthome.core.library.types,
     org.eclipse.smarthome.test,
     org.eclipse.smarthome.test.java,
     org.hamcrest;core=split,
     org.junit;version="4.0.0",
     org.junit.runner,
     org.junit.runners,
     org.mockito,
     org.osgi.service.cm

Tests are typically placed inside the folder `src/test/java`. 

Unit tests
---

Each class with a name which ends with `Test`, inside the *test* folder will have all public methods with a `@Test` annotation  automatically executed as a test. Inside the class one can refer to all classes from the host bundle and all imported classes. The following code snippet shows a simple JUnit test which tests the `toString` conversation of a PercentType.

```(java)
public class PercentTypeTest {
    @Test
    public void DoubleValue() {
        PercentType pt = new PercentType("0.0001");
        assertEquals("0.0001", pt.toString());
    }
}
```

Using the [hamcrest matcher library](http://hamcrest.org/JavaHamcrest/) is a good way to write expressive assertions. In contrast to the original assertion statements from JUnit the hamcrest matcher library allows to define the assertion in a more natural order:

```(java)
PercentType pt = new PercentType("0.0001");
assertThat(pt.toString(), is(equalTo("0.0001")));
```

Assertions
---

Here is small example on when to use Hamcrest or JUnit assertions.
In general Hamcrest should be favoured over JUnit as for the more advanced and detailed error output:

```(java)
import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.collection.IsCollectionWithSize.hasSize;
import static org.hamcrest.core.IsCollectionContaining.hasItem;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.StringContains.containsString;
...
@Test
public void assertionsToBeUsed() {
    // use JUnit assertions for very basic checks:
    assertNotNull(new Object());
    assertNull(null);

    boolean booleanValue = true;
    assertTrue(booleanValue); // test boolean values only, no conditions or constraints

    // use Hamcrest assertions for everything else:
    assertThat("myString", is("myString"));
    assertThat("myString", is(instanceOf(String.class)));
    assertThat("myString", containsString("yS"));
    assertThat(Arrays.asList("one", "two"), hasItem("two"));
    assertThat(Arrays.asList("one", "two"), hasSize(2));

    // also valuable for null/boolean checks as the error output is advanced:
    assertThat(null, is(nullValue()));
    assertThat(new Object(), is(not(nullValue())));
    assertThat(true, is(not(false)));
} 
```

OSGi Tests
---

In addition to plain unit tests more advanced OSGi tests are provided.
Those should be used sparingly as the setup is more complex and introduces execution overhead.
Most situations can be tested using mocks (see [Mockito](#mockito)).

In the OSGi context of Eclipse SmartHome test execution must always be run inside an OSGi runtime. Eclipse PDE Plugin allows to run the JUnit test classes as `Plug-in test` but the required bundles have to be selected first:
The most easy way to execute tests in a test fragment is to use the provided launch configuration from the binding test archetype. This may be modified in the `Run Configurations...` menu to match the required bundles/plug-ins.
Another way is to create a test/package/bundle specific lanuch configuration with the following steps:
- Select the test class/package or bundle
- In context menu select `Run as -> JUnit Plug-in Test`
- after test run (which might fail due to unmet dependencies) select the configuration in `Run Configurations...`
- select `plug-ins selected below only` in the `Plug-ins` tab then `Deselect all`
- search for your test fragment bundle and enable it, then clear the search field (important to enable the action buttons again)
- select `Add Required Plug-ins`, then `Apply`, then `Run`
- since the `Add Required Plug-ins` action is a little overeager it will also select other `.test` fragments which you may be required to deselect manually.

From maven one can execute the test with `mvn install` command from the folder of the test fragment bundle.

Mockito
---
In order to keep unit tests as focused as possible we use the mocking framework [https://github.com/mockito/mockito Mockito]. Mockito lets us verify interactions between supporting classes and the unit under test and additionally supports stubbing of method calls for these classes. Please read the very short but expressive introduction on the [http://site.mockito.org/ Mockito homepage] in addition to this small example:

```(java)
public class MyBindingHandlerTest {

    private ThingHandler handler;

    @Mock
    private ThingHandlerCallback callback;

    @Mock
    private Thing thing;

    @Before
    public void setUp() {
        initMocks(this);
        handler = new MyBindingHandler(thing);
        handler.setCallback(callback);
    }
    
    @After
    public void tearDown() {
        // Free any resources, like open database connections, files etc.
        handler.dispose();
    }

    @Test
    public void initializeShouldCallTheCallback() {
        // we expect the handler#initialize method to call the callback during execution and
        // pass it the thing and a ThingStatusInfo object containing the ThingStatus of the thing.
        handler.initialize();

        // verify the interaction with the callback.
        // Check that the ThingStatusInfo given as second parameter to the callback was build with the ONLINE status:
        verify(callback).statusUpdated(eq(thing), argThat(arg -> arg.getStatus().equals(ThingStatus.ONLINE)));
    }

}
```

The code shown above will be created for you once you run the extensions/binding/create_binding_skeleton.[sh|cmd] script. See the OSGi-Tests section for another example.

_Groovy - DEPRECATED_
---
_The use of groovy is deprecated and should not be further extended. The existing groovy tests should be migrated over time. This way we want to reduce complexity in project setup and tooling. The mocking capabilities of groovy will be replaced by the java framework mockito._

OSGi-Tests
---
Some components of Eclipse SmartHome are heavily bound to the OSGi runtime, because they use OSGi core services like the EventAdmin or the ConfigurationAdmin. That makes it hard to test those components outside of the OSGi container. Equinox provides a possibility to execute a JUnit test inside the OSGi environment, where the test has access to OSGi services.

Eclipse SmartHome comes with an abstract base class `JavaOSGiTest` for OSGi tests. The base class sets up a bundle context and has convenience methods for registering mocks as OSGi services and the retrieval of registered OSGi services. Public methods with a @Test annotation will automatically be executed as OSGi tests, as long as the class-name ends with `Test`. The following JUnit/Mockito test class shows how to test the `ItemRegistry` by providing a mocked `ItemProvider`.

```(java)
import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.collection.IsCollectionWithSize.hasSize;
import static org.junit.Assert.assertThat;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.initMocks;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.smarthome.core.items.Item;
import org.eclipse.smarthome.core.items.ItemProvider;
import org.eclipse.smarthome.core.items.ItemRegistry;
import org.eclipse.smarthome.core.library.items.SwitchItem;
import org.eclipse.smarthome.test.java.JavaOSGiTest;
import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;

import com.google.common.collect.Lists;

public class JavaItemRegistryOSGiTest extends JavaOSGiTest {

    private static String ITEM_NAME = "switchItem";
    private ItemRegistry itemRegistry;

    @Mock
    private ItemProvider itemProvider;

    @Before
    public void setUp() {
        initMocks(this);
        itemRegistry = getService(ItemRegistry.class);
        when(itemProvider.getAll()).thenReturn(Lists.newArrayList(new SwitchItem(ITEM_NAME)));
    }

    @Test
    public void getItemsShouldReturnItemsFromRegisteredItemProvider() {
        assertThat(itemRegistry.getItems(), hasSize(0));

        registerService(itemProvider);

        List<Item> items = new ArrayList<>(itemRegistry.getItems());
        assertThat(items, hasSize(1));
        assertThat(items.get(0).getName(), is(equalTo(ITEM_NAME)));

        unregisterService(itemProvider);

        assertThat(itemRegistry.getItems(), hasSize(0));
    }
}
```

In the `setUp` method all mocks (annotated with @Mock) are created. This is `itemProvider` for this test. Then the `ItemRegistry` OSGi service is retrieved through the method `getService` from the base class `OSGiTest` and assigned to a private variable. Then the `ItemProvider` mock is configured to return a list with one SwitchItem when `itemProvider#getAll` gets called. The test method first checks that the registry delivers no items by default. Afterwards it registers the mocked `ItemProvider` as OSGi service with the method `registerService` and checks if the `ItemRegistry` returns one item now. At the end the mock is unregistered again.

In Eclipse the tests can be executed by right-clicking the test file and clicking on `Run As => JUnit Plug-In Test`. The launch config must be adapted, by selecting the bundle to test under the `Plug-Ins` tab and by clicking on `Add Required Plug-Ins`. Moreover you have to set the Auto-Start option to `true`. If the bundle that should be tested makes use of declarative services (has xml files in OSGI-INF folder), the bundle `org.eclipse.equinox.ds` must also be selected and also the required Plug-Ins of it. The `Validate Plug-Ins` button can be used to check if the launch config is valid. To avoid the manual selection of bundles, one can also choose `all workspace and enabled target plug-ins` with default `Default Auto-Start` set to `true`. The disadvantage is that this will start all bundles, which makes the test execution really slow and will produce a lot of errors on the OSGi console. It is a good practice to store a launch configuration file that launches all test cases for a test fragment.

From maven the test can be executed by calling `mvn integration-test`. For executing the test in maven, tycho calculates the list of depended bundles automatically from package imports. Only if there is no dependency to a bundle, the bundle must be added manually to the test execution environment. For example Eclipse SmartHome makes use of OSGi declarative services. That allows to define service components through XML files. In order to support declarative services in the test environment the according bundle `org.eclipse.equinox.ds` must be added in the pom file within the `tycho-surefire-plugin` configuration section as dependency and furthermore the startlevel has to be defined as shown below. The snippet also shows how to enable `logging` during the test-execution with maven. Therefor you have to add the bundles `ch.qos.logback.classic, ch.qos.logback.core ch.qos.logback.slf4j` as dependency to your tycho-surefire configuration.

    ...
    <build>
     <plugins>
         <plugin>
             <groupId>org.eclipse.tycho</groupId>
             <artifactId>tycho-surefire-plugin</artifactId>
             <version>${tycho-version}</version>
             <configuration>
                 <dependencies>
                     <dependency>
                         <type>eclipse-plugin</type>
                         <artifactId>org.eclipse.equinox.ds</artifactId>
                         <version>0.0.0</version>
                     </dependency>
                     <!-- Required Bundles to enable LOGGING -->
                     <dependency>
                         <type>eclipse-plugin</type>
                         <artifactId>ch.qos.logback.classic</artifactId>
                         <version>0.0.0</version>
                     </dependency>
                     <dependency>
                         <type>eclipse-plugin</type>
                         <artifactId>ch.qos.logback.core</artifactId>
                         <version>0.0.0</version>
                     </dependency>
                     <dependency>
                         <type>eclipse-plugin</type>
                         <artifactId>ch.qos.logback.slf4j</artifactId>
                         <version>0.0.0</version>
                     </dependency>
                 </dependencies>
                 <bundleStartLevel>
                     <bundle>
                         <id>org.eclipse.equinox.ds</id>
                         <level>1</level>
                         <autoStart>true</autoStart>
                     </bundle>
                 </bundleStartLevel>
             </configuration>
         </plugin>
     </plugins>
    </build>
    ...
    
In the dependency definition the `artifactId` is the name of the required bundle, where the version can always be `0.0.0`. Within the `bundleStartLevel` definition the start level and auto start of the depended bundles can be configured. The `org.eclipse.equinox.ds` bundle must have level 1 and must be started automatically.

Common errors
---

### Failed to execute goal org.eclipse.tycho:tycho-surefire-plugin:XXX:test (default-test) on project XXX: No tests found.

Maven might report this error when building your project, it means that the surefire plugin cannot find any tests to execute, please check the following details:

* Did you add any test classes with a class-name which ends with `Test` (singular)
* Did you annotate any methods with `@Test`
---
layout: documentation
---

{% include base.html %}

# Bridge Handler Implementation

A `BridgeHandler` handles the communication between the Eclipse SmartHome framework and a *bridge*  (a device that acts as a gateway to enable the communication with other devices) represented by a `Bridge` instance.
 
A bridge handler has the same properties as thing handler. Therefore, the `BridgeHandler` interface extends the `ThingHandler` interface.
 
## The BaseBridgeHandler

Eclipse SmartHome provides an abstract implementation of the `BridgeHandler` interface named `BaseBridgeHandler`. It is recommended to use this class, because it covers a lot of common logic.


## Life cycle

A `BridgeHandler` has the same life cycle than a `ThingHandler` (created by a `ThingHandlerFactory`, well defined life cycle by handler methods `initialize()` and `dispose()`, see chapter [Life Cycle](thing-handler.html#life-cycle)). A bridge acts as a gateway in order to provide access to other devices, the *child things*. Hence, the life cycle of a child handler depends on the life cycle of a bridge handler. Bridge and child handlers are subject to the following restrictions: 

- A `BridgeHandler` of a bridge is initialized before `ThingHandler`s of its child things are initialized.
- A `BridgeHandler` is disposed after all `ThingHandler`s of its child things are disposed.     


## Handler initialization notification
A `BridgeHandler` is notified about the initialization and disposal of child things. Therefore, the `BridgeHandler` interface provides the two methods `childHandlerInitialized(ThingHandler, Thing)` and `childHandlerDisposed(ThingHandler, Thing)`.  

These methods can be used to allocate and deallocate resources for child things.
---
layout: documentation
---

{% include base.html %}

# Handling Code Dependencies

## Eclipse SmartHome Packages

When implementing a binding, you should make sure that you do not introduce too many dependencies on different parts of Eclipse SmartHome. The following list of Java packages should suffice (if you use [create binding scripts](https://github.com/eclipse/smarthome/tree/master/extensions/binding) to create a binding these packages will be automatically added as imports in the manifest):  

 - org.eclipse.smarthome.config.core  
 - org.eclipse.smarthome.core.library.types  
 - org.eclipse.smarthome.core.thing  
 - org.eclipse.smarthome.core.thing.binding  
 - org.eclipse.smarthome.core.thing.binding.builder  
 - org.eclipse.smarthome.core.thing.type  
 - org.eclipse.smarthome.core.types  
 - org.eclipse.smarthome.core.util  
 
Depending on the kind of communication that you need to implement, you can optionally also add any exported packages from these bundles:

 - org.eclipse.smarthome.config.discovery
 - org.eclipse.smarthome.io.transport.mdns
 - org.eclipse.smarthome.io.transport.mqtt
 - org.eclipse.smarthome.io.transport.serial
 - org.eclipse.smarthome.io.transport.upnp
 
## Optional Bundles

You might also have the need to use other libraries for specific use cases like XML processing etc. In order to not have every binding use a different library, the following packages are available by default: 

### For XML Processing  
 - com.thoughtworks.xstream  
 - com.thoughtworks.xstream.annotations  
 - com.thoughtworks.xstream.converters  
 - com.thoughtworks.xstream.io  
 - com.thoughtworks.xstream.io.xml  

### For JSON Processing  
 - com.google.gson.*  
 
### For HTTP Operations  
 - org.eclipse.jetty.client.*  
 - org.eclipse.jetty.client.api.*  
 - org.eclipse.jetty.http.*  
 - org.eclipse.jetty.util.*  
 
Note: HttpClient instances should be obtained by the handler factory through the `HttpClientFactory` service and unless there are specific configuration requirements, the shared instance should be used.
 
### For Web Socket Operations  
 - org.eclipse.jetty.websocket.client  
 - org.eclipse.jetty.websocket.api
 
Note: WebSocketClient instances should be obtained by the handler factory through the `WebSocketClientFactory` service and unless there are specific configuration requirements, the shared instance should be used.

## 3rd Party Libraries

If you want your binding to rely on a custom library that might not even be an OSGi bundle, you can embed it in your bundle as a jar file following these steps: 

 - Put your jar file in the file system of your project (e.g. ```lib/library.jar```).
 - Add the new library to the ```bin.includes``` section of your [build.properties](http://help.eclipse.org/luna/index.jsp?topic=/org.eclipse.pde.doc.user/reference/pde_feature_generating_build.htm) file 
 to make sure that the library will be included in the binary.
 - To compile the binding in Eclipse, you have to add the library to your ```.classpath``` as well. Do this by adding a new classpath entry:
 `<classpathentry kind="lib" path="lib/library.jar"/>` 
 - Add the library project to the bundle classpath in MANIFEST.MF file  
  ```Bundle-ClassPath: .,
      lib/library.jar```
	  
Keep in mind that if you want to use third party libraries they have to be compatible with the [list of licenses approved for use by third-party code redistributed by Eclipse projects](https://eclipse.org/legal/eplfaq.php#3RDPARTY).  
Every bundle must contain an [NOTICE](https://www.eclipse.org/projects/handbook/#legaldoc) file, listing the 3rd party libraries and their licenses.
---
layout: documentation
---

{% include base.html %}

# Implementing a Discovery Service

Bindings can implement the `DiscoveryService` interface and register it as an OSGi service to inform the framework about devices and services, that can be added as things to the system (see also [Inbox & Discovery Concept](../../concepts/discovery.html)).

A discovery service provides discovery results.
The following table gives an overview about the main parts of a `DiscoveryResult`: 

| Field | Description |
|-------|-------------|
| `thingUID` | The `thingUID` is the unique identifier of the specific discovered thing (e.g. a device's serial number). It  *must not* be constructed out of properties, that can change (e.g. IP addresses). A typical `thingUID` could look like this: `hue:bridge:001788141f1a` 
| `thingTypeUID` | Contrary to the `thingUID` is the `thingTypeUID` that specifies the type the discovered thing belongs to. It could be constructed from e.g. a product number. A typical `thingTypeUID` could be the following: `hue:bridge`. 
| `bridgeUID` | If the discovered thing belongs to a bridge, the `bridgeUID` contains the UID of that bridge. 
| `properties` | The `properties` of a `DiscoveryResult` contain the configuration for the newly created thing. 
| `label` | The human readable representation of the discovery result. Do not put IP/MAC addresses or similar into the label but use the special `representationProperty` instead. |
| `representationProperty` | The name of one of the properties which discriminates the discovery result best against other results of the same type. Typically this is a serial number, IP or MAC address. The representationProperty often matches a configuration parameter and is also explicitly given in the thing-type definition. |

To simplify the implementation of own discovery services, an abstract base class `AbstractDiscoveryService` implements the `DiscoveryService`, that must only be extended.
Subclasses of `AbstractDiscoveryService` do not need to handle the `DiscoveryListeners` themselves, they can use the methods `thingDiscovered` and `thingRemoved` to notify the registered listeners.
Most of the descriptions in this chapter refer to the `AbstractDiscoveryService`.

For UPnP and mDNS there already are generic discovery services available.
Bindings only need to implement a `UpnpDiscoveryParticipant` resp. `mDNSDiscoveryParticipant`.
For details refer to the chapters [UPnP Discovery](#upnp-discovery) and [mDNS Discovery](#mdns-discovery). 

The following example is taken from the `HueLightDiscoveryService`, it calls `thingDiscovered` for each found light.
It uses the `DiscoveryResultBuilder` to create the discovery result. 

```java
    private void onLightAddedInternal(FullLight light) {
        ThingUID thingUID = getThingUID(light);
        if (thingUID != null) {
            ThingUID bridgeUID = hueBridgeHandler.getThing().getUID();
            Map<String, Object> properties = new HashMap<>(1);
            properties.put(LIGHT_ID, light.getId());
            DiscoveryResult discoveryResult = DiscoveryResultBuilder.create(thingUID).withProperties(properties)
                    .withBridge(bridgeUID).withLabel(light.getName()).build();
            thingDiscovered(discoveryResult);
        } else {
            logger.debug("discovered unsupported light of type '{}' with id {}", light.getModelID(), light.getId());
        }
    }
```

The discovery service needs to provide the list of supported thing types, that can be found by the discovery service.
This list will be given to the constructor of `AbstractDiscoveryService` and can be requested by using `DiscoveryService#getSupportedThingTypes` method. 

## Registering as an OSGi service

The `Discovery` class of a binding which implements `AbstractDiscoveryService` should be annotated with

```java
@Component(service = DiscoveryService.class, immediate = true, configurationPid = "discovery.<bindingID>")
```

where `<bindingID>` is the id of the binding, i.e. `astro` for the Astro binding.
Such a registered service will be picked up automatically by the framework.

## Discovery 

### Background Discovery 

If the implemented discovery service enables background discovery, the `AbstractDiscoveryService` class automatically starts it.
If background discovery is enabled, the framework calls `AbstractDiscoveryService#startBackgroundDiscovery` when the binding is activated and `AbstractDiscoveryService#stopBackgroundDiscovery` when the component is deactivated.
The default implementations of both methods are empty and could be overridden by the binding developer.
Depending on the concrete implementation the discovery service might start and stop a scheduler in these method or register a listener for an external protocol.
The `thingDiscovered` method can be used to notify about a newly discovered thing.

The following example shows the implementation of the above mentioned methods in the Wemo binding. 

```java
    @Override
    protected void startBackgroundDiscovery() {
        logger.debug("Start WeMo device background discovery");
        if (wemoDiscoveryJob == null || wemoDiscoveryJob.isCancelled()) {
            wemoDiscoveryJob = scheduler.scheduleWithFixedDelay(wemoDiscoveryRunnable, 0, refreshInterval, TimeUnit.SECONDS);
        }
    }

    @Override
    protected void stopBackgroundDiscovery() {
        logger.debug("Stop WeMo device background discovery");
        if (wemoDiscoveryJob != null && !wemoDiscoveryJob.isCancelled()) {
            wemoDiscoveryJob.cancel(true);
            wemoDiscoveryJob = null;
        }
    }
```

### Active Scan

If the user triggers an active scan for a binding or specific set of thing types, the method `startScan` of each discovery service which supports these thing type is called.
Within these methods the things can be discovered.
The abstract base class automatically starts a thread, so the implementation of this method can be long-running.

The following example implementation for `startScan` is taken from the `HueLightDiscoveryService`, that triggers a scan for known and also for new lights of the hue bridge.
Already discovered things are identified by the ThingUID the DiscoveryResult was created with, and won't appear in the inbox again.

```java
    @Override
    public void startScan() {
        List<FullLight> lights = hueBridgeHandler.getFullLights();
        if (lights != null) {
            for (FullLight l : lights) {
                onLightAddedInternal(l);
            }
        }
        // search for unpaired lights
        hueBridgeHandler.startSearch();
    }
```

### Re-Discovered Results and Things

The `getThingUID` method of the discovery service should create a consistent UID every time the same thing gets discovered.
This way existing discovery results and existing things with this UID will be updated with the properties from the current scan.
With this, dynamic discoveries (like UPnP or mDNS) can re-discover existing things and update communication properties like host names or TCP ports.

### Remove older results

Normally, older discovery results already in the inbox are left untouched by a newly triggered scan.
If this behavior is not appropriate for the implemented discovery service, one can override the method `stopScan` to call `removeOlderResults` as shown in the following example from the Hue binding: 

```java
    @Override
    protected synchronized void stopScan() {
        super.stopScan();
        removeOlderResults(getTimestampOfLastScan());
    }
```

## UPnP Discovery

UPnP discovery is implemented in the framework as `UpnpDiscoveryService`.
It is widely used in bindings. To facilitate the development, binding developers only need to implement a `UpnpDiscoveryParticipant`.
Here the developer only needs to implement three simple methods: 

- `getSupportedThingTypeUIDs` - Returns the list of thing type UIDs that this participant supports.
The discovery service uses this method of all registered discovery participants to return the list of currently supported thing type UIDs. 
- `getThingUID` - Creates a thing UID out of the UPnP result or returns `null` if this is not possible.
This method is called from the discovery service during result creation to provide a unique thing UID for the result. 
- `createResult` - Creates the `DiscoveryResult` out of the UPnP result.
This method is called from the discovery service to create the actual discovery result.
It uses the `getThingUID` method to create the thing UID of the result. 

The following example shows the implementation of the UPnP discovery participant for the Hue binding, the `HueBridgeDiscoveryParticipant`. 

```java
public class HueBridgeDiscoveryParticipant implements UpnpDiscoveryParticipant {

    @Override
    public Set<ThingTypeUID> getSupportedThingTypeUIDs() {
        return Collections.singleton(THING_TYPE_BRIDGE);
    }

    @Override
    public DiscoveryResult createResult(RemoteDevice device) {
        ThingUID uid = getThingUID(device);
        if (uid != null) {
            Map<String, Object> properties = new HashMap<>(2);
            properties.put(HOST, device.getDetails().getBaseURL().getHost());
            properties.put(SERIAL_NUMBER, device.getDetails().getSerialNumber());

            DiscoveryResult result = DiscoveryResultBuilder.create(uid).withProperties(properties)
                    .withLabel(device.getDetails().getFriendlyName()).withRepresentationProperty(SERIAL_NUMBER).build();
            return result;
        } else {
            return null;
        }
    }

    @Override
    public ThingUID getThingUID(RemoteDevice device) {
        DeviceDetails details = device.getDetails();
        if (details != null) {
            ModelDetails modelDetails = details.getModelDetails();
            if (modelDetails != null) {
                String modelName = modelDetails.getModelName();
                if (modelName != null) {
                    if (modelName.startsWith("Philips hue bridge")) {
                        return new ThingUID(THING_TYPE_BRIDGE, details.getSerialNumber());
                    }
                }
            }
        }
        return null;
    }
}
```

## mDNS Discovery

mDNS discovery is implemented in the framework as `MDNSDiscoveryService`.
To facilitate the development, binding developers only need to implement a `MDNSDiscoveryParticipant`.
Here the developer only needs to implement four simple methods: 

- `getServiceType` - Defines the [mDNS service type](http://www.dns-sd.org/ServiceTypes.html).
- `getSupportedThingTypeUIDs` - Returns the list of thing type UIDs that this participant supports.
The discovery service uses this method of all registered discovery participants to return the list of currently supported thing type UIDs. 
- `getThingUID` - Creates a thing UID out of the mDNS service info or returns `null` if this is not possible.
This method is called from the discovery service during result creation to provide a unique thing UID for the result. 
- `createResult` - Creates the `DiscoveryResult` out of the UPnP result.
This method is called from the discovery service to create the actual discovery result.
It uses the `getThingUID` method to create the thing UID of the result. 
---
layout: documentation
---

{% include base.html %}

# Documenting a Binding

A binding should come with some documentation in form of a ```README.md``` file (in markdown syntax) within its project folder.
If a single file is not enough, additional resources (e.g. further md-files, images, example files) can be put in a ```doc``` folder.
To facilitate reviews and diffs, there should be a new line for every sentence within a paragraph.
Such line breaks won't have any impact on the rendering, but they immensely help for the maintenance.

__Note__: As the ```README.md``` pages might be used on Jekyll-based websites, it is important to also respect the following formatting rules:

- There must be an empty line after every header (`#...`).
- There must be an empty line before and after every list.
- There must be an empty line before and after every code section.

Neither the ```README.md``` file nor the ```doc``` folder must be added to ```build.properties```, i.e. they only exist in the source repo, but should not be packaged within the binary bundles.

It is planned to generate parts of the documentation based on the files that are available with the ```ESH-INF``` folder of the binding.
As this documentation generation is not (yet) in place, the documentation currently needs to be maintained fully manually.
The Maven archetype creates a [template for the binding documentation](https://github.com/eclipse/smarthome/blob/master/tools/archetype/binding/src/main/resources/archetype-resources/README.md).
---
layout: documentation
---

{% include base.html %}

# Frequently Asked Questions (FAQs)

Here is a list of frequently asked questions around the development of bindings. If you do not find an answer to your question, do not hesitate to ask it on the support forum.

### Structuring Things and Thing Types

1. _I am implementing a binding for system X. Shall I design this as one Thing or as a Bridge with multiple Things for the different functionalities?_ 
  
    In general, both options are valid:

    1. You have one Thing which has channels for all your actors, sensors and other functions
    2. You have one Bridge and an additional Thing for every actor and sensor and they would hold the channels

    The preferred architecture is the latter, if this is feasible. This means that the physical devices should be represented by a Thing each. This only makes sense if your system allows you to identify the different physical devices at all. Especially, such an architecture is useful if you can do a discovery of new devices that could then be presented to the user/admin.
    
    If your system does not provide you any possibility to get hold of such information, but rather only shows you a "logical" view of it, then 1) is also a valid option to pursue.
  
2. _Do I have to create XML files in `ESH-INF/thing` for all devices or is there any other option?_

    No, the XML files are only one way to describe your devices. Alternatively, you can implement your own [ThingTypeProvider](https://github.com/eclipse/smarthome/blob/master/bundles/core/org.eclipse.smarthome.core.thing/src/main/java/org/eclipse/smarthome/core/thing/binding/ThingTypeProvider.java), through which you can provide thing descriptions in a programmatic way. Nonetheless, the static XML descriptions of thing types can be picked up for documentation generation and other purposes. So whenever possible, static XML descriptions should be provided. 

3. _For my system XY, there are so many different variants of devices. Do I really need to define a thing type for every single one of them?_

    Thing types are important if you have no chance to request any structural information about the devices from your system and if you need users to manually chose a thing to add or configure (i.e. there is also no automatic discovery). The thing types that you provide will be the list the user can choose from. If your system supports auto-discovery and you can also dynamically construct things (and their channels) from structural information that you can access during runtime, there is in theory no need to provide any thing type description at all. Nonetheless, static descriptions of thing types have the advantage that the user knows which kind of devices are supported, no matter if he has a device at home or not - so you should at least have static XML descriptions for the devices that are known to you at implementation time.
     
4. _I have a device that can have different firmware versions with slightly different functionality. Should I create one or two thing types for it?_
   
    If the firmware version makes a huge difference for the device (and can be seen as a different model of it), then it is ok to have different things defined. If the list of channels can be determined by knowing the firmware revision, this is good. If you can only determine the existing channels by querying the device itself, it might be the better option to have only one thing type and construct its channels upon first access.

5. _When creating a Thing through my ThingHanderFactory, does it exactly have to have the channels that are defined in the thing type description?_
 
    It must at least have the channels that are defined in its thing type (and they are already automatically added by the super() implementation). Nonetheless, you are free to add any number of additional channels to the thing.

### State Updates of Channels

1. I have an image in my binding and want to pass it to the framework. What is the best way to achieve this?

    The Thing that wants to provide the image should have a Channel defined with `<item-type>Image</item-type>`.
The `ThingHandler` can update this Channel with a state of type `RawType` that represents the raw bytes of the image.
If the image should be downloaded from a URL, the helper method `HttpUtil.downloadImage(URL url)` can be used.
A user may link this Channel to an Item of type `Image` which can then be displayed.
Please note that data put as a `RawType` in a Channel will stay in **memory only**, i.e., this data will **not** be persisted anywhere.
Also keep in mind that the memory needed for these images will be consumed on the server running the framework, so creating a lot of `RawType` channels is not recommended.
---
layout: documentation
---

{% include base.html %}

# Implementing a Binding

A binding is an extension to the Eclipse SmartHome runtime that integrates an external system like a service, a protocol or a single device. Therefore the main purpose of a binding is to translate events from the Eclipse SmartHome event bus to the external system and vice versa. The external system is represented as a set of *Things*. For each *Thing* the binding must provide a proper `ThingHandler` implementation that is able to handle the communication.

In this tutorial you will learn how to implement a simple binding and you will get familiar with important concepts and APIs of Eclipse SmartHome. The [Yahoo Weather Binding](https://github.com/eclipse/smarthome/tree/master/extensions/binding/org.eclipse.smarthome.binding.yahooweather) is taken as example.

## Structure of a Binding

The structure of a binding follows the structure of a typical OSGi bundle project. Therefore there exists a `MANIFEST.MF` file inside the `META-INF` folder and other OSGi artefacts like the `build.properties` file. In the `ESH-INF` folder XML configuration files for Eclipse SmartHome are located. The Java source code is under `src/main/java`.

The structure of the Yahoo Weather Binding:

```
|- ESH-INF
|---- binding
|------- binding.xml
|---- thing
|------- thing-types.xml
|- META-INF
|---- MANIFEST.MF
|- OSGI-INF
|---- YahooWeatherHandlerFactory.xml
|- src
|---- main
|------- java
|---------- [...]
|- build.properties
|- pom.xml
```

## Binding Definition

Every binding needs to define a `binding.xml` file, which is located in the folder `/ESH-INF/binding/`. In this file meta information for a binding like the author and a description, that are accessible at runtime, can be defined. The binding ID is a unique identifier for the binding. The following `binding.xml` shows the binding definition of the Yahoo Weather Binding:

```xml
<binding:binding id="yahooweather"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:binding="http://eclipse.org/smarthome/schemas/binding/v1.0.0"
        xsi:schemaLocation="http://eclipse.org/smarthome/schemas/binding/v1.0.0 http://eclipse.org/smarthome/schemas/binding-1.0.0.xsd">

    <name>YahooWeather Binding</name>
    <description>The Yahoo Weather Binding requests the Yahoo Weather Service
		to show the current temperature, humidity and pressure.</description>
    <author>Kai Kreuzer</author>

</binding:binding>
```

## Describing Things

External systems are represented as *Things* in the Eclipse SmartHome runtime. When starting the implementation of an Eclipse SmartHome binding, you should think about the abstraction of your external system. Different services or devices should be represented as individual *Things* described by a *ThingType*. Each functionality of the *Thing* should be modelled as a `Channel`. A binding should define all *ThingTypes* that are supported by that binding.

Eclipse SmartHome allows you to define your *ThingTypes* in a declarative way through XML files. The XML files must be located at `/ESH-INF/thing/`. A *ThingType* definition must contain the UID and optionally a description and a manufacturer. Moreover, supported channels must be specified. For channels it is important to specify which type of *Item* can be linked to the *Channel*. Below an excerpt of the Yahoo Weather service *ThingType* definition is shown:

```xml
<thing-type id="weather">
    <label>Weather Information</label>
    <description>Provides various weather data from the Yahoo service</description>
    <channels>
        <channel id="temperature" typeId="temperature" />
    </channels>
    <config-description>
        <parameter name="location" type="integer" required="true">
            <label>Location</label>
            <description>Location for the weather information.
                Syntax is WOEID, see https://en.wikipedia.org/wiki/WOEID.
            </description>
        </parameter>
        <parameter name="refresh" type="integer" min="1">
            <label>Refresh interval</label>
            <description>Specifies the refresh interval in seconds.</description>
            <default>60</default>
        </parameter>
    </config-description>
</thing-type>

<channel-type id="temperature">
    <item-type>Number:Temperature</item-type>
    <label>Temperature</label>
    <description>Current temperature</description>
    <category>Temperature</category>
    <state readOnly="true" pattern="%.1f %unit%" />
</channel-type>
```

The channel type definition allows one to specify a category and additional meta information for the state of the linked item. 
Together with the definition of the `readOnly` attribute, user interfaces get an idea how to render an item for this channel.
For example, a channel with the category `Temperature` which is readable only, indicates that this is a sensor for temperature.
In that case the user interface can render an appropriate icon and label for the current value. 

The label is further described by the `state` tags `pattern` attribute: 
In this case the temperature should be rendered with one decimal place followed by the unit the binding specifies for the current measurement. 
The `Number:Temperature` item type describes this channels ability to send state updates using the type `QuantityType` with a value and a unit. 
For detailed information about _dimensions_ and _units_ see the [QuantityType definition](../../concepts/units-of-measurement.html#quantitytype). 

If the `readOnly` flag is set to `false` (which is the default value), the user interface could render a slider to change the temperature, since this means it is temperature actuator. 
Restrictions of the state such as the minimum or maximum value can also be specified.

In order to give user interfaces a chance to render good default UIs for things, the binding should specify as much meta data as possible. For a complete list of possible configuration options and categories please see the [Thing Definition](thing-definition.html#channels) section.

## The ThingHandlerFactory

The `ThingHandlerFactory` is responsible for creating `ThingHandler` instances. Every binding must implement a `ThingHandlerFactory` and register it as OSGi service so that the runtime knows which class needs to be called for creating and handling things. From the generated archetype there already exists a `ThingHandlerFactory`, which can be extended with further *ThingTypes*.

When a new *Thing* is added, the Eclipse SmartHome runtime queries every `ThingHandlerFactory` for support of the *ThingType* by calling the `supportsThingType` method. When the method returns `true`, the runtime calls `createHandler`, which should then return a proper `ThingHandler` implementation.

The `YahooWeatherHandlerFactory` supports only one *ThingType* and instantiates a new `YahooWeatherHandler` for a given thing:

```java
@NonNullByDefault
@Component(configurationPid = "binding.yahooweather", service = ThingHandlerFactory.class)
public class YahooWeatherHandlerFactory extends BaseThingHandlerFactory {
    
    private static final Collection<ThingTypeUID> SUPPORTED_THING_TYPES_UIDS = Collections.singleton(YahooWeatherBindingConstants.THING_TYPE_WEATHER);
    
    @Override
    public boolean supportsThingType(ThingTypeUID thingTypeUID) {
        return SUPPORTED_THING_TYPES_UIDS.contains(thingTypeUID);
    }

    @Override
    protected @Nullable ThingHandler createHandler(Thing thing) {
        ThingTypeUID thingTypeUID = thing.getThingTypeUID();

        if (YahooWeatherBindingConstants.THING_TYPE_WEATHER.equals(thingTypeUID)) {
            return new YahooWeatherHandler(thing);
        }

        return null;
    }
}
```

Constants like the `THING_TYPE_WEATHER` UID and also *Channel* UIDs are typically defined inside a public `BindingConstants` class.

Depending on your implementation, each *ThingType* may use its own handler. It is also possible to use the same handler for different *Things*, or use different handlers for the same *ThingType*, depending on the configuration.

## The ThingHandler

The core part of a binding is the `ThingHandler` implementation. The handler is responsible for translating Eclipse SmartHome commands and states to the external system and vice versa. 

### Handling Commands and Updating the State

For handling commands the `ThingHandler` interface defines the `handleCommand` method. This method is called when a command is sent to an item linked to a channel on a *Thing*. Inside the `handleCommand` method binding specific logic can be executed. The following code snippet shows the handle command method of the Yahoo Weather Binding:

```java
@Override
public void handleCommand(ChannelUID channelUID, Command command) {
    if (command instanceof RefreshType) {
        
        updateWeatherData();
        
        switch (channelUID.getId()) {
            case CHANNEL_TEMPERATURE:
                updateState(channelUID, getTemperature());
                break;
            case CHANNEL_HUMIDITY:
                [...]
        }
    }
}
```

When a `RefreshType` command is sent to the `ThingHandler` it updates the weather data by executing an HTTP call in the `updateWeatherData` method and sends a state update via the `updateState` method. This will update the state of the Item, which is linked to the channel for the given channel UID.

### Lifecycle

The `ThingHandler` has two important lifecycle methods: `initialize` and `dispose`. The `initialize` method is called when the handler is started and `dispose` just before the handler is stopped. Therefore these methods can be used to allocate and deallocate resources. For an example, the Yahoo Weather binding starts and stops a scheduled job within these methods.

### Configuration

*Things* can be configured with parameters. To retrieve the configuration of a *Thing* one can call `getThing().getConfiguration()` inside the `ThingHandler`. The configuration class has the equivalent methods as the `Map` interface, thus the method `get(String key)` can be used to retrieve a value for a given key. 

Moreover the configuration class has a utility method `as(Class<T> configurationClass)` that transforms the configuration into a Java object of the given type. All configuration values will be mapped to properties of the class. The type of the property must match the type of the configuration. Only the following types are supported for configuration values: `Boolean`, `String` and `BigDecimal`.

For example, the Yahoo Weather binding allows configuration of the location and the refresh frequency.

### Properties

*Things* can have properties. If you would like to add meta data to your thing, e.g. the vendor of the thing, then you can define your own thing properties by simply adding them to the thing type definition. The properties section [here](thing-definition.html#Properties) explains how to specify such properties.

To retrieve the properties one can call the operation `getProperties` of the corresponding `org.eclipse.smarthome.core.thing.type.ThingType` instance. If a thing will be created for this thing type then its properties will be automatically copied into the new thing instance. Therefore the `org.eclipse.smarthome.core.thing.Thing` interface also provides the `getProperties` operation to retrieve the defined properties. In contrast to the `getProperties` operation of the thing type instance the result of the thing´s `getProperties` operation will also contain the properties updated during runtime (cp. the thing handler [documentation](thing-handler.html)).

## Bridges

In the domain of an IoT system there are often hierarchical structures of devices and services. For example, one device acts as a gateway that enables communication with other devices that use the same protocol. In Eclipse SmartHome this kind of device or service is called *Bridge*. Philips Hue is one example of a system that requires a bridge. The Hue gateway is an IP device with an HTTP API, which communicates over the ZigBee protocol with the Hue bulbs. In the Eclipse SmartHome model the Hue gateway is represented as a *Bridge* with connected *Things*, that represent the Hue bulbs. *Bridge* inherits from *Thing*, so that it also has *Channels* and all other features of a thing, with the addition that it also holds a list of things.

When implementing a binding with *Bridges*, the logic to communicate with the external system is often shared between the different `ThingHandler` implementations. In that case it makes sense to implement a handler for the *Bridge* and delegate the actual command execution from the *ThingHandler* to the *BridgeHandler*. To access the *BridgeHandler* from the *ThingHandler*, call `getBridge().getHandler()`

The following excerpt shows how the `HueLightHandler` delegates the command for changing the light state to the `HueBridgeHandler`:

```java
@Override
public void handleCommand(ChannelUID channelUID, Command command) {

    HueBridgeHandler hueBridgeHandler = (HueBridgeHandler) getBridge().getHandler();

    switch (channelUID.getId()) {
        case CHANNEL_ID_COLOR_TEMPERATURE:
            StateUpdate lightState = lightStateConverter.toColorLightState(command);    
            hueBridgeHandler.updateLightState(getLight(), lightState);
            break;    
        case CHANNEL_ID_COLOR: 
            // ...
    }
}
```

Inside the `BridgeHandler` the list of *Things* can be retrieved via the `getThings()` call.

## Documentation

When you have finished the implementation of the binding, you should spend a minute to also document it. Please find some [details here](docs.html).
---
layout: documentation
---

{% include base.html %}

# Profiles

This section explains how custom `Profile`s can be created.
For a general explanation of Profiles, please see the [concept section](../../concepts/profiles.html).

## Profile Properties

A `Profile` is determined by its type, i.e. `StateProfileType` or `TriggerProfileType` and its `ProfileTypeUID`.
Both types are specified via interfaces `StateProfile` and `TriggerProfile`, respectively.

The `ProfileTypeUID` identifies one specific type of `Profile`.
Each `Profile` exists in a certain scope.
There are pre-defined `Profile`s that are defined in scope `ProfileTypeUID.SYSTEM_SCOPE`, which is "system".
Custom `Profiles` should be created in a different scope.
Thus a `ProfileTypeUID` can be created as follows: `new ProfileTypeUID("MyScope", "MyProfileName")`.

A `StateProfile` receives `Commands` and `StateUpdates` from the `ThingHandler` and from the `Item`.
It has to implement four methods that specify how the `Command`s or `StateUpdate`s should be handled.

A `TriggerProfile` makes it possible to link a `TriggerChannel` to an `Item`.
This `Profile` receives the `State` of the `Item` and the `Event` that has been triggered.

## ProfileTypeProvider

Custom `ProfileType`s have to be annouced by a `ProfileTypeProvider` to the framework via an OSGi service:

```java
@Component(service = { ProfileTypeProvider.class })
public class MyProfileTypeProvider implements ProfileTypeProvider {
    @Override
    public Collection<ProfileType> getProfileTypes(Locale locale) {
        //return custom types
    }
}
```

## ProfileFactory

The most important interface is the `ProfileFactory` which has to be implemented and announced as an OSGi service:

```java
@Component(service = { ProfileFactory.class })
public class MyProfileFactory implements ProfileFactory {
```

Such a factory is responsible for specific `ProfileTypeUID`s that should be returned by `Collection<ProfileTypeUID> getSupportedProfileTypeUIDs()`.
Further it is capable of creating these `Profile`s via `createProfile(ProfileTypeUID profileTypeUID, ProfileCallback callback, ProfileContext profileContext);`.

For convenience, the `ProfileFactory` and the `ProfileTypeProvider` can be put into one class and announce the two services:

```java
@Component(service = { ProfileFactory.class, ProfileTypeProvider.class })
public class MyProfileFactory implements ProfileFactory, ProfileTypeProvider {
```

### ProfileCallback

`Profile`s need the opportunity to notify the framework about what they did with the `Command`s and `StateUpdate`s it received from the framework.
The `ProfileCallback` provides methods to forward the results of a `Profile`s processing to the `ThingHandler` and to the `Framework`.
It should be injected into the `Profile` upon its creation.

### ProfileContext

Some more advanced `Profile`s which can be configured need access to their `Configuration` object.
This is offered via the `ProfileContext`.
A `ScheduledExecutorService` can also be retrieved via the `ProfileContext` in order to schedule long running tasks in a separate Thread.
The `ProfileContext` may also be injected into the `Profile` upon its creation.

## ProfileAdvisor

A `ProfileAdvisor` is an optional component which can be used to suggest a specific `ProfileTypeUID` for a given `Channel` or `ChannelType`.
Two methods have to be implemented to achieve this:

`ProfileTypeUID getSuggestedProfileTypeUID(Channel channel, @Nullable String itemType);`

`ProfileTypeUID getSuggestedProfileTypeUID(ChannelType channelType, @Nullable String itemType);`

## Using Profiles

### .items file

`Profiles`s can be specified as a parameter for a given channel:

```java
<item-type> MyItem { channel="<bindingID>:<thing-typeID>:MyThing:myChannel"[profile="MyScope:MyProfile"]}
```

## Existing Profiles

### FollowProfile

If one device should "follow" the actions of another device, the FollowProfile can be used. The term "follow" in this case means that any state that is sent to an `Item` will be forwarded from this `Item` to any linked channel with the FollowProfile. The FollowProfile takes state updates on an `Item` and sends them as a command onto the channel. In the direction from the ThingHandler towards the `Item`, the FollowProfile ignores state updates.

```java
<itemType> <itemName> { channel="<channelUID>", channel="<followChannelUID>"[profile="follow"]}
```

### OffsetProfile

The `OffsetProfile` provides the possibility to adjust a value from a device before it arrives at the framework.
An offset can be specified via the parameter `offset` which has to be a `QuantityType` or `DecimalType`.
A positive offset is the amount of change from the device towards the framework, i.e. all values from the device are increased by this offset and values sent to the device are decreased by this offset.
A negative offset subtracts the offset from the value sent by the device to the framework and adds the offset to values sent from the framework to the device.

```java
Number <itemName> { channel="<bindingID>:<thing-typeID>:<thingName>:<channelName>"[profile="offset", offset="<value>"]}
```
---
layout: documentation
---

{% include base.html %}

# Thing Type Definitions

In order to work with things, some meta information about them is needed. This is provided through 'ThingType' definitions, which describe details about their functionality and configuration options.

Technically, the thing types are provided by [ThingTypeProvider](https://github.com/eclipse/smarthome/blob/master/bundles/core/org.eclipse.smarthome.core.thing/src/main/java/org/eclipse/smarthome/core/thing/binding/ThingTypeProvider.java)s. 
Eclipse SmartHome comes with an implementation of such a provider that reads XML files from the folder `ESH-INF/thing` of bundles. Although we refer to this XML syntax in the following, you also have the option to provide directly object model instances through your own provider implementation. 
The same applies for the channel types. 
The [ChannelTypeProvider](https://github.com/eclipse/smarthome/blob/master/bundles/core/org.eclipse.smarthome.core.thing/src/main/java/org/eclipse/smarthome/core/thing/type/ChannelTypeProvider.java) interface can be registered as OSGi service to provide channel types programmatically. 
When implementing a dynamic `ThingTypeProvider` you can also refer to the channel types that are defined inside XML files.

## Things

Things represent devices or services that can be individually added to, configured or removed from the system. 
They either contain a set of channels or a set of channel groups. 
A bridge is a specific type of thing as it can additionally provide access to other Things as well. 
Which Things can be associated through which bridge type is defined within the description of a thing:

```xml
    <thing-type id="thingTypeID">
        <supported-bridge-type-refs>
            <bridge-type-ref id="bridgeTypeID" />
        </supported-bridge-type-refs>
        <label>Sample Thing</label>
        <description>Some sample description</description>
        <category>Lightbulb</category>
		...
    </thing-type>
```

Bindings may optionally set the listing of a thing type. By doing do, they indicate to user interfaces whether it should be shown to the users or not, e.g. when pairing things manually:

```xml
    <thing-type id="thingTypeID" listed="false">
        ...
    </thing-type>
```

Thing types are listed by default, unless specified otherwise. 
Hiding thing types potentially makes sense if they are deprecated and should not be used anymore. 
Also, this can be useful if users should not be bothered with distinguishing similar devices which for technical reasons have to have separate thing types. 
In that way, a generic thing type could be listed for users and a corresponding thing handler would change the thing type immediately to a more concrete one, handing over control to the correct specialized handler.

### Thing Categories

A description about thing categories as well as an overview about which categories exist can be found in our [categories overview](../../concepts/categories.html).

## Channels

A channel describes a specific functionality of a thing and can be linked to an item.
So the basic information is, which command types the channel can handle and which state it sends to the linked item.
This can be specified by the accepted item type.
Inside the thing type description XML file a list of channels can be referenced.
The channel type definition is specified on the same level as the thing type definition.
That way channels can be reused in different things.

The granularity of channel types should be on its semantic level, i.e. very fine-grained:
If a Thing measures two temperature values, one for indoor and one for outdoor, this should be modelled as two different channel types.
Overriding labels of a channel type must only be done if the very same functionality is offered multiple times, e.g. having an actuator with 5 relays, which each is a simple "switch", but you want to individually name the channels (1-5).

The following XML snippet shows a thing type definition with 2 channels and one referenced channel type:

```xml
<thing-type id="thingTypeID">
    <label>Sample Thing</label>
    <description>Some sample description</description>
    <channels>
        <channel id="switch" typeId="powerSwitch" />
        <channel id="temperature" typeId="setpointTemperature" />
    </channels>
</thing-type>
<channel-type id="setpointTemperature" advanced="true">
    <item-type>Number</item-type>
    <label>Setpoint Temperature</label>
    <category>Temperature</category>
    <state min="12" max="30" step="0.5" pattern="%.1f °C" readOnly="false" />
</channel-type>
```

In order to reuse identical channels in different bindings a channel type can be system-wide.
A channel type can be declared as system-wide by setting its `system` property to true and can then be referenced using a `system.` prefix in a `channel` `typeId` attribute in any binding - note that this should only be done in the core framework, but not by individual bindings!

The following XML snippet shows a system channel type definition and thing type definition that references it:

```xml
<thing-type id="thingTypeID">
    <label>Sample Thing</label>
    <description>Some sample description</description>
    <channels>
        <channel id="s" typeId="system.system-channel" />
    </channels>
</thing-type>
<channel-type id="system-channel" system="true">
    <item-type>Number</item-type>
    <label>System Channel</label>
    <category>QualityOfService</category>
</channel-type>
```

### System State Channel Types

There exist system-wide channel types that are available by default:

| Channel Type ID      | Reference typeId            | Item Type            | Category         | Description                                                                                                                                                                                                             |
|----------------------|-----------------------------|----------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| signal-strength      | system.signal-strength      | Number               | QualityOfService | Represents signal strength of a device as a Number with values 0, 1, 2, 3 or 4; 0 being worst strength and 4 being best strength.                                                                                       |
| low-battery          | system.low-battery          | Switch               | Battery          | Represents a low battery warning with possible values on (low battery) and off (battery ok).                                                                                                                                                           |
| battery-level        | system.battery-level        | Number               | Battery          | Represents the battery level as a percentage (0-100%). Bindings for things supporting battery level in a different format (e.g. 4 levels) should convert to a percentage to provide a consistent battery level reading. |
| power                | system.power                | Switch               | -                | Turn a device on/off.                                                                                                                                                                                                   |
| brightness           | system.brightness           | Dimmer               | Light            | Brightness of a bulb (0-100%).                                                                                                                                                                                          |
| color                | system.color                | Color                | ColorLight       | Color of a bulb.                                                                                                                                                                                                        |
| color-temperature    | system.color-temperature    | Dimmer               | ColorLight       | Color temperature of a bulb (0-100%). 0% should be the coldest setting (highest Kelvin value).                                                                                                                          |
| location             | system.location             | Location             | -                | Location in lat.,lon.,height coordinates.                                                                                                                                                                               |
| motion               | system.motion               | Switch               | Motion           | Motion detected by the device (ON if motion is detected).                                                                                                                                                               |
| mute                 | system.mute                 | Switch               | SoundVolume      | Turn on/off the volume of a device.                                                                                                                                                                                     |
| volume               | system.volume               | Dimmer               | SoundVolume      | Change the sound volume of a device (0-100%).                                                                                                                                                                           |
| media-control        | system.media-control        | Player               | MediaControl     | Control for a media player.                                                                                                                                                                                             |
| media-title          | system.media-title          | String               | -                | Title of a (played) media file.                                                                                                                                                                                         |
| media-artist         | system.media-artist         | String               | -                | Artist of a (played) media file.                                                                                                                                                                                        |
| outdoor-temperature  | system.outdoor-temperature  | Number:Temperature   | Temperature      | Current outdoor temperature.                                                                                                                                                                                            |
| wind-direction       | system.wind-direction       | Number:Angle         | Wind             | Wind direction in degrees (0-360°).                                                                                                                                                                                     |
| wind-speed           | system.wind-speed           | Number:Speed         | Wind             | Wind speed                                                                                                                                                                                                              |
| atmospheric-humidity | system.atmospheric-humidity | Number:Dimensionless | Humidity         | Atmospheric humidity in percent.                                                                                                                                                                                        |
| barometric-pressure  | system.barometric-pressure  | Number:Pressure      | Pressure         | Barometric pressure                                                                                                                                                                                                     |

For further information about categories see the [categories page](../../concepts/categories.html).

The `advanced` property indicates whether this channel is a basic or a more specific functionality of the thing. 
If `advanced` is set to `true` a user interface may hide this channel by default. 
The default value is `false` and thus will be taken if the `advanced` attribute is not specified. 
Especially for complex devices with a lot of channels, only a small set of channels - the most important ones - should be shown to the user to reduce complexity. 
Whether a channel should be declared as `advanced` depends on the device and can be decided by the binding developer. 
If a functionality is rarely used it should be better marked as `advanced`.

The following XML snippet shows a trigger channel:

```xml
<thing-type id="thingTypeID">
    <label>Sample Thing</label>
    <description>Some sample description</description>
    <channels>
        <channel id="s" typeId="trigger-channel" />
    </channels>
</thing-type>
<channel-type id="trigger-channel">
    <kind>trigger</kind>
    <label>Trigger Channel</label>
    <event>
        <options>
            <option value="PRESSED">pressed</option>
            <option value="RELEASED">released</option>
            <option value="DOUBLE_PRESSED">double pressed</option>
        </options>
    </event>
</channel-type>
```

This channel can emit the event payloads `PRESSED`, `RELEASED` and `DOUBLE_PRESSED`.

If no `<event>` tag is specified, the channel can be triggered, but has no event payload.
If an empty `<event>` tag is specified, the channel can trigger any event payload.

### System Trigger Channel Types

There exist system-wide trigger channel types that are available by default:

| Channel Type ID | Reference typeId       | Description  |
|-----------------|------------------------|------------- |
| trigger         | system.trigger         | Can only trigger, no event payload |
| rawbutton       | system.rawbutton       | Can trigger `PRESSED` and `RELEASED` |
| button          | system.button          | Can trigger `SHORT_PRESSED`, `DOUBLE_PRESSED` and `LONG_PRESSED` |
| rawrocker       | system.rawrocker       | Can trigger `DIR1_PRESSED`, `DIR1_RELEASED`, `DIR2_PRESSED` and `DIR2_RELEASED` |

In the following sections the declaration and semantics of tags, state descriptions and channel categories will be explained in more detail. 
For a complete sample of the thing types XML file and a full list of possible configuration options please see the [XML Configuration Guide](xml-reference.html).

### Default Tags

The XML definition of a ThingType allows to assign default tags to channels. 
All items bound to this channel will automatically be tagged with these default tags. 
The following snippet shows a 'Lighting' tag definition:

```xml
<tags>
    <tag>Lighting</tag>
</tags>
```

Please note that only tags from a pre-defined tag library should be used.
This library is still t.b.d., and only a very small set of tags are defined so far:

| Tag                | Item Types                 | Description                                                                           |
|--------------------|----------------------------|---------------------------------------------------------------------------------------|
| Lighting           | Switch, Dimmer, Color      | A light source, either switchable, dimmable or color                                  |
| Switchable         | Switch, Dimmer, Color      | An accessory that can be turned off and on.                                           |
| CurrentTemperature | Number, Number:Temperature | An accessory that provides a single read-only temperature value.                      |
| TargetTemperature  | Number, Number:Temperature | A target temperature that should engage a thermostats heating and cooling actions.   |
| CurrentHumidity    | Number                     | An accessory that provides a single read-only value indicating the relative humidity. |


### State Description

The state description allows to specify restrictions and additional information for the state of an item, that is linked to the channel. 
Some configuration options are only valid for specific item types. 
The following XML snippet shows the definition for a temperature actuator channel:

```xml
<state min="12" max="30" step="0.5" pattern="%.1f %unit%" readOnly="false"></state>
```

The attributes `min` and `max` can only be declared for channel with the item type `Number`. 
It defines the range of the numeric value. 
The Java data type is a BigDecimal. 
For example user interfaces can create sliders with an appropriate scale based on this information. 
The `step` attribute can be declared for `Number` and `Dimmer` items and defines what is the minimal step size that can be used. 
The `readonly` attribute can be used for all item types and defines if the state of an item can be changed. 
For all sensors the `readonly` attribute should be set to `true`. 
The `pattern` attribute can be used for `Number` and  `String` items. 
It gives user interface a hint how to render the item. 
The format of the pattern must be compliant to the [Java Number Format](http://docs.oracle.com/javase/tutorial/java/data/numberformat.html). 
The pattern can be localized (see also [Internationalization](../../features/internationalization.html)).
The special pattern placeholder `%unit%` is used for channels which bind to items of type `Number:<dimension>` which define a dimension for unit support. 
These channels will send state updates of type [QuantityType](../../concepts/units-of-measurement.html#quantitytype) and the unit is then rendered for the placeholder. 

Some channels might have only a limited and countable set of states. 
These states can be specified as options. 
A `String` item must be used as item type. 
The following XML snippet defines a list of predefined state options:

```xml
<state readOnly="true">
    <options>
        <option value="HIGH">High Pressure</option>
        <option value="MEDIUM">Medium Pressure</option>
        <option value="LOW">Low Pressure</option>
    </options>
</state>
```

The user interface can use these values to render labels for values or to provide a selection of states, when the channel is writable. 
The option labels can also be localized.

#### Dynamic State Description

In situations where the static definition of a state description is not sufficient a binding may implement a `DynamicStateDescriptionProvider`.
It allows to provide a StateDescription based on the specific `Channel`.
Also implement this interface if you want to provide dynamic state options.
The original `StateDescription` is available for modification and enhancement.
The `StateDescriptionFragmentBuilder` can be used to only provide the information which is available at the time of construction.

### Channel Categories

A description about channel categories as well as an overview about which categories exist can be found in out [categories overview](../../concepts/categories.html).

### Channel Groups

Some devices might have a lot of channels. 
There are also complex devices like a multi-channel actuator, which is installed inside the switchboard, but controls switches in other rooms. 
Therefore channel groups can be used to group a set of channels together into one logical block. 
A thing can only have direct channels or channel groups, but not both.

Inside the thing types XML file channel groups can be defined like this:

```xml
<thing-type id="multiChannelSwitchActor">
    <!-- ... -->
    <channel-groups>
        <channel-group id="switchActor1" typeId="switchActor" />
        <channel-group id="switchActor2" typeId="switchActor" />
    </channel-groups>
    <!-- ... -->
</thing-type>    
```

The channel group type is defined on the same level as the thing types and channel types. 
The group type must have a label, an optional description, and an optional [category](../../concepts/categories.html). 
Moreover the list of contained channels must be specified:

```xml
<channel-group-type id="switchActor">
    <label>Switch Actor</label>
    <description>This is a single switch actor with a switch channel</description>
    <category>Light</category>
    <channels>
        <channel id="switch" typeId="switch" />
    </channels>
</channel-group-type>
```

When a thing will be created for a thing type with channel groups, the channel UID will contain the group ID in the last segment divided by a hash (#).
If an Item should be linked to a channel within a group, the channel UID would be `binding:multiChannelSwitchActor:myDevice:switchActor1#switch` for the XML example before.
Details about the category can be found in our [categories overview](../../concepts/categories.html).

## Properties

Solutions based on Eclipse SmartHome might require meta data from a device. 
These meta data could include:

- general device information, e.g. the device vendor, the device series or the model ID, ...
- device characteristics, e.g. if it is battery based, which home automation protocol is used, what is the current firmware version or the serial number, ...
- physical descriptions, e.g. what is the size, the weight or the color of the device, ...
- any other meta data that should be made available for the solution by the binding

Depending on the solution the provided meta data can be used for different purposes. 
Among others the one solution could use the data during a device pairing process whereas another solution might use the data to group the devices/things by the vendors or by the home automation protocols on a user interface. 
To define such thing meta data the thing type definition provides the possibility to specify so-called `properties`:

```xml
    <thing-type id="thingTypeId">
        ...
        <properties>
             <property name="vendor">MyThingVendor</property>
             <property name="modelId">thingTypeId</property>
             <property name="protocol">ZigBee</property>
             ...
        </properties>
		...
    </thing-type>
```

In general each `property` must have a name attribute which should be written in camel case syntax. 
The actual property value is defined as plain text and is placed as child node of the property element. 
It is recommended that at least the vendor and the model id properties are specified here since they should be definable for the most of the devices. 
In contrast to the properties defined in the 'ThingType' definitions the thing handler [documentation](thing-handler.html) explains how properties can be set during runtime.

### Representation Property

A thing type can contain a so-called `representation property`. 
This optional property contains the _name_ of a property whose value can be used to uniquely identify a device.
The `thingUID` cannot be used for this purpose because there can be more than one thing for the same device.

Each physical device normally has some kind of a technical identifier which is unique.
This could be a MAC address (e.g. Hue bridge, camera, all IP-based devices), a unique device id (e.g. a Hue lamp) or some other property that is unique per device type. 
This property is normally part of a discovery result for that specific thing type. 
Having this property identified per binding it could be used as the `representation property` for this thing.

The `representation property` will be defined in the thing type XML: 

```xml
    <thing-type id="thingTypeId">
        ...
        <properties>
            <property name="vendor">Philips</property>
        </properties>
        <representation-property>serialNumber</representation-property>
        ...
    </thing-type>
```

Note that the `representation property` is normally not listed in the `properties` part of the thing type, as this part contains static properties, that are the same for each thing of this thing type. 
The name of the `representation property` identifies a property that is added to the thing in the thing handler upon successful initialization. 

### Representation Property and Discovery

The representation property is being used to auto-ignore discovery results of devices that already have a corresponding thing. 
This happens if a device is being added manually. 
If the new thing is going online, the auto-ignore service of the inbox checks if the inbox already contains a discovery result of the same type where the value of its `representation property` is identical to the value of the `representation property` of the newly added thing. 
If this is the case, the result in the inbox is automatically set to ignored. 
Note that this result is automatically removed when the manual added thing is eventually removed. 
A new discovery would then automatically find this device again and add it to the inbox properly. 

## Formatting Labels and Descriptions

The label and descriptions for things, channels and config descriptions should follow the following format. 
The label should be short so that for most UIs it does not spread across multiple lines. 
The description can contain longer text to describe the thing in more detail. 
Limited use of HTML tags is permitted to enhance the description - if a long description is provided, the first line should be kept short, and a line break (```<br />```) placed at the end of the line to allow UIs to display a short description in limited space.

Configuration options should be kept short so that they are displayable in a single line in most UIs. 
If you want to provide a longer description of the options provided by a particular parameter, then this should be placed into the ```<description>``` of the parameter to keep the option label short. 
The description can include limited HTML to enhance the display of this information.

The following HTML tags are allowed : ```<b>, <br />, <em>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <i>, <p>, <small>, <strong>, <sub>, <sup>, <ul>, <ol>, <li>```. 
These must be inside the XML escape sequence - e.g. ```<description><![CDATA[ HTML marked up text here ]]></description>```.

## Auto Update Policies

Channel types can optionally define a policy with respect to the auto update handling. 
This influences the decision within the framework if an auto-update of the item's state should be sent in case a command is received for it.
The auto update policy typically is inherited by the channel from its channel type. 
Nevertheless, this value can be overridden in the channel definition.

In this example, an auto update policy is defined for the channel type, but is overridden in the channel definition:

```xml
<channel-type id="channel">
    <label>Channel with an auto update policy</label>
    <autoUpdatePolicy>recommend</autoUpdatePolicy>
</channel-type>

<thing-type id="thingtype">
    <label>Sample Thing</label>
    <description>Thing type which overrides the auto update policy of a channel</description>
    <channels>
      <channel id="instance" typeId="channel">
        <autoUpdatePolicy>default</autoUpdatePolicy>
      </channel>
    </channels>
</thing-type>
```

The following policies are supported:

* **veto**: No automatic state update should be sent by the framework. The thing handler will make sure it sends a state update and it can do it better than just converting the command to a state.
* **default**: The binding does not care and the framework may do what it deems to be right. The state update which the framework will send out normally will correspond the command state anyway. This is the default if no other policy is set explicitly.
* **recommend**: An automatic state update should be sent by the framework because no updates are sent by the binding. This usually is the case when devices don't expose their current state to the handler.
---
layout: documentation
---

{% include base.html %}

# Thing Handler Implementation

A `ThingHandler` handles the communication between the Eclipse SmartHome framework and an entity from the real world, e.g. a physical device, a web service, represented by a `Thing`. 

The communication is bidirectional. The framework informs a thing handler about commands, state and configuration updates, and so on, by the corresponding handler methods. The handler can notify the framework about changes like state and status updates, updates of the whole thing, by a `ThingHandlerCallback`.

In this section the ThingHandler API is described in more detail and you get hints how to implement your binding.

## The BaseThingHandler

Eclipse SmartHome provides an abstract base class named `BaseThingHandler`. It is recommended to use this class, because it covers a lot of common logic. Most of the explanations are based on the assumption, that the binding inherits from the BaseThingHandler in all concrete `ThingHandler` implementations. Nevertheless if there are reasons why you can not use the base class, the binding can also directly implement the `ThingHandler` interface.

The communication between the framework and the ThingHandler is bidirectional. If the framework wants the binding to do something or just notfiy it about changes, it calls methods like `handleCommand`, `handleUpdate` or `thingUpdated`. If the ThingHandler wants to inform the framework about changes, it uses a callback. The `BaseThingHandler` provides convience methods like `updateState`, `updateStatus` `updateThing` or `triggerChannel`, that can be used to inform the framework about changes.

## Life cycle 

The `ThingHandler` has a well defined life cycle. The two most important life cycle methods are: `initialize` and `dispose`. The `initialize` method is called, when the handler is started and `dispose` is called just before the handler is stopped. Therefore the methods can be used to allocate and deallocate resources.

### Startup

The startup of a handler is divided in two essential steps:

1. Handler is registered: `ThingHandler` instance is created by a `ThingHandlerFactory` and tracked by the framework. In addition, the handler can be registered as a service if required, e.g. as `FirmwareUpdateHandler` or `ConfigStatusProvider`.
 
2. Handler is initialized: `ThingHandler.initialize()` is called by the framework in order to initialize the handler. This method is only called if all 'required' configuration parameters of the Thing are present. The handler is ready to work (methods like `handleCommand`, `handleUpdate` or `thingUpdated` can be called).

The diagram below illustrates the startup of a handler in more detail. The life cycle is controlled by the `ThingManager`.

![thing_life_cycle_startup](diagrams/thing_life_cycle_startup.png)

The `ThingManager` mediates the communication between a `Thing` and a `ThingHandler` from the binding. The `ThingManager` creates for each Thing a `ThingHandler` instance using a `ThingHandlerFactory`. Therefore, it tracks all `ThingHandlerFactory`s from the binding. 

The `ThingManager` determines if the `Thing` is initializable or not. A `Thing` is considered as *initializable* if all *required* configuration parameters (cf. property *parameter.required* in [Configuration Description](xml-reference.html)) are available. If so, the method `ThingHandler.initialize()` is called.

Only Things with status (cf. [Thing Status](../../concepts/things.html#thing-status)) *UNKNOWN*, *ONLINE* or *OFFLINE* are considered as *initialized* by the framework and therefore it is the handler's duty to assign one of these states sooner or later. To achieve that, the status must be reported to the framework via the callback or `BaseThingHandler.updateStatus(...)` for convenience. Furthermore, the framework expects `initialize()` to be non-blocking and to return quickly. For longer running initializations, the implementation has to take care of scheduling a separate job which must guarantee to set the status eventually. Also, please note that the framework expects the `initialize()` method to handle anticipated error situations gracefully and set the thing to *OFFLINE* with the corresponding status detail (e.g. *COMMUNICATION_ERROR* or *CONFIGURATION_ERROR* including a meaningful description) instead of throwing exceptions. 

If the `Thing` is not initializable the configuration can be updated via `ThingHandler.handleConfigurationUpdate(Map)`. The binding has to notify the `ThingManager` about the updated configuration by a callback. The `ThingManager` tries to initialize the `ThingHandler` resp. `Thing` again.

After the handler is initialized, the handler must be ready to handle methods calls like `handleCommand` and `handleUpdate`, as well as `thingUpdated`. 

### Shutdown

The shutdown of a handler is also divided in two essential steps:

1. Handler is unregistered: `ThingHandler` instance is no longer tracked by the framework. The `ThingHandlerFactory` can unregister handler services (e.g. `FirmwareUpdateHandler` or `ConfigStatusProvider`) if registered, or release resources.

2. Handler is disposed: `ThingHandler.disposed()` method is called. The framework expects `dispose()` to be non-blocking and to return quickly. For longer running disposals, the implementation has to take care of scheduling a separate job. 

![thing_life_cycle_shutdown](diagrams/thing_life_cycle_shutdown.png)

After the handler is disposed, the framework will not call the handler anymore.

## Bridge Status Changes

A `ThingHandler` is notified about Bridge status changes to *ONLINE* and *OFFLINE* after a `BridgeHandler` has been initialized. Therefore, the method `ThingHandler.bridgeStatusChanged(ThingStatusInfo)` must be implemented (this method is not called for a bridge status updated through the bridge initialization itself). If the Thing of this handler does not have a Bridge, this method is never called.

If the bridge status has changed to OFFLINE, the status of the handled thing must also be updated to *OFFLINE* with detail *BRIDGE_OFFLINE*. If the bridge returns to *ONLINE*, the thing status must be changed at least to *OFFLINE* with detail *NONE* or to another thing specific status.


## Handling Commands

For handling commands the `ThingHandler` interface defines the `handleCommand` method. This method is called when a command is sent to an item, which is linked to a channel of the *Thing*. A Command represents the intention that an action should be executed on the external system, or that the state should be changed. Inside the `handleCommand` method binding specific logic can be executed.

The ThingHandler implementation must be prepared to handle different command types depending on the item types, that are defined by the channels. The method can also be called at the same time from different threads, so it must be thread-safe.

If an exception is thrown in the method, it will be caught by the framework and logged as an error. So it is better to handle communication errors within the binding and to update the thing status accordingly. Typically only the binding is knowledgeable about the severity of an error and if it should be logged as info, warning or error message. If the communication to the device or service was successful it is good practice to set the thing status to *ONLINE* by calling `statusUpdated(ThingStatus.ONLINE)`.

The following code block shows a typical implementation of the `handleCommand` method:

```java
@Override
public void handleCommand(ChannelUID channelUID, Command command) {
    try {
    	switch (channelUID.getId()) {
	    	case CHANNEL_TEMPERATURE:
	        	if(command instanceof OnOffType.class) {
	        		// binding specific logic goes here
	        		SwitchState deviceSwitchState = convert((OnOffType) command);
	        		updateDeviceState(deviceSwitchState);
	        	}
	        	break;
	    	// ...
    	}
    	statusUpdated(ThingStatus.ONLINE);
	} catch(DeviceCommunicationException ex) {
		// catch exceptions and handle it in your binding
		logger.warn("Communication with device failed: " + ex.getMessage(), ex);
        statusUpdated(ThingStatus.OFFLINE);
    }
}
```

## Updating the Channel State

State updates are sent from the binding to inform the framework, that the state of a channel has been updated. For this the binding developer can call a method from the `BaseThingHandler` class like this:

```java
updateState("channelId", OnOffType.ON)
```    

The call will be delegated to the framework, which changes the state of all bound items. It is binding specific when the channel should be updated. If the device or service supports an event mechanism the ThingHandler should make use of it and update the state every time when the device changes its state.

### Polling for a State

If no event mechanism is available, the binding can poll for the state. The `BaseThingHandlerFactory` has an accessible `ScheduledExecutorService`, which can be used to schedule a job. The following code block shows how to start a polling job in the initialize method of a `ThingHandler`, which runs with an interval of 30 seconds:

```java
@Override
public void initialize() {
    Runnable runnable = new Runnable() {
        @Override
        public void run() {
            // execute some binding specific polling code
        }
    };
    pollingJob = scheduler.scheduleAtFixedDelay(runnable, 0, 30, TimeUnit.SECONDS);
}
```

Of course, the polling job must be cancelled in the dispose method:

```java
@Override
public void dispose() {
    pollingJob.cancel(true);
}
```

Even if the state has not changed since the last update, the binding should inform the framework, because it indicates that the value is still present.

## Trigger a channel

The binding can inform the framework, that a channel has been triggered. For this the binding developer can call a method from the BaseThingHandler class like this:

```java
triggerChannel("channelId")
```

If an event payload is needed, use the overloaded version:

```java
triggerChannel("channelId", "PRESSED")
```

The call will be delegated to the framework. It is binding specific when the channel should be triggered.

## Updating the Thing Status

The *ThingHandler* must also manage the thing status (see also: [Thing Status Concept](../../concepts/things.html#thing-status)). If the device or service is not working correctly, the binding should change the status to *OFFLINE* and back to *ONLINE*, if it is working again. The status can be updated via an inherited method from the BaseThingHandler class by calling:

```java
updateStatus(ThingStatus.OFFLINE, ThingStatusDetail.OFFLINE.COMMUNICATION_ERROR);
```    

The second argument of the method takes a `ThingStatusDetail` enumeration value, which further specifies the current status situation. A complete list of all thing statuses and thing status details is listed in the [Thing Status](../../concepts/things.html#thing-status) chapter.

For debugging purposes the binding can also provide an additional status description. This description might contain technical information (e.g. an HTTP status code, or any other protocol specific information, which helps to identify the current problem):

```java
updateStatus(ThingStatus.OFFLINE, ThingStatusDetail.OFFLINE.COMMUNICATION_ERROR, "HTTP 401");
```

After the thing is created, the framework calls the `initialize` method of the handler. At this time the state of the thing is *INTIALIZING* as long as the binding sets it to something else. Because of this the default implementation of the `initialize()` method in the `BaseThingHandler` just changes the status to *ONLINE*.

*Note:* A binding should not set any other state than ONLINE, OFFLINE and UNKNOWN. Additionally, REMOVED must be set after `handleRemoval()` has completed the removal process. All other states are managed by the framework.

Furthermore bindings can specify a localized description of the thing status by providing the reference of the localization string, e.g &#64;text/rate_limit. The corresponding handler is able to provide placeholder values as a JSON-serialized array of strings:

```
&#64;text/rate_limit ["60", "10", "@text/hour"]
```

```
rate_limit=Device is blocked by remote service for {0} minutes. Maximum limit of {1} configuration changes per {2} has been exceeded. For further info please refer to device vendor.
```

## Channel Links

Some bindings might want to start specific functionality for a channel only if an item is linked to the channel.
The `ThingHandler` has two callback methods `channelLinked(ChannelUID channelUID)` and `channelUnlinked(ChannelUID channelUID)`, which are called for every link that is added or removed to/from a channel.
So please be aware of the fact that both methods can be called multiple times.

The `channelLinked` method is only called, if the thing handler has been initialized (status ONLINE/OFFLINE/UNKNOWN).
To actively check if a channel is linked, you can use the `isChannelLinked(ChannelUID channelUID)` method of the `ThingHandlerCallback`.

## Handling Thing Updates

If the structure of a thing has been changed during runtime (after the thing was created), the binding is informed about this change in the ThingHandler within the `thingUpdated` method. The `BaseThingHandler` has a default implementation for this method:

```java
@Override
public void thingUpdated(Thing thing) {
    dispose();
    this.thing = thing;
    initialize();
}
```

If your binding contains resource-intensive logic in your initialize method, you should think of implementing the method by yourself and figuring out what is the best way to handle the change.

For configuration updates, which are triggered from the binding, the framework does not call the `thingUpdated` method to avoid infinite loops.

## Handling Configuration Updates

For changes of the configuration the `ThingHandler` has a separate callback named  `handleConfigurationUpdate(Map<String, Object> configurationParameters)`. This method is called with a map of changed configuration parameters. Depending on the UI multiple parameters can be sent at once, or just a subset or even a single parameter.

The default implementation of this method in the `BaseThingHandler` class does simply apply the configuration parameters, updates the configuration of the thing and reinitializes the handler:

```java
 @Override
public void handleConfigurationUpdate(Map<String, Object> configurationParmeters) {
    // can be overridden by subclasses
    Configuration configuration = editConfiguration();
    for (Entry<String, Object> configurationParmeter : configurationParmeters.entrySet()) {
        configuration.put(configurationParmeter.getKey(), configurationParmeter.getValue());
    }

    // reinitialize with new configuration and persist changes
    dispose();
    updateConfiguration(configuration);
    initialize();
}
```

If configuration needs to be sent to devices, this method should be overridden and some binding-specific logic should be performed. The binding is also responsible for updating the thing, so as in the default implementation `updateConfiguration` should be called, if the configuration was successfully updated. In some radio protocols configuration cannot directly be transmitted to devices, because the communication is done in specific intervals only. The binding could indicate a not yet transmitted configuration change for a device by setting the thing status detail to `CONFIGURATION_PENDING` (see [Thing Status Section](../../concepts/things.html#status-details)).


## Updating the Thing from a Binding

It can happen that the binding wants to update the configuration or even the whole structure of a thing. If the `BaseThingHandler` class is used, it provides some helper methods for modifying the thing.

Please note that not all thing providers are writable. Therefore bindings must not rely on any thing changes to be persisted. 

### Updating the Configuration

Usually the configuration is maintained by the user and the binding is informed about the updated configuration. But if the configuration can also be changed in the external system, the binding should reflect this change and notify the framework about it.

If the configuration should be updated, then the binding developer can retrieve a copy of the current configuration by calling `editConfiguration()`. The updated configuration can be stored as a whole by calling `updateConfiguration(Configuration)`.

Suppose that an external system causes an update of the configuration, which is read in as a `DeviceConfig` instance. The following code shows how to update configuration:

```java
protected void deviceConfigurationChanged(DeviceConfig deviceConfig) {
    Configuration configuration = editConfiguration();
    configuration.put("parameter1", deviceConfig.getValue1());
    configuration.put("parameter2", deviceConfig.getValue2());
    updateConfiguration(configuration);
}
```

The `BaseThingHandler` will propagate the update to the framework, which then notifies all registered listeners about the updated thing. But the thing update is **not** propagated back to the handler through a `thingUpdated(Thing)` call.

### Updating Thing Properties

Thing properties can be updated in the same way as the configuration. The following example shows how to modify two properties of a thing:

```java
protected void devicePropertiesChanged(DeviceInfo deviceInfo) {
	Map<String, String> properties = editProperties();
    properties.put(Thing.PROPERTY_SERIAL_NUMBER, deviceInfo.getSerialNumber());
    properties.put(Thing.PROPERTY_FIRMWARE_VERSION, deviceInfo.getFirmwareVersion());
    updateProperties(properties);
}
```

If only one property must be changed, there is also a convenient method `updateProperty(String name, String value)`. Both methods will only inform the framework that the thing was modified, if at least one property was added, removed or updated. Thing handler implementations must not rely though on properties to be persisted as not all providers support that.

### Updating the Thing Structure

The binding also has the possibility to change the thing structure by adding or removing channels. The following code shows how to use the ThingBuilder to add one channel to the thing:

```java
protected void thingStructureChanged() {
    ThingBuilder thingBuilder = editThing();
    Channel channel = ChannelBuilder.create(new ChannelUID("bindingId:type:thingId:1"), "String").build();
    thingBuilder.withChannel(channel);
    updateThing(thingBuilder.build());
}
```

## Handling Thing Removal

If a thing should be removed, the framework informs the binding about the removal request by calling `handleRemoval` at the thing handler. The thing will not be removed from the runtime until the binding confirms the deletion by setting the thing status to `REMOVED`. If no special removal handling is required by the binding, you do not have to care about removal because the default implementation of this method in the `BaseThingHandler` class just calls `updateStatus(ThingStatus.REMOVED)`.

However, for some radio-based devices it is needed to communicate with the device in order to unpair it safely. After the device was successfully unpaired, the binding must inform the framework that the thing was removed by setting the thing status to `REMOVED`.

After the removal was requested (i.e. the thing is in  `REMOVING` state), it cannot be changed back anymore to `ONLINE`/`OFFLINE`/`UNKNOWN` by the binding. The binding may only initiate the status transition to `REMOVED`.

## Providing the Configuration Status
As on the [XML Reference](xml-reference.html) page explained the *ThingHandler* as handler for the thing entity can provide the configuration status of the thing by implementing the `org.eclipse.smarthome.config.core.status.ConfigStatusProvider` interface. For things that are created by sub-classes of the `BaseThingHandlerFactory` the provider is already automatically registered as an OSGi service if the concrete thing handler implements the configuration status provider interface. Currently the framework provides two base thing handler implementations for the configuration status provider interface:
* `org.eclipse.smarthome.core.thing.binding.ConfigStatusThingHandler` extends the `BaseThingHandler` and is to be used if the configuration status is to be provided for thing entities
* `org.eclipse.smarthome.core.thing.binding.ConfigStatusBridgeHandler` extends the `BaseBridgeHandler` and is to be used if the configuration status is to be provided for bridge entities

Sub-classes of these handlers must only override the operation `getConfigStatus` to provide the configuration status in form of a collection of `org.eclipse.smarthome.config.core.status.ConfigStatusMessage`s.

The framework will take care of internationalizing the messages. For this purpose there must be an i18n properties file inside the bundle of the configuration status provider that has a message declared for the message key of the `ConfigStatusMessage`. The actual message key is built by the operation `withMessageKeySuffix(String)` of the message´s builder in the manner that the given message key suffix is appended to *config-status."config-status-message-type."*. As a result depending on the type of the message the final constructed message keys are:
* config-status.information.any-suffix
* config-status.warning.any-suffix
* config-status.error.any-suffix
* config-status.pending.any-suffix
---
layout: documentation
---

{% include base.html %}

# Declaring Configurations, Bindings and Things

Specific services and bindings have to provide meta information which is used for visualization, validation or internal service mapping. Meta information can be provided by registering specific services at the *OSGi* service registry or by specifying them in a declarative way, which is described in this chapter.

**Three kinds of descriptions/definitions exist:**

- Configuration descriptions: Used for visualization and validation of configuration properties (optional)
- Binding definitions: Required to declare a binding (mandatory)
- Bridge and *Thing* descriptions: Required to specify which bridges and *Thing*s are provided by the binding, which relations they have to each other and which channels they offer (mandatory)


## Configuration Descriptions

Specific services or bindings usually require a configuration to be operational in a meaningful way. To visualize or validate concrete configuration properties, configuration descriptions should be provided. All available configuration descriptions are accessible through the `org.eclipse.smarthome.config.core.ConfigDescriptionRegistry` service.

Although configuration descriptions are usually specified in a declarative way (as described in this section), they can also be provided as `org.eclipse.smarthome.config.core.ConfigDescriptionProvider`.
Any `ConfigDescriptionProvider`s must be registered as service at the *OSGi* service registry. The full Java API for configuration descriptions can be found in the Java package `org.eclipse.smarthome.config.core`. In addition to this there is a `org.eclipse.smarthome.config.core.validation.ConfigDescriptionValidator` that can be used to validate a set of configuration parameters against their declarations in the configuration description before the actual configuration is updated with the new configuration parameters.

Configuration descriptions must be placed as XML file(s) (with the ending `.xml`) in the bundle's folder `/ESH-INF/config/`.

### Formatting Labels
The label and descriptions for things, channels and config descriptions should follow the following format. The label should be short so that for most UIs it does not spread across multiple lines. The description can contain longer text to describe the thing in more detail. Limited use of HTML tags is permitted to enhance the description - if a long description is provided, the first line should be kept short and a line break (```<br>```) should be placed at the end of the line to allow UIs to display a short description in limited space.

Configuration options should be kept short so that they are displayable on a single line in most UIs. If you want to provide a longer description of the options provided by a particular parameter, then this should be placed into the ```<description>``` of the parameter to keep the option label short. The description can include limited HTML to enhance the display of this information.

The following HTML tags are allowed -: ```<b>, <br>, <em>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <i>, <p>, <small>, <strong>, <sub>, <sup>, <ul>, <ol>, <li>```. These must be inside the XML escape sequence - eg. ```<description><![CDATA[ HTML marked up text here ]]></description>```.

### XML Structure for Configuration Descriptions
```xml
<?xml version="1.0" encoding="UTF-8"?>
<config-description:config-descriptions
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:config-description="http://eclipse.org/smarthome/schemas/config-description/v1.0.0"
    xsi:schemaLocation="http://eclipse.org/smarthome/schemas/config-description/v1.0.0
        http://eclipse.org/smarthome/schemas/config-description-1.0.0.xsd">

  <config-description uri="{binding|thing-type|channel-type|any_other}:bindingID:...">
    <parameter-group name="String">
      <label>String</label>
      <description>String</description>
      <context>String</context>
      <advanced>{true|false}</advanced>
    </parameter-group>

    <parameter name="String" type="{text|integer|decimal|boolean}" min="Decimal" max="Decimal" step="Decimal" pattern="String" required="{true|false}" readOnly="{true|false}" multiple="{true|false}" groupName="String" unit="A|cd|K|kg|m|mol|s|g|rad|sr|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|Cel|lm|lx|Bq|Gy|Sv|kat|m/s2|m2v|m3|kph|%|l|ms|min|h|d|week|y">
      <context>{network-address|serial-port|password|password-create|color|date|datetime|email|month|week|dayOfWeek|time|tel|url|item|thing|group|tag|service|channel|rule|location}</context>
      <required>{true|false}</required>
      <default>String</default>
      <label>String</label>
      <description>String</description>
      <unitLabel>String</unitLabel>
      <options>
        <option value="String">String</option>
      </options>
      <filter>
        <criteria name="String">String</criteria>
      </filter>
    </parameter>
  </config-description>

  <config-description uri="{binding|thing-type|channel-type|any_other}:bindingID:...">
    ...
  </config-description>
...
</config-description:config-descriptions>
```

<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>config-description.uri</td><td>The URI of this description within the ConfigDescriptionRegistry (mandatory).</td></tr>
  <tr><td>parameter</td><td>The description of a concrete configuration parameter (optional).</td></tr>
  <tr><td>parameter.name</td><td>The name of the configuration parameter (mandatory).</td></tr>
  <tr><td>parameter.type</td><td>The data type of the configuration parameter (mandatory).</td></tr>
  <tr><td>parameter.min</td><td>The minimal value for numeric types, or the minimal length of strings. Note that the value of any options may be outside of this value. (optional).</td></tr>
  <tr><td>parameter.max</td><td>The maximum value for numeric types, or the maximum length of strings. Note that the value of any options may be outside of this value. (optional).</td></tr>  
  <tr><td>parameter.step</td><td>The value granularity for a numeric value (optional).</td></tr>
  <tr><td>parameter.pattern</td><td>The regular expression for a text type (optional).</td></tr>
  <tr><td>parameter.required</td><td>Specifies whether the value is required (optional).</td></tr>
  <tr><td>parameter.readOnly</td><td>Specifies whether the value is read-only (optional).</td></tr>
  <tr><td>parameter.multiple</td><td>Specifies whether multiple selections of options are allowed (optional).</td></tr>
  <tr><td>parameter.groupName</td><td>Sets a group name for this parameter (optional).</td></tr>
  <tr><td>parameter.unit</td><td>Specifies the unit of measurements. The unit declaration in the parameter definition shown above contains the set of valid units. The unit must only be set if the type of the parameter is either integer or decimal (optional).</td></tr>
  <tr><td>advanced</td><td>Specifies that this is an advanced parameter. Advanced parameters may be hidden by a UI (optional).</td></tr>
  <tr><td>verify</td><td>Specifies that this is parameter requires a verification stage with the user before sending. Parameters flagged with *verify=true* could be considered dangerous and should be protected from accidental use by a UI - eg by adding an "Are you sure" prompt (optional).</td></tr>
  <tr><td>context</td><td>The context of the configuration parameter (optional).</td></tr>
  <tr><td>required</td><td>The flag indicating if the configuration parameter has to be set or not (deprecated, optional, default: false).</td></tr>
  <tr><td>default</td><td>The default value of the configuration parameter (optional).</td></tr>
  <tr><td>label</td><td>A human-readable label for the configuration parameter (optional).</td></tr>
  <tr><td>description</td><td>A human-readable description for the configuration parameter (optional).</td></tr>
  <tr><td>unitLabel</td><td>The unit label represents a human-readable label for the unit. It can also be used to provide unit labels for natural language units as iterations, runs, etc. The unit label must only be set if the type of the parameter is either integer or decimal (optional).</td></tr>
  <tr><td>option</td><td>The element definition of a static selection list (optional).</td></tr>
  <tr><td>option.value</td><td>The value of the selection list element. Note that the value may be outside of the range specified in the min/max if this is specified.</td></tr>
  <tr><td>multipleLimit</td><td>If multiple is true, sets the maximum number of options that can be selected (optional).</td></tr>
  <tr><td>limitToOptions</td><td>If true (default) will only allow the user to select items in the options list. If false, will allow the user to enter other text (optional).</td></tr>
  <tr><td>criteria</td><td>The filter criteria for values of a dynamic selection list (optional).</td></tr>  
  <tr><td>criteria.name</td><td>The name of the context related filter.</td></tr>  
</table>

### Supported Contexts

Context is used to provide some semantic details about the parameter. The UIs use it to render different kind of input widgets. The following contexts require a specific format of the content:

<table><tr><th>Name</th><th>Type</th><th>Format</th><th>Sample implementation</th></tr>
  <tr><td>network-address</td><td>text</td><td>IPv4,IPv6, domain name</td><td><code>&lt;input type="text"/></code></td></tr>
  <tr><td>serial-port</td><td>text</td><td>Serial port name, e.g. COM1</td><td>custom input field</td></tr>
  <tr><td>password</td><td>text</td><td>alphanumeric characters</td><td><code>&lt;input type="password"/></code></td></tr>
  <tr><td>password-create</td><td>text</td><td>alphanumeric characters</td><td>custom password input</td></tr>
  <tr><td>color</td><td>text</td><td>#000000 - #ffffff (hex color)</td><td><code>&lt;input type="color"/></code></td></tr>
  <tr><td>date</td><td>text</td><td>YYYY-MM-DD</td><td><code>&lt;input type="date"/></code></td></tr>
  <tr><td>datetime</td><td>text</td><td>YYYY-MM-DD hh:mm</td><td>custom input field</td></tr>
  <tr><td>email</td><td>text</td><td>username@domain.com</td><td><code>&lt;input type="email"/></code></td></tr>
  <tr><td>month</td><td>text</td><td>month of year</td><td>custom input field</td></tr>
  <tr><td>week</td><td>integer</td><td>week of year</td><td>custom input field</td></tr>
  <tr><td>dayOfWeek</td><td>text</td><td>MON, TUE, WED, THU, FRI, SAT, SUN <br></td><td>custom input field</td></tr>
  <tr><td>time</td><td>text/integer</td><td>hh:mm:ss/milliseconds since epoch</td><td><code>&lt;input type="time"/></code></td></tr>
  <tr><td>telephone</td><td>text</td><td>telephone number</td><td>custom input field</td></tr>
  <tr><td>url</td><td>text</td><td>web url</td><td><code>&lt;input type="url"/></code></td></tr>
  <tr><td>item</td><td>text</td><td>Item name</td><td>custom input field</td></tr>
  <tr><td>thing</td><td>text</td><td>UID of a thing</td><td>custom input field</td></tr>
  <tr><td>group</td><td>text</td><td>group name to which this parameter belongs</td><td></td></tr>
  <tr><td>tag</td><td>text</td><td>tag name</td><td>custom input field</td></tr>
  <tr><td>service</td><td>text</td><td>service name</td><td>custom input field</td></tr>
  <tr><td>channel</td><td>text</td><td>UID of a channel<br></td><td>custom input field</td></tr>
  <tr><td>rule</td><td>text</td><td>UID of a rule<br></td><td>custom input field</td></tr>
  <tr><td>location</td><td>text</td><td>latitude,longitude[,altitude]<br></td><td>custom input field</td></tr>
  
</table>

Further, the <strong>item</strong> context can contain criteria to filter the list of items. For example:

```xml
<filter>
  <criteria name="type">Switch,Dimmer</criteria>
  <criteria name="tag">Light,Heating</criteria>
</filter>
```

In the case of above filter only those items will be shown that satisfy the filter's conditions. The above filter is evaluated as follows: 

```
(type=Switch OR type=Dimmer) AND (tag=Light OR tag=Heating) 

```
Similarly, the <strong>Channel</strong> context can contain criteria to filter channels based on <strong>kind</strong> field. The value of <strong>kind</strong> can either be STATE or TRIGGER. For example:

```xml
<filter>
  <criteria name="kind">STATE|TRIGGER</criteria>
</filter>
```

Groups allow parameters to be grouped together into logical blocks so that the user can find the parameters they are looking for. A parameter can be placed into a group so that the UI knows how to display the information.
<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>group.name</td><td>The group name - this is used to link the parameters into the group, along with the groupName option in the parameter (mandatory).</td></tr>
  <tr><td>label</td><td>The human-readable label of the group. (mandatory).</td></tr>
  <tr><td>description</td><td>The description of the group. (optional).</td></tr>
  <tr><td>context</td><td>Sets a context tag for the group. The context may be used in the UI to provide some feedback on the type of parameters in this group (optional).</td></tr>
  <tr><td>advanced</td><td>Specifies that this is an advanced group. The UI may hide this group from the user (optional).</td></tr>
</table>


The full XML schema for configuration descriptions is specified in the [ESH config description XSD](http://eclipse.org/smarthome/schemas/config-description-1.0.0.xsd) file.

**Hints:**

- Although the attribute `uri` is optional, it *must* be specified in configuration description files. Only for embedded configuration descriptions in documents for binding definitions and `Thing` type descriptions, the attribute is optional.


### Example

The following code gives an example for one configuration description.  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config-description:config-description uri="thing-type:my-great-binding:my-bridge-name"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:config-description="http://eclipse.org/smarthome/schemas/config-description/v1.0.0"
    xsi:schemaLocation="http://eclipse.org/smarthome/schemas/config-description/v1.0.0
        http://eclipse.org/smarthome/schemas/config-description-1.0.0.xsd">

  <parameter name="ipAddress" type="text" required="true">
    <context>network-address</context>
    <label>Network Address</label>
    <description>Network address of the device.</description>
  </parameter>

  <parameter name="userName" type="text" required="true">
    <label>User Name</label>
  </parameter>

  <parameter name="password" type="text" required="false">
    <context>password</context>
  </parameter>

</config-description:config-description>
```

## Binding Definitions

Every binding has to provide meta information such as binding id or name. The meta information of all bindings is accessible through the `org.eclipse.smarthome.core.binding.BindingInfoRegistry` service.

Although binding definitions are usually specified in a declarative way (as described in this section), they can also be provided as `org.eclipse.smarthome.core.binding.BindingInfo`.
Any `BindingInfo` must be registered as service at the *OSGi* service registry. The full Java API for binding definitions can be found in the Java package `org.eclipse.smarthome.core.binding`.

Binding definitions must be placed as XML file(s) (with the ending `.xml`) in the bundle's folder `/ESH-INF/binding/`.


### XML Structure for Binding Definitions

```xml
<?xml version="1.0" encoding="UTF-8"?>
<binding:binding id="bindingID"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:binding="http://eclipse.org/smarthome/schemas/binding/v1.0.0"
    xsi:schemaLocation="http://eclipse.org/smarthome/schemas/binding/v1.0.0
        http://eclipse.org/smarthome/schemas/binding-1.0.0.xsd">

  <name>String</name>
  <description>String</description>
  <author>String</author>

  <config-description>
    ...
  </config-description>
  OR
  <config-description-ref uri="{binding|thing-type|channel-type|any_other}:bindingID:..." />

</binding:binding>
```

<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>binding.id</td><td>An identifier for the binding (mandatory).</td></tr>
  <tr><td>name</td><td>A human-readable name for the binding (mandatory).</td></tr>
  <tr><td>description</td><td>A human-readable description for the binding (optional).</td></tr>
  <tr><td>author</td><td>The author of the binding (optional).</td></tr>
  <tr><td>service-id</td><td>The ID (service.pid or component.name) of the main binding service, which can be configured through OSGi configuration admin service. Should only be used in combination with a config description definition (optional).</td></tr>
  <tr><td>config-description</td><td>The configuration description for the binding within the ConfigDescriptionRegistry (optional).</td></tr>
  <tr><td>config-description-ref</td><td>The reference to a configuration description for the binding within the ConfigDescriptionRegistry (optional).</td></tr>
  <tr><td>config-description-ref.uri</td><td>The URI of the configuration description for the binding within the ConfigDescriptionRegistry (mandatory).</td></tr>
</table>

The full XML schema for binding definitions is specified in the [ESH binding XSD](http://eclipse.org/smarthome/schemas/binding-1.0.0.xsd) file.

**Hints:**

- The attribute `uri` in the section `config-description` is optional, it *should not* be specified in binding definition files because it's an embedded configuration. If the `uri` is *not* specified, the configuration description is registered as `binding:bindingID`, otherwise the given `uri` is used.
- If a configuration description is already specified somewhere else and the binding wants to (re-)use it, a `config-description-ref` should be used instead.
- Normally the service id must not be defined, because it is implicitly set to "binding.&lt;binding.id&gt;". A binding can register an OSGi service which implements the ManagedService interface and define the service.pid as e.g."binding.hue" to receive the configuration.


### Example

The following code gives an example for a binding definition.  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<binding:binding id="hue"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:binding="http://eclipse.org/smarthome/schemas/binding/v1.0.0"
    xsi:schemaLocation="http://eclipse.org/smarthome/schemas/binding/v1.0.0
        http://eclipse.org/smarthome/schemas/binding-1.0.0.xsd">

  <name>hue Binding</name>
  <description>The hue Binding integrates the Philips hue system. It allows to control hue bulbs.</description>
  <author>ACME</author>

</binding:binding>
```

## Bridges and Thing Descriptions

Every binding has to provide meta information about which bridges and/or *Thing*s it provides and how their relations to each other are structured. In that way a binding could describe that it requires specific bridges to be operational or define which channels (e.g. temperature, color, etc.) it provides.

Every bridge or *Thing* has to provide meta information such as label or description. The meta information of all bridges and *Thing*s is accessible through the `org.eclipse.smarthome.core.thing.binding.ThingTypeProvider` service.

Bridge and *Thing* descriptions must be placed as XML file(s) (with the ending `.xml`) in the bundle's folder `/ESH-INF/thing/`. The full Java API for bridge and *Thing* descriptions can be found in the Java package `org.eclipse.smarthome.core.thing.type`.


### XML Structure for Thing Descriptions

```xml
<?xml version="1.0" encoding="UTF-8"?>
<thing:thing-descriptions bindingId="bindingID"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:thing="http://eclipse.org/smarthome/schemas/thing-description/v1.0.0"
    xsi:schemaLocation="http://eclipse.org/smarthome/schemas/thing-description/v1.0.0
        http://eclipse.org/smarthome/schemas/thing-description-1.0.0.xsd">

  <bridge-type id="bridgeTypeID" listed="{true|false}" extensible="channelTypeId1,channelTypeId2,...">
    <supported-bridge-type-refs>
      <bridge-type-ref id="bridgeTypeID" />
      ...
    </supported-bridge-type-refs>

    <label>String</label>
    <description>String</description>
    <category>String</category>

    <channels>
      <channel id="channelID" typeId="channelTypeID" />
      OR
      <channel id="channelID" typeId="channelTypeID">
        <label>String</label>
        <description>String</description>
      </channel>
      ...
    </channels>
    OR
    <channel-groups>
      <channel-group id="channelGroupID" typeId="channelGroupTypeID" />
      OR
      <channel-group id="channelGroupID" typeId="channelGroupTypeID">
        <label>String</label>
        <description>String</description>
      </channel-group>
      ...
    </channel-groups>

    <properties>
        <property name="propertyName">propertyValue</property>
        ...
    </properties>
    <representation-property>propertyName</representation-property>

    <config-description>
      ...
    </config-description>
    OR
    <config-description-ref uri="{binding|thing-type|channel-type|any_other}:bindingID:..." />
  </bridge-type>

  <thing-type id="thingTypeID" listed="{true|false}" extensible="channelTypeId1,channelTypeId2,...">
    <supported-bridge-type-refs>
      <bridge-type-ref id="bridgeTypeID" />
      ...
    </supported-bridge-type-refs>

    <label>String</label>
    <description>String</description>
    <category>String</category>

    <channels>
      <channel id="channelID" typeId="channelTypeID" />
      OR
      <channel id="channelID" typeId="channelTypeID">
        <label>String</label>
        <description>String</description>
      </channel>
      ...
    </channels>
    OR
    <channel-groups>
      <channel-group id="channelGroupID" typeId="channelGroupTypeID" />
      OR
      <channel-group id="channelGroupID" typeId="channelGroupTypeID">
        <label>String</label>
        <description>String</description>
      </channel-group>
      ...
    </channel-groups>

    <properties>
        <property name="propertyName">propertyValue</property>
        ...
    </properties>
    <representation-property>propertyName</representation-property>

    <config-description>
      ...
    </config-description>
    OR
    <config-description-ref uri="{binding|thing-type|channel-type|any_other}:bindingID:..." />
  </thing-type>

  <channel-type id="channelTypeID" advanced="{true|false}">
    <item-type>Dimmer</item-type>
    OR
    <kind>trigger</kind>
    <label>String</label>
    <description>String</description>
    <category>String</category>

    <tags>
      <tag>String</tag>
      ...
    </tags>

    <state min="decimal" max="decimal" step="decimal" pattern="String" readOnly="{true|false}">
      <options>
        <option value="String" />
        OR
        <option value="String">String</option>
        ...
      </options>
    </state>
    OR
    <event>
      <options>
        <option value="String" />
        OR
        <option value="String">String</option>
        ...
      </options>
    </event>
    
    <command>
      <options>
        <option value="String" />
        OR
        <option value="String">String</option>
        ...
      </options>
    </command>

    <config-description>
      ...
    </config-description>
    OR
    <config-description-ref uri="{binding|thing-type|channel-type|any_other}:bindingID:..." />
  </channel-type>   

  <channel-group-type id="channelGroupTypeID" advanced="{true|false}">
    <label>String</label>
    <description>String</description>
    <category>String</category>

    <channels>
      <channel id="channelID" typeId="channelTypeID" />
      ...
    </channels>
  </channel-group-type>   

  ...

</thing:thing-descriptions>
```

<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>thing-descriptions.bindingId</td><td>The identifier of the binding this types belong to (mandatory).</td></tr>
</table>

**Bridges and Things:**
<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>bridge-type.id | thing-type.id</td><td>An identifier for the bridge/<i>Thing</i> type (mandatory).</td></tr>
  <tr><td>bridge-type.listed | thing-type.listed</td><td>Denotes if user interfaces should list the bridge/<i>Thing</i>, e.g. for pairing (optional, defaults to true).</td></tr>
  <tr><td>bridge-type.extensible | thing-type.extensible</td><td>If the bridge/<i>Thing</i> supports a generic number of channels the allowed channelTypeIds can be listed here (optional). This provides a hint for UIs to support adding/removing channels. Channel groups are not supported.</td></tr>
  <tr><td>supported-bridge-type-refs</td><td>The identifiers of the bridges this bridge/<i>Thing</i> can connect to (optional).</td></tr>
  <tr><td>bridge-type-ref.id</td><td>The identifier of a bridge this bridge/<i>Thing</i> can connect to (mandatory).</td></tr>
  <tr><td>label</td><td>A human-readable label for the bridge/<i>Thing</i> (mandatory).</td></tr>
  <tr><td>description</td><td>A human-readable description for the bridge/<i>Thing</i> (optional).</td></tr>
  <tr><td>category</td><td>Category this bridge/<i>Thing</i> belongs to, see <a href="../../concepts/categories.html">categories</a>) (optional).</td></tr>
  <tr><td>channels</td><td>The channels the bridge/<i>Thing</i> provides (optional).</td></tr>
  <tr><td>channel.id</td><td>An identifier of the channel the bridge/<i>Thing</i> provides (mandatory).</td></tr>
  <tr><td>channel.typeId</td><td>An identifier of the channel type definition the bridge/<i>Thing</i> provides (mandatory).</td></tr>
  <tr><td>label</td><td>A human-readable label for the channel (optional).</td></tr>
  <tr><td>description</td><td>A human-readable description for the channel (optional).</td></tr>
  <tr><td>channel-groups</td><td>The channel groups defining the channels the bridge/<i>Thing</i> provides (optional).</td></tr>
  <tr><td>channel-group.id</td><td>An identifier of the channel group the bridge/<i>Thing</i> provides (mandatory).</td></tr>
  <tr><td>channel-group.typeId</td><td>An identifier of the channel group type definition the bridge/<i>Thing</i> provides (mandatory).</td></tr>
  <tr><td>properties</td><td>Name/value pairs for properties to be set to the thing (optional).</td></tr>
  <tr><td>representation-property</td><td>The name of the property that contains a unique identifier of the thing (optional).</td></tr>
  <tr><td>config-description</td><td>The configuration description for the bridge/<i>Thing</i> within the ConfigDescriptionRegistry (optional).</td></tr>
  <tr><td>config-description-ref</td><td>The reference to a configuration description for the bridge/<i>Thing</i> within the ConfigDescriptionRegistry (optional).</td></tr>
  <tr><td>config-description-ref.uri</td><td>The URI of the configuration description for the bridge/<i>Thing</i> within the ConfigDescriptionRegistry (mandatory).</td></tr>
</table>

**Channels:**
<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>channel-type.id</td><td>An identifier for the channel type (mandatory).</td></tr>
  <tr><td>channel-type.advanced</td><td>The flag indicating if this channel contains advanced functionalities which should be typically not shown in the basic view of user interfaces (optional, default: false).</td></tr>
  <tr><td>kind</td><td>The kind of channel. <code>state</code> for channels which have a state, <code>trigger</code> for trigger channels. <code>state</code> is the default.</td></tr>
  <tr><td>item-type</td><td>An item type of the channel (mandatory if kind <code>state</code>, which is the default). All item types are specified in <code>ItemFactory</code> instances. The following items belong to the core: <code>Switch, Rollershutter, Contact, String, Number, Dimmer, DateTime, Color, Image</code>.</td></tr>
  <tr><td>label</td><td>A human-readable label for the channel (mandatory).</td></tr>
  <tr><td>description</td><td>A human-readable description for the channel (optional).</td></tr>
  <tr><td>category</td><td>The category for the channel, e.g. <code>TEMPERATURE</code> (optional).</td></tr>
  <tr><td>tags</td><td>A list of default tags to be assigned to bound items (optional).</td></tr>
  <tr><td>tag</td><td>A tag semantically describes the feature (typical usage) of the channel e.g. <code>AlarmSystem</code>. There are no pre-default tags, they are custom-specific (mandatory).</td></tr>
  <tr><td>state</td><td>The restrictions of an item state which gives information how to interpret it (optional).</td></tr>
  <tr><td>state.min</td><td>The minimum decimal value of the range for the state (optional).</td></tr>
  <tr><td>state.max</td><td>The maximum decimal value of the range for the state (optional).</td></tr>
  <tr><td>state.step</td><td>The increasing/decreasing decimal step size within the defined range, specified by the minimum/maximum values (optional).</td></tr>
  <tr><td>state.pattern</td><td>The pattern following the <code>printf</code> syntax to render the state (optional).</td></tr>
  <tr><td>state.readOnly</td><td>The flag indicating if the state is read-only or can be modified (optional, default: false).</td></tr>
  <tr><td>options</td><td>A list restricting all possible values (optional).</td></tr>
  <tr><td>option</td><td>The description for the option (optional).</td></tr>
  <tr><td>option.value</td><td>The value for the option (mandatory). Note that the value may be outside of the range specified in the min/max if this is specified.</td></tr>
  <tr><td>command</td><td>Commands this channel will send to the binding. This is used to model "write-only" channels and gives UIs a hint to display push-buttons without state (optional).</td></tr>
  <tr><td>options</td><td>A list defining the possible commands (optional).</td></tr>
  <tr><td>option</td><td>The description for the option (optional).</td></tr>
  <tr><td>option.value</td><td>The value for the option (mandatory). This is the actual command send to the channel.</td></tr>
  <tr><td>event</td><td>The restrictions of an trigger event which gives information how to interpret it (optional).</td></tr>
  <tr><td>autoUpdatePolicy</td><td>The auto update policy to use (optional).</td></tr>
  <tr><td>config-description</td><td>The configuration description for the channel within the ConfigDescriptionRegistry (optional).</td></tr>
  <tr><td>config-description-ref</td><td>The reference to a configuration description for the channel within the ConfigDescriptionRegistry (optional).</td></tr>
  <tr><td>config-description-ref.uri</td><td>The URI of the configuration description for the channel within the ConfigDescriptionRegistry (mandatory).</td></tr>
</table>

**Channel Groups:**
<table>
  <tr><td><b>Property</b></td><td><b>Description</b></td></tr>
  <tr><td>channel-group-type.id</td><td>An identifier for the channel group type (mandatory).</td></tr>
  <tr><td>channel-group-type.advanced</td><td>The flag indicating if this channel group contains advanced functionalities which should be typically not shown in the basic view of user interfaces (optional, default: false).</td></tr>
  <tr><td>label</td><td>A human-readable label for the channel group (mandatory).</td></tr>
  <tr><td>description</td><td>A human-readable description for the channel group (optional).</td></tr>
  <tr><td>category</td><td>The category for the channel group, e.g. <code>TEMPERATURE</code> (optional).</td></tr>
  <tr><td>channels</td><td>The channels the bridge/<i>Thing</i> provides (mandatory).</td></tr>
  <tr><td>channel.id</td><td>An identifier of the channel the bridge/<i>Thing</i> provides (mandatory).</td></tr>
  <tr><td>channel.typeId</td><td>An identifier of the channel type definition the bridge/<i>Thing</i> provides (mandatory).</td></tr>
</table>

The full XML schema for Thing type descriptions is specified in the <a href="https://www.eclipse.org/smarthome/schemas/thing-description-1.0.0.xsd">ESH thing description XSD</a> file.

**Hints:**

-  Any identifiers of the types are automatically mapped to unique identifiers: `bindingID:id`.
-  The attribute `uri` in the section `config-description` is optional, it *should not* be specified in bridge/*Thing*/channel type definition files because it's an embedded configuration. If the `uri` is *not* specified, the configuration description is registered as `thing-type:bindingID:id` or `channel-type:bindingID:id` otherwise the given `uri` is used.
-  If a configuration description is already specified somewhere else and the bridge/*Thing*/channel type wants to (re-)use it, a `config-description-ref` should be used instead.

## Config Status Provider
Each entity that has a configuration can provide its current configuration status for UIs or specific services to point to issues or to provide further general information of the current configuration. For this purpose the handler of the entity has to implement the interface `org.eclipse.smarthome.config.core.status.ConfigStatusProvider` that has to be registered as OSGi service. The `org.eclipse.smarthome.config.core.status.ConfigStatusService` tracks each configuration status provider and delivers the corresponding `org.eclipse.smarthome.config.core.status.ConfigStatusInfo` by the operation `getConfigStatus(String, Locale)`.
---
layout: documentation
---

{% include base.html %}

# RESTful Web Service API Demo #

## Description ##

The purpose of the demo is to give an example of how to use the Eclipse SmartHome Automation RESTful API. It provides implementation of a simple SmartHome Automation REST Client that gives to the user:

- access to the Automation REST Rule Resource, which provides ability to:
	- list all Automation Rules if there are any
	- create one particular Automation Rule - `AutomationRestAPIDemoSampleRule`
	- update the contents of an Automation Rule, specified by UID
	- list the contents of an Automation Rule, specified by UID
	- delete an Automation Rule, specified by UID
	- enable/disable an Automation Rule, specified by UID
	- list the configuration parameters of an Automation Rule, specified by UID
	- update the configuration parameter values of an Automation Rule, specified by UID
	- list all modules, corresponding to a category, for Automation Rule, specified by UID
	- list a module, corresponding to a category and UID, for Automation Rule, specified by UID
	- list a module configuration, for Module corresponding to a category and UID and for Automation Rule, specified by UID
	- list a module configuration parameter, specified by name, for Module corresponding to a category and UID and for Automation Rule, specified by UID
	- update the value of the module configuration parameter, specified by name, for Module corresponding to a category and UID and for Automation Rule, specified by UID
- access to the Automation REST Module Type Resource, which provides ability to:
	- list all Automation Module Types if there are any
	- list the contents of an Automation Module Type, specified by UID
- access to the Automation REST Template Resource, which provides ability to:
	- list all Automation Templates if there are any
	- list the contents of an Automation Template, specified by UID

## HTTP Service Resources ##

HTTP Service Resources are registered under `**alias** = "/esh/automation/restdemo"`:

- `**name** = "/index.html"`
- `**name** = "/rules.html"`
- `**name** = "/module-types.html"`
- `**name** = "/templates.html"`

----------
Legend:

	**alias** is the equivalent of the OSGi Http Services "alias" in registerResource.
	**name** is the equivalent of the OSGi Http Services "name" in registerResource.
---
layout: documentation
---

{% include base.html %}

# SmartHome Rule Configuration

This document intends to describe the JSON meta definitions for the commonly used module types `ItemStateChangeTrigger`, `ItemStateCondition`, and `ItemCommandAction` in a more textual and intuitive way.

## Item State Change Trigger Configuration

Item state change triggers fire on state changes of a specified item defined in the `itemName` attribute. A trigger's type is to be set to `ItemStateChangeTrigger` when used as a state change trigger. Unlike the related `ItemStateUpdateTrigger`, this trigger requires the triggering state to have changed to a different value.

    {
      "id": "trigger_1",
      "label": "Item State Change Trigger",
      "description": "This triggers a rule if an items state changed",
      "configuration": {
        "itemName": "switchA"
      },
      "type": "ItemStateChangeTrigger"
    }

## Item State Condition Configuration

Rule conditions are usually represented by the following JSON object:

    {
      "inputs": {},
      "id": "condition_1",
      "label": "Item state condition",
      "description": "compares the items current state with the given",
      "configuration": {
        "itemName": "switchA",
        "state": "ON",
        "operator": "="
      },
      "type": "ItemStateCondition"
    }

`itemName` again holds the unique identifier of the polled item. `state` is one of the corresponding item type's supported state strings. The state string is automatically converted to a state object that fits its value and is supported by the corresponding item. For example, `ON` will be converted to an `OnOffType` and `120,100,100` will be converted to an `HSBType`. `operator` specifies a comparative operator, namely one of the following: `=`, `!=`, `<`, `>`

## Action Command Configuration

Similarly to `ItemStateCondition`s, action command configurations reference an item by name and an action string:

    {
      "inputs": {},
      "id": "action_1",
      "label": "Post command to an item",
      "description": "posts commands on items",
      "configuration": {
        "itemName": "switchB",
        "command": "OFF"
      },
      "type": "ItemPostCommandAction"
    }

The string used as the command depends on the item type and its corresponding supported command types, e.g. an HSB value of `120,100,100` to set a colored light's color to green. Similar to state change triggers, the correct state/action type is chosen automatically.

## Item Types and Command Type Formatting

See [Items](../../concepts/items.html)
---
layout: documentation
---

{% include base.html %}

# Java API Demo

The purpose of the demo is to give an example of how to use the Eclipse SmartHome Automation Java API. It is a basic example of an application, named "Welcome Home Application". The application gives ability to the user to switch on the air conditioner and lights in its home remotely. It initializes and registers the services that provide this functionality - Rule Provider, Rule Template Provider, Module Type Provider and Handler Factory for handlers of the modules that compose the rules. Of course, these providers are not mandatory for each application. Some applications may contain only Template Provider or Rule Provider, or Module Type Provider, or Module Handler Factory for some particular module types. Also, to enable the user to have control over the settings and to enforce execution, the demo initializes and registers a service that provides console commands.

## Welcome Home Application

The Welcome Home Application illustrates:

* How to implement Module Types and their provider and how to register it.
* How to implement Rule Templates and their provider and how to register it.
* How to use templates for creation of the Automation Rules.
* How to inject the rules into the Automation Rule Engine by registering Rule Provider service.
* How to implement a Module Handler Factory that helps the Automation Engine to execute the rules and how to register it.
* How to implement the Module Handles of the Automation Module objects.

### Module Types

The Welcome Home Application illustrates how to create your own Module Types and how to provide them to the Automation Engine. Module Types are templates for the creation of the Automation Module objects - Conditions, Triggers and Actions, which are the building blocks of the Automation Rules. When creating an Automation Module object you must specify a Module Type. This will inform the Rule Engine how to treat this object.

#### Trigger Type

Trigger Type gives a base for creation of Trigger objects. Welcome Home Application illustrates how to implement some specific Trigger Types and how to provide them to the Automation Engine. In this demo are exposed two Trigger Types:

	AirConditionerTriggerType
	LightsTriggerType

`AirConditionerTriggerType` can be used for creation of the Triggers that firing a rule that will switch on the Air Conditioner if its current state is "off" and the current room temperature is lower or higher comparing to the target temperature and if the mode of the conditioner is  accordingly "Heating" or "Cooling".

`LightsTriggerType` can be used for creation of the Triggers that firing a rule that will switch on the lights if their current state is "off" or a rule that will lowering the blinds if their current state is "up".

#### Condition Type

Condition Type gives a base for creation of Condition objects. Welcome Home Application illustrates how to implement some specific Condition Types and how to provide them to the Automation Engine. In this demo are exposed two Condition Types:

	TemperatureConditionType
	StateConditionType

`TemperatureConditionType` can be used for creation of the Conditions that make the comparison between the desired temperature and the current room temperature and gives a permission to the Automation Engine to complete the execution of the rule or to terminate it.

`StateConditionType` can be used for creation of the Conditions that make the comparison between the desired state and the current state and gives a permission to the Automation Engine to complete the execution of the rule or to terminate it.

These conditions can be missed if the particular home devices handle the situation.

#### Action Type

Action Type gives a base for creation of Action objects. Welcome Home Application illustrates how to implement some specific Action Types and how to provide them. In this demo is exposed one Action Type:

    WelcomeHomeActionType

`WelcomeHomeActionType` can be used for creation of the Actions that give a command to the particular home devices. Then they will execute it and the rule will be completed.

#### Module Type Provider

Module Type Provider informs the Rule Engine, that it provides some particular Module Types by registering itself as a `ModuleTypeProvider` service and declaring their UIDs in its own registration property `REG_PROPERTY_MODULE_TYPES = "module.types"`.

Example:

	Map<String, ModuleType> providedModuleTypes = new HashMap<String, ModuleType>();
	Dictionary<String, Object> properties = new Hashtable<String, Object>();
	properties.put(REG_PROPERTY_MODULE_TYPES, providedModuleTypes.keySet());
	(BundleContext)bc.registerService(ModuleTypeProvider.class.getName(), moduleTypeProviderObj, properties);

Simple implementation of the `moduleTypeProviderObj` is offered by the class `WelcomeHomeModuleTypeProvider`.

This is the way to give possibility to other applications or users to use these Module Types for creating their own Rules or Templates.

### Rule Templates

The Welcome Home Application illustrates how to create your own Rule Templates and how to provide them to the Automation Engine. They can be used for creation of Automation Rules. The template can be created by one person but other person to choose the rule template and by providing a configuration for it, to create a rule from that. Of course, Welcome Home Application also illustrates a creation of the rules directly from scratch, without need of templates.

#### Rule Templates Description

In this demo is exposed one rule template `AirConditionerRuleTemplate`.

It is created using described above Module Types for creation of its Automation Modules and illustrates how to define its configuration and how to refer its configuration parameters into the configuration of the Automation Modules.

The template configuration parameters are:

* `CONFIG_TARGET_TEMPERATURE = "targetTemperature"` referred by `TemperatureConditionType.CONFIG_TEMPERATURE = "temperature"`
* `CONFIG_OPERATION = "operation"` referred by `TemperatureConditionType.CONFIG_OPERATOR = "operator"`

which are the configuration parameters of the `TemperatureConditionType`. Their default values are `"operation" = "heating"` and `"targetTemperature" = 18`. They are referred so the user can modify their values. For example the `"targetTemperature"` can be set to 20 or the `"operation"` can be set to "cooling".


Also the template illustrates how to connect the outputs of the Trigger to the inputs of the Conditions and Action in scope of the template. The outputs are defined into the `AirConditionerTriggerType`.

The outputs of the Trigger are:

	StateConditionType.INPUT_CURRENT_STATE = "currentState"
	TemperatureConditionType.INPUT_CURRENT_TEMPERATURE = "currentTemperature"

If the default configuration parameter values are set ("heating", 18) and "currentState" output is "off", "currentTemperature" output is 12, the air conditioner will be switched on. If the "currentState" output is "on" or the "currentTemperature" output is 20, then the rule will end before the action to be executed.

If we change the configuration parameter values to the offered one ("cooling", 20) and "currentState" output is "off", "currentTemperature" output is 22, the air conditioner will be switched on. If the "currentState" output is "on" or the "currentTemperature" output is 20, then the rule will end before the action to be executed.

#### Rule Template Provider

Rule Template Provider informs the Rule Engine, that it provides some particular Rule Templates by registering itself as a `TemplateProvider` service and declaring their UIDs in its own registration property `REG_PROPERTY_RULE_TEMPLATES = "rule.templates"`.

Example:

	Map<String, RuleTemplate> providedRuleTemplates = new HashMap<String, RuleTemplate>();
	Dictionary<String, Object> properties = new Hashtable<String, Object>();
	properties.put(REG_PROPERTY_RULE_TEMPLATES, providedRuleTemplates.keySet());
	(BundleContext)bc.registerService(TemplateProvider.class.getName(), ruleTemplateProviderObj, properties);

Simple implementation of the `ruleTemplateProviderObj` is offered by the class `WelcomeHomeTemplateProvider`.

This is the way to give possibility to other applications or users to use the Templates for creating their own Rules.

### Rules

The Welcome Home Application illustrates how to create your own Rules and how to provide them to the Automation Engine, so it can execute them.

#### Rules Description

Creation of the rules provided by this demo are exposed into `WelcomeHomeRulesProvider` class.

Demo Rule UIDs are:

	AC_UID = "AirConditionerSwitchOnRule"
	L_UID = "LightsSwitchOnRule"

`AirConditionerSwitchOnRule` illustrates how to create a rule from template by defining `UID`, `templateUID` and `configuration`. The configuration should contain as keys all required parameter names of the configuration parameters of the template and values for them. This rule gives ability to the user to switch on the air conditioner if it is switched off, his mode is set on "heating" and the current temperature is lower then target temperature or to switch on the air conditioner if it is switched off, his mode is set on "cooling" and the current temperature is higher then target temperature.

`LightsSwitchOnRule` illustrates how to create a rule from scratch by defining one trigger, two conditions, one action, configuration descriptions, configuration values and tags. This rule gives ability to the user to switch on the lights in its home if they are switched off.

#### Rule Provider

Rule Provider is implemented by `WelcomeHomeRulesProvider` class. It provides two rules that give ability to the user to switch on the air conditioner and lights in its home remotely. It informs the Automation Engine by registering itself as a `RuleProvider` service.

Example:

	(BundleContext)bc.registerService(RuleProvider.class.getName(), ruleProviderObj, null);

### Module Handlers

Module Handlers are helpers of the Automation Engine. Automation Engine gives them the module and they know what to do with it. They do the real work. The Automation Engine only decides which of them to use and when.

#### Trigger Handler

Trigger Handler serves to notify the Automation Engine about firing the Triggers. Simple implementation of it can be seen into `WelcomeHomeTriggerHandler` class.

#### Condition Handler

Condition Handler serves to help the Automation Engine to decide if it continues with the execution of the rule or to terminate it. Simple implementation of it can be seen into `StateConditionHandler` or `TemperatureConditionHandler` class.

#### Action Handler

Action Handler is used to help the Automation Engine to execute the specific Actions. A simple implementation of it can be seen into `WelcomeHomeActionHandler` class.

#### Module Handler Factory

Module Handler Factory serves as provider of the Module Handlers. It registers itself as a service to inform the Automation Engine, handlers for which Module Types provides. The Automation Engine refers to it, gives it a module and receives in response a handler of the module. A simple implementation of it can be seen into `WelcomeHomeHandlerFactory` class.

### Commands

The demo provides two commands that enable the user to have control over the settings and to enforce execution of the rules.

#### Welcomehome Commands Description

##### Command `settings`
Parameters: `<mode> <temperature>`

Description:
	Serves to configure air conditioner's mode(cooling/heating) and target temperature by updating the `AirConditionerSwitchOnRule` rule configuration

##### Command `activateAC`
Parameters: `<currentState> <currentTemperature>`

Description:
	Serves to switch on the air conditioner by providing current temperature, current state(on/off) of the air conditioner as inputs of the conditions `TemperatureConditionType` and `StateConditionType`

##### Command `activateLights`
Parameters: `<currentState>`

Description:
	Serves to switch on the lights by providing current state(on/off) of the lights as an input of the condition `StateConditionType`


##### Examples:

###### `welcomehome settings cooling 20` -> result : "AirConditionerSwitchOnRule" rule configuration will be updated: "targetTemperature"=20, "operation"="cooling"

###### `welcomehome activateAC off 20` -> result : Air Conditioner is switched on

###### `welcomehome activateLights off` -> result : Lights are switched on


You can try to play with these values and see what will happen.

#### SmartHome Commands

To see the automation objects that this demo provides you can use `smarthome automation` group commands.

Example(s):
* `smarthome automation listRules AirConditionerSwitchOnRule`
---
layout: documentation
---

{% include base.html %}

# Audio & Voice

Eclipse SmartHome provides a modular architecture that enables all kinds of different use cases.
At its core, there is the notion of an _audio stream_.
Audio streams are provided by _audio sources_ and consumed by _audio sinks_.
Each binding for handling and controlling audio services can implement an audio sink to provide their supported devices to the framework to be used as sound output.
An audio sink is identified by an unique id which in general is similar to the thing type id.
The framework itself can handle multiple audio sinks at the same time.
You can define a default sink for your purpose (e.g. in the Paper UI).

## Audio

The distribution comes with these built-in audio sinks options:

| Output device     | Audio sink                        | Description                                                                                                                                                                                                                                                                                                        |
|-------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| javasound         | System Speaker                    | This uses the JRE sound drivers to play audio to the local sound interface.                                                                                                                                                                                                                                        |
| enhancedjavasound | System Speaker (with mp3 support) | This uses the JRE sound drivers plus an additional 3rd party library, which adds support for mp3 files.                                                                                                                                                                                                            |
| webaudio          | Web Audio                         | If sounds should not be played on the server but on the client: This sink sends the audio stream through HTTP to web clients, which then cause it to be played back by the browser. The browser needs to be opened and have a compatible UI running. Currently this feature is supported by Paper UI and HABPanel. |

The framework is able to play sound either from the file system, from URLs (e.g. Internet radio streams) or generated by text-to-speech engines (which are available as optional Voice add-ons).
There are two different ways to play or stream audio:

- using built-in functions within DSL rules;
- using text console commands: smarthome:audio;

### Built-in functions within DSL rules

| Command                                                | Description                                                                                                 |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `playSound(String filename)`                           | plays a sound from the sounds folder to the default sink                                                    |
| `playSound(String filename, PercentType volume)`       | plays a sound with the given volume from the sounds folder to the default sink                              |
| `playSound(String sink, filename)`                     | plays a sound from the sounds folder to the given sink(s)                                                   |
| `playSound(String sink, filename, PercentType volume)` | plays a sound with the given volume from the sounds folder to the given sink(s)                             |
| `playStream(String url)`                               | plays an audio stream from an url to the default sink (set `url` to `null` if streaming should be stopped)  |
| `playStream(String sink, String url)`                  | plays an audio stream from an url to the given sink(s) (set `url` to `null` if streaming should be stopped) |
| `float getMasterVolume()`                              | gets the master volume, returns the volume as a float in the range [0,1]                                    |
| `setMasterVolume(float volume)`                        | sets the master volume, `volume` in the range [0,1]                                                         |
| `setMasterVolume(PercentType percent)`                 | sets the master volume                                                                                      |
| `increaseMasterVolume(float percent)`                  | increases the master volume, `percent` in the range (0,100]                                                 |
| `decreaseMasterVolume(float percent)`                  | increases the master volume, `percent` in the range (0,100]                                                 |

### Text console commands

| Command                                           | Description                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `smarthome:audio play [<sink>] <filename>`        | plays a sound file from the `conf/sounds` folder through the optionally specified audio sink(s)                |
| `smarthome:audio play <sink> <filename> <volume>` | plays a sound file from the `conf/sounds` folder through the specified audio sink(s) with the specified volume |
| `smarthome:audio stream [<sink>] <url>`           | streams the sound from the url through the optionally specified audio sink(s)                                  |
| `smarthome:audio sources`                         | lists the audio sources                                                                                        |
| `smarthome:audio sinks`                           | lists the audio sinks                                                                                          |

## Voice

Voice services are separate bindings with the ability to synthesize written text to speech using a given voice.
In order to use text-to-speech, you need to install at least one TTS service.
Once you have done so, you will find different voices available in your system.
Each voice supports exactly one language.
You can define a default TTS service and a default voice to use (e.g. in the Paper UI).
How to use TTS:

- using built-in functions within DSL rules;
- using text console commands: smarthome:voice;
- using REST API methods (only for HLI);

### Built-in functions within DSL rules

| Command                                                           | Description                                                                                |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `String interpret(Object text)`                                   | interprets a given text by the default human language interpreter, human language response |
| `String interpret(Object text, String interpreter)`               | interprets a given text by a given human language interpreter, human language response     |
| `say(Object text)`                                                | says a given text with the default voice                                                   |
| `say(Object text, PercentType volume)`                            | says a given text with the default voice and the given volume                              |
| `say(Object text, String voice)`                                  | says a given text with a given voice                                                       |
| `say(Object text, String voice, PercentType volume)`              | says a given text with a given voice and the given volume                                  |
| `say(Object text, String voice, String sink)`                     | says a given text with a given voice through the given sink                                |
| `say(Object text, String voice, String sink, PercentType volume)` | says a given text with a given voice and the given volume through the given sink           |

### Text console commands

| Command                               | Description                                                            |
|---------------------------------------|------------------------------------------------------------------------|
| `smarthome:voice say <text>`          | speaks a text on the default audio sink with the default TTS and voice |
| `smarthome:voice voices`              | lists available voices of the active TTS services                      |
| `smarthome:voice interpret <command>` | interprets a human language command                                    |

### REST API

- GET /voice/interpreters Get the list of all interpreters.
- POST /voice/interpreters Sends a text to the default human language interpreter.
- GET /voice/interpreters/{id} Gets a single interpreters.
- POST /voice/interpreters/{id} Sends a text to a given human language interpreter.

---
layout: documentation
---

{% include base.html %}

# Textual Configuration

Eclipse SmartHome provides the possibility to do fully text-based system setups. This is done using domain specific languages (DSLs) for the different kinds of artifacts.
In addition, configuration files can be used to configure OSGi services which are able to be configured by Configuration Admin.  

## Thing Configuration DSL

Things can be configured with a Domain specific Language (DSL). It is recommended to use the Eclipse SmartHome Designer for editing the DSL files, because it supports validation and auto-completion.

Thing configuration files must be placed under the `things` folder inside the Eclipse SmartHome `conf` folder and must end with the suffix `.things`.

## Defining Things

Things can be defined as followed:

```
Thing yahooweather:weather:berlin [ location=638242 ]
Thing yahooweather:weather:losangeles "Los Angeles" @ "home" [ location=2442047, unit="us", refresh=120 ]
```

The first keyword defines whether the entry is a bridge or a thing. The next statement defines the UID of the thing which contains of the following three segments: binding id, thing type id, thing id. So the first two segments must match to thing type supported by a binding (e.g. `yahooweather:weatheryahooweather`), whereas the thing id can be freely defined. Optionally, you may provide a label in order to recognize it easily, otherwise the default label from the thing type will be displayed.

To help organizing your things, you also may define a location (here: "home"), which should point to an item. This item can either be a simple String item carrying e.g. the room name, or you may of course also use a Location item containing some geo coordinates.  

Inside the squared brackets configuration parameters of the thing are defined.

The type of the configuration parameter is determined by the binding and must be specified accordingly in the DSL. If the binding requires a text the configuration parameter must be specified as a decimal value: `location=2442047`. Other types are for example boolean values (`refreshEnabled=true`).

For each thing entry in the DSL the framework will create a thing by calling the ThingFactory of the according binding.

### Shortcut

It is possible to skip the `Thing` keyword: `yahooweather:weather:berlin [ location=638242 ]`

## Defining Bridges

The DSL also supports the definition of bridges and contained things. The following configuration shows the definition of a hue bridge with two hue lamps:

```
Bridge hue:bridge:mybridge [ ipAddress="192.168.3.123" ] {
	Thing 0210 bulb1 [ lightId="1" ]
	Thing 0210 bulb2 [ lightId="2" ]
}
```

Within the curly brackets things can be defined, that should be members of the bridge. For the contained thing only the thing type ID and thing ID must be defined (e.g. `0210 bulb1`). So the syntax is `Thing <thingTypeId> <thingId> []`. The resulting UID of the thing is `hue:0210:mybridge:bulb1`.

Bridges that are defined somewhere else can also be referenced in the DSL:

```
Thing hue:0210:mybridge:bulb (hue:bridge:mybridge) [lightId="3"]
```

The referenced bridge is specified in the parentheses. Please notice that the UID of the thing also contains the bridge ID as third segment. For the contained notation of things the UID will be inherited and the bridge ID is automatically taken as part of the resulting thing UID.

## Defining Channels

It is also possible to manually define channels in the DSL. Usually this is not needed, as channels will be automatically created by the binding based on the thing type description. But there might be some bindings, that require the manual definition of channels.

### State channels

```
Thing yahooweather:weather:losangeles [ location=2442047, unit="us", refresh=120 ] {
	Channels:
		State String : customChannel1 "My Custom Channel" [
			configParameter="Value"
		]
		State Number : customChannel2 []
}
```

Each channel definition must be placed inside the curly braces and begin with the keyword `State` followed by the accepted item type (e.g. String). After this the channel ID follows with the configuration of a channel. The framework will merge the list of channels coming from the binding and the user-defined list in the DSL.

As state channels are the default channels, you can omit the `State` keyword, the following example creates the same channels as the example above:

```
Thing yahooweather:weather:losangeles [ location=2442047, unit="us", refresh=120 ] {
	Channels:
		String : customChannel1 "My Custom Channel" [
			configParameter="Value"
		]
		Number : customChannel2 []
}
```

You may optionally give the channel a proper label (like "My Custom Channel" in the example above) so you can distinguish the channels easily.


### Trigger channels

```
Thing yahooweather:weather:losangeles [ location=2442047, unit="us", refresh=120 ] {
	Channels:
		Trigger String : customChannel1 [
			configParameter="Value"
		]
}
```

Trigger channels are defined with the keyword `Trigger` and only support the type String.

### Referencing existing channel types

Many bindings provide standalone channel type definitions like this:  

```
<thing:thing-descriptions bindingId="yahooweather" [...]>
    <channel-type id="temperature">
        <item-type>Number</item-type>
        <label>Temperature</label>
        <description>Current temperature in degrees celsius</description>
        <category>Temperature</category>
        <state readOnly="true" pattern="%.1f °C">
        </state>
    </channel-type>
    [...]
</thing:thing-descriptions>
```

They can be referenced within a thing's channel definition, so that they need to be defined only once and can be reused for many channels. You may do so in the DSL as well:

```
Thing yahooweather:weather:losangeles [ location=2442047, unit="us", refresh=120 ] {
    Channels:
        Type temperature : my_yesterday_temperature "Yesterday's Temperature"
}
```

The `Type` keyword indicates a reference to an existing channel definition. The channel kind and accepted item types of course are takes from the channel definition, therefore they don't need to be specified here again.

You may optionally give the channel a proper label (like "Yesterday's Temperature" in the example above) so you can distinguish the channels easily. If you decide not to, then the label from the referenced channel type definition will be used.

## Configuring OSGi Services

In order to provide file based, static configuration for OSGi services, Eclipse SmartHome provides a way to read, parse and observe configuration files.
The configuration which is read from these files will be passed to the OSGi Configuration Admin.
The fundamentals of configuring OSGi services are described [here](http://enroute.osgi.org/doc/217-ds.html) in great detail.

### Default Configuration File

Eclipse SmartHome reads its basic configuration from the default configuration file `conf/smarthome.cfg` in the programs root folder.
The path to this file can be altered using the program argument `smarthome.servicecfg`.
In case only the `conf` folder path should be altered the program argument `smarthome.configdir` can be used (be aware that this will also change the location for the `things`, `items` and all other configuration folders).
Configurations for OSGi services are kept in a subfolder that can be provided as a program argument `smarthome.servicedir` (default is "services"). Any file in this folder with the extension .cfg will be processed.

### Configuration File Format
The basic configuration file format is very simple. This format is used in the `smarthome.cfg` to address different services from one file:

```
<configuration_pid1>:<key1>=<value1>
<configuration_pid1>:<key2>=<value2>

<configuration_pid2>:<key>=<value>

<configuration_pid3>:<key>=<value>
```

The line prefix `configuration_pid[1-3]` correspond to the configuration PID which is configured for the specific OSGi service.
`<key>` and `<value>` define the configuration option for the specific service.

With every line denoting a specific configuration PID, several services can be configured using just one configuration file.
In addition the configuration PID can also be derived from the filename.
Given the configuration file `conf/services/org.eclipse.smarthome.basicui.cfg` with content `defaultSitemap=demo` will configure the `defaultSitemap` option of the Basic UI service, giving it the value `demo`.
This way a service can be configured just by giving `<key>=<value>` pairs in the file.

When providing the PID by filename or by line prefix there is one additional shortcut:
The files are processed line-by-line from top to bottom.
The last defined PID (either by file name or by line prefix) will be kept to be used for the next entry.
This makes the following example a valid and fully functional service configuration for multiple services.

Although not recommended, the file `conf/services/org.eclipse.smarthome.threadpool.cfg` with the following content:

```property
thingHandler=3
discovery=3

org.eclipse.smarthome.basicui:defaultSitemap=demo
enableIcons=true
condensedLayout=false
```

will configure the `org.eclipse.smarthome.threadpool` service to have the `thingHandler` and `discovery` option set to `3` and also configure the `org.eclipse.smarthome.basicui` service with three different options.

All the above configuration files will be observed for changes.
When the framework detects a change (or even a new *.cfg file) the changes will be read and applied to the specific service.
Since a single service may be configured using multiple files this observation will _not delete_  configuration options from the Configuration Admin.
In order to track deletion of configuration entries and files the configuration has to be marked as an exclusive service configuration.

### Exclusive Service Configuration

The framework will track exclusively marked service configurations for file or entry deletions. This way a configuration can be removed during runtime. For factory services even a whole service instance can be added and removed during runtime.

To mark a configuration file exclusively for one service the _first line_ has to define the configuration PID in the format `pid:<configuration_pid>`.
By giving this PID marker the framework creates an exclusive configuration for the contents of this file.
Other files without this marker which also define configurations for the given PID will be ignored for this PID.

The file `conf/services/myService.cfg` with contents

```property
pid:org.eclipse.smarthome.bundle.myService
timeout=30
callback=MyCallback

```

will exclusively configure the OSGi service with configuration_pid `org.eclipse.smarthome.bundle.myService` set.
Any other configuration for this PID in other configuration files will be ignored now.
In contrast, when removing the line `timeout=30` from the file, the service's `modified` method will be called with a new configuration which does not include the `timeout` option anymore.
When removing the whole file the configuration will completely be deleted from the Configuration Admin.


### Factory Service Configuration

Using the format of an exclusive service configuration it is also possible to create several instances of a specific service.
By giving a unique context along with the exclusive PID in the format `pid:<configuration_pid>#<context>` the framework will create a new instance for this service.
---
layout: documentation
---

{% include base.html %}

# Event Type Definition

Eclipse SmartHome provides the possibility to easily implement new event types and event factories. 

## Define new Event Type

Events can be added by implementing the `Event` interface or extending the `AbstractEvent` class which offers a default implementation. Both classes are located in the Eclipse SmartHome core bundle. 

The following Java snippet shows a new event type extending the class `AbstractEvent`.

```java
public class SunriseEvent extends AbstractEvent {

    public static final String TYPE = SunriseEvent.class.getSimpleName();
    
    private final SunriseDTO sunriseDTO;

    SunriseEvent(String topic, String payload, SunriseDTO sunriseDTO) {
        super(topic, payload, null);
        this.sunriseDTO = sunriseDTO;
    }

    @Override
    public String getType() {
        return TYPE;
    }
    
    public SunriseDTO getSunriseDTO() {
        return sunriseDTO;
    }

    @Override
    public String toString() {
        return "Sunrise at '" + getSunriseDTO.getTime() + "'.";
    }
}
```

The listing below summarizes some coding guidelines as illustrated in the example above:

- Events should only be created by event factories. Constructors do not have any access specifier in order to make the class package private.
- The serialization of the payload into a data transfer object (e.g. `SunriseDTO`) should be part of the event factory and will be assigned to a class member via the constructor. 
- A public member `TYPE` represents the event type as string representation and is usually the name of the class.
- The `toString()` method should deliver a meaningful string since it is used for event logging.
- The source of an event can be `null` if not required.

For more information about implementing an event, please refer to the Java documentation.

## Define new Event Factory

Event factories can be added by implementing the `EventFactory` interface or extending the `AbstractEventFactory` class. The `AbstractEventFactory` provides some useful utility for parameter validation and payload serialization & deserialization with JSON. The classes are located in the Eclipse SmartHome core bundle.

```java 
public class SunEventFactory extends AbstractEventFactory {

    private static final String SUNRISE_EVENT_TOPIC = "smarthome/sun/{time}/sunrise";

    public SunEventFactory() {
        super(Sets.newHashSet(SunriseEvent.TYPE);
    }

    @Override
    protected Event createEventByType(String eventType, String topic, String payload, String source) throws Exception {
        if (SunriseEvent.TYPE.equals(eventType)) {
            return createSunriseEvent(topic, payload);
        } 
        return null;
    }
    
    private Event createSunriseEvent(String topic, String payload) {
        SunriseDTO sunriseDTO = deserializePayload(payload, SunriseDTO.class);
        return new SunriseEvent(topic, payload, sunriseDTO);
    }
    
    public static SunriseEvent createSunriseEvent(Sunrise sunrise) {
        String topic = buildTopic(SUNRISE_EVENT_TOPIC, sunrise.getTime());
        SunriseDTO sunriseDTO = map(sunrise);
        String payload = serializePayload(sunriseDTO);
        return new SunriseEvent(topic, payload, sunriseDTO);
    }
}
```
The listing below summarizes some guidelines as illustrated in the example above:

- Provide the supported event types (`SunriseEvent.TYPE`) via an `AbstractEventFactory` constructor call. The supported event types will be returned by the `AbstractEventFactory.getSupportedEventTypes()` method.
- The event factory defines the topic (`SUNRISE_EVENT_TOPIC`) of the supported event types. Please ensure that the topic format follows the topic structure of the Eclipse SmartHome core events, similar to a REST URI (`{namespace}/{entityType}/{entity}/{sub-entity-1}/.../{sub-entity-n}/{action}`). The namespace must be `smarthome`.
- Implement the method `createEventByType(String eventType, String topic, String payload, String source)` to create a new event based on the topic and the payload, determined by the event type. This method will be called by the framework in order to dispatch received events to the corresponding event subscribers. If the payload is serialized with JSON, the method `deserializePayload(String payload, Class<T> classOfPayload)` can be used to deserialize the payload into a data transfer object.
- Provide a static method to create event instances based on a domain object (Item, Thing, or in the example above `Sunrise`). This method can be used by components in order to create events based on domain objects which should be sent by the EventPublisher. If the data transfer object should be serialized into a JSON payload, the method `serializePayload(Object payloadObject)` can be used.

For more information about implementing an event factory, please refer to the Java documentation.
---
layout: documentation
---

{% include base.html %}

# Events

The Eclipse SmartHome framework provides an event bus for inter-component communication. The communication is based on events which can be sent and received through the event bus in an asynchronous way. Examples of Eclipse SmartHome event types are _ItemCommandEvent_, _ItemStateEvent_, _ItemAddedEvent_, _ThingStatusInfoEvent_, etc.

This section gives a short overview about the event API and illustrates how to receive such events. Furthermore, the sending of events and the implementation of new event types will be described.

A code snippet about receiving events can be found in chapter "Receive Events". In particular, receiving _ItemStateEvents_ and _ItemCommandEvents_ is described in chapter "Receive ItemStateEvents and ItemCommandEvents".

## API Introduction

### The Interfaces

![Event Interfaces](diagrams/event_interfaces.png)

The `EventPublisher` posts `Event`s through the Eclipse SmartHome event bus in an asynchronous way. The `EventSubscriber` defines the callback interface to receive  events of specific types to which the event subscriber is subscribed. The EventPublisher and the EventSubscribers are registered as OSGi services. An event subscriber can provide an `EventFilter` in order to filter events based on the topic or the content. If there is no filter all subscribed event types are received. The event itself will be subclassed for each event type, which exists in the System (e.g. ItemCommandEvent, ItemUpdatedEvent, ThingStatusInfoEvent).

### The Core Events
This section lists the core events provided by Eclipse SmartHome which can be divided into the categories _Item Events_, _Thing Events_ and _Inbox Events_.

An event consists of a `topic`, a `type`, a `payload` and a `source`. The payload can be serialized with any String representation and is determined by its concrete event type implementation (e.g. ItemCommandEvent, ItemUpdatedEvent). The payloads of the Eclipse SmartHome core events are serialized with JSON. Each event implementation provides the payload as high level methods as well, usually presented by a data transfer object (DTO).

A topic clearly defines the target of the event and its structure is similar to a REST URI, except the last part, the action. The topics of Eclipse SmartHome events are divided into the following four parts: `{namespace}/{entityType}/{entity}/{action}`, e.g. `smarthome/items/{itemName}/command`.

The type of an event is represented by a string, usually the name of the concrete event implementation class, e.g. ItemCommandEvent, ItemUpdatedEvent. This string type presentation is used by event subscribers for event subscription (see chapter "Receive Events") and by the framework for the creation of concrete event instances.

The event source is optional and represents the name of the source identifying the sender.

#### Item Events

| Event                 |Description                                      |Topic                                   |
|-----------------------|-------------------------------------------------|----------------------------------------|
| ItemAddedEvent        |An item has been added to the item registry.     |smarthome/items/{itemName}/added        |
| ItemRemovedEvent      |An item has been removed from the item registry. |smarthome/items/{itemName}/removed      |
| ItemUpdatedEvent      |An item has been updated in the item registry.   |smarthome/items/{itemName}/updated      |
| ItemCommandEvent      |A command is sent to an item via a channel.      |smarthome/items/{itemName}/command      |
| ItemStateEvent        |The state of an item is updated.                 |smarthome/items/{itemName}/state        |
| ItemStateChangedEvent |The state of an item has changed.                |smarthome/items/{itemName}/statechanged |

**Note:** The ItemStateEvent is always sent if the state of an item is updated, even if the state did not change. ItemStateChangedEvent is sent only if the state of an item was really changed. It contains the old and the new state of the item.

#### Thing Events

| Event                 |Description                                       |Topic                                   |
|-----------------------|-------------------------------------------------|-----------------------------------|
| ThingAddedEvent         |A thing has been added to the thing registry.    |smarthome/things/{thingUID}/added  |
| ThingRemovedEvent      |A thing has been removed from the thing registry.|smarthome/things/{thingUID}/removed|
| ThingUpdatedEvent     |A thing has been updated in the thing registry.  |smarthome/things/{thingUID}/updated|
| ThingStatusInfoEvent    |The status of a thing is updated.                  |smarthome/things/{thingUID}/status |
| ThingStatusInfoChangedEvent    |The status of a thing changed.                  |smarthome/things/{thingUID}/statuschanged |

**Note:** The ThingStatusInfoEvent is always sent if the status info of a thing is updated, even if the status did not change. ThingStatusInfoChangedEvent is sent only if the status of a thing was really changed. It contains the old and the new status of the thing.

#### Inbox Events

| Event                 |Description                                         |Topic                                   |
|-----------------------|---------------------------------------------------|-----------------------------------|
| InboxAddedEvent         |A discovery result has been added to the inbox.     |smarthome/inbox/{thingUID}/added   |
| InboxRemovedEvent     |A discovery result has been removed from the inbox. |smarthome/inbox/{thingUID}/removed |
| InboxUpdateEvent         |A discovery result has been updated in the inbox.   |smarthome/inbox/{thingUID}/updated |

#### Link Events

| Event                       |Description                                              |Topic                                           |
|-----------------------------|---------------------------------------------------------|------------------------------------------------|
| ItemChannelLinkAddedEvent   |An item channel link has been added to the registry.     |smarthome/links/{itemName}-{channelUID}/added   |
| ItemChannelLinkRemovedEvent |An item channel link has been removed from the registry. |smarthome/links/{itemName}-{channelUID}/removed |

#### Channel Events

| Event                       |Description                                              |Topic                                           |
|-----------------------------|---------------------------------------------------------|------------------------------------------------|
| ChannelTriggeredEvent       |A channel has been triggered.                            |smarthome/channels/{channelUID}/triggered       |

## Receive Events

This section describes how to receive Eclipse SmartHome events in Java. If you want to receive events "outside" Eclipse SmartHome, e.g. with JavaScript, please refer to the [Server Sent Events section](../features/rest.html).

An event subscriber defines the callback interface for receiving events from the Eclipse SmartHome event bus. The following Java snippet shows how to receive `ItemStateEvent`s and `ItemCommandEvent`s from the event bus. Therefore, the `EventSubscriber` interface must be implemented.

```java
public class SomeItemEventSubscriber implements EventSubscriber {
    private final Set<String> subscribedEventTypes = ImmutableSet.of(ItemStateEvent.TYPE, ItemCommandEvent.TYPE);
    private final EventFilter eventFiter = new TopicEventFilter("smarthome/items/ItemX/.*");

    @Override
    public Set<String> getSubscribedEventTypes() {
        return subscribedEventTypes;
    }

    @Override
    public EventFilter getEventFilter() {
        return eventFilter;
    }

    @Override
    public void receive(Event event) {
        String topic = event.getTopic();
        String type = event.getType();
        String payload = event.getPayload();
        if (event instanceof ItemCommandEvent) {
            ItemCommandEvent itemCommandEvent = (ItemCommandEvent) event;
            String itemName = itemCommandEvent.getItemName();
            Command command = itemCommandEvent.getItemCommand();
            // ...
        } else if (event instanceof ItemStateEvent) {
            ItemStateEvent itemStateEvent = (ItemStateEvent) event;
            // ...
        }
    }
}
```
The `SomeItemEventSubscriber` is subscribed to the event types `ItemStateEvent` and `ItemCommandEvent`, provided by the method `getSubscribedEventTypes()`. A string representation of an event type can be found by a public member `TYPE` which usually presents the name of the class. To subscribe to all available event types, use the public member `ALL_EVENT_TYPES` of the event subscriber interface.

The event subscriber provides a `TopicEventFilter` which is a default Eclipse SmartHome `EventFilter` implementation that ensures filtering of events based on a topic. The argument of the filter is a [Java regular expression](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html). The filter method `EventFilter.apply()` will be called for each event on the event bus to which the event subscriber is subscribed (in the example above ItemStateEvent and ItemCommandEvent). If the filter applies (in the given example for all item events with the item name "ItemX"), the event will be received by the `EventSubscriber.receive()` method. Received events can be cast to the event implementation class for further processing.

Each event subscriber must be registered via OSGi Declarative Services (DS) under the  `org.eclipse.smarthome.event.EventSubscriber` interface.

```xml
<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.1.0" immediate="true" name="SomeItemEventSubscriber">
   <implementation class="org.eclipse.smarthome.core.items.events.SomeItemEventSubscriber"/>
   <service>
      <provide interface="org.eclipse.smarthome.core.events.EventSubscriber"/>
   </service>
</scr:component>
```  

The listing below summarizes some best practices in order to implement event subscribers:

- To subscribe to only one event type Eclipse SmartHome provides the `org.eclipse.smarthome.core.events.AbstractTypedEventSubscriber` implementation. To receive an already cast event the `receiveTypedEvent(T)` method must be implemented. To provide an event filter the method `getEventFilter()` can be overridden.
- Eclipse SmartHome provides an `AbstractItemEventSubscriber` class in order to receive ItemStateEvents and ItemCommandEvents (more information can be obtained in the next chapter).
- To filter events based on a topic the  `org.eclipse.smarthome.core.events.TopicEventFilter` implementation from the Eclipse SmartHome core bundle can be used. The filtering is based on [Java regular expression](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).
- The subscribed event types and the filter should be stored as class members (see example above) due to performance reasons.
- If the subscribed event types are sufficient in order to receive all interested events, do not return any filter (in that case the method getFilter() returns null) due to performance reasons.
- Avoid the creation of too many event subscribers. Similar event types can be received in one event subscriber.
- Handle exceptions in event subscriber implementation and throw only serious exceptions. Thrown exceptions will be handled in the framework by logging an error message with the cause.
- The receive method should terminate quickly, since it blocks other event subscribers. Create a thread for long running operations.


### Receive ItemStateEvents and ItemCommandEvents
Due to the fact that receiving ItemStateEvents and ItemCommandEvents is a common use case, Eclipse SmartHome provides an abstract event subscriber implementation via the core bundle. The class `org.eclipse.smarthome.core.items.events.AbstractItemEventSubscriber` provides two methods `receiveUpdate(ItemStateEvent)` and `receiveCommand(ItemCommandEvent)` which can be implemented in order to receive and handle such events.

```java
public class SomeItemEventSubscriber extends AbstractItemEventSubscriber {
    private final EventFilter eventFiter = new TopicEventFilter("smarthome/items/ItemX/.*");

    @Override
    public EventFilter getEventFilter() {
        return eventFilter;
    }

    @Override    
    protected void receiveCommand(ItemCommandEvent commandEvent) {
        // do something
    }

    @Override
    protected void receiveUpdate(ItemStateEvent stateEvent) {
        // do something
    }
}
```

## Send Events

Usually the core events are only sent by the Eclipse SmartHome framework. However, it is possible to sent events explicitly, e.g. ItemCommandEvents and ItemStateEvents. The Java snippet below illustrates how to send events via the EventPublisher. The Eclipse SmartHome core events can only be created via the corresponding event factory.

```java
public class SomeComponentWantsToPost {
    private EventPublisher eventPublisher;

    public void postSomething() {
        ItemCommandEvent itemCommandEvent = ItemEventFactory.createCommandEvent("ItemX", OnOffType.ON);
        eventPublisher.post(itemCommandEvent);
    }

    protected void setEventPublisher(EventPublisher eventPublisher) {
        this.eventPublisher = eventPublisher;
    }

    protected void unsetEventPublisher(EventPublisher eventPublisher) {
        this.eventPublisher = null;
    }
}
```

The EventPublisher will be injected via OSGi Declarative Services.

```xml
<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.1.0" immediate="true" name="SomeComponentWantsToPost">
    <!-- ... -->
   <reference bind="setEventPublisher" cardinality="1..1" interface="org.eclipse.smarthome.core.events.EventPublisher"
           name="EventPublisher" policy="static" unbind="unsetEventPublisher"/>
</scr:component>
```

## Define new Event Types

It is possible to create and provide new event types. For a detailed description please refer to the [Event Type Definition section](./event-type-definition.html).
---
layout: documentation
---

# Framework Utilities

In this chapter useful services/utilities of the Eclipse SmartHome project are described. 

## Network Address Service

The `NetworkAddressService` is an OSGi service that can be used like any other OSGi service by adding a service reference to it. Its OSGi service name is `org.eclipse.smarthome.network`.
A user can configure his default network address via Paper UI under `Configuration -> System -> Network Settings`.
One can obtain the configured address via the `getPrimaryIpv4HostAddress()` method on the service.
This service is useful for example in the `ThingHandlerFactory` or an `AudioSink` where one needs a specific IP address of the host system to provide something like a `callback` URL.

Some static methods like `getAllBroadcastAddresses()` for retrieving all interface broadcast addresses or `getInterfaceAddresses()` for retrieving all assigned interface addresses might be usefull as well for discovery services.

### Network Address Change Listener

The `NetworkAddressChangeListener` is a consumer type OSGi service interface. If listeners want to be notified about network interface address changes, they can implement `NetworkAddressChangeListener` and register as an OSGi service.

Please be aware that not all network interface changes are notified to the listeners, only "useful" network interfaces :--
When a network interface status changes from "up" to "down", it is considered as "removed".
When a "loopback" or "down" interface is added, the listeners are not notified.

## Caching

The framework provides some caching solutions for common scenarios.

### Simple expiring and reloading cache

A common usage case is in a `ThingHandler` to encapsulate one value of an internal state and attach an expire time on that value. A cache action will be called to refresh the value if it is expired. This is what `ExpiringCache` implements. If `handleCommand(ChannelUID channelUID, Command command)` is called with the "RefreshType" command, you just return `cache.getValue()`. 

It is a good practice to return as fast as possible from the `handleCommand(ChannelUID channelUID, Command command)` method to not block callers especially UIs.
Use this type of cache only, if your refresh action is a quick to compute, blocking operation. If you deal with network calls, consider the asynchronously reloading cache implementation instead.

### Expiring and asynchronously reloading cache

If we refreshed a value of the internal state in a `ThingHandler` just recently, we can return it immediately via the usual `updateState(channel, state)` method in response to a "RefreshType" command.
If the state is too old, we need to fetch it first and this may involve network calls, interprocess operations or anything else that will would block for a considerable amout of time.

A common usage case of the `ExpiringCacheAsync` cache type is in a `ThingHandler` to encapsulate one value of an internal state and attach an expire time on that value.


A **handleCommand** implementation with the interesting *RefreshType* could look like this:
```
public void handleCommand(ChannelUID channelUID, Command command) {
    if (command instanceof RefreshType) {
        switch (channelUID.getId()) {
            case CHANNEL_1:
                cache1.getValue(updater).thenAccept(value -> updateState(CHANNEL_1, value));
                break;
            ...
        }
    }
}
```

The interesting part is the `updater`. If the value is not yet expired, the returned CompletableFuture will complete immediately and the given code is executed.
If the value is expired, the updater will be used to request a refreshed value.

An updater can be any class or lambda that implements the funtional interface of `Supplier<CompletableFuture<VALUE_TYPE>>`.

In the following example the method `CompletableFuture<VALUE_TYPE> get()` is accordingly implemented. The example assumes that we deal
with a still very common callback based device refreshing method `doSuperImportantAsyncStuffHereToGetRefreshedValue(listener)`. The listener is the class
itself, which implements `DeviceStateUpdateListener`. We will be called back with a refreshed device state in `asyncCallbackFromDeviceStateRefresh`
and mark the Future as *complete*.

```
class FetchValueFromDevice implements Supplier<CompletableFuture<double>>, DeviceStateUpdateListener {
    CompletableFuture<double> c;
    
    @Override
    CompletableFuture<double> get() {
       if (c != null) {
          c = new CompletableFuture<double>();
          doSuperImportantAsyncStuffHereToGetRefreshedValue( (DeviceStateUpdateListener)this );
       }
       return c;
    }
    
    // Here you process the callback from your device refresh method
    @Override
    void asyncCallbackFromDeviceStateRefresh(double newValue) {
       // Notify the future that we have something
       if (c != null) {
          c.complete(newValue);
          c = null;
       }
    }
}
```
If you deal with a newer implementation with a CompletableFuture support, it is even easier. You would just return your CompletableFuture.
---
layout: documentation
---

{% include base.html %}

# Icon Support

Bundle: `org.eclipse.smarthome.ui.icon`

## Icon Servlet

Eclipse SmartHome comes with a flexible infrastructure for handling icons that are to be used within user interfaces.
This bunde registers a servlet under the url `/icon/`, which can then be easily queried for icons using GET requests of the form `/icon/<category>?state=<state>&format=[png|svg]&iconset=<iconsetid>`, where 
- `category` is one from the [list of channel categories](../concepts/categories.html#channel-categories) or any custom category that might be used within the solution
-`state` (optional) is the string-representation of an item state
- `format` (optional) defines the requested format to be either PNG or SVG 
- `iconset` (optional) specifies an iconset to use

If no icon set is specified in the request, "classic" will be used as a default. This default setting can be configured by the setting:

```
org.eclipse.smarthome.iconset:default=<iconsetId>
```

## Icon Sets

Icon sets can either provide icons in PNG or SVG format or both. All standard channel categories should be covered by the icon set in the supported format.
Icon sets can easily be added as additional bundles. All that has to be done is to register a service, which implements the `IconProvider` interface. Icons are provided as byte streams, so they do not have to be static resources, but can also be dynamically generated at runtime (e.g. for providing specific icons for certain states).
 
---
layout: documentation
---

{% include base.html %}

# Feature Overview

Eclipse SmartHome is a framework for building smart home solutions. With its very flexible architecture, it fosters the modularity provided by OSGi for Java applications.
As such, Eclipse SmartHome consists of a rich set of OSGi bundles that serve different purposes. Not all solutions that build on top of Eclipse SmartHome will require all of those bundles - instead they can choose what parts are interesting for them.

There are the following categories of bundles:

 - `config`: everything that is concerned with general configuration of the system like config files, xml parsing, discovery, etc.	
 - `core`: the main bundles for the logical operation of the system - based on the abstract item and event concepts.
 - `io`: all kinds of optional functionality that have to do with I/O like console commands, audio support or HTTP/REST communication.
 - `model`: support for domain specific languages (DSLs). 
 - `designer`: Eclipse RCP support for DSLs and other configuration files.
 - `ui`: user interface related bundles that provide services that can be used by different UIs, such as charting or icons.

## Runtime Services

### Optional Bundles

 - `org.eclipse.smarthome.core.id`: [Unique instance IDs](core/id.html)
 - `org.eclipse.smarthome.ui.icon`: [Icon support](icons.html)

Besides the very core framework that is mandatory for all solutions, there are many optional features like the support for textual configurations (DSLs), the REST API or the sitemap support.

## Extensions

Being a framework, Eclipse SmartHome defines many extension types that allows building modular solutions with pluggable components (extensions). 

The list of extension types will grow over time and you are invited to discuss useful extension types in [our forum](https://www.eclipse.org/forums/eclipse.smarthome).

Note that many "existing" extension types like rule actions, persistence services, TTS modules, etc. are not covered in this documentation as it is planned to address and heavily refactor them in future - the current version is still from the initial contribution which came from openHAB 1 and thus is tight to textual configuration and not usable in a wider context.

#### Extension Service

Eclipse SmartHome comes with an API that allows implementing a service that manages the installed extensions within a solution. All that needs to be done is to register an OSGi service that implements `org.eclipse.smarthome.core.extension.ExtensionService`. Such a service has to provide a list of available extensions and then can be called in order to install and uninstall them.

What kind of implementation is chosen is completely up to the solution. Suitable mechanisms might be Eclipse p2, Apache Felix FileInstall, Apache Karaf FeatureInstaller, etc. For testing purposes, Eclipse SmartHome comes with a sample implementation in the bundle `org.eclipse.smarthome.core.extension.sample`.

Installation and uninstallation requests are executed by a thread pool named "extensionService". If an implementation does not support concurrent execution of such operations, the thread pool size should be set to 1.

### Bindings

A binding is an extension to the Eclipse SmartHome runtime that integrates an external system like a service, a protocol or a single device. Therefore the main purpose of a binding is to translate events from the Eclipse SmartHome event bus to the external system and vice versa. Learn about the internals of a binding in our [binding tutorial](../development/bindings/how-to.html).

Bindings can optionally include [discovery services](../concepts/discovery.html), which allow the system to automatically find accessible devices and services. Furthermore, they can register devices as [audio sources and audio sinks](../concepts/audio.html), so that microphones and speakers can be made available to the audio and voice support features of the framework.

### User Interfaces

User interfaces normally use the REST API for communication, but if they are not client-side, but served from the runtime, they also have the option to use all local Java services.

Currently, there are 3 available user interfaces in Eclipse SmartHome: the Classic UI, the Basic UI and the Paper UI.

All user interfaces can share icon sets, so that these do not have to be included in every single user interface.
Eclipse SmartHome comes with the following iconsets:

 - `org.eclipse.smarthome.ui.iconset.classic`: [Classic Icon Set](ui/iconset/classic/readme.html)

### Voice Services
 
Voice extensions provide implementations for Text-to-Speech, Speech-to-Text and Human Language Interpreter services.
 
These services are often very solution specific, so there is no one-fits-all implementation in Eclipse SmartHome.
For easy demonstration, there is a TTS service available, which uses the built-in "say" command of MacOS (which obviously only works on Macs, though).
Additionally, there is a basic human language interpreter implementation, which supports simple smart home commands like switching lights and controlling music both in English and German.
 
---
layout: documentation
---

# Internationalization

In this chapter the Eclipse SmartHome support for internationalization is described. 
Translations

All texts can be internationalized by using Java I18N properties files. For each language a specific file with a postfix notation is used. The postfix consists of a language code and an optional region code (country code).

```
Format:     any_<language-code>_<country-code>.properties
Example:    any_de_DE.properties
```

The language code is either two or three lowercase letters that are conform to the ISO 639 standard. The region code (country code) consists of two uppercase letters that are conform to the ISO 3166 standard or to the UN M.49 standard.

The search order for those files is the following:

```
any_<language-code>_<country-code>.properties
any_<language-code>.properties
any.properties
```

You can find detailed information about Java internationalization support and a list of the ISO 639 and ISO 3166 codes at [The Java Tutorials](http://docs.oracle.com/javase/tutorial/i18n/locale/create.html) page. 

The properties files have to be placed in the following directory of the bundle:

```
ESH-INF/i18n
```

Example files:

```
|- ESH-INF
|---- i18n
|------- yahooweather_de.properties
|------- yahooweather_de_DE.properties
|------- yahooweather_fr.properties
```

## Internationalize Binding XML files

In Eclipse SmartHome a binding developer has to provide different XML files. In these XML files label and description texts must be specified. To Internationalize these texts Java I18N properties files must be defined.

For the binding definition and the thing types XML files Eclipse SmartHome defines a standard key scheme, that allows to easily reference the XML nodes. Inside the XML nodes the text must be specified in the default language English. Typically all texts for a binding are put into one file with name of the binding, but they can also be split into multiple files.

### Binding Definition

The following snippet shows the binding XML file of the Yahoo Weather Binding and its language file that localizes the binding name and description for the German language.

XML file (binding.xml):

```xml
<binding:binding id="yahooweather">
    <name>YahooWeather Binding</name>
    <description>The Yahoo Weather Binding requests the Yahoo Weather Service
		to show the current temperature, humidity and pressure.</description>
    <author>Kai Kreuzer</author>
</binding:binding>
```

Language file (yahooweather_de.properties):

```ini
binding.yahooweather.name = Yahoo Wetter Binding
binding.yahooweather.description = Das Yahoo Wetter Binding stellt verschiedene Wetterdaten wie die Temperatur, die Luftfeuchtigkeit und den Luftdruck für konfigurierbare Orte vom yahoo Wetterdienst bereit.
```

So the key for referencing the name of a binding is `binding.<binding-id>.name` and `binding.<binding-id>.description` for the description text. 

### Thing Types

The following snippet shows an excerpt of the thing type definition XML file of the Yahoo Weather Binding and its language file that localizes labels and descriptions for the German language.

XML file (thing-types.xml):

```xml
<thing:thing-descriptions bindingId="yahooweather">
    <thing-type id="weather">
        <label>Weather Information</label>
        <description>Provides various weather data from the Yahoo service</description>
        <channels>
            <channel id="precipitation" typeId="precipitation" />
            <channel id="temperature" typeId="temperature" />
            <channel id="minTemperature" typeId="temperature">
                <label>Min. Temperature</label>
                <description>Minimum temperature in degrees celsius (metric) or fahrenheit (imperial).</description>
            </channel>
        </channels>
        <config-description>
            <parameter name="location" type="text">
                <label>Location</label>
                <description>Location for the weather information. Syntax is WOEID, see https://en.wikipedia.org/wiki/WOEID.
                </description>
                <required>true</required>
            </parameter>
        </config-description>
    </thing-type>
    <channel-type id="precipitation">
        <item-type>String</item-type>
        <label>Precipitation</label>
        <description>Current precipitation (dry, rain, snow).</description>
        <state readOnly="true" pattern="%s">
            <options>
                <option value="dry">dry</option>
                <option value="rain">rain</option>
                <option value="snow">snow</option>
            </options>
        </state>
    </channel-type>
    <channel-type id="temperature">
        <item-type>Number</item-type>
        <label>Temperature</label>
        <description>Current temperature in degrees celsius (metric) or fahrenheit (imperial).</description>
        <state readOnly="true" pattern="%d Value" />
        <config-description>
            <parameter name="unit" type="text" required="true">
                <label>Temperature unit</label>
                <description>Select the temperature unit.</description>
                <options>
                    <option value="C">Degree Celsius</option>
                    <option value="F">Degree Fahrenheit</option>
                </options>
                <default>C</default>
            </parameter>
        </config-description>
    </channel-type>
    <channel-type id="cmd-channel">
        <item-type>String</item-type>
        <label>Device Commands</label>
        <description>Send one of the defined command options to the device.</description>
        <command>
            <options>
                <option value="RESET">Reset</option>
                <option value="CMD_1">Command 1</option>
                <option value="CMD_2">Command 2</option>
            </options>
        </command>
    </channel-type>
</thing:thing-descriptions>

```

Language file (yahooweather_de.properties):

```ini
thing-type.yahooweather.weather.label = Wetterinformation
thing-type.yahooweather.weather.description = Stellt verschiedene Wetterdaten vom Yahoo Wetterdienst bereit.

thing-type.config.yahooweather.weather.location.label = Ort
thing-type.config.yahooweather.weather.location.description = Ort der Wetterinformation. Syntax ist WOEID, siehe https://en.wikipedia.org/wiki/WOEID.

channel-type.yahooweather.precipitation.label = Niederschlag
channel-type.yahooweather.precipitation.description = Aktueller Niederschlag (Trocken, Regen, Schnee).
channel-type.yahooweather.precipitation.state.option.dry = Trocken
channel-type.yahooweather.precipitation.state.option.rain = Regen
channel-type.yahooweather.precipitation.state.option.snow = Schnee

channel-type.yahooweather.temperature.label = Temperatur
channel-type.yahooweather.temperature.description = Aktuelle Temperatur in Grad Celsius (Metrisch) oder Grad Fahrenheit (US).
channel-type.yahooweather.temperature.state.pattern = %d Wert

thing-type.yahooweather.weather.channel.minTemperature.label = Min. Temperatur
thing-type.yahooweather.weather.channel.minTemperature.description = Minimale Temperatur in Grad Celsius (Metrisch) oder Grad Fahrenheit (US).

channel-type.config.yahooweather.temperature.unit.label = Temperatur Einheit
channel-type.config.yahooweather.temperature.unit.description = Auswahl der gewünschten Temperatur Einheit.
channel-type.config.yahooweather.temperature.unit.option.C = Grad Celsius
channel-type.config.yahooweather.temperature.unit.option.F = Grad Fahrenheit

channel-type.yahooweather.cmd-channel.command.option.RESET = Reset Device
channel-type.yahooweather.cmd-channel.command.option.CMD1 = Command one
channel-type.yahooweather.cmd-channel.command.option.CMD2 = Command two
```

So the key for referencing a label of a defined thing type is `thing-type.<binding-id>.<thing-type-id>.label`.
A label of a channel type can be referenced with `channel-type.<binding-id>.<channel-type-id>.label` and a label of a channel definition with `thing-type.<binding-id>.<thing-type-id>.channel.<channel-id>.label`.
And finally the config description parameter key is `thing-type.config.<binding-id>.<thing-type-id>.<parameter-name>.label` or `channel-type.config.<binding-id>.<channel-type-id>.<parameter-name>.label`.

The following snippet shows an excerpt of the thing type definition XML file of the Weather Underground Binding and its language file that localizes labels and descriptions for the French language.

XML file (thing-types.xml):

```xml
<thing:thing-descriptions bindingId="weatherunderground">

    <thing-type id="weather">
        <label>Weather Information</label>
        <description>Provides various weather data from the Weather Underground service</description>

        <channel-groups>
            <channel-group id="current" typeId="current" />
            <channel-group id="forecastTomorrow" typeId="forecast">
                <label>Weather Forecast Tomorrow</label>
                <description>This is the weather forecast for tomorrow</description>
            </channel-group>
            <channel-group id="forecastDay2" typeId="forecast">
                <label>Weather Forecast Day 2</label>
                <description>This is the weather forecast in two days</description>
            </channel-group>
        </channel-groups>
        
        <config-description>
            <parameter name="apikey" type="text" required="true">
                <context>password</context>
                <label>API Key</label>
                <description>API key to access the Weather Underground service</description>
            </parameter>
            <parameter name="location" type="text" required="true">
                <label>Location of Weather Information</label>
                <description>Multiple syntaxes are supported. Please read the binding documentation for more information</description>
            </parameter>
            <parameter name="language" type="text" required="false">
                <label>Language</label>
                <description>Language to be used by the Weather Underground service</description>
                <options>
                    <option value="EN">English</option>
                    <option value="FR">French</option>
                    <option value="DL">German</option>
                </options>
            </parameter>
            <parameter name="refresh" type="integer" min="5" required="false" unit="min">
                <label>Refresh interval</label>
                <description>Specifies the refresh interval in minutes.</description>
                <default>30</default>
            </parameter>
        </config-description>
    </thing-type>

    <channel-group-type id="current">
        <label>Current Weather</label>
        <description>This is the current weather</description>
        <channels>
            <channel id="conditions" typeId="currentConditions" />
            <channel id="temperature" typeId="temperature" />
        </channels>
    </channel-group-type>

    <channel-group-type id="forecast">
        <label>Weather Forecast</label>
        <description>This is the weather forecast</description>
        <channels>
            <channel id="temperature" typeId="temperature">
                <label>Temperature</label>
                <description>Forecasted temperature</description>
            </channel>
            <channel id="maxTemperature" typeId="maxTemperature" />
        </channels>
    </channel-group-type>

    <channel-type id="currentConditions">
        <item-type>String</item-type>
        <label>Current Conditions</label>
        <description>Weather current conditions</description>
        <state readOnly="true" pattern="%s"></state>
    </channel-type>

    <channel-type id="temperature">
        <item-type>Number</item-type>
        <label>Temperature</label>
        <description>Current temperature</description>
        <category>Temperature</category>
        <state readOnly="true" pattern="%.1f" />
        <config-description>
            <parameter name="SourceUnit" type="text" required="true">
                <label>Temperature Source Unit</label>
                <description>Select the temperature unit provided by the Weather Underground service</description>
                <options>
                    <option value="C">Degree Celsius</option>
                    <option value="F">Degree Fahrenheit</option>
                </options>
                <default>C</default>
            </parameter>
        </config-description>
    </channel-type>

    <channel-type id="maxTemperature">
        <item-type>Number</item-type>
        <label>Maximum Temperature</label>
        <description>Maximum temperature</description>
        <category>Temperature</category>
        <state readOnly="true" pattern="%.1f" />
        <config-description>
            <parameter name="SourceUnit" type="text" required="true">
                <label>Maximum Temperature Source Unit</label>
                <description>Select the maximum temperature unit provided by the Weather Underground service</description>
                <options>
                    <option value="C">Degree Celsius</option>
                    <option value="F">Degree Fahrenheit</option>
                </options>
                <default>C</default>
            </parameter>
        </config-description>
    </channel-type>

</thing:thing-descriptions>
```

Language file (weatherunderground_fr.properties):

```ini
# binding
binding.weatherunderground.name = Extension WeatherUnderground
binding.weatherunderground.description = L'extension Weather Underground interroge le service Weather Underground pour récupérer des données météo.

# thing types
thing-type.weatherunderground.weather.label = Informations météo
thing-type.weatherunderground.weather.description = Présente diverses données météo fournies par le service Weather Underground.

# thing type configuration
thing-type.config.weatherunderground.weather.apikey.label = Clé d'accès
thing-type.config.weatherunderground.weather.apikey.description = La clé d'accès au service Weather Underground.
thing-type.config.weatherunderground.weather.location.label = Emplacement des données météo
thing-type.config.weatherunderground.weather.location.description = Plusieurs syntaxes sont possibles. Merci de consulter la documentation de l'extension pour plus d'information.
thing-type.config.weatherunderground.weather.language.label = Langue
thing-type.config.weatherunderground.weather.language.description = La langue à utiliser par le service Weather Underground.
thing-type.config.weatherunderground.weather.language.option.EN = Anglais
thing-type.config.weatherunderground.weather.language.option.FR = Français
thing-type.config.weatherunderground.weather.language.option.DL = Allemand
thing-type.config.weatherunderground.weather.refresh.label = Fréquence de rafraîchissement
thing-type.config.weatherunderground.weather.refresh.description = La fréquence de rafraîchissement des données en minutes.

# channel group types
channel-group-type.weatherunderground.current.label = Météo actuelle
channel-group-type.weatherunderground.current.description = La météo actuelle.
channel-group-type.weatherunderground.forecast.label = Météo prévue
channel-group-type.weatherunderground.forecast.description = La météo prévue.

# channel groups
thing-type.weatherunderground.weather.group.forecastTomorrow.label = Météo de demain
thing-type.weatherunderground.weather.group.forecastTomorrow.description = La météo prévue demain.
thing-type.weatherunderground.weather.group.forecastDay2.label = Météo dans 2 jours
thing-type.weatherunderground.weather.group.forecastDay2.description = La météo prévue dans 2 jours.

# channel types
channel-type.weatherunderground.currentConditions.label = Conditions actuelles
channel-type.weatherunderground.currentConditions.description = Les conditions météo actuelles.
channel-type.weatherunderground.temperature.label = Température
channel-type.weatherunderground.temperature.description = La température actuelle.
channel-type.weatherunderground.maxTemperature.label = Température maximale
channel-type.weatherunderground.maxTemperature.description = La température maximale.

# channels inside a channel group type
channel-group-type.weatherunderground.current.channel.temperature.label = Température
channel-group-type.weatherunderground.current.channel.temperature.description = La température prévue.

# channel type configuration
channel-type.config.weatherunderground.temperature.SourceUnit.label = Unité de température
channel-type.config.weatherunderground.temperature.SourceUnit.description = Choix de l'unité de température fournie par le service Weather Underground pour la température actuelle.
channel-type.config.weatherunderground.temperature.SourceUnit.option.C = Degrés Celsius
channel-type.config.weatherunderground.temperature.SourceUnit.option.F = Degrés Fahrenheit
channel-type.config.weatherunderground.maxTemperature.SourceUnit.label = Unité de température maximale
channel-type.config.weatherunderground.maxTemperature.SourceUnit.description = Choix de l'unité de température fournie par le service Weather Undergroundde pour la température maximale.
channel-type.config.weatherunderground.maxTemperature.SourceUnit.option.C = Degrés Celsius
channel-type.config.weatherunderground.maxTemperature.SourceUnit.option.F = Degrés Fahrenheit

```

So the label of a channel group type can be referenced with `channel-group-type.<binding-id>.<channel-group-type-id>.label` and the label of a channel group definition with `thing-type.<binding-id>.<thing-type-id>.group.<channel-group-id>.label`.
A label of a channel definition inside a channel group type can be translated with `channel-group-type.<binding-id>.<channel-group-type-id>.channel.<channel-id>.label`.

### Using custom Keys

In addition to the default keys the developer can also specify custom keys inside the XML file. But with this approach the XML file cannot longer contain the English texts. So it is mandatory to define a language file for the English language. The syntax for custom keys is `@text/<key>`. The keys are unique across the whole bundle, so a constant can reference any key in all files inside the `ESH-INF/i18n` folder.

The following snippet shows a binding XML that uses custom keys:

XML file (binding.xml):

```xml
<binding:binding id="yahooweather">
    <name>@text/bindingName</name>
    <description>@text/bindingName</description>
    <author>Kai Kreuzer</author>
</binding:binding>
```

Language file (yahooweather_en.properties):

```ini
bindingName = Yahoo Weather Binding

offline.communication-error=The Yahoo Weather API is currently not available.
```

Language file (yahooweather_de.properties):

```ini
bindingName = Yahoo Wetter Binding

offline.communication-error=Die Yahoo Wetter API ist zur Zeit nicht verfügbar.
```

The custom keys are a very good practice to translate bundle dependent error messages.

```java
updateStatus(ThingStatus.OFFLINE, ThingStatusDetail.OFFLINE.COMMUNICATION_ERROR, "@text/offline.communication-error");
```

## I18n Text Provider API

To programmatically resolve texts for certain languages Eclipse SmartHome provides the OSGi service `TranslationProvider`. The service parses every file inside the `ESH-INF/i18n` folder and caches all texts. A localized text can be retrieved via the method `getText(Bundle bundle, String key, String default, Locale locale)` (or via the method `getText(Bundle bundle, String key, String default, Locale locale, Object... arguments)` if additional arguments are to be injected into the localized text), where bundle must be the reference to the bundle, in which the file is stored. The BundleContext from the Activator provides a method to get the bundle.

```java
String text = i18nProvider.getText(bundleContext.getBundle(), "my.key", "DefaultValue", Locale.GERMAN);
```

## Locale Provider

To programmatically fetch the locale used by the Eclipse SmartHome system an OSGi service `LocaleProvider` is offered. The service contains a `getLocale()` method that can be used to choose a configurable locale.

## Getting Thing Types and Binding Definitions in different languages

Thing types can be retrieved through the `ThingTypeRegistry` OSGi service. Every method takes a `Locale` as last argument. If no locale is specified the thing types are returned for the default locale which is determined by using the `LocaleProvider`, or the default text, which is specified in the XML file, if no language file for the default locale exists.

The following snippet shows how to retrieve the list of Thing Types for the German locale:

```java
List<ThingType> thingTypes = thingTypeRegistry.getThingTypes(Locale.GERMAN);
```

If one binding supports the German language and another does not, it might occur that the languages of the returned thing types are mixed.

For Binding Info and ConfigDescription, the localized objects can be retrieved via the `BindingInfoRegistry` and the `ConfigDescriptionRegistry` in the same manner as described for Thing Types.

---
layout: documentation
---

{% include base.html %}

# REST API

## Introduction

The REST API of Eclipse SmartHome serves different purposes. It can be used to integrate with other system as it allows read access to items and item states as well as status updates or the sending of commands for items. Furthermore, it gives access to things, links, sitemaps, etc., so that it is the main interface to be used by remote UIs (e.g. fat clients or HTML5 web applications).

The REST API is complemented by support for server sent events (SSE), so you can subscribe  on change notification for certain resources.

## Configuration Options

By default, the REST API is registered on the HTTP service under `rest`. This configuration can be changed through configuring the property `root` of the service pid `com.eclipsesource.jaxrs.connector` through the Configuration Admin service.

## REST Endpoints

The details about available REST urls, their parameters, etc. can be found [here](../../rest/index.html).

## Server Sent Events (SSE)

In order to receive notice of important events outside of the Eclipse SmartHome framework they are exposed using the Server Sent Events (SSE) standard.

To subscribe to events a developer can listen to `/rest/events`. In general any SSE Consumer API can be used (for example HTML5 EventSource Object) to read from the event stream.

### Events

The framework broadcasts all events on the Eclipse SmartHome event bus also as an SSE event. A complete list of the framework event types can be found in the [Event chapter](events.html).

All events are represented as JSON objects on the stream with the following format:

```json
{
    "topic": "smarthome/inbox/yahooweather:weather:12811438/added",
    "type": "InboxAddedEvent",
    "payload": "{
        "flag": "NEW",
        "label": "Yahoo weather Berlin, Germany",
        "properties": {
            "location": "12811438"
        },
        "thingUID": "yahooweather:weather:12811438"
    }"
}
```

* `topic`: the event topic (see also [Runtime Events](events.html))
* `type`: the event type (see also [Runtime Events](event-type-definition.html))
* `payload`: String, which contains the payload of the Eclipse SmartHome event. For all core events, the payload will be in the JSON format. For example the `smarthome/items/item123/added` event will include the new item that was added and the `smarthome/items/item123/updated` event will include both old and new item.
  
### Filtering

By default when listening to `/rest/events` a developer will receive all events that are currently broadcasted. In order to listen for specific events the `topics` query parameter can be used.

For example while listening to `/services/events?topics=smarthome/items/*` a developer would receive notifications about item events only. The wildcard character (\*) can be used replacing one (or multiple) parts of the topic.

The `topics` query parameter also allows for multiple filters to be specified using a comma (,) for a separator - `?topics=smarthome/items/*, smarthome/things/*`.

### Example

An example of listing events in JavaScript using the HTML5 EventSource object is provided below:

```js
//subscribe for all kind of 'added' and 'inbox' events
var eventSource = new EventSource("/rest/events?topics=smarthome/*/added,smarthome/inbox/*");

eventSource.addEventListener('message', function (eventPayload) {

    var event = JSON.parse(eventPayload.data);
    console.log(event.topic);
    console.log(event.type);
    console.log(event.payload);

    if (event.type === 'InboxAddedEvent') {
        var discoveryResult = JSON.parse(event.payload);
        console.log(discoveryResult.flag);
        console.log(discoveryResult.label);
        console.log(discoveryResult.thingUID);
    }
});
```
---
layout: documentation
---

{% include base.html %}

# Rules

Eclipse SmartHome provides a modular rule engine than can be easily extended.

## Concept


In general this rule engine aims to support rules defined with syntax similar to:

```
ON item_id state changed IF item_id.state == desired_value THEN item_id2.state = desired_value2 
```

Each rule can have some basic information like name, tags, description and three module sections (**triggers, conditions, actions**)


- The **'triggers'** section is the trigger (eventing) part. 


- The **'conditions'** section lists the conditions which act as a filter for the events - actions of the rule will be executed only if the conditions evaluating the event data are satisfied and return 'true'. In case there are multiple conditions in the 'if' section then all of them must be satisfied - logical AND is used 

- The **'actions'** section contains the actions which specify what should be executed when the event is received (and all conditions are met, if any).


One rule can invoke one and the same operation upon receiving each trigger event, or the operation can be dynamic using input parameters from the event itself or from the system objects

The main building blocks of the rules are modules and each rule consists of one or more instances of each of the following modules:

> **trigger** - specifies when to execute the rule, usually it is an event;
> **condition** - acts like a filter depending on the defined condition type and its input and configuration. An example of a condition can be evaluation of trigger outputs or the state of the system / items;
> **action** - specifies the operation of the rule which will be executed if the condition is statisfied. If more than one actions are specified in a rule they will be executed sequentially where the output of the previous action can be used as an input for the next action - like a processor modifying the data of the trigger output (e.g. converting temperature values from Celsius to Fahrenheit).

Each module is created from a template called "module type" and can specify configuration parameters for the template, like e.g. "eventTopic" for the "GenericEventTrigger" or "operator" for the "GenericCompareCondition".
Since there are system module types which are provided by the system, composite module types can be added which are extensions of these system module types and use predefined configurations and/or modified module input/output objects. An example is the module type "ItemStateChangeTrigger" which is based on the GenericEventTrigger but specifies in its configuration that it is triggered only by item's state change events.

A given **Module type** has the following elements:

    uid - unique id
    label - localizable text
    description - localizable text
    configDescriptions - list of meta data for the configuration properties
    input variables - list of meta data for the supported input objects
    output variables - list of meta data for the supported output objects

**configDescriptions** has the following metadata defined for each property:

    name
    type - one of the following "text", "integer", "decimal", "boolean"
    label - localizable text
    description - localizable text
    required - boolean flag indicating if this configuration property can be optional and thus it can be ommited in the rule, by default required is false
    defaultValue - default value for the configuration property when not specified in the rule

**Input property** has the following metadata:

    name
    type - fully qualified name of Java class ("java.lang.Integer")
    label - localizable text
    description - localizable text
    defaultValue - default value for the configuration property when not specified in the rule
    tags - shows how to be considered a given value. For example, as a Temperature


**Output property** has the following metadata:

    name
    type - fully qualified name of Java class ("java.lang.Integer")
    label - localizable text
    description - localizable text
    defaultValue - default value for the configuration property when not specified in the rule
    reference - which means the property value can be specified as a reference to configuration parameter or input parameter
    tags - shows how a given value should be considered (e.g. as a Temperature)

**Supported Types**

The types supported in the **input/output** objects can be any string and the following validation is performed:

- if the input type and the output type are equal as string the connection is valid
- if the input type is "*" and the output type is any the connection is valid
- if the input type and the output type are strings representing full qualified names which can be loaded and the input type is assignable from output type the connection is valid

The types in the **Configuration** object are restricted to the following:

- TEXT - The data type for a UTF8 text value
- INTEGER - The data type for a signed integer value in the range of Integer#MIN_VALUE, Integer#MAX_VALUE
- DECIMAL - The data type for a signed floating point value (IEEE 754) in the range of Float#MIN_VALUE, Float#MAX_VALUE
- BOOLEAN - The data type for a boolean: true or false


## Defining Rules via JSON

**JSON schemas for:**

 * [module types](../development/rules/ModuleTypes_schema.json)
 * [rule templates](../development/rules/Templates_schema.json)
 * [rule instances](../development/rules/Rules_schema.json)

### Sample Rules

 * **Sample rule instance referencing module types:**

```
{
        "uid":"sample.rule1",
        "name":"SampleRule",
        "tags":[
            "sample",
            "rule"
        ],
        "description":"Sample Rule definition.",
        "triggers":[
            {
                "id":"SampleTriggerID",
                "type":"SampleTrigger"
            }
        ],
        "conditions":[
            {
                "id":"SampleConditionID",
                "type":"SampleCondition",
                "configuration":{
                    "operator":"=",
                    "constraint":"dtag"
                },
                "inputs":{
                    "conditionInput":"SampleTriggerID.triggerOutput"
                }
            }
        ],
        "actions":[
            {
                "id":"SampleActionID",
                "type":"SampleAction",
                "configuration":{
                    "message":">>> Hello World!!!"
                }
            }
        ]
}
```

 * **Sample module types:**

```
"triggers":[  
      {  
         "uid":"SampleTrigger",
         "label":"SampleTrigger label",
         "description":"Sample Trigger description.",
         "outputs":[  
            {  
               "name":"triggerOutput",
               "type":"java.lang.String",
               "label":"TriggerOutput label",
               "description":"Text from user input or default message.",
               "reference":"consoleInput",
               "defaultValue":"dtag"
            }
         ]
      },
      {  
         "uid":"CompositeSampleTrigger",
         "label":"CompositeTrigger label",
         "description":"Composite Trigger description.",
         "outputs":[  
            {  
               "name":"compositeTriggerOutput",
               "type":"java.lang.String",
               "label":"compositeTriggerOutput label",
               "description":"Text from user input or default message.",
               "reference":"compositeChildTrigger1.triggerOutput"
            }
         ],
         "children":[  
            {  
               "id":"compositeChildTrigger1",
               "type":"SampleTrigger"
            }
         ]
      }
]
```

```
   "conditions":[  
      {  
         "uid":"SampleCondition",
         "label":"SampleCondition label",
         "description":"Sample Condition description",
         "configDescriptions":[  
            {  
               "name":"operator",
               "type":"TEXT",
               "description":"Valid operators are =,>,<,!=",
               "required":true
            },
            {  
               "name":"constraint",
               "type":"TEXT",
               "description":"Right operand which is compared with the input.",
               "required":true
            }
         ],
         "inputs":[  
            {  
               "name":"conditionInput",
               "type":"java.lang.String",
               "label":"ConditionInput label",
               "description":"Left operand which will be evaluated.",
               "required":true
            }
         ]
      }
   ]
```

```
"actions":[  
      {  
         "uid":"SampleAction",
         "label":"SampleAction label",
         "description":"Sample Action description.",
         "configDescriptions":[  
            {  
               "name":"message",
               "type":"TEXT",
               "label":"message label",
               "description":"Defines the message description.",
               "defaultValue":"Default message",
               "required":false
            }
         ]
      },
      {  
         "uid":"CompositeSampleAction",
         "label":"CompositeAction label",
         "description":"Composite Action description.",
         "configDescriptions":[  
            {  
               "name":"compositeMessage",
               "type":"TEXT",
               "label":"custom message label",
               "description":"Defines the custom message description.",
               "defaultValue":">>> Default Custom Message",
               "required":false
            }
         ],
         "inputs":[  
            {  
               "name":"compositeActionInput",
               "type":"java.lang.String",
               "label":"ActionInput label",
               "description":"Text that will be printed.",
               "required":true
            }
         ],
         "children":[  
            {  
               "id":"SampleAction1",
               "type":"SampleAction",
               "configuration":{  
                  "message":"$compositeMessage"
               }
            },
            {  
               "id":"SampleAction2",
               "type":"SampleAction",
               "configuration":{  
                  "message":"$compositeActionInput"
               }
            }
         ]
      }
]
```


## Working with Rules


There are several ways to add new rules:

  * using **JAVA API** from package: **org.eclipse.smarthome.automation.api**;
  * using **text console commands: smarthome automation**;
  * using **resource bundles** that provide moduletypes, rules and rule templates stored in **.json** files;
  * using **REST API** - see the next chapter bellow.

## REST API
* http://<host:port>/rest/module-types - lists module types.
* http://<host:port>/rest/templates" - lists rule templates. 
* http://<host:port>/rest/rules - lists rule instances.

#### /rest/templates
 - GET /rest/templates - returns all registered rule templates.
 - GET /rest/templates/{templateUID} - returned response includes only the content of the specified template.

#### /rest/module-types
 - GET /rest/module-types - returns all registered module types.
 - optional parameter 'type' with possible values: 'trigger', 'condition' or 'action' - filters the response to include only module definitions of specified type.
 - optional parameter 'tags' - filters the response to include only module types which have specified tags.
 - GET /rest/module-types/{moduleTypeUID} - returned response includes only the content of the specified module type.
  
#### /rest/rules
 - GET /rest/rules - returns all registered rule instances.
 - POST /rest/rules - adds new rule instance to the rule registry.
 - DELETE /rest/rules/{ruleUID} - deletes the specified rule instance.
 - PUT /rest/rules/{ruleUID} - updates the specified rule instance.
 - PUT /rest/rules/{ruleUID}/enable - enable/disable specified rule instance.
 - PUT /rest/rules/{ruleUID}/runnow - executes actions of specified rule instance.
 - GET /rest/rules/{ruleUID}/config - returns the configuration of the specified rule instance.
 - PUT /rest/rules/{ruleUID}/config - updates the configuration of the specified rule instance.
 - GET /rest/rules/{ruleUID}/triggers - returns the triggers defined for the specified rule instance.
 - GET /rest/rules/{ruleUID}/conditions - returns the conditions defined for the specified rule instance.
 - GET /rest/rules/{ruleUID}/actions - returns the actions defined for the specified rule instance.
 - GET /rest/rules/{ruleUID}/{moduleCategory}/{id} - returns module instance with specified id and category {triggers/conditions/actions} of the specified rule. 
 - GET /rest/rules/{ruleUID}/{moduleCategory}/{id}/config - returns the configuration of the specified module instance.
 - GET /rest/rules/{ruleUID}/{moduleCategory}/{id}/config/{param} - returns the value of specified module configuration parameter (media type is text/plain).
 - PUT /rest/rules/{ruleUID}/{moduleCategory}/{id}/config/{param} - updates the value of specified module configuration parameter (media type is text/plain).
 


## JAVA API
`org.eclipse.smarthome.automation.RuleRegistry` - provides main functionality to manage rules in the Rule Engine. It can add rules, get existing ones and remove them from the Rule Engine.

`org.eclipse.smarthome.automation.type.ModuleTypeRegistry` - provides functionality to get module types from the Rule Engine.

`org.eclipse.smarthome.automation.template.TemplateRegistry` - provides functionality to get templates from the Rule Engine.


## Text console commands
`automation listModuleTypes [-st] <filter> ` - lists all Module Types. If filter is present, lists only matching Module Types.

`automation listTemplates [-st] <filter> ` - lists all Templates. If filter is present, lists only matching Templates.

`automation listRules [-st] <filter> `- lists all Rules. If filter is present, lists only matching Rules.

`automation removeModuleTypes [-st] <url> ` - Removes the Module Types, loaded from the given url.

`automation removeTemplates [-st] <url ` - Removes the Templates, loaded from the given url.

`automation removeRule [-st] <uid> ` - Removes the rule, specified by given UID.

`automation removeRules [-st] <filter> `- Removes the rules. If filter is present, removes only matching Rules.

`automation importModuleTypes [-p] <parserType> [-st] <url> ` - Imports Module Types from given url. If parser type missing, "json" parser will be set as default.

`automation importTemplates [-p] <parserType> [-st] <url> ` - Imports Templates from given url. If parser type missing, "json" parser will be set as default.

`automation importRules [-p] <parserType> [-st] <url> ` - Imports Rules from given url. If parser type missing, "json" parser will be set as default.

`automation exportModuleTypes [-p] <parserType> [-st] <file> ` - Exports Module Types in a file. If parser type missing, "json" parser will be set as default.

`automation exportTemplates [-p] <parserType> [-st] <file> ` - Exports Templates in a file. If parser type missing, "json" parser will be set as default.

`automation exportRules [-p] <parserType> [-st] <file> ` - Exports Rules in a file. If parser type missing, "json" parser will be set as default.

`automation enableRule [-st] <uid> <enable> ` - Enables the Rule, specified by given UID. If enable parameter is missing, the result of the command will be visualization of enabled/disabled state of the rule, if its value is "true" or "false", the result of the command will be to set enable/disable on the Rule.

 
## Resource bundles
Bundles that provide rules in json format should have the following folder structure:


`ESH-INF\automation\moduletypes` - folder for .json files with module types;

`ESH-INF\automation\rules` - folder for .json files with rule instances;

`ESH-INF\automation\templates` - folder for .json files with rule templates.


## Rule Templates


Rule templates can simplify the definition of rules with similar behavior by providing additional configuration properties. Then rule instance definition only refers the rule template and provides the values of the configuration properties. The rule template is used only once when the rule is imported in the Rule Engine. After that the reference from the rule instance to the rule template is removed and a given rule may exist even if the rule template is removed or modified - this will not have any impact on the already imported rules.

 * **Sample rule instance referencing rule template:**

```
  {  
    "uid": "sample.rulebytemplate",
    "name": "RuleByTemplate",
    "templateUID": "SampleRuleTemplate",
    "tags": [  
      "rule",
      "template"
    ],
    "configuration": {  
      "condition_operator": "!=",
      "condition_constraint": "template"
    }
  }
```

 * **Sample rule template:**

```
  {  
    "uid":"SampleRuleTemplate",
    "description":"Sample Rule Template",
    "tags":[  
      "sample",
      "rule",
      "template"
    ],
    "configDescriptions":[  
         {
          "name":"condition_operator",              
          "type": "TEXT",
          "description": "Valid operators are =,>,<,!=",
          "required": true
        },
         {
          "name":"condition_constraint",              
          "type": "TEXT",
          "description": "Right operand which is compared with the input.",
          "required": true
        }
    ],
    "triggers": [  
      {  
        "id": "CompositeSampleTriggerTemplateID",
        "type": "CompositeSampleTrigger",
        "label": "Sample Trigger",
        "description": "This is a sample composite trigger"
      }
    ],
    "conditions": [
      {
        "id": "SampleConditionTemplateID",
        "type": "SampleCondition",
        "label": "Sample Condition",
        "description": "This is a sample condition",
        "configuration": {
          "operator": "$condition_operator",
          "constraint": "$condition_constraint"
        },
        "inputs": {
          "conditionInput": "CompositeSampleTriggerTemplateID.compositeTriggerOutput"
        }
      }
    ],
    "actions": [
      {  
        "id": "CompositeActionTemplateID",
        "type": "CompositeSampleAction",
        "label": "Sample Action",
        "description": "This is a sample action",
        "configuration": {
          "compositeMessage": "Hello World!!!"
        },
        "inputs": {  
          "compositeActionInput": "CompositeSampleTriggerTemplateID.compositeTriggerOutput"
        }
      }
    ]
  }
```

The above example uses two rule configuration properties: "condition_operator" and "condition_constraint" that update the configuration of the "SampleCondition".


## System Module Types


### GenericEventTrigger

GenericEventTrigger has 3 configuration paramters: `eventTopic`,` eventSource` and `eventTypes` and one output: 'event'.

      {  
         "uid":"GenericEventTrigger",
         "label":"Basic Event Trigger",
         "description":"Triggers Rules on Events",
         "configDescriptions":[  
            {  
               "name":"eventTopic",
               "type":"TEXT",
               "label":"Topic",
               "description":"This is the topic, the trigger will listen to: >>smarthome/*<<",
               "required":true,
               "defaultValue":"smarthome/*"
            },
            {  
               "name":"eventSource",
               "type":"TEXT",
               "label":"Source",
               "description":"This is the source of the event (eg. item name)",
               "required":true,
               "defaultValue":""
            },
            {  
               "name":"eventTypes",
               "type":"TEXT",
               "label":"Event Type",
               "description":"the event type, the trigger should listen to. Multiple types can be specified comma-separated",
               "required":true,
               "defaultValue":""
            }
         ],
         "outputs":[  
            {  
               "name":"event",
               "type":"org.eclipse.smarthome.core.events.Event",
               "label":"Event",
               "description":"The events which was sent.",
               "reference":"event"
            }
         ]
      }


### GenericCompareCondition

This module type is used to compare a value against a configuration property using an operator like `<, >, =`.
The value to be compared can be specified either as an input or as a configuration property.

    {
      "uid":"GenericCompareCondition",
      "label":"CompareCondition",
      "description":"configurable compare condition",
      "configDescriptions":[
        {
          "name":"inputproperty",
          "label":"Input property",
          "type":"TEXT",
          "description":"property of the input to be compared",
          "required":false
        },
        {
          "name":"right",
          "type":"TEXT",
          "label":"compare with",
          "description":"the value to be compared with the input",
          "required":true
        },
        {
          "name":"operator",
          "type":"TEXT",
          "description":"the compare operator, allowed are <, >, =",
          "required":true,
          "defaultValue":"="
        }
      ],
        "inputs": [
            {
              "name":"input",
              "type": "java.lang.Object",
              "label": "input",
              "description": "The input which will be compared.",
              "required":true
            }
    ]
    }

## Providing new Module Types

The rule engine is pluggable - any OSGi bundle can provide implementation for triggers, actions and condition module types and their corresponding metatype definition in JSON format. 

The extension bundle should register the service ModuleHandlerFactory (`org.eclipse.smarthome.automation.handler.ModuleHandlerFactory`) 
and implement the necessary methods for creation of instances of the supported module handlers:

- `org.eclipse.smarthome.automation.handler.TriggerHandler`
- `org.eclipse.smarthome.automation.handler.ConditionHandler`
- `org.eclipse.smarthome.automation.handler.ActionHandler`


## Composite module types

Another way to extend the supported module types is by defining composite module types as an extension of the system module types. The composite module type wraps one or more instances of a system module type and defines new configuration parameters, inputs and outputs.


      {  
         "uid":"ItemStateChangeTrigger",
         "label":"Item State Trigger",
         "description":"This triggers a rule if an items state changed",
         "configDescriptions":[  
            {  
               "name":"itemName",
               "type":"TEXT",
               "context":"item",
               "label":"item name",
               "description":"the name of the item which's state change should be observed",
               "required":true
            }
         ],
         "children":[  
            {  
               "id":"itemStateChangeTriggerID",
               "type":"GenericEventTrigger",
               "configuration":{  
                  "eventSource":"$itemName",
                  "eventTopic":"smarthome/items/*",
                  "eventTypes":"ItemStateEvent"
               }
            }
         ],
         "outputs":[  
            {  
               "name":"event",
               "type":"org.eclipse.smarthome.core.events.Event",
               "description":"the event of the item state change",
               "label":"event",
               "reference":"itemStateChangeTriggerID.event"
            }
         ]
      }

This example demonstrates a new module type *ItemStateChangeTrigger* which wraps the system module type *GenericEventTrigger* and defines new configuration property `itemName` which is used as the `eventSource` property of the *GenericEventTrigger*, while the other config paramters `eventTopic` and `eventTypes` are fixed.
The composite module type can also have inputs and outputs and can use a reference to map them to inputs and outputs of the nested system module type(s). 

---
layout: documentation
---

{% include base.html %}

# Scenes

In the general context of home automation, a scene is a defined set of states of one or more home devices. An example of
such a scene could be a **night scene**, which turns on all the indoor lights. The notion of scenes is not directly
available in Eclipse SmartHome, but scenes can be created by the means of using rules.

## Concept

In Eclipse SmartHome, a scene is created by defining states for different items inside the action section of a rule. The
triggers and conditions of the rule are left empty. Once the rule is activated, the actions set the state of the items
thereby activating a specific scene.

A scene can only be activated and no deactivation is possible. It can be activated either manually or automatically. To
manually activate a scene, a **runnow** request must be sent to the rest endpoint. To automate the scene activation, a
second rule must be created. The action section of this second rule is responsible for executing the scene with the
`core.RunRuleAction` module type.

The `core.RunRuleAction` module type, used for running the scenes, supports the direct execution of the actions without
requiring to evaluate the conditions. This way all actions are executed even if an action before returns an error.


## Scene creation and activation

A scene can be created by making a POST request to the following endpoint provided by the rule-engine:

`POST /rest/rules`


 * **Sample scene instance created using rule-engine:**

```
{
  "uid": "light.scene1",
  "name": "IndoorLightScene",
  "tags": [
    "night",
    "scene"
  ],
  "description": "A night scene for indoor lights.",
  "triggers": [],
  "conditions": [],
  "actions": [
    {
      "id": "ItemPostCommandActionID1",
      "type": "core.ItemCommandAction",
      "configuration": {
        "itemName": "corridorLightItem",
        "command": "ON"
      }
    },
    {
      "id": "ItemPostCommandActionID2",
      "type": "core.ItemCommandAction",
      "configuration": {
        "itemName": "roomLampItem",
        "command": "ON"
      }
    }
  ]
}
```

The sample scene shown above turns on the `corridorLightItem` and `roomLampItem` by sending the ON command to both of
these items. Notice that this rule contains a tag called **scene**. It is advisable to use such a tag on a rule-scene to
express its purpose.

* **The above scene can be activated by sending a PUT request to the following endpoint:**
 `/rest/rules/sample.scene1/runnow`

* **It can also be activated by defining an action within another rule as shown in the code block below:**

```
{
  "name": "SceneActivationSampleRule",
  "uid": "SceneActivationSampleRule_1",
  "tags": [
    "sample",
    "item",
    "rule"
  ],
  "configuration": {},
  "description": "Sample Rule for activating scenes.",
  "triggers": [
    {
      "id": "ItemStateChangeTriggerID",
      "type": "core.GenericEventTrigger",
      "configuration": {
        "eventSource": "myAstroItem",
        "eventTopic": "smarthome/items/*",
        "eventTypes": "ItemStateEvent"
      }
    }
  ],
  "actions": [
    {
      "id": "enableSceneAction",
      "type": "core.RunRuleAction",
      "configuration": {
        "ruleUIDs": "light.scene1"
      }
    }
  ]
}
```
## REST API
You will need the rule REST endpoints provided by the rule-engine to work with the scenes. The complete list of the REST
operations can be found [here](rules.html#rest-api).
---
layout: documentation
---

{% include base.html %}

# Unique Instance IDs

Bundle: `org.eclipse.smarthome.core.id`

## Description

When communicating with external systems, it is often desirable to have a unique identifier for the instance of Eclipse SmartHome. This optional bundle is a mean to generate such an id, which is automatically persisted. The persistence is done in the configured `userdata` directory as a file called `uuid`. 

The id is provided through a static method and can be retrieved through
```
    String uuid = InstanceUUID.get();
```

If the [REST API](../rest.html) is installed as well, this bundle will additionally register a rest endpoint `uuid` (e.g. `http://localhost:8080/rest/uuid`), which returns the id as a plain string on a GET access.
---
layout: documentation
---

{% include base.html %}

<div class="swagger-section">

<div id="message-bar" class="swagger-ui-wrap" data-sw-translate>&nbsp;</div>
<div id="swagger-ui-container" class="swagger-ui-wrap"></div>
</div>

  <link href='css/screen.css' media='screen' rel='stylesheet' type='text/css'/>
  <link href='css/esh.css' media='screen' rel='stylesheet' type='text/css'/>
  <script src='lib/jquery-1.8.0.min.js' type='text/javascript'></script>
  <script src='lib/jquery.slideto.min.js' type='text/javascript'></script>
  <script src='lib/jquery.wiggle.min.js' type='text/javascript'></script>
  <script src='lib/jquery.ba-bbq.min.js' type='text/javascript'></script>
  <script src='lib/handlebars-2.0.0.js' type='text/javascript'></script>
  <script src='lib/underscore-min.js' type='text/javascript'></script>
  <script src='lib/backbone-min.js' type='text/javascript'></script>
  <script src='swagger-ui.min.js' type='text/javascript'></script>
  <script src='lib/highlight.7.3.pack.js' type='text/javascript'></script>
  <script src='lib/marked.js' type='text/javascript'></script>
  <script src='lib/swagger-oauth.js' type='text/javascript'></script>

  <!-- Some basic translations -->
  <!-- <script src='lang/translator.js' type='text/javascript'></script> -->
  <!-- <script src='lang/ru.js' type='text/javascript'></script> -->
  <!-- <script src='lang/en.js' type='text/javascript'></script> -->

  <script type="text/javascript">
    $(function () {
      url = "https://www.eclipse.org/smarthome/rest/swagger.json";

      // Pre load translate...
      if(window.SwaggerTranslator) {
        window.SwaggerTranslator.translate();
      }
      window.swaggerUi = new SwaggerUi({
        url: url,
        dom_id: "swagger-ui-container",
        supportedSubmitMethods: [],
        onComplete: function(swaggerApi, swaggerUi){

          if(window.SwaggerTranslator) {
            window.SwaggerTranslator.translate();
          }

          $('pre code').each(function(i, e) {
            hljs.highlightBlock(e)
          });

          addApiKeyAuthorization();
        },
        onFailure: function(data) {
          log("Unable to Load SwaggerUI");
        },
        docExpansion: "none",
        apisSorter: "alpha",
        showRequestHeaders: false
      });

      function addApiKeyAuthorization(){
        var key = encodeURIComponent($('#input_apiKey')[0].value);
        if(key && key.trim() != "") {
            var apiKeyAuth = new SwaggerClient.ApiKeyAuthorization("api_key", key, "query");
            window.swaggerUi.api.clientAuthorizations.add("api_key", apiKeyAuth);
            log("added key " + key);
        }
      }

      $('#input_apiKey').change(addApiKeyAuthorization);

      // if you have an apiKey you would like to pre-populate on the page for demonstration purposes...
      /*
        var apiKey = "myApiKeyXXXX123456789";
        $('#input_apiKey').val(apiKey);
      */

      window.swaggerUi.load();

      function log() {
        if ('console' in window) {
          console.log.apply(console, arguments);
        }
      }
  });
  </script>
---
layout: post
title: "Null Annotations"
date:   2017-08-21
image: "2017-08-21-article-template.png"
published: false
---

Everything is better with Null Annotations. Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. <!--more--> 

##### The first paragraph
Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks 

##### Null or not Null is the question
One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. "What's happened to me?" he thought

```
/**
 * Creates a thing based on given thing type uid.
 *
 * @param thingTypeUID
 *            thing type uid (can not be null)
 * @param configuration
 *            (can not be null)
 * @param thingUID
 *            thingUID (can not be null)
 * @return thing (can be null, if thing type is unknown)
 */
protected @Nullable Thing createThing(
        @NonNull ThingTypeUID thingTypeUID, 
        @NonNull Configuration configuration,
        @NonNull ThingUID thingUID) {
    return createThing(thingTypeUID, configuration, thingUID, null);
}
```
It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer.

##### Nullable is okay here
This is a very important image: 
![openHAB logo](http://3.bp.blogspot.com/-ejvDecjGQiA/UZASTVsv0oI/AAAAAAAAF0k/87RVq4PMAzk/s1600/openhab.jpg)
---
layout: post
title: "Smart Home Day @ EclipseCon Europe 2017"
date:   2017-10-31
image: "2017-10-31-smarthomeday.jpg"
published: true
---

Similar to every year since 2006, [EclipseCon Europe](https://www.eclipsecon.org/europe2017/) took place at the end of October in Ludwigsburg, Germany, and it was packed with great talks and content all around the Eclipse universe.

<!--more-->

For the first time, there was also a [Smart Home Day](https://www.eclipsecon.org/europe2017/smarthome) colocated on the Sunday before EclipseCon started. 
The Smart Home Day was hosted by the [openHAB Foundation](https://www.openhabfoundation.org/) with [QIVICON by Deutsche Telekom](https://www.qivicon.com/en/) as a sponsor.

The day was all about [Eclipse SmartHome](https://www.eclipse.org/smarthome/), its solutions and especially its community.
There were twelve great presentations over the day and a huge number of core community members attended the day.
Additionally, live demos and posters about openHAB-related research projects at universities were shown.

The agenda proved to be very attractive: More than a week before the date the event was already fully booked. With more than 90 attendees it was beyond any expectation and the venue had reached its maximum capacity.

{:.center}
<img class="img-responsive" src="https://www.openhabfoundation.org/images/posts/2017-10_shd_overview.jpg" alt="">

##### The Morning

The day started with presentations around Open Source in general, a technical look into the QIVICON platform and the latest updates from the Eclipse SmartHome framework developments. All presentations were recorded (thanks to Markus Storm) and can be viewed by clicking the image (while the talk titles link to the slides):

| [Welcome and Introduction](https://www.openhabfoundation.org/documents/2017-10_Kai_Kreuzer_Welcome.pdf)<br/>Kai Kreuzer, President openHAB Foundation | [![Welcome and Introduction](https://img.youtube.com/vi/h8Jn8k1IDdY/1.jpg)](https://www.youtube.com/watch?v=h8Jn8k1IDdY) |
| [Why Open Source Foundations Matter](https://www.openhabfoundation.org/documents/2017-10_Ian_Skerrett_Why_Open_Source_Foundations.pdf)<br/>Ian Skerrett, VP Marketing Eclipse Foundation | [![Why Open Source Foundations Matter](https://img.youtube.com/vi/gR1Kidk04D8/1.jpg)](https://www.youtube.com/watch?v=gR1Kidk04D8) |
| [How Deutsche Telekom Delivers a Mass Market Product based on Eclipse SmartHome](https://www.openhabfoundation.org/documents/2017-10_Jochen_Hiller_QIVICON.pdf)<br/>Jochen Hiller, Product Owner QIVICON Runtime | [![How Deutsche Telekom Delivers a Mass Market Product based on Eclipse SmartHome](https://img.youtube.com/vi/TVNmorY9Y3M/1.jpg)](https://www.youtube.com/watch?v=TVNmorY9Y3M) |
| [About the Importance of UX in Open Source Projects](https://www.openhabfoundation.org/documents/2017-10_Thomas_Dietrich_UX.pdf)<br/>Thomas Dietrich, openHAB Documentation Lead and openHABian Maintainer | [![About the Importance of UX in Open Source Projects](https://img.youtube.com/vi/EgzARcG3_1I/1.jpg)](https://www.youtube.com/watch?v=EgzARcG3_1I) |
| [Eclipse SmartHome turned Inside Out - Updates from the Core Framework](https://www.openhabfoundation.org/documents/2017-10_Simon_Kaufmann_ESH_Updates.pdf)<br/>Simon Kaufmann, Eclipse SmartHome Committer | [![Eclipse SmartHome turned Inside Out - Updates from the Core Framework](https://img.youtube.com/vi/RoG4L9gATd8/1.jpg)](https://www.youtube.com/watch?v=RoG4L9gATd8) |

##### The Early Afternoon

Right after lunch the day continued with some deeper technical insights - the VS Code Extension was shown as a replacement for the Eclipse SmartHome Designer, people learned about the Z-Wave protocol and how it is integrated in openHAB and the internals of the openHAB Cloud were discussed.

| [Using VS Code as a Powerful Editor for Textual Configurations](https://www.openhabfoundation.org/documents/2017-10_Kuba_Wolanin_Visual_Studio_Code.pdf)<br/>Kuba Wolanin, VS Code Extension Maintainer | [![Using VS Code as a Powerful Editor for Textual Configurations](https://img.youtube.com/vi/3X_5JUf5vY4/1.jpg)](https://www.youtube.com/watch?v=3X_5JUf5vY4) |
| [A Deep Dive into the Z-Wave Binding ](https://www.openhabfoundation.org/documents/2017-10_Chris_Jackson_A_Deep_Dive_into_Z-Wave.pdf)<br/>Chris Jackson, Z-Wave & ZigBee Binding and HABmin Maintainer | [![A Deep Dive into the Z-Wave Binding](https://img.youtube.com/vi/yldzfQjnTtY/1.jpg)](https://www.youtube.com/watch?v=yldzfQjnTtY) |
| openHAB Cloud: From IFTTT, Alexa & Google Home Integration to a Scalable Multi-Cloud Microservices Architecture<br/>Mehmet Arziman, openHAB Cloud Maintainer | [![openHAB Cloud: From IFTTT, Alexa & Google Home Integration to a Scalable Multi-Cloud Microservices Architecture](https://img.youtube.com/vi/AxLZgtlKo5Y/1.jpg)](https://www.youtube.com/watch?v=AxLZgtlKo5Y) |

##### The Late Afternoon

After a coffee break, which was extensively used for networking and discussions, a sequence of short inspirational talks concluded the day.

Besides a brief intro to the oneM2M standard and its prototyped integration with Eclipse SmartHome and a praise of the virtues of code reviews, community members presented what they have realized with Eclipse SmartHome resp. openHAB:

It was extremely impressive with what little latency a local voice recognition can score and how well it works if there is a restricted vocabulary.
The setup of a whole office proved convincingly that openHAB can easily scale to be the brain of whole buildings and not just private homes - and that it is running smoothly since 18 months without a single reboot. And Markus Storm gave a glimpse into some of his personal, more advanced use cases that help him to deal with automatic mowers, robot cleaners, kids and mothers-in-law alike.

| Connecting Domains: Interworking of Eclipse SmartHome with oneM2M<br/>Andreas Kraft, Telekom Innovation Laboratories | [![Connecting Domains: Interworking of Eclipse SmartHome with oneM2M](https://img.youtube.com/vi/xAsNeWRggqo/1.jpg)](https://www.youtube.com/watch?v=xAsNeWRggqo) |
| [About the Why and How of Code Reviews](https://www.openhabfoundation.org/documents/2017-10_Martin_van_Wingerden_Code_reviews.pdf)<br/>Martin van Wingerden, openHAB Add-ons Maintainer | [![About the Why and How of Code Reviews](https://img.youtube.com/vi/IrbdME7gECM/1.jpg)](https://www.youtube.com/watch?v=IrbdME7gECM) |
| Experiences with Offline Voice Interaction in openHAB<br/>Yannick Schaus, HABPanel Maintainer | [![Experiences with Offline Voice Interaction in openHAB ](https://img.youtube.com/vi/E90HCCoaMac/1.jpg)](https://www.youtube.com/watch?v=E90HCCoaMac) |
| [An Enterprise Grade Project with openHAB](https://www.openhabfoundation.org/documents/2017-10_George_Erhan_An_enterprise_grade_project_with_openHAB.pdf)<br/>George Erhan, openHAB Community Member | [![An Enterprise Grade Project with openHAB](https://img.youtube.com/vi/LJiw5INmwmc/1.jpg)](https://www.youtube.com/watch?v=LJiw5INmwmc) |
| [Presence Detection and Other Cool Applications](https://www.openhabfoundation.org/documents/2017-10_.Markus_Storm_Presence_detection_and_some_cool_applications.pdf)<br/>Markus Storm, openHAB Community Member | [![Presence Detection and Other Cool Applications](https://img.youtube.com/vi/AG48Amt1afM/1.jpg)](https://www.youtube.com/watch?v=AG48Amt1afM) |
|||

A big thanks to everyone who has attended the event and also thanks for all the positive feedback about it!
It is tentatively planned to repeat a similar event next year at EclipseCon Europe - so please make sure to save October 21, 2018 in your calendar!

You can find pictures of the Smart Home Day on Google Photos:

{:.center}
<a href="https://photos.app.goo.gl/BuwQveaWomH7lE6E3"><img class="img-responsive" src="https://www.openhabfoundation.org/images/posts/2017-10_googlephotos.jpg" alt=""></a>
---
layout: post
title: "Less NPE's - Eclipse SmartHome now uses Eclipse null annotations!"
date:   2017-11-30
image: "2017-11-30-nullannotations.png"
published: true
---

`NullPointerException`s (aka NPE's) are pretty nasty since they are `RuntimeException`s and thus developers do not immediately notice them while coding in their IDE.
Hence, data-flow analyses where written that show potential accesses to null pointers before they occur at runtime. Eclipse SmartHome (ESH) decided to make use of these analyses and get rid of (some) null pointers.

<!--more-->

Two popular projects that offer such an analysis are the [Checker Framework](https://checkerframework.org) and the [Eclipse JDT compiler](https://wiki.eclipse.org/JDT_Core/Null_Analysis).
In order to obtain better results from these analyses, developers can make use of annotations in the code.
In the current snapshots and in the next release such annotations are supported in the provided Eclipse IDE setup and Maven configuration.
The Eclipse SmartHome project decided to use the implementation offered by the Eclipse JDT compiler.

#### Making JavaDoc comments explicit

Since ESH is a framework that will be integrated into solutions which are build by others, it has provided proper Javadoc documentation on the public interfaces in the past.
In these Javadoc comments the project states that a method will never return `null`, a parameter should never be `null` or is optional and thus may be `null`.
Maintaining these comments by hand is error-prone and they can be easily overseen by developers.
Therefore ESH has decided to provide these comments in a machine readable way so the IDE can support developers in showing them errors or warnings in case they violate them.

As described in the [Coding Guidelines]({{ site.url }}/documentation/development/guidelines.html#a-code-style), classes are annotated with the `@NonNullByDefault` annotation which declares that every field, return value, parameter defined in this class will always have other values than `null`.
If a specific field, return value, or parameter in the class should be allowed to become `null` is is annotated with `@Nullable`.
Basically what these annotations are doing is translating the contract written in the Javadoc comment into something that can automatically be checked by the compiler.

ESH has already started to annotate the core packages so binding developers can benefit from them.

### Real life examples

One simple example is the [ThingHandler:handleCommand(ChannelUID channelUID, Command command)](https://github.com/eclipse/smarthome/blob/master/bundles/core/org.eclipse.smarthome.core.thing/src/main/java/org/eclipse/smarthome/core/thing/binding/ThingHandler.java#L99).
It guarantees to binding developers that both arguments are **not** `null`.
Therefore they can safely implement their logic by going through the IDs via `switch (channelUID.getId())` without the risk of running into a NPE.

{:.center}
![NonNull annotation]({{ site.url }}/img/blog/2017-11-30-nullannotations_handleCommand.png)

For bindings which use bridge things and call [BaseThingHandler:getBridge()](https://github.com/eclipse/smarthome/blob/master/bundles/core/org.eclipse.smarthome.core.thing/src/main/java/org/eclipse/smarthome/core/thing/binding/BaseThingHandler.java#L584) there now is the `@Nullable` annotation in place that reminds developers to do a proper `null` check before using the return value of this method.
Without the `null` check, implementors will get a warning as shown below.

{:.center}
![Nullable annotation with warning]({{ site.url }}/img/blog/2017-11-30-nullannotations_bridgeNullable.png)

After the `null` check has been implemented, the warning is gone:

{:.center}
![Nullable annotation without warning]({{ site.url }}/img/blog/2017-11-30-nullannotations_bridgeNullableCorrected.png)

If developers violate the `null` specifications, the IDE will immediately show an error.
In the example below, the `BaseThingHandler:updateState(String channelID, State state)` method requires both parameters to be non-`null`.
Since in the `else` branch the variable used as a second argument is set to `null`, the IDE infers that `null` is passed as an argument to the method and shows an error.

{:.center}
![Null violation]({{ site.url }}/img/blog/2017-11-30-nullannotations_error.png)

If you are interested to see a fully annotated binding, please have a look at the [Philips Hue binding](https://github.com/eclipse/smarthome/tree/master/extensions/binding/org.eclipse.smarthome.binding.hue).


### Outlook: Third party code

If ESH integrates external libraries and use their return values in the framework code, the compiler cannot decide whether these values are always non-`null` or might become `null` at some point.
This will generate a warning that is currently switched off by the IDE and Maven setup.
In the future, the plan is to support *external annotations* which are files that contain information about the method signatures of external libraries.
The [Last NPE project](http://www.lastnpe.org) has started a crowd-sourcing initative to create these external annotations and ESH is planing to use them.
---
layout: post
title: "Units of Measurement with Eclipse SmartHome"
date:   2018-02-22
image: "2018-02-22-units-of-measurement.png"
published: true
---

A lot of functionality in a smart home setup is based on environmental conditions which until now are measured without an explicit unit. Now Eclipse SmartHome comes with full "Units of Measurement" support to make the unit part of the item state and provide automatic or specific unit conversion. <!--more--> 

##### Overview
A lot of functionality in a smart home setup is based on environmental conditions. Sensors will report temperatures from all sorts of locations, weather data is collected and displayed, or in house luminance is measured to control steady lighting conditions.
All these sensor data is not only measured with a scalar value which represents the current state but has an implicit unit attached to it. Temperatures are usually given in either degree Celsius or degree Fahrenheit. Wind speed will be displayed in either kilometers per hour (km/h) or miles per hour (mph). The measured value might even be given in a device specific unit or value scale.
Up to now these units where not represented in Eclipse SmartHome and the user had to "know" its units and model items and rules accordingly.
In order to unify the different values and units and let the smart home make use of it, Eclipse SmartHome now comes with support for "Units of Measurement" or in short "UoM".

##### Units of Measurement
From the [UoM Wikipedia](https://en.wikipedia.org/wiki/Units_of_measurement) article: "A unit of measurement is a definite magnitude of a quantity, defined and adopted by convention or by law, that is used as a standard for measurement of the same kind of quantity. Any other quantity of that kind can be expressed as a multiple of the unit of measurement."
Units are organised in systems of units and the global standard for units is the [International System of Units (SI)](https://en.wikipedia.org/wiki/International_System_of_Units).
Apart from SI there are other systems in use like the imperial unit system. The same physical quantity can be expressed in different units and mathematical transformations exist to convert between them.
Depending on the users locale or cultural preference a specific unit might fit the users needs. For temperature it is common to use degree Celsius (°C) in most places around the globe but degree Fahrenheit (°F) is used in the United States of America.

##### UoM data with QuantityType
Sensor devices and internet services connected to Eclipse SmartHome as Things provide their scalar values in an implicit unit of measurement. The binding developer knows what exact unit the sensor or service data uses and can pass those values to the framework using the new [`QuantityType`]({{ site.baseurl }}{% link documentation/concepts/units-of-measurement.md %}). QuantityType represents the scalar value with the corresponding unit. It also serves as the main API to convert between different units.
The Yahoo Weather binding makes use of `QuantityType` and publishes state updates in the following form:

```(java)
QuantityType<Temperature> state = new QuantityType<>(tempDouble, SIUnits.CELSIUS);
updateState(temperatureChannelUID, state);
```

For this example the binding developer knows from the Yahoo API description that degree Celsius is used for temperature values. For pressure values the API description states that Hecto Pascal (hPa) is used, so a state update for the pressure channel looks like this:

```(java)
QuantityType<Pressure> state = new QuantityType<>(pressDouble, HECTO(SIUnits.PASCAL));
updateState(pressureChannelUID, state);
```

In the temperature example the state is marked to be a "\<Temperature\>" typed QuantityType. It will only accept units which correspond to the dimension type, like degree Celsius, degree Fahrenheit or kelvin.
In the same way the Thing's Channels and the linked Number items have to be typed to match against each other. Both Channel and Item definition use an extended item type format which passes the expected dimension to a Number item.

The temperature channel definition for Yahoo Weather looks like this:

```(xml)
<channel-type id="temperature">
    <item-type>Number:Temperature</item-type>
    <label>Temperature</label>
    <description>Current temperature</description>
    <category>Temperature</category>
    <state readOnly="true" pattern="%.1f %unit%"/>
</channel-type>
```

A corresponding item definition in the `*.items` DSL is:

```
Number:Temperature Weather_Temperature "Outside Temperature [%.1f %unit%]" { channel="yahooweather:weather:berlin:temperature" }
```

Both definitions use the extended item type `Number:Temperature` which configures the Number item to only accept state updates with units from the dimension "Temperature".
For backward compatibility a Number item without a specified dimension will receive state updates as DecimalType. For this situation the scalar value from the QuantityType is taken without any conversion and passed on to the item. 

##### Conversion
Once a binding provides state updates with QuantityTypes the unit which should be used on the item can be different from the unit selected by the binding.

###### Locale Conversion
The default behavior of the framework is to convert the source value to the unit which is defined to be the default for the current measurement system.
Currently two measurement systems are supported by Eclipse SmartHome: For a system locale which is set to "US" or a system language which is set to "en-LR" (which is Liberia) the imperial system is chosen. The SI system of units is chosen otherwise. 

###### Fixed Measurement System
Apart from the locale based selection the framework may be configured to use a predefined measurement system by configuring the `UnitProvider` component.

###### Item State Conversion
In case the default conversion to the system's measurement system does not fit the current use case, items may define their own target unit. The formatter pattern in the item's state description may use the `%unit%` placeholder to render the default unit (see item definition example above) or just define a fixed unit to which state updates will be converted:

```
Number:Temperature Weather_Temperature "Outside Temperature [%.1f K]" { channel="yahooweather:..." }
```

With this definition the target unit is defined to be kelvin (K) so all state updates to this item will be converted to kelvin.

##### Rendering Units in UIs
The same unit conversion mechanism used by the item's state description can be used in sitemap descriptions. The `label` property of a widget in a sitemap and also the `mapping` property of `Switch` and `Select` widgets support the unit definition in the formatter pattern. 

##### QuantityType commands
Any number item which is defined to use QuantityType states will also accept commands from matching units for its dimension. These commands will be forwarded to the corresponding channel(s).
From Paper UI, Basic UI and Classic UI numerous widgets bound to number items will issue QuantityType commands to these items. 

##### Scripts & Rules
The classic rule engine in Eclipse SmartHome also has full support of the new QuantityType. It can be used in arithmetic calculations and comparison with automatic unit conversion.
The `Weather_Temperature` item from the example above with the fixed unit kelvin can be compared against other QuantityType instances with other units from the Temperature dimension.

The scripts

```
20.0|"°C" > 20|"°F"
```

and 

```
20.0|°C > 20|°F
```

both evaluate to `true` and

```
postUpdate(myTemperature, 20.0|°C)
```

will create a new QuantityType and update the Number item `myTemperature` to 20°C.

Note that a QuantityType in scripts and rules must be written as `<value>|"<unit>"`. Some frequently used units and those which are valid identifiers can also ommit the quotation marks and can conveniently be written as `<value>|<unit>` (e.g. `20|°C`)

##### Coding the UoM
###### Packages
When using units, metric prefixes (like MILLI, CENTI, HECTO, ...) and dimensions please make sure to use the following package imports:
For units and metric prefixes use `org.eclipse.smarthome.core.library.unit` package, for dimensions use the `org.eclipse.smarthome.core.library.dimension` or the official `javax.measure.quantity` package.
###### Classes
Prominent classes are `SIUnits` for units unique to the SI standard measurement system, `ImperialUnits` for units unique to the imperial system and `SmartHomeUnits` which are used in both systems.
The `MetricPrefix` class provides wrapper methods to generate prefixed units.
All interfaces from the dimension packages mentioned above should be used to type the generic `QuantityType` and respective units. 

##### Extend UoM
At the time of releasing the UoM support there are only physical units and the two measurement systems SI and Imperial available. While these will already cover the majority of use cases there might be the need for solutions to extend the available units and measurement systems. The start point for extension is to provide an individual implementation of the `org.eclipse.smarthome.core.i18n.UnitProvider`. This way also device dependent units and conversion of those to physical units may be implemented. 
---
layout: post
title: "Smart Home Day @ EclipseCon Europe 2018"
date:   2018-10-29
image: "2018-10-29_smarthomeday.jpg"
published: true
---

Another year has passed and [EclipseCon Europe 2018](https://www.eclipsecon.org/europe2018/) took place in Ludwigsburg, Germany - and with it, our second edition of a colocated [Smart Home Day](https://www.eclipsecon.org/europe2018/smarthome).<!--more-->

The Smart Home Day was hosted by the [openHAB Foundation](https://www.openhabfoundation.org/) with [Bosch SI](https://www.bosch-si.com), [codecentric](https://www.codecentric.de) and [Deutsche Telekom](https://www.qivicon.com/en/) as sponsors.
<!-- more -->
Just like last year, the day was all about [Eclipse SmartHome](https://www.eclipse.org/smarthome/), its solutions and especially its community.
Not only were there again very interesting talks about the internals of Eclipse SmartHome and some of its new features. The audience also learned about cool projects that have been realised with it. The program concluded with a panel discussion about the pros and cons of different build and IDE approaches for the project - giving good insights into Maven, Tycho and Bnd.

As the community is spread over the whole world and not everyone had the chance to come to Ludwigsburg, the Smart Home Day presentations were professionally recorded this year by the [CCC Video Operations Center](https://c3voc.de/). They did an awesome job and not only provided us high-quality recordings, but also had all of them uploaded and shared [a few minutes after the event was over](https://twitter.com/kaikreuzer/status/1053999503471243264).

<!--{:.center}-->
<img class="img-responsive" src="{{ site.url }}/img/blog/2018-10_shd.jpg" alt="">

#### The Agenda

The day was packed with content from 10am in the morning until 5pm in the afternoon. All videos are available on a [YouTube playlist](https://www.youtube.com/playlist?list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs) as well as on [media.ccc.de](https://media.ccc.de/c/ece-shd18).

| Presentation (link to slides) | Video |
|-|-|
| Welcome and Introduction<br/>_Kai Kreuzer, President openHAB Foundation_ | [![Welcome and Introduction](https://img.youtube.com/vi/t3Z-QB0N-GM/2.jpg)](https://www.youtube.com/watch?v=t3Z-QB0N-GM&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=2&t=0s) |
| Eclipse IoT: State of the Union<br/>_Benjamin Cabé, Eclipse IoT Evangelist Eclipse Foundation_ | [![Eclipse IoT: State of the Union](https://img.youtube.com/vi/PvD8o4ILq4Y/1.jpg)](https://www.youtube.com/watch?v=PvD8o4ILq4Y&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=3&t=0s) |
| [Updates from the Core Framework](https://www.openhabfoundation.org/documents/2018-10_Core_Framework_Updates.pdf)<br/>_Henning Treu, Eclipse SmartHome Committer_ | [![Updates from the Core Framework](https://img.youtube.com/vi/fdhNg-ZTe54/2.jpg)](https://www.youtube.com/watch?v=fdhNg-ZTe54&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=4&t=0s) |
| MQTT Integration for Eclipse SmartHome<br/>_David Graeff, Eclipse SmartHome Contributor_ | [![MQTT Integration for Eclipse SmartHome](https://img.youtube.com/vi/QkD8tJrGV6Q/3.jpg)](https://www.youtube.com/watch?v=QkD8tJrGV6Q&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=12&t=0s) |
| HABot - a Chat Bot for openHAB<br/>_Yannick Schaus, openHAB Maintainer_ | [![HABot - a Chat Bot for openHAB](https://img.youtube.com/vi/y_3U4zcD5i4/2.jpg)](https://www.youtube.com/watch?v=y_3U4zcD5i4&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=6&t=0s) |
| [Building Automation at codecentric Headquarters - A Look Behind the Scenes](https://www.openhabfoundation.org/documents/2018-10_BuildingAutomationAtCodecentric.pdf)<br/>_Christina Zenzes & Anna Backs, codecentric_ | [![Building Automation at codecentric Headquarters - A Look Behind the Scenes](https://img.youtube.com/vi/TjxCG2vED5M/1.jpg)](https://www.youtube.com/watch?v=TjxCG2vED5M&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=5&t=0s) |
| SmartHome Cloud: An Open & Extensible Cloud-Native Plattform for Consumer IoT<br/>_Mehmet Arziman, openHAB Cloud Maintainer_ | [![SmartHome Cloud: An Open & Extensible Cloud-Native Plattform for Consumer IoT](https://img.youtube.com/vi/CtqjrZ0lDBY/2.jpg)](https://www.youtube.com/watch?v=CtqjrZ0lDBY&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=7&t=0s) |
| Smartening a Residential Complex. The 2^5 Application!<br/>_George Erhan, openHAB Community Member_ | [![Smartening a Residential Complex. The 2^5 Application!](https://img.youtube.com/vi/Xct2o_up6L8/1.jpg)](https://www.youtube.com/watch?v=Xct2o_up6L8&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=8&t=0s) |
| The Eclipse Smart Home Automation Engine – From Open Source to Production<br/>_Kai Hackbarth, Evangelist, Bosch SI_ | [![The Eclipse Smart Home Automation Engine – From Open Source to Production](https://img.youtube.com/vi/bBIXWbje17Y/1.jpg)](https://www.youtube.com/watch?v=bBIXWbje17Y&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=9&t=0s) |
| [Eclipse SmartHome & Bndtools](https://www.openhabfoundation.org/documents/2018-10_ESH-Bndtools.pdf)<br/>_Jochen Hiller, Runtime Architect, Deutsche Telekom_ | [![Eclipse SmartHome & Bndtools](https://img.youtube.com/vi/V7ycfWp9cbw/2.jpg)](https://www.youtube.com/watch?v=V7ycfWp9cbw&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=10&t=0s) |
| Eclipse SmartHome & Plain Old Maven<br/>_Lukasz Dywicki, Founder Code-House_ | [![Eclipse SmartHome & Plain Old Maven](https://img.youtube.com/vi/WBxCHxi1pM8/2.jpg)](https://www.youtube.com/watch?v=WBxCHxi1pM8&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=11&t=0s) |
| Panel Discussion - Build Tooling for Eclipse SmartHome<br/>_Candidate 1: Maven - Advocated by Lukasz Dywicki<br/>Candidate 2: Tycho - Advocated by Kai Kreuzer<br/>Candidate 3: Bnd - Advocated by BJ Hargrave<br/>Moderation: Henning Treu_ | [![Panel Discussion - Build Tooling for Eclipse SmartHome](https://img.youtube.com/vi/92szjGgt0SY/3.jpg)](https://www.youtube.com/watch?v=92szjGgt0SY&list=PLEGbpQEn6rvyikXIhZXmuztwgUz7V8Ufs&index=13&t=0s) |

A big thanks to everyone who has attended the event as well as to all the speakers that helped making the day a great success! There was a lot of very positive feedback on the talks and it always makes a very special atmosphere to have so many passionate community members together at one place. While we will try to repeat doing such events in future, everybody should feel encouraged to organise local meet-ups or other types of events around their favorite project - it is absolutely worth the efforts!

You can find pictures of the Smart Home Day on Google Photos:
<!--{:.center}-->
<a href="https://photos.app.goo.gl/Nw3UB1aLJCqBTxg57"><img class="img-responsive" src="{{ site.url }}/img/blog/2018-10_googlephotos.jpg" alt=""></a>
# Astro Binding

The Astro binding is used for calculating 
    * many DateTime and positional values for sun and moon.
    * Radiation levels (direct, diffuse and total) of the sun during the day

## Supported Things

This binding supports two Things: Sun and Moon

## Discovery

If a system location is set, "Local Sun" and a "Local Moon" will be automatically discovered for this location.

If the system location is changed, the background discovery updates the configuration of "Local Sun" and "Local Moon" automatically.

## Binding Configuration

No binding configuration required.

## Thing Configuration

All Things require the parameter `geolocation` (as `<latitude>,<longitude>,[<altitude in m>]`) for which the calculation is done. 
The altitude segment is optional and sharpens results provided by the Radiation group.
Optionally, a refresh `interval` (in seconds) can be defined to also calculate positional data like azimuth and elevation.


## Channels

* **thing** `sun`
    * **group** `rise, set, noon, night, morningNight, astroDawn, nauticDawn, civilDawn, astroDusk, nauticDusk, civilDusk, eveningNight, daylight`
        * **channel** 
            * `start, end` (DateTime)
            * `duration` (Number:Time)
    * **group** `position`
        * **channel** 
            * `azimuth, elevation` (Number:Angle)
            * `shadeLength` (Number)
    * **group** `radiation`
        * **channel** 
            * `direct, diffuse, total` (Number:Intensity)
    * **group** `zodiac`
        * **channel** 
            * `start, end` (DateTime) 
            * `sign` (String), values: `ARIES, TAURUS, GEMINI, CANCER, LEO, VIRGO, LIBRA, SCORPIO, SAGITTARIUS, CAPRICORN, AQUARIUS, PISCES`
    * **group** `season`
        * **channel**: 
            * `spring, summer, autumn, winter` (DateTime)
            * `name` (String), values `SPRING, SUMMER, AUTUMN, WINTER`
    * **group** `eclipse`
        * **channel**: 
            * `total, partial, ring` (DateTime)
    * **group** `phase`
        * **channel** 
            * `name` (String), values: `SUN_RISE, ASTRO_DAWN, NAUTIC_DAWN, CIVIL_DAWN, CIVIL_DUSK, NAUTIC_DUSK, ASTRO_DUSK, SUN_SET, DAYLIGHT, NIGHT`
* **thing** `moon`
    * **group** `rise, set`
        * **channel** 
            * `start, end` (DateTime)
    * **group** `phase`
        * **channel**: 
            * `firstQuarter, thirdQuarter, full, new` (DateTime)
            * `age` (Number:Time)
            * `ageDegree` (Number:Angle)
            * `agePercent, illumination` (Number:Dimensionless)
            * `name` (String), values: `NEW, WAXING_CRESCENT, FIRST_QUARTER, WAXING_GIBBOUS, FULL, WANING_GIBBOUS, THIRD_QUARTER, WANING_CRESCENT`
    * **group** `eclipse`
        * **channel**: 
            * `total, partial` (DateTime)
    * **group** `distance`
        * **channel**: 
            * `date` (DateTime)
            * `distance` (Number:Length)
    * **group** `perigee`
        * **channel**: 
            * `date` (DateTime), 
            * `distance` (Number:Length)
    * **group** `apogee`
        * **channel**: 
            * `date` (DateTime)
            * `distance` (Number:Length)
    * **group** `zodiac`
        * **channel** 
            * `sign` (String), values: `ARIES, TAURUS, GEMINI, CANCER, LEO, VIRGO, LIBRA, SCORPIO, SAGITTARIUS, CAPRICORN, AQUARIUS, PISCES`
    * **group** `position`
        * **channel** 
            * `azimuth, elevation` (Number:Angle)

### Trigger Channels

* **thing** `sun`
    * **group** `rise, set, noon, night, morningNight, astroDawn, nauticDawn, civilDawn, astroDusk, nauticDusk, civilDusk, eveningNight, daylight`
        * **event** `START, END`
    * **group** `eclipse`
        * **event**: `TOTAL, PARTIAL, RING`
* **thing** `moon`
    * **group** `rise`
        * **event** `START`
    * **group** `set`
        * **event** `END`
    * **group** `phase`
        * **event**: `FIRST_QUARTER, THIRD_QUARTER, FULL, NEW`
    * **group** `eclipse`
        * **event**: `TOTAL, PARTIAL`
    * **group** `perigee`
        * **event**: `PERIGEE`
    * **group** `apogee`
        * **event**: `APOGEE`

### Channel config

**Offsets:** For each event group you can optionally configure an `offset` in minutes.
The `offset` must be configured in the channel properties for the corresponding thing.

The minimum allowed offset is -1440 and the maximum allowed offset is 1440.

**Earliest/Latest:** For each trigger channel and `start`, `end` datetime value, you can optionally configure the `earliest` and `latest` time of the day.

e.g `sun#set earliest=18:00, latest=20:00`

sunset is 17:40, but `earliest` is set to 18:00 so the event/datetime value is moved to 18:00.

OR

sunset is 22:10 but `latest` is set to 20:00 so the event/datetime value is moved 20:00.

## Full Example

Things:

```
astro:sun:home  [ geolocation="52.5200066,13.4049540,100", interval=60 ]
astro:moon:home [ geolocation="52.5200066,13.4049540", interval=60 ]
```

or optionally with an event offset

```
astro:sun:home [ geolocation="52.5200066,13.4049540,100", interval=60 ] {
    Channels:
        Type rangeEvent : rise#event [
            offset=-30
        ]
}
astro:moon:home [ geolocation="52.5200066,13.4049540", interval=60 ]
```

or a datetime offset

```
astro:sun:home [ geolocation="52.5200066,13.4049540,100", interval=60 ] {
    Channels:
        Type start : rise#start [
            offset=5
        ]
        Type end : rise#end [
            offset=5
        ]
}
```

or a offset and latest

```
astro:sun:home [ geolocation="52.5200066,13.4049540,100", interval=60 ] {
    Channels:
        Type rangeEvent : rise#event [
            offset=-10,
            latest="08:00"
        ]
}
```

Items:

```
DateTime         Sunrise_Time       "Sunrise [%1$tH:%1$tM]"                   { channel="astro:sun:home:rise#start" }
DateTime         Sunset_Time        "Sunset [%1$tH:%1$tM]"                    { channel="astro:sun:home:set#start" }
Number:Angle     Azimuth            "Azimuth"                                 { channel="astro:sun:home:position#azimuth" }
Number:Angle     Elevation          "Elevation"                               { channel="astro:sun:home:position#elevation" }
String           MoonPhase          "MoonPhase"                               { channel="astro:moon:home:phase#name" }
Number:Length    MoonDistance       "MoonDistance [%.1f %unit%]"              { channel="astro:moon:home:distance#distance" }
Number:Intensity Total_Radiation    "Radiation [%.2f %unit%]"                 { channel="astro:sun:home:radiation#total" }
Number:Intensity Diffuse_Radiation  "Diffuse Radiation [%.2f %unit%]"         { channel="astro:sun:home:radiation#diffuse" }
```

Events:

```
rule "example trigger rule"
when
    Channel 'astro:sun:home:rise#event' triggered START
then
    ...
end
```

## Tips

Do not worry if for example the "astro dawn" is undefined at your location.
The reason might be that you live in a northern country and it is summer, such that the sun is not 18 degrees below the horizon in the morning.
For details see [this Wikipedia article](https://en.wikipedia.org/wiki/Dawn).
The "civil dawn" event might often be the better choice.
# Bluetooth Binding overview
 
The Bluetooth binding is implemented to allow bundles to extend the main Bluetooth bundle (this one) in order to add new Bluetooth adapter as well as device support.
This architecture means that such extension bundles must utilise the binding name `bluetooth`.

A base class structure is defined in the `org.eclipse.smarthome.binding.bluetooth` bundle.
This includes the main classes required to implement Bluetooth:
 
* `BluetoothAdapter`. This interface defines the main functionality required to be implemented by a Bluetooth adapter, including device discovery. Typically, this interface is implemented by a BridgeHandler and then registered as an OSGi service
* `BluetoothDiscoveryParticipant`. An interface to be implemented by services that can identify specific Bluetooth devices.
* `BluetoothDevice`. This implements a Bluetooth device. It manages the notifications of device notifications, Bluetooth service and characteristic management, and provides the main interface to communicate to a Bluetooth device.
* `BluetoothService`. Implements the Bluetooth service. A service holds a number of characteristics.
* `BluetoothCharacteristic`. Implements the Bluetooth characteristic. This is the basic component for communicating data to and from a Bluetooth device.
* `BluetoothDescriptor`. Implements the Bluetooth descriptors for each characteristic.
 
## Implementing a new Bluetooth Adapter bundle
 
Bluetooth adapters are modelled as a bridge in ESH.
The bridge handler provides the link with the Bluetooth hardware (eg a dongle, or system Bluetooth API).
An adapter bundle needs to implement two main classes: the `BridgeHandler` which should implement `BluetoothAdapter` (any be registered as a service), and a `ThingFactory`, which is required to instantiate the handler.
 
The bridge handler must implement any functionality required to interface to the Bluetooth layer.
It is responsible for managing the Bluetooth scanning, device discovery (i.e. the device interrogation to get the list of services and characteristics) and reading and writing of characteristics.
The bridge needs to manage any interaction between the interface with any things it provides – this needs to account for any constraints that a interface may impose such that things do not need to worry about any peculiarities imposed by a specific interface.

Classes such as `BluetoothCharacteristic` or `BluetoothService` may be extended to provide additional functionality to interface to a specific library if needed.
 
## Implementing specific Bluetooth device support
 
A specific Bluetooth thing handler provides the functionality required to interact with a specific Bluetooth device.
The new thing bundle needs to implement three main classes – a `BluetoothDiscoveryParticipant`, a `ThingHandler` and a `ThingFactory`, which is required to instantiate the handler.
 
Two fundamental communications methods can be employed in Bluetooth: beacons and connected mode. A Bluetooth thing handler can implement one or both of these communications
 In practice, a connected mode Thing implementation would normally handle the beacons in order to provide as a minimum the RSSI data.

### Thing Naming

To avoid naming conflicts with different Bluetooth bundles a strict naming policy for things and thing xml files is proposed. 
This should use the bundle name and the thing name, separated with an underscore - e.g. for a Yeelight binding Blue2 thing, the thing type would be `yeelight_blue2`.
 
### Connected Mode Implementation
 
The connected mode `BluetoothThingHandler` needs to handle the following functionality
* Extend the connected bluetooth thing handler. This holds the `adapter` through which all communication is done.
* Call the `adapter.getDevice()` method to get the `BluetoothDevice` class for the requested device. The `getDevice()` method will return a `BluetoothDevice` class even if the device is not currently known.
* Implement the `BluetoothDeviceListener` methods. These provide callbacks for various notifications regarding device updates – e.g. when the connection state of a device changes, when the device discovery is complete, when a read and write completes, and when beacon messages are received.
* The parent class calls the `device.connect()` method to connect to the device. Once the device is connected, the `BluetoothDeviceListener.onConnectionStateChange()` callback will be called.
* The parent class  calls the `device.discoverServices()` method to discover all the BluetoothServices and `BluetoothCharacteristic`s implemented by the device. Once this is complete, the `BluetoothDeviceListener.onServicesDiscovered()` callback will be called.
* Call the `readCharacteristic` or `writeCharacteristic` methods to interact with the device. The `BluetoothDeviceListener.onCharacteristicReadComplete()` and `BluetoothDeviceListener.onCharacteristicWriteComplete()` methods will be called on completion.
* Implement the `BluetoothDeviceListener.onCharacteristicUpdate()` method to process any read responses or unsolicited updates of a characteristic value.
 
### Beacon Mode Implementation
 
The beacon mode thing handler needs to handle the following functionality:

* Extend the beacon Bluetooth thing handler. This holds the `adapter` through which all communication is done.
* Call the `adapter.getDevice()` method to get the `BluetoothDevice` class for the requested device. The `getDevice()` method will return a `BluetoothDevice` class even if the device is not currently known.
* Implement the `BluetoothDeviceListener.onScanRecordReceived()` method to process the beacons. The notification will provide the current receive signal strength (RSSI), the raw beacon data, and various elements of generally useful beacon data is provided separately.

### Generic Bluetooth Device Support

The core Bluetooth binding already includes generic "beacon" and "connected" Bluetooth thing types.
All devices for which no discovery participant defines a specific thing type are added to the inbox as a beacon device.
The corresponding handler implementation (`BeaconBluetoothHandler`) uses Beacon mode and merely defines a channel for RSSI for such devices.

The "connected" thing type can be used by manually defining a thing.
The corresponding handler implementation (`ConnectedBluetoothHandler`) uses Connected mode and thus immediately connects to the device and reads its services.
Common services are added as channels (t.b.d.).
# Bluetooth Binding

This binding provides support for generic Bluetooth devices.

It has the following extensions:

<!--list-subs-->

## Bridges

In order to function, this binding requires a Bluetoooth adapter to be present, which handles the wireless communication.
As there is no standard in Bluetooth for such dongles resp. chips, different adapters require a different implementation.
This is why the Bluetooth binding itself does not come with any bridge handlers for such adapters itself, but instead is extensible by additional bundles which can implement support for a specific adapter. 

For Linux, there exists a special bundle which provides a Bluetooth bridge that talks to BlueZ.
This should be the best choice for any Linux-based single board computers like e.g. the Raspberry Pi.

## Supported Things

Two thing types are supported by this binding:

| Thing Type ID | Description                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------|
| beacon        | A Bluetooth device that is not connected, but only broadcasts annoucements.                             |
| connected     | A Bluetooth device that allows a direct connection and which provides specific services when connected. |


## Discovery

Discovery is performed through the Bluetooth bridge.
Normally, any broadcasting Bluetooth device can be uniquely identified and thus a bridge can create an inbox result for it.
As this might lead to a huge list of devices, bridges usually also offer a way to deactivate this behavior.

## Thing Configuration

Both thing types only require a single configuration parameter `address`, which corresponds to the Bluetooth address of the device (in format "XX:XX:XX:XX:XX:XX").

## Channels

Every Bluetooth thing has the following channel:

| Channel ID | Item Type | Description                                                                                         |
|------------|-----------|-----------------------------------------------------------------------------------------------------|
| rssi       | Number    | The "Received Signal Strength Indicator", the [RSSI](https://blog.bluetooth.com/proximity-and-rssi) |

`connected` Things are dynamically queried for their services and if they support certain standard GATT characteristics, the appropriate channels are automatically added as well:

| Channel ID    | Item Type | Description                                                     |
|---------------|-----------|-----------------------------------------------------------------|
| battery_level | Number    | The device's battery level in percent                           |


## Full Example

demo.things (assuming you have a Bluetooth bridge with the ID `bluetooth:bluez:hci0`):

```
bluetooth:beacon:hci0:b1  "BLE Beacon" (bluetooth:bluez:hci0) [ address="68:64:4C:14:FC:C4" ]
```

demo.items:

```
Number Beacon_RSSI "My Beacon [%.0f]" { channel="bluetooth:beacon:hci0:b1:rssi" }
```

demo.sitemap:

```
sitemap demo label="Main Menu"
{
    Frame {
        Text item=Beacon_RSSI
    }
}
```

See also the following extensions for further examples:

<!--list-subs-->
# Bluetooth BlueGiga Adapter

This extension supports Bluetooth access via a BlueGiga (BLED112) USB dongle.

## Supported Things

It defines the following bridge type:

| Bridge Type ID | Description                                                               |
|----------------|---------------------------------------------------------------------------|
| bluegiga       | A BlueGiga USB dongle using a BLED112 chip                                |


## Discovery

The adapter cannot be discovered; its serial port must be manually configured.

## Bridge Configuration

The bluegiga bridge requires the configuration parameter `port`, which corresponds to the serial port the dongle is connected to.
Additionally, the parameter `discovery` can be set to true/false. When set to true, any Bluetooth device of which broadcasts are received is added to the Inbox.

## Example

This is how an BlueGiga adapter can be configured textually in a *.things file:

```
Bridge bluetooth:bluegiga:1 [ port="/dev/ttyS0", discovery=false ]
```
/**
 * Copyright (c) 2014,2019 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0
 *
 * SPDX-License-Identifier: EPL-2.0
 */
package org.eclipse.smarthome.binding.bluetooth.bluegiga.internal.command.system;

import org.eclipse.smarthome.binding.bluetooth.bluegiga.internal.BlueGigaResponse;

/**
 * Class to implement the BlueGiga command <b>noLicenseKeyEvent</b>.
 * <p>
 * This error is produced when no valid license key found form the Smart hardware. When there is
 * no Bluetooth valid license key the Bluetooth radio will not be operational. A new license key
 * can be requested from the Bluegiga Technical Support.
 * <p>
 * This class provides methods for processing BlueGiga API commands.
 * <p>
 * Note that this code is autogenerated. Manual changes may be overwritten.
 *
 * @author Chris Jackson - Initial contribution of Java code generator
 */
public class BlueGigaNoLicenseKeyEvent extends BlueGigaResponse {
    public static int COMMAND_CLASS = 0x00;
    public static int COMMAND_METHOD = 0x05;

    /**
     * Event constructor
     */
    public BlueGigaNoLicenseKeyEvent(int[] inputBuffer) {
        // Super creates deserializer and reads header fields
        super(inputBuffer);

        event = (inputBuffer[0] & 0x80) != 0;

        // Deserialize the fields
    }


    @Override
    public String toString() {
        return "BlueGigaNoLicenseKeyEvent []";
    }
}
# Bluetooth BlueZ Adapter

This extension supports Bluetooth access via BlueZ on Linux (ARMv6hf).

Please note that at least BlueZ 5.43 is required, while 5.48 or above are [not (yet) supported](https://github.com/intel-iot-devkit/tinyb/issues/131) either.

Also note that the OS user needs to be a member of the "bluetooth" group of Linux in order to have the rights to access the BlueZ stack.

## Supported Things

It defines the following bridge type:

| Bridge Type ID | Description                                                               |
|----------------|---------------------------------------------------------------------------|
| bluez          | A Bluetooth adapter that is supported by BlueZ                            |


## Discovery

If BlueZ is enabled and can be accessed, all available adapters are automatically discovered.

## Bridge Configuration

The bluez bridge requires the configuration parameter `address`, which corresponds to the Bluetooth address of the adapter (in format "XX:XX:XX:XX:XX:XX").
Additionally, the parameter `discovery` can be set to true/false.When set to true, any Bluetooth device of which broadcasts are received is added to the Inbox.

## Example

This is how an BlueZ adapter can be configured textually in a *.things file:

```
Bridge bluetooth:bluez:hci0 [ address="12:34:56:78:90:AB", discovery=false ]
```
# Blukii

This extension adds support for [Blukii](http://www.blukii.com/) Sensor Beacons. 

## Supported Things

Only a single thing type is added by this extension:

| Thing Type ID | Description                                     |
|---------------|-------------------------------------------------|
| blukii_beacon | A Blukii Sensor Beacon                          |

## Discovery

As any other Bluetooth device, Blukii Beacons are discovered automatically by the corresponding bridge. 

## Thing Configuration

There is only a single configuration parameter `address`, which corresponds to the Bluetooth address of the device (in format "XX:XX:XX:XX:XX:XX").

## Channels

A Blukii Smart Beacon has the following channels:

| Channel ID    | Item Type              | Description                        |
|---------------|------------------------|------------------------------------|
| temperature   | Number:Temperature     | The measured temperature           |
| humidity      | Number:Dimensionless   | The measured humidity              |
| pressure      | Number:Pressure        | The measured air pressure          |
| luminance     | Number:Illuminance     | The measured brightness            |
| tiltx         | Number:Angle           | The tilt (x-axis)                  |
| titly         | Number:Angle           | The tilt (y-axis)                  |
| tiltz         | Number:Angle           | The tilt (z-axis)                  |

## Example

demo.things:

```
bluetooth:blukii:hci0:beacon  "Blukii Sensor Beacon" (bluetooth:bluez:hci0) [ address="12:34:56:78:9A:BC" ]
```

demo.items:

```
Number:Temperature      temperature "Room Temperature [%.1f %unit%]" { channel="bluetooth:blukii:hci0:beacon:temperature" }
Number:Dimensionless    humidity    "Humidity [%.0f %unit%]"         { channel="bluetooth:blukii:hci0:beacon:humidity" }
Number:Pressure         pressure    "Air Pressure [%.0f %unit%]"     { channel="bluetooth:blukii:hci0:beacon:pressure" }
Number:Illuminance      luminance   "Luminance [%.0f %unit%]"        { channel="bluetooth:blukii:hci0:beacon:luminance" }
Number:Angle            tiltX       "Tilt (X-Axis) [%.0f %unit%]"    { channel="bluetooth:blukii:hci0:beacon:tiltx" }
Number:Angle            tiltY       "Tilt (Y-Axis) [%.0f %unit%]"    { channel="bluetooth:blukii:hci0:beacon:tilty" }
Number:Angle            tiltZ       "Tilt (Z-Axis) [%.0f %unit%]"    { channel="bluetooth:blukii:hci0:beacon:tiltz" }
```# Bose SoundTouch Binding

This binding supports the Bose SoundTouch multiroom system.

## Supported Things
 
The following Bose devices are supported:

| Name                                  | Thing Type                  |
|---------------------------------------|-----------------------------|
| Bose SoundTouch 10                    | 10                          |
| Bose SoundTouch 20                    | 20                          |
| Bose SoundTouch 30                    | 30                          |
| Bose SoundTouch 300                   | 300                         |
| Bose Wave SoundTouch Music System IV  | waveSoundTouchMusicSystemIV |
| Bose SoundTouch Wireless Link Adapter | wirelessLinkAdapter         |
| Bose SoundTouch SA-5 Amplifier        | sa5Amplifier                |
| Any other Bose SoundTouch device      | device                      |
 
## Discovery
 
Speakers are automatically discovered using mDNS in the local network.
 
## Binding Configuration
 
The binding has no configuration options, all configuration is done at Thing level.
 
## Thing Configuration
 
All thing types have the same configuration parameters:

| Parameter Name      | Type   | Required | Description                                                  |
|---------------------|--------|----------|--------------------------------------------------------------|
| host                | String | Yes      | The host name or IP address of the device                    |
| macAddress          | String | Yes      | The MAC address of the used interface (format "123456789ABC")|
| appKey              | String |  No      | An authorization key used to identify the client application |

The required properties are set when using discovery. For manual configuration, these values can be found in the Bose smartphone app (Settings -> About -> Device Name).
Note that the device might have two MAC addresses, one for ethernet and one for Wifi.

The authorization key is used to identify the client application when using the Notification API. It must be requested from the developer portal.
 
## Channels

All devices share the same set of channels, while some of them might not be available on all devices.

| Channel ID                | Item Type | Description                                                  |
|---------------------------|-----------|--------------------------------------------------------------|
| keyCode                   | String    | Simulates pushing a remote control button                    |
| mute                      | Switch    | Mutes the sound                                              |
| notificationsound         | String    | Play a notification sound by a given URI                     |                              
| nowPlayingAlbum           | String    | Current playing album name                                   |
| nowPlayingArtist          | String    | Current playing artist name                                  |
| nowPlayingArtwork         | Image     | Artwork for the current playing song                         |
| nowPlayingDescription     | String    | Description to current playing song                          |
| nowPlayingGenre           | String    | Genre of current playing song                                |
| nowPlayingItemName        | String    | Visible description shown in display                         |
| nowPlayingStationLocation | String    | Location of current playing radio station                    |
| nowPlayingStationName     | String    | Name of current playing radio station                        |
| nowPlayingTrack           | String    | Track currently playing                                      |
| operationMode             | String    | Current Operation Mode                                       |
| playerControl             | Player    | Control the Player                                           |
| power                     | Switch    | SoundTouch power state                                       |
| preset                    | Number    | 1-6 Preset of Soundtouch, >7 Binding Presets                 |
| rateEnabled               | Switch    | Current source allows rating                                 |
| saveAsPreset              | Number    | A selected presetable item is saved as preset with number >6 |
| skipEnabled               | Switch    | Current source allows skipping to next track                 |
| skipPreviousEnabled       | Switch    | Current source allows scrolling through tracks               |
| volume                    | Dimmer    | Set or get the volume                                        |
| bass                      | Number    | Bass (-9 minimum, 0 maximum)                                 |
 

The *notificationsound* channel has the following optional configuration parameters:

 - notificationVolume - Desired volume level while playing the notification, it must be between 10 and 70 (inclusive). A value outside this range will result in an error and not play the notification.
 - notificationService - The service providing the notification
 - notificationReason - The reason for the notification
 - notificationMessage - Further details about the notification
 
The texts for the notification service, reason and message appear on the device display (when available) and the SoundTouch application screen.
Upon completion of the notification, the speaker volume returns to its original value. If not present, the notification will play at the existing volume level.
 
## Full Example

Things:

```
bosesoundtouch:device:demo @ "Living"  [ host="192.168.1.2", macAddress="123456789ABC" ]
```

Items:

```
Switch  Bose1_Power                      "Power: [%s]"          <switch>      { channel="bosesoundtouch:device:demo:power" }
Dimmer  Bose1_Volume                     "Volume: [%d %%]"      <volume>      { channel="bosesoundtouch:device:demo:volume" }
Number  Bose1_Bass                       "Bass: [%d %%]"        <volume>      { channel="bosesoundtouch:device:demo:bass" }
Switch  Bose1_Mute                       "Mute: [%s]"           <volume_mute> { channel="bosesoundtouch:device:demo:mute" }
String  Bose1_OperationMode              "OperationMode: [%s]"  <text>        { channel="bosesoundtouch:device:demo:operationMode" }
String  Bose1_PlayerControl              "Player Control: [%s]" <text>        { channel="bosesoundtouch:device:demo:playerControl" }
Number  Bose1_Preset                     "Preset: [%d]"         <text>        { channel="bosesoundtouch:device:demo:preset" }
Number  Bose1_SaveAsPreset               "Save as Preset: [%d]" <text>        { channel="bosesoundtouch:device:demo:saveAsPreset" }
String  Bose1_KeyCode                    "Key Code: [%s]"       <text>        { channel="bosesoundtouch:device:demo:keyCode" }
Switch  Bose1_RateEnabled                "Rate: [%s]"           <switch>      { channel="bosesoundtouch:device:demo:rateEnabled" }
Switch  Bose1_SkipEnabled                "Skip: [%s]"           <switch>      { channel="bosesoundtouch:device:demo:skipEnabled" }
Switch  Bose1_SkipPreviousEnabled        "SkipPrevious: [%s]"   <switch>      { channel="bosesoundtouch:device:demo:skipPreviousEnabled" }
String  Bose1_nowPlayingAlbum            "Album: [%s]"          <text>        { channel="bosesoundtouch:device:demo:nowPlayingAlbum" }
String  Bose1_nowPlayingArtist           "Artist: [%s]"         <text>        { channel="bosesoundtouch:device:demo:nowPlayingArtist" }
Image   Bose1_nowPlayingArtwork          "Artwork"              <text>        { channel="bosesoundtouch:device:demo:nowPlayingArtwork" }
String  Bose1_nowPlayingDescription      "Description: [%s]"    <text>        { channel="bosesoundtouch:device:demo:nowPlayingDescription" }
String  Bose1_nowPlayingGenre            "Genre: [%s]"          <text>        { channel="bosesoundtouch:device:demo:nowPlayingGenre" }
String  Bose1_nowPlayingItemName         "Playing: [%s]"        <text>        { channel="bosesoundtouch:device:demo:nowPlayingItemName" }
String  Bose1_nowPlayingStationLocation  "Radio Location: [%s]" <text>        { channel="bosesoundtouch:device:demo:nowPlayingStationLocation" }
String  Bose1_nowPlayingStationName      "Radio Name: [%s]"     <text>        { channel="bosesoundtouch:device:demo:nowPlayingStationName" }
String  Bose1_nowPlayingTrack            "Track: [%s]"          <text>        { channel="bosesoundtouch:device:demo:nowPlayingTrack" }
```

Sitemap:

```
sitemap demo label="Bose Test Items"
{
	Frame label="Bose 1" {
        Switch item=Bose1_Power
		Slider item=Bose1_Volume
		Text item=Bose1_Bass
		Switch item=Bose1_Mute
		Text item=Bose1_OperationMode
		Text item=Bose1_PlayerControl
		Text item=Bose1_Preset
		Text item=Bose1_SaveAsPreset
		Text item=Bose1_KeyCode
		Text item=Bose1_nowPlayingAlbum
		Text item=Bose1_nowPlayingArtist
		Text item=Bose1_nowPlayingArtwork
		Text item=Bose1_nowPlayingDescription
		Text item=Bose1_nowPlayingGenre
		Text item=Bose1_nowPlayingItemName
		Text item=Bose1_nowPlayingStationLocation
		Text item=Bose1_nowPlayingTrack
	}
}
```
# digitalSTROM Binding

  This binding integrates the [digitalSTROM-System](http://www.digitalstrom.de/).
The integration happens through the digitalSTROM-Server, which acts as a gateway to connect the digitalSTROM-Devices.
The digitalSTROM-Server communicates through the digitalSTROM-Meters with the digitalSTROM-Devices, which are directly connected to the power-line.

**Note:** All was tested with digitalSTROM-Server firmware version 1.9.3 to 1.10.3.

![various_digitalSTROM_clamps](doc/DS-Clamps.jpg)

## Supported Things

### digitalSTROM-Server

The digitalSTROM-Server is required for accessing any other digitalSTROM-Devices. It acts like a *"bridge"*.

### digitalSTROM-Devices

At this point almost all available **GE**, **SW**, **GR** and **BL** digitalSTROM-Devices with a set output-mode, unequal *disabled*, are supported by this binding. Furthermore sensor devices like the **dS-iSens200** and **SW-devices** with binary-inputs are supported.
Last but not least the **circuit** (dS-Meter) is supported, too. They will provide the power consumption and electric meter as channels.

For that there are identically named thing types. Only the *GR* type has a channel (shade), which cannot be changed. The other types add their channels dynamically affected by the set color-group and output-mode. They also automatically change or add the channels, if the color-group or output-mode has changed through the dSS-web-configuration or the configured sensor priorities of the thing has changed.

- The following table shows all tested digitalSTROM-Devices with their output-modes.

| HW-Type | Output-Mode    | Tested color group  |
|-----------------|------------------------|--------------|
| GE-KL200 | switched | yellow  |
| GE-KM200 | switched, dimmed | yellow |
| GE-TKM210 | switched, dimmed | yellow |
| GE-SDM200 | switched, dimmed | yellow |
| GE-UMV200 | 1-10V dimmed | yellow |
| GR-KL200 | standard output-mode | grey |    
| GR-KL210 | standard output-mode| grey |
| GR-KL220 | standard output-mode | grey |
| SW-KL200 | switch, powersave, wipe | black, yellow |
| SW-UMR200 | single switched, combined switch, combined 2 stage switch, combined 3 stage switch | yellow , black |
| SW-ZWS200 | switch, powersave, wipe | black, yellow |
| BL-KM200 | switch, pwm | blue |

- Binary-inputs were tested with SW-UMR200.
- Sensor channels were tested with dS-iSens200 and power sensor with all other supported devices, which are listed in the table above.

### digitalSTROM-Scenes

Furthermore the digitalSTROM-Scene concept is part of the digitalSTROM-Binding.
These scenes are implemented as virtual things.
The different scene thing types are listed in the following table.

| Thing-Type-ID | Label    | Description |
|-----------------|------------------------|--------------|
| appScene  | Apartment-Scene | Represents a digitalSTROM Apartment-Scene.  |
| zoneScene  | Zone-Scene | Represents a digitalSTROM Zone-Scene.  |
| groupScene  | Group-Scene | Represents a digitalSTROM Group-Scene.  |
| namedScene  | Named-Scene | Represents a digitalSTROM Scene, which has a user-defined name.  |
 
### digitalSTROM-Zone-Temperature-Control

Last but not least, the digitalSTROM-Zone-Temperature-Control is also supported, if a zone-temerature-control is configured, as thing-type **zone_temperature_control**.
The difference between the digitalSTROM-heating-control-app is, that there are no operation-modes, like *comfort* or *eco*. You can directly set the target temperature, in case *pid-control* is configured, otherwise you can set the value in percent of heating valves at the zone. 
The needed channels will be added automatically, as it is also the case for the devices. 

## Discovery

The digitalSTROM-Server is discovered by mDNS or *dss.local.* at the local network.
Once the server is added as a thing, you have to set a user name and password or insert a valid application-token to authenticate with the server.
If the binding is authorized, it automatically reads all supported devices, the dS-Meters and temperature controlled configured zones, that are set up on the digitalSTROM-System, and puts them into the *inbox*.
 
digitalSTROM-Scenes can be discovered, too.
The background scene-discovery is deactivated by default to not flood the inbox.
Otherwise it will discover so many scenes, that it can be difficult to find the searched devices.
 
Discoverable scenes are all user named scenes, group scenes that are reachable by local push-buttons, zone scenes and apartment scenes.
The discovery also will discover all called scenes, if they aren't automatically discovered yet.
Temperature control scenes, like *eco* will be ignored, so they cannot be discovered. 

If you only want to discover one of the thing types, you can start a discovery scan on the thing type you want to have discovered.
You can use the command line command, e.g.: ``smarthome:discovery start digitalstrom:namedScene`` to start the scan.
Which thing types this binding supports, please have a look at **Supported Things**. 

## Thing Configuration and Properties

### digitalSTROM-Server

The digitalSTROM-Server thing has the following configuration parameter groups: *Connection configuration*, *Server information* and *General configurations*.

#### Connection configuration

If the digitalSTROM-Server isn’t found automatically, e.g. because the server isn’t placed at the local network or the mDNS-service is deactivated, you have to insert the network address or URL and the authentication data manually through the graphical user interface or type it into the \*.thing with textual configuration.
If you use your user name and password for authentication and there is already a token for this application, it will be automatically retrieved from the digitalSTROM-Server, otherwise a new application-token will be generated. 

| Parameter Label | Parameter ID | Description  | Required | Advanced 
|--------------|------------|--------------------------------|----------------- |------------- |
| Network address | dSSAddress | Network address of the digitalSTROM-Server.| true | false |
| User name | userName | Name of a registered user to authenticate to the digitalSTROM-Server.| user name and password or Application-Token | false |
| Password | password | Password of a registered user to authenticate to the digitalSTROM-Server. | user name and password or Application-Token | false |
| Application-Token | applicationToken | The Application-Token to authenticate to the digitalSTROM-Server. | user name and password or Application-Token| false |

#### Server information
 
The parameter group *Server information* only includes informative parameters, which have no special functionality.


| Parameter Label | Parameter ID | Description  | Required | Advanced 
|-----------------|-------------|--------------------------|---------- |------------- |
| dSID | dSID | The unique identifier of a digitalSTROM-server. | false| false | 

#### General configuration:

Here you can set general binding configuration parameters, which are shown in following table: 

| Parameter Label | Parameter ID| Description  | Required | Advanced | default 
|-----------------|------------------|-----------------------------------------|---------------- |------------- | ----------------- |
| Sensor update interval | sensorDataUpdateInterval | Sets the seconds after the digitalSTROM-Device sensor data will be updated. If the priority is higher than 'never'. | false | false | 60 |
| Total power update interval | totalPowerUpdateInterval | Sets the interval in seconds, after the digitalSTROM total power consumption and total electric meter sensor data will be updated. | false | false | 30 |
| Days to be slaked trash bin devices | defaultTrashBinDeleateTime| Sets the days after the temporary saved digitalSTROM-Device configuration from not reachable digitalSTROM-Devices get permanently deleted. | false | false | 7 |
| Wait time sensor reading | sensorWaitTime| Waiting time between the evaluation of the sensor values and the reading of the scenes in seconds. **ATTENTION:** digitalSTROM rule 8 and 9 require a waiting period of 1 minute. Values less than 60 seconds could affect the digitalSTROM system. | false | true | 60 | 

At the thing file, a manual configuration looks e.g. like

```
Bridge digitalstrom:dssBridge:dssBridge1 [ dSSAddress="dss.local.",  userName="dssadmin", password="dssadmin", sensorDataUpdateInterval=180]
```

#### Properties

In addition to the configuration the digitalSTROM-Server has the following properties.

| Property-Name | Description |
| ------------- | ----------- |
| serverCert    | The SSL-Certificate of the digitalSTROM-Server. |
| dS-Installation-Name | The digitalSTROM-System installation name. |
| version | The digitalSTROM-Server-Application version. |
| distroVersion | The digitalSTROM-Server firmware version. |
| Hardware | The digitalSTROM-Server hardware identifier. |
| Revision | The digitalSTROM-Server hardware revision number. |
| Serial | The digitalSTROM-Server hardware serial number. |
| Ethernet | The digitalSTROM-Server IEEE mac address. |
| MachineID | The digitalSTROM-Server unique id. |
| Kernel | The digitalSTROM-Server linux kernel release string. | 

### digitalSTROM-Devices

The digitalSTROM-Device things have the following configuration parameter groups *Device information* and *Sensor setup*.
   
#### Device information

Each digitalSTROM-Device needs the device ID named dSID as configuration parameter.
The device ID is printed as serial number at the digitalSTROM-Device and can also be found within the web-interface of the digitalSTROM-Server.
The following table shows the parameter: 

| Parameter Label | Parameter ID| Description  | Required | Advanced 
|-----------------|------------------------|--------------|----------------- |------------- |
| ID | dSID| The unique identifier of a digitalSTORM-device. | true | false |

#### Sensor setup

The GE, BL and SW digitalSTROM-Devices usually have sensors to capture power consumption data.
So these devices have the following parameters to read them out.  

| Parameter Label | Parameter ID| Description  | Required | Advanced | Default |
|-----------------|--------------------|-----------------------------|----------------- |------------- | -----------|
| Active power refresh priority | activePowerRefreshPriority | Sets the refresh priority for the active power sensor value. Can be never, low priority, medium priority or high priority. | false | false | never |
| Electric meter refresh priority | electricMeterRefreshPriority | Sets the refresh priority for the electric meter sensor value. Can be never, low priority, medium priority or high priority. | false | false | never |
| Output current refresh priority | outputCurrentRefreshPriority | Sets the refresh priority for the output current sensor value. Can be never, low priority, medium priority or high priority. | false | false | never |

#### Properties

Furthermore a supported digitalSTROM-Device has some informative properties.
The following table shows all informative properties: 

| Property-Name | Description |
| ------------- | ------------------------------------- |
|dSUID | The unique identifier of a digitalSTORM-device with virtual devices. | 
| deviceName | he name of a digitalSTROM-Device. | 
| meterDSID | Identifier of the meter to which the device is connected. |   
| hwInfo | The hardware type from this digitalSTROM-Device. |   
| zoneID |The digitalSTROM-Device is part of this zone. |   
| groups | The digitalSTROM-Device is part of this user-defined or functional groups. |    
| output mode | The current digitalSTROM-Device output mode e.g. 22 = dimmable. |    
| funcColorGroup | The current digitalSTROM-Device functional color group e.g. yellow = light. | 

The device scene configurations will also be persisted in the properties. There are in the format:

| Property-Name | Description |
| ------------- | ------------------------------------- |
| scene[sceneID] | {Scene: [sceneID], dontcare: [don't care flag], localPrio: [local prio flag], specialMode: [special mode flag]}(0..1), {sceneValue: [scene value], sceneAngle: [scene angle]}(0..1) | 

### digitalSTROM-Meter

A digitalSTROM-Meter needs, like the digitalSTROM-Devices, only the unique digitalSTROM device ID named dSID as configuration parameter, which has the same parameters, so please have a look at the point *Device information*. 

#### Properties

In contrast to the digitalSTROM-Device there are other informal properties. The following table shows the available properties:

| Property-Name | Description |
| ------------- | ------------------------------------- |
| hwName | The hardware name of the digitalSTROM-Meter |
| swVersion | The software version of the digitalSTROM-Meter |
| apiVersion | The api version of the digitalSTROM-Meter |
| dspSwVersion | The dsp software version of the digitalSTROM-Meter |
| dSUID | The dSUID of the digitalSTROM-Meter |
| deviceName | The user defined name of the digitalSTROM-Meter |
| armSwVersion | The arm software version of the digitalSTROM-Meter |
| hwVersion | The hardware version of the digitalSTROM-Meter |

### digitalSTROM-Zone-Temperature-Control

The thing type of a digitalSTROM-Zone-Temperature-Control is **zone_temperature_control**. 
As configuration only the zone ID or the zone name, to identify the controlled zone, is needed.

| Parameter Label | Parameter ID| Description  | Required | Advanced | 
|-----------------|------------------------|----------------------------------|----------------- |------------- |
| Zone ID or name | zoneID | The zone id or zone name of the temperature controlled zone.  | true | false | 

#### Properties

| Property-Name | Description |
| ------------- | ------------------------------------- |
| controlMode | The currently configured control mode. |
| controlDSUID | The dSID of the meter or service that runs the control algorithm. |
| controlState | The currently configured control state. |

### digitalSTROM-Scenes

The digitalSTROM-Scenes can be defined with following parameters.  

| Parameter Label | Parameter ID| Description  | Required | Advanced | 
|-----------------|------------------------|----------------------------------|----------------- |------------- |
| Zone ID or name | zoneID | The zone ID or zone name of the called scene. 0 or empty is broadcast to all. | false | false | 
| Group ID or name | groupID | The group ID or group name of the called scene. 0 or empty is broadcast to all. | false | false | 
| Scene ID or name | sceneID |The call scene ID or scene name, e.g. preset 1 for scene ID 5. Callable scenes are from 0 to 126. | false | false | 

The Scene-Thing-Type *Named-Scene* and *Group-Scene* have all parameters.
The *Apartment-Scene* only has the parameters *Scene name* and *Scene ID* an the *Zone-Scene* has all parameters without *Group ID or name*. 


### Textual configuration examples

Usually the discovery works reliable, so that a manual configuration is not needed.

However, at the thing file, a manual configuration looks e.g. like 

#### digitalSTROM-Devices

```
Thing digitalstrom:GE:GE-KM200 (digitalstrom:dssBridge:myDssBridge) [ dSID="3504175fe0000000000043d4",  activePowerRefreshPriority="low", electricMeterRefreshPriority=“medium", outputCurrentRefreshPriority="high"]
Thing digitalstrom:GR:GR-KL200 (digitalstrom:dssBridge:myDssBridge) [ dSID="3504175fe0000000000043d5"]
```

#### digitalSTROM-Meters

```
Thing digitalstrom:circuit:circuit (digitalstrom:dssBridge:myDssBridge) [ dSID="3504175fe0000000000043d5"]
```

#### digitalSTROM-Zone-Temperature-Control

```
Thing digitalstrom:zone_temperature_control:zone_temperature_control3 (digitalstrom:dssBridge:myDssBridge)  [ zoneID="3"]
```

#### digitalSTROM-Group-Scene

```
Thing digitalstrom:groupScene:preset1 (digitalstrom:dssBridge:myDssBridge) [ zoneID="3", groupID="1", sceneID="5"]
```

## Channels

All devices support some of the following channels:  

### Output-Channels

digitalSTROM-Devices with an activated output mode.

| Channel Type ID | Item Type    | Description  | supported device type |
|-------|---------|------------------------------------|----------------- |
| light_dimmer | Dimmer | The *light_dimm* channel allows to dimm a light device.  | GE, SW | 
| light_switch | Switch | The *light_switch* channel allows to turn a light device on or off. | GE, SW | 
| light_2_stage | String| The *light_2_stage* channel allows to turn both light devices on or off or switch only 1 of the both light device on or off. | SW-UMR200 | 
| light_3_stage | String | The *light_3_stage* channel allows to turn both light devices on or off or switch both light devices separated from each other on or off. | SW-UMR200 | 
| shade | Rollershutter | The *shade* channel allows to control shade device e.g. a roller shutter or awnings. | GR |
| shade_angle | Dimmer | The *shade_angle* channel allows to control the relative slat position in percent of blinds. | GR | 
| general_dimmer | Dimmer | The *general_dimmer* channel allows to control the power of a device e.g. a ceiling fan. | SW | 
| general_switch | Switch | The *general_switch* channel allows to turn a device on or off e.g. a HIFI-System. | SW | 
| general_2_stage  | String | The *general_2_stage* channel allows to turn both relais of the device on or off or switch only 1 of the both relais on or off. | SW-UMR200 | 
| general_3_stage  | String | The *general_3_stage* channel allows to turn both relais of the device on or off or switch both relais of the device separated from each other on or off. | SW-UMR200 | 
| heating_switch | Switch | The *heating_switch* channel allows to turn a heating device on or off. | BL |
| heating_dimmer | Dimmer | The *heating_switch* channel allows to control the value in percent of heating valve. | BL |

digitalSTROM-Zone-Temperature-Controlled

| Channel Type ID | Item Type    | Description  | 
|-------|---------|------------------------------------|
| heating_temperature_controled | Number | The *heating_temperature_controled* channel allows to set a target temperature of a zone. |
| heating_dimmer | Dimmer | The *heating_switch* channel allows to control the value in percent of heating valve. | 

### Sensor-Channels

digitalSTROM-Devices which have sensors data.

| Channel Type ID | Item Type    | Description  | supported device type |
|-------|---------|------------------------------------|----------------- |
| active_power | Number | This channel indicates the current active power in watt (W) of the device." | GE, SW, BL | 
| output_current | Number | This channel indicates the current output current in milliamper (mA) of the device." | GE, SW, BL | 
| electric_meter | Number | This channel indicates the current electric meter value in killowatts hours (kWh) of the device. | GE, SW, BL | 
| temperature_indoors | Number |  This channel indicates the current temperature indoors in Celsius (°C) of the device. | dS-iSens200 |
| temperature_outdoors | Number |  This channel indicates the current temperature outdoors in Celsius (°C) of the device. | --- |
| brightness_indoors | Number |  This channel indicates the current brightness indoors in Lux (Lx) of the device. | --- |
| brightness_outdoors | Number |  This channel indicates the current brightness outdoors in Lux (Lx) of the device. | --- |
| relative_humidity_indoors | Number |  This channel indicates the current relative humidity indoors in percent of the device. | dS-iSens200 |
| relative_humidity_outdoors | Number |  This channel indicates the current relative humidity outdoors in percent of the device. | --- |
| air_pressure | Number |  This channel indicates the current relative humidity outdoors in hectopscal (hPa bzw. mbar) of the device. | --- |
| wind_speed | Number |  This channel indicates the current wind speed in m/s of the device. | --- |
| wind_direction | Number |  This channel indicates the current wind direction in degree of the device. | --- |
| precipitation | Number |  This channel indicates the current precipitation in milliliter per square meter of the device. | --- |
| carbon_dioxide | Number |  This channel indicates the current carbon dioxide in parts per million of the device. | --- |
| sound_pressure_level | Number |  This channel indicates the current carbon dioxide in Dezibel (dB) of the device. | --- |
| room_temperation_set_point | Number |  This channel indicates the current room temperation set point in Celsius (°C) of the device. | --- |
| room_temperation_control_variable | Number |  This channel indicates the current room temperation control variable in Celsius (°C) of the device. | --- |

*If no supported device type is at the table, digitalSTROM currently does not offer a device, which support this type of sensor. 

### Binary-Input-Channels

digitalSTROM-Devices which are able to set a binary-input sensor like SW-UMR200 or SW-AKM200.

| Channel Type ID | Item Type    | Description  | supported device type |
|-------|---------|------------------------------------|----------------- |
| binary_input_presence | Switch |  Will be activated, if a presence is detected.  | SW |
| binary_input_brightness | Switch |  Will be activated, if the brightness is higher than a setted value. | SW |
| binary_input_presence_in_darkness | Switch |  Will be activated, if a presence is detected. Sensor has a integrated twilight sensor.  | SW |
| binary_input_twilight | Switch |  Will be activated by twilight.  | SW |
| binary_input_motion | Switch |  Will be activated, if a motion is detected. | SW |
| binary_input_motion_in_darkness | Switch |  Will be activated, if a motion is detected. Sensor has a integrated twilight sensor. | SW |
| binary_input_smoke | Switch |  Will be activated, if smoke is detected. | SW |
| binary_input_wind_strenght_above_limit | Switch |   Will be activated, if wind strength is above a user adjusted limit. | SW |
| binary_input_rain | Switch |  Will be activated, if rain is detected. | SW |
| binary_input_sun_radiation | Switch |  Will be activated, if the sun light is above threshold. | SW |
| binary_input_temperation_below_limit | Switch |  Will be activated, if the temperature is below a limit. | SW |
| binary_input_battery_status_is_low | Switch |  Will be activated, if the battery status is low. | SW |
| binary_input_window_is_open | Switch |  Will be activated, if a window is open. | SW |
| binary_input_door_is_open | Switch |  Will be activated, if a door is open. | SW |
| binary_input_window_is_tilted | Switch |  Will be activated, if a window is tilted. | SW |
| binary_input_garage_door_is_open | Switch |  Will be activated, if a garage door is open. | SW |
| binary_input_sun_protection | Switch |  Will be activated, if the sun light is too heavy. | SW |
| binary_input_frost | Switch |  Will be activated by frost. | SW |
| binary_input_heating_operation_on_off | Switch |  Will be activated, if heating operation is on, otherwise it will be deactivated. | SW |
| binary_input_change_over_heating_cooling | Switch |  Will be activated, if heating is activated, otherwise cooling is activated. | SW |

### Metering-Channels

The digitalSTROM-Meters 

| Channel Type ID | Item Type    | Description  | supported device type |
|-------|---------|------------------------------------|----------------- |
| consumption_Wh | Number | The *consumption_Wh* channel indicates the current power consumption in watt (W)  of the  circuit. | circuit | 
| energy_Wh | Number | The *energy_Wh* channel indicates the current electric meter value in killowatt hours of the circuit. | circuit  |

The digitalSTROM-Server 

| Channel Type ID | Item Type    | Description  | supported device type |
|-------|---------|------------------------------------|----------------- |
| total_consumption_Wh | Number | The *total_consumption_Wh* channel indicates the current consumption power in watt (W)  of all connected circuits to the digitalSTROM-System. | dssBridge | 
| total_energy_Wh | Number | The *total_energy_Wh* channel indicates the current electric meter value in killowatt hours of all connected circuits to the digitalSTROM-System. | dssBridge  | 

### Scenes

| Channel Type ID | Item Type    | Description  | supported device type |
|-------|---------|------------------------------------|----------------- |
| scene | Switch | The scene channel allows to call or undo a scene from digitalSTROM. | all scene-types | 

**Notes: **

*Generally:*

* The digitalSTROM-Server only informs the binding about scene-commands. So if you set the output value of devices e.g. through  the dSS-App, the binding will not be informed about the changes and you have to send a "refresh-command" to update the channel.
* If you press a physical switch at your digitalSTROM-installation and the called scene-value is not red out yet, it can take a bit time to read it out and change the state of the channel.
It the scene-value is red out, the state will change immediately.
See also *General-Informations/digitalSTROM-Scenes*.   

*Channels with accepted command type increase and decrease:*

  * digitalSTROM will only evaluate increase and decrease commands, if a scene was called before which turn the device on. 
   
*Blinds:*

 * Increase, decrease and up, down commands of the shade channel changes the angle in digitalSTROM, too. If you want to set only the position, you have to set the value directly.
 * To protect the slats digitalSTROM changes the position by setting the angle, too, if the position is very high or low. So if you want to see the correct position, you have to send a refresh or stop command, if the blind is ready. 

## Full Example

### demo.things:

```
Bridge digitalstrom:dssBridge:dSS [ dSSAddress="urlOfMyDss",  userName="dssadmin", password="mySecretPassword", sensorDataUpdateInterval=180] {
  GE GE-KM-200 [ dSID="3504175fe000000000010db9",  activePowerRefreshPriority="low", electricMeterRefreshPriority="medium", outputCurrentRefreshPriority="high"] 
  SW SW-ZWS-200 [ dSID="3504175fe0000000000651c0"] 
  SW SW-UMR-200 [ dSID="302ed89f43f00ec0000a1034"] 
  dSiSens200 dS-iSens200 [ dSID="302ed89f43f026800003543d"] 
  zoneTemperatureControl zoneTemperatureControl [ zoneID="livingroom"]     
  GR GR-KL220 [ dSID="3504175fe0000000000651c1" ] 
  namedScene Scene1 [ zoneID="5", groupID="1", sceneID="5"] 
  circuit circuit1 [ dSID="3504175fe0000010000004e4" ]    
  GR GR-KL200 [ dSID="3504175fe0000000000651c1" ]
}
```

### demo.items:

```
//dSS
Number TotalActivePower { channel="digitalstrom:dssBridge:dSS:total_consumption_wh" }
Number TotalElectricMeter { channel="digitalstrom:dssBridge:dSS:total_energy_wh" }

//circuit (circuit1)
Number TotalActivePowerDsm { channel="digitalstrom:circuit:dSS:circuit1:energy_wh" }
Number TotalElectricMeterDsm { channel="digitalstrom:circuit:dSS:circuit1:consumption_wh" }

//Light (KM-200)
Dimmer Brightness { channel="digitalstrom:GE:dSS:GE-KM-200:light_dimmer" }
Number ActivePower { channel="digitalstrom:GE:dSS:GE-KM-200:active_power" }
Number OutputCurrent { channel="digitalstrom:GE:dSS:GE-KM-200:output_current" }
Number ElectricMeter { channel="digitalstrom:GE:dSS:GE-KM-200:electric_meter" }

//Device
Switch DeviceSwitch { channel="digitalstrom:SW:dSS:SW-ZWS-200:general_switch" }

//Rollershutter (GR-KL200)
Rollershutter Shutter { channel="digitalstrom:GR:GR-KL200:shade" }

//Blind (GR-KL220)
Rollershutter BlindPosition { channel="digitalstrom:GR:GR-KL210:shade" }
Dimmer BlindAngle { channel="digitalstrom:GR:GR-KL210:shade_angle" }

//Scene (Scene1)
Switch Scene { channel="digitalstrom:namedScene:dSS:Scene1:scene" }

//binary input device (SW-UMR-200)
Switch SensorSwitch { channel="digitalstrom:SW:dSS:SW-UMR-200:binary_input_change_over_heating_cooling" }

//indoor climate (dSiSens200)
Number TempIndoor { channel="digitalstrom:dSiSens200:dSS:dS-iSens200:temperature_indoors" }
Number HumidityIndoor { channel="digitalstrom:dSiSens200:dSS:dS-iSens200:relative_humidity_indoors" }

//target temperature (zoneTemperatureControl)
Number Temperature { channel="digitalstrom:zoneTemperatureControl:dSS:zoneTemperatureControl:heating_temperature_controlled" }
```

### demo.sitemap:

```
sitemap demo label="Main Menu"
{
  Frame label="System" {
   Frame label="digitalSTROM-Server"{
      Text item=TotalActivePower 
      Text item=TotalElectricMeter 
    }
  
   Frame label="digitalSTROM-Meter"{
      Text item=TotalActivePowerDsm
      Text item=TotalElectricMeterDsm
    }
  }
  
  Frame label="Climate" {
   Frame label="heating/cooling"{
      Switch item=SensorSwitch 
    }
    
   Frame label="iSens200"{
      Text item=TempIndoor
      Text item=HumidityIndoor
    }
    
   Frame label="Target temperature"{
      Slider item=Temperature
      Text item=Temperature
    }
  }
  
  Frame label="Shade"{
   Frame label="Rollerschutter"{
      Slider item=Shade 
      Text item=Shade
    }
    
   Frame label="Blind"{
      Slider item=BlindPosition 
      Slider item=BlindAngle
    }
  }
  
  Frame label="Scenes"{
    Frame label="TV scene"{
      Switch item=Scene 
    }
  }
  
  Frame label="HiFi" {
    Frame label="TV light"{
      Slider item=Brightness 
      Switch item=Brightness
      Text item=ActivePower 
      Text item=OutputCurrent 
      Text item=ElectricMeter 
    }
    
   Frame label="TV"{
      Switch item=DeviceSwitch
    }  
  }
}
```

## General-Informations

### digitalSTROM-Scenes

The device scene configuration will be saved persistently to the thing properties, if the thing is not textual configured (because textual configured things will not be persisted), to update the device state faster. 
For that each scene configuration of each device has to be read out first, because of the digitalSTROM-rule 9 that requires a waiting period of one minute, that take some time so that at the first start a scene call can be take some time to read it out and update the device state. 
To read it out faster only the discovered or called scenes will be read out. 
 
**Note:**
Because the digitalSTROM-Server can't inform the binding about save scene events at this time, the persistently saved scene configurations can't be updated.
The current troubleshooting to read out the new scene configuration after a save scene action at the digitalSTROM-Server is the following:

1. delete the thing to delete the persistently saved scene configuration
2. restart the server to delete the temporary saved scene configuration 
3. add the thing again to read out the scene configuration again.   

### Initial state of digitalSTROM-Scenes and devices

To get the device and scene state after a server start or restart, the binding uses the last called group scenes of digitalSTROM.
Because of that there are two things to be observed:

1. If a device status has changed through a device scene or a directly set output value, the status is maybe not correct.
2. If the last called group scene was not read out yet, it can takes some time until the status will be updated. 

### Textual configuration notice

If you configure your system with textual configuration files, like *\*.thing*, there is one things you have to  consider.

* The feature of the persisting of scene-configurations, to get the scene-configurations after a restart faster (see *digitalSTROM-Scenes* above), will not support  textural configured things, because the properties cannot be persist in this case. 

### Rule specific notice

If you want to create a rule, which uses things of the digitalSTROM-Binding, there are also two things you have to consider.

1. If the rule contains several digitalSTROM-Devices, which can be summarized in a digitalSTROM-Scene, e.g. some lights in a zone, please use a equivalent supported scene. That will significantly reduce the communication to the digitalSTROM-Server, increases performance and does not bypass the digitalSTROM state-machine.
2. If you implement your own temperature control algorithm for a zone/room, e.g. because you want to use other temperature sensors, and call more than one digitalSTROM-BL-KM200, please use the *zone_temperature_control* for valve value control. The *zone_temperature_control* for valve value control will call all digitalSTROM-BL-KM200 with one command and increases the performance. To get the needed channel at the *zone_temperature_control* you have to choose a control mode unequal to *pid-controlled* for the affected zone at the digitalSTROM-heating-control-app. 
# DMX Binding

The DMX binding integrates DMX devices. There are different output devices supported as well as Dimmers and Chasers. 

Each output device (bridges) is representing exactly one universe, each thing is bound to a bridge. 
At least one bridge and one thing is needed for the binding to work properly. 

## Supported Things

### Bridges

Two DMX over Ethernet devices are supported as DMX output:  ArtNet and sACN/E1.31. 
The ArtNet bridge can only be operated in unicast mode (broadcast mode is not supported as the specification recommends using it if more than 40 nodes are connected, which is unlikely in the case of a smarthome). 
The sACN bridge supports both, unicast and multicast. 

Additionally Lib485 devices are supported via the Lib485 bridge.

### Things

The most generic thing is a dimmer. 
A dimmer can contain one or more DMX channels. 
It can be bound to Switch and Dimmer items. 
If more than one DMX channel is defined, the item will be updated according to the state of the first DMX channel. 
There are two other things similar to the dimmer thing. 
One is the color thing, it can be bound to Switch, Dimmer or Color Items and is best used for RGB lamps. 
The second one is the tunable white thing, it allows to control the color temperature of lamps with seperate DMX channels for cool white and warm white.

The last supported thing is a chaser. 
It can contain one or more DMX channels and binds to Switch items only. 
If the thing receives an ON command all running fades in all channels are either suspended (if resumeAfter is set to true) or cleared and replaced with the fades defined in this thing. 
An OFF command stops the fades and either restores the previously suspended fades (if resumeAfter is set to true) or just holds the current values. 
If any of the DMX channels in a chaser receives a command from another thing, the status of the chaser is updated to OFF. 
Chaser things define a control channel that can be used to dynamically change the chasers fade configuration.

## Discovery

Discovery is not supported at the moment. You have to add all bridges and things manually.  

## Thing Configuration

Since the brightness perception of the human eye is not linear, all bridges support `applycurve`,  a list of channels `applycurve` that have a CIE 1931 lightness correction (cf. [Poynton, C.A.: “Gamma” and its Disguises: The Nonlinear Mappings of Intensity in Perception, CRTs, Film and Video, SMPTE Journal Dec. 1993, pp. 1099 - 1108](http://www.poynton.com/PDFs/SMPTE93_Gamma.pdf)) applied. 
This list follows the format of the thing channel definition. 
This is used regardless of the thing(s) that are associated to the channel.

All bridges can make use of the `refreshrate` option. 
It determines at what frequency the DMX output is refreshed. 
The achievable refresh rate depends on the number of channels and the output type. 
A value of `0` disables the output, the default value is 30 Hz.

### ArtNet Bridge (`artnet-bridge`)

The ArtNet bridge has one mandatory configuration value: network address (`address`). 
The network address defines the IP address of the receiving node, it is also allowed to use a FQDN if DNS resolution is available.
If necessary the default port 6454 can be changed by adding `:<port>` to the address.
Multiple receivers can be added, separated by a comma.

The universe (`universe`) can range from 0-32767, this value defaults to 0. 

There are two more configuration values that usually don't need to be touched. 
The address and port of the sender will be automatically selected by the kernel, if they need to be set to a fixed value, this can be done with `localaddress`. 
The format is identical to the receiver address. 
Unlike DMX512-A (E1.11), the ArtNet standard allows to suppress repeated transmissions of unchanged universes for a certain time.
This is enabled by default and will re-transmit unchanged data with a fixed refresh rate of 800ms.
If for some reason continuous transmission is needed, the `refreshmode` can be set to `always`, opposed to the default `standard`.

### Lib485 Bridge (`lib485-bridge`)

The Lib485 bridge has one mandatory configuration value: network address (`address`).
This is the host/port where lib485 is running.
This can be an IP address but it is also allowed to use a FQDN if DNS resolution is available.
If necessary the default port 9020 can be changed by adding `:<port>` to the address.
The default address is localhost.
Multiple receivers can be added, separated by a comma.

### sACN/E1.31 Bridge (`sacn-bridge`)

The sACN bridge has one mandatory configuration value: transmission mode (`mode`).
The transmission mode can be set to either `unicast` or `multicast`, where the later one is the default value. 
If unicast mode is selected, it is mandatory to define the network address (`address`) of the receiving node.
This can be an IP address but it is also allowed to use a FQDN if DNS resolution is available.
If necessary the default port 5568 can be changed by adding `:<port>` to the address.
Multiple receivers can be added, separated by a comma.

The universe (`universe`) can range from 1-63999, this value defaults to 1. 

There are some more configuration values that usually don't need to be touched.
The address and port of the sender will be automatically selected by the kernel, if they need to be set to a fixed value, this can be done with `localaddress`.
The format is identical to the receiver address. 

Unlike DMX512-A (E1.11), the E1.31 standard allows to suppress repeated transmissions of unchanged universes for a certain time.
This is enabled by default and will re-transmit unchanged data with a fixed refresh rate of 800ms.
If for some reason continuous transmission is needed, the `refreshmode` can be set to `always`, opposed to the default `standard`.

### Chaser Thing (`chaser`)

There are two mandatory configuration values for a chaser thing: the `dmxid` and `steps`. 

The `dmxid` is a list of DMX channels that are associated with this thing.
There are several possible formats: `channel,channel,channel,...` or `channel/width` or a combination of both. 

The `steps` value is a list of steps that shall be run by the chaser.
The format of a single step is `fadetime:value,value2, ...:holdtime`, two or more steps are concatenated by `step1|step2|...`.
In textual configuration line-breaks, spaces and tabs are allowed for readability.
The fadetime is used for fading from the current value to the new value.
In contrast to the dimmer thing, this is an absolute value.
The hold time defines how long this step shall wait before advancing to the next step.
A value of -1 is used to hold forever.
Both times are in ms.

An optional configuration value is `resumeafter`.
It defaults to false but if set to true, the original state of the channel (including running fades) will be suspended until the chaser receives an OFF command.

### Dimmer Thing (`dimmer`)

There is one mandatory configuration value for a dimmer thing.
It is the `dmxid`, a list of DMX channels that are associated with this thing.
There are several possible formats: `channel1,channel2,channel3,...` or `channel/width` or a combination of both. 

The `fadetime` option allows a smooth transition from the current to the new value.
The time unit is ms and the interval is for a fade from 0-100%.
If the current value is 25% and the new value is 75% the time needed for this change is half of `fadetime`.
`fadetime`is used for absolute values or ON/OFF commands send to the `brightness` channel. 
Related is the `dimtime` option: it defines the time in ms from 0-100% if incremental dimming (`INCREASE`/`DECREASE`) is used.
For convenient use `dimtime` usually is set to a larger value than `fadetime`.
Typical values are 500-1000 ms for `fadetime` and 2000-5000 ms for `dimtime`. 

Advanced options are the `turnonvalue`and the `turnoffvalue`. 
They default to 255 (equals 100%) and 0 (equals 0%) respectively.
This value can be set individually for all DMX channels, the format is `value1,value2, ...` with values from 0 to 255.
If less values than DMX channels are defined, the values will be re-used from the beginning (i.e. if two values are defined, value1 will be used for channel1, channel3, ... and value2 will be used for channel2, channel4, ...).
These values will be used if the thing receives an ON or OFF command. 

The `dynamicturnonvalue` can be set to `true` or `false` (default).
If enabled, thing overwrites the previous turn-on value with the current channel values.
The next `ON` command uses these values instead of the default (or configuration supplied) values. 

### Color Thing (`color`)

There is one mandatory configuration value for a dimmer thing.
It is the `dmxid`, a list of DMX channels that are associated with this thing.
There are several possible formats: `channel1,channel2,channel3,...` or `channel/width` or a combination of both.
The number of channels has to be a multiple of three. 

The `fadetime` option allows a smooth transition from the current to the new value.
The time unit is ms and the interval is for a fade from 0-100%.
If the current value is 25% and the new value is 75% the time needed for this change is half of `fadetime`.
`fadetime`is used for absolute values or ON/OFF commands send to the `brightness` channel. 
Related is the `dimtime` option: it defines the time in ms from 0-100% if incremental dimming (`INCREASE`/`DECREASE`) is used.
For convenient use `dimtime` usually is set to a larger value than `fadetime`.
Typical values are 500-1000 ms for `fadetime` and 2000-5000 ms for `dimtime`.

Advanced options are the `turnonvalue`and the `turnoffvalue`.
They default to 255 (equals 100%) and 0 (equals 0%) respectively.
This value can be set individually for all DMX channels, the format is `value1,value2, ...` with values from 0 to 255.
If less values than DMX channels are defined, the values will be re-used from the beginning (i.e. if two values are defined, value1 will be used for channel1, channel3, ... and value2 will be used for channel2, channel4, ...).
For color things the number of values has to be a multiple of three.
These values will be used if the thing receives an ON or OFF command. 

The `dynamicturnonvalue` can be set to `true` or `false` (default).
If enabled, thing overwrites the previous turn-on value with the current channel values.
The next `ON` command uses these values instead of the default (or configuration supplied) values. 

### Tunable White Thing (`tunablewhite`)

There is one mandatory configuration value for a dimmer thing. 
It is the `dmxid`, a list of DMX channels that are associated with this thing.
There are several possible formats: `channel1,channel2,channel3,...` or `channel/width` or a combination of both.
The number of channels has to be even. In the order "cool white, warm white".
Additionally a channel for cool and warm white brightness as well as color temperature (`0` being the coolest, `100` being the warmest) will be provided. 

The `fadetime` option allows a smooth transition from the current to the new value.
The time unit is ms and the interval is for a fade from 0-100%.
If the current value is 25% and the new value is 75% the time needed for this change is half of `fadetime`.
`fadetime`is used for absolute values or ON/OFF commands send to the `brightness` channel. 
Related is the `dimtime` option: it defines the time in ms from 0-100% if incremental dimming (`INCREASE`/`DECREASE`) is used.
For convenient use `dimtime` usually is set to a larger value than `fadetime`.
Typical values are 500-1000 ms for `fadetime` and 2000-5000 ms for `dimtime`.

Advanced options are the `turnonvalue`and the `turnoffvalue`.
They default to 255 (equals 100%) and 0 (equals 0%) respectively.
This value can be set individually for all DMX channels, the format is `value1,value2, ...` with values from 0 to 255.
If less values than DMX channels are defined, the values will be re-used from the beginning (i.e. if two values are defined, value1 will be used for channel1, channel3, ... and value2 will be used for channel2, channel4, ...). 
For tunable white things the number of values has to be a multiple of two.
These values will be used if the thing receives an ON or OFF command. 
 
The `dynamicturnonvalue` can be set to `true` or `false` (default).
If enabled, thing overwrites the previous turn-on value with the current channel values.
The next `ON` command uses these values instead of the default (or configuration supplied) values. 
 
 
## Channels

| Type-ID         | Thing               | Item                 | Description                                        |
|-----------------|---------------------|----------------------|----------------------------------------------------|
|brightness       |dimmer, tunablewhite |Switch, Dimmer        | controls the brightness                            |
|color            |color                |Switch, Dimmer, Color | allows to set the color and brightness             |
|colortemperature |tunablewhite         |Number                | allows to set the color temperature                |
|brightness_r     |color                |Switch, Dimmer        | controls the brightness of the red channel         |
|brightness_g     |color                |Switch, Dimmer        | controls the brightness of the green channel       |
|brightness_b     |color                |Switch, Dimmer        | controls the brightness of the blue channel        |
|brightness_cw    |tunablewhite         |Switch, Dimmer        | controls the brightness of the cool white channel  |
|brightness_ww    |tunablewhite         |Switch, Dimmer        | controls the brightness of the warm white channel  |
|control          |chaser               |String                | allows to change the chaser steps                  |
|switch           |chaser               |Switch                | turns the chaser ON or OFF                         |
|mute             |(all bridges)        |Switch                | mutes the DMX output of the bridge                 |

*Note:* the string send to the control channel of chaser things has to be formatted like the `steps` configuration of the chaser thing. If the new string is invalid, the old configuration will be used.

## Rule Actions

This binding includes a rule action, which allows to immediately change DMX channels from within rules.
There is a separate instance for each bridge, which can be retrieved e.g. through

```
val dmxActions = getActions("dmx","dmx:sacn-bridge:mydmxbridge")
```

where the first parameter always has to be `dmx` and the second is the full Thing UID of the bridge that should be used.
Once this action instance is retrieved, you can invoke the `sendFade(String channels, String fade, Boolean resumeAfter)` method on it:

```
dmxActions.sendFade("1:41/3","10000:255,255,255:-1", false)
```

The parameters are the same as in a chaser thing configuration.

## Full Example

This example defines a sACN/E1.31 bridge in unicast mode which transmits universe 2 and three things: a three channel dimmer used to control a RGB light, which takes 1s to fade from one color to another and 10s from 0-100% on incremental dim commands, a single channel dimmer which will turn on only to 90% if it receives a ON command and does not fully switch off (to 10%) if it receives an OFF command and chaser which changes the colors like a traffic light.

### demo.things:

```
Bridge dmx:sacn-bridge:mybridge [ mode="unicast", address="192.168.0.60", universe=2 ] {
 color  rgb    [dmxid="5/3", fadetime=1000, dimtime=10000 ]
 dimmer single [dmxid="50", fadetime=1000, turnonvalue="230", turnoffvalue="25" ]
 chaser ampel  [dmxid="10,12,13", steps="100:255,0,0:1000|100:255,255,0:500|100:0,0,255:1000|100:0,255,0:500" ] 
}
```

### demo.items:

```
Color MyColorItem "My Color Item" { channel="dmx:color:mybridge:rgb:color" }
Dimmer MyDimmerItem "My Dimmer Item" { channel="dmx:dimmer:mybridge:single:brightness" }
Switch MyChaserItem "My Chaser Item" { channel="dmx:chaser:mybridge:ampel:switch" }
```

### demo.sitemap:

```
sitemap demo label="Main Menu"
{
    Frame {
        // Color
        Colorpicker item=MyColorItem
        
        // Dimmer
        Switch item=MyDimmerItem
        Slider item=MyDimmerItem
        
        // Chaser
        Switch item=MyChaserItem
    }
}
```
# FS Internet Radio Binding

This binding integrates internet radios based on the [Frontier Silicon chipset](http://www.frontier-silicon.com/).

## Supported Things

Successfully tested are internet radios:

 * [Hama IR100](https://de.hama.com/00054823/hama-internetradio-ir110)
 * [Medion MD87180, MD86988, MD86955, MD87528](http://internetradio.medion.com/)
 * [Silvercrest SMRS18A1, SMRS30A1, SMRS35A1, SIRD 14 C2](http://www.silvercrest-multiroom.de/en/products/stereo-internet-radio/)
 * [Roberts Stream 83i and 93i](https://www.robertsradio.com/uk/products/radio/smart-radio/)
 * [Auna Connect 150, Auna KR200](https://www.auna.de/Radios/Internetradios/)
 * [TechniSat DIGITRADIO 350 IR and 850](https://www.technisat.com/en_XX/DAB+-Radios-with-Internetradio/352-10996/)
 * [TTMicro AS Pinell Supersound](http://www.ttmicro.no/radio)
 * [Revo SuperConnect](https://revo.co.uk/products/)
 * [Sangean WFR-28C](http://sg.sangean.com.tw/products/product_category.asp?cid=2)
 * [Roku SoundBridge M1001](https://soundbridge.roku.com/soundbridge/index.php)
 * [Dual IR 3a](https://www.dual.de/produkte/digitalradio/radio-station-ir-3a/) 

But in principle, all internet radios based on the [Frontier Silicon chipset](http://www.frontier-silicon.com/) should be supported because they share the same API.
So It is very likely that other internet radio models of the same manufacturers do also work.

## Community

For discussions and questions about supported radios, check out [this thread](https://community.openhab.org/t/internet-radio-i-need-your-help/2131).

## Discovery

The radios are discovered through UPnP in the local network.

If your radio is not discovered, please try to access its API via: `http://<radio-ip>/fsapi/CREATE_SESSION?pin=1234` (1234 is default pin, if you get a 403 error, check the radio menu for the correct pin).<br/>
If you get a 404 error, maybe a different port than the standard port 80 is used by your radio; try scanning the open ports of your radio.<br/>
If you get a result like `FS_OK 1902014387`, your radio is supported.

If this is the case, please [add your model to this documentation](https://github.com/eclipse/smarthome/edit/master/extensions/binding/org.eclipse.smarthome.binding.fsinternetradio/README.md) and/or provide discovery information in [this thread](https://community.openhab.org/t/internet-radio-i-need-your-help/2131).

## Binding Configuration

The binding itself does not need a configuration.

## Thing Configuration

Each radio must be configured via its ip address, port, pin, and a refresh rate.

* If the ip address is not discovered automatically, it must be manually set.
* The default port is `80` which should work for most radios.
* The default pin is `1234` for most radios, but if it does not work or if it was changed, look it up in the on-screen menu of the radio.
* The default refresh rate for the radio items is `60` seconds; `0` disables periodic refresh.

## Channels

All devices support some of the following channels:

| Channel Type ID | Item Type | Description | Access |
|-----------------|-----------|-------------|------- |
| power | Switch | Switch the radio on or off | R/W |
| volume-percent | Dimmer | Radio volume (min=0, max=100) | R/W |
| volume-absolute | Number | Radio volume (min=0, max=32) | R/W |
| mute | Switch | Mute the radio | R/W |
| mode | Number | The radio mode, e.g. FM radio, internet radio, AUX, etc. (model-specific, see list below) | R/W |
| preset | Number | Preset radio stations configured in the radio (write-only) | W |
| play-info-name | String | The name of the current radio station or track | R |
| play-info-text | String | Additional information e.g. of the current radio station | R |

The radio mode depends on the internet radio model (and its firmware version!).
This list is just an example how the mapping looks like for some of the devices, please try it out and adjust your sitemap for your particular radio.

| Radio Mode               | 0              | 1                       | 2         | 3            | 4         | 5        | 6            | 7         | 8         | 9      |
|--------------------------|----------------|-------------------------|-----------|--------------|-----------|----------|--------------|-----------|-----------| -------|
| Hama IR110               | Internet Radio | Spotify                 | Player    | AUX in       | -         | -        | -            | -         | -         | -      |
| Medion MD87180           | Internet Radio | Music Player (USB, LAN) | DAB Radio | FM Radio     | AUX in    | -        | -            | -         | -         | -      |
| Medion MD 86988          | Internet Radio | Music Player            | FM Radio  | AUX in       | -         | -        | -            | -         | -         | -      |
| Technisat DigitRadio 580 | Internet Radio | Spotify                 | -         | Music Player | DAB Radio | FM Radio | AUX in       | CD        | Bluetooth | -      |
| Dual IR 3a               | Internet Radio | Spotify                 | -         | Music Player | DAB Radio | FM Radio | Bluetooth    | -         | -         | -      |
| Silvercrest SIRD 14 C2   | Internet Radio | TIDAL                   | Deezer    | Qobuz        | Spotify   | -        | Music Player | DAB Radio | FM Radio  | AUX in |
| Auna KR200 Kitchen Radio | Internet Radio | Spotify                 | -         | Music Player | DAB Radio | FM Radio | AUX in       | -         | -         | -      |


## Full Example

demo.things:

```
fsinternetradio:radio:radioInKitchen [ ip="192.168.0.42" ]
```

demo.items:

```
Switch RadioPower "Radio Power" { channel="fsinternetradio:radio:radioInKitchen:power" }
Switch RadioMute "Radio Mute" { channel="fsinternetradio:radio:radioInKitchen:mute" }
Dimmer RadioVolume "Radio Volume" { channel="fsinternetradio:radio:radioInKitchen:volume-percent" }
Number RadioMode "Radio Mode" { channel="fsinternetradio:radio:radioInKitchen:mode" }
Number RadioPreset "Radio Stations" { channel="fsinternetradio:radio:radioInKitchen:preset" }
String RadioInfo1 "Radio Info1" { channel="fsinternetradio:radio:radioInKitchen:play-info-name" }
String RadioInfo2 "Radio Info2" { channel="fsinternetradio:radio:radioInKitchen:play-info-text" }
```

demo.sitemap:

```
sitemap demo label="Main Menu"
{
	Frame {
		Switch item=RadioPower
		Slider visibility=[RadioPower==ON] item=RadioVolume
		Switch visibility=[RadioPower==ON] item=RadioMute
		Selection visibility=[RadioPower==ON] item=RadioPreset mappings=[0="Favourit 1", 1="Favourit 2", 2="Favourit 3", 3="Favourit 4"]
		Selection visibility=[RadioPower==ON] item=RadioMode mappings=[0="Internet Radio", 1="Musik Player", 2="DAB", 3="FM", 4="AUX"]
		Text visibility=[RadioPower==ON] item=RadioInfo1
		Text visibility=[RadioPower==ON] item=RadioInfo2
	}
}
```
# Homematic Binding

This is the binding for the [eQ-3 Homematic Solution](http://www.eq-3.de/).
This binding allows you to integrate, view, control and configure all Homematic devices in Eclipse SmartHome.

## Supported Bridges

All gateways which provides the Homematic BIN- or XML-RPC API:

- CCU 1, 2 and 3
- [RaspberryMatic](https://github.com/jens-maus/RaspberryMatic)
- [Homegear](https://www.homegear.eu) (>= 0.8.0-1988)
- [piVCCU](https://github.com/alexreinert/piVCCU)
- [YAHM](https://github.com/leonsio/YAHM)
- [Windows BidCos service](http://www.eq-3.de/downloads.html?kat=download&id=125)
- [OCCU](https://github.com/eq-3/occu)

The Homematic IP Access Point **does not support** this API and and can't be used with this binding.

Homematic IP support:
- CCU2 with at least firmware 2.17.15
- [RaspberryMatic](https://github.com/jens-maus/RaspberryMatic) with the [HM-MOD-RPI-PCB](https://www.elv.de/homematic-funkmodul-fuer-raspberry-pi-bausatz.html) or [RPI-RF-MOD](https://www.elv.de/homematic-funk-modulplatine-fuer-raspberry-pi-3-rpi-rf-mod-komplettbausatz.html) RF module
- [piVCCU](https://github.com/alexreinert/piVCCU)
- [YAHM](https://github.com/leonsio/YAHM)

These ports are used by the binding by default to communicate **TO** the gateway:

- RF components: 2001
- WIRED components: 2000
- HMIP components: 2010
- CUxD: 8701
- TclRegaScript: 8181
- Groups: 9292

And **FROM** the gateway to the binding:

- XML-RPC: 9125
- BIN-RPC: 9126

CCU Autodiscovery:
* UDP 43439

**Note:** The binding tries to identify the gateway with XML-RPC and uses henceforth:

-   **CCU**
    - **RF**: XML-RPC
    - **WIRED**: XML-RPC
    - **HMIP**: XML-RPC
    - **CUxD**: BIN-RPC (CUxD version >= 1.6 required)
    - **Groups**: XML-RPC

-   **Homegear**
    - BIN-RPC

-   **Other**
    - XML-RPC

## Supported Things

All devices connected to a Homematic gateway.
All required metadata are generated during device discovery.
With Homegear or a CCU, variables and scripts are supported too.

## Discovery

Gateway discovery is available:
* CCU
* RaspberryMatic >= 2.29.23.20171022
* Homegear >= 0.6.x
* piVCCU

For all other gateways you have to manually add a bridge in a things file. Device discovery is supported for all gateways.

The binding has a gateway type autodetection, but sometimes a gateway does not clearly notify the type.
If you are using a YAHM for example, you have to manually set the gateway type in the bride configuration to CCU.

If autodetection can not identify the gateway, the binding uses the default gateway implementation.
The difference is, that variables, scripts and device names are not supported, everything else is the same.

### Automatic install mode during discovery

Besides discovering devices that are already known by the gateway, it may be desired to connect new devices to your system - which requires your gateway to be in install mode. Starting the binding's DiscoveryService will automatically put your gateway(s) in install mode for a specified period of time (see installModeDuration).

**Note:** Enabling / disabling of install mode is also available via GATEWAY_EXTRAS. You may use this if you prefer.

**Exception:** If a gateway is not ONLINE, the install mode will not be set automatically. _For instance during initialization of the binding its DiscoveryService is started and will discover devices that are already connected. However, the install mode is not automatically enabled in this situation because the gateway is in the status INITIALIZING._

## Bridge Configuration

There are several settings for a bridge:

-   **gatewayAddress** (required)
Network address of the Homematic gateway

-   **gatewayType**
Hint for the binding to identify the gateway type (auto|ccu|noccu) (default = auto).

-   **callbackHost**
Callback network address of the system runtime, default is auto-discovery

-   **bindAddress**
The address the XML-/BINRPC server binds to, default is callbackHost

-   **callbackPort DEPRECATED, use binCallbackPort and xmlCallbackPort**
Callback port of the binding's server, default is 9125 and counts up for each additional bridge

-   **xmlCallbackPort**
Callback port of the binding's XML-RPC server, default is 9125 and counts up for each additional bridge

-   **binCallbackPort**
Callback port of the binding's BIN-RPC server, default is 9126 and counts up for each additional bridge

-   **aliveInterval DEPRECATED, not necessary anymore**
The interval in seconds to check if the communication with the Homematic gateway is still alive. If no message receives from the Homematic gateway, the RPC server restarts (default = 300)

-   **reconnectInterval DEPRECATED, not necessary anymore**
The interval in seconds to force a reconnect to the Homematic gateway, disables aliveInterval! (0 = disabled, default = disabled).
If you have no sensors which sends messages in regular intervals and/or you have low communication, the aliveInterval may restart the connection to the Homematic gateway to often.
The reconnectInterval disables the aliveInterval and reconnects after a fixed period of time.
Think in hours when configuring (one hour = 3600)

-   **timeout**
The timeout in seconds for connections to a Homematic gateway (default = 15)

-   **discoveryTimeToLive**
The time to live in seconds for discovery results of a Homematic gateway (default = -1, which means infinite)

-   **socketMaxAlive**
The maximum lifetime of a socket connection to and from a Homematic gateway in seconds (default = 900)

-   **rfPort**
The port number of the RF daemon (default = 2001)

-   **wiredPort**
The port number of the HS485 daemon (default = 2000)

-   **hmIpPort**
The port number of the HMIP server (default = 2010)

-   **cuxdPort**
The port number of the CUxD daemon (default = 8701)

-   **installModeDuration**
Time in seconds that the controller will be in install mode when a device discovery is initiated (default = 60)

-   **unpairOnDeletion**
If set to true, devices are automatically unpaired from the gateway when their corresponding things are deleted.
**Warning!** The option "factoryResetOnDeletion" also unpairs a device, so in order to avoid unpairing on deletion completely, both options need to be set to false! (default = false)

-   **factoryResetOnDeletion**
If set to true, devices are automatically factory reset when their corresponding things are removed.
Due to the factory reset, the device will also be unpaired from the gateway, even if "unpairOnDeletion" is set to false! (default = false)

The syntax for a bridge is:

```java
homematic:bridge:NAME
```

- **homematic** the binding id, fixed
- **bridge** the type, fixed
- **name** the name of the bridge

### Example

- minimum configuration

```java
Bridge homematic:bridge:ccu [ gatewayAddress="..."]
```

- with callback settings

```java
Bridge homematic:bridge:ccu [ gatewayAddress="...", callbackHost="...", callbackPort=... ]
```

- multiple bridges

```java
Bridge homematic:bridge:lxccu [ gatewayAddress="..."]
Bridge homematic:bridge:occu  [ gatewayAddress="..."]
```

## Thing Configuration

Things are all discovered automatically, you can handle them in PaperUI.

If you really like to manually configure a thing:

```java
Bridge homematic:bridge:ccu [ gatewayAddress="..." ]
{
  Thing HM-LC-Dim1T-Pl-2    JEQ0999999
}
```

The first parameter after Thing is the device type, the second the serial number.
If you are using Homegear, you have to add the prefix ```HG-``` for each type.
The ```HG-``` prefix is only needed for Things, not for Items or channel configs.
This is necessary, because the Homegear devices supports more datapoints than Homematic devices.

```java
  Thing HG-HM-LC-Dim1T-Pl-2     JEQ0999999
```

As additional parameters you can define a name and a location for each thing.
The Name will be used to identify the Thing in the Paper UI lists, the Location will be used in the Control section of PaperUI to sort the things.

```java
  Thing HG-HM-LC-Dim1T-Pl-2     JEQ0999999  "Name"  @  "Location"
```

All channels have two configs:

- **delay**: delays transmission of a command **to** the Homematic gateway, duplicate commands are filtered out
- **receiveDelay**: delays a received event **from** the Homematic gateway, duplicate events are filtered out (OH 2.2)

The receiveDelay is handy for dimmers and rollershutters for example.
If you have a slider in a UI and you move this slider to a new position, it jumps around because the gateway sends multiple events with different positions until the final has been reached.
If you set the ```receiveDelay``` to some seconds, these events are filtered out and only the last position is distributed to the binding.
The disadvantage is of course, that all events for this channel are delayed.

```java
  Thing HM-LC-Dim1T-Pl-2    JEQ0999999 "Name"  @  "Location" {
      Channels:
          Type HM-LC-Dim1T-Pl-2_1_level : 1#LEVEL [
              delay = 0,
              receiveDelay = 4
          ]
  }
```

The Type is the device type, channel number and lowercase channel name separated with a underscore.
Note that, for Homegear devices, in contrast to the specification of the Thing above no ```HG-``` prefix is needed for the specification of the Type of the Channel.

The channel configs are optional.
Example without channel configs
```java
  Thing HM-LC-Dim1T-Pl-2    JEQ0999999 "Name"  @  "Location" {
      Channels:
          Type HM-LC-Dim1T-Pl-2_1_LEVEL : 1#LEVEL
  }
```

### Items

In the items file, you can map the datapoints, the syntax is:

```java
homematic:TYPE:BRIDGE:SERIAL:CHANNELNUMBER#DATAPOINTNAME
```

- **homematic:** the binding id, fixed
- **type:** the type of the Homematic device
- **bridge:** the name of the bridge
- **serial:** the serial number of the Homematic device
- **channelnumber:** the channel number of the Homematic datapoint
- **datapointname:** the name of the Homematic datapoint

```java
Switch  RC_1  "Remote Control Button 1" { channel="homematic:HM-RC-19-B:ccu:KEQ0099999:1#PRESS_SHORT" }
Dimmer  Light "Light [%d %%]"           { channel="homematic:HM-LC-Dim1T-Pl-2:ccu:JEQ0555555:1#LEVEL" }
```

**Note:** don't forget to add the ```HG-``` type prefix for Homegear devices

## Virtual device and datapoints

The binding supports one virtual device and some virtual datapoints.
Virtual datapoints are generated by the binding and provides special functionality.

### GATEWAY-EXTRAS

The GATEWAY-EXTRAS is a virtual device which contains a switch to reload all values from all devices and also a switch to put the gateway in the install mode to add new devices.
If the gateway supports variables and scripts, you can handle them with this device too.
The type is generated: GATEWAY-EXTRAS-&lsqb;BRIDGE_ID&rsqb;.
Example: bridgeId=ccu, type=GATEWAY-EXTRAS-CCU
Address: fixed GWE00000000

### RELOAD_ALL_FROM_GATEWAY

A virtual datapoint (Switch) to reload all values for all devices, available in channel 0 in GATEWAY-EXTRAS

### RELOAD_RSSI

A virtual datapoint (Switch) to reload all rssi values for all devices, available in channel 0 in GATEWAY-EXTRAS

### RSSI

A virtual datapoint (Number) with the unified RSSI value from RSSI_DEVICE and RSSI_PEER, available in channel 0 for all wireless devices

### INSTALL_MODE

A virtual datapoint (Switch) to start the install mode on the gateway, available in channel 0 in GATEWAY-EXTRAS

### INSTALL_MODE_DURATION

A virtual datapoint (Integer) to hold the duration for the install mode, available in channel 0 in GATEWAY-EXTRAS (max 300 seconds, default = 60)

### DELETE_MODE

A virtual datapoint (Switch) to remove the device from the gateway, available in channel 0 for each device. Deleting a device is only possible if DELETE_DEVICE_MODE is not LOCKED

### DELETE_DEVICE_MODE

A virtual datapoint (Enum) to configure the device deletion with DELETE_MODE, available in channel 0 for each device

- **LOCKED:** (default) device can not be deleted
- **RESET:** device is reset to factory settings before deleting
- **FORCE:** device is also deleted if it is not reachable
- **DEFER:** if the device can not be reached, it is deleted at the next opportunity

**Note:** if you change the value and don't delete the device, the virtual datapoints resets to LOCKED after 30 seconds

### ON_TIME_AUTOMATIC

A virtual datapoint (Number) to automatically set the ON_TIME datapoint before the STATE or LEVEL datapoint is sent to the gateway, available for all devices which supports the ON_TIME datapoint.
This is usefull to automatically turn off the datapoint after the specified time.

### DISPLAY_OPTIONS

A virtual datapoint (String) to control the display of a 19 button Homematic remote control (HM-RC-19), available on channel 18

The remote control display is limited to five characters, a longer text is truncated.

You have several additional options to control the display.

- BEEP *(TONE1, TONE2, TONE3)* - let the remote control beep
- BACKLIGHT *(BACKLIGHT_ON, BLINK_SLOW, BLINK_FAST)* - control the display backlight
- UNIT *(PERCENT, WATT, CELSIUS, FAHRENHEIT)* - display one of these units
- SYMBOL *(BULB, SWITCH, WINDOW, DOOR, BLIND, SCENE, PHONE, BELL, CLOCK, ARROW_UP, ARROW_DOWN)* - display symbols, multiple symbols possible

You can combine any option, they must be separated by a comma.
If you specify more than one option for BEEP, BACKLIGHT and UNIT, only the first one is taken into account and all others are ignored. For SYMBOL you can specify multiple options.

**Examples:**

Assumed you mapped the virtual datapoint to a String item called Display_Options

```java
String Display_Options "Display_Options" { channel="homematic:HM-RC-19-B:ccu:KEQ0099999:18#DISPLAY_OPTIONS" }
```

show message TEST:

```shell
smarthome send Display_Options "TEST"
```

show message TEXT, beep once and turn backlight on:

```shell
smarthome send Display_Options "TEXT, TONE1, BACKLIGHT_ON"
```

show message 15, beep once, turn backlight on and shows the celsius unit:

```shell
smarthome send Display_Options "15, TONE1, BACKLIGHT_ON, CELSIUS"
```

show message ALARM, beep three times, let the backlight blink fast and shows a bell symbol:

```shell
smarthome send Display_Options "ALARM, TONE3, BLINK_FAST, BELL"
```

Duplicate options: TONE3 is ignored, because TONE1 is specified previously.

```shell
smarthome send Display_Options "TEXT, TONE1, BLINK_FAST, TONE3"
```

### DISPLAY_SUBMIT

Adds multiple virtual datapoints to the HM-Dis-WM55 and HM-Dis-EP-WM55 devices to easily send (colored) text and icons to the display.

**Note:** The HM-Dis-EP-WM55 has only a black and white display and therefore does not support datapoints for colored lines. In addition, only lines 1-3 can be set.

Example: Display text at line 1,3 and 5 when the bottom button on the display is pressed

- Items

```java
String Display_line_1   "Line 1"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_LINE_1" }
String Display_line_3   "Line 3"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_LINE_3" }
String Display_line_5   "Line 5"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_LINE_5" }

String Display_color_1  "Color 1"   { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_COLOR_1" }
String Display_color_3  "Color 3"   { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_COLOR_3" }
String Display_color_5  "Color 5"   { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_COLOR_5" }

String Display_icon_1   "Icon 1"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_ICON_1" }
String Display_icon_3   "Icon 3"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_ICON_3" }
String Display_icon_5   "Icon 5"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_ICON_5" }

Switch Button_bottom    "Button"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#PRESS_SHORT" }
Switch Display_submit   "Submit"    { channel="homematic:HM-Dis-WM55:ccu:NEQ0123456:1#DISPLAY_SUBMIT" }
```

- Rule

```javascript
rule "Display Test"
when
    Item Button_bottom received update ON
then
    sendCommand(Display_line_1, "Line 1")
    sendCommand(Display_line_3, "Line 3")
    sendCommand(Display_line_5, "Line 5")

    sendCommand(Display_icon_1, "NONE")
    sendCommand(Display_icon_3, "OPEN")
    sendCommand(Display_icon_5, "INFO")

    sendCommand(Display_color_1, "NONE")
    sendCommand(Display_color_3, "RED")
    sendCommand(Display_color_5, "BLUE")

    sendCommand(Display_submit, ON)
end
```

### BUTTON

A virtual datapoint (String) to simulate a key press, available on all channels that contains PRESS_ datapoints.
Available values:
* `SHORT_PRESS`: triggered on a short key press
* `LONG_PRESS`: triggered on a key press longer than `LONG_PRESS_TIME` (variable configuration per key, default is 0.4 s)
* `DOUBLE_PRESS`: triggered on a short key press but only if the latest `SHORT_PRESS` or `DOUBLE_PRESS` event is not older than 2.0 s (not related to `DBL_PRESS_TIME` configuration, which is more like a key lock because if it is other than `0.0` single presses are not notified anymore)

Example: to capture a short key press on the 19 button remote control in a rule

```javascript
rule "example trigger rule"
when
    Channel 'homematic:HM-RC-19-B:ccu:KEQ0012345:1#BUTTON' triggered SHORT_PRESS
then
    ...
end
```


## Troubleshooting

**SHORT & LONG_PRESS events of push buttons do not occur on the event bus**

It seems buttons like the HM-PB-2-WM55 do just send these kind of events to the CCU if they are mentioned in a CCU program.
A simple workaround to make them send these events is, to create a program (rule inside the CCU) that does just have a "When" part and no "Then" part, in this "When" part each channel needs to be mentioned at least once.
As the HM-PB-2-WM55 for instance has two channels, it is enough to mention the SHORT_PRESS event of channel 1 & 2.
The LONG_PRESS events will work automatically as they are part of the same channels.
After the creation of this program, the button device will receive configuration data from the CCU which have to be accepted by pressing the config-button at the back of the device.

**INSTALL_TEST**

If a button is still not working and you do not see any PRESS_LONG / SHORT in your log file (loglevel DEBUG), it could be because of enabled security.
Try to disable security of your buttons in the HomeMatic Web GUI and try again.
If you can't disable security try to use key INSTALL_TEST which gets updated to ON for each key press

**-1 Failure**

A device may return this failure while fetching the datapoint values.
I've tested pretty much but i did not found the reason. The HM-ES-TX-WM device for example always returns this failure, it's impossible with the current CCU2 firmware (2.17.15) to fetch the values.
I've implemented two workarounds, if a device returns the failure, workaround one is executed, if the device still returns the failure, workaround two is executed.
This always works in my tests, but you may see a OFFLINE, ONLINE cycle for the device.
Fetching values is only done at startup or if you trigger a REFRESH. I hope this will be fixed in one of the next CCU firmwares.
With [Homegear](https://www.homegear.eu) everything works as expected.

**No variables and scripts in GATEWAY-EXTRAS**

The gateway autodetection of the binding can not clearly identify the gateway and falls back to the default implementation.
Use the ```gatewayType=ccu``` config to force the binding to use the CCU implementation.

**Variables out of sync**

The CCU only sends a event if a datapoint of a device has changed.
There is (currently) no way to receive a event automatically when a variable has changed.
To reload all variable values, send a REFRESH command to any variable.
e.g you have a item linked to a variable with the name Var_1
In the console:

```shell
smarthome:send Var_1 REFRESH
```

In scripts:

```javascript
import org.eclipse.smarthome.core.types.RefreshType
...
sendCommand(Var_1, RefreshType.REFRESH)
```

**Note:** adding new and removing deleted variables from the GATEWAY-EXTRAS Thing is currently not supported. You have to delete the Thing, start a scan and add it again.

### Debugging and Tracing

If you want to see what's going on in the binding, switch the loglevel to DEBUG in the Karaf console

```shell
log:set DEBUG org.eclipse.smarthome.binding.homematic
```

If you want to see even more, switch to TRACE to also see the gateway request/response data

```shell
log:set TRACE org.eclipse.smarthome.binding.homematic
```

Set the logging back to normal

```shell
log:set INFO org.eclipse.smarthome.binding.homematic
```

To identify problems, i need a full startup TRACE log

```shell
stop org.eclipse.smarthome.binding.homematic
log:set TRACE org.eclipse.smarthome.binding.homematic
start org.eclipse.smarthome.binding.homematic
```
# Philips Hue Binding

This binding integrates the [Philips Hue Lighting system](http://www.meethue.com).
The integration happens through the Hue bridge, which acts as an IP gateway to the ZigBee devices.

![Philips Hue](doc/hue.jpg)

## Supported Things

The Hue bridge is required as a "bridge" for accessing any other Hue devices.

Almost all available Hue devices are supported by this binding.
This includes not only the "friends of Hue", but also products like the LivingWhites adapter.
Additionally, it is possible to use OSRAM Lightify devices as well as other ZigBee LightLink compatible products.
Please note that the devices need to be registered with the Hue bridge before it is possible for this binding to use them.

The Hue binding supports all seven types of lighting devices defined for ZigBee LightLink ([see page 24, table 2](https://www.nxp.com/documents/user_manual/JN-UG-3091.pdf).
These are:

| Device type              | ZigBee Device ID | Thing type |
|--------------------------|------------------|------------|
| On/Off Light             | 0x0000           | 0000       |
| On/Off Plug-in Unit      | 0x0010           | 0010       |
| Dimmable Light           | 0x0100           | 0100       |
| Dimmable Plug-in Unit    | 0x0110           | 0110       |
| Colour Light             | 0x0200           | 0200       |
| Extended Colour Light    | 0x0210           | 0210       |
| Colour Temperature Light | 0x0220           | 0220       |

All different models of Hue, OSRAM, or other bulbs nicely fit into one of these seven types.
This type also determines the capability of a device and with that the possible ways of interacting with it.
The following matrix lists the capabilities (channels) for each type:

| Thing type  | On/Off | Brightness | Color | Color Temperature |
|-------------|:------:|:----------:|:-----:|:-----------------:|
|  0000       |    X   |            |       |                   |    
|  0010       |    X   |            |       |                   |    
|  0100       |    X   |     X      |       |                   |
|  0110       |    X   |     X      |       |                   |
|  0200       |    X   |            |   X   |                   |
|  0210       |    X   |            |   X   |          X        |
|  0220       |    X   |     X      |       |          X        |

Beside bulbs and luminaires the Hue binding supports some ZigBee sensors.
Currently only Hue specific sensors are tested successfully (e.g. Hue Motion Sensor and Hue Dimmer Switch).
The Hue Motion Sensor registers a `ZLLLightLevel` sensor, a `ZLLPresence` sensor and a `ZLLTemperature` sensor in one device.

| Device type                 | ZigBee Device ID | Thing type |
|-----------------------------|------------------|------------|
| Light Sensor                | 0x0106           | 0106       |
| Occupancy Sensor            | 0x0107           | 0107       |
| Temperature Sensor          | 0x0302           | 0302       |
| Non-Colour Controller       | 0x0820           | 0820       |
| Non-Colour Scene Controller | 0x0830           | 0830       |

The type of a specific device can be found in the configuration section for things in the PaperUI.
It is part of the unique thing id which could look like:

```
hue:0210:00178810d0dc:1
```

The thing type is the second string behind the first colon and in this example it is **0210**.

## Discovery

The Hue bridge is discovered through UPnP in the local network.
Once it is added as a Thing, its authentication button (in the middle) needs to be pressed in order to authorize the binding to access it.
Once the binding is authorized, it automatically reads all devices that are set up on the Hue bridge and puts them into the Inbox.

## Thing Configuration

The Hue bridge requires the IP address as a configuration value in order for the binding to know where to access it.
In the thing file, this looks e.g. like

```
Bridge hue:bridge:1 [ ipAddress="192.168.0.64" ]
```

A user to authenticate against the Hue bridge is automatically generated.
Please note that the generated user name cannot be written automatically to the `.thing` file, and has to be set manually.
The generated user name can be found in the log files after pressing the authentication button on the bridge.
The user name can be set using the `userName` configuration value, e.g.:

```
Bridge hue:bridge:1 [ ipAddress="192.168.0.64", userName="qwertzuiopasdfghjklyxcvbnm1234" ]
```

| Parameter             | Description                                                                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ipAddress             | Network address of the Hue bridge. **Mandatory**                                                                                                                                                                                         |
| userName              | Name of a registered Hue bridge user, that allows to access the API. **Mandatory**                                                                                                                                                       |
| pollingInterval       | Seconds between fetching light values from the Hue bridge. Optional, the default value is 10 (min="1", step="1").                                                                                                                        |
| sensorPollingInterval | Milliseconds between fetching sensor-values from the Hue bridge. A higher value means more delay for the sensor values, but a too low value can cause congestion on the bridge. Optional, the default value is 500 (min="50", step="1"). |

### Devices

The devices are identified by the number that the Hue bridge assigns to them (also shown in the Hue App as an identifier).
Thus, all it needs for manual configuration is this single value like

```
0210 bulb1 [ lightId="1" ]
```

or

```
0107 motion-sensor [ sensorId="4" ]
```

## Channels

The devices support some of the following channels:

| Channel Type ID   | Item Type          | Description                                                                                                                             | Thing types supporting this channel |
|-------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| switch            | Switch             | This channel supports switching the device on and off.                                                                                  | 0000, 0010                          |
| color             | Color              | This channel supports full color control with hue, saturation and brightness values.                                                    | 0200, 0210                          |
| brightness        | Dimmer             | This channel supports adjusting the brightness value. Note that this is not available, if the color channel is supported.               | 0100, 0110, 0220                    |
| color_temperature | Dimmer             | This channel supports adjusting the color temperature from cold (0%) to warm (100%).                                                    | 0210, 0220                          |
| alert             | String             | This channel supports displaying alerts by flashing the bulb either once or multiple times. Valid values are: NONE, SELECT and LSELECT. | 0000, 0100, 0200, 0210, 0220        |
| effect            | Switch             | This channel supports color looping.                                                                                                    | 0200, 0210, 0220                    |
| dimmer_switch     | Number             | This channel shows which button was last pressed on the dimmer switch.                                                                  | 0820                                |
| illuminance       | Number:Illuminance | This channel shows the current illuminance measured by the sensor.                                                                      | 0106                                |
| light_level       | Number             | This channel shows the current light level measured by the sensor. **Advanced**                                                         | 0106                                |
| dark              | Switch             | This channel indicates whether the light level is below the darkness threshold or not.                                                  | 0106                                |
| daylight          | Switch             | This channel indicates whether the light level is below the daylight threshold or not.                                                  | 0106                                |
| presence          | Switch             | This channel indicates whether a motion is detected by the sensor or not.                                                               | 0107                                |
| temperature       | Number:Temperature | This channel shows the current temperature measured by the sensor.                                                                      | 0302                                |
| last_updated      | DateTime           | This channel the date and time when the sensor was last updated.                                                                        | 0820, 0830, 0106, 0107, 0302        |
| battery_level     | Number             | This channel shows the battery level.                                                                                                   | 0820, 0106, 0107, 0302             |
| battery_low       | Switch             | This channel indicates whether the battery is low or not.                                                                               | 0820, 0106, 0107, 0302             |

### Trigger Channels

The dimmer switch additionally supports a trigger channel.

| Channel ID          | Description                      | Thing types supporting this channel |
|---------------------|----------------------------------|-------------------------------------|
| dimmer_switch_event | Event for dimmer switch pressed. | 0820                                |
| tap_switch_event    | Event for tap switch pressed.    | 0830                                |

The `dimmer_switch_event` can trigger one of the following events:

| Button              | State           | Event |
|---------------------|-----------------|-------|
| Button 1 (ON)       | INITIAL_PRESSED | 1000  |
|                     | HOLD            | 1001  |
|                     | SHORT RELEASED  | 1002  |
|                     | LONG RELEASED   | 1003  |
| Button 2 (DIM UP)   | INITIAL_PRESSED | 2000  |
|                     | HOLD            | 2001  |
|                     | SHORT RELEASED  | 2002  |
|                     | LONG RELEASED   | 2003  |
| Button 3 (DIM DOWN) | INITIAL_PRESSED | 3000  |
|                     | HOLD            | 3001  |
|                     | SHORT RELEASED  | 3002  |
|                     | LONG RELEASED   | 3003  |
| Button 4 (OFF)      | INITIAL_PRESSED | 4000  |
|                     | HOLD            | 4001  |
|                     | SHORT RELEASED  | 4002  |
|                     | LONG RELEASED   | 4003  |

The `tap_switch_event` can trigger one of the following events:

| Button   | State    | Event |
|----------|----------|-------|
| Button 1 | Button 1 | 34    |
| Button 2 | Button 2 | 16    |
| Button 3 | Button 3 | 17    |
| Button 4 | Button 4 | 18    |

## Full Example

In this example **Bulb1** is a standard Philips Hue bulb (LCT001) which supports `color` and `color_temperature`.
Therefore it is a thing of type **0210**.
**Bulb2** is an OSRAM tunable white bulb (PAR16 50 TW) supporting `color_temperature` and so the type is **0220**.

### demo.things:

```
Bridge hue:bridge:1 [ ipAddress="192.168.0.64" ] {
	0210 bulb1 [ lightId="1" ]
	0220 bulb2 [ lightId="2" ]
	0106 light-level-sensor [ sensorId="3" ]
	0107 motion-sensor [ sensorId="4" ]
	0302 temperature-sensor [ sensorId="5" ]
	0820 dimmer-switch [ sensorId="6" ]
}
```

### demo.items:

```
// Bulb1
Switch	Light1_Toggle		{ channel="hue:0210:1:bulb1:color" }
Dimmer	Light1_Dimmer		{ channel="hue:0210:1:bulb1:color" }
Color	Light1_Color		{ channel="hue:0210:1:bulb1:color" }
Dimmer	Light1_ColorTemp	{ channel="hue:0210:1:bulb1:color_temperature" }
String	Light1_Alert		{ channel="hue:0210:1:bulb1:alert" }
Switch	Light1_Effect		{ channel="hue:0210:1:bulb1:effect" }

// Bulb2
Switch	Light2_Toggle		{ channel="hue:0220:1:bulb2:brightness" }
Dimmer	Light2_Dimmer		{ channel="hue:0220:1:bulb2:brightness" }
Dimmer	Light2_ColorTemp	{ channel="hue:0220:1:bulb2:color_temperature" }

// Light Level Sensor
Number:Illuminance LightLevelSensorIlluminance { channel="hue:0106:light-level-sensor:illuminance" }

// Motion Sensor
Switch   MotionSensorPresence     { channel="hue:0107:motion-sensor:presence" }
DateTime MotionSensorLastUpdate   { channel="hue:0107:motion-sensor:last_updated" }
Number   MotionSensorBatteryLevel { channel="hue:0107:motion-sensor:battery_level" }
Switch   MotionSensorLowBattery   { channel="hue:0107:motion-sensor:battery_low" }

// Temperature Sensor
Number:Temperature TemperatureSensorTemperature { channel="hue:0302:temperature-sensor:temperature" }
```

Note: The bridge ID is in this example **1** but can be different in each system.

### demo.sitemap:

```
sitemap demo label="Main Menu"
{
	Frame {
		// Bulb1
		Switch		item=		Light1_Toggle
		Slider		item=		Light1_Dimmer
		Colorpicker	item=		Light1_Color
		Slider		item=		Light1_ColorTemp
		Switch		item=		Light1_Alert		mappings=[NONE="None", SELECT="Alert", LSELECT="Long Alert"]
		Switch		item=		Light1_Effect

		// Bulb2
		Switch		item=		Light2_Toggle
		Slider		item=		Light2_Dimmer
		Slider		item=		Light2_ColorTemp

		// Motion Sensor
		Switch item=MotionSensorPresence
		Text item=MotionSensorLastUpdate
		Text item=MotionSensorBatteryLevel
		Switch item=MotionSensorLowBattery
	}
}
```

### Events

 ```php
rule "example trigger rule"
when
    Channel "hue:0820:dimmer-switch:dimmer_switch_event" triggered <EVENT>
then
    ...
end
```
# LIFX Binding

This binding integrates the [LIFX LED Lights](http://www.lifx.com/). All LIFX lights are directly connected to the WLAN and the binding communicates with them over a UDP protocol.

![LIFX E27](doc/lifx_e27.jpg)

## Supported Things

The following table lists the thing types of the supported LIFX devices:

| Device Type                  | Thing Type   |
|------------------------------|--------------|
| Original 1000                | colorlight   |
| Color 650                    | colorlight   |
| Color 1000                   | colorlight   |
| Color 1000 BR30              | colorlight   |
| LIFX A19                     | colorlight   |
| LIFX BR30                    | colorlight   |
| LIFX Downlight               | colorlight   |
| LIFX GU10                    | colorlight   |
| LIFX Mini Color              | colorlight   |
| LIFX Tile                    | colorlight   |
|                              |              |
| LIFX+ A19                    | colorirlight |
| LIFX+ BR30                   | colorirlight |
|                              |              |
| LIFX Beam                    | colormzlight |
| LIFX Z                       | colormzlight |
|                              |              |
| White 800 (Low Voltage)      | whitelight   |
| White 800 (High Voltage)     | whitelight   |
| White 900 BR30 (Low Voltage) | whitelight   |
| LIFX Mini Day and Dusk       | whitelight   |
| LIFX Mini White              | whitelight   |

The thing type determines the capability of a device and with that the possible ways of interacting with it. The following matrix lists the capabilities (channels) for each type:

| Thing Type   | On/Off | Brightness | Color | Color Zone | Color Temperature | Color Temperature Zone | Infrared |
|--------------|:------:|:----------:|:-----:|:----------:|:-----------------:|:----------------------:|:--------:|
| colorlight   | X      |            | X     |            | X                 |                        |          |
| colorirlight | X      |            | X     |            | X                 |                        | X        |
| colormzlight | X      |            | X     | X          | X                 | X                      |          |
| whitelight   | X      | X          |       |            | X                 |                        |          |

## Discovery

The binding is able to auto-discover all lights in a network over the LIFX UDP protocol. Therefore all lights must be turned on.

*Note:* To get the binding working, all lights must be added to the WLAN network first with the help of the [LIFX smart phone applications](http://www.lifx.com/pages/go). The binding is NOT able to add or detect lights outside the network.

## Thing Configuration

Each light needs a Device ID or Host as a configuration parameter. The device ID is printed as a serial number on the light and can also be found within the native LIFX Android or iOS application. But usually the discovery works quite reliably, so that a manual configuration is not needed.

However, in the thing file, a manual configuration looks e.g. like

```
Thing lifx:colorlight:living [ deviceId="D073D5A1A1A1", fadetime=200 ]
```

The *fadetime* is an optional thing configuration parameter which configures the time to fade to a new color value (in ms). When the *fadetime* is not configured, the binding uses 300ms as default.

You can optionally also configure a fixed Host or IP address when lights are in a different subnet and are not discovered.

```
Thing lifx:colorirlight:porch [ host="10.120.130.4", fadetime=0 ]
```

## Channels

All devices support some of the following channels:

| Channel Type ID | Item Type | Description                                                                                                                                                      | Thing Types                                        |
|-----------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| brightness      | Dimmer    | This channel supports adjusting the brightness value.                                                                                                            | whitelight                                         |
| color           | Color     | This channel supports full color control with hue, saturation and brightness values.                                                                             | colorlight, colorirlight, colormzlight             |
| colorzone       | Color     | This channel supports full zone color control with hue, saturation and brightness values.                                                                        | colormzlight                                       |
| infrared        | Dimmer    | This channel supports adjusting the infrared value. *Note:* IR capable lights only activate their infrared LEDs when the brightness drops below a certain level. | colorirlight                                       |
| signalstrength  | Number    | This channel represents signal strength with values 0, 1, 2, 3 or 4; 0 being worst strength and 4 being best strength.                                           | colorlight, colorirlight, colormzlight, whitelight |
| temperature     | Dimmer    | This channel supports adjusting the color temperature from cold (0%) to warm (100%).                                                                             | colorlight, colorirlight, colormzlight, whitelight |
| temperaturezone | Dimmer    | This channel supports adjusting the zone color temperature from cold (0%) to warm (100%).                                                                        | colormzlight                                       |

The *color* and *brightness* channels have a "Power on brightness" configuration option that is used to determine the brightness when a light is switched on. When it is left empty, the brightness of a light remains unchanged when a light is switched on or off.

The *color* channels have a "Power on color" configuration option that is used to determine the hue, saturation, brightness levels when a light is switched on. When it is left empty, the color of a light remains unchanged when a light is switched on or off. Configuration options contains 3 comma separated values, where first value is hue (0-360), second  saturation (0-100) and third brightness (0-100). If both "Power on brightness" and "Power on color" configuration options are defined, "Power on brightness" option overrides the brightness level defined on the "Power on color" configuration option.

The *temperature* channels have a "Power on temperature" configuration option that is used to determine the color temperature when a light is switched on. When it is left empty, the color temperature of a light remains unchanged when a light is switched on or off.

MultiZone lights (*colormzlight*) have serveral channels (e.g. *colorzone0*, *temperaturezone0*, etc.) that allow for controlling specific zones of the light. Changing the *color* and *temperature* channels will update the states of all zones. The *color* and *temperature* channels of MultiZone lights always return the same state as *colorzone0*, *temperaturezone0*.


## Full Example

In this example **living** is a Color 1000 light that has a *colorlight* thing type which supports *color* and *temperature* channels.

The **porch** light is a LIFX+ BR30 that has a *colorirlight* thing type which supports *color*, *temperature* and *infrared* channels.

The **ceiling** light is a LIFX Z with 2 strips (16 zones) that has a *colormzlight* thing type which supports *color*, *colorzone*, *temperature* and *temperaturezone* channels.

Finally, **kitchen** is a White 800 (Low Voltage) light that has a *whitelight* thing type which supports *brightness* and *temperature* channels.

Either create a single *Color* item linked to the *color* channel and define *Switch*, *Slider* and *Colorpicker* entries with this item in the sitemap.
Or create items for each type (*Color*, *Switch*, *Dimmer*) and define the correspondent entries in the sitemap.


### demo.things:

```
Thing lifx:colorlight:living [ deviceId="D073D5A1A1A1" ]

Thing lifx:colorlight:living2 [ deviceId="D073D5A2A2A2" ] {
    Channels:
        Type color : color [ powerOnBrightness=50 ]
}

Thing lifx:colorirlight:porch [ deviceId="D073D5B2B2B2", host="10.120.130.4", fadetime=0 ] {
    Channels:
        Type color : color [ powerOnBrightness=75 ]
}

Thing lifx:colorirlight:porch [ deviceId="D073D5B2B2B2", host="10.120.130.4", fadetime=0 ] {
    Channels:
        Type temperature : temperature [ powerOnTemperature=20 ]
}

Thing lifx:colorirlight:porch [ deviceId="D073D5B2B2B2", host="10.120.130.4", fadetime=0 ] {
    Channels:
        Type color : color [ powerOnColor="120,100,50" ] // Deep green, 50% brightness
}

Thing lifx:colormzlight:ceiling [ host="10.120.130.5" ]

Thing lifx:whitelight:kitchen [ deviceId="D073D5D4D4D4", fadetime=150 ]
```

### demo.items:

```
// Living
Color Living_Color { channel="lifx:colorlight:living:color" }
Dimmer Living_Temperature { channel="lifx:colorlight:living:temperature" }

// Living2 (alternative approach)
Color Living2_Color { channel="lifx:colorlight:living2:color" }
Switch Living2_Switch { channel="lifx:colorlight:living2:color" }
Dimmer Living2_Dimmer { channel="lifx:colorlight:living2:color" }
Dimmer Living2_Temperature { channel="lifx:colorlight:living2:temperature" }

// Porch
Color Porch_Color { channel="lifx:colorirlight:porch:color" }
Dimmer Porch_Infrared { channel="lifx:colorirlight:porch:infrared" }
Dimmer Porch_Temperature { channel="lifx:colorirlight:porch:temperature" }
Number Porch_Signal_Strength { channel="lifx:colorirlight:porch:signalstrength" }

// Ceiling
Color Ceiling_Color { channel="lifx:colormzlight:ceiling:color" }
Dimmer Ceiling_Temperature { channel="lifx:colormzlight:ceiling:temperature" }
Color Ceiling_Color_Zone_0 { channel="lifx:colormzlight:ceiling:colorzone0" }
Dimmer Ceiling_Temperature_Zone_0 { channel="lifx:colormzlight:ceiling:temperaturezone0" }
Color Ceiling_Color_Zone_15 { channel="lifx:colormzlight:ceiling:colorzone15" }
Dimmer Ceiling_Temperature_Zone_15 { channel="lifx:colormzlight:ceiling:temperaturezone15" }

// Kitchen
Switch Kitchen_Toggle { channel="lifx:whitelight:kichen:brightness" }
Dimmer Kitchen_Brightness { channel="lifx:whitelight:kitchen:brightness" }
Dimmer Kitchen_Temperature { channel="lifx:whitelight:kitchen:temperature" }
```

### demo.sitemap:

```
sitemap demo label="Main Menu"
{
    Frame label="Living" {
        Switch item=Living_Color
        Slider item=Living_Color
        Colorpicker item=Living_Color
        Slider item=Living_Temperature
    }

    Frame label="Living2" {
        Switch item=Living2_Toggle
        Slider item=Living2_Dimmer
        Colorpicker item=Living2_Color
        Slider item=Living2_Temperature
    }

    Frame label="Porch" {
        Switch item=Porch_Color
        Slider item=Porch_Color
        Colorpicker item=Porch_Color
        Slider item=Porch_Temperature
        Slider item=Porch_Infrared
        Text item=Porch_Signal_Strength
    }

    Frame label="Ceiling" {
        Switch item=Ceiling_Color
        Slider item=Ceiling_Color
        Colorpicker item=Ceiling_Color
        Slider item=Ceiling_Temperature
        Colorpicker item=Ceiling_Color_Zone_0
        Slider item=Ceiling_Temperature_Zone_0
        Colorpicker item=Ceiling_Color_Zone_15
        Slider item=Ceiling_Temperature_Zone_15
    }

    Frame label="Kitchen" {
        Switch item=Kitchen_Toggle
        Slider item=Kitchen_Brightness
        Slider item=Kitchen_Temperature
    }
}
```
# LIRC Binding

This binding integrates infrared transceivers through [LIRC](http://www.lirc.org) or [WinLIRC](http://winlirc.sourceforge.net).

A list of remote configuration files for LIRC is available [here](http://lirc-remotes.sourceforge.net/remotes-table.html).


## Supported Things

This binding supports LIRC and WinLIRC as bridges for accessing the configured remotes.

LIRC must be started with TCP enabled. On systemd based systems, TCP can be enabled by editing the file
`/usr/lib/systemd/system/lirc.service` and adding `--listen` to the end of the `ExecStart` line. An example
systemd service file for LIRC is shown below.

```ini
[Unit]
Description=Linux Infrared Remote Control
After=network.target

[Service]
RuntimeDirectory=lirc
ExecStart=/usr/sbin/lircd --nodaemon --driver=default --device=/dev/lirc0 --listen

[Install]
WantedBy=multi-user.target
```

By default, LIRC will listen on IP address 0.0.0.0 (any available IP address) and port 8765. If you would
rather run LIRC on a specific port or IP address, you can use `--listen=192.168.1.100:9001` instead.


## Discovery

Discovery of the LIRC bridge is not supported. However, remotes will be automatically discovered once
a bridge is configured.

## Example Configuration

### Things

```xtend
Bridge lirc:bridge:local [ host="192.168.1.120", portNumber="9001" ] {
    Thing remote Onkyo_RC_799M [ remote="Onkyo_RC-799M" ]
    Thing remote Samsung [ remote="Samsung" ]
}
```

Bridge:

* **host**: IP address or hostname of the LIRC server. Defaults to localhost
* **port**: The port number the LIRC server is listening on. Defaults to 8765

Remote:

* **remote**: The name of the remote as known by LIRC

### Items

```xtend
String Remote_AVReceiver { channel="lirc:remote:local:Onkyo_RC_799M:transmit" }
String Remote_TV { channel="lirc:remote:local:Samsung:transmit" }
```

### Rules

```xtend
rule "LIRC Test"
when
    Channel 'lirc:remote:local:Samsung:event' triggered KEY_DVD
then
    // Toggle base boost on the AV Receiver
    sendCommand(Remote_AVReceiver, "KEY_BASEBOOST")
    // Increase the volume by 5.
    sendCommand(Remote_AVReceiver, "KEY_VOLUMEUP 5")
end
```


## Channels

This binding currently supports following channels:

| Channel Type ID | Item Type    | Description                           |
|-----------------|--------------|---------------------------------------|
| event           | Trigger      | Triggers when a button is pressed.    |
| transmit        | String       | Used to transmit IR commands to LIRC. |
# meteoblue Binding

The meteoblue binding uses the [meteoblue weather service](https://content.meteoblue.com/en/content/view/full/4511)
to provide weather information.


## Supported Things

The binding has two thing types.

The first thing type is the weather thing. Each weather thing has the ID `weather` and retrieves weather data for one location.
The second thing type is the bridge thing. The bridge thing, which has the ID `bridge`, holds the API key to be used for all of
its child things.


## Thing Configuration

### Bridge Thing Configuration

| Property      | Default Value | Required? | Description          |
| ------------- |:-------------:| :-------: | -------------------- |
| apiKey        |               | Yes       | The api key to be used with the meteoblue service |


### Weather Thing Configuration

| Property      | Default Value | Required? | Description          |
| ------------- |:-------------:| :-------: | -------------------- |
| location      |               | Yes       | The latitude, longitude, and optionally altitude of the location, separated by commas (e.g. 45.6,45.7,45.8). Altitude, if given, should be in meters.
| refresh       | 240           | No        | The time between calls to refresh the weather data, in minutes |
| serviceType   | NonCommercial | No        | The service type to be used.  Either 'Commercial' or 'NonCommercial' |
| timeZone      |               | No        | The time zone to use for the location. Optional, but the service recommends it be specified. The service gets the time zone from a database if not specified. |


## Channels

### Channel Groups

| Group Name       | Description |
| ---------------- | ----------- |
| forecastToday    | Today's forecast |
| forecastTomorrow | Tomorrow's forecast |
| forecastDay2     | Forecast 2 days out |
| forecastDay3     | Forecast 3 days out |
| forecastDay4     | Forecast 4 days out |
| forecastDay5     | Forecast 5 days out |
| forecastDay6     | Forecast 6 days out |

### Channels

Each of the following channels is supported in all of the channel groups.

| Channel                  | Item Type          | Description |
| ------------------------ | ------------------ | ----------- |
| height                   | Number:Length      | Altitude above sea-level of the location (in meters) |
| forecastDate             | DateTime           | Forecast date |
| UVIndex                  | Number             | UltraViolet radiation index at ground level (0-16) |
| minTemperature           | Number:Temperature | Low temperature |
| maxTemperature           | Number:Temperature | High temperature |
| meanTemperature          | Number:Temperature | Mean temperature |
| feltTemperatureMin       | Number:Temperature | Low "feels like" temperature |
| feltTemperatureMax       | Number:Temperature | High "feels like" temperature |
| relativeHumidityMin      | Number             | Low relative humidity |
| relativeHumidityMax      | Number             | High relative humidity |
| relativeHumidityMean     | Number             | Mean relative humidity |
| precipitationProbability | Number             | Percentage probability of precipitation |
| precipitation            | Number:Length      | Total precipitation (water amount) |
| convectivePrecipitation  | Number:Length      | Total rainfall (water amount) |
| rainSpot                 | String             | Precipitation distribution around the location |
| rainArea                 | Image              | Color-coded image generated from rainSpot |
| snowFraction             | Number             | Percentage of precipitation falling as snow |
| snowFall                 | Number:Length      | Total snowfall (calculated) |
| cardinalWindDirection    | String             | Name of the wind direction (eg. N, S, E, W, etc.) |
| windDirection            | Number             | Wind direction (in degrees) |
| minWindSpeed             | Number:Speed       | Low wind speed  |
| maxWindSpeed             | Number:Speed       | High wind speed |
| meanWindSpeed            | Number:Speed       | Mean wind speed |
| minSeaLevelPressure      | Number:Pressure    | Low sea level pressure  |
| maxSeaLevelPressure      | Number:Pressure    | High sea level pressure |
| meanSeaLevelPressure     | Number:Pressure    | Mean sea level pressure |
| condition                | String             | A brief description of the forecast weather condition (e.g. 'Overcast') |
|                          |                    | Valid values range from 1 - 17 (see the [meteoblue docs](https://content.meteoblue.com/nl/service-specifications/standards/symbols-and-pictograms#eztoc14635_1_6)) |
| icon                     | Image              | Image used to represent the forecast (calculated) |
| predictability           | Number             | Estimated certainty of the forecast (percentage) |
| predictabilityClass      | Number             | Range 0-5 (0=very low, 5=very high) |
| precipitationHours       | Number             | Total hours of the day with precipitation |
| humidityGreater90Hours   | Number             | Total hours of the day with relative humidity greater than 90% |


## Full Example

demo.things:

```
Bridge meteoblue:bridge:metBridge "metBridge" [ apiKey="XXXXXXXXXXXX" ] {
	Thing weather A51 "Area 51" [ serviceType="NonCommercial", location="37.23,-115.5,1360", timeZone="America/Los_Angeles", refresh=240 ] {
	}
}
```

demo.items:

```
// ----------------- meteoblue GROUPS ------------------------------------------
Group weatherDay0 "Today's Weather"
Group weatherDay1 "Tomorrow's Weather"
Group weatherDay2 "Weather in 2 days"
Group weatherDay3 "Weather in 3 days"
Group weatherDay4 "Weather in 4 days"
Group weatherDay5 "Weather in 5 days"
Group weatherDay6 "Weather in 6 days"


// ----------------- meteoblue ITEMS -------------------------------------------
DateTime todayForecastDate  "Forecast for [%1$tY/%1$tm/%1$td]"  <calendar>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#forecastDate"}
String todayPCode    "Pictocode [%d]"  <iday>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#condition"}
String todayCond     "Condition [%s]"  <iday>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#condition"}
String todayIcon     "Icon [%s]"       (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#icon"}
Number todayUV       "UV Index [%d]"  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#UVIndex"}
Number:Temperature  todayTempL  "Low Temp [%.2f F]"   <temperature>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#minTemperature"}
Number:Temperature  todayTempH  "High Temp [%.2f F]"  <temperature>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#maxTemperature"}
Number todayHumM     "Mean Humidity [%d %%]"  <humidity>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#relativeHumidityMean"}
Number todayPrecPr   "Prec. Prob. [%d %%]"  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#precipitationProbability"}
Number:Length todayPrec     "Total Prec. [%.2f in]"  <rain>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#precipitation"}
Number:Length todayRain     "Rainfall [%.2f in]"  <rain>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#convectivePrecipitation"}
Image  todayRainArea "Rain area"   <rain>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#rainArea"}
Number todaySnowF    "Snow fraction [%.2f]"  <climate>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#snowFraction"}
Number:Length  todaySnow     "Snowfall [%.2f in]"  <rain>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#snowFall"}
Number:Pressure  todayPressL   "Low Pressure [%d %unit%]"   <pressure>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#minSeaLevelPressure"}
Number:Pressure  todayPressH   "High Pressure [%d %unit%]"  <pressure>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#maxSeaLevelPressure"}
Number todayWindDir   "Wind Direction [%d]"  <wind>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#windDirection"}
String todayCWindDir  "Cardinal Wind Direction [%s]"  <wind>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#cardinalWindDirection"}
Number:Speed  todayWindSpL   "Low Wind Speed [%.2f mph]"   <wind>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#minWindSpeed"}
Number:Speed  todayWindSpH   "High Wind Speed [%.2f mph]"  <wind>  (weatherDay0)  {channel="meteoblue:weather:metBridge:A51:forecastToday#maxWindSpeed"}
```

demo.sitemap:

````
sitemap weather label="Weather"
{
  Frame label="Weather" {
    Group item=weatherDay0
    Group item=weatherDay1
    Group item=weatherDay2
    Group item=weatherDay3
    Group item=weatherDay4
    Group item=weatherDay5
    Group item=weatherDay6
  }
}
````
# MQTT Binding

> MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol.
> It was designed as an extremely lightweight publish/subscribe messaging transport.

MQTT is a server/client architecture.
A server, also called broker is not provided within this binding,
but it allows to detect running brokers and to manage connections.
The hereby configured broker connections make it possible to link MQTT topics to Things and Channels.

It has the following extensions:

<!--list-subs-->

## Supported Bridges

* Broker: This bridge represents an MQTT Broker connection, configured and managed by this binding.
* SystemBroker: A system configured broker cannot be changed by this binding and will be listed as read-only system-broker.

## Bridge Configuration
 
Required configuration parameters are:

* __host__: The IP/Hostname of the MQTT broker. Be aware that this binding allows only one bridge / one connection per unique host:port.
* __port__: The optional port of the MQTT broker. If none is provided, the typical ports 1883 and 8883 (SSL) are used. Be aware that this binding allows only one bridge / one connection per unique host:port.
* __secure__: Uses TLS/SSL to establish a secure connection to the broker. Can be "OFF","ON","AUTO". The AUTO setting prefers a secure connection but will fall-back to an insecure one. Default is ON.

Additionally the following parameters can be set:

* __qos__: Quality of Service. Can be 0, 1 or 2. Please read the MQTT specification for details. Defaults to 0.
* __clientID__: Use a fixed client ID. Defaults to empty which means a user ID is generated for this connection.
* __retainMessages__: Retain messages. Defaults to false.

Reconnect parameters are:

* __reconnectTime__: Reconnect time in ms. If a connection is lost, the binding will wait this time before it tries to reconnect. Defaults to 60000 (60s).
* __keepAlive__: Keep alive / heartbeat timer in ms. It can take up to this time to determine if a server connection is lost. A lower value may keep the broker unnecessarily busy for no or little additional value. Defaults to 60000 (60s).

An MQTT last will and testament can be configured:

* __lwtMessage__: An optional last will and testament message. Defaults to empty. 
* __lwtTopic__: The last will topic. Defaults to empty and therefore disables the last will. 
* __lwtQos__: The optional qos of the last will. Defaults to 0. 
* __lwtRetain__: Retain last will message. Defaults to false.

For more security, the following optional parameters can be altered:

* __username__: The MQTT username (since MQTT 3.1). Defaults to empty.
* __password__: The MQTT password (since MQTT 3.1). Defaults to empty.
* __certificatepin__: If this is set: After the next connection has been successfully established, the certificate is pinned. The connection will be refused if another certificate is used. Clear **certificate** to allow a new certificate for the next connection attempt. This option will increase security.
* __publickeypin__: If this is set: After the next connection has been successfully established, the public key of the broker is pinned. The connection will be refused if another public key is used. Clear **publickey** to allow a new public key for the next connection attempt. This option will increase security.
* __certificate__: The certificate hash. If **certificatepin** is set this hash is used to verify the connection. Clear to allow a new certificate pinning on the next connection attempt. If empty will be filled automatically by the next successful connection. An example input would be `SHA-256:83F9171E06A313118889F7D79302BD1B7A2042EE0CFD029ABF8DD06FFA6CD9D3`.
* __publickey__: The public key hash. If **publickeypin** is set this hash is used to verify the connection. Clear to allow a new public key pinning on the next connection attempt. If empty will be filled automatically by the next successful connection. An example input would be `SHA-256:83F9171E06A313118889F7D79302BD1B7A2042EE0CFD029ABF8DD06FFA6CD9D3`.

## Supported Channels

You can extend your broker connection bridges with a channel:

* __publishTrigger__: This channel is triggered when a value is published to the configured MQTT topic on this broker connection. The event payload will be the received MQTT topic value.

Configuration parameters are:

* __stateTopic__: This channel will trigger on this MQTT topic. This topic can contain wildcards like + and # for example "all/in/#" or "sensors/+/config".
* __payload__: An optional condition on the value of the MQTT topic that must match before this channel is triggered.

## Full Example

In a first example a very secure connection to a broker is defined. It pins the returned certificate and public key.
If someone tries a man in the middle attack later on, this broker connection will recognize it and refuse a connection.
Be aware that if your brokers certificate changes, you need to remove the connection entry and add it again. Secure connections are default, if you do not provide the "secure" parameter.

The second connection is a plain, unsecured one. Use this only for local MQTT Brokers.

A third connection uses a username and password for authentication.
Secure is set to false as the username and password is requested by the broker.
The credentials are plain values on the wire, therefore you should only use this on a secure connection.

In a forth connection, the public key pinning is enabled again.
This time, a public key hash is provided to pin the connection to a specific server.
It follows the form "hashname:hashvalue". Valid *hashnames* are SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 and all others listed
in [Java MessageDigest Algorithms](https://docs.oracle.com/javase/9/docs/specs/security/standard-names.html#messagedigest-algorithms).

`mqttConnections.things`:

```xtend
mqtt:broker:mySecureBroker [ host="192.168.0.41", secure=true, certificatepin=true, publickeypin=true ]
mqtt:broker:myUnsecureBroker [ host="192.168.0.42", secure=false ]

mqtt:broker:myAuthentificatedBroker [ host="192.168.0.43", secure=false, username="user", password="password" ]

mqtt:broker:pinToPublicKey [ host="192.168.0.44", secure=true, publickeypin=true, publickey="SHA-256:9a6f30e67ae9723579da2575c35daf7da3b370b04ac0bde031f5e1f5e4617eb8" ]
```
# MQTT Generic Thing Binding

> MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport.

This binding allows to link MQTT topics to Things.

## Supported Things

There a few Things dedicated to MQTT conventions available and a Generic MQTT Thing.
The last one is comparable to what was found in the mqtt 1.x binding. 

### Homie Thing

Devices that follow the [Homie convention](https://homieiot.github.io/) 3.x and better
are auto-discovered and represented by this Homie Thing.

Find the next table to understand the topology mapping from Homie to the Framework: 

| Homie    | Framework     | Example MQTT topic                 |
|----------|---------------|------------------------------------|
| Device   | Thing         | homie/super-car                    |
| Node     | Channel Group | homie/super-car/engine             |
| Property | Channel       | homie/super-car/engine/temperature |

System trigger channels are supported using non-retained properties, with *enum* data type and with the following formats:
* Format: "PRESSED,RELEASED" -> system.rawbutton
* Format: "SHORT\_PRESSED,DOUBLE\_PRESSED,LONG\_PRESSED" -> system.button
* Format: "DIR1\_PRESSED,DIR1\_RELEASED,DIR2\_PRESSED,DIR2\_RELEASED" -> system.rawrocker

### HomeAssistant Thing

HomeAssistant MQTT Components are recognised as well. The base topic needs to be **homeassistant**. 
The mapping is structured like this:


| HA MQTT               | Framework     | Example MQTT topic                 |
|-----------------------|---------------|------------------------------------|
| Object                | Thing         | homeassistant/../../object         |
| Component+Node        | Channel Group | homeassistant/component/node/object|
| -> Component Features | Channel       | state/topic/defined/in/comp/config |

### Generic MQTT Thing

A generic MQTT Thing has no configuration and is a pure shell for channels that you add yourself.

You can manually add the following channels:

#### Supported Channels

* **string**: This channel can show the received text on the given topic and can send text to a given topic.
* **number**: This channel can show the received number on the given topic and can send a number to a given topic. It can have a min, max and step values.
* **dimmer**: This channel handles numeric values as percentages. It can have min, max and step values.
* **contact**: This channel represents a open/close state of a given topic.
* **switch**: This channel represents a on/off state of a given topic and can send an on/off value to a given topic.
* **colorRGB**: This channel handles color values in RGB format.
* **colorHSB**: This channel handles color values in HSB format.
* **location**: This channel handles a location.
* **image**: This channel handles binary images in common java supported formats (bmp,jpg,png).
* **datetime**: This channel handles date/time values.
* **rollershutter**: This channel is for rollershutters.

## Thing and Channel Configuration

All things require a configured broker.

### Common Channel Configuration Parameters

* __stateTopic__: The MQTT topic that represents the state of the thing. This can be empty, the thing channel will be a state-less trigger then. You can use a wildcard topic like "sensors/+/event" to retrieve state from multiple MQTT topics. 
* __transformationPattern__: An optional transformation pattern like [JSONPath](http://goessner.net/articles/JsonPath/index.html#e2) that is applied to all incoming MQTT values.
* __transformationPatternOut__: An optional transformation pattern like [JSONPath](http://goessner.net/articles/JsonPath/index.html#e2) that is applied before publishing a value to MQTT.
* __commandTopic__: The MQTT topic that commands are send to. This can be empty, the thing channel will be read-only then. Transformations are not applied for sending data.
* __formatBeforePublish__: Format a value before it is published to the MQTT broker. The default is to just pass the channel/item state. If you want to apply a prefix, say "MYCOLOR,", you would use "MYCOLOR,%s". If you want to adjust the precision of a number to for example 4 digits, you would use "%.4f".
* __postCommand__: If the received MQTT value should not only update the state of linked items, but command them, enable this option. You usually need this enabled if your item is also linked to another channel, say a KNX actor, and you want a received MQTT payload to command that KNX actor. 
* __retained__: The value will be published to the command topic as retained message. A retained value stays on the broker and can even be seen by MQTT clients that are subscribing at a later point in time. 

### Channel Type "string"

* __allowedStates__: An optional comma separated list of allowed states. Example: "ONE,TWO,THREE"

You can connect this channel to a String item.

### Channel Type "number"

* __min__: An optional minimum value.
* __max__: An optional maximum value.
* __step__: For decrease, increase commands the step needs to be known

A decimal value (like 0.2) is send to the MQTT topic if the number has a fractional part.
If you always require an integer, please use the formatter.

You can connect this channel to a Number item.

### Channel Type "dimmer"
 
* __on__: A optional string (like "ON"/"Open") that is recognised as minimum.
* __off__: A optional string (like "OFF"/"Close") that is recognised as maximum.
* __min__: A required minimum value.
* __max__: A required maximum value.
* __step__: For decrease, increase commands the step needs to be known

The value is internally stored as a percentage for a value between **min** and **max**.

The channel will publish a value between `min` and `max`.

You can connect this channel to a Rollershutter or Dimmer item.

### Channel Type "contact", "switch"

* __on__: A optional number (like 1, 10) or a string (like "ON"/"Open") that is recognised as on/open state.
* __off__: A optional number (like 0, -10) or a string (like "OFF"/"Close") that is recognised as off/closed state.

The contact channel by default recognises `"OPEN"` and `"CLOSED"`. You can connect this channel to a Contact item.
The switch channel by default recognises `"ON"` and `"OFF"`. You can connect this channel to a Switch item.

If **on** and **off** are not configured it publishes the strings mentioned before respectively.

You can connect this channel to a Contact or Switch item.

### Channel Type "colorRGB", "colorHSB"

* __on__: An optional string (like "BRIGHT") that is recognised as on state. (ON will always be recognised.)
* __off__: An optional string (like "DARK") that is recognised as off state. (OFF will always be recognised.)
* __onBrightness__: If you connect this channel to a Switch item and turn it on,
color and saturation are preserved from the last state, but
the brightness will be set to this configured initial brightness (default: 10%).

You can connect this channel to a Color, Dimmer and Switch item.

This channel will publish the color as comma separated list to the MQTT broker,
e.g. "112,54,123" for an RGB channel (0-255 per component) and "360,100,100" for a HSB channel (0-359 for hue and 0-100 for saturation and brightness).

The channel expects values on the corresponding MQTT topic to be in this format as well.

### Channel Type "location"

You can connect this channel to a Location item.

The channel will publish the location as comma separated list to the MQTT broker,
e.g. "112,54,123" for latitude, longitude, altitude. The altitude is optional. 

The channel expects values on the corresponding MQTT topic to be in this format as well. 

### Channel Type "image"

You can connect this channel to an Image item. This is a read-only channel.

The channel expects values on the corresponding MQTT topic to contain the binary
data of a bmp, jpg, png or any other format that the installed java runtime supports. 

### Channel Type "datetime"

You can connect this channel to a DateTime item.

The channel will publish the date/time in the format "yyyy-MM-dd'T'HH:mm"
for example 2018-01-01T12:14:00. If you require another format, please use the formatter.

The channel expects values on the corresponding MQTT topic to be in this format as well. 

### Channel Type "rollershutter"

* __on__: An optional string (like "Open") that is recognised as UP state.
* __off__: An optional string (like "Close") that is recognised as DOWN state.
* __stop__: An optional string (like "Stop") that is recognised as STOP state.

You can connect this channel to a Rollershutter or Dimmer item.

## Rule Actions

This binding includes a rule action, which allows to publish MQTT messages from within rules.
There is a separate instance for each MQTT broker (i.e. bridge), which can be retrieved through

```
val mqttActions = getActions("mqtt","mqtt:systemBroker:embedded-mqtt-broker")
```

where the first parameter always has to be `mqtt` and the second (`mqtt:systemBroker:embedded-mqtt-broker`) is the Thing UID of the broker that should be used.
Once this action instance is retrieved, you can invoke the `publishMQTT(String topic, String value)` method on it:

```
mqttActions.publishMQTT("mytopic","myvalue")
```

## Limitations

* The HomeAssistant Fan Components only support ON/OFF.
* The HomeAssistant Cover Components only support OPEN/CLOSE/STOP.
* The HomeAssistant Light Component does not support XY color changes.
* The HomeAssistant Climate Components is not yet supported.

## Incoming Value Transformation

All mentioned channels allow an optional transformation for incoming MQTT topic values.

This is required if your received value is wrapped in a JSON or XML response.

Here are a few examples to unwrap a value from a complex response:

| Received value                                                      | Tr. Service | Transformation                            |
|---------------------------------------------------------------------|-------------|-------------------------------------------|
| `{device: {status: { temperature: 23.2 }}}`                         | JSONPATH    | `JSONPATH:$.device.status.temperature`    |
| `<device><status><temperature>23.2</temperature></status></device>` | XPath       | `XPath:/device/status/temperature/text()` |
| `THEVALUE:23.2°C`                                                   | REGEX       | `REGEX::(.*?)°`                           |

Transformations can be chained by separating them with the mathematical intersection character "∩".

## Outgoing Value Transformation

All mentioned channels allow an optional transformation for outgoing values.
Please prefer formatting as described in the next section whenever possible.

## Format before Publish

This feature is quite powerful in transforming an item state before it is published to the MQTT broker.
It has the syntax: `%[flags][width]conversion`.
Find the full documentation on the [Java](https://docs.oracle.com/javase/7/docs/api/java/util/Formatter.html) web page.

The default is "%s" which means: Output the item state as string.

Here are a few examples:

* All uppercase: "%S". Just use the upper case letter for the conversion argument.
* Apply a prefix: "myprefix%s"
* Apply a suffix: "%s suffix"
* Number precision: ".4f" for a 4 digit precision. Use the "+" flag to always add a sign: "+.4f".
* Decimal to Hexadecimal/Octal/Scientific: For example "60" with "%x", "%o", "%e" becomes "74", "3C", "60".
* Date/Time: To reference the item state multiple times, use "%1$". Use the "tX" conversion where "X" can be any of [h,H,m,M,I,k,l,S,p,B,b,A,a,y,Y,d,e].
  - For an output of *May 23, 1995* use "%1$**tb** %1$**te**,%1$**tY**".
  - For an output of *23.05.1995* use "%1$**td**.%1$**tm**.%1$**tY**".
  - For an output of *23:15* use "%1$**tH**:%1$**tM**".

## Troubleshooting

* If you get the error "No MQTT client": Please update your installation.
* If you use the Mosquitto broker: Please be aware that there is a relatively low setting
  for retained messages. At some point messages will just not being delivered
  anymore: Change the setting 

## Examples

Have a look at the following textual examples.

### A broker Thing with a Generic MQTT Thing and a few channels 

demo.Things:

```xtend
Bridge mqtt:broker:myUnsecureBroker [ host="192.168.0.42", secure=false ]
{
    Thing topic mything {
    Channels:
        Type switch : lamp "Kitchen Lamp" [ stateTopic="lamp/enabled", commandTopic="lamp/enabled/set" ]
        Type switch : fancylamp "Fancy Lamp" [ stateTopic="fancy/lamp/state", commandTopic="fancy/lamp/command", on="i-am-on", off="i-am-off" ]
        Type string : alarmpanel "Alarm system" [ stateTopic="alarm/panel/state", commandTopic="alarm/panel/set", allowedStates="ARMED_HOME,ARMED_AWAY,UNARMED" ]
        Type color : lampcolor "Kitchen Lamp color" [ stateTopic="lamp/color", commandTopic="lamp/color/set", rgb=true ]
        Type dimmer : blind "Blind" [ stateTopic="blind/state", commandTopic="blind/set", min=0, max=5, step=1 ]
    }
}
```

demo.items:

```xtend
Switch Kitchen_Light "Kitchen Light" { channel="mqtt:topic:myUnsecureBroker:mything:lamp" }
Rollershutter shutter "Blind" { channel="mqtt:topic:myUnsecureBroker:mything:blind" }
```

### Publish an MQTT value on startup

An example "demo.rules" rule to publish to `system/started` with the value `true` on every start:

```xtend
rule "Send startup message"
when
  System started
then
  val actions = getActions("mqtt","mqtt:broker:myUnsecureBroker")
  actions.publishMQTT("system/started","true")    
end
```

### Synchronise two instances

Define a broker and a trigger channel on that broker in a "demo.Things" file:

```xtend
Bridge mqtt:broker:myUnsecureBroker [ host="192.168.0.42", secure=false ]
{
    Channels:
        Type publishTrigger : myTriggerChannel "Receive everything" [ stateTopic="allItems/#", separator="#" ]
}
```

If you want to publish all item changes to an MQTT topic "allItems/",
group items into a `myGroupOfItems` and do this in a "publishAll.rules" file:

```xtend
rule "Publish all"
when 
      Member of myGroupOfItems changed
then
   val actions = getActions("mqtt","mqtt:broker:myUnsecureBroker")
   actions.publishMQTT("allItems/"+triggeringItem.name,triggeringItem.state)
end
```

If you want to receive all item changes from an MQTT topic "allItems/",
do this in a "ReceiveAll.rules" file:

```xtend
rule "Publish all"
when 
      Channel "mqtt:broker:myUnsecureBroker:myTriggerChannel" triggered
then
   // TODO
end
```

## Converting an MQTT1 installation

The conversion is straight forward, but need to be done for each item.
You do not need to convert everything in one go. MQTT1 and MQTT2 can coexist.

> For mqtt1 make sure you have enabled the Legacy 1.x repository and installed "mqtt1".

### 1 Command / 1 State topic 

Assume you have this item:

```xtend
Switch ExampleItem "Heatpump Power" { mqtt=">[mosquitto:heatpump/set:command:*:DEFAULT)],<[mosquitto:heatpump/state:JSONPATH($.power)]" }
```

This converts to an entry in your *.things file with a **Broker Thing** and a **Generic MQTT Thing** that uses the bridge:

```xtend
Bridge mqtt:broker:myUnsecureBroker [ host="192.168.0.42", secure=false ]
{
    Thing mqtt:topic:mything {
    Channels:
        Type switch : heatpumpChannel "Heatpump Power" [ stateTopic="heatpump", commandTopic="heatpump/set" transformationPattern="JSONPATH:$.power" ]
    }
}
```

Add as many channels as you have items and add the *stateTopic* and *commandTopic* accordingly. 

Your items change to:

```xtend
Switch ExampleItem "Heatpump Power" { channel="mqtt:myUnsecureBroker:topic:mything:heatpumpChannel" }
```


### 1 Command / 2 State topics 

If you receive updates from two different topics, you need to create multiple channels now, 1 for each MQTT receive topic.

```xtend
Switch ExampleItem "Heatpump Power" { mqtt=">[mosquitto:heatpump/set:command:*:DEFAULT)],<[mosquitto:heatpump/state1:state:*:DEFAULT",<[mosquitto:heatpump/state2:state:*:DEFAULT" }
```

This converts to:

```xtend
Bridge mqtt:broker:myUnsecureBroker [ host="192.168.0.42", secure=false ]
{
    Thing mqtt:topic:mything {
    Channels:
        Type switch : heatpumpChannel "Heatpump Power" [ stateTopic="heatpump/state1", commandTopic="heatpump/set" ]
        Type switch : heatpumpChannel2 "Heatpump Power" [ stateTopic="heatpump/state2" ]
    }
}
```

Link both channels to one item. That item will publish to "heatpump/set" on a change and
receive values from "heatpump/state1" and "heatpump/state2".

```xtend
Switch ExampleItem "Heatpump Power" { channel="mqtt:myUnsecureBroker:topic:mything:heatpumpChannel",
                                      channel="mqtt:myUnsecureBroker:topic:mything:heatpumpChannel2" }
```
# NTP Binding
 
The NTP binding is used for displaying the local date and time based update from an NTP server.
 
## Supported Things
 
This binding supports one ThingType: ntp
 
## Discovery
 
Discovery is used to place one default item in the inbox as a convenient way to add a Thing for the local time.
 
## Binding Configuration
 
The binding has no configuration options, all configuration is done at Thing level.
 
## Thing Configuration
 
The thing has a few configuration options:

| Option |  Description  |
|-----------------|--------------------------------------------------- |
| hostname | NTP host server, e.g. nl.pool.ntp.org |
| refreshInterval | Interval that new time updates are posted to the eventbus in seconds |
| refreshNtp | Number of updates between querying the NTP server (e.g. with refreshinterval = 60 (seconds) and refreshNtp = 30 the NTP server is queried each half hour. |
| timeZone | Timezone, can be left blank for using the default system one |
| locale | Locale, can be left blank for using the default system one |

 
## Channels
 
The ntp binding has two channels:

* `dateTime` which provides the data in a dateTime type
* `string` which provides the data in a string type. The string channel can be configured with the formatting of the date & time. This also allows proper representation of timezones other than the java machine default one.

See the [java documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html) for the detailed information on the formatting

 
 
## Full Example
 
Things:

```
ntp:ntp:demo  [ hostname="nl.pool.ntp.org", refreshInterval=60, refreshNtp=30 ]
```

Items:

```
DateTime Date  "Date [%1$tA, %1$td.%1$tm.%1$tY %1$tH:%1$tM]"  { channel="ntp:ntp:demo:dateTime" }
```
# OneWire Binding

The OneWire binding integrates OneWire (also spelled 1-Wire) devices. 
OneWire is a serial bus developed by Dallas Semiconductor.
It provides cheap sensors for temperature, humidity, digital I/O and more.
  
## Supported Things

### Bridges

Currently only one bridge is supported. 

The OneWire File System (OWFS, http://owfs.org) provides an abstraction layer between the OneWire bus and this binding. 
The `owserver` is the bridge that connects to an existing OWFS installation. 

### Things

There are different types of things: the generic ones (`counter2`, `digitalio`, `digitalio2`, `digitalio8`, `ibutton`, `temperature`), multisensors built around the DS1923/DS2438 chip (`ms-tx`) and more advanced sensors from Elaborated Networks (www.wiregate.de) (`ams`, `bms`) and Embedded Data System (`edsenv`). 

The thing types `ms-th`and `ms-tv` have been marked deprecated and will be updated to `ms-tx`automatically. 
Manually (via textual configuration) defined things should be changed to `ms-tx`. 

## Discovery

Discovery is supported for things. You have to add the bridges manually.  

## Thing Configuration

It is strongly recommended to use discovery and Paper UI for thing configuration.
Please note that:

* All things need a bridge.
* The sensor id parameter supports only the dotted format, including the family id (e.g. `28.7AA256050000`).
DS2409 MicroLAN couplers (hubs) are supported by adding their id and the branch (`main` or `aux`) in a directory-like format in front of the sensor id (e.g. `1F.EDC601000000/main/28.945042000000`).
* Refresh time is the minimum time in seconds between two checks of that thing.
It defaults to 300s for analog channels and 10s for digital channels.
* Some thing channels need additional configuration, please see below in the channels section.

### OWFS Bridge (`owserver`)

There are no configuration options for the owserver besides the network address.
It consists of two parts: `address` and `port`.

The `address` parameter is used to denote the location of the owserver instance. 
It supports both, a hostname or an IP address. 

The `port` parameter is used to adjust non-standard OWFS installations.
It defaults to `4304`, which is the default of each OWFS installation.  

Bridges of type `owserver` are extensible with channels of type `owfs-number` and `owfs-string`. 
  
### Counter (`counter2`)

The counter thing supports the DS2423 chip, a dual counter.
Two `counterX` channels are supported. 
`X` is either `0` or `1`.

It has two parameters: sensor id `id` and refresh time `refresh`.
 

### Digital I/O (`digitalio`, `digitalio2`, `digitalio8`) 

The digital I/O things support the DS2405, DS2406, DS2408 and DS2413 chips.
Depending on the chip, one (DS2405), two (DS2406/DS2413) or eight (DS2408) `digitalX`  channels are supported.
`X` is a number from `0` to `7`.

It has two parameters: sensor id `id` and refresh time `refresh`.

### iButton (`ibutton`)

The iButton thing supports only the DS2401 chips.
It is used for presence detection and therefore only supports the `present` channel.
It's value is `ON` if the device is detected on the bus and `OFF` otherwise.

It has two parameters: sensor id `id` and refresh time `refresh`.

### Multisensor (`ms-tx`)

The multisensor is build around the DS2438 or DS1923 chipset. 
It always provides a `temperature` channel.

Depnding on the actual sensor, additional channels (`current`, `humidity`, `light`, `voltage`, `supplyvoltage`) are added.
If the voltage input of the DS2438 is connected to a humidity sensor, several common types are supported (see below).

It has two parameters: sensor id `id` and refresh time `refresh`.

Known DS2438-base sensors are iButtonLink (https://www.ibuttonlink.com/) MS-T (recognized as generic DS2438), MS-TH, MS-TC, MS-TL, MS-TV.
Unknown multisensors are added as generic DS2438 and have `temperature`, `current`, `voltage` and `supplyvoltage` channels.

In case the sensor is not properly detected (e.g. because it is a self-made sensor), check if it is compatible with one of the sensors listed above. If so, the first byte of page 3 of the DS2438 needs to be set to the correct identification (0x00 = generic/MS-T, 0x19 = MS-TH, 0x1A = MS-TV, 0x1B = MS-TL, 0x1C = MS-TC). **Note: Updating the pages of a sensor can break other software. This is fully your own risk.** 

### Temperature sensor (`temperature`)

The temperature thing supports DS18S20, DS18B20 and DS1822 sensors.
It provides only the `temperature` channel.

It has two parameters: sensor id `id` and refresh time `refresh`. 

### Elaborated Networks Multisensors (`ams`, `bms`)

These things are complex devices from Elaborated networks. 
They consist of a DS2438 and a DS18B20 with additional circuitry on one PCB.
The AMS additionally has a second DS242438 and a DS2413 for digital I/O on-board.
Analog light sensors can optionally be attached to both sensors.

These sensors provide `temperature`, `humidity` and `supplyvoltage` channels.
If the light sensor is attached and configured, a `light` channel is provided, otherwise a `current` channel.
The AMS has an additional `voltage`and two `digitalX` channels.

It has two (`bms`) or four (`ams`) sensors.
The id parameter (`id`) has to be configured with the sensor id of the humidity sensor.

Additionally the refresh time `refresh` can be configured.
The AMS supports a `digitalrefresh` parameter for the refresh time of the digital channels.

Since both multisensors have two temperature sensors on-board, the `temperaturesensor` parameter allows to select `DS18B20` or `DS2438` to be used for temperature measurement.
This parameter has a default of `DS18B20` as this is considered more accurate.
The `temperature` channel is of type `temperature` if the internal sensor is used and of type `temperature-por-res` for the external DS18B20.

The last parameter is the `lightsensor` option to configure if an ambient light sensor is attached.
It defaults to `false`.
In that mode, a `current`  channel is provided.
If set to `true`, a `light` channel is added to the thing.
The correct formula for the ambient light is automatically determined from the sensor version.

### Embedded Data System Environmental sensors (`edsenv`)

This thing supports EDS0064, EDS0065, EDS0066 or EDS0067 sensors.
It has two parameters: sensor id `id` and refresh time `refresh`.

All things have a `temperature` channel.
Additional channels (`light`, `pressure`, `humidity`, `dewpoint`, `abshumidity`) will be added if available from the sensor automatically.


## Channels

| Type-ID             | Thing                      | Item                     | readonly   | Description                                        |
|---------------------|----------------------------|--------------------------|------------|----------------------------------------------------|
| absolutehumidity    | ms-tx, ams, bms, edsenv    | Number:Density           | yes        | absolute humidity                                  |
| current             | ms-tx, ams                 | Number:ElectricCurrent   | yes        | current                                            |
| counter             | counter2                   | Number                   | yes        | countervalue                                       |
| dewpoint            | ms-tx, ams, bms, edsenv    | Number:Temperature       | yes        | dewpoint                                           |
| dio                 | digitalX, ams              | Switch                   | no         | digital I/O, can be configured as input or output  |
| humidity            | ms-tx, ams, bms, edsenv    | Number:Dimensionless     | yes        | relative humidity                                  |
| humidityconf        | ms-tx                      | Number:Dimensionless     | yes        | relative humidity                                  |
| light               | ams, bms, edsenv           | Number:Illuminance       | yes        | lightness                                          |
| owfs-number         | owserver                   | Number                   | yes        | direct access to OWFS nodes                        |
| owfs-string         | owserver                   | String                   | yes        | direct access to OWFS nodes                        |
| present             | all                        | Switch                   | yes        | sensor found on bus                                |
| pressure            | edsenv                     | Number:Pressure          | yes        | environmental pressure                             |
| supplyvoltage       | ms-tx                      | Number:ElectricPotential | yes        | sensor supplyvoltage                               |
| temperature         | temperature, ms-tx, edsenv | Number:Temperature       | yes        | environmental temperature                          |
| temperature-por     | temperature                | Number:Temperature       | yes        | environmental temperature                          |
| temperature-por-res | temperature, ams, bms      | Number:Temperature       | yes        | environmental temperature                          |
| voltage             | ms-tx, ams                 | Number:ElectricPotential | yes        | voltage input                                      |

### Digital I/O (`dio`)

Channels of type `dio` channels each have two parameters: `mode` and `logic`.

The `mode` parameter is used to configure this channels as `input` or `output`.

The `logic` parameter can be used to invert the channel.
In `normal` mode the channel is considered `ON` for logic high, and `OFF` for logic low.
In `inverted` mode `ON` is logic low and `OFF` is logic high.

### Humidity (`humidity`, `humidityconf`, `abshumidity`, `dewpoint`)

Depending on the sensor, a `humidity` or `humidityconf` channel may be added.
This is only relevant for DS2438-based sensors of thing-type `ms-tx`.
`humidityconf`-type channels have the `humiditytype` parameter.
Possible options are `/humidity` for HIH-3610 sensors, `/HIH4000/humidity` for HIH-4000 sensors, `/HTM1735/humidity` for HTM-1735 sensors and `/DATANAB/humidity` for sensors from Datanab.

All humidity sensors also support `absolutehumidity` and `dewpoint`.

### OWFS Direct Access (`owfs-number`, `owfs-string`)

These channels allow direct access to OWFS nodes.
They have two configuration parameters: `path` and `refresh`.

The `path` parameter is mandatory and contains a full path inside the OWFS (e.g. `statistics/errors/CRC8_errors`).

The `refresh` parameter is the number of seconds between two consecutive (successful) reads of the node.
It defaults to 300s.

### Temperature (`temperature`, `temperature-por`, `temperature-por-res`)

There are three temperature channel types: `temperature`, `temperature-por`and `temperature-por-res`.
The correct channel-type is selected automatically by the thing handler depending on the sensor type.

If the channel-type is `temperature`, there is nothing else to configure.

Some sensors (e.g. DS18x20) report 85 °C as Power-On-Reset value.
In some installations this leads to errorneous temperature readings.
If the `ignorepor` parameter is set to `true` 85 °C values will be filtered.
The default is `false` as correct reading of 85 °C will otherwise be filtered, too.

A channel of type `temperature-por-res` has one parameter: `resolution`.
OneWire temperature sensors are capable of different resolutions: `9`, `10`, `11` and `12` bits.
This corresponds to 0.5 °C, 0.25 °C, 0.125 °C, 0.0625 °C respectively.
The conversion time is inverse to that and ranges from 95 ms to 750 ms.
For best performance it is recommended to set the resolution only as high as needed. 
 
## Full Example

** Attention: Adding channels with UIDs different from the ones mentioned in the thing description will not work and may cause problems.
Please use the pre-defined channel names only. **

This is the configuration for a OneWire network consisting of an owserver as bridge (`onewire:owserver:mybridge`) as well as a temperature sensor, a BMS and a 2-port Digital I/O as things (`onewire:temperature:mybridge:mysensor`, `onewire:bms:mybridge:mybms`, `onewire:digitalio2:mybridge:mydio`). 

### demo.things:

```
Bridge onewire:owserver:mybridge [ 
    network-address="192.168.0.51" 
    ] {
    
    Thing temperature mysensor [
        id="28.505AF0020000", 
        refresh=60
        ] {
            Channels:
                Type temperature-por-res : temperature [
                    resolution="11"
                ]
        } 
    
    Thing bms mybms [
        id="26.CD497C010000",
        refresh=60, 
        lightsensor=true, 
        temperaturesensor="DS18B20", 
        ] {
            Channels:
                Type temperature-por-res : temperature [
                    resolution="9"
                ]
        } 

    Thing digitalio2 mydio [
        id="3A.134E47DB60000"
        ] {
            Channels:
                Type dio : digital0 [
                    mode="input"
                ]
                Type dio : digital1 [
                    mode="output"
                ]
        }
        
    Channels:
        Type owfs-number : crc8errors [
            path="statistics/errors/CRC8_errors"
        ]
}
```

### demo.items:

```
Number:Temperature      MySensor    "MySensor [%.1f °C]"            { channel="onewire:temperature:mybridge:mysensor:temperature" }
Number:Temperature      MyBMS_T     "MyBMS Temperature [%.1f °F]"   { channel="onewire:bms:mybridge:mybms:temperature" }
Number:Dimensionless    MyBMS_H     "MyBMS Humidity [%.1f %unit%]"  { channel="onewire:bms:mybridge:mybms:humidity" }
Switch                  Digital0    "Digital 0"                     { channel="onewire:digitalio2:mybridge:mydio:digital0" }
Switch                  Digital1    "Digital 1"                     { channel="onewire:digitalio2:mybridge:mydio:digital1" }
Number                  CRC8Errors  "Bus-Errors [%d]"               { channel="onewire:owserver:mybridge:crc8errors" }
```

### demo.sitemap:

```
sitemap demo label="Main Menu"
{
    Frame {
        Text item=MySensor
        Text item=MyBMS_T
        Text item=MyBMS_H
        Text item=CRC8Errors
        Text item=Digital0
        Switch item=Digital1
    }
}
```
---
layout: documentation
---

{% include base.html %}

# OpenWeatherMap Binding

This binding integrates the [OpenWeatherMap weather API](https://openweathermap.org/api).

## Supported Things

There are three supported things.

### OpenWeatherMap Account

First one is a bridge `weather-api` which represents the OpenWeatherMap account.
The bridge holds the mandatory API key to access the OpenWeatherMap API and several global configuration parameters.
If your system language is supported by the OpenWeatherMap API it will be used as default language for the requested data.

### Current Weather And Forecast

The second thing `weather-and-forecast` supports the [current weather](https://openweathermap.org/current), [5 day / 3 hour forecast](https://openweathermap.org/forecast5) and optional [16 day / daily forecast](https://openweathermap.org/forecast16) services for a specific location.
It requires coordinates of the location of your interest.
You can add as many `weather-and-forecast` things for different locations to your setup as you like to observe.
**Attention**: The daily forecast is only available for [paid accounts](https://openweathermap.org/price).
The binding tries to request daily forecast data from the OpenWeatherMap API.
If the request fails, all daily forecast channel groups will be removed from the thing and further request will be omitted.

### Current UV Index And Forceast

The third thing `uvindex` supports the [current UV Index](https://openweathermap.org/api/uvi#current) and [forecasted UV Index](https://openweathermap.org/api/uvi#forecast) for a specific location.
It requires coordinates of the location of your interest.
You can add as much `uvindex` things for different locations to your setup as you like to observe.

## Discovery

If a system location is set, a "Local Weather And Forecast" (`weather-and-forecast`) thing and "Local UV Index" (`uvindex`) thing will be automatically discovered for this location.
Once the system location will be changed, the background discovery updates the configuration of both things accordingly.

## Thing Configuration

### OpenWeatherMap Account

| Parameter       | Description                                                                                                                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| apikey          | API key to access the OpenWeatherMap API. **Mandatory**                                                                                                                                                                                                                           |
| refreshInterval | Specifies the refresh interval (in minutes). Optional, the default value is 60, the minimum value is 10.                                                                                                                                                                          |
| language        | Language to be used by the OpenWeatherMap API. Optional, valid values are: `ar`, `bg`, `ca`, `de`, `el`, `en`, `es`, `fa`, `fi`, `fr`, `gl`, `hr`, `hu`, `it`, `ja`, `kr`, `la`, `lt`, `mk`,  `nl`, `pl`, `pt`, `ro`, `ru`, `sk`, `sl`, `sw`, `tr`, `ua`, `vi`, `zh_cn`, `zh_tw`. |

### Current Weather And Forecast

| Parameter      | Description                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------|
| location       | Location of weather in geographical coordinates (latitude/longitude/altitude). **Mandatory**                                   |
| forecastHours  | Number of hours for hourly forecast. Optional, the default value is 24 (min="0", max="120", step="3").                         |
| forecastDays   | Number of days for daily forecast (including todays forecast). Optional, the default value is 6 (min="0", max="16", step="1"). |

Once the parameters `forecastHours` or `forecastDays` will be changed, the available channel groups on the thing will be created or removed accordingly.

### Current UV INdex And Forecast

| Parameter      | Description                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------|
| location       | Location of weather in geographical coordinates (latitude/longitude/altitude). **Mandatory**                                   |
| forecastDays   | Number of days for UV Index forecast (including todays forecast). Optional, the default value is 6 (min="1", max="8", step="1"). |

Once the parameter `forecastDays` will be changed, the available channel groups on the thing will be created or removed accordingly.

## Channels

### Station

| Channel Group ID | Channel ID | Item Type | Description                                  |
|------------------|------------|-----------|----------------------------------------------|
| station          | id         | String    | Id of the weather station or the city.       |
| station          | name       | String    | Name of the weather station or the city.     |
| station          | location   | Location  | Location of the weather station or the city. |

### Current Weather

| Channel Group ID | Channel ID     | Item Type            | Description                                                             |
|------------------|----------------|----------------------|-------------------------------------------------------------------------|
| current          | time-stamp     | DateTime             | Time of data observation.                                               |
| current          | condition      | String               | Current weather condition.                                              |
| current          | condition-id   | String               | Id of the current weather condition. **Advanced**                       |
| current          | icon           | Image                | Icon representing the current weather condition.                        |
| current          | icon-id        | String               | Id of the icon representing the current weather condition. **Advanced** |
| current          | temperature    | Number:Temperature   | Current temperature.                                                    |
| current          | pressure       | Number:Pressure      | Current barometric pressure.                                            |
| current          | humidity       | Number:Dimensionless | Current atmospheric humidity.                                           |
| current          | wind-speed     | Number:Speed         | Current wind speed.                                                     |
| current          | wind-direction | Number:Angle         | Current wind direction.                                                 |
| current          | gust-speed     | Number:Speed         | Current gust speed. **Advanced**                                        |
| current          | cloudiness     | Number:Dimensionless | Current cloudiness.                                                     |
| current          | rain           | Number:Length        | Rain volume for the last three hours.                                   |
| current          | snow           | Number:Length        | Snow volume for the last three hours.                                   |

### 3 Hour Forecast

| Channel Group ID                                       | Channel ID     | Item Type            | Description                                                                |
|--------------------------------------------------------|----------------|----------------------|----------------------------------------------------------------------------|
| forecastHours03, forecastHours06, ... forecastHours120 | time-stamp     | DateTime             | Time of data forecasted.                                                   |
| forecastHours03, forecastHours06, ... forecastHours120 | condition      | String               | Forecast weather condition.                                                |
| forecastHours03, forecastHours06, ... forecastHours120 | condition-id   | String               | Id of the forecasted weather condition. **Advanced**                       |
| forecastHours03, forecastHours06, ... forecastHours120 | icon           | Image                | Icon representing the forecasted weather condition.                        |
| forecastHours03, forecastHours06, ... forecastHours120 | icon-id        | String               | Id fo the icon representing the forecasted weather condition. **Advanced** |
| forecastHours03, forecastHours06, ... forecastHours120 | temperature    | Number:Temperature   | Forecasted temperature.                                                    |
| forecastHours03, forecastHours06, ... forecastHours120 | pressure       | Number:Pressure      | Forecasted barometric pressure.                                            |
| forecastHours03, forecastHours06, ... forecastHours120 | humidity       | Number:Dimensionless | Forecasted atmospheric humidity.                                           |
| forecastHours03, forecastHours06, ... forecastHours120 | wind-speed     | Number:Speed         | Forecasted wind speed.                                                     |
| forecastHours03, forecastHours06, ... forecastHours120 | wind-direction | Number:Angle         | Forecasted wind direction.                                                 |
| forecastHours03, forecastHours06, ... forecastHours120 | gust-speed     | Number:Speed         | Forecasted gust speed. **Advanced**                                        |
| forecastHours03, forecastHours06, ... forecastHours120 | cloudiness     | Number:Dimensionless | Forecasted cloudiness.                                                     |
| forecastHours03, forecastHours06, ... forecastHours120 | rain           | Number:Length        | Expected rain volume for the next 3 hours.                                 |
| forecastHours03, forecastHours06, ... forecastHours120 | snow           | Number:Length        | Expected snow volume for the next 3 hours.                                 |

### Daily Forecast

| Channel Group ID                                                 | Channel ID      | Item Type            | Description                                                                |
|------------------------------------------------------------------|-----------------|----------------------|----------------------------------------------------------------------------|
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | time-stamp      | DateTime             | Date of data forecasted.                                                   |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | condition       | String               | Forecast weather condition.                                                |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | condition-id    | String               | Id of the forecasted weather condition. **Advanced**                       |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | icon            | Image                | Icon representing the forecasted weather condition.                        |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | icon-id         | String               | Id of the icon representing the forecasted weather condition. **Advanced** |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | min-temperature | Number:Temperature   | Minimum forecasted temperature of a day.                                   |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | max-temperature | Number:Temperature   | Maximum forecasted temperature of a day.                                   |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | pressure        | Number:Pressure      | Forecasted barometric pressure.                                            |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | humidity        | Number:Dimensionless | Forecasted atmospheric humidity.                                           |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | wind-speed      | Number:Speed         | Forecasted wind speed.                                                     |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | wind-direction  | Number:Angle         | Forecasted wind direction.                                                 |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | gust-speed      | Number:Speed         | Forecasted gust speed. **Advanced**                                        |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | cloudiness      | Number:Dimensionless | Forecasted cloudiness.                                                     |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | rain            | Number:Length        | Expected rain volume of a day.                                             |
| forecastToday, forecastTomorrow, forecastDay2, ... forecastDay16 | snow            | Number:Length        | Expected snow volume of a day.                                             |

### UV Index

| Channel Group ID                                          | Channel ID | Item Type | Description                    |
|-----------------------------------------------------------|------------|-----------|---------------------------------|
| current, forecastTomorrow, forecastDay2, ... forecastDay7 | time-stamp | DateTime  | Date of data observation / forecast.        |
| current, forecastTomorrow, forecastDay2, ... forecastDay7 | uvindex    | Number    | Current or forecasted UV Index. |

## Full Example

### Things

demo.things

```java
Bridge openweathermap:weather-api:api "OpenWeatherMap Account" [apikey="AAA", refreshInterval=30, language="de"] {
    Thing weather-and-forecast local "Local Weather And Forecast" [location="XXX,YYY", forecastHours=0, forecastDays=7]
    Thing weather-and-forecast miami "Weather And Forecast In Miami" [location="25.782403,-80.264563", forecastHours=24, forecastDays=0]
    Thing uvindex local "Local UV Index" [location="XXX,YYY", forecastDays=7]
}
```

### Items

demo.items

```java
String localStationId "ID [%s]" { channel="openweathermap:weather-and-forecast:api:local:station#id" }
String localStationName "Name [%s]" { channel="openweathermap:weather-and-forecast:api:local:station#name" }
Location localStationLocation "Location [%2$s°N %3$s°E]" <location> { channel="openweathermap:weather-and-forecast:api:local:station#location" }

DateTime localLastMeasurement "Timestamp of last measurement [%1$tY-%1$tm-%1$tdT%1$tH:%1$tM:%1$tS]" <time> { channel="openweathermap:weather-and-forecast:api:local:current#time-stamp" }
String localCurrentCondition "Current condition [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:local:current#condition" }
Image localCurrentConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:local:current#icon" }
Number:Temperature localCurrentTemperature "Current temperature [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:current#temperature" }
Number:Pressure localCurrentPressure "Current barometric pressure [%.1f %unit%]" <pressure> { channel="openweathermap:weather-and-forecast:api:local:current#pressure" }
Number:Dimensionless localCurrentHumidity "Current atmospheric humidity [%d %unit%]" <humidity> { channel="openweathermap:weather-and-forecast:api:local:current#humidity" }
Number:Speed localCurrentWindSpeed "Current wind speed [%.1f km/h]" <wind> { channel="openweathermap:weather-and-forecast:api:local:current#wind-speed" }
Number:Angle localCurrentWindDirection "Current wind direction [%d %unit%]" <wind> { channel="openweathermap:weather-and-forecast:api:local:current#wind-direction" }
Number:Dimensionless localCurrentCloudiness "Current cloudiness [%d %unit%]" <clouds> { channel="openweathermap:weather-and-forecast:api:local:current#cloudiness" }
Number:Length localCurrentRainVolume "Current rain volume [%.1f %unit%]" <rain> { channel="openweathermap:weather-and-forecast:api:local:current#rain" }
Number:Length localCurrentSnowVolume "Current snow volume [%.1f %unit%]" <snow> { channel="openweathermap:weather-and-forecast:api:local:current#snow" }

DateTime localDailyForecastTodayTimestamp "Timestamp of forecast [%1$tY-%1$tm-%1$td]" <time> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#time-stamp" }
String localDailyForecastTodayCondition "Condition for today [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#condition" }
Image localDailyForecastTodayConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:local:forecastToday#icon" }
Number:Temperature localDailyForecastTodayMinTemperature "Minimum temperature for today [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#min-temperature" }
Number:Temperature localDailyForecastTodayMaxTemperature "Maximum temperature for today [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#max-temperature" }
Number:Pressure localDailyForecastTodayPressure "Barometric pressure for today [%.1f %unit%]" <pressure> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#pressure" }
Number:Dimensionless localDailyForecastTodayHumidity "Atmospheric humidity for today [%d %unit%]" <humidity> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#humidity" }
Number:Speed localDailyForecastTodayWindSpeed "Wind speed for today [%.1f km/h]" <wind> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#wind-speed" }
Number:Angle localDailyForecastTodayWindDirection "Wind direction for today [%d %unit%]" <wind> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#wind-direction" }
Number:Dimensionless localDailyForecastTodayCloudiness "Cloudiness for today [%d %unit%]" <clouds> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#cloudiness" }
Number:Length localDailyForecastTodayRainVolume "Rain volume for today [%.1f %unit%]" <rain> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#rain" }
Number:Length localDailyForecastTodaySnowVolume "Snow volume for today [%.1f %unit%]" <snow> { channel="openweathermap:weather-and-forecast:api:local:forecastToday#snow" }

DateTime localDailyForecastTomorrowTimestamp "Timestamp of forecast [%1$tY-%1$tm-%1$td]" <time> { channel="openweathermap:weather-and-forecast:api:local:forecastTomorrow#time-stamp" }
String localDailyForecastTomorrowCondition "Condition for tomorrow [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:local:forecastTomorrow#condition" }
Image localDailyForecastTomorrowConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:local:forecastTomorrow#icon" }
Number:Temperature localDailyForecastTomorrowMinTemperature "Minimum temperature for tomorrow [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:forecastTomorrow#min-temperature" }
Number:Temperature localDailyForecastTomorrowMaxTemperature "Maximum temperature for tomorrow [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:forecastTomorrow#max-temperature" }
...

DateTime localDailyForecastDay2Timestamp "Timestamp of forecast [%1$tY-%1$tm-%1$td]" <time> { channel="openweathermap:weather-and-forecast:api:local:forecastDay2#time-stamp" }
String localDailyForecastDay2Condition "Condition in 2 days [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:local:forecastDay2#condition" }
Image localDailyForecastDay2ConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:local:forecastDay2#icon" }
Number:Temperature localDailyForecastDay2MinTemperature "Minimum temperature in 2 days [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:forecastDay2#min-temperature" }
Number:Temperature localDailyForecastDay2MaxTemperature "Maximum temperature in 2 days [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:local:forecastDay2#max-temperature" }
...

String miamiCurrentCondition "Current condition in Miami [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:miami:current#condition" }
Image miamiCurrentConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:miami:current#icon" }
Number:Temperature miamiCurrentTemperature "Current temperature in Miami [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:miami:current#temperature" }
...

String miamiHourlyForecast03Condition "Condition in Miami for the next three hours [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:miami:forecastHours03#condition" }
Image miamiHourlyForecast03ConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:miami:forecastHours03#icon" }
Number:Temperature miamiHourlyForecast03Temperature "Temperature in Miami for the next three hours [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:miami:forecastHours03#temperature" }
...
String miamiHourlyForecast06Condition "Condition in Miami for hours 3 to 6 [%s]" <sun_clouds> { channel="openweathermap:weather-and-forecast:api:miami:forecastHours06#condition" }
Image miamiHourlyForecast06ConditionIcon "Icon" { channel="openweathermap:weather-and-forecast:api:miami:forecastHours06#icon" }
Number:Temperature miamiHourlyForecast06Temperature "Temperature in Miami for hours 3 to 6 [%.1f %unit%]" <temperature> { channel="openweathermap:weather-and-forecast:api:miami:forecastHours06#temperature" }
...

DateTime localCurrentUVIndexTimestamp "Timestamp of last measurement [%1$tY-%1$tm-%1$td]" <time> { channel="openweathermap:uvindex:api:local:current#timestamp" }
Number localCurrentUVIndex "Current UV Index [%d]" { channel="openweathermap:uvindex:api:local:current#uvindex" }

DateTime localForecastTomorrowUVIndexTimestamp "Timestamp of forecast [%1$tY-%1$tm-%1$td]" <time> { channel="openweathermap:uvindex:api:local:forecastTomorrow#timestamp" }
Number localForecastTomorrowUVIndex "UV Index for tomorrow [%d]" { channel="openweathermap:uvindex:api:local:forecastTomorrow#uvindex" }
...
```

### Sitemap

demo.sitemap

```perl
sitemap demo label="OpenWeatherMap" {
    Frame label="Local Weather Station" {
        Text item=localStationId
        Text item=localStationName
        Mapview item=localStationLocation
    }
    Frame label="Current local weather" {
        Text item=localLastMeasurement
        Text item=localCurrentCondition
        Image item=localCurrentConditionIcon
        Text item=localCurrentTemperature
        Text item=localCurrentPressure
        Text item=localCurrentHumidity
        Text item=localCurrentWindSpeed
        Text item=localCurrentWindDirection
        Text item=localCurrentCloudiness
        Text item=localCurrentRainVolume
        Text item=localCurrentSnowVolume
    }
    Frame label="Local forecast for today" {
        Text item=localDailyForecastTodayTimestamp
        Text item=localDailyForecastTodayCondition
        Image item=localDailyForecastTodayConditionIcon
        Text item=localDailyForecastTodayMinTemperature
        Text item=localDailyForecastTodayMaxTemperature
        Text item=localDailyForecastTodayPressure
        Text item=localDailyForecastTodayHumidity
        Text item=localDailyForecastTodayWindSpeed
        Text item=localDailyForecastTodayWindDirection
        Text item=localDailyForecastTodayCloudiness
        Text item=localDailyForecastTodayRainVolume
        Text item=localDailyForecastTodaySnowVolume
    }
    Frame label="Local forecast for tomorrow" {
        Text item=localDailyForecastTomorrowTimestamp
        Text item=localDailyForecastTomorrowCondition
        Image item=localDailyForecastTomorrowConditionIcon
        Text item=localDailyForecastTomorrowMinTemperature
        Text item=localDailyForecastTomorrowMaxTemperature
        ...
    }
    Frame label="Local forecast in 2 days" {
        Text item=localDailyForecastDay2Timestamp
        Text item=localDailyForecastDay2Condition
        Image item=localDailyForecastDay2ConditionIcon
        Text item=localDailyForecastDay2MinTemperature
        Text item=localDailyForecastDay2MaxTemperature
        ...
    }
    Frame label="Current weather in Miami" {
        Text item=miamiCurrentCondition
        Image item=miamiCurrentConditionIcon
        Text item=miamiCurrentTemperature
        ...
    }
    Frame label="Forecast in Miami for the next three hours" {
        Text item=miamiHourlyForecast03Condition
        Image item=miamiHourlyForecast03ConditionIcon
        Text item=miamiHourlyForecast03Temperature
        ...
    }
    Frame label="Forecast weather in Miami for the hours 3 to 6" {
        Text item=miamiHourlyForecast06Condition
        Image item=miamiHourlyForecast06ConditionIcon
        Text item=miamiHourlyForecast06Temperature
        ...
    }
    Frame label="UV Index" {
        Text item=localCurrentUVIndexTimestamp
        Text item=localCurrentUVIndex
        Text item=localForecastTomorrowUVIndexTimestamp
        Text item=localForecastTomorrowUVIndex
        ...
    }
}
```
# Serial Button Binding

This is a binding for probably one of the simplest devices possible: A simple push button which short-cuts two pins on a serial port.

## Supported Things

The binding defines a single thing type called `button`.

A button requires the single configuration parameter `port`, which specifies the serial port that should be used. 

The only available channel is a `SYSTEM_RAWBUTTON` channel called `button`, which emits `PRESSED` events (no `RELEASED` events though) whenever data is available on the serial port (which will be read and discarded).

The use case is simple: Connect any push button to pins 2 and 7 of an RS-232 interface as short-cutting those will signal that data is available.
Using the default toggle profile, this means that you can use this channel to toggle any Switch item through the button.

## Full Example

demo.things:

```
serialbutton:button:mybutton "My Button" [ port="/dev/ttyS0" ]
```

demo.items:

```
Switch MyLight { channel="serialbutton:button:mybutton:button" }
```

_Note:_ This is a trigger channel, so you will most likely bind a second (state) channel to your item, which will control your physical light, so you might end up with the following, if you want to use your button with a Hue bulb:

```
Switch MyLight { channel="hue:0210:1:bulb1:color,serialbutton:button:mybutton:button" }
```

demo.sitemap:

```
sitemap demo label="Main Menu"
{
    Frame {
        Switch item=MyLight label="My Light"
    }
}
```
# Sonos Binding

This binding integrates the [Sonos Multi-Room Audio system](http://www.sonos.com).

**Attention:** 
You might run into trouble if your control system (the binding) is in another subnet than your Sonos device. 
Sonos devices make use of multicast which in most cases needs additional router configuration outside of a single subnet.   
If you observe communication errors (COMMUNICATION_ERROR/not registered), you might need to configure your router to increase the TTL of the packets send by your Sonos device. 
This happens because of a TTL=1 for ALIVE packets send by Sonos devices, resulting in dropped packets after one hop.

## Supported Things

All available Sonos (playback) devices are supported by this binding. This includes the One, Play:1, Play:3, Play:5, Connect, Connect:Amp, Playbar, Playbase, Beam and Sub. The Bridge and Boost are not supported, but these devices do only have an auxiliary role in the Sonos network and do not have any playback capability. All supported Sonos devices are registered as an audio sink in the framework.

When being defined in a \*.things file, the specific thing types One, PLAY1, PLAY3, PLAY5, PLAYBAR, PLAYBASE, Beam, CONNECT and CONNECTAMP should be used.

Please note that these thing types are case sensitive (you need to define them in upper case).

## Discovery

The Sonos devices are discovered through UPnP in the local network and all devices are put in the Inbox. Beware that all Sonos devices have to be added to the local Sonos installation as described in the Sonos setup procedure, e.g. through the Sonos Controller software or smartphone app.

## Binding Configuration

The binding has the following configuration options, which can be set for "binding:sonos":

| Parameter   | Name             | Description                                                              | Required |
|-------------|------------------|--------------------------------------------------------------------------|----------|
| opmlUrl     | OPML Service URL | URL for the OPML/tunein.com service                                      | no       |
| callbackUrl | Callback URL     | URL to use for playing notification sounds, e.g. http://192.168.0.2:8080 | no       |

## Thing Configuration

The Sonos Thing requires the UPnP UDN (Unique Device Name) as a configuration value in order for the binding to know how to access it.
All the Sonos UDN have the "RINCON_000E58D8403A0XXXX" format.
Additionally, a refresh interval, used to poll the Sonos device, can be specified (in seconds).
You can use the `notificationVolume` property for setting a default volume (in percent) to be used to play notifications.
In the thing file, this looks e.g. like

```
Thing sonos:PLAY1:1 [udn="RINCON_000E58D8403A0XXXX", refresh=60, notificationVolume=25]
```

## Channels

The devices support the following channels:

| Channel Type ID     | Item Type | Access Mode | Description                                                                                                                                               | Thing types                          |
|---------------------|-----------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| add                 | String    | W           | Add the given Zone Player to the group of this Zone Player                                                                                                | all                                  |
| alarm               | Switch    | W           | Set the first occurring alarm either ON or OFF. Alarms first have to be defined through the Sonos Controller app                                          | all                                  |
| alarmproperties     | String    | R           | Properties of the alarm currently running                                                                                                                 | all                                  |
| alarmrunning        | Switch    | R           | Set to ON if the alarm was triggered                                                                                                                      | all                                  |
| clearqueue          | Switch    | W           | Suppress all songs from the current queue                                                                                                                 | all                                  |
| control             | Player    | RW          | Control the Zone Player, e.g. start/stop/next/previous/ffward/rewind                                                                                      | all                                  |
| coordinator         | String    | R           | UDN of the coordinator for the current group                                                                                                              | all                                  |
| currentalbum        | String    | R           | Name of the album currently playing                                                                                                                       | all                                  |
| currentalbumart     | Image     | R           | Cover art of the album currently playing                                                                                                                  | all                                  |
| currentalbumarturl  | String    | R           | Cover art URL of the album currently playing                                                                                                              | all                                  |
| currentartist       | String    | R           | Name of the artist currently playing                                                                                                                      | all                                  |
| currenttitle        | String    | R           | Title of the song currently playing                                                                                                                       | all                                  |
| currenttrack        | String    | R           | Name of the current track or radio station currently playing                                                                                              | all                                  |
| currenttrackuri     | String    | R           | URI of the current track                                                                                                                                  | all                                  |
| currenttransporturi | String    | R           | URI of the current AV transport                                                                                                                           | all                                  |
| favorite            | String    | W           | Play the given favorite entry. The favorite entry has to be predefined in the Sonos Controller app                                                        | all                                  |
| led                 | Switch    | RW          | Set or get the status of the white led on the front of the Zone Player                                                                                    | all                                  |
| linein              | Switch    | R           | Indicator set to ON when the line-in of the Zone Player is connected                                                                                      | PLAY5, CONNECT, CONNECTAMP, PLAYBASE |
| localcoordinator    | Switch    | R           | Indicator set to ON if the this Zone Player is the Zone Group Coordinator                                                                                 | all                                  |
| mute                | Switch    | RW          | Set or get the mute state of the master volume of the Zone Player                                                                                         | all                                  |
| nightmode           | Switch    | RW          | Enable or disable the night mode feature                                                                                                                  | PLAYBAR, PLAYBASE, Beam              |
| notificationsound   | String    | W           | Play a notification sound by a given URI                                                                                                                  | all                                  |
| playlinein          | String    | W           | This channel supports playing the audio source connected to the line-in of the zoneplayer identified by the Thing UID or UPnP UDN provided by the String. | PLAY5, CONNECT, CONNECTAMP, PLAYBAR, PLAYBASE, Beam |
| playlist            | String    | W           | Play the given playlist. The playlist has to predefined in the Sonos Controller app                                                                       | all                                  |
| playqueue           | Switch    | W           | Play the songs from the current queue                                                                                                                     | all                                  |
| playtrack           | Number    | W           | Play the given track number from the current queue                                                                                                        | all                                  |
| playuri             | String    | W           | Play the given URI                                                                                                                                        | all                                  |
| publicaddress       | Switch    | W           | Put all Zone Players in one group, and stream audio from the line-in from the Zone Player that triggered the command                                      | all                                  |
| radio               | String    | W           | Play the given radio station. The radio station has to be predefined in the Sonos Controller app                                                          | all                                  |
| remove              | String    | W           | Remove the given Zone Player from the group of this Zone Player                                                                                           | all                                  |
| repeat              | String    | RW          | Repeat the track or queue playback. The accepted values are OFF, ONE and ALL                                                                              | all                                  |
| restore             | Switch    | W           | Restore the state of the Zone Player                                                                                                                      | all                                  |
| restoreall          | Switch    | W           | Restore the state of all the Zone Players                                                                                                                 | all                                  |
| save                | Switch    | W           | Save the state of the Zone Player                                                                                                                         | all                                  |
| saveall             | Switch    | W           | Save the state of all the Zone Players                                                                                                                    | all                                  |
| shuffle             | Switch    | RW          | Shuffle the queue playback                                                                                                                                | all                                  |
| sleeptimer          | Number    | RW          | Set/show the duration of the SleepTimer in seconds                                                                                                        | all                                  |
| snooze              | Number    | W           | Snooze the running alarm, if any, with the given number of minutes                                                                                        | all                                  |
| speechenhancement   | Switch    | RW          | Enable or disable the speech enhancement feature                                                                                                          | PLAYBAR, PLAYBASE, Beam              |
| standalone          | Switch    | W           | Make the Zone Player leave its Group and become a standalone Zone Player                                                                                  | all                                  |
| state               | String    | R           | The State channel contains state of the Zone Player, e.g. PLAYING, STOPPED, ...                                                                           | all                                  |
| stop                | Switch    | W           | Write `ON` to this channel: Stops the Zone Player player.                                                                                                 | all                                  |
| tuneinstationid     | String    | RW          | Provide the current TuneIn station id or play the TuneIn radio given by its station id                                                                    | all                                  |
| volume              | Dimmer    | RW          | Set or get the master volume of the Zone Player                                                                                                           | all                                  |
| zonegroupid         | String    | R           | Id of the Zone Group the Zone Player belongs to                                                                                                           | all                                  |
| zonename            | String    | R           | Name of the Zone associated to the Zone Player                                                                                                            | all                                  |

## Audio Support

All supported Sonos devices are registered as an audio sink in the framework.
Audio streams are treated as notifications, i.e. they are fed into the `notificationsound` channel.
The `notificationsound` channel change the volume of the audio sink to the value defined in the `notificationVolume` property of the thing and restores it after finished playing.
Note that the Sonos binding has a limit of 20 seconds for notification sounds.
Any sound that is longer than that will be cut off.

URL audio streams (e.g. an Internet radio stream) are an exception and do not get sent to the `notificationsound` channel.
Instead, these will be sent to the `playuri` channel.

## Full Example

demo.things:

```
Thing sonos:PLAY1:living [ udn="RINCON_000E58D8403A0XXXX", refresh=60]
```

demo.items:

```
Group Sonos <player>

Player Sonos_Controller   "Controller"                          (Sonos) {channel="sonos:PLAY1:living:control"}
Dimmer Sonos_Volume       "Volume [%.1f %%]" <soundvolume>      (Sonos) {channel="sonos:PLAY1:living:volume"}
Switch Sonos_Mute         "Mute"             <soundvolume_mute> (Sonos) {channel="sonos:PLAY1:living:mute"}
Switch Sonos_LED          "LED"              <switch>           (Sonos) {channel="sonos:PLAY1:living:led"}
String Sonos_CurrentTrack "Now playing [%s]" <text>             (Sonos) {channel="sonos:PLAY1:living:currenttrack"}
String Sonos_State        "Status [%s]"      <text>             (Sonos) {channel="sonos:PLAY1:living:state"}
```

demo.sitemap:

```
sitemap demo label="Main Menu"
{
		Frame label="Sonos" {
			Default item=Sonos_Controller
			Slider  item=Sonos_Volume
			Switch  item=Sonos_Mute
			Switch  item=Sonos_LED
			Text    item=Sonos_CurrentTrack		
			Text    item=Sonos_State
		}
}
```
# SonyAudio Binding

This binding integrates the [Sony Audio Control API](https://developer.sony.com/develop/audio-control-api/).

## Supported Things

For the moment the devices that are supported by this binding are
 * STR-DN1080
 * HT-CT800
 * SRS-ZR5
 * HT-ST5000
 * HT-Z9F
 * HT-ZF9
 * HT-MT500

When being defined in a \*.things file, the specific thing types
STR-DN1080, HT-ST5000, HT-ZF9, HT-Z9F, HT-CT800, HT-MT500 and SRS-ZR5 should be used.

Please note that these thing types are case sensitive (you need to define them in upper case).

## Discovery

The SonyAudio devices are discovered through UPnP in the local network and all devices are put in the Inbox.

## Thing Configuration

The SonyAudio Thing requires the network address, port and path as a configuration value in order for the binding to know how to access the device.
Additionally, a refresh interval, used to poll the Sony Audio device, can be specified (in seconds).

```
Thing sonyaudio:HT-ST5000:1 [ipAddress="192.168.123.123", port=10000, path="/sony", refresh=60]
```

## Channels

The devices support the following channels:

| Channel Type ID            | Item Type | Access Mode | Description                                                                           | Thing types                                            |
|----------------------------|-----------|-------------|---------------------------------------------------------------------------------------|--------------------------------------------------------|
| power                      | Switch    | RW          | Main power on/off                                                                     | HT-CT800, SRS-ZR5, HT-ST5000, HT-ZF9, HT-Z9F, HT-MT500 |
| input                      | String    | RW          | Set or get the input source                                                           | HT-CT800, SRS-ZR5, HT-ST5000, HT-ZF9, HT-Z9F, HT-MT500 |
| volume                     | Dimmer    | RW          | Set or get the master volume                                                          | HT-CT800, SRS-ZR5, HT-ST5000, HT-ZF9, HT-Z9F, HT-MT500 |
| mute                       | Switch    | RW          | Set or get the mute state of the master volume                                        | HT-CT800, SRS-ZR5, HT-ST5000, HT-ZF9, HT-Z9F, HT-MT500 |
| soundField                 | String    | RW          | Sound field                                                                           | HT-CT800, SRS-ZR5, HT-ST5000, HT-ZF9, HT-Z9F, HT-MT500 |
| master#power               | Switch    | RW          | Main power on/off                                                                     | STR-1080                                               |
| master#soundField          | String    | RW          | Sound field                                                                           | STR-1080                                               |
| zone1#power                | Switch    | RW          | Power for zone1 for devices supporting multizone                                      | STR-1080                                               |
| zone1#input                | String    | RW          | Set or get the input source for zone1 for devices supporting multizone                | STR-1080                                               |
| zone1#volume               | Dimmer    | RW          | Set or get the zone1 volume for devices supporting multizone                          | STR-1080                                               |
| zone1#mute                 | Switch    | RW          | Set or get the mute state for zone1 volume                                            | STR-1080                                               |
| zone2#power                | Switch    | RW          | Power for zone2 for devices supporting multizone                                      | STR-1080                                               |
| zone2#input                | String    | RW          | Set or get the input source for zone2 for devices supporting multizone                | STR-1080                                               |
| zone2#volume               | Dimmer    | RW          | Set or get the zone2 volume for devices supporting multizone                          | STR-1080                                               |
| zone2#mute                 | Switch    | RW          | Set or get the mute state for zone2 volume                                            | STR-1080                                               |
| zone3#power                | Switch    | RW          | Power for zone3 for devices supporting multizone                                      | none                                                   |
| zone3#input                | String    | RW          | Set or get the input source for zone3 for devices supporting multizone                | none                                                   |
| zone3#volume               | Dimmer    | RW          | Set or get the zone3 volume for devices supporting multizone                          | none                                                   |
| zone3#mute                 | Switch    | RW          | Set or get the mute state for zone3 volume                                            | none                                                   |
| zone4#power                | Switch    | RW          | Power for zone4 for devices supporting multizone                                      | STR-1080                                               |
| zone4#input                | String    | RW          | Set or get the input source for zone4 for devices supporting multizone                | STR-1080                                               |
| zone4#volume               | Dimmer    | RW          | Set or get the zone4 volume for devices supporting multizone                          | STR-1080                                               |
| zone4#mute                 | Switch    | RW          | Set or get the mute state for zone4 volume                                            | STR-1080                                               |
| radio#broadcastFreq        | Number    | R           | Current radio frequency                                                               | STR-1080                                               |
| radio#broadcastStation     | Number    | RW          | Set or get current preset radio station                                               | STR-1080                                               |
| radio#broadcastSeekStation | String    | W           | Seek for new broadcast station, forward search "fwdSeeking" and backward "bwdSeeking" | STR-1080                                               |


## Full Example

demo.things:

```
Thing sonyaudio:HT-ST5000:living [ipAddress="192.168.123.123"]
```

demo.items:

```
Group  SonyAudio <sonyaudio>

Dimmer Sony_Volume       "Volume [%.0f %%]"  <soundvolume>      (SonyAudio) {channel="sonyaudio:HT-ST5000:living:volume"}
Switch Sony_Mute         "Mute"              <soundvolume_mute> (SonyAudio) {channel="sonyaudio:HT-ST5000:living:mute"}
String Sony_Sound_Field  "Sound Field: [%s]" <text>             (SonyAudio) {channel="sonyaudio:HT-ST5000:living:master#soundField"}
```

demo.sitemap:

```
sitemap demo label="Main Menu" {
    Frame label="Sony" {
        Text label="Volume" icon="soundvolume" {
            Slider item=Sony_Volume
            Switch item=Sony_Mute
        }
        Text item=Sony_Sound_Field
    }
}
```
# TRÅDFRI Binding

This binding integrates the IKEA TRÅDFRI gateway and devices connected to it (such as dimmable LED bulbs).

## Supported Things

Beside the gateway (thing type "gateway"), the binding currently supports colored bulbs, dimmable warm white bulbs as well as white spectrum bulbs and control outlets.
The binding also supports read-only data from remote controls and motion sensors (e.g. the battery status).
The TRÅDFRI controller and sensor devices currently cannot be observed right away.
We assume that they are communicating directly with the bulbs or lamps without routing their commands through the gateway.
This makes it nearly impossible to trigger events for pressed buttons.
We only can access some static data like the present status or battery level. 

The thing type ids are defined according to the lighting devices defined for ZigBee LightLink ([see page 24, table 2](https://www.nxp.com/documents/user_manual/JN-UG-3091.pdf).
These are:

| Device type                     | ZigBee Device ID | Thing type |
|---------------------------------|------------------|------------|
| Dimmable Light                  | 0x0100           | 0100       |
| Colour Temperature Light        | 0x0220           | 0220       |
| Extended Colour Light           | 0x0210           | 0210       |
| Occupancy Sensor                | 0x0107           | 0107       |
| Non-Colour Controller           | 0x0820           | 0820       |
| Non-Colour Scene Controller     | 0x0830           | 0830       |
| Control Outlet                  | 0x0010           | 0010       |

The following matrix lists the capabilities (channels) for each of the supported lighting device types:

| Thing type  | Brightness | Color | Color Temperature | Battery Level | Battery Low | Power |
|-------------|:----------:|:-----:|:-----------------:|:-------------:|:-----------:|:-----:|
|  0010       |            |       |                   |               |             |   X   |
|  0100       |     X      |       |                   |               |             |       |
|  0220       |     X      |       |         X         |               |             |       |
|  0210       |            |   X   |         X         |               |             |       |
|  0107       |            |       |                   |       X       |      X      |       |
|  0820       |            |       |                   |       X       |      X      |       |
|  0830       |            |       |                   |       X       |      X      |       |

## Thing Configuration

For first pairing - the gateway requires a `host` parameter for the hostname or IP address and a `code`, which is the security code that is printed on the bottom of the gateway.
Optionally, a `port` can be configured, but any standard gateway uses the default port 5684.

The `code` is used during the initialization for retrieving unique identity and pre-shared key from the gateway (fw version 1.2.0042 onwards) and then it's discarded from the configuration. The newly created authentication data is stored in advanced parameters `identity` and `preSharedKey`.
On each initialization if the code is present in the thing configuration - the `identity` and `preSharedKey` are recreated and the `code` is again discarded.

The devices require only a single (integer) parameter, which is their instance id. Unfortunately, this is not displayed anywhere in the IKEA app, but it seems that they are sequentially numbered starting with 65537 for the first device. If in doubt, use the auto-discovered things to find out the correct instance ids.

## Channels

The dimmable bulbs support the `brightness` channel.
The white spectrum bulbs additionally also support the `color_temperature` channel. 

Full color bulbs support the `color_temperature` and `color` channels.
Brightness can be changed with the `color` channel.

The remote control and the motion sensor supports the `battery_level` and `battery_low` channels for reading the battery status.

The control outlet supports the 'power' channel.

Refer to the matrix above.

| Channel Type ID   | Item Type | Description                                      |
|-------------------|-----------|--------------------------------------------------|
| brightness        | Dimmer    | The brightness of the bulb in percent            |
| color_temperature | Dimmer    | color temperature from 0% = cold to 100% = warm  |
| color             | Color     | full color                                       |
| battery_level     | Number    | battery level (in %)                             |
| battery_low       | Switch    | battery low warning (<=10% = ON, >10% = OFF)     |
| power             | Switch    | power switch                                     |

## Full Example

demo.things:

```
Bridge tradfri:gateway:mygateway [ host="192.168.0.177", code="EHPW5rIJKyXFgjH3" ] {
    0100 myDimmableBulb "My Dimmable Bulb" [ id=65537 ]    
    0220 myColorTempBulb "My Color Temp Bulb" [ id=65538 ]
    0210 myColorBulb "My Color Bulb" [ id=65539 ]
    0830 myRemoteControl "My Remote Control" [ id=65545 ]
    0010 myControlOutlet "My Control Outlet" [ id=65542 ]
}
```

demo.items:

```
Dimmer Light1 { channel="tradfri:0100:mygateway:myDimmableBulb:brightness" }
Dimmer Light2_Brightness { channel="tradfri:0220:mygateway:myColorTempBulb:brightness" }
Dimmer Light2_ColorTemperature { channel="tradfri:0220:mygateway:myColorTempBulb:color_temperature" }
Color ColorLight { channel="tradfri:0210:mygateway:myColorBulb:color" }
Number RemoteControlBatteryLevel { channel="tradfri:0830:mygateway:myRemoteControl:battery_level" } 
Switch RemoteControlBatteryLow { channel="tradfri:0830:mygateway:myRemoteControl:battery_low" }
Switch ControlOutlet { channel="tradfri:0010:mygateway:myControlOutlet:power" }
```

demo.sitemap:

```
sitemap demo label="Main Menu"
{
    Frame {
        Slider item=Light1 label="Light1 Brightness [%.1f %%]"
        Slider item=Light2_Brightness label="Light2 Brightness [%.1f %%]"
        Slider item=Light2_ColorTemperature label="Light2 Color Temperature [%.1f %%]"
        Colorpicker item=ColorLight label="Color"
        Text item=RemoteControlBatteryLevel label="Battery level [%d %%]"
        Switch item=RemoteControlBatteryLow label="Battery low warning"
        Switch item=ControlOutlet label="Power Switch"
    }
}
```
---
layout: documentation
---

{% include base.html %}

# WeatherUnderground Binding

This binding uses the [Weather Underground service](https://www.wunderground.com/weather/api/) for providing weather information for any location worldwide.

The Weather Underground API is provided by The Weather Underground, LLC (WUL) free of charge but there is a daily limit and minute rate limit to the number of requests that can be made to the API for free (until 2018/12/31).
WUL will monitor your daily usage of the API to determine if you have exceeded the free-use threshold by using an API key. You may exceed this threshold only if you are or become a fee paying subscriber.
By using this binding, you confirm that you agree with the [Weather Underground API terms and conditions of use](https://www.wunderground.com/weather/api/d/terms.html).

To use this binding, you first need to [register and get your API key](https://www.wunderground.com/weather/api/d/pricing.html) .

## Supported Things

There are exactly two supported thing types. The first one is the bridge thing, which represents the connection to the Weather Underground service through the API key. It has the id `bridge`. The second one is the weather thing, which represents the weather information for an observed location. It has the id `weather`.  Each `weather` thing uses a `bridge` thing ; it cannot be set online if no `bridge` thing is defined.

## Discovery

If a system location is set, "Local Weather" will be automatically discovered for this location.

If the system location is changed, the background discovery updates the configuration of "Local Weather" automatically.

If a bridge is correctly configured, the discovered thing will automatically go online. 

## Binding Configuration

The binding has no configuration options, all configuration is done at Thing and Channel levels.

## Thing Configuration

The bridge only has one configuration parameter:

| Parameter | Description                                                              |
|-----------|------------------------------------------------------------------------- |
| apikey    | API key to access the Weather Underground service. Mandatory.            |

The thing has a few configuration parameters:

| Parameter | Description                                                              |
|-----------|------------------------------------------------------------------------- |
| location  | Location to be considered by the Weather Underground service. Mandatory. |
| language  | Language to be used by the Weather Underground service. Optional, the default is to use the language from the system locale. |
| refresh   | Refresh interval in minutes. Optional, the default value is 30 minutes and the minimum value is 5 minutes.  |

For the location parameter, different syntaxes are possible:

| Syntax                  | Example          |
|-------------------------|----------------- |
| US state/city           | CA/San_Francisco |
| US zipcode              | 60290            |
| country/city            | Australia/Sydney |
| latitude,longitude      | 37.8,-122.4      |
| airport code            | KJFK             |
| PWS id                  | pws:KCASANFR70   |

It can happen that the service is not able to determine the station to use, for example when you select as location a city in which several stations are registered. In this case, the thing configuration will fail because the service will not return the data expected by the binding. The best solution in this case is to use as location latitude and longitude, the service will automatically select a station from this position.

For the language parameter Weather Underground uses a special set of language codes which are different from ISO 639-1 standard, for example for German use `DL`  or Swedish use `SW`. See [Weather Underground language support documentation](https://www.wunderground.com/weather/api/d/docs?d=language-support) for a detailed list. 

## Channels

The weather information that is retrieved is available as these channels:

| Channel Group ID | Channel ID | Item Type    | Description             |
|------------------|------------|--------------|-------------------------|
| Current          | location             | String               | Weather observation location |
| Current          | stationId            | String               | Weather station identifier |
| Current          | observationTime      | DateTime             | Observation date and time |
| Current          | conditions           | String               | Weather conditions |
| Current          | temperature          | Number:Temperature   | Temperature |
| Current          | relativeHumidity     | Number:Dimensionless | Relative humidity |
| Current          | windDirection        | String               | Wind direction |
| Current          | windDirectionDegrees | Number:Angle         | Wind direction as an angle |
| Current          | windSpeed            | Number:Speed         | Wind speed |
| Current          | windGust             | Number:Speed         | Wind gust |
| Current          | pressure             | Number:Pressure      | Pressure |
| Current          | pressureTrend        | String               | Pressure trend ("up", "stable" or "down") | |
| Current          | dewPoint             | Number:Temperature   | Dew Point temperature |
| Current          | heatIndex            | Number:Temperature   | Heat Index |
| Current          | windChill            | Number:Temperature   | Wind chill temperature |
| Current          | feelingTemperature   | Number:Temperature   | Feeling temperature |
| Current          | visibility           | Number:Length        | Visibility |
| Current          | solarRadiation       | Number:Intensity     | Solar radiation |
| Current          | UVIndex              | Number               | UV Index |
| Current          | precipitationDay     | Number:Length        | Rain fall during the day |
| Current          | precipitationHour    | Number:Length        | Rain fall during the last hour |
| Current          | icon                 | Image                | Icon representing the weather current conditions |
| Current          | iconKey              | String               | Key used in the icon URL |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | forecastTime                | DateTime             | Forecast date and time |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | conditions                  | String               | Weather forecast conditions |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | minTemperature              | Number:Temperature   | Minimum temperature |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | maxTemperature              | Number:Temperature   | Maximum temperature |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | relativeHumidity            | Number:Dimensionless | Relative humidity |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | probaPrecipitation          | Number:Dimensionless | Probability of precipitation |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | precipitationDay            | Number:Length        | Rain fall |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | snow                        | Number:Length        | Snow fall |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | maxWindDirection            | String               | Maximum wind direction | |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | maxWindDirectionDegrees     | Number:Angle         | Maximum wind direction as an angle | |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | maxWindSpeed                | Number:Speed         | Maximum wind speed |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | averageWindDirection        | String               | Average wind direction | |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | averageWindDirectionDegrees | Number:Angle         | Average wind direction as an angle |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | averageWindSpeed            | Number:Speed         | Average wind speed | 
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | icon                        | Image                | Icon representing the weather forecast conditions |
| forecastToday forecastTomorrow forecastDay2 ... forecastDay9 | iconKey                     | String               | Key used in the icon URL |


## Full Example

demo.things:

```
Bridge weatherunderground:bridge:api "API" [ apikey="XXXXXXXXXXXX" ] {
        Thing weather paris "Météo Paris" [ location="France/Paris", language="FR", refresh=15 ]
}
```

demo.items:

```
String Conditions "Conditions [%s]" {channel="weatherunderground:weather:api:paris:current#conditions"}
Image Icon "Icon" {channel="weatherunderground:weather:api:paris:current#icon"}
String IconKey "Icon key [%s]" {channel="weatherunderground:weather:api:paris:current#iconKey"}
DateTime ObservationTime "Observation time [%1$tH:%1$tM]" <clock>  {channel="weatherunderground:weather:api:paris:current#observationTime"}
String ObservationLocation "Location [%s]" {channel="weatherunderground:weather:api:paris:current#location"}
String Station "Station [%s]" {channel="weatherunderground:weather:api:paris:current#stationId"}

Number:Temperature Temperature "Current temperature [%.1f %unit%]" <temperature> {channel="weatherunderground:weather:api:paris:current#temperature"}
Number:Temperature FeelTemp "Feeling temperature [%.1f %unit%]" <temperature>  {channel="weatherunderground:weather:api:paris:current#feelingTemperature"}

Number:Dimensionless Humidity "Humidity [%d %%]" <humidity> {channel="weatherunderground:weather:api:paris:current#relativeHumidity"}
Number:Pressure Pressure "Pressure [%.0f %unit%]" {channel="weatherunderground:weather:api:paris:current#pressure"}
String PressureTrend "Pressure trend [%s]" {channel="weatherunderground:weather:api:paris:current#pressureTrend"}

Number:Length RainD "Rain [%.1f &unit%]" <rain> {channel="weatherunderground:weather:api:paris:current#precipitationDay"}
Number:Length RainH "Rain [%.1f %unit%/h]" <rain> {channel="weatherunderground:weather:api:paris:current#precipitationHour"}

String WindDirection "Wind direction [%s]" <wind> {channel="weatherunderground:weather:api:paris:current#windDirection"}
Number:Angle WindDirection2 "Wind direction [%.0f %unit%]" <wind>  {channel="weatherunderground:weather:api:paris:current#windDirectionDegrees"}
Number:Speed WindSpeed "Wind speed [%.1f %unit%]" <wind> {channel="weatherunderground:weather:api:paris:current#windSpeed"}
Number:Speed WindGust "Wind gust [%.1f %unit%]" <wind> {channel="weatherunderground:weather:api:paris:current#windGust"}

Number:Temperature DewPoint "Dew Point [%.1f %unit%]" <temperature>  {channel="weatherunderground:weather:api:paris:current#dewPoint"}
Number:Temperature HeatIndex "Heat Index [%.1f %unit%]" <temperature>  {channel="weatherunderground:weather:api:paris:current#heatIndex"}
Number:Temperature WindChill "Wind Chill [%.1f %unit%]" <temperature>  {channel="weatherunderground:weather:api:paris:current#windChill"}
Number:Length Visibility "Visibility [%.1f %unit%]" {channel="weatherunderground:weather:api:paris:current#visibility"}
Number:Intensity SolarRadiation "Solar Radiation [%.2f %unit%]"  {channel="weatherunderground:weather:api:paris:current#solarRadiation"}
Number UV "UV Index [%.1f]" {channel="weatherunderground:weather:api:paris:current#UVIndex"}

DateTime ForecastTime "Forecast time [%1$tH:%1$tM]" <clock>  {channel="weatherunderground:weather:api:paris:forecastToday#forecastTime"}
String ForecastCondition "Forecast conditions [%s]"  {channel="weatherunderground:weather:api:paris:forecastToday#conditions"}
Image ForecastIcon "Forecast icon"  {channel="weatherunderground:weather:api:paris:forecastToday#icon"}
String ForecastIconKey "Forecast icon key [%s]"  {channel="weatherunderground:weather:api:paris:forecastToday#iconKey"}
Number:Temperature ForecastTempMin "Forecast min temp [%.1f %unit%]" <temperature>  {channel="weatherunderground:weather:api:paris:forecastToday#minTemperature"}
Number:Temperature ForecastTempMax "Forecast max temp [%.1f %unit%]" <temperature>  {channel="weatherunderground:weather:api:paris:forecastToday#maxTemperature"}
Number:Dimensionless ForecastHumidity "Forecast Humidity [%d %unit%]" <humidity>  {channel="weatherunderground:weather:api:paris:forecastToday#relativeHumidity"}
Number:Dimensionless ForecastProbaPrecip "Proba precip [%d %unit%]" <rain>  {channel="weatherunderground:weather:api:paris:forecastToday#probaPrecipitation"}
Number:Length ForecastRain "Rain [%.1f %unit%]" <rain> {channel="weatherunderground:weather:api:paris:forecastToday#precipitationDay"}
Number:Length ForecastSnow "Snow [%.2f %unit%]" <rain> {channel="weatherunderground:weather:api:paris:forecastToday#snow"}
String ForecastMaxWindDirection "Max wind direction [%s]" <wind>  {channel="weatherunderground:weather:api:paris:forecastToday#maxWindDirection"}
Number:Angle ForecastMaxWindDirection2 "Max wind direction [%.0f %unit%]" <wind>  {channel="weatherunderground:weather:api:paris:forecastToday#maxWindDirectionDegrees"}
Number:Speed ForecastMaxWindSpeed "Max wind speed [%.1f %unit%]" <wind>  {channel="weatherunderground:weather:api:paris:forecastToday#maxWindSpeed"}
String ForecastAvgWindDirection "Avg wind direction [%s]" <wind>  {channel="weatherunderground:weather:api:paris:forecastToday#averageWindDirection"}
Number:Angle ForecastAvgWindDirection2 "Avg wind direction [%.0f %unit%]" <wind>  {channel="weatherunderground:weather:api:paris:forecastToday#averageWindDirectionDegrees"}
Number:Speed ForecastAvgWindSpeed "Avg wind speed [%.1f %unit%]" <wind>  {channel="weatherunderground:weather:api:paris:forecastToday#averageWindSpeed"}
```
# Belkin Wemo Binding

This binding integrates the [Belkin WeMo Family](http://www.belkin.com/us/Products/c/home-automation/).
The integration happens either through the WeMo-Link bridge, which acts as an IP gateway to the ZigBee devices or through WiFi connection to standalone devices.

## Supported Things

The WeMo Binding supports the Socket, Insight, Lightswitch, Motion and Maker devices, as well as the WeMo-Link bridge with WeMo LED bulbs.

## Discovery

The WeMo devices are discovered through UPnP discovery service in the network. Devices will show up in the inbox and can be easily added as Things.

## Binding Configuration

The binding does not need any special configuration

## Thing Configuration

For manual Thing configuration, one needs to know the UUID of a certain WeMo device.
In the thing file, this looks e.g. like

```
wemo:socket:Switch1 [udn="Socket-1_0-221242K11xxxxx"]
```

For a WeMo Link bridge and paired LED Lights, please use the following Thing definition

```
Bridge wemo:bridge:Bridge-1_0-231445B01006A0 [udn="Bridge-1_0-231445B010xxxx"] {
MZ100 94103EA2B278xxxx [ deviceID="94103EA2B278xxxx" ]
MZ100 94103EA2B278xxxx [ deviceID="94103EA2B278xxxx" ]
}
```



## Channels

Devices support some of the following channels:

| Channel Type ID | Item Type    | Description  |
|-----------------|------------------------|--------------|----------------- |------------- |
| motionDetection | Switch | On if motion is detected, off otherwise. (Motion Sensor only) |
| lastMotionDetected | DateTime | Representing the Date and Time when the last motion was detected. (Motion Sensor only) |
| state | Switch       | This channel controls the actual binary State of a Device or represents Motion Detection. |
| lastChangedAt | DateTime | Representing the Date and Time the device was last turned on or of. |
| lastOnFor | Number       | Time in seconds an Insight device was last turned on for. |
| onToday   | Number       | Time in seconds an Insight device has been switched on today.   |
| onTotal   | Number       | Time in seconds an Insight device has been switched on totally. |
| timespan  | Number       | Time in seconds over which onTotal applies. Typically 2 weeks except first used. |
| averagePower | Number    | Average power consumption in Watts. 
| currentPower | Number    | Current power consumption of an Insight device. 0 if switched off. |
| energyToday | Number     | Energy in Wh used today. |
| energyTotal | Number     | Energy in Wh used in total. |
| standbyLimit | Number    | Minimum energy draw in W to register device as switched on (default 8W, configurable via WeMo App). |
| brightness   | Number    | Brightness of a WeMo LED. |


## Full Example

demo.things:

```
wemo:socket:Switch1 [udn="Socket-1_0-221242K11xxxxx"]
wemo:motion:Sensor1 [udn="Sensor-1_0-221337L11xxxxx"]
Bridge wemo:bridge:Bridge-1_0-231445B010xxxx [udn="Bridge-1_0-231445B010xxxx"] {
MZ100 94103EA2B278xxxx [ deviceID="94103EA2B278xxxx" ]
MZ100 94103EA2B278xxxx [ deviceID="94103EA2B278xxxx" ]
}
```

demo.items:

```
Switch DemoSwitch    { channel="wemo:socket:Switch1:state" }
Switch LightSwitch   { channel="wemo:lightswitch:Lightswitch1:state" }
Switch MotionSensor  { channel="wemo:Motion:Sensor1:motionDetection" }
Switch MotionDetected  { channel="wemo:Motion:Sensor1:lastMotionDetected" }
Number InsightPower  { channel="wemo:insight:Insight1:currentPower" }
Number InsightLastOn { channel="wemo:insight:Insight1:lastOnFor" }
Number InsightToday  { channel="wemo:insight:Insight1:onToday" }
Number InsightTotal  { channel="wemo:insight:Insight1:onTotal" }
Switch LED1 { channel="wemo:MZ100:Bridge-1_0-231445B010xxxx:94103EA2B278xxxx:state" }
Dimmer dLED1 { channel="wemo:MZ100:Bridge-1_0-231445B010xxxx:94103EA2B278xxxx:brightness" }
Switch LED2 { channel="wemo:MZ100:Bridge-1_0-231445B010xxxx:94103EA2B278xxxx:state" }
Dimmer dLED2 { channel="wemo:MZ100:Bridge-1_0-231445B010xxxx:94103EA2B278xxxx:brightness" }
```

demo.sitemap:

```
sitemap demo label="Main Menu"
{
		Frame label="WeMo" {
			Switch item=DemoSwitch
			Switch item=LightSwitch
			Switch item=MotionSensor
			Number item=InsightPower
			Number item=InsightLastOn
			Number item=InsightToday
			Number item=InsightTotal
			Switch item=LED1
			Slider item=dLED1
			Switch item=LED2
			Slider item=dLED2
		}
}
```
# Embedded MQTT Broker

    MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport.

This bundle allows to configure and start an embedded MQTT broker (based on [Moquette](https://github.com/andsel/moquette)) for an easy way to have an MQTT Server up and running with a click.

## Service Configuration

All parameters are optional.

* __port__: The port, the embedded broker should run on. Defaults to not set, which means the typical ports 1883 and 8883 (SSL) are used.
* __username__: The user name that clients need to provide to connect to this broker.
* __password__: The password that clients need to provide to connect to this broker.
* __secure__: If set, hosts a secure SSL connection on port 8883 or otherwise a non secure connection on port 1883 (if not overwritten by the port parameter).
* __persistence_file__: An optional persistence file. Retained messages are stored in this file. Can be empty to not store anything. If it starts with "/" on Linux/MacOS or with a drive letter and colon (eg "c:/") it will be treated as an absolute path. Be careful to select a path that you have write access to.
# mapdb Persistence

The [mapdb](http://www.mapdb.org/) Persistence Service is based on simple key-value store that only saves the last value.
The intention is to use this for `restoreOnStartup` items because all other persistence options have their drawbacks if values are only needed for reload.
They:

* grow in time
* require complex installs (`mysql`, `influxdb`, ...)
* `rrd4j` can't store all item types (only numeric types)

Querying the mapdb persistence service for historic values other than the last value make no sense since the persistence service can only store one value per item.

## Configuration

All item and event related configuration is done in the file `persistence/mapdb.persist`.

To configure this service as the default persistence service for Eclipse SmartHome, add or change the line

```
org.eclipse.smarthome.persistence:default=mapdb
```

in the file `services/runtime.cfg`.


## Troubleshooting

Restore of items after startup is taking some time.
Rules are already started in parallel.
Especially in rules that are started via `System started` trigger,
it may happen that the restore is not completed resulting in undefined items.
In these cases the use of restored items has to be delayed by a couple of seconds.
This delay has to be determined experimentally.
# Exec Transformation Service

Transforms an input string with an external program.

Executes an external program and returns the output as a string.
In the given command line the placeholder `%s` is substituted with the input value.

The external program must either be in the executable search path of the server process, or an absolute path has to be used.

## Examples

### General Setup

**Item**

This will replace the visible label in the UI with the transformation you apply with the command <TransformProgram>.
  
```java
String yourItem "Some info  [EXEC(/absolute/path/to/your/<TransformProgram> %s):%s]"
```

**Rule**

```java
rule "Your Rule Name"
when
    Item YourTriggeringItem changed
then
    var formatted = transform("EXEC","/absolute/path/to/your/<TransformProgram>", YourTriggeringItem.state.toString)
    yourFormattedItem.sendCommand(formatted.toString) 
end
```

### Example with a program

Substitute the `/absolute/path/to/your/<TransformProgram>` with

```shell
/bin/date -v1d -v+1m -v-1d -v-%s
```

When the input argument for `%s` is `fri` the execution returns a string with the last weekday of the month, formated as readable text.

```
Fri 31 Mar 2017 13:58:47 IST`
```

Or replace it with

```shell
numfmt --to=iec-i --suffix=B --padding=7 %s
```

When the input argument for `%s` is 1234567 it will return the bytes formated in a better readable form

```shell
1.2MiB
```

### Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:EXEC", function="<shellcommand>", sourceFormat="<valueFormat>"]}
```

The shell command to be executed has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.

# Further Reading

* [Manual](http://man7.org/linux/man-pages/man1/date.1.html) and [tutorial](https://linode.com/docs/tools-reference/tools/use-the-date-command-in-linux/) for date.
* [Manual](http://man7.org/linux/man-pages/man1/numfmt.1.html) and [tutorial](http://www.pixelbeat.org/docs/numfmt.html) for numfmt.


Bundle resources go in here!# JavaScript Transformation Service

Transform an input to an output using JavaScript. 

It expects the transformation rule to be read from a file which is stored under the `transform` folder. 
To organize the various transformations, one should use subfolders.

## Example

Let's assume we have received a string containing `foo bar baz` and we're looking for a length of the last word (`baz`).

transform/getValue.js:

```
(function(i) {
    var array = i.split(" ");
    return array[array.length - 1].length;
})(input)
```

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:JS", function="<filename>", sourceFormat="<valueFormat>"]}
```

The Javascript file (from within the `transform` folder) to be used has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.
Bundle resources go in here!# JsonPath Transformation Service

Transforms a JSON structure on basis of the [JsonPath](https://github.com/jayway/JsonPath#jayway-jsonpath) expression to an JSON containing the requested data.

## Examples

### Basic Example

Given the JSON

```
[{ "device": { "location": "Outside", "status": { "temperature": 23.2 }}}]
```

the JsonPath expression `$.device.location` exstracts the string instead a valid JSON `[ "Outside" ]`, see [differences](#differences-to-standard-jsonpath).

```
Outside
```

the JsonPath expression `$.device.status.temperature` exstracts the number instead a valid JSON `[ 23.2 ]`, see [differences](#differences-to-standard-jsonpath).

```
23.2
```

### In Setup

**Item**

```csv
String  Temperature_json "Temperature [JSONPATH($.device.status.temperature):%s °C]" {...}
Number  Temperature "Temperature [%.1f °C]"
```

**Rule**

```php
rule "Convert JSON to Item Type Number"
  when
    Item Temperature_json changed
 then
    // use the transformation service to retrieve the value
    val newValue = transform("JSONPATH", ".$.device.status.temperature", Temperature_json.state.toString)

    // post the new value to the Number Item
    Temperature.postUpdate( newValue )
 end
```

Now the resulting Number can also be used in the label to [change the color](https://docs.openhab.org/configuration/sitemaps.html#label-and-value-colors) or in a rule as value to compare.

## Differences to standard JsonPath

Compared to standard JSON the transformation it returns evaluated values when a single alement is retrieved from the query.
Means it does not return a valid JSON `[ 23.2 ]` but `23.2`, `[ "Outside" ]` but `Outside`.
This makes it possible to use it in labels or output channel of things and get Numbers or Strings instead of JSON arrays.
A query which returns multiple elements as list is not supported.

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:JSONPATH", function="<jsonPath>", sourceFormat="<valueFormat>"]}
```

The JSONPath expression to be used has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.

## Further Reading

* An extended [introduction](https://www.w3schools.com/js/js_json_intro.asp) can be found at W3School.
* As JsonPath transformation is based on [Jayway](https://github.com/json-path/JsonPath) using a [online validator](https://jsonpath.herokuapp.com/) which also uses Jaway will give most similar results. 
Bundle resources go in here!# Map Transformation Service

Transforms the input by mapping it to another string. It expects the mappings to be read from a file which is stored under the `transform` folder. 

This file should be in property syntax, i.e. simple lines with "key=value" pairs. 
The file format is documented [here](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html#load-java.io.Reader-).
To organize the various transformations one might use subfolders.

A default value can be provided if no matching entry is found by using "=value" syntax

## Example

transform/binary.map:

```properties
key=value
1=ON
0=OFF
ON=1
OFF=0
=default
```

| input      | output    |
|------------|-----------|
| `1`        | `ON`      |
| `OFF`      | `0`       |
| `key`      | `value`   |
| `anything` | `default` |

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:MAP", function="<filename>", sourceFormat="<valueFormat>"]}
```

The mapping filename (within the `transform` folder) has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.
Bundle resources go in here!# RegEx Transformation Service

Transforms a source string on basis of the regular expression (regex) search pattern to a defined result string.

The simplest regex is in the form `<regex>` and transforms the input string on basis of the regex pattern to a result string.
A full regex is in the form `s/<regex>/<substitution>/g` whereat the delimiter `s` and the regex flag `g` have a special meaning.

The regular expression in the format `s/<regex>/result/g`, replaces all occurrences of `<regex>` in the source string with `result`.
The regular expression in the format `s/<regex>/result/` (without `g`), replaces the first occurrence of `<regex>` in the source string with `result`.

If the regular expression contains a [capture group](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html#cg) defined by `()`, it returns the captured string. 
Multiple capture groups can be used to retrieve multiple strings and can be combined as a result string defined in the `substitution`.

The transformation can be set to be restricted to only match if the input string begins with a character by prepending `^` to the beginning of a pattern or to only match if the input string ends with a specified character by appending `$` at the end.
So the regex `^I.*b$` only matches when the input string starts with `I` and ends with `b`, like in `I'm Bob`. Both can be used alone or in combination.

The special characters `\.[]{}()*+-?^$|` have to be escaped when they should be used as literal characters.

## Examples

### Basic Examples

|         Input String        |    Regular Expression    |         Output String        | Explanation              |
|---------------------------|------------------------|----------------------------|--------------------------|
| `My network does not work.` | `s/work/cast/g` | `"My netcast does not cast."` | Replaces all matches of the string "work" with the string "cast". |
| `My network does not work.` | `.*(\snot).*` | `" not"` | Returns only the first match and strips of the rest, "\s" defines a  whitespace. |
| `temp=44.0'C` | `temp=(.*?)'C)`          | `44.0` | Matches whole string and returns the content of the captcha group `(.?)`. |
| `48312` | `s/(.{2})(.{3})/$1.$2/g` | `48.312` | Captures 2 and 3 character, returns first capture group adds a dot and the second capture group. This divides by 1000. |

### Example In Setup

**Input String**

```shell
temp=44.0'C
```

the regex transformation can be used to extract the value to display it on the label.

**.items**

```csv
String  Temperature_str "Temperature [REGEX(.*=(\\d*.\\d*).*):%s °C]" {...}
Number  Temperature "Temperature [%.1f °C]"
```

The regex pattern is is defined as follows
* `.*` match any character, zero and unlimited times
* `=` match the equal sign literally, used to find the position
*  `()` capture group match 
    * `\d*` match a digit (equal to [0-9]), zero and unlimited times, the backslash has to be escaped see [string vs plain](#Differences-to-plain-Regex)
    * `.` match the dot literally
    * `\w*` match a word character (equal to [a-zA-Z_0-9]), zero and unlimited times, the backslash has to be escaped see [string vs plain](#Differences-to-plain-Regex)
* `.*` match any character, zero and unlimited times

The result will be `44.0` and displayed on the label as `Temperature 44.0°C`.
A better solution would be to use the regex on the result from the binding either in a rule or when the binding allows it on the output channel. 
Thus the value `44.0` would be saved as a number.

**.rules**

```php
rule "Convert String to Item Number"
  when
    Item Temperature_str changed
 then
    // use the transformation service to retrieve the value
    val newValue = transform("REGEX", ".*=(\\d*.\\d*).*", Temperature_str.state.toString)

    // post the new value to the Number Item
    Temperature.postUpdate( newValue )
 end
```

Now the resulting Number can also be used in the label to [change the color](https://docs.openhab.org/configuration/sitemaps.html#label-and-value-colors) or in a rule as value for comparison.

## Differences to plain Regex

The regex is embedded in a string so when double quotes `"` are used in a regex they need to be escaped `\"` to keep the string intact.
As the escape character of strings is the backslash this has to be escaped additionally.
To use a dot as literal in the regex it has to be escape `\.`, but in a string it has to be escaped twice `"\\."`.
The first backslash escapes the second backslash in the string so it can be used in the regex.
Using a backslash in a Regex as literal `\\` will have this form `"\\\\"`.

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:REGEX", function="<regex>", sourceFormat="<valueFormat>"]}
```

The regular expression to be executed has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.

## Further Reading

* A full [introduction](https://www.w3schools.com/jsref/jsref_obj_regexp.asp) for regular expression is available at W3School.
* Online validator help to check the syntax of a regex and give information how to design it.
    * [Regex 101](https://regex101.com/)
    * [Regex R](https://regexr.com/)
Bundle resources go in here!# Scale Transformation Service

The Scale Transformation Service is a an easy to handle tool that can help you with the discretization of number inputs.
It transforms a given input by matching it to specified ranges.
The input string must be in numerical format.

The file is expected to exist in the `transform` configuration directory and its ending has to be `.scale`.
It should follow the format given in the table below.

Range expressions always contain two parts.
The range to scale on, which is located left from the equality sign and the corresponding output string on the right of it.
A range consists of two bounds. Both are optional, the range is then open. Both bounds can be inclusive or exclusive.

| Scale Expression | Returns XYZ when the given value is                        |
|------------------|------------------------------------------------------------|
| `[12..23]=XYZ`   | `between (or equal to) 12 and 23`                          |
| `]12..23[=XYZ`   | `between 12 and 23 (12 and 23 are excluded in this case.)` |
| `[..23]=XYZ`     | `lower than or equal to 23`                                |
| `]12..]=XYZ`     | `greater than 12`                                          |

These expressions are evaluated from top to bottom.
The first range that includes the value is selected.

## Example

The following example shows how to break down numeric UV values into fixed UV index categories.
We have an example UV sensor that sends numeric values from `0` to `100`, which we then want to scale into the [UV Index](https://en.wikipedia.org/wiki/Ultraviolet_index) range.

Example item:

```java
Number Uv_Sensor_Level "UV Level [SCALE(uvindex.scale):%s]"
```

Referenced scale file `uvindex.scale` in the `transform` folder:

```python
[..3]=1
]3..6]=2
]6..8]=3
]8..10]=4
[10..100]=5
```

Each value the item receives, will be categorized to one of the five given ranges.
Values **lower than or equal to 3** are matched with `[..3]=1`.
Greater values are catched in ranges with 2 values as criteria.
The only condition here is that the received value has to be lower or equal than `100` in our example, since we haven't defined other cases yet.
If **none** of the configured conditions matches the given value, the response will be empty.

Please note that all ranges for values above **3** are opened with a `]`.
So the border values (3, 6, 8 and 10) are always transformed to the lower range, since the `]` excludes the given critera.

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:SCALE", function="<filename>", sourceFormat="<valueFormat>"]}
```

The filename (within the `transform` folder) of the scale file has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.
Bundle resources go in here!# XPath Transformation Service

Transforms an [XML](https://www.w3.org/XML/) input using an [XPath](https://www.w3.org/TR/xpath/#section-Expressions) expression.

## Examples

### Basic Example

Given a retrieved XML 

**Input XML**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PTZStatus version="2.0" >
    <AbsoluteHigh>
        <elevation>0</elevation>
        <azimuth>450</azimuth>
        <absoluteZoom>10</absoluteZoom>
    </AbsoluteHigh>
</PTZStatus>
```

The XPath `/PTZStatus/AbsoluteHigh/azimuth/text()` returns the document

```
450
```

## Advanced Example

Given a retrieved XML (e.g. from an HIK Vision device with the namespace `xmlns="http://www.hikvision.com/ver20/XMLSchema"`):

**Input XML**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PTZStatus version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
    <AbsoluteHigh>
        <elevation>0</elevation>
        <azimuth>450</azimuth>
        <absoluteZoom>10</absoluteZoom>
    </AbsoluteHigh>
</PTZStatus>
```

A simple xpath query to fetch the Azimut value does not work as it does not address the namespace.

There are two ways to address the namespace.
* Simple path which may not work in complex XML.
* With full qualified path.
* 
The XPath 
* `[name()='PTZStatus']/*[name()='AbsoluteHigh']/*[name()='azimuth']/`
* `/*[local-name()='PTZStatus' and namespace-uri()='http://www.hikvision.com/ver20/XMLSchema']/*[local-name()='AbsoluteHigh' and namespace-uri()='http://www.hikvision.com/ver20/XMLSchema']/*[local-name()='azimuth' and namespace-uri()='http://www.hikvision.com/ver20/XMLSchema']`

returns 

```
<azimuth>450</azimuth>
```

### In Setup

**.items**

```csv
String  Temperature_xml "Temperature [XPATH(/*[name()='PTZStatus']/*[name()='AbsoluteHigh']/*[name()='azimuth']/):%s °C]" {...}
Number  Temperature "Temperature [%.1f °C]"
```

**.rules**

```php
rule "Convert XML to Item Type Number"
  when
    Item Temperature_xml changed
  then
    // use the transformation service to retrieve the value
    // Simple
    val mytest = transform("XPATH", "/*[name()='PTZStatus']
                                     /*[name()='AbsoluteHigh']
                                     /*[name()='azimuth']
                                     /text()", 
                                    Temperature_xml.state.toString )  
    // Fully qualified
    val mytest = transform("XPATH", "/*[local-name()='PTZStatus'    and namespace-uri()='http://www.hikvision.com/ver20/XMLSchema']
                                     /*[local-name()='AbsoluteHigh' and namespace-uri()='http://www.hikvision.com/ver20/XMLSchema']
                                     /*[local-name()='azimuth'      and namespace-uri()='http://www.hikvision.com/ver20/XMLSchema']
                                     /text()",
                                    Temperature_xml.state.toString )

    // post the new value to the Number Item
    Temperature.postUpdate( newValue )
end
```

Now the resulting Number can also be used in the label to [change the color](https://docs.openhab.org/configuration/sitemaps.html#label-and-value-colors) or in a rule as value for comparison.

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:XPATH", function="<xpath>", sourceFormat="<valueFormat>"]}
```

The XPath expression to be executed has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.

## Further Reading

* An [introduction](https://www.w3schools.com/xml/xpath_intro.asp) to XPath at W3School
* A informative explanation of [common mistakes](https://qxf2.com/blog/common-xpath-mistakes/).
* Online validation tools like [this](https://www.freeformatter.com/xpath-tester.html) to check the syntax.
Bundle resources go in here!# XSLT Transformation Service

Transform input using the XML Stylesheet Language for Transformations (XSLT).

XSLT is a standard method to transform an XML structure from one document into a new document with a different structure.

The transformation expects the rule to be read from a file which is stored under the `transform` folder. 
To organize the various transformations one should use subfolders.

General transformation rule summary:

* The directive `xsl:output` defines how the output document should be structured.
* The directive `xsl:template` specifies matching attributes for the XML node to find. 
* The `xsl:template` tag contains the rule which specifies what should be done.

The Rule uses XPath to gather the XML node information.
For more information have a look at the [XPath transformation](https://docs.openhab.org/addons/transformations/xpath/readme.html) .

## Examples

### Basic Example

A simple but complete XSLT transformation looks like in the following example, which was taken from [here](https://en.wikipedia.org/wiki/Java_API_for_XML_Processing#Example).

**input XML**

```xml
<?xml version='1.0' encoding='UTF-8'?>
<root><node val='hello'/></root>
```

**transform/helloworld.xsl**

* `xsl:output`: transform incoming document into another XML-like document, without indentation.
* `xsl:template`: `match="/"` "any type of node", so the whole document.
* The `xsl` rule does `select` the node `/root/node` and extracts the `value-of` attribute `val`.

```xml
<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version='2.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>
   <xsl:output method='xml' indent='no'/>
   <xsl:template match='/'>
      <reRoot><reNode><xsl:value-of select='/root/node/@val' /> world</reNode></reRoot>
   </xsl:template>
</xsl:stylesheet>
```

**Output XML**

```xml
<reRoot><reNode>hello world</reNode></reRoot>
```

### Advanced Example

This example has a namespace defined, as you would find in real world applications, which has to be matched in the rule.

**input XML**

* The tag `<PTZStatus>` contains an attribute `xmlns=` which defines the namespace `http://www.hikvision.com/ver20/XMLSchema`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PTZStatus version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
	<AbsoluteHigh>
		<elevation>0</elevation>
		<azimuth date="Fri, 18 Dec 2009 9:38 am PST" >450</azimuth>
		<absoluteZoom>10</absoluteZoom>
	</AbsoluteHigh>
</PTZStatus>
```

**transform/azimut.xsl**

In the rule, the tag `<xsl:stylesheet>` has to have an attribute `xmlns:xsl="http://www.w3.org/1999/XSL/Transform"` and a second attribute `xmlns:`. 
This attribute has to be the same as the namespace for the input document.
In the rule each step traversed along the path to the next tag has to be prepended with the `xmlns` namespace, here defined as `h`.

* `xsl:output` transform incoming document into another XML-like document, no indentation, **without XML**.
* `xsl:template`: `match="/"` whole document.
* Full path to node `azimuth` reading out `date` attribute.
* Add a linebreak by setting `&#10;` as text.
* Search for node `azimuth` by prepending `//` and get the `text`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:h="http://www.hikvision.com/ver20/XMLSchema">
   <xsl:output method="xml" indent="no" encoding="UTF-8" omit-xml-declaration="yes"  />
   <xsl:template match="/">
      <xsl:value-of select="/h:PTZStatus/h:AbsoluteHigh/h:azimuth/@date" />
      <xsl:text>&#10;</xsl:text>
      <xsl:value-of select="//h:azimuth/text()" />
   </xsl:template>
</xsl:stylesheet>
```

**Output Document**

```
Fri, 18 Dec 2009 9:38 am PST
450
```

## Usage as a Profile

The functionality of this `TransformationService` can be used in a `Profile` on an `ItemChannelLink` too.
To do so, it can be configured in the `.items` file as follows:

```java
String <itemName> { channel="<channelUID>"[profile="transform:XSLT", function="<xsltExpression>", sourceFormat="<valueFormat>"]}
```

The XSLT file (from within the `transform` folder) to be used has to be set in the `function` parameter.
The parameter `sourceFormat` is optional and can be used to format the input value **before** the transformation, i.e. `%.3f`.
If omitted the default is `%s`, so the input value will be put into the transformation without any format changes.

Please note: This profile is a one-way transformation, i.e. only values from a device towards the item are changed, the other direction is left untouched.

## Further Reading

* Extended introduction and more [examples](https://en.wikipedia.org/wiki/XSLT#XSLT_examples) at Wikipedia.
* A good [introduction](https://www.w3schools.com/xml/xsl_intro.asp) and [tutorial](https://www.w3schools.com/xml/xsl_transformation.asp) at W3School.
* An informative [tutorial](https://www.ibm.com/developerworks/library/x-xsltmistakes/) of common mistakes.

Bundle resources go in here!# Classic Icon Set

This is a modernized version of the original icon set from openHAB 1.x.
The set is provided with the distribution in both the PNG and SVG file format.

{% assign allIconsStr = "alarm.png,attic.png,baby_1.png,baby_2.png,baby_3.png,baby_4.png,baby_5.png,baby_6.png,bath.png,battery.png,batterylevel.png,batterylevel-0.png,batterylevel-10.png,batterylevel-20.png,batterylevel-30.png,batterylevel-40.png,batterylevel-50.png,batterylevel-60.png,batterylevel-70.png,batterylevel-80.png,batterylevel-90.png,batterylevel-100.png,battery-0.png,battery-10.png,battery-20.png,battery-30.png,battery-40.png,battery-50.png,battery-60.png,battery-70.png,battery-80.png,battery-90.png,battery-100.png,bedroom.png,bedroom_blue.png,bedroom_orange.png,bedroom_red.png,blinds.png,blinds-0.png,blinds-10.png,blinds-20.png,blinds-30.png,blinds-40.png,blinds-50.png,blinds-60.png,blinds-70.png,blinds-80.png,blinds-90.png,blinds-100.png,bluetooth.png,boy_1.png,boy_2.png,boy_3.png,boy_4.png,boy_5.png,boy_6.png,calendar.png,camera.png,carbondioxide.png,cellar.png,chart.png,cinema.png,cinemascreen.png,cinemascreen-0.png,cinemascreen-10.png,cinemascreen-20.png,cinemascreen-30.png,cinemascreen-40.png,cinemascreen-50.png,cinemascreen-60.png,cinemascreen-70.png,cinemascreen-80.png,cinemascreen-90.png,cinemascreen-100.png,cistern.png,cistern-0.png,cistern-10.png,cistern-20.png,cistern-30.png,cistern-40.png,cistern-50.png,cistern-60.png,cistern-70.png,cistern-80.png,cistern-90.png,cistern-100.png,climate.png,climate-on.png,colorlight.png,colorpicker.png,colorwheel.png,contact.png,contact-ajar.png,contact-closed.png,contact-open.png,corridor.png,door.png,door-closed.png,door-open.png,dryer.png,dryer-0.png,dryer-1.png,dryer-2.png,dryer-3.png,dryer-4.png,dryer-5.png,energy.png,error.png,fan.png,fan_box.png,fan_ceiling.png,faucet.png,fire.png,fire-off.png,fire-on.png,firstfloor.png,flow.png,flowpipe.png,frontdoor.png,frontdoor-closed.png,frontdoor-open.png,garage.png,garagedoor.png,garagedoor-0.png,garagedoor-10.png,garagedoor-20.png,garagedoor-30.png,garagedoor-40.png,garagedoor-50.png,garagedoor-60.png,garagedoor-70.png,garagedoor-80.png,garagedoor-90.png,garagedoor-100.png,garagedoor-ajar.png,garagedoor-closed.png,garagedoor-open.png,garage_detached.png,garage_detached_selected.png,garden.png,gas.png,girl_1.png,girl_2.png,girl_3.png,girl_4.png,girl_5.png,girl_6.png,greenhouse.png,groundfloor.png,group.png,heating.png,heating-0.png,heating-20.png,heating-40.png,heating-60.png,heating-80.png,heating-100.png,heating-off.png,heating-on.png,house.png,humidity.png,humidity-0.png,humidity-10.png,humidity-20.png,humidity-30.png,humidity-40.png,humidity-50.png,humidity-60.png,humidity-70.png,humidity-80.png,humidity-90.png,humidity-100.png,incline.png,keyring.png,kitchen.png,lawnmower.png,light.png,lightbulb.png,light-0.png,light-10.png,light-20.png,light-30.png,light-40.png,light-50.png,light-60.png,light-70.png,light-80.png,light-90.png,light-100.png,light-off.png,light-on.png,line.png,line-decline.png,line-incline.png,line-stagnation.png,lock.png,lock-closed.png,lock-open.png,lowbattery.png,lowbattery-off.png,lowbattery-on.png,man_1.png,man_2.png,man_3.png,man_4.png,man_5.png,man_6.png,mediacontrol.png,microphone.png,moon.png,motion.png,movecontrol.png,network.png,network-off.png,network-on.png,niveau.png,office.png,oil.png,outdoorlight.png,pantry.png,parents-off.png,parents_1_1.png,parents_1_2.png,parents_1_3.png,parents_1_4.png,parents_1_5.png,parents_1_6.png,parents_2_1.png,parents_2_2.png,parents_2_3.png,parents_2_4.png,parents_2_5.png,parents_2_6.png,parents_3_1.png,parents_3_2.png,parents_3_3.png,parents_3_4.png,parents_3_5.png,parents_3_6.png,parents_4_1.png,parents_4_2.png,parents_4_3.png,parents_4_4.png,parents_4_5.png,parents_4_6.png,parents_5_1.png,parents_5_2.png,parents_5_3.png,parents_5_4.png,parents_5_5.png,parents_5_6.png,parents_6_1.png,parents_6_2.png,parents_6_3.png,parents_6_4.png,parents_6_5.png,parents_6_6.png,party.png,pie.png,piggybank.png,player.png,poweroutlet.png,poweroutlet-off.png,poweroutlet-on.png,poweroutlet_au.png,poweroutlet_eu.png,poweroutlet_uk.png,poweroutlet_us.png,presence.png,presence-off.png,pressure.png,price.png,projector.png,pump.png,qualityofservice.png,qualityofservice-0.png,qualityofservice-1.png,qualityofservice-2.png,qualityofservice-3.png,qualityofservice-4.png,radiator.png,rain.png,receiver.png,receiver-off.png,receiver-on.png,recorder.png,returnpipe.png,rgb.png,rollershutter.png,rollershutter-0.png,rollershutter-10.png,rollershutter-20.png,rollershutter-30.png,rollershutter-40.png,rollershutter-50.png,rollershutter-60.png,rollershutter-70.png,rollershutter-80.png,rollershutter-90.png,rollershutter-100.png,screen.png,screen-off.png,screen-on.png,settings.png,sewerage.png,sewerage-0.png,sewerage-10.png,sewerage-20.png,sewerage-30.png,sewerage-40.png,sewerage-50.png,sewerage-60.png,sewerage-70.png,sewerage-80.png,sewerage-90.png,sewerage-100.png,shield.png,shield-0.png,shield-1.png,siren.png,siren-off.png,siren-on.png,slider.png,slider-0.png,slider-10.png,slider-20.png,slider-30.png,slider-40.png,slider-50.png,slider-60.png,slider-70.png,slider-80.png,slider-90.png,slider-100.png,smiley.png,smoke.png,snow.png,sofa.png,softener.png,solarplant.png,soundvolume.png,soundvolume-0.png,soundvolume-33.png,soundvolume-66.png,soundvolume-100.png,soundvolume_mute.png,status.png,suitcase.png,sun.png,sunrise.png,sunset.png,sun_clouds.png,switch.png,switch-off.png,switch-on.png,temperature.png,temperature_cold.png,temperature_hot.png,terrace.png,text.png,time.png,time-on.png,toilet.png,vacation.png,video.png,wallswitch.png,wallswitch-off.png,wallswitch-on.png,wardrobe.png,washingmachine.png,washingmachine_2.png,washingmachine_2-0.png,washingmachine_2-1.png,washingmachine_2-2.png,washingmachine_2-3.png,water.png,whitegood.png,wind.png,window.png,window-ajar.png,window-closed.png,window-open.png,woman_1.png,woman_2.png,woman_3.png,woman_4.png,woman_5.png,woman_6.png,zoom.png," %}
{% assign allIcons = allIconsStr | split: ',' %}

{% for icon in allIcons %}
  {% assign iconLower = icon | downcase | split: "." %}
  {% assign iconWithoutExt = iconLower[0] %}
  {% assign allIconsWithoutExtensionStr = allIconsWithoutExtensionStr | append: iconWithoutExt | append: ',' %}
{% endfor %}
{% assign allIconsWithoutExtension = allIconsWithoutExtensionStr | split: ',' %}


## Places

{% for category in site.data.categories_places %}
    {% assign categoryNamesStr = categoryNamesStr | append: category.name | downcase | append: ',' %}
{% endfor %}
{% assign placesCategoryNames = categoryNamesStr | split: ',' %}

<div id="iconset-preview-locations" class="icons">
{% for category in placesCategoryNames %}
  {% assign iconSrc = base | append: "/img/icon_no_category.png" %}
  {% if allIconsWithoutExtension contains category %}
    {% assign iconSrc = "icons/" | append: category | append: ".png" %}
  {% endif %}
  <figure>
    <img src="{{iconSrc}}" alt="{{category}}" title="{{category}}">
    <figcaption>{{category}}</figcaption>
  </figure>
{% endfor %}
</div>

## Things

{% assign categoryNamesStr = "" %}
{% for category in site.data.categories_thing %}
    {% assign categoryNamesStr = categoryNamesStr | append: category.name | downcase | append: ',' %}
{% endfor %}
{% assign thingCategoryNames = categoryNamesStr | split: ',' %}

<div id="iconset-preview-things" class="icons">
{% for category in thingCategoryNames %}
  {% assign iconSrc = base | append: "/img/icon_no_category.png" %}
  {% if allIconsWithoutExtension contains category %}
    {% assign iconSrc = "icons/" | append: category | append: ".png" %}
  {% endif %}

  {% assign altText = "" %}
  {% for i in allIcons %}
    {% assign prefix = category | append: "-" %}    
    {% if i contains prefix %}
      {% assign iWithoutExt = i | split: "." %}
      {% assign altText = altText | append: iWithoutExt[0] | append: " " %}
    {% endif %}
  {% endfor %}
  <figure>
    <img src="{{iconSrc}}" alt="{{altText}}" title="{{altText}}">
    <figcaption>{{category}}</figcaption>
  </figure>
{% endfor %}
</div>

## Channels

{% for category in site.data.categories %}
    {% assign typesStr = typesStr | append: category.type | append: ',' %}
{% endfor %}
{% assign types = typesStr | split: ',' | uniq %}

{% for type in types %}

#### {{type}}

  {% assign channelCategoryNamesStr = "" %}
  {% for category in site.data.categories %}
    {% if category.type == type %}
      {% assign channelCategoryNamesStr = channelCategoryNamesStr | append: category.name | downcase | append: ',' %}
    {% endif %}
  {% endfor %}
  {% assign channelCategoryNames = channelCategoryNamesStr | split: ',' %}
  {% assign channelCategories = channelCategories | concat: channelCategoryNames %}

  <div id="iconset-preview-channels" class="icons">
  {% for channelCategory in channelCategoryNames %}
    {% assign iconSrc = base | append: "/img/icon_no_category.png" %}
    {% if allIconsWithoutExtension contains channelCategory %}
      {% assign iconSrc = "icons/" | append: channelCategory | append: ".png" %}
    {% endif %}

    {% assign altText = "" %}
    {% for i in allIcons %}
      {% assign prefix = channelCategory | append: "-" %}    
      {% if i contains prefix %}
        {% assign iWithoutExt = i | split: "." %}
        {% assign altText = altText | append: iWithoutExt[0] | append: " " %}
      {% endif %}
    {% endfor %}

    <figure>
      <img src="{{iconSrc}}" alt="{{altText}}" title="{{altText}}">
      <figcaption>{{channelCategory}}</figcaption>
    </figure>
  {% endfor %}
  </div>

{% endfor %}

## Other Icons

{% assign allCategories = thingCategoryNames | concat: channelCategories | concat: placesCategoryNames | sort | uniq %}

<div id="iconset-preview-other" class="icons">
{% for icon in allIcons %}
  {% assign categoryLower = icon | downcase | split: "." %}
  {% assign plainCategory = categoryLower[0] %}

  {% assign otherIcon = true %}
  {% for catWithIcon in allCategories %}
    {% if catWithIcon.size <= plainCategory.size %}
      {% assign plainCategoryStart = plainCategory | truncate: catWithIcon.size, "" %}
      {% if plainCategoryStart == catWithIcon %}
        {% assign otherIcon = false %}
        {% break %}
      {% endif %}
    {% endif %}
  {% endfor %}

  {% if otherIcon == false %}
    {% continue %}
  {% endif %}

  {% unless icon contains "-" %}

    {% assign altText = "" %}
    {% for i in allIcons %}
      {% assign prefix = plainCategory | append: "-" %}    
      {% if i contains prefix %}
        {% assign iWithoutExt = i | split: "." %}
        {% assign altText = altText | append: iWithoutExt[0] | append: " " %}
      {% endif %}
    {% endfor %}
  
    <figure>
      <img src="icons/{{icon}}" alt="{{altText}}" title="{{altText}}">
      <figcaption>{{plainCategory}}</figcaption>
    </figure>
  {% endunless %}
{% endfor %}
</div>

#!/usr/bin/env sh

READMEMD="$(cd "$(dirname "$0")"; pwd)/README.md"

cat <<EOF > "$READMEMD"
# Classic Icon Set

This is a modernized version of the original icon set from openHAB 1.x.
The set is provided with the distribution in both the PNG and SVG file format.

EOF

for icon in $(ls icons/*.png | sort -V); do
  name=$(basename "$icon")
  echo "Adding icon '$name'"
  if [ "$name" = "none.png" ] || [ "$name" = "none.svg" ]; then continue; fi
  allIcons="$allIcons$name,"
done

allIcons=${allIcons:: -1}

cat <<EOF >> "$READMEMD"
{% assign allIconsStr = "$allIcons" %}
{% assign allIcons = allIconsStr | split: ',' %}

{% for icon in allIcons %}
  {% assign iconLower = icon | downcase | split: "." %}
  {% assign iconWithoutExt = iconLower[0] %}
  {% assign allIconsWithoutExtensionStr = allIconsWithoutExtensionStr | append: iconWithoutExt | append: ',' %}
{% endfor %}
{% assign allIconsWithoutExtension = allIconsWithoutExtensionStr | split: ',' %}


## Places

{% for category in site.data.categories_places %}
    {% assign categoryNamesStr = categoryNamesStr | append: category.name | downcase | append: ',' %}
{% endfor %}
{% assign placesCategoryNames = categoryNamesStr | split: ',' %}

<div id="iconset-preview-locations" class="icons">
{% for category in placesCategoryNames %}
  {% assign iconSrc = base | append: "/img/icon_no_category.png" %}
  {% if allIconsWithoutExtension contains category %}
    {% assign iconSrc = "icons/" | append: category | append: ".png" %}
  {% endif %}
  <figure>
    <img src="{{iconSrc}}" alt="{{category}}" title="{{category}}">
    <figcaption>{{category}}</figcaption>
  </figure>
{% endfor %}
</div>

## Things

{% assign categoryNamesStr = "" %}
{% for category in site.data.categories_thing %}
    {% assign categoryNamesStr = categoryNamesStr | append: category.name | downcase | append: ',' %}
{% endfor %}
{% assign thingCategoryNames = categoryNamesStr | split: ',' %}

<div id="iconset-preview-things" class="icons">
{% for category in thingCategoryNames %}
  {% assign iconSrc = base | append: "/img/icon_no_category.png" %}
  {% if allIconsWithoutExtension contains category %}
    {% assign iconSrc = "icons/" | append: category | append: ".png" %}
  {% endif %}

  {% assign altText = "" %}
  {% for i in allIcons %}
    {% assign prefix = category | append: "-" %}    
    {% if i contains prefix %}
      {% assign iWithoutExt = i | split: "." %}
      {% assign altText = altText | append: iWithoutExt[0] | append: " " %}
    {% endif %}
  {% endfor %}
  <figure>
    <img src="{{iconSrc}}" alt="{{altText}}" title="{{altText}}">
    <figcaption>{{category}}</figcaption>
  </figure>
{% endfor %}
</div>

## Channels

{% for category in site.data.categories %}
    {% assign typesStr = typesStr | append: category.type | append: ',' %}
{% endfor %}
{% assign types = typesStr | split: ',' | uniq %}

{% for type in types %}

#### {{type}}

  {% assign channelCategoryNamesStr = "" %}
  {% for category in site.data.categories %}
    {% if category.type == type %}
      {% assign channelCategoryNamesStr = channelCategoryNamesStr | append: category.name | downcase | append: ',' %}
    {% endif %}
  {% endfor %}
  {% assign channelCategoryNames = channelCategoryNamesStr | split: ',' %}
  {% assign channelCategories = channelCategories | concat: channelCategoryNames %}

  <div id="iconset-preview-channels" class="icons">
  {% for channelCategory in channelCategoryNames %}
    {% assign iconSrc = base | append: "/img/icon_no_category.png" %}
    {% if allIconsWithoutExtension contains channelCategory %}
      {% assign iconSrc = "icons/" | append: channelCategory | append: ".png" %}
    {% endif %}

    {% assign altText = "" %}
    {% for i in allIcons %}
      {% assign prefix = channelCategory | append: "-" %}    
      {% if i contains prefix %}
        {% assign iWithoutExt = i | split: "." %}
        {% assign altText = altText | append: iWithoutExt[0] | append: " " %}
      {% endif %}
    {% endfor %}

    <figure>
      <img src="{{iconSrc}}" alt="{{altText}}" title="{{altText}}">
      <figcaption>{{channelCategory}}</figcaption>
    </figure>
  {% endfor %}
  </div>

{% endfor %}

## Other Icons

{% assign allCategories = thingCategoryNames | concat: channelCategories | concat: placesCategoryNames | sort | uniq %}

<div id="iconset-preview-other" class="icons">
{% for icon in allIcons %}
  {% assign categoryLower = icon | downcase | split: "." %}
  {% assign plainCategory = categoryLower[0] %}

  {% assign otherIcon = true %}
  {% for catWithIcon in allCategories %}
    {% if catWithIcon.size <= plainCategory.size %}
      {% assign plainCategoryStart = plainCategory | truncate: catWithIcon.size, "" %}
      {% if plainCategoryStart == catWithIcon %}
        {% assign otherIcon = false %}
        {% break %}
      {% endif %}
    {% endif %}
  {% endfor %}

  {% if otherIcon == false %}
    {% continue %}
  {% endif %}

  {% unless icon contains "-" %}

    {% assign altText = "" %}
    {% for i in allIcons %}
      {% assign prefix = plainCategory | append: "-" %}    
      {% if i contains prefix %}
        {% assign iWithoutExt = i | split: "." %}
        {% assign altText = altText | append: iWithoutExt[0] | append: " " %}
      {% endif %}
    {% endfor %}
  
    <figure>
      <img src="icons/{{icon}}" alt="{{altText}}" title="{{altText}}">
      <figcaption>{{plainCategory}}</figcaption>
    </figure>
  {% endunless %}
{% endfor %}
</div>

EOF

echo "Finished."
## Contributing

Javascript linting, compressing and LESS compilation is handled through Gulp. Therefore, please run `gulp` instead of changing compressed CSS/JS manually. Default Gulp task will also check the code using ESLint.

Installing build dependencies:

```
npm install
```
## Basic UI

The Basic UI is a web interface based on Material Design Lite from Google.

### Features

* Responsive layout suitable for various screen sizes
* AJAX navigation
* Live update

### Configuration

```
org.eclipse.smarthome.basicui:defaultSitemap=demo
# Icons can be disabled
org.eclipse.smarthome.basicui:enableIcons=true
# Icons can be shown as PNG or SVG images
# Default: PNG
org.eclipse.smarthome.basicui:iconType=svg
```

### Accessing Sitemaps

The Basic UI has a default layout showing all things and their corresponding items. You may create your own sitemaps and access them through the basic UI in 2 ways.

1. Set the default sitemap via the Paper UI via Configuration -> Services -> Basic UI -> Configure, and set the Default Sitemap name.

2. Passing the "sitemap" parameter to the URL used to access the server.

Example: http://hostname:8080/basicui/app?sitemap=sitemapname


### Screenshots:

[![Screenshot 1](doc/screenshot-1.png)](doc/screenshot-1-full.png)
[![Screenshot 2](doc/screenshot-2.png)](doc/screenshot-2-full.png)

Bundle resources go in here!## Classic UI

The Classic UI is the original web user interface of openHAB 1 and thus is the most stable and widely used UI as of today.
Nonetheless, the look and feel does not match modern standards anymore, the [Basic UI](../basic/readme.html) is meant to be its successor.

The Classic UI is based on the [WebApp.Net](http://webapp-net.com/) framework and can be used by any (webkit-based) web browser. 

WebApp.Net consists mainly of Javascript and CSS files and thus has low expectations about the hardware capabilities of the client. In fact, it even works rather smoothly on an iPod 1st gen from 2008.

### Configuration

The Classic UI has a few configuration options, which can also be set through the [Paper UI](../paper/readme.html):

```
# Defining the default sitemap to use
org.eclipse.smarthome.classicui:defaultSitemap=demo

# The icon type to use, either png or svg
org.eclipse.smarthome.classicui:iconType=png

# Disable in-memory caching of html fragments
# If this is true, on every request the html files are loaded from disk (default is false)
org.eclipse.smarthome.classicui:disableHtmlCache=false
```

### Accessing Sitemaps

The Classic UI has a default layout showing all things and their corresponding items. You may create your own sitemaps and access them through the basic UI in 2 ways.

1. Set the default sitemap via the Paper UI via Configuration -> Services -> Classic UI -> Configure, and set the Default Sitemap name.

2. Passing the "sitemap" parameter to the URL used to access the server.

      Example: http://hostname:8080/classicui/app?sitemap=sitemapname

### Screenshots:

![Screenshot](doc/screenshot.png)

Bundle resources go in here!WebApp.Net -- http://webapp-net.com/
Copyright (c) 2008-2010, Chris Apers (Chrilith)
All rights reserved.

Full license: http://webapp-net.com/license.php

================================================================================
DISCLAIMER
================================================================================

The following discaimer applies to all the licenses below.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


================================================================================
WIP / BETA SOFTWARE LICENSE
================================================================================

Beta Version of WebApp.Net are provided for testing and evaluation purpose only.
You are not allowed to use Beta Version of WebApp.Net in production services
whether personal or commercial. The tools and/or features exposed in Beta
Version are not garanteed to be part of any future Release Version and are
subject to changes. You are not allowed to disclose all or part of the provided
Beta Version without specific prior written permission, regardless of the fact
this beta version is public or private.


================================================================================
RELEASE CANDIDATE SOFTWARE LICENSE
================================================================================

The same license as Release Version applies to Release Candidate Version
including the fact that some tools and/or features exposed in Release Candidate
Version might changes during the evaluation of this Release Candidate Version.


================================================================================
RELEASE SOFTWARE LICENSE
================================================================================

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the above disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of the WebApp.Net nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.
WebApp.Net 0.5.2 version (20100206)

A web application micro-framework for iPhone and iPod Touch,
webOS, Android and any other WebKit based browser

�2008-2010 Chris Apers - Read LICENSE.TXT for details
================================================================================
================================================================================

WebApp.Net has been designed to mimic the actual iPhone and iPod Touch graphic
user interface. It provides many powerful and easy to use items, based on
javascript and cascading style sheets technologies, to help you designing great
and must seen web applications for Apple's latest mobile devices.

WebApp.Net can be used with any server side technology (ASP.Net, PHP, ...).

================================================================================

A full features and changes list is available on the website.

Site     http://webapp-net.com/
Doc      http://webapp-net.com/Doc/
Forums   http://webapp-net.com/Forums/
Demo     http://demo.webapp-net.com/

Contact  chrilith@gmail.com# Paper UI 

The Paper UI is an HTML5 web application. The Paper UI implements Google's Material Design and is responsive, so that it smoothly renders on different screen sizes. All modern browsers (Safari, Chrome, Firefox) besides the Internet Explorer are supported in their newest version. The Internet Explorer is mainly lacking support for SSE.

Note that the Paper UI currently only supports limited use cases. It is mainly meant for setup and administration purposes, not for operation, for which you should rather refer to the [Basic UI](../basic/readme.html).

Even for setup and administration purposes, there are many features not yet available, which can be done through textual configuration, i.e. complex item definitions with grouping, sitemap definitions, textual rules and scripts, configuration of persistence, etc.
Therefore power users are advised to prefer textual configuration over the pure use of the Paper UI.

## Features

The following features are implemented:

* Inbox & discovery of Things
* Manual setup of Things
* Binding information
* Configuration of Things
* Configuration of services
* Event support for item state updates, Thing status updates and new inbox entries


## FAQ
 
### Why is it named Paper UI?
 
Google's Material Design approach uses so called "cards", which looks like paper. As the Paper UI also uses this card, it was decided to call it Paper UI.

### Why does it not support sitemaps?
 
Sitemaps require the Xtext DSL. The Paper UI aims to provide a full UI-only experience without any need for modifying configuration files. Thus the Paper UI can not make use of Sitemaps now, until it is refactored to have DSL support optional as it was done for items and things.
# macOS Text-to-Speech

## Overview

The macOS Text-to-Speech (TTS) service uses the macOS "say" command for producing spoken text.

Obviously, this service only works on a host that is running macOS.

## Configuration

There is no need to configure anything for this service.

## Voices

It automatically scans all available voices and registers them, see e.g.

```
> voice voices
mactts:Alex Alex (en_US)
mactts:Ioana Ioana (ro_RO)
mactts:Moira Moira (en_IE)
mactts:Sara Sara (da_DK)
mactts:Ellen Ellen (nl_BE)
mactts:Thomas Thomas (fr_FR)
mactts:Zosia Zosia (pl_PL)
mactts:Steffi Steffi (de_DE)
mactts:Amelie Amelie (fr_CA)
mactts:Veena Veena (en_IN)
mactts:Luciana Luciana (pt_BR)
mactts:Mariska Mariska (hu_HU)
mactts:Sinji Sin-ji (zh_HK)
mactts:Markus Markus (de_DE)
mactts:Zuzana Zuzana (cs_CZ)
mactts:Kyoko Kyoko (ja_JP)
mactts:Satu Satu (fi_FI)
mactts:Yuna Yuna (ko_KR)
...
```

## Supported Audio Formats

The MacTTS service produces audio streams using WAV containers and PCM (signed) codec with 16bit depth and 44.1kHz frequency.

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Eclipse Public License - Version 2.0</title>
    <style type="text/css">
      body {
        margin: 1.5em 3em;
      }
      h1{
        font-size:1.5em;
      }
      h2{
        font-size:1em;
        margin-bottom:0.5em;
        margin-top:1em;
      }
      p {
        margin-top:  0.5em;
        margin-bottom: 0.5em;
      }
      ul, ol{
        list-style-type:none;
      }
    </style>
  </head>
  <body>
    <h1>Eclipse Public License - v 2.0</h1>
    <p>THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
      PUBLIC LICENSE (&ldquo;AGREEMENT&rdquo;). ANY USE, REPRODUCTION OR DISTRIBUTION
      OF THE PROGRAM CONSTITUTES RECIPIENT&#039;S ACCEPTANCE OF THIS AGREEMENT.
    </p>
    <h2 id="definitions">1. DEFINITIONS</h2>
    <p>&ldquo;Contribution&rdquo; means:</p>
    <ul>
      <li>a) in the case of the initial Contributor, the initial content
        Distributed under this Agreement, and
      </li>
      <li>
        b) in the case of each subsequent Contributor:
        <ul>
          <li>i) changes to the Program, and</li>
          <li>ii) additions to the Program;</li>
        </ul>
        where such changes and/or additions to the Program originate from
        and are Distributed by that particular Contributor. A Contribution
        &ldquo;originates&rdquo; from a Contributor if it was added to the Program by such
        Contributor itself or anyone acting on such Contributor&#039;s behalf.
        Contributions do not include changes or additions to the Program that
        are not Modified Works.
      </li>
    </ul>
    <p>&ldquo;Contributor&rdquo; means any person or entity that Distributes the Program.</p>
    <p>&ldquo;Licensed Patents&rdquo; mean patent claims licensable by a Contributor which
      are necessarily infringed by the use or sale of its Contribution alone
      or when combined with the Program.
    </p>
    <p>&ldquo;Program&rdquo; means the Contributions Distributed in accordance with this
      Agreement.
    </p>
    <p>&ldquo;Recipient&rdquo; means anyone who receives the Program under this Agreement
      or any Secondary License (as applicable), including Contributors.
    </p>
    <p>&ldquo;Derivative Works&rdquo; shall mean any work, whether in Source Code or other
      form, that is based on (or derived from) the Program and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship.
    </p>
    <p>&ldquo;Modified Works&rdquo; shall mean any work in Source Code or other form that
      results from an addition to, deletion from, or modification of the
      contents of the Program, including, for purposes of clarity any new file
      in Source Code form that contains any contents of the Program. Modified
      Works shall not include works that contain only declarations, interfaces,
      types, classes, structures, or files of the Program solely in each case
      in order to link to, bind by name, or subclass the Program or Modified
      Works thereof.
    </p>
    <p>&ldquo;Distribute&rdquo; means the acts of a) distributing or b) making available
      in any manner that enables the transfer of a copy.
    </p>
    <p>&ldquo;Source Code&rdquo; means the form of a Program preferred for making
      modifications, including but not limited to software source code,
      documentation source, and configuration files.
    </p>
    <p>&ldquo;Secondary License&rdquo; means either the GNU General Public License,
      Version 2.0, or any later versions of that license, including any
      exceptions or additional permissions as identified by the initial
      Contributor.
    </p>
    <h2 id="grant-of-rights">2. GRANT OF RIGHTS</h2>
    <ul>
      <li>a) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free copyright
        license to reproduce, prepare Derivative Works of, publicly display,
        publicly perform, Distribute and sublicense the Contribution of such
        Contributor, if any, and such Derivative Works.
      </li>
      <li>b) Subject to the terms of this Agreement, each Contributor hereby
        grants Recipient a non-exclusive, worldwide, royalty-free patent
        license under Licensed Patents to make, use, sell, offer to sell,
        import and otherwise transfer the Contribution of such Contributor,
        if any, in Source Code or other form. This patent license shall
        apply to the combination of the Contribution and the Program if,
        at the time the Contribution is added by the Contributor, such
        addition of the Contribution causes such combination to be covered
        by the Licensed Patents. The patent license shall not apply to any
        other combinations which include the Contribution. No hardware per
        se is licensed hereunder.
      </li>
      <li>c) Recipient understands that although each Contributor grants the
        licenses to its Contributions set forth herein, no assurances are
        provided by any Contributor that the Program does not infringe the
        patent or other intellectual property rights of any other entity.
        Each Contributor disclaims any liability to Recipient for claims
        brought by any other entity based on infringement of intellectual
        property rights or otherwise. As a condition to exercising the rights
        and licenses granted hereunder, each Recipient hereby assumes sole
        responsibility to secure any other intellectual property rights needed,
        if any. For example, if a third party patent license is required to
        allow Recipient to Distribute the Program, it is Recipient&#039;s
        responsibility to acquire that license before distributing the Program.
      </li>
      <li>d) Each Contributor represents that to its knowledge it has sufficient
        copyright rights in its Contribution, if any, to grant the copyright
        license set forth in this Agreement.
      </li>
      <li>e) Notwithstanding the terms of any Secondary License, no Contributor
        makes additional grants to any Recipient (other than those set forth
        in this Agreement) as a result of such Recipient&#039;s receipt of the
        Program under the terms of a Secondary License (if permitted under
        the terms of Section 3).
      </li>
    </ul>
    <h2 id="requirements">3. REQUIREMENTS</h2>
    <p>3.1 If a Contributor Distributes the Program in any form, then:</p>
    <ul>
      <li>a) the Program must also be made available as Source Code, in
        accordance with section 3.2, and the Contributor must accompany
        the Program with a statement that the Source Code for the Program
        is available under this Agreement, and informs Recipients how to
        obtain it in a reasonable manner on or through a medium customarily
        used for software exchange; and
      </li>
      <li>
        b) the Contributor may Distribute the Program under a license
        different than this Agreement, provided that such license:
        <ul>
          <li>i) effectively disclaims on behalf of all other Contributors all
            warranties and conditions, express and implied, including warranties
            or conditions of title and non-infringement, and implied warranties
            or conditions of merchantability and fitness for a particular purpose;
          </li>
          <li>ii) effectively excludes on behalf of all other Contributors all
            liability for damages, including direct, indirect, special, incidental
            and consequential damages, such as lost profits;
          </li>
          <li>iii) does not attempt to limit or alter the recipients&#039; rights in the
            Source Code under section 3.2; and
          </li>
          <li>iv) requires any subsequent distribution of the Program by any party
            to be under a license that satisfies the requirements of this section 3.
          </li>
        </ul>
      </li>
    </ul>
    <p>3.2 When the Program is Distributed as Source Code:</p>
    <ul>
      <li>a) it must be made available under this Agreement, or if the Program (i)
        is combined with other material in a separate file or files made available
        under a Secondary License, and (ii) the initial Contributor attached to
        the Source Code the notice described in Exhibit A of this Agreement,
        then the Program may be made available under the terms of such
        Secondary Licenses, and
      </li>
      <li>b) a copy of this Agreement must be included with each copy of the Program.</li>
    </ul>
    <p>3.3 Contributors may not remove or alter any copyright, patent, trademark,
      attribution notices, disclaimers of warranty, or limitations of liability
      (&lsquo;notices&rsquo;) contained within the Program from any copy of the Program which
      they Distribute, provided that Contributors may add their own appropriate
      notices.
    </p>
    <h2 id="commercial-distribution">4. COMMERCIAL DISTRIBUTION</h2>
    <p>Commercial distributors of software may accept certain responsibilities
      with respect to end users, business partners and the like. While this
      license is intended to facilitate the commercial use of the Program, the
      Contributor who includes the Program in a commercial product offering should
      do so in a manner which does not create potential liability for other
      Contributors. Therefore, if a Contributor includes the Program in a
      commercial product offering, such Contributor (&ldquo;Commercial Contributor&rdquo;)
      hereby agrees to defend and indemnify every other Contributor
      (&ldquo;Indemnified Contributor&rdquo;) against any losses, damages and costs
      (collectively &ldquo;Losses&rdquo;) arising from claims, lawsuits and other legal actions
      brought by a third party against the Indemnified Contributor to the extent
      caused by the acts or omissions of such Commercial Contributor in connection
      with its distribution of the Program in a commercial product offering.
      The obligations in this section do not apply to any claims or Losses relating
      to any actual or alleged intellectual property infringement. In order to
      qualify, an Indemnified Contributor must: a) promptly notify the
      Commercial Contributor in writing of such claim, and b) allow the Commercial
      Contributor to control, and cooperate with the Commercial Contributor in,
      the defense and any related settlement negotiations. The Indemnified
      Contributor may participate in any such claim at its own expense.
    </p>
    <p>For example, a Contributor might include the Program
      in a commercial product offering, Product X. That Contributor is then a
      Commercial Contributor. If that Commercial Contributor then makes performance
      claims, or offers warranties related to Product X, those performance claims
      and warranties are such Commercial Contributor&#039;s responsibility alone.
      Under this section, the Commercial Contributor would have to defend claims
      against the other Contributors related to those performance claims and
      warranties, and if a court requires any other Contributor to pay any damages
      as a result, the Commercial Contributor must pay those damages.
    </p>
    <h2 id="warranty">5. NO WARRANTY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN &ldquo;AS IS&rdquo; BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING,
      WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT,
      MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is
      solely responsible for determining the appropriateness of using and
      distributing the Program and assumes all risks associated with its
      exercise of rights under this Agreement, including but not limited to the
      risks and costs of program errors, compliance with applicable laws, damage
      to or loss of data, programs or equipment, and unavailability or
      interruption of operations.
    </p>
    <h2 id="disclaimer">6. DISCLAIMER OF LIABILITY</h2>
    <p>EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT PERMITTED
      BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY
      LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
      OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST PROFITS),
      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
      LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
      OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS
      GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
    </p>
    <h2 id="general">7. GENERAL</h2>
    <p>If any provision of this Agreement is invalid or unenforceable under
      applicable law, it shall not affect the validity or enforceability of the
      remainder of the terms of this Agreement, and without further action by the
      parties hereto, such provision shall be reformed to the minimum extent
      necessary to make such provision valid and enforceable.
    </p>
    <p>If Recipient institutes patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Program itself
      (excluding combinations of the Program with other software or hardware)
      infringes such Recipient&#039;s patent(s), then such Recipient&#039;s rights granted
      under Section 2(b) shall terminate as of the date such litigation is filed.
    </p>
    <p>All Recipient&#039;s rights under this Agreement shall terminate if it fails to
      comply with any of the material terms or conditions of this Agreement and
      does not cure such failure in a reasonable period of time after becoming
      aware of such noncompliance. If all Recipient&#039;s rights under this Agreement
      terminate, Recipient agrees to cease use and distribution of the Program
      as soon as reasonably practicable. However, Recipient&#039;s obligations under
      this Agreement and any licenses granted by Recipient relating to the
      Program shall continue and survive.
    </p>
    <p>Everyone is permitted to copy and distribute copies of this Agreement,
      but in order to avoid inconsistency the Agreement is copyrighted and may
      only be modified in the following manner. The Agreement Steward reserves
      the right to publish new versions (including revisions) of this Agreement
      from time to time. No one other than the Agreement Steward has the right
      to modify this Agreement. The Eclipse Foundation is the initial Agreement
      Steward. The Eclipse Foundation may assign the responsibility to serve as
      the Agreement Steward to a suitable separate entity. Each new version of
      the Agreement will be given a distinguishing version number. The Program
      (including Contributions) may always be Distributed subject to the version
      of the Agreement under which it was received. In addition, after a new
      version of the Agreement is published, Contributor may elect to Distribute
      the Program (including its Contributions) under the new version.
    </p>
    <p>Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
      receives no rights or licenses to the intellectual property of any
      Contributor under this Agreement, whether expressly, by implication,
      estoppel or otherwise. All rights in the Program not expressly granted
      under this Agreement are reserved. Nothing in this Agreement is intended
      to be enforceable by any entity that is not a Contributor or Recipient.
      No third-party beneficiary rights are created under this Agreement.
    </p>
    <h2 id="exhibit-a">Exhibit A &ndash; Form of Secondary Licenses Notice</h2>
    <p>&ldquo;This Source Code may also be made available under the following 
        Secondary Licenses when the conditions for such availability set forth 
        in the Eclipse Public License, v. 2.0 are satisfied: {name license(s),
        version(s), and exceptions or additional permissions here}.&rdquo;
    </p>
    <blockquote>
      <p>Simply including a copy of this Agreement, including this Exhibit A
        is not sufficient to license the Source Code under Secondary Licenses.
      </p>
      <p>If it is not possible or desirable to put the notice in a particular file,
        then You may include the notice in a location (such as a LICENSE file in a
        relevant directory) where a recipient would be likely to look for
        such a notice.
      </p>
      <p>You may add additional accurate notices of copyright ownership.</p>
    </blockquote>
  </body>
</html>Copyright (c) 2014,${year} Contributors to the Eclipse Foundation
 
See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.
 
This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0 which is available at
http://www.eclipse.org/legal/epl-2.0
 
SPDX-License-Identifier: EPL-2.0
This place could be used to inject third party JARs to the target platform.
This mechanism works for the Eclipse IDE only because Tycho does not support the location types "Directory", "Installation", and "Features".

It allows us to add third party JARs for the development process.
Also if you need to test the Runtime with a third party bundle you can use this mechanism to add it easily to the launch configuration.

Drop the JARs to this directory, refresh the target platform, start coding / testing.
# <bindingName> Binding

_Give some details about what this binding is meant for - a protocol, system, specific device._

_If possible, provide some resources like pictures, a YouTube video, etc. to give an impression of what can be done with this binding. You can place such resources into a `doc` folder next to this README.md._

## Supported Things

_Please describe the different supported things / devices within this section._
_Which different types are supported, which models were tested etc.?_
_Note that it is planned to generate some part of this based on the XML files within ```ESH-INF/thing``` of your binding._

## Discovery

_Describe the available auto-discovery features here. Mention for what it works and what needs to be kept in mind when using it._

## Binding Configuration

_If your binding requires or supports general configuration settings, please create a folder ```cfg``` and place the configuration file ```<bindingId>.cfg``` inside it. In this section, you should link to this file and provide some information about the options. The file could e.g. look like:_

```
# Configuration for the Philips Hue Binding
#
# Default secret key for the pairing of the Philips Hue Bridge.
# It has to be between 10-40 (alphanumeric) characters 
# This may be changed by the user for security reasons.
secret=EclipseSmartHome
```

_Note that it is planned to generate some part of this based on the information that is available within ```ESH-INF/binding``` of your binding._

_If your binding does not offer any generic configurations, you can remove this section completely._

## Thing Configuration

_Describe what is needed to manually configure a thing, either through the (Paper) UI or via a thing-file. This should be mainly about its mandatory and optional configuration parameters. A short example entry for a thing file can help!_

_Note that it is planned to generate some part of this based on the XML files within ```ESH-INF/thing``` of your binding._

## Channels

_Here you should provide information about available channel types, what their meaning is and how they can be used._

_Note that it is planned to generate some part of this based on the XML files within ```ESH-INF/thing``` of your binding._

## Full Example

_Provide a full usage example based on textual configuration files (*.things, *.items, *.sitemap)._

## Any custom content here!

_Feel free to add additional sections for whatever you think should also be mentioned about your binding!_
