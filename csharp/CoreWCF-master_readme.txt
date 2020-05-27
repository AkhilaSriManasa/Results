# How to contribute

The easiest way to contribute is to open an issue and start a discussion.
Then we can decide if and how a feature or a change could be implemented and if you should submit a pull requests with code changes. We encourage all contributors to write tests for the features they are contributing.

Also read this first: [Being a good open source citizen](https://hackernoon.com/being-a-good-open-source-citizen-9060d0ab9732#.x3hocgw85)

## General feedback and discussions

Please start a discussion on the [core repo issue tracker](https://github.com/CoreWCF/CoreWCF/issues).

## Platform

Core WCF is built on top of .NET Core 2.2.

## Building

Run `dotnet build` from the command line inside the src folder. This builds Core WCF.

## Other discussions

https://gitter.im/CoreWCF/CoreWCF

## Filing issues

The best way to get your bug fixed is to be as detailed as you can be about the problem.
Providing a minimal project with steps to reproduce the problem is ideal.
Here are questions you can answer before you file a bug to make sure you're not missing any important information.

1. Did you read the [documentation](https://corewcf.readthedocs.io/en/latest/)?
2. Did you include the snippet of broken code in the issue?
3. What are the *EXACT* steps to reproduce this problem (including source/destination types, mapping configuration and execution)?

GitHub supports [markdown](https://github.github.com/github-flavored-markdown/), so when filing bugs make sure you check the formatting before clicking submit.

## Contributing code and content

You will need to sign a [Contributor License Agreement](https://cla.dotnetfoundation.org/) before submitting your pull request.

Make sure you can build the code. Familiarize yourself with the project workflow and our coding conventions. If you don't know what a pull request is read this article: https://help.github.com/articles/using-pull-requests.

**We only accept PRs to the master branch.**

Before submitting a feature or substantial code contribution please discuss it with the team and ensure it follows the product roadmap. Here's a list of blog posts that are worth reading before doing a pull request:

* [Open Source Contribution Etiquette](http://tirania.org/blog/archive/2010/Dec-31.html) by Miguel de Icaza
* [Don't "Push" Your Pull Requests](http://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) by Ilya Grigorik.
* [10 tips for better Pull Requests](http://blog.ploeh.dk/2015/01/15/10-tips-for-better-pull-requests/) by Mark Seemann
* [How to write the perfect pull request](https://github.com/blog/1943-how-to-write-the-perfect-pull-request) by GitHub

Here's a few things you should always do when making changes to the code base:

**Commit/Pull Request Format**

```
Summary of the changes (Less than 80 chars)
 - Detail 1
 - Detail 2

#bugnumber (in this specific format)
```

**Tests**

-  Tests need to be provided for every bug/feature that is completed.
-  Tests only need to be present for issues that need to be verified by QA (e.g. not tasks).
-  If there is a scenario that is far too hard to test there does not need to be a test for it.
  - "Too hard" is determined by the team as a whole.
  - With WCF there are many infrastructure scenarios which are hard to automate because of that infrastructure (kerberos auth in a Windows domain for example) but the tests are simple to write, just not execute. We will clarify such  scenarios which are too hard to test because of infrastructure requirements, but we will provide test code which isn't run as part of automated tests, but can be run manually in a configured environment. For example, on the WCF client we have tests which require being in a domain which are disabled but we have a flag we can set to enable running those tests so that if you are executing them in a domain, you can still test it.
The MIT License (MIT)

Copyright (c) 2019 .NET Foundation

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
### What is Core WCF? 

Core WCF is a port of Windows Communication Framework (WCF) to .NET Core. The goal of this project is to enable existing WCF projects to move to .NET Core. Please note that right now, this port is not production ready. We suggest waiting until there are release packages available before using WCF in a production environment. 

### How do I get started?

There are pre-release packages available from a NuGet feed hosted in Azure DevOps. You can download the packages by adding the following package source to your list of feeds.

    https://pkgs.dev.azure.com/dotnet/CoreWCF/_packaging/CoreWCF/nuget/v3/index.json

If you are using a nuget.config file with only the default nuget.org package source, after adding the CoreWCF feed it would like like this:
```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="CoreWCF" value="https://pkgs.dev.azure.com/dotnet/CoreWCF/_packaging/CoreWCF/nuget/v3/index.json" />
  </packageSources>
</configuration>
```
### How do I contribute?

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.



### License, etc.

This project has adopted the code of conduct defined by the Contributor Covenant to clarify expected behavior in our community.
For more information see the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct).

Core WCF is Copyright &copy; 2019 .NET Foundation and other contributors under the [MIT license](LICENSE.txt).

### .NET Foundation

This project is supported by the [.NET Foundation](https://dotnetfoundation.org).
Using the CoreWCF Postman Samples Collection.json within Postman

- Run the DesktopServer or NetCoreServer example applications
- Start Postman
- Go to 'File' and then select 'Import..' on the dropdown menu
- Click on 'Choose Files'
- Browse to thse location of, and select, the JSON file
- Expand the collection in the left-hand pane and select the 'CoreWCF NetCoreServer Sample Request'
- Click on 'Send'