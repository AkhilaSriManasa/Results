# Contributing to dephell

Thank you for deciding to contribute to DepHell!  This guide is to assist you with contributing code.  If you have a question that isn't answered here, please [open an issue][open issue].

## The basics

So you want to contribute some code?  Great! Here are the basic steps:

1. Find an [issue][issues] that you want to work on. Good places to start are [good first issues] or [help wanted]. You could also [open an issue][open issue] if there is something specific you want to contribute. Wait for a response before you start coding though, as the thing you want might already exist somewhere!
1. Fork DepHell.
1. Clone your fork.
1. Create a branch to work against.
1. Run tests to make sure they work for your system.
1. Write some tests.
1. Write some code.
1. Run tests to make sure it works.
1. Run flake8 checks.
1. Write some docs.
1. Push your branch (to your fork).
1. Create a pull request to dephell/master
1. Wait for checks to run and fix anything that was wrong

## Testing

Any new code that you contribute will be ideally covered under an automated test. To run existing tests:

```bash
dephell venv create --env pytest
dephell deps install --env pytest
dephell venv run --env pytest
```

To write new tests using [pytest], place them in the `tests` directory.  This directory should roughly follow the same file structure as the source directory (`dephell`) except that every file/module is prepended with `test_`.  For example, the file containing tests for `dephell/commands/deps_convert.py` is `tests/test_commands/test_deps_convert.py`.

## Style

All the code you contribute must follow the same style as the rest of dephell:

- Follow [PEP8]
- Use `'single quotes'` for strings, not `"double quotes"`

Run flake8 to see how you're doing:

```bash
dephell venv create --env flake8
dephell deps install --env flake8
dephell venv run --env flake8
```

Sort imports before pushing:

```bash
dephell venv create --env isort
dephell deps install --env isort
dephell venv run --env isort
```

