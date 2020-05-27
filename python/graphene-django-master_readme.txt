# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at me@syrusakbary.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
# Contributing

Thanks for helping to make graphene-django great!

We welcome all kinds of contributions:

- Bug fixes
- Documentation improvements
- New features
- Refactoring & tidying


## Getting started

If you have a specific contribution in mind, be sure to check the [issues](https://github.com/graphql-python/graphene-django/issues) and [projects](https://github.com/graphql-python/graphene-django/projects) in progress - someone could already be working on something similar and you can help out.


## Project setup

After cloning this repo, ensure dependencies are installed by running:

```sh
make dev-setup
```

## Running tests

After developing, the full test suite can be evaluated by running:

```sh
make tests
```

## Opening Pull Requests

Please fork the project and open a pull request against the master branch.

This will trigger a series of test and lint checks.

We advise that you format and run lint locally before doing this to save time:

```sh
make format
make lint
```

## Documentation

The [documentation](http://docs.graphene-python.org/projects/django/en/latest/) is generated using the excellent [Sphinx](http://www.sphinx-doc.org/) and a custom theme.

The documentation dependencies are installed by running:

```sh
cd docs
pip install -r requirements.txt
```

Then to produce a HTML version of the documentation:

```sh
make html
```The MIT License (MIT)

Copyright (c) 2016-Present Syrus Akbary

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
Please read [UPGRADE-v2.0.md](https://github.com/graphql-python/graphene/blob/master/UPGRADE-v2.0.md) to learn how to upgrade to Graphene `2.0`.

---

# ![Graphene Logo](http://graphene-python.org/favicon.png) Graphene-Django [![Build Status](https://travis-ci.org/graphql-python/graphene-django.svg?branch=master)](https://travis-ci.org/graphql-python/graphene-django) [![PyPI version](https://badge.fury.io/py/graphene-django.svg)](https://badge.fury.io/py/graphene-django) [![Coverage Status](https://coveralls.io/repos/graphql-python/graphene-django/badge.svg?branch=master&service=github)](https://coveralls.io/github/graphql-python/graphene-django?branch=master)


A [Django](https://www.djangoproject.com/) integration for [Graphene](http://graphene-python.org/).

## Documentation

[Visit the documentation to get started!](https://docs.graphene-python.org/projects/django/en/latest/)

## Quickstart

For installing graphene, just run this command in your shell

```bash
pip install "graphene-django>=2.0"
```

### Settings

```python
INSTALLED_APPS = (
    # ...
    'django.contrib.staticfiles', # Required for GraphiQL
    'graphene_django',
)

GRAPHENE = {
    'SCHEMA': 'app.schema.schema' # Where your Graphene schema lives
}
```

### Urls

We need to set up a `GraphQL` endpoint in our Django app, so we can serve the queries.

```python
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    path('graphql', GraphQLView.as_view(graphiql=True)),
]
```

## Examples

Here is a simple Django model:

```python
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
```

To create a GraphQL schema for it you simply have to write the following:

```python
from graphene_django import DjangoObjectType
import graphene

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()

schema = graphene.Schema(query=Query)
```

Then you can simply query the schema:

```python
query = '''
    query {
      users {
        name,
        lastName
      }
    }
'''
result = schema.execute(query)
```

To learn more check out the following [examples](examples/):

* **Schema with Filtering**: [Cookbook example](examples/cookbook)
* **Relay Schema**: [Starwars Relay example](examples/starwars)


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## Release Notes

* See [Releases page on github](https://github.com/graphql-python/graphene-django/releases)
Please read
`UPGRADE-v2.0.md <https://github.com/graphql-python/graphene/blob/master/UPGRADE-v2.0.md>`__
to learn how to upgrade to Graphene ``2.0``.

--------------

|Graphene Logo| Graphene-Django |Build Status| |PyPI version| |Coverage Status|
===============================================================================

A `Django <https://www.djangoproject.com/>`__ integration for
`Graphene <http://graphene-python.org/>`__.


Documentation
-------------

`Visit the documentation to get started! <https://docs.graphene-python.org/projects/django/en/latest/>`__

Quickstart
----------

For installing graphene, just run this command in your shell

.. code:: bash

    pip install "graphene-django>=2.0"

Settings
~~~~~~~~

.. code:: python

    INSTALLED_APPS = (
        # ...
        'graphene_django',
    )

    GRAPHENE = {
        'SCHEMA': 'app.schema.schema' # Where your Graphene schema lives
    }

Urls
~~~~

We need to set up a ``GraphQL`` endpoint in our Django app, so we can
serve the queries.

.. code:: python

    from django.conf.urls import url
    from graphene_django.views import GraphQLView

    urlpatterns = [
        # ...
        url(r'^graphql$', GraphQLView.as_view(graphiql=True)),
    ]

Examples
--------

Here is a simple Django model:

.. code:: python

    from django.db import models

    class UserModel(models.Model):
        name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

To create a GraphQL schema for it you simply have to write the
following:

.. code:: python

    from graphene_django import DjangoObjectType
    import graphene

    class User(DjangoObjectType):
        class Meta:
            model = UserModel

    class Query(graphene.ObjectType):
        users = graphene.List(User)

        @graphene.resolve_only_args
        def resolve_users(self):
            return UserModel.objects.all()

    schema = graphene.Schema(query=Query)

Then you can simply query the schema:

.. code:: python

    query = '''
        query {
          users {
            name,
            lastName
          }
        }
    '''
    result = schema.execute(query)

To learn more check out the following `examples <examples/>`__:

-  **Schema with Filtering**: `Cookbook example <examples/cookbook>`__
-  **Relay Schema**: `Starwars Relay example <examples/starwars>`__

Contributing
------------

See `CONTRIBUTING.md <CONTRIBUTING.md>`__.

.. |Graphene Logo| image:: http://graphene-python.org/favicon.png
.. |Build Status| image:: https://travis-ci.org/graphql-python/graphene-django.svg?branch=master
   :target: https://travis-ci.org/graphql-python/graphene-django
.. |PyPI version| image:: https://badge.fury.io/py/graphene-django.svg
   :target: https://badge.fury.io/py/graphene-django
.. |Coverage Status| image:: https://coveralls.io/repos/graphql-python/graphene-django/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/graphql-python/graphene-django?branch=master
Sphinx==1.5.3
sphinx-autobuild==0.7.1
# Docs template
http://graphene-python.org/sphinx_graphene_theme.zip
Cookbook Example Django Project
===============================

This example project demos integration between Graphene and Django.
The project contains two apps, one named `ingredients` and another
named `recipes`.

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the
whole Graphene repository:

```bash
# Get the example project code
git clone https://github.com/graphql-python/graphene-django.git
cd graphene-django/examples/cookbook
```

It is good idea (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to keep things simple,
but you may also find something like
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to be useful:

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

Now setup our database:

```bash
# Setup the database
./manage.py migrate

# Load some example data
./manage.py loaddata ingredients

# Create an admin user (useful for logging into the admin UI
# at http://127.0.0.1:8000/admin)
./manage.py createsuperuser
```

Now you should be ready to start the server:

```bash
./manage.py runserver
```

Now head on over to
[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
and run some queries!
(See the [Graphene-Django Tutorial](http://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/#testing-our-graphql-schema)
for some example queries)
graphene
graphene-django
graphql-core>=2.1rc1
django==3.0
django-filter>=2
Cookbook Example Django Project
===============================

This example project demos integration between Graphene and Django.
The project contains two apps, one named `ingredients` and another
named `recipes`.

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the
whole Graphene repository:

```bash
# Get the example project code
git clone https://github.com/graphql-python/graphene-django.git
cd graphene-django/examples/cookbook
```

It is good idea (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to keep things simple,
but you may also find something like
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to be useful:

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

Now setup our database:

```bash
# Setup the database
./manage.py migrate

# Load some example data
./manage.py loaddata ingredients

# Create an admin user (useful for logging into the admin UI
# at http://127.0.0.1:8000/admin)
./manage.py createsuperuser
```

Now you should be ready to start the server:

```bash
./manage.py runserver
```

Now head on over to
[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
and run some queries!
(See the [Graphene-Django Tutorial](http://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/#testing-our-graphql-schema)
for some example queries)
graphene
graphene-django
graphql-core>=2.1rc1
django==2.2.8
