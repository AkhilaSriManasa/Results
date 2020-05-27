# Change log

This page describes the changes in each release.

To update your kit, see the [system updates guide][system-updates].
All system images can be downloaded from the [GitHub releases page][github-releases].

## AIY Kits Release 2019-11-13

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

Based on the [Raspbian Buster with desktop][raspbian].

**Fixes**

* Fix driver compilation errors on the latest Raspbian
* Fix HACKING.md instructions
* Fix gpiozero integration

**Improvements**

* Debian packages are now hosted at https://packages.cloud.google.com/
* Original Raspbian image is modified in the minimal way (no unnecessary packages)

## AIY Kits Release 2018-11-16

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

**Fixes**

* Fix tts engine click sound
* Fix `assistant_grpc_demo.service`: add DISPLAY environment variable and proper
systemd dependencies
* Fix various linter findings: python3 compatibility, wrong variable names, etc.

**Improvements**

* New `board.py` to access button and LED on all boards
* New audio API in `voice/audio.py`
* Direct python support for iNaturalist models
* Load anchors/labels directly from text files
* Add `get_inference_state()` and `resest()` to Vision Bonnet protocol
* Add Voice HAT schematic in `docs` folder
* Add sparse representation for output tensors to increase data transfer rate
* SVG-image overlay for video streaming (experimental)

## AIY Kits Release 2018-08-03

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

**Fixes**

* Fix PulseAudio infinite loop with Voice Bonnet
* Fix PulseAudio volume control
* Fix gpiozero LED on/off bug
* Fix local USB networking on macOS, no driver required
* Fix check_audio.py

**Improvements**

* Add Makefile for common shortcuts
* Add vision unit tests for all models and examples
* Add video streaming support (experimental)
* Add Google Cloud IoT support (experimental)
* Add more documentation (pinouts, drivers, troubleshooting, etc.)
* Add new code examples and update existing ones
* Add CHANGES.md to track release changes
* Remove unnecessary files (e.g. ALSA configs)
* Update vision driver to support mmap syscall
* Update sound driver to support latest Raspbian image
* Update HACKING.md

## AIY Kits Release 2018-04-13

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

## AIY Kits Release 2018-02-21

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

## AIY Kits Release 2017-12-18

Compatible with Voice HAT and Vision Bonnet.

## VoiceKit Classic Image 2017-09-11

Compatible with Voice HAT.

[github-releases]: https://github.com/google/aiyprojects-raspbian/releases
[system-updates]: https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/HACKING.md
[raspbian]: https://www.raspberrypi.org/downloads/raspbian/
# Contributing

We'd love to accept your patches and contributions to this project.
There are just a few small guidelines you need to follow.

## Scope of Contributions

This project consists of the support libraries (audio, gRPC, etc) required for
AIY Projects, as well as simple examples to experiment with and build upon.

Please limit pull requests to bug fixes or improvements to code or documentation
clarity. If you've added new examples and you'd like to publish your fork for
others to use, you can post on [hackster.io] or other channels.

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution,
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult [GitHub Help] for more
information on using pull requests.

[hackster.io]: https://www.hackster.io/
[GitHub Help]: https://help.github.com/articles/about-pull-requests/# Install the AIY Projects software

This page describes how to install all software for an AIY Vision Bonnet or Voice Bonnet.