Main things you contribute are ideas and implementation. So, if you struggled with flake8 checks, don't worry, just ask help of maintainers in comments to your Pull Request. If your code passed CI, merging of Pull Request can't be rejected or delayed because of style. No [bikeshedding](https://en.wikipedia.org/wiki/Law_of_triviality) and meaningless discussions.

## Using an IDE

If you want to use an IDE to edit / test dephell code, you'll have to point that IDE to the virtual environment dephell created.  You can either get this path using `dephell inspect venv` or create the venv in a directory your IDE will find (e.g. `dephell venv create --venv .venv`).  Some tests currently assume they are being run from the root of the project.  If your IDE likes to run tests from other directories, you may need to update some existing tests to use relative paths.

[issues]: https://github.com/dephell/dephell/issues?utf8=✓&q=is%3Aissue+is%3Aopen+
[open issue]: https://github.com/dephell/dephell/issues/new
[help wanted]: https://github.com/dephell/dephell/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22
[good first issues]: https://github.com/dephell/dephell/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22

[pytest]: https://docs.pytest.org/en/latest/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
MIT License

Copyright (c) 2019 Gram

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
# ![DepHell](./assets/logo.png)

[![pypi](https://img.shields.io/pypi/v/dephell.svg)](https://pypi.python.org/pypi/dephell/)
[![MIT License](https://img.shields.io/pypi/l/dephell.svg)](https://github.com/dephell/dephell/blob/master/LICENSE)
[![Travis CI](https://travis-ci.org/dephell/dephell.svg?branch=master)](https://travis-ci.org/dephell/dephell)
[![Powered by DepHell](./assets/badge.svg)](./docs/badge.md)

**DepHell** -- project management for Python.

Why it is better than all other tools:

1. **Format agnostic**. You can use DepHell with your favorite format: setup.py, requirements.txt, Pipfile, poetry. DepHell supports them all and much more.
1. **Use your favorite tool on any project**. Want to install a poetry based project, but don't like poetry? Just tell DepHell to convert the project's meta information into a setup.py and install it with pip. Or directly work with the project from DepHell, because DepHell can do everything that you usually want to do with packages.
1. **DepHell doesn't try to replace your favorite tools**. If you use poetry, you have to use poetry's file formats and commands. However, DepHell can be combined with any other tool or can even combine all these tools together by converting formats. You can use DepHell, poetry, and pip all at the same time.
1. **Easily extendable**. DepHell has strong modularity and can be easily extended with new formats and commands.
1. **Developer friendly**. We aren't going to place all of our modules into [`_internal`](https://github.com/pypa/pip/tree/master/src/pip/_internal). Also, DepHell has a [large ecosystem](https://github.com/dephell) with separated libraries so you can use only the parts of DepHell that you need.
1. **All-in-one-solution**. DepHell can manage dependencies, virtual environments, tests, CLI tools, packages, generate configs, show licenses for dependencies, assist with security audits, get download statistics from PyPI, search packages and much more.
1. **Smart dependency resolution**. Sometimes pip and pipenv fail to lock your dependencies. Try to execute `pipenv install oslo.utils==1.4.0`. Pipenv can't handle it, but DepHell can: `dephell deps add --from=Pipfile oslo.utils==1.4.0` to add new dependency and `dephell deps convert --from=Pipfile --to=Pipfile.lock` to lock it.
1. **Asyncio based**. DepHell doesn't support Python 2.7, and that allows us to use modern features to make network and filesystem requests as fast as possible.
1. **Multiple environments**. You can have as many environments for project as you want. Separate sphinx dependencies from your main and dev environment. Other tools like pipenv and poetry don't support this.

Features:

+ Manage dependencies: [convert between formats](https://dephell.org/docs/cmd-deps-convert.html), [instаll](https://dephell.org/docs/cmd-deps-install.html), lock, [add new](https://dephell.org/docs/cmd-deps-add.html), resolve conflicts.
+ Manage virtual environments: [create](https://dephell.org/docs/cmd-venv-create.html), [remove](https://dephell.org/docs/cmd-venv-destroy.html), [inspect](https://dephell.org/docs/cmd-inspect-venv.html), [run shell](https://dephell.org/docs/cmd-venv-shell.html), [run commands inside](https://dephell.org/docs/cmd-venv-run.html).
+ [Install CLI tools](https://dephell.org/docs/cmd-jail-install.html) into isolated environments.
+ Manage packages: [install](https://dephell.org/docs/cmd-package-install.html), [list](https://dephell.org/docs/cmd-package-list.html), [search](https://dephell.org/docs/cmd-package-search.html) on PyPI.
+ [Build](https://dephell.org/docs/cmd-project-build.html) packages (to upload on PyPI), [test](https://dephell.org/docs/cmd-project-test.html), [bump project version](https://dephell.org/docs/cmd-project-bump.html).
+ [Discover licenses](https://dephell.org/docs/cmd-deps-licenses.html) of all project dependencies, show [outdated](https://dephell.org/docs/cmd-deps-outdated.html) packages, [find security issues](https://dephell.org/docs/cmd-deps-audit.html).
+ Generate [.editorconfig](https://dephell.org/docs/cmd-generate-editorconfig.html), [LICENSE](https://dephell.org/docs/cmd-generate-license.html), [AUTHORS](https://dephell.org/docs/cmd-generate-authors.html), [.travis.yml](https://dephell.org/docs/cmd-generate-travis.html).

See [documentation](https://dephell.org/docs/) for more details.

Follow [@PythonDepHell](https://twitter.com/PythonDepHell) on Twitter to get updates about new features and releases.

## Installation

```bash
curl -L dephell.org/install | python3
```

See [installation documentation](https://dephell.org/docs/installation.html) for alternatives.

## Supported formats

1. Archives:
    1. [*.egg-info](https://setuptools.readthedocs.io/en/latest/formats.html) (`egginfo`)
    1. [*.tar.gz](https://packaging.python.org/glossary/#term-distribution-package) (`sdist`)
    1. [*.whl](https://pythonwheels.com) (`wheel`)
1. [pip](https://pip.pypa.io/en/stable/):
    1. [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files) (`pip`)
    1. [requirements.lock](https://nvie.com/posts/pin-your-packages/) (`piplock`)
1. [pipenv](https://pipenv.readthedocs.io/en/latest/):
    1. [Pipfile](https://github.com/pypa/pipfile) (`pipfile`)
    1. [Pipfile.lock](https://stackoverflow.com/a/49867443/8704691) (`pipfilelock`)
1. [pоetry](https://github.com/sdispater/poetry):
    1. [pyproject.toml](https://poetry.eustace.io/docs/pyproject/) (`poetry`)
    1. [poetry.lock](https://poetry.eustace.io/docs/basic-usage/#installing-without-poetrylock) (`poetrylock`)
1. Environment:
    1. Imports in the package (`imports`).
    1. Installed packages (`installed`).
1. Other:
    1. [setup.py](https://docs.python.org/3/distutils/setupscript.html) (`setuppy`)
    1. [flit](https://flit.readthedocs.io/en/latest/pyproject_toml.html) (`flit`)
    1. [conda](https://conda.io/en/latest/)'s [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) (`conda`)
    1. [pyproject.toml build-system requires](https://www.python.org/dev/peps/pep-0518/#build-system-table) (`pyproject`)

## Usage

First of all, install DepHell and activate autocomplete:

```bash
python3 -m pip install --user dephell[full]
dephell self autocomplete
```

Let's get [sampleproject](https://github.com/pypa/sampleproject) and make it better.

```bash
git clone https://github.com/pypa/sampleproject.git
cd sampleproject
```

This project uses [setup.py](https://docs.python.org/3/distutils/setupscript.html) for dependencies and metainfo. However, this format is over-complicated for most projects. Let's convert it into [poetry](https://poetry.eustace.io/docs/pyproject/):

```bash
dephell deps convert --from=setup.py --to=pyproject.toml
```

It will make next `pyproject.toml`:

```toml
[tool.poetry]
name = "sampleproject"
version = "1.2.0"
description = "A sample Python project"
authors = ["The Python Packaging Authority <pypa-dev@googlegroups.com>"]
readme = "README.md"

[tool.poetry.scripts]
sample = "sample:main"

[tool.poetry.dependencies]
python = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,<4,>=2.7"
coverage = {optional = true}
peppercorn = "*"

[tool.poetry.dev-dependencies]
check-manifest = "*"

[tool.poetry.extras]
test = ["coverage"]
```

Now, let's generate some useful files:

```bash
dephell generate authors

dephell generate license MIT

# https://editorconfig.org/
dephell generate editorconfig
```

Our users probably have not installed poetry, but they are likely to have pip and can install files from setup.py. Let's make it easier to generate `setup.py` from our `pyproject.toml`. Also, it points to DepHell as your default dependencies file. Add the following lines in the `pyproject.toml`:

```toml
[tool.dephell.main]
from = {format = "poetry", path = "pyproject.toml"}
to = {format = "setuppy", path = "setup.py"}
```

You can see a full, real-world example of a config in [DepHell's own pyproject.toml](./pyproject.toml).

Now we can call DepHell commands without explicitly specifying `from` and `to`:

```bash
dephell deps convert
```

It will make setup.py and README.rst from pyproject.toml and README.md.

Now let's test our code in a virtual environment:

```bash
$ dephell venv run pytest
WARNING venv does not exist, creating... (project=/home/gram/Documents/sampleproject, env=main, path=/home/gram/.local/share/dephell/venvs/sampleproject-Whg0/main)
INFO venv created (path=/home/gram/.local/share/dephell/venvs/sampleproject-Whg0/main)
WARNING executable does not found in venv, trying to install... (executable=pytest)
INFO build dependencies graph...
INFO installation...
# ... pip output
# ... pytest output
```

We can now activate the virtual environment for our project and run any commands inside:

```bash
dephell venv shell
```

Ugh, we have tests, but don't have `pytest` in our dependencies file. Let's add it:

```bash
dephell deps add --envs dev test -- pytest
```

Afer that our dev-dependencies looks like this:

```toml
[tool.poetry.dev-dependencies]
check-manifest = "*"
pytest = "*"

[tool.poetry.extras]
test = ["coverage", "pytest"]
```

Eventually we will have many more dependencies. Let's look at how many of them we have now:

```bash
$ dephell deps tree
- check-manifest [required: *, locked: 0.37, latest: 0.37]
- coverage [required: *, locked: 4.5.3, latest: 4.5.3]
- peppercorn [required: *, locked: 0.6, latest: 0.6]
- pytest [required: *, locked: 4.4.0, latest: 4.4.0]
  - atomicwrites [required: >=1.0, locked: 1.3.0, latest: 1.3.0]
  - attrs [required: >=17.4.0, locked: 19.1.0, latest: 19.1.0]
  - colorama [required: *, locked: 0.4.1, latest: 0.4.1]
  - funcsigs [required: >=1.0, locked: 1.0.2, latest: 1.0.2]
  - more-itertools [required: <6.0.0,>=4.0.0, locked: 5.0.0, latest: 7.0.0]
    - six [required: <2.0.0,>=1.0.0, locked: 1.12.0, latest: 1.12.0]
  - more-itertools [required: >=4.0.0, locked: 7.0.0, latest: 7.0.0]
  - pathlib2 [required: >=2.2.0, locked: 2.3.3, latest: 2.3.3]
    - scandir [required: *, locked: 1.10.0, latest: 1.10.0]
    - six [required: *, locked: 1.12.0, latest: 1.12.0]
  - pluggy [required: >=0.9, locked: 0.9.0, latest: 0.9.0]
  - py [required: >=1.5.0, locked: 1.8.0, latest: 1.8.0]
  - setuptools [required: *, locked: 41.0.0, latest: 41.0.0]
  - six [required: >=1.10.0, locked: 1.12.0, latest: 1.12.0]
```

Hm...Is it as many as it seems? Let's look at their size.

```bash
$ dephell inspect venv --filter=lib_size
11.96Mb
```

Ugh...Ok, it's Python. Are they actual?

```bash
$ dephell deps outdated
[
  {
    "description": "More routines for operating on iterables, beyond itertools",
    "installed": [
      "5.0.0"
    ],
    "latest": "7.0.0",
    "name": "more-itertools",
    "updated": "2019-03-28"
  },
]
```

`Pytest` requires old version of `more-itertools`. That happens.

If our tests and dependencies are OK, it's time to deploy. First of all, increment the project version:

```bash
$ dephell project bump minor
INFO generated new version (old=1.2.0, new=1.3.0)
```

And then build packages:

```bash
$ dephell project build
INFO dumping... (format=setuppy)
INFO dumping... (format=egginfo)
INFO dumping... (format=sdist)
INFO dumping... (format=wheel)
INFO builded
```

Now, we can upload these packages to [PyPI](https://pypi.org/) with [twine](https://github.com/pypa/twine/).

These are some of the most useful commands. See [documentation](https://dephell.org/docs/) for more details.

## Compatibility

DepHell is tested on Linux and Mac OS X with Python 3.5, 3.6, 3.7. And one of the coolest things is that DepHell is run by DepHell on Travis CI.

## How can I help

1. Star project on Github. Developers believe in the stars.
1. Tell your fellows that [Gram](http://github.com/orsinium) has a made [cool thing](https://github.com/dephell/dephell) for you.
1. [Open an issue](https://github.com/dephell/dephell/issues/new) if you have thoughts on how to make DepHell better.
1. Things that you can contribute in any project in [DepHell ecosystem](https://github.com/dephell):
    1. Fix grammar and typos.
    1. Document new things.
    1. Tests, we always need more tests.
    1. Make READMEs more nice and friendly.
    1. View issues with the [help wanted](https://github.com/dephell/dephell/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) label to find things that you can fix.
    1. Anything what you want. If it is a new feature, please open an issue before writing code.

Thank you :heart:
flake8

flake8-comprehensions   # https://github.com/adamchainz/flake8-comprehensions
flake8-alfred           # https://github.com/datatheorem/flake8-alfred
flake8-blind-except     # https://github.com/elijahandrews/flake8-blind-except
flake8-bugbear          # https://github.com/PyCQA/flake8-bugbear
flake8-commas           # https://github.com/PyCQA/flake8-commas
flake8-debugger         # https://github.com/JBKahn/flake8-debugger
flake8-logging-format   # https://github.com/globality-corp/flake8-logging-format
flake8-mutable          # https://github.com/ebeweber/flake8-mutable
flake8-pep3101          # https://github.com/gforcada/flake8-pep3101
flake8-quotes           # https://github.com/zheller/flake8-quotes
flake8-tidy-imports     # https://github.com/adamchainz/flake8-tidy-imports
flake8-variables-names  # https://github.com/best-doctor/flake8-variables-names
pep8-naming             # https://github.com/PyCQA/pep8-naming


# flake8-string-format  # https://github.com/xZise/flake8-string-format
# disabled: https://github.com/xZise/flake8-string-format/issues/16

# flake8-broken-line    # https://github.com/sobolevn/flake8-broken-line
# disabled: https://github.com/sobolevn/flake8-broken-line/issues/38

## Short description

<!-- Thank you for your feedback! Please, fill the sections below to help us to solve the issue. -->

## Output

<!-- What is the output of invalid command and what is the expected behavior. -->

## Steps to reproduce

<!-- Please, provide as detailed and minimal set of commands to reproduce the bug as possible. If it is an Open Source Project, add `git clone ...` command as well. -->

```bash
$ git clone ...
$ cd ...
$ dephell deps convert
...
```

## Traceback

<!-- If a command fails, run it with `--traceback` and attach output -->

```
...
```

## Config

<!-- Attach `cat pyproject.toml` output -->

```toml
[tool.dephell.main]
...
```

# Versions

<!-- Attach `dephell inspect self` output -->

```json
...
```
# built-in
from argparse import ArgumentParser
from collections import defaultdict

# app
from ..actions import make_json
from ..config import builders
from .base import BaseCommand


class DepsLicensesCommand(BaseCommand):
    """Show licenses for all project dependencies.
    """
    @staticmethod
    def build_parser(parser) -> ArgumentParser:
        builders.build_config(parser)
        builders.build_from(parser)
        builders.build_resolver(parser)
        builders.build_api(parser)
        builders.build_output(parser)
        builders.build_other(parser)
        return parser

    def __call__(self) -> bool:
        resolver = self._get_locked()
        if resolver is None:
            return False

        # get licenses
        licenses = defaultdict(set)
        for dep in resolver.graph:
            if dep.license:
                license = dep.license if isinstance(dep.license, str) else dep.license.id
                licenses[license].add(dep.name)
            else:
                licenses['Unknown'].add(dep.name)
        licenses = {name: sorted(deps) for name, deps in licenses.items()}
        print(make_json(
            data=licenses,
            key=self.config.get('filter'),
            colors=not self.config['nocolors'],
            table=self.config['table'],
            sep=None,
        ))
        return True
# built-in
from argparse import REMAINDER, ArgumentParser
from datetime import datetime
from getpass import getuser
from pathlib import Path

# external
from dephell_discover import Root as PackageRoot
from dephell_licenses import licenses

# app
from ..config import builders
from ..converters import CONVERTERS
from .base import BaseCommand


class GenerateLicenseCommand(BaseCommand):
    """Create LICENSE file.
    """
    @staticmethod
    def build_parser(parser) -> ArgumentParser:
        builders.build_config(parser)
        builders.build_output(parser)
        builders.build_other(parser)
        parser.add_argument('--owner', help='name of the owner')
        parser.add_argument('name', nargs=REMAINDER, help='license name')
        return parser

    def __call__(self) -> bool:
        # get license object
        name = ' '.join(self.args.name).strip()
        if not name:
            name = 'MIT'
        license = licenses.get_by_id(name)
        if license is None:
            license = licenses.get_by_name(name)
        if license is None:
            self.logger.error('cannot find license with given name')
            return False

        # author name from --owner
        author = self.config.get('owner')

        # get author from `from`
        if not author and 'from' in self.config:
            loader = CONVERTERS[self.config['from']['format']]
            loader = loader.copy(project_path=Path(self.config['project']))
            root = loader.load(self.config['from']['path'])
            if root.authors:
                author = root.authors[0]

        # author from project config file
        if not author:
            metainfo = PackageRoot(Path(self.config['project'])).metainfo
            if metainfo and metainfo.authors:
                author = metainfo.authors[0]

        # author from getuser().title
        if not author:
            author = getuser().title()

        # generate license text
        text = license.make_text(copyright='{year} {name}'.format(
            year=datetime.now().year,
            name=author,
        ))
        (Path(self.config['project']) / 'LICENSE').write_text(text)
        self.logger.info('license generated', extra=dict(license=license.name))
        return True
# built-in
import re
from pathlib import Path
from string import Template
from typing import Optional

# external
import attr
from m2r import convert

# app
from ..cached_property import cached_property
from ..constants import EXTENSIONS


CODE = """
import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, '${fname}')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')
"""

REX_README_NAME = re.compile(r'(README\.[a-z]+)')


@attr.s()
class Readme:
    path = attr.ib(type=Path)

    @classmethod
    def discover(cls, path: Path) -> Optional['Readme']:
        for name in ('README', 'Readme', 'readme', 'ReadMe'):
            for ext in EXTENSIONS:
                if ext:
                    ext = '.' + ext
                fpath = (path / name).with_suffix(ext)
                if fpath.exists():
                    return cls(path=fpath)
        return None

    @classmethod
    def from_code(cls, path: Path, content: Optional[str] = None) -> Optional['Readme']:
        if content is None:
            content = path.read_text()
        match = REX_README_NAME.search(content)
        if match is None:
            return None
        new_path = path.parent / match.groups()[0]
        if not new_path.exists():
            return None
        return cls(path=new_path)

    @cached_property
    def markup(self) -> str:
        try:
            return EXTENSIONS[self.path.suffix.replace('.', '')]
        except KeyError as e:
            raise ValueError('invalid readme extension: *' + self.path.suffix) from e

    @property
    def content_type(self) -> str:
        if self.markup == 'rst':
            return 'text/x-rst'
        if self.markup == 'md':
            return 'text/markdown'
        return 'text/plain'

    def as_rst(self) -> str:
        if self.markup == 'rst':
            return self.path.read_text()
        if self.markup == 'md':
            content = convert(self.path.read_text())
            content = content.replace('.. code-block:: toml', '.. code-block::')
            return content
        if self.markup == 'txt':
            return self.path.read_text()
        raise ValueError('invalid markup')

    def to_rst(self) -> 'Readme':
        if self.markup in ('txt', 'rst'):
            return self
        new_path = self.path.with_name(self.path.stem).with_suffix('.rst')
        new_path.write_text(self.as_rst())
        return type(self)(path=new_path)

    def as_code(self) -> str:
        return Template(CODE).substitute(fname=self.path.name)
# Badge

If you want to show your users how to use your project more effective and what `dephell.tool.main` in your `pyproject.toml` means just add badge in your readme:

[![Powered by DepHell](https://github.com/dephell/dephell/blob/master/assets/badge.svg)](https://github.com/dephell/dephell)

```md
[![Powered by DepHell](https://github.com/dephell/dephell/blob/master/assets/badge.svg)](https://github.com/dephell/dephell)
```
# CHANGELOG

Follow [@PythonDepHell](https://twitter.com/PythonDepHell) on Twitter to get updates about new features and releases.

## v.0.8.0 (2019-12-19)

New commands:

+ [dephell package bug](https://dephell.readthedocs.io/cmd-package-bug.html) ([#318](https://github.com/dephell/dephell/pull/318)).
+ [dephell jail show](https://dephell.readthedocs.io/cmd-jail-show.html) ([#318](https://github.com/dephell/dephell/pull/319)).
+ [dephell inspect versioning](https://dephell.readthedocs.io/cmd-inspect-versioning.html) ([#318](https://github.com/dephell/dephell/pull/320)).

Improvements:

+ Meet [dephell_argparse](https://github.com/dephell/dephell_argparse) ([#317](https://github.com/dephell/dephell/pull/317)).
+ Meet [DepHell-powered projects](https://dephell.readthedocs.io/use-projects.html) list ([#339](https://github.com/dephell/dephell/pull/339))
+ Rename `dephell autocomplete` into `dephell self autocomplete`, and `dephell auth` into `dephell self auth` ([#321](https://github.com/dephell/dephell/pull/321)).
+ Support `allow-prereleases` key from Poetry 1.0.0 ([#323](https://github.com/dephell/dephell/pull/323))
+ From now DepHell will not be tested on Python 3.5 installation because nobody installs DepHell on Python 3.5 ([#334](https://github.com/dephell/dephell/pull/334)).
+ [a little bit more](https://github.com/dephell/dephell/milestone/3?closed=1).

## v.0.7.9 (2019-11-19)

New commands:

+ [dephell self uncache](cmd-self-uncache) ([#312](https://github.com/dephell/dephell/pull/312)).
+ [dephell self upgrade](cmd-self-upgrade) ([#311](https://github.com/dephell/dephell/pull/311)).
+ [dephell generate contributing](cmd-generate-contributing) ([#255](https://github.com/dephell/dephell/pull/255)).
+ [dephell inspect project](cmd-inspect-project) ([#296](https://github.com/dephell/dephell/pull/296)).
+ [dephell project validate](cmd-project-validate) ([#310](https://github.com/dephell/dephell/pull/310)).

Improvements:

+ Smart `setup.py` parsing. Meet [dephell_setuptools](https://github.com/dephell/dephell_setuptools) ([#308](https://github.com/dephell/dephell/pull/308)).
+ Stable `setup.py` generation ([#292](https://github.com/dephell/dephell/pull/292)).
+ Cleaner sdist ([#297](https://github.com/dephell/dephell/pull/297)).
+ [a little bit more](https://github.com/dephell/dephell/milestone/2?closed=1)

## v.0.7.8 (2019-10-22)

+ Fuzzy command name search ([#247](https://github.com/dephell/dephell/pull/247), [#122](https://github.com/dephell/dephell/issues/122)).
+ [Configure](config) DepHell with environment variables ([#248](https://github.com/dephell/dephell/pull/248)).
+ Colored JSON output ([#262](https://github.com/dephell/dephell/pull/262), [#260](https://github.com/dephell/dephell/pull/260), [#205](https://github.com/dephell/dephell/issues/205)).
+ Table output with `--table` ([#277](https://github.com/dephell/dephell/pull/277), [#267](https://github.com/dephell/dephell/pull/267), [#206](https://github.com/dephell/dephell/issues/206)).
+ New [attrs](https://www.attrs.org) ([#261](https://github.com/dephell/dephell/pull/261)).
+ ruamel.yaml instead of pyyaml ([#275](https://github.com/dephell/dephell/pull/275))
+ pip 19.3.1 support ([#276](https://github.com/dephell/dephell/pull/276)).
+ [a little bit more](https://github.com/dephell/dephell/milestone/1?closed=1)

## v.0.7.7 (2019-07-23)

+ Meet [dephell.org](https://dephell.org/) ([#244](https://github.com/dephell/dephell/pull/244)).
+ Lazy dependencies overwriting ([#232](https://github.com/dephell/dephell/pull/232), [#229](https://github.com/dephell/dephell/issues/229)).
+ Removed Snyk support ([#245](https://github.com/dephell/dephell/pull/245)).
+ Added custom User-Agent to all requests ([#242](https://github.com/dephell/dephell/pull/242), [#243](https://github.com/dephell/dephell/pull/243), [#231](https://github.com/dephell/dephell/issues/231))
+ Updated documentation interface ([#241](https://github.com/dephell/dephell/pull/241)).
+ `path` support for `pip`, `pipenv`, `poetry` ([#230](https://github.com/dephell/dephell/pull/230), [#227](https://github.com/dephell/dephell/issues/227)).

## v.0.7.6 (2019-07-17)

+ Docker support ([#220](https://github.com/dephell/dephell/pull/220), [#49](https://github.com/dephell/dephell/issues/49)).
+ Fixed dependencies for DepHell itself ([#218](https://github.com/dephell/dephell/pull/218), [#216](https://github.com/dephell/dephell/issues/216)).
+ Resolve paths to dependency files relatively to the project, and local dependencies relatively to the dependency file ([#217](https://github.com/dephell/dephell/pull/217), [#88](https://github.com/dephell/dephell/issues/88)).
+ Fixed repositories dumping for poetry ([#215](https://github.com/dephell/dephell/pull/215), [#177](https://github.com/dephell/dephell/issues/177)).
+ Simplified "usage" for commands' help ([#212](https://github.com/dephell/dephell/pull/212), [#120](https://github.com/dephell/dephell/issues/120)).
+ Install extras in [dephell project test](cmd-project-test) if needed ([#204](https://github.com/dephell/dephell/pull/204), [#195](https://github.com/dephell/dephell/issues/195)).

## v.0.7.5 (2019-07-07)

+ Vendorization ([dephell vendor download](cmd-vendor-download) and [dephell vendor import](cmd-vendor-import)) ([#194](https://github.com/dephell/dephell/pull/194), [#109](https://github.com/dephell/dephell/issues/109))
+ Now CLI for some commands accepts `--from` instead of `--to`, because it makes much more sense ([#194](https://github.com/dephell/dephell/pull/194), [#138](https://github.com/dephell/dephell/issues/138))
+ Always PEP-compatible name for names of wheel and sdist ([#203](https://github.com/dephell/dephell/pull/203), [#192](https://github.com/dephell/dephell/issues/192))
+ Now `--tag` option for [dephell project bump](cmd-project-bump) allows to specify tag prefix or template ([#199](https://github.com/dephell/dephell/pull/199), [#197](https://github.com/dephell/dephell/issues/197))
+ Meet [dephell_versioning](https://github.com/dephell/dephell_versioning), our new friend to handle packages versioning ([#191](https://github.com/dephell/dephell/pull/191), [#147](https://github.com/dephell/dephell/issues/147))
+ Shorter links in documentation ([#183](https://github.com/dephell/dephell/pull/183), [#182](https://github.com/dephell/dephell/issues/182))

## v.0.7.4 (2019-06-17)

+ Custom warehouse and simple index support ([#53](https://github.com/dephell/dephell/issues/53), [#128](https://github.com/dephell/dephell/pull/128)).
+ Fixed bug with packages names that made them incompatible with `pkg_resources` ([#110](https://github.com/dephell/dephell/issues/110), [#117](https://github.com/dephell/dephell/pull/117)).
+ Now `project bump` doesn't make git tag by default. Use `--tag` to add tag or add `tag = true` into config ([#114](https://github.com/dephell/dephell/pull/114), [#106](https://github.com/dephell/dephell/issues/106)).
+ Support for output into stdout for [dephell deps convert](cmd-deps-convert) ([#140](https://github.com/dephell/dephell/pull/140), [#136](https://github.com/dephell/dephell/issues/136)).
+ Allow to install prereleases into jail ([#118](https://github.com/dephell/dephell/pull/118), [#113](https://github.com/dephell/dephell/issues/113))
+ Smarter detection of owner name for `generate license`. You can force the name with `--owner=Name` (or `owner = "Name"` in config) ([#108](https://github.com/dephell/dephell/pull/108), [#107](https://github.com/dephell/dephell/issues/107), [#104](https://github.com/dephell/dephell/pull/104), [#87](https://github.com/dephell/dephell/issues/87)).
+ Local filesystem path support for `--warehouse` parameter ([#145](https://github.com/dephell/dephell/pull/145)).
+ Improved documentation ([#162](https://github.com/dephell/dephell/pull/162)).
+ Improved pre-release support for [dephell project bump](cmd-project-bump) ([#144](https://github.com/dephell/dephell/pull/144), [#142](https://github.com/dephell/dephell/issues/142)).
+ Improved poetry support ([#159](https://github.com/dephell/dephell/pull/159), [#152](https://github.com/dephell/dephell/issues/152), [#154](https://github.com/dephell/dephell/issues/154)).
+ Lazy load for bash autocomplete ([#132](https://github.com/dephell/dephell/pull/132)).

## v.0.7.3 (2019-05-19)

+ Added `imports` converter to get dependencies from package imports ([#97](https://github.com/dephell/dephell/pull/97)).
+ `sdist` includes tests if they not too big (`--sdist-ratio` option) ([#99](https://github.com/dephell/dephell/pull/99), [#95](https://github.com/dephell/dephell/issues/95)).
+ You can specify path to `.env` file ([#69](https://github.com/dephell/dephell/issues/69), [#100](https://github.com/dephell/dephell/pull/100)).
+ `dephell package list` doesn't fail if some packages missed on PyPI ([#85](https://github.com/dephell/dephell/issues/85), [#102](https://github.com/dephell/dephell/pull/102)).

## v.0.7.2 (2019-05-19)

+ [flit](https://flit.readthedocs.io/en/latest/pyproject_toml.html) support.
+ Missed meta information (like project version when you read from `requirements.txt`) will be automatically parsed from magic variables (like `__version__`) in the project source code.
+ Fix `plugins` parsing in poetry and `extras` parsing for `egg-info` and `sdist` ([#86](https://github.com/dephell/dephell/issues/86), [#89](https://github.com/dephell/dephell/pull/89)).
+ Fix `sdist` structure ([#94](https://github.com/dephell/dephell/pull/94), [#93](https://github.com/dephell/dephell/issues/93)).

## v.0.7.1 (2019-05-12)

+ [`dependency_links`](https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi) support for `setup.py`, `sdist` and `wheel` ([#79](https://github.com/dephell/dephell/pull/79), [#63](https://github.com/dephell/dephell/issues/63)).
+ Python 3.8 support ([#78](https://github.com/dephell/dephell/pull/78)).
+ Fix autocomplete for Mac OS X ([#65](https://github.com/dephell/dephell/pull/65), [#62](https://github.com/dephell/dephell/pull/62)).
+ Preserve dots in packages names ([#71](https://github.com/dephell/dephell/issues/71), [#80](https://github.com/dephell/dephell/pull/80), [pypa/pip#3666](https://github.com/pypa/pip/issues/3666)).
+ Make autocomplete for zsh really cool: added support for paths and choices ([#81](https://github.com/dephell/dephell/pull/81)).

## v.0.7.0 (2019-05-05)

+ Filter dependencies by envs ([#56](https://github.com/dephell/dephell/issues/56), [#58](https://github.com/dephell/dephell/pull/58)).
+ Change API: now all import must be from the second level. For example, `from dephell.models import Dependency` instead of `from dephell import Dependency` or `from dephell.models.dependency import Dependency`.
+ Support for `allow-prereleases`, `python` and `platform` options in poetry ([#59](https://github.com/dephell/dephell/pull/59)).
+ [Serial versioning](https://packaging.python.org/guides/distributing-packages-using-setuptools/#serial-versioning) support ([#60](https://github.com/dephell/dephell/pull/60)).

## v.0.6.0 (2019-04-30)

+ [Conda](https://github.com/conda/conda/) support ([#48](https://github.com/dephell/dephell/pull/48)).
    + [Anaconda Cloud](https://docs.anaconda.com/anaconda-cloud/).
    + Recipes from Github for [conda-forge](https://github.com/conda-forge/) and [bioconda](https://github.com/bioconda/bioconda-recipes/).
    + Support in `project show`, `project search` and `project releases`.
    + Converter for [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment).
+ Do not write hashes in `piplock` when some dependencies is local ([#41](https://github.com/dephell/dephell/issues/41), [#47](https://github.com/dephell/dephell/pull/47)).
+ Do not mess up setup.py on `project bump` ([#46](https://github.com/dephell/dephell/pull/46)).

## v.0.5.8 (2019-04-25)

+ Fix some typos ([#43](https://github.com/dephell/dephell/issues/43), [#40](https://github.com/dephell/dephell/pull/40)).
+ Fix autocomplete when data directory wasn't created ([#42](https://github.com/dephell/dephell/issues/42)).

## Before

+ The first public release: 2019-03-14.
+ The first proof-of-concept: 2018-09-03.
# dephell deps add

Add new dependencies into project.

Algorithm:

1. Get dependencies from `from` file.
1. Add new dependencies.
1. Check that these new dependencies has no conflicts with existing.
1. Write dependencies back into `from` file.

You can specify `--envs` to add dependencies into.

## Basic usage

Simple usage:

```bash
dephell deps add --from=poetry flake8
```

Best practice is specify your dependencies file in `pyproject.toml` DepHell config:

```bash
[tool.dephell.main]
from = {format = "poetry", path = "pyproject.toml"}
```

And after that DepHell will automatically detect your dependencies file:

```bash
dephell deps add flake8
```

See [configuration documentation](config) for more details.

## Specify dependencies environments

Environments for dependencies is the name of dependencies section (`main` and `dev` for `poetry` and `pipfile`) or name of [extras](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies). DepHell uses `main` by default, but you can specify another one:

```bash
dephell deps add --envs dev tests -- flake8==3.1.0 pytest
```

This will produce dependencies next lines in your poetry config:

```toml
[tool.poetry.dev-dependencies]
pytest = "*"
flake8 = "==3.1.0"

[tool.poetry.extras]
tests = ["flake8", "pytest"]
```

## See also

1. [How to configure DepHell](config).
1. [How to filter commands JSON output](filters).
1. [dephell deps convert](cmd-deps-convert) for details about locking dependencies and supported file formats.
1. [dephell deps install](cmd-deps-install) to install new dependencies into virtual environment.
1. [dephell package install](cmd-package-list) to install single package without adding it into requirements.
# dephell deps audit

Returns list of known vulnerabilities for your dependencies.

This command returns non-zero code if some vulnerabilities was found, so you can use it on CI.

## Sources

[pyup.io](https://pyup.io/) provides public repository [safety-db](https://github.com/pyupio/safety-db) with all vulnerabilities in their database. DepHell uses it. This repository automatically updates every month. So, if you want to get actual reports you have to use their official solutions. They provide Safety CI that [free for Open Source](https://pyup.io/pricing/) and $30 for personal usage. If you have "Business" plan you also can get API key and use their [official CLI](https://github.com/pyupio/safety).

We used [snyk.io](https://snyk.io/) before, but now they have removed RSS feed.

## Dependencies lookup

1. If some package and version explicitly specified then this package will be used. Example: `dephell deps audit jinja2==2.0`.
1. If `to` format is a lockfile (`piplock`, `pipfilelock` or `poetrylock`) dependencies from this file will be used.
1. If `to` isn't specified and `from` is a lockfile dependencies from this file will be used.
1. Otherwise it uses common [Python environment lookup](python-lookup). TL;DR: project venv, current venv, python from config, python from dependencies file, current interpreter.

## Examples

Audit dependencies:

```bash
$ dephell deps audit
[
  {
    "current": "2.10",
    "description": "Sandbox Escape in jinja2 (pip) with medium severity ",
    "latest": "2.10.1",
    "links": [
      "https://pypi.org/project/Jinja2/",
      "https://palletsprojects.com/blog/jinja-2-10-1-released",
      "https://snyk.io/vuln/SNYK-PYTHON-JINJA2-174126"
    ],
    "name": "jinja2",
    "updated": "2019-04-06",
    "vulnerable": "<2.10.1"
  }
]
```

Audit a package:

```bash
$ dephell deps audit jinja2==2.0
[
  {
    "current": "2.0",
    "description": "jinja2 2.7.2 fixes a security issue: Changed the default folder for the filesystem cache to be user specific and read and write protected on UNIX systems.  See  for more information.",
    "latest": "2.10.1",
    "links": [
      "http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=734747"
    ],
    "name": "jinja2",
    "updated": "2019-04-06",
    "vulnerable": "<2.7.2"
  },
  ...
]
```

Show only descriptions:

```bash
$ dephell deps audit --filter="#.description" jinja2==2.0
[
  "jinja2 2.7.2 fixes a security issue: Changed the default folder for the filesystem cache to be user specific and read and write protected on UNIX systems.  See  for more information.",
  "The default configuration for bccache.FileSystemBytecodeCache in Jinja2 before 2.7.2 does not properly create temporary files, which allows local users to gain privileges via a crafted .cache file with a name starting with __jinja2_ in /tmp.",
  "Sandbox Escape in jinja2 (pip) with medium severity "
]
```

Show only links:

```bash
$ dephell deps audit --filter="#.links.flatten()" jinja2==2.0
[
  "http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=734747",
  "https://nvd.nist.gov/vuln/detail/CVE-2014-1402",
  "https://pypi.org/project/Jinja2/",
  "https://palletsprojects.com/blog/jinja-2-10-1-released",
  "https://snyk.io/vuln/SNYK-PYTHON-JINJA2-174126"
]
```

See [filtering documentation](filters) for more information how to work with JSON output.

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [How to filter commands JSON output](filters).
1. [dephell deps outdated](cmd-deps-outdated) to find outdated dependencies.
1. [dephell package list](cmd-package-list) to show information about installed packages.
1. [dephell package show](cmd-package-show) to get information about package.
# dephell deps check

Show difference between virtual environment and project dependencies.

```bash
dephell deps check
INFO get dependencies (format=setuppy, path=setup.py)
INFO build dependencies graph...
[
  {
    "action": "remove",
    "installed": "2.2.1",
    "locked": null,
    "name": "deal"
  }
]
```

Fields:

+ `action` -- what would happened if you run [dephell deps sync](cmd-deps-sync). Can be `install`, `update` or `remove`.
+ `name` -- package name (wow!).
+ `installed` -- installed version of a package. `null` if a package isn't installed.
+ `locked` -- version of a package in the dependencies graph or locked by resolver. `null` if a package isn't represented in dependencies graph.

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [dephell deps install](cmd-deps-install) to install project dependencies.
1. [dephell venv create](cmd-venv-create) to create virtual environment for dependencies.
1. [dephell package install](cmd-package-install) to install single package
1. [dephell jail install](cmd-package-install) to install some Python CLI tool into isolated virtual environment.
# dephell deps convert

Convert dependencies between formats. Dephell will automagically lock them if needed and resolve all conflicts.

Dephell uses four pieces of information for conversion:

1. `--from-format`: The format to convert from (e.g. `poetry`)
1. `--from-path`: The path to the file to read from (e.g. `pyproject.toml`)
1. `--to-format`: The format to convert to (e.g. `setuppy`)
1. `--to-path`: The path to the file where the result should be put (e.g. `setup.py`). You can provide the special case 'stdout' to this option to output to the screen instead of a file.

Dephell can try to guess the formats or paths you want to use given the other piece of information, giving you three different ways to specify what you want:

1. Explicitly specify path and format: `--from-format=poetry --from-path=pyproject.toml` and `--to-format=setuppy --to-path=setup.py`.
1. Specify only path: `--from=pyproject.toml` and `--to=setup.py`.
1. Specify only format: `--from=poetry` and `--to=setuppy`.

## Supported formats

1. Archives:
    1. [*.egg-info](https://setuptools.readthedocs.io/en/latest/formats.html) (`egginfo`)
    1. [*.tar.gz](https://packaging.python.org/glossary/#term-distribution-package) (`sdist`)
    1. [*.whl](https://pythonwheels.com) (`wheel`)
1. [pip](https://pip.pypa.io/en/stable/):
    1. [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files) (`pip`)
    1. [requirements.lock](https://nvie.com/posts/pin-your-packages/) (`piplock`)
1. [pipenv](https://pipenv.readthedocs.io/en/latest/):
    1. [Pipfile](https://github.com/pypa/pipfile) (`pipfile`)
    1. [Pipfile.lock](https://stackoverflow.com/a/49867443/8704691) (`pipfilelock`)
1. [poetry](https://github.com/sdispater/poetry):
    1. [pyproject.toml](https://poetry.eustace.io/docs/pyproject/) (`poetry`)
    1. [poetry.lock](https://poetry.eustace.io/docs/basic-usage/#installing-without-poetrylock) (`poetrylock`)
1. Environment:
    1. Imports in the package (`imports`). Pass path to package or module and dephell will automatically detect required packages.
    1. Installed packages (`installed`). It works like [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/). Dephell can only read from this format, of course. If you want to install packages, use [install command](cmd-deps-install).
1. Other:
    1. [setup.py](https://docs.python.org/3/distutils/setupscript.html) (`setuppy`)
    1. [flit](https://flit.readthedocs.io/en/latest/pyproject_toml.html) (`flit`)
    1. [conda](https://conda.io/en/latest/)'s [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually) (`conda`)
    1. [pyproject.toml build-system requires](https://www.python.org/dev/peps/pep-0518/#build-system-table) (`pyproject`)

## Examples

Lock dependencies for Pipfile:

```bash
$ dephell deps convert --from=Pipfile --to=Pipfile.lock
```

Or the same, but more explicit:

```bash
$ dephell deps convert \
    --from-format=pipfile --from-path=Pipfile \
    --to-format=pipfilelock --to-path=Pipfile.lock
```

Best practice is specify your dependencies file in `pyproject.toml` DepHell config:

```bash
[tool.dephell.main]
from = {format = "pipfile", path = "Pipfile"}
to = {format = "pipfilelock", path = "Pipfile.lock"}
```

And after that DepHell will automatically detect your dependencies file:

```bash
$ dephell deps convert
```

You can still override this config for one-off actions:

```bash
$ dephell deps convert --to requirements.txt
```

See [configuration documentation](config) for more details.

## More examples

You can convert anything to anything:

1. Lock requirements.txt: `dephell deps convert --from=requirements.in --to=requirements.txt`
1. Lock Pipfile: `dephell deps convert --from=Pipfile --to=Pipfile.lock`
1. Lock poetry: `dephell deps convert --from=pyproject.toml --to=poetry.lock`
1. Migrate from setup.py to poetry: `dephell deps convert --from=setup.py --to=pyproject.toml`
1. Migrate from pipenv to poetry: `dephell deps convert --from=Pipenv --to=pyproject.toml`
1. Generate setup.py for poetry (to make project backward compatible with setuptools): `dephell deps convert --from=pyproject.toml --to=setup.py`
1. Generate requirements.txt from Pipfile to work on a pipenv-based project without pipenv: `dephell deps convert --from=Pipenv --to=requirements.txt`
1. Generate requirements.txt from poetry to work on a poetry-based project without poetry: `dephell deps convert --from=pyproject.toml --to=requirements.txt`
1. Pipe poetry requirements into pip for installation in a custom environment: `pip install -r <(dephell deps convert --to-path stdout --to-format pip)`

## Filter dependencies

You can filter dependencies by envs with `--envs` flag. All dependencies included in `main` or `dev` env. Also, some dependencies can be included in [extras](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies). There is an example of poetry config with envs in comments:

```toml
[tool.poetry.dependencies]
python = ">=3.5"
aiohttp = "*"       # main, asyncio
textdistance = "*"  # main

[tool.poetry.dev-dependencies]
pytest = "*"    # dev, tests
sphinx = "*"    # dev

[tool.poetry.extras]
asyncio = ["aiohttp"]
tests = ["pytest"]
```

Examples, how to filter these deps:

```bash
$ dephell deps convert --envs main
# aiohttp, textdistance

$ dephell deps convert --envs asyncio
# aiohttp

$ dephell deps convert --envs main tests
# aiohttp, textdistance, pytest
```

## See also

1. [dephell project build](cmd-deps-install) to fast convert dependencies into setup.py, sdist and wheel.
1. [dephell deps install](cmd-deps-install) to install project dependencies.
1. [dephell deps tree](cmd-deps-tree) to show dependencies tree for project.
# dephell deps install

Install project dependencies.

Dependencies from `to` option will be used if available. This is because when you specified in config file source dependencies in `from` and locked dependencies in `to` then, of course, you want to install dependencies from lock file. However, if `to` (and `to-format` and `to-file`) isn't specified in the config and CLI arguments then `from` will be used.

Place to install lookup:

1. If some virtual environment already active in the current shell then this environment will be used.
1. If virtual environment for current project (can be specified with `--config`) and environment (can be specified with `--env`) exists then this virtual environment will be used. This is the reason why you have to [create virtual environment](cmd-venv-create) before dependencies installation.
1. If virtual environment isn't found then your current python will be used.

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [dephell deps sync](cmd-deps-sync) to install project dependencies and drop obsolete packages.
1. [dephell venv create](cmd-venv-create) to create virtual environment for dependencies.
1. [dephell package install](cmd-package-install) to install single package
1. [dephell jail install](cmd-package-install) to install some Python CLI tool into isolated virtual environment.
# dephell deps licenses

This command shows license for all your project's dependencies (from `from` section of current environment) in JSON format. Dephell detects the same license described in the different ways, like "MIT" and "MIT License", and combine these dependencies together. Dephell shows licenses **for all project's dependencies** including dependencies of dependencies.

```bash
$ dephell deps licenses

INFO resolved
{
  "Apache-2.0": [
    "aiofiles",
    "aiohttp",
    ...
  ],
  ...
  "Python Software Foundation License": [
    "backports-weakref",
    "editorconfig",
    "typing",
    "typing-extensions"
  ],
}
```

If you want to process this JSON to other tool disable dephell's helping output with `--level` and `--silent` arguments:

```bash
$ dephell deps licenses --level=WARNING --silent | jq --compact-output '."Apache-2.0"'
["aiofiles","aiohttp",...]
```

This example uses [jq](https://stedolan.github.io/jq/) to filter only one license from output. However, for simple filtering by license name you can just pass this name as positional argument in the command:

```bash
$ dephell deps licenses --filter="Apache-2.0"

INFO resolved
[
  "aiofiles",
  "aiohttp",
  ...
]
```

## See also

1. [Example of this command usage](use-licenses)
1. [dephell generate license](cmd-generate-license) to make license file for your project.
1. [How dephell works with config and parameters](config)
1. [Full list of config parameters](params)
# dephell deps outdated

Show outdated project dependencies. It compares latest package version on [PyPI](https://pypi.org/) and version in the lockfile or project environment and shows packages that version is different.

Place to get dependencies from lookup:

1. If `to` format is a lockfile (`piplock`, `pipfilelock` or `poetrylock`) dependencies from this file will be used.
1. If `to` isn't specified and `from` is a lockfile dependencies from this file will be used.
1. Otherwise it uses common [Python environment lookup](python-lookup). TL;DR: project venv, current venv, python from config, python from dependencies file, current interpreter.

Some packages can have different version because their latest version incompatible with some other project dependencies, and DepHell's dependency resolver has locked their older (compatible) version. These packages also will be listed in the `dephell deps outdated` command output because explicit better than implicit.

This command returns non-zero code if some vulnerabilities was found, so you can use it on CI.

## Usage

Show all outdated packages:

```bash
$ dephell deps outdated

[
  {
    "description": "More routines for operating on iterables, beyond itertools",
    "locked": "6.0.0",
    "latest": "7.0.0",
    "name": "more-itertools",
    "updated": "2019-03-28"
  },
  ...
]
```

[Filter](filters) only package name and latest release upload time:

```bash
$ dephell deps outdated --filter="#.name+updated.each()"
INFO get packages from project environment (path=/home/gram/.local/share/dephell/venvs/dephell-nLn6/main)
[
  {
    "name": "more-itertools",
    "updated": "2019-03-28"
  },
  ...
]
```

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [How to filter commands JSON output](filters).
1. [dephell deps audit](cmd-deps-audit) to check dependencies for known vulnerabilities.
1. [dephell package list](cmd-package-list) to show information about installed packages.
1. [dephell package show](cmd-package-show) to get information about package.
1. [dephell venv create](cmd-venv-create) to create virtual environment for dependencies.
1. [dephell package install](cmd-package-install) to install a single package.
# dephell deps sync

This command works in the same way as [dephell deps install](cmd-deps-install), but also removes from environment all packages that not presented in project dependencies (obsolete).

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [dephell venv create](cmd-venv-create) to create virtual environment for dependencies.
1. [dephell deps install](cmd-deps-install) to install dependencies without dropping obsolete packages.
1. [dephell package install](cmd-package-install) to install single package.
1. [dephell jail install](cmd-package-install) to install some Python CLI tool into isolated virtual environment.
# dephell deps tree

Show dependencies tree for your dependencies  from `from` section or given package.

Show project dependencies:

```bash
$ dephell deps tree
- aiofiles [required: *, locked: 0.4.0, latest: 0.4.0]
- aiohttp [required: *, locked: 3.5.4, latest: 3.5.4]
  - async-timeout [required: <4.0,>=3.0, locked: 3.0.1, latest: 3.0.1]
  - attrs [required: >=17.3.0, locked: 19.1.0, latest: 19.1.0]
  - chardet [required: <4.0,>=2.0, locked: 3.0.4, latest: 3.0.4]
  - idna-ssl [required: >=1.0, locked: 1.1.0, latest: 1.1.0]
    - idna [required: >=2.0, locked: 2.8, latest: 2.8]
  ...
```

Field `locked` shows version that was resolved by this command, **not** the version that represented in any environment or lockfile.

Show dependencies for given package:

```bash
$ dephell deps tree aiohttp==3.5.4
- aiohttp [required: ==3.5.4, locked: 3.5.4, latest: 3.5.4]
  - async-timeout [required: <4.0,>=3.0, locked: 3.0.1, latest: 3.0.1]
  - attrs [required: >=17.3.0, locked: 19.1.0, latest: 19.1.0]
  - chardet [required: <4.0,>=2.0, locked: 3.0.4, latest: 3.0.4]
  - idna-ssl [required: >=1.0, locked: 1.1.0, latest: 1.1.0]
    - idna [required: >=2.0, locked: 2.8, latest: 2.8]
  ...
```

## Graph output

You can specify `--type=graph` to build dependencies graph:

```bash
$ dephell deps tree --type=graph aiohttp==3.5.4
```

It will create next graph in `.dephell_report` directory:

![graph example](../assets/graph-example.png)

## JSON output

You can specify `--type=json` to generate JSON with information for every node in graph:

```bash
$ dephell deps tree --type=json aiohttp==3.5.4
[
  {
    "best": "3.5.4",
    "constraint": "==3.5.4",
    "dependencies": [
      "attrs",
      "chardet",
      "multidict",
      "async-timeout",
      "yarl",
      "idna-ssl",
      "typing-extensions"
    ],
    "latest": "3.5.4",
    "name": "aiohttp"
  },
  ...
]
```

As for any other command, you can [filter](filters) JSON output:

```bash
dephell deps tree --type=json --filter="#.name+constraint.each()" aiohttp==3.5.4
[
  {
    "constraint": "==3.5.4",
    "name": "aiohttp"
  },
  {
    "constraint": "<4.0,>=3.0",
    "name": "async-timeout"
  },
  ...
]
```

## See also

1. [Command usage example for git repo](use-tree-git).
1. [How to filter commands JSON output](filters).
1. [dephell package outdated](cmd-package-list) to show outdated packages in a lockfile or project virtual environment.
1. [dephell package list](cmd-package-list) to show information about installed packages.
1. [dephell package show](cmd-package-show) to get information about single package.
# dephell docker create

Create a new docker container for the project. Usually, you don't need to call this command directly because all other commands in [dephell docker](index-docker) group (except [dephell docker destroy](cmd-docker-destroy)) will create container if it doesn't exist.

```bash
$ sudo dephell docker create
INFO creating container for project... (container=dephell-dephell-nLn6-main)
INFO image not found, pulling... (repository=python, tag=latest)
INFO pulled
INFO container created
```

By default, the command creates container with authogenerated name (based on project path and current environment) from [python:latest](https://hub.docker.com/_/python) You can specify these parameters in [dephell config](config):

```toml
[tool.dephell.main.docker]
container = "container-name"
repo = "python"
tag = "3.7.4-stretch"
```

Also, DepHell mounts your current directory into `/opt/project/` inside the container. However, it won't be mounted if you're running this command from root or home folder because it's too much to mount.

## See also

1. [dephell docker prepare](cmd-docker-prepare) to make a container nice.
1. [dephell venv create](cmd-venv-create) to create a virtual environment (less isolation, better integration).
1. [dephell docker destroy](cmd-docker-destroy) to remove a container.
1. [dephell docker shell](cmd-docker-shell) to run shell inside a container.
# dephell docker destroy

Remove docker container for current project and environment. Like [dephell venv destroy](cmd-venv-destroy), but for docker.

## See also

1. [dephell docker stop](cmd-docker-stop) to stop processes in a container without removing it.
1. [dephell docker create](cmd-docker-create) to create a new container.
# dephell docker prepare

Installs some nice things into container to make work with it more pleasant:

+ [zsh](https://en.wikipedia.org/wiki/Z_shell)
+ [oh-my-zsh](https://ohmyz.sh/)
+ [glances](https://nicolargo.github.io/glances/)
+ [pure](https://github.com/sindresorhus/pure)
+ dephell

## See also

1. [dephell docker create](cmd-docker-create) to create a clean container.
1. [dephell docker shell](cmd-docker-shell) to run a shell inside a container.
1. [dephell docker run](cmd-docker-run) to run a command inside a container.
# dephell docker run

Run a command inside the Docker container.

```bash
$ sudo dephell docker run echo "Hello, world"

[sudo] password for gram:
INFO running... (container=dephell-dephell-nLn6-main, command=['echo', 'Hello, world'])
Hello, world
INFO done
```

If a command isn't specified, dephell will try to get it from [config](config):

```toml
[tool.dephell.main]
command = "echo 'Hello, world!'"
```

## See also

1. [dephell docker create](cmd-docker-create) to read how dephell creates a new container.
1. [dephell docker shell](cmd-docker-shell) to run a shell inside a container.
1. [dephell docker stop](cmd-docker-stop) to stop command execution inside a container.
# dephell docker shell

Run a shell inside of the Docker container for a current project and environment. Dephell tries to get the best shell in the following order:

1. zsh
1. bash
1. sh

The command is also useful for quick experiments with project in the isolated environment:

```bash
$ sudo dephell docker shell --docker-container=tmp
WARNING creating container... (container=tmp)
INFO openning shell... (container=tmp)
sh: 1: zsh: not found
root@d6ceb924fea6:/opt/project#
```

## See also

1. [dephell docker create](cmd-docker-create) to read how dephell creates a new container.
1. [dephell docker run](cmd-docker-run) to run a command inside a container.
# dephell docker stop

The command stops the Docker container for a current project and environment. It works like [docker stop](https://docs.docker.com/engine/reference/commandline/stop/). If something (even shell) executes inside the container, it will be stopped. However, you won't lost created files and installed programs inside of the container. If you want to get rid of everything inside, use [dephell docker destroy](cmd-docker-destroy).

## See also

1. [dephell docker destroy](cmd-docker-destroy) to remove a container.
1. [dephell docker shell](cmd-docker-shell) to run a shell inside a container.
1. [dephell docker run](cmd-docker-run) to run a command inside a container.
# dephell docker tags

Get available tags for a docker repository on [Docker Hub](https://hub.docker.com/). Use [filters](filters) to get only last 10 tags:

```bash
$ dephell docker tags --docker-repo=elasticsearch --filter=:10
WARNING cannot find config file
[
  "7.2.0",
  "6.8.1",
  "7.1.1",
  "7.1.0",
  "6.8.0",
  "7.0.1",
  "6.7.2",
  "7.0.0",
  "6.7.1",
  "5-alpine"
]
```

## See also

1. [How filters work](filters)
1. [dephell docker create](cmd-docker-create) to create a new container.
# dephell generate authors

This command looks into your git commits history, get list of all contributors, removes duplicates by e-mail and saves it into `AUTHORS` file.

```bash
$ dephell generate authors
```

Easy :)

## See also

1. [dephell generate license](cmd-generate-license) to make license file for project.
# dephell generate config

This command scans project directory for known dependencies files, try to combine them into known most common combinations like `Pipfile + Pipfile.lock` and makes dephell config for them.

```bash
$ dephell generate config
```

Good for quick start.

## See also

1. [dephell inspect config](cmd-inspect-config) to show current config parameters.
1. [How dephell works with config and parameters](config)
1. [Full list of config parameters](params)
# dephell generate contributing

Adds `CONTRIBUTING.md` for your project. It reads environments from the dephell config and looks for some known environments, like `pytest`, `typing`, `flake8`. For every such environment a section with instructions will be created in the output file.

## See also

1. [dephell generate license](cmd-generate-license) to make LICENSE file for project.
1. [dephell generate travis](cmd-generate-travis) to generate config for TravisCI.
# dephell generate editorconfig

This command scans project directory for known files formats and makes [.editorconfig](https://editorconfig.org) for them.

```bash
$ dephell generate editorconfig
```

## See also

1. [dephell generate license](cmd-generate-license) to make LICENSE file for project.
1. [dephell generate authors](cmd-generate-authors) to make AUTHORS file for project.
# dephell generate license

Add LICENSE file in the project. This command gets the license name as input, downloads license template, substitutes current year and current system user name and saves result into LICENSE file.

```bash
$ dephell generate license MIT
$ dephell generate license --owner="Your Company Name" Apache-2.0
```

## Which license should I choose

For open source software use [MIT License](https://en.wikipedia.org/wiki/MIT_License). For proprietary software pay to a lawyer to help you make right choose in your case. You can discover other licenses on the [choosealicense.com](https://choosealicense.com/), but all of them has some limitations in real world that can harm your project:

1. [Apache 2.0](https://en.wikipedia.org/wiki/Apache_License) cool license, but requires you to insert license notice at the beginning of every source code file in the project. Also, Apache 2.0 requires all contributors to track all changes in a special file (usually named CHANGELOG). It takes some time that you can spendmore effective. There are some special tools that allow you to [generate CHANGELOG](https://stackoverflow.com/a/23047890/8704691) and [insert copyright notice](https://github.com/licenses/lice) in source files, but so.
1. [GNU GPLv3](https://en.wikipedia.org/wiki/GNU_General_Public_License#Version_3) forbid to use your project in proprietary projects. It useful when you want to make open source only for open source, but really limit your project popularity and usage. Almost all developers writes some proprietary software, and only a bit dvelopers get paid for open source. So, don't forbid your users to use your code.
1. [The Unlicense](https://en.wikipedia.org/wiki/Unlicense) and [WTFPL](https://en.wikipedia.org/wiki/WTFPL) have limitations on usage in some countries. Don't use them.
1. Most of your users don't know about other licenses like [Mozilla Public License](https://en.wikipedia.org/wiki/Mozilla_Public_License). Don't force them to read about new licenses specially for your project. Please, value their time.

## See also

1. [dephell deps licenses](cmd-deps-licenses) to show licenses for all project dependencies.
1. [dephell generate authors](cmd-generate-authors) to make AUTHORS file for project.
# dephell generate travis

Adds `.travis.yml` config for your project.

1. If your `main` env has lockfile as `to` format, DepHell adds [audit](cmd-deps-audit) and [outdated](cmd-deps-outdated) checks. Also, DepHell marks they as `allow_failures` because these command can produce false-positive alerts. So, we don't want to fail whole your CI besause of it.
1. If some env has `pytest` command than this env will be ran on next envs:
    1. Linux: Python 3.5, 3.6, 3.7.
    1. Mac OS: Python 3.6.
1. If some envs has `command` specified (not `pytest`) then DepHell will make env for them too.

Of course, this file has to be manually validated and cleaned before running on CI. However, this is good bootstrap. If command doesn't work to you then use config example below to configure it on your own.

Output example:

```yaml
# Config for Travis CI, tests powered by DepHell.
# https://travis-ci.org/
# https://github.com/dephell/dephell

language: python

before_install:
  # show a little bit more information about environment
  - sudo apt-get install -y tree
  - env
  - tree
  # install DepHell
  # https://github.com/travis-ci/travis-ci/issues/8589
  - curl https://raw.githubusercontent.com/dephell/dephell/master/install.py | /opt/python/3.6/bin/python
  - dephell inspect self
install:
  - dephell venv create --env=$ENV --python="/opt/python/$TRAVIS_PYTHON_VERSION/bin/python"
  - dephell deps install --env=$ENV
script:
  - dephell venv run --env=$ENV

matrix:
  allow_failures:
    - name: security
    - name: outdated

  include:
    - name: security
      install:
        - "true"
      script:
        - dephell deps audit
    - name: outdated
      install:
        - "true"
      script:
        - dephell deps outdated

    - python: "3.6"
      env: ENV=flake8

    - python: "3.6"
      env: ENV=typing

    - python: "3.5"
      env: ENV=pytest
    - python: "3.6"
      env: ENV=pytest
    - python: "3.7-dev"
      env: ENV=pytest
    - python: "pypy3.5"
      env: ENV=pytest

    - os: osx
      language: generic
      env: ENV=pytest
      before_install:
        - curl https://raw.githubusercontent.com/dephell/dephell/master/install.py | /usr/local/bin/python3
        - dephell inspect self
      install:
        - dephell venv create --env=$ENV --python=/usr/local/bin/python3
        - dephell deps install --env=$ENV
```

## See also

1. [dephell generate config](cmd-generate-config) to make DepHell config for project.
# dephell inspect auth

Shows all [added credentials](cmd-self-auth).

```bash
$ dephell self auth example.com gram "p@ssword"
INFO credentials added (hostname=example.com, username=gram)

$ dephell inspect auth
[
  {
    "hostname": "example.com",
    "password": "p@ssword",
    "username": "gram"
  }
]
```

Use [filters](filters) to remove passwords from output:

```bash
$ dephell inspect auth --filter="#.hostname+username.each()"
[
  {
    "hostname": "example.com",
    "username": "gram"
  }
]
```

## See also

1. [dephell self auth](cmd-self-auth) to add new credentials.
1. [dephell inspect config](cmd-inspect-config) to show all other params in the config.
1. [Private PyPI repository](use-warehouse) usage details and examples.
# dephell inspect config

Shows current dephell config options. You can combine it with different arguments to inspect dephell behavior.

## Show all config

```bash
$ dephell inspect config
{
  "bin": "/home/gram/.local/bin",
  "bitbucket": "https://api.bitbucket.org/2.0",
  "cache": {
    "path": "/home/gram/.local/share/dephell/cache",
    "ttl": 3600
  },
  "envs": [
    "main"
  ],
  ...
  "warehouse": "https://pypi.org/pypi/"
}
```

## Filter output

Show one section:

```bash
$ dephell inspect config --filter=from
{
  "format": "poetry",
  "path": "pyproject.toml"
}

```

Show one value:

```bash
$ dephell inspect config --filter=from-format
poetry

$ dephell inspect config --filter=warehouse
https://pypi.org/pypi/
```

## Combine it with arguments

```bash
$ dephell inspect config --from-path=lol --filter=from
{
  "format": "poetry",
  "path": "lol"
}

$ dephell inspect config --from=setup.py --filter=from
{
  "format": "setuppy",
  "path": "setup.py"
}
```

## See also

1. [dephell generate config](cmd-generate-config) to initialize DepHell config for project.
1. [How dephell works with config and parameters](config).
1. [Full list of config parameters](params).
1. [How to filter commands JSON output](filters).
# dephell inspect project

Shows metainfo from the `from` dependency file, like project name, version, required python, etc.

```bash
$ dephell inspect project
{
  "description": "Dependency resolution for Python",
  "links": {
    "documentation": "https://dephell.org/docs/",
    "homepage": "https://dephell.org/",
    "repository": "https://github.com/dephell/dephell"
  },
  "name": "dephell",
  "python": ">=3.5",
  "version": "0.7.8"
}
```

## See also

1. [dephell project validate](cmd-project-validate) to check project metadata for compatibility issues and missed information.
1. [dephell inspect config](cmd-inspect-config) to get information about the project configuration.
# dephell inspect self

Shows information about DepHell installation.

```bash
$ dephell inspect self
{
  "path": "/home/gram/Documents/dephell/dephell",
  "python": "/usr/local/bin/python3.7",
  "version": "0.3.1"
}
```

## See also

1. [dephell self uncache](cmd-self-uncache) to remove dephell cache.
1. [dephell self upgrade](cmd-self-upgrade) to upgrade dephell and dependencies to the latest version.
1. [dephell self autocomplete](cmd-venv-create) to enable params autocomplete for commands in your shell.
1. [dephell inspect config](cmd-inspect-config) to get information about config parameters.
# dephell inspect venv

Shows information about virtual environment for current project and environment.

```bash
$ dephell inspect venv
{
  "activate": "/home/gram/.local/share/dephell/venvs/dephell-nLn6/main/bin/activate",
  "bin": "/home/gram/.local/share/dephell/venvs/dephell-nLn6/main/bin",
  "exists": true,
  "lib": "/home/gram/.local/share/dephell/venvs/dephell-nLn6/main/lib/python3.7/site-packages",
  "lib_size": "32.93Mb",
  "project": "/home/gram/Documents/dephell",
  "python": "/home/gram/.local/share/dephell/venvs/dephell-nLn6/main/bin/python3.7",
  "venv": "/home/gram/.local/share/dephell/venvs/dephell-nLn6/main"
}
```

Specify `--env` to get information about other environment:

```bash
$ dephell inspect venv --env=docs
```

Specify `--filter` to get one field from command output:

```bash
$ dephell inspect venv --filter=project
/home/gram/Documents/dephell
```

## See also

1. [dephell venv create](cmd-venv-create) for information about virtual environments management in DepHell.
1. [dephell inspect config](cmd-inspect-config) to get information about config parameters like venv path template.
1. [How to filter commands JSON output](filters).
# dephell inspect versioning

Shows info about project versioning scheme and current version.

```bash
$ dephell inspect versioning
{
  "rules": {
    "supported": [
      "init",
      "local",
      "major",
      "minor",
      "patch",
      "pre",
      "premajor",
      "preminor",
      "prepatch",
      "release"
    ],
    "unsupported": [
      "dev",
      "post"
    ]
  },
  "scheme": "semver",
  "version": "0.7.9"
}
```

Read about schemes and rules in [dephell project bump](cmd-project-bump) docs.

## See also

1. [dephell project bump](cmd-project-bump) to bump project version.
1. [dephell inspect project](cmd-inspect-project) to get information about the project metainfo.
1. [dephell inspect config](cmd-inspect-config) to get information about the project configuration.
# dephell jail install

Install package into isolated virtual environment. It works similar to [pipsi](https://github.com/mitsuhiko/pipsi), but with DepHell magic:

1. Creates virtual environment named after package to install.
1. Resolves package dependencies.
1. Installs package and dependencies.
1. Creates symlinks for package entrypoints.

Like [dephell package install](cmd-package-install), it can parse any [pip-compatible input](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format). For example:

```bash
$ dephell jail install isort[requirements,pipfile]
```

It will install [isort](https://github.com/timothycrosley/isort) with [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files) and [Pipfile](https://github.com/pypa/pipfile) support in the isolated virtual environment named `isort`.

## See also

1. [How DepHell choose Python interpreter](python-lookup).
1. [dephell jail list](cmd-jail-list) to show all created jails.
1. [dephell jail remove](cmd-jail-remove) to remove jail.
1. [dephell venv create](cmd-venv-create) for information about virtual environments management in DepHell.
1. [dephell package install](cmd-package-install) to install package into project virtual environment.
1. [dephell deps install](cmd-deps-install) to install all project dependencies.
# dephell jail list

Shows a list of all packages installed by [dephell jail install](cmd-jail-install) and their endpoints.

```bash
$ dephell jail list
{
  "flake8": [
    "flake8"
  ],
  "httpie": [
    "http"
  ]
}
```

Output can be filtered by jail name:

```bash
$ dephell jail list --filter=httpie
[
  "http"
]
```

## See also

1. [How to filter commands JSON output](filters).
1. [dephell jail show](cmd-jail-show) to show more info about a particular jail.
1. [dephell jail install](cmd-jail-install) to create a new jail.
1. [dephell jail remove](cmd-jail-remove) to remove jail.
# dephell jail remove

Removes isolated virtual environment and symlinks on it created by [dephell jail install](cmd-jail-install).

```bash
$ dephell jail remove isort
```

## See also

1. [dephell jail install](cmd-jail-install) to create a new jail.
1. [dephell jail list](cmd-jail-list) to show all created jails.
# dephell jail list

Shows information about a jail installed by [dephell jail install](cmd-jail-install).

```bash
$ dephell jail list
{
  "flake8": [
    "flake8"
  ],
  "httpie": [
    "http"
  ]
}
```

## See also

1. [dephell jail list](cmd-jail-list) to show a little bit less information but about all installed jails.
1. [dephell jail install](cmd-jail-install) to create a new jail.
1. [dephell jail remove](cmd-jail-remove) to remove jail.
# dephell jail try

Try python packages in an isolated environment.

Try [textdistance](https://github.com/orsinium/textdistance):

```bash
$ dephell jail try textdistance
INFO creating venv... (python=/usr/local/bin/python3.7, venv=/tmp/tmpgixqt4_q)
INFO build dependencies graph...
INFO installation... (executable=/tmp/tmpgixqt4_q/bin/python3.7, packages=1)
Collecting textdistance==4.1.3 (from -r /tmp/tmpduyecsir/requirements.txt (line 2))
Installing collected packages: textdistance
Successfully installed textdistance-4.1.3
INFO installed
INFO running...
Python 3.7.0 (default, Dec 24 2018, 12:47:36)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

In this example DepHell installs latest `texdistance` release in a temporary virtual environment and runs python interpreter with already imported `textdistance` inside.

Use [ipython](https://ipython.org/) instead of standard python interpreter:

```bash
$ dephell jail try --command=ipython textdistance
```

Set python version:

```bash
$ dephell jail try --python=3.5 textdistance
...
Python 3.5.3 (928a4f70d3de, Feb 08 2019, 10:42:58)
[PyPy 7.0.0 with GCC 6.2.0 20160901] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>>
```

Install flake8 and plugin for it and run checks on given path:

```bash
$ dephell jail try --command="flake8 ./dephell" flake8 flake8-commas
```

## See also

1. [How DepHell choose Python interpreter](python-lookup).
1. [dephell jail install](cmd-jail-install) to install CLI tool in permanent jail.
1. [dephell venv create](cmd-venv-create) for information about virtual environments management in DepHell.
1. [dephell package install](cmd-package-install) to install package into project virtual environment.
1. [dephell deps install](cmd-deps-install) to install all project dependencies.
# dephell package bug

Report bug in a package. The command finds a bug tracker, associated with the package, and opens the tracker URL in a new browser tab.

```bash
$ dephell package bug flask
```

Packages in Conda also supported:

```bash
$ dephell package bug --repo conda textdistance
```

## See also

1. [dephell package show](cmd-package-show) to get information about package.
1. [dephell package search](cmd-package-search) to search packages on [PyPI](https://pypi.org/).
# dephell package downloads

Get downloads statistic for package from [PyPI.org](https://pypi.org/). This command works with amazing [PyPI Stats](https://pypistats.org/) API, God bless this service.

```bash
$ dephell package downloads textdistance
{
  "pythons": [
    {
      "category": "35",
      "chart": "▅▂▄▃▁▂▄ ▇█▄▄▆█▄ ▂▂▄▅▁▁▄ ▅▄▅▄▁▁▄",
      "day": 120,
      "month": 3726,
      "week": 786
    },
    ...
  ],
  "systems": [
    {
      "category": "Linux",
      "chart": "▄▄▅▃▂▁█ ▇█▄▄▄▄▄ ▅▃▄▅▁▁▄ ▅▃▅▄▁▁▄",
      "day": 259,
      "month": 6947,
      "week": 1421
    },
    ...
  ],
  "total": {
    "day": 284,
    "month": 8751,
    "week": 1731
  }
}
```

## Fields

+ `pythons` -- statistic by python versions.
+ `systems` -- statistic by operating systems.
+ `total.day` -- total downloads yesterday.
+ `total.week` -- total downloads for previous 7 days.
+ `total.month` -- total downloads from yesterday to the same day in the previous month.
+ `pythons.#.chart` and `systems.#.chart` -- downloads bar chart for last 28 days grouped by 7 days.
+ `pythons.#.day` and `systems.#.day` -- total downloads yesterday.
+ `pythons.#.week` and `systems.#.week` -- total downloads for previous 7 days.
+ `pythons.#.month` and `systems.#.month` -- total downloads for previous 30 days.

## Filtering

This command, as all commands with JSON output, supports [filtering](filters). For example, get only month stat for pythons:

```bash
dephell package downloads textdistance --filter="pythons.#.category+month.each()"
[
  {
    "category": "27",
    "month": 332
  },
  ...
]
```

## See also

1. [How to filter commands JSON output](filters).
1. [dephell package show](cmd-package-show) to get information about package.
1. [dephell package search](cmd-package-search) to search packages on [PyPI](https://pypi.org/).
# dephell package install

Install package. See [how DepHell looks for Python environment](python-lookup).

```bash
$ dephell package install pytest
```

Package specification the same as for [pip requirements file](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format):

```bash
$ dephell package install requests[security]>=2.17.0
```

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [dephell venv create](cmd-venv-create) for information about virtual environments management in DepHell.
1. [dephell deps install](cmd-deps-install) to install all project dependencies.
1. [dephell jail install](cmd-jail-install) to install Python CLI tools into isolated virtual environment.
# dephell package list

Show installed packages. See [how DepHell looks for Python environment](python-lookup).

```bash
$ dephell package list
[
  {
    "authors": [
      "Hynek Schlawack",
      "Hynek Schlawack"
    ],
    "description": "Classes Without Boilerplate",
    "installed": [
      "19.1.0"
    ],
    "latest": "19.1.0"
    "license": "MIT",
    "links": {
      "home": "https://www.attrs.org/",
      "project": "Documentation, https://www.attrs.org/"
    },
    "name": "attrs",
  },
  ...
]
```

Output of this command is really long. So, in most cases you want to [filter it](filters).

Show only names:

```bash
dephell package list --filter="#.name.sorted()"
[
  "aiofiles",
  "aiohttp",
  "appdirs",
  ...
]
```

Show only name and installed versions:

```bash
$ dephell package list --filter="#.name+installed.each()"
[
  {
    "installed": [
      "1.2"
    ],
    "name": "cerberus"
  },
  ...
]
```

Show name and description for first 10 packages (it can be useful for pagination by output):

```bash
$ dephell package list --filter="#.name+description.each().:10"
[
  {
    "description": "Lightweight, extensible schema and data validation tool for Python dictionaries.",
    "name": "cerberus"
  },
  ...
]
```

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [How to filter commands JSON output](filters).
1. [dephell deps outdated](cmd-deps-outdated) to show outdated packages in the virtual environment or lockfile.
1. [dephell package search](cmd-package-search) to search packages on [PyPI](https://pypi.org/).
1. [dephell package show](cmd-package-show) to get information about single package.
1. [dephell package install](cmd-package-install) to install package.
# dephell package purge

Remove package with package dependencies:

```bash
$ dephell package purge tomlkit
```

This command removes package and package dependencies that aren't required for other packages in the environment. For example, you want to remove `pathlib2`. This package has `scandir` and `six` in the requirements. However, `six` also used in `requests`, that also installed on your system. `scandir` isn't used in another package. So, this command will remove only `pathlib2` and `scandir`. Of course, `scandir` can be used in some of your projects that isn't explicitly installed. So, if you want to avoid it and drop only package without dependencies use [dephell package remove](cmd-package-remove).

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [dephell package remove](cmd-package-remove) to remove package without dependencies.
1. [dephell package install](cmd-package-install) to install package into environment.
1. [dephell deps install](cmd-deps-install) to install all project dependencies.
1. [dephell jail install](cmd-jail-install) to install Python CLI tools into isolated virtual environment.
# dephell package releases

Show available releases of package.

```bash
dephell package releases textdistance
[
  {
    "date": "2019-03-18",
    "python": "*",
    "version": "4.1.2"
  },
  ...
]
```

[Filter](filters) only versions:

```bash
dephell package releases --filter="#.version" textdistance
[
  "4.1.2",
  "4.1.1",
  "4.1.0",
  "4.0.0",
  "3.1.0",
  ...
]
```

Show 10 latest releases from git repository:

```bash
$ dephell package releases --filter=:10 git+https://github.com/orsinium/deal.git#egg=deal
[
  {
    "date": "2018-02-04",
    "python": "*",
    "version": "1.1.0"
  },
  ...
]
```

## Conda

Show releases on [Anaconda Cloud](https://docs.anaconda.com/anaconda-cloud/):

```bash
$ dephell package releases --repo=conda textdistance
[
  {
    "date": "2019-03-13",
    "python": "*",
    "version": "4.1.0"
  },
  ...
]
```

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [How to filter commands JSON output](filters).
1. [dephell package search](cmd-package-search) to search packages on [PyPI](https://pypi.org/).
1. [dephell package show](cmd-package-list) to show information about package.
1. [dephell package install](cmd-package-install) to install package.
# dephell package remove

Remove package without package dependencies:

```bash
$ dephell package remove homoglyphs
```

This command doesn't remove package dependencies because we can't be sure that these dependencies aren't used anywhere in your system. For example, you want to remove `requests` that has `urllib3` in the dependencies list. But also you have somewhere on your system your personal project that depends on `urllib3` too. So, we can't sure that we can remove it. If it is OK to you use [dephell package purge](cmd-package-purge).

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [dephell package purge](cmd-package-purge) to remove package with dependencies.
1. [dephell package install](cmd-package-install) to install package into environment.
1. [dephell deps install](cmd-deps-install) to install all project dependencies.
1. [dephell jail install](cmd-jail-install) to install Python CLI tools into isolated virtual environment.
# dephell package search

Search packages on [PyPI](https://pypi.org/) or [Anaconda Cloud](https://docs.anaconda.com/anaconda-cloud/).

## Simple search by name

```bash
dephell package search dephell
[
  {
    "description": "Dependency resolution for Python",
    "name": "dephell",
    "url": "https://pypi.org/project/dephell/",
    "version": "0.3.1"
  },
  {
    "description": "Work with python versions",
    "name": "dephell-pythons",
    "url": "https://pypi.org/project/dephell-pythons/",
    "version": "0.1.0"
  },
  ...
]
```

## Query filters

Supported query filters:

+ author_email
+ author
+ description
+ download_url
+ home_page
+ keywords
+ license
+ maintainer_email
+ maintainer
+ name
+ platform
+ summary
+ version

Get all projects of author:

```bash
$ dephell package search author:orsinium
[
  {
    "description": "Find project modules and data files (packages and package_data for setup.py).",
    "name": "dephell-discover",
    "url": "https://pypi.org/project/dephell-discover/",
    "version": "0.1.0"
  },
  ...
]
```

Or get first 10 packages with "environment markers" in the summary:

```bash
$ dephell package search --filter=":10" summary:"environment markers"
[
  {
    "description": "A compiler for PEP 345 environment markers.",
    "name": "markerlib",
    "url": "https://pypi.org/project/markerlib/",
    "version": "0.6.0"
  },
  {
    "description": "Work with environment markers (PEP-496)",
    "name": "dephell-markers",
    "url": "https://pypi.org/project/dephell-markers/",
    "version": "0.2.3"
  },
  ...
]
```

You can combine any query filters together:

```bash
$ dephell package search author:orsinium name:dephell
```

## Anaconda Cloud

A few differences from search on PyPI:

1. Specify `--repo=conda` to search on Anaconda Cloud.
1. Search text (text without query filters) is required.
1. Available query filters:
    1. `type` (`conda`, `pypi`, `env`, `ipynb`)
    1. `platform` (`osx-32`, `osx-64`, `win-32`, `win-64`, `linux-32`, `linux-64`, `linux-armv6l`, `linux-armv7l`, `linux-ppc64le`, `noarch`)
1. Results also contain fields `links`, `license`, and `channel`.

Examples:

```bash
$ dephell package search --repo=conda textdistance
[
  {
    "channel": "conda-forge",
    "description": "TextDistance – python library for comparing distance between two or more sequences by many algorithms.",
    "license": "LGPL-3.0",
    "links": {
      "anaconda": "http://anaconda.org/conda-forge/textdistance",
      "documentation": "https://pypi.org/project/textdistance/#description",
      "homepage": "https://github.com/orsinium/textdistance",
      "repository": "https://github.com/orsinium/textdistance"
    },
    "name": "textdistance",
    "version": "4.1.0"
  }
]
```

```bash
dephell package search --repo=conda --filter=":5" keras type:ipynb
[
  {
    "channel": "zenlambda",
    "description": "IPython notebook",
    "license": {},
    "links": {
      "anaconda": "http://anaconda.org/zenlambda/keras"
    },
    "name": "keras",
    "version": "2017.02.26.2159"
  },
  ...
]
```

## See also

1. [How to filter commands JSON output](filters).
1. [dephell package show](cmd-package-search) to show information about single package.
1. [dephell package list](cmd-package-list) to show information about installed packages.
1. [dephell package install](cmd-package-install) to install package.
# dephell package show

Show information about package by name.

```bash
$ dephell package show jsonschema
{
  "authors": [
    "Julian Berman <Julian@GrayVines.com>"
  ],
  "description": "An implementation of JSON Schema validation for Python",
  "installed": [
    "2.6.0",
    "3.0.1"
  ],
  "latest": "3.0.1",
  "license": "MIT",
  "links": {
    "homepage": "https://github.com/Julian/jsonschema",
    "package": "https://pypi.org/project/jsonschema/"
  },
  "locations": [
    "/home/gram/.local/lib/python3.7/site-packages/jsonschema",
    "/usr/local/lib/python3.7/site-packages/jsonschema"
  ],
  "name": "jsonschema",
  "size": "620.11Kb",
  "updated": "2019-03-01"
}
```

If virtual environment for current project and environment exists this command will get package version for this virtual environment. Otherwise, this command will get package versions from all paths from `sys.path` for current Python. This is the reason why `version.installed` is a list.

## Conda (Anaconda Cloud and conda-forge recipes)

By default, this command uses information from [PyPI](http://pypi.org). However, you can explicitly specify `--repo` to search package among conda recipes.

Search recipes in the [conda-froge](https://github.com/conda-forge/) Github repository:

```bash
$ dephell package show --repo=conda_git make
{
  "authors": [],
  "description": "GNU Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files.",
  "latest": "4.2.1",
  "license": "GPLv3",
  "links": {
    "documentation": "https://www.gnu.org/software/make/manual/",
    "homepage": "https://www.gnu.org/software/make/"
  },
  "name": "make",
  "updated": "2019-01-12"
}
```

Search builded packages in [Anaconda Cloud](https://anaconda.org/):

```bash
$ dephell package show --repo=conda_cloud make
{
  "authors": [],
  "description": "GNU Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files.",
  "latest": "4.2.1",
  "license": "GPLv3",
  "links": {
    "anaconda": "https://anaconda.org/conda-forge/make",
    "documentation": "https://www.gnu.org/software/make/manual/",
    "homepage": "https://www.gnu.org/software/make/",
    "source": "https://ftp.gnu.org/gnu/make/make-4.2.1.tar.bz2"
  },
  "name": "make",
  "updated": "1970-01-01"
}
```

```bash
$ dephell package show --repo=conda_cloud textdistance
{
  "authors": [],
  "description": "TextDistance – python library for comparing distance between two or more sequences by many algorithms.",
  "latest": "4.1.0",
  "license": "LGPL-3.0",
  "links": {
    "anaconda": "https://anaconda.org/conda-forge/textdistance",
    "documentation": "https://pypi.org/project/textdistance/#description",
    "homepage": "https://github.com/orsinium/textdistance",
    "repository": "https://github.com/orsinium/textdistance",
    "source": "https://pypi.io/packages/source/t/textdistance/textdistance-4.1.0.tar.gz"
  },
  "name": "textdistance",
  "updated": "2019-03-13"
}
```

## See also

1. [How DepHell choose Python environment](python-lookup).
1. [How to filter commands JSON output](filters).
1. [dephell package search](cmd-package-search) to search packages.
1. [dephell package list](cmd-package-list) to show information about installed packages.
1. [dephell package install](cmd-package-install) to install package.
# dephell project build

Build package for project:

1. Get dependencies from `from` parameter.
1. Make `setup.py` and `README.rst`.
1. Make [egg-info](https://setuptools.readthedocs.io/en/latest/formats.html).
1. Make sdist (archived project source code and egg-info).
1. Make [wheel](https://pythonwheels.com/).

After all you can use [twine](https://github.com/pypa/twine/) to upload it on PyPI.

## Example

```bash
$ dephell project build --from pyproject.toml
$ twine upload dist/*
```

## See also

1. [dephell deps convert](cmd-deps-convert) for details how DepHell converts dependencies from one format to another.
1. [Full list of config parameters](params)
# dephell project bump

Bump project version. Versioning scheme specified as `--versioning` and bumping rule or new version specified as positional argument. For example, bump minor version number by semver rules:

```bash
$ dephell project bump --versioning=semver minor
INFO generated new version (old=0.3.2, new=0.4.0)
INFO file bumped (path=/home/gram/Documents/dephell/dephell/__init__.py)
```

It's recommend to explicitly add `versioning` in config to let your users know which scheme you're using in your project:

```toml
[tool.dephell.main]
versioning = "semver"
```

Command steps:

1. Try to detect version from `from` file.
1. Try to detect version from project source code.
1. Generate new version.
1. Write new version in source code. DepHell looks for `__version__` variable in project source and writes new version in it.
1. Write new version in `from` file.

Also, the command adds git tag if `--tag` option (or `tag = <your_template>` in the config) is specified as template.
Template can be string with `{version}` placeholder (e.g. `v.{version}`) or just prefix string (e.g. `v.`)

```bash
$ dephell project bump --tag=v. minor
INFO generated new version (old=0.8.0, new=0.9.0)
INFO file bumped (path=/home/gram/Documents/dephell/dephell/__init__.py)
INFO commit and tag
INFO tag created, do not forget to push it: git push --tags
```

## Rules

1. `init` -- write initial version for current versioning scheme.
1. `major` or `breaking` -- increment first number of version. In `pep`, `semver`, and `comver` it means breaking changes that can broke third-party code that depends on your project. Example: `1.2.3` → `2.0.0`. Zero major version has special meaning: before `1.0.0` release any increment of `minor` number can break anything.
1. `minor` or `feature` -- increment second number of version. In `pep`, and `semver` it means non-breaking new features. Example: `1.2.3` → `1.2.0`.
1. `patch`, `fix` or `micro` -- increment third number of version. In `pep`, and `semver` it means bugfixes that don't add new features or break anything. For `calver` it usually means hotfixes that must be delivered ASAP. Example: `1.2.3` → `1.2.4`.
1. `pre`, `rc` or `alpha` -- increment pre-release number. Semantic depends on versioning scheme. A pre-release version indicates that the version is unstable and anything can be changed until release.
1. `premajor` -- applies both `pre` and `major`.  Example: `1.2.3` → `2.0.0-rc.1`
1. `preminor` -- applies both `pre` and `minor`.  Example: `1.2.3` → `1.3.0-rc.1`
1. `prepatch` -- applies both `pre` and `patch`.  Example: `1.2.3` → `1.2.4-rc.1`
1. `release` -- removes any pre-release number.  Example: `1.2.3-rc.1` → `1.2.3`
1. `post` -- increment post-release number. This is supported only by `pep`. Post-release number increment means some changes that do not affect the distributed software at all. For example, correcting an error in the release notes, metainfo, including license in the package etc.
1. `dev` -- increment `dev` number. Kind of pre-release that must not be used for any purposes except the project development. So, dev-releases should not be uploaded on public index servers. This version number also supported only by `pep`.
1. `local` -- increment local version number. This number separated from main version by `+`. See more details in the next section.

## Local number

1. Local number specified in `pep` and behave like post-release: `1.2+1` > `1.2`.
1. Be careful, local numbers compared as strings: `1.2+9` > `1.2+10`.
1. PEP recommends to use this number to indicate applying some patches to the release. For example, patch for compatibility with Ubuntu, with Django or with another project.
1. `semver` and `comver` allow to use "build metadata" with the same meaning as local number in `pep`. However, in `semver` and `comver` these metadata doesn't affect versions ordering. For example, `1.2+1 == 1.2`. For all Python projects all tools uses pep, so you shouldn't worry about it. Thence, DepHell allows you to use local number for `semver` and `comver` too.
1. Local number can contains any ASCII letters, digits and dot.
1. We recommend to use local number for nightly releases. It's like pre-release, but when you don't know version of future release and just add local number to the latest release version. See discussion in SemVer repository for more details: [Nightly builds not supported](https://github.com/semver/semver/issues/200)
1. When you specifying rule as `local`, DepHell just increments previous local number: 1 → 2 → 3... When you want to specify exact value for local version you can pass instead of rule `+` sign and local version number. For example, if your current version `1.2.3+1` and you run `dephell project bump +lol` your new version will be `1.2.3+lol`.

## Versioning schemes

1. [pep](https://www.python.org/dev/peps/pep-0440/#version-scheme) -- versioning scheme specified in PEP-420. Based on SemVer, but has much more features. All tools in Python (and DepHell too) parse projects versions by this PEP, so you can use it for your project and don't care about machines. However, this pep allows to make over-complicated versions that really difficult to understand for humans.
1. [semver](https://semver.org/) -- most recommend versioning scheme. Allows your users (and machines) by version easily understand when you have broken something in your project, have added some new features or have fixed some bugs. If you don't know what to use, use it.
1. [comver](https://github.com/staltz/comver) -- this is semver without `patch` number. All changes that don't broke anything increments `minor` version number. You can use it if in your project it's difficult to separate bug fixes and features.
1. [calver](https://calver.org/) -- it's when you use current date (year and month) instead of version. For example, `2018.12`. DepHell uses 4-numbers year as major number to explicitly indicate that your project uses CalVer. Also you can pass `micro` rule to add day in the version number. If previous release was today then `micro` rule will just increment this number. You can use this versioning if you don't want to care about versioning at all. However, this is strongly discouraged for any projects that can be used as dependency for third-party code.
1. [romver](http://dafoster.net/articles/2015/03/14/semantic-versioning-vs-romantic-versioning/) -- romantic versioning (not [Sentimental Versioning](http://sentimentalversioning.org/), please) is when humans and marketing more important for you than machines. Bumping `major`, `minor` or `patch` number shows importance of changes and says nothing about type of this changes. Every update can break everything. As calver, never use this versioning in tools that can be used in any third-party code. But it's OK for products for users like Firefox. DepHell allows only `major`, `minor` and `patch` rules for RomVer because this versioning for humans, and humans don't understand complicated combinations of `pre`, `post` and `local`.
1. [serial](https://packaging.python.org/guides/distributing-packages-using-setuptools/#serial-versioning) -- this is just single number that you increment for every release (1, 2, 3...). Simplest versioning scheme, but doesn't provide any information about release changes type. Avoid this scheme if possible.
1. [roman](https://en.wikipedia.org/wiki/Roman_numerals) -- roman numbers versioning. Never use it. It won't work after third release. However, you can try it for your internal project. Just for fun. Don't say anyone that I've recommended it to you.
1. [zerover](https://0ver.org/) -- kind of `semver`, but your `major` number always 0. Sounds like joke, but this is the best versioning for experimental projects that can broke anything in any release. So, if it's about your project then explicitly specify `zerover` versioning in your DepHell config. It says to your users that they can't upgrade without running quite strong integration tests.

## Projects that use these versioning schemes

1. semver:
    + [six](https://pypi.org/project/six/#history)
    + [botocore](https://pypi.org/project/botocore/#history)
    + [python-dateutil](https://pypi.org/project/python-dateutil/#history)
    + [requests](https://pypi.org/project/requests/#history)
    + [chardet](https://pypi.org/project/chardet/#history)
    + [rsa](https://pypi.org/project/rsa/#history)
1. comver:
    + [PyYAML](https://pypi.org/project/PyYAML/#history)
    + [idna](https://pypi.org/project/idna/#history)
    + [terminator](https://launchpad.net/terminator)
1. calver:
    + [pytz](https://pypi.org/project/pytz/#history)
    + [certify](https://pypi.org/project/certifi/#history)
    + [PyCharm](https://www.jetbrains.com/pycharm/download/previous.html)
    + [Ubuntu](http://releases.ubuntu.com/)
1. romver:
    + [pip](https://pypi.org/project/pip/#history) (`1.5.6` → `6.0`)
    + [pipenv](https://pypi.org/project/pipenv/#history) (`0.2.8` → `3.0.0`)
1. roman:
    + [Mac OS X](https://en.wikipedia.org/wiki/MacOS)
    + [WordPerfect Office](https://en.wikipedia.org/wiki/WordPerfect#WordPerfect_Office)
    + [3.V album by Zebra band](https://en.wikipedia.org/wiki/3.V)
    + [состояние птиц](https://bsos.bandcamp.com/)
1. zerover:
    + [html5lib](https://github.com/html5lib/html5lib-python/issues/282) 0.999999999
    + [docutils](https://pypi.org/project/docutils/#history) 0.14 (16 years from first release)
    + [pyasn1](https://pypi.org/project/pyasn1/#history) 0.4.5 (13 years from first release)
    + [pandas](https://pypi.org/project/pandas/#history) 0.24.2 (10 years from first release)
    + [colorama](https://pypi.org/project/colorama/#history) 0.4.1 (9 years from first release)
    + See more 0ver projects on [0ver.org](https://0ver.org/#notable-zerover-projects).

## Command examples

SemVer:

```bash
$ dephell project bump init
INFO generated new version (old=0.0.0, new=0.1.0)

$ dephell project bump fix
INFO generated new version (old=0.1.0, new=0.1.1)

$ dephell project bump minor
INFO generated new version (old=0.1.1, new=0.2.0)

$ dephell project bump major
INFO generated new version (old=0.2.0, new=1.0.0)

$ dephell project bump pre
INFO generated new version (old=1.0.0, new=1.0.0-rc.1)

$ dephell project bump post
ERROR ValueError: rule post is unsupported by scheme semver

$ dephell project bump local
INFO generated new version (old=1.0.0-rc.1, new=1.0.0-rc.1+1)

$ dephell project bump +ubuntu1
INFO generated new version (old=1.0.0-rc.1+1, new=1.0.0-rc.1+ubuntu1)
```

CalVer:

```bash
$ dephell project bump --versioning=calver init
INFO generated new version (old=1.0.0-rc.1+ubuntu1, new=2019.4)

# today
$ dephell project bump --versioning=calver micro
INFO generated new version (old=2019.4, new=2019.4.9)

# if execute `micro` again: today + 1
$ dephell project bump --versioning=calver micro
INFO generated new version (old=2019.4.9, new=2019.4.10)
```

PEP:

```bash
$ dephell project bump --versioning=pep init
INFO generated new version (old=2019.4.10, new=0.1.0)

$ dephell project bump --versioning=pep pre
INFO generated new version (old=0.1.0, new=0.1.0rc1)

$ dephell project bump --versioning=pep post
INFO generated new version (old=0.1.0rc1, new=0.1.0.post1)

# `dev` can be attached to `pre` or `post` too
$ dephell project bump --versioning=pep dev
INFO generated new version (old=0.1.0.post1, new=0.1.0.post1.dev1)
```

ZeroVer:

```bash
$ dephell project bump --versioning=zerover major
ERROR ValueError: rule major is unsupported by scheme zerover

$ dephell project bump --versioning=zerover minor
INFO generated new version (old=0.3.2, new=0.4.0)
```

Roman:

```bash
$ dephell project bump --versioning=roman init
INFO generated new version (old=0.3.2, new=I)

$ dephell project bump --versioning=roman major
INFO generated new version (old=I, new=II)
```

Custom version:

```bash
$ dephell project bump 0.3.2
INFO generated new version (old=0.1.0.post1.dev1, new=0.3.2)
```

## See also

1. [dephell inspect versioning](cmd-inspect-versioning) to get information about the project versioning scheme and available rules.
# dephell project test

Test project package.

1. Get project dependencies from `from`.
1. Attach dependencies from `and`.
1. Build wheel package.
1. Detect pythons to run. By default, all installed pythons that supported by project. You can limit it by one python version with `--python`.
1. For every python:
    1. Make temporary virtual environment.
    1. Copy inside test files specified in `tests`.
    1. Install package from wheel.
    1. Install test command.
    1. Run command from `command` in config.

Use [dephell venv run](cmd-venv-run) instead of this command if you want to run tests for current code without many pythons, temporary environments, and creating package.

## Example

DepHell contains next environment in the config:

```bash
[tool.dephell.pytest]
# read dependencies from poetry format
from = {format = "poetry", path = "pyproject.toml"}
# copy files that requred for tests
tests = ["tests", "README.md"]
# run command `pytest`
command = "pytest -x tests/"
```

And next lines in the poetry config:

```bash
[tool.poetry]
name = "dephell"
version = "0.3.2"
# ...

[tool.poetry.dependencies]
python = ">=3.5"
# ...
```

You can run tests on this environment by the next command:

```bash
$ dephell project test --env=pytest
INFO creating wheel...
INFO get interpreters
INFO create venv (python=3.7.0)
INFO copy files (path=tests)
INFO copy files (path=README.md)
INFO install project (path=/home/gram/Documents/dephell/dist/dephell-0.3.2-py3-none-any.whl)
INFO executable not found, installing (executable=pytest)
INFO run tests (command=['pytest', '-x', 'tests/'])
...
```

If you have installed python 2.7, 3.5, 3.6, and 3.7 then this command will test your code on 3.5, 3.6, and 3.7. Also, you can explicitly specify required python:

```bash
dephell project test --traceback --env=pytest --python=3.7
```

## See also

1. [dephell venv run](cmd-venv-run) to run tests for current codebase without complicated isolation.
1. [dephell deps convert](cmd-deps-convert) for details how DepHell converts dependencies from one format to another.
1. [Python lookup](python-lookup) for details how you can specify Python version for commands.
1. [Full list of config parameters](params)
# dephell project validate

Validate project metadata that required to build good and compatible distribution package.

## Errors

+ "field is unspecified". Next fields should be specified and not empty:
    + name
    + version
    + license
    + keywords
    + classifiers
    + description
+ "bad name". Project name should be normalized.
+ "version should be str"
+ "cannot find Python files for package"
+ "short description is too long". Short description should be shorter than 140 chars.
+ "short description is too short". Short description should be longer than 10 chars.
+ "no authors specified"
+ "no links specified"
+ "no license specified in classifier"
+ "no development status specified in classifier"
+ "no python version specified in classifier"

## Warnings

+ "no dependencies found". Maybe, your project has no dependencies. Or maybe, you forgot to specify them.

## See also

1. [dephell project build](cmd-project-build) to build package for the project.
# dephell self auth

Manage credentials: add, update, remove. These credentials are used for [Basic HTTP authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) for [custom PyPI repositories](https://www.python.org/dev/peps/pep-0503/).

Add new credentials:

```bash
$ dephell self auth pypi.example.com my-useranme "my-p@ssword"
INFO credentials added (hostname=pypi.example.com, username=my-useranme)
```

Remove credentials for user:

```bash
$ dephell self auth pypi.example.com my-useranme
INFO credentials removed (hostname=pypi.example.com, username=my-useranme)
```

Remove credentials for all users for given hostname:

```bash
$ dephell self auth pypi.example.com
INFO credentials removed (hostname=pypi.example.com, count=1)
```

Credentials are stored in global config. If you add credentials for `example.com`, they will be used in all projects to connect to `example.com`.

## See also

1. [Private PyPI repository](use-warehouse) usage details and examples.
1. [dephell inspect auth](cmd-inspect-auth) to list added credentials.
1. [dephell deps install](cmd-deps-install) to install dependencies from private repository.
# dephell self autocomplete

Enable dephell autocompletion for current shell. Supported shells:

1. bash
1. zsh

This command generates shell script to achieve better suggestions performance. So, please, execute `dephell self autocomplete` after DepHell update again.
# dephell self uncache

Remove dephell cache.

```bash
$ dephell self uncache
INFO cache removed (size=64.98Mb)
```

## See also

1. [dephell inspect self](cmd-inspect-self) to get information about dephell installation like current cache size.
# dephell self upgrade

Upgrade dephell to the latest version. If dephell installed in venv or jail, it also updates all dependencies.

```bash
$ dephell self upgrade
```

## See also

1. [dephell inspect self](cmd-inspect-self) to get information about dephell installation like current cache size.
# dephell vendor download

Download and extract project dependencies in a given directory.

```bash
dephell vendor download --from=requirements.txt --vendor-path=my_project/_vendor/
```

Some packages can be nightly and not ready for vendorization. So, you can exclude them:

```toml
[tool.dephell.vendorized]
from = {format = "pip", path = "requirements.txt"}

[tool.dephell.vendorized.vendor]
path = "my_project/_vendor"
exclude = ["jinja2", "setuptools"]
```

And then:

```bash
dephell vendor download --env=vendorized
```

How to find out packages that can't be vendorized? Do experiment:

1. `git checkout .`
1. Vendorize.
1. [Patch imports](cmd-vendor-import)
1. Try to run your project.
1. Have `ImportError` or `AttributeError`? Add this package into `exclude` list and try again.

## See also

1. [vendor commands index](index-vendor) to read more about vendorization.
1. [dephell vendor import](cmd-vendor-import) to patch all imports in your project.
# dephell vendor import

Patch all imports in your project and vendorized dependencies itself to use these vendorized dependencies. For example, if you're using `requests` third-party library and have `my_project/_vendor/requests` directory, run the next command:

```bash
dephell vendor import --vendor-path=my_project/_vendor/
```

After that all imports of `requests` inside `my_project` will be patched to import `my_project._vendor.requests` instead.

Python import system makes a big difference between packages and subpackages, and what worked in library itself can be broken when you place this library inside your project. So, be ready to exclude some libraries from vendorization. Read about it in [dephell vendor download](cmd-vendor-download) documentation.

## See also

1. [vendor commands index](index-vendor) to read more about vendorization.
1. [dephell vendor download](cmd-vendor-download) to download your project dependencies in some directory.
# dephell venv create

Create virtual environment for current project and environment. Always create virtual environment before executing [dephell deps install](cmd-deps-install) or [dephell package install](cmd-package-install) if you want them to install packages into special virtual environment. Otherwise, these commands will use your current virtual environment (or global interpreter).

Path to virtual environment contains these substitutions:

+ `{project}` will be replaced by the project name (name of path from `project` option, this is name of the current directory by default).
+ `{digest}` will be replaced by the short 4-letters digest of the project path to avoid conflicts for the projects with the same name in different locations.
+ `{env}` will be replaced by current environment (`main` by default).

So, virtual environment unique for every project and environment by default.

For example, create virtual environment for `docs` environment of current project:

```bash
$ dephell venv create --env=docs
```

Get venv path template with [dephell inspect config](cmd-inspect-config) command:

```bash
$ dephell inspect config --filter=venv
/home/gram/.local/share/dephell/venvs/{project}-{digest}/{env}
```

Get path to the current venv (if created) with [dephell inspect venv](cmd-inspect-venv) command:

```bash
$ dephell inspect venv venv
/home/gram/.local/share/dephell/venvs/dephell-nLn6/main
```

## See also

1. [How DepHell choose Python interpreter](python-lookup).
1. [dephell deps install](cmd-deps-install) to install project dependencies into created virtual environment.
1. [dephell package install](cmd-package-install) to install package into created virtual environment.
1. [dephell jail install](cmd-jail-install) to install Python CLI tools into isolated virtual environment.
1. [dephell venv destroy](cmd-venv-destroy) to remove virtual environment.
1. [dephell venv run](cmd-venv-run) to run tool from virtual environment.
1. [dephell venv shell](cmd-venv-shell) to activate virtual environment for current shell.
# dephell venv destroy

Removes virtual environment for current environment and project.

For example, destroy virtual environment for `docs` environment of current project:

```bash
$ dephell venv destroy --env=docs
```
# dephell venv run

Runs command in the virtual environment of current project and environment.

1. If the virtual environment doesn't exist DepHell will [create it](cmd-venv-create).
1. If script doesn't exist in the virtual environment DepHell tries to install it from [PyPI](https://pypi.org/).

For example, get help for `sphinx-build` from `docs` environment of current project:

```bash
$ dephell venv run --env=docs sphinx-build --help
```

Command can be specified in the config:

```toml
[tool.dephell.docs]
command = "sphinx-build --help"
```

In this case command can be omitted:

```bash
$ dephell venv run --env=docs
```

## Environment variables

This command passes next [environment variables](https://en.wikipedia.org/wiki/Environment_variable) into running command:

1. Your current environment variables.
1. Values from `vars` in config.
1. Values from [.env](https://github.com/theskumar/python-dotenv) file.

example of `.env` file:

```bash
export POSTGRES_USERNAME="dephell"
export POSTGRES_PASSWORD="PasswordExample"
export POSTGRES_URL="psql://$POSTGRES_USERNAME:$POSTGRES_PASSWORD@localhost"
```

DepHell supports any format of `.env` file: `export` word optional, quotes optional, `=` can be surrounded by spaces. However, we recommend to use above format, because it allows you to use [source command](https://bash.cyberciti.biz/guide/Source_command) to load these variables in your current shell.

Features for `.env` file:

1. Parameters expansion. In the example above `POSTGRES_URL` value will be expanded into `psql://dephell:PasswordExample@localhost`. If variable does not exist DepHell won't touch it. You can explicitly escape $ sign (`\$`) to avoid expansion.
1. Escape sequences. You can insert escape sequences like `\n` in values, and DepHell will process it.

Config example:

```toml
[tool.dephell.main]
vars = {PYTHONPATH = "."}
command = "python"

[tool.dephell.flake8]
vars = {TOXENV = "flake8"}
command = "tox"
```

Use `.env` for secret things like database credentials and `vars` in config for some environment-specific settings for running commands like environment for flake.

If you want to pass temporary variable that not intended to be stored in any file then just set this variable in your current shell:

```bash
$ CHECK=me dephell venv run python -c "print(__import__('os').environ['CHECK'])"
INFO running...
me
INFO command successfully completed
```

## See also

1. [dephell venv shell](cmd-venv-shell) to activate virtual environment for your current shell.
# dephell venv shell

Activates virtual environment of current project and environment for current shell. If virtual environment doesn't exist DepHell will create it.

Supported shells:

+ [cmd.exe](https://en.wikipedia.org/wiki/Cmd.exe)
+ [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
+ [Bash](https://bit.ly/1ikp2Hl)
+ [Fish](https://fishshell.com/)
+ [Zsh](https://en.wikipedia.org/wiki/zsh)
+ [Xonsh](http://xon.sh/index.html)
+ [Tcsh](https://en.wikipedia.org/wiki/Tcsh)
+ [Csh](https://en.wikipedia.org/wiki/C_shell)

```bash
$ dephell venv shell --env=docs
```

This command build environment variables in the same way as [dephell venv run](cmd-venv-run).

## See also

1. [dephell venv run](cmd-venv-run) to run single command in a virtual environment.
# Configuration and parameters

Dephell makes config from 4 layers:

1. Default parameters.
1. Section from config file.
1. Environment variables.
1. CLI arguments.

## Config file

Config should be [TOML](https://github.com/toml-lang/toml) file with `tool.dephell.ENV_NAME` sections (see [PEP-518](https://www.python.org/dev/peps/pep-0518/#tool-table)).

1. By default, dephell tries to read `pyproject.toml` or `dephell.toml`. You can change it by `--config` argument.
1. Default environment: `main`. Environment is the name of the section inside of `tool.dephell` section in config file. You can change environment by `--env` argument.

Config example:

```toml
[tool.dephell.main]
# read from poetry format
from = {format = "poetry", path = "pyproject.toml"}
# drop dev-dependencies
envs = ["main"]
# and convert into setup.py
to = {format = "setuppy", path = "setup.py"}

[tool.dephell.pytest]
# read dependencies from setup.py
from = {format = "setuppy", path = "setup.py"}
# install main dependencies and `tests` extra dependencies
envs = ["main", "tests"]
# run command `pytest`
command = "pytest"
```

## CLI arguments

You can (re)define any config options with CLI arguments. For example, there is how you can define the same parameters as in the `pytest` section above:

```bash
$ dephell deps install \
    --from-format setuppy \
    --from-path setup.py \
    --envs main tests --

$ dephell deps run --command="pytest"

# Also for `venv run` you can specify command as positional argument:
$ dephell venv run pytest
```

It's OK for one-time actions, but for everyday usage we recommend to define config section for every kind of tasks you perform. For example, for dephell we have defined envs `main` to convert from poetry to setup.py, `flake8` for linting, `pytest` for tests, and `docs` for generating documentation. So, you can install and run test environment for dephell much simpler:

```bash
$ dephell venv create --env=pytest
$ dephell deps install --env=pytest
$ dephell venv run --env=pytest
```

Also, by default, DepHell uses `--env` to generate path to the virtual environment, so different `--env` values have different virtual environments.

## Environment variables

Sometimes, specifying config parameters in environment variables can be more suitable for you. Most common case is to set up `env` or path to config file. For example:

```bash
export DEPHELL_ENV=flake8
export DEPHELL_CONFIG="./project/dephell.toml"

# commands below will be executed with specified above env and path to config
dephell venv create
dephell deps install
dephell venv run

# do not forget to remove variables after all
unset DEPHELL_ENV
unset DEPHELL_CONFIG
```

DepHell do type casting in the same way as [dynaconf](https://dynaconf.readthedocs.io/en/latest/guides/environment_variables.html#precedence-and-type-casting). Just use TOML syntax for values:

```bash
# Numbers
DEPHELL_CACHE_TTL=42
DEPHELL_SDIST_RATIO=0.5

# Text
DEPHELL_FROM_FORMAT=pip
DEPHELL_FROM_FORMAT="pip"

# Booleans
DEPHELL_SILENT=true
DEPHELL_SILENT=false

# Use extra quotes to force a string from other type
DEPHELL_PYTHON="'3.6'"
DEPHELL_PROJECT="'true'"

# Arrays
DEPHELL_ENVS="['main', 'dev']"

# Dictionaries
DEPHELL_FROM='{format="pip", path="req.txt"}'
```

## See also

1. [`inspect config` command](cmd-inspect-config) to discover how dephell makes config for your project.
1. [dephell's own config](https://github.com/dephell/dephell/blob/master/pyproject.toml) to see real and full example.
# Filter JSON output

JSON output of any command can be filtered with `--filter` argument.

## Commands with JSON output

+ [dephell deps licenses](cmd-deps-licenses)
+ [dephell inspect config](cmd-inspect-config)
+ [dephell inspect venv](cmd-inspect-venv)
+ [dephell jail list](cmd-jail-list)
+ [dephell package list](cmd-package-list)
+ [dephell package search](cmd-package-search)
+ [dephell package show](cmd-package-show)

## Filters

Filters separated by `.` or `-` and can be one of the following type:

+ Field name to get some field from dict output.
+ Sum of fields. Will return dictionary with given fields. For example, `name+license` will return `{"license": "BSD-2-Clause", "name": "click"}`.
+ Index to get some element from list output.
+ Slice to get set of elements from list output. For example:
    + `:10` to get first 10 elements,
    + `10:` to drop out first 10 elements,
    + `2:5` to get elements with indices 2, 3 and 4.
+ Function to process output.

Functions:

+ `each()` or `#` -- convert list of dicts to dict of lists and vice versa. For example, `[{a: 1, b: 2}, {a: 3, b: 4}]` will be converted into `{a: [1, 3], b: [2, 4]}`.
+ `first()` or `0` -- get first element from list.
+ `flatten()` or `flat()` -- squash list of lists into one-level (flat) list.
+ `last()` or `latest()` -- get last element from list.
+ `len()`, `length()`, `count()` or `size()` -- get count of elements in a list.
+ `max()` -- get maximum value from a list.
+ `min()` -- get minimum value from a list.
+ `reverse()` or `reversed()` -- reverse values in a list.
+ `sort()` or `sorted()` -- sort values in a list.
+ `sum()` -- sum of values in a list.
+ `type()` -- get value type.
+ `zip()` -- transpose output. `[[a, b], [c, d], [e, f]]` will be converted into `[[a, c, e], [b, d, f]]`.

First filter gets command output. Next filters get output from previous filter.

## Example

Let's filter output of [dephell package show](cmd-package-show):

```bash
$ dephell package show textdistance
{
  "authors": [
    "orsinium <master_fess@mail.ru>"
  ],
  "description": "Compute distance between the two texts.",
  "installed": [],
  "latest": "4.1.2",
  "license": "MIT",
  "links": {
    "download": "https://github.com/orsinium/textdistance/tarball/master",
    "homepage": "https://github.com/orsinium/textdistance",
    "package": "https://pypi.org/project/textdistance/"
  },
  "name": "textdistance",
  "updated": "2019-03-18"
}
```

Get some fields:

```bash
# one field value:
$ dephell package show --filter=latest textdistance
4.1.2

# a few fields:
$ dephell package show --filter="latest+installed" textdistance
{
  "installed": [],
  "latest": "4.1.2"
}
```

Filter list items:

```bash
$ dephell package show --filter=authors click
[
  "Armin Ronacher <armin.ronacher@active-4.com>",
  "Pallets Team <contact@palletsprojects.com>"
]

# first element
$ dephell package show --filter="authors.first()" click
Armin Ronacher <armin.ronacher@active-4.com>

# last element
$ dephell package show --filter="authors.last()" click
Pallets Team <contact@palletsprojects.com>

# get element by index
$ dephell package show --filter="authors.0" click
Armin Ronacher <armin.ronacher@active-4.com>

# reverse list
$ dephell package show --filter="authors.reverse()" click
[
  "Pallets Team <contact@palletsprojects.com>",
  "Armin Ronacher <armin.ronacher@active-4.com>"
]

# get records count
$ dephell package show --filter="authors.len()" click
2
```

Work with items in a list:

```bash
dephell package search author:orsinium
[
  {
    "description": "Work with python versions",
    "name": "dephell-pythons",
    "url": "https://pypi.org/project/dephell-pythons/",
    "version": "0.1.0"
  },
  ...
]

# get field from each record
$ dephell package search --filter="#.name" author:orsinium
[
  "dephell-discover",
  "pros",
  "homoglyphs",
  ...
]

# sort
$ dephell package search --filter="#.name.sort()" author:orsinium
[
  "advice",
  "aop",
  "deal",
  ...
]

# get a few fields
$ dephell package search --filter="#.name+description.each()" author:orsinium
[
  {
    "description": "Find project modules and data files (packages and package_data for setup.py).",
    "name": "dephell-discover"
  },
  {
    "description": "UNIX pipeline on python and steroids",
    "name": "pros"
  },
  ...
]

# get only first 10 elements for previous filter:
$ dephell package search --filter="#.name+description.each().:10" author:orsinium
```

## Alternatives

In some rare cases you could want to specify some complex filter that not covered by DepHell. So, you can process DepHell output into some other command that can process JSON. Some of them:

+ [jq](https://stedolan.github.io/jq/)
+ [jj](https://github.com/tidwall/jj)
+ [jd](https://github.com/tidwall/jd)

Also, it's recommend for better processing to disable INFO-messages and progress bars. For example:

```bash
$ dephell deps licenses --level=WARNING --silent | jq --compact-output '."Apache-2.0"'
["aiofiles","aiohttp",...]
```
# Packaging issues

My favorite issues collection.

## Pip

1. Pip doesn't support Pipfile ([pipfile#80](https://github.com/pypa/pipfile/issues/80)).
1. Pip doesn't have dependency resolution ([pip#988](https://github.com/pypa/pip/issues/988))

## Pipenv

1. Pipenv doesn't support more than 2 environments for project ([pipfile#99](https://github.com/pypa/pipfile/issues/99)).
1. Pipenv doesn't support "allow pre-releases" option for single dependency ([pipenv#1760](https://github.com/pypa/pipenv/issues/1760)).
1. Pipenv doesn't support python version range ([pipfile#87](https://github.com/pypa/pipfile/issues/87)).
1. Pipenv doesn't support local packages installation like `--find-links` in `pip` or `dependency_links` in `setup.py` do ([pipenv#2231](https://github.com/pypa/pipenv/issues/2231))

## Poetry

1. Poetry supports only `platform` and `python` specification. This is not documented ([poetry#738](https://github.com/sdispater/poetry/issues/738)). This doesn't allow you to specify other markers like python implementation ([poetry#21](https://github.com/sdispater/poetry/issues/21)).
1. Poetry doesn't allow you to specify editable dependencies in the config ([poetry#34](https://github.com/sdispater/poetry/issues/34)).

## PyPI

1. PyPI API doesn't provide dependecies list for some packages ([packaging-problems#54](https://github.com/pypa/packaging-problems/issues/54) and [warehouse#789](https://github.com/pypa/warehouse/issues/789)).
# **deps**: project dependencies

Commands to manage project dependencies: [convert between formats](cmd-deps-convert), [install](cmd-deps-install), lock, [add new](cmd-deps-add), resolve conflicts, do [security audit](cmd-deps-audit), [review licenses](cmd-deps-licenses), [find outdated packages](cmd-deps-outdated) in lockfile or environment, [build dependencies tree](cmd-deps-tree).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-deps-add
    cmd-deps-audit
    cmd-deps-check
    cmd-deps-convert
    cmd-deps-install
    cmd-deps-licenses
    cmd-deps-outdated
    cmd-deps-sync
    cmd-deps-tree
```
# **docker**: venv on steroids

Commands to simply manage [Docker](https://en.wikipedia.org/wiki/Docker_(software)) containers for the current project: [create](cmd-docker-create) and [destroy](cmd-docker-destroy), run [shell](cmd-docker-shell) and [commands](cmd-docker-run) inside, [make it cool](cmd-docker-prepare). Motivation isn't wrap around whole Docker, but make it easier for newbies to work with simple containers and integrate it with DepHell. It's achieved by providing all commands from [dephell venv](index-venv) group and a little bit more.

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-docker-create
    cmd-docker-destroy
    cmd-docker-prepare
    cmd-docker-run
    cmd-docker-shell
    cmd-docker-stop
    cmd-docker-tags
```
# **generate**: files generation

Commands to generate useful files based on project metadata: [AUTHORS](cmd-generate-authors), [pyproject.toml](cmd-generate-config), [.editorconfig](cmd-generate-editorconfig), [LICENSE](cmd-generate-license), [.travis.yml](cmd-generate-travis), [CONTRIBUTING.md](cmd-generate-contributing).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-generate-authors
    cmd-generate-config
    cmd-generate-contributing
    cmd-generate-editorconfig
    cmd-generate-license
    cmd-generate-travis
```
# **inspect**: info about environment

Commands to get information about environment: [dephell config](cmd-inspect-config), [dephell ecosystem versions](cmd-inspect-self), [project metainfo](cmd-inspect-project), [versioning scheme](cmd-inspect-versioning), [virtual environment](cmd-inspect-venv), [stored credentials](cmd-inspect-auth).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-inspect-auth
    cmd-inspect-config
    cmd-inspect-project
    cmd-inspect-self
    cmd-inspect-venv
    cmd-inspect-versioning
```
# **jail**: CLI tools management

Commands to manage CLI tools (like [httpie](https://httpie.org/)) to keep them into isolated virtual environment: [install](cmd-jail-install), [show installed](cmd-jail-list), [remove](cmd-jail-remove), [try some lib or tool without installation](cmd-jail-try).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-jail-install
    cmd-jail-list
    cmd-jail-remove
    cmd-jail-show
    cmd-jail-try
```
# **package**: single package actions

Commands to work with single packages.

Get information: [download statistics](cmd-package-downloads), [installed packages](cmd-package-list), [available releases](cmd-package-releases), [package metainfo](cmd-package-show), [search packages](cmd-package-search).

Manage: [install](cmd-package-install), [remove](cmd-package-remove), [remove with dependencies](cmd-package-purge), [report bug](cmd-package-bug).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-package-bug
    cmd-package-downloads
    cmd-package-install
    cmd-package-list
    cmd-package-purge
    cmd-package-releases
    cmd-package-remove
    cmd-package-search
    cmd-package-show
```
# **project**: make releases

Commands to manage project: [run tests](cmd-project-test) into separated environment, [bump version](cmd-project-bump), [build packages](cmd-project-build), [validate metadata](cmd-project-validate).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-project-build
    cmd-project-bump
    cmd-project-test
    cmd-project-validate
```
# **self**: manage dephell

Commands to manage dephell installation: [upgrade to the latest version](cmd-self-upgrade), [clear cache](cmd-self-uncache), [enable autocomplete](cmd-self-autocomplete), [add credentials](cmd-self-auth).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-self-auth
    cmd-self-autocomplete
    cmd-self-uncache
    cmd-self-upgrade
```
# Recipes and examples

There are some real-world examples, recipes and hacks how to use DepHell for different tasks.

```eval_rst
.. toctree::
    :maxdepth: 1

    use-warehouse
    use-git-hook
    use-tree-git
    use-poetry-lock
    use-licenses
    use-projects
```
# **vendor**: vendorize dependencies

[Vendorization](http://bitprophet.org/blog/2012/06/07/on-vendorizing/) is a placing external dependencies inside a folder in the project itself. It's a bad practice, but sometimes really useful and helpful. It allows you to pack dependencies inside your project to avoid conflicts with other packages, patch libraries, ship packages that aren't released on PyPI, make consistent environments etc. Use it only for internal projects and CLI tools. Never use it for libraries that used in other projects.

Some tools with vendorized dependencies: setuptools, pip, pipenv, pkg_resources.

DepHell can help you to [download and unpack](cmd-vendor-download) dependencies and [patch all imports](cmd-vendor-import).

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-vendor-download
    cmd-vendor-import
```
# **venv**: virtual environments

Commands to manage virtual environments for the project: [create](cmd-venv-create), and [destroy](cmd-venv-destroy), [activate](cmd-venv-shell), [run commands inside](cmd-venv-run). Most important thing here is you can have as much separated environments for one project as you want. DepHell make it really cheap.

```eval_rst
.. toctree::
    :maxdepth: 1

    cmd-venv-create
    cmd-venv-destroy
    cmd-venv-run
    cmd-venv-shell
```
# DepHell

**DepHell** -- project management for Python.

+ Manage dependencies: [convert between formats](cmd-deps-convert), [install](cmd-deps-install), lock, [add new](cmd-deps-add), resolve conflicts.
+ Manage virtual environments: [create](cmd-venv-create), [remove](cmd-venv-destroy), [inspect](cmd-inspect-venv), [run shell](cmd-venv-shell), [run commands inside](cmd-venv-run).
+ [Install CLI tools](cmd-jail-install) into isolated environments.
+ Manage packages: [install](cmd-package-install), [list](cmd-package-list), [search](cmd-package-search) on PyPI.
+ [Build](cmd-project-build) packages (to upload on PyPI), [test](cmd-project-test), [bump project version](cmd-project-bump).
+ [Discover licenses](cmd-deps-licenses) of all project dependencies, show [outdated](cmd-deps-outdated) packages, [find security issues](cmd-deps-audit).
+ Generate [.editorconfig](cmd-generate-editorconfig), [LICENSE](cmd-generate-license), [AUTHORS](cmd-generate-authors), [.travis.yml](cmd-generate-travis).

## Quick start

1. [Install](installation) DepHell.
1. [Convert](cmd-deps-convert) dependencies from one format to another.
1. [Make config](config) for DepHell to simplify commands.

And that's it! Now you can use any tools with any Python project. Every other commands build around ability to read project dependencies and metadata and resolve conflicts. When you ready to boost your productivity, read how to manage your environment with DepHell:

1. [Create virtual environment](cmd-venv-create).
1. [Install](cmd-deps-install) or [synchronize](cmd-deps-sync) dependencies.
1. [Run](cmd-venv-run) commands inside or [activate virtual environment](cmd-venv-shell).

```eval_rst
.. toctree::
    :maxdepth: 1
    :caption: Main Info

    installation
    config
    params
    filters
    python-lookup

.. toctree::
    :maxdepth: 1
    :caption: Commands

    index-deps
    index-docker
    index-generate
    index-inspect
    index-jail
    index-package
    index-project
    index-self
    index-vendor
    index-venv

.. toctree::
    :maxdepth: 1
    :caption: Dive deeper

    index-use
    badge
    changelog
    hell
```
# Installation

Stable version

```bash
curl -L dephell.org/install | python3
```

It will install DepHell into DepHell's jail ([WE NEED TO GO DEEPER](https://knowyourmeme.com/memes/we-need-to-go-deeper)).

If installation script doesn't work:

```bash
python3 -m pip install --user dephell[full]
```

This command installs DepHell globally, without virtual environment. Extra `full` is optional and installs some dependencies that isn't required, but makes DepHell a little bit better. So, if you can't install by the recommend way and have some conflicts with your global modules, install without it:

```bash
python3 -m pip install --user dephell
```

## Get development version

Install dev version inside of site-packages:

```bash
curl -L dephell.org/install > install.py
python3 install.py --branch=master
```

Or get whole project and teach Python to use it:

```bash
$ git clone https://github.com/dephell/dephell.git
$ cd dephell
$ sudo python3 -m pip install -e .
```
# Parameters list

Parameters represented as CLI arguments. To make config file parameter name from CLI name just strip `--` from the begining and split by `-`.

For example, `--cache-path=.cache --` and `--project=./dephell` can be written in the next way:

```toml
[tool.dephell.main]
cache = {path = ".cache"}
project = "./dephell"
```

To make sure which of these options accepted by some command use `dephell COMMAND --help`. For example, `dephell deps convert --help`.

## Select config file and environment

+ `-c`, `--config` -- path to config file.
+ `-e`, `--env` -- environment in config.

Of course, you can use this options only in CLI. You can't specify path to config in the config :)

## Paths to dependencies

+ `--from` -- path or format for reading requirements. If it is format then dephell will scan current directory to find out file that can be parsed by this converter. If it is filename then dephell will automatically determine file format.
+ `--from-format` -- format for reading requirements. See [deps convert](cmd-deps-convert) command documentation for full list of accepted formats.
+ `--from-path` -- path to input file.
+ `--to` -- path or format for writing requirements.
+ `--to-format` -- output requirements file format.
+ `--to-path` -- path to output file.
+ `--sdist-ratio` -- ratio of tests and project size after which tests will be excluded from sdist. By default is 2 that means tests will be included while their size less than doubled package size.

Commands that accept these parameters:

+ Only `deps convert` accepts `from` and `to` at the same time.
+ `deps install` prefers `to` option if available. This is because when you specified in config file source dependencies in `from` and locked dependencies in `to` then, of course, you want to install dependencies from lock file. However, if `to` (and `to-format` and `to-file`) isn't specified in the config and CLI arguments then `from` will be used.
+ `deps licenses` uses dependencies from `from`, lock them and shows licenses specified on PyPI.
+ `jail install`, `venv create`, `venv run`, and `venv shell` commands use `from` to determine preferred python version for project.

## Resolver and API

+ `--strategy` -- algorithm to select best release. Available values: `min` and `max`. By default is `max`, because almost all resolvers uses this strategy. Read blog post [Minimal Version Selection](https://research.swtch.com/vgo-mvs) for details about `min` strategy.
+ `--prereleases` -- allow prereleases.
+ `--mutations` -- maximum mutations when trying to resolve conflicts. 200 by default.
+ `--warehouse` -- warehouse URLs or local paths to archives with releases.
+ `--bitbucket` -- bitbucket API URL. Dephell isn't use Bitbucket API yet, but option already available.
+ `--repo` -- force repository for first-level dependencies. Useful when you want to use `conda` instead of `pypi` (for example, in [dephell package search](cmd-package-search) command).

## Virtual environment

+ `--venv` -- path to venv directory for project. Replacements:
    + `{project}` will be replaced by the project name (name of path from `project` option, this is name of the current directory by default).
    + `{digest}` will be replaced by the short 4-letters digest of the project path to avoid conflicts for the projects with the same name in different locations.
    + `{env}` will be replaced by current environment (`main` by default).
+ `--python` -- python version for venv. This can be reloaded in the dependencies file.
+ `vars` (config only) -- dict of environment variables to pass in virtual environment.

## Output

+ `--format` -- output format.
+ `--level` -- minimal level for log messages. Available levels: `DEBUG`, `INFO`, `WARNING`, `ERROR` and `EXCEPTION`. `INFO` by default. `DEBUG` and `INFO` writes in the stdout, other levels in the stderr.
+ `--nocolors` -- do not color output.
+ `--silent` -- suppress any output except errors. Disables progress bar for resolver.
+ `--filter` -- [filter for JSON output](filters).
+ `--traceback` -- show traceback for exceptions.
    + `--pdb` -- run [pdb](https://docs.python.org/3/library/pdb.html) when critical exception occurred.

Other:

+ `--owner` -- name of the owner.
+ `--cache-path` -- path to dephell cache.
+ `--cache-ttl` -- Time to live for releases list cache (in seconds). 1 hour by default.
+ `--project` -- path to the current project. Current directory by default.
+ `--bin` -- path to the dir for installing scripts.
+ `--envs` -- environments (`main`, `dev`) or extras to install or convert.
+ `--tests` -- path to test files for [dephell project test](cmd-project-test) command.
+ `--versioning` -- versioning scheme for project. See [dephell project bump](cmd-project-bump) for details.

## Default values

Default values a little bit varies for different systems. Please, use [inspect config](cmd-inspect-config) to view your actual config for current system, project and environment.
# Python and venv lookup

Some commands try to find out the best venv to get information about packages or the best python executable to install packages or create venv. There is described lookup order for these commands.

## Python interpreter lookup

1. `python` parameter in the [config](config) (or as CLI argument `--python`, of course). You can define python here in any way as you want:
    1. Version (`3.7`)
    1. Exact version (`3.7.2`)
    1. Constraint (`>=3.5`)
    1. Executable name (`python3`)
    1. Path to the executable (`/usr/bin/python3`)
1. Dependencies file defined in `from` parameter. For example, [python_requires](https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires) from setup.py.
1. If nothing was found current interpreter (that runs DepHell) will be used.

This lookup is used in commands that can create virtual environment:

+ [dephell jail install](cmd-jail-install)
+ [dephell venv create](cmd-venv-create)
+ [dephell venv run](cmd-venv-run)
+ [dephell venv shell](cmd-venv-shell)

## Virtual environment (venv) lookup

1. If virtual environment for current project (can be specified with `--config`) and environment (can be specified with `--env`) exists then this virtual environment will be used. This is the reason why you have to [create virtual environment](cmd-venv-create) before dependencies installation. Can be overwritten by `--venv` parameter.
1. If some venv is active then it will be used.

This lookup is used in command [dephell inspect venv](cmd-inspect-venv).

## Python environment

Python environment -- any python interpreter: virtual environment or globally installed interpreter. This lookup used when DepHell looks for place to work with packages (analyze, install, remove).

1. First of all, DepHell tries to find virtual environment by virtual environment lookup.
1. If there is no virtual environment then DepHell looks for best global interpreter by Python interpreter lookup.

Commands that use this lookup:

+ [dephell deps install](cmd-deps-install)
+ [dephell deps outdated](cmd-deps-outdated)
+ [dephell package install](cmd-package-install)
+ [dephell package list](cmd-package-list)
+ [dephell package show](cmd-package-show)

If you want to force DepHell ignore project venvs and use global interpreter you can pass into command non-existent venv:

```bash
$ dephell package install --venv=none homoglyphs
INFO build dependencies graph...
INFO installation... (executable=/usr/local/bin/python3.7, packages=1)
...
```
# Pre-commit hook for git

[Pre-commit](https://pre-commit.com/) allows you to do some action before every commit. In these examples, you can generate `requirements.txt` and `setup.py` from `poetry`.

## Without DepHell config

Add next lines in [.pre-commit-config.yaml](https://github.com/mverteuil/precommit-dephell):

```yaml
- repo: https://github.com/mverteuil/precommit-dephell
  rev: master
  hooks:
    - id: pyproject-toml-to-setup-py
    - id: pyproject-toml-to-requirements-txt
```

## With DepHell config

If you have [dephell config](config) you can make the same things quite easier.

Add next lines in [.pre-commit-config.yaml](https://github.com/mverteuil/precommit-dephell):

```yaml
- repo: https://github.com/mverteuil/precommit-dephell
  rev: master
  hooks:
    - id: dephell
```

## See also

1. [Source repository](https://github.com/mverteuil/precommit-dephell).
1. [DepHell config](config).
1. [Hooks in Git](https://githooks.com/).
# Show licenses for your dependencies

You can use [dephell deps licenses](cmd-deps-licenses) command to reveal licenses for all dependencies (and dependencies of dependencies) of your project. For example, let's get licenses for flake8 plugins of dephell. First of all, get dephell source code:

```bash
git clone https://github.com/dephell/dephell.git
cd dephell
```

## With CLI arguments

```bash
$ dephell deps licenses --from-format=pip --from-path=requirements-flake.txt

INFO resolved
{
  "BSD-2-Clause": [
    "enum34"
  ],
  ...
  "Unknown": [
    "flake8-logging-format"
  ]
}
```

## With config

Dephell contains this section in the `pyproject.toml`:

```toml
[tool.dephell.flake8]
from = {format = "pip", path = "requirements-flake.txt"}
```

So, you can write command above quite shorter:

```bash
$ dephell deps licenses --env=flake8
```

## See also

1. [How dephell works with config and parameters](config).
1. [dephell deps licenses](cmd-deps-licenses) documentation.
1. [dephell generate license](cmd-generate-license) to make license for project.
# Lock poetry dependencies

Let's lock [poetry](https://github.com/sdispater/poetry) dependencies for dephell. First of all, get dephell source code:

```bash
git clone https://github.com/dephell/dephell.git
cd dephell
```

## With CLI arguments

```bash
$ dephell deps convert --from=pyproject.toml --to=poetry.lock
```

## With config

Add this in your `pyproject.toml`:

```toml
[tool.dephell.main]
from = {format = "poetry", path = "pyproject.toml"}
to = {format = "poetrylock", path = "poetry.lock"}
```

And then run:

```bash
$ dephell deps convert --config=pyproject.toml --env=main
```

Dephell by default uses `pyproject.toml` config and `main` section, so you can run it much simpler:

```bash
$ dephell deps convert
```

## See also

1. [How dephell works with config and parameters](config)
1. [`dephell deps convert` command](cmd-deps-convert)
# DepHell-powered projects

Need more inspiration? Check out real use cases.

## 50-100 stars

+ [deal](https://github.com/life4/deal) -- Design by contract for Python with many validators support.
+ [lightbus](https://github.com/adamcharnock/lightbus) -- RPC & event framework for Python 3.
+ [scdlbot](https://github.com/gpchelkin/scdlbot) -- Telegram Bot for downloading MP3 rips of tracks/sets from SoundCloud, Bandcamp, YouTube with tags and artwork.

## 10-50 stars

+ [abilian-core](https://github.com/abilian/abilian-core) -- Abilian Core framework and services.
+ [abilian-sbe](https://github.com/abilian/abilian-sbe) -- Abilian Social Business Engine - an enterprise social networking / collaboration platform.
+ [aepp-sdk-python](https://github.com/aeternity/aepp-sdk-python) -- Python SDK for the Æternity blockchain.
+ [fastapi-jsonrpc](https://github.com/smagafurov/fastapi-jsonrpc) -- JSON-RPC server based on fastapi.
+ [flakehell](https://github.com/life4/flakehell) -- Flake8 wrapper to make it nice, legacy-friendly, configurable.
+ [homoglyphs](https://github.com/life4/homoglyphs) -- get similar letters, convert to ASCII, detect possible languages and UTF-8 group.
+ [jazzband-roadies](https://github.com/jazzband-roadies/website) -- Code for the Jazzband website.
+ [micropy-cli](https://github.com/BradenM/micropy-cli) -- Micropython Project Management Tool with VSCode support, Linting, Intellisense, Dependency Management, and more!
+ [plexdl](https://github.com/danielhoherd/plexdl) -- A plex direct downloader. The whole point is to get media that has not been modified.
+ [python-open-controls](https://github.com/qctrl/python-open-controls) -- Q-CTRL Open Controls.
+ [runrestic](https://github.com/andreasnuesslein/runrestic) -- A wrapper script for Restic backup software that inits, creates, prunes and checks backups.
# Make dependencies graph for git repo

Let's make dependencies graph for [ehtim](https://github.com/achael/eht-imaging). This is software that used to [take a photo of black hole](https://www.theguardian.com/science/2019/apr/14/the-new-black-hole-what-can-we-really-see). We can make this graph with [dephell deps tree](cmd-deps-tree) command:

```bash
dephell deps tree --type=graph git+https://github.com/achael/eht-imaging.git#egg=ehtim
```

![ehtim dependencies graph](../assets/ehtim-graph.png)
# Private PyPI repository

## Add PyPI URL

By default, DepHell uses [pypi.org](https://pypi.org/) as warehouse repository:

```bash
$ dephell inspect config --filter="warehouse"
[
  "https://pypi.org/pypi/"
]
```

You can reload it with `--warehouse` [parameter](params):

```bash
$ dephell inspect config --warehouse example1.com example2.com --filter="warehouse"
[
  "example1.com",
  "example2.com"
]
```

You can specify it in the [DepHell config](config):

```toml
[tool.dephell.main]
warehouse = ["example1.com", "example2.com"]
```

DepHell supports path to local directory with releases archives:

```toml
[tool.dephell.main]
warehouse = ["./path/to/releases"]
```

If you explicitly specify `warehouse`, DepHell drops default value and don't use [pypi.org](https://pypi.org/) anymore. If you want to use it after your private repository, also add it in the list:

```bash
dephell inspect config --warehouse https://example1.com/simple https://pypi.org/ --filter="warehouse"
[
  "https://example1.com/simple",
  "https://pypi.org/"
]
```

You can remove any repositories at all to use only specified in dependencies file:

```bash
$ dephell inspect config --warehouse --filter="warehouse"
[]
```

## Authentication

Use [dephell self auth](cmd-self-auth) to add credentials for host in global config:

```bash
$ dephell self auth example.com gram "p@ssword"
INFO credentials added (hostname=example.com, username=gram)
```

You can list stored credentials with [dephell inspect auth](cmd-inspect-auth):

```bash
$ dephell inspect auth
[
  {
    "hostname": "example.com",
    "password": "p@ssword",
    "username": "gram"
  }
]
```

## Dependency file

Some dependency formats support explicit repository specification. These repositories always have higher priority than specified in config.

`requirements.txt`:

```bash
-i https://example.com/
-i https://pypi.org/simple/
...
```

`Pipfile`:

```toml
[[source]]
url = "https://example.com/"
verify_ssl = true
name = "example"

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

# ...

[packages]
deal = {index="example"}
# ^ try to find in "example" repository before all
```

Poetry (`pyproject.toml`)

```toml
# ...

[[tool.poetry.source]]
name = "example"
url = "https://example.com/"

[[tool.poetry.source]]
name = "pypi"
url = "https://pypi.org/simple"
```
attrs
requests
Django<=1.11
deal>=2.0
Django>=1.11
Django<1.9
scipy==0.19.1
pandas>=0.20.3
numpy<=1.17.0
git+https://github.com/gwtwod/poetrylibtest#egg=libtest-0.1.0
[console_scripts]
dephell = dephell.cli:entrypoint

# ![DepHell](./assets/logo.png)

Dependency resolution for Python.

## Installation

```bash
sudo pip3 install dephell
```

## CLI usage

With arguments:

```bash
python3 -m dephell convert \
    --from-format=pip --from-path=requirements.in \
    --to-format=piplock --to-path=requirements.txt
```

With config:

```bash
python3 -m dephell convert --config=pyproject.toml --env=main
```

Mix config and arguments:

```bash
python3 -m dephell convert --config=pyproject.toml \
    --to-format=piplock --to-path=requirements.txt
```

Available formats:

1. `pip` -- [pip's requirements file](https://pip.pypa.io/en/stable/user_guide/#id1).
1. `piplock` -- [locked](https://pip.pypa.io/en/stable/reference/pip_freeze/) pip's requirements file.
1. `pipfile` -- not locked [Pipfile](https://github.com/pypa/pipfile#pipfile)
1. `pipfilelock` -- locked [Pipfile](https://github.com/pypa/pipfile#pipfilelock)

## Python lib usage

```python
from dephell import PIPConverter, Requirement

loader = PIPConverter(lock=False)
resolver = loader.load_resolver(path='requirements.in')

resolver.resolve()
reqs = Requirement.from_graph(resolver.graph, lock=True)

dumper = PIPConverter(lock=True)
dumper.dump(reqs=reqs, path='requirements.txt')
```

## TODO

1. poetry
1. poetry lock
1. Python version
1. Zero release (compatible with any constraints)
1. url defined release
1. git based dependency


.. image:: ./assets/logo.png
   :target: ./assets/logo.png
   :alt: DepHell

=============================================================================

Dependency resolution for Python.

Installation
------------

.. code-block:: bash

   sudo pip3 install dephell

CLI usage
---------

With arguments:

.. code-block:: bash

   python3 -m dephell convert \
       --from-format=pip --from-path=requirements.in \
       --to-format=piplock --to-path=requirements.txt

With config:

.. code-block:: bash

   python3 -m dephell convert --config=pyproject.toml --env=main

Mix config and arguments:

.. code-block:: bash

   python3 -m dephell convert --config=pyproject.toml \
       --to-format=piplock --to-path=requirements.txt

Available formats:


#. ``pip`` -- `pip's requirements file <https://pip.pypa.io/en/stable/user_guide/#id1>`_.
#. ``piplock`` -- `locked <https://pip.pypa.io/en/stable/reference/pip_freeze/>`_ pip's requirements file.
#. ``pipfile`` -- not locked `Pipfile <https://github.com/pypa/pipfile#pipfile>`_
#. ``pipfilelock`` -- locked `Pipfile <https://github.com/pypa/pipfile#pipfilelock>`_

Python lib usage
----------------

.. code-block:: python

   from dephell import PIPConverter, Requirement

   loader = PIPConverter(lock=False)
   resolver = loader.load_resolver(path='requirements.in')

   resolver.resolve()
   reqs = Requirement.from_graph(resolver.graph, lock=True)

   dumper = PIPConverter(lock=True)
   dumper.dump(reqs=reqs, path='requirements.txt')

TODO
----


#. poetry
#. poetry lock
#. Python version
#. Zero release (compatible with any constraints)
#. url defined release
#. git based dependency
attrs
cached_property
packaging
requests
libtest

[windows]
colorama
setup.py
dephell.egg-info/PKG-INFO
dephell.egg-info/SOURCES.txt
dephell.egg-info/dependency_links.txt
dephell.egg-info/entry_points.txt
dephell.egg-info/requires.txt
dephell.egg-info/top_level.txt
# built-in
import json
from pathlib import Path

# external
import pytest

# project
from dephell.commands import DepsLicensesCommand
from dephell.config import Config


@pytest.mark.allow_hosts()
def test_deps_licenses_command(temp_path: Path, capsys):
    reqs_path = temp_path / 'requirements.txt'
    reqs_path.write_text('six==1.12.0')

    config = Config()
    config.attach({
        'from': dict(format='pip', path=str(reqs_path)),
        'level': 'WARNING',
        'silent': True,
        'nocolors': True,
    })

    command = DepsLicensesCommand(argv=[], config=config)
    result = command()

    captured = capsys.readouterr()
    output = json.loads(captured.out)
    assert result is True
    assert output == {'MIT': ['six']}
# built-in
from datetime import date
from pathlib import Path

# external
import pytest

# project
from dephell.commands import GenerateLicenseCommand
from dephell.config import Config


@pytest.mark.allow_hosts(['pypi.org', '140.211.169.8'])
def test_generate_license_command(temp_path: Path):
    config = Config()
    config.attach({'project': str(temp_path)})
    command = GenerateLicenseCommand(argv=['MIT'], config=config)
    result = command()

    assert result is True
    assert (temp_path / 'LICENSE').exists()
    content = (temp_path / 'LICENSE').read_text()
    assert 'MIT License' in content
    assert str(date.today().year) in content
