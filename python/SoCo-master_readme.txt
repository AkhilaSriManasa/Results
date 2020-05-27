The MIT License (MIT)
=====================

Copyright (c) Rahim Sonawalla and individual contributors (see AUTHORS)

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
THE SOFTWARE.SoCo
====

SoCo (Sonos Controller) is a Python project that allows you to
programmatically control `Sonos speakers`_. It was originally created at `Music
Hack Day Sydney`_ by `Rahim Sonawalla`_ and is now developed by a `team of
people`_ at its `GitHub repository`_

For more background on the project, please see Rahim's `blog post
<http://www.hirahim.com/blog/2012/04/29/dissecting-the-sonos-controller/>`_.

Visit the `SoCo documentation`_ for a more detailed overview of all the functionailty.

.. image:: https://badges.gitter.im/SoCo/SoCo.svg
   :alt: Join the chat at https://gitter.im/SoCo/SoCo
   :target: https://gitter.im/SoCo/SoCo?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://travis-ci.com/SoCo/SoCo.svg?branch=master
   :target: https://travis-ci.com/SoCo/SoCo
   :alt: Build Status

.. image:: https://img.shields.io/requires/github/SoCo/SoCo/master.svg?style=flat
   :target: https://requires.io/github/SoCo/SoCo/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://img.shields.io/pypi/v/soco.svg?style=flat
    :target: https://pypi.python.org/pypi/soco/
    :alt: Latest PyPI version

WARNING
-------

Sonos has changed the way music service account information is available. This means that **currently a group of music service will give authentication issues and cannot be used at all**. Known members of this group are: Google Play Music, Apple Music, Amazon Music, Spotify and Napster.

Issue #557 is a meta issue for this problem and you can use that to track progress on solving the issues, but
*please refrain from posting "me too" comments* in there. Also, there is no need to open any more separate issue about this.

If you have another music service that should be on the list, comment in #557

Installation
------------

SoCo requires Python 2.7, or 3.4 or newer.

Use pip:

``pip install soco``


SoCo depends on the `Requests`_ HTTP library. If you use pip to install Soco,
Requests will be installed automatically for you. If not, you can use:

``pip install requests``


Basic Usage
-----------

You can interact with a Sonos Zone Player through a SoCo object. If you know
the IP address of a Zone Player, you can create a SoCo object directly:

.. code:: python

    >>> from soco import SoCo
    >>> my_zone = SoCo('192.168.1.101')
    >>> my_zone.player_name
    Kitchen
    >>> my_zone.status_light = True
    >>> my_zone.volume = 6


But perhaps the easiest way is to use the module-level `discover` function.
This will find all the Zone Players on your network, and return a python
set containing them:

.. code:: python

    >>> import soco
    >>> for zone in soco.discover():
    ...        print zone.player_name
    Living Room
    Kitchen


If you prefer a list to a set:

.. code:: python

    >>> zone_list = list(soco.discover())
    >>> zone_list
    [SoCo("192.168.1.101"), SoCo("192.168.1.102")]
    >>> zone_list[0].mute = True

Of course, you can also play music!

.. code:: python

    #!/usr/bin/env python
    from soco import SoCo

    if __name__ == '__main__':
        sonos = SoCo('192.168.1.102') # Pass in the IP of your Sonos speaker
        # You could use the discover function instead, if you don't know the IP

        # Pass in a URI to a media file to have it streamed through the Sonos
        # speaker
        sonos.play_uri(
            'http://ia801402.us.archive.org/20/items/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy.mp3')

        track = sonos.get_current_track_info()

        print track['title']

        sonos.pause()

        # Play a stopped or paused track
        sonos.play()

Support
-------

If you need support for SoCo, feel free to post your question either on our `Google Group`_ or on the #soco IRC channel on `freenode`_.

Example Applications
--------------------

To show off what can be made with SoCo, a simple web application is included in
the ``examples`` folder.

.. figure:: https://github.com/SoCo/SoCo/raw/master/examples/webapp/screenshot.png
   :alt: Screenshot of web app

   Screenshot of web app


Features
--------

SoCo supports the following controls amongst others:

-  Play, Pause, Stop
-  Next track, Previous track
-  Volume get and set
-  Mute (or unmute)
-  Get current transport information (if speaker is
   playing, paused or stopped)
-  Get information about the currently playing track

   -  Track title
   -  Artist
   -  Album
   -  Album Art (if available)
   -  Track length
   -  Duration played (for example, 30 seconds into a 3 minute song)
   -  Playlist position (for example, item 5 in the playlist)
   -  Track URI

