The MIT License (MIT)

Copyright (c) 2017 IST Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# Scrapy Cluster

[![Build Status](https://travis-ci.org/istresearch/scrapy-cluster.svg?branch=master)](https://travis-ci.org/istresearch/scrapy-cluster) [![Documentation](https://readthedocs.org/projects/scrapy-cluster/badge/?version=latest)](http://scrapy-cluster.readthedocs.io/en/latest/) [![Join the chat at https://gitter.im/istresearch/scrapy-cluster](https://badges.gitter.im/istresearch/scrapy-cluster.svg)](https://gitter.im/istresearch/scrapy-cluster?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Coverage Status](https://coveralls.io/repos/github/istresearch/scrapy-cluster/badge.svg?branch=master)](https://coveralls.io/github/istresearch/scrapy-cluster?branch=master) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/istresearch/scrapy-cluster/blob/master/LICENSE) [![Docker Pulls](https://img.shields.io/docker/pulls/istresearch/scrapy-cluster.svg)](https://hub.docker.com/r/istresearch/scrapy-cluster/)

This Scrapy project uses Redis and Kafka to create a distributed on demand scraping cluster.

The goal is to distribute seed URLs among many waiting spider instances, whose requests are coordinated via Redis. Any other crawls those trigger, as a result of frontier expansion or depth traversal, will also be distributed among all workers in the cluster.

The input to the system is a set of Kafka topics and the output is a set of Kafka topics. Raw HTML and assets are crawled interactively, spidered, and output to the log. For easy local development, you can also disable the Kafka portions and work with the spider entirely via Redis, although this is not recommended due to the serialization of the crawl requests.

## Dependencies

Please see the ``requirements.txt`` within each sub project for Pip package dependencies.

Other important components required to run the cluster

- Python 2.7: https://www.python.org/downloads/
- Redis: http://redis.io
- Zookeeper: https://zookeeper.apache.org
- Kafka: http://kafka.apache.org

## Core Concepts

This project tries to bring together a bunch of new concepts to Scrapy and large scale distributed crawling in general. Some bullet points include:

- The spiders are dynamic and on demand, meaning that they allow the arbitrary collection of any web page that is submitted to the scraping cluster
- Scale Scrapy instances across a single machine or multiple machines
- Coordinate and prioritize their scraping effort for desired sites
- Persist data across scraping jobs
- Execute multiple scraping jobs concurrently
- Allows for in depth access into the information about your scraping job, what is upcoming, and how the sites are ranked
- Allows you to arbitrarily add/remove/scale your scrapers from the pool without loss of data or downtime
- Utilizes Apache Kafka as a data bus for any application to interact with the scraping cluster (submit jobs, get info, stop jobs, view results)
- Allows for coordinated throttling of crawls from independent spiders on separate machines, but behind the same IP Address
- Enables completely different spiders to yield crawl requests to each other, giving flexibility to how the crawl job is tackled

## Scrapy Cluster test environment

To set up a pre-canned Scrapy Cluster test environment, make sure you have the latest **Virtualbox** + **Vagrant >= 1.7.4** installed.  Vagrant will automatically mount the base **scrapy-cluster** directory to the **/vagrant** directory, so any code changes you make will be visible inside the VM. Please note that at time of writing this will not work on a [Windows](http://docs.ansible.com/ansible/intro_installation.html#control-machine-requirements) machine.

### Steps to launch the test environment:
1.  `vagrant up` in base **scrapy-cluster** directory.
2.  `vagrant ssh` to ssh into the VM.
3.  `sudo supervisorctl status` to check that everything is running.
4.  `virtualenv sc` to create a virtual environment
5.  `source sc/bin/activate` to activate the virtual environment
6.  `cd /vagrant` to get to the **scrapy-cluster** directory.
7.  `pip install -r requirements.txt` to install Scrapy Cluster dependencies.
8.  `./run_offline_tests.sh` to run offline tests.
9.  `./run_online_tests.sh` to run online tests (relies on kafka, zookeeper, redis).

## Documentation

Please check out the official [Scrapy Cluster 1.2.1 documentation](http://scrapy-cluster.readthedocs.org/en/latest/) for more information on how everything works!

## Branches

The `master` branch of this repository contains the latest stable release code for `Scrapy Cluster 1.2.1`.

The `dev` branch contains bleeding edge code and is currently working towards [Scrapy Cluster 1.3](https://github.com/istresearch/scrapy-cluster/milestone/3). Please note that not everything may be documented, finished, tested, or finalized but we are happy to help guide those who are interested.
# this file is deprecated and will be removed

ConcurrentLogHandler==0.9.1
Flask==0.12 # Updated from 0.11
Jinja2==2.9.5 # Updated from 2.8
MarkupSafe==1.0 # Updated from 0.23
PyDispatcher==2.0.5
PyYAML==3.12
Scrapy==1.3.3 # Updated from 1.3.1
Twisted==17.1.0 # Updated from 16.4.0
Werkzeug==0.12.1 # Updated from 0.11.11
attrs==16.3.0 # Updated from 16.1.0
cffi==1.9.1 # Updated from 1.7.0
characteristic==14.3.0
click==6.7 # Updated from 6.6
coverage==4.3.4 # Updated from 4.0.3
cryptography==1.8.1 # Updated from 1.5
cssselect==1.0.1 # Updated from 0.9.2
enum34==1.1.6
funcsigs==1.0.2
future==0.16.0 # Updated from 0.15.2
idna==2.5 # Updated from 2.1
ipaddress==1.0.18 # Updated from 1.0.16
itsdangerous==0.24
jsonschema==2.6.0 # Updated from 2.5.1
kafka-python==1.3.3 # Updated from 1.3.2
kazoo==2.2.1
lxml==3.7.3 # Updated from 3.6.4
mock==2.0.0
nose==1.3.7
parsel==1.1.0 # Updated from 1.0.3
pbr==2.0.0 # Updated from 1.10.0
pyOpenSSL==16.2.0 # Updated from 16.1.0
pyasn1-modules==0.0.8
pyasn1==0.2.3 # Updated from 0.1.9
pycparser==2.17 # Updated from 2.14
python-json-logger==0.1.7 # Updated from 0.1.5
python-redis-lock==3.2.0 # Updated from 3.1.0
queuelib==1.4.2
redis==2.10.5
requests-file==1.4.1 # Updated from 1.4
requests==2.13.0 # Updated from 2.11.1
retrying==1.3.3
scutils==1.2.0
service-identity==16.0.0
six==1.10.0
testfixtures==4.13.5 # Updated from 4.11.0
tldextract==2.0.2 # Updated from 2.0.1
ujson==1.35
w3lib==1.17.0 # Updated from 1.16.0
zope.interface==4.3.3 # Updated from 4.2.0
# Generated with piprot 0.9.7The MIT License (MIT)

Copyright (c) 2014 David Wittman

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
# Dec. 3, 1024
# Original scripts modified by andrew.carter@soteradefense.com to remove Debian support, and be managed by supervisord.


# ansible-redis

[![Build Status](https://travis-ci.org/DavidWittman/ansible-redis.svg?branch=master)](https://travis-ci.org/DavidWittman/ansible-redis)

 - Requires Ansible 1.6.3+
 - Compatible with most versions of Ubuntu/Debian and RHEL/CentOS 6.x

## Installation

``` bash
$ ansible-galaxy install DavidWittman.redis
```

## Getting started

### Single Redis node

Deploying a single Redis server node is pretty trivial; just add the role to your playbook and go. Here's an example which we'll make a little more exciting by setting the bind address to 127.0.0.1:

``` yml
---
- hosts: redis01.example.com
  vars:
    - redis_bind: 127.0.0.1
  roles:
    - redis
```

``` bash
$ ansible-playbook -i redis01.example.com, redis.yml
```

**Note:** You may have noticed above that I just passed a hostname in as the Ansible inventory file. This is an easy way to run Ansible without first having to create an inventory file, you just need to suffix the hostname with a comma so Ansible knows what to do with it.

That's it! You'll now have a Redis server listening on 127.0.0.1 on redis01.example.com. By default, the Redis binaries are installed under /opt/redis, though this can be overridden by setting the `redis_install_dir` variable.

### Master-Slave replication

Configuring [replication](http://redis.io/topics/replication) in Redis is accomplished by deploying multiple nodes, and setting the `redis_slaveof` variable on the slave nodes, just as you would in the redis.conf. In the example that follows, we'll deploy a Redis master with three slaves.

In this example, we're going to use groups to separate the master and slave nodes. Let's start with the inventory file:

``` ini
[redis-master]
redis-master.example.com

[redis-slave]
redis-slave0[1:3].example.com
```

And here's the playbook:

``` yml
---
- name: configure the master redis server
  hosts: redis-master
  roles:
    - redis

- name: configure redis slaves
  hosts: redis-slave
  vars:
    - redis_slaveof: redis-master.example.com 6379
  roles:
    - redis
```

In this case, I'm assuming you have DNS records set up for redis-master.example.com, but that's not always the case. You can pretty much go crazy with whatever you need this to be set to. In many cases, I tell Ansible to use the eth1 IP address for the master. Here's a more flexible value for the sake of posterity:

``` yml
redis_slaveof: "{{ hostvars['redis-master.example.com'].ansible_eth1.ipv4.address }} {{ redis_port }}"
```

Now you're cooking with gas! Running this playbook should have you ready to go with a Redis master and three slaves.

### Redis Sentinel

#### Introduction

Using Master-Slave replication is great for durability and distributing reads and writes, but not so much for high availability. If the master node fails, a slave must be manually promoted to master, and connections will need to be redirected to the new master. The solution for this problem is [Redis Sentinel](http://redis.io/topics/sentinel), a distributed system which uses Redis itself to communicate and handle automatic failover in a Redis cluster.

Sentinel itself uses the same redis-server binary that Redis uses, but runs with the `--sentinel` flag and with a different configuration file. All of this, of course, is abstracted with this Ansible role, but it's still good to know.

#### Configuration

To add a Sentinel node to an existing deployment, assign this same `redis` role to it, and set the variable `redis_sentinel` to True on that particular host. This can be done in any number of ways, and for the purposes of this example I'll extend on the inventory file used above in the Master/Slave configuration:

``` ini
[redis-master]
redis-master.example.com

[redis-slave]
redis-slave0[1:3].example.com

[redis-sentinel]
redis-sentinel0[1:3].example.com redis_sentinel=True
```

Above, we've added three more hosts in the **redis-sentinel** group (though this group serves no purpose within the role, it's merely an identifier), and set the `redis_sentinel` variable inline within the inventory file.

Now, all we need to do is set the `redis_sentinel_monitors` variable to define the Redis masters which Sentinel should monitor. In this case, I'm going to do this within the playbook:

``` yml
- name: configure the master redis server
  hosts: redis-master
  roles:
    - redis

- name: configure redis slaves
  hosts: redis-slave
  vars:
    - redis_slaveof: redis-master.example.com 6379
  roles:
    - redis

- name: configure redis sentinel nodes
  hosts: redis-sentinel
  vars:
    - redis_sentinel_monitors:
      - name: master01
        host: redis-master.example.com
        port: 6379
  roles:
    - redis
```

This will configure the Sentinel nodes to monitor the master we created above using the identifier `master01`. By default, Sentinel will use a quorum of 2, which means that at least 2 Sentinels must agree that a master is down in order for a failover to take place. This value can be overridden by setting the `quorum` key within your monitor definition. See the [Sentinel docs](http://redis.io/topics/sentinel) for more details.

Along with the variables listed above, Sentinel has a number of its own configurables just as Redis server does. These are prefixed with `redis_sentinel_`, and are enumerated in the **Configurables** section below.


## Installing redis from a source file in the ansible role

If the environment your server resides in does not allow downloads (i.e. if the machine is sitting in a dmz) set the variable `redis_tarball` to the path of a locally downloaded tar.gz file to prevent a http download from redis.io.  
Do not forget to set the version variable to the same version of the tar.gz. to avoid confusion !

For example (file was stored in same folder as the playbook that included the redis role):
```yml
vars:
  - redis_version: 2.8.14
  - redis_tarball: redis-2.8.14.tar.gz
```
In this case the source archive is copied towards the server over ssh rather than downloaded.



## Configurables

Here is a list of all the default variables for this role, which are also available in defaults/main.yml. One of these days I'll format these into a table or something.

``` yml
---
## Installation options
redis_version: 2.8.8
redis_install_dir: /opt/redis
redis_user: redis
# Working directory for Redis. RDB and AOF files will be written here.
redis_dir: /var/lib/redis/{{ redis_port }}
redis_tarball: false
# The open file limit for Redis/Sentinel
redis_nofile_limit: 16384
# Configure Redis as a service
# When set to false, this role will not create init scripts or manage
# the Redis/Sentinel processes.
# This is usually needed when a tool like Supervisor will manage the process.
redis_as_service: true

## Networking/connection options
redis_bind: 0.0.0.0
redis_port: 6379
redis_password: false
redis_tcp_backlog: 511
redis_tcp_keepalive: 0
# Max connected clients at a time
redis_maxclients: 10000
redis_timeout: 0

## Replication options
# Set slaveof just as you would in redis.conf. (e.g. "redis01 6379")
redis_slaveof: false
# Make slaves read-only. "yes" or "no"
redis_slave_read_only: "yes"
redis_slave_priority: 100
redis_repl_backlog_size: false

## Logging
redis_logfile: '""'                                                             
# Enable syslog. "yes" or "no"                                                  
redis_syslog_enabled: "yes"                                                     
redis_syslog_ident: redis_{{ redis_port }}                                      
# Syslog facility. Must be USER or LOCAL0-LOCAL7                                
redis_syslog_facility: USER   

## General configuration
redis_daemonize: "yes"                                                          
redis_pidfile: /var/run/redis/{{ redis_port }}.pid
# Number of databases to allow
redis_databases: 16
redis_loglevel: notice
# Log queries slower than this many milliseconds. -1 to disable
redis_slowlog_log_slower_than: 10000
# Maximum number of slow queries to save
redis_slowlog_max_len: 128
# Redis memory limit (e.g. 4294967296, 4096mb, 4gb)
redis_maxmemory: false
redis_maxmemory_policy: noeviction
redis_rename_commands: []
# How frequently to snapshot the database to disk
# e.g. "900 1" => 900 seconds if at least 1 key changed
redis_save:
  - 900 1
  - 300 10
  - 60 10000

## Redis sentinel configs
# Set this to true on a host to configure it as a Sentinel
redis_sentinel: false
redis_sentinel_dir: /var/lib/redis/sentinel_{{ redis_sentinel_port }}
redis_sentinel_bind: 0.0.0.0
redis_sentinel_port: 26379
redis_sentinel_pidfile: /var/run/redis/sentinel_{{ redis_sentinel_port }}.pid
redis_sentinel_logfile: '""'                                                    
redis_sentinel_syslog_ident: sentinel_{{ redis_sentinel_port }}
redis_sentinel_monitors:
  - name: master01
    host: localhost
    port: 6379
    quorum: 2
    auth_pass: ant1r3z
    down_after_milliseconds: 30000
    parallel_syncs: 1
    failover_timeout: 180000
    notification_script: false
    client_reconfig_script: false
```

## Facts

The following facts are accessible in your inventory or tasks outside of this role.

- `{{ ansible_local.redis.bind }}`
- `{{ ansible_local.redis.port }}`
- `{{ ansible_local.redis.sentinel_bind }}`
- `{{ ansible_local.redis.sentinel_port }}`
- `{{ ansible_local.redis.sentinel_monitors }}`
attrs==16.3.0 # Updated from 16.1.0
cffi==1.9.1 # Updated from 1.7.0
ConcurrentLogHandler==0.9.1
cryptography==1.8.1 # Updated from 1.5
cssselect==1.0.1 # Updated from 0.9.2
enum34==1.1.6
funcsigs==1.0.2
future==0.16.0 # Updated from 0.15.2
idna==2.5 # Updated from 2.1
ipaddress==1.0.18 # Updated from 1.0.16
kafka-python==1.3.3 # Updated from 1.3.2
kazoo==2.2.1
lxml==3.7.3 # Updated from 3.6.4
mock==2.0.0
nose==1.3.7
parsel==1.1.0 # Updated from 1.0.3
pbr==2.0.0 # Updated from 1.10.0
pyasn1==0.2.3 # Updated from 0.1.9
pyasn1-modules==0.0.8
pycparser==2.17 # Updated from 2.14
PyDispatcher==2.0.5
pyOpenSSL==16.2.0 # Updated from 16.1.0
python-json-logger==0.1.7 # Updated from 0.1.5
PyYAML==3.12
queuelib==1.4.2
redis==2.10.5
requests==2.13.0 # Updated from 2.11.1
requests-file==1.4.1 # Updated from 1.4
retrying==1.3.3
Scrapy==1.3.3
scutils==1.2.0
service-identity==16.0.0
six==1.10.0
testfixtures==4.13.5 # Updated from 4.10.0
tldextract==2.0.2 # Updated from 2.0.1
Twisted==17.1.0 # Updated from 16.4.0
ujson==1.35
w3lib==1.17.0 # Updated from 1.16.0
zope.interface==4.3.3 # Updated from 4.2.0
# Generated with piprot 0.9.7
Docker
======

This folder houses the Dockerfiles and settings associated with Scrapy Cluster.

For more information please check out the [documentation](http://scrapy-cluster.readthedocs.org)

Want to build your own containers? From the root directory of this project run

```
$ docker build -t <your_tag> -f docker/<component>/Dockerfile .

# build the redis monitor on the dev branch
$ docker build -t istresearch/scrapy-cluster:redis-monitor-dev -f docker/redis-monitor/Dockerfile .
```# Scrapy Cluster Documentation

You can follow [this](http://docs.readthedocs.org/en/latest/getting_started.html#in-rst) guide on readthedocs to get your own local documentation up and running.

Otherwise, it boils down to the following commands

```bash
$ pip install sphinx sphinx-autobuild sphinx-rtd-theme
$ cd docs
$ sphinx-build . _build_html
$ sphinx-autobuild . _build_html

Serving on http://127.0.0.1:8000
...
```

You will now be able to view the documentation as you live edit it on your machine.
License
=======

::

    The MIT License (MIT)

    Copyright (c) 2017 IST Research

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
ELK
===

This folder houses sample files used when integrating Scrapy Cluster with Elasticsearch, Logstash and Kibana. For more information please see Scrapy Cluster's official Documentation.

Last tested on Nov 27, 2016 with:

* Elasticsearch 5.0

* Logstash 5.0

* Kibana 5.0ConcurrentLogHandler==0.9.1
funcsigs==1.0.2
future==0.16.0 # Updated from 0.15.2
idna==2.5 # Updated from 2.1
jsonschema==2.6.0 # Updated from 2.5.1
kafka-python==1.3.3 # Updated from 1.3.2
kazoo==2.2.1
mock==2.0.0
nose==1.3.7
pbr==2.0.0 # Updated from 1.10.0
python-json-logger==0.1.7 # Updated from 0.1.5
python-redis-lock==3.2.0 # Updated from 3.1.0
PyYAML==3.12
redis==2.10.5
requests==2.13.0 # Updated from 2.11.1
requests-file==1.4.1 # Updated from 1.4
retrying==1.3.3
scutils==1.2.0
six==1.10.0
testfixtures==4.13.5 # Updated from 4.10.0
tldextract==2.0.2 # Updated from 2.0.1
ujson==1.35
# Generated with piprot 0.9.7ConcurrentLogHandler==0.9.1
funcsigs==1.0.2
future==0.16.0 # Updated from 0.15.2
kafka-python==1.3.3 # Updated from 1.3.2
kazoo==2.2.1
mock==2.0.0
nose==1.3.7
pbr==2.0.0 # Updated from 1.10.0
python-json-logger==0.1.7 # Updated from 0.1.5
python-redis-lock==3.2.0 # Updated from 3.1.0
PyYAML==3.12
redis==2.10.5
retrying==1.3.3
scutils==1.2.0
six==1.10.0
testfixtures==4.13.5 # Updated from 4.10.0
ujson==1.35
# Generated with piprot 0.9.7click==6.7 # Updated from 6.6
ConcurrentLogHandler==0.9.1
Flask==0.12 # Updated from 0.11
funcsigs==1.0.2
future==0.16.0 # Updated from 0.15.2
itsdangerous==0.24
Jinja2==2.9.5 # Updated from 2.8
jsonschema==2.6.0 # Updated from 2.5.1
kafka-python==1.3.3 # Updated from 1.3.2
kazoo==2.2.1
MarkupSafe==1.0 # Updated from 0.23
mock==2.0.0
nose==1.3.7
pbr==2.0.0 # Updated from 1.10.0
python-json-logger==0.1.7 # Updated from 0.1.5
redis==2.10.5
requests==2.13.0 # Updated from 2.11.1
retrying==1.3.3
scutils==1.2.0
six==1.10.0
testfixtures==4.13.5 # Updated from 4.11.0
ujson==1.35
Werkzeug==0.12.1 # Updated from 0.11.11
# Generated with piprot 0.9.7************************
Scrapy Cluster Utilities
************************

Overview
--------

The ``scutils`` package is a collection of utilities that are used by the Scrapy Cluster project.  These utilities are agnostic enough that they can be used by any application.

Requirements
------------

- Unix based machine (Linux or OS X)
- Python 2.7.x

Installation
------------

Inside a virtualenv, run ``pip install -U scutils``.  This will install the latest version of the Scrapy Cluster Utilities.  If you are running a Scrapy Cluster, ``scutils`` is included inside of the **requirements.txt** so there is no need to install it separately.

Documentation
-------------

Full documentation for the ``scutils`` package is included as part of the Official Scrapy Cluster Documentation, which can be found `here <http://scrapy-cluster.readthedocs.org/en/latest/topics/utils/index.html>`_ under the **Utilities** section.

argparse_helper.py
==================

The ``argparse_helper`` module is used to help print top level ``--help`` arguments from argparse when used with subparsers. Useful for running applications that have multiple combinations of subcommands and command line arguments.

log_factory.py
==============

The ``log_factory`` module provides a standardized way for creating logs for multithreaded and concurrent process log data.  It supports all log levels, stdout or to a file, and various output formats including JSON.

method_timer.py
===============

The ``method_timer`` module provides a simple decorator that can be added to functions or methods requiring an execution timeout period.

redis_queue.py
==============

The ``redis_queue`` module provides 3 core queue classes which use Redis as the place to store data. Includes FIFO, Stack, and Priority Queues.

redis_throttled_queue.py
========================

The ``redis_throttled_queue`` module provides a throttled or moderated Redis queue structure that can be used to mitigate the number of pops from the queue within a given time frame.

settings_wrapper.py
===================

The ``settings_wrapper`` module is a class the handles loading of default python application settings, which can then be overridden or added to by a local settings file. In the end provides a single dictionary object of all your loaded application settings.


stats_collector.py
==================

The ``stats_collector`` module generates Redis based statistics based on time windows or in total. Statistics collection includes time windows, rolling time windows, counters, unique counters, hyperloglog counters, and bitmap counters.

zookeeper_watcher.py
====================

The ``zookeeper_watcher`` module provides an easy way to tell an application that it's watched Zookeeper file has changed. It also handles Zookeeper session disconnects and reconnects behind the scenes of your application.
