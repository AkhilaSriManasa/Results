Credits
=======
  - Showdown v0
    * [Srikanth Ronanki](https://github.com/ronanki)<br/>
      Bug fixing and current Github project maintainer
      
  - Original Project
    * [Zhizheng Wu](http://www.zhizheng.org/)<br/>
      Main contributor
    * [Oliver Watts](http://homepages.inf.ed.ac.uk/owatts/)<br/>
      Main contributor
# INSTALL

To install Merlin, `cd` merlin and run the below steps:

- Install some basic tools in Merlin
```sh
bash tools/compile_tools.sh
```
- Install python dependencies
```sh
pip install -r requirements.txt
```

## More advanced instructions

1. go to `tools/`  and follow INSTALL instructions there.
2. Merlin is coded in python and need third-party python libraries such as:

#### numpy, scipy, matplotlib, lxml 

- Usually shipped with your python packages 
- Available in Ubuntu packages

#### theano

- Can be found on pip
- Need version 0.7 and above
- http://deeplearning.net/software/theano

#### bandmat

- Can be found on pip
- https://pypi.python.org/pypi/bandmat

#### For running on NVIDIA GPU, you will need also CUDA

- https://developer.nvidia.com/cuda-zone

#### and you might want also CUDNN [optionnal]

- https://developer.nvidia.com/cudnn

### Computational efficiency
    
- Computationnal efficiency is obviously greatly improved using GPU.
- It is also improved using the latest versions of theano and numpy.

## Some Linux Instructions

#### For Ubuntu: 
```sh
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git libc6-dev-i386 glibc-devel.i686 csh
```

#### For Fedora: 
```sh
sudo yum install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git libc6-dev-i386 glibc-devel.i686 csh python-lxml libxslt-devel unzip
```

#### Common libraries for both Ubuntu and Fedora:
```sh
sudo env "PATH=$PATH" pip install Theano
sudo env "PATH=$PATH" pip install matplotlib
sudo env "PATH=$PATH" pip install bandmat
sudo env "PATH=$PATH" pip install lxml
```

#### For all stand-alone machines:
- If you are not a sudo user, this [post](https://cstr-edinburgh.github.io/install-merlin/) may help you install Merlin.

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
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright {yyyy} {name of copyright owner}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
[![Build Status](https://travis-ci.org/CSTR-Edinburgh/merlin.svg?branch=master)](https://travis-ci.org/CSTR-Edinburgh/merlin)

## Merlin: The Neural Network (NN) based Speech Synthesis System

This repository contains the Neural Network (NN) based Speech Synthesis System  
developed at the Centre for Speech Technology Research (CSTR), University of 
Edinburgh. 

Merlin is a toolkit for building Deep Neural Network models for statistical parametric speech synthesis. 
It must be used in combination with a front-end text processor (e.g., Festival) and a vocoder (e.g., STRAIGHT or WORLD).

The system is written in Python and relies on the Theano numerical computation library.

Merlin comes with recipes (in the spirit of the [Kaldi](https://github.com/kaldi-asr/kaldi) automatic speech recognition toolkit) to show you how to build state-of-the art systems.

Merlin is free software, distributed under an Apache License Version 2.0, allowing unrestricted commercial and non-commercial use alike.

Read the documentation at [cstr-edinburgh.github.io/merlin](https://cstr-edinburgh.github.io/merlin/).

Merlin is compatible with: __Python 2.7-3.6__.

Installation
------------

Merlin uses the following dependencies:

- numpy, scipy
- matplotlib
- bandmat
- theano
- tensorflow (optional, required if you use tensorflow models)
- sklearn, keras, h5py (optional, required if you use keras models)

To install Merlin, `cd` merlin and run the below steps:

- Install some basic tools in Merlin
```sh
bash tools/compile_tools.sh
```
- Install python dependencies
```sh
pip install -r requirements.txt
```

For detailed instructions, to build the toolkit: see [INSTALL](https://github.com/CSTR-Edinburgh/merlin/blob/master/INSTALL.md) and [CSTR blog post](https://cstr-edinburgh.github.io/install-merlin/).  
These instructions are valid for UNIX systems including various flavors of Linux;


Getting started with Merlin
---------------------------

To run the example system builds, see `egs/README.txt`

As a first demo, please follow the scripts in `egs/slt_arctic`

Now, you can also follow Josh Meyer's [blog post](http://jrmeyer.github.io/tts/2017/02/14/Installing-Merlin.html) for detailed instructions <br/> on how to install Merlin and build SLT demo voice.

For a more in-depth tutorial about building voices with Merlin, you can check out:

- [Deep Learning for Text-to-Speech Synthesis, using the Merlin toolkit (Interspeech 2017 tutorial)](http://www.speech.zone/courses/one-off/merlin-interspeech2017)
- [Arctic voices](https://cstr-edinburgh.github.io/merlin/getting-started/slt-arctic-voice)
- [Build your own voice](https://cstr-edinburgh.github.io/merlin/getting-started/build-own-voice)


Synthetic speech samples
------------------------

Listen to [synthetic speech samples](https://cstr-edinburgh.github.io/merlin/demo.html) from our SLT arctic voice.

Development pattern for contributors
------------------------------------

1. [Create a personal fork](https://help.github.com/articles/fork-a-repo/)
of the [main Merlin repository](https://github.com/CSTR-Edinburgh/merlin) in GitHub.
2. Make your changes in a named branch different from `master`, e.g. you create
a branch `my-new-feature`.
3. [Generate a pull request](https://help.github.com/articles/creating-a-pull-request/)
through the Web interface of GitHub.

Contact Us
----------

Post your questions, suggestions, and discussions to [GitHub Issues](https://github.com/CSTR-Edinburgh/merlin/issues).

Citation
--------

If you publish work based on Merlin, please cite: 

Zhizheng Wu, Oliver Watts, Simon King, "[Merlin: An Open Source Neural Network Speech Synthesis System](https://isca-speech.org/archive/SSW_2016/pdfs/ssw9_PS2-13_Wu.pdf)" in Proc. 9th ISCA Speech Synthesis Workshop (SSW9), September 2016, Sunnyvale, CA, USA.

numpy
scipy
scikit-learn
matplotlib
bandmat>=0.5
theano>=0.8
keras>=2.0.5
h5py>=2.7.0
tensorflow>=1.2.0
# Merlin Documentation

The source for Merlin documentation is in this directory under `templates/`. 
Our documentation uses extended Markdown, as implemented by [MkDocs](http://mkdocs.org) and is similar to Keras.

## Building the documentation

- install MkDocs: `pip install mkdocs`
- `cd` to the `docs/` folder and run:
    - `mkdocs serve`    # Starts a local webserver:  [localhost:8000](localhost:8000)
    - `mkdocs build`    # Builds a static site in "site" directory
# Merlin guided unit selection synthesis

coming soon...

## Merlin: The Neural Network (NN) based Speech Synthesis System

This repository contains the Neural Network (NN) based Speech Synthesis System  
developed at the Centre for Speech Technology Research (CSTR), University of 
Edinburgh. 

Merlin is a toolkit for building Deep Neural Network models for statistical parametric speech synthesis. 
It must be used in combination with a front-end text processor (e.g., Festival) and a vocoder (e.g., STRAIGHT or WORLD).

The system is written in Python and relies on the Theano numerical computation library.

Merlin comes with recipes (in the spirit of the [Kaldi](https://github.com/kaldi-asr/kaldi) automatic speech recognition toolkit) to show you how to build state-of-the art systems.

Merlin is free software, distributed under an Apache License Version 2.0, allowing unrestricted commercial and non-commercial use alike.

Read the documentation at [cstr-edinburgh.github.io/merlin](https://cstr-edinburgh.github.io/merlin/).

Merlin is compatible with: __Python 2.7__.

Installation
------------

Merlin uses the following dependencies:

- numpy, scipy
- matplotlib
- bandmat
- theano
- sklearn, keras (optional, required if you use keras models)

To install Merlin, `cd` merlin and run the below steps:

- Install some tools in Merlin
```sh
bash tools/compile_tools.sh
```
- Install python dependencies
```sh
pip install -r requirements.txt
```

For detailed instructions, to build the toolkit: see [`INSTALL`](https://github.com/CSTR-Edinburgh/merlin/blob/master/INSTALL.md).  
These instructions are valid for UNIX
systems including various flavors of Linux;


Getting started with Merlin
---------------------------

To run the example system builds, see `egs/README.txt`

As a first demo, please follow the scripts in `egs/slt_arctic`

Now, you can also follow Josh Meyer [blog post](http://jrmeyer.github.io/merlin/2017/02/14/Installing-Merlin.html) for detailed instructions <br/> on how to install Merlin and build SLT demo voice.

For a more in-depth tutorial about building voices with Merlin, you can check out:

- [Arctic voices](https://cstr-edinburgh.github.io/merlin/slt-arctic-voice)
- [Build your own voice](https://cstr-edinburgh.github.io/merlin/build-own-voice)


Synthetic speech samples
------------------------

Listen to [synthetic speech samples](https://cstr-edinburgh.github.io/merlin/demo.html) from our SLT arctic voice.

Development pattern for contributors
------------------------------------

1. [Create a personal fork](https://help.github.com/articles/fork-a-repo/)
of the [main Merlin repository](https://github.com/CSTR-Edinburgh/merlin) in GitHub.
2. Make your changes in a named branch different from `master`, e.g. you create
a branch `my-new-feature`.
3. [Generate a pull request](https://help.github.com/articles/creating-a-pull-request/)
through the Web interface of GitHub.

Contact Us
----------

Post your questions, suggestions, and discussions to [GitHub Issues](https://github.com/CSTR-Edinburgh/merlin/issues).

Citation
--------

If you publish work based on Merlin, please cite: 

Zhizheng Wu, Oliver Watts, Simon King, "[Merlin: An Open Source Neural Network Speech Synthesis System](http://ssw9.net/papers/ssw9_PS2-13_Wu.pdf)" in Proc. 9th ISCA Speech Synthesis Workshop (SSW9), September 2016, Sunnyvale, CA, USA.

# DNN-based speaker adaptation

coming soon...

# Parallel voice conversion

coming soon...

# Build your own voice

To build your own voice, `cd egs/build_your_own_voice/s1` and follow the below steps:

## Setting up

The first step is to run setup as it creates directories and some text files for testing.

The next steps demonstrate on how to setup voice. 

```sh
./01_setup.sh my_voice
```

It also creates a global config file: `conf/global_settings.cfg`, where default settings are stored.
You need to modify these params as per your own data.

## Prepare labels

To prepare labels
```sh
./02_prepare_labels.sh <path_to_wav_dir> <path_to_text_dir> <path_to_labels_dir>
```

## Prepare acoustic features
 
To prepare acoustic features
```sh
./03_prepare_acoustic_features.sh <path_to_wav_dir> <path_to_feat_dir>
```

## Prepare config files

At this point, we have to prepare two config files to train DNN models
- Acoustic Model
- Duration Model

To prepare config files:
```sh
./04_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

## Train duration model

To train duration model:
```sh
./05_train_duration_model.sh <path_to_duration_conf_file>
```

## Train acoustic model

To train acoustic model:
```sh
./06_train_acoustic_model.sh <path_to_acoustic_conf_file>
```
## Synthesize speech

To synthesize speech:
```sh
./07_run_merlin.sh <path_to_text_dir> <path_to_test_dur_conf_file> <path_to_test_synth_conf_file>
```

# Arctic voices

The CMU_ARCTIC databases were constructed at the Language Technologies Institute at 
Carnegie Mellon University as phonetically balanced, 
US English single speaker databases designed for unit selection speech synthesis research.

The databases consist of around 1150 utterances carefully selected from out-of-copyright texts from Project Gutenberg. 
The databses include US English male (bdl), female (slt) speakers (both experinced voice talent) and few other accented speakers.

To run one of these voices, `cd egs/slt_arctic/s1` and follow the below steps:

## Setting up

The first step is to run setup as it creates directories and downloads the required training data files.

To see the list of available voices, run:
```sh
./01_setup.sh
```
The next steps demonstrate on how to setup slt arctic voice. 

- To run on short data(about 50 utterances for training)
```sh
./01_setup.sh slt_arctic_demo
```
- To run on full data(about 1000 sentences for training)
```sh
./01_setup.sh slt_arctic_full
```

It also creates a global config file: `conf/global_settings.cfg`, where default settings are stored.
 
## Prepare config files

At this point, we have to prepare two config files to train DNN models
- Acoustic Model
- Duration Model

To prepare config files:
```sh
./02_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

## Train duration model

To train duration model:
```sh
./03_train_duration_model.sh <path_to_duration_conf_file>
```

## Train acoustic model

To train acoustic model:
```sh
./04_train_acoustic_model.sh <path_to_acoustic_conf_file>
```
## Synthesize speech

To synthesize speech:
```sh
./05_run_merlin.sh <path_to_test_dur_conf_file> <path_to_test_synth_conf_file>
```

coming soon...

coming soon...

coming soon...

This directory contains example scripts that demonstrate how to 
use Merlin.  Each subdirectory corresponds to a corpus that we have
example scripts for.

Build your own voice
--------------------

Each subdirectory of this directory contains the scripts for a sequence of experiments.

  s1: To run your_own_voice with WORLD vocoder and radio phoneset.


# Build your own voice


## Requirements

You need to have installed:
* [Merlin](https://github.com/CSTR-Edinburgh/merlin#installation)
* festival: ```bash tools/compile_other_speech_tools.sh```
* htk: ```bash tools/compile_htk.sh```


## Building Steps

To build your own voice, `cd egs/build_your_own_voice/s1` and follow the below steps:

### Setting up

The first step is to run setup as it creates directories and some text files for testing.

The next steps demonstrate on how to setup voice. 

```sh
./01_setup.sh my_voice
```

It also creates a global config file: `conf/global_settings.cfg`, where default settings are stored.
You need to modify these params as per your own data.

### Prepare labels

To prepare labels
```sh
./02_prepare_labels.sh <path_to_wav_dir> <path_to_text_dir> <path_to_labels_dir>
```

### Prepare acoustic features
 
To prepare acoustic features
```sh
./03_prepare_acoustic_features.sh <path_to_wav_dir> <path_to_feat_dir>
```

### Prepare config files

At this point, we have to prepare two config files to train DNN models
- Acoustic Model
- Duration Model

To prepare config files:
```sh
./04_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

### Train duration model

To train duration model:
```sh
./05_train_duration_model.sh <path_to_duration_conf_file>
```

### Train acoustic model

To train acoustic model:
```sh
./06_train_acoustic_model.sh <path_to_acoustic_conf_file>
```
### Synthesize speech

To synthesize speech:
```sh
./07_run_merlin.sh <path_to_text_dir> <path_to_test_dur_conf_file> <path_to_test_synth_conf_file>
```

About the Blizzard 2017 corpus
-------------------------------

This corpus is released as part of Blizzard 2017 challenge and was used in Merlin benchmark for Blizzard challenge workshop.
It consists of 7253 sentences -- train(5866), valid(134) and test(253).

1. This data is released under a license for non-commercial use only. 
2. Read and accept the [license](http://www.cstr.ed.ac.uk/projects/blizzard/2017/usborne_blizzard2017/license.html)

For more details about the corpus, please follow below link:
http://www.cstr.ed.ac.uk/projects/blizzard/2018/usborne_blizzard2018/

Each subdirectory of this directory contains the scripts for a sequence of experiments.

  s1: To run fls_blizzard2017 with WORLD vocoder and unilex phoneset
      


Download Merlin
---------------

```bash
git clone https://github.com/CSTR-Edinburgh/merlin.git 
```

Install tools
-------------

```bash
bash merlin/tools/compile_tools.sh
```

Merlin benchmark for Blizzard 2017
--------------

To run full voice, please follow below steps:

```bash
cd merlin/egs/fls_blizzard2017/s1
./run_merlin_benchmark.sh
```

Merlin benchmark for Blizzard 2017 made use of WORLD vocoder and Unilex phoneset, training on 5866 utterances. The training of the voice approximately takes 4 to 6 hours. 

Compare the results in log files to baseline results from [RESULTS.md](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/fls_blizzard2017/s1/RESULTS.md)

Generate new sentences
----------------------

To generate new sentences, please follow below steps:

```bash
./merlin_synthesis.sh
```

Nick Hurricane Corpus
=====================

Demo data: 
----------
herald_001 -- herald_060 (60 utterances) <br/>
Data distribution: Train: 50; Valid: 5; Test: 5;

Full data: 
----------
herald_001 -- hvd_719 (2542 utterances) <br/>
Data distribution: Train: 2400; Valid: 70; Test: 72;

RESULTS
=======

Baseline results from demo data
-------------------------------

Objective scores from duration model: <br/>

Valid -- RMSE: 6.221 frames/phoneme; CORR: 0.718; <br/>
Test  -- RMSE: 6.902 frames/phoneme; CORR: 0.678;

Objective scores from acoustic model: <br/> 

Valid -- MCD: 5.714 dB; BAP: 2.158 dB; F0:- RMSE: 11.197 Hz; CORR: 0.766; VUV: 6.202%
Test  -- MCD: 5.662 dB; BAP: 2.183 dB; F0:- RMSE: 13.595 Hz; CORR: 0.632; VUV: 7.175%


Baseline results from full data
-------------------------------

Objective scores from duration model: <br/>


Objective scores from acoustic model: <br/> 


# Hybrid speech synthesis

## ATTENTION: still in experimental phase...won't work straight-forward...requires lot of debugging!!

Hybrid speech synthesis is one of the main driving force behind most of the commercial systems that are present today. 

Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. Multisyn is an open-source toolkit for building unit selection voice with any speech corpus. This post gives detailed instructions on how to use Multisyn to build an unit selection model and Festival for final waveform synthesis. 

# Hybrid speech synthesis

## ATTENTION: still in experimental phase...won't work straight-forward...requires lot of debugging!!

Hybrid speech synthesis is one of the main driving force behind most of the commercial systems that are present today. 

Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. Multisyn is an open-source toolkit for building unit selection voice with any speech corpus. This post gives detailed instructions on how to use Multisyn to build an unit selection model and Festival for final waveform synthesis. 

## Tools required

1. [Speech tools](http://www.cstr.ed.ac.uk/projects/speech_tools)
2. [Festival](http://www.cstr.ed.ac.uk/projects/festival)
3. [Multisyn](http://www.cstr.ed.ac.uk/downloads/festival/multisyn_build)
4. [HTK](http://htk.eng.cam.ac.uk)

To build a new voice with Festival Multisyn, follow the step-by-step procedure given below:

## Step-by-step procedure

### Install tools

You might be familiar with most of these tools, but there are some differences in the way we setup these tools. 

- A version of [speech tools](http://www.cstr.ed.ac.uk/downloads/festival/2.4/speech_tools-2.4-with-wrappers.tar.gz) with python wrappers has to be installed in order to work with Multisyn.
- Latest version of [Festival](http://104.131.174.95/downloads/tools/festival-2.4-current.tar.gz) has to be installed in order to use hybrid unit selection. 

Therefore, we recommend installing a fresh copy of these tools following the [scripts provided in Merlin](https://github.com/CSTR-Edinburgh/merlin/blob/master/tools/compile_unit_selection_tools.sh). 

To install speech tools, Festival and Multisyn:

```bash
bash compile_unit_selection_tools.sh
```

To install HTK:

```bash
bash compile_htk.sh
```

Make sure you install all these tools without any errors and check environment variables before proceeding further. 

### Demo data

At this point, make sure you have data ready:

- a [directory containing audio files](http://festvox.org/cmu_arctic/cmu_arctic/cmu_us_slt_arctic/wav/) with file extension `.wav` 
- a [text file](http://festvox.org/cmu_arctic/cmu_arctic/cmu_us_slt_arctic/etc/txt.done.data) with transcriptions in the typical festival format.

For demo purpose, we use [SLT corpus from CMU Arctic Database](http://festvox.org/cmu_arctic/cmu_arctic/packed/cmu_us_slt_arctic-0.95-release.zip). 

### Setting up

The first step is to run setup as it creates directories and some text files for testing.

The next steps demonstrate on how to setup voice. 

```sh
./01_setup.sh conf/global_settings.cfg
```

You need to modify these params as per your own data.

### Build unit-selection model with Multisyn

Choose one of the lexicons:
1. cmulex
2. unilex-rpx
3. combilex-rpx

Choose gender:
1. 'm' for male
2. 'f' for female

If no arguments provided, the script uses default options: unilex and female assuming slt database

```sh
./02_build_unit_selection_model.sh
```

### Build parametric model with Merlin

```sh
./03_build_parametric_model.sh
```

### Build hybrid model

```sh
./04_build_hybrid_model.sh
```

### Synthesis with Festival

The below instructions are for Festival Multisyn voice:

```sh
$FESTDIR/bin/festival
```

Make festival speak "Hello world!" with new voice:

```sh
festival> (voice_cstr_edi_slt_multisyn)
festival> (SayText "Hello world!")
festival> (utt.save.wave (utt.synth (Utterance Text "Hello world!" )) "hello_world.wav")
```

For batch processing:

```sh
./05_run_hybrid_voice.sh <path_to_text_dir> <path_to_wav_dir>
```

For hybrid voice, please use the scm file in `scripts`.
Mandarin Voice
------------------------------------
This is a mandarin speech synthesis demo using only 250 wav from thchs30
dataset(A11 speaker)

A simple mandarin frontend is in https://github.com/jackiexiao/mtts 
Synthetic speech samples: Listen to https://jackiexiao.github.io/MTTS/
generated by different dataset

About THCHS30 Dataset 
------------------------------------
THCHS30 is an open Chinese speech database published by Center for Speech and Language Technology (CSLT) at Tsinghua University.

Actually this dataset is for researchers in the field of speech recognition,
but there is no any mandarin open-source dataset for speech synthesis, so we
use part of this dataset to demostrate mandarin tts.

Directory
------------------------------------
Each subdirectory of this directory contains the scripts for a sequence of experiments.
  s1: To run mandarin_voice with WORLD vocoder
# Mandarin Voice

## To run_demo
```
bash run_demo.sh
```

## To train with your own dataset

(1) Create the following dir and copy your file to dir (suppose current dir is merlin/egs/mandarin_voice/s1/)

* database/wav 
* database/labels/label_phone_align 
* database/prompt-lab 
* copy your own Question file to merlin/misc/questions

(2) modify params as per your own data in 01_setup.sh file, especially

* Voice Name
* QuestionFile
* Labels_Type(phone_align or state_align)
* SamplingFreq
* Train
* Valid
* Test

default setting is 

* QuestionFile=questions-mandarin.hed
* Labels=phone_align
* SamplingFreq=16000
* Train=200
* Valid=25
* Test=25

(3) then run

```
./run_mandarin_voice.sh
```
About the Nick Hurricane corpus
-------------------------------

This corpus is subset of Nick corpus and is used in Merlin demo paper from CSTR in SSW9.
It consists of 2542 sentences -- train(2400), valid(70) and test(72).

For more details about the corpus, please follow below link:
http://datashare.is.ed.ac.uk/handle/10283/347 

Each subdirectory of this directory contains the scripts for a sequence of experiments.

  s1: To run nick_hurricane with STRAIGHT vocoder and combilex phoneset
      The data is not publicly available as it includes features extracted from STRAIGHT and 
      labels using Combilex phoneset (both of them have restricted usage).

      Therefore, the scripts are meant for internal purpose and also for those who have license to both.
      For password, please mail me, only if you have license to both. 


Download Merlin
---------------

git clone https://github.com/CSTR-Edinburgh/merlin.git

Setup
-----

To setup demo voice: 

./01_setup.sh nick_hurricane_demo

    (or)   

To setup full voice:

./01_setup.sh nick_hurricane_full

Demo setup makes use of short amount of data (60 utterances) for training, validation and testing. <br/>
Full setup makes use of whole data (2542 utterances) for training, validation and testing. 

Run Merlin
----------

Once after setup, use below script to create acoustic, duration models and perform final test synthesis:

./02_run_merlin.sh

If demo setup is used, merlin trains only on 50 utterances and should not take more than 5 min. <br/>
Compare the results in log files to baseline results from demo data in [RESULTS.md](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/nick_hurricane/s1/RESULTS.md)

If full setup is used, merlin utilizes the whole cstr-hurricane data (2542 utterances). The training of the voice approximately takes 1 to 2 hours. <br/>
Compare the results in log files to baseline results from full data in [RESULTS.md](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/nick_hurricane/s1/RESULTS.md)

Generate new sentences
----------------------

To generate new sentences, please follow [steps] (https://github.com/CSTR-Edinburgh/merlin/issues/28) in below script:

./03_merlin_synthesis.sh

Nick Hurricane Corpus
=====================

Demo data: 
----------
herald_001 -- herald_060 (60 utterances) <br/>
Data distribution: Train: 50; Valid: 5; Test: 5;

Full data: 
----------
herald_001 -- hvd_719 (2542 utterances) <br/>
Data distribution: Train: 2400; Valid: 70; Test: 72;

RESULTS
=======

Baseline results from demo data
-------------------------------

Objective scores from duration model: <br/>

Valid -- RMSE: 6.221 frames/phoneme; CORR: 0.718; <br/>
Test  -- RMSE: 6.902 frames/phoneme; CORR: 0.678;

Objective scores from acoustic model: <br/> 

Valid -- MCD: 5.714 dB; BAP: 2.158 dB; F0:- RMSE: 11.197 Hz; CORR: 0.766; VUV: 6.202%
Test  -- MCD: 5.662 dB; BAP: 2.183 dB; F0:- RMSE: 13.595 Hz; CORR: 0.632; VUV: 7.175%


Baseline results from full data
-------------------------------

Objective scores from duration model: <br/>


Objective scores from acoustic model: <br/> 


About the SLT Arctic corpus

The CMU_ARCTIC databases were constructed at the Language Technologies Institute at Carnegie Mellon University as phonetically balanced, US English single speaker databases designed for unit selection speech synthesis research.

The databases consist of around 1150 utterances carefully selected from out-of-copyright texts from Project Gutenberg. The databses include US English male (bdl) and female (slt) speakers (both experienced voice talent) as well as other accented speakers.

Each subdirectory of this directory contains the
scripts for a sequence of experiments.

  s1: To run slt_arctic_demo with WORLD vocoder.
  s2: To run slt_arctic_demo with MagPhase vocoder (includes acoustic feature extraction).


Download Merlin
---------------

Step 1: git clone https://github.com/CSTR-Edinburgh/merlin.git 

Install tools
-------------

Step 2: cd merlin/tools <br/>
Step 3: ./compile_tools.sh

Demo voice
----------

To run demo voice, please follow below steps:
 
Step 4: cd merlin/egs/slt_arctic/s1 <br/>
Step 5: ./run_demo.sh

Demo voice trains only on 50 utterances and shouldn't take more than 5 min. 

Compare the results in log files to baseline results from demo data in [RESULTS.md](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/slt_arctic/s1/RESULTS.md)

Full voice
----------

To run full voice, please follow below steps:

Step 6: cd merlin/egs/slt_arctic/s1 <br/>
Step 7: ./run_full_voice.sh

Full voice utilizes the whole arctic data (1132 utterances). The training of the voice approximately takes 1 to 2 hours. 

Compare the results in log files to baseline results from full data in [RESULTS.md](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/slt_arctic/s1/RESULTS.md)

Generate new sentences
----------------------

To generate new sentences, please follow below steps:

Step 8: Run either demo voice or full voice. <br/>
Step 9: ./merlin_synthesis.sh

SLT Arctic Corpus
=================

Demo data: 
----------
arctic_a0001 -- arctic_a0060 (60 utterances) <br/>
Data distribution: Train: 50; Valid: 5; Test: 5;

Full data: 
----------
arctic_a0001 -- arctic_b0539 (1132 utterances) <br/>
Data distribution: Train: 1000; Valid: 66; Test: 66;

RESULTS
=======

Baseline results from demo data
-------------------------------

Objective scores from duration model: <br/>

Labels: state_align; Network: [416->5] LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- RMSE: 6.826 frames/phoneme; CORR: 0.624; <br/>
Test  -- RMSE: 7.840 frames/phoneme; CORR: 0.562;

Labels: phone_align; Network: [416->1] LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- RMSE: 6.777 frames/phoneme; CORR: 0.633; <br/> 
Test  -- RMSE: 7.665 frames/phoneme; CORR: 0.593;

Objective scores from acoustic model: <br/> 

Labels: state_align; Network: [425->187], LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- MCD: 6.559 dB; BAP: 0.242 dB; F0:- RMSE: 19.573 Hz; CORR: 0.529; VUV: 11.655%  <br/>
Test  -- MCD: 6.586 dB; BAP: 0.259 dB; F0:- RMSE: 15.309 Hz; CORR: 0.701; VUV: 8.821%

Labels: phone_align; Network: [420->187], LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- MCD: 6.762 dB; BAP: 0.246 dB; F0:- RMSE: 19.433 Hz; CORR: 0.538; VUV: 11.403% <br/>
Test  -- MCD: 6.704 dB; BAP: 0.262 dB; F0:- RMSE: 15.264 Hz; CORR: 0.700; VUV: 8.907%


Baseline results from full data
-------------------------------

Objective scores from duration model: <br/>

Labels: state_align; Network: [416->5] LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- RMSE: 6.810 frames/phoneme; CORR: 0.758; <br/>
Test  -- RMSE: 6.330 frames/phoneme; CORR: 0.773;

Labels: state_align; Network: [416->5] LR 0.002 [6 TANH] [6*1024]; <br/>
Valid -- RMSE: 6.564 frames/phoneme; CORR: 0.779; <br/>
Test  -- RMSE: 6.148 frames/phoneme; CORR: 0.788;
 
Labels: phone_align; Network: [416->1] LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- RMSE: 6.953 frames/phoneme; CORR: 0.746; <br/> 
Test  -- RMSE: 6.585 frames/phoneme; CORR: 0.752;

Objective scores from acoustic model: <br/> 

Labels: state_align; Network: [425->187], LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- MCD: 5.067 dB; BAP: 0.228 dB; F0:- RMSE: 11.186 Hz; CORR: 0.761; VUV: 6.312%  <br/>
Test  -- MCD: 5.070 dB; BAP: 0.238 dB; F0:- RMSE: 12.051 Hz; CORR: 0.752; VUV: 5.732%

Labels: state_align; Network: [425->187], LR 0.002 [6 TANH] [6*1024]; <br/>
Valid -- MCD: 4.912 dB; BAP: 0.225 dB; F0:- RMSE: 11.140 Hz; CORR: 0.763; VUV: 6.007% <br/>
Test  -- MCD: 4.912 dB; BAP: 0.232 dB; F0:- RMSE: 11.903 Hz; CORR: 0.759; VUV: 5.348%

Labels: phone_align; Network: [420->187], LR 0.002 [4 TANH] [4*512]; <br/>
Valid -- MCD: 5.255 dB; BAP: 0.235 dB; F0:- RMSE: 11.295 Hz; CORR: 0.754; VUV: 6.822% <br/>
Test  -- MCD: 5.247 dB; BAP: 0.244 dB; F0:- RMSE: 12.003 Hz; CORR: 0.757; VUV: 6.111%

# SLT Arctic TTS Demo using MagPhase Vocoder

## Overview

It is a Text-To-Speech demo using the [new release of the MagPhase vocoder (v2.0)](https://github.com/CSTR-Edinburgh/magphase), which now also supports:

* Constant frame-rate.
* Improved sound quality.
* Two types of post-filter available.
* Selectable number of coefficients for phase features (*real* and *imag*).
* Selectable number of coefficients for the magnitude feature (*mag*).


As a difference with other demos, it also includes **acoustic feature extraction**, thus the recipe works using as input data:
* label state aligned files (.lab).
* wav files (.wav).

Both are downloaded automatically during running the demo script.

## Run Demo Voice

Assuming Merlin is installed, just run:
```
cd merlin/egs/slt_arctic/s2/
python run_demo.py
```
Basically, ```run_demo.py``` script will:

1. Download the input data for you (.lab, .wav).
2. Create the experiment directory in ```./experiments```.
3. Perform acoustic feature extraction with MagPhase vocoder.
4. Build and train duration and acoustic models using Merlin.
5.  Synthesise waveforms using predicted durations. The synthesised waveforms will be stored in: ```/<experiment_dir>/test_synthesis/gen_acous_wav_pf_<postfilter_type>```

## Changing Parameters
Alternatively, you can also experiment by changing the input parameters (See section "INPUT" in *run_demo.py*):

* **exper_type:** Type of experiment. "demo" (50 training utts) or "full" (1k training utts.)

**Steps:**
* **b_download_data:** Download wavs and label data.
* **b_setup_data:** Copy downloaded data into the experiment directory. Plus, make a backup copy of *run_demo.py* script inside the experiment directory.
* **b_config_merlin:** Save new configuration files for Merlin.
* **b_feat_extr:** Perform acoustic feature extraction using the MagPhase vocoder.
* **b_conv_labs_rate:** Convert the state aligned labels to variable rate if running in variable frame rate mode (*b_const_rate=False*).
* **b_dur_train:** Merlin: Training of duration model.
* **b_acous_train:** Merlin: Training of acoustic model.
* **b_dur_syn:** Merlin: Generation of state durations using the duration model.
* **b_acous_syn:** Merlin: Waveform generation for the utterances provided in ```./test_synthesis/prompt-lab```


**MagPhase Vocoder:**

* **mag_dim:** Number of coefficients for magnitude feature (*mag*).
* **phase_dim:** Number of coefficients for phase features (*real* and *imag*).
* **b_const_rate:** To work in constant frame rate mode.
* **l_pf_type:** List containing the postfilters to apply during waveform generation.

* **b_feat_ext_multiproc:** Acoustic feature extraction done in multiprocessing mode (faster).# Speaker adaptation

This directory contains required files to build a speaker adaptation system. The VCTK-Corpus was used for the experiments.
1) Build an average voice model (AVM) over multiple speakers
2) Build a stand alone model of adapt speaker
3) Adapt the AVM for the adapt speaker 

## Download the data
The data is available for free to download. It comprises of a total 108 speakers of which 47 are male speakers. To download and extract the data:

```sh
./download_data.sh
```
Note: the size of tar file is around 11GB and afer extraction it will be around 16GB. Thus you need atleast 27GB of free space.

# Build an average voice model (AVM)
For Demo purpose we are building the AVM over 9 speakers (3 male and 6 female).

## Setting up

The first step is to run setup as it creates directories and some text files for testing.

The next steps demonstrate on how to setup voice. 

```sh
./01_setup.sh vctk_avm
```

It also creates a global config file: `conf/global_settings.cfg`, where default settings are stored. You need to modify these params as per the data.

## Prepare labels

To prepare labels
```sh
./02_prepare_labels.sh <path_to_wav_dir> <path_to_text_dir> <path_to_labels_dir>
```

## Prepare acoustic features
 
To prepare acoustic features
```sh
./03_prepare_acoustic_features.sh <path_to_wav_dir> <path_to_feat_dir>
```

## Prepare config files

At this point, we have to prepare two config files to train DNN models
- Acoustic Model
- Duration Model

To prepare config files:
```sh
./04_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

## Train duration model

To train duration model:
```sh
./05_train_duration_model.sh <path_to_duration_conf_file>
```

## Train acoustic model

To train acoustic model:
```sh
./06_train_acoustic_model.sh <path_to_acoustic_conf_file>
```
## Synthesize speech

To synthesize speech:
```sh
./07_run_merlin.sh <path_to_text_dir> <path_to_test_dur_conf_file> <path_to_test_synth_conf_file>
```

# Build voice of speaker p234 without adaptation
Just follow the above steps to creat the voice of p234


# Adapt the speaker `p234` on the AVM

## Setting up
To setup the data and directories

```sh
./08_setup_adapt.sh <voice_name> <average_duration_model> <average_acoustic_model> <adaptation_method>
```

It creates a global config file: `conf/global_settings_adapt.cfg`, where default settings are stored. You need to modify these params as per the data.

## Prepare labels

To prepare labels
```sh
./09_prepare_labels_adapt.sh <path_to_wav_dir> <path_to_text_dir> <path_to_labels_dir>
```

## Prepare acoustic features
 
To prepare acoustic features
```sh
./10_prepare_acoustic_features.sh <path_to_wav_dir> <path_to_feat_dir>
```

## Prepare config files

At this point, we have to prepare two config files to adapt DNN models
- Acoustic Model
- Duration Model

To prepare config files:
```sh
./11_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

## Train duration model

To train duration model:
```sh
./12_adapt_duration_model.sh <path_to_duration_conf_file>
```

## Train acoustic model

To train acoustic model:
```sh
./13_adapt_acoustic_model.sh <path_to_acoustic_conf_file>
```
## Synthesize speech
VCTK corpus
=================

Average vocie model (AVM) data (demo): 
--------------------------------
Speakers: 6 female + 3 male, from `p225` to `p233` (3358 utterances) <br/>
Data distribution: Train: 3258; Valid: 50; Test: 50;

Speaker p235 voice model
-------------------------
Speaker: Female (357 utterances) <br/>
Data distribution: Train: 307; Valid: 25; Test: 25;

RESULTS
=======

Baseline results of AVM from demo data
-------------------------------
Duration model tains in about 20 minutes on GPU (Nvidia Titan)

Objective scores from duration model: <br/>

Labels: state_align; Network: [416->5] LR 0.002 [6 TANH] [6*1024]; <br/>
Develop -- RMSE: 5.751 frames/phoneme; CORR: 0.791; <br/>
Test  -- RMSE: 5.502 frames/phoneme; CORR: 0.808;

Acoustic model trains in about 1 hour 30 minutes on GPU (Nvidia Titan)

Objective scores from acoustic model: <br/> 

Labels: state_align; Network: [425->199], LR 0.002 [4 TANH] [4*512]; <br/>
Develop -- MCD: 6.145 dB; BAP: 0.345 dB; F0:- RMSE: 47.039 Hz; CORR: 0.678; VUV: 8.771%  <br/>
Test  -- MCD: 6.097 dB; BAP: 0.329 dB; F0:- RMSE: 46.723 Hz; CORR: 0.627; VUV: 8.474%


Baseline results of speaker `p234` from full data
-------------------------------------------------
Duration model trains in about 5 minutes
Objective scores from duration model: <br/>

Labels: state_align; Network: [416->5] LR 0.002 [6 TANH] [6*1024]; <br/>
Develop -- RMSE: 6.145 frames/phoneme; CORR: 0.664; <br/>
Test  -- RMSE: 7.604 frames/phoneme; CORR: 0.687;

Acoustic model trains in about 10 minutes
Objective scores from acoustic model: <br/> 

Labels: state_align; Network: [425->199], LR 0.002 [6 TANH] [6*1024]; <br/>
Develop: DNN -- MCD: 5.476 dB; BAP: 0.401 dB; F0:- RMSE: 15.202 Hz; CORR: 0.537; VUV: 13.190%
Test   : DNN -- MCD: 5.441 dB; BAP: 0.407 dB; F0:- RMSE: 17.097 Hz; CORR: 0.542; VUV: 16.853%


Adapt speaker `p234` on the average voice model
-----------------------------------------------
Here we used the fine-tune method for the adaptation.

Duration model adapts in about 5 minutes
Objective scores from duration model: <br/>

Labels: state_align; Network: [416->5] LR 0.002 [6 TANH] [6*1024]; <br/>
Develop -- RMSE: 5.214 frames/phoneme; CORR: 0.797; <br/>
Test  -- RMSE: 5.483 frames/phoneme; CORR: 0.851;

Acoustic model adapts in about 10 minutes
Objective scores from acoustic model: <br/> 

Labels: state_align; Network: [425->199], LR 0.002 [6 TANH] [6*1024]; <br/>
Develop: DNN -- MCD: 5.240 dB; BAP: 0.383 dB; F0:- RMSE: 15.034 Hz; CORR: 0.524; VUV: 12.280%  <br/>
Test   : DNN -- MCD: 5.213 dB; BAP: 0.389 dB; F0:- RMSE: 18.190 Hz; CORR: 0.473; VUV: 16.459%
# About voice conversion

Voice conversion aims at transforming the characteristics of a speech
signal uttered by a source speaker in such a way that the transformed
speech sounds like the target speaker. Such a conversion requires 
transformation of spectral and prosody features. 

Most of the current voice conversion techniques need a parallel
database where the source and target speakers record the
same set of utterances. 

CMU ARCTIC databases consists of 7 speakers with each speaker recording 
a set of 1132 phonetically balanced utterances. Therefore, it is an ideal 
choice to perform voice conversion experiments. 

Each subdirectory of this directory contains the
scripts for a sequence of experiments.

- s1: To run voice conversion with either world or straight vocoder.
- s2: To run voice conversion with MagPhase vocoder.

## Demo data

You can download the data from [here](http://104.131.174.95/downloads/voice_conversion/).
- Source: bdl (300 utterances)
- Target: slt (300 utterances)

## About the Arctic corpus

The CMU ARCTIC databases were constructed at the Language Technologies Institute at Carnegie Mellon University as phonetically balanced, US English single speaker databases designed for unit selection speech synthesis research.

The databases consist of around 1150 utterances carefully selected from out-of-copyright texts from Project Gutenberg. The databses include US English male (bdl) and female (slt) speakers (both experinced voice talent) as well as other accented speakers.

For more details, please visit [cmu arctic page](http://www.festvox.org/cmu_arctic/).


# Voice Conversion

To manipulate source speaker's voice to sound like target without changing language content. 

## Install Merlin

Before proceeding any further, you first [install Merlin](https://github.com/CSTR-Edinburgh/merlin#installation) and then run the below steps.

## Dependency tools

Along with Merlin, we need to install few other speech tools in order to run voice conversion. 
- [speech tools](http://www.cstr.ed.ac.uk/downloads/festival/2.4/speech_tools-2.4-release.tar.gz)
- [festvox](http://festvox.org/festvox-2.7/festvox-2.7.0-release.tar.gz)

```sh
bash merlin/tools/compile_other_speech_tools.sh 
```

All these tools are required for only one task i.e., dynamic time warping (DTW) to create parallel data. 
You can check this [tutorial](http://speech.zone/exercises/dtw-in-python) for DTW implementation.

As an alternative, [fastdtw](https://github.com/CSTR-Edinburgh/merlin/blob/master/misc/scripts/voice_conversion/dtw_aligner.py) from python bindings can also be used.  
Please check [step 3](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/voice_conversion/s1/README.md#align-source-features-with-target) for its usage.
 
To convert source voice to target voice, `cd egs/voice_conversion/s1` and follow the below steps:

## Voice conversion challenge 2016 data

Now, you can run Merlin voice conversion using VC2016 data. 

To download the data:
```sh
./scripts/download_vcc2016_data.sh
```

To run voice conversion between any source-target pair, give the speaker names as arguments:
```sh
./run_vcc2016_benchmark.sh [SOURCE_SPEAKER] [TARGET_SPEAKER]
```

## Demo data

You can download the data from [here](http://104.131.174.95/downloads/voice_conversion/).
- Source: bdl (300 utterances)
- Target: slt (300 utterances)

To run voice conversion on demo data
```sh
./run_demo_vc.sh
```

However, we recommend using step-by-step procedure to correct any errors if raised. 

## Setting up

The first step is to run setup as it creates directories.

The next steps demonstrate on how to setup voice. 

```sh
./01_setup.sh speakerA speakerB
```

It also creates a global config file: `conf/global_settings.cfg`, where default settings are stored.
You need to modify these params as per your own data.

## Prepare acoustic features

To prepare acoustic features
```sh
./02_prepare_acoustic_features.sh <path_to_wav_dir> <path_to_feat_dir>
```

You have to run this script twice, for speakerA and speakerB

## Align source features with target

For voice conversion, we require parallel sentences for training. For this, we use dynamic-time-warping from Festvox 
to align source features with target. 

To align source features with target
```sh
./03_align_src_with_target.sh <path_to_src_feat_dir> <path_to_tgt_feat_dir> <path_to_src_align_dir>
```

Alternatively, [fastdtw](https://github.com/CSTR-Edinburgh/merlin/blob/master/misc/scripts/voice_conversion/dtw_aligner.py) from python bindings can also be used.  

```bash
pip install fastdtw
```

To use fastdtw, replace `dtw_aligner_festvox.py` with `dtw_aligner.py` at line number 60 in `03_align_src_with_target.sh`.

## Prepare config files

At this point, we have to prepare two config files for voice conversion
- Source acoustic model
- Source2Target acoustic Model

To prepare config files:
```sh
./04_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

## Prepare source acoustic features 

To prepare acoustic features for SpeakerA
```sh
./05_train_acoustic_model.sh <path_to_acoustic_source_conf_file>
```

## Create a symbolic link for source acoustic features 

At this point, we have to create a symbolic link for source features in the main voice directory.

To prepare symbolic link for source features
```sh
./scripts/create_symbolic_link.sh
```

Input dimension for source features is computed based on sampling rate provided in global conf file. 

## Train acoustic model for voice conversion

To train acoustic model:
```sh
./05_train_acoustic_model.sh <path_to_acoustic_voice_conf_file>
```

## Voice conversion from source to target

To transform voice from speakerA to speakerB:
```sh
./06_run_merlin_vc.sh <path_to_src_wav_dir> <path_to_test_source_conf_file> <path_to_test_synth_conf_file>
```

# Voice Conversion Using MagPhase Vocoder

To manipulate source speaker's voice to sound like target without changing language content. 

MagPhase vocoder for VC has the advantage that in addition to using magnitude spectra derived features, it makes possible to map **phase features** from one speaker to another.

## Install Merlin

Before proceeding any further, you first [install Merlin](https://github.com/CSTR-Edinburgh/merlin#installation) and then run the below steps.

## Dependency tools

Along with Merlin, we need to install few other speech tools in order to run voice conversion. 
- [speech tools](http://www.cstr.ed.ac.uk/downloads/festival/2.4/speech_tools-2.4-release.tar.gz)
- [festvox](http://festvox.org/festvox-2.7/festvox-2.7.0-release.tar.gz)

```sh
bash merlin/tools/compile_other_speech_tools.sh 
```

All these tools are required for only one task i.e., dynamic time warping (DTW) to create parallel data. 
You can check this [tutorial](http://speech.zone/exercises/dtw-in-python) for DTW implementation.

As an alternative, [fastdtw](https://github.com/CSTR-Edinburgh/merlin/blob/master/misc/scripts/voice_conversion/dtw_aligner.py) from python bindings can also be used.  
Please check [step 3](https://github.com/CSTR-Edinburgh/merlin/blob/master/egs/voice_conversion/s1/README.md#align-source-features-with-target) for its usage.
 
To convert source voice to target voice, `cd egs/voice_conversion/s2` and follow the below steps:

## Run with demo data

To do voice conversion on demo data, you can simply run:
```sh
./run_demo_vc.sh
```
Which will download the [data](http://104.131.174.95/downloads/voice_conversion/) and run the whole voice conversion recipe for you. The data consists of:

* Source: bdl (300 utterances)
* Target: slt (300 utterances)

However, we recommend using step-by-step procedure to correct any errors if raised:

### I. Setting up

The first step is to run setup as it creates directories.

The next steps demonstrate on how to setup voice. 

```sh
./01_setup.sh speakerA speakerB
```

It also creates a global config file: `conf/global_settings.cfg`, where default settings are stored.
You need to modify these params as per your own data.

### II. Prepare acoustic features

To prepare acoustic features
```sh
./02_prepare_acoustic_features.sh <path_to_wav_dir> <path_to_feat_dir>
```

You have to run this script twice, for speakerA and speakerB

### III. Align source features with target

For voice conversion, we require parallel sentences for training. For this, we use dynamic-time-warping from Festvox 
to align source features with target. 

To align source features with target
```sh
./03_align_src_with_target.sh <path_to_src_feat_dir> <path_to_tgt_feat_dir> <path_to_src_align_dir>
```

Alternatively, [fastdtw](https://github.com/CSTR-Edinburgh/merlin/blob/master/misc/scripts/voice_conversion/dtw_aligner.py) from python bindings can also be used.  

```bash
pip install fastdtw
```

To use fastdtw, replace `dtw_aligner_festvox.py` with `dtw_aligner.py` at line number 60 in `03_align_src_with_target.sh`.

### IV. Prepare config files

At this point, we have to prepare two config files for voice conversion
- Source acoustic model
- Source2Target acoustic Model

To prepare config files:
```sh
./04_prepare_conf_files.sh conf/global_settings.cfg
```
Four config files will be generated: two for training, and two for testing. 

### V. Prepare source acoustic features

To prepare acoustic features for SpeakerA
```sh
./05_train_acoustic_model.sh <path_to_acoustic_source_conf_file>
```

### VI. Create a symbolic link for source acoustic features

At this point, we have to create a symbolic link for source features in the main voice directory.

To prepare symbolic link for source features
```sh
./scripts/create_symbolic_link.sh
```

Input dimension for source features is computed based on sampling rate provided in global conf file. 

### VII. Train acoustic model for voice conversion

To train acoustic model:
```sh
./05_train_acoustic_model.sh <path_to_acoustic_voice_conf_file>
```

### VIII. Voice conversion from source to target

To transform voice from speakerA to speakerB:
```sh
./06_run_merlin_vc.sh <path_to_src_wav_dir> <path_to_test_source_conf_file> <path_to_test_synth_conf_file>
```

## TODO

* Constant frame rate support.
* Selectable phase and magnitude dimensions.
* Selectable postfilter.

phone (0-348) (438-440)
syl   (348-405) (440-461)
word  (405-438) (461-481)
phone (0-442) (557-559)
syl   (442-524) (559-580)
word  (524-557) (580-600)
forced alignment
----------------

state_align -- create training labels for merlin with HTK tools

phone_align -- create training labels for merlin with festvox tools

To train a new voice with Merlin, either state_align or phone_align labels are required, but not both. So, chose one as per your convenience and set the option accordingly in global_settings.cfg file.
Create training labels for merlin with festvox tools
----------------------------------------------------

Step 0: Install [speech_tools] (http://festvox.org/packed/festival/2.4/speech_tools-2.4-release.tar.gz), [festival] (http://festvox.org/packed/festival/2.4/festival-2.4-release.tar.gz), 
and [festvox] (http://festvox.org/download.html).

Step 1: Run setup.sh -- to download slt data and to create the config file. <br/>
./setup.sh

Step 2: Please configure paths to all tools in config.cfg

Step 3: Run aligner.sh -- which uses ehmm in clustergen setup (from festvox tools) to do forced-alignment. <br/>
./run_aligner.sh config.cfg

If all the above steps performed successfully, you should have your labels ready !! :)

EHMM Aligner
------------

The steps to perform ehmm alignment are adapted from: <br/>
[http://festvox.org/bsv/c3174.html] (http://festvox.org/bsv/c3174.html)


Create training labels for merlin with HTK tools
------------------------------------------------

Step 0: Install [festival](http://festvox.org/packed/festival/2.4/festival-2.4-release.tar.gz), 
and [HTK](http://htk.eng.cam.ac.uk/download.shtml).

Step 1: Run setup.sh -- to download slt data and to create the config file. <br/>
./setup.sh

Step 2: Please configure paths to all tools in config.cfg

Step 3: Run aligner.sh -- which uses HVite (from HTK tools) to do forced-alignment. <br/>
./run_aligner.sh config.cfg

If all the above steps performed successfully, you should have your labels ready !! :)

HTK Aligner
-----------

The steps to perform HTK alignment are adapted from HTS source code: <br/>
[HMM-based Speech Synthesis System (HTS)](http://hts.sp.nitech.ac.jp/)


################################################
#####  Make HTS labels from Festival utts  #####
################################################

FESTDIR="/afs/inf.ed.ac.uk/group/cstr/projects/phd/s1432486/work/test/merlin/tools/festival"

./make_labels ./test/labels/ ./test/utts  $FESTDIR/examples/dumpfeats .


### the args are:
# ./test/labels/     ## Put the newly made labels here.
# ./test/utts      ## Look for existing utterances here.
# dumpfeats         ## This needs to point to Festival's dumpfeats script, usually in .festival/examples
#  .                # Following scirpts must be here: extra_feats.scm label.feats label-full.awk  label-mono.awk
 
#### Change label-full.awk according to the separators you need in output labels. 
Vocoders
--------

a) STRAIGHT - extracts 60-dim MGC, 25-dim BAP, 1-dim LF0 

b) WORLD - extracts 60-dim MGC, variable-dim BAP, 1-dim LF0 <br/>
(BAP dim: 1 for 16Khz, 5 for 48Khz) 

c) MAGPHASE - extracts 60-dim mag, 45-dim real, 45-dim imag, 1-dim LF0 <br/>
(Dimensions of mag, real and imag can be fine-tuned)

d) WORLD_v2 - extracts 60-dim MGC, 5-dim BAP, 1-dim LF0 <br/>
(dimensions of MGC and BAP can be fine-tuned)

We recommend using either STRAIGHT or WORLD. 

WORLD_v2 and MAGPHASE are still under development and require more testing. 
# Build your own voice using the MagPhase vocoder


## Requirements

You need to have installed:
* [Merlin](https://github.com/CSTR-Edinburgh/merlin#installation)
* festival: ```bash tools/compile_other_speech_tools.sh```
* htk: ```bash tools/compile_htk.sh```

## Building Steps

### Generating state-aligned label files
1. Run the recipe **egs/build_your_own_voice/s1** until the step **02_prepare_labels.sh**

    As a result, you will have state aligned label files for your data.

### Acoustic Modelling and Synthesis

2. Edit the script **egs/build_your_own_voice/s2/build_voice.py** according to your data.

3. Run the script:
    ```
    python build_voice.py
    ```

INSTALL
=======

### To install basic tools

Merlin by default requires installation of some basic tools
e.g., SPTK, WORLD

```sh
bash tools/compile_tools.sh
```

### To install other speech tools

When building a new voice, Merlin requires few other tools in order to build labels:
e.g., speech tools, festival and festvox

```sh
bash tools/compile_other_speech_tools.sh
```

If you want to build state align labels, Merlin requires installation of HTK

```sh
bash tools/compile_htk.sh
```
/* ----------------------------------------------------------------- */
/*           WORLD: High-quality speech analysis,                    */
/*           modification and synthesis system                       */
/*           developed by M. Morise                                  */
/*           http://ml.cs.yamanashi.ac.jp/world/                     */
/* ----------------------------------------------------------------- */
/*                                                                   */
/*  Copyright (c) 2010-2016  M. Morise                               */
/*                                                                   */
/* All rights reserved.                                              */
/*                                                                   */
/* Redistribution and use in source and binary forms, with or        */
/* without modification, are permitted provided that the following   */
/* conditions are met:                                               */
/*                                                                   */
/* - Redistributions of source code must retain the above copyright  */
/*   notice, this list of conditions and the following disclaimer.   */
/* - Redistributions in binary form must reproduce the above         */
/*   copyright notice, this list of conditions and the following     */
/*   disclaimer in the documentation and/or other materials provided */
/*   with the distribution.                                          */
/* - Neither the name of the M. Morise nor the names of its          */
/*   contributors may be used to endorse or promote products derived */
/*   from this software without specific prior written permission.   */
/*                                                                   */
/* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND            */
/* CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,       */
/* INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF          */
/* MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          */
/* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS */
/* BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,          */
/* EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED   */
/* TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,     */
/* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON */
/* ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   */
/* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY    */
/* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE           */
/* POSSIBILITY OF SUCH DAMAGE.                                       */
/* ----------------------------------------------------------------- */
# World - a high-quality speech analysis, manipulation and synthesis system

WORLD is free software for high-quality speech analysis, manipulation and synthesis.
It can estimate Fundamental frequency (F0), aperiodicity and spectral envelope
and also generate the speech like input speech with only estimated parameters.

This source code is released under the modified-BSD license.
There is no patent in all algorithms in WORLD.
OS 	: Windows 7 64 bit
CPU 	: Core i7-3540M 3.0 GHz
RAM 	: 16 GB

Software
Microsoft Visual Studio 2015WORLD - a high-quality speech analysis, manipulation and synthesis system

WORLD is free software for high-quality speech analysis, manipulation and synthesis.
It can estimate Fundamental frequency (F0), aperiodicity and spectral envelope
and also generate the speech like input speech with only estimated parameters.

2. Usage
Please see test.cpp.

(1) F0 estimation by Dio()
(1-1) F0 is refined by StoneMask() if you need more accurate result.
(2) Spectral envelope estimation by CheapTrick()
(3) Aperiodicity estimation by D4C().
(4) You can manipulation these parameters in this phase. 
(5) Voice synthesis by Synthesis().

English document is written by a Japanese poor editor.
I willingly accept your kind indication on my English text.

3. License
WORLD is free software, and you can redistribute it and 
modify it under the terms of the modified BSD License.
Please see copying.txt for more information.
You can use this program for business, while I hope that 
you contact me after you developed software with WORLD.
This information is crucial to obtain a grant to develop WORLD.

4. Contacts
WORLD was written by Masanori Morise.
You can contact him via e-mail (mmorise [at] yamanashi.ac.jp)
or Twitter: @m_morise͍ WORLD

gɂẮCtest.cppQlɂĂD

WORLD͏CBSDCZXłD

--------------------------------------------------------------------
{IȍlF
́CƉFɂ\łƂ܂D
ŐVłł́CF0CwWCXyNgŕ\܂D
́CVocoderƓ̍lłD

(1) Dio() ɂ艹̊{g𐄒
(1-1) KvɉStoneMask() ɂ{g␳
(2) CheapTrick() ɂ艹̃XyNg𐄒
(3) D4C() ɂ艹̔wW𐄒
(4) Kvɉĉ≹F̐
(5) Synthesis() ɂ艹

--------------------------------------------------------------------
肢F
WORLD𗘗pꍇ́Cp/񏤗pɊւ炸X
񒸂΍Kł (͋`ł͂܂)D
̏́ClXȌlۂɖ𗧂܂D
̌́CWORLD𔭓W邽߂ɗp܂D

҂֘A
mmorise [at] yamanashi.ac.jp
Twitter: @m_morise /* ----------------------------------------------------------------- */
/*           WORLD: High-quality speech analysis,                    */
/*           modification and synthesis system                       */
/*           developed by M. Morise                                  */
/*           http://ml.cs.yamanashi.ac.jp/world/                     */
/* ----------------------------------------------------------------- */
/*                                                                   */
/*  Copyright (c) 2010-2016  M. Morise                               */
/*                                                                   */
/* All rights reserved.                                              */
/*                                                                   */
/* Redistribution and use in source and binary forms, with or        */
/* without modification, are permitted provided that the following   */
/* conditions are met:                                               */
/*                                                                   */
/* - Redistributions of source code must retain the above copyright  */
/*   notice, this list of conditions and the following disclaimer.   */
/* - Redistributions in binary form must reproduce the above         */
/*   copyright notice, this list of conditions and the following     */
/*   disclaimer in the documentation and/or other materials provided */
/*   with the distribution.                                          */
/* - Neither the name of the M. Morise nor the names of its          */
/*   contributors may be used to endorse or promote products derived */
/*   from this software without specific prior written permission.   */
/*                                                                   */
/* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND            */
/* CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,       */
/* INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF          */
/* MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          */
/* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS */
/* BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,          */
/* EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED   */
/* TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,     */
/* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON */
/* ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   */
/* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY    */
/* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE           */
/* POSSIBILITY OF SUCH DAMAGE.                                       */
/* ----------------------------------------------------------------- */
# World - a high-quality speech analysis, manipulation and synthesis system

WORLD is free software for high-quality speech analysis, manipulation and synthesis.
It can estimate Fundamental frequency (F0), aperiodicity and spectral envelope
and also generate the speech like input speech with only estimated parameters.

This source code is released under the modified-BSD license.
There is no patent in all algorithms in WORLD.
OS 	: Windows 7 64 bit
CPU 	: Core i7-3540M 3.0 GHz
RAM 	: 16 GB

Software
Microsoft Visual Studio 2015WORLD - a high-quality speech analysis, manipulation and synthesis system

WORLD is free software for high-quality speech analysis, manipulation and synthesis.
It can estimate Fundamental frequency (F0), aperiodicity and spectral envelope
and also generate the speech like input speech with only estimated parameters.

2. Usage
Please see test.cpp.

(1) F0 estimation by Dio()
(1-1) F0 is refined by StoneMask() if you need more accurate result.
(2) Spectral envelope estimation by CheapTrick()
(3) Aperiodicity estimation by D4C().
(4) You can manipulation these parameters in this phase. 
(5) Voice synthesis by Synthesis().

English document is written by a Japanese poor editor.
I willingly accept your kind indication on my English text.

3. License
WORLD is free software, and you can redistribute it and 
modify it under the terms of the modified BSD License.
Please see copying.txt for more information.
You can use this program for business, while I hope that 
you contact me after you developed software with WORLD.
This information is crucial to obtain a grant to develop WORLD.

4. Contacts
WORLD was written by Masanori Morise.
You can contact him via e-mail (mmorise [at] yamanashi.ac.jp)
or Twitter: @m_morise͍ WORLD

gɂẮCtest.cppQlɂĂD

WORLD͏CBSDCZXłD

--------------------------------------------------------------------
{IȍlF
́CƉFɂ\łƂ܂D
ŐVłł́CF0CwWCXyNgŕ\܂D
́CVocoderƓ̍lłD

(1) Dio() ɂ艹̊{g𐄒
(1-1) KvɉStoneMask() ɂ{g␳
(2) CheapTrick() ɂ艹̃XyNg𐄒
(3) D4C() ɂ艹̔wW𐄒
(4) Kvɉĉ≹F̐
(5) Synthesis() ɂ艹

--------------------------------------------------------------------
肢F
WORLD𗘗pꍇ́Cp/񏤗pɊւ炸X
񒸂΍Kł (͋`ł͂܂)D
̏́ClXȌlۂɖ𗧂܂D
̌́CWORLD𔭓W邽߂ɗp܂D

҂֘A
mmorise [at] yamanashi.ac.jp
Twitter: @m_morise 