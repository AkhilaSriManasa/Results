# Code of Conduct

This project has adopted the code of conduct defined by the Contributor Covenant
to clarify expected behavior in our community.
For more information, see the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct).
# Contributing

We welcome contributions. Great ways to contribute include trying things out, filing bugs, joining in design conversations and fixing issues. If you're looking at places to contribute code, take a look at our [help wanted issues](https://github.com/dotnet/project-system/issues?q=is%3Aopen+is%3Aissue+label%3A%22Help+Wanted%22).

If you want to submit a feature or a substantial code contribution, please discuss it first with the the team by [filing an issue](https://github.com/dotnet/project-system/issues/new), making sure it follows our [Roadmap](docs/repo/roadmap.md).

For additional information, see the following:

- [Getting Started](docs/repo/getting-started.md)
- [Coding Conventions](docs/repo/coding-conventions.md)
- [Debugging Tips](docs/repo/debugging-tips.md)
- [Features](docs/repo/features.md)
- [Architecture](docs/repo/architecture.md)
- [Rules of the Project System](docs/repo/rules-of-the-project-system.md)
- [Visual Studio Threading Guidelines](https://github.com/Microsoft/vs-threading/blob/master/doc/index.md)
- [Common Project System (CPS) Documention](https://github.com/microsoft/vsprojectsystem)
- [Code of Conduct](https://github.com/dotnet/home/blob/master/guidance/be-nice.md)

# IntelliCode

To provide better IntelliSense results when working with this project in Visual Studio 2019 you can [add our IntelliCode model](https://docs.microsoft.com/en-us/visualstudio/intellicode/share-models#add-a-custom-model) to your installation.

https://prod.intellicode.vsengsaas.visualstudio.com/get?m=A17F43B28B8B4488B7A89D27F33E1BB6Copyright (c) .NET Foundation and Contributors

All rights reserved.

Licensed under the Apache License, Version 2.0 (the “License”); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
# C#, F# and Visual Basic project system

|Release|Unit Tests (Debug)|Unit Tests (Release)| Localization | Coverage (Debug)
|---|:--:|:--:|:--:|:--:|
|[16.0](https://github.com/dotnet/project-system/tree/dev16.0.x)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=dev16.0.x&jobName=Windows&configuration=Windows%20debug&label=dev16.0.x)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=dev16.0.x)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=dev16.0.x&jobName=Windows&configuration=Windows%20Release&label=dev16.0.x)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=dev16.0.x)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=dev16.0.x&jobName=Spanish&label=dev16.0.x)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=dev16.0.x)|[![codecov](https://codecov.io/gh/dotnet/project-system/branch/dev16.0.x/graph/badge.svg)](https://codecov.io/gh/dotnet/project-system)
|[16.4](https://github.com/dotnet/project-system/tree/dev16.4.x)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=dev16.4.x&jobName=Windows_Debug&%20debug&label=dev16.4.x)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=dev16.4.x)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=dev16.4.x&jobName=Windows_Release&%20Release&label=dev16.4.x)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=dev16.4.x)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=dev16.4.x&jobName=Spanish&label=dev16.4.x)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=dev16.4.x)|[![codecov](https://codecov.io/gh/dotnet/project-system/branch/dev16.4.x/graph/badge.svg)](https://codecov.io/gh/dotnet/project-system)
|[master](https://github.com/dotnet/project-system/tree/master)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=master&jobName=Windows_Debug&%20debug&label=master)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=master)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=master&jobName=Windows_Release&%20Release&label=master)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=master)|[![Build Status](https://dev.azure.com/dnceng/public/_apis/build/status/dotnet/project-system/unit-tests?branchName=master&jobName=Spanish&label=master)](https://dev.azure.com/dnceng/public/_build/latest?definitionId=406&branchName=master)|[![codecov](https://codecov.io/gh/dotnet/project-system/branch/master/graph/badge.svg)](https://codecov.io/gh/dotnet/project-system)

[![Join the chat at https://gitter.im/dotnet/project-system](https://badges.gitter.im/dotnet/project-system.svg)](https://gitter.im/dotnet/project-system?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This repository contains the new C#, F# and Visual Basic project system that has been rewritten on top of the [Common Project System (CPS)](https://github.com/microsoft/vsprojectsystem). In [Visual Studio 2017](https://www.visualstudio.com/vs/), this project system is used by default for Shared Projects (C# and Visual Basic), and .NET Core (C#, F# and Visual Basic) project types, however, [long term](docs/repo/roadmap.md) it will be the basis of all C#, F# and Visual Basic project types. For a list of feature differences between the project systems, see [Feature Comparison](https://github.com/dotnet/project-system/blob/master/docs/feature-comparison.md).

The existing C# and Visual Basic project systems (csproj.dll and msvbprj.dll), which first shipped back in Visual Studio.net nearly 15 years ago, have served us well but are:

- Native and COM-based
- Single threaded and bound to the UI thread
- Hard to extend outside of aggregation via the use of `<ProjectTypeGuids>` and [sub types (flavors)](https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/project-types)
- Tied to Visual Studio

The new C#, F# and Visual Basic project system is:

- Managed and managed-interface based
- Multi-threaded, scalable, and responsive
- Easy to extend via the use of the  Managed Extensibility Framework (MEF) and composable. Many parties, including 3rd parties, can contribute to a single project system
- Hostable outside of Visual Studio

## What is a project system?
A project system sits between a project file on disk (for example, .csproj and .vbproj) and various Visual Studio features including, but not limited to, Solution Explorer, designers, the debugger, language services, build and deployment. Almost all interaction that occurs with files contained in a project file, happens through the project system.

There are many technologies that come together to make up the .NET project system:

- [MSBuild](https://github.com/microsoft/msbuild) provides the build engine and file format.
- [SDK](https://github.com/dotnet/sdk) provides the MSBuild tasks and targets needed to build .NET projects.
- [Common Project System](https://github.com/microsoft/vsprojectsystem) provides the base building blocks for the project system including (but not limited to) project tree, build and debugger coordination and Visual Studio integration.
- [Roslyn](https://github.com/dotnet/roslyn) provides C# and Visual Basic language support including compilers, IntelliSense, refactorings, analyzers and code fixes.
- [Visual F# tools](https://github.com/Microsoft/visualfsharp) provides F# language support.
- [CLI](https://github.com/dotnet/cli) is the .NET command-line interface for building, running and interacting with .NET projects.

![image](https://cloud.githubusercontent.com/assets/1103906/24277819/d1e48eba-1093-11e7-811f-ae5debcc1e6c.png)

## How do I engage and contribute?
We welcome you to try things out, [file issues](https://github.com/dotnet/project-system/issues), make feature requests and join us in design conversations. If you are looking for something to work on, take a look at our [help wanted issues](https://github.com/dotnet/project-system/issues?q=is%3Aopen+is%3Aissue+label%3A%22Help+Wanted%22) for a great place to start. Also be sure to check out our [contributing guide](CONTRIBUTING.md).

This project has adopted a code of conduct adapted from the [Contributor Covenant](http://contributor-covenant.org/) to clarify expected behavior in our community. This code of conduct has been [adopted by many other projects](http://contributor-covenant.org/adopters/). For more information see [Contributors Code of conduct](https://github.com/dotnet/home/blob/master/guidance/be-nice.md). 
**Visual Studio Version**:

**Summary**:


**Steps to Reproduce**:

1. 

2. 

3. 

**Expected Behavior**:

**Actual Behavior**:

**User Impact**:
# Compatibility

The following is a list of known compatibility issues and behavioral differences between the legacy project system and the new project system.

For a list of feature differences; see [Feature Comparison](feature-comparison.md).

## Builds

### Design-time builds are run out-of-process.
Similar to normal builds, the new project system runs [design-time builds](design-time-builds.md) in a separate process instead of within the Visual Studio process. This means that tasks and assemblies adhere to the binding policy of MSBuild.exe regardless of whether they loaded in a design-time build or a normal build. In the legacy project system, design-time builds use the binding policy of Visual Studio (devenv.exe), whereas normal builds use the binding policy of MSBuild.exe.

### Design-time builds are asynchronous.
The legacy project system used to guarantee that a design-time build had occurred by the time certain changes had been done to the project, such as adding or removing files or switching configurations. While easier for components to reason about, this was to the detriment of user experience because this would be done as a UI blocking call.

In the new project system design-time builds are asynchronous, and are not guaranteed to have completed by the time the above changes have been made to the project.

### Design-time build errors and warnings show in the Error List
Design-time build errors and warnings appear in the Error List alongside a normal build's errors and warnings. This might result in warnings and errors showing up that we're previously hidden by the legacy project system.

### Design-time builds might run targets in the same build
For performance reasons, the new project system will group and run multiple targets together in the same build which might result in different behavior for targets that have incomplete or inaccurate target dependencies.

## Configurations

### Configurations are inferred differently
To keep the project file simple, configurations are inferred differently. More details [here](configurations.md)
# Configurations

The way configurations are inferred for a given project is different between the legacy and new project systems. This is also a breaking change in 15.3 compared to 15.0 RTM

## Legacy project system behavior  
In legacy projects configurations of a project are inferred based on conditions in the project file. So if a project had this text,
```xml
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
…
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">
…
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|x86' ">
```

the project system would have inferred that the project had two Configurations called Debug and Release and two Platforms called AnyCPU and x86. The old project system would look only in the project and not in any imported props\targets. 

## New project system behavior

### VS 2017 RTM
For the new project system, the old behavior got in the way of project simplification because we would have had to have these conditions in the project file. So for VS2017 RTM we hid these away in the imported targets files and CPS can infer these configurations from there. However, now if the user goes to the configuration manager in VS and deletes\modifies these configurations, we can’t do anything because we’d have to change the imported targets which may not be user files. This was broken in VS2017 RTM.

### VS 2017 "15.3" 
We’ve fixed the issues with deleting the configurations in 15.3 by not inferring these configurations anymore based on conditions but instead we just read two properties called ‘Configurations’ and ‘Platforms’ from the project which would be semi-colon separated list of configurations\platforms. So by default the SDK has these values:

```xml
  <Configurations>Debug;Release</Configurations>
  <Platforms>AnyCPU</Platforms>
```

And these are the same defaults that VS 2017 RTM had. If the user now renames the Debug configuration to MyDebug then we would simply write `<Configurations>MyDebug;Release</Configurations>` to the project file and we get to keep the clean project file.
 
## Breaking change

### TL;DR
If you had a project that had configurations like this:
```xml
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'MyDebug|AnyCPU' " />
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'MyDebug|x86' " />
```

change the project to have two properties like this:
```xml
<PropertyGroup>
   <Configurations>MyDebug;Debug;Release</Configurations>
   <Platforms>AnyCPU;x86</Platforms>
</PropertyGroup>
```

### Details

This is a breaking change because we *only* read configurations from these properties now and don't infer them anymore from conditions on propertygroups. If someone had created a new configuration with RTM tools like this
```xml
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'MyDebug|AnyCPU' ">
```
and that was set as the active configuration then the active configuration gets persisted into the sln file. The RTM product would have inferred the MyDebug config and loaded it whereas 15.3 looks at the Configurations property and will think it only has Debug. The sln file will however ask the project system to load the MyDebug configuration which will cause the project to fail to load with a configuration not found error.
 
### Rationale
We looked at the telemetry we have for how many .NET Core projects were created with non-standard configurations and it was about 1% of projects and very small absolute number as well. The effort to have a hybrid and support both styles of inferring configurations would be quite high and based on the data we don't think it's worth investing in given the fix for the affected projects is fairly straightforward. 
# Design-time builds

- [What is a design-time build?](#what-is-a-design-time-build)
- [Targets that run during design-time builds](#targets-that-run-during-design-time-builds)
- [Designing targets for use in design-time builds](#designing-targets-for-use-in-design-time-builds)
- [Diagnosing design-time builds](#diagnosing-design-time-builds)

## What is a design-time build?

Design-time builds are special builds that are launched by the project system to gather just enough information to populate the language service and other project services, such as the Dependencies node.  Design-time builds are not directly user-initiated, but may be indirectly launched in response to a user action such as changing the project file, build options, adding/removing source files and references, or switching configurations.

For performance reasons, and unlike normal builds which call the _Build_ target, design-time builds call a limited set of targets. This can lead to custom builds that succeed during a normal build, but end up failing during a design-time build, typically due to custom targets with under-specified dependencies.

## Targets that run during design-time builds

The following design-time targets are called, including any dependencies, during design-time builds in the C#/VB project systems. Other project systems, such as C++ or JavaScript will call different targets. 

Design-Time Target                            | Normal Target                      | Description
----------------------------------------------|------------------------------------|------------------
ResolveAssemblyReferencesDesignTime           | ResolveAssemblyReferences          | Resolves `<Reference>` items to their paths.
ResolveProjectReferencesDesignTime            | ResolveProjectReferences           | Resolves `<ProjectReference>` items to their output paths.
ResolveComReferencesDesignTime                | ResolveComReferences               | Resolves `<COMReference>` items to their primary interop assemblies (PIA) paths.
ResolveFrameworkReferencesDesignTime          | ResolveFrameworkReferences         | Resolves `<FrameworkReference>` items to their paths.
ResolvePackageDependenciesDesignTime          | ResolvePackageDependencies         | Resolves `<PackageReference>` items to their paths.
CompileDesignTime (new project system)/Compile| Compile                            | Passes command-line arguments, `<Compile>` items and `<Analyzer>` items to the compiler in normal builds, or to the language service in design-time builds.

The design-time targets are typically simple wrappers around their normal target equivalents, with customized behavior for design-time builds. 

## Designing targets for use in design-time builds

Targets that dynamically change references, source files or compilation options _must_ run during design-time builds to avoid unexpected behavior in Visual Studio. In contrast, if a target does not contribute these items, then it should actively avoid running in these builds to ensure design-time builds are as fast as possible. Whether a target is run in design-time builds is based on whether a target's `BeforeTargets` and `AfterTargets` attributes specifies a direct or indirect dependency of any of the above  targets. See [Diagnosing design-time builds](#diagnosing-design-time-builds) to see logs that help you figure out if your target is being run or not.

### Running in a design-time build

If you've determined that your target needs to run in a design-time build, using the above table set `BeforeTargets` to the normal target equivalent of what you are contributing to the build. For example, if a target changes `<Reference>` items, then it should indicate that it runs _before_ `ResolveAssemblyReferences` target:

``` XML
  <Target Name="AddAdditionalReferences" BeforeTargets="ResolveAssemblyReferences">
     ...
  </Target>
```
The `AddAdditionalReferences` target will run in both normal builds _and_ design-time builds, leading to consistent results between them.

### Determining whether a target is running in a design-time build

Use both the `DesignTimeBuild` (CPS-based projects) and `BuildingProject` (legacy project system) properties to determine whether a target is running in a design-time build or a normal build. This can be used to avoid expensive calculations or work that is only needed for a normal build, helping to keep the IDE responsive.

``` XML
  <Target Name="AddAdditionalReferences" BeforeTargets="ResolveAssemblyReferences">
     <PropertyGroup Condition="'$(DesignTimeBuild)' == 'true' OR '$(BuildingProject)' != 'true'">
         <_AvoidExpensiveCalculation>true</_AvoidExpensiveCalculation>
     </PropertyGroup>
     ...
  </Target>
```

__NOTE:__ The `DesignTimeBuild` property is typically empty (`''`) in normal builds, so avoid comparisons to `'false'`.
 
### Specifying explicit dependencies

If your target has dependencies on properties, items or files produced during the build, it must have a `DependsOnTargets` attribute that accurately indicates the set of targets that produce those assets. An under-specified `DependsOnTargets` will lead to unexpected behavior, such as targets that fail on the first design-time build or fail during every design-time build.

## Diagnosing design-time builds

### Signs that a design-time build is failing or taking too long

While the results of design-time builds are not directly visible by default, the following symptoms are good indicators that one is failing for a given project:

- Source files in a project are marked as coming from the `Miscellaneous Files` project when opened in the editor
- IntelliSense shows incomplete and/or incorrect results
- A normal build succeeds inside and outside of Visual Studio, yet the Error List continues to show build errors

The following are symptoms of a design-time build that is taking too long:

- Project modifications, such as renaming, adding or deleting files, take a long time
- Switching build configurations, for example from Debug to Release, takes a long time

### Getting Visual Studio to output the results of a design-time build

You can force Visual Studio to show the results of a design-time build using the following instructions:

#### Visual Studio 2015 or below

1. Delete the `.vs` directory that sits alongside the solution that is experiencing the problem
2. Start a _Developer Command Prompt for VS2015_
3. At the prompt, run `SET TRACEDESIGNTIME=true`
4. At the prompt, run `devenv`
5. Open the solution
6. Under `%TEMP%`, look for `[RANDOMGUID].designtime.log` files, these will contain the results of the design-time build. If running Visual Studio 2015 Update 2 or higher, the name of the project and design-time target that is being called will also be included in the file name.

#### Visual Studio 2017 or later

1. Install the [Project System Tools](https://marketplace.visualstudio.com/items?itemName=VisualStudioProductTeam.ProjectSystemTools) extension
2. In Visual Studio, choose the `View > Other Windows > Build Logging` menu item.
3. Click on the "play" button.

This will cause design-time builds to show up in the build logging tool window. If you have the [MSBuild Binary and Structured Log Viewer](http://msbuildlog.com/) installed, you can double-click on a log to view it in the viewer, otherwise you can right-click and choose `Save As...` to save the log in the new [binary log format](https://github.com/Microsoft/msbuild/wiki/Binary-Log).

### Diagnosing failing or slow design-time builds

After following the above instructions, open the resulting build log file or Output window (for the new project system).

#### Failing design-time build
For a failing build, look for errors at the end of the log:

```
Build FAILED.

c:\Projects\MyProject\MyProject.csproj(17,5): error : An error occurred!
    0 Warning(s)
    1 Error(s)
```

These errors indicate that a target failed, typically this is due to targets that have not correctly specified their dependencies.


#### Slow design-time build
For a slow design-time, look for the target performance summary at end of the log which can indicate long running tasks and targets:

```
Target Performance Summary:
        0 ms  AfterClean                                 1 calls
        0 ms  Clean                                      1 calls
        0 ms  CleanReferencedProjects                    1 calls
        0 ms  CleanPublishFolder                         1 calls
        0 ms  BeforeRebuild                              1 calls
        0 ms  BeforeClean                                1 calls
        0 ms  BeforeBuild                                1 calls
        0 ms  _SplitProjectReferencesByFileExistence     1 calls
        1 ms  CleanXsdCodeGen                            1 calls
        2 ms  AssignProjectConfiguration                 1 calls
        7 ms  CoreClean                                  1 calls
       10 ms  _CheckForInvalidConfigurationAndPlatform   1 calls

Task Performance Summary:
        0 ms  RemoveDuplicates                           1 calls
        0 ms  Error                                      1 calls
        1 ms  MakeDir                                    1 calls
        1 ms  Message                                    2 calls
        1 ms  ReadLinesFromFile                          1 calls
        1 ms  WriteLinesToFile                           1 calls
        1 ms  FindUnderPath                              2 calls
        1 ms  AssignProjectConfiguration                 1 calls
        2 ms  Delete                                     3 calls
``` 
# Feature Comparison

The following is an incomplete list of features differences between the legacy project system and the new project system. 

For a list of behavior differences; see [Compatibility](compatibility.md).

**Feature**|**Legacy**|**New**|**Notes**
---|:---:|:---:|---
**Platforms**                                                               |
.NET Standard                                                               |          | ●
.NET Core                                                                   |          | ●
.NET Framework                                                              | ●        | ◖  | No ASP.NET AppModel support in new project system
**App Models**                                                              |
ASP.NET Core (.NET Framework & .NET Core)                                   |          | ●
ASP.NET                                                                     | ●        |   
Xamarin                                                                     | ●        |   
Universal Windows Platform (UWP)                                            | ●        |
Windows Presentation Framework (WPF)                                        | ●        | 16.3
Windows Forms                                                               | ●        | 16.3
Windows Workflow Foundation (WWF)                                           | ●        |
**Build**|
Target multiple frameworks (multi-target) from single project               |          | ●
Show build (design-time) errors & warnings in Error List as you make them   |          | ●
**Debug**|
Debug multiple frameworks from single project                               |          | ●
Debug with multiple environments from single project ("launch profiles")    |          | ●
Debug settings persistence                                                  |project.csproj.user|launchsettings.json
Modify environment variables on debug                                       |          | ● 
Launch with native debugging                                                | ●        | ●
Launch with SQL Server debugging                                            | ●        | 16.4
Launch with remote debugging                                                | ●        |   
Launch with Azure Snapshot Debugger                                         |          | ●
**Publish**                                                                 |
Publish to Azure                                                            |          | ●
ClickOnce Publish                                                           | ●        | 
**Project**                                                                 |
Globbing support                                                            |          | ●    | `<Compile Include="*.cs" />`
Simplified project format                                                   |          | ●    | `<Project Sdk="Microsoft.Net.Sdk">`
Simplified configuration syntax                                             |          | ●    | `<Configurations>Debug;Release<Configurations>;<Platforms>AnyCPU;x64</Platforms>`
Implicit configuration syntax                                               | ●        |      | `<PropertyGroup Condition="'$(Configuration)\|$(Platform)' == 'Debug\|AnyCPU'">`
Edit project XML while project is loaded                                    |          | ●
Find & Find in Files in project file                                        |          | ●
Automatically reload project file with no prompts                           |          | ●
Automatically reload targets files                                          |          | ●
Automatically refresh Solution Explorer to reflect file system              |          | ●
Show items included in imports (.targets/.props)                            |          | ●
**Dependencies**|
Auto-restore packages on load and external edit                             |          | ● 
PackageReference support                                                    | ●        | ●
Dependency node showing package/project graph                               |          | ● 
Transitive ProjectReference                                                 |          | ●
Generate NuGet package on build                                             |          | ● 
**Features**|
Add Service Reference                                                       | ●        | 
Add Web Reference                                                           | ●        | 
Add Data Source                                                             | ●        | 16.4
DataSet Designer                                                            | ●        |
"Initialize Interactive Window with Project"                                | ●        | ● | Only when targeting .NET Framework.
Class Diagrams                                                              | ●        | ●
Code Analysis                                                               | ●        | 
Code Metrics                                                                | ●        | ● 
Code Clones                                                                 | ●        | ●
Fakes                                                                       | ●        | 
T4 Templates                                                                | ●        | 
[Automation Extenders](https://msdn.microsoft.com/en-us/library/0y92k2w2.aspx)| ●      | ●
# Opening with the new project system

***NOTE:** The behaviors listed below are subject to change as we add support for more project types in the new project system.*

## When does a project open with the new project system versus the legacy project system?

Because both the new project system and legacy project systems use the same file extensions (csproj, vbproj and fsproj), two factors determine whether a project will open in one or the other.

### TargetFramework/TargetFrameworks properties

*Applies to C# and Visual Basic only*

If a csproj or vbproj project contains a `<TargetFramework>` or `<TargetFrameworks>` property in the body of the project file (not in any of its imports), then it will be automatically opened in the new project system. Specifically, **in version 16.3 and earlier** Visual Studio will scan the raw text of the project file for `</TargetFramework>` or `</TargetFrameworks>`. In **version 16.4 and later** Visual Studio will look for a `<TargetFramework>` or `<TargetFrameworks>` element parented by a `<PropertyGroup>` element.

For example, the following two csproj or vbproj projects will open in the new project system:

``` XML
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net45</TargetFramework>
  </PropertyGroup>
</Project>
```

``` XML
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFrameworks>net45;netstandard1.3</TargetFrameworks>
  </PropertyGroup>
</Project>
```

Whereas, the following csproj or vbproj will open in the legacy project system:

``` XML
<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="15.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props" Condition="Exists('$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props')" />

  <PropertyGroup>
      <TargetFrameworkVersion>v4.6.1</TargetFrameworkVersion>
  </PropertyGroup>

  <Import Project="$(MSBuildToolsPath)\Microsoft.CSharp.targets" />
</Project>
```

### SDKs

*Applies to F# in 16.3 and earlier, and to F#, C#, and Visual Basic in 16.4 and later*

If a project is marked as importing an SDK in the body of the project file (not in any of its imports), then the project is opened in the new project system.

Specifically, VS looks for an `Sdk` attribute within a `<Project>` or `<Import>` element. For example, the following two projects will open in the new project system:

``` XML
<Project Sdk="Microsoft.NET.Sdk">

</Project>
```

``` XML
<Project>
  <Import Project="Sdk.props" Sdk="Microsoft.NET.Sdk" />

  <Import Project="Sdk.targets" Sdk="Microsoft.NET.Sdk" />
</Project>
```

In addition, for C# and Visual Basic projects only, VS will look for an `<Sdk>` element parented by a `<Project>` element. For example:

``` XML
<Project>
  <Sdk Name="Microsoft.NET.Sdk" Version="1.2.3" />

</Project>
```

Whereas the following will open in the legacy project system:

``` XML
<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="15.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props" Condition="Exists('$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props')" />

  <PropertyGroup>
      <TargetFrameworkVersion>v4.6.1</TargetFrameworkVersion>
  </PropertyGroup>

  <Import Project="$(MSBuildToolsPath)\Microsoft.CSharp.targets" />
</Project>
```

### Project Type GUIDs

Inside the solution, there are GUIDs associated with a project called a "project type". By default, all csproj, vbproj and fsproj point to the following three GUIDs (the first GUID in the line):

```
Project("{F2A71F9B-5D33-465A-A702-920D77279786}") = "Library1", "Library1.fsproj", "{9B232C4C-AE37-4BC6-A68A-52A275F253C2}"
EndProject
Project("{F184B08F-C81C-45F6-A57F-5ABD9991F28F}") = "Library2", "Library2.vbproj", "{629B0BD5-ADD4-46A9-85E2-0D75CA49DCCB}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Library3", "Library3.csproj", "{ADFEAAF5-225C-4E13-8B65-77057AAC44B8}"
EndProject
```

When these GUIDs are set, the behavior called out above of whether to open in the new project system or the old project system kicks in. However, it is possible to force projects to open in the new project system by changing these GUIDs to the following:

```
Project("{6EC3EE1D-3C4E-46DD-8F32-0CC8E7565705}") = "Library1", "Library1.fsproj", "{9B232C4C-AE37-4BC6-A68A-52A275F253C2}"
EndProject
Project("{778DAE3C-4631-46EA-AA77-85C1314464D9}") = "Library2", "Library2.vbproj", "{629B0BD5-ADD4-46A9-85E2-0D75CA49DCCB}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "Library3", "Library3.csproj", "{ADFEAAF5-225C-4E13-8B65-77057AAC44B8}"
EndProject
```

All three of these projects will be force loaded into the new project system, regardless of the format of the project. This is helpful, for example, if you'd like to move `<TargetFramework>` property to an import.
# Up-to-date Check

The Project System's _Fast Up-to-date Check_ saves developers time by quickly assessing whether a project needs to be
built or not. If not, Visual Studio can avoid a comparatively expensive call to MSBuild.

At a superficial level, the check compares timestamps between the project's inputs and its outputs. For more
information on how it works in detail, see [this document](repo/up-to-date-check-implementation.md).

Note that the _fast_ up-to-date check is intended to speed up the majority of cases where a build is not required,
yet it cannot reliably cover all cases correctly. Where necessary, it errs on the side of caution as triggering a
redundant build is better than not triggering a required build. MSBuild performs its own checks, so even if the 
fast up-to-date check incorrectly determines the project is out-of-date, MSBuild may still not perform a full
build.

## Customization

For most projects the up-to-date check works automatically and you won't need to know or think about this feature.
However if your build is highly customized then you may need to provide some extra information to help the up-to-date
check work correctly.

For customized builds, you may add to the following item types:

- `UpToDateCheckInput` &mdash; Describes an input file that MSBuild would not otherwise know about
- `UpToDateCheckBuilt` &mdash; Describes an output file that MSBuild would not otherwise know about

Note that `UpToDateCheckOutput` exists but is deprecated and only maintained for backwards compatability.
Projects should use to `UpToDateCheckBuilt` instead.

You may add to these item types declaratively. For example:

```xml
<ItemGroup>
  <UpToDateCheckInput Include="MyCustomBuildInput.abc" />
</ItemGroup>
```

Alternatively, you may override the MSBuild targets that Visual Studio calls to collect these items. Overriding targets
allows custom logic to be executed when determining the set of items. The relevant targets are defined in
`Microsoft.Managed.DesignTime.targets` with names:

- `CollectUpToDateCheckInputDesignTime`
- `CollectUpToDateCheckBuiltDesignTime`

Note that changes to inputs **must** result in changes to outputs. If this rule is not observed, then an input may
have a timestamp after all outputs, which leads the up-to-date check to consider the project out-of-date after building
indefinitely. This can lead to longer build times.

### Grouping inputs and outputs into sets

For some advanced scenarios, it's necessary to partition inputs and outputs into groups and consider each separately.
This can be achieved by adding `Set` metadata to the relevant items.

For example, an ASP.NET project may use sets to group Razor `.cshtml` files with their output assembly `MyProject.Views.dll`,
which is distinct from the other compilation target `MyProject.dll`. This could be achieved with something like:

```xml
<ItemGroup>
  <UpToDateCheckInput Include="Home.cshtml" Set="Views" />
  <UpToDateCheckOutput Include="MyProject.Views.dll" Set="Views" />
</ItemGroup>
```

Items that do not specify a `Set` are included in the default set. Items may be added to multiple sets by separating
their names with a semicolon (e.g. `Set="Set1;Set2"`).

### Copied files

Builds may copy files from a source location to a destination location. Information about these locations should be
captured in the project so that the up-to-date check can determine if the source file is newer than the destination,
in which case the project is out-of-date and a build will be allowed.

To model this, use:

```xml
<UpToDateCheckBuilt Include="Source\File.txt" Original="Destination\File.txt" />
```

When specifying `Original` metadata, the `Set` property has no effect. Each copied file is considered in isolation,
looking only at the timestamps of the source and destination. Sets are used to compare groups of items, so these
features do not compose. If both properties are present, `Original` will take effect and `Set` is ignored.

## Debugging

By default the up-to-date check does not log anything, though you can infer its decision from your build output summary:

```text
========== Build: 0 succeeded, 0 failed, 1 up-to-date, 0 skipped ==========
```

In this example the up-to-date check determined the project was up-to-date. If `succeeded` or `failed` was instead
non-zero, then the check would have determined the project was not up-to-date, resulting in a call to MSBuild.

To debug issues with the up-to-date check, enable its logging.

> Tools | Options | Projects and Solutions | .NET Core

![Projects and Solutions, .NET Core options](repo/images/options.png)

Setting this level to a value other than `None` results in messages prefixed with `FastUpToDate:` in Visual Studio's
build output.

- `None` disables log output.
- `Minimal` produces a single message per out-of-date project.
- `Info` and `Verbose` provide increasingly detailed information about the inner workings of the check, which are useful for debugging.

## Disabling the Up-to-date Check

If you do not wish to use the fast up-to-date check, preferring to always call MSBuild, you can disable it by either:

- Unchecking "Don't call MSBuild if a project appears to be up to date" (shown above), or
- Adding property `<DisableFastUpToDateCheck>True</DisableFastUpToDateCheck>` to your project

Note that in both cases this only disables Visual Studio's up-to-date check. MSBuild will still perform its own
determination as to whether the project should be rebuilt.

If you are disabling the check because you feel it is not behaving correctly, please file an issue in this repo and
include details from the verbose log so that we can improve the feature.
# __Well Known Project Properties, Items and Item Metadata__

There are two types of properties, items and item metadata that are stored in MSBuild project, targets and props files. 

- [Build  Properties, Items and Item  Metadata](#build-properties-items-and-item-metadata)

- [Design-Time Properties, Items and Item Metadata](#design-time-properties-items-and-item-metadata)

## __Build Properties, Items and Item Metadata__
These properties, items and item metadata can be used to influence builds.

#### __DesignTimeBuild (bool)__

Specifies whether the current build is a [design-time build](design-time-builds.md).

| Value                 | Description    |
|-----------------------| ---------------|
| _true_                | The current build is a design-time build.|
| _false_ or empty ('') | The current build is a normal build.|

##### __Example__
``` XML
  <Target Name="AddAdditionalReferences" BeforeTargets="ResolveAssemblyReference">
     <PropertyGroup Condition="'$(DesignTimeBuild)' == 'true'">
         <_AvoidExpensiveCalculation>true</_AvoidExpensiveCalculation>
     </PropertyGroup>

     ...
  </Target>
```

### __Build Properties__

#### __PreBuildEvent (string)__
| Language      | Default            |
|---------------| -------------------|
| C#            | empty ('')         |
| Visual Basic  | empty ('')         |

Specifies commands to execute before the build starts.

##### __Example__
``` XML
  <PropertyGroup>
    <PreBuildEvent>call CopyBuildDependencies.cmd</PreBuildEvent>
  </PropertyGroup>
```

#### __PostBuildEvent (string)__
| Language      | Default            |
|---------------| -------------------|
| C#            | empty ('')         |
| Visual Basic  | empty ('')         |

Specifies commands to execute after the build ends. To control whether these commands are run on failed or update-to-date builds, set the _RunPostBuildEvent_ property.

##### __Example__
``` XML
  <PropertyGroup>
    <PostBuildEvent>call DeployTestEnvironment.cmd</PostBuildEvent>
  </PropertyGroup>
```

#### __ProvideCommandLineArgs (bool)__

| Language      | Default            |
|---------------| -------------------|
| C#            | empty ('')         |
| Visual Basic  | empty ('')         |

Specifies whether `CoreCompile` should output the command-line arguments that were passed (or would have been passed if `SkipCompilerExecution` is `true`) to the Csc.exe and Vbc.exe executables.

| Value                 | Description    |
|-----------------------| ---------------|
| _true_                | CoreCompile will return the command-line arguments passed to Csc.exe or Vbc.exe.|
| _false_ or empty ('') | CoreCompile will not return the command-line arguments passed to Csc.exe or Vbc.exe.|

##### __Example__
``` XML
  <PropertyGroup>
    <ProvideCommandLineArgs>true</ProvideCommandLineArgs>
    <SkipCompilerExecution>true</SkipCompilerExecution>
  </PropertyGroup>

  <Target Name="PrintCommandLineArguments" AfterTargets="CoreCompile">
    
    <Message Text="Csc: @(CscCommandLineArguments)" />
    <Message Text="Vbc: @(VbcCommandLineArguments)" />

  </Target>
```

#### __RunPostBuildEvent (enum)__

| Language      | Default            |
|---------------| -------------------|
| C#            | OnBuildSuccess     |
| Visual Basic  | OnBuildSuccess     |

Specifies the conditions for the command in _PostBuildEvent_ to run.

| Value           | Description    |
|-----------------| ---------------|
| Always          | Post-build event will run regardless of whether the build succeeds.     |
| OnOutputUpdated | Post-build event will run only when the project output is different than the previous output.|
| OnBuildSuccess  | Post-build event will run if the build succeeds, regardless of whether the project output is up-to-date.|


#### __SkipCompilerExecution (bool)__

| Language      | Default            |
|---------------| -------------------|
| C#            | empty ('')         |
| Visual Basic  | empty ('')         |

Specifies whether `CoreCompile` should skip compiler execution.

| Value                 | Description    |
|-----------------------| ---------------|
| _true_                | CoreCompile will not call the Csc.exe or Vbc.exe executables.|
| _false_ or empty ('') | CoreCompile will call the Csc.exe or Vbc.exe executables.|

This property is helpful when used with the [ProvideCommandLineArgs](#providecommandlineargs_(bool)) property.

##### __Example__
``` XML
  <PropertyGroup>
    <RunPostBuildEvent>Always</RunPostBuildEvent>
  </PropertyGroup>
```

---

## __Design-Time Properties, Items and Item Metadata__
These properties, items and item metadata are used for solely for Visual Studio and design-time purposes, and have no influence on the resulting build.

### __Design-Time Properties__

#### __AppDesignerFolder (string)__

| Language      | Default            |
|---------------| -------------------|
| C#            | Properties         |
| Visual Basic  | My Project         |

Specifies the name of the _Application Designer_ folder, which by default contains source and other files pertinent to the project as a whole, including AssemblyInfo.cs/AssemblyInfo.vb.

##### __Example__
``` XML
<PropertyGroup>
    <AppDesignerFolder>Dave's Properties</AppDesignerFolder>
<PropertyGroup>
```

#### __AppDesignerFolderContentsVisibleOnlyInShowAllFiles (bool)__

| Language      | Default            |
|---------------| -------------------|
| C#            | false              |
| Visual Basic  | true               |

Specifies whether the contents of the _Application Designer_ folder are only visible when Solution Explorer's _Show All Files_ mode is turned on.

| Value                 | Description    |
|-----------------------| ---------------|
| _true_                | The __Application Designer__ folder's contents are only visible when Solution Explorer's _Show All Files__ mode is turned on.|
| _false_ or empty ('') | The __Application Designer__ folder's contents are always visible.|

##### __Example__
``` XML
<PropertyGroup>
    <AppDesignerFolderContentsVisibleOnlyInShowAllFiles>true</AppDesignerFolderContentsVisibleOnlyInShowAllFiles>
<PropertyGroup>
```

#### __DesignerFunctionVisibility (enum)__

| Language      | Default            |
|---------------| -------------------|
| C#            | Private            |
| Visual Basic  | Friend             |

Specifies the designer function access level (for example, `InitializeComponent()`).

| Value     | Description    |
|-----------| ---------------|
| _Friend_  | The designer function has friend (internal) visibility.       |
| _Private_ | The designer function has private visibility.                 |
| _Public_  | The designer has public visibility (currently not supported). |

These values map to members of the [`VSDESIGNER_FUNCTIONVISIBILITY`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.interop.vsdesigner_functionvisibility) enum in the VS SDK.

##### __Example__
``` XML
<PropertyGroup>
    <DesignerFunctionVisibility>Private</DesignerFunctionVisibility>
<PropertyGroup>
```

#### __DesignerVariableNaming (enum)__

| Language      | Default |
|---------------| --------|
| C#            | Camel   |
| Visual Basic  | VB      |

Specifies the naming convention used by the designer.

| Value   | Description    |
|---------| ---------------|
| _Camel_ | Names use camel case (e.g. `checkBox1`).       |
| _VB_    | Names use VB / Pascal case (e.g. `CheckBox1`). |

These values map to members of the [`VSDESIGNER_VARIABLENAMING`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.interop.vsdesigner_variablenaming) enum in the VS SDK.

##### __Example__
``` XML
<PropertyGroup>
    <DesignerVariableNaming>Camel</DesignerVariableNaming>
<PropertyGroup>
```

#### __DesignerHiddenCodeGeneration (enum list)__

| Language      | Default                         |
|---------------| --------------------------------|
| C#            | Declarations                    |
| Visual Basic  | Declarations | InitMethods      |

Specifies which code the designer should put in the hidden designer file.

| Value            | Description                            |
|------------------| ---------------------------------------|
| _Declarations_   | Include declarations.                  |
| _InitMethods_    | Include member initialization members. |
| _EventMethods_   | Include event methods.                 |

These values map to members of the [`__VSDESIGNER_HIDDENCODEGENERATION`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.interop.__vsdesigner_hiddencodegeneration) enum in the VS SDK.

##### __Example__
``` XML
<PropertyGroup>
    <DesignerHiddenCodeGeneration>Declarations;InitMethods</DesignerHiddenCodeGeneration>
<PropertyGroup>
```

#### __ProjectGuid (GUID) [deprecated]__

| Language      | Default            |
|---------------| -------------------|
| C#            | empty ('')         |
| Visual Basic  | empty ('')         |

Specifies a unique key of a project within a Visual Studio solution. In the new [C#, F# and Visual Basic project system](http://github.com/dotnet/project-system), this is now optional.

##### __Example__
``` XML
<PropertyGroup>
    <ProjectGuid>{3B812812-7B6F-4327-948D-DF7CD21EFE4C}</ProjectGuid>
<PropertyGroup>
```
# Architecture

|||
|-------:|:----------|
| ![layers01](https://user-images.githubusercontent.com/1103906/61422795-9b549400-a950-11e9-8164-c8fa67aa5ae3.png) | ![layers02](https://user-images.githubusercontent.com/9797472/27418842-8564a266-56d2-11e7-92c6-456116ee0c65.png)|

## Layering Rules:

1. Assemblies cannot depend on the layer above it
2. Assemblies below the Visual Studio layer cannot depend on the Visual Studio SDK (no dependency on IVsXXX) nor any CPS-VS assembly. This layer and below should be hostable and usable outside of Visual Studio.

### Host-Agnostic Layer

|Assembly|Description|
|:-------|:----------|
|__Microsoft.VisualStudio.ProjectSystem.Managed__| Contains components that are shared between C#, F# and Visual Basic projects agnostic of host.|

### Visual Studio Layer

|Assembly|Description|
|:-------|:----------|
|__Microsoft.VisualStudio.ProjectSystem.Managed.VS__| Contains components that are shared between C#, F# and Visual Basic projects. |

### Visual Studio Designer Layer

|Assembly|Description|
|:-------|:----------|
|__Microsoft.VisualStudio.AppDesigner__| Contains the "Application Designer", which hosts property pages in a document window.|
|__Microsoft.VisualStudio.Editors__| Contains resources and settings editors, and C#, F# and Visual Basic property pages.|
# Coding Conventions

## Code

We use the same coding style conventions as outlined in [.NET Framework Coding Styles](https://github.com/dotnet/corefx/blob/master/Documentation/coding-guidelines/coding-style.md), with the following additions:

- **DO** put one type per file, including nested types. Files containing a nested type, should follow the `Parent.NestedType.cs` convention. Generic types should follow the ``GenericWithOneTypeParameter`1.cs``, ``GenericWithTwoTypeParameters`2.cs`` convention. If you have a single generic type,`GeneraticWithOneTypeParameter.cs` is acceptable.
- **DO NOT** use regions.
- **DO** sort members in classes in the following order; fields, constructors, events, properties and then methods.
- **DO** flavor private fields over private properties.
- **DO** case internal fields as `PascalCased` not `_camelCased`.

The majority of the guidelines, where possible, are enforced via the [.editorconfig](https://github.com/dotnet/project-system/blob/master/.editorconfig) in the root the repository.

## MEF

- **DO** use constructor injection over property/field injection.
  
- **DO** use MEF imports over direct usage of `IComponentModel`.

## VS APIs

- **DO** flavor `IVsUIService<T>` and `IVsUIService<TService, TInterface>` over usage of `IServiceProvider`.
  
`IVsUIService` enforces UI thread access which prevents accidental RPC calls from a background thread.
  
- **DO** flavor `IVsService<T>` and `IVsService<TService, TInterface>` over usage of `IAsyncServiceProvider`.
  
`IVsService` ensures casts are performed on the UI thread which prevents accidental RPC calls from a background thread.

- **DO** flavor `HResult` over `VSConstants` and raw constants.

- **DO** flavor `HierarchyId` over `VSConstants.VSITEMID` and raw constants.

## Tests

- **DO** flavor a single Assert per unit test.

- **DO** use the `Method_Setup_Behavior` naming style for unit tests, for example, `GetProperty_NullAsName_ThrowsArgument` or `CalculateValues_WhenDisposed_ReturnsNull`.

- **DO** flavor static `CreateInstance` for creating the object under test versus directly calling the constructor

This reduces the amount of refactoring/fixup needed when adding a new import to a service.

# Guidelines

## Data

- **DO NOT** mix snapshot and "live" project data in the same component. 

For example, listening to data flow blocks from `IProjectSubscriptionService` and then reading properties from `ProjectProperties` within the callback will lead to inconsistent results. The dataflow represents a "snapshot" of the project from changes in the past, whereas ProjectProperties represents the actual live project. These will not always agree. The same applies to consuming other CPS APIs from within a dataflow block, the majority of them use live data to provide results and hence will return results inconsistent with the snapshot that you are reading in the dataflow.

- **DO NOT** parse or attempt to reason about the values of properties that make up the dimensions for a project configuration; `$(Configuration)`, `$(Platform)` and `$(TargetFramework)`, and their plural counterparts; `$(Configurations)`, `$(Platforms)` and `$(TargetFrameworks)`.

These properties are user "aliases" and should only be used for conditions, display and grouping purposes. Instead, the project system should be using their canonical equivalents; `$(PlatformTarget)` instead of `$(Platform)`, and `$(TargetFrameworkMoniker)` instead of `$(TargetFramework)`.

## Threading

- **DO** follow the [3 threading rules](https://github.com/Microsoft/vs-threading/blob/master/doc/threading_rules.md#3-threading-rules) inside Visual Studio.

- **DO NOT** call `IProjectThreadingService.ExecuteSynchronously` or `JoinableTaskFactory.Run` from a ThreadPool thread that marshals to another thread (such as via `JoinableTaskFactory.SwitchToMainThreadAsync` or calling an STA-based `IVsXXX` object).
If you synchronously block on other async code, often that code needs to run or finish on a ThreadPool thread. When the number of threads in the ThreadPool reaches a certain threshold, the ThreadPool manager slows down thread creation and only adds a new thread to the pool every 250 - 500ms. This can result in random UI deadlocks for short periods of time while the code on the UI thread waits for a new thread to be spun up. See [ThreadPool Starvation](https://github.com/Microsoft/vs-threading/blob/master/doc/threadpool_starvation.md) for more information.

- **AVOID** marking `await` calls with `ConfigureAwait(true)` or `ConfigureAwait(false)`.

We follow the [Visual Studio guidelines](https://github.com/Microsoft/vs-threading/blob/master/doc/cookbook_vs.md#should-i-await-a-task-with-configureawaitfalse) around `ConfigureAwait` usage.
# Debugging Tips

- [Setting up your Debugging Environment](/docs/repo/debugging/setting-up-environment.md)
- [Design-Time Builds](/docs/repo/debugging/design-time-builds.md)
- [Debugging Async Test Hangs](/docs/repo/debugging/async-test-hangs.md)
- [CPS Tracing](/docs/repo/debugging/tracing.md)
- [Project System Logging](/docs/repo/debugging/logging.md)
- [Capabilities](/docs/repo/debugging/capabilities.md)
- [Crash Dumps, UI Delays and Hang Data](/docs/repo/debugging/watson.md)
- [.NET SDK](/docs/repo/debugging/sdk.md)
- [Visual Studio](/docs/repo/debugging/visualstudio.md)
# Dependencies Node Roadmap

This document describes, at a high level, the design and implementation of the Dependencies node with pointers to the important types.

Let's start at the top and work our way down. There are two fundamentally different paths that dependency information takes from the Project System to Solution Explorer. Direct dependencies go through CPS, whereas transitive dependencies generally go through graph node providers.

## Overview

### The CPS View of Dependencies

On the CPS side the project tree is composed of instances of the `IProjectTree` and `IProjectItemTree` interfaces. `IProjectTree` captures the structure of the tree (e.g. it has properties to access the parent and child nodes) and the "UI" aspects of the node&mdash;name, icons, visibility, etc. An `IProjectItemTree` captures all of that but also represents a concrete item within the project like a file, assembly reference, or NuGet package.

An `IProjectTree` is immutable. When a part of the tree needs to be updated, we need to replace it and form a new tree.

Components wishing to add items to the project tree must implement and export the `IProjectTreeProvider` interface. In practice we implement the interface by deriving from the abstract `ProjectTreeProviderBase` class provided by CPS. In general, we receive events/messages from CPS detailing changes to the project, generate an updated `IProjectTree`, and then pass it back to CPS via `ProjectTreeProviderBase.SubmitTreeUpdateAsync`.

### The Graph Node Provider View of Dependencies

On the Graph Node side, transitive dependencies are represented as `GraphNode` instances and are frequently associated with `IGraphContexts`. In contrast to `IProjectTree`s, graphs are not realized in their entirety "up front" nor are they immutable. Instead, a graph starts with a small set of initial nodes. As the user expands nodes or searches within the graph an `IGraphProvider` implementation is asked to mutate the graph via an `IGraphContext`. The `IGraphContext` contains the current graph, a description of the operation at hand (checking if a node has children, getting the set of children, search for nodes matching certain text, etc.) and a set of "input" nodes marking the starting point for the operation. The `IGraphProvider` then adds `GraphNodes` to the graph as appropriate.

### The Project System View of Dependencies

Internally every individual dependency (both direct and transitive) is represented as an [`IDependency`][IDependency].

All the [`IDependency`][IDependency]s for a given target framework in a given project are collected together into a [`TargetedDependenciesSnapshot`][TargetedDependenciesSnapshot]. All of those for a given project are, in turn, collected into a [`DependenciesSnapshot`][DependenciesSnapshot].

The [`DependenciesSnapshotProvider`][DependenciesSnapshotProvider] is responsible for providing access to the current [`DependenciesSnapshot`][DependenciesSnapshot] and firing events when the snapshot has changed.

Much of the code for the Dependencies node is concerned with creating [`IDependency`][IDependency]s and translating them into new `IProjectTree`s when they change.

## CPS/Project System Interaction

In general, items _directly_ referenced by the project file (e.g., through `Reference`, `ProjectReference`, and `Analyzer` items in the project file) are represented with `IProjectTree` nodes as opposed to `GraphNodes`. This makes it possible for them to be represented in the project's `IVsHierarchy` and, crucially, makes it easier to code the sorts of interactions users expect for these items. For example, a user should be able to right-click on an assembly reference and remove it, or modify the properties of an assembly reference.

> Aside: There are exceptions to this. In practice analyzers are not directly referenced but rather brought in as part of a NuGet package. We still represent all analyzers as `IProjectTree` items directly under the "Analyzers" node. This makes it much easier for the C#/VB language service to add nodes for each diagnostic underneath the analyzer's node, and it makes it easy for the user to find so they can check the severity of the diagnostic and potentially change it using the context menu.

### DependenciesProjectTreeProvider

The primary connection point between CPS and the Dependencies node is the [`DependenciesProjectTreeProvider`][DependenciesProjectTreeProvider], implementing the `IProjectTreeProvider` interface. It is directly responsible for the following:

1. Creating the `IProjectTree` for the "Dependencies" node itself (children are handled elsewhere).
2. Handling explicit commands to copy or remove a node underneath the "Dependencies" node.
3. Mapping back and forth between `IProjectTree` instances and paths.
4. Listening for changes to the set of dependencies via the [`DependenciesSnapshotProvider`][DependenciesSnapshotProvider], delegating to the [`IDependenciesTreeViewProvider`][IDependenciesTreeViewProvider] to rebuild the tree underneath the Dependencies node, and submitting the updated tree back to CPS.

### Generating Dependencies

As evaluations and design-time builds occur, CPS pushes project changes through TPL Dataflow blocks (available via `IProjectSubscriptionService`, where `ProjectRuleSource` provides evaluation data, and `JointRuleSource` provides design-time build data).

Various implementations of [`IDependenciesRuleHandler`][IDependenciesRuleHandler] exist, and each specifies the set of rules they wish to handle (e.g. `PackageReference`, `ResolvedProjectReference`, etc.). The abstract class [`DependenciesRuleHandlerBase`][DependenciesRuleHandlerBase] exists to make implementing [`IDependenciesRuleHandler`][IDependenciesRuleHandler] easier.

The [`DependencyRulesSubscriber`][DependencyRulesSubscriber] (implementing [`IDependencyCrossTargetSubscriber`][IDependencyCrossTargetSubscriber]) subscribes via Dataflow to the union of rules specified by the handlers. When updates are received, a [`CrossTargetDependenciesChangesBuilder`][CrossTargetDependenciesChangesBuilder] is instantiated and each handler is given a chance to add/update/remove [`IDependencyModel`][IDependencyModel] instances through the builder. Once complete, the `IDependencyCrossTargetSubscriber.DependenciesChanged` event is fired, carrying dependency model changes.

Each project has an instance of [`DependenciesSnapshotProvider`][DependenciesSnapshotProvider] that holds the latest `DependenciesSnapshot` object. It imports `IDependencyCrossTargetSubscriber` implementations (such as `DependencyRulesSubscriber`) and subscribes to their `DependenciesChanged` events. When these events fire, the current snapshot is combined with changes to produce a new snapshot. That snapshot is then propagated via the `DependenciesSnapshotProvider.SnapshotChanged` event.

This `SnapshotChanged` event is then handled by:

- [`DependenciesProjectTreeProvider`][DependenciesProjectTreeProvider] to update the tree, and
- [`AggregateDependenciesSnapshotProvider`][AggregateDependenciesSnapshotProvider] which fires a solution-level `SnapshotChanged` event (useful for P2P references and graph updates, for example.)

### Translating snapshots to trees

Most of the work of translating [`IDependency`][IDependency]s to `IProjectTree`s is done by [`DependenciesTreeViewProvider`][DependenciesTreeViewProvider] (implementing [`IDependenciesTreeViewProvider`][IDependenciesTreeViewProvider]). It takes a [`DependenciesSnapshot`][DependenciesSnapshot] and generates the nodes for the target frameworks, the groupings under each framework, (Assemblies, Analyzers, Packages, Projects, etc.), and the top-level nodes under each of those groupings. In the common case that a project has a single target framework it leaves out the framework node entirely and simply hangs the different groupings directly off the `IProjectTree` for the Dependencies node.

The [`DependenciesTreeViewProvider`][DependenciesTreeViewProvider] traverses down the existing `IProjectTree` and the new [`DependenciesSnapshot`][DependenciesSnapshot] in parallel, starting from the Dependencies node itself and proceeding on to target framework, groupings, and then the individual top-level dependencies. Along the way it incrementally generates new `IProjectTree`s as it finds dependencies that have been updated, added, or removed.

> Aside: The `IProjectTree` nodes are intentionally updated from top to bottom as it prevents the Solution Explorer from collapsing expanded nodes during the update. At the very least this would be visually distracting to the user.

[`IDependency`][IDependency]s are not translated directly into `IProjectTree`s. They are first converted to [`IDependencyViewModel`][IDependencyViewModel]s and those in turn become the `IProjectTree`s. This makes it a little easier to create the `IProjectTree`s for targets and groups (e.g. the Assemblies, NuGet, Projects, etc. nodes) which are not themselves [`IDependency`][IDependency]s. In some cases a [`IDependencyModel`][IDependencyModel] may be converted directly to a [`IDependencyViewModel`][IDependencyViewModel].

### Identifiers

#### `IDependencyModel` Identifiers

Instances of [`IDependencyModel`][IDependencyModel]'s produced by an [`IProjectDependenciesSubTreeProvider`][IProjectDependenciesSubTreeProvider] must have an `Id` propety that's unique to that provider and that project.

For dependencies obtained via MSBuild evaluations (Packages, Assemblies, etc...) the `Id` is just the `OriginalItemSpec`.

#### `IDependency` Identifiers

Once a dependency model is integrated into a dependencies snapshot as an [`IDependency`][IDependency], its `Id` will be constructed from the target framework, provider type and model ID. For example: `netstandard2.0/nugetdependency/newtonsoft.json`

This allows the ID to be unique within both the provider and the target framework.

## Graph/Project System Interaction

The direct dependencies of a project will often bring in a number of transitive dependencies. For example, you may have a direct dependency on a NuGet package via a `PackageReference` element in the project file. That package causes transitive dependencies on the assemblies and analyzers within it as well as other packages it depends on. A `ProjectReference` may add transitive dependencies on other projects and packages. These dependencies form a directed graph and as such we can't properly represent them via `IProjectTree`s.

Also, the set of transitive dependencies may be very large, potentially much larger than the set of direct dependencies. For memory reasons we don't want to realize the full graph "up front". 

At the same time the user can only interact with these items in a very limited way&mdash;there's no way for them to delete an individual assembly brought in by a NuGet package for example.

These requirements lead us to represent transitive dependencies as `Microsoft.VisualStudio.GraphModel.GraphNode`s.

### DependenciesGraphProvider

The primary connection point between the Graph Nodes and the Project System is the [`DependenciesGraphProvider`][DependenciesGraphProvider] class, via the `IGraphProvider` interface. It is directly responsible for the following:

1. Specifying which graph operations it supports, via the `GetCommands` property. The only supported standard command is `GraphCommandDefinition.Contains` which is used to find the children of a given graph node.
2. Delegate the actual implementation of graph operations to various [`IDependenciesGraphActionHandler`][IDependenciesGraphActionHandler]s via the `BeginGetGraphData` method.
3. Handle the low-level mechanics of adding and removing nodes from the graph via its [`IDependenciesGraphBuilder`][IDependenciesGraphBuilder] implementation.

### Generating new `GraphNode`s

New `GraphNode`s are added to the graph as a result of operations initiated by the user.

For example, when the user expands a NuGet package node:

1. The `IGraphProvider.BeginGetGraphData` implementation in [`DependenciesGraphProvider`][DependenciesGraphProvider] is called with an `IGraphContext` describing the current graph, the input node (e.g. the node for the NuGet Package) and the operation (e.g. "get the children of the input node").
2. Each implementation of [`IDependenciesGraphActionHandler`][IDependenciesGraphActionHandler] that can handle the request is asked to do so.
3. We retrieve the current [`DependenciesSnapshot`][DependenciesSnapshot] for the project as well as the [`IDependency`][IDependency] for the input node (via [`IAggregateDependenciesSnapshotProvider`][IAggregateDependenciesSnapshotProvider]/[`DependenciesSnapshotProvider`][DependenciesSnapshotProvider]).
4. We find the first [`IDependenciesGraphViewProvider`][IDependenciesGraphViewProvider] that supports the given [`IDependency`][IDependency] and ask it to build up the corresponding parts of the graph.
5. The [`IDependenciesGraphViewProvider`][IDependenciesGraphViewProvider] decides what nodes to add to the graph, and calls [`IDependenciesGraphBuilder`][IDependenciesGraphBuilder]`.AddGraphNode` (implemented by [`DependenciesGraphProvider`][DependenciesGraphProvider]) to handle the actual mechanics.

### Connecting `GraphNode`s to `IProjectTree` nodes

CPS and the core graph logic automatically create `GraphNode`s for `IProjectTree` nodes marked with the `ProjectTreeFlags.Common.ResolvedReference` flag. For example, we will create an `IProjectTree` for a top-level NuGet package and an associated `GraphNode` will be generated automatically. We will later see this `GraphNode` as an input node in an `IGraphContext` and create and link new `GraphNode`s for its transitive dependencies.

While we don't need to create these top-level `GraphNode`s we do sometimes need to adjust their properties.

### Tracking changes to the graph

Changes to the dependencies may require that we update the graph nodes already produced. The [`DependenciesGraphChangeTracker`][DependenciesGraphChangeTracker] holds weak references to all the graphs that may need to be updated due to dependency changes, and subscribes to the [`IAggregateDependenciesSnapshotProvider`][IAggregateDependenciesSnapshotProvider]`.SnapshotChanged` event.

Whenever this event fires we find the corresponding [`IDependency`][IDependency], find the [`IDependenciesGraphViewProvider`][IDependenciesGraphViewProvider] that supports it, and delegate to the provider's `ApplyChanges` method. This generates lists of graph nodes to add and remove based on the current graph contents and the current project snapshot contents. The [`IDependenciesGraphBuilder`][IDependenciesGraphBuilder] is then called to handle the actual additions and removals.

### Identifiers

Each `GraphNode` must have a unique ID of type `Microsoft.VisualStudio.GraphModel.GraphNodeId`.

`GraphNodeId` is a recursive type, meaning an instance may be comprised of several partial `GraphNodeId` objects. This composition is performed by `GraphNodeId.GetNested`.

As mentioned earlier, `GraphNode`s are automatically created for `IProjectTree` nodes marked with the `ProjectTreeFlags.Common.ResolvedReference` flag. These graph nodes are created with IDs comprising two sub-IDs:

1. `Assembly` which identifies the project (a `Uri` of full path to the containing project file)
2. `File` which identifies the graph node within that project (a `Uri` modelling something unique about that node)
   - For top level dependency nodes, this is the numeric ID assigned to the node as a string prefixed with `>` (e.g. `>56`)
   - For child nodes (created lazily when the user expands top level nodes), this is the composite [`IDependency.Id`][IDependency] discussed above (e.g. `netstandard2.0/nugetdependency/newtonsoft.json`)

If a project is renamed, the `Assembly` URI of graph nodes within that project are automatically updated to reflect the new project path.

## Extensibility Model

Project flavors can extend the Dependencies node with additional sub-trees. To do so:

- Implement and export an [`IProjectDependenciesSubTreeProvider`][IProjectDependenciesSubTreeProvider] implementation per sub-tree
- Provide a custom implementation of [`IDependencyModel`][IDependencyModel]
- Potentially implement `IProjectTreeProvider` (usually by deriving from `ProjectTreeProviderBase`)

The _Web Tools Extensions_ project is a good example of a project flavor that does this.


[AggregateCrossTargetProjectContext]:     /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/CrossTarget/AggregateCrossTargetProjectContext.cs "AggregateCrossTargetProjectContext.cs"
[IDependenciesRuleHandler]:               /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/CrossTarget/IDependenciesRuleHandler.cs "IDependenciesRuleHandler.cs"
[DependenciesProjectTreeProvider]:        /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/DependenciesProjectTreeProvider.cs "DependenciesProjectTreeProvider.cs"
[DependenciesTreeViewProvider]:           /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/DependenciesTreeViewProvider.cs "DependenciesTreeViewProvider.cs"
[IDependenciesGraphActionHandler]:        /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/Actions/IDependenciesGraphActionHandler.cs "IDependenciesGraphActionHandler.cs"
[TrackChangesGraphActionHandler]:         /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/Actions/TrackChangesGraphActionHandler.cs "TrackChangesGraphActionHandler.cs"
[DependenciesGraphChangeTracker]:         /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/DependenciesGraphChangeTracker.cs "DependenciesGraphChangeTracker.cs"
[DependenciesGraphProvider]:              /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/DependenciesGraphProvider.cs "DependenciesGraphProvider.cs"
[IDependenciesGraphBuilder]:              /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/IDependenciesGraphBuilder.cs "IDependenciesGraphBuilder.cs"
[IDependenciesGraphViewProvider]:         /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/ViewProviders/IDependenciesGraphViewProvider.cs "IDependenciesGraphViewProvider.cs"
[ProjectGraphViewProvider]:               /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/GraphNodes/ViewProviders/ProjectGraphViewProvider.cs "ProjectGraphViewProvider.cs"
[IDependencyModel]:                       /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/IDependencyModel.cs "IDependencyModel.cs"
[IDependenciesTreeViewProvider]:          /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/IDependenciesTreeViewProvider.cs "IDependenciesTreeViewProvider.cs"
[IProjectDependenciesSubTreeProvider]:    /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/IProjectDependenciesSubTreeProvider.cs "IProjectDependenciesSubTreeProvider.cs"
[IDependencyViewModel]:                   /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Models/IDependencyViewModel.cs "IDependencyViewModel.cs"
[AggregateDependenciesSnapshotProvider]:  /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/AggregateDependenciesSnapshotProvider.cs "AggregateDependenciesSnapshotProvider.cs"
[DependenciesSnapshot]:                   /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/DependenciesSnapshot.cs "DependenciesSnapshot.cs"
[IDependenciesSnapshotFilter]:            /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/Filters/IDependenciesSnapshotFilter.cs "IDependenciesSnapshotFilter.cs"
[IAggregateDependenciesSnapshotProvider]: /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/IAggregateDependenciesSnapshotProvider.cs "IAggregateDependenciesSnapshotProvider.cs"
[DependenciesSnapshot]:                   /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/DependenciesSnapshot.cs "DependenciesSnapshot.cs"
[IDependency]:                            /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/IDependency.cs "IDependency.cs"
[TargetedDependenciesSnapshot]:           /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Snapshot/TargetedDependenciesSnapshot.cs "TargetedDependenciesSnapshot.cs"
[CrossTargetDependenciesChangesBuilder]:  /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Subscriptions/CrossTargetDependenciesChangesBuilder.cs "CrossTargetDependenciesChangesBuilder.cs"
[DependenciesRuleHandlerBase]:            /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Subscriptions/RuleHandlers/DependenciesRuleHandlerBase.cs "DependenciesRuleHandlerBase.cs"
[DependencyRulesSubscriber]:              /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Subscriptions/DependencyRulesSubscriber.cs "DependencyRulesSubscriber.cs"
[DependenciesSnapshotProvider]:           /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Subscriptions/DependenciesSnapshotProvider.cs "DependenciesSnapshotProvider.cs"
[IDependencyCrossTargetSubscriber]:       /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Subscriptions/IDependencyCrossTargetSubscriber.cs "IDependencyCrossTargetSubscriber.cs"
[ProjectRuleHandler]:                     /src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/ProjectSystem/VS/Tree/Dependencies/Subscriptions/ProjectRuleHandler.cs "ProjectRuleHandler.cs"
# Features

This repository contains the following broad features:

## C# and Visual Basic project system for .NET Core/.NET Standard/Shared Projects
[Host Agnostic Source](/src/Microsoft.VisualStudio.ProjectSystem) | [Visual Studio Source](/src/Microsoft.VisualStudio.ProjectSystem.VS)

## Application Designer ("AppDesigner")
[Source](/src/Microsoft.VisualStudio.AppDesigner)

![Visual Basic project system](/docs/repo/images/appdesigner.png?raw=true)

## Property Pages
[Source](/src/Microsoft.VisualStudio.Editors/PropPages)

## Resources Editor
[Source](/src/Microsoft.VisualStudio.Editors/ResourceEditor)

![Resources Editor](/docs/repo/images/resourceseditor.png?raw=true)

## Settings Designer
[Source](/src/Microsoft.VisualStudio.Editors/SettingsDesigner)

![Settings Designer](/docs/repo/images/settingsdesigner.png?raw=true)
# Getting Started

#### Prerequisites
- [Visual Studio 16.3 Preview 2 or higher](https://visualstudio.microsoft.com/vs/preview/)
- GitHub account
- Basic Git experience: https://try.github.io/

All commands below are run under a [Visual Studio Developer Prompt](https://msdn.microsoft.com/en-us/library/ms229859(v=vs.150).aspx).

## Code

Contribution to this repository is via the [fork model](https://help.github.com/articles/fork-a-repo/). Contributors push changes to their own "forked" version of project-system, and then submit a pull request into it requesting those changes be merged.

To get started:

1. Fork the repo by clicking Fork in the top right corner:

![image](https://user-images.githubusercontent.com/1103906/44329309-7ab55d00-a4a7-11e8-9d1f-74a91f5229f5.png)

2. From a Visual Studio Developer Prompt, run (replacing _[user-name]_ with your GitHub user name):

```
\> git clone https://github.com/[user-name]/project-system
\> cd project-system
\project-system> git remote add upstream https://github.com/dotnet/project-system
\project-system> git remote set-url --push upstream no_push
```

The last command prevents an accidental push to this repository without going through a pull request.

After running above, `git remote -v` should show something similar to the following:
```
\project-system> git remote -v 

origin  https://github.com/davkean/project-system (fetch)
origin  https://github.com/davkean/project-system (push)
upstream        https://github.com/dotnet/project-system (fetch)
upstream        no_push (push)
```

## Build

### Command-line

From within a [Visual Studio Developer Prompt](https://docs.microsoft.com/en-us/dotnet/framework/tools/developer-command-prompt-for-vs), from the repo root, run:

```
project-system> build.cmd
```

This builds, runs tests and deploys to an experimental instance of Visual Studio.

### Visual Studio
From within [Visual Studio 2019](https://visualstudio.microsoft.com/downloads/), open _ProjectSystem.sln_.

Inside Visual Studio, you can build, run tests and deploy.

## Debugging/Deploying

By default when you build inside Visual Studio or the command-line, the project system and other binaries gets deployed to the _Exp_ experimental instance of Visual Studio. They will automatically _override_ any binaries that come with Visual Studio when you launch that instance.

First of all, [setup your debugging environment](https://github.com/dotnet/project-system/blob/master/docs/repo/debugging/setting-up-environment.md).

### Command-line

From the command-line, after you've run `build.cmd` you can launch a Visual Studio instance with your recently built bits with:

```
project-system> launch.cmd
```

### Visual Studio

To start debugging:

1. Open __ProjectSystem.sln__
2. Press _F5_

If this is your first launch of the project system, or _ProjectSystem_ experimental instance, press _CTRL+F5_ to pre-prime and avoid a _long_ start up time.

For tips, see [Debugging Tips](debugging-tips.md)

### Deploying to a different hive

When testing inconjunction with other repositories, it's handy to be able to deploy to the same hive so that you can test them together.

Both Visual Studio and command-line respect the `ROOTSUFFIX` environment variable:

```
project-system> set ROOTSUFFIX=RoslynDev

project-system> build.cmd
project-system> launch.cmd
```

```
project-system> set ROOTSUFFIX=RoslynDev

project-system> devenv ProjectSystem.sln
```

Alternatively, both `build.cmd` and `launch.cmd` provide a `/rootsuffix` switch:

``` 
project-system> build.cmd /rootsuffix RoslynDev
project-system> launch.cmd /rootsuffix RoslynDev
```

## Testing 

### Project System
While the long term goal is to have all C#, F# and Visual Basic projects use this project system, currently only .NET Core, .NET Standard and Shared Projects do. If you want to test other project types, you can manually create a project to test this:

1. __File__ -> __New__ -> __Project__ -> __C#__ -> __Templates__ -> __Visual C#__ -> __Windows__ -> __Console App (.NET Framework)__
2. Right-click on the project and choose __Open in File Explorer__
3. __File__ -> __Close Solution__
4. In __File Explorer__, rename project from _[project].csproj_ -> _[project].msbuildproj_
5. __File__ -> __Open__ -> __Project/Solution__ and browse to the project you just renamed and choose __Open__

### AppDesigner, Settings, Resource Editors and Property Pages
Both the new project system and the existing project system use the features built from this repository.

## Code Coverage

### Visual Studio

You can collect code coverage within Visual Studio, to do so, do the following:

1. __Test__ -> __Test Settings__ -> __Select Test Settings File__
2. In __Open Settings Files__, browse to and select _src\CodeCoverage.runsettings_. This will exclude files from the coverage run that are not part of the product.
3. Choose __Test__ -> __Analyze Code Coverage__ -> __All Tests__
# Basic
1. Open
   a. Language service is hooked up correctly
2. Build
3. Debug
4. Close
5. Switch configuration
6. Add sln configuration
7. Add project configuration
8. Open with sln config not matching project configs
9. Open with upgrade
10. Open with projects missing on disk
11. Add/Remove Reference
12. Add/Remove NuGet Package
13. Add/Remove ComReference
14. Add/Remove ProjectReference
15. Add/Rename/Remove file
16. Add/Rename/Remove folder
17. DTE Properties/Properties Grid for Projects, folders, files (Expected names and values, editable)
18. CodeModel and other DTE APIs
19. Project Properties pages
20. Shared Projects
21. Cross language P2P refs (C# <--> VB)
22. Cross language P2P refs (C#/VB <--> C++)
23. Single file generators
24. Class designer support
	
# CPS Only
1. Edit project file
2. Dependencies node
3. Globs work as expected (file not munged with other edits/when adding/removing files)
4. Multi-targeting
5. Launch profiles
6. Publish to Azure
7. Auto-restore on open
	
# CSProj only
1. Winforms designer
2. Xaml designer
3. Publish to ClickOnce
4. Sql debugging
5. Remote debugging
6. Add Service reference
7. Add Web reference
8. Add Data Source
9. Code Analysis
10. Code metrics
11. Fakes
12. T4 templates
13. Zero impact projects ("Save new projects when created")
14. Simplified configurations ("Show advanced build configurations")
## Loading components

Components that are exported through MEF will be automatically discovered as necessary by any imports that exist, but loading and initializing is still a manual process. Additionally, components are typically applied to specific capabilities which can be dynamic, meaning they can be applied or unapplied throughout the lifetime of a project, when:

* A targets file is present, which carries the capability via `<ProjectCapability Include="Foo"/>`
* A package is installed with the capability
* It comes and goes dynamically from other sources

A capability can also be fixed for the lifetime of a project, in which case it cannot be changed without reloading the project. Fixed capabilities tend to come from `[assembly: ProjectTypeRegsitration(Capabilities = "A;B;C")]`.

Why is a "targets file" considered dynamic? Because the outer UnconfiguredProject "inherits" capabilities from any active configuration, targets are only ever evaluated inside a configuration. There is a time early in a project's lifetime before `ProjectLoadCheckpoint.ProjectInitialCapabilitiesEstablished` where there is no active configuration, or the active configuration's capabilities haven't been applied to the UnconfiguredProject. Also, the active configuration can change causing a new set of capabilities to be applied to the UnconfiguredProject.

### The old way

The old way to get your component loaded is to use either the `[ProjectAutoLoad]` or `[ConfiguredProjectAutoLoad]` attributes on a method within your component.

The dynamic nature of capabilities presents a problem however; `[ProjectAutoLoad]` says "load me automatically at the stage I've indicated" but that can be before the set of capabilities you are "applied to" have even been determined. You've said "I need to be loaded before we've determined the active configuration", but your capability doesn't appear until after that.

Another problem is that there's no mechanism to unload the component if the capability disappeared when someone changed the active configuration.

### The new way

To handle these situations, we've decided that changes to capabilities that are applied to `[ProjectAutoLoad]` components, if we've already loaded them or the stage has passed where we should have loaded them, will cause us to automatically [reload the project](https://github.com/Microsoft/VSProjectSystem/blob/master/doc/overview/dynamicCapabilities.md#critical-capabilities-changes-error). We did this for compatibility mostly. We did also consider disposing autoload components if their capability disappeared, but it was very likely that their dependencies probably weren't prepared for that.

To handle these dynamic capabilities that come and go without requiring us to reload the project, we introduced a new concept `IProjectDynamicLoadComponent`; LoadAsync gets called when the capability first appears, UnloadAsync gets called when the capability disappears. Most of our newish components opt into this. This isn't a direct replacement for [ProjectAutoLoad] or [ConfiguredProjectAutoLoad] because components will get loaded later (typically around `ProjectInitialCapabilitiesEstablished`), but is a requirement if you are a dynamic capability.

To help with implementing these dynamic components we also have `AbstractMultiLifetimeComponent` which serves to simplify the lifetime of a component that is loaded and unloaded multiple times.
### Roadmap

The first release of the project system ("15.0") was heavily focused on supporting .NET Core scenarios and parity with [VS 2015 project.json tooling](https://github.com/dotnet/project-system/issues?utf8=%E2%9C%93&q=label%3AParity-XProj%20). This will continue through the Visual Studio 15.x.x updates and releases. In 16.0, we'll start focusing on [feature parity](https://github.com/dotnet/project-system/labels/Parity-Legacy) with the legacy project system and support for .NET Core 3.0.

|Release|Branches|Version|Description|
|-------|--------|--------|--------|
|[15.0.x](https://github.com/dotnet/project-system/milestone/4)|[15.0.x](https://github.com/dotnet/project-system/tree/dev15.0.x)|Visual Studio 2017|This release is considered done and will only be patched for security-related issues.
|[15.9](https://github.com/dotnet/project-system/milestone/21)|[15.9.x](https://github.com/dotnet/project-system/tree/dev15.9.x)|Visual Studio 2017|This release is considered done, and only impactful bugs, crashes and hangs that block _major_ scenarios will be taken.
|[16.x](https://github.com/dotnet/project-system/milestone/25)|N/A|Visual Studio 2019| This release will be focused on [feature parity](https://github.com/dotnet/project-system/labels/Parity-Legacy) with the legacy project system, support for [.NET Core 3.0](https://github.com/dotnet/project-system/labels/Feature-.NET-Core), [WinForms](https://github.com/dotnet/project-system/labels/Feature-WinForms) and [WPF](https://github.com/dotnet/project-system/labels/Feature-XAML).
|[Backlog](https://github.com/dotnet/project-system/milestone/5)|none| |Uncommitted features/bugs.
# Rules of the Project System

The following are a set of rules and guidelines that we should follow as we write the new project system.

## Upgrade
- Developers will not be prompted to upgrade, convert or otherwise change their existing projects when opened in Visual Studio 2017. 
    
- Existing projects once opened in Visual Studio 2017 and saved, can be reopened in previous versions of Visual Studio right back to Visual Studio 2010

The exception the above rules are XProj-based projects which will be converted to csproj-based projects in Visual Studio 2017.

## Project Files
- New properties and items that are used only for Visual Studio or designer purposes should not be persisted in the project file. This file should be treated as a "user" file and as such, should be readable, easily editable and understandable by the user.

## Visual Studio
- Project System behavioral differences between languages (C#, Visual Basic or F#) or project types (WinForms, Web, etc), such as which files to nest or hide by default, should be configurable and persisted in the associated Microsoft.[Language].Designer.targets file.

# Up-to-date Check Implementation

See [this documenent](../up-to-date-check.md) for more general information about the up-to-date check.

The `IBuildUpToDateCheckProvider` interface (from CPS) has two members:

- `IsUpToDateCheckEnabledAsync`, which is serviced by `IProjectSystemOptions.GetFastUpToDateLoggingLevelAsync`
- `IsUpToDateAsync` which performs the checks described below

## What is checked

There are several checks which must all pass. 

All :heavy_check_mark: statements must be true for everything to be up to date.

Checks occur in the order listed.

As soon as one returns `false`, we are _not_ up to date and return immediately without performing further checks.

### Environment

- :heavy_check_mark: The query `BuildAction` is `Build`
- :heavy_check_mark: `IProjectAsynchronousTasksService.IsTaskQueueEmpty(ProjectCriticalOperation.Build)` is `true`
- :heavy_check_mark: We have received project and item data via Dataflow
- :heavy_check_mark: The current project's version is up to date with data received via Dataflow
- :heavy_check_mark: The list of items received via Dataflow has _not_ changed since the last check
- :heavy_check_mark: `DisableFastUpToDateCheck` is `false` or not specified
- :heavy_check_mark: No project items have `CopyToOutputDirectory` as `Always`

### Outputs

Output files break down as follows:

`_customOutputs` are `UpToDateCheckOutput` items published via `ProjectSubscription.JointRuleSource`
`_builtOutputs` are `UpToDateCheckBuilt` items published via `ProjectSubscription.JointRuleSource` (having no or empty `Original` property)

- :heavy_check_mark: All `_customOutputs` and `_builtOutputs` files exist

### Inputs

- :heavy_check_mark: All input files exist
- :heavy_check_mark: All input files are older than the earliest output (`_customOutputs` and `_builtOutputs`)
- :heavy_check_mark: All input files were modified before the last up-to-date check was performed

### `CopyUpToDateMarker` and `ResolvedCompilationReference`

If `ProjectSubscription.JointRuleSource` published a `CopyUpToDateMarker`...

- :heavy_check_mark: ...at least one `ResolvedCompilationReference` was also published
- :heavy_check_mark: ...at least one `ResolvedCompilationReference` file exists
- :heavy_check_mark: ...the `CopyUpToDateMarker` file exists
- :heavy_check_mark: ...the `CopyUpToDateMarker` file is newer than all existing `ResolvedCompilationReference` files

### Project items with `CopyToOutputDirectory` as `PreserveNewest`

All project items having `CopyToOutputDirectory` as `PreserveNewest`...

- :heavy_check_mark: ...exist
- :heavy_check_mark: ...have existing output files
- :heavy_check_mark: ...are older or equal to their output files

### Copied output files

`_copiedOutputFiles` is a map from destination to source paths (relative). It is populated with `UpToDateCheckBuilt` items published via `ProjectSubscription.JointRuleSource` having non-empty `Original` property.

For each `_copiedOutputFiles` source/destination

- :heavy_check_mark: ...the source must exist
- :heavy_check_mark: ...the destination must exist
- :heavy_check_mark: ...the destination must be older or the same age as the source

## Implementation

- [`BuildUpToDateCheck.cs`](https://github.com/dotnet/project-system/blob/master/src/Microsoft.VisualStudio.ProjectSystem.Managed/ProjectSystem/UpToDate/BuildUpToDateCheck.cs)
- [`BuildUpToDateCheckTests.cs`](https://github.com/dotnet/project-system/blob/master/tests/Microsoft.VisualStudio.ProjectSystem.Managed.UnitTests/ProjectSystem/UpToDate/BuildUpToDateCheckTests.cs)
# Project Configuration Properties & Project Properties

In the following discussion, C# is used as a reference but this discussion holds true for VB as well.

In general, we have two ways to get _Project Configuration Properties_. One is through the project's `IVSHierarchy.GetProperty` method using `IVsCfgBrowseObject`. The other is through Automation via DTE.


## Legacy project system

![native](https://cloud.githubusercontent.com/assets/10550513/26130958/0df90f52-3a4c-11e7-8fd9-a3c50198148f.png)

In the legacy project system, both of these mechanisms end up returning the same object, `CCSharpProjectConfigProperties`, which implements `IVsCfgBrowseObject` and a bunch of public interfaces like `CSharpProjectConfigurationProperties3`, `CSharpProjectConfigurationProperties4`, `CSharpProjectConfigurationProperties5`, `CSharpProjectConfigurationProperties6` and few more.

## CPS-based project system

![current](https://cloud.githubusercontent.com/assets/10550513/26237643/dfc6113a-3c2a-11e7-87cc-c45acb42a6ff.png)

In the CPS world, the object returned through `IVsCfgBrowseObject` implementation (`ProjectConfig` object) and the object returned via Automation are different. This automation object, `CSharpProjectConfigurationProperties`, exported by Managed Project System, overrides the default implementation.

## Future design for the new CPS based project system

![future](https://cloud.githubusercontent.com/assets/10550513/26237655/ed3cb60c-3c2a-11e7-923f-9908ddc641a4.png)

In the future, we would like to get to a design similar to the legacy project system, where the browse object and the automation object are both the same.

To achieve this,

1. Managed project system will export an implementation of the public VS interfaces, which gets ComAggregated over ProjectConfig.
2. This `ProjectConfig` will then be imported by Some_Wrapper, which then exports the `ProjectConfig` instance as the Automation Object.

## Project Properties

Project properties are not configuration based. In the legacy project system, `CCSharpProjectProperties` object is returned through `IVsHierarchy.GetProperty` and through Automation (`ENVDTE.Project.Properties`). In the new project system, we return `DynamicTypeBrowseObject`, backed by the browse object rule when `IVsHierarchy.GetProperty` or Automation is called. `CCSharpProjectProperties`, similar to `CCSharpProjectConfigProperties`, implements a bunch of public VS interfaces (`CSharpProjectProperties3`, `CSharpProjectProperties4`, `CSharpProjectProperties5`...), which are not implemented by the `DynamicTypeBrowseObject` object. This is not a problem as long as the browse object contains the properties that the interfaces defined because `EnvDte.Project.Properties` does not return `CCSharpProjectProperties`, which implements the VS interface, but instead returns a wrapper around the implementation, although the interfaces were public.
# Debugging Async Test Hangs

(Adapted from an internal document originally written by @jaredpar)

Tests hanging on CI machines are often caused by async tests that are blocked waiting for results that will never complete. Unlike traditional synchronous hangs, attaching to an async hang and looking at executing threads typically will not provide anything useful as there won't be any threads actually executing the "awaiting"  methods.

This document walks through debugging a test hang using WinDBG and SOS.

## Prerequisites 

- [WinDBG](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools)
- Basic understanding of async machinery  
- WinDBG attached to the hanging process, or opened with a dump from the hanging process

## Loading SOS

32-bit dump/process:

```
> .load C:\Windows\Microsoft.NET\Framework\v4.0.30319\sos.dll
```

64-bit dump/process:

```
> .load C:\Windows\Microsoft.NET\Framework64\v4.0.30319\sos.dll
```

## Determining the executing test

We need to find the xUnit types in memory that track test exception, in this case; [InvokeTestAsync](https://github.com/xunit/xunit/blob/9d10262a3694bb099ddd783d735aba2a7aac759d/src/xunit.execution/Sdk/Frameworks/Runners/XunitTestRunner.cs#L67). It is an async method, so we're going to find the blocked tests by looking through instances of its async state machine.

```
> !dumpheap -type InvokeTestAsync
```

```
 Address       MT     Size
036c8cb0 08389c3c       44     
037a1828 08389c3c       44     
039d9c40 08389c3c       44     
03adb7c4 08389c3c       44     
03b9cf68 08389c3c       44     
03bd7638 08389c3c       44     
03bf5748 08389c3c       44     
03d75740 08389c3c       44     
03d7fee0 08389c3c       44     
03dc019c 08389c3c       44     
03dc2e9c 08389c3c       44     
03dd51a4 08389c3c       44     
03ee8c00 08389c3c       44     
03f98a38 08389c3c       44     
03ff07e4 08389c3c       44     
0bff4e9c 08389c3c       44     
0c037b98 08389c3c       44     
0c05c2b0 08389c3c       44     

Statistics:
      MT    Count    TotalSize Class Name
08389c3c       18          792 Xunit.Sdk.XunitTestRunner+<InvokeTestAsync>d__4
Total 18 objects
```

The output tells me there's 18 instances of the async state machine in memory. What we are looking for are state machines that have not completed.

**Note:** *If you have Prefer DML (Command -> Prefer DML) turned on, the Address and MT (method table) column should be hyperlinked - you can just click the links instead of manually typing the commands.*

Let's dump the first one:

```
> !DumpObj /d 036c8cb0
```
```
Name:        Xunit.Sdk.XunitTestRunner+<InvokeTestAsync>d__4
MethodTable: 08389c3c
EEClass:     083b7c8c
Size:        44(0x2c) bytes
File:        E:\project-system2\artifacts\Debug\bin\UnitTests\xunit.execution.desktop.dll
Fields:
      MT    Field   Offset                 Type VT     Attr    Value Name
7243f2dc  4000237       14         System.Int32  1 instance       -2 <>1__state
015c84d8  4000238       18 ...lib]], mscorlib]]  1 instance 037a1840 <>t__builder
08383de4  4000239        4 ...k.XunitTestRunner  0 instance 036b0ca0 <>4__this
07869498  400023a        8 ...ceptionAggregator  0 instance 036b2d3c aggregator
7243d488  400023b        c        System.String  0 instance 03501228 <output>5__2
08389e5c  400023c       10 ....TestOutputHelper  0 instance 00000000 <testOutputHelper>5__3
015c8dc4  400023d       24 ...cimal, mscorlib]]  1 instance 037a184c <>u__1

```

The value of the `<>1__state` field is what we're interested in, this represents the "current state" of the state machine:

Value|Meaning
---:|---
-2|Finished executing
-1|Not started or currently executing (should be active call stack)
&gt;=0| Blocked in an await. The number indicates the zero-based ordinal of which await in the method is currently waiting. 

Above, the value in the statement is `-2` indicating that it has finished executing, and hence not the test we are looking for.

Let's dump the second one:

```
> !DumpObj /d 037a1828
```
```
Name:        Xunit.Sdk.XunitTestRunner+<InvokeTestAsync>d__4
MethodTable: 08389c3c
EEClass:     083b7c8c
Size:        44(0x2c) bytes
File:        E:\project-system2\artifacts\Debug\bin\UnitTests\xunit.execution.desktop.dll
Fields:
      MT    Field   Offset                 Type VT     Attr    Value Name
7243f2dc  4000237       14         System.Int32  1 instance        0 <>1__state
015c84d8  4000238       18 ...lib]], mscorlib]]  1 instance 036c8cc8 <>t__builder
08383de4  4000239        4 ...k.XunitTestRunner  0 instance 036b843c <>4__this
07869498  400023a        8 ...ceptionAggregator  0 instance 036b84e8 aggregator
7243d488  400023b        c        System.String  0 instance 03501228 <output>5__2
08389e5c  400023c       10 ....TestOutputHelper  0 instance 00000000 <testOutputHelper>5__3
015c8dc4  400023d       24 ...cimal, mscorlib]]  1 instance 036c8cd4 <>u__1
```

In the above state machine instance, the value of `<>1__state` is `0` indicating this currently blocked on the first await in [InvokeTestAsync](https://github.com/xunit/xunit/blob/9d10262a3694bb099ddd783d735aba2a7aac759d/src/xunit.execution/Sdk/Frameworks/Runners/XunitTestRunner.cs#L67) which executes the test. 

This indicates that we're interested in diving into this instance to find the hanging test.

To find the test class and test name, we need to dump the `<>4__this` field:

```
> !DumpObj /d 036b843c
```

```
Name:        Xunit.Sdk.XunitTestRunner
MethodTable: 08383de4
EEClass:     083b2410
Size:        48(0x30) bytes
File:        E:\project-system2\artifacts\Debug\bin\UnitTests\xunit.execution.desktop.dll
Fields:
      MT    Field   Offset                 Type VT     Attr    Value Name
07869498  400004e        4 ...ceptionAggregator  0 instance 036b8418 <Aggregator>k__BackingField
724834a4  400004f        8 ...lationTokenSource  0 instance 0367cb24 <CancellationTokenSource>k__BackingField
7243d87c  4000050        c      System.Object[]  0 instance 036a0148 <ConstructorArguments>k__BackingField
0707d53c  4000051       10 ...t.Sdk.IMessageBus  0 instance 0367d4e0 <MessageBus>k__BackingField
7243d488  4000052       14        System.String  0 instance 00000000 <SkipReason>k__BackingField
083850a4  4000053       18 ...bstractions.ITest  0 instance 036b83d8 <Test>k__BackingField
7243e688  4000054       1c          System.Type  0 instance 03554c1c <TestClass>k__BackingField
72442a84  4000055       20 ...ection.MethodInfo  0 instance 03585798 <TestMethod>k__BackingField
7243d87c  4000056       24      System.Object[]  0 instance 03569578 <TestMethodArguments>k__BackingField
08385180  400006d       28 ...ute, xunit.core]]  0 instance 036b8400 beforeAfterAttributes
```

To find the class, dump the ` <TestClass>k__BackingField` field:

```
> !DumpObj /d 03554c1c
```
```
Name:        System.RuntimeType
MethodTable: 7243e89c
EEClass:     72014fd0
Size:        28(0x1c) bytes
Type Name:   Microsoft.VisualStudio.ProjectSystem.OnceInitializedOnceDisposedUnderLockAsyncTests
Type MT:     07071d04
[...]
```

To find the method, dump the `<TestMethod>k__BackingField` field, followed by the `m_name` field:

```
> !DumpObj /d 03585798
```
```
Name:        System.Reflection.RuntimeMethodInfo
MethodTable: 7248e500
EEClass:     7202b1dc
Size:        60(0x3c) bytes
File:        C:\WINDOWS\Microsoft.Net\assembly\GAC_32\mscorlib\v4.0_4.0.0.0__b77a5c561934e089\mscorlib.dll
Fields:
      MT    Field   Offset                 Type VT     Attr    Value Name
72443db8  4001cb3       28        System.IntPtr  1 instance  7071cc0 m_handle
72443e20  4001cb4        4 ...+RuntimeTypeCache  0 instance 035853d4 m_reflectedTypeCache
7243d488  4001cb5        8        System.String  0 instance 03691920 m_name
[...]

```

```
> !DumpObj /d 03691920
```

```

Name:        System.String
MethodTable: 7243d488
EEClass:     72014a50
Size:        114(0x72) bytes
File:        C:\WINDOWS\Microsoft.Net\assembly\GAC_32\mscorlib\v4.0_4.0.0.0__b77a5c561934e089\mscorlib.dll
String:      ExecuteUnderLockAsync_AvoidsOverlappingWithDispose
[...]
```

Combining those, points us to the `OnceInitializedOnceDisposedUnderLockAsyncTests.ExecuteUnderLockAsync_AvoidsOverlappingWithDispose` method as the hanging test.

Based on what we learned above, we can dig further to figure out where it's hanging:

```
> !dumpheap -type ExecuteUnderLockAsync_AvoidsOverlappingWithDispose
```

```
 Address       MT     Size
036c8440 088fdfb4       60     

Statistics:
      MT    Count    TotalSize Class Name
088fdfb4        1           60 Microsoft.VisualStudio.ProjectSystem.OnceInitializedOnceDisposedUnderLockAsyncTests+<ExecuteUnderLockAsync_AvoidsOverlappingWithDispose>d__9
Total 1 objects

```

Dump that first address:

```
> !DumpObj /d 036c8440
```
```
Name:        Microsoft.VisualStudio.ProjectSystem.OnceInitializedOnceDisposedUnderLockAsyncTests+<ExecuteUnderLockAsync_AvoidsOverlappingWithDispose>d__9
MethodTable: 088fdfb4
EEClass:     083e5d80
Size:        60(0x3c) bytes
File:        E:\project-system2\artifacts\Debug\bin\UnitTests\Microsoft.VisualStudio.ProjectSystem.Managed.UnitTests.dll
Fields:
      MT    Field   Offset                 Type VT     Attr    Value Name
7243f2dc  4000266       20         System.Int32  1 instance        2 <>1__state
72489528  4000267       24 ...TaskMethodBuilder  1 instance 036c8464 <>t__builder
72485c7c  4000268        4 ...eading.Tasks.Task  0 instance 036c7788 firstAction
72485c7c  4000269        8 ...eading.Tasks.Task  0 instance 036c791c secondAction
083ce314  400026a        c ...cManualResetEvent  0 instance 036b8740 firstEntered
083ce314  400026b       10 ...cManualResetEvent  0 instance 036b879c firstRelease
083ce314  400026c       14 ...cManualResetEvent  0 instance 036b87f8 secondEntered
07071d04  400026d       18 ...derLockAsyncTests  0 instance 036b8600 <>4__this
088fe084  400026e       1c ...__DisplayClass9_0  0 instance 036c847c <>8__1
7247ddf4  400026f       30 ...vices.TaskAwaiter  1 instance 036c8470 <>u__1
015c5230  4000270       34 ...ption, mscorlib]]  1 instance 036c8474 <>u__2
```
`<>1__state` has a value of `2`, which as per above table indicates that 3rd await within the method currently blocked:

``` C#
[Fact]
public void ExecuteUnderLockAsync_AvoidsOverlappingWithDispose()
{

    [...]

    await firstEntered.WaitAsync();
    await Assert.ThrowsAsync<TimeoutException>(() => secondEntered.WaitAsync().WithTimeout(TimeSpan.FromMilliseconds(50)));

    firstRelease.Set();
    await secondEntered.WaitAsync(); // <!-- blocked here
    await Task.WhenAll(firstAction, secondAction);

    [...]
}
```

That's the line that you should start investigating.

## Further information

You can see more information, including a WinDBG extension that dumps async callstacks, over on [Async Hang Investigations](https://github.com/Microsoft/vs-threading/blob/master/doc/async_hang.md).# Capabilities

You can see the active capabilities for a given project, by turning on the `DiagnoseCapabilities` capability:

``` XML
  <ItemGroup>
    <ProjectCapability Include="DiagnoseCapabilities"/>
  </ItemGroup>
```

This will add a node in Solution Explorer that will list the current 'active' capabilities:

![image](https://cloud.githubusercontent.com/assets/1103906/22411354/16dccb2a-e6f7-11e6-91dc-91c451cc6371.png)
# Debugging Design-Time Builds

## Diagnosing Design-Time Builds

See [Diagnosing Design-Time Builds](/docs/design-time-builds.md#diagnosing-design-time-builds).

## Failing Design-Time Builds

You can artificially fail a design-time build with the following:

``` XML
  <Target Name="FailDesignTimeBuild" AfterTargets="ResolveAssemblyReferences">
      <Error Text="Failed design-time build" />
  </Target>
```
## Delaying Design-Time Builds

You can artificially delay a design-time build with the following:

``` XML
<UsingTask TaskName="Sleep" TaskFactory="CodeTaskFactory" AssemblyFile="$(MSBuildToolsPath)\Microsoft.Build.Tasks.v4.0.dll">
  <ParameterGroup>
    <!-- Delay in milliseconds -->
    <Delay ParameterType="System.Int32" Required="true" />
  </ParameterGroup>
  <Task>
    <Code Type="Fragment" Language="cs">
      <![CDATA[
      System.Threading.Thread.Sleep(this.Delay);
      ]]>
    </Code>
  </Task>
</UsingTask>

<Target Name="DelayDesignTimeBuild" AfterTargets="ResolveAssemblyReferences">
  <Sleep Delay="10000" />
</Target>
```

## Measuring Design-Time Builds

An easy way of measuring performance of a design-time build outside of VS is to run something like (replacing solution paths with appropriate solution):

> msbuild /nologo /m:1 /v:m /clp:Summary;PerformanceSummary /t:CollectResolvedSDKReferencesDesignTime;DebugSymbolsProjectOutputGroup;ResolveComReferencesDesignTime;ContentFilesProjectOutputGroup;DocumentationProjectOutputGroupDependencies;SGenFilesOutputGroup;ResolveProjectReferencesDesignTime;SourceFilesProjectOutputGroup;DebugSymbolsProjectOutputGroupDependencies;SatelliteDllsProjectOutputGroup;BuiltProjectOutputGroup;SGenFilesOutputGroupDependencies;ResolveAssemblyReferencesDesignTime;CollectSDKReferencesDesignTime;DocumentationProjectOutputGroup;PriFilesOutputGroup;BuiltProjectOutputGroupDependencies;SatelliteDllsProjectOutputGroupDependencies /p:"SolutionFileName=**Roslyn.sln**;LangName=en-US;Configuration=Debug;LangID=1033;DesignTimeBuild=true;SolutionDir=**E:\\roslyn\\**;SolutionExt=.sln;BuildingInsideVisualStudio=true;DefineExplicitDefaults=true;Platform=AnyCPU;SolutionPath=**E:\\roslyn\\Roslyn.sln**;SolutionName=**Roslyn**;DevEnvDir=C:\Program Files (x86)\Microsoft Visual Studio\Enterprise\Common7\IDE;BuildingProject=false" **E:\roslyn\src\Workspaces\CSharp\Portable\CSharpWorkspace.csproj**
# Logging

The project system code logs information to a custom Output Window pane either
while debugging or when a certain environment variable is set.

## Enabling project system logs

Setting the `PROJECTSYSTEM_PROJECTOUTPUTPANEENABLED` environment variable to
`1` enables project system logging.

This environment variable is set automatically when launching the
`ProjectSystemSetup` project within Visual Studio, via its
`launchSettings.json` file.

To enable this logging in other situations you may, for example:

1. Start a Developer Command Prompt
2. Run: `set PROJECTSYSTEM_PROJECTOUTPUTPANEENABLED=1`
3. Run: `devenv`
4. Open a solution
5. Use "View.Output Window"
6. Select the pane titled "Project" from the dropdown

## Up to date logs

The up-to-date check uses a separate CPS mechanism for logging (disabled by
default) that logs to the "Build" section of the "Output" pane. It is
controlled via Visual Studio's "Options" dialog:

![Projects and Solutions, .NET Core options](../images/options.png)# Debugging .NET SDK

## Testing SDK Changes

If you're making changes to the SDK (that is, the [dotnet/sdk](https://github.com/dotnet/sdk) repo) you can easily test VS or msbuild.exe with those changes by setting the `DOTNET_MSBUILD_SDK_RESOLVER_SDKS_DIR` environment variable.

After you build, find the generated Sdks directory. For example, if your repo is at D:\Projects\sdk, you'll find it at D:\Projects\sdk\bin\Debug\Sdks. Set the environment variable to point to this location:

`set DOTNET_MSBUILD_SDK_RESOLVER_SDKS_DIR=D:\Projects\sdk\bin\Debug\Sdks`

Now any instances of msbuild.exe or VS that inherit that setting will use your locally-produced SDK.# Setting up your Debugging Environment

## Debugger Settings

The day-to-day job of a developer that works on Visual Studio involves debugging and inspecting code outside of this repository. For best results, you'll want to flip some of the defaults so that you can can step into (Microsoft-employees only) other Visual Studio, framework and Windows code and inspect locals, fields, etc.

![image](https://user-images.githubusercontent.com/1103906/44320403-3fa23200-a485-11e8-9baa-b743cb96948d.png)

![image](https://user-images.githubusercontent.com/1103906/44320478-8a23ae80-a485-11e8-9426-0b7906093e9a.png)

![image](https://user-images.githubusercontent.com/1103906/44320534-e25ab080-a485-11e8-885b-811800d20684.png)

## Launch Settings

If you need to debug into native code (for example, msenv.dll, where the solution code lives), you can change your launch settings from ProjectSystem.sln to launch with the native debugger engine:

![image](https://user-images.githubusercontent.com/1103906/44320680-e2a77b80-a486-11e8-9887-8e5a44a4a26c.png)

If you are having troubling inspecting variables due to optimizations (assuming __Suppress JIT optimization on module load__ above is checked), you can also try bypassing NGEN images which should improve your debugging experience.
# Tracing

Common Project System (CPS) writes traces messages to both a TraceSource and a circular buffer.

## Inspecting Trace While Debugging

When you build this repository under debug either within Visual Studio or via the command-line, a trace listener is hooked up to output CPS tracing to the Debug category of the Output Window. You can use this to diagnose lots of issues, such as failing rules or missing snapshots.

You can increase the verbosity of what is output to the window by changing the verbosity level in [ManagedProjectSystemPackage.DebuggingTraceListener](https://github.com/dotnet/project-system/blob/master/src/Microsoft.VisualStudio.ProjectSystem.Managed.VS/Packaging/ManagedProjectSystemPackage.DebuggerTraceListener.cs#L44).

## Inspecting Trace Within a Memory Dump

You can inspect the circular buffer within WinDbg with the following:

```
> !name2ee Microsoft.VisualStudio.ProjectSystem.dll Microsoft.VisualStudio.ProjectSystem.TraceUtilities
```
```
Module:      10c841c0
Assembly:    Microsoft.VisualStudio.ProjectSystem.dll
Token:       02000180
MethodTable: 16f88e70
EEClass:     07f85f14
Name:        Microsoft.VisualStudio.ProjectSystem.TraceUtilities
```
```
> !DumpClass /d 07f85f14
```

```
Class Name:      Microsoft.VisualStudio.ProjectSystem.TraceUtilities
mdToken:         02000180
File:            c:\program files (x86)\microsoft visual studio\preview\enterprise\common7\ide\commonextensions\microsoft\project\Microsoft.VisualStudio.ProjectSystem.dll
Parent Class:    6ded15b0
Module:          10c841c0
Method Table:    16f88e70
Vtable Slots:    4
Total Method Slots:  5
Class Attributes:    100180  Abstract, 
Transparency:        Critical
NumInstanceFields:   0
NumStaticFields:     3
      MT    Field   Offset                 Type VT     Attr    Value Name
6d69ee10  4000326      1f4 ...stics.TraceSource  0   shared   static Source
    >> Domain:Value  00b88180:0c559288 <<
6e37dfdc  4000327      1f8      System.String[]  0   shared   static CriticalTraceRotatingBuffer
    >> Domain:Value  00b88180:0c559360 <<
6e37f2d8  4000328      434         System.Int32  1   shared   static currentTraceIndex
    >> Domain:Value  00b88180:0 <<
```

```
> !DumpObj /d 0c559360; * Dump CriticalTraceRotatingBuffer
```
```
Name:        System.String[]
MethodTable: 6e37dfdc
EEClass:     6df54b80
Size:        140(0x8c) bytes
Array:       Rank 1, Number of elements 32, Type CLASS (Print Array)
Fields:
None
```
```
> !DumpArray /d 0c559360; * Print Array
```
This will output the values in the array if it can
```
Name:        System.String[]
MethodTable: 6e37dfdc
EEClass:     6df54b80
Size:        140(0x8c) bytes
Array:       Rank 1, Number of elements 32, Type CLASS
Element Methodtable: 6e37d484
[0] 11c4be4c
[1] 11c4be4c
[2] 11c4be4c
[3] null
[4] null
[5] null
[6] null
[7] null
[8] null
[9] null
[10] null
[11] null
[12] null
[13] null
[14] null
[15] null
[16] null
[17] null
[18] null
[19] null
[20] null
[21] null
[22] null
[23] null
[24] null
[25] null
[26] null
[27] null
[28] null
[29] null
[30] null
[31] null
```
> !DumpObj /d 11c4be4c
```
Name:        System.String
MethodTable: 7286eb40
EEClass:     72444a50
Size:        190(0xbe) bytes
File:        C:\WINDOWS\Microsoft.Net\assembly\GAC_32\mscorlib\v4.0_4.0.0.0__b77a5c561934e089\mscorlib.dll
String:      Generating snapshot for rule "{0}" failed because the rule was missing from the project.
Fields:
      MT    Field   Offset                 Type VT     Attr    Value Name
72870994  4000279        4         System.Int32  1 instance       88 m_stringLength
7286f588  400027a        8          System.Char  1 instance       47 m_firstChar
7286eb40  400027e       5c        System.String  0   shared   static Empty
    >> Domain:Value  01187c20:NotInit  <<
```
💡 Maybe there is a problem with a rule?
# Visual Studio

## Figuring out the Git SHA for your current build

1. In Explorer, look at the properties of %VSINSTALLDIR%\Common7\IDE\Extensions\Microsoft\ManagedProjectSystem\Microsoft\Microsoft.VisualStudio.ProjectSystem.Managed.dll

![image](https://user-images.githubusercontent.com/1103906/48829215-dbfe0c80-edc5-11e8-8618-b4c9844359c7.png)

The Product Version field contains the Git SHA from which that branch was built.
# Crash Dumps, UI Delays and Hang Data

## Crash Dumps

To get Windows to automatically save a memory dump every time Visual Studio crashes, merge the following registry settings:

[AlwaysSaveDevEnvCrashDumps.reg](/docs/repo/content/AlwaysSaveDevEnvCrashDumps.reg?raw=true)

Dumps will be saved to C:\Crashdumps.

## Non-Fatal Watsons

To view Visual Studio's non-fatal watson reports on a machine:

1. Open up Event Viewer
2. Right-click on Custom Views and choose Import Custom View
3. In file name, point to [NonFatalWatsons.xml](/docs/repo/content/NonFatalWatsons.xml?raw=true) and click OK

## UI Delays

To get Windows to automatically send on data about UI delays in Visual Studio, merge the following registry settings:

[AlwaysSendPerfWatsonData.reg](/docs/repo/content/AlwaysSendPerfWatsonData.reg?raw=true)

For more information on these settings, see [Configure Windows telemetry in your organization](https://docs.microsoft.com/en-us/windows/configuration/configure-windows-telemetry-in-your-organization).
# Resources

Files in this directory are used to generate images contained within the project. These files are not included in assemblies directly.# Banned APIs across the project.

# Syntax:
#
#       E:Event
#       M:Method
#       F:Field
#       P:Property
#       T:Type

T:Microsoft.VisualStudio.ProjectSystem.IProjectLockService; Using IProjectAccessor enables checkout from source control on write, and allows async release

T:Microsoft.VisualStudio.ProjectSystem.VS.IProjectGuidService; Using ISafeProjectGuidService avoids reading the GUID before it is safe to do so during initialisation
T:Microsoft.VisualStudio.ProjectSystem.VS.IProjectGuidService2; Using ISafeProjectGuidService avoids reading the GUID before it is safe to do so during initialisation

P:Microsoft.VisualStudio.ProjectSystem.VS.IProjectAsyncLoadDashboard.ProjectLoadedInHost; Using IUnconfiguredProjectTasksService.ProjectLoadedInHost prevents waiting indefinitely when the project is closed before it has finished loading

M:Microsoft.VisualStudio.ProjectSystem.CommonProjectSystemTools.LoadedProject(Microsoft.VisualStudio.ProjectSystem.IProjectAsynchronousTasksService); Using IUnconfiguredProjectTasksService.LoadedProjectAsync is unit testable
M:Microsoft.VisualStudio.ProjectSystem.CommonProjectSystemTools.LoadedProjectAsync(Microsoft.VisualStudio.ProjectSystem.IProjectAsynchronousTasksService,System.Func{System.Threading.Tasks.Task},System.Boolean); Using IUnconfiguredProjectTasksService.LoadedProjectAsync is unit testable
M:Microsoft.VisualStudio.ProjectSystem.CommonProjectSystemTools.LoadedProjectAsync`1(Microsoft.VisualStudio.ProjectSystem.IProjectAsynchronousTasksService,System.Func{System.Threading.Tasks.Task{``0}},System.Boolean); Using IUnconfiguredProjectTasksService.LoadedProjectAsync is unit testable

M:System.Threading.Tasks.Task.ConfigureAwait(System.Boolean); "ConfigureAwait(true)" should be removed, and "ConfigureAwait(false)" should be replaced with "await TaskScheduler.Default"
M:System.Threading.Tasks.Task`1.ConfigureAwait(System.Boolean); "ConfigureAwait(true)" should be removed, and "ConfigureAwait(false)" should be replaced with "await TaskScheduler.Default"
M:System.Threading.Tasks.ValueTask.ConfigureAwait(System.Boolean); "ConfigureAwait(true)" should be removed, and "ConfigureAwait(false)" should be replaced with "await TaskScheduler.Default"
M:System.Threading.Tasks.ValueTask`1.ConfigureAwait(System.Boolean); "ConfigureAwait(true)" should be removed, and "ConfigureAwait(false)" should be replaced with "await TaskScheduler.Default"

M:System.Threading.Tasks.Task.Run(System.Action); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run`1(System.Func{``0}); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run`1(System.Func{System.Threading.Tasks.Task{``0}}); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run(System.Func{System.Threading.Tasks.Task}); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run(System.Action,System.Threading.CancellationToken); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run`1(System.Func`1{``0},System.Threading.CancellationToken); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run(System.Func{System.Threading.Tasks.Task},System.Threading.CancellationToken); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons
M:System.Threading.Tasks.Task.Run`1(System.Func{System.Threading.Tasks.Task{``0}},System.Threading.CancellationToken); Task.Run should be replaced with IProjectThreadingService.RunAndForget, which prevents the project being unloaded while the Task is running and ensures that failed tasks are reported as non-fatal watsons

T:System.IServiceProvider; Import and use IVsUIService<T> and IVsUIService<TService, TInterface> which enforce usage on the UI thread and prevent blocking RPC calls from background threads
T:Microsoft.VisualStudio.Shell.SVsServiceProvider; Import and use IVsUIService<T> and IVsUIService<TService, TInterface> which enforce usage on the UI thread and prevent blocking RPC calls from background threads

T:Microsoft.VisualStudio.Shell.IAsyncServiceProvider; Import and use IVsService<T> and IVsService<TService, TInterface> which prevent blocking RPC calls from background threads
T:Microsoft.VisualStudio.Shell.Interop.SAsyncServiceProvider; Import and use IVsService<T> and IVsService<TService, TInterface> which prevent blocking RPC calls from background threads

T:Microsoft.VisualStudio.ProjectSystem.VS.IServiceProviderExtensions; Import and use IVsUIService<T> and IVsUIService<TService, TInterface> which enforce usage on the UI thread and prevent blocking RPC calls from background threads

M:Microsoft.VisualStudio.Threading.TplExtensions.Forget(System.Threading.Tasks.Task); Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.Shell.VsTaskLibraryHelper.FileAndForget(System.Threading.Tasks.Task,System.String,System.String,System.Func{System.Exception,System.Boolean}); Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.Shell.VsTaskLibraryHelper.FileAndForget(Microsoft.VisualStudio.Threading.JoinableTask,System.String,System.String,System.Func{System.Exception,System.Boolean}); Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component

M:Microsoft.VisualStudio.ProjectSystem.IProjectFaultHandlerService.HandleFaultAsync(System.Exception,Microsoft.VisualStudio.ProjectSystem.ErrorReportSettings,Microsoft.VisualStudio.ProjectSystem.ProjectFaultSeverity,Microsoft.VisualStudio.ProjectSystem.UnconfiguredProject); Use IProjectFaultHandlerService.ReportFaultAsync to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.ProjectSystem.IProjectFaultHandlerService.RegisterFaultHandler(System.Threading.Tasks.Task,Microsoft.VisualStudio.ProjectSystem.ErrorReportSettings,Microsoft.VisualStudio.ProjectSystem.ProjectFaultSeverity,Microsoft.VisualStudio.ProjectSystem.UnconfiguredProject); Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.ProjectSystem.IProjectFaultHandlerService.RegisterFaultHandler`1(System.Threading.Tasks.Task{``0},Microsoft.VisualStudio.ProjectSystem.ErrorReportSettings,Microsoft.VisualStudio.ProjectSystem.ProjectFaultSeverity,Microsoft.VisualStudio.ProjectSystem.UnconfiguredProject); Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component

M:Microsoft.VisualStudio.Telemetry.PostFault(Microsoft.VisualStudio.Telemetry.TelemetrySession,System.String,System.String);Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.Telemetry.PostFault(Microsoft.VisualStudio.Telemetry.TelemetrySession,System.String,System.String,System.Exception);Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.Telemetry.PostFault(Microsoft.VisualStudio.Telemetry.TelemetrySession,System.String,System.String,System.Exception,System.Func{Microsoft.VisualStudio.Telemetry.IFaultUtility,System.Int32});Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component
M:Microsoft.VisualStudio.Telemetry.PostFault(Microsoft.VisualStudio.Telemetry.TelemetrySession,System.String,System.String,System.Exception,System.Func{Microsoft.VisualStudio.Telemetry.IFaultUtility,System.Int32},Microsoft.VisualStudio.Telemetry.TelemetryEventCorrelation[]);Use IProjectFaultHandlerService.Forget to ensure that failed tasks are reported as non-fatal watsons and assigned to the correct component

M:Microsoft.VisualStudio.ProjectSystem.IProjectThreadingService.Fork(System.Func{System.Threading.Tasks.Task},Microsoft.VisualStudio.Threading.JoinableTaskFactory,Microsoft.VisualStudio.ProjectSystem.UnconfiguredProject,Microsoft.VisualStudio.ProjectSystem.ConfiguredProject,Microsoft.VisualStudio.ProjectSystem.ErrorReportSettings,Microsoft.VisualStudio.ProjectSystem.ProjectFaultSeverity,Microsoft.VisualStudio.ProjectSystem.ForkOptions); Use IProjectThreadingService.RunAndForget to ensure non-fatal watsons are assigned to the correct component

T:System.Threading.Tasks.Dataflow.ActionBlock`1;Use DataflowUtilities.LinkToAction/LinkToAsyncAction or DataflowBlockSlim.CreateActionBlock to reduce memory and avoid the overhead of the built-in blocks
T:System.Threading.Tasks.Dataflow.BroadcastBlock`1;Use DataflowBlockSlim.CreateBroadcastBlock to reduce memory and avoid the overhead of the built-in blocks
T:System.Threading.Tasks.Dataflow.TransformManyBlock`2;Use DataflowBlockSlim.CreateTransformManyBlock to reduce memory and avoid the overhead of the built-in blocks

F:Microsoft.VisualStudio.VSConstants.S_OK;Use HResult.OK or HResult.IsOK
F:Microsoft.VisualStudio.VSConstants.E_FAIL;Use HResult.Fail or HResult.Failed
F:Microsoft.VisualStudio.VSConstants.S_FALSE;Use HResult.False or HResult.IsFalse
F:Microsoft.VisualStudio.VSConstants.E_NOTIMPL;Use HResult.NotImplemented or HResult.IsNotImplemented
F:Microsoft.VisualStudio.VSConstants.E_INVALIDARG;Use HResult.InvalidArg
F:Microsoft.VisualStudio.VSConstants.RPC_E_WRONG_THREAD;Use HResult.WrongThread
F:Microsoft.VisualStudio.VSConstants.E_ABORT;Use HResult.Abort
F:Microsoft.VisualStudio.VSConstants.E_PENDING;Use HResult.Pending
F:Microsoft.VisualStudio.VSConstants.DISP_E_MEMBERNOTFOUND;Use HResult.MemberNotFound
F:Microsoft.VisualStudio.VSConstants.E_NOINTERFACE;Use HResult.NoInterface
F:Microsoft.VisualStudio.VSConstants.E_UNEXPECTED;Use HResult.Unexpected
F:Microsoft.VisualStudio.OLE.Interop.Constants.OLECMDERR_E_NOTSUPPORTED;Use HResult.Ole.Cmd.NotSupported
F:Microsoft.VisualStudio.OLE.Interop.Constants.OLECMDERR_E_UNKNOWNGROUP;Use HResult.Ole.Cmd.UnknownGroup

T:Microsoft.VisualStudio.Shell.ThreadHelper;Import JoinableTaskContext if inside a MEF component for unit testing purposes

T:Microsoft.VisualStudio.ProjectSystem.Properties.StandardRuleDataflowLinkOptions;Use DataflowOption.WithRuleNames to avoid boilerplate initialization
T:System.Threading.Tasks.Dataflow.DataflowLinkOptions;Use DataflowOption.PropagateCompletion to avoid boilerplate initialization
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_ESERVER_HANDLER = 256 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_INPROC_HANDLER = 2 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_INPROC_HANDLER16 = 32 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_INPROC_HANDLERX86 = 128 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_INPROC_SERVER = 1 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_INPROC_SERVER16 = 8 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_INPROC_SERVERX86 = 64 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_LOCAL_SERVER = 4 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_NO_CODE_DOWNLOAD = 1024 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_REMOTE_SERVER = 16 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.CLSCTX_RESERVED = 512 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.DISP_E_MEMBERNOTFOUND = -2147352573 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.DISPID_UNKNOWN = -1 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.DLGC_WANTTAB = 2 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.EM_UNDO = 199 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.FACILITY_WIN32 = 7 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.FALSE = 0 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.FNERR_BUFFERTOOSMALL = 12291 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.GW_CHILD = 5 -> UInteger
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDF_BITMAP_ON_RIGHT = 4096 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDF_IMAGE = 2048 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDF_STRING = 16384 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDI_FORMAT = 4 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDI_IMAGE = 32 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDI_TEXT = 2 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDM_SETIMAGELIST = 4616 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.HDM_SETITEMW = 4620 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.LVM_EDITLABELA = 4119 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.LVM_EDITLABELW = 4214 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.LVM_GETHEADER = 4127 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.MAX_PATH = 260 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.OLE_E_PROMPTSAVECANCELLED = -2147221492 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.OLECMDERR_E_NOTSUPPORTED = -2147221248 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_ALLEVENTS = 191 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_ALLINPUT = 255 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_ALLPOSTMESSAGE = 256 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_HOTKEY = 128 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_INPUT = 7 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_KEY = 1 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_MOUSE = 6 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_MOUSEBUTTON = 4 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_MOUSEMOVE = 2 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_PAINT = 32 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_POSTMESSAGE = 8 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_SENDMESSAGE = 64 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.QS_TIMER = 16 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.SC_CONTEXTHELP = 61824 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.SPI_GETSCREENREADER = 70 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.TRUE = 1 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.TVIF_STATE = 8 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.TVIS_STATEIMAGEMASK = 61440 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.TVM_SETITEMA = 4365 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WAVE_FORMAT_ADPCM = 2 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WAVE_FORMAT_IEEE_FLOAT = 3 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WAVE_FORMAT_PCM = 1 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_CHAR = 258 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_CONTEXTMENU = 123 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_GETDLGCODE = 135 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_HELP = 83 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_KEYDOWN = 256 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_KEYUP = 257 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_PALETTECHANGED = 785 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_PASTE = 770 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_RBUTTONDOWN = 516 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_RBUTTONUP = 517 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SETFOCUS = 7 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SETTINGCHANGE = 26 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SYSCHAR = 262 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SYSCOLORCHANGE = 21 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SYSCOMMAND = 274 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SYSKEYDOWN = 260 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_SYSKEYUP = 261 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_THEMECHANGED = 794 -> Integer
Const Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.WM_USER = 1024 -> Integer
Const Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.PROPPAGESTATUS_CLEAN = 4 -> Integer
Const Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.PROPPAGESTATUS_DIRTY = 1 -> Integer
Const Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.PROPPAGESTATUS_VALIDATE = 2 -> Integer
Const Microsoft.VisualStudio.Editors.Constants.WS_CHILD = 1073741824 -> Integer
Const Microsoft.VisualStudio.Editors.Constants.WS_CLIPSIBLINGS = 67108864 -> Integer
Const Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.NestingCharacter = ":" -> String
Const Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SW_HIDE = 0 -> Integer
Const Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SW_SHOW = 5 -> Integer
Const Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SW_SHOWNORMAL = 1 -> Integer
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.CurrentDesignerHost() -> System.ComponentModel.Design.IDesignerHost
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.New() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.New(ServiceProvider As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ServiceProvider() -> System.IServiceProvider
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ServiceProvider(Value As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.SetFontStyles() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ShowDialog() -> System.Windows.Forms.DialogResult
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ShowHelp() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.New() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.RefreshMenuStatus() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.RegisterMenuCommands(MenuCommands As System.Collections.ArrayList, KeepRegisteredMenuCommands As Boolean = True) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.RemoveMenuCommands() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.SelectionService() -> System.ComponentModel.Design.ISelectionService
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.ShowContextMenu(ContextMenuID As System.ComponentModel.Design.CommandID, X As Integer, Y As Integer) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.CheckCommandStatusHandler
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.IVsWindowPaneCommit_CommitPendingEdit(ByRef pfCommitFailed As Integer) -> Integer
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.New(surface As System.ComponentModel.Design.DesignSurface, SupportToolbox As Boolean) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.View() -> System.Windows.Forms.Control
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.New(provider As System.IServiceProvider, SupportToolbox As Boolean) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand.New(RootDesigner As Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner, CommandID As System.ComponentModel.Design.CommandID, CommandHandler As System.EventHandler, CommandEnabledHandler As Microsoft.VisualStudio.Editors.AppDesDesignerFramework.CheckCommandStatusHandler = Nothing, CommandCheckedHandler As Microsoft.VisualStudio.Editors.AppDesDesignerFramework.CheckCommandStatusHandler = Nothing, CommandVisibleHandler As Microsoft.VisualStudio.Editors.AppDesDesignerFramework.CheckCommandStatusHandler = Nothing, AlwaysCheckStatus As Boolean = False, CommandText As String = Nothing) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand.RefreshStatus() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox.New() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.New() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.New(errors As System.Collections.ICollection) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.New(ex As System.Exception) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.New(Text As String) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.AreFilesEditable() -> Boolean
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.EnsureFilesEditable() -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.ManagedFiles() -> System.Collections.Generic.List(Of String)
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.ManagedFiles(Value As System.Collections.Generic.List(Of String)) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.ManageFile(mkDocument As String) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.New(sp As System.IServiceProvider, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Void
Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.StopManagingFile(mkDocument As String) -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.CAUUIDMarshaler
Microsoft.VisualStudio.Editors.AppDesInterop.CAUUIDMarshaler.New() -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.CorMetaDataDispenser
Microsoft.VisualStudio.Editors.AppDesInterop.CorMetaDataDispenser.New() -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.ILangInactiveCfgPropertyNotifySink
Microsoft.VisualStudio.Editors.AppDesInterop.ILangInactiveCfgPropertyNotifySink.OnChanged(dispid As Integer, wszConfigName As String) -> Integer
Microsoft.VisualStudio.Editors.AppDesInterop.ILangPropertyProvideBatchUpdate
Microsoft.VisualStudio.Editors.AppDesInterop.ILangPropertyProvideBatchUpdate.BeginBatch() -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.ILangPropertyProvideBatchUpdate.EndBatch() -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.ILangPropertyProvideBatchUpdate.IsBatchModeEnabled(ByRef BatchModeEnabled As Boolean) -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.ILangPropertyProvideBatchUpdate.PushOptionsToCompiler(dispid As UInteger) -> Void
Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant
Microsoft.VisualStudio.Editors.AppDesInterop.Win32Constant.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.Close() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.MapLogicalView(ByRef rguidLogicalView As System.Guid, ByRef pbstrPhysicalView As String) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.SetSite(Site As Microsoft.VisualStudio.OLE.Interop.IServiceProvider) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader.InitializeEx(ServiceProvider As Microsoft.VisualStudio.Shell.ServiceProvider, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, punkDocData As Object) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ActualGuid() -> System.Guid
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CloseFrame() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CommitPendingEdit() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CreateDesigner() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomMkDocumentProvider() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomMkDocumentProvider(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomViewProvider() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomViewProvider(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocCookie() -> UInteger
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocData() -> Object
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocData(Value As Object) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocView() -> System.Windows.Forms.Control
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocView(Value As System.Windows.Forms.Control) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditFlags() -> UInteger
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditFlags(Value As UInteger) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorCaption() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorCaption(Value As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorGuid() -> System.Guid
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorGuid(Value As System.Guid) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.Hierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.IsDirty() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.IsPropertyPage() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ItemId() -> UInteger
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.m_Debug_cWindowFrameBoundsUpdated -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.m_Debug_cWindowFrameShow -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.MkDocument() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.MkDocument(Value As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.New(View As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, PropertyPageInfo As Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.New(View As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.OnWindowActivated(activated As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.PhysicalView() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.PhysicalView(Value As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.PropertyPageInfo() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ShowDesigner(Show As Boolean = True) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabAutomationName() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabAutomationName(Value As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabTitle() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabTitle(Value As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.UpdateWindowFrameBounds() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.VsUIShell5() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.VsWindowFrame() -> Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.VsWindowFrame(Value As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.Hierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.Hierarchy(Value As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.ItemId() -> UInteger
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.ItemId(Value As UInteger) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.RootDesigner() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.CommitAnyPendingChanges() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.Component() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.GetView() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.ActiveView() -> System.Guid
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.ActiveView(Value As System.Guid) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.CommitAnyPendingChanges() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DelayRefreshDirtyIndicators() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DsMsgBox(ex As System.Exception, HelpLink As String = Nothing) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DsMsgBox(Message As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton = System.Windows.Forms.MessageBoxDefaultButton.Button1, HelpLink As String = Nothing) -> System.Windows.Forms.DialogResult
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DTEProject() -> EnvDTE.Project
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.GetPropertyPages() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo()
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.GetSaveTreeItems(flags As Microsoft.VisualStudio.Shell.Interop.__VSRDTSAVEOPTIONS) -> Microsoft.VisualStudio.Shell.Interop.VSSAVETREEITEM()
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.InitializationComplete() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.InitView() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.New(serviceProvider As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.NotifyShuttingDown() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterAttributeChange(docCookie As UInteger, grfAttribs As UInteger) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterDocumentWindowHide(docCookie As UInteger, pFrame As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterFirstDocumentLock(docCookie As UInteger, dwRDTLockType As UInteger, dwReadLocksRemaining As UInteger, dwEditLocksRemaining As UInteger) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterLastDocumentUnlock(Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, MkDocument As String, ClosedWithoutSaving As Integer) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterSave(docCookie As UInteger) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterSaveAll() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnBeforeDocumentWindowShow(docCookie As UInteger, fFirstShow As Integer, pFrame As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnBeforeFirstDocumentLock(Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, MkDocument As String) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnBeforeLastDocumentUnlock(docCookie As UInteger, dwRDTLockType As UInteger, dwReadLocksRemaining As UInteger, dwEditLocksRemaining As UInteger) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnCmdUIContextChanged(dwCmdUICookie As UInteger, fActive As Integer) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnElementValueChanged(elementid As UInteger, varValueOld As Object, varValueNew As Object) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnInitializationComplete() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnSelectionChanged(pHierOld As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidOld As UInteger, pMISOld As Microsoft.VisualStudio.Shell.Interop.IVsMultiItemSelect, pSCOld As Microsoft.VisualStudio.Shell.Interop.ISelectionContainer, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger, pMISNew As Microsoft.VisualStudio.Shell.Interop.IVsMultiItemSelect, pSCNew As Microsoft.VisualStudio.Shell.Interop.ISelectionContainer) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.SetUndoRedoCleanStateOnAllPropertyPages() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.SpecialFiles() -> Microsoft.VisualStudio.Shell.Interop.IVsProjectSpecialFiles
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.SwitchTab(forward As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.WindowFrame() -> Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.ActivateLogicalView(ByRef rguidLogicalView As System.Guid) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.AppDesignerView() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.CloseFrameNoSave() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.ClosePromptSave() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.GetActiveLogicalView(ByRef pguidLogicalView As System.Guid) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.IsLogicalViewActive(ByRef rguidLogicalView As System.Guid, ByRef pIsActive As Integer) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.IVsWindowPaneCommit_CommitPendingEdit(ByRef pfCommitFailed As Integer) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.New(surface As System.ComponentModel.Design.DesignSurface) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.NextTab() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.PrevTab() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.SaveChildren(flags As Microsoft.VisualStudio.Shell.Interop.__VSRDTSAVEOPTIONS) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.SaveProjectFile() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.VsUIShell2Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell2
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.VsUIShell5Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.VsUIShellService() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPaneControl
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPaneControl.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.CmdTargetHelper
Microsoft.VisualStudio.Editors.ApplicationDesigner.CmdTargetHelper.New(WindowPane As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.Dispose() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.DeferrableWindowPaneProviderService
Microsoft.VisualStudio.Editors.ApplicationDesigner.DeferrableWindowPaneProviderService.New(provider As System.IServiceProvider, docData As Microsoft.VisualStudio.Shell.Design.Serialization.DocData) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.New(ErrorText As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.New(Exception As System.Exception) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.DelayRefreshDirtyIndicators() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.DsMsgBox(ex As System.Exception, HelpLink As String = Nothing) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.GetLocaleID() -> UInteger
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.ApplicationDesigner.IVsEditWindowNotify
Microsoft.VisualStudio.Editors.ApplicationDesigner.IVsEditWindowNotify.OnActivated(activated As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.AccessibleState() -> System.Windows.Forms.AccessibleStates
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.ButtonIndex() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.DirtyIndicator() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.DirtyIndicator(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.Location() -> System.Drawing.Point
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.Location(Value As System.Drawing.Point) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.SetIndex(index As Integer) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.TextWithDirtyIndicator() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.AddTab(Title As String, AutomationName As String) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ClearTabs() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.GetTabButton(index As Integer) -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.HostingPanel() -> System.Windows.Forms.Panel
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.HoverItem() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.InvalidateLayout() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemEnter(e As System.EventArgs, item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemLeave(e As System.EventArgs, item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.Renderer() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedIndex() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedIndex(Value As Integer) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedItem() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedItem(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ServiceProvider() -> System.IServiceProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ServiceProvider(Value As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.TabButtonCount() -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.TabButtons() -> System.Collections.Generic.IEnumerable(Of Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChanged(sender As Object, args As System.EventArgs) -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.VsUIShell2Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell2
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.VsUIShell5Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.VsUIShellService() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.CreateGDIObjects(ForceUpdate As Boolean = False) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.New(owner As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.PerformLayout() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.PreferredButtonForSwitchableSlot() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.PreferredButtonForSwitchableSlot(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.RenderBackground(g As System.Drawing.Graphics) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.RenderButton(g As System.Drawing.Graphics, button As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton, IsSelected As Boolean, IsHovered As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.ServiceProvider() -> System.IServiceProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.ServiceProvider(Value As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.UpdateCacheState() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.ComPropPageInstance() -> Microsoft.VisualStudio.OLE.Interop.IPropertyPage
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Guid() -> System.Guid
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.IsConfigPage() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.LoadException() -> System.Exception
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.New(ParentView As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, Guid As System.Guid, IsConfigurationDependentPage As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Site() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Title() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.BackingServiceProvider() -> System.IServiceProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.BackingServiceProvider(Value As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.CommitPendingChanges() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.GetLocaleID(ByRef pLocaleID As UInteger) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.GetPageContainer(ByRef ppunk As Object) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.GetService(serviceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.HasBeenSetDirty() -> Boolean
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.HasBeenSetDirty(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.New(View As Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner, PropPage As Microsoft.VisualStudio.OLE.Interop.IPropertyPage) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.OnStatusChange(dwFlags As UInteger) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.QueryService(ByRef guidService As System.Guid, ByRef riid As System.Guid, ByRef ppvObject As System.IntPtr) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.TranslateAccelerator(pMsg As Microsoft.VisualStudio.OLE.Interop.MSG()) -> Integer
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomDocumentMonikerProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomDocumentMonikerProvider.New(DesignerView As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, SpecialFileId As Integer) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.New() -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.SetSite(ViewProvider As Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.DesignerPanel() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.DesignerView() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.LinkText() -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.New(DesignerView As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, DesignerPanel As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel, SpecialFileId As Integer, LinkText As String) -> Void
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.SpecialFileId() -> Integer
Microsoft.VisualStudio.Editors.Constants
Microsoft.VisualStudio.Editors.Constants.New() -> Void
Microsoft.VisualStudio.Editors.IVBPackage
Microsoft.VisualStudio.Editors.IVBPackage.GetLastShownApplicationDesignerTab(projectHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Integer
Microsoft.VisualStudio.Editors.IVBPackage.SetLastShownApplicationDesignerTab(projectHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, tab As Integer) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationPropertiesBase
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationPropertiesBase.New() -> Void
Microsoft.VisualStudio.Editors.Package.InternalException
Microsoft.VisualStudio.Editors.Package.InternalException.New() -> Void
Microsoft.VisualStudio.Editors.Package.InternalException.New(info As System.Runtime.Serialization.SerializationInfo, context As System.Runtime.Serialization.StreamingContext) -> Void
Microsoft.VisualStudio.Editors.Package.InternalException.New(InnerException As System.Exception) -> Void
Microsoft.VisualStudio.Editors.Package.InternalException.New(Message As String, InnerException As System.Exception) -> Void
Microsoft.VisualStudio.Editors.Package.InternalException.New(Message As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.GetLocaleID() -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.GetTransaction(description As String) -> System.ComponentModel.Design.DesignerTransaction
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.New(childPage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase, wrappedInternalSite As Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal, wrappedUndoSite As Microsoft.VisualStudio.ManagedInterfaces.ProjectDesigner.IVsProjectDesignerPageSite) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.OnPropertyChanged(propertyName As String, propertyDescriptor As System.ComponentModel.PropertyDescriptor, oldValue As Object, newValue As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.OnPropertyChanging(propertyName As String, propertyDescriptor As System.ComponentModel.PropertyDescriptor) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.OnStatusChange(flags As Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.TranslateAccelerator(msg As System.Windows.Forms.Message) -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.CommonProperty = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.Dirty = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.Hidden = 64 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.None = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.NoOptimisticFileCheckout = 32768 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInApplicationDefinitionFile = 16384 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInAppManifestFile = 1024 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInAssemblyInfoFile = 2048 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInProjectUserFile = 256 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInVBMyAppFile = 512 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.ProjectMayBeReloadedDuringPropertySet = 4096 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.RefreshAllPropertiesWhenChanged = 8192 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.UserHandledEvents = 32 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.UserPersisted = 16 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper
Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.New(defaultDescriptor As System.ComponentModel.PropertyDescriptor) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.HiddenIfMissingPropertyControlData
Microsoft.VisualStudio.Editors.PropertyPages.HiddenIfMissingPropertyControlData.New(id As Integer, name As String, formControl As System.Windows.Forms.Control) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.Apply() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.EditProperty(dispid As Integer) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.GetHelpContextF1Keyword() -> String
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.Help(HelpDir As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.IsPageDirty() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.SetObjects(objects As Object()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.SetPageSite(base As Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.GetLocaleID() -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.OnStatusChange(flags As Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.TranslateAccelerator(msg As System.Windows.Forms.Message) -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.ProjectReloadedException
Microsoft.VisualStudio.Editors.PropertyPages.ProjectReloadedException.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ProjectReloadedException.New(Info As System.Runtime.Serialization.SerializationInfo, Context As System.Runtime.Serialization.StreamingContext) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AllInitialValues() -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AllInitialValuesExpanded() -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AssociatedControls -> System.Windows.Forms.Control()
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.CommonPropertiesObject() -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.DispId() -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.DisplayPropertyName -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.EnableAssociatedControl(control As System.Windows.Forms.Control, Enabled As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.EnableControls(Enabled As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.Flags -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.FormControl() -> System.Windows.Forms.Control
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetControlValueMultipleValues() -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetControlValueNative() -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetFlags() -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.InitialValue() -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsCommonProperty() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsCommonProperty(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsConfigurationSpecificProperty() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsDirty() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsDirty(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsHidden() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsHidden(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsIndeterminate() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsMissing() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsReadOnly() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsSpecialValue() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserHandledEvents() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserHandledEvents(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserPersisted() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserPersisted(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_FormControl -> System.Windows.Forms.Control
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_Initializing -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_isCommitingChange -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_PropPage -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, AssocControls As System.Windows.Forms.Control()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssocControls As System.Windows.Forms.Control()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssocControls As System.Windows.Forms.Control()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssocControls As System.Windows.Forms.Control()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate, multiValueSetter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate, multiValueGetter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssociatedControls As System.Windows.Forms.Control()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ObjectsPropertyDescriptorsArray() -> System.ComponentModel.PropertyDescriptorCollection()
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropDesc -> System.ComponentModel.PropertyDescriptor
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropertyName() -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropPage() -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetControlValue(value As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDirty(ReadyToApply As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetInitialValues(AllInitialValues As Object()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetInitialValues(InitialValue As Object, AllInitialValues As Object()) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetInitialValues(InitialValue As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener
Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener.OnChanged(dispid As Integer, wszConfigName As String) -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(Info As System.Runtime.Serialization.SerializationInfo, Context As System.Runtime.Serialization.StreamingContext) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, helpLink As String, innerException As System.Exception) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, helpLink As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, innerException As System.Exception, ShowHeaderAndFooterInErrorControl As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, innerException As System.Exception) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.ShowHeaderAndFooterInErrorControl() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.ShowHeaderAndFooterInErrorControl(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.FinishPendingValidations() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetLocaleID() -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.OnStatusChange(flags As Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.OnWindowActivated(activated As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.TranslateAccelerator(msg As System.Windows.Forms.Message) -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.New(ServiceProvider As System.IServiceProvider, F1Keyword As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.PropPage() -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.PropPage(Value As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.SetFocusToPage() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.Clean = 4 -> Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.Dirty = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.Validate = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddChangeHandlers() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ApplyChanges(sender As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CanApplyNow() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CanApplyNow(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CheckoutProjectFile(ByRef ProjectReloaded As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ClearIsDirty() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CommonPropertiesObject() -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DelayValidate(dataControl As System.Windows.Forms.Control) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DISPID_UNKNOWN -> Integer
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DTE() -> EnvDTE.DTE
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DTEProject() -> EnvDTE.Project
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EnableControl(control As System.Windows.Forms.Control, enabled As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Enabled() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Enabled(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EnterProjectCheckoutSection() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ExtendedPropertiesObjects(Data As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData) -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyDescriptor(PropertyName As String) -> System.ComponentModel.PropertyDescriptor
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValue(prop As System.ComponentModel.PropertyDescriptor) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValue(PropertyName As String) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValueNative(prop As System.ComponentModel.PropertyDescriptor) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValueNative(PropertyName As String) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetControlValue(name As String) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetControlValueNative(name As String) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCurrentProperty(dispid As Integer, PropertyName As String, ByRef obj As Object) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDialogFont() -> System.Drawing.Font
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirectoryViaBrowse(InitialDirectory As String, DialogTitle As String, ByRef NewValue As String) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirectoryViaBrowseRelative(RelativeInitialDirectory As String, BasePath As String, DialogTitle As String, ByRef NewRelativePath As String) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirectoryViaBrowseRelativeToProject(InitialDirectory As String, DialogTitle As String, ByRef NewValue As String) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirty(sender As Object) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetFileViaBrowse(InitialDirectory As String, ByRef NewValue As String, Filter As String) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProjectPath() -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProjectRelativeDirectoryPath(DirectoryPath As String) -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProjectRelativeFilePath(FilePath As String) -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyDescriptor(PropertyName As String) -> System.ComponentModel.PropertyDescriptor
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetRelativeDirectoryPath(BasePath As String, DirectoryPath As String) -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetRelativeFilePath(BasePath As String, FilePath As String) -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetServiceFromPropertyPageSite(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.InitializeAllProperties() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsActivated() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsAnyPropertyDirty() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsConfigurationSpecificPage() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsCSProject() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsDirty() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsDirty(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsInProjectCheckoutSection() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsUndoEnabled() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsVBProject() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.LeaveProjectCheckoutSection() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_CommonPropertyDescriptors -> System.ComponentModel.PropertyDescriptorCollection
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ControlData -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData()
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ExtendedObjects -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_fInsideInit -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_IsDirty -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_Objects -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ObjectsPropertyDescriptorsArray -> System.ComponentModel.PropertyDescriptorCollection()
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ScalingCompleted -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ManualPageScaling() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ManualPageScaling(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.MultiProjectSelect() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.New(serviceProvider As Microsoft.VisualStudio.Shell.ServiceProvider) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyChanged(DISPID As Integer, DebugSourceName As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyRequestEdit(DISPID As Integer, DebugSourceName As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PageRequiresScaling() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PageRequiresScaling(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProcessDelayValidationQueue(canThrow As Boolean) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectHierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectKind() -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectLanguage() -> String
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectProperties() -> VSLangProj.ProjectProperties
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectReloadedDuringCheckout() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.Direct = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.External = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.Indirect = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyPageSite() -> Microsoft.VisualStudio.OLE.Interop.IPropertyPageSite
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RawPropertiesObjects(Data As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData) -> Object()
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ResumePropertyChangeListening(DispId As Integer) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ServiceProvider() -> Microsoft.VisualStudio.Shell.ServiceProvider
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValue(prop As System.ComponentModel.PropertyDescriptor, Value As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValue(PropertyName As String, value As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValueNative(prop As System.ComponentModel.PropertyDescriptor, Value As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValueNative(PropertyName As String, Value As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(dispid As Integer, ReadyToApply As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(dispid As Integer) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(ReadyToApply As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(sender As Object, ReadyToApply As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(sender As Object) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowChildPage(Title As String, PageType As System.Type, F1Keyword As String) -> System.Windows.Forms.DialogResult
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowChildPage(Title As String, PageType As System.Type) -> System.Windows.Forms.DialogResult
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(errorMessage As String, ex As System.Exception) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(errorMessage As String, HelpLink As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(errorMessage As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(ex As System.Exception, HelpLink As String) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(ex As System.Exception) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SkipValidating(dataControl As System.Windows.Forms.Control) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SuspendPropertyChangeListening(DispId As Integer) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.TryGetNonCommonPropertyValue(Descriptor As System.ComponentModel.PropertyDescriptor) -> Object
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ValidatePageChanges(allowDelayValidation As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.VsUIShell2Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell2
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.VsUIShell5Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.VsUIShellService() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell
Microsoft.VisualStudio.Editors.PropertyPages.SKUMatrix
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.Failed = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.Succeeded = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.Warning = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult
Microsoft.VisualStudio.Editors.PropertyPages.VBPropPageBase
Microsoft.VisualStudio.Editors.PropertyPages.VBPropPageBase.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.AcademicProfessional = 2100 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.AcademicStudent = 2100 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.DownloadTrial = 2500 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Enterprise = 3000 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Express = 500 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.None = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Professional = 2000 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Standard = 1000 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.VSTO = 1500 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.Architect = 8 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.CSharp = 4 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.IDE = 16 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.None = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.VB = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.VC = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.Web = 64 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ChangeSelection(ConfigIndex As Integer, PlatformIndex As Integer, FireNotifications As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ChangeSelection(ConfigName As String, ConfigSelectionType As Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes, PlatformName As String, PlatformSelectionType As Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes, PreferExactMatch As Boolean, FireNotifications As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.CheckForModeChanges() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacks() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationDropdownEntries() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem()
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChanged() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.Dispose() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.DisplayName() -> String
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.Name -> String
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.New(Name As String, SelectionType As Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.SelectionType -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.GetAllConfigs() -> Microsoft.VisualStudio.Shell.Interop.IVsCfg()
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.IsSimplifiedConfigMode() -> Boolean
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.New(Project As EnvDTE.Project, ProjectHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, View As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnActiveProjectCfgChange(pIVsHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnCfgNameAdded(pszCfgName As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnCfgNameDeleted(CfgName As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnCfgNameRenamed(OldName As String, NewName As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnPlatformNameAdded(pszPlatformName As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnPlatformNameDeleted(pszPlatformName As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.PlatformDropdownEntries() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem()
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.Project() -> EnvDTE.Project
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigIndex() -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChanged() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedPlatformIndex() -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.Active = 1 -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.All = 2 -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.Normal = 0 -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChanged() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_Begin(ByRef pfCancelUpdate As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_Cancel() -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_Done(fSucceeded As Integer, fModified As Integer, fCancelCommand As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_StartUpdate(ByRef pfCancelUpdate As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.VsCfgProvider() -> Microsoft.VisualStudio.Shell.Interop.IVsCfgProvider2
Microsoft.VisualStudio.Editors.PropPageDesigner.DeferrableWindowPaneProviderService
Microsoft.VisualStudio.Editors.PropPageDesigner.DeferrableWindowPaneProviderService.New(provider As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.ConfigNames -> String()
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.DebugTrace(Message As String) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.GetObjects(VsCfgProvider As Microsoft.VisualStudio.Shell.Interop.IVsCfgProvider2) -> Object()
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.New(VsCfgProvider As Microsoft.VisualStudio.Shell.Interop.IVsCfgProvider2, Objects As Object(), Values As Object(), SelectedConfigName As String, SelectedPlatformName As String) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.PlatformNames -> String()
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.SelectedConfigName -> String
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.SelectedPlatformName -> String
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.Values -> Object()
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.New(PropDesc As System.ComponentModel.PropertyDescriptor, PropertyName As String) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.New(Provider As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.Close() -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.Close2() -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetData(ByRef riidKey As System.Guid, ByRef pvtData As Object) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetGuidEditorType(ByRef pClassID As System.Guid) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetGuidEditorType2(ByRef pClassID As System.Guid) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetSite(ByRef riid As System.Guid, ByRef ppvSite As System.IntPtr) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetTextBuffer(ByRef ppTextBuffer As Microsoft.VisualStudio.TextManager.Interop.IVsTextLines) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataDirty(ByRef pfDirty As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataDirty2(ByRef pfDirty As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataReadOnly(ByRef pfReadOnly As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataReloadable(ByRef pfReloadable As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataReloadable2(ByRef pfReloadable As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadDocData(pszMkDocument As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadDocData2(pszMkDocument As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LockTextBuffer(fLock As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.New(BaseProvider As System.IServiceProvider) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnFileChanged -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnLoadCompleted -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnRegisterDocData(docCookie As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnRegisterDocData2(docCookie As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.ReloadDocData(grfFlags As UInteger) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.ReloadDocData2(grfFlags As UInteger) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.RenameDocData(grfAttribs As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger, pszMkDocumentNew As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.RenameDocData2(grfAttribs As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger, pszMkDocumentNew As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SaveDocData(dwSave As Microsoft.VisualStudio.Shell.Interop.VSSAVEFLAGS, ByRef pbstrMkDocumentNew As String, ByRef pfSaveCanceled As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SaveDocData2(dwSave As Microsoft.VisualStudio.Shell.Interop.VSSAVEFLAGS, ByRef pbstrMkDocumentNew As String, ByRef pfSaveCanceled As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetData(ByRef riidKey As System.Guid, vtData As Object) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetDocDataDirty(fDirty As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetDocDataReadOnly(fReadOnly As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetSite(pUnkSite As Object) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetTextBuffer(pTextBuffer As Microsoft.VisualStudio.TextManager.Interop.IVsTextLines) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetUntitledDocPath(pszDocDataPath As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetUntitledDocPath2(pszDocDataPath As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.Close() -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.MapLogicalView(ByRef rguidLogicalView As System.Guid, ByRef pbstrPhysicalView As String) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.New() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.SetSite(Site As Microsoft.VisualStudio.OLE.Interop.IServiceProvider) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerLoader
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerLoader.New() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.Hierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.Hierarchy(Value As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.ItemId() -> UInteger
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.ItemId(Value As UInteger) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.Name() -> String
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.New() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.RootDesigner() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.Component() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.GetView() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.New() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ActivatePage(PropPage As Microsoft.VisualStudio.OLE.Interop.IPropertyPage) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.DesignerHost() -> System.ComponentModel.Design.IDesignerHost
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.DsMsgBox(Message As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton = System.Windows.Forms.MessageBoxDefaultButton.Button1, HelpLink As String = Nothing) -> System.Windows.Forms.DialogResult
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.DTEProject() -> EnvDTE.Project
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.FocusFirstOrLastPropertyPageControl(First As Boolean) -> Boolean
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetProperty(PropertyName As String) -> Object
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetPropertyPageTopHwnd() -> System.IntPtr
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetService(ServiceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetTransaction(Description As String) -> System.ComponentModel.Design.DesignerTransaction
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.Init(DTEProject As EnvDTE.Project, PropPage As Microsoft.VisualStudio.OLE.Interop.IPropertyPage, PropPageSite As Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, IsConfigPage As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IsConfigPage() -> Boolean
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IsConfigPage(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IsNativeHostedPropertyPageActivated() -> Boolean
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IVsProjectDesignerPageSite_OnPropertyChanged(PropertyName As String, PropertyDescriptor As System.ComponentModel.PropertyDescriptor, OldValue As Object, NewValue As Object) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IVsProjectDesignerPageSite_OnPropertyChanging(PropertyName As String, PropertyDescriptor As System.ComponentModel.PropertyDescriptor) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IVsWindowPaneCommit_CommitPendingEdit(ByRef pfCommitFailed As Integer) -> Integer
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.New() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.New(RootDesigner As Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.OnActivated(activated As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropPage() -> Microsoft.VisualStudio.OLE.Interop.IPropertyPage
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel.New() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel.StopAutoScrollToControl(needStop As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SetProperty(PropertyName As String, Value As Object) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SetUndoRedoCleanState() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ShouldShowDirtyIndicator() -> Boolean
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ShowErrorMessage(Message As String, HelpLink As String = Nothing) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.UnLoadPage() -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerWindowPane
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerWindowPane.New(surface As System.ComponentModel.Design.DesignSurface) -> Void
Microsoft.VisualStudio.Editors.VBPackageUtils
Microsoft.VisualStudio.Editors.VBPackageUtils.getServiceDelegate
Microsoft.VisualStudio.Editors.VBPackageUtils.New() -> Void
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider.GetDocumentMoniker() -> String
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.CloseView() -> Void
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.CreateView() -> Void
MustOverride Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.CreateControl() -> System.Windows.Forms.Control
Overloads Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ReportError(errorMessage As String, helpLink As String) -> Void
Overloads Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ReportError(ErrorMessage As String) -> Void
Overloads Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ShowMessage(Message As String, Caption As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton) -> System.Windows.Forms.DialogResult
Overloads Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.ShowMessage(Message As String, Caption As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon) -> System.Windows.Forms.DialogResult
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Dispose() -> Void
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Dispose(disposing As Boolean) -> Void
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.Dispose() -> Void
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.Dispose(disposing As Boolean) -> Void
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener.Dispose() -> Void
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(FileName As String, CopyFile As Boolean) -> EnvDTE.ProjectItem
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(FileName As String) -> EnvDTE.ProjectItem
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(ProjectItems As EnvDTE.ProjectItems, FileName As String, CopyFile As Boolean, BuildAction As VSLangProj.prjBuildAction) -> EnvDTE.ProjectItem
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(ProjectItems As EnvDTE.ProjectItems, FileName As String, CopyFile As Boolean) -> EnvDTE.ProjectItem
Overloads Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.Dispose() -> Void
Overridable Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.F1Keyword() -> String
Overridable Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.F1Keyword(Value As String) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CloseFrameInternal(WindowFrame As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame, flags As Microsoft.VisualStudio.Shell.Interop.__FRAMECLOSE) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ShowWindowFrame() -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.Dispose(Disposing As Boolean) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton, reactivatePage As Boolean) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemGotFocus(e As System.EventArgs, item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnThemeChanged() -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.TryLoadPropertyPage() -> Void
Overridable Microsoft.VisualStudio.Editors.MyApplication.MyApplicationPropertiesBase.FilesToCheckOut(CreateIfNotExist As Boolean) -> String()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AddChangeHandlers() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ApplyChanges() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ComboBox_SelectionChangeCommitted(sender As Object, e As System.EventArgs) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ExtendedPropertiesObjects() -> Object()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.FilesToCheckOut() -> String()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetAllPropertyValuesNative(Extenders As Object(), ByRef Values As Object(), ByRef ValueOrIndeterminate As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetControlValue() -> Object
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetPropertyValueNative(Extender As Object) -> Object
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetUserDefinedPropertyDescriptor() -> System.ComponentModel.PropertyDescriptor
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.Initialize(PropertyPage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.InitPropertyUI() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.InitPropertyValue() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.OnPropertyChanged(OldValue As Object, NewValue As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.OnPropertyChanging() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.RawPropertiesObjects() -> Object()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ReadUserDefinedProperty(PropertyName As String, ByRef Value As Object) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.RefreshValue() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.RestoreInitialValue() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetNonCommonPropertyValueCore(Value As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetNonCommonPropertyValueMultipleValuesCore(Objects As Object(), Values As Object()) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetPropertyValue(Value As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetPropertyValueNative(Value As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetPropertyValueNativeMultipleValues(Objects As Object(), Values As Object()) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SupportsMultipleValueUndo() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.TryGetPropertyValueNative(Extenders As Object()) -> Object
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.WriteUserDefinedProperty(PropertyName As String, Value As Object) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Apply() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.ControlTypeForResources() -> System.Type
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Deactivate() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DefaultSize() -> System.Drawing.Size
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DefaultSize(Value As System.Drawing.Size) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DocString() -> String
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DocString(Value As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetProperty(PropertyName As String) -> Object
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetPropertyMultipleValues(PropertyName As String, ByRef Objects As Object(), ByRef Values As Object()) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Help(strHelpDir As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpContext() -> UInteger
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpContext(Value As UInteger) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpFile() -> String
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpFile(Value As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.IsPageDirty() -> Integer
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Objects() -> Object()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetObjects(cObjects As UInteger, objects As Object()) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetProperty(PropertyName As String, Value As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetPropertyMultipleValues(PropertyName As String, Objects As Object(), Values As Object()) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetSite(site As Microsoft.VisualStudio.ManagedInterfaces.ProjectDesigner.IVsProjectDesignerPageSite) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SupportsMultipleValueUndo(PropertyName As String) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SupportsTheming() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.TranslateAccelerator(pMsg As Microsoft.VisualStudio.OLE.Interop.MSG()) -> Integer
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Apply() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ApplyPageChanges() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CleanupCOMReferences() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CommitTransaction(Transaction As System.ComponentModel.Design.DesignerTransaction) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ControlData() -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DisableOnBuild() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DisableOnDebug() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DisableWhenDebugMode(mode As Microsoft.VisualStudio.Shell.Interop.DBGMODE) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EditProperty(dispid As Integer) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EnableAllControls(enabled As Boolean) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetF1HelpKeyword() -> String
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProperty(dispid As Integer, ByRef obj As Object) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyControl(PropertyId As Integer) -> System.Windows.Forms.Control
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyControlData(PropertyId As Integer) -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyControlData(PropertyName As String) -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetTransaction() -> System.ComponentModel.Design.DesignerTransaction
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetTransactionDescription() -> String
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetUserDefinedPropertyDescriptor(PropertyName As String) -> System.ComponentModel.PropertyDescriptor
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Help(HelpTopic As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.InitPage() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsPageDirty() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_GetPropertyMultipleValues(PropertyName As String, ByRef Objects As Object(), ByRef Values As Object()) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_GetPropertyValue(PropertyName As String) -> Object
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_SetPropertyValue(PropertyName As String, Value As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_SetPropertyValueMultipleValues(PropertyName As String, Objects As Object(), Values As Object()) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_SupportsMultipleValueUndo(PropertyName As String) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnApplyComplete(ApplySuccessful As Boolean) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyChanged(Data As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData, Source As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyChanged(DISPID As Integer, Source As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnPageActivated(activated As Boolean) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnPropertyChanged(PropertyName As String, PropDesc As System.ComponentModel.PropertyDescriptor, OldValue As Object, NewValue As Object) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnPropertyChanging(PropertyName As String, PropDesc As System.ComponentModel.PropertyDescriptor) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnSetSite(site As Microsoft.VisualStudio.OLE.Interop.IPropertyPageSite) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnThemeChanged() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PageResizable() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PostApplyPageChanges() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PostInitPage() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PreApplyPageChanges() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PreInitPage() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ReadUserDefinedProperty(PropertyName As String, ByRef Value As Object) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RefreshPropertyStandardValues() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RefreshPropertyValues() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RestoreInitialValues() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ScaleWindowToCurrentFont() -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDialogFont(ScaleDialog As Boolean) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetObjects(objects As Object()) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SupportsTheming() -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ValidateProperty(controlData As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData, ByRef message As String, ByRef returnControl As System.Windows.Forms.Control) -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ValidationControlGroups() -> System.Windows.Forms.Control()()
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.WriteUserDefinedProperty(PropertyName As String, Value As Object) -> Boolean
Microsoft.VisualStudio.Editors.IVBPackage.GetService(serviceType As System.Type) -> Object
Microsoft.VisualStudio.Editors.IVBPackage.MenuCommandService() -> System.ComponentModel.Design.IMenuCommandService
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.IsImmediateApply() -> Boolean
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.View() -> System.Windows.Forms.Control
MustOverride Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.ControlType() -> System.Type
MustOverride Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Title() -> String
Overridable Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.ErrorText() -> System.Windows.Forms.TextBox
Overridable Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.ErrorText(WithEventsValue As System.Windows.Forms.TextBox) -> Void
Overridable Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.IconGlyph() -> System.Windows.Forms.PictureBox
Overridable Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.IconGlyph(WithEventsValue As System.Windows.Forms.PictureBox) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OverflowButton() -> System.Windows.Forms.Button
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OverflowButton(WithEventsValue As System.Windows.Forms.Button) -> Void
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.LinkLabel() -> VSThemedLinkLabel
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.LinkLabel(WithEventsValue As VSThemedLinkLabel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigDividerLine() -> System.Windows.Forms.Label
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigDividerLine(WithEventsValue As System.Windows.Forms.Label) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationComboBox() -> System.Windows.Forms.ComboBox
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationComboBox(WithEventsValue As System.Windows.Forms.ComboBox) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationFlowLayoutPanel() -> System.Windows.Forms.FlowLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationFlowLayoutPanel(WithEventsValue As System.Windows.Forms.FlowLayoutPanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationLabel() -> System.Windows.Forms.Label
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationLabel(WithEventsValue As System.Windows.Forms.Label) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationPanel() -> System.Windows.Forms.TableLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PLatformTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PLatformTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformComboBox() -> System.Windows.Forms.ComboBox
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformComboBox(WithEventsValue As System.Windows.Forms.ComboBox) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformLabel() -> System.Windows.Forms.Label
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformLabel(WithEventsValue As System.Windows.Forms.Label) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropPageDesignerViewLayoutPanel() -> System.Windows.Forms.TableLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropPageDesignerViewLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropertyPagePanel() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropertyPagePanel(WithEventsValue As Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.Cancel() -> System.Windows.Forms.Button
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.Cancel(WithEventsValue As System.Windows.Forms.Button) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.OK() -> System.Windows.Forms.Button
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.OK(WithEventsValue As System.Windows.Forms.Button) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.okCancelTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.okCancelTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.overArchingTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.overArchingTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseDialog.GetService(ServiceType As System.Type) -> Object
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner.Dispose(Disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.CreateWindowPane(surface As System.ComponentModel.Design.DesignSurface) -> Microsoft.VisualStudio.Shell.Design.DesignerWindowPane
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.Dispose(disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.GetToolboxItemSupported(toolboxItem As Microsoft.VisualStudio.OLE.Interop.IDataObject) -> Boolean
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.OnClose() -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.OnCreate() -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DeferrableWindowPaneProviderServiceBase.DesignerWindowPaneBase.Window() -> System.Windows.Forms.IWin32Window
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand.Invoke() -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand.Invoke(inArg As Object, outArg As System.IntPtr) -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand.Invoke(inArg As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMenuCommand.OleStatus() -> Integer
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.GetPreferredSize(proposedSize As System.Drawing.Size) -> System.Drawing.Size
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.Text() -> String
Overrides Microsoft.VisualStudio.Editors.AppDesDesignerFramework.ErrorControl.Text(Value As String) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader.Dispose() -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.Dispose(disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.OnLayout(levent As System.Windows.Forms.LayoutEventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.Initialize(component As System.ComponentModel.IComponent) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton, reactivatePage As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.EditorView() -> Object
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.Window() -> System.Windows.Forms.IWin32Window
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.DeferrableWindowPaneProviderService.CreateWindowPane(surface As System.ComponentModel.Design.DesignSurface) -> Microsoft.VisualStudio.Shell.Design.DesignerWindowPane
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.CloseView() -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.CreateView() -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.Dispose(Disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.View() -> System.Windows.Forms.Control
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.CreateAccessibilityInstance() -> System.Windows.Forms.AccessibleObject
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnClick(e As System.EventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnGotFocus(e As System.EventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnLostFocus(e As System.EventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnMouseEnter(e As System.EventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnMouseLeave(e As System.EventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnPaint(e As System.Windows.Forms.PaintEventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.ProcessDialogKey(keyData As System.Windows.Forms.Keys) -> Boolean
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.CreateAccessibilityInstance() -> System.Windows.Forms.AccessibleObject
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.Dispose(disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnLayout(levent As System.Windows.Forms.LayoutEventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnPaint(e As System.Windows.Forms.PaintEventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnPaintBackground(e As System.Windows.Forms.PaintEventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomDocumentMonikerProvider.GetDocumentMoniker() -> String
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.Dispose(disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.CloseView() -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.CreateView() -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.Dispose(Disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.View() -> System.Windows.Forms.Control
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.Attributes() -> System.ComponentModel.AttributeCollection
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.CanResetValue(component As Object) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.Category() -> String
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.ComponentType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.Converter() -> System.ComponentModel.TypeConverter
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.Description() -> String
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.DesignTimeOnly() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.DisplayName() -> String
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.GetChildProperties(instance As Object, filter As System.Attribute()) -> System.ComponentModel.PropertyDescriptorCollection
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.GetEditor(editorBaseType As System.Type) -> Object
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.GetValue(component As Object) -> Object
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.IsBrowsable() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.IsLocalizable() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.IsReadOnly() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.PropertyType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.ResetValue(component As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.SetValue(component As Object, value As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.ShouldSerializeValue(component As Object) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.SupportsChangeEvents() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.HiddenIfMissingPropertyControlData.InitPropertyValue() -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Dispose(disposing As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPreferredSize(startSize As System.Drawing.Size) -> System.Drawing.Size
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnLayout(levent As System.Windows.Forms.LayoutEventArgs) -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProcessDialogKey(keyData As System.Windows.Forms.Keys) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.WndProc(ByRef m As System.Windows.Forms.Message) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.DeferrableWindowPaneProviderService.CreateWindowPane(surface As System.ComponentModel.Design.DesignSurface) -> Microsoft.VisualStudio.Shell.Design.DesignerWindowPane
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.CanResetValue(Component As Object) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.ComponentType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.Converter() -> System.ComponentModel.TypeConverter
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.DisplayName() -> String
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.GetChildProperties(instance As Object, filter As System.Attribute()) -> System.ComponentModel.PropertyDescriptorCollection
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.GetEditor(editorBaseType As System.Type) -> Object
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.GetValue(Component As Object) -> Object
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.IsReadOnly() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.Name() -> String
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.PropertyType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.ResetValue(Component As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.SetValue(Component As Object, Value As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.ShouldSerializeValue(Component As Object) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.CreateStore() -> System.ComponentModel.Design.Serialization.SerializationStore
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.Deserialize(Store As System.ComponentModel.Design.Serialization.SerializationStore, Container As System.ComponentModel.IContainer) -> System.Collections.ICollection
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.Deserialize(Store As System.ComponentModel.Design.Serialization.SerializationStore) -> System.Collections.ICollection
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.DeserializeTo(Store As System.ComponentModel.Design.Serialization.SerializationStore, Container As System.ComponentModel.IContainer, ValidateRecycledTypes As Boolean, applyDefaults As Boolean) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.LoadStore(Stream As System.IO.Stream) -> System.ComponentModel.Design.Serialization.SerializationStore
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.Serialize(Store As System.ComponentModel.Design.Serialization.SerializationStore, Value As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.SerializeAbsolute(store As System.ComponentModel.Design.Serialization.SerializationStore, value As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.SerializeMember(Store As System.ComponentModel.Design.Serialization.SerializationStore, OwningObject As Object, Member As System.ComponentModel.MemberDescriptor) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.SerializeMemberAbsolute(Store As System.ComponentModel.Design.Serialization.SerializationStore, OwningObject As Object, Member As System.ComponentModel.MemberDescriptor) -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerLoader.Dispose() -> Void
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PreProcessMessage(ByRef msg As System.Windows.Forms.Message) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel.ScrollToControl(activeControl As System.Windows.Forms.Control) -> System.Drawing.Point
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox.Show(RootDesigner As Microsoft.VisualStudio.Editors.AppDesDesignerFramework.BaseRootDesigner, Message As String, Caption As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton = System.Windows.Forms.MessageBoxDefaultButton.Button1, HelpLink As String = Nothing) -> System.Windows.Forms.DialogResult
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox.Show(ServiceProvider As System.IServiceProvider, ex As System.Exception, Caption As String, HelpLink As String = Nothing) -> Void
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox.Show(ServiceProvider As System.IServiceProvider, Message As String, Caption As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton = System.Windows.Forms.MessageBoxDefaultButton.Button1, HelpLink As String = Nothing) -> System.Windows.Forms.DialogResult
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox.Show(ServiceProvider As System.IServiceProvider, Message As String, ex As System.Exception, Caption As String, HelpLink As String = Nothing) -> Void
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.DesignerMessageBox.ShowInternal(UIService As System.Windows.Forms.Design.IUIService, VsUIShell As Microsoft.VisualStudio.Shell.Interop.IVsUIShell, Message As String, Caption As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton, HelpLink As String) -> System.Windows.Forms.DialogResult
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.QueryEditableFiles(sp As System.IServiceProvider, files As System.Collections.Generic.List(Of String), throwOnFailure As Boolean, checkOnly As Boolean, ByRef fileReloaded As Boolean, allowInMemoryEdits As Boolean = True, allowFileReload As Boolean = True) -> Boolean
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.QueryEditableFiles(sp As System.IServiceProvider, files As System.Collections.Generic.List(Of String), throwOnFailure As Boolean, checkOnly As Boolean) -> Boolean
Shared Microsoft.VisualStudio.Editors.AppDesDesignerFramework.SourceCodeControlManager.QuerySave(sp As System.IServiceProvider, files As System.Collections.Generic.List(Of String), throwOnFailure As Boolean) -> Boolean
Shared Microsoft.VisualStudio.Editors.AppDesInterop.CAUUIDMarshaler.GetData(cauuid As Microsoft.VisualStudio.OLE.Interop.CAUUID) -> System.Guid()
Shared Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.CommandUIGuid() -> System.Guid
Shared Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.EditorGuid() -> System.Guid
Shared Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.IsAnyCpsComponent(components As Object()) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.CpsPropertyDescriptorWrapper.IsCpsComponent(component As Object) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetAllPropertyValuesNative(Descriptor As System.ComponentModel.PropertyDescriptor, Extenders As Object(), ByRef Values As Object(), ByRef ValueOrIndeterminate As Object) -> Void
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetCommonPropertyValue(Descriptor As System.ComponentModel.PropertyDescriptor, ProjectCommonPropertiesObject As Object) -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, ProjectCommonPropertiesObject As Object) -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetNonCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, Extender As Object) -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetValueOrIndeterminateFromArray(Values As Object()) -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.HideOrDisableControls(Controls As System.Windows.Forms.Control(), Hide As Boolean) -> Void
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.Indeterminate() -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsSpecialValue(Value As Object) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MissingProperty() -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ObjectsAreEqual(Object1 As Object, Object2 As Object) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropertyDescriptorSetValue(Descriptor As System.ComponentModel.PropertyDescriptor, Component As Object, Value As Object) -> Void
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, Value As Object, ProjectCommonPropertiesObject As Object) -> Void
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.TryGetNonCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, Extenders As Object()) -> Object
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener.TryCreate(PropPage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase, EventSource As Object, DebugSourceName As String, ProjectHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ListenToInactiveConfigs As Boolean) -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyFromRunningPages(SourcePage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase, dispid As Integer, ByRef obj As Object) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.SKUMatrix.IsHidden(PropertyId As Integer) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsAcademic() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsEnterprise() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsExpress() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsProfessional() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsStandard() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsVB() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsVC() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsVSTO() -> Boolean
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.ProductSKU() -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.ProductSubSKU() -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition
Shared Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.CommandUIGuid() -> System.Guid
Shared Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.EditorGuid() -> System.Guid
Shared Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.CommitAnyPendingChanges() -> Void
Shared Microsoft.VisualStudio.Editors.VBPackageUtils.PackageInstance(GetService As Microsoft.VisualStudio.Editors.VBPackageUtils.getServiceDelegate) -> Microsoft.VisualStudio.Editors.IVBPackage
Shared ReadOnly Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropPageBackColor -> System.Drawing.Color
VSThemedLinkLabel
VSThemedLinkLabel.New() -> Void
VSThemedLinkLabel.SetThemedColor(vsUIShell5 As Microsoft.VisualStudio.Shell.Interop.IVsUIShell5, supportsTheming As Boolean) -> Void
VSThemedLinkLabel.SetThemedColor(vsUIShell5 As Microsoft.VisualStudio.Shell.Interop.IVsUIShell5) -> VoidConst Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.PROPPAGESTATUS_CLEAN = 4 -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.PROPPAGESTATUS_DIRTY = 1 -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.PROPPAGESTATUS_VALIDATE = 2 -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SW_HIDE = 0 -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SW_SHOW = 5 -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SW_SHOWNORMAL = 1 -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.NestingCharacter = ":" -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Const Microsoft.VisualStudio.Editors.SettingsDesigner.PublicSettingsSingleFileGenerator.SingleFileGeneratorName = "PublicSettingsSingleFileGenerator" -> String
Const Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator.SingleFileGeneratorName = "SettingsSingleFileGenerator" -> String
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.Close() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.MapLogicalView(ByRef rguidLogicalView As System.Guid, ByRef pbstrPhysicalView As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.SetSite(Site As Microsoft.VisualStudio.OLE.Interop.IServiceProvider) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader.InitializeEx(ServiceProvider As Microsoft.VisualStudio.Shell.ServiceProvider, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, punkDocData As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ActualGuid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CloseFrame() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CommitPendingEdit() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CreateDesigner() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomMkDocumentProvider() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomMkDocumentProvider(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomViewProvider() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CustomViewProvider(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocCookie() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocData() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocData(Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocView() -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.DocView(Value As System.Windows.Forms.Control) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditFlags() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditFlags(Value As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorCaption() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorCaption(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorGuid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.EditorGuid(Value As System.Guid) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.Hierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.IsDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.IsPropertyPage() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ItemId() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.MkDocument() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.MkDocument(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.New(View As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.New(View As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, PropertyPageInfo As Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.OnWindowActivated(activated As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.PhysicalView() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.PhysicalView(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.PropertyPageInfo() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ShowDesigner(Show As Boolean = True) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabAutomationName() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabAutomationName(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabTitle() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.TabTitle(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.UpdateWindowFrameBounds() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.VsUIShell5() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.VsWindowFrame() -> Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.VsWindowFrame(Value As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.m_Debug_cWindowFrameBoundsUpdated -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.m_Debug_cWindowFrameShow -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.Hierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.Hierarchy(Value As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.ItemId() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.ItemId(Value As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent.RootDesigner() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.CommitAnyPendingChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.Component() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootComponent (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.GetView() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.ActiveView() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.ActiveView(Value As System.Guid) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.CommitAnyPendingChanges() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DTEProject() -> EnvDTE.Project (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DelayRefreshDirtyIndicators() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DsMsgBox(Message As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton = System.Windows.Forms.MessageBoxDefaultButton.Button1, HelpLink As String = Nothing) -> System.Windows.Forms.DialogResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.DsMsgBox(ex As System.Exception, HelpLink As String = Nothing) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.GetPropertyPages() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.GetSaveTreeItems(flags As Microsoft.VisualStudio.Shell.Interop.__VSRDTSAVEOPTIONS) -> Microsoft.VisualStudio.Shell.Interop.VSSAVETREEITEM() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.InitView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.InitializationComplete() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.New(serviceProvider As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.NotifyShuttingDown() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterAttributeChange(docCookie As UInteger, grfAttribs As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterDocumentWindowHide(docCookie As UInteger, pFrame As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterFirstDocumentLock(docCookie As UInteger, dwRDTLockType As UInteger, dwReadLocksRemaining As UInteger, dwEditLocksRemaining As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterLastDocumentUnlock(Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, MkDocument As String, ClosedWithoutSaving As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterSave(docCookie As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnAfterSaveAll() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnBeforeDocumentWindowShow(docCookie As UInteger, fFirstShow As Integer, pFrame As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnBeforeFirstDocumentLock(Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ItemId As UInteger, MkDocument As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnBeforeLastDocumentUnlock(docCookie As UInteger, dwRDTLockType As UInteger, dwReadLocksRemaining As UInteger, dwEditLocksRemaining As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnCmdUIContextChanged(dwCmdUICookie As UInteger, fActive As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnElementValueChanged(elementid As UInteger, varValueOld As Object, varValueNew As Object) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnInitializationComplete() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnSelectionChanged(pHierOld As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidOld As UInteger, pMISOld As Microsoft.VisualStudio.Shell.Interop.IVsMultiItemSelect, pSCOld As Microsoft.VisualStudio.Shell.Interop.ISelectionContainer, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger, pMISNew As Microsoft.VisualStudio.Shell.Interop.IVsMultiItemSelect, pSCNew As Microsoft.VisualStudio.Shell.Interop.ISelectionContainer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.SetUndoRedoCleanStateOnAllPropertyPages() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.SpecialFiles() -> Microsoft.VisualStudio.Shell.Interop.IVsProjectSpecialFiles (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.SwitchTab(forward As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.WindowFrame() -> Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.ActivateLogicalView(ByRef rguidLogicalView As System.Guid) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.AppDesignerView() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.CloseFrameNoSave() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.ClosePromptSave() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.GetActiveLogicalView(ByRef pguidLogicalView As System.Guid) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.IVsWindowPaneCommit_CommitPendingEdit(ByRef pfCommitFailed As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.IsLogicalViewActive(ByRef rguidLogicalView As System.Guid, ByRef pIsActive As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.New(surface As System.ComponentModel.Design.DesignSurface) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.NextTab() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.PrevTab() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.SaveChildren(flags As Microsoft.VisualStudio.Shell.Interop.__VSRDTSAVEOPTIONS) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.SaveProjectFile() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.VsUIShell2Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell2 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.VsUIShell5Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.VsUIShellService() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPaneControl (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPaneControl.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CmdTargetHelper (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CmdTargetHelper.New(WindowPane As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.DeferrableWindowPaneProviderService (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.DeferrableWindowPaneProviderService.New(provider As System.IServiceProvider, docData As Microsoft.VisualStudio.Shell.Design.Serialization.DocData) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.New(ErrorText As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.New(Exception As System.Exception) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.DelayRefreshDirtyIndicators() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.DsMsgBox(ex As System.Exception, HelpLink As String = Nothing) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.GetLocaleID() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IVsEditWindowNotify (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.IVsEditWindowNotify.OnActivated(activated As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.AccessibleState() -> System.Windows.Forms.AccessibleStates (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.ButtonIndex() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.DirtyIndicator() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.DirtyIndicator(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.Location() -> System.Drawing.Point (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.Location(Value As System.Drawing.Point) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.SetIndex(index As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.TextWithDirtyIndicator() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.AddTab(Title As String, AutomationName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ClearTabs() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.GetTabButton(index As Integer) -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.HostingPanel() -> System.Windows.Forms.Panel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.HoverItem() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.InvalidateLayout() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemEnter(e As System.EventArgs, item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemLeave(e As System.EventArgs, item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.Renderer() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedIndex() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedIndex(Value As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedItem() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.SelectedItem(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ServiceProvider() -> System.IServiceProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ServiceProvider(Value As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.TabButtonCount() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.TabButtons() -> System.Collections.Generic.IEnumerable(Of Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChanged -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.VsUIShell2Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell2 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.VsUIShell5Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.VsUIShellService() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.CreateGDIObjects(ForceUpdate As Boolean = False) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.New(owner As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.PerformLayout() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.PreferredButtonForSwitchableSlot() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.PreferredButtonForSwitchableSlot(Value As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.RenderBackground(g As System.Drawing.Graphics) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.RenderButton(g As System.Drawing.Graphics, button As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton, IsSelected As Boolean, IsHovered As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.ServiceProvider() -> System.IServiceProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.ServiceProvider(Value As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabRenderer.UpdateCacheState() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.ComPropPageInstance() -> Microsoft.VisualStudio.OLE.Interop.IPropertyPage (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Guid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.IsConfigPage() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.LoadException() -> System.Exception (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.New(ParentView As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, Guid As System.Guid, IsConfigurationDependentPage As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Site() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Title() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.BackingServiceProvider() -> System.IServiceProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.BackingServiceProvider(Value As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.CommitPendingChanges() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.GetLocaleID(ByRef pLocaleID As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.GetPageContainer(ByRef ppunk As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.GetService(serviceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.HasBeenSetDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.HasBeenSetDirty(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.New(View As Microsoft.VisualStudio.Editors.ApplicationDesigner.IPropertyPageSiteOwner, PropPage As Microsoft.VisualStudio.OLE.Interop.IPropertyPage) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.OnStatusChange(dwFlags As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.QueryService(ByRef guidService As System.Guid, ByRef riid As System.Guid, ByRef ppvObject As System.IntPtr) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.TranslateAccelerator(pMsg As Microsoft.VisualStudio.OLE.Interop.MSG()) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomDocumentMonikerProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomDocumentMonikerProvider.New(DesignerView As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, SpecialFileId As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.SetSite(ViewProvider As Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.DesignerPanel() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.DesignerView() -> Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.LinkText() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.New(DesignerView As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView, DesignerPanel As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel, SpecialFileId As Integer, LinkText As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.SpecialFileId() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.AreFilesEditable() -> Boolean
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.EnsureFilesEditable() -> Void
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.ManageFile(mkDocument As String) -> Void
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.ManagedFiles() -> System.Collections.Generic.List(Of String)
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.ManagedFiles(Value As System.Collections.Generic.List(Of String)) -> Void
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.New(sp As System.IServiceProvider, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Void
Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.StopManagingFile(mkDocument As String) -> Void
Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes
Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes.CommandLineApp = 2 -> Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes
Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes.WebControl = 4 -> Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes
Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes.WindowsApp = 0 -> Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes
Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes.WindowsClassLib = 1 -> Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes
Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes.WindowsService = 3 -> Microsoft.VisualStudio.Editors.MyApplication.ApplicationTypes
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.AuthenticationMode() -> Integer
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.AuthenticationMode(Value As Integer) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.CustomSubMain() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.CustomSubMain(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.EnableVisualStyles() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.EnableVisualStyles(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.MainForm() -> String
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.MainForm(Value As String) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.SaveMySettingsOnExit() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.SaveMySettingsOnExit(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.ShutdownMode() -> Integer
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.ShutdownMode(Value As Integer) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.SingleInstance() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.SingleInstance(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.SplashScreen() -> String
Microsoft.VisualStudio.Editors.MyApplication.IVsMyApplicationProperties.SplashScreen(Value As String) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationCodeGenerator
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationCodeGenerator.New() -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationManager
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationManager.New() -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.AuthenticationMode() -> Integer
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.AuthenticationMode(Value As Integer) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.CustomSubMain() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.CustomSubMain(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.EnableVisualStyles() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.EnableVisualStyles(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.MainForm() -> String
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.MainForm(Value As String) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.PropertyChanged -> System.ComponentModel.PropertyChangedEventHandler
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.SaveMySettingsOnExit() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.SaveMySettingsOnExit(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.ShutdownMode() -> Integer
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.ShutdownMode(Value As Integer) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.SingleInstance() -> Boolean
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.SingleInstance(Value As Boolean) -> Void
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.SplashScreen() -> String
Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.SplashScreen(Value As String) -> Void
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ChangeSelection(ConfigIndex As Integer, PlatformIndex As Integer, FireNotifications As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ChangeSelection(ConfigName As String, ConfigSelectionType As Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes, PlatformName As String, PlatformSelectionType As Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes, PreferExactMatch As Boolean, FireNotifications As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.CheckForModeChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacks -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationDropdownEntries() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChanged -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.DisplayName() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.Name -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.New(Name As String, SelectionType As Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem.SelectionType -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.GetAllConfigs() -> Microsoft.VisualStudio.Shell.Interop.IVsCfg() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.IsSimplifiedConfigMode() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.New(Project As EnvDTE.Project, ProjectHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, View As Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnActiveProjectCfgChange(pIVsHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnCfgNameAdded(pszCfgName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnCfgNameDeleted(CfgName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnCfgNameRenamed(OldName As String, NewName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnPlatformNameAdded(pszPlatformName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.OnPlatformNameDeleted(pszPlatformName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.PlatformDropdownEntries() -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.DropdownItem() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.Project() -> EnvDTE.Project (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigIndex() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChanged -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedPlatformIndex() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.Active = 1 -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.All = 2 -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.Normal = 0 -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectionTypes.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChanged -> Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_Begin(ByRef pfCancelUpdate As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_Cancel() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_Done(fSucceeded As Integer, fModified As Integer, fCancelCommand As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.UpdateSolution_StartUpdate(ByRef pfCancelUpdate As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.VsCfgProvider() -> Microsoft.VisualStudio.Shell.Interop.IVsCfgProvider2 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.DeferrableWindowPaneProviderService (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.DeferrableWindowPaneProviderService.New(provider As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.ConfigNames -> String() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.DebugTrace(Message As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.GetObjects(VsCfgProvider As Microsoft.VisualStudio.Shell.Interop.IVsCfgProvider2) -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.New(VsCfgProvider As Microsoft.VisualStudio.Shell.Interop.IVsCfgProvider2, Objects As Object(), Values As Object(), SelectedConfigName As String, SelectedPlatformName As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.PlatformNames -> String() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.SelectedConfigName -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.SelectedPlatformName -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.MultipleValuesStore.Values -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.Close() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.Close2() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetData(ByRef riidKey As System.Guid, ByRef pvtData As Object) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetGuidEditorType(ByRef pClassID As System.Guid) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetGuidEditorType2(ByRef pClassID As System.Guid) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetSite(ByRef riid As System.Guid, ByRef ppvSite As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.GetTextBuffer(ByRef ppTextBuffer As Microsoft.VisualStudio.TextManager.Interop.IVsTextLines) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataDirty(ByRef pfDirty As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataDirty2(ByRef pfDirty As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataReadOnly(ByRef pfReadOnly As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataReloadable(ByRef pfReloadable As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.IsDocDataReloadable2(ByRef pfReloadable As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadDocData(pszMkDocument As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadDocData2(pszMkDocument As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LockTextBuffer(fLock As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.New(BaseProvider As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnFileChanged -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnLoadCompleted -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnRegisterDocData(docCookie As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.OnRegisterDocData2(docCookie As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.ReloadDocData(grfFlags As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.ReloadDocData2(grfFlags As UInteger) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.RenameDocData(grfAttribs As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger, pszMkDocumentNew As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.RenameDocData2(grfAttribs As UInteger, pHierNew As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, itemidNew As UInteger, pszMkDocumentNew As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SaveDocData(dwSave As Microsoft.VisualStudio.Shell.Interop.VSSAVEFLAGS, ByRef pbstrMkDocumentNew As String, ByRef pfSaveCanceled As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SaveDocData2(dwSave As Microsoft.VisualStudio.Shell.Interop.VSSAVEFLAGS, ByRef pbstrMkDocumentNew As String, ByRef pfSaveCanceled As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetData(ByRef riidKey As System.Guid, vtData As Object) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetDocDataDirty(fDirty As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetDocDataReadOnly(fReadOnly As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetSite(pUnkSite As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetTextBuffer(pTextBuffer As Microsoft.VisualStudio.TextManager.Interop.IVsTextLines) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetUntitledDocPath(pszDocDataPath As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.SetUntitledDocPath2(pszDocDataPath As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.Close() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.MapLogicalView(ByRef rguidLogicalView As System.Guid, ByRef pbstrPhysicalView As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.SetSite(Site As Microsoft.VisualStudio.OLE.Interop.IServiceProvider) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerLoader (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerLoader.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.Hierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.Hierarchy(Value As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.ItemId() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.ItemId(Value As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.Name() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent.RootDesigner() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.Component() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootComponent (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.GetView() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ActivatePage(PropPage As Microsoft.VisualStudio.OLE.Interop.IPropertyPage) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.DTEProject() -> EnvDTE.Project (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.DesignerHost() -> System.ComponentModel.Design.IDesignerHost (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.DsMsgBox(Message As String, Buttons As System.Windows.Forms.MessageBoxButtons, Icon As System.Windows.Forms.MessageBoxIcon, DefaultButton As System.Windows.Forms.MessageBoxDefaultButton = System.Windows.Forms.MessageBoxDefaultButton.Button1, HelpLink As String = Nothing) -> System.Windows.Forms.DialogResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.FocusFirstOrLastPropertyPageControl(First As Boolean) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetProperty(PropertyName As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetPropertyPageTopHwnd() -> System.IntPtr (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.GetTransaction(Description As String) -> System.ComponentModel.Design.DesignerTransaction (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IVsProjectDesignerPageSite_OnPropertyChanged(PropertyName As String, PropertyDescriptor As System.ComponentModel.PropertyDescriptor, OldValue As Object, NewValue As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IVsProjectDesignerPageSite_OnPropertyChanging(PropertyName As String, PropertyDescriptor As System.ComponentModel.PropertyDescriptor) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IVsWindowPaneCommit_CommitPendingEdit(ByRef pfCommitFailed As Integer) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.Init(DTEProject As EnvDTE.Project, PropPage As Microsoft.VisualStudio.OLE.Interop.IPropertyPage, PropPageSite As Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite, Hierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, IsConfigPage As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IsConfigPage() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IsConfigPage(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.IsNativeHostedPropertyPageActivated() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.New(RootDesigner As Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.OnActivated(activated As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropPage() -> Microsoft.VisualStudio.OLE.Interop.IPropertyPage (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel.StopAutoScrollToControl(needStop As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SetProperty(PropertyName As String, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.SetUndoRedoCleanState() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ShouldShowDirtyIndicator() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ShowErrorMessage(Message As String, HelpLink As String = Nothing) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.UnLoadPage() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerWindowPane (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerWindowPane.New(surface As System.ComponentModel.Design.DesignSurface) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.New(PropDesc As System.ComponentModel.PropertyDescriptor, PropertyName As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.New(Provider As System.IServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.AddIconsFromProjectItem(ProjectItem As EnvDTE.ProjectItem, ApplicationIconCombobox As System.Windows.Forms.ComboBox) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.AddManifestsFromProjectItem(ProjectItem As EnvDTE.ProjectItem, ApplicationManifestCombobox As System.Windows.Forms.ComboBox) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.ApplicationIconGet(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, ByRef value As Object) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.ApplicationManifestEntryIsDefault(text As String) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.ApplicationManifestSupported() -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.BrowseForAppIcon(ApplicationIconCombobox As System.Windows.Forms.ComboBox, ApplicationIconPictureBox As System.Windows.Forms.PictureBox) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.IconEntryIsSpecial(EntryText As String) -> Boolean
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.LastIconImage() -> String
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.UpdateIconImage(ApplicationIconCombobox As System.Windows.Forms.ComboBox, ApplicationIconPictureBox As System.Windows.Forms.PictureBox, AddToProject As Boolean) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.m_DefaultIcon -> System.Drawing.Icon
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.m_DefaultIconText -> String
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.m_DefaultManifestText -> String
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.m_NoManifestText -> String
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationWithMyPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.ApplicationWithMyPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.BuildEventsPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.BuildEventsPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.BuildPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.BuildPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.CSharpApplicationPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.CSharpApplicationPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.GetLocaleID() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.GetTransaction(description As String) -> System.ComponentModel.Design.DesignerTransaction (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.New(childPage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase, wrappedInternalSite As Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal, wrappedUndoSite As Microsoft.VisualStudio.ManagedInterfaces.ProjectDesigner.IVsProjectDesignerPageSite) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.OnPropertyChanged(propertyName As String, propertyDescriptor As System.ComponentModel.PropertyDescriptor, oldValue As Object, newValue As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.OnPropertyChanging(propertyName As String, propertyDescriptor As System.ComponentModel.PropertyDescriptor) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.OnStatusChange(flags As Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ChildPageSite.TranslateAccelerator(msg As System.Windows.Forms.Message) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.CompilePropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.CompilePropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.CommonProperty = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.Dirty = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.Hidden = 64 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.NoOptimisticFileCheckout = 32768 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.None = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInAppManifestFile = 1024 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInApplicationDefinitionFile = 16384 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInAssemblyInfoFile = 2048 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInProjectUserFile = 256 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.PersistedInVBMyAppFile = 512 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.ProjectMayBeReloadedDuringPropertySet = 4096 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.RefreshAllPropertiesWhenChanged = 8192 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.UserHandledEvents = 32 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.UserPersisted = 16 -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.DebugPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.DebugPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.Apply() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.EditProperty(dispid As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.GetHelpContextF1Keyword() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.Help(HelpDir As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.IsPageDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.SetObjects(objects As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageInternal.SetPageSite(base As Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.GetLocaleID() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.IsImmediateApply() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.OnStatusChange(flags As Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.IPropertyPageSiteInternal.TranslateAccelerator(msg As System.Windows.Forms.Message) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.MyExtensibilityPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.MyExtensibilityPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.Clean = 4 -> Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.Dirty = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.Validate = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PackagePropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.PackagePropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ProjectReloadedException (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ProjectReloadedException.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ProjectReloadedException.New(Info As System.Runtime.Serialization.SerializationInfo, Context As System.Runtime.Serialization.StreamingContext) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.FinishPendingValidations() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetLocaleID() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetService(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.OnStatusChange(flags As Microsoft.VisualStudio.Editors.PropertyPages.PROPPAGESTATUS) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.OnWindowActivated(activated As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.TranslateAccelerator(msg As System.Windows.Forms.Message) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.New(ServiceProvider As System.IServiceProvider, F1Keyword As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.PropPage() -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.PropPage(Value As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.SetFocusToPage() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddChangeHandlers() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ApplyChanges(sender As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CanApplyNow() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CanApplyNow(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CheckoutProjectFile(ByRef ProjectReloaded As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ClearIsDirty() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CommonPropertiesObject() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DISPID_UNKNOWN -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DTE() -> EnvDTE.DTE (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DTEProject() -> EnvDTE.Project (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DelayValidate(dataControl As System.Windows.Forms.Control) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EnableControl(control As System.Windows.Forms.Control, enabled As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Enabled() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Enabled(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EnterProjectCheckoutSection() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ExtendedPropertiesObjects(Data As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData) -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyDescriptor(PropertyName As String) -> System.ComponentModel.PropertyDescriptor (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValue(PropertyName As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValue(prop As System.ComponentModel.PropertyDescriptor) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValueNative(PropertyName As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCommonPropertyValueNative(prop As System.ComponentModel.PropertyDescriptor) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetControlValue(name As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetControlValueNative(name As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetCurrentProperty(dispid As Integer, PropertyName As String, ByRef obj As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDialogFont() -> System.Drawing.Font (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirectoryViaBrowse(InitialDirectory As String, DialogTitle As String, ByRef NewValue As String) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirectoryViaBrowseRelative(RelativeInitialDirectory As String, BasePath As String, DialogTitle As String, ByRef NewRelativePath As String) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirectoryViaBrowseRelativeToProject(InitialDirectory As String, DialogTitle As String, ByRef NewValue As String) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetDirty(sender As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetFileViaBrowse(InitialDirectory As String, ByRef NewValue As String, Filter As String) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProjectPath() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProjectRelativeDirectoryPath(DirectoryPath As String) -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProjectRelativeFilePath(FilePath As String) -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyDescriptor(PropertyName As String) -> System.ComponentModel.PropertyDescriptor (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetRelativeDirectoryPath(BasePath As String, DirectoryPath As String) -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetRelativeFilePath(BasePath As String, FilePath As String) -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetServiceFromPropertyPageSite(ServiceType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.InitializeAllProperties() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsActivated() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsAnyPropertyDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsCSProject() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsConfigurationSpecificPage() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsDirty(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsInProjectCheckoutSection() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsUndoEnabled() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsVBProject() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.LeaveProjectCheckoutSection() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ManualPageScaling() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ManualPageScaling(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.MultiProjectSelect() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.New(serviceProvider As Microsoft.VisualStudio.Shell.ServiceProvider) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyChanged(DISPID As Integer, DebugSourceName As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyRequestEdit(DISPID As Integer, DebugSourceName As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PageRequiresScaling() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PageRequiresScaling(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProcessDelayValidationQueue(canThrow As Boolean) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectHierarchy() -> Microsoft.VisualStudio.Shell.Interop.IVsHierarchy (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectKind() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectLanguage() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectProperties() -> VSLangProj.ProjectProperties (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProjectReloadedDuringCheckout() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.Direct = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.External = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.Indirect = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyPageSite() -> Microsoft.VisualStudio.OLE.Interop.IPropertyPageSite (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RawPropertiesObjects(Data As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData) -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ResumePropertyChangeListening(DispId As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ServiceProvider() -> Microsoft.VisualStudio.Shell.ServiceProvider (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValue(PropertyName As String, value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValue(prop As System.ComponentModel.PropertyDescriptor, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValueNative(PropertyName As String, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetCommonPropertyValueNative(prop As System.ComponentModel.PropertyDescriptor, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(ReadyToApply As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(dispid As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(dispid As Integer, ReadyToApply As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(sender As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDirty(sender As Object, ReadyToApply As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowChildPage(Title As String, PageType As System.Type) -> System.Windows.Forms.DialogResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowChildPage(Title As String, PageType As System.Type, F1Keyword As String) -> System.Windows.Forms.DialogResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(errorMessage As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(errorMessage As String, HelpLink As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(errorMessage As String, ex As System.Exception) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(ex As System.Exception) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ShowErrorMessage(ex As System.Exception, HelpLink As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SkipValidating(dataControl As System.Windows.Forms.Control) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SuspendPropertyChangeListening(DispId As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.TryGetNonCommonPropertyValue(Descriptor As System.ComponentModel.PropertyDescriptor) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ValidatePageChanges(allowDelayValidation As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.VsUIShell2Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell2 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.VsUIShell5Service() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell5 (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.VsUIShellService() -> Microsoft.VisualStudio.Shell.Interop.IVsUIShell (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_CommonPropertyDescriptors -> System.ComponentModel.PropertyDescriptorCollection (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ControlData -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ExtendedObjects -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_IsDirty -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_Objects -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ObjectsPropertyDescriptorsArray -> System.ComponentModel.PropertyDescriptorCollection() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_ScalingCompleted -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.m_fInsideInit -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AllInitialValues() -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AllInitialValuesExpanded() -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AssociatedControls -> System.Windows.Forms.Control() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.CommonPropertiesObject() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.DispId() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.DisplayPropertyName -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.EnableAssociatedControl(control As System.Windows.Forms.Control, Enabled As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.EnableControls(Enabled As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.Flags -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.FormControl() -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetControlValueMultipleValues() -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetControlValueNative() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetFlags() -> Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.InitialValue() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsCommonProperty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsCommonProperty(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsConfigurationSpecificProperty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsDirty(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsHidden() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsHidden(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsIndeterminate() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsMissing() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsReadOnly() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsSpecialValue() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserHandledEvents() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserHandledEvents(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserPersisted() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsUserPersisted(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, AssocControls As System.Windows.Forms.Control()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssocControls As System.Windows.Forms.Control()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssocControls As System.Windows.Forms.Control()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssocControls As System.Windows.Forms.Control()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.New(id As Integer, name As String, FormControl As System.Windows.Forms.Control, setter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate, getter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate, multiValueSetter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate, multiValueGetter As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate, flags As Microsoft.VisualStudio.Editors.PropertyPages.ControlDataFlags, AssociatedControls As System.Windows.Forms.Control()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ObjectsPropertyDescriptorsArray() -> System.ComponentModel.PropertyDescriptorCollection() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropDesc -> System.ComponentModel.PropertyDescriptor (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropPage() -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropertyName() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetCallback -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetControlValue(value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate.New(TargetObject As Object, TargetMethod As System.IntPtr) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDirty(ReadyToApply As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetInitialValues(AllInitialValues As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetInitialValues(InitialValue As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetInitialValues(InitialValue As Object, AllInitialValues As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_FormControl -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_Initializing -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_PropPage -> Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.m_isCommitingChange -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener.OnChanged(dispid As Integer, wszConfigName As String) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(Info As System.Runtime.Serialization.SerializationInfo, Context As System.Runtime.Serialization.StreamingContext) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, helpLink As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, helpLink As String, innerException As System.Exception) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, innerException As System.Exception) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.New(message As String, innerException As System.Exception, ShowHeaderAndFooterInErrorControl As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.ShowHeaderAndFooterInErrorControl() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.PropertyPageException.ShowHeaderAndFooterInErrorControl(Value As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ReferencePathsPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.ReferencePathsPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ReferencePropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.ReferencePropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.ServicesPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.ServicesPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor
Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.New(Name As String, PropertyType As System.Type) -> Void
Microsoft.VisualStudio.Editors.PropertyPages.VBPropPageBase (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VBPropPageBase.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.New() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.AcademicProfessional = 2100 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.AcademicStudent = 2100 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.DownloadTrial = 2500 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Enterprise = 3000 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Express = 500 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.None = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Professional = 2000 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.Standard = 1000 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.VSTO = 1500 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.Architect = 8 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.CSharp = 4 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.IDE = 16 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.None = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.VB = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.VC = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.Web = 64 -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.Failed = 2 -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.Succeeded = 0 -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.Warning = 1 -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult.value__ -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Microsoft.VisualStudio.Editors.PropertyPages.WPFApplicationWithMyPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.WPFApplicationWithMyPropPageComClass.New() -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.BeforeOpeningFile(projectItem As EnvDTE.ProjectItem) -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.New() -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.ProjectFinishedGenerating(project As EnvDTE.Project) -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.ProjectItemFinishedGenerating(projectItem As EnvDTE.ProjectItem) -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.RunFinished() -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.RunStarted(automationObject As Object, replacementsDictionary As System.Collections.Generic.Dictionary(Of String, String), runKind As Microsoft.VisualStudio.TemplateWizard.WizardRunKind, customParams As Object()) -> Void
Microsoft.VisualStudio.Editors.ResourceEditor.ResxItemWizard.ShouldAddProjectItem(filePath As String) -> Boolean
Microsoft.VisualStudio.Editors.SettingsDesigner.PublicSettingsSingleFileGenerator
Microsoft.VisualStudio.Editors.SettingsDesigner.PublicSettingsSingleFileGenerator.New() -> Void
Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator
Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator.New() -> Void
Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGeneratorBase
Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGeneratorBase.New() -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.BeforeOpeningFile(projectItem As EnvDTE.ProjectItem) -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.New() -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.ProjectFinishedGenerating(project As EnvDTE.Project) -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.ProjectItemFinishedGenerating(projectItem As EnvDTE.ProjectItem) -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.RunFinished() -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.RunStarted(automationObject As Object, replacementsDictionary As System.Collections.Generic.Dictionary(Of String, String), runKind As Microsoft.VisualStudio.TemplateWizard.WizardRunKind, customParams As Object()) -> Void
Microsoft.VisualStudio.Editors.XmlToSchema.Wizard.ShouldAddProjectItem(filePath As String) -> Boolean
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomDocumentMonikerProvider.GetDocumentMoniker() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.CloseView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.CreateView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
MustOverride Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.View() -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
MustOverride Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.ControlType() -> System.Type (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
MustOverride Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.CreateControl() -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
MustOverride Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Title() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.Dispose(disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageSite.Dispose(disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.Dispose() -> Void
Overloads Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(FileName As String) -> EnvDTE.ProjectItem (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(FileName As String, CopyFile As Boolean) -> EnvDTE.ProjectItem (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(ProjectItems As EnvDTE.ProjectItems, FileName As String, CopyFile As Boolean) -> EnvDTE.ProjectItem (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.AddFileToProject(ProjectItems As EnvDTE.ProjectItems, FileName As String, CopyFile As Boolean, BuildAction As VSLangProj.prjBuildAction) -> EnvDTE.ProjectItem (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overloads Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.CloseFrameInternal(WindowFrame As Microsoft.VisualStudio.Shell.Interop.IVsWindowFrame, flags As Microsoft.VisualStudio.Shell.Interop.__FRAMECLOSE) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.ShowWindowFrame() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.CustomViewProvider.Dispose(Disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton, reactivatePage As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnItemGotFocus(e As System.EventArgs, item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnThemeChanged() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OverflowButton() -> System.Windows.Forms.Button (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OverflowButton(WithEventsValue As System.Windows.Forms.Button) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler.BeginInvoke(sender As Object, args As System.EventArgs, DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.ThemeChangedEventHandler.Invoke(sender As Object, args As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.PropertyPageInfo.TryLoadPropertyPage() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.LinkLabel() -> VSThemedLinkLabel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.LinkLabel(WithEventsValue As VSThemedLinkLabel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler.BeginInvoke(DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ClearConfigPageUndoRedoStacksEventHandler.Invoke() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler.BeginInvoke(DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.ConfigurationListAndSelectionChangedEventHandler.Invoke() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler.BeginInvoke(DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SelectedConfigurationChangedEventHandler.Invoke() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler.BeginInvoke(DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.ConfigurationState.SimplifiedConfigModeChangedEventHandler.Invoke() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate.BeginInvoke(ChangeFlags As UInteger, FileAttrs As UInteger, DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.FileChangedDelegate.Invoke(ChangeFlags As UInteger, FileAttrs As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate.BeginInvoke(Reload As Integer, DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerDocData.LoadCompletedDelegate.Invoke(Reload As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigDividerLine() -> System.Windows.Forms.Label (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigDividerLine(WithEventsValue As System.Windows.Forms.Label) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationComboBox() -> System.Windows.Forms.ComboBox (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationComboBox(WithEventsValue As System.Windows.Forms.ComboBox) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationFlowLayoutPanel() -> System.Windows.Forms.FlowLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationFlowLayoutPanel(WithEventsValue As System.Windows.Forms.FlowLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationLabel() -> System.Windows.Forms.Label (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationLabel(WithEventsValue As System.Windows.Forms.Label) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationPanel() -> System.Windows.Forms.TableLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ConfigurationTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PLatformTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PLatformTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformComboBox() -> System.Windows.Forms.ComboBox (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformComboBox(WithEventsValue As System.Windows.Forms.ComboBox) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformLabel() -> System.Windows.Forms.Label (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PlatformLabel(WithEventsValue As System.Windows.Forms.Label) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropPageDesignerViewLayoutPanel() -> System.Windows.Forms.TableLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropPageDesignerViewLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropertyPagePanel() -> Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PropertyPagePanel(WithEventsValue As Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.AddIconEntryToCombobox(ApplicationIconCombobox As System.Windows.Forms.ComboBox, IconRelativePath As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.IconEntryIsBrowse(EntryText As String) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.IconEntryIsDefault(EntryText As String) -> Boolean
Overridable Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.PopulateIconList(FindIconsInProject As Boolean, ApplicationIconCombobox As System.Windows.Forms.ComboBox, CurrentIconValue As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.ApplicationPropPageBase.PopulateManifestList(FindManifestInProject As Boolean, ApplicationManifestCombobox As System.Windows.Forms.ComboBox, CurrentManifestValue As String) -> Void
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Apply() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.ControlTypeForResources() -> System.Type (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Deactivate() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DefaultSize() -> System.Drawing.Size (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DefaultSize(Value As System.Drawing.Size) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DocString() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.DocString(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetProperty(PropertyName As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.GetPropertyMultipleValues(PropertyName As String, ByRef Objects As Object(), ByRef Values As Object()) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Help(strHelpDir As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpContext() -> UInteger (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpContext(Value As UInteger) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpFile() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.HelpFile(Value As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.IsPageDirty() -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.Objects() -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetObjects(cObjects As UInteger, objects As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetProperty(PropertyName As String, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetPropertyMultipleValues(PropertyName As String, Objects As Object(), Values As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SetSite(site As Microsoft.VisualStudio.ManagedInterfaces.ProjectDesigner.IVsProjectDesignerPageSite) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SupportsMultipleValueUndo(PropertyName As String) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.SupportsTheming() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageBase.TranslateAccelerator(pMsg As Microsoft.VisualStudio.OLE.Interop.MSG()) -> Integer (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.Cancel() -> System.Windows.Forms.Button (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.Cancel(WithEventsValue As System.Windows.Forms.Button) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.OK() -> System.Windows.Forms.Button (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.OK(WithEventsValue As System.Windows.Forms.Button) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.okCancelTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.okCancelTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.overArchingTableLayoutPanel() -> System.Windows.Forms.TableLayoutPanel (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageHostDialog.overArchingTableLayoutPanel(WithEventsValue As System.Windows.Forms.TableLayoutPanel) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Apply() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ApplyPageChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CleanupCOMReferences() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.CommitTransaction(Transaction As System.ComponentModel.Design.DesignerTransaction) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ControlData() -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DisableOnBuild() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DisableOnDebug() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.DisableWhenDebugMode(mode As Microsoft.VisualStudio.Shell.Interop.DBGMODE) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EditProperty(dispid As Integer) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.EnableAllControls(enabled As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetF1HelpKeyword() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetProperty(dispid As Integer, ByRef obj As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyControl(PropertyId As Integer) -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyControlData(PropertyId As Integer) -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyControlData(PropertyName As String) -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetTransaction() -> System.ComponentModel.Design.DesignerTransaction (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetTransactionDescription() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetUserDefinedPropertyDescriptor(PropertyName As String) -> System.ComponentModel.PropertyDescriptor (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Help(HelpTopic As String) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_GetPropertyMultipleValues(PropertyName As String, ByRef Objects As Object(), ByRef Values As Object()) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_GetPropertyValue(PropertyName As String) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_SetPropertyValue(PropertyName As String, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_SetPropertyValueMultipleValues(PropertyName As String, Objects As Object(), Values As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IVsProjectDesignerPage_SupportsMultipleValueUndo(PropertyName As String) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.InitPage() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.IsPageDirty() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnApplyComplete(ApplySuccessful As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyChanged(DISPID As Integer, Source As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnExternalPropertyChanged(Data As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData, Source As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropertyChangeSource) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnPageActivated(activated As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnPropertyChanged(PropertyName As String, PropDesc As System.ComponentModel.PropertyDescriptor, OldValue As Object, NewValue As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnPropertyChanging(PropertyName As String, PropDesc As System.ComponentModel.PropertyDescriptor) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnSetSite(site As Microsoft.VisualStudio.OLE.Interop.IPropertyPageSite) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnThemeChanged() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PageResizable() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PostApplyPageChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PostInitPage() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PreApplyPageChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PreInitPage() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ReadUserDefinedProperty(PropertyName As String, ByRef Value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RefreshPropertyStandardValues() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RefreshPropertyValues() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.RestoreInitialValues() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ScaleWindowToCurrentFont() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetDialogFont(ScaleDialog As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SetObjects(objects As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.SupportsTheming() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ValidateProperty(controlData As Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData, ByRef message As String, ByRef returnControl As System.Windows.Forms.Control) -> Microsoft.VisualStudio.Editors.PropertyPages.ValidationResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ValidationControlGroups() -> System.Windows.Forms.Control()() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.WriteUserDefinedProperty(PropertyName As String, Value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.AddChangeHandlers() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ApplyChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ComboBox_SelectionChangeCommitted(sender As Object, e As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ExtendedPropertiesObjects() -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.FilesToCheckOut() -> String() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetAllPropertyValuesNative(Extenders As Object(), ByRef Values As Object(), ByRef ValueOrIndeterminate As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetControlValue() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate.BeginInvoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, ByRef value As Object, DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate.EndInvoke(ByRef value As Object, DelegateAsyncResult As System.IAsyncResult) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetDelegate.Invoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, ByRef value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetPropertyValueNative(Extender As Object) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetUserDefinedPropertyDescriptor() -> System.ComponentModel.PropertyDescriptor (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.InitPropertyUI() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.InitPropertyValue() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.Initialize(PropertyPage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate.BeginInvoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, ByRef Values As Object(), DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate.EndInvoke(ByRef Values As Object(), DelegateAsyncResult As System.IAsyncResult) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueGetDelegate.Invoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, ByRef Values As Object()) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate.BeginInvoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, Values As Object(), DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MultiValueSetDelegate.Invoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, Values As Object()) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.OnPropertyChanged(OldValue As Object, NewValue As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.OnPropertyChanging() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.RawPropertiesObjects() -> Object() (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ReadUserDefinedProperty(PropertyName As String, ByRef Value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.RefreshValue() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.RestoreInitialValue() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate.BeginInvoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, value As Object, DelegateCallback As System.AsyncCallback, DelegateAsyncState As Object) -> System.IAsyncResult (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate.EndInvoke(DelegateAsyncResult As System.IAsyncResult) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetDelegate.Invoke(control As System.Windows.Forms.Control, prop As System.ComponentModel.PropertyDescriptor, value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetNonCommonPropertyValueCore(Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetNonCommonPropertyValueMultipleValuesCore(Objects As Object(), Values As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetPropertyValue(Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetPropertyValueNative(Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetPropertyValueNativeMultipleValues(Objects As Object(), Values As Object()) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SupportsMultipleValueUndo() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.TryGetPropertyValueNative(Extenders As Object()) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.WriteUserDefinedProperty(PropertyName As String, Value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overridable Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGeneratorBase.AddRequiredReferences(GenerateProgress As Microsoft.VisualStudio.Shell.Interop.IVsGeneratorProgress) -> Void
Overridable Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGeneratorBase.GetProjectRootNamespace() -> String
Overridable Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGeneratorBase.OnCompileUnitCreated(compileUnit As System.CodeDom.CodeCompileUnit, generatedClass As System.CodeDom.CodeTypeDeclaration) -> Void
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerLoader.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.Dispose(disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerPanel.OnLayout(levent As System.Windows.Forms.LayoutEventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerRootDesigner.Initialize(component As System.ComponentModel.IComponent) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerView.OnItemClick(item As Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton, reactivatePage As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.EditorView() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerWindowPane.Window() -> System.Windows.Forms.IWin32Window (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.DeferrableWindowPaneProviderService.CreateWindowPane(surface As System.ComponentModel.Design.DesignSurface) -> Microsoft.VisualStudio.Shell.Design.DesignerWindowPane (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.CloseView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.CreateView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.Dispose(Disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ErrorControlCustomViewProvider.View() -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.CreateAccessibilityInstance() -> System.Windows.Forms.AccessibleObject (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnClick(e As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnGotFocus(e As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnLostFocus(e As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnMouseEnter(e As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnMouseLeave(e As System.EventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.OnPaint(e As System.Windows.Forms.PaintEventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabButton.ProcessDialogKey(keyData As System.Windows.Forms.Keys) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.CreateAccessibilityInstance() -> System.Windows.Forms.AccessibleObject (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.Dispose(disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnLayout(levent As System.Windows.Forms.LayoutEventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnPaint(e As System.Windows.Forms.PaintEventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.ProjectDesignerTabControl.OnPaintBackground(e As System.Windows.Forms.PaintEventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomDocumentMonikerProvider.GetDocumentMoniker() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomView.Dispose(disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.CloseView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.CreateView() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.Dispose(Disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.ApplicationDesigner.SpecialFileCustomViewProvider.View() -> System.Windows.Forms.Control (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.MyApplication.MyApplicationProperties.FilesToCheckOut(CreateIfNotExist As Boolean) -> String()
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.DeferrableWindowPaneProviderService.CreateWindowPane(surface As System.ComponentModel.Design.DesignSurface) -> Microsoft.VisualStudio.Shell.Design.DesignerWindowPane (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerLoader.Dispose() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.PreProcessMessage(ByRef msg As System.Windows.Forms.Message) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerView.ScrollablePanel.ScrollToControl(activeControl As System.Windows.Forms.Control) -> System.Drawing.Point (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.CanResetValue(Component As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.ComponentType() -> System.Type (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.Converter() -> System.ComponentModel.TypeConverter (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.DisplayName() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.GetChildProperties(instance As Object, filter As System.Attribute()) -> System.ComponentModel.PropertyDescriptorCollection (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.GetEditor(editorBaseType As System.Type) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.GetValue(Component As Object) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.IsReadOnly() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.Name() -> String (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.PropertyType() -> System.Type (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.ResetValue(Component As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.SetValue(Component As Object, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPagePropertyDescriptor.ShouldSerializeValue(Component As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.CreateStore() -> System.ComponentModel.Design.Serialization.SerializationStore (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.Deserialize(Store As System.ComponentModel.Design.Serialization.SerializationStore) -> System.Collections.ICollection (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.Deserialize(Store As System.ComponentModel.Design.Serialization.SerializationStore, Container As System.ComponentModel.IContainer) -> System.Collections.ICollection (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.DeserializeTo(Store As System.ComponentModel.Design.Serialization.SerializationStore, Container As System.ComponentModel.IContainer, ValidateRecycledTypes As Boolean, applyDefaults As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.LoadStore(Stream As System.IO.Stream) -> System.ComponentModel.Design.Serialization.SerializationStore (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.Serialize(Store As System.ComponentModel.Design.Serialization.SerializationStore, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.SerializeAbsolute(store As System.ComponentModel.Design.Serialization.SerializationStore, value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.SerializeMember(Store As System.ComponentModel.Design.Serialization.SerializationStore, OwningObject As Object, Member As System.ComponentModel.MemberDescriptor) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropPageDesigner.PropertyPageSerializationService.SerializeMemberAbsolute(Store As System.ComponentModel.Design.Serialization.SerializationStore, OwningObject As Object, Member As System.ComponentModel.MemberDescriptor) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropertyPages.MyExtensibilityPropPageComClass.ControlType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropertyPages.MyExtensibilityPropPageComClass.CreateControl() -> System.Windows.Forms.Control
Overrides Microsoft.VisualStudio.Editors.PropertyPages.MyExtensibilityPropPageComClass.Title() -> String
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.Dispose(disposing As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPreferredSize(startSize As System.Drawing.Size) -> System.Drawing.Size (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.OnLayout(levent As System.Windows.Forms.LayoutEventArgs) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.ProcessDialogKey(keyData As System.Windows.Forms.Keys) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.WndProc(ByRef m As System.Windows.Forms.Message) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.CanResetValue(component As Object) -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.ComponentType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.GetValue(component As Object) -> Object
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.IsReadOnly() -> Boolean
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.PropertyType() -> System.Type
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.ResetValue(component As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.SetValue(component As Object, value As Object) -> Void
Overrides Microsoft.VisualStudio.Editors.PropertyPages.UserPropertyDescriptor.ShouldSerializeValue(component As Object) -> Boolean
Shared Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.CommandUIGuid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.ApplicationDesigner.ApplicationDesignerEditorFactory.EditorGuid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.QueryEditableFiles(sp As System.IServiceProvider, files As System.Collections.Generic.List(Of String), throwOnFailure As Boolean, checkOnly As Boolean) -> Boolean
Shared Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.QueryEditableFiles(sp As System.IServiceProvider, files As System.Collections.Generic.List(Of String), throwOnFailure As Boolean, checkOnly As Boolean, ByRef fileReloaded As Boolean, allowInMemoryEdits As Boolean = True, allowFileReload As Boolean = True) -> Boolean
Shared Microsoft.VisualStudio.Editors.DesignerFramework.SourceCodeControlManager.QuerySave(sp As System.IServiceProvider, files As System.Collections.Generic.List(Of String), throwOnFailure As Boolean) -> Boolean
Shared Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.CommandUIGuid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerEditorFactory.EditorGuid() -> System.Guid (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropPageDesigner.PropPageDesignerRootDesigner.CommitAnyPendingChanges() -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.GetPropertyFromRunningPages(SourcePage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase, dispid As Integer, ByRef obj As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetAllPropertyValuesNative(Descriptor As System.ComponentModel.PropertyDescriptor, Extenders As Object(), ByRef Values As Object(), ByRef ValueOrIndeterminate As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetCommonPropertyValue(Descriptor As System.ComponentModel.PropertyDescriptor, ProjectCommonPropertiesObject As Object) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, ProjectCommonPropertiesObject As Object) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetNonCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, Extender As Object) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.GetValueOrIndeterminateFromArray(Values As Object()) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.HideOrDisableControls(Controls As System.Windows.Forms.Control(), Hide As Boolean) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.Indeterminate() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.IsSpecialValue(Value As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.MissingProperty() -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.ObjectsAreEqual(Object1 As Object, Object2 As Object) -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.PropertyDescriptorSetValue(Descriptor As System.ComponentModel.PropertyDescriptor, Component As Object, Value As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.SetCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, Value As Object, ProjectCommonPropertiesObject As Object) -> Void (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyControlData.TryGetNonCommonPropertyValueNative(Descriptor As System.ComponentModel.PropertyDescriptor, Extenders As Object()) -> Object (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener.TryCreate(PropPage As Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase, EventSource As Object, DebugSourceName As String, ProjectHierarchy As Microsoft.VisualStudio.Shell.Interop.IVsHierarchy, ListenToInactiveConfigs As Boolean) -> Microsoft.VisualStudio.Editors.PropertyPages.PropertyListener (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsAcademic() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsEnterprise() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsExpress() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsProfessional() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsStandard() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsVB() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsVC() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.IsVSTO() -> Boolean (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.ProductSKU() -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.ProductSubSKU() -> Microsoft.VisualStudio.Editors.PropertyPages.VSProductSKU.VSASubSKUEdition (forwarded, contained in Microsoft.VisualStudio.AppDesigner)
Shared ReadOnly Microsoft.VisualStudio.Editors.PropertyPages.PropPageUserControlBase.PropPageBackColor -> System.Drawing.Color (forwarded, contained in Microsoft.VisualStudio.AppDesigner)Microsoft.VisualStudio.Editors.PropertyPages.CodeAnalysisPropPageComClass
Microsoft.VisualStudio.Editors.PropertyPages.CodeAnalysisPropPageComClass.New() -> Void
My.Resources.GeneralOptionPageResources
Shared My.Resources.GeneralOptionPageResources.Culture() -> System.Globalization.CultureInfo
Shared My.Resources.GeneralOptionPageResources.Culture(Value As System.Globalization.CultureInfo) -> Void
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck() -> String
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck_LogLevel() -> String
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck_LogLevel_Info() -> String
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck_LogLevel_Minimal() -> String
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck_LogLevel_None() -> String
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck_LogLevel_Verbose() -> String
Shared My.Resources.GeneralOptionPageResources.General_FastUpToDateCheck_Title() -> String
Shared My.Resources.GeneralOptionPageResources.ResourceManager() -> System.Resources.ResourceManagerThe colors from custom_vs_system3 were renamed as follows:


VSCOLOR_APPDESIGNER_BACKGROUND_LIGHT =  VSCOLOR_PROJECTDESIGNER_BACKGROUND_GRADIENTBEGIN
VSCOLOR_APPDESIGNER_BACKGROUND_DARK =  VSCOLOR_PROJECTDESIGNER_BACKGROUND_GRADIENTEND
VSCOLOR_APPDESIGNER_BORDER_OUTER = VSCOLOR_PROJECTDESIGNER_BORDER_OUTSIDE
VSCOLOR_APPDESIGNER_BORDER_INNER = VSCOLOR_PROJECTDESIGNER_BORDER_INSIDE
VSCOLOR_APPDESIGNER_TAB_BACKGROUND_START = VSCOLOR_PROJECTDESIGNER_TAB_BACKGROUND_GRADIENTBEGIN
VSCOLOR_APPDESIGNER_TAB_BACKGROUND_END = VSCOLOR_PROJECTDESIGNER_TAB_BACKGROUND_GRADIENTEND
VSCOLOR_APPDESIGNER_TAB_SEP_UPPER_START = VSCOLOR_PROJECTDESIGNER_TAB_SEP_TOP_GRADIENTBEGIN
VSCOLOR_APPDESIGNER_TAB_SEP_UPPER_END = VSCOLOR_PROJECTDESIGNER_TAB_SEP_TOP_GRADIENTEND
VSCOLOR_APPDESIGNER_TAB_SEP_LOWER_START = VSCOLOR_PROJECTDESIGNER_TAB_SEP_BOTTOM_GRADIENTBEGIN
VSCOLOR_APPDESIGNER_TAB_SEP_LOWER_END = VSCOLOR_PROJECTDESIGNER_TAB_SEP_BOTTOM_GRADIENTEND
VSCOLOR_APPDESIGNER_TAB_SELECTED_RIGHTBORDER = VSCOLOR_PROJECTDESIGNER_TAB_SELECTED_INSIDEBORDER
VSCOLOR_APPDESIGNER_TAB_SELECTED_OUTERBORDER = VSCOLOR_PROJECTDESIGNER_TAB_SELECTED_BORDER
VSCOLOR_APPDESIGNER_TAB_SELECTED_HIGHLIGHT1 = VSCOLOR_PROJECTDESIGNER_TAB_SELECTED_HIGHLIGHT1
VSCOLOR_APPDESIGNER_TAB_SELECTED_HIGHLIGHT2 = VSCOLOR_PROJECTDESIGNER_TAB_SELECTED_HIGHLIGHT2
VSCOLOR_APPDESIGNER_TAB_SELECTED_BACKGROUND = VSCOLOR_PROJECTDESIGNER_TAB_SELECTED_BACKGROUND
VSCOLOR_APPDESIGNER_INNERFRAME_BACKGROUND = VSCOLOR_PROJECTDESIGNER_CONTENTS_BACKGROUND

The original definitions of the custom colors relating to the project designer (see vswhidbey:312967):


VSCOLOR_APPDESIGNER_BACKGROUND_LIGHT
(all) System: Window

VSCOLOR_APPDESIGNER_BACKGROUND_DARK
(all) System: ControlLight

VSCOLOR_APPDESIGNER_BORDER_OUTER
Blue: 145,167,180
Olive: 166,161,166
Silver: 145,167,180
System: ControlDark

VSCOLOR_APPDESIGNER_BORDER_INNER
Blue: 131,151,162
Olive: 155,172,156
Silver: 131,151,162
System: ControlDark

VSCOLOR_APPDESIGNER_TAB_BACKGROUND_START
Blue: 255,255,255
Olive: 255,255,246
Silver: 255,255,255
System: Window

VSCOLOR_APPDESIGNER_TAB_BACKGROUND_END
Blue: 240,240,234
Olive: 242,236,219
Silver: 190,190,216
System: ControlLight

VSCOLOR_APPDESIGNER_TAB_SEP_UPPER_START
Blue: 255,255,255
Olive: 255,255,250
Silver: 255,255,255
System: Window

VSCOLOR_APPDESIGNER_TAB_SEP_UPPER_END
Blue: 248,248,245
Olive: 249,246,239
Silver: 230,230,237
System: Window

VSCOLOR_APPDESIGNER_TAB_SEP_LOWER_START
Blue: 239,238,232
Olive: 239,238,228
Silver: 217,217,225
System: InactiveBorder

VSCOLOR_APPDESIGNER_TAB_SEP_LOWER_END
Blue: 232,231,222
Olive: 233,229,216
Silver: 193,193,207
System: InactiveBorder

VSCOLOR_APPDESIGNER_TAB_SELECTED_RIGHTBORDER
Blue: 173,190,204
Olive: 207,211,194
Silver: 173,190,204
System: Control

VSCOLOR_APPDESIGNER_TAB_SELECTED_OUTERBORDER
Blue: 145,155,156
Olive: 145,155,156
Silver: 145,155,156
System: ControlDarkDark

VSCOLOR_APPDESIGNER_TAB_SELECTED_HIGHLIGHT1
Blue: 230,139,44
Olive: 207,114,37
Silver: 230,139,44
System: ControlDark

VSCOLOR_APPDESIGNER_TAB_SELECTED_HIGHLIGHT2
Blue: 255,199,60
Olive: 227,147,84
Silver: 255,199,60
System: Control

VSCOLOR_APPDESIGNER_TAB_SELECTED_BACKGROUND
(all) System: Window

VSCOLOR_APPDESIGNER_INNERFRAME_BACKGROUND
Blue: 248,246,240
Olive: 248,246,240
Silver: 243,243,244
System: ControlLight
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.Arguments = "Arguments" -> string
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.EnvironmentVariables = "EnvironmentVariables" -> string
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.Executable = "Executable" -> string
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.LaunchUrl = "LaunchUrl" -> string
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.WorkingDirectory = "WorkingDirectory" -> string
Microsoft.VisualStudio.ProjectSystem.Configuration.IConfigurationDimensionDescriptionMetadataView
Microsoft.VisualStudio.ProjectSystem.Configuration.IConfigurationDimensionDescriptionMetadataView.DimensionName.get -> string[]
Microsoft.VisualStudio.ProjectSystem.Configuration.IConfigurationDimensionDescriptionMetadataView.IsVariantDimension.get -> bool[]
Microsoft.VisualStudio.ProjectSystem.Debug.IActiveDebugFrameworkServices
Microsoft.VisualStudio.ProjectSystem.Debug.IActiveDebugFrameworkServices.GetActiveDebuggingFrameworkPropertyAsync() -> System.Threading.Tasks.Task<string>
Microsoft.VisualStudio.ProjectSystem.Debug.IActiveDebugFrameworkServices.GetConfiguredProjectForActiveFrameworkAsync() -> System.Threading.Tasks.Task<Microsoft.VisualStudio.ProjectSystem.ConfiguredProject>
Microsoft.VisualStudio.ProjectSystem.Debug.IActiveDebugFrameworkServices.GetProjectFrameworksAsync() -> System.Threading.Tasks.Task<System.Collections.Generic.List<string>>
Microsoft.VisualStudio.ProjectSystem.Debug.IActiveDebugFrameworkServices.SetActiveDebuggingFrameworkPropertyAsync(string activeFramework) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.IDebugTokenReplacer
Microsoft.VisualStudio.ProjectSystem.Debug.IDebugTokenReplacer.ReplaceTokensInProfileAsync(Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile) -> System.Threading.Tasks.Task<Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile>
Microsoft.VisualStudio.ProjectSystem.Debug.IDebugTokenReplacer.ReplaceTokensInStringAsync(string rawString, bool expandEnvironmentVars) -> System.Threading.Tasks.Task<string>
Microsoft.VisualStudio.ProjectSystem.Debug.IJsonSection
Microsoft.VisualStudio.ProjectSystem.Debug.IJsonSection.JsonSection.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IJsonSection.SerializationType.get -> System.Type
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.CommandLineArgs.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.CommandName.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.EnvironmentVariables.get -> System.Collections.Immutable.ImmutableDictionary<string, string>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.ExecutablePath.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.LaunchBrowser.get -> bool
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.LaunchUrl.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.Name.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.OtherSettings.get -> System.Collections.Immutable.ImmutableDictionary<string, object>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile.WorkingDirectory.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings.ActiveProfile.get -> Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings.GetGlobalSetting(string settingsName) -> object
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings.GlobalSettings.get -> System.Collections.Immutable.ImmutableDictionary<string, object>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings.Profiles.get -> System.Collections.Immutable.ImmutableList<Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.ActiveProfile.get -> Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.AddOrUpdateGlobalSettingAsync(string settingName, object settingContent) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.AddOrUpdateProfileAsync(Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile, bool addToFront) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.CurrentSnapshot.get -> Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.LaunchSettingsFile.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.RemoveGlobalSettingAsync(string settingName) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.RemoveProfileAsync(string profileName) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.SetActiveProfileAsync(string profileName) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.SourceBlock.get -> System.Threading.Tasks.Dataflow.IReceivableSourceBlock<Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.UpdateAndSaveSettingsAsync(Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings profiles) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider.WaitForFirstSnapshot(int timeout) -> System.Threading.Tasks.Task<Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider2
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsProvider2.GetLaunchSettingsFilePathAsync() -> System.Threading.Tasks.Task<string>
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsSerializationProvider
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsUIProvider
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsUIProvider.CommandName.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsUIProvider.CustomUI.get -> System.Windows.Controls.UserControl
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsUIProvider.FriendlyName.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsUIProvider.ProfileSelected(Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings curSettings) -> void
Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettingsUIProvider.ShouldEnableProperty(string propertyName) -> bool
Microsoft.VisualStudio.ProjectSystem.Debug.IPersistOption
Microsoft.VisualStudio.ProjectSystem.Debug.IPersistOption.DoNotPersist.get -> bool
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.CommandLineArgs.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.CommandLineArgs.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.CommandName.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.CommandName.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.EnvironmentVariables.get -> System.Collections.Generic.Dictionary<string, string>
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.ExecutablePath.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.ExecutablePath.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.LaunchBrowser.get -> bool
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.LaunchBrowser.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.LaunchUrl.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.LaunchUrl.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.Name.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.Name.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.OtherSettings.get -> System.Collections.Generic.Dictionary<string, object>
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.ToLaunchProfile() -> Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.WorkingDirectory.get -> string
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile.WorkingDirectory.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings.ActiveProfile.get -> Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings.ActiveProfile.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings.GlobalSettings.get -> System.Collections.Generic.Dictionary<string, object>
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings.Profiles.get -> System.Collections.Generic.List<Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchProfile>
Microsoft.VisualStudio.ProjectSystem.Debug.IWritableLaunchSettings.ToLaunchSettings() -> Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchSettings
Microsoft.VisualStudio.ProjectSystem.Debug.IWritablePersistOption
Microsoft.VisualStudio.ProjectSystem.Debug.IWritablePersistOption.DoNotPersist.get -> bool
Microsoft.VisualStudio.ProjectSystem.Debug.IWritablePersistOption.DoNotPersist.set -> void
Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName
Microsoft.VisualStudio.ProjectSystem.Properties.IInterceptingPropertyValueProviderMetadata
Microsoft.VisualStudio.ProjectSystem.Properties.IInterceptingPropertyValueProviderMetadata.PropertyName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Extensibility.IProjectExportProvider
Microsoft.VisualStudio.ProjectSystem.VS.Extensibility.IProjectExportProvider.GetExport<T>(string projectFilePath) -> T
Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs.Changes.get -> Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependenciesChanges
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs.DependenciesChangedEventArgs(Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider provider, string targetShortOrFullName, Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependenciesChanges changes, Microsoft.VisualStudio.ProjectSystem.Properties.IProjectCatalogSnapshot catalogs, System.Collections.Immutable.IImmutableDictionary<Microsoft.VisualStudio.ProjectSystem.NamedIdentity, System.IComparable> dataSourceVersions) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs.DependenciesChangedEventArgs(Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider provider, string targetShortOrFullName, Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependenciesChanges changes, System.Threading.CancellationToken token) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs.Provider.get -> Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs.TargetShortOrFullName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs.Token.get -> System.Threading.CancellationToken
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependenciesChanges
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependenciesChanges.AddedNodes.get -> System.Collections.Immutable.IImmutableList<Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel>
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependenciesChanges.RemovedNodes.get -> System.Collections.Immutable.IImmutableList<Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel>
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Caption.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.DependencyIDs.get -> System.Collections.Immutable.IImmutableList<string>
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.ExpandedIcon.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Flags.get -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Icon.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Id.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Implicit.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Name.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.OriginalItemSpec.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Path.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Priority.get -> int
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Properties.get -> System.Collections.Immutable.IImmutableDictionary<string, string>
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.ProviderType.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Resolved.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.SchemaItemType.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.SchemaName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.TopLevel.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.UnresolvedExpandedIcon.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.UnresolvedIcon.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Version.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel.Visible.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider.CreateRootDependencyNode() -> Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IDependencyModel
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider.DependenciesChanged -> System.EventHandler<Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependenciesChangedEventArgs>
Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.IProjectDependenciesSubTreeProvider.ProviderType.get -> string
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.NativeDebugging = "NativeDebugging" -> string
const Microsoft.VisualStudio.ProjectSystem.Debug.UIProfilePropertyName.SqlDebugging = "SQLDebugging" -> string
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ApplicationPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ApplicationWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.CodeInformationPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.CodeInformationWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.Component.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ComponentPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ComponentWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ErrorSmall.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.Framework.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.FrameworkPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.FrameworkWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.LibraryWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.NuGetGrey.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.NuGetGreyPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.NuGetGreyWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ProjectImports.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ReferenceGroup.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ReferenceGroupWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.ReferencePrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.Sdk.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.SdkPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.SdkWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.SharedProject.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.SharedProjectPrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.SharedProjectWarning.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.TargetFile.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.TargetFilePrivate.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static Microsoft.VisualStudio.ProjectSystem.VS.ManagedImageMonikers.WarningSmall.get -> Microsoft.VisualStudio.Imaging.Interop.ImageMoniker
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.BaseReferenceFlags -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.DependencyFlags -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.ResolvedDependencyFlags -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.ShowEmptyProviderRootNode -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.SupportsHierarchy -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.SupportsRemove -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Tree.Dependencies.DependencyTreeFlags.UnresolvedDependencyFlags -> Microsoft.VisualStudio.ProjectSystem.ProjectTreeFlags// Copyright (c) Microsoft.  All Rights Reserved.  Licensed under the Apache License, Version 2.0.  See License.txt in the project root for license information.

using System.ComponentModel.Composition;

namespace Microsoft.VisualStudio.ProjectSystem.SpecialFileProviders
{
    /// <summary>
    ///     Provides a <see cref="ISpecialFileProvider"/> that handles the 'licenses.licx' file; 
    ///     a file that contains a list of licensed (typically Windows Forms) components used by
    ///     a project and is typically found under the 'AppDesigner' folder.
    /// </summary>
    [ExportSpecialFileProvider(SpecialFiles.Licenses)]
    [AppliesTo(ProjectCapability.DotNet)]
    internal class LicensesSpecialFileProvider : AbstractFindByNameUnderAppDesignerSpecialFileProvider
    {
        [ImportingConstructor]
        public LicensesSpecialFileProvider(ISpecialFilesManager specialFilesManager, IPhysicalProjectTree projectTree)
            : base("licenses.licx", specialFilesManager, projectTree)
        {
        }
    }
}
const Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.ProfileCommandNames.Executable = "Executable" -> string
const Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.ProfileCommandNames.IISExpress = "IISExpress" -> string
const Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.ProfileCommandNames.NoAction = "NoAction" -> string
const Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.ProfileCommandNames.Project = "Project" -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.__id.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.__project.get -> object
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AbsoluteProjectDirectory.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ActiveConfigurationSettings.get -> VSLangProj.ProjectConfigurationProperties
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ActiveFileSharePath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ActiveWebAccessMethod.get -> VSLangProj.prjWebAccessMethod
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AddWebReference(string bstrUrl) -> EnvDTE.ProjectItem
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ApplicationIcon.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ApplicationIcon.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyKeyContainerName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyKeyContainerName.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyName.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyOriginatorKeyFile.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyOriginatorKeyFile.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyOriginatorKeyMode.get -> VSLangProj.prjOriginatorKeyMode
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AssemblyOriginatorKeyMode.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AutoGenerateBindingRedirects.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.AutoGenerateBindingRedirects.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.BuildManager.get -> VSLangProj.BuildManager
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.CopyProject(string bstrDestFolder, string bstrDestUNCPath, VSLangProj.prjCopyProjectOption copyProjectOption, string bstrUsername, string bstrPassword) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.CreateWebReferencesFolder() -> EnvDTE.ProjectItem
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultClientScript.get -> VSLangProj.prjScriptLanguage
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultClientScript.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultHTMLPageLayout.get -> VSLangProj.prjHTMLPageLayout
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultHTMLPageLayout.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultNamespace.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultNamespace.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultTargetSchema.get -> VSLangProj.prjTargetSchema
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DefaultTargetSchema.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DelaySign.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DelaySign.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.DTE.get -> EnvDTE.DTE
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.EnumConnectionPoints(out Microsoft.VisualStudio.OLE.Interop.IEnumConnectionPoints ppEnum) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.Events.get -> VSLangProj.VSProjectEvents
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.Exec(VSLangProj.prjExecCommand command, int bSuppressUI, object varIn, out object pVarOut) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ExtenderCATID.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ExtenderNames.get -> object
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.FileName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.FileName.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.FileSharePath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.FileSharePath.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.FindConnectionPoint(ref System.Guid riid, out Microsoft.VisualStudio.OLE.Interop.IConnectionPoint ppCP) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.FullPath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.GenerateKeyPairFiles(string strPublicPrivateFile, string strPublicOnlyFile = "0") -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.get_Extender(string ExtenderName) -> object
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.GetUniqueFilename(object pDispatch, string bstrRoot, string bstrDesiredExt) -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.Imports.get -> VSLangProj.Imports
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.LinkRepair.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.LinkRepair.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.LocalPath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OfflineURL.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OnSinkAdded(Microsoft.VisualStudio.OLE.Interop.IPropertyNotifySink sink) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OnSinkRemoved(Microsoft.VisualStudio.OLE.Interop.IPropertyNotifySink sink) -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OptionCompare.get -> VSLangProj.prjCompare
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OptionCompare.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OptionExplicit.get -> VSLangProj.prjOptionExplicit
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OptionExplicit.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OptionStrict.get -> VSLangProj.prjOptionStrict
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OptionStrict.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OutputFileName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OutputType.get -> VSLangProj.prjOutputType
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OutputType.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OutputTypeEx.get -> VSLangProj110.prjOutputTypeEx
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.OutputTypeEx.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.Project.get -> EnvDTE.Project
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ProjectType.get -> VSLangProj.prjProjectType
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ReferencePath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ReferencePath.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.References.get -> VSLangProj.References
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.Refresh() -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.RootNamespace.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.RootNamespace.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.ServerExtensionsVersion.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.StartupObject.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.StartupObject.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.TemplatePath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.URL.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WebAccessMethod.get -> VSLangProj.prjWebAccessMethod
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WebAccessMethod.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WebReferencesFolder.get -> EnvDTE.ProjectItem
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WebServer.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WebServerVersion.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WorkOffline.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Automation.VSProject.WorkOffline.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.ConnectionPoint.ConnectionPointContainer
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider.OnAfterLaunchAsync(Microsoft.VisualStudio.ProjectSystem.Debug.DebugLaunchOptions launchOptions, Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider.OnBeforeLaunchAsync(Microsoft.VisualStudio.ProjectSystem.Debug.DebugLaunchOptions launchOptions, Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile) -> System.Threading.Tasks.Task
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider.QueryDebugTargetsAsync(Microsoft.VisualStudio.ProjectSystem.Debug.DebugLaunchOptions launchOptions, Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile) -> System.Threading.Tasks.Task<System.Collections.Generic.IReadOnlyList<Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugLaunchSettings>>
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider.SupportsProfile(Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile) -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider2
Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugProfileLaunchTargetsProvider2.QueryDebugTargetsForDebugLaunchAsync(Microsoft.VisualStudio.ProjectSystem.Debug.DebugLaunchOptions launchOptions, Microsoft.VisualStudio.ProjectSystem.Debug.ILaunchProfile profile) -> System.Threading.Tasks.Task<System.Collections.Generic.IReadOnlyList<Microsoft.VisualStudio.ProjectSystem.VS.Debug.IDebugLaunchSettings>>
Microsoft.VisualStudio.ProjectSystem.VS.LanguageServices.IVsContainedLanguageComponentsFactory
Microsoft.VisualStudio.ProjectSystem.VS.LanguageServices.IVsContainedLanguageComponentsFactory.GetContainedLanguageFactoryForFile(string filePath, out Microsoft.VisualStudio.Shell.Interop.IVsHierarchy hierarchy, out uint itemid, out Microsoft.VisualStudio.TextManager.Interop.IVsContainedLanguageFactory containedLanguageFactory) -> int
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.__id.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.AllowUnsafeBlocks.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.AllowUnsafeBlocks.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.BaseAddress.get -> uint
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.BaseAddress.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CheckForOverflowUnderflow.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CheckForOverflowUnderflow.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisCulture.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisCulture.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisDictionaries.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisDictionaries.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisFailOnMissingRules.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisFailOnMissingRules.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisIgnoreBuiltInRules.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisIgnoreBuiltInRules.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisIgnoreBuiltInRuleSets.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisIgnoreBuiltInRuleSets.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisIgnoreGeneratedCode.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisIgnoreGeneratedCode.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisInputAssembly.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisInputAssembly.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisLogFile.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisLogFile.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisModuleSuppressionsFile.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisModuleSuppressionsFile.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisOverrideRuleVisibilities.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisOverrideRuleVisibilities.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleAssemblies.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleAssemblies.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleDirectories.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleDirectories.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRules.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRules.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleSet.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleSet.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleSetDirectories.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisRuleSetDirectories.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisSpellCheckLanguages.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisSpellCheckLanguages.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisUseTypeNameInSuppression.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.CodeAnalysisUseTypeNameInSuppression.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.ConfigurationOverrideFile.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.ConfigurationOverrideFile.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DebugInfo.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DebugInfo.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DebugSymbols.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DebugSymbols.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DefineConstants.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DefineConstants.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DefineDebug.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DefineDebug.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DefineTrace.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DefineTrace.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DocumentationFile.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.DocumentationFile.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableASPDebugging.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableASPDebugging.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableASPXDebugging.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableASPXDebugging.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableSQLServerDebugging.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableSQLServerDebugging.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableUnmanagedDebugging.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.EnableUnmanagedDebugging.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.ExtenderCATID.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.ExtenderNames.get -> object
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.FileAlignment.get -> uint
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.FileAlignment.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.GenerateSerializationAssemblies.get -> VSLangProj80.sgenGenerationOption
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.GenerateSerializationAssemblies.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.get_Extender(string arg) -> object
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.IncrementalBuild.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.IncrementalBuild.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.IntermediatePath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.IntermediatePath.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.LanguageVersion.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.LanguageVersion.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.NoStdLib.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.NoStdLib.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.NoWarn.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.NoWarn.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.Optimize.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.Optimize.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.OutputPath.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.OutputPath.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.PlatformTarget.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.PlatformTarget.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.Prefer32Bit.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.Prefer32Bit.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RegisterForComInterop.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RegisterForComInterop.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RemoteDebugEnabled.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RemoteDebugEnabled.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RemoteDebugMachine.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RemoteDebugMachine.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RemoveIntegerChecks.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RemoveIntegerChecks.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RunCodeAnalysis.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.RunCodeAnalysis.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartAction.get -> VSLangProj.prjStartAction
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartAction.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartArguments.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartArguments.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartPage.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartPage.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartProgram.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartProgram.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartURL.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartURL.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartWithIE.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartWithIE.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartWorkingDirectory.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.StartWorkingDirectory.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.TreatSpecificWarningsAsErrors.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.TreatSpecificWarningsAsErrors.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.TreatWarningsAsErrors.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.TreatWarningsAsErrors.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.UseVSHostingProcess.get -> bool
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.UseVSHostingProcess.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.WarningLevel.get -> VSLangProj.prjWarningLevel
Microsoft.VisualStudio.ProjectSystem.VS.Properties.AbstractProjectConfigurationProperties.WarningLevel.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.GetProfileNameDialog
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.GetProfileNameDialog.GetProfileNameDialog(Microsoft.VisualStudio.Shell.SVsServiceProvider sp, Microsoft.VisualStudio.ProjectSystem.IProjectThreadingService threadingService, string suggestedName, System.Predicate<string> validator) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.GetProfileNameDialog.InitializeComponent() -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.GetProfileNameDialog.ProfileName.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.GetProfileNameDialog.ProfileName.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.ProfileCommandNames
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.Activate(System.IntPtr hWndParent, Microsoft.VisualStudio.OLE.Interop.RECT[] pRect, int bModal) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.Apply() -> int
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.ContextObjects.get -> System.Collections.Generic.List<Microsoft.VisualStudio.ProjectSystem.Properties.IVsBrowseObjectContext>
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.Deactivate() -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.GetPageInfo(Microsoft.VisualStudio.OLE.Interop.PROPPAGEINFO[] pPageInfo) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.Help(string pszHelpDir) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.IsPageDirty() -> int
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.Move(Microsoft.VisualStudio.OLE.Interop.RECT[] pRect) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.OnModeChange(Microsoft.VisualStudio.Shell.Interop.DBGMODE dbgmodeNew) -> int
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.SetObjects(uint cObjects, object[] ppunk) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.SetPageSite(Microsoft.VisualStudio.OLE.Interop.IPropertyPageSite pPageSite) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.Show(uint nCmdShow) -> void
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPage.TranslateAccelerator(Microsoft.VisualStudio.OLE.Interop.MSG[] pMsg) -> int
Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources
Microsoft.VisualStudio.ProjectSystem.VS.Utilities.FocusAttacher
Microsoft.VisualStudio.ProjectSystem.VS.Utilities.FocusAttacher.FocusAttacher() -> void
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.GetProfileNameDialog.DialogCaption.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.AddBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.AllFiles.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ApplicationArguments.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ApplicationArgumentsWatermark.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.BrowseBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.CancelBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.Culture.get -> System.Globalization.CultureInfo
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.Culture.set -> void
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.DebugPropertyPageTitle.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.DeleteBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.DuplicateKey.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.EnvironmentVariables.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.EnvVariableNameWatermark.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.EnvVariableValueWatermark.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ErrorsMustBeCorrectedPriorToSaving.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.Executable.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ExecutableFiles.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ExecutablePathWatermark.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.Launch.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.LaunchURL.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.LaunchUrlWatermark.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.NameCannotBeEmpty.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.NameHeader.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.NewBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.NewProfileCaption.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.NewProfileSeedName.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.OKBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.Profile.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileKindExecutableName.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileKindIISExpressName.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileKindNoActionName.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileKindProjectName.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileName.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileNameInvalid.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ProfileNameRequired.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.RemoveBtn.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ResourceManager.get -> System.Resources.ResourceManager
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ValueCannotBeEmpty.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.ValueHeader.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.WorkingDirectory.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.WorkingDirectoryWatermark.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.Utilities.FocusAttacher.GetFocus(System.Windows.DependencyObject d) -> bool
static Microsoft.VisualStudio.ProjectSystem.VS.Utilities.FocusAttacher.SetFocus(System.Windows.DependencyObject d, bool value) -> void
static readonly Microsoft.VisualStudio.ProjectSystem.VS.Utilities.FocusAttacher.FocusProperty -> System.Windows.DependencyProperty
XamlGeneratedNamespace.GeneratedInternalTypeHelper
XamlGeneratedNamespace.GeneratedInternalTypeHelper.GeneratedInternalTypeHelper() -> voidMicrosoft.VisualStudio.ProjectSystem.VS.Properties.CSharp.CSharpProjectConfigurationProperties
Microsoft.VisualStudio.ProjectSystem.VS.Properties.CSharp.CSharpProjectConfigurationProperties.ErrorReport.get -> string
Microsoft.VisualStudio.ProjectSystem.VS.Properties.CSharp.CSharpProjectConfigurationProperties.ErrorReport.set -> void
Microsoft.VisualStudio.ProjectSystem.VS.Properties.VisualBasic.VisualBasicProjectConfigurationProperties
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.CancelBtnHelpText.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.DeleteBtnHelpText.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.NewBtnHelpText.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.OKBtnHelpText.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.chkLaunchBrowserHelpText.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.chkNativeCodeDebuggingText.get -> string
static Microsoft.VisualStudio.ProjectSystem.VS.PropertyPages.PropertyPageResources.chkSqlCodeDebuggingText.get -> stringTo avoid tests copying the same binaries to the common build directory and causing races, this
project is used to copy and deploy all the required product, xUnit and Moq binaries required
to run all the project system tests.

When adding new dependencies, reference them from this project.// Copyright (c) Microsoft.  All Rights Reserved.  Licensed under the Apache License, Version 2.0.  See License.txt in the project root for license information.

namespace Microsoft.VisualStudio.ProjectSystem.SpecialFileProviders
{
    public class LicensesSpecialFileProviderTests : AbstractFindByNameUnderAppDesignerSpecialFileProviderTestBase
    {
        public LicensesSpecialFileProviderTests()
            : base("licenses.licx")
        {
        }

        internal override AbstractFindByNameUnderAppDesignerSpecialFileProvider CreateInstance(ISpecialFilesManager specialFilesManager, IPhysicalProjectTree projectTree)
        {
            return new LicensesSpecialFileProvider(specialFilesManager, projectTree);
        }
    }
}