-  Receive events when the player state changes
-  Search for and play music items:

   -  Local music library
   -  Webradio via TuneIn and music services (still unstable)
   -  Saved Sonos favorites, favorite radio stations and shows

-  Switch the speaker’s source to line-in or TV input (if the Zone Player
   supports it)
-  Manage the Sonos queue:

   -  Get the items in the queue
   -  Add items to the queue
   -  Clear the queue
   -  Play a specific song from the queue

-  Join or unjoin speakers from a group
-  Put all Sonos speakers in a network into “party mode”.

-  Get or set alarms
-  Get or set sleep timers

-  Get or set the speaker’s bass and treble EQ
-  Toggle the speaker’s loudness compensation, night mode and dialog mode
-  Toggle the white status light on the unit
-  Get the speaker’s information

   -  Zone Name
   -  Zone Icon
   -  UID (usually something like RINCON\_XXXXXXXXXXXXXXXXX)
   -  Serial Number
   -  Software version
   -  Hardware version
   -  MAC Address

-  Set the speaker’s Zone Name
-  Start a music library update and determine if one is in progress

SoCo also supports lower level access from Python to all Sonos services
(e.g. ContentDirectory or RenderingControl).


Related Projects
----------------

Socos is a command line tool for controlling Sonos devices. It is developed
in conjunction with Soco, but in a `separate repository <https://github.com/SoCo/socos>`_.

More of a Ruby fan? Not a problem, `Sam Soffes`_ is building out an
awesome `Ruby gem`_.

Looking for a GUI that’s more than just a sample project? `Joel
Björkman`_ is building a Sonos Controller GUI–great for folks on Linux
where there isn’t an official Sonos Controller application! Find, fork,
and contribute to it here: https://github.com/labero/SoCo-Tk.


Google Group
------------

There is a Soco group over at `Google Groups`_.  Feel free to drop by for support, ideas or casual conversation related to SoCo.


License
-------

SoCo is released under the `MIT license`_.


.. _Sonos speakers: http://www.sonos.com/system/
.. _Music Hack Day Sydney: http://sydney.musichackday.org/2012/
.. _blog post: http://www.hirahim.com/blog/2012/04/29/dissecting-the-sonos-controller/
.. _Requests: http://docs.python-requests.org/
.. _Sam Soffes: https://github.com/soffes
.. _Ruby gem: https://github.com/soffes/sonos
.. _Joel Björkman: https://github.com/labero
.. _MIT license: http://www.opensource.org/licenses/mit-license.php
.. _Rahim Sonawalla: https://github.com/rahims/SoCo
.. _GitHub repository: https://github.com/SoCo/SoCo
.. _team of people: https://github.com/SoCo/SoCo/blob/master/AUTHORS.rst
.. _Google Groups: https://groups.google.com/forum/#!forum/python-soco
.. _Google Group: https://groups.google.com/forum/#!forum/python-soco
.. _SoCo documentation: https://soco.readthedocs.org/en/latest/
.. _freenode: https://freenode.net/
sphinx >=1.3
sphinx_rtd_theme
pytest >= 2.5
mock >= 1.0.1
graphviz
flake8
pylint >= 1.4
coveralls
pytest-cov>=2.4.0
wheel
requests
xmltodict
tunein.py will play a radio preset from the TuneIn service on your Sonos system.

For a great example of a command line Sonos contoller using SoCo, see
https://github.com/SoCo/socos# SoCo Web App
This example demonstrates a basic web-based Sonos controller built with SoCo.

![Screenshot of web app](https://github.com/SoCo/SoCo/raw/master/examples/webapp/screenshot.png)

## Set up
This example depends on several external libraries. The easiest way to install everything is by running the following command:

`pip install -r requirements.txt`

Once all dependanices have been installed, rename `settings.py.example` to `settings.py` and edit the file.

### Album Art
In order to show album art, this example makes use of the [Rovi API](http://developer.rovicorp.com). If you'd like to have album art, you'll need to sign up for your own (free) API key. You can do so by going to their [Developer Portal](http://developer.rovicorp.com) and clicking on "Register" at the top right of the page. API keys are issued automatically, but Album Art must be manually enabled for accounts. Simply send an e-mail to [apisupport@rovicorp.com](apisupport@rovicorp.com) and ask that it be enabled for your account.

## Basic Usage
Run `python index.py` to start the application. Then open up a web browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000).

## License
Copyright (C) 2012 Rahim Sonawalla ([rsonawalla@gmail.com](mailto:rsonawalla@gmail.com) / [@rahims](http://twitter.com/rahims)).

Released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).
Flask
soco