If you're updating an existing AIY kit or starting from scratch, we recommend you [install our
pre-built image](#install-our-pre-build-aiy-projects-image). But if you have your own Raspbian
system that you'd like to use with an AIY kit, then you can
[install our software on your existing Raspbian system](#install-aiy-software-on-an-existing-raspbian-system).

## Install our pre-build AIY Projects image

To flash our latest pre-built system image onto an SD card, follow these steps:

1. Download the latest `.img.xz` file from our [releases page on GitHub][github-releases].
   (For release details, see the [Change log][changelog].)
1. Plug-in your MicroSD card to your computer with an adapter.
1. Use a program such as [balenaEtcher](https://www.balena.io/etcher/) to flash the `.img.xy` file
   onto your MicroSD card. (balenaEtcher is free and works on Windows, Mac, and Linux.)

When flashing is done, put the MicroSD card back in your kit and you're good to go!


## Install AIY software on an existing Raspbian system

Follow these steps to install the AIY drivers and software onto an existing Raspbian system.

**Note:** This process is compatible with Raspbian Buster (2019-06-20) or later only.
Before you start, be sure you have the latest version of [Raspbian][raspbian].

### 1. Add the AIY Debian packages repo

Add AIY package repo:

```bash
echo "deb https://packages.cloud.google.com/apt aiyprojects-stable main" | sudo tee /etc/apt/sources.list.d/aiyprojects.list
```

Add Google package keys:

```bash
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

Update and install the latest system updates (including kernel):

```bash
sudo apt-get update
sudo apt-get upgrade
```

Reboot after update:

```bash
sudo reboot
```

### 2. Install optional packages

#### RGB Button Driver

This package is needed only if you're using the light-up RGB button that's included with
the Vision/Voice Bonnet:

```bash
sudo apt-get install -y leds-ktd202x-dkms
```

Run `sudo modprobe leds_ktd202x` to load the driver and `sudo modprobe -r leds_ktd202x` to
unload it. Vision/Voice Bonnet does this automatically via built-in device tree overlay
saved in the board's EEPROM.

#### Piezo Buzzer Driver

This package is needed only if you're using the piezo buzzer included with the Vision Bonnet:

```bash
sudo apt-get install -y pwm-soft-dkms
```

#### Pi Zero Ethernet-over-USB

This package is needed only if you're using Ethernet-over-USB on Pi Zero:
```bash
sudo apt-get install -y aiy-usb-gadget
```
Default Pi IP address is `192.168.11.2`, host IP address will be assigned automatically.

#### Support for AIY Projects app

In order to make the Pi work with the [AIY Projects][aiy-app] app:

```bash
sudo apt-get install -y aiy-bt-prov-server
```

### 3. Install required packages

Use the following commands to install packages for either the
[Vision Bonnet](#install-vision-bonnet-packages) or the
[Voice Bonnet/HAT](#install-voice-bonnethat-packages).

#### Install Vision Bonnet packages

Install the bonnet drivers:

```bash
sudo apt-get install -y aiy-vision-dkms
```

Install the [example vision models][aiy-models]:

```bash
sudo apt-get install -y aiy-models
```

Install the optimized `protobuf` library for better performance:

```bash
sudo apt-get install -y aiy-python-wheels
```

Enable camera module:
```bash
echo "start_x=1" | sudo tee -a /boot/config.txt
```

Set GPU memory to 128MB:
```bash
echo "gpu_mem=128" | sudo tee -a /boot/config.txt
```

Reboot:

```bash
sudo reboot
```

Then verify that `dmesg` output contains `Myriad ready` message:

```bash
dmesg | grep -i "Myriad ready"
```

You can also verify that camera is working fine by watching video on the
connected monitor:
```bash
raspivid -t 0
```

Or use `ffplay` to get video output on the host machine:
```bash
ssh pi@raspberrypi.local "raspivid --nopreview --timeout 0 -o -" | ffplay -loglevel panic -
```

#### Install Voice Bonnet/HAT packages

Install the bonnet/HAT drivers:

```bash
sudo apt-get install -y aiy-voicebonnet-soundcard-dkms
```

Disable built-in audio:

```bash
sudo sed -i -e "s/^dtparam=audio=on/#\0/" /boot/config.txt
```

Install PulseAudio:

```bash
sudo apt-get install -y pulseaudio
sudo mkdir -p /etc/pulse/daemon.conf.d/
echo "default-sample-rate = 48000" | sudo tee /etc/pulse/daemon.conf.d/aiy.conf
```

If you want to use Google Assistant, install the Raspberry-Pi-compatible
`google-assistant-library` python library:

```bash
sudo apt-get install -y aiy-python-wheels
```

Reboot:

```bash
sudo reboot
```

Then verify that you can record audio:

```bash
arecord -f cd test.wav
```

...and play a sound:

```bash
aplay test.wav
```

Additionally, the Voice Bonnet/HAT requires access to Google Cloud APIs.
To complete this setup, follow the [Voice Kit setup instructions][aiy-voice-setup].


### 4. Install the AIY Projects Python library

Finally, you need to install the [AIY Projects Python library](
https://aiyprojects.readthedocs.io/en/latest/index.html).

First make sure you have `git` installed:

```bash
sudo apt-get install -y git
```

Then clone this `aiyprojects-raspbian` repo from GitHub:

```bash
git clone https://github.com/google/aiyprojects-raspbian.git AIY-projects-python
```

And now install the Python library in editable mode:

```bash
sudo pip3 install -e AIY-projects-python
```

## Appendix: List of all AIY Debian packages

The following is just a reference of all packages that are installed when you
follow the above steps.

### Vision and Voice Bonnets

* `aiy-dkms` contains MCU drivers:

  * `aiy-io-i2c` &mdash; firmware update support
  * `pwm-aiy-io` &mdash; [PWM][kernel-pwm] sysfs interface
  * `gpio-aiy-io` &mdash; [GPIO][kernel-gpio] sysfs interface
  * `aiy-adc`  &mdash; [Industrial I/O][kernel-iio] ADC interface

* `aiy-io-mcu-firmware` contains MCU firmware update service
* `leds-ktd202x-dkms` contains `leds-ktd202x` LED driver
* `pwm-soft-dkms` contains `pwm-soft` software PWM driver

* `aiy-python-wheels` contains optimized `protobuf` python
wheel (until [this issue][protobuf-issue] is fixed) along with [Google Assistant Library][assistant-library] for different Raspberry Pi boards.

### Vision Bonnet

* `aiy-vision-dkms` contains `aiy-vision` Myriad driver
* `aiy-vision-firmware` contains Myriad firmware
* `aiy-models` contains [models][aiy-models] for on-device inference:

  * Face Detection
  * Object Detection
  * Image Classification
  * Dish Detection
  * Dish Classification
  * iNaturalist Classification (plants, insects, birds)

### Voice Bonnet

* `aiy-voicebonnet-soundcard-dkms` contains sound drivers:

  * `rl6231`
  * `rt5645`
  * `snd_aiy_voicebonnet`


[changelog]: CHANGES.md
[raspbian]: https://www.raspberrypi.org/downloads/raspbian/
[image-flash]: https://www.raspberrypi.org/documentation/installation/installing-images/
[aiy-models]: https://aiyprojects.withgoogle.com/models/
[github-releases]: https://github.com/google/aiyprojects-raspbian/releases
[aiy-voice-setup]: https://aiyprojects.withgoogle.com/voice#google-assistant--get-credentials
[assistant-library]: https://pypi.org/project/google-assistant-library/
[protobuf-issue]: https://github.com/bennuttall/piwheels/issues/97
[kernel-pwm]: https://www.kernel.org/doc/Documentation/pwm.txt
[kernel-gpio]: https://www.kernel.org/doc/Documentation/gpio/sysfs.txt
[kernel-iio]: https://www.kernel.org/doc/Documentation/driver-api/iio/core.rst
[aiy-app]: https://play.google.com/store/apps/details?id=com.google.android.apps.aiy

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
# AIY Projects

This repository contains an easy-to-use Python API for the [AIY Vision Kit][aiy-vision]
and [AIY Voice Kit][aiy-voice]. The code for all AIY kits is in the `aiyprojects` branch,
and is included in images starting with `aiyprojects-2017-12-18.img`.
The previous `voicekit` branch contains code just for the Voice Kit, and the
`master` branch contains the original deprecated `Voice Recognizer` demo.

## Documentation

If you're just getting started with the Vision or Voice kit, see the
assembly guide and other maker guides at [aiyprojects.withgoogle.com].

If you just need the Python API reference, see [aiyprojects.readthedocs.io].
Also have a look at the [example code][aiy-github-examples].

If you want to flash the latest AIY system image or install AIY packages on an existing
Raspbian system, read the [system updates guide][HACKING.md].

## Releases

* [Image downloads][downloads]
* [Change log][changelog]

## Bugs & Support

If you've found a bug, please [review the known issues and report a new one][aiy-github-issues].

If you've fixed a bug yourself, please send us a pull request!
For details, read [CONTRIBUTING.md].

If you're having trouble assembling your kit or running the demos, try the following links:

* [AIY Help docs][help-docs]
* [AIY Forums][aiy-forums]
* [AIY Stack Overflow][aiy-stack-overflow]
* [AIY GitHub Issues][aiy-github-issues]
* support-aiyprojects@google.com

If you've found a problem with the Assistant API (for example, it crashes
or provides incorrect responses), try the following:

* [Assistant Stack Overflow][assistant-stack-overflow]
* [Assistant GitHub Issues][assistant-github-issues]

##

<p align="center">
  <img width="15%" src="https://aiyprojects.withgoogle.com/static/images/icons/aiy-circular-logo.svg">
</p>

[HACKING.md]: HACKING.md
[CONTRIBUTING.md]: CONTRIBUTING.md
[downloads]: https://github.com/google/aiyprojects-raspbian/releases
[changelog]: CHANGES.md

[aiyprojects.withgoogle.com]: https://aiyprojects.withgoogle.com
[aiyprojects.readthedocs.io]: https://aiyprojects.readthedocs.io
[aiy-vision]: https://aiyprojects.withgoogle.com/vision/
[aiy-voice]: https://aiyprojects.withgoogle.com/voice/

[help-docs]: https://aiyprojects.withgoogle.com/help
[aiy-forums]: https://www.raspberrypi.org/forums/viewforum.php?f=114
[aiy-stack-overflow]: https://stackoverflow.com/questions/tagged/google-aiy
[aiy-github-issues]: https://github.com/google/aiyprojects-raspbian/issues
[aiy-github-examples]: https://github.com/google/aiyprojects-raspbian/tree/aiyprojects/src/examples

[assistant-stack-overflow]: https://stackoverflow.com/questions/tagged/google-assistant-sdk
[assistant-github-issues]: https://github.com/googlesamples/assistant-sdk-python/issues
.. |code| raw:: html

    <code>

.. |endcode| raw:: html

    </code># Documentation

This directory holds the source files required to build the AIY Python reference with Sphinx.

You can see the generated files at [aiyprojects.readthedocs.io](https://aiyprojects.readthedocs.io/).

If you've downloaded the [aiyprojects-raspbian](https://github.com/google/aiyprojects-raspbian)
repository, you can build these docs locally with the `make docs` command. Of course, this requires
that you install Sphinx and other Python dependencies:

    # We require Python3, so if that's not your default, first start a virtual environment:
    python3 -m venv ~/.aiy_venv
    source ~/.aiy_venv/bin/activate

    # Move to the aiyprojects-raspbian repo root...

    # Install the dependencies:
    python3 -m pip install -r docs/requirements.txt

    # Build the docs:
    make docs

The results are output in `docs/_build/html/`.

**Note:** These output files should not be committed to this repository. We use readthedocs.org
to generate the HTML documentation directly from GitHub—this repo holds the *source files
only*, not the built files.

For more information about the syntax in these RST files, see the [reStructuredText documentation](
http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).
# Python packages required to build the docs
sphinx
sphinx_rtd_theme
recommonmark
Pillow
# Vision Kit overview

<img src="_static/images/vision-kit.png" class="attempt-right" alt=""
width="200"/>

The AIY Vision Kit is a do-it-yourself intelligent camera built with a
Raspberry Pi and the Vision Bonnet.

After you assemble the kit and run the included demos,
you can extend the kit with your own software and hardware.

Also see the [Vision Kit assembly guide](
https://aiyprojects.withgoogle.com/vision/).

## Software

To execute ML models and perform other actions with the Vision Kit, the
system image includes the Python library with the following modules:

* [`aiy.toneplayer`](aiy.toneplayer.html):
A simple melodic music player for the piezo buzzer.
* [`aiy.trackplayer`](aiy.trackplayer.html):
A tracker-based music player for the piezo buzzer.
* [`aiy.vision.annotator`](aiy.vision.annotator.html):
An annotation library that draws overlays on the Raspberry Pi’s camera preview.
* [`aiy.vision.inference`](aiy.vision.inference.html):
An inference engine that communicates with the Vision Bonnet from the Raspberry
Pi side.
* [`aiy.vision.models`](aiy.vision.models.html):
A collection of modules that perform ML inferences with specific types of image
classification and object detection models.
* [`aiy.board`](aiy.board.html):
APIs to use the button that’s attached to the Vision Bonnet’s button connector.
* [`aiy.leds`](aiy.leds.html):
APIs to control certain LEDs, such as the LEDs in the button and the privacy
LED.
* [`aiy.pins`](aiy.pins.html):
Pin definitions for the bonnet's extra GPIO pins, for use with gpiozero.


## Vision Bonnet

### Hardware

* SOC: `Myriad 2450`
* MCU: `ATSAMD09D14` [I&sup2;C address: `0x51`]
* LED Driver: `KTD2027A` [I&sup2;C address: `0x30`]
* Crypto (optional): `ATECC608A` [I&sup2;C address: `0x60`]
* IMU: `BMI160`

### Drivers

* MCU driver: `modinfo aiy-io-i2c`
* MCU PWM driver: `modinfo pwm-aiy-io`
* MCU GPIO driver: `modinfo gpio-aiy-io`
* MCU ADC driver: `modinfo aiy-adc`
* LED driver: `modinfo leds-ktd202x`
* Software PWM driver for buzzer: `modinfo pwm-soft`
* Myriad driver: `modinfo aiy-vision`

To reset MCU:
```
echo 1 | sudo tee /sys/bus/i2c/devices/1-0051/reset
```

To get MCU status message (including firmware version) and last error code:
```
cat /sys/bus/i2c/devices/1-0051/{status_message,error_code}
```

### Pinout (40-pin header)

```
                   3.3V --> 1    2 <-- 5V
                I2C_SDA --> 3    4 <-- 5V
                I2C_SCL --> 5    6 <-- GND
                            7    8
                    GND --> 9   10
                            11  12
                            13  14 <-- GND
  (GPIO_22) BUZZER_GPIO --> 15  16 <-- BUTTON_GPIO (GPIO_23)
                   3.3V --> 17  18
               SPI_MOSI --> 19  20 <-- GND
               SPI_MISO --> 21  22
               SPI_SCLK --> 23  24 <-- SPI_CE_MRD
                    GND --> 25  26
                 ID_SDA --> 27  28 <-- ID_SCL
                            29  30 <-- GND
          PI_TO_MRD_IRQ --> 31  32
          MRD_TO_PI_IRQ --> 33  34 <-- GND
                            35  36
             MRD_UNUSED --> 37  38
                    GND --> 39  40
```

Also see the [Vision Bonnet on pinout.xyz](https://pinout.xyz/pinout/aiy_vision_bonnet).

## Troubleshooting

See the [Vision Kit help](https://aiyprojects.withgoogle.com/help#vision-kit).
# Voice Kit overview

<img src="_static/images/voice-kit.png" class="attempt-right" alt="" width="200"/>

The AIY Voice Kit is a do-it-yourself intelligent speaker built with a
Raspberry Pi and the Voice Bonnet (or Voice HAT if using the V1 Voice Kit).

After you assemble the kit and run the included demos,
you can extend the kit with your own software and hardware.

Also see the [Voice Kit assembly guide](https://aiyprojects.withgoogle.com/voice/).

## Software

To interact with the Google Assistant, convert speech to text, and perform other
actions with the Voice Kit, the system image includes Python library with the
following modules:

* [`aiy.assistant`](aiy.assistant.html):
A collection of modules that simplify interaction with the Google Assistant API.
* [`aiy.cloudspeech`](aiy.cloudspeech.html):
APIs to simplify interaction with the Google Cloud Speech-to-Text service.
* [`aiy.voice.audio`](aiy.voice.audio.html):
APIs to record and play audio files.
* [`aiy.voice.tts`](aiy.voice.tts.html):
An API that performs text-to-speech.
* [`aiy.board`](aiy.board.html):
APIs to use the button that’s attached to the Voice Bonnet’s button connector.
* [`aiy.leds`](aiy.leds.html):
APIs to control certain LEDs, such as the LEDs in the button and the privacy
LED.
* [`aiy.pins`](aiy.pins.html):
Pin definitions for the bonnet's extra GPIO pins, for use with gpiozero.

## Voice Bonnet (Voice Kit V2)

### Hardware

* Audio Codec: `ALC5645` [I&sup2;C address: `0x1A`]
* MCU: `ATSAMD09D14` [I&sup2;C address: `0x52`]
* LED Driver: `KTD2027B` [I&sup2;C address: `0x31`]
* Crypto (optional): `ATECC608A` [I&sup2;C address: `0x62`]
* Microphone: `SPH1642HT5H-1` x 2

### Drivers

* MCU driver: `modinfo aiy-io-i2c`
* MCU PWM driver: `modinfo pwm-aiy-io`
* MCU GPIO driver: `modinfo gpio-aiy-io`
* MCU ADC driver: `modinfo aiy-adc`
* LED driver: `modinfo leds-ktd202x`
* Software PWM driver for buzzer: `modinfo pwm-soft`
* Sound drivers: `modinfo rl6231 rt5645 snd_aiy_voicebonnet`

### Pinout (40-pin header)

```
       3.3V --> 1    2 <-- 5V
                3    4 <-- 5V
                5    6 <-- GND
                7    8
        GND --> 9   10
                11  12 <-- I2S_BCLK
                13  14 <-- GND
                15  16 <-- BUTTON_GPIO (GPIO_23)
       3.3V --> 17  18
                19  20 <-- GND
                21  22 <-- LED_GPIO (GPIO_25)
                23  24
        GND --> 25  26
     ID_SDA --> 27  28 <-- ID_SCL
                29  30 <-- GND
                31  32
                33  34 <-- GND
  I2S_LRCLK --> 35  36 <-- AMP_ENABLE
                37  38 <-- I2S_DIN
        GND --> 39  40 <-- I2S_DOUT
```

Also see the [Voice Bonnet on pinout.xyz](https://pinout.xyz/pinout/aiy_voice_bonnet).


## Voice HAT (Voice Kit V1)

### Hardware

* Audio Amplifier: `MAX98357A`
* Microphone: `ICS-43432` x 2

### Schematics

* [Main Board](https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/schematics/voice_hat/voice_hat.pdf)
* [Microphone Board](https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/schematics/voice_hat/voice_hat_mic.pdf)

### Drivers

* [googlevoicehat-codec.c](https://github.com/raspberrypi/linux/blob/rpi-4.14.y/sound/soc/bcm/googlevoicehat-codec.c)
* [googlevoicehat-soundcard.c](https://github.com/raspberrypi/linux/blob/rpi-4.14.y/sound/soc/bcm/googlevoicehat-soundcard.c)
* [googlevoicehat-soundcard-overlay.dts](https://github.com/raspberrypi/linux/blob/rpi-4.14.y/arch/arm/boot/dts/overlays/googlevoicehat-soundcard-overlay.dts)

Manual overlay load:
```
sudo dtoverlay googlevoicehat-soundcard
```

Load overlay on each boot:
```
echo "dtoverlay=googlevoicehat-soundcard" | sudo tee -a /boot/config.txt
```

### Pinout (40-pin header)

```
       3.3V --> 1    2 <-- 5V
    I2C_SDA --> 3    4 <-- 5V
    I2C_SCL --> 5    6 <-- GND
                7    8
        GND --> 9   10
                11  12 <-- I2S_BCLK
                13  14 <-- GND
                15  16 <-- BUTTON_GPIO (GPIO_23)
       3.3V --> 17  18
                19  20 <-- GND
                21  22
                23  24
        GND --> 25  26
     ID_SDA --> 27  28 <-- ID_SCL
                29  30 <-- GND
                31  32
                33  34 <-- GND
  I2S_LRCLK --> 35  36
                37  38 <-- I2S_DIN
        GND --> 39  40 <-- I2S_DOUT
```

Also see the [Voice HAT on pinout.xyz](https://pinout.xyz/pinout/voice_hat).

## Troubleshooting

See the [Voice Kit help](https://aiyprojects.withgoogle.com/help#voice-kit).
Broadway
https://github.com/mbebenita/Broadway

Copyright (c) 2011, Project Authors (see AUTHORS file)
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

  *  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
  *  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
  *  Neither the names of the Project Authors nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

--

The 3-clause BSD above applies to all code except for code originating
from the Android project (the .cpp files in Avc/). Those files are under
the Android project's Apache 2.0 license.
# Streaming protocol specification

Server streams data to clients. There is only one server and there can be zero
or more connected clients.

## Messages from Server to Client (ClientBound)

Each server streaming session must start with `ClientBound{start}` and
stop with `ClientBound{stop}` messages. Interleaved  `ClientBound{video}`
and `ClientBound{overlay}` are allowed in between:

```
-> ClientBound{start={width=<width>, height=<height>}}

-> ClientBound{video} or ClientBound{overlay}

-> ClientBound{stop}
```

Each video message contains one or more H264 encoded NAL units. Partial NAL
units are not allowed. The first NAL unit must be SPS (Sequence Parameter Set),
the second one is IDR. Concatenation of all video messages should produce a
valid H264 bitstream. All subsequent SPS NAL units must contain the same
information as the first one.

Overlay messages are allowed at any time. You can think that there are two
logical streams during the session: video stream and stream of overlays.
Each overlay message contains SVG image which is drawn on top of the video.

## Messages from Client to Server (ServerBound)

Client can control the server by sending `ServerBound{stream_control}` messages.
There are only two allowed: `ServerBound{stream_control={enabled=true}}` to
start streaming and `ServerBound{stream_control={enabled=false}}` to stop
streaming. Server could ignore these messages if it is already in the requested
state.

```
<- ServerBound{stream_control={enabled=true}}


<- ServerBound{stream_control={enabled=false}}

```

## Example

From the Server's point of view ordered by absolute time:

```
<- ServerBound{stream_control={enabled=true}}
-> ClientBound{start={width=720, height=480}}
-> ClientBound{overlay={svg=<DATA>}
-> ClientBound{video={<SPS>}}  # First NAL unit in video stream
-> ClientBound{overlay={svg=<DATA>}
-> ClientBound{video={<IDR>}}  # Second NAL unit in video stream
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{overlay={svg=<DATA>}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{overlay={svg=<DATA>}
-> ClientBound{video={<SPS>}}  # The same as the first SPS NAL unit.
-> ClientBound{video={<IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{overlay={svg=<DATA>}
<- ServerBound{stream_control={enabled=false}}
-> ClientBound{video={<IDR>}}
-> ClientBound{video={<NON-IDR>}}
-> ClientBound{stop}
```

## References

[Protocol Buffers](https://developers.google.com/protocol-buffers/)
[H264 Specification](https://www.itu.int/rec/T-REC-H.264-201704-I)
[SVG Specification](https://www.w3.org/TR/SVG11/)
# Image classification demo

## Physical Setup

-   VisionHat installed on a Raspberry Pi Zero
-   Servo connected to vision hat (signal - PIN_A, Vcc - POWER, Ground - GND)
    -   Servo mounted in label display
-   (optional) Monitor connected to raspberry pi.
catamaran
container ship/containership/container vessel
lifeboat
speedboat
paddle/boat paddle
pirate/pirate ship
paddlewheel/paddle wheel
submarine/pigboat/sub/U-boat
fireboat
