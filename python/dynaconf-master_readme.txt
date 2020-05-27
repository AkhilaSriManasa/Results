Changelog
=========


2.2.2 (2019-12-26)
------------------
- Release version 2.2.2. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (3):
            Release version 2.2.1
            Fix #258 custom message for validators
            Pin python-box version because of a breaking release

      Hildeberto (1):
            Close #178. Included integration tests redis/vault
- Pin python-box version because of a breaking release. [Bruno Rocha]

  The release of python-box https://github.com/cdgriffith/Box/pull/116
  is a breaking change.

  So pinning this until this project addapts.

  Also pinning other direct deps.
- Fix #258 custom message for validators. [Bruno Rocha]
- Close #178. Included integration tests redis/vault. [Hildeberto]
- Release version 2.2.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (4):
            Release version 2.2.0
            Fix #251 recursive call was using mutable memoized data (#254)
            Fix #266 created new variable FORCE_ENV to override ENV_FOR_DYNACONF
            Fix coverage for validators

      David Moreau Simard (1):
            Add ara as a user of dynaconf (#252)

      Emmanuel Nosa Evbuomwan (1):
            Update sensitive_secrets.md

      Hildeberto (1):
            Adjust remote upstream URL

      Jan Willhaus (1):
            Add support for detecting duplicate validators being added (and ignore them) (#256)

      Oliver Lehmann (5):
            fix: env_loader.write: quote_mode for non-string values
            : added line break
            fix str comparison
            changing quote logic
            fix open error @py3.5


2.2.1 (2019-12-06)
------------------

Fix
~~~
- Env_loader.write: quote_mode for non-string values. [Oliver Lehmann]

Other
~~~~~
- Release version 2.2.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (4):
            Release version 2.2.0
            Fix #251 recursive call was using mutable memoized data (#254)
            Fix #266 created new variable FORCE_ENV to override ENV_FOR_DYNACONF
            Fix coverage for validators

      David Moreau Simard (1):
            Add ara as a user of dynaconf (#252)

      Emmanuel Nosa Evbuomwan (1):
            Update sensitive_secrets.md

      Hildeberto (1):
            Adjust remote upstream URL

      Jan Willhaus (1):
            Add support for detecting duplicate validators being added (and ignore them) (#256)

      Oliver Lehmann (5):
            fix: env_loader.write: quote_mode for non-string values
            : added line break
            fix str comparison
            changing quote logic
            fix open error @py3.5
- Fix coverage for validators. [Bruno Rocha]
- Fix #266 created new variable FORCE_ENV to override ENV_FOR_DYNACONF.
  [Bruno Rocha]
- Adjust remote upstream URL. [Hildeberto]
- Update sensitive_secrets.md. [Emmanuel Nosa Evbuomwan]

  Updated the file reference from `settings`.toml{json|py|ini|yaml} to the convention used thus far; `secrets`.toml{json|py|ini|yaml}. This can help alleviate the slightest chance of the information becoming misleading or confusing. This can also be ignored if Dynaconf can be set to search for secrets in files other than `secrets.<ext>`
- Fix open error @py3.5. [Oliver Lehmann]
- Changing quote logic. [Oliver Lehmann]
- Fix str comparison. [Oliver Lehmann]
- : added line break. [Oliver Lehmann]
- Add support for detecting duplicate validators being added (and ignore
  them) (#256) [Jan Willhaus]
- Fix #251 recursive call was using mutable memoized data (#254) [Bruno
  Rocha]

  replaced with recursive passing of parent data.

  NOTE to SELF: Never! use a mutable memoized data
                Always use `==` to compare when you dont know the types
- Add ara as a user of dynaconf (#252) [David Moreau Simard]
- Release version 2.2.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (5):
            Release version 2.1.1
            Fix #236 added .local. files loading and module impersonation docs (#239)
            Replace key.upper with `upperfy` function that keeps `__` attributes (#240)
            Fix #241 new merge standards (#243)
            Add support for PRELOAD_ setting. (#244)

      Kedar Kulkarni (1):
            Fixing how filename.local.* files are loaded (#238)

      paskozdilar (1):
            fix crash on empty settings (#242)


2.2.0 (2019-10-09)
------------------
- Release version 2.2.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (5):
            Release version 2.1.1
            Fix #236 added .local. files loading and module impersonation docs (#239)
            Replace key.upper with `upperfy` function that keeps `__` attributes (#240)
            Fix #241 new merge standards (#243)
            Add support for PRELOAD_ setting. (#244)

      Kedar Kulkarni (1):
            Fixing how filename.local.* files are loaded (#238)

      paskozdilar (1):
            fix crash on empty settings (#242)
- Add support for PRELOAD_ setting. (#244) [Bruno Rocha]
- Fix #241 new merge standards (#243) [Bruno Rocha]

  Adds dynaconf_merge and @merge for better merge standards. ref #241
- Fix crash on empty settings (#242) [paskozdilar]

  * fix crash on empty settings

  * add test for empty environment

  * fix PEP 8 issue (expected 2 blank lines, found 1)
- Replace key.upper with `upperfy` function that keeps `__` attributes
  (#240) [Bruno Rocha]
- Fix #236 added .local. files loading and module impersonation docs
  (#239) [Bruno Rocha]

  also MERGE_ENABLED is no more deprecated.
- Fixing how filename.local.* files are loaded (#238) [Kedar Kulkarni]
- Release version 2.1.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (7):
            Release version 2.1.0
            Improve validators to use `from_env` method (#225)
            Add info about dunder envvars on django.md docs guide (#226)
            Fix #228 add `ignore` argument to Django explicit mode. (#229)
            Improvement to close #230 - do not throw error for base envs. (#231)
            dynaconf init will not write all possible envs, only [default] (#233)
            When both enabled, Vault has the priority over Redis for overriding (#234)

      Dave Barnow (1):
            Fix typo in CLI init (#227)

      Kedar Kulkarni (1):
            Fixing self._root_path to fall back to os.getcwd() only when `settings.load_file` is called directly or from includes (#232)


2.1.1 (2019-09-16)
------------------
- Release version 2.1.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (7):
            Release version 2.1.0
            Improve validators to use `from_env` method (#225)
            Add info about dunder envvars on django.md docs guide (#226)
            Fix #228 add `ignore` argument to Django explicit mode. (#229)
            Improvement to close #230 - do not throw error for base envs. (#231)
            dynaconf init will not write all possible envs, only [default] (#233)
            When both enabled, Vault has the priority over Redis for overriding (#234)

      Dave Barnow (1):
            Fix typo in CLI init (#227)

      Kedar Kulkarni (1):
            Fixing self._root_path to fall back to os.getcwd() only when `settings.load_file` is called directly or from includes (#232)
- When both enabled, Vault has the priority over Redis for overriding
  (#234) [Bruno Rocha]
- Dynaconf init will not write all possible envs, only [default] (#233)
  [Bruno Rocha]
- Fixing self._root_path to fall back to os.getcwd() only when
  `settings.load_file` is called directly or from includes (#232) [Kedar
  Kulkarni]
- Improvement to close #230 - do not throw error for base envs. (#231)
  [Bruno Rocha]
- Fix #228 add `ignore` argument to Django explicit mode. (#229) [Bruno
  Rocha]
- Fix typo in CLI init (#227) [Dave Barnow]
- Add info about dunder envvars on django.md docs guide (#226) [Bruno
  Rocha]
- Improve validators to use `from_env` method (#225) [Bruno Rocha]
- Release version 2.1.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (8):
            Release version 2.0.4
            Merge branch 'dgarcia360-master'
            Fix #197 add support for DOTTED__ENV__VARS (#215)
            Add support to export merged env to filesystem via cli. (#217)
            Adds `from_env` method and change `_store` to be a `DynaBox` (#219)
            hotfix: next release will be 2.1.0 because new features added. (#220)
            Fix `make test_examples` to use better assertions, redis and vault loader now respects `envs` (#222)
            fix #221 removed JSON,YAML,INI,TOML cosntants from default_settings (#223)

      Kedar Kulkarni (1):
            Add `list_envs` function to vault loader and now envs can have `_` on its name.

      Pavel Alimpiev (1):
            Fix typo in documentation for a Validator class (#213)

      dgarcia360 (3):
            Updated configuration options table to csv table
            Added responsive table fix
            Fix format


2.1.0 (2019-09-05)
------------------
- Release version 2.1.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (8):
            Release version 2.0.4
            Merge branch 'dgarcia360-master'
            Fix #197 add support for DOTTED__ENV__VARS (#215)
            Add support to export merged env to filesystem via cli. (#217)
            Adds `from_env` method and change `_store` to be a `DynaBox` (#219)
            hotfix: next release will be 2.1.0 because new features added. (#220)
            Fix `make test_examples` to use better assertions, redis and vault loader now respects `envs` (#222)
            fix #221 removed JSON,YAML,INI,TOML cosntants from default_settings (#223)

      Kedar Kulkarni (1):
            Add `list_envs` function to vault loader and now envs can have `_` on its name.

      Pavel Alimpiev (1):
            Fix typo in documentation for a Validator class (#213)

      dgarcia360 (3):
            Updated configuration options table to csv table
            Added responsive table fix
            Fix format
- Fix #221 removed JSON,YAML,INI,TOML cosntants from default_settings
  (#223) [Bruno Rocha]

  Default settings should hold only constants ending in _FOR_DYNACONF
- Fix `make test_examples` to use better assertions, redis and vault
  loader now respects `envs` (#222) [Bruno Rocha]
- Hotfix: next release will be 2.1.0 because new features added. (#220)
  [Bruno Rocha]
- Adds `from_env` method and change `_store` to be a `DynaBox` (#219)
  [Bruno Rocha]
- Add `list_envs` function to vault loader and now envs can have `_` on
  its name. [Kedar Kulkarni]

  * Adding new feature to address issue #211 `list_envs ` function on vault loader
  * Removing restriction with env cannot contain underscore chars
- Add support to export merged env to filesystem via cli. (#217) [Bruno
  Rocha]

  fix #200

  ```bash
  dynaconf list -o path/to/file.yaml --output-flat
  ```
- Fix #197 add support for DOTTED__ENV__VARS (#215) [Bruno Rocha]

  * Fix #197 add support for DOTTED__ENV__VARS

  * Full support for `__` - @reset and @del markers
- Merge branch 'dgarcia360-master' [Bruno Rocha]
- Fix format. [dgarcia360]
- Added responsive table fix. [dgarcia360]
- Updated configuration options table to csv table. [dgarcia360]
- Fix typo in documentation for a Validator class (#213) [Pavel
  Alimpiev]
- Release version 2.0.4. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (2):
            Release version 2.0.3
            Fix #207 allow python module path name for includes (#209)

      Michał Bartoszkiewicz (1):
            Update usage.md (#208)

      Pavel Alimpiev (2):
            Refactor Vault integration (#202)
            Update configuration.md (#205)

      Tanveer Alam (2):
            Update usage.md (#196)
            Update usage.md (#195)


2.0.4 (2019-08-22)
------------------
- Release version 2.0.4. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (2):
            Release version 2.0.3
            Fix #207 allow python module path name for includes (#209)

      Michał Bartoszkiewicz (1):
            Update usage.md (#208)

      Pavel Alimpiev (2):
            Refactor Vault integration (#202)
            Update configuration.md (#205)

      Tanveer Alam (2):
            Update usage.md (#196)
            Update usage.md (#195)
- Fix #207 allow python module path name for includes (#209) [Bruno
  Rocha]
- Update usage.md (#208) [Michał Bartoszkiewicz]

  Change 'FLask' to 'Flask'
- Update configuration.md (#205) [Pavel Alimpiev]
- Refactor Vault integration (#202) [Pavel Alimpiev]

  * Add AppRole based authorization for Vault loader

  * Fix default value for VAULT_PATH_FOR_DYNACONF, Update docs

  * HVAC automatically adds /secret/ prefix on read and write access
  * /dynaconf was never added to the VAULT_PATH_FOR_DYNACONF value
  * Docs was inconsistent with the actual code base

  * Fix inconsistency in the docs

  * Remove VAULT_SESSION_FOR_DYNACONF config variable.

  * HVAC's session argument must be a fully initialized Session object,
  that means - it's very complicated to setup Vault client with this
  argument, via default instruments (.toml, .env, etc)
  * Users can still setup this argument by setting up VAULT_FOR_DYNACONF
  directly

  * Update documentation for VAULT_* configuration

  * Fix code style
- Update usage.md (#195) [Tanveer Alam]
- Update usage.md (#196) [Tanveer Alam]
- Release version 2.0.3. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (2):
            Release version 2.0.2
            Fix #194 flask.app.config __setitem__ (#199)

      Jan Willhaus (1):
            Catch BoxKeyError when contents are TOML parsable but not keyable (#192)

      Raoul Snyman (1):
            Use the Key Value API rather than the old 'read' and 'write' methods (#198)


2.0.3 (2019-06-27)
------------------
- Release version 2.0.3. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (2):
            Release version 2.0.2
            Fix #194 flask.app.config __setitem__ (#199)

      Jan Willhaus (1):
            Catch BoxKeyError when contents are TOML parsable but not keyable (#192)

      Raoul Snyman (1):
            Use the Key Value API rather than the old 'read' and 'write' methods (#198)
- Fix #194 flask.app.config __setitem__ (#199) [Bruno Rocha]

  Flask.config was not proxying __setitem__ atribute so this
  change adds a call to __setitem__ on contrib/flask_dynaconf
- Use the Key Value API rather than the old 'read' and 'write' methods
  (#198) [Raoul Snyman]
- Catch BoxKeyError when contents are TOML parsable but not keyable
  (#192) [Jan Willhaus]
- Release version 2.0.2. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (8):
            Release version 2.0.1
            Add note to release script
            Adhering to Github Community Standards (#175)
            removed pytest-xdist (#181)
            Add example and test for issue #182 (#183)
            Fix #179 dynaconf cli shows only user defined vars unless -a used (#188)
            Fix #184 - workdir should walk to root in ipython REPL (#190)
            Fix #189 added `settings.as_dict()` and `dynaconf list -o file.json` (#191)

      Jan Willhaus (4):
            Fix `False` not being an acceptable env (#176)
            Fix  base loader when having no ENVVAR_PREFIX_ (Addresses #177) (#185)
            Hide DeprecationWarning from Pytest when testing for them (#186)
            Replace logging.basicConfig with handler on logger (#187)


2.0.2 (2019-04-29)
------------------
- Release version 2.0.2. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (8):
            Release version 2.0.1
            Add note to release script
            Adhering to Github Community Standards (#175)
            removed pytest-xdist (#181)
            Add example and test for issue #182 (#183)
            Fix #179 dynaconf cli shows only user defined vars unless -a used (#188)
            Fix #184 - workdir should walk to root in ipython REPL (#190)
            Fix #189 added `settings.as_dict()` and `dynaconf list -o file.json` (#191)

      Jan Willhaus (4):
            Fix `False` not being an acceptable env (#176)
            Fix  base loader when having no ENVVAR_PREFIX_ (Addresses #177) (#185)
            Hide DeprecationWarning from Pytest when testing for them (#186)
            Replace logging.basicConfig with handler on logger (#187)
- Fix #189 added `settings.as_dict()` and `dynaconf list -o file.json`
  (#191) [Bruno Rocha]
- Fix #184 - workdir should walk to root in ipython REPL (#190) [Bruno
  Rocha]
- Fix #179 dynaconf cli shows only user defined vars unless -a used
  (#188) [Bruno Rocha]

  Command `dynaconf list` will show only user defined vars
  IF `--all|-a` is passed then it includes internal variables.
- Replace logging.basicConfig with handler on logger (#187) [Jan
  Willhaus]
- Hide DeprecationWarning from Pytest when testing for them (#186) [Jan
  Willhaus]

  * Hide DeprecationWarnings from Pytest when testing for them

  * Use parametrized test instead of repeating code
- Fix  base loader when having no ENVVAR_PREFIX_ (Addresses #177) (#185)
  [Jan Willhaus]

  * Fix `False` not being an acceptable env

  * Additional testcase for prefix being false from envvar

  * Fix mistaken reference to ENVVAR_PREFIX

  * Fix typo
- Add example and test for issue #182 (#183) [Bruno Rocha]

  * Add working example for issue 182

  * Option 2 added

  * Allowed `settings.load_file` programmatically
- Removed pytest-xdist (#181) [Bruno Rocha]

  Now tests run in a separate tmpdir so xdist is not needed anymore
- Fix `False` not being an acceptable env (#176) [Jan Willhaus]

  * Fix `False` not being an acceptable env

  * Additional testcase for prefix being false from envvar

  * unset envvar_prefix after test
- Adhering to Github Community Standards (#175) [Bruno Rocha]
- Add note to release script. [Bruno Rocha]
- Release version 2.0.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (17):
            Release version 2.0.0
            Added Django explicit mode to docs (#149)
            HOTIX: Django doc
            Logger is now cached (removed logging import time overhead)
            Update issue templates
            Adjusts issue templates
            Fix Typo in issue template
            fix #160 - invoking directory should not be search breaking point.
            Add explicit call to main() on cli.py (#165)
            Generate coverage.xml file (#167)
            Fix #166 renamed GLOBAL_ENV_ to ENVVAR_PREFIX_ (#168)
            Fix #169 renamed SETTINGS_MODULE_ to SETTINGS_FILE_ (#170)
            HOTFIX config.md on docs [skip ci] (#171)
            Fix some open file descriptors on exampls and tests (#172)
            Fix #151 setup pre-commit and black (#173)
            Add CONTRIBUTING.md, conrtib isntructions and Black badge (#174)
            Fix release script

      David Moreau Simard (1):
            Fix typos in bash export examples

      Jan Willhaus (2):
            Skip reloading envs for validators that only apply to current_env (#162)
            Fix #163 Allow disabling env prefix (#164)


2.0.1 (2019-04-22)
------------------
- Release version 2.0.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (17):
            Release version 2.0.0
            Added Django explicit mode to docs (#149)
            HOTIX: Django doc
            Logger is now cached (removed logging import time overhead)
            Update issue templates
            Adjusts issue templates
            Fix Typo in issue template
            fix #160 - invoking directory should not be search breaking point.
            Add explicit call to main() on cli.py (#165)
            Generate coverage.xml file (#167)
            Fix #166 renamed GLOBAL_ENV_ to ENVVAR_PREFIX_ (#168)
            Fix #169 renamed SETTINGS_MODULE_ to SETTINGS_FILE_ (#170)
            HOTFIX config.md on docs [skip ci] (#171)
            Fix some open file descriptors on exampls and tests (#172)
            Fix #151 setup pre-commit and black (#173)
            Add CONTRIBUTING.md, conrtib isntructions and Black badge (#174)
            Fix release script

      David Moreau Simard (1):
            Fix typos in bash export examples

      Jan Willhaus (2):
            Skip reloading envs for validators that only apply to current_env (#162)
            Fix #163 Allow disabling env prefix (#164)
- Fix release script. [Bruno Rocha]
- Add CONTRIBUTING.md, conrtib isntructions and Black badge (#174)
  [Bruno Rocha]
- Fix #151 setup pre-commit and black (#173) [Bruno Rocha]

  * Add pre-commit to makefile

  * Fix #151 setup pre-commit and black
- Fix some open file descriptors on exampls and tests (#172) [Bruno
  Rocha]
- HOTFIX config.md on docs [skip ci] (#171) [Bruno Rocha]
- Fix #169 renamed SETTINGS_MODULE_ to SETTINGS_FILE_ (#170) [Bruno
  Rocha]

  Backwards compatibility maintained!
- Fix #166 renamed GLOBAL_ENV_ to ENVVAR_PREFIX_ (#168) [Bruno Rocha]

  * Fix #166 renamed GLOBAL_ENV_ to ENVVAR_PREFIX_

  See #166

  * Added django compat example
- Generate coverage.xml file (#167) [Bruno Rocha]
- Add explicit call to main() on cli.py (#165) [Bruno Rocha]

  To use click-web tool the module should be able to be explicitly called. `python -m dynaconf.cli`
- Fix #163 Allow disabling env prefix (#164) [Jan Willhaus, janw
  <mail@janwillhaus.de>    * Update docs for use of False instead of
  none]

  * Allow setting GLOBAL_ENV to "" or NoneType to remove prefix

  * Allow for underscore-only prefix with empty string GLOBAL_ENV

  * Test cases for the different GLOBAL_ENV settings

  * Update docs, add usage example

  * Apply suggestions from code review
- Skip reloading envs for validators that only apply to current_env
  (#162) [Jan Willhaus]

  * Simplify control flow for single-env use-cases

  * Ensure uppercase env/current_env

  * Add test not reloading env with validation in same env

  * Pep8 compliance

  * Change mock call assertions for support in Py3.5
- Fix #160 - invoking directory should not be search breaking point.
  [Bruno Rocha]

  Search should stop at breaking point  only if ROOT_PATH is defined
- Fix Typo in issue template. [Bruno Rocha]
- Adjusts issue templates. [Bruno Rocha]
- Update issue templates. [Bruno Rocha]
- Logger is now cached (removed logging import time overhead) [Bruno
  Rocha]

  Debugged using:

  `python3.7 -X importtime -c 'import app'` and `python3.7 -X importtime -c 'import dynaconf'`

  Found that the tries to import `logzero` were consuming 0.1us (not so much, but we dont want it)

  removed logzero, cached logger using lru_cache (that means that if loglevel changes, log changes)

  - imporved docs and badges.
- Fix typos in bash export examples. [David Moreau Simard]
- HOTIX: Django doc. [Bruno Rocha]
- Added Django explicit mode to docs (#149) [Bruno Rocha]
- Release version 2.0.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Aaron DeVore (1):
            GH-111: Fix MERGE_ENABLED merging settings with themselves

      Bruno Rocha (21):
            Merge branch 'jperras-merge-multiple-settings-files'
            Merge branch 'master' of github.com:rochacbruno/dynaconf
            Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths
            Update dynaconf/utils/boxing.py
            Update dynaconf/utils/boxing.py
            Add release script and CHANGELOG in place of history.
            Release version 1.2.0
            Tox is now part of pre-publish command
            Drop Python 3.4
            Release version 1.2.1
            add top contributors
            Fix #129 on settings file, single keys should be case insensitive.
            Fix #125 settings_module not being set on .configure()
            Fix #127 add configurable yaml loader method, default to full_load
            Fix #122 allow disable of core loaders, added examples.
            Fix #117 add support for extra secrets file (like for jenkins CI)
            Fix #110 add docs for dynaconf_include
            Add dynaconf_include examples
            Set up CI with Azure Pipelines (#142)
            Add dynaconf_merge fucntionality for dict and list settings. (#139)
            Preparing for 2.0.0

      Byungjin Park (1):
            Fix typo

      Jaepil Koh (1):
            Update django.md

      Joel Perras (3):
            Allow dotted-path based setting of configuration key/value pairs.
            Handle nested includes in settings files.
            Remove extraneous lines.

      Mantas (3):
            Add INSTANCE_FOR_DYNACONF and --instance
            Remove mocker fixture
            Python 3.4 has different error message

      Matthias (1):
            Fix small typo in README.md

      Pete Savage (1):
            Fix exponential slow down when loader is run multiple times

      Raoul Snyman (1):
            Add environments into the path in Vault so that the same Vault server can be used for multiple environments

      mspinelli (2):
            fixed infinite recursion caused by copy()
            add tests for dynabox fix


2.0.0 (2019-04-09)
------------------
- Release version 2.0.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Aaron DeVore (1):
            GH-111: Fix MERGE_ENABLED merging settings with themselves

      Bruno Rocha (21):
            Merge branch 'jperras-merge-multiple-settings-files'
            Merge branch 'master' of github.com:rochacbruno/dynaconf
            Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths
            Update dynaconf/utils/boxing.py
            Update dynaconf/utils/boxing.py
            Add release script and CHANGELOG in place of history.
            Release version 1.2.0
            Tox is now part of pre-publish command
            Drop Python 3.4
            Release version 1.2.1
            add top contributors
            Fix #129 on settings file, single keys should be case insensitive.
            Fix #125 settings_module not being set on .configure()
            Fix #127 add configurable yaml loader method, default to full_load
            Fix #122 allow disable of core loaders, added examples.
            Fix #117 add support for extra secrets file (like for jenkins CI)
            Fix #110 add docs for dynaconf_include
            Add dynaconf_include examples
            Set up CI with Azure Pipelines (#142)
            Add dynaconf_merge fucntionality for dict and list settings. (#139)
            Preparing for 2.0.0

      Byungjin Park (1):
            Fix typo

      Jaepil Koh (1):
            Update django.md

      Joel Perras (3):
            Allow dotted-path based setting of configuration key/value pairs.
            Handle nested includes in settings files.
            Remove extraneous lines.

      Mantas (3):
            Add INSTANCE_FOR_DYNACONF and --instance
            Remove mocker fixture
            Python 3.4 has different error message

      Matthias (1):
            Fix small typo in README.md

      Pete Savage (1):
            Fix exponential slow down when loader is run multiple times

      Raoul Snyman (1):
            Add environments into the path in Vault so that the same Vault server can be used for multiple environments

      mspinelli (2):
            fixed infinite recursion caused by copy()
            add tests for dynabox fix
- Preparing for 2.0.0. [Bruno Rocha]

  Dynaconf 2.0.0

  - Fix #129 get_fresh should be case insensitive
  - Fix #125 .configure was not loading `settings_module` passed as argument
  - Fix #127 fix YAML warnings and default to full_load
  - Allow disable of core loaders #122
  - Added support for Jenkins secrets file #117
  - Added more examples for includes #110
  - Moved to Azure Pipelines CI #142
  - Added 100% test coverage on windows (Unit & Functional tests)
  - Deprecated MERGE_ENABLED in favor of local dynaconf_merge
  - Fix #74 - Better File Searching (now building a reasonable Search Tree)
  - Now it finds settings when invoking from out of Script folder
  - Fixed test environment (each test now run in a separate tmpdir)
  - Added a check to avoid Circular references when starting settings inside settings
  - Added Django Extension v2 with better syntax and a lot od `inspect` instrospetion
  - Updated documentation about new features
  - Added a not that YAML is the recommended format for Django
  - Added support for Django Standalone Script
  - Added support for Django unit testing
  - Fix #148 `env` was not being passed to custom loaders
  - Fix #144 removed `six` as it is a Py3.4+ only project
  - Added Backwards compatibility for users using old django Extension
  - start_dotenv is now Lazy (only when settings._setup is called)
  - Added new _FOR_DYNACONF config options ENV_SWITCHER, SKIP_FILES, INCLUDES & SECRETS
  - Renamed config PROJECT_ROOT -> ROOT_PATH
- Add dynaconf_merge fucntionality for dict and list settings. (#139)
  [Bruno Rocha]

  If your settings has existing variables of types `list` ot `dict` and you want to `merge` instead of `override` then
  the `dynaconf_merge` and `dynaconf_merge_unique` stanzas can mark that variable as a candidate for merging.

  For **dict** value:

  Your main settings file (e.g `settings.toml`) has an existing `DATABASE` dict setting on `[default]` env.

  Now you want to contribute to the same `DATABASE` key by addind new keys, so you can use `dynaconf_merge` at the end of your dict:

  In specific `[envs]`

  ```toml
  [default]
  database = {host="server.com", user="default"}

  [development]
  database = {user="dev_user", dynaconf_merge=true}

  [production]
  database = {user="prod_user", dynaconf_merge=true}
  ```

  In an environment variable:

  ```bash
  export DYNACONF_DATABASE='{password=1234, dynaconf_merge=true}'
  ```

  Or in an additional file (e.g `settings.yaml, .secrets.yaml, etc`):

  ```yaml
  default:
    database:
      password: 1234
      dynaconf_merge: true
  ```

  The `dynaconf_merge` token will mark that object to be merged with existing values (of course `dynaconf_merge` key will not be added to the final settings it is jsut a mark)

  The end result will be on `[development]` env:

  ```python
  settings.DATABASE == {'host': 'server.com', 'user': 'dev_user', 'password': 1234}
  ```

  The same can be applied to **lists**:

  `settings.toml`
  ```toml
  [default]
  plugins = ["core"]

  [development]
  plugins = ["debug_toolbar", "dynaconf_merge"]
  ```

  And in environment variable

  ```bash
  export DYNACONF_PLUGINS='["ci_plugin", "dynaconf_merge"]'
  ```

  Then the end result on `[development]` is:

  ```python
  settings.PLUGINS == ["ci_plugin", "debug_toolbar", "core"]
  ```

  The `dynaconf_merge_unique` is the token for when you want to avoid duplications in a list.

  Example:

  ```toml
  [default]
  scripts = ['install.sh', 'deploy.sh']

  [development]
  scripts = ['dev.sh', 'test.sh', 'deploy.sh', 'dynaconf_merge_unique']
  ```

  ```bash
  export DYNACONF_SCRIPTS='["deploy.sh", "run.sh", "dynaconf_merge_unique"]'
  ```

  The end result for `[development]` will be:

  ```python
  settings.SCRIPTS == ['install.sh', 'dev.sh', 'test.sh', 'deploy.sh', 'run.sh']
  ```

  > Note that `deploy.sh` is set 3 times but it is not repeated in the final settings.

  The **dynaconf_merge** functionality works only for the first level keys, it will not merge subdicts or nested lists (yet).
- Set up CI with Azure Pipelines (#142) [Bruno Rocha]

  - setup azure pipelines ci
  - remove travis
  - fix windows support
- Add dynaconf_include examples. [Bruno Rocha]
- Fix #110 add docs for dynaconf_include. [Bruno Rocha]

  fix #110
- Fix #117 add support for extra secrets file (like for jenkins CI)
  [Bruno Rocha]

  Now it is possible to export SECRETS_FOR_DYNACONF and have this
  extra point loaded, like in a Jenkins CI you can specify on job.

  ```yaml
  secret_file:
    variable: SECRETS_FOR_DYNACONF
    credentials:
      type: specific_credentials
      value: /path/to/secrets_file.toml{json,ini,yaml,py}

  ```

  That variable can also be a list of paths.
- Fix #122 allow disable of core loaders, added examples. [Bruno Rocha]
- Fix #127 add configurable yaml loader method, default to full_load.
  [Bruno Rocha]
- Fix #125 settings_module not being set on .configure() [Bruno Rocha]
- Fix #129 on settings file, single keys should be case insensitive.
  [Bruno Rocha]
- GH-111: Fix MERGE_ENABLED merging settings with themselves. [Aaron
  DeVore]
- Add top contributors. [Bruno Rocha]
- Release version 1.2.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (9):
            Merge branch 'jperras-merge-multiple-settings-files'
            Merge branch 'master' of github.com:rochacbruno/dynaconf
            Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths
            Update dynaconf/utils/boxing.py
            Update dynaconf/utils/boxing.py
            Add release script and CHANGELOG in place of history.
            Release version 1.2.0
            Tox is now part of pre-publish command
            Drop Python 3.4

      Byungjin Park (1):
            Fix typo

      Jaepil Koh (1):
            Update django.md

      Joel Perras (3):
            Allow dotted-path based setting of configuration key/value pairs.
            Handle nested includes in settings files.
            Remove extraneous lines.

      Mantas (3):
            Add INSTANCE_FOR_DYNACONF and --instance
            Remove mocker fixture
            Python 3.4 has different error message

      Matthias (1):
            Fix small typo in README.md

      Pete Savage (1):
            Fix exponential slow down when loader is run multiple times

      Raoul Snyman (1):
            Add environments into the path in Vault so that the same Vault server can be used for multiple environments

      mspinelli (2):
            fixed infinite recursion caused by copy()
            add tests for dynabox fix


1.2.1 (2019-03-11)
------------------
- Release version 1.2.1. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (9):
            Merge branch 'jperras-merge-multiple-settings-files'
            Merge branch 'master' of github.com:rochacbruno/dynaconf
            Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths
            Update dynaconf/utils/boxing.py
            Update dynaconf/utils/boxing.py
            Add release script and CHANGELOG in place of history.
            Release version 1.2.0
            Tox is now part of pre-publish command
            Drop Python 3.4

      Byungjin Park (1):
            Fix typo

      Jaepil Koh (1):
            Update django.md

      Joel Perras (3):
            Allow dotted-path based setting of configuration key/value pairs.
            Handle nested includes in settings files.
            Remove extraneous lines.

      Mantas (3):
            Add INSTANCE_FOR_DYNACONF and --instance
            Remove mocker fixture
            Python 3.4 has different error message

      Matthias (1):
            Fix small typo in README.md

      Pete Savage (1):
            Fix exponential slow down when loader is run multiple times

      Raoul Snyman (1):
            Add environments into the path in Vault so that the same Vault server can be used for multiple environments

      mspinelli (2):
            fixed infinite recursion caused by copy()
            add tests for dynabox fix
- Fix exponential slow down when loader is run multiple times. [Pete
  Savage]

  * When using context managers, the loader is invoked each time.
    This was slowing down in an exponential manner each time the it was run.
    The eventual cause of this was down to an attribute being used as a list.
    The object merge dutifully tried to expand this item out again and again
    even in the case that the list was a single item, resulting in [item],
    becoming [item, item]. The next time the merge was run, this process was
    run again, but for each item in the list. In this particular instance
    the list was identical, it meant that the list grew exponentially.
  * This fix is a short optimization that checks to see if the old list
    is identical to the new list. In which case, there is no merge to complete
    so we simply return.
- Add environments into the path in Vault so that the same Vault server
  can be used for multiple environments. [Raoul Snyman]
- Fix typo. [Byungjin Park]
- Drop Python 3.4. [Bruno Rocha]
- Tox is now part of pre-publish command. [Bruno Rocha]
- Release version 1.2.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (6):
            Merge branch 'jperras-merge-multiple-settings-files'
            Merge branch 'master' of github.com:rochacbruno/dynaconf
            Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths
            Update dynaconf/utils/boxing.py
            Update dynaconf/utils/boxing.py
            Add release script and CHANGELOG in place of history.

      Jaepil Koh (1):
            Update django.md

      Joel Perras (3):
            Allow dotted-path based setting of configuration key/value pairs.
            Handle nested includes in settings files.
            Remove extraneous lines.

      Mantas (3):
            Add INSTANCE_FOR_DYNACONF and --instance
            Remove mocker fixture
            Python 3.4 has different error message

      Matthias (1):
            Fix small typo in README.md

      mspinelli (2):
            fixed infinite recursion caused by copy()
            add tests for dynabox fix


1.2.0 (2018-11-30)
------------------
- Release version 1.2.0. [Bruno Rocha]

  Shortlog of commits since last release:

      Bruno Rocha (6):
            Merge branch 'jperras-merge-multiple-settings-files'
            Merge branch 'master' of github.com:rochacbruno/dynaconf
            Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths
            Update dynaconf/utils/boxing.py
            Update dynaconf/utils/boxing.py
            Add release script and CHANGELOG in place of history.

      Jaepil Koh (1):
            Update django.md

      Joel Perras (3):
            Allow dotted-path based setting of configuration key/value pairs.
            Handle nested includes in settings files.
            Remove extraneous lines.

      Mantas (3):
            Add INSTANCE_FOR_DYNACONF and --instance
            Remove mocker fixture
            Python 3.4 has different error message

      Matthias (1):
            Fix small typo in README.md

      mspinelli (2):
            fixed infinite recursion caused by copy()
            add tests for dynabox fix
- Add release script and CHANGELOG in place of history. [Bruno Rocha]
- Add tests for dynabox fix. [mspinelli]
- Update dynaconf/utils/boxing.py. [Bruno Rocha, mspinelli]
- Update dynaconf/utils/boxing.py. [Bruno Rocha, mspinelli]
- Fixed infinite recursion caused by copy() [mspinelli]
- Fix #106 make PROJECT_ROOT_FOR_DYNACONF to work with custom paths.
  [Bruno Rocha]

  Added example/project_root and entry on Makefile:test_examples
- Update django.md. [Jaepil Koh]

  Typo!
- Fix small typo in README.md. [Matthias]
- Merge branch 'master' of github.com:rochacbruno/dynaconf. [Bruno
  Rocha]
- Python 3.4 has different error message. [Mantas]
- Remove mocker fixture. [Mantas]

  Left this accidentaly.

  https://travis-ci.org/rochacbruno/dynaconf/jobs/452612532
- Add INSTANCE_FOR_DYNACONF and --instance. [Mantas]

  There parameters allows dynaconf to use different LazySettings instance
  if project uses one.

  Also did some other fixes along the way:

  - Added `catch_exceptions=False` to `CliRunner.invoke` in order to
    prevent click from swallowing errors silently. This uncovered other
    errors in init and validate cli commands.

  - Removed module level code execution from cli module. Module level code
    execution makes it really difficult to test code. Now cli does not
    rely on global state and can be tested properly.

  - Removed a code snipper from LazySettings which modified global
    default_settings values. This means, that each LazySettings
    constructor call has side effects.

  - `dynaconf validate` command tests were useless because they didn't
    test anything and I found, that `dynaconf validate` command don't even
    work and raises ValidationError if there are any validation errors.
    Changed that to cli friendly error message.
- Merge branch 'jperras-merge-multiple-settings-files' [Bruno Rocha]
- Remove extraneous lines. [Joel Perras]
- Handle nested includes in settings files. [Joel Perras]

  A settings file can include a `dynaconf_include` stanza, whose exact
  syntax will depend on the type of settings file (json, yaml, toml, etc)
  being used:

  ```toml
  [default]
  dynaconf_include = ["/absolute/path/to/plugin1.toml", "relative/path/to/plugin2.toml"]
  DEBUG = false
  SERVER = "www.example.com"
  ```

  When loaded, the files located at the (relative or absolute) paths in
  the `dynaconf_include` key will be parsed, in order, and override any
  base settings that may exist in your current configuration.

  The paths can be relative to the base `settings.(toml|yaml|json|ini|py)`
  file, or can be absolute paths.

  The idea here is that plugins or extensions for whatever framework or
  architecture you are using can provide their own configuration values
  when necessary.

  It is also possible to specify glob-based patterns:

  ```toml
  [default]
  dynaconf_include = ["configurations/*.toml"]
  DEBUG = false
  SERVER = "www.example.com"
  ```

  Currently, only a single level of includes is permitted to keep things
  simple and straightforward.
- Allow dotted-path based setting of configuration key/value pairs.
  [Joel Perras]

  You can set a value with an arbitrary number of nested keys, separated
  by dots:

  ```python
  settings.set('nested_1.nested_2.nested_3.nested_4', 'secret')
  ```

  And accessing the keys/values with dotted-path lookup behaves as
  expected:

  ```python
  print(settings.NESTED_1.NESTED_2.NESTED_3.to_dict())
  ```

  If for some reason you didn't want to have a key parsed into nested
  structures delimited by dots and just wanted a key of "foo.bar", you can
  disable the parsing with:

  ```python
  settings.set('nested_1.nested_2.nested_3.nested_4',
               'secret',
               dotted_lookup=False)
  ```

  And accessing keys that don't exist will raise `KeyError`:

  ```python
  settings.NESTED_1.NESTED_5
  ```


1.1.0 (2018-10-26)
------------------
- Released 1.1.0. [Bruno Rocha]

  - Added `MERGE_ENABLED_FOR_DYNACONF` with ability to merge nested dictionaries instead of replacing PR #88
  - Support for dot notation to access nested dictionaries like `settings['KEY.OTHER.NESTED.DEEPER']` PR #93
  - Support dotted notation for validators PR #98
  - Fixed a bug in SETTINGS_MODULE cleanup when `.setenv` method was called PR #97
  - Added Python 3.7 to test matrix PR #99
- Fixing new flake8 warnings. [Bruno Rocha]
- Update py.test command in tox to allow passing positional arguments.
  [Joel Perras]

  The basic, default functionality of running `tox` remains unchanged. You
  are now, however, able to pass positional arguments to `py.test` at
  invocation time. For example:

  ```bash
  tox -- -x --pdb tests/test_basic.py
  ```

  Which will pass all input after the `--` separator (which is used to
  signify the end of possible options to `tox`) down to the `py.test`
  command in the `{posargs}` location, as defined in `tox.ini`.
- Enable Python 3.7 env for tox testing. [Joel Perras]
- Enable python 3.7 in TravisCI config. [Joel Perras]
- Updates Missing singleton with __eq__ dunder. (#98) [Joël Perras]

  Adds some additional tests for the `Missing` class and singleton
  instance usage to ensure it returns equality only for comparisons to
  itself and not `None`, or `False`, or `True`.
- Merge branch 'jperras-dotted-validators' [Bruno Rocha]
- Updates Missing singleton with __eq__ dunder. [Joel Perras]

  Adds some additional tests for the `Missing` class and singleton
  instance usage to ensure it returns equality only for comparisons to
  itself and not `None`, or `False`, or `True`.
- Implements dotted-path validator name declarations. [Joel Perras]

  One is now able to write:

  ```python
  settings.validators.register(
      Validator('REDIS',  must_exist=True,  is_type_of=dict),
      Validator('REDIS.HOST', must_exist=True, is_type_of=str),
      Validator('REDIS.PORT', must_exist=True, is_type_of=int),
  )
  ```

  Which will validate the dotted attributes as nested structures. For
  example, in yaml:

  ```yaml
  DEFAULT:
      REDIS:
          HOST: localhost
          PORT: 1234
  ```

  This necessitated a slight but non-negligible change in the
  implementation of `Settings.exists()`, which previously did a shallow
  check of loaded data. It has now been updated to perform a
  `Settings.get()` of the key in question, and compares that to a newly
  defined sentinel value to ensure `None` values do not cause a false
  negative result.

  New tests and assertions have been added to cover the new functionality.
  Docs have been updated to show an example of the nested validator name
  definition in action.

  Closes rochacbruno/dynaconf#85.
- Fix #94 setenv cleans SETTINGS_MODULE attribute. [Bruno Rocha]
- Merge branch 'jperras-dot-traversal-access' [Bruno Rocha]
- Merge branch 'dot-traversal-access' of
  https://github.com/jperras/dynaconf into jperras-dot-traversal-access.
  [Bruno Rocha]
- Allow dot-traversal access to nested dictionaries. [Joel Perras]

  A simple memoized recursion has been added to `get()` if the key
  contains at least one dot.

  The caller can choose to opt-out of this behaviour by specifying the
  `dotted_lookup` argument:

  ```python
  settings('AUTH.USERNAME', dotted_lookup=False)
  ```

  While the performance impact of this has not been quantified, the net
  impact in any real-world application should be minimal due to typical
  nesting levels, and the fact that we overwrite the memoized portion of
  the dotted-key lookup on each iteration.

  - Avoids regressions [✓]
  - Can be opted-out on a per-call basis [✓]
  - Minimal performance impact [✓]
  - Documented [✓]
  - Tested [✓]
  - Examples added [✓]

  Closes rochacbruno/dynaconf#84
- Merge branch 'rsnyman-merge-settings' [Bruno Rocha]
- Add example for merge_configs. [Bruno Rocha]
- Add setting merging. [Raoul Snyman]

  - Addd the ability to merge nested structures instead of completely overwriting them
  - Use monkeypatch to stop one test from interferring with another
  - Updated documentation


1.0.6 (2018-09-13)
------------------
- Release 1.0.6. [Bruno Rocha]

  Fixed issue #81 -  added ENCODING_FOR_DYNACONF to handle different settings files encodings specially on Windows
- Add ENCODING_FOR_DYNACONF to handle different file encoding Fix #81.
  [Bruno Rocha]

  By default ENCODING_FOR_DYNACONF is utf-8 (recommended to always write settings files in utf-8)
  If you need to change the format of settings file set the variable:

  ```
  export ENCODING_FOR_DYNACONF="cp1252"
  ```


1.0.5 (2018-09-07)
------------------
- Bump dev version. [Bruno Rocha]
- Added few more enhancements to django and flask extensions + docs.
  [Bruno Rocha]
- Bump dev version. [Bruno Rocha]


1.0.4 (2018-09-07)
------------------
- Fix the definition of Django prefixed variable. [Bruno Rocha]
- Merge pull request #78 from mattkatz/patch-1. [Bruno Rocha]

  small corrections for usage.md
- Small corrections for usage.md. [Matt Katz]

  This library is great, just a correction in the docs.

  There must be AT LEAST one default section.

  Changed **ATTENTION** to **ATTENTION**: to match with the style of **NOTE:**
- Merge pull request #75 from yoyonel/master. [Bruno Rocha]

  Fix in 'dynaconf/base.py' for __getitem__ method
- Bump version. [latty]
- [Fix] in 'dynaconf/base.py' for __getitem__ method, change (fix) the
  condition to raise a exception. Update unit tests. Bump version.
  [latty]
- Release 1.0.3. [Bruno Rocha]

  - Excluded example and tests from realease dist
  - removed root logger configuration


1.0.3 (2018-06-26)
------------------
- Merge pull request #72 from chobeat/issue_71. [Bruno Rocha]

  Removed root config
- Removed root config. [Simone Robutti]
- Merge pull request #70 from allan-silva/master. [Bruno Rocha]

  Exclude example and tests folders from setup (twitter help wanted)
- Exclude example and tests folders from setup (twitter help wanted)
  [allan.silva]
- Merge pull request #67 from cassiobotaro/patch-1. [Bruno Rocha]

  Incorrect help
- Fix docs. [cassiobotaro]
- Incorrect help. [Cássio Botaro]

  For while is impossible to use --to as argument.
- Merge pull request #66 from gpkc/patch-1. [Bruno Rocha]

  Fixing typos
- Merge pull request #1 from gpkc/patch-2. [Guilherme Caminha]

  Update README.md
- Update README.md. [Guilherme Caminha]
- Update usage.md. [Guilherme Caminha]
- Adjust logs to include python module names. [Bruno Rocha]
- Fix sphinx aafig syntax for python 3.x. [Bruno Rocha]


1.0.2 (2018-05-31)
------------------
- Merge pull request #65 from rochacbruno/testing_bare_install. [Bruno
  Rocha]

  Add install test stage
- Add -y. [Bruno Rocha]
- Add install test stage. [Bruno Rocha]
- Fix loader import error and improved logs. [Bruno Rocha]
- Clean up [skip ci] [Bruno Rocha]
- Fix URL generation in markdown for sphinx [skip ci] [Bruno Rocha]
- Merge pull request #64 from rochacbruno/improve_docs. [Bruno Rocha]

  Improved documentation
- Improved documentation. [Bruno Rocha]
- [skip ci] [Bruno Rocha]


1.0.1 (2018-05-30)
------------------
- Merge pull request #63 from rochacbruno/adds_more_python_versions.
  [Bruno Rocha]

  Adds more python versions
- Cover. [Bruno Rocha]
- Cover. [Bruno Rocha]
- Skip 3.7-dev. [Bruno Rocha]
- More trabis build stages. [Bruno Rocha]
- Add missing .env. [Bruno Rocha]
- Fix #60 CLI validator command. [Bruno Rocha]
- Fix #59 cli commands working for Flask and Django apps. [Bruno Rocha]
- Fixes to support Python 3.4, 3.5 and 3.6 Fix #62. [Bruno Rocha]
- Strict use of _FOR_DYNACONF envvars. [Bruno Rocha]
- Aafigure. [Bruno Rocha]
- Pinned docutils. [Bruno Rocha]
- Rtfd fix. [Bruno Rocha]
- Add rtfd yml. [Bruno Rocha]
- Added init file to docs. [Bruno Rocha]
- Add import path. [Bruno Rocha]
- Docs. [Bruno Rocha]
- Finished README with all the new implementations. [Bruno Rocha]


1.0.0 (2018-05-28)
------------------
- Merge pull request #56 from
  rochacbruno/all_the_namespace_changed_to_env. [Bruno Rocha]

  Major Breaking Refactor related to #54
- Travis fix 2. [Bruno Rocha]
- Travis global fix. [Bruno Rocha]
- Travis fix for new style toml envvars. [Bruno Rocha]
- Deprecated `@type` casting in favor of TOML syntax, rewriting readme.
  [Bruno Rocha]
- Add `settings.flag` [Bruno Rocha]
- Using `dynaconf write` in test_redis|vault. [Bruno Rocha]
- Added `dynaconf --docs` [Bruno Rocha]
- Added `dynaconf --version` [Bruno Rocha]
- Removed transformators. [Bruno Rocha]
- 100% coverage for validators. [Bruno Rocha]
- Increase cli test coverage. [Bruno Rocha]
- Dynaconf variables in blue and user variables in green. [Bruno Rocha]
- Added `dynaconf list` and `dynaconf write` subcommands. [Bruno Rocha]
- More cli commands lsit and write. [Bruno Rocha]
- Added more tests for cli and py loader. [Bruno Rocha]
- Replaced coveralls with codecov #57. [Bruno Rocha]
- Modularized the loaders, added `dynaconf init` command. [Bruno Rocha]
- As environment variable the only prefix allowed is the GLOBAL_ENV..
  default to DYNACONF_ [Bruno Rocha]
- Added more examples/tests and test_cli. [Bruno Rocha]
- Removed cleaners. [Bruno Rocha]
- Major Breaking Refactor related to #54. [Bruno Rocha]


0.7.6 (2018-05-21)
------------------
- Merge pull request #52 from rochacbruno/fix_namespace_in_django.
  [Bruno Rocha]

  Fix namespace swithc in django apps
- Add missing .env. [Bruno Rocha]
- Fix namespace swithc in django apps. [Bruno Rocha]


0.7.5 (2018-05-20)
------------------
- Merge pull request #51 from rochacbruno/added_django_extension. [Bruno
  Rocha]

  Added django extension
- 0.7.5 release with Django extension (experimental) [Bruno Rocha]
- Dont commit dbs. [Bruno Rocha]
- Added Django extension tests and example app. [Bruno Rocha]
- Added Django extension. [Bruno Rocha]


0.7.4 (2018-05-19)
------------------
- Merge pull request #50 from rochacbruno/074. [Bruno Rocha]

  Fix precedence of namespace in loaders
- Fix precedence of namespace in loaders. [Bruno Rocha]
- Merge pull request #49 from thekashifmalik/patch-1. [Bruno Rocha]

  Fix typo in README.
- Fix typo in README. [Kashif Malik]
- HOTFIX: redis config. [Bruno Rocha]
- Merge pull request #48 from rochacbruno/redis_tests. [Bruno Rocha]

  Added tests for Redis loader
- Added tests for Redis loader. [Bruno Rocha]
- Merge pull request #47 from rochacbruno/vault_tests. [Bruno Rocha]

  Added test for vaultproject
- Fix deadlock in vault writer. [Bruno Rocha]
- Added test for vaultproject. [Bruno Rocha]


0.7.3 (2018-05-13)
------------------
- Merge pull request #45 from rochacbruno/vault_loader. [Bruno Rocha]

  Added support for vaultproject (hashi corp) loader
- Added README section. [Bruno Rocha]
- Added note to readme. [Bruno Rocha]
- Added tests. [Bruno Rocha]
- Fixing for python-box 3.2.0. [Bruno Rocha]
- Added config AUTO_CAST_FOR_DYNACONF=off|0|disabled|false Suggested by
  @danilobellini. [Bruno Rocha]
- Fixed env variable for debug level in README.md. [Simone Robutti]
- Implementation of Vault loader. [Bruno Rocha]
- Vaultproject loader implementation. [Bruno Rocha]
- Merge pull request #46 from rochacbruno/disable_cast. [Bruno Rocha]

  Added config AUTO_CAST_FOR_DYNACONF=off|0|disabled|false
- Added note to readme. [Bruno Rocha]
- Added tests. [Bruno Rocha]
- Fixing for python-box 3.2.0. [Bruno Rocha]
- Added config AUTO_CAST_FOR_DYNACONF=off|0|disabled|false Suggested by
  @danilobellini. [Bruno Rocha]
- Merge pull request #44 from chobeat/patch-1. [Bruno Rocha]

  Fixed env variable for debug level in README.md
- Fixed env variable for debug level in README.md. [Simone Robutti]


0.7.2 (2018-05-07)
------------------
- Added test for compat. [Bruno Rocha]
- Added SETTINGS_MODULE to SETTINGS_MODULE_FOR_DYNACONF in compat.
  [Bruno Rocha]
- Added backwards compatibility for old style kwargs. [Bruno Rocha]
- Merge pull request #30 from vladcalin/add-docs. [Bruno Rocha]

  Add docs skeleton with autogenerated module docs
- Add docs skeleton with autogenerated module docs. [Vlad Calin]


0.7.0 (2018-05-07)
------------------
- README updates [ci skip] [Bruno Rocha]
- Added support for `.secrets` files. [Bruno Rocha]
- Merge pull request #43 from rochacbruno/test_coverage. [Bruno Rocha]

  Adjusting ENVVARS names and better test coverage
- Travis testing. [Bruno Rocha]
- Adjust travis.yml for muultiple jobs. [Bruno Rocha]
- Never cleans default keys. [Bruno Rocha]
- Refactoring for better test cov. [Bruno Rocha]
- Adjusting ENVVARS names and better test coverage. [Bruno Rocha]


0.6.0 (2018-05-04)
------------------
- Release of 0.6.0. [Bruno Rocha]
- Merge pull request #42 from rochacbruno/fix41. [Bruno Rocha]

  Fix #41
- Fix #41. [Bruno Rocha]
- Merge pull request #40 from rochacbruno/inifiles. [Bruno Rocha]

  ini and json files + parseconf recursive and find_file function
- Ini and json files + parseconf recursive and find_file function.
  [Bruno Rocha]

  - Added support for .ini and .json files
  - parse conf is now recursive to parse dict inner data
  - Cloned find_file function from dotenv
- Merge pull request #38 from rochacbruno/flask_dot_env. [Bruno Rocha]

  Added Flask 1.0 dotenv support
- IMplemented TOML loader. [Bruno Rocha]
- Adjusted MARKDOWN. [Bruno Rocha]
- Added Flask 1.0 dotenv support. [Bruno Rocha]


0.5.2 (2017-10-03)
------------------
- Small fix on 0.5.2 :hamster: [Bruno Rocha]
- 0.5.1 with YAML hotfixes and allowing multiple yaml files. [Bruno
  Rocha]


0.5.0 (2017-09-26)
------------------
- Drop 3.4 and 3.5. [Bruno Rocha]
- Silent errors on YAML missing namespace by default. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Merge branch 'Sytten-expand-yaml-config' [Bruno Rocha]
- Specialized Box as Dynabox to allow upper and lower case access.
  [Bruno Rocha]
- Use box. [Emile Fugulin]
- Add expanded object for yaml. [Emile Fugulin]


0.4.5 (2017-05-30)
------------------
- Update README.md. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Merge pull request #20 from douglas/master. [Bruno Rocha]

  Upgrade dynaconf to 0.4.5 =)
- Upgrade dynaconf to 0.4.5 =) [Douglas Soares de Andrade]
- Improves the way Tox installs the projects dependencies. [Douglas
  Soares de Andrade]
- Make tests directory a package. [Douglas Soares de Andrade]

  - So we can use the syntax from dynaconf import …
- Make it clear where we are getting LazySettings from. [Douglas Soares
  de Andrade]
- Add m2r and Flask to Pipenv. [Douglas Soares de Andrade]
- Removing pdbpp as it breaks with Python 3.3. [Douglas Soares de
  Andrade]
- Update readme. [Bruno Rocha]
- Update README. [Bruno Rocha]


0.4.4 (2017-03-21)
------------------
- HOTFIX: Flask templates always expects `None` for KeyError or
  AttrError. [Bruno Rocha]
- Bump version. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Added FlaskDynaconf to readme. [Bruno Rocha]
- Merge pull request #16 from rochacbruno/added_flaskdynaconf. [Bruno
  Rocha]

  Added FlaskDynaconf
- Added FlaskDynaconf. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Merge pull request #15 from douglas/master. [Bruno Rocha]

  Make the project work both on Python2 and Python3
- PEP8/Pylint and fixes equality operators. [Douglas Soares de Andrade]
- Remove unused code. [Douglas Soares de Andrade]
- PEP8 and Pylint fixes. [Douglas Soares de Andrade]
- Remove pypy3 as it does not work. [Douglas Soares de Andrade]
- Adding pypy and pypy3 to Travis. [Douglas Soares de Andrade]
- Oops, need to rename _super to super. [Douglas Soares de Andrade]
- Fix the import according to pep8. [Douglas Soares de Andrade]
- Remove this to see if it is still an issue. [Douglas Soares de
  Andrade]
- Adding Python 2.7. [Douglas Soares de Andrade]
- Adding the editorconfig file. [Douglas Soares de Andrade]
- Add Pipfile.lock to .gitignore. [Douglas Soares de Andrade]
- Small Refactory. [Douglas Soares de Andrade]

  - Adding object to the Settings classe to make it work with Python2
- Small Refactory. [Douglas Soares de Andrade]

  - Reordering the imports according to  pylint and flake8
  - Adding object to the classes to make them work with Python2
- Small Refactory. [Douglas Soares de Andrade]

  - Fixing the __init__ signature to make it compatible with python2 and
  python3
  - Adding object to the class to make Python2 work
- Adding the Pipenv file. [Douglas Soares de Andrade]

  - To allow us to use: https://github.com/kennethreitz/pipenv
- Adding Tox to helps us test the library. [Douglas Soares de Andrade]
- Fix #14 casting bool for booleans tks to @dbstraffin. [Bruno Rocha]
- Fix yaml cleaner, renamed `defined` to `must_exist` in validator.
  [Bruno Rocha]
- Added validators. [Bruno Rocha]


0.4.1 (2017-02-12)
------------------
- Bump 0.4.1. [Bruno Rocha]
- Merge pull request #13 from rochacbruno/add_yaml_support. [Bruno
  Rocha]

  Added YAML support
- Added YAML support. [Bruno Rocha]
- Force pip upgrade in travis. [Bruno Rocha]
- Drop support to Python 2.x - #MoveToPython3 Now! [Bruno Rocha]
- Add 'decode_responses': True note. [Bruno Rocha]
- Fix travis error. [Bruno Rocha]
- Python 3 support. [Bruno Rocha]
- Update README.md. [Bruno Rocha]


0.3.0 (2016-01-14)
------------------
- Fix error when envvar key has leading or trailing spaces. [Bruno
  Rocha]
- Pip released. [Bruno Rocha]
- Pypi is in troublr to release. [Bruno Rocha]
- Bump. [Bruno Rocha]
- If 'settings.py' is found on PROJECT_ROOT it is read. [Bruno Rocha]
- Make release. [Bruno Rocha]
- Path_for returns rooted path if starts with / [Bruno Rocha]
- Added settings.path_for. [Bruno Rocha]
- Ignore functional styling smells. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Travis envvars matrix. [Bruno Rocha]
- Update .travis.yml. [Bruno Rocha]
- Starting to write tests :) [Bruno Rocha]
- Simplified objects, removed UserSettings, removed exceptions. [Bruno
  Rocha]


0.2.7 (2015-12-23)
------------------
- Removed six and used obj.set. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Added png. [Bruno Rocha]
- Redis loader uses hash. [Bruno Rocha]
- Using HASH to store data, added always_fresh vars and context thanks
  to @dmoliveira and @ederfmartins. [Bruno Rocha]
- Added settings_module as cached property. [Bruno Rocha]
- Added delete function to redis_writer. [Bruno Rocha]
- Added note about get_fresh in readme. [Bruno Rocha]
- Better namespace management, get_fresh(key) to access redis. [Bruno
  Rocha]
- Now it can be used programatically. [Bruno Rocha]


0.2.1 (2015-12-20)
------------------
- Added redis_writer. [Bruno Rocha]
- Update readme. [Bruno Rocha]


0.2.0 (2015-12-20)
------------------
- Can also load from arbitraty filepath. [Bruno Rocha]
- Renamed var, added loaders, bump version. [Bruno Rocha]


0.1.2 (2015-08-20)
------------------
- Format on readme. [Bruno Rocha]
- More casting options. [Bruno Rocha]
- Fix #1 multiple namespaces. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Update README.md. [Bruno Rocha]
- Added default. [Bruno Rocha]
- Initial commit. [Bruno Rocha]
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
reported by contacting the project team at `rochacbruno [at] gmail [dot] com`. All
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

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

1. Ensure you read https://github.com/rochacbruno/dynaconf/issues/154
2. Also please read https://github.com/rochacbruno/dynaconf/issues/156

## Pull Request Process

1. Ensure your local environment is set.
   1. Clone your own fork of this repo
   2. Activate a python3.6+ virtualenv
   3. Code
2. Update the `docs/guides/` related to your changes.
3. Update `example/` (editing or adding a new one related to your changes)
4. Ensure tests are passing (see below `make all`)
   1. This project uses `pre-commit` and `Black` for code styling and adequacy tests.
5. Commit, Push and make a Pull Request!


### Common Workflow:

```bash
# clone your fork of this repo
git clone git@github.com:{$USER}/dynaconf.git

# Add the upstream remote
git remote add upstream https://github.com/rochacbruno/dynaconf.git

# Activate your Python Environment
python3.7 -m venv venv
source venv/bin/activate

# Install dynaconf for development
make all

# Checkout to a working branch
git checkout -b my_feature

# Open your favorite editor (VSCode for example)
code .

# After editing please rebase with upstream
git fetch upstream; git rebase upstream/master
# Fix any conflicts if any.

# Update docs/guides/ if needed
# Edit example/ if needed
# Create a new app in example/{your_example} and add it to Makefile.

# Then ensure everything is ok
make all

# Now commit your changes
git commit -am "Changed XPTO to fix #issue_number"

# Push to your own fork
git push -u origin HEAD

# Open github.com/rochacbruno/dynaconf and send a Pull Request.
```

### Run integration tests

* "make all" do not run integration tests for Redis and Vault.
* If you want to run integration tests, make sure you have docker installed

```bash

# To install docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
<output truncated>

# To permit your user run docker commands without sudo
sudo usermod -aG docker {$USER}

# Run complete integration tests
make test_integration

# or Run functional example tests individually
make test_redis
make test_vault

```

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

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

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at `rochacbruno [at] gmail [dot] com`. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
The MIT License (MIT)

Copyright (c) 2015 Bruno Rocha

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
[![Dynaconf](https://raw.githubusercontent.com/rochacbruno/dynaconf/master/docs/_static/logo_big.svg?sanitize=true)](http://dynaconf.readthedocs.io)

> **dynaconf** - The **dyna**mic **conf**igurator for your Python Project

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE) [![PyPI](https://img.shields.io/pypi/v/dynaconf.svg)](https://pypi.python.org/pypi/dynaconf) [![PyPI](https://img.shields.io/pypi/pyversions/dynaconf.svg)]() ![PyPI - Downloads](https://img.shields.io/pypi/dm/dynaconf.svg?label=pip%20installs&logo=python) [![Build Status](https://dev.azure.com/rochacbruno/dynaconf/_apis/build/status/rochacbruno.dynaconf?branchName=master)](https://dev.azure.com/rochacbruno/dynaconf/_build/latest?definitionId=1&branchName=master) ![Azure DevOps builds (branch)](https://img.shields.io/azure-devops/build/rochacbruno/3e08a9d6-ea7f-43d7-9584-96152e542071/1/master.svg?label=windows%20build&logo=windows) ![Azure DevOps builds (branch)](https://img.shields.io/azure-devops/build/rochacbruno/3e08a9d6-ea7f-43d7-9584-96152e542071/1/master.svg?label=linux%20build&logo=linux) [![codecov](https://codecov.io/gh/rochacbruno/dynaconf/branch/master/graph/badge.svg)](https://codecov.io/gh/rochacbruno/dynaconf) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5074f5d870a24ddea79def463453545b)](https://www.codacy.com/app/rochacbruno/dynaconf?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rochacbruno/dynaconf&amp;utm_campaign=Badge_Grade) ![GitHub issues](https://img.shields.io/github/issues/rochacbruno/dynaconf.svg) ![GitHub stars](https://img.shields.io/github/stars/rochacbruno/dynaconf.svg) ![GitHub Release Date](https://img.shields.io/github/release-date/rochacbruno/dynaconf.svg) ![GitHub commits since latest release](https://img.shields.io/github/commits-since/rochacbruno/dynaconf/latest.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/rochacbruno/dynaconf.svg) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)

**dynaconf** a layered configuration system for Python applications -
with strong support for [12-factor applications](https://12factor.net/config)
and extensions for **Flask** and **Django**.

**Read the Full Documentation at**: http://dynaconf.readthedocs.io/


# Top Contributors

[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/0)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/0)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/1)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/1)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/2)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/2)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/3)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/3)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/4)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/4)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/5)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/5)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/6)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/6)[![](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/images/7)](https://sourcerer.io/fame/rochacbruno/rochacbruno/dynaconf/links/7)

# Features

- Strict separation of settings from code (following [12-factor applications](https://12factor.net/config) Guide).
- Define comprehensive default values.
- Store parameters in multiple file formats (**.toml**, .json, .yaml, .ini and .py).
- Sensitive **secrets** like tokens and passwords can be stored in safe places like `.secrets` file or `vault server`.
- Parameters can optionally be stored in external services like Redis server.
- Simple **feature flag** system.
- Layered **[environment]** system.
- Environment variables can be used to override parameters.
- Support for `.env` files to automate the export of environment variables.
- Correct data types (even for environment variables).
- Have **only one** canonical settings module to rule all your instances.
- Drop in extension for **Flask** `app.config` object.
- Drop in extension for **Django** `conf.settings` object.
- Powerful **$ dynaconf** CLI to help you manage your settings via console.
- Customizable **Validation** System to ensure correct config parameters.
- Allow the change of **dyna**mic parameters on the fly without the need to redeploy your application.

## Read the docs

**Documentation**: http://dynaconf.readthedocs.io/

```
██████╗ ██╗   ██╗███╗   ██╗ █████╗  ██████╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗╚██╗ ██╔╝████╗  ██║██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔════╝
██║  ██║ ╚████╔╝ ██╔██╗ ██║███████║██║     ██║   ██║██╔██╗ ██║█████╗
██║  ██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║     ██║   ██║██║╚██╗██║██╔══╝
██████╔╝   ██║   ██║ ╚████║██║  ██║╚██████╗╚██████╔╝██║ ╚████║██║
╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝
```
# base
redis
wheel
twine
PyYAML
flask>=1.0
setuptools>=38.6.0
configobj
hvac
django
gitchangelog

python-box<4.0.0
python-dotenv<=0.10.3
toml<=0.10.0
click<=7.0

# testing
codecov
pytest
pytest-cov
pytest-mock
commentjson
docker-compose
lovely-pytest-docker

# style check
flake8
pep8-naming
flake8-debugger
flake8-print
flake8-todo
radon
pre-commit

# tools
ipython
ipdb

# documentation
sphinx
recommonmark
docutils>=0.14
aafigure>=0.6

# editable dynaconf
--editable .
---
name: Bug report
about: Create a report to help us improve
title: "[bug]"
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Having the following folder structure

<!-- Describe or use the command `$ tree -v` and paste below -->

<details>
<summary> Project structure </summary>

```bash

# /path/
# ...../folder/...
# please provide your folder structure here

```
</details>

2. Having the following config files:

<!-- Please adjust if you are using different files and formats! -->

<details>
<summary> Config files </summary>

**/path/.env**
```bash
Your .env content here
```

and

**/path/settings.toml**
```toml
[default]
```

</details>

3. Having the following app code:

<details>
<summary> Code </summary>

**/path/src/app.py**
```python
from dynaconf import settings
...
```

</details>

4. Executing under the following environment

<details>
<summary> Execution </summary>

```bash
# other commands and details?
# virtualenv activation?

$ python /path/src/app.py
```

</details>

**Expected behavior**
A clear and concise description of what you expected to happen.

**Debug output**

<details>
<summary> Debug Output </summary>

```bash

export `DEBUG_LEVEL_FOR_DYNACONF=DEBUG` reproduce your problem and paste the output here

```

</details>

**Environment (please complete the following information):**
 - OS: [e.g. Linux/Fedora29, Windows/x.x.x, Linux/Ubuntu16.x]
 - Dynaconf Version [e.g. 2.0.0/source]
 - Frameworks in use (Flask, Django? versions..)

**Additional context**
Add any other context about the problem here.
---
name: Discussion
about: Discussions, questions, etc...
title: ''
labels: question
assignees: ''

---
---
name: Feature request
about: Suggest an idea for this project
title: "[RFC]"
labels: Not a Bug, RFC
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
# Accessing parameters

Dynaconf offers different ways to access settings parameters

Assuming the following `settings.toml` file

```ini
[default]
host = "server"
port = 5555
auth = {user="admin", passwd="1234"}
```

## As attributes (dot notation)

Using dot notation

```python
settings.HOST
```

> Raises: **AttributeError** if not defined

## As dictionary [item]

Using item access

```python
settings['PORT']
```

> Raises: **KeyError** if not defined

## Default values (get)

Using dict style get

```python
settings.get('TIMEOUT', 300)
```

> Returns the default (300) if not defined

Using dotted-path lookup

```python
settings.get('AUTH.USER', 'anonymous')
```

> Returns the default ('anonymous') if not defined

Explicitly disabling dotted-path lookup

```python
settings.get('AUTH.USER', dotted_lookup=False)
```

## Forcing type casting

```python
settings.as_int('PORT')
```

Available casts:

- as_int
- as_float
- as_bool
- as_json

## Boxed values

In Dynaconf values are Boxed, it means the dot notation can also be used to access dictionary members, example:

settings.toml

```ini
[default]
mysql = {host="server.com", port=3600, auth={user="admin", passwd=1234}}
```

You can now access

```python
from dynaconf import settings

connect(
    host=settings.MYSQL.host,
    port=settings.MYSQL.port,
    username=settings.MYSQL.auth.user,
    passwd=settings.MYSQL.auth.get('passwd'),
)
```

## Export settings as a Python dictionary

After exporting the settings to a python dictionary it is easy to use it to serialize as a JSON, YAML or any other format you may need.

### Programmatically

```py
from dynaconf import settings
settings.as_dict()  # a dict with only user defined values in current env
settings.as_dict(env='production')  # a dict with only user defined values in production env
settings.as_dict(internal=True)  # a dict with all values, user defined and dynaconf internal
```

### CLI (export to json)

from your project root folder (generally the same place where you have `.env` or from where you call your scripts.

```bash
dynaconf list -o path/to/file.json
dynaconf list -e production -o path/to/file.json
```
# Advanced Usage

Yeah **Dynamic** is part of the name of this library so you can do lots of things :)

## Customizing the settings object

Sometimes you want to override settings for your existing Package or Framework
lets say you have a **conf** module exposing a **config** object and used to do:

```python
from myprogram.conf import config
```

Now you want to use Dynaconf, open that `conf.py` or `conf/__init__.py` and do:

```python
# coding: utf-8
from dynaconf import LazySettings

config = LazySettings(ENVVAR_PREFIX_FOR_DYNACONF="MYPROGRAM")
```

Now you can use `export MYPROGRAM_FOO=bar` instead of `DYNACONF_FOO=bar`

## Module impersonation

In some cases you may need to impersonate your legacy `settings` module for example you already have a program that does.

```python
from myprogram import settings
```

and now you want to use dynaconf without the need to change your whole codebase.

Go to your `myprogram/settings.py` and apply the module impersonation.

```python
import sys
from dynaconf import LazySettings

sys.modules[__name__] = LazySettings()
```

the last line of above code will make the module to replace itself with a dynaconf instance in the first time it is imported.

## Switching working environments

You can switch between existing environments using:

- `from_env`: (**recommended**) Will create a new settings instance pointing to defined env.
- `setenv`: Will set the existing instance to defined env.
- `using_env`: Context manager that will have defined env only inside its scope.

### from_env

> **New in 2.1.0**

Return a new isolated settings object pointing to specified env.

Example of settings.toml::

```ini
[development]
message = 'This is in dev'
foo = 1
[other]
message = 'this is in other env'
bar = 2
```

Program::

```py
>>> from dynaconf import settings
>>> print(settings.MESSAGE)
'This is in dev'
>>> print(settings.FOO)
1
>>> print(settings.BAR)
AttributeError: settings object has no attribute 'BAR'
```

Then you can use `from_env`:

```py
>>> print(settings.from_env('other').MESSAGE)
'This is in other env'
>>> print(settings.from_env('other').BAR)
2
>>> print(settings.from_env('other').FOO)
AttributeError: settings object has no attribute 'FOO'
```

The existing `settings` object remains the same.

```py
>>> print(settings.MESSAGE)
'This is in dev'
```

You can assign new settings objects to different `envs` like:

```py
development_settings = settings.from_env('development')
other_settings = settings.from_env('other')
```

And you can choose if the variables from different `envs` will be chained and overridden in a sequence:

```py
all_settings = settings.from_env('development', keep=True).from_env('other', keep=True)

>>> print(all_settings.MESSAGE)
'This is in other env'
>>> print(all_settings.FOO)
1
>>> print(all_settings.BAR)
2
```

The variables from [development] are loaded keeping pre-loaded values, then the variables from [other] are loaded keeping pre-loaded from [development] and overriding it.

It is also possible to pass additional [configuration](configuration.html) variables to `from_env` method.

```py
new_settings = settings.from_env('production', keep=True, SETTINGS_FILE_FOR_DYNACONF='another_file_path.yaml')
```

Then the `new_settings` will inherit all the variables from existing env and also load the `another_file_path.yaml` production env.

### setenv

Will change `in_place` the `env` for the existing object.

```python
from dynaconf import settings

settings.setenv('other')
# now values comes from [other] section of config
assert settings.MESSAGE == 'This is in other env'

settings.setenv()
# now working env are back to previous
```

### using_env

Using context manager

```python
from dynaconf import settings

with settings.using_env('other'):
    # now values comes from [other] section of config
    assert settings.MESSAGE == 'This is in other env'

# existing settings back to normal after the context manager scope
assert settings.MESSAGE == 'This is in dev'
```

## Populating objects

> **New in 2.0.0**

You can use dynaconf values to populate Python objects (intances).

example:
```py
class Obj:
   ...
```

then you can do:

```py
from dynaconf import settings  # assume it has DEBUG=True and VALUE=42.1
obj = Obj()

settings.populate_obj(obj)

assert obj.DEBUG is True
assert obj.VALUE == 42.1

```

Also you can specify only some keys:

```py
from dynaconf import settings  # assume it has DEBUG=True and VALUE=42.1
obj = Obj()

settings.populate_obj(obj, keys=['DEBUG'])

assert obj.DEBUG is True  # ok

assert obj.VALUE == 42.1  # AttributeError

```

## Customizations

It is possible to customize how your project will load settings, example: You want your users to customize a settings file defined in `export PROJECTNAME_SETTINGS=/path/to/settings.toml` and you want environment variables to be loaded from `PROJECTNAME_VARNAME`


```python
ENVVAR_PREFIX_FOR_DYNACONF = "PROJECTNAME"
"""This defines which environment variable global prefix dynaconf will load
That means that `export PROJECTNAME_FOO=1` will be loaded to `duanconf.settings.FOO
On command line it is possible to check it with `dynaconf list -k foo`"""

ENV_SWITCHER_FOR_DYNACONF='PROJECTNAME_ENV'
"""By default it is DYNACONF_ENV, this is the envvar used to switch from development to production
but with this settings your users can do `export PROJECT_ENV=production` (new in 2.0.0)"""


ENVVAR_FOR_DYNACONF = "PROJECTNAME_SETTINGS"
"""This defines which path dynaconf will look to load config files
example: export PROJECTNAME_SETTINGS=/path/to/settings.toml and the format can be
.ini, .json, .yaml or .toml

e.g::

    export PROJECTNAME_SETTINGS=settings.toml
    [default]
    FOO = 1
    [development]
    FOO = 2
    [production]
    FOO = 3


OR::

    export PROJECTNAME_SETTINGS=settings.yaml
    default:
      foo: 1
    development:
      foo: 2
    production:
      foo: 3


It is also possible to pass a list of files::

    export PROJECTNAME_SETTINGS=settings.toml,other_settings.yaml,another.json

The variables will be cascaded in the defined order (last wins the precedence)
The environment variables wins precedence over all!
"""

# load dynaconf
settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF=ENVVAR_PREFIX_FOR_DYNACONF,
    ENVVAR_FOR_DYNACONF=ENVVAR_FOR_DYNACONF.
    ENV_SWITCHER_FOR_DYNACONF=ENV_SWITCHER_FOR_DYNACONF
)
```

Then the working environment can now be switched using `export PROJECTNAME_ENV=production`

## Exporting

You can generate a file with current configs by calling `dynaconf list -o /path/to/file.ext` see more in [cli](cli.html)

You can also do that programmatically with:

```py
from dynaconf import loaders
from dynaconf import settings
from dynaconf.utils.boxing import DynaBox

# generates a dict with all the keys for `development` env
data = settings.as_dict(env='development')

# writes to a file, the format is inferred by extension
# can be .yaml, .toml, .ini, .json, .py
loaders.write('/path/to/file.yaml', DynaBox(data).to_dict(), merge=False, env='development')
```


## Preloading files

> New in **2.2.0**

Useful for plugin based apps.

```py
from dynaconf import LazySettings

settings = LazySettings(
  PRELOAD_FOR_DYNACONF=["/path/*", "other/settings.toml"],                # <-- Loaded first
  SETTINGS_FILE_FOR_DYNACONF="/etc/foo/settings.py",                      # <-- Loaded second (the main file)
  INCLUDES_FOR_DYNACONF=["other.module.settings", "other/settings.yaml"]  # <-- Loaded at the end
)

```
# Alternatives

Dynaconf tries to define standard and good practices for config and aims to have flexibility and 100% of test coverage for Python 3.x.

Dynaconf implements the best parts of the alternatives below, to implement Dynaconf lots of configuration libraries have been tested and studied.

But if you are still looking for something different take a look at the following excellent alternatives.

- [Python Decouple](https://github.com/henriquebastos/python-decouple)
- [PrettyConf](https://github.com/osantana/prettyconf)
- [Profig](https://bitbucket.org/dhagrow/profig)
- [Everett](https://github.com/willkg/everett)
- [Configman](https://configman.readthedocs.io/en/latest/)
- [PyMLconf](https://pypi.org/project/pymlconf/)
- [AnyConfig](https://github.com/ssato/python-anyconfig)
- [Config](https://pypi.org/project/config/)
- [Conman](https://github.com/the-gigi/conman)
# The dynaconf CLI

The `$ dynaconf` cli provides some useful commands

> **IMPORTANT** if you are using [Flask Extension](flask.html) the env var `FLASK_APP` must be defined to use the CLI, and if using [Django Extension](django.html) the `DJANGO_SETTINGS_MODULE` must be defined.

## dynaconf --help

```
Usage: dynaconf [OPTIONS] COMMAND [ARGS]...

  Dynaconf - Command Line Interface

Options:
  --version  Show dynaconf version
  --docs     Open documentation in browser
  --banner   Show awesome banner
  -i, --instance TEXT  Custom instance of LazySettings
  --help     Show this message and exit.

Commands:
  init      Inits a dynaconf project By default it...
  list      Lists all defined config values
  write     Writes data to specific source
  validate  Validates based on dynaconf_validators.toml file
```

## dynaconf init

Use init to easily configure your application configuration, once dynaconf is installed go to the root directory of your application and run:

creates settings files in current directory

```
$ dynaconf init -v key=value -v foo=bar -s token=1234 -e production
```

The above command will create in the current directory

`settings.toml`

```ini
[default]
KEY = "default"
FOO = "default"

[production]
KEY = "value"
FOO = "bar"
```

also `.secrets.toml`

```ini
[default]
TOKEN = "default"

[production]
TOKEN = "1234"
```

The command will also create a `.env` setting the working environment to **[production]**

```bash
ENV_FOR_DYNACONF="PRODUCTION"
```

And will include the `.secrets.toml` in the `.gitignore`

```ini
# Ignore dynaconf secret files
.secrets.*
```

> For sensitive data in production is recommended using [Vault Server](sensitive_secrets.html)

```
Usage: dynaconf init [OPTIONS]

  Inits a dynaconf project By default it creates a settings.toml and a
  .secrets.toml for [default|development|staging|testing|production|global]
  envs.

  The format of the files can be changed passing --format=yaml|json|ini|py.

  This command must run on the project's root folder or you must pass
  --path=/myproject/root/folder.

  If you want to have a .env created with the ENV defined there e.g:
  `ENV_FOR_DYNACONF=production` just pass --env=production and then .env
  will also be created and the env defined to production.

Options:
  -f, --format [ini|toml|yaml|json|py|env]
  -p, --path TEXT                 defaults to current directory
  -e, --env TEXT                  Sets the working env in `.env` file
  -v, --vars TEXT                 extra values to write to settings file file
                                  e.g: `dynaconf init -v NAME=foo -v X=2
  -s, --secrets TEXT              secret key values to be written in .secrets
                                  e.g: `dynaconf init -s TOKEN=kdslmflds
  --wg / --no-wg
  -y
  --django TEXT
  --help                          Show this message and exit.

```

## dynaconf list

List all defined parameters and optionally export to a json file.

```
Usage: dynaconf list [OPTIONS]

  Lists all user defined config values and if `--all` is passed it also
  shows dynaconf internal variables.

Options:
  -e, --env TEXT     Filters the env to get the values
  -k, --key TEXT     Filters a single key
  -m, --more         Pagination more|less style
  -l, --loader TEXT  a loader identifier to filter e.g: toml|yaml
  -a, --all          show dynaconf internal settings?
  -o, --output FILE  Filepath to write the listed values as json
  --output-flat      Output file is flat (do not include [env] name)
  --help             Show this message and exit.
```

### Exporting current environment as a file

```bash
dynaconf list -o path/to/file.yaml
```

The above command will export all the items showed by `dynaconf list` to the desired format which is inferred by the `-o` file extension, supported formats `yaml, toml, ini, json, py`

When using `py` you may want a flat output (without being nested inside the env key)

```bash
dynaconf list -o path/to/file.py --output-flat
```

## dynaconf write

```
Usage: dynaconf write [OPTIONS] TO

  Writes data to specific source

Options:
  -v, --vars TEXT     key values to be written e.g: `dynaconf write toml
                      -e NAME=foo -e X=2
  -s, --secrets TEXT  secret key values to be written in .secrets e.g:
                      `dynaconf write toml -s TOKEN=kdslmflds -s X=2
  -p, --path TEXT     defaults to current directory/settings.{ext}
  -e, --env TEXT      env to write to defaults to DEVELOPMENT for files for
                      external sources like Redis and Vault it will be
                      DYNACONF or the value set in $ENVVAR_PREFIX_FOR_DYNACONF
  -y
  --help              Show this message and exit.
```

## dynaconf validate

> **NEW in 1.0.1**

Starting on version 1.0.1 it is possible to define validators in **TOML** file called **dynaconf_validators.toml** placed in the same fodler as your settings files.

`dynaconf_validators.toml` equivalent to program above

```ini
[default]

version = {must_exist=true}
name = {must_exist=true}
password = {must_exist=false}

  [default.age]
  must_exist = true
  lte = 30
  gte = 10

[production]
project = {eq="hello_world"}
```

Then to fire the validation use:

```
$ dynaconf validate
```

If validates it returns status 0 (success) and this command can be called in your CI/CD/Deploy jobs.

## dynaconf --version

returns dynaconf version

```
$ dynaconf --version
1.0.0
```

## dynaconf --docs

Opens Dynaconf documentation in browser


## dynaconf --banner

Prints this awesome ascii made banner in the console :)

```
$ dynaconf --banner

██████╗ ██╗   ██╗███╗   ██╗ █████╗  ██████╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗╚██╗ ██╔╝████╗  ██║██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔════╝
██║  ██║ ╚████╔╝ ██╔██╗ ██║███████║██║     ██║   ██║██╔██╗ ██║█████╗
██║  ██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║     ██║   ██║██║╚██╗██║██╔══╝
██████╔╝   ██║   ██║ ╚████║██║  ██║╚██████╗╚██████╔╝██║ ╚████║██║
╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝

Learn more at: http://github.com/rochacbruno/dynaconf
```
# Configuring Dynaconf

Dynaconf can be configured through variables suffixed with `_FOR_DYNACONF` those settings can be used to change various dynaconf defaults and behaviors.

Each config variable here can be exported to environment variables or wrote to `.env` file, example:

```bash
export DEBUG_LEVEL_FOR_DYNACONF=DEBUG
export ENV_FOR_DYNACONF=production
```

Or when using your own Dynaconf instance you can pass as parameters directly:

```py
from dynaconf import LazySettings
settings = LazySettings(
    DEBUG_LEVEL_FOR_DYNACONF='DEBUG',
    ENVVAR_PREFIX_FOR_DYNACONF='MYPROGRAM',
    ENVVAR_FOR_DYNACONF='MYPROGRAM_SETTINGS',
)
```

It can also be passed as parameters to extensions like `FlaskDynaconf` or set in the `DjangoDynaconf` on settings.py file.

## Configuration options

> NOTE: Append `_FOR_DYNACONF` when exporting these variables.

```eval_rst
.. csv-table::
    :header: "Variable", "Type", "Usage", "default", "example"
    :widths: 15, 15, 50, 30, 50
    :delim: |

    AUTO_CAST | bool | *@casting* like *@int* is parsed. | true | AUTO_CAST_FOR_DYNACONF=false
    COMMENTJSON_ENABLED | bool | Enable comments in json files. | false (req:*pip install commentjson*) | COMMENTJSON_ENABLED_FOR_DYNACONF=true
    CORE_LOADERS | list | A list of enabled core loaders. | [‘YAML’, ‘TOML’, ‘INI’, ‘JSON’, ‘PY’] | CORE_LOADERS_FOR_DYNACONF=’[“YAML”, “JSON”]’ or ‘[]’
    DEBUG_LEVEL | str | Upper case logging level. | NOTSET | DEBUG_LEVEL_FOR_DYNACONF=DEBUG
    DOTENV_OVERRIDE | bool | *.env* should override the exported envvars. | false | DOTENV_OVERRIDE_FOR_DYNACONF=true
    DOTENV_PATH | str | Defines where to look for *.env* file. | PROJECT_ROOT | DOTENV_PATH_FOR_DYNACONF=”/tmp/.env”
    ENCODING | str | Encoding to read settings files. | utf-8 | ENCODING_FOR_DYNACONF=”cp1252”
    ENV | str | Working environment. | “development” | ENV_FOR_DYNACONF=production
    *FORCE_ENV | str | Force the working environment | None | FORCE_ENV_FOR_DYNACONF=other
    ENV_SWITCHER | str | Variable used to change working env. | ENV_FOR_DYNACONF | ENV_SWITCHER_FOR_DYNACONF=MYPROGRAM_ENV
    ENVVAR | str | The envvar which holds the list of settings files. | ‘SETTINGS_FILE_FOR_DYNACONF’ | ENVVAR_FOR_DYNACONF=MYPROGRAM_SETTINGS
    ENVVAR_PREFIX | str | Prefix for exporting parameters as env vars. Example: If your program is called *MYPROGRAM* you may want users to use *MYPROGRAM_FOO=bar* instead of *DYNACONF_FOO=bar* on envvars. | “DYNACONF” | ENVVAR_PREFIX_FOR_DYNACONF=MYPROGRAM (loads MYPROGRAM_VAR) ENVVAR_PREFIX_FOR_DYNACONF=’’ (loads _VAR) ENVVAR_PREFIX_FOR_DYNACONF=false (loads VAR)
    FRESH_VARS | list | A list of vars to be re-loaded on every access. | [] | FRESH_VARS_FOR_DYNACONF=[“HOST”, “PORT”]
    INCLUDES | list | A list of paths or a glob to load can be a toml-like list, or sep by , or ; | [] | INCLUDES_FOR_DYNACONF=”[‘path1.ext’, ‘folder/*’]” INCLUDES_FOR_DYNACONF=”path1.toml;path2.toml” INCLUDES_FOR_DYNACONF=”path1.toml,path2.toml” INCLUDES_FOR_DYNACONF=”single_path.toml” INCLUDES_FOR_DYNACONF=”single_path/glob/.toml”
    INSTANCE **used only by** *$dynaconf** *cli*. | str | Custom instance of LazySettings Must be an importable Python module. | None | INSTANCE_FOR_DYNACONF=myapp.settings
    LOADERS | list | A list of enabled external loaders. |	[‘dynaconf.loaders.env_loader’] | LOADERS_FOR_DYNACONF=’[‘module.mycustomloader’, …]’
    MERGE_ENABLED | bool | A bool to activate the global merge feature | False | MERGE_ENABLED_FOR_DYNACONF=1
    NESTED_SEPARATOR | str | Separator for nested assignment like `export DYNACONF_DATABASES__NAME='foo'` | `__` double underline | NESTED_SEPARATOR_FOR_DYNACONF='___'
    PRELOAD | list | A list of paths or glob to be pre-loaded before main settings file. | [] | PRELOAD_FOR_DYNACONF="['path1.ext', 'folder/*']"
    REDIS_DB | int | Redis DB. | 0 | REDIS_DB_FOR_DYNACONF=1
    REDIS_ENABLED | bool | Redis loader is enabled. | false | REDIS_ENABLED_FOR_DYNACONF=true
    REDIS_HOST | str | Redis server address. | localhost | REDIS_HOST_FOR_DYNACONF=”localhost”
    REDIS_PORT | int | Redis port. | 6379 | REDIS_PORT_FOR_DYNACONF=8899
    ROOT_PATH | str | Directory to look for settings files. This path is the base to search for files defined in *SETTINGS_FILE*. Dynaconf will also search for files in a relative *config/* subfolder if exists. | *None*. If set Dynaconf will look this path first before it starts to search for file in the other locations. see: `<usage.html#the-settings-files>`_ | ROOT_PATH_FOR_DYNACONF=”/my/custom/absolute/path/”
    SECRETS | str | Path to aditional secrets file to be loaded. |	None | SECRETS_FOR_DYNACONF=/var/jenkins/settings_ci.toml
    SETTINGS_FILE | list, str | List of files to load. | List of all supportes files: *settings.{py,toml,yaml,ini,conf,json} .secrets.{py,toml,yaml,ini,conf,json}*. This var name can be replaced by: *ENVVAR_FOR_DYNACONF=MYPROGRAM_SETTINGS* | SETTINGS_FILE_FOR_DYNACONF=”myconfig.toml” SETTINGS_FILE_FOR_DYNACONF=”[‘conf.toml’,’settings.yaml’]” SETTINGS_FILE_FOR_DYNACONF=”conf.toml,settings.yaml” SETTINGS_FILE_FOR_DYNACONF=”conf.toml;settings.yaml” MYPROGRAM_SETTINGS=”conf.toml,settings.yaml”
    SILENT_ERRORS | bool | Loading errors should be silenced. | true | SILENT_ERRORS_FOR_DYNACONF=false
    SKIP_FILES | list | Files to skip/ignore if found on search tree. | [] | SKIP_FILES_FOR_DYNACONF=”[‘/absolute/path/to/file.ext’]”
    VAULT_ALLOW_REDIRECTS | bool | Vault allow redirects. | None | VAULT_ALLOW_REDIRECTS_FOR_DYNACONF=false
    VAULT_CERT | str | Vault cert/pem file path. | None | VAULT_CERT_FOR_DYNACONF=”~/.ssh/key.pem”
    VAULT_ENABLED | bool | Vault server is enabled. | false | VAULT_ENABLED_FOR_DYNACONF=true
    VAULT_HOST | str | Vault host. | localhost | VAULT_HOST_FOR_DYNACONF=”server”
    VAULT_PATH | str | Vault path to the configuration. | None | VAULT_PATH_FOR_DYNACONF=”secret_data”
    VAULT_PORT | str | Vault port. | 8200 | VAULT_PORT_FOR_DYNACONF=”2800”
    VAULT_PROXIES | dict | Vault proxies. | None | VAULT_PROXIES_FOR_DYNACONF={http=”http:/localhost:3128/”}
    VAULT_ROLE_ID | str | Vault Role ID. | None | VAULT_ROLE_ID_FOR_DYNACONF=”some-role-id”
    VAULT_SCHEME | str | Vault scheme. | http | VAULT_SCHEME_FOR_DYNACONF=”https”
    VAULT_SECRET_ID | str | Vault Secret ID. | None | VAULT_SECRET_ID_FOR_DYNACONF=”some-secret-id”
    VAULT_TIMEOUT | int | Vault timeout in seconds. | None | VAULT_TIMEOUT_FOR_DYNACONF=60
    VAULT_TOKEN | str | Vault token. | None | VAULT_TOKEN_FOR_DYNACONF=”myroot”
    VAULT_URL | str | Vault URL. | http:// localhost :8200 | VAULT_URL_FOR_DYNACONF=”http://server/8200”
    VAULT_VERIFY | bool | Vault should verify. | None | VAULT_VERIFY_FOR_DYNACONF=true
    YAML_LOADER | str | yaml method name {safe,full,unsafe}_load. | full_load | YAML_LOADER_FOR_DYNACONF=unsafe_load
```

## Internal use variables

- FORCE_ENV_FOR_DYNACONF:  This variable exists to support the `from_env` method, you are not encouraged to override it manually.

## Deprecated options

Some configuration options has been deprecated and replaced with a new name, we try to make it without breaking backwards compatibility with old version, but you may receive a warning if use:

- `PROJECT_ROOT` replaced by `ROOT_PATH_FOR_DYNACONF`
- `PROJECT_ROOT_FOR_DYNACONF` replaced by `ROOT_PATH_FOR_DYNACONF`
- `DYNACONF_NAMESPACE` replaced by `ENV_FOR_DYNACONF`
- `NAMESPACE_FOR_DYNACONF` replaced by `ENV_FOR_DYNACONF`
- `BASE_NAMESPACE_FOR_DYNACONF` replaced by `DEFAULT_ENV_FOR_DYNACONF`
- `DYNACONF_SETTINGS_MODULE` replaced by `SETTINGS_FILE_FOR_DYNACONF`
- `DYNACONF_SETTINGS` replaced by `SETTINGS_FILE_FOR_DYNACONF`
- `SETTINGS_MODULE` replaced by `SETTINGS_FILE_FOR_DYNACONF`
- `DYNACONF_SILENT_ERRORS` replaced by `SILENT_ERRORS_FOR_DYNACONF`
- `DYNACONF_ALWAYS_FRESH_VARS` replaced by `FRESH_VARS_FOR_DYNACONF`
- `GLOBAL_ENV_FOR_DYNACONF` replaced by `ENVVAR_PREFIX_FOR_DYNACONF`
- `SETTINGS_MODULE_FOR_DYNACONF` replaced by `SETTINGS_FILE_FOR_DYNACONF`

```eval_rst
.. autoclass:: dynaconf.default_settings
    :show-inheritance:
```
# How to contribute

In github [repository](https://github.com/rochacbruno/dynaconf/) issues and Pull Request are welcomed!

- New implementations
- Bug Fixes
- Bug reports
- More examples of use in /example folder
- Documentation
- Feedback as issues and comments or joining #dynaconf on freenode
- Donation to rochacbruno [at] gmail.com in PayPal
# Credits

- Dynaconf is inspired by `flask.config` and `django.conf.settings`
- Some ideas also taken from Rust `config` crate
- Environments definitions ideas taken from Rust `rocket` framework
# Django Extension

> **New in 2.0.0**

Dynaconf extensions for Django works by patching the `settings.py` file with dynaconf loading hooks, the change is done on a single file and then in your whole project every time you call `django.conf.settings` you will have access to `dynaconf` attributes and methods.

Ensure dynaconf is installed on your env `pip install dynaconf[yaml]`

## Initialize the extension

You can manually append at the bottom of your django project's `settings.py` the following code:

```python
# HERE STARTS DYNACONF EXTENSION LOAD (Keep at the very bottom of settings.py)
# Read more at https://dynaconf.readthedocs.io/en/latest/guides/django.html
import dynaconf  # noqa
settings = dynaconf.DjangoDynaconf(__name__)  # noqa
# HERE ENDS DYNACONF EXTENSION LOAD (No more code below this line)
```

Or **optionally** you can, on the same directory where your `manage.py` is located run:

```bash
export DJANGO_SETTINGS_MODULE=yourapp.settings
$ dynaconf init

# or passing the location of the settings file

$ dynaconf init --django yourapp/settings.py

```

Dynaconf will append its extension loading code to the bottom of your `yourapp/settings.py` file and will create `settings.toml` and `.secrets.toml` in the current folder (the same where `manage.py` is located).

> **TIP** Take a look at [example/django_example](https://github.com/rochacbruno/dynaconf/tree/master/example/django_example)

## Using `DJANGO_` environment variables

Then **django.conf.settings** will work as a `dynaconf.settings` instance and `DJANGO_` will be the global prefix to export environment variables.

Example:

```bash
export DJANGO_DEBUG=true     # django.conf.settings.DEBUG
export DJANGO_INTVALUE=1     # django.conf.settings['INTVALUE']
export DJANGO_HELLO="Hello"  # django.conf.settings.get('HELLO')
```

> **TIP**: If you dont want to use `DJANGO_` as prefix for envvars you can customize by passing a new name e.g: `dynaconf.DjangoDynaconf(__name__, ENVVAR_PREFIX_FOR_DYNACONF="FOO")` then `export FOO_DEBUG=true`

You can also set nested dictionary values, for example lets say you have a configuration like this:

`settings.py`

```py
...
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'module.foo.engine',
        'ARGS': {'timeout': 30}
    }
}
...
```

And  now you want to change the values of `ENGINE` to `other.module`, via environment variables you can use the format `${ENVVAR_PREFIX}_${VARIABLE}__${NESTED_ITEM}__${NESTED_ITEM}`

Each `__` (dunder, a.k.a *double underline*) denotes access to nested elements in a dictionary.

So:

```bash
export DYNACONF_DATABASES__default__ENGINE=other.module
```

will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module',
        'ARGS': {'timeout': 30}
    }
}
```

Read more on [environment variables](https://dynaconf.readthedocs.io/en/latest/guides/environment_variables.html#nested-keys-in-dictionaries-via-environment-variables)

## Settings files

You can also have settings files for your Django app, in the root directory (the same where `manage.py` is located) put your `settings.{yaml, toml, ini, json, py}` and `.secrets.{yaml, toml, ini, json, py}` files and then define your environments `[default]`, `[development]` and `[production]`.

> NOTE: **.yaml** is the recommended format for Django applications because it allows complex data structures in easy way, but feel free to choose any format you are familiar with.

To switch the working environment the `DJANGO_ENV` variable can be used, so `DJANGO_ENV=development` to work
in development mode or `DJANGO_ENV=production` to switch to production.

> **IMPORTANT**: To use `$ dynaconf` CLI the `DJANGO_SETTINGS_MODULE` environment variable must be defined.

IF you don't want to manually create your config files take a look at the [CLI](cli.html)

## Customizations

It is possible to customize how your django project will load settings, example: You want your users to customize a settings file defined in `export PROJECTNAME_SETTINGS=/path/to/settings.toml` and you want environment variables to be loaded from `PROJECTNAME_VARNAME`

Edit django `settings.py` and modify the dynaconf extension part:

from:

```python
# HERE STARTS DYNACONF EXTENSION LOAD
...
settings = dynaconf.DjangoDynaconf(__name__)
# HERE ENDS DYNACONF EXTENSION LOAD
```

to:

```python
# HERE STARTS DYNACONF EXTENSION LOAD
...
settings = dynaconf.DjangoDynaconf(
    __name__,
    ENVVAR_PREFIX_FOR_DYNACONF='PROJECTNAME',
    ENV_SWITCHER_FOR_DYNACONF='PROJECTNAME_ENV',
    SETTINGS_FILE_FOR_DYNACONF='/etc/projectname/settings.toml',
    ENVVAR_FOR_DYNACONF='PROJECTNAME_SETTINGS',
    INCLUDES_FOR_DYNACONF=['/etc/projectname/plugins/*'],
)
# HERE ENDS DYNACONF EXTENSION LOAD
```

 Variables on environment can be set/override using `PROJECTNAME_` prefix e.g: `export PROJECTNAME_DEBUG=true`.

Working environment can now be switched using `export PROJECTNAME_ENV=production` it defaults to `development`.

Your settings are now read from `/etc/projectname/settings.toml` (dynaconf will not perform search for all the settings formats). This settings location can be changed via envvar using `export PROJECTNAME_SETTINGS=/other/path/to/settings.py{yaml,toml,json,ini}`

You can have additional settings read from `/etc/projectname/plugins/*` any supoprted file from this folder will be loaded.

You can set more options, take a look on [configuration](configuration.html)

## Reading Settings on Standalone Scripts

> **NOTE**: The recommended way to create standalone scripts is by creating `management commands` inside your Django applications or pugins.

> **IMPORTANT** If you need that script to be out of your Django Application Scope, it is also possible and **if needed** you can use `settings.DYNACONF.configure()` instead of the common `settings.configure()` provided by Django.

### Examples:

Examples below assumes you have `DJANGO_SETTINGS_MODULE` environment variable set, either by `exporting` it to your env or by explicitly adding it to `os.environ` dictionary.

> **IMPORTANT**: If you call `settings.configure()` directly dynaconf will be disabled. As you have `DJANGO_SETTINGS_MODULE` exported you don't need to call it, but if you need please use: `settings.DYNACONF.configure()`.

#### Common case

/etc/my_script.py
```python
from django.conf import settings
print(settings.DATABASES)
```

#### Explicitly adding the setting module

/etc/my_script.py
```python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'foo.settings'

from django.conf import settings
print(settings.DATABASES)
```

#### When you need the `configure`

> Calling `DYNACONF.configure()` is needed when you want to access dynaconf special methods like `using_env`, `get`, `get_fresh` etc...

/etc/my_script.py
```python
from django.conf import settings
settings.DYNACONF.configure()
print(settings.get('DATABASES'))
```

#### Importing settings directly (recommended for the above case)

/etc/my_script.py
```python
from foo.settings import settings
print(settings.get('DATABASES'))
```

#### Importing settings via importlib

/etc/my_script.py
```python
import os
import importlib
settings = importlib.import_module(os.environ['DJANGO_SETTINGS_MODULE'])
print(settings.get('DATABASES'))
```

## Testing on Django

Django testing must work out of the box!

But in some cases when you `mock` stuff and need to add `environment variables` to `os.environ` on demand for test cases it may be needed to `reload` the `dynaconf`.

To do that write up on your test case setup part:

```py
import os
import importlib
from myapp import settings # NOTE: this uses your app module not django.conf

class TestCase(...):
    def setUp(self):
        os.environ['DJANGO_FOO'] = 'BAR'  # dynaconf should read it and set `settings.FOO`
        importlib.reload(settings)

    def test_foo(self):
        self.assertEqual(settings.FOO, 'BAR')
```

## Explicit mode

Some users have the preference to explicitly load each setting variable inside the `settings.py` and then let django manage it in the common way, it is possible.

> **NOTE** Doing this way misses the ability to use dynaconf methods like `using_env`, `get` etc on your django applications code, you can use it only inside settings.py

Dynaconf will be available only on `settings.py` scope, on the rest of your application settings is managed by Django normally.

`settings.py`
```py
import sys
from dynaconf import LazySettings

settings = LazySettings(**YOUR_OPTIONS_HERE)

DEBUG = settings.get('DEBUG', False)
DATABASES = settings.get('DATABASES', {
    'default': {
        'ENGINE': '...',
        'NAME': '...
    }
})
...

# At the end of your settings.py
settings.populate_obj(sys.modules[__name__], ignore=locals())
```

> **NOTE**: Starting in `2.1.1` the `ignore` argument will tell Dynaconf to not override variables that already exists in the current settings file, remove it if you want all the existing local variables to be overwritten by dynaconf.

You can still change env with `export DJANGO_ENV=production` and also can export variables lile `export DJANGO_DEBUG=true`

## Knowm Caveats

- If `settings.configure()` is called directly it disables Dynaconf, use `settings.DYNACONF.configure()`

## Deprecation note

On old dynaconf releases the solution was to add `dynaconf.contrib.django_dynaconf` to `INSTALLED_APPS` as the first item, this still works but has some limitations so it is not recommended anymore.
# Environment variables

## overloading parameters via env vars

All configuration parameters, including **custom** environments and [dynaconf configuration](configuration.html), can be overridden through environment variables.

To override the configuration parameter **{param}**, use an environment variable named **DYNACONF_{PARAM}**. For instance, to override the **"HOST"** configuration parameter, you can run your application with:

```bash
DYNACONF_HOST='otherhost.com' python yourapp.py
```

## .env files

If you don't want to declare the variables on every program call you can run `export DYNACONF_{PARAM}` in your shell or put the values in a `.env` file located in the same directory as your settings files (the root directory of your application or the same folder where your program script is located), variables in `.env` does not overrride existing environment variables.

> **IMPORTANT**: Dynaconf will search for a `.env` on the order explained [here](usage.html). So to avoid conflicts with existing `.env` in parent directories it is recommended to have a `.env` inside your project even if it is empty.

## Precedence and type casting

Environment variables take precedence over all other configuration sources: if the variable is set, it will be used as the value for the parameter even if parameter exists in `settings` files or in `.env`.

Variable values are parsed as if they were **TOML** syntax. As illustration, consider the following examples:

```ini
# Numbers
DYNACONF_INTEGER=42
DYNACONF_FLOAT=3.14

# Text
DYNACONF_STRING=Hello
DYNACONF_STRING="Hello"

# Booleans
DYNACONF_BOOL=true
DYNACONF_BOOL=false

# Use extra quotes to force a string from other type
DYNACONF_STRING="'42'"
DYNACONF_STRING="'true'"

# Arrays must be homogenous in toml syntax
DYNACONF_ARRAY=[1, 2, 3]
DYNACONF_ARRAY=[1.1, 2.2, 3.3]
DYNACONF_ARRAY=['a', 'b', 'c']

# Dictionaries
DYNACONF_DICT={key="abc",val=123}
```

```python
# toml syntax does not allow `None/null` values so use @none
DYNACONF_NONE='@none None'

# toml syntax does not allow mixed type arrays so use @json
DYNACONF_ARRAY='@json [42, 3.14, "hello", true, ["otherarray"], {"foo": "bar"}]'
```

> **NOTE**: Older versions of Dynaconf used the `@casting` prefixes for env vars like `export DYNACONF_INTEGER='@int 123'` still works but this casting is deprecated in favor of using TOML syntax described above. To disable the `@casting` do `export AUTO_CAST_FOR_DYNACONF=false`

## Merging new data to existing variables

### Nested keys in dictionaries via environment variables.

> **New in 2.1.0**
> 
> This is useful for `Django` settings.

Lets say you have a configuration like this:

`settings.py`

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'module.foo.engine',
        'ARGS': {'timeout': 30}
    }
}
```

And  now you want to change the values of `ENGINE` to `other.module`, via environment variables you can use the format `${ENVVAR_PREFIX}_${VARIABLE}__${NESTED_ITEM}__${NESTED_ITEM}`

Each `__` (dunder, a.k.a *double underline*) denotes access to nested elements in a dictionary.

So 

```py
DATABASES['default']['ENGINE'] = 'other.module'
```

Can be expressed as environment variables as:

```bash
export DYNACONF_DATABASES__default__ENGINE=other.module
```

> **NOTE**: if you are using Django extension then the prefix will be `DJANGO_` instead of `DYNACONF_` and the same if you are using `FLASK_` or a custom prefix if you have customized the `ENVVAR_PREFIX`.

This will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module',
        'ARGS': {'timeout': 30}
    }
}
```

> **IMPORTANT** lower case keys are respected only on *nix systems, unfortunately Windows environment variables are case insensitive and Python reads it as all upper cases, that means that if you are running on Windows the dictionary can have only upper case keys.

Now if you want to add a new item to `ARGS` key:

```bash
export DYNACONF_DATABASES__default__ARGS__retries=10
```

This will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module',
        'ARGS': {'timeout': 30, 'retries': 10}
    }
}
```

and you can also pass a `toml` like dictionary to be merged with existing `ARGS` key.

```bash
export DYNACONF_DATABASES__default__ARGS='{timeout=50, size=1}'
```

will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module',
        'ARGS': {'retries': 10, 'timeout': 50, 'size': 1}
    }
}
```

Now if you want to clean an existing nested attribute you can use the `@reset` token on exported env var.

```bash
export DYNACONF_DATABASES__default__ARGS='@reset {}'
```

This will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module',
        'ARGS': {}
    }
}
```

And also you can do a `@reset` followed by a re-assignment

> Dynaconf env vars are parsed using `toml` so the format for dictionaries is a bit different.

```bash
export DYNACONF_DATABASES__default__ARGS='@reset {timeout=90}'
```

This will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module',
        'ARGS': {'timeout': 90}
    }
}
```

And if in any case you need to completely remove that key from the dictionary:

```bash
export DYNACONF_DATABASES__default__ARGS='@del'
```

This will result in

```py
DATABASES = {
    'default': {
        'NAME': 'db',
        'ENGINE': 'other.module'
    }
}
```

### Using the `dynaconf_merge` mark on configuration files.

> **New in 2.0.0**

To merge exported variables there is the **dynaconf_merge** tokens, example:

Your main settings file (e.g `settings.toml`) has an existing `DATABASE` dict setting on `[default]` env.

Now you want to contribute to the same `DATABASE` key by adding new keys, so you can use `dynaconf_merge` at the end of your dict:

In specific `[envs]`

```cfg
[default]
database = {host="server.com", user="default"}

[development]
database = {user="dev_user", dynaconf_merge=true}
```

or

> New in **2.2.0**

```cfg
[default]
database = {host="server.com", user="default"}

[development.database]
dynaconf_merge = {user="dev_user"}
```

In an environment variable use `@merge` token:

> **New in 2.2.0**

```bash
# Toml formatted envvar
export DYNACONF_DATABASE='@merge {password=1234}'
```

or `dunder` (recommended)

```bash
# Toml formatted envvar
export DYNACONF_DATABASE__PASSWORD=1234
```

The end result will be on `[development]` env:

```python
settings.DATABASE == {'host': 'server.com', 'user': 'dev_user', 'password': 1234}
```

Read more in [Getting Started Guide](usage.html#merging-existing-values)

### The global prefix

The **DYNACONF_{param}** prefix is set by **ENVVAR_PREFIX_FOR_DYNACONF** and serves only to be used in environment variables to override config values.

This prefix itself can be changed to something more significant for your application, however we recommend keeping **DYNACONF_{param}** as your global env prefix.

Setting **ENVVAR_PREFIX_FOR_DYNACONF** to `false` will disable the prefix entirely and cause Dynaconf to load *all* environment variables. When providing `ENVVAR_PREFIX_FOR_DYNACONF` as parameter to **LazySettings** or **settings.configure**, make sure to give it a Python-native `False`:

```python
from dynaconf import LazySettings
settings = LazySettings(ENVVAR_PREFIX_FOR_DYNACONF=False)
```

> **NOTE**: See the [Configuring dynaconf](configuration.html) section in documentation to learn more on how to use `.env` variables to configure dynaconf behavior.
# Examples

## Supported file formats

### TOML

```cfg
[default]
DEBUG = true
SERVER = "flaskdynaconf.com"
PORT = 6666
MESSAGE = "Dynaconf works like a charm with Flask and TOML"
TEST_RULE = '/flask_with_toml'

[development]
DEBUG = true
SERVER = "dev.flaskdynaconf.com"

[production]
DEBUG = false
SERVER = "prod.flaskdynaconf.com"
```

### YAML

```yaml
default:
  DEBUG: true
  SERVER: flaskdynaconf.com
  PORT: 6666
  MESSAGE: Dynaconf works like a charm with Flask and YAML
  TEST_RULE: /flask_with_yaml
development:
  DEBUG: true
  SERVER: dev.flaskdynaconf.com
production:
  DEBUG: false
  SERVER: prod.flaskdynaconf.com
```

### INI

```ini
[default]
DEBUG = true
SERVER = "flaskdynaconf.com"
PORT = 6666
MESSAGE = "Dynaconf works like a charm with Flask and INI"
TEST_RULE = '/flask_with_ini'

[development]
DEBUG = true
SERVER = "dev.flaskdynaconf.com"

[production]
DEBUG = false
SERVER = "prod.flaskdynaconf.com"
```

### JSON

```json
{
  "default": {
    "DEBUG": true,
    "SERVER": "flaskdynaconf.com",
    "PORT": 6666,
    "MESSAGE": "Dynaconf works like a charm with Flask and JSON",
    "TEST_RULE": "/flask_with_json"
  },
  "development": {
    "DEBUG": true,
    "SERVER": "dev.flaskdynaconf.com"
  },
  "production": {
    "DEBUG": false,
    "SERVER": "prod.flaskdynaconf.com"
  }
}
```

### PY

In python fils the `environment` is set by prefixing the file names

`settings.py`

```python
DEBUG = True
SERVER = "flaskdynaconf.com"
PORT = 6666
MESSAGE = "Dynaconf works like a charm with Flask and .py"
TEST_RULE = '/flask_with_ini'
```

`development_settings.py`

```python
DEBUG = True 
SERVER = "dev.flaskdynaconf.com"
```

`production_settings.py`

```python
DEBUG = False 
SERVER = "prod.flaskdynaconf.com"
```

### .env

`.env` allows only the `global` environment (overrides everything)

```bash
DEBUG=true
SERVER="flaskdynaconf.com"
PORT=6666
MESSAGE="Dynaconf works like a charm with Flask and .env"
TEST_RULE='/flask_with_ini'
```

## Using a default main config file plus variable settings file

On the `.env`

```bash
export SETTINGS_FILE_FOR_DYNACONF="default.toml"
```

The default file

```ini
[default]
variable1 = 'value1'
```

Now having specific settings per environment

Use cases:

- plugin based apps
- user specific settings
- dev specific settings

On the **user1** environment

```bash
export INCLUDES_FOR_DYNACONF='/path/to/user1_specific_settings.toml'
```

On the **user2** environment

```bash
export INCLUDES_FOR_DYNACONF='/path/to/user2_specific_settings.toml'
```

It can be a glob

```bash
export INCLUDES_FOR_DYNACONF='/path/to/config/*.toml'
```

And also supports having a `;` or `,` separated list of paths or globs.

## More examples

Take a look at [example/](https://github.com/rochacbruno/dynaconf/tree/master/example) for more examples.
# Extending

## Creating new loaders

In your project i.e called `myprogram` create your custom loader.

`myprogram/my_custom_loader.py`

```python
def load(obj, env=None, silent=True, key=None, filename=None):
    """
    Reads and loads in to "obj" a single key or all keys from source
    :param obj: the settings instance
    :param env: settings current env (upper case) default='DEVELOPMENT'
    :param silent: if errors should raise
    :param key: if defined load a single key, else load all from `env`
    :param filename: Custom filename to load (useful for tests)
    :return: None
    """
    # Load data from your custom data source (file, database, memory etc)
    # use `obj.set(key, value)` or `obj.update(dict)` to load data
    # use `obj.logger.debug` to log your loader activities
    # use `obj.find_file('filename.ext')` to find the file in search tree
    # Return nothing
```

In the `.env` file or exporting the envvar define:

```bash
LOADERS_FOR_DYNACONF=['myprogram.my_custom_loader', 'dynaconf.loaders.env_loader']
```

Dynaconf will import your `myprogram.my_custom_loader.load` and call it.

> **IMPORTANT**: the `'dynaconf.loaders.env_loader'` must be the last in the loaders list
> if you want to keep the behavior of having envvars to override parameters.

In case you need to disable all external loaders and rely only the `settings.*` file loaders define:

```bash
LOADERS_FOR_DYNACONF=false
```

In case you need to disable all core loaders and rely only on external loaders:

```bash
CORE_LOADERS_FOR_DYNACONF='[]'  # a toml empty list
```

See [example/custom_loader](https://github.com/rochacbruno/dynaconf/tree/master/example/custom_loader)
# External storages

An external storage is needed in some programs for scenarios like:

1) Having a single storage for settings and distribute across multiple instances
2) The need to change settings on the fly without redeploying or restarting the app (see [Feature Flags](feature_flag.html))
3) Storing sensitive values in a safe sealed **Vault**

## Using REDIS

1. Run a Redis server installed or via docker:

```bash
$ docker run -d -p 6379:6379 redis
```

2. Install support for redis in dynaconf

```bash
$ pip install dynaconf[redis]
```

3. In your `.env` file or in exported environment variables define:

```bash
REDIS_ENABLED_FOR_DYNACONF=true
REDIS_HOST_FOR_DYNACONF=localhost
REDIS_PORT_FOR_DYNACONF=6379
```

You can now write variables direct in to a redis hash named `DYNACONF_< env >` for example:

- `DYNACONF_DEFAULT`: default values
- `DYNACONF_DEVELOPMENT`: loaded only when `ENV_FOR_DYNACONF=development` (default)
- `DYNACONF_PRODUCTION`: loaded only when `ENV_FOR_DYNACONF=production`
- `DYNACONF_CUSTOM`: loaded only when `ENV_FOR_DYNACONF=custom`

You can also use the redis writer

```bash
$ dynaconf write redis -v name=Bruno -v database=localhost -v port=1234
```

The above data will be recorded in redis as a hash:

```
DYNACONF_DEFAULT {
    NAME='Bruno'
    DATABASE='localhost'
    PORT='@int 1234'
}
```

If you want to write to specific `env` pass the `-e` option.

```bash
$ dynaconf write redis -v name=Bruno -v database=localhost -v port=1234 -e production
```

The above data will be recorded in redis as a hash:

```
DYNACONF_PRODUCTION {
    NAME='Bruno'
    DATABASE='localhost'
    PORT='@int 1234'
}
```

Then to access that values you can set `export ENV_FOR_DYNACONF=production` or directly via `settings.from_env('production').NAME`

> if you want to skip type casting, write as string intead of PORT=1234 use PORT="'1234'".

Data is read from redis and another loaders only once when `dynaconf.settings` is first accessed
or when `from_env`, `.setenv()` or `using_env()` are invoked.

You can access the fresh value using **settings.get_fresh(key)**

There is also the **fresh** context manager

```python
from dynaconf import settings

print(settings.FOO)  # this data was loaded once on import

with settings.fresh():
    print(settings.FOO)  # this data is being freshly reloaded from source

print(settings.get('FOO', fresh=True))  # this data is being freshly reloaded from source
```

And you can also force some variables to be **fresh** setting in your setting file

```python
FRESH_VARS_FOR_DYNACONF = ['MYSQL_HOST']
```

or using env vars

```bash
export FRESH_VARS_FOR_DYNACONF='["MYSQL_HOST", "OTHERVAR"]'
```

Then

```python
from dynaconf import settings

print(settings.FOO)         # This data was loaded once on import

print(settings.MYSQL_HOST)  # This data is being read from redis imediatelly!
```

## Using Hashicorp Vault to store secrets

Read more in [Using Vault Server section](sensitive_secrets.html)

## Custom Storages

Do you want to store settings in other databases like NoSQL, Relational Databases or other services?

Please see how to [extend dynaconf](extend.html) to add your custom loaders.
# Feature flag system

## feature toggles

Feature flagging is a system to dynamically toggle features in your
application based in some settings value.

The advantage of using it is to perform changes on the fly without the need to redeploy ou restart the application.

Learn more on how to design your program using Feature Flags: [http://martinfowler.com/articles/feature-toggles.html](http://martinfowler.com/articles/feature-toggles.html)

Example:

Lets say you have 2 versions of your app dashboard and you want to serve the new version only for premium users.

write flags to [redis](external_storages.html)

```
$ dynaconf write redis -s NEWDASHBOARD=true -e premiumuser
```

In your program do:

```python
usertype = 'premiumuser'  # assume you loaded it as part of your auth

# user has access to new dashboard?
if settings.flag('newdashboard', usertype):
    activate_new_dashboard()
else:
    # User will have old dashboard if not a premiumuser
    activate_old_dashboard()
```

The value is ensured to be loaded fresh from redis server so features can be enabled or
disabled at any time without the need to redeploy.

It also works with file settings but the recommended is redis
as the data can be loaded once it is updated.
# Flask Extension

Dynaconf provides a drop in replacement for `app.config`.

As Flask encourages the composition by overriding the `config_class` attribute this extension follows the [patterns of Flask](http://flask.pocoo.org/docs/0.12/patterns/subclassing/) and turns your Flask's `app.config` in to a `dynaconf` instance.

## Initialize the extension

Initialize the **FlaskDynaconf** extension in your `app`

```python
from flask import Flask
from dynaconf import FlaskDynaconf

app = Flask(__name__)
FlaskDynaconf(app)
```

> You can optionally use `init_app` as well.

## Use `FLASK_` environment variables

Then the `app.config` will work as a `dynaconf.settings` instance and `FLASK_` will be the global prefix for exporting environment variables.

Example:

```bash
export FLASK_DEBUG=true              # app.config.DEBUG
export FLASK_INTVALUE=1              # app.config['INTVALUE']
export FLASK_MAIL_SERVER='host.com'  # app.config.get('MAIL_SERVER')
```

## Settings files

You can also have settings files for your Flask app, in the root directory (the same where you execute `flask run`) put your `settings.toml` and `.secrets.toml` files and then define your environments `[default]`, `[development]` and `[production]`.

To switch the working environment the `FLASK_ENV` variable can be used, so `FLASK_ENV=development` to work
in development mode or `FLASK_ENV=production` to switch to production.

> **IMPORTANT**: To use `$ dynaconf` CLI the `FLASK_APP` must be defined.

IF you don't want to manually create your config files take a look at the [CLI](cli.html)

## Customizations

It is possible to customize how your Flask project will load settings, example: You want your users to customize a settings file defined in `export PROJECTNAME_SETTINGS=/path/to/settings.toml` and you want environment variables to be loaded from `PROJECTNAME_VARNAME`

your flask `app.py` (or wherever you setup dynaconf)

```python
ENVVAR_PREFIX_FOR_DYNACONF = "PROJECTNAME"
"""This defines which environment variable global prefix dynaconf will load
That means that `export PROJECTNAME_FOO=1` will be loaded to `app.config.FOO
On command line it is possible to check it with `dynaconf list -k foo`"""

ENVVAR_FOR_DYNACONF = "PROJECTNAME_SETTINGS"
"""This defines which path dynaconf will look to load config files
example: export PROJECTNAME_SETTINGS=/path/to/settings.toml and the format can be
.ini, .json, .yaml or .toml

e.g::

    export PROJECTNAME_SETTINGS=settings.toml
    [default]
    FOO = 1
    [development]
    FOO = 2
    [production]
    FOO = 3


OR::

    export PROJECTNAME_SETTINGS=settings.yaml
    default:
      foo: 1
    development:
      foo: 2
    production:
      foo: 3


It is also possible to pass a list of files::

    export PROJECTNAME_SETTINGS=settings.toml,other_settings.yaml,another.json

The variables will be cascaded in the defined order (last wins the precedence)
The environment variables wins precedence over all!
"""

# load dynaconf
app = Flask(__name__)
FlaskDynaconf(
    app,
    ENVVAR_PREFIX_FOR_DYNACONF=ENVVAR_PREFIX_FOR_DYNACONF,
    ENVVAR_FOR_DYNACONF=ENVVAR_FOR_DYNACONF
)
```

Then the working environment can now be switched using `export PROJECTNAME_ENV=production`
# Sensitive secrets

## Using .secrets files

To safely store sensitive data Dynaconf also searches for a `.secrets.{toml|py|json|ini|yaml}` file to look for data like tokens and passwords.

example `.secrets.toml`:

```ini
[default]
password = "sek@987342$"
```

The secrets file supports all the **environment** definitions supported in the **settings** file.

> **IMPORTANT**: The reason to use a `.secrets.*` file is the ability to omit this file when committing to the repository so a recommended `.gitignore` should include `.secrets.*` line.

## Using Vault server

The [vaultproject.io/](https://www.vaultproject.io/) is a key:value store for secrets and Dynaconf can load
variables from a Vault secret.

1. Run a vault server

Run a Vault server installed or via docker:

```bash
$ docker run -d -e 'VAULT_DEV_ROOT_TOKEN_ID=myroot' -p 8200:8200 vault
```

2. Install support for vault in dynaconf

```bash
$ pip install dynaconf[vault]
```

3. In your `.env` file or in exported environment variables define:

```bash
VAULT_ENABLED_FOR_DYNACONF=true
VAULT_URL_FOR_DYNACONF="http://localhost:8200"
VAULT_TOKEN_FOR_DYNACONF="myroot"
```

Now you can have keys like `PASSWORD` and `TOKEN` defined in the vault and
dynaconf will read it.

To write a new secret you can use http://localhost:8200 web admin and write keys
under the `/secret/dynaconf/< env >` secret database.

You can also use the Dynaconf writer via console:

```bash
# writes {'password': 123456} to secret/dynaconf/default
$ dynaconf write vault -s password=123456  

# writes {'password': 123456, 'username': 'admin'} to secret/dynaconf/default
$ dynaconf write vault -s password=123456 -s username=admin

# writes {'password': 555555} to secret/dynaconf/development
$ dynaconf write vault -s password=555555  -e development

# writes {'password': 777777, 'username': 'admin'} to secret/dynaconf/production
$ dynaconf write vault -s password=777777 -s username=produser -e production
```

then you can access values normally in your program

```py
from dynaconf import settings

settings.PASSWORD == 555555  # if ENV_FOR_DYNACONF is the default `development`
settings.USERNAME == 'admin'  # if ENV_FOR_DYNACONF is the default `development`

settings.PASSWORD == 777777  # if ENV_FOR_DYNACONF is `production`
settings.USERNAME == 'produser'  # if ENV_FOR_DYNACONF is `production`
```

You can also ask settings to be loaded from specific env with `from_env` method:

```py
settings.from_env('production').PASSWORD == 777777
settings.from_env('production').USERNAME == 'produser'
```

## Additional secrets file (for CI, jenkins etc.)

It is common to have an extra `secrets` file that is available only when running on specific CI environment like `Jenkins`, usually there will be an environment variable pointing to the file.

On Jenkins it is done on job settings by exporting the `secrets` information.

Dynaconf can handle this via `SECRETS_FOR_DYNACONF` environment variable.

ex:

```bash
export SECRETS_FOR_DYNACONF=/path/to/secrets.toml{json|py|ini|yaml}
```

If that variable exists in your environment then Dynaconf will also load it.
# Testing and mocking

For testing it is recommended to just switch to `testing` environment and read the same config files.

```
ENV_FOR_DYNACONF=testing python program.py
```

But it is common in unit tests to `mock` some objects and you may need in rare cases to mock the `dynaconf.settings` when running your tests.

```python
from dynaconf.utils import DynaconfDict
mocked_settings = DynaconfDict({'FOO': 'BAR'})
```

DynaconfDict is a dict like obj that can be populated from a file:

```python
from dynaconf.loaders import toml_loader
toml_loader.load(mocked_settings, filename='my_file.toml', env='testing')
```
# Getting Started

## Installation

> Python 3.x is required

```
$ pip install dynaconf
```

> Default installation supports .toml, .py and .json file formats and also environment variables (.env supported) - to support YAML add `pip install dynaconf[yaml]` or `pip install dynaconf[all]`

## Usage

### Accessing config variables in your Python application

In your Python program wherever you need to access a settings variable you use the canonical object `from dynaconf import settings`:

#### Example of program to connect to some database

```python
from some.db import Client

from dynaconf import settings

conn = Client(
    username=settings.USERNAME,             # attribute style access
    password=settings.get('PASSWORD'),      # dict get style access
    port=settings['PORT'],                  # dict item style access
    timeout=settings.as_int('TIMEOUT'),     # Forcing casting if needed
    host=settings.get('HOST', 'localhost')  # Providing defaults
)
```

### Understanding the settings

Dynaconf aims to have a flexible and usable configuration system. Your applications can be configured via a [**configuration files**](#the-settings-files), through [**environment variables**](environment_variables.html), or both. Configurations can be separated into environments: **[default], [development], [staging], [testing] and [production]**. The working environment is switched via an environment variable.

But this is all **optional** you can of course follow strictly the [12 factor app](https://12factor.net/config) guide, have your configuration coming only from environment variables and provide files only to store `[default]` values. (take also a look on how to add a [dynaconf validation](validation.html) file to your project).

**Sensitive data** like tokens, secret keys and password can be stored in `.secrets.*` files and/or [external storages](external_storages.html) like `Redis` or `vault` secrets server.

Besides the built-in optional support to **Redis** as settings storage dynaconf allows you to create [**Custom Loaders**](extend.html) and store the data wherever you want e.g: databases, memory storages, other file formats, nosql databases etc.

## Working environments

At any point in time, your application is operating in a given configuration environment. By default there are four such environments:

- [development] (selected by default)
- [staging]
- [testing]
- [production]
- [{custom}] <-- You can create named environments that you need

> There is also the pseudo-envs **[default]** to provide comprehensive default values and **[global]** to provide global values to override in any other environment.

Without any action, your applications by default run in the **[development]** environment. The environment can be changed via the `ENV_FOR_DYNACONF` environment variable. For example, to launch an application in the **[staging]** environment, we can run:

```bash
export ENV_FOR_DYNACONF=staging
```

or

```bash
ENV_FOR_DYNACONF=staging python yourapp.py
```

> **NOTE:** When using [Flask Extension](flask.html) the environment can be changed via `FLASK_ENV` variable and for [Django Extension](django.html) you can use `DJANGO_ENV`.

## The settings files

> **NOTE:** The settings files are optional. If it is not present, only the values from **environment variables** and enabled external loaders are used (**.env** file is also supported).

Dynaconf will search for the settings files defined in `SETTINGS_FILE_FOR_DYNACONF` which by default is a list containing combinations of **settings.{py|toml|json|ini|yaml}** and **.secrets.{py|toml|json|ini|yaml}**
and dynaconf will try to find each one of those combinations, optionally it is possible to configure it to a different set of files e.g: `export SETTINGS_FILE_FOR_DYNACONF='["myfilename.toml", "another.json"]'`, this value contains a list of relative or absolute paths, can be a toml-like list or a comma/semicolon separated string and can be exported to `envvars`, write to `.env` file or passed directly to Dynaconf instance.

> IMPORTANT: Dynaconf by default reads settings files using `utf-8` encoding, if you have settings files written in other encoding please set `ENCODING_FOR_DYNACONF` environment variable.

See more details in [configuration](configuration.html)

## Settings files location

To find the files defined in `SETTINGS_FILE_FOR_DYNACONF` the search will start at the path defined in `ROOT_PATH_FOR_DYNACONF` (if defined), then will recursively walk to its root and then will try the **folder where the called program is located** and then it will recursively try its parent directories **until the root parent is reached which can be File System `/` or the current working dir** then finally will try the **current working directory** as the last option.

> **NOTE**: If by any reason you need Dynaconf to first look at the current working dir you can customize the `ROOT_PATH_FOR_DYNACONF` via environment variable or by creating a [custom settings object](advanced_usage.html#customizing-the-settings-object)

Some people prefer to put settings in a sub-folder so for each of the paths it will also search in a relative folder called `config/`.

And for each file dynaconf will also try to load a `.local.` file, for example, if you have a `settings.toml` after loading it Dynaconf will also try to find a `settings.local.toml` if exists.

Dynaconf will stop searching on the first match for each file and if no file is found it will **fail silently** unless `SILENT_ERRORS_FOR_DYNACONF=false` is exported.

### Illustrative Example

> **New in 2.0.0**

If your program has the following structure:

```text
|_ myprogram/
   |_ src/
      |_ app.py
         # from dynaconf import settings
         # print(settings.NAME)
         # print(settings.PASSWORD)
         # print(settings.FOO)
   |_ config
      |_ settings.toml
         # [default]
         # name = "Jon Doe"
   |_ settings.local.toml
      # [default]
      # name = "Oscar Wilde"
   |_ .env
      # DYNACONF_FOO='BAR'
   |_ .secrets.toml
      # [default]
      # password = "Utopi@"
```

And you call it from `myprogram` working dir.

```bash
cd myprogram
python src/app.py
```

What happens is:

> NOTE: The behavior explained here is valid only for the above file structure, other arrangements are possible and depending on how folders are organized dynaconf can behave differently.

1. app.py:1 does `from dynaconf import settings`

    -  Only the `.env` file will be searched, other settings are lazy evaluated.
    -  `.env` will be searched starting on `myprogram/src/.env`
    -  if not found then `myprogram/src/config/.env` 
    -  if not found then `myprogram/.env`  **actually found here so stops searching**
    -  if not found then `myprogram/config/.env`
    -  It will load all values from `.env` to the environment variables and create the instance of `settings`

2. app.py:2 does the first access to a settings on `print(settings.NAME)`

    - Dynaconf will execute the loaders defined in `CORE_LOADERS` and `LOADERS`, it will initialize the `settings` object and start the file search.
    - `settings.{py|toml|json|ini|yaml}` will be searched on `myprogram/src/`
    - if not found then `myprogram/src/config`
    - if not found then `myprogram/`
    - if not found then `myprogram/config` **settings.toml actually found here so stops searching for toml**
    - It will load all the values defined in the `settings.toml`
    - It will continue to look all the other files e.g: settings.json, settings.ini, settings.yaml etc.
    - Then
    - It will search for **.secrets.{py|toml|json|ini|yaml}** on `myprogram/src/`
    - if not found then `myprogram/src/config`
    - if not found then `myprogram/`  **.secrets.toml actually found here so stops searching for toml**
    - if not found then `myprogram/config` 
    - It will load all the values defined in `.secrets.toml` (if filename is `*.secret.*` values are hidden on logs)
    - It will continue to look all the other files e.g: .secrets.json, .secrets.ini, .secrets.yaml etc.
    - Then
    - It will iterate the list of loaded files containing `[settings.toml, .secrets.toml]` and for each of them it will also try to find a `settings.local.toml` (**found in myprogram/settings.local.toml**) and a `.secrets.local.toml` using the same search tree until it is found or it will skip if not found.
    - Then
    - It will execute **external loaders** like `Redis` and `Vault` if enabled.
    - It will execute **custom loaders** if configured.
    - Then finally
    - It will read all **environment variables** prefixed with `DYNACONF_` and load its values, in our example it loads `FOO='BAR'` from `.env` file.

3. app.py:3 does second access to a settings on `print(settings.PASSWORD)` 

    - All the loaders, loaded files, config options and vars are now **cached** no loading has been executed.
    - Only if `settings.get_fresh('PASSWORD')` is used, dynaconf will force a re-load of everything to ensure the fresh value.
    - Also if `settings.using_env|from_env` or `ENV_FOR_DYNACONF` switched, e.g: from `[development]` to `[staging]`, then re-load happens.
    - It is also possible to explicitly force a `load` or `reload`.

4. Complete program output is:

```bash
Oscar Wilde
Utopi@
BAR
```

> TIP: If you add `DEBUG_LEVEL_FOR_DYNACONF=DEBUG` on `.env` or export this variable then you can follow the dynaconf loading process.

## Loading order

Dynaconf loads file in a overriding cascade loading order using the predefined order:

1. First the environment variables (and `.env` file) to read for [configuration](configuration.html) options
2. Then the paths provided in `PRELOAD_FOR_DYNACONF` using all enabled loaders.
3. Then the files defined in `SETTINGS_FILE_FOR_DYNACONF` using all enabled loaders.
    - Files containing `.local.` in its name will be loaded at the end. e.g: `settings.local.yaml`
4. Then contents of `SECRETS_FOR_DYNACONF` envvar filename if defined (useful for jenkins and other CI)
5. Then the loaders defined in `LOADERS_FOR_DYNACONF` 
    - Redis if enabled by `REDIS_FOR_DYNACONF=1`
    - Vault if enabled by `Vault_FOR_DYNACONF=1`
    - Custom loaders if any added
    - Environment variables loader will be the last always
6. If there is any `DYNACONF_INCLUDE` key found or `INCLUDES_FOR_DYNACONF` env vars this will be loaded.

The order can be changed by overriding the `SETTINGS_FILE_FOR_DYNACONF` the `CORE_LOADERS_FOR_DYNACONF` and `LOADERS_FOR_DYNACONF` variables.

> **NOTE**: Dynaconf works in an **layered override** mode based on the above order, so if you have multiple file formats with conflicting keys defined, the precedence will be based on the loading order.
> If you dont want to have values like `lists` and `dicts` overwritten take a look on how to [merge existing values](usage.html#merging-existing-values)

## Local configuration files and merging to existing data

> New in **2.2.0**

This feature is useful for maintaining a shared set of config files for a team, while still allowing for local configuration.

Any file matched by the glob `*.local.*` will be read at the end of file loading order. So it is possible to have local settings files that are for example not committed to the version controlled repository. (e:g add `**/*.local*` to your `.gitignore`)

So if you have `settings.toml` Dynaconf will load it and after all will also try to load a file named `settings.local.toml` if it does exist. And the same applies to all the other supported extensions `settings.local.{py,json,yaml,toml,ini,cfg}`

Example:

```ini
# settings.toml        # <-- 1st loaded
[default]
colors = ["green", "blue"]
parameters = {enabled=true, number=42}

# .secrets.toml        # <-- 2nd loaded  (overrides previous existing vars)
[default]
password = 1234

# settings.local.toml  # <-- 3rd loaded  (overrides previous existing vars)
[default]
colors = ["pink"]
parameters = {enabled=false}
password = 9999
```

So with above the values will be:

```python
settings.COLORS == ["pink"]
settings.PARAMETERS == {"enabled": False}
settings.PASSWORD == 9999
```

For each loaded file dynaconf will `override` previous existing keys so if you want to `append` new values to existing variables you can use 3 strategies.

### Mark the local file to be entirely merged

> New in **2.2.0**

```ini
# settings.local.toml
dynaconf_merge = true
[default]
colors = ["pink"]
parameters = {enabled=false}
```

By adding `dynaconf_merge` to the top root of the file mark entire file to be merged.

And then the values will be updated in to existing data structures.

```python
settings.COLORS == ["pink", "green", "blue"]
settings.PARAMETERS == {"enabled": False, "number": 42}
settings.PASSWORD == 9999
```

You can also mark a single `env` like `[development]` to be merged.

```ini
# settings.local.toml
[development]
dynaconf_merge = true
colors = ["pink"]
parameters = {enabled=false}
```

### dynaconf merge token

```ini
# settings.local.toml
[default]
colors = ["pink", "dynaconf_merge"]
parameters = {enabled=false, dynaconf_merge=true}
```

By adding `dynaconf_merge` to a `list` or `dict` marks it as a merge candidate.

And then the values will be updated in to existing data structures.

```python
settings.COLORS == ["pink", "green", "blue"]
settings.PARAMETERS == {"enabled": False, "number": 42}
settings.PASSWORD == 9999
```

> New in **2.2.0**

And it also works having `dynaconf_merge` as dict keys holding the value to be merged.

```ini
# settings.local.toml
[default.colors]
dynaconf_merge = ["pink"]  # <-- value ["pink"] will be merged in to existing colors

[default.parameters]
dynaconf_merge = {enabled=false}
```

### Dunder merging for nested structures

For nested structures the recommendation is to use dunder merging because it it easier to read and also it has no limitations in terms of nesting levels.

```ini
# settings.local.yaml
[default]
parameters__enabled = false
```

The use of `__` to denote nested level will ensure the key is merged with existing values read more in [merging existing values](#merging-existing-values).

### Global merge

```bash
export MERGE_ENABLED_FOR_DYNACONF=true
```

or put it in your `.env` file then Dynaconf will automatically merge all existing variables.

> **BEWARE**: Using `MERGE_ENABLED_FOR_DYNACONF` can lead to unexpected results because you do not have granular control of what is being merged or overwritten so the recommendation is to use other options.

## Settings File Formats

The recommended file format is **TOML** but you can choose to use any of **.{py|toml|json|ini|yaml}**.

The file must be a series of sections, at least one for **[default]**, optionally one for each **[environment]**, and an optional **[global]** section. Each section contains **key-value** pairs corresponding to configuration parameters for that **[environment]**. If a configuration parameter is missing, the value from **[default]** is used. The following is a complete `settings.toml` file, where every standard configuration parameter is specified within the **[default]** section:

> **NOTE**: if the file format choosen is `.py` as it does not support sections you can create multiple files like `settings.py` for [default], `development_settings.py`, `production_settings.py` and `global_settings.py`. **ATTENTION**: using `.py` is not recommended for configuration - prefer to use static files like **TOML**!

```ini
[default]
username = "admin"
port = 5000
host = "localhost"
message = "default message"
value = "default value"

[development]
username = "devuser"

[staging]
host = "staging.server.com"

[testing]
host = "testing.server.com"

[production]
host = "server.com"

[awesomeenv]
value = "this value is set for custom [awesomeenv]"

[global]
message = "This value overrides message of default and other envs"
```

The **[global]** pseudo-environment can be used to set and/or override configuration parameters globally. A parameter defined in a **[global]** section sets, or overrides if already present, that parameter in every environment. 

> IMPORTANT: the environments and pseudo envs such as `[global], ['default']` affects only the current file, it means that a value in `[global]` will override values defined only on that file or previous loaded files, if in another file the value is reloaded then the global values is overwritten. Dynaconf supports multiple file formats but the recommendation is not to mix them, choose a format and stick with it.

For example, given the following `settings.toml` file, the value of address will be **"1.2.3.4"** in every environment:

```cfg
[global]
address = "1.2.3.4"

[development]
address = "localhost"

[production]
address = "0.0.0.0"
```

> **NOTE**: The **[env]** name and first level variables are case insensitive as internally dynaconf will always use upper case, that means **[development]** and **[DEVELOPMENT]** are equivalent and **address** and **ADDRESS** are also equivalent. **But the recommendation is to `always use lower case in files` and `always use upper case in env vars and .py files`** (This rule does not apply for inner data structures as dictionaries and arrays).

## Supported file formats

By default **toml** is the recommended format to store your configuration, however you can switch to a different supported format.

```bash
# If you wish to include support for more sources
pip3 install dynaconf[yaml|ini|redis|vault]

# for a complete installation
pip3 install dynaconf[all]
```

Once the support is installed no extra configuration is needed to load data from those files.

If you need a different file format take a look on how to extend dynaconf writing a [custom loader](extend.html)

## Additional secrets file (for CI, jenkins etc.)

It is common to have an extra `secrets` file that is available only when running on specific CI environment like `Jenkins`, usually there will be an environment variable pointing to the file.

On Jenkins it is done on job settings by exporting the `secrets` information.

Dynaconf can handle this via `SECRETS_FOR_DYNACONF` environment variable.

ex:

```bash
export SECRETS_FOR_DYNACONF=/path/to/settings.toml{json|py|ini|yaml}
```

If that variable exists in your environment then Dynaconf will also load it.

## Including files inside files

Sometimes you have multiple fragments of settings in different files, dynaconf allow easy merging of those files via `dynaconf_include`.

Example:

`plugin1.toml`

```cfg
[development]
plugin_specific_variable = 'value for development'
```

and even mixing different formats:  
`plugin2.yaml`

```yaml
production:
  plugin_specific_variable: 'value for production'
```

Then it can be merged on main `settings.toml` file via `dynaconf_include`

`settings.toml`

```cfg
[default]
dynaconf_include = ["plugin1.toml", "plugin2.yaml"]
DEBUG = false
SERVER = "base.example.com"
PORT = 6666
```

A settings file can include a `dynaconf_include` stanza, whose exact
  syntax will depend on the type of settings file (json, yaml, toml, etc)
  being used:

  ```cfg
  [default]
  dynaconf_include = ["/absolute/path/to/plugin1.toml", "relative/path/to/plugin2.toml"]
  DEBUG = false
  SERVER = "www.example.com"
  ```

  When loaded, the files located at the (relative or absolute) paths in
  the `dynaconf_include` key will be parsed, in order, and override any
  base settings that may exist in your current configuration.

  The paths can be relative to the base `settings.(toml|yaml|json|ini|py)`
  file, or can be absolute paths.

  The idea here is that plugins or extensions for whatever framework or
  architecture you are using can provide their own configuration values
  when necessary.

  It is also possible to specify glob-based patterns:

  ```cfg
  [default]
  dynaconf_include = ["configurations/*.toml"]
  DEBUG = false
  SERVER = "www.example.com"
  ```

  Currently, only a single level of includes is permitted to keep things
  simple and straightforward.

### Including via environment variable

It is also possible to setup includes using environment variable.

```bash
# A glob pattern
export INCLUDES_FOR_DYNACONF='/etc/myprogram/conf.d/*.toml'
# a single path
export INCLUDES_FOR_DYNACONF='/path/to/file.yaml'
# multiple files
export INCLUDES_FOR_DYNACONF='/path/to/file.yaml;/other/path/to/file.toml'
```

## Programmatically loading a settings file

```python
from dynaconf import settings
settings.load_file(path="/path/to/file.toml")  # list or `;/,` separated allowed
```

> **NOTE**: programmatically loaded file is not persisted, once `env` is changed via `setenv|ugin_env`, or a `reload` or `configure` is invoked it will be cleaned, to persist it needs to go to `INCLUDES_FOR_DYNACONF` variable or you need to load it programmatically again.

## Merging existing values

If your settings has existing variables of types `list` ot `dict` and you want to `merge` instead of `override` then 
the `dynaconf_merge` and `dynaconf_merge_unique` stanzas can mark that variable as a candidate for merging.

For **dict** value:

Your main settings file (e.g `settings.toml`) has an existing `DATABASE` dict setting on `[default]` env.

Now you want to contribute to the same `DATABASE` key by adding new keys, so you can use `dynaconf_merge` at the end of your dict:

In specific `[envs]`

```cfg
[default]
database = {host="server.com", user="default"}

[development]
database = {user="dev_user", dynaconf_merge=true}

[production]
database = {user="prod_user", dynaconf_merge=true}
```

also allowed the alternative short format

```cfg
[default]
database = {host="server.com", user="default"}

[development.database]
dynaconf_merge = {user="dev_user"}

[production.database]
dynaconf_merge = {user="prod_user"}
```

In an environment variable:

Using `@merge` mark

```bash
# Toml formatted envvar
export DYNACONF_DATABASE='@merge {password=1234}'
```

or `@merge` mark short format

```bash
# Toml formatted envvar
export DYNACONF_DATABASE='@merge password=1234'
```

It is also possible to use nested `dunder` traversal like:

```bash
export DYNACONF_DATABASE__password=1234
export DYNACONF_DATABASE__user=admin
export DYNACONF_DATABASE__ARGS__timeout=30
export DYNACONF_DATABASE__ARGS__retries=5
```

Each `__` is parsed as a level traversing thought dict keys. read more in [environment variables](environment_variables.html#nested-keys-in-dictionaries-via-environment-variables)

So the above will result in

```py
DATABASE = {'password': 1234, 'user': 'admin', 'ARGS': {'timeout': 30, 'retries': 5}}
```

> **IMPORTANT** lower case keys are respected only on *nix systems, unfortunately Windows environment variables are case insensitive and Python reads it as all upper cases, that means that if you are running on Windows the dictionary can have only upper case keys.

You can also export a toml dictionary.

```bash
# Toml formatted envvar
export DYNACONF_DATABASE='{password=1234, dynaconf_merge=true}'
```

Or in an additional file (e.g `settings.yaml, .secrets.yaml, etc`) by using `dynaconf_merge` token:

```yaml
default:
  database:
    password: 1234
    dynaconf_merge: true
```

or

```yaml
default:
  database:
    dynaconf_merge:
      password: 1234
```

The `dynaconf_merge` token will mark that object to be merged with existing values (of course `dynaconf_merge` key will not be added to the final settings it is just a mark)

The end result will be on `[development]` env:

```python
settings.DATABASE == {'host': 'server.com', 'user': 'dev_user', 'password': 1234}
```

The same can be applied to **lists**:

`settings.toml`

```cfg
[default]
plugins = ["core"]

[development]
plugins = ["debug_toolbar", "dynaconf_merge"]
```

or

```cfg
[default]
plugins = ["core"]

[development.plugins]
dynaconf_merge = ["debug_toolbar"]
```

And in environment variable

using `@merge` token

```bash
export DYNACONF_PLUGINS='@merge ["ci_plugin"]'
```

or short version

```bash
export DYNACONF_PLUGINS='@merge ci_plugin'
```

comma separated values also supported:

```bash
export DYNACONF_PLUGINS='@merge ci_plugin,other_plugin'
```

or explicitly

```bash
export DYNACONF_PLUGINS='["ci_plugin", "dynaconf_merge"]'
```

Then the end result on `[development]` is:

```python
settings.PLUGINS == ["ci_plugin", "debug_toolbar", "core"]
```

If your value is a dictionary:

```bash
export DYNACONF_DATA="@merge {foo='bar'}"

# or the short

export DYNACONF_DATA="@merge foo=bar"
```

### Avoiding duplications on lists

The `dynaconf_merge_unique` is the token for when you want to avoid duplications in a list.

Example:

```cfg
[default]
scripts = ['install.sh', 'deploy.sh']

[development]
scripts = ['dev.sh', 'test.sh', 'deploy.sh', 'dynaconf_merge_unique']
```

```bash
export DYNACONF_SCRIPTS='["deploy.sh", "run.sh", "dynaconf_merge_unique"]'
```

The end result for `[development]` will be:

```python
settings.SCRIPTS == ['install.sh', 'dev.sh', 'test.sh', 'deploy.sh', 'run.sh']
```

> Note that `deploy.sh` is set 3 times but it is not repeated in the final settings.

### Known caveats

The **dynaconf_merge** and **@merge** functionalities works only for the first level keys, it will not merge subdicts or nested lists (yet).

For deeper nested objects use [dunder merge](environment_variables.html#nested-keys-in-dictionaries-via-environment-variables).

### Global merge

```bash
export MERGE_ENABLED_FOR_DYNACONF=true
```

or put it in your `.env` file then Dynaconf will automatically merge all existing variables.

> **BEWARE**: Using `MERGE_ENABLED_FOR_DYNACONF` can lead to unexpected results because you do not have granular control of what is being merged or overwritten so the recommendation is to use other options.

## More examples

Take a look at the [example](https://github.com/rochacbruno/dynaconf/tree/master/example) folder to see some examples of use with different file formats and features.
# Validation

Dynaconf allows the validation of settings parameters, in some cases you may want to validate the settings before starting the program.

Lets say you have `settings.toml`

```ini
[default]
version = "1.0.0"
age = 35
name = "Bruno"

[production]
PROJECT = "This is not hello_world"
```

## Validating in Python programatically

At any point of your program you can do:

```python
from dynaconf import settings, Validator

# Register validators
settings.validators.register(
    # Ensure some parameters exists (are required)
    Validator('VERSION', 'AGE', 'NAME', must_exist=True),

    # Ensure some password cannot exist
    Validator('PASSWORD', must_exist=False),

    # Ensure some parameter mets a condition
    # conditions: (eq, ne, lt, gt, lte, gte, identity, is_type_of, is_in, is_not_in)
    Validator('AGE', lte=30, gte=10),

    # validate a value is eq in specific env
    Validator('PROJECT', eq='hello_world', env='production'),
)

# Fire the validator
settings.validators.validate()
```

The above will raise `dynaconf.validators.ValidationError("AGE must be lte=30 but it is 35 in env DEVELOPMENT")` and `dynaconf.validators.ValidationError("PROJECT must be eq='hello_world' but it is 'This is not hello_world' in env PRODUCTION")`

You can also use dot-delimited paths for registering validators on nested structures:

```python
from dynaconf import settings, Validator

# Register validators
settings.validators.register(

    # Ensure the database.host field exists.
    Validator('DATABASE.HOST', must_exist=True),

    # Make the database.password field optional. This is a default behavior.
    Validator('DATABASE.PASSWORD', must_exist=None),
)

# Fire the validator
settings.validators.validate()
```

## CLI and dynaconf_validators.toml

> **NEW in 1.0.1**

Starting on version 1.0.1 it is possible to define validators in **TOML** file called **dynaconf_validators.toml** placed in the same fodler as your settings files.

`dynaconf_validators.toml` equivalent to program above

```ini
[default]

version = {must_exist=true}
name = {must_exist=true}
password = {must_exist=false}

# dot notation is also supported
'a_big_dict.nested_1.nested_2.nested_3.nested_4' = {must_exist=true, eq=1}

  [default.age]
  must_exist = true
  lte = 30
  gte = 10

[production]
project = {eq="hello_world"}
```

Then to fire the validation use:

```bash
$ dynaconf validate
```

This returns code 0 (success) if validation is ok.
commentjson
flask>=0.12
dynaconf>=0.6.0
commentjson
flask>=1.0
dynaconf>=0.5.3
PyYAML
flask>=0.12
dynaconf>=0.4.3
PyYAML
flask>=0.12
dynaconf>=0.6.0
flask>=0.12
dynaconf>=0.4.3
PyYAML
flask>=0.12
dynaconf>=0.4.3
PyYAML
