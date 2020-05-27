## FlubuCore 4.3.7.0
- DotnetBuildTask, DotnetPackTask, DotnetPublishTask: VersionSuffix option key is not added anymore if it is null or empty.
- Changed properties accessors on DefaultBuildScript so they can not be overriden through passed arguments.
- Interactive mode: Fixed load and reload of build script.
- Interactive mode: Fixed load and reload of build script when build script location is specified by user (-s)
- Interactive mode: Fixed hint highlights for script properties.
- Interactive mode: Fixed suggestions for properties with more than one key.
- Interactive mode: Help now shows build script global arguments.
- Interactive mode: Added logging when build script is not found. 
- Added some more default build script locations.
- Added some more default csproj locations.
- Flubu help: Adds colon betwen target name and target description even if description is empty.

## FlubuCore 4.3.5.0
- BuildVersionWithQuality adds back the dash separator if necessary
- BuildVersionWithQuality version field count is now optional
- Added Implicit string operator for FileFullPath

## FlubuCore 4.3.4.0
- UpdateNetCoreVersionTask: Version field count is now configurable
- UpdateNetCoreVersionTask: Option to add PackageVersion to csproj.
- UpdateNetCoreVersionTask: Fixes set of version suffix when setting version to more than one csproj.

## FlubuCore 4.3.3.0
- Fixes SetBuildVersionWithSuffix which also caused bug in UpdateNetCoreVersionTask
- Fixes spacing when displaying target dependencies in help
- Interactive mode: Fixes suggestions when suggestion key is null

## FlubuCore 4.3.1.0
- Added GetFiles with globing option to task context
- Added GetDirectory with globing option to task context
- Target: Added Requires method which checks if specified parameter is null. If it is null target execution fails before any tasks are executed.
- Option to run flubu script from other than root dir (only when .flubu file is found)
. Get project root directory from task context and DefaultBuildScript
- Get Output directory from task context and DefaultBuildScript
- Flubu setup: option to enter script csproj location even if build script location is found.
- GetVsSolution: Easier access to various project information
- GetVsSolution: Filter projects by name with glob pattern
- AppVeyor: Added branch name.
- AppVeyor: Added IsTag 
- AppVeyor: Added TagName
- Fixed include directory attribute to load only cs files
- Overidable argument now checks if same short/long key was already added and overrides appropriate one.
- Added GetFiles To FullPath class. 
- Target help now shows target dependencies in brackets
- Target help now shows default target with orange color
- Global script arguments of enum type have all available values listed in help now
- Added some more default build script locations.
- Interactive Mode: Suggetions for parameter values of enum type
- Interactive mode: Allows multiple tab key presses on sugestions(goes to next suggestion)
- Interactive mode: When listing files file length is now formated.
- Interactive mode: when pressing space sugestion is now hidden. 
## FlubuCore 4.2.8.0
- FlubCore global tool for .net core 3.0
## FlubuCore 4.2.7.0
- FromArg attribute now supports multiple keys. Keys must be seperated with |
- DotnetCoreTasks: Fixed dotnet executable path for OSX
- LoadSolutionTask: Fixed path to solution and project files in linux and mac
- Interactive mode: Fixed crash after clear screen (cls)
- Interactive mode: Fixed crash when external process is not found when executing target
- Interactive mode: Fixed delete character in console
- Interactive mode: Fixed space when not typing at the end
- Interactive mode: Improved error handling when target fails. 
 

 
## FlubuCore 4.2.4.0

- Added dotnet msbuild task with tab completion in interactive mode.
- Added new docker tasks and updates existing ones by regenerating them from documentation
- Added git branch task
- Added git merge task
- Added git extension on ITaskContext which contains local repository information. For example: ` context.Git().CurrentBranchName()`
- Added GitHubActions build system
- Added Azure pipelines build system
- Added some more jenkins helpes in coresponding build system
- Added some more travis helpers in coresponding build system
- Updated options on existing git tasks 
- Added missing dotnet nuget push options
- Added missing dotnet publish options
- Added missing options to dotnet test
- PackageTask: AddDirectory now support directory filtering when subdirectories are packaged
- PackageTask: Added support for filtering by glob pattern
- FromArg attribute now supports enums
- Moved Chocolatey tasks from FlubuCore plugin to FlubuCore (possible braking change) - Just remove plugin if you are using it.
- Interactive mode: tab completion for all docker commands and options
- Interactive mode: Directory completion with tab key on cd command
- Interactive mode: Added cls internal command for clearing the screen
- Interactive mode: Improved tab completion for external processes
- Interactive mode: hints are now case insensitive
- Interactive mode: Different colors for different types of suggestions
- Interactive mode: removed duplicated shor and long options sugestions 
- Interactive mode: move to path root with 'cd...'
- Interactive mode: fixed bug where flubu in interactive mode crashed when clearing old help
- Interactive mode: Fixed target detailed help
- Interactive mode: Removes new lines and unecessary whitespaces from help at the bottom.
- Interactive mode: Task execution errors are now logged.
- Interactive mode: Fixes cd.. so it doesn't go to the root directory on disk.
- docker tasks: optional options are now as optional parameters.
- External process task do not log RunProgramTask execution info anymore.
- Flubu cli tool and global tool works now with only .net core 3.0 installed on machine.  
- Fixed various bugs in chocolatey task. 
- Fixed docker options key prefix.
- Fixed package task when no files exists to zip
- Fixed a bug where interactive mode hang on illegal command.
- minor logging fixes
- fixed null or empty parameters in WithArguments 
- External process tasks: Improved value required error message when passing argument with value.
- Internal: changable key value separator in WithArgumentKeyFromAttribute method
- Internal: Implemented FlubuConsole task generator
- Internal: Various task generator improvements


## FlubuCore 4.1.2.0
- Interactive mode: Option to execute external processes such as dotnet, git, docker... 
 
- Options completion in interactive mode for tasks that run's external process

currently tab completion is available for all dotnet commands, most of git commands, coverlet, sqlcmd, gitversion.
It is planned that all docker, azure, npm, octopus commands will support tab completion in near feature.
![FlubuCore interactive mode](https://raw.githubusercontent.com/dotnetcore/flubu.core/master/assets/FlubuCore_Interactive_mode_external_process.gif)


- Interactive mode: help for targets and options

![FlubuCore interactive mode](https://raw.githubusercontent.com/dotnetcore/flubu.core/master/assets/FlubuCore_Interactive_mode.gif)

- interactive mode: reload or load another script

You can load new script with following commands in interactive mode:
`load -s=newscript.cs`
`l -s=newscript cs`

You can reload script with the following command:
`reload`
`r`

- Override existing options or add additional options to tasks through console improvements

Let's say you have target (this is just simple dummy example)
```c#
context.CreateTarget("Example")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 
    .AddCoreTask)x => x.Pack("ExampleProject");
You could just write in console
```

`flubu build -c=Debug`

flubu would execute

`dotnet build MySolution.sln -c Debug`

- interactive mode: navigation between folders 
- fixed terminal entered command. Flubu executed sugestion instead of actually entered command 
- FetchBuildVersionFromFile: Fixed default locations output
- Fixed additional options prefixes
## FlubuCore 4.0.3.0
- FlubuCore interactive mode which offers target tab completition, options tab completition, toogle targets and options, executed commands history and more.   

![FlubuCore interactive mode](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCore_Interactive_mode.gif)

- Targets: Execute another target within target with AddTarget.

``` C#
    protected override void ConfigureTargets(ITaskContext context)
    {
       var exampleB = context.CreateTarget("TargetB")
            .Do(Something);

       context.CreateTarget("TargetA")
           .AddCoreTask(x => x.Build())
           .AddTarget(exampleB)  //Target is executed in the order it was added
           .Do(JustAnExample);
    }

    public void JustAnExample(ITaskContext context)
    {
        ...
    }
```
- Target: Add tasks to target with a foreach loop.
```c#
  protected override void ConfigureTargets(ITaskContext context)
  {
         var solution = context.Properties.Get<VSSolution>(BuildProps.Solution);

         context.CreateTarget("Pack")
                .ForEach(solution.Projects, (item, target) =>
                {
                    target.AddCoreTask(x => x.Pack().Project(item.ProjectName))
                          .Do(JustAnExample, item);
                });
  }

  private void JustAnExample(ITaskContext context, VSProjectInfo vsProjectInfo)
  {
        //// Do something.
  }
```

- Override existing options or add additional options to tasks through console

<sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Let's say you have target</sup>
```c#
context.CreateTarget("Build")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 
```

<sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and you wan't to build solution in debug configuration.</sup>

<sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You could just write in console</sup>

`flubu build /o:configuration=Debug`

<sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or</sup>

`flubu build /o:c=Debug`

<sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flubu would execute </sup>

`dotnet build MySolution.sln -c Debug`
- sequentiall logging in asynchronus executed tasks and targets.

```c#
context.CreateTarget("Test")
        .SetAsDefault()
        .SequentialLogging(true)
        .AddCoreTaskAsync(x => x.Pack())
        .AddCoreTaskAsync(x => x.Pack())
        .DependsOnAsync(test2, test3);
```

- New plugins are available: Chocolatey, Gitter and Slack plugin.
- Added Get solution infromation as task context extension
- Added support for multiple Musts on target
- Logs have now indentation for better readability.
- Logs have now timemark (actions that takes more than 2sec).
- Improved build summary in logs.
- Loged build finish time and build duration
- Fixed GitVersionTask
- Targets: Must now accepts optional error message parameter.
- UpdateNetCoreTask can now write version quality(version suffix)
- FetchBuildVersionFromFile can now fetch version quality(version suffix).
- FetchBuildVersionFromFile improved logging.
- Added options to set versions in dotnet tasks (dotnet build, dotnet pack, dotnet publish)
- LoadSoluationTask returns solution information
- Added WithArgument to IRunProgramTask interface
- Fixed check of unknown targets.

## FlubuCore 3.2.1.0
- Fixed build status
- Improved message when build script is not found.

## FlubuCore 3.2.0.0
- Added coverlet task ```.AddCoreTask(x => x.CoverletTask("assembly.dll")```
- Adds flubu setup where you can set location of the build script and project file. run ```flubu setup```
- Added When condition to all tasks.
```c#
 var compile = context
            .CreateTarget("compile")
            .SetDescription("Compiles the VS solution")
            .AddCoreTask(x => x.Build().Configuration("Release").When(
            () =>
            {
                return context.BuildSystems().IsLocalBuild;

            }, task => { task.Configuration("Debug"); }));
 ```
- Fixed bug where nuget and assemlby references were not loaded if csproj didnt have both of them
- Adds OnBuildFailed event.
```c#
public class BuildScript : DefaultBuildScript
{
    protected override void OnBuildFailed(ITaskSession session, Exception ex)
    {
    } 
}
 ```
- Adds before and after target execution events.
```c#
    protected override void BeforeTargetExecution(ITaskContext context)
    {
    }

    protected override void AfterTargetExecution(ITaskContext context)
    {
    }
```    
- Adds before and after build execution events.
```c#
    protected override void BeforeBuildExecution(ITaskContext context)
    {
    }

    protected override void AfterBuildExecution(ITaskSession session)
    {
    }
 ```
- Improved nunit tasks fluent intefaces.
- Added skipped target dependencies and tasks logging.
- Publicly exposed task name.
- fixed one of the default build script csproj locations.

## FlubuCore 3.1.2.0
- Fixes Must on target fluent interface.
- Fixes script when using partial classes. Script failed in some scenarios.
- script allows includes of other cs files in partial classes.
- System.Drawing.Primitives assembly reference doesn't need to be referenced exlicitly anymore in script uses collored logging (issue was only present when target .net core framework)
- Improved some script error messages.

## FlubuCore 3.1.1.0
- Fixes loading of nuget packages that don't have target framework specified.
- FetchBuildVersionFromFileTask: Improves fetching of version from file by allowing version to be in any line not just first.
- FetchBuildVersionFromFileTask: Adds default project version file locations.
- FetchBuildVersionFromFileTask: Adds option to remove prefix from version.
- FetchBuildVersionFromFileTask: Adds option to allow any suffix. 
- Improves error messages when cs files that are used in script are not included.
- Improves error messages when script assembly references are not loaded.
- Added Null and empty target name validation.

## FlubuCore 3.1.0.0
- Added IncludeFromDirectoryAttribute: Attribute adds all .cs files from specified directory. With second optional parameter you can include subdirectories. 

```c#
[IncludeFromDirectory(@".\Helpers")]
public class BuildScript : DefaultBuildScript
{
}
 ```
- AssemblyFromDirectoryAttribute: When added on script class FlubuCore should add all assemblies from specified directory to script.

```c#
    [AssemblyFromDirectory(@".\Lib")]
    public class BuildScript : DefaultBuildScript
    {
    }
```
- Load base script class automatically. Must be in same directory as script.
- Improved collored console logging by wrapping strings of the output in ANSI codes that instruct the terminal to color the string based on the interpreted code.
- Allow namespaces in included cs files. Executing script does not fail anymore if included cs file contain namespace.
- Disable collored logging with attribute or script argument. 

## FlubuCore 3.0.2.0
- Fixed attribute "directives"

## FlubuCore 3.0.1.0
- Fixes restoring and loading of nuget packages with old csproj
- Stylecop nuget packages are not loaded anymore
- build status is now logged with color.
- Target and task information is now logged with color.

## FlubuCore 3.0.0.0
- Resolve nuget packages from build script csproj file automatically. No need for directives in build scripts anymore when executing script that is in project. For standalone scripts you still need directives.
- Load referenced libraries from build csproj file automatically. No need for directives in build scripts anymore when executing script that is in project. For standalone scripts you still need directives.
- All nuget dependencies are loaded automatically.
- Added GitVersionTask: GitVersion is a tool to help you achieve Semantic Versioning on your project. [Documentation](https://gitversion.readthedocs.io/en/latest/)

```C#
  context.CreateTarget("Example")
         .AddTask(x => x.GitVersionTask());
```
- Automatic load of build script partial classes. Partial classes have to be in same directory as build script.
- Automatic update of FlubuCore web api to new version. Just navigate to /UpdateCenter
- Added small web app to FlubuCore web api for executing scripts. Navigate to /Script
- Pass console and config arguments to targets defined with attribute
```C#
 [Target("ExampleTarget", "Default string")]     
 [Target("ExampleTarget2", "Default2 string")]
 public void Example(ITarget target, [FromArg("e")]string Example)
 {
     target.Do(x => { x.LogInfo(boo });
 }
```

`dotnet flubu ExampleTarget -e=Hello`

or

`dotnet flubu ExampleTarget -Example=Hello`

- load assembly references, nuget references through script class attributes. Alternative to directives.

```C#
[Assembly(@".\packages\Newtonsoft.Json.9.0.1\lib\net45\Newtonsoft.Json.dll")]
[NugetPackage("Newtonsoftjson", "11.0.2")]
[Reference("System.Xml.XmlDocument, System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")]
public class BuildScript : DefaultBuildScript
{
}
```
- Added Must method to target fluent interface. Condition in must will have to be meet otherwise target execution will fail before any task get executed.

- Option to execute custom code before each target execution(target dependencies are excluded). Just override following methods:

```C#
 protected override void BeforeTargetExecution(ITaskContext context)
  {
  }

  protected override void AfterTargetExecution(ITaskContext context)
  {
  }
```

- Colored console logging

```C#
  public void Example(ITaskContext context)
    {
        context.LogInfo("Some text", ConsoleColor.DarkGray, ConsoleColor.DarkMagenta);
        context.LogInfo("Some Text2", ConsoleColor.Blue);
        context.LogError("Error", ConsoleColor.Blue);
    }
```

 - FetchVersionFromExternalSourceTask now supports following build systems : Bamboo, Bitrise, ContinousCl, Jenkins, TFS, TeamCity, TravisCI.

- CompileSolutionTask: support for VS2019 
- Restoring of nuget packages has fallback to msbuild now if dotnet core sdk is not installed
- New Config attribute: Disable load of script references from csproj
- New Config Attribute: Always recompile build script
- Expose the output of ExternalProcessTaskBase
- Fix: Specifing flubu script path in config file does not work
- Fix: BuildScript assembly is not recompiled when included cs files are changed
- Fix: Added interactive method to task fluent interface.
- Fixed switched capture output and capture error output
- Fixed GetRemoveFileTask base methods (null reference exception)
- Fixed GitPushFileTask base methods (null reference excetpion).
- Fixed GitAddTask base methods (null reference excetpion).
- External process task return type is now generic
- script key is now case insensitive in file configuration.
- switched from Microsoft.Extensions.CommandLineUtils to McMaster.Extensions.CommadLineUtils
- Minor visual improvements when displaying help.
- Added Net462 Web api deploy package for x86
- Added some more default build script locations.

## FlubuCore 2.14.0

- Add support for interactive task members. 

Example:

        protected override void ConfigureTargets(ITaskContext context)
        {
             context.CreateTarget("Example")
                    .AddTask(x => x.CompileSolutionTask()
                        .Interactive(m => m.BuildConfiguration("default value if interactive mode disabled or value is 
                         passed as argument."), consoleText: "Enter build configuration:"));

            context.CreateTarget("Example2")
                .SetAsDefault()
                .Do(Example2, 
                     "default value if interactive mode disabled or value is passed as argument", 
                      options => { options.Interactive(m => m.Param, "-test", consoleText: "Enter example value to print to console:"); });
        }

        private static void Example2(ITaskContext context, string value)
        {
            context.LogInfo($"Entered: {value}");
        }

If u run target Example2 from console u will be prompted by Flubu to enter value which will be then printed to console.

- Flubu now supports cleanup actions when hitting control + c.. If u want that cleanup actions are performed You have to explicitly set parameter in task Finally method or in group parameter.

Bellow is example in which FlubuCore performs specified cleanup actions when hitting control + c or control + break (two optional parameters with true value are added)

     context.CreateTarget("run.postgres")
            .SetAsDefault()
            .Group(
                target =>
                {
                    target
                        .AddTaskAsync(task =>
                            task
                                .DockerTasks()
                                .Run("postgres:10.5", string.Empty)
                                .Finally(innerContext => innerContext.LogInfo("Testing1"), true));
                }, innerContext => { innerContext.LogInfo("Testing2"); },
                cleanUpOnCancel: true);  
                
- Improves logging on web api client tasks.
- (Possible breaking change)Removed obsolete methods from some tasks
- Adds option to set destination package folder in CreateZipPackageFromProjcet tasks. Currently only default destination folder could be used.

## FlubuCore 2.13.0.0
- Added docker generated tasks
- (Breaking changes) Old Docker task's that were previously manually implemented were overwriten with generated task.
  - Docker tasks that used property of type List<> were replaced with params. 
  - Some method names in docker tasks were renamed to the same name as it is option name in the docker command.
- Improved target fluent interface intelisense by adding methods from base interface.
- GitBranch information can be readed for jenkins build system. context.BuildSystems().Jenkins().GitBranch;
- WebApi increased max size limit of uploaded content

## FlubuCore 2.12.0 
- Added Git tasks:Clone, Pull Add, Commit, Push, Tag, RemoveFilesTask
            
          context.Tasks().GitTasks().Commit();

- Added Docker tasks: Build, Run, Stop, RemoveContainer, RemoveImage   

          context.Tasks().DockerTasks().Build(".");

## FlubuCore 2.11.0
- [FlubuCore cake plugin](https://github.com/flubu-core/FlubuCore.CakePlugin) which allows you to use any cake addin in FlubuCore.
- Added FlubuCore specific code analyzers. Added target parameter analyzers when specifing target's with Target attribute. Added FromArg attribute analyzer.
- Greatly improved performance for .net core.
- Improved nuget package resolving performance.

## FlubuCore 2.10.0
- Json configuration file can now be specified by machine name. FlubuSettings.{MachineName}.Json
- Added WaitForDebugger task context extension.

## FlubuCore 2.9.0
- Added support for referencing a nuget package in build script. https://github.com/flubu-core/flubu.core/wiki/2-Build-script-fundamentals#Referencing-nuget-packages
- Added support for debugging the script by attaching flubu process to the debuger. https://github.com/flubu-core/flubu.core/wiki/6-Writing-build-script-tests,-debuging-and-running-flubu-tasks-in-other-applications

## FlubuCore 2.8.2 

- FlubuCore is now available as .net core global tool. `dotnet tool install --global FlubuCore.GlobalTool`
- Flubu dotnet cli tool and web api is now available for .net core 2.1.
- Console arguments, configuration properties, enviroment variables can now be passed to script properties with FromArg attribute. Property doesn't need to have attribute. Argument key in that case is same as the property name.

      public class SimpleScript : DefaultBuildScript
      {
        [FromArg("-sn", "If true app is deployed on second node. Otherwise not.")]
        public bool deployOnSecondNode { get; set; }

        protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
        {
        }

        protected override void ConfigureTargets(ITaskContext context)
        {
            context.CreateTarget("Deploy.Exapmle")
                .AddTask(x => x.FlubuWebApiTasks().GetTokenTask("user", "pass").SetWebApiBaseUrl("noade1Url"))
                .AddTask(x => x.FlubuWebApiTasks().UploadPackageTask("packageDir", "*.zip"))
                .AddTask(x => x.FlubuWebApiTasks().ExecuteScriptTask("Deploy", "DeployScript.cs"))
                .Group(target =>
                    {
                    target.AddTask(x => x.FlubuWebApiTasks().GetTokenTask("user", "pass").SetWebApiBaseUrl("noade2Url"))
                               .AddTask(x => x.FlubuWebApiTasks().UploadPackageTask("packageDir", "*.zip"))
                               .AddTask(x => x.FlubuWebApiTasks().ExecuteScriptTask("Deploy", "DeployScript.cs"));
                     },
                     when: c => deployOnSecondNode);
         }
       }

You could then pass argument to property like so:

`Dotnet flubu Deploy.Example -sn=true`

- Target's can now be defined with attribute on method.

        [Target("targetName", "a", "b")]
        [Target("targetName2", "c", "d")]
        [Target("targetName3", "e", "f")]
        public void Example(ITargetFluentInterface target, string source, string destination)
        {
                target.AddTask(x => x.CopyFileTask(source, destination, true));
        }

## Flubu 2.7.0
- Added Xunit task - For running xunit tasks with xunit console runner.
- WebApi: Option to include flubu web api server logs into ExecuteScript response.
- WebApi: Option to include StackTrace to error response.
- Added Build system providers - You can acces various build, commit... information for various build systems (such as Jenkins, TeamCity, AppVeyor, Travis...) 

      protected override void ConfigureTargets(ITaskContext context)
      {
            bool isLocalBuild = context.BuildSystems().IsLocalBuild;
            var gitCommitId = context.BuildSystems().Jenkins().GitCommitId;
      }

-  Added conditonal task execution with when cluase on single task (see bellow for group of tasks)

       context.CreateTarget("Example")
            .AddTask(x => x.CompileSolutionTask())
            .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
                .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);

- Added finally block on single task. Finally block acts just like finally in try catch  (see bellow for group of tasks)

       context.CreateTarget("Example")
            .AddTask(x => x.CompileSolutionTask())
            .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec")
                .Finally(c => c.Tasks().DeleteFilesTask("pathtoNuspec", "*.*", true).Execute(c)));

- Added onError block on single task.  You can perform some custom action when error occures on single task(see bellow for group of tasks)

       context.CreateTarget("Example")
            .AddTask(x => x.CompileSolutionTask())
            .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec")
                .OnError((c, ex) => c.Tasks().DeleteFilesTask("pathtoNuspec", "*.*", true).Execute(context)));

-  Added conditonal task execution with When clause on group of tasks.

       protected override void ConfigureTargets(ITaskContext context)
       {
             context.CreateTarget("Example")
            .AddCoreTask(x => x.Build())
            .Group(
                target =>
                {
                    target.AddCoreTask(x => x.Pack());
                    target.AddCoreTask(x => x.NugetPush("pathToPackage"));
                },
                when: c => !c.BuildSystems().Jenkins().IsRunningOnJenkins);
        }

- Finally on group of tasks: Added onFinally block on group of tasks. onFinally acts just like finally in try/catch.

        context.CreateTarget("Example")
                .AddCoreTask(x => x.Build())
                .Group(
                    target =>
                    {
                        target.AddCoreTask(x => x.Pack());
                        target.AddCoreTask(x => x.NugetPush("pathToPackage"));
                    },
                    onFinally: c =>
                    {
                        c.Tasks().DeleteFilesTask("pathToNupkg", "*.*", true).Execute(c);
                    });
- OnError on group of tasks:  You can perform some custom action when error occures in any of tasks that are in group.

        context.CreateTarget("Example")
            .AddCoreTask(x => x.Build())
            .Group(
                target =>
                {
                    target.AddCoreTask(x => x.Pack());
                    target.AddCoreTask(x => x.NugetPush("pathToPackage"));
                },
                onError: (c, error) =>
                {
                   //// some custom action when error occures in any of the task in group.
                });

## Flubu 2.6.0

- Added option to add multiple tasks, dependencies With (anonimous) method to target with Do method.

        protected override void ConfigureTargets(ITaskContext context)
        {
            context.CreateTarget("deploy.PreProduction")
                .Do(Deploy, @"C:\Web", "AppPool_Preprod", "PreProduction");

            context.CreateTarget("deploy.Production")
                .Do(Deploy, @"d:\Web", "AppPool_Prod", "Production");
        }

        public void Deploy(ITargetFluentInterface target, string deployPath, string appPoolName, string enviromentName)
        {
            target.AddTask(x => x.IisTasks().ControlAppPoolTask(appPoolName, ControlApplicationPoolAction.Stop))
                .Do(UnzipPackage)
                .AddTask(x => x.DeleteDirectoryTask(deployPath, false).Retry(30, 5000))
                .AddTask(x => x.CreateDirectoryTask(deployPath, false))
                .AddTask(x => x.CopyDirectoryStructureTask(@"Packages\WebApi", deployPath, true))
                .AddTask(x => x.IisTasks().ControlAppPoolTask(appPoolName, ControlApplicationPoolAction.Start));
        }

## Flubu 2.5.0

- Added create HttpClient task.

## Flubu 2.4.0
- Added BuildScriptEngine for writing build script tests, build script debuging and executing flubu tasks in other .net (core) applications. See example: https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs

## Flubu 2.3.0
- Option to pass through arguments to tasks

        context.CreateTarget("ExampleTarget")
            .AddTask(x => x.CompileSolutionTask()
                .ForMember(m => m.BuildConfiguration("Release"), "c"));

        //// alternatively you can get argument value like this:
        string configuraiton = context.ScriptArgs["c"];

You can execute target with -c argument:

`build.exe ExampleTarget -c=Debug`

You can also set value in configuration file (flubusettings.json) or through enviroment variable. See https://github.com/flubu-core/flubu.core/wiki/2-Build-script-fundamentals#Script-arguments for more info.

## Flubu 2.0.0

- Added support for multiple target execution in script runner.
- Added task for executing powershell scripts.
- Added NunitWithDotCover task.
- Added option to get predefined build properties - See build script fundamentals for more info.

1.9.0.0
- add support for setting verbosity and other logging properties for msbuild (Compile Task).  
- Improved ServiceControlTask inteface.
- Added CreateService task.
- All Task that uses external program now implements external process tasks interface(Improved usability).

1.8.1.0
- dotnet-flubu is now also build in .netcoreapp 1.0 target framework to support older versions.  

1.8.0.0
- added support for finding and using MSBuild 15.0 in builds.
- All tasks that uses external programs have now fluent interface to add custom arguments.
- Improved dotnet core task fluent interface.
- Added GetEnviromentVariable extension method to TaskContext.

1.7.3.0
- if not target specified and not default target, display help.

1.7.2.0
- added SleepTask.
- added Sc.exe task.
- added generic interface for external process tasks.

1.7.1.0
- Fixed script arguments pass through on flubu runner and dotnet-flubu cli tool.

1.7.0.5
- Fixed NoLog ITask interface.

1.7.0.4
- Option to disable task logging.

1.7.0.3
- Updated SqlCmdTask (do not escape args).

1.7.0.2
- merged replaceToken and replaceText tasks.

1.7.0.1
- added standard sqlcmd params.

1.7.0.0
- Added SqlCmd task with output capture support.
- Added capture output support for RunProgramTask.

1.6.9.1
- fixed compile task (correctly pass arguments to msbuild).

1.6.9.0
- updated compile task to support workingFolder and any params for msbuild.
- fixed il merge generation with libz container.

1.6.8.0
- Fixed references to system assemblies in .net 462 which caused stackoverflow exception in flubu.runner in atleast package task.

1.6.7.1
- Fixed PackageTask logging.

1.6.7.0
- Fixed retry on tasks.

1.6.6.1
- Fixed binding redirect for System.Security.Cryptography.Algorithms.
- Display flubu version info.

1.6.6.0
- Flubu is now build with .net core sdk 2.0 on build serve.

1.6.5.0
- fixed flubuCore runner binding redirects.

1.6.4.0
- Dotnet-flubu now targets netcoreapp1.1.

1.6.3.1
- Added SqlCmd task for executing MS SQL scripts.
1.6.3.0
- FlubuCore: Fixed generic parameters in Do Task.
- FlubuCore: Removed verbose switch for default NUnit 3 task. Issues with nunit 3.7.

1.6.2.0
- FlubuCore: Fixed web api set of base url when doing more that one request in one target.
- FlubuCore: Added option to add generic parameters to Do task. 

1.6.1.0
- FlubCore: All tasks have now retry mechanism option.
- FlubuCore: All tasks have now do not fail option.

1.6.0.0
- FlubuCore, WebApi: Added option to pasthrough arguments to targets and custom tasks.
- FlubuCore: Added upload script task.
- FlubuCore: Added delete packages task.
- FlubuCore: Fixed web api base url set through build propertis.
- WebApi: Added option to upload scripts to web api through web api method.
- WebApi: Fixed CommandArguments lifestyle.
- WebApi: Only scripts in script directory can now be executed.

1.5.2.0
- Fixed UploadPackageTask.
- web api ip white list access restriction.

1.5.1.0
- Added flubu web api GetToken task.
- Improved flubu web api UploadPackageTask and ExecuteScriptTask.
- Added web api documentation.

1.5.0.0
- Added FlubuCore web api for remote script execution.
- Added FlubuCore web api client.
- Added Flubu web api tasks to FlubuCore.

1.4.13.0
- Removed Client from FlubuCore.

1.4.12.0
- Upgraded nuget packages.

1.4.11.0
- Added generic DoNotFailOnError setting for tasks.

1.4.10.0
- Updated nuget packages.
- Fixed ControlAppPoolTask missing dependencie.

1.4.8.0
- Fixed version information in GenerateCommonAssemblyInfo task extension.
- GenerateCommonAssemblyInfo task extension has now GenerateCommonAssemblyInfo task action parameter.
- BREAKING CHANGE: Improved core pacakge extension tasks.
- Improved some others task extensions with task action parameter.

1.4.6.0
- Added do not fail option to run program task.

1.4.5.0
- Fixed dotnet core fluent interface for dotnet restore build and publish.

1.4.4.0
- Fixed dotnet core tasks (build, restore, clean, publish,) when no project name is defined. 

1.4.3.0
- BREAKING CHANGE updated flubu.core and flubu.runner .net framework from .net4.6 to .net.462.

1.4.2.0
- Added support for including other .cs files into buildscript with //#imp {PathToCsFile}.
- Added dotnet nuget push task.
- Added dotnet entity framework task.
- CompileSolutionTask: Improved Msbuild path locator Using Microsoft tool location helper now. Registry locator is now used as fallback .
- Solution name and configuration are now added form build props in DotNet specific tasks if not specified explicitly.
- PackageTask: Added option to disable logging of which files were filtered and copied.
- Updated flubu dependencies. No release candidates are referenced anymore. See https://bitbucket.org/zoroz/flubu.core/commits/cfeaec842a83dfd06f62c13aadd2b74496e47fa7 for more info.

1.3.11.0
- Updated Microsoft.Web.Administration from 10.0.0-rc1 to 10.0.0 used for iis tasks.
1.3.10.0
- CompileSolution task now supports specifing your own paths to Msbuild. If msbuild path is not specified or not found MsBuild is still searched at default locations. 
1.3.9.0
- SSH command capture output stream directly.
1.3.8.0
- SSH command task fixes.
1.3.7.0
- Added SSH support for entering password.
- Added support for executing multiple commands in one session.
1.3.6.0
- Added support for SSH. SshCommand and SshCopy tasks.
1.3.5.0
- CreateApplicationPool iis task: .Net clr version can now be set.
- All iis tasks have now fluent interface.
1.3.4.0
- Fixed iis task interfaces. They now contain Execute and ExecuteVoid methods.
- PackageTask - fixed issue when output zip file name contains more than one dot.
1.3.3.0
- Added support for external assembly loading by assembly relative path
- Target names are case insensitve now
- If target to be run does not exist help is now shown instead of default target being run.
- Build script can now contain namespace
1.3.2.0
- Added support for external reference based on type loading.
- Added support for external assembly loading by assembly full path.
- Do in Target is now a task.
- BREAKING CHANGE: Do is now executed in the order specified in build script and not anymore before all tasks.
- Added DoAsync to target: For asynchronus custom code execution.
- Added AddTaskAsync to target: For asynchronus task execution.
- Added DependsOnAsync to Target: For asynchronus target dependencies execution.
- All tasks have now ExecuteAsync method.
1.2.3.0
- Added explicit System.IO reference to Roslyn scripting engine.
1.2.2.0
- Added LogInfo and LogError to TaskContext.
- Added fluent interface to PublishNugetPackageTask.
- Added fluent interface to CopyDirectoryStructureTask.
- Added fluent interface to FetchBuildVersionFromFileTask.
- Added fluent interface to UpdateXmlFileTask.
- Added fluent interface to ReplaceTokensTask.
- moved packaging filters to it's own namespace.
- Added FlubuCore and dotnet-flubu nuget metadata.
1.2.1.0
- Minor fixes.
1.2.0.0
- Flubu.Runner now works without any manual config modifications. 
- Task fluent interface documentation.
- Added Dotnet specific tasks and extensions.
- BREAKING CHANGE: Splited TaskExtensions into CoreTaskExtensions and TaskExtensions.
1.1.10.0
- Updated nuget packages to latest version.
1.1.9.0
- Removed dotnet test -xml output parameter. It won't work under VS2017 RC.
1.1.8.0
- BREAKING CHANGE: Removed DependsOn by TaskExtensionsFluentInterface from TargetFluentInterface. Use BackToTarget instead on TaskExtensionFluentInterface.
1.1.7.0
- System tests.
1.1.6.0
- CompileSolutionTask - specific platform can be set now. Default is still AnyCPU.
- CompileSolutionTask - Custom arguments can be added now. 

1.1.5.0
- Added FlubuCore.Runner for .net 4.6.
1.1.4.0
N/A
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at mzorec@gmail.com or zoro.zorec@gmail.com. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
# Contribution Guidelines

First of all, thanks for thinking of contributing to this project! 👏

This project has a [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## 🛎 Questions

Feel free to open a ticket with your question.

If u have any improvement or feature proposal's we would be glad to hear from you. Add new issue as proposal and we will discuss it with you.

Please put some effort in requesting a new feature. If someone else is going to implement something, the least you can do is describe the feature in detail, and why it would be useful to others as well.

## 🐛 File a Bug

In case you've encountered a bug, please make sure:

* You are using the latest version
* You have read the [documentation](https://github.com/flubu-core/flubu.core/wiki) first, and double-checked your configuration.
* In your issue description, please include:
	* What you expected to see, and what happened instead.
	* Your operating system and other environment information.
	* As much information as possible, such as the command and configuration used.
	* Interesting parts of code and script logs with `--debug` argument applied.
	* All steps to reproduce the issue.
* When you are requesting to fix a bug or new feature you should become a stargazer.

## 🎁 I Want to contribute to the code

Pull requests are welcome! We are also looking for new team member's [![Gitter](https://img.shields.io/gitter/room/FlubuCore/Lobby.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Please keep the following in mind:

* You can contribute to the code by fixing a bug, implement new feature or improve existing code. 
  Search issues by label Help wanted, Good first issue, Enchantment, New task, New plugin or take any other issue if u know how to implement/fix it.
* If u found a new bug and want to fix it your self or you want to implement new feature first open new issue so we discuss it with you.
* Make sure the tests pass. Your changes probably deserve new tests as well.
* Remember that this project is cross-platform compatible (macOS, Windows, Linux)

MIT License

Copyright (c) 2018 FlubuCore

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
<p align="center">
  <span>English</span> |  
  <a href="https://github.com/dotnetcore/FlubuCore/tree/master/lang/chinese">中文</a>
</p>

# FlubuCore

[![Travis](https://img.shields.io/travis/dotnetcore/FlubuCore.svg?branch=maste&?style=flat-square&label=build)](https://travis-ci.org/dotnetcore/FlubuCore)
[![NuGet Badge](https://buildstats.info/nuget/flubucore)](https://www.nuget.org/packages/FlubuCore/)
[![Gitter](https://img.shields.io/gitter/room/FlubuCore/Lobby.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Member project of .NET Core Community](https://img.shields.io/badge/member%20project%20of-NCC-9e20c9.svg)](https://github.com/dotnetcore)
[![License](https://img.shields.io/github/license/dotnetcore/FlubuCore.svg)](https://github.com/dotnetcore/FlubuCore/blob/master/LICENSE)

- [Introduction](#Introduction)
- [Features and Advantages](#Features-and-Advantages)
- [Getting Started](#Getting-Started)
- [Examples](#Examples)
- [Contributing](#Contributing)
- [Backers and Sponsors](#Further-Development)
- [Acknowledgements](#Acknowledgements)

## Introduction

"FlubuCore - Fluent Builder Core" is a cross platform build and deployment automation system. You can define your build and deployment scripts in C# using an intuitive fluent interface. This gives you code completion, IntelliSense, debugging, FlubuCore custom analyzers, and native access to the whole .NET ecosystem inside of your scripts.

![FlubuCore in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/demo.gif)

FlubuCore offers a .net (core) console application that uses power of roslyn to compile and execute scripts. Above example can be run from console with:

* FlubuCore runner (.NET 4.62+)  ``` flubu.exe Default ```
* FlubuCore dotnet cli tool (.NET Core 1.0+) ``` dotnet flubu Default ```
* FlubuCore global tool (.NET Core 2.1+) ``` flubu Default ```
## Features and Advantages

* Intuitive an easy to learn. C#, fluent interface, and IntelliSense make even most complex script creation a breeze.

```cs
context.CreateTarget("Example")
  .DependsOn(fetchBuildVersionTarget)
  .AddTask(x => x.CompileSolutionTask())
  .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
      .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);
```
          
* [Large number of often used built-in tasks](https://flubucore.dotnetcore.xyz/tasks/) like e.g. running tests, managing IIS, creating deployment packages, publishing NuGet packages, docker tasks, executing PowerShell scripts and many more.

```cs
context.CreateTarget("build")
   .AddTask(x => x.GitVersionTask())
   .AddTask(x => x.CompileSolutionTask("MySolution.sln").BuildConfiguration("Release");

context.CreateTarget("run.tests")
   .AddTask(x => x.XunitTaskByProjectName("MyProject").StopOnFail())
   .AddTask(x => x.NUnitTask(NunitCmdOptions.V3, "MyProject2").ExcludeCategory("Linux"))
   .AddCoreTask(x => x.CoverletTask("MyProject.dll"));
```

* [Execute your own custom C# code.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Custom-code)

```cs
context.CreateTarget("MyCustomBuildTarget")
     .AddTask(x => x.CompileSolutionTask())
     .Do(MyCustomMethod)
     .Do(NuGetPackageReferencingExample);
```

* [assembly references and nuget packages are loaded automatically](https://flubucore.dotnetcore.xyz/referencing-external-assemblies/) when script is used together with project file. When script is executed alone (for example when deploying with FlubuCore script on production environment) references can be added with attributes.

```cs
[NugetPackage("Newtonsoft.json", "11.0.2")]
[Assembly(".\Lib\EntityFramework.dll")]
public class BuildScript : DefaultBuildScript
{
   public void NuGetPackageReferencingExample(ITaskContext context)
    {
        JsonConvert.SerializeObject("Example");
    }
}
```

* [Easily run any external program or console command in your script.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Run-any-program)

```cs
context.CreateTarget("Run.Libz")
    .AddTask(x => x.RunProgramTask(@"packages\LibZ.Tool\1.2.0\tools\libz.exe")
        .WorkingFolder(@".\src")
        .WithArguments("add")
        .WithArguments("--libz", "Assemblies.libz"));
```

* [Pass command line arguments, settings from json configuration file or environment variables to your script.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Script-arguments)

 ```cs
 public class SimpleScript : DefaultBuildScript
 {
    [FromArg("sn", "If true app is deployed on second node. Otherwise not.")]
    public bool deployOnSecondNode { get; set; }

 
     protected override void ConfigureTargets(ITaskContext context)
     {
         context.CreateTarget("compile")
            .AddTask(x => x.CompileSolutionTask()
                .ForMember(y => y.SolutionFileName("someSolution.sln"), "solution", "The solution to build.")); 
     }
  }
 ```
 
 ```
  flubu.exe compile -solution=someOtherSolution.sln -sn=true
 ```
* [Extending FlubuCore fluent interface by writing your own tasks within FlubuCore plugins.](https://flubucore.dotnetcore.xyz/write-plugins)

    ```cs
    public class ExampleFlubuPluginTask : TaskBase<int, ExampleFlubuPluginTask>
    {
        protected override int DoExecute(ITaskContextInternal context)
        {
            // Write your task logic here.
            return 0;
        }
    }
    ```
* [Growing list of FlubuCore plugins complements built in tasks.](https://flubucore.dotnetcore.xyz/AwesomePlugins/awesome-plugins/)

* [Asynchronous or parallel execution of tasks, target dependencies and custom code.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Async-execution)

    ```cs
    context.CreateTarget("Run.Tests")
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName3"));
    ```

* [Override existing options or add additional options to tasks through console](https://flubucore.dotnetcore.xyz/override-add-options/)

   ```c#
  context.CreateTarget("Example")`
      .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 
   ``` 

  `flubu example --configuration=Debug`

   flubu would execute `dotnet build MySolution.sln --configuration Debug`    

* [Full .NET Core support including the global CLI tool](https://flubucore.dotnetcore.xyz/getting-started#getting-started-net-core)

    ```
    dotnet tool install --global FlubuCore.GlobalTool
    flubu compile
    ```
    
* [FlubuCore interactive mode](https://flubucore.dotnetcore.xyz/build-script-runner-interactive/) which offers target tab completition, options tab completition, toogle targets/options, executed commands history. It is also possible to execute external commands and operable programs. For some of them FlubuCore offers tab completion with help displayed at the bottom of console out of the box(such as dotnet, git..)

![FlubuCore interactive mode](https://raw.githubusercontent.com/dotnetcore/flubu.core/master/assets/FlubuCore_Interactive_mode_full.gif)

* [Possibility to test and debug your build scripts.](https://flubucore.dotnetcore.xyz/Tests-debugging)

    ```cs
    context.WaitForDebugger();
    ```

* [Easily automate deployments remotely via the FlubuCore Web API.](https://flubucore.dotnetcore.xyz/WebApi/getting-started/)

* [Possibility to use FlubuCore tasks in any other .NET application.](https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs)

* Improved developer experience with FlubuCore custom analyzers.

![FlubuCore analyzers in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCoreCustomAnalyzerDemo.png)

## Getting Started
Using FlubuCore is straightforward and very simple :-) It is also fully and throughly documented.

The [Getting Started](https://flubucore.dotnetcore.xyz/getting-started/) chapter in [FlubuCore Documentation](https://flubucore.dotnetcore.xyz) will help you set up your first FlubuCore build in no time.

A comprehensive list of features that FlubuCore has to offer with descriptions can be found in the [Build Script Fundamentals](https://flubucore.dotnetcore.xyz/buildscript-fundamentals) chapter.

Once you have your build and deployment scripts defined, the following Wiki chapters will explain how to run them:
* For .NET Framework projects use [FlubuCore.Runner](https://flubucore.dotnetcore.xyz/getting-started#Installation.net)
* For .NET Core projects use [FlubuCore CLI global tool](https://flubucore.dotnetcore.xyz/getting-started#Installation-.net-core)

## Examples
Aside from the detailed Wiki FlubuCore comes with example projects that reflect real-life situations. The examples can be found in the separate [Examples repository](https://github.com/flubu-core/examples/).

These examples will help you to get quickly start with FlubuCore:
* [.NET Framework build example](https://github.com/flubu-core/examples/blob/master/MVC_NET4.61/BuildScripts/BuildScript.cs
) - Example covers versioning, building the project, running tests, packaging application for deployment and some other basic use cases.

* [.NET Core build example](https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScript.cs
) - Example covers versioning, building the project, running tests, packaging application for deployment and some other basic use cases.

* [Deployment script example](https://github.com/flubu-core/examples/blob/master/DeployScriptExample/BuildScript/DeployScript.cs
) - Example shows how to write simple deployment script. 

* [Open source library example](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCoreOpenSource/Build/BuildScript.cs) - Example covers versioning, building the project, running tests and publishing nuget package. It also covers how to run build script on Appveyor and Travis CI.
## Have a question?

 [![Join the chat at https://gitter.im/FlubuCore/Lobby](https://badges.gitter.im/mbdavid/LiteDB.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Contributing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

### Ways to Contribute

* We appreciate deeply any feedback that you may have! Feel free to participate in the chat, or add an issue in the issue tracker.
* Spread the word about the project.
* If you like the project don't forget to give it a star so that the community get's bigger.
* Improve documentation.
* Report, fix a bug.
* Implement a new feature.
* Discuss potential ways to improve project.
* Improve existing implementation, performance, etc.

## Changelog and Roadmap

Changes with description and examples can be found in [Changelog](https://github.com/flubu-core/flubu.core/blob/master/CHANGELOG.md) 
 
You can see FlubuCore roadmap by exploring opened [Milestones.](https://github.com/flubu-core/flubu.core/milestones)

## Further Development
If you find FlubuCore useful (you feel it helps you on the daily basis) you can support further development by buying us a coffee (or become a backer or sponsor). Sometimes it's hard to stay awake till midnight implementing new features, coffee helps us with that. We would really appreciate your support. Money from sponsorship will also be used for the promotion of the project. If you are a backer or a sponsor you can also request for a new feature or ask for support. These issues will be handled with highest priority.

[![](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/NCOpMkt)

### Backers and Sponsors
[![OpenCollective](https://opencollective.com/flubucore/backers/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12502) 
[![OpenCollective](https://opencollective.com/flubucore/sponsors/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12503)

## Used & Powered by
Thank's to Comtrade for supporting us.

[![FlubuCore analyzers in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/Svg/COMTRADE_logo.PNG)](https://www.comtrade.com)

## Acknowledgements

* Special thanks to [@ironcev](https://github.com/ironcev) for greatly improving readme and for giving some valuable advices.
* Special thanks to [@alexinea](https://github.com/https://github.com/alexinea) for translating whole documentation to Chinese.
We are glad you're about to open a PR. Just a few tips before you click submit:

* Please make sure you read, CONTRIBUTING.md
* We may not take PRs if they come out of the blue and make big changes. 
  If you're not sure if something is a "big change", please open an issue first.
  
Thanks!
---
name: Bug report
about: Create a report to help us improve

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Using this version of the library '...'
2. Run this code '....'
3. With these arguments '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Additional context**
Add any other context about the problem here.
---
name: Feature request
about: Suggest an idea for this project

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. 
Example. I'm am trying to do [...] but [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
---
name: Question
about: Fell free to ask anything about FlubuCore.

---



When executing flubu script or any other process locally in console it is recomended to run FlubuCore in interactive mode it gives you some really nice features which are listed in the [features section.](#features) To start FlubuCore interactive mode just execute command `flubu -i` in your favorite console. 

## **Demo**
![Interactive mode in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCore_Interactive_mode_full.gif)
 *[Build script](https://gist.github.com/mzorec/c2e0d0572ed023f1d3ebbe72cb5903fc) used in demo.*

## **Features**

Features in interactive mode

- Target's tab completition with tab key
- Option's (parameter) tab completition with tab key
- Option's (parameter) value tab completition with tab key for enum types
- Target help displayed at the bottom of console
- Option help displayed at the bottom of console
- Execute external commands. Meaning if you run FlubuCore interactive mode for example in powershell all powershell commands are available in FlubuCore interactive mode.
- Execute external processes. For some of them FlubuCore offers tab completion with help at the bottom of console out of the box(such as dotnet, git...[See full list](#external-processes-tab-completion-list))
- Next / previos target with up and down arrow
- Next / previos option with up and down arrow
- Next / previos target or option with tab key
- History of executed commans with up and down arrow
- No need to load script for each executed target
- reload or load another script
- Navigation beatwen folders


## **Internal commands**

- `cd` change directory.
- `dir` list files and directories
- `l|load -s={script}` Load another FlubuCore script.
- `r|reload` Reload currently loaded script.
- `e|q|exit|quit` Exit Flubu Core interactive mode.

## **Hot keys**
Following hot keys are supported:

- `Enter` Executes entered command
- `Tab` completes user's input with active target/option hint (if found)
- `Up arrow` select previous command from history if user's input is empty or select previous hint (if possible)
- `Down arrow` select next command from history if user's input is empty or select next hint (if possible)
- `Left arrow` move cursor left
- `Right arrow` move cursor right
- `Backspace` removes character before cursor
- `Delete` removes character under cursor
- `Home` move cursor to the beginning of user's input
- `End` move cursor to the end of user's input

## External processes tab completion list

List of external processes for which tab completion of options/switches is available in FlubuCore interactive mode. 
it is planned that all docker, octopus, azure, npm and chocolatey commands will also be supported in the near feature.

- dotnet build
- dotnet test
- dotnet pack
- dotnet publish
- dotnet nuget push
- dotnet restore
- dotnet tool install
- dotnet tool update
- dotnet tool uniinstall
- git add
- git commit
- git push
- git checkout
- git clone
- git submodule
- git rm
- git tag
- gitversion
- coverlet
- sqlcmd.exe

In .NET you run flubu build scripts with console application flubu.exe. Add Flubu.Runner nuget to get the console application.

In .NET core you run flubu build scripts with dotnet command line tool or global tool. How to install tools see [Getting started section]

### **Usage**

.NET core usage: `dotnet flubu {TargetToExecute} {Flubu options} {build script arguments}`

.NET core global tool usage: `flubu {TargetToExecute} {Flubu options} {build script arguments}`

.NET usage: flubu.exe `{TargetToExecute} {Flubu options} {build script arguments}`

#### Multiple target execution

.NET core usage: dotnet flubu {TargetToExecute} {TargetToExecute2} {TargetToExecute3...} {Options}

.NET usage: flubu.exe {TargetToExecute} {TargetToExecute2} {TargetToExecute3...} {Options}

Target's can be executed in parallel with added `-parallel` option 
### **Flubu options**

![N/A](img/FlubuHelp.png "Flubu help")

### **target help**

List all available targets:

`flubu help`

`dotnet flubu help`

Target specific help:

`flubu {TargetName} help`

`dotnet flubu {TargetName} help`

It displays all tasks with description that will be executed by target. It also displays which argument(with description) can be passed through to specific task in target. 

#### Specifiying which script Flubu should run.

Easiest way is to put build script at one of the default locations (you can find list of default locations below). If it is located at one of the default locations FlubuCore will execute the script automatically `flubu {TargetName}`. 
Second option is to specify script location with -s option `flubu {TargetName} -s={pathToScriptFile}` Third option is to run `flubu setup` and specify script and csproj(optional) location in interactive mode.
 Flubu will store script and csproj location to `.flubu` file. if `.flubu` file is present FlubuCore will read location of the script and csproj file from that file. Additional benefit when storing location to `.flubu` file is 
 that you don't need to execute script at the root directory of the project. Meaning if your project is for example located at "c:\_git\myproject" you can execute script inside any subfolder of that location.

### **Default build script locations**

- "Build.cs"

- “BuildScript.cs”

- “DeployScript.cs”

- "DeploymentScript.cs"

- "_Build/Build.cs"

- "_Build/BuildScript.cs"

- "Build/Build.cs"

- "Build/BuildScript.cs"

- "_BuildScript/BuildScript.cs"

- "_BuildScripts/BuildScript.cs"

- “BuildScript/BuildScript.cs”

- “buildscript/deployscript.cs”

- “buildscripts/buildscript.cs”

- “buildscripts/deployscript.cs”

- "BuildScript/DeploymentScript.cs"

- "BuildScripts/DeploymentScript.cs"

[Getting started section]: getting-started.md## **Build script**


Each build script should inherit from DefaulBuildScript class. Two abstact methods from DefaultBuildScript have to be implemented.

- ConfigureTargets: Here you can create new targets that will perform specific work.

- ConfigureBuildProperties: Here you can set various build properties which can be shared between multiple tasks and your custom csharp code.

Empty build script example

```C#
public class BuildScript : DefaultBuildScript
{
	protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
    {
    }

    protected override void ConfigureTargets(ITaskContext session)
    {
    }
}
```

<a name="Targets"></a>

## **Targets**
-------

Targets are used to perform specific work in a specific order. A target can for example execute flubu built in tasks like a task for compiling the solution or it can execute some custom csharp code. Target can also have dependencies on other targets.

### **Create a new Target**

Following code will create a new target that will execute a built in task.

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Compile")
		.SetDescription("Compiles the solution")
        .AddTask(x => x.CompileSolutionTask());
}
```

Target's can also be defined with attributes on method.

```C#
[Target("targetName", "a", "b")]
[Target("targetName2", "c", "d")]
[Target("targetName3", "e", "f")]
public void Example(ITarget target, string source, string destination)
{
	target.AddTask(x => x.CopyFileTask(source, destination, true));
}
```

You can also pass values to parameter through console arguments or FlubuCore config file.

`Flubu targetName2 -destination=SomeOtherDestination`

<a name="Tasks"></a>

### **Tasks**

Tasks are divided in tasks and core tasks. tasks can be executed in .net and .net core projects. Core tasks can only be executed in .net core projects.

Following example executes 2 core tasks in a target. Order of execution is the same as specified in code.

```C#  
context.CreateTarget("Build")
    .AddCoreTask(x => x.Restore())
    .AddCoreTask(x => x.Build());
```

All Tasks have following methods:
  
- ``` .OnError((c, ex) => { c.LogInfo("Example");})) ``` - onError can perform some custom action when error occurs on specific task.

- ``` .Retry(5, 1000) ``` - Retry mechanism. You can apply specific condition when retry mechanism will retry task.

- ``` .Finally(c => { c.LogInfo("Example");})) ``` - Finally block acts just like finally in try catch.

- ``` .DoNotFailOnError() ``` - script does not fail in case of exception. You can apply specific condition when task will not fail. 

- ``` .NoLog() ``` - Task doesn't log anything to console output.

- ``` .SetDescription() ``` - Overrides the default help description of the task.

- ``` .ForMember() ``` - pass through console argument to method or property. See [Pass console arguments, settings from json configuration file, environment variables with ForMember to tasks](#Arguments-pass-through-to-tasks) for more details.

- conditonal task execution with when cluase on single task (see bellow for group of tasks)

```c#
context.CreateTarget("Example")
	.AddTask(x => x.CompileSolutionTask())
    .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
    .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);
```

- set task parameters only when specified condition is meet.

```c#
 var compile = context
	.CreateTarget("compile")
    .SetDescription("Compiles the VS solution")
    .AddCoreTask(x => x.Build().Configuration("Release")
	.When(
		() =>
		{
	    	return context.BuildSystems().IsLocalBuild;
	    }, 
		task => { task.Configuration("Debug"); }));
```

- ```.Interactive()``` - Interactively pass argument from console to specified task method / parameter.

<a name="Custom-code"></a>

### **Custom c# code / tasks**

Following example executes some custom code. You can also use built in flubu tasks in custom code as shown in example.

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Example")
       .Do(CustomCodeExample);
}

private static void CustomCodeExample(ITaskContext context)
{
    //// You can put any c# code here and use any .net libraries.
    Console.WriteLine("Dummy custom code");
    context.Tasks().NUnitTaskForNunitV3("project name").Execute(context);
}
```

You can also have parameters in methods:

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Example")
		.Do(CustomCodeExample, "some value", 1);
}

private static void CustomCodeExample(ITaskContext context, string arg1, int arg2)
{
	Console.WriteLine("Dummy custom code");
    context.Tasks().NUnitTaskForNunitV3("project name").Execute(context);
}
```

<a name="Target-dependencies"></a>

### **Target dependencies**

Target can have dependencies on other targets. All dependenies will be executed before target in the specified order.

When targetC is executed target’s will execute in the following order: TargetB, TargetA, TargetC

```C#
var targetA = context.CreateTarget("TargetA");
var targetB = context.CreateTarget("TargetB");
var targetC = context.CreateTarget("TargetC").DependsOn(targetB, targetA);      
```

<a name="Reuse-set-of-tasks"></a>

### **Add target to target**

Target can be executed within other target with AddTarget. Target is executed in the order it was added

Example:
``` C#
    protected override void ConfigureTargets(ITaskContext context)
    {
       var exampleB = context.CreateTarget("TargetB")
            .Do(Something);

       context.CreateTarget("TargetA")
           .AddCoreTask(x => x.Build())
           .AddTarget(exampleB)
           .Do(JustAnExample);
    }

    public void JustAnExample(ITaskContext context)
    {
        ...
    }
```
following execution order is taken when  TargetA is executed

1. Build task
2. TargetB target
3. JustAnExample method


### **Reuse set of tasks in different targets**

Following example shows how to reuse set of tasks in different targets:

```C#
protected override void ConfigureTargets(ITaskContext session)
{
	session.CreateTarget("deploy.local").AddTasks(Deploy, "c:\\ExamplaApp").SetAsDefault();
                
    session.CreateTarget("deploy.test").AddTasks(Deploy, "d:\\ExamplaApp");

    session.CreateTarget("deploy.prod").AddTasks(Deploy, "e:\\ExamplaApp");
}

private void Deploy(ITarget target, string deployPath)
{
    target
        .AddTask(x => x.IisTasks().CreateAppPoolTask("Example app pool").Mode(CreateApplicationPoolMode.DoNothingIfExists))
        .AddTask(x => x.IisTasks().ControlAppPoolTask("Example app pool", ControlApplicationPoolAction.Stop).DoNotFailOnError())
        .Do(UnzipPackage)
        .AddTask(x => x.CopyDirectoryStructureTask(@"Packages\ExampleApp", @"C:\ExampleApp", true).Retry(20, 5000))
        .Do(CreateWebSite)
}    
```

### **Add tasks to target with a foreach loop**

Following example shows how to add multiple tasks to target with a foreach loop

```c#
  protected override void ConfigureTargets(ITaskContext context)
  {
         var solution = context.Properties.Get<VSSolution>(BuildProps.Solution);

         context.CreateTarget("Pack")
                .ForEach(solution.Projects, (item, target) =>
                {
                    target.AddCoreTask(x => x.Pack().Project(item.ProjectName))
                          .Do(JustAnExample, item);
                });
  }

  private void JustAnExample(ITaskContext context, VSProjectInfo vsProjectInfo)
  {
        //// Do something.
  }
```

Example will execute Pack task for each project in solution.

<a name="Group-task"></a>

### **Group tasks and apply When, OnError, Finally on them**

-  Conditonal task execution with When clause on group of tasks.

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Example")
        .AddCoreTask(x => x.Build())
        .Group(
               target =>
               {
                    target.AddCoreTask(x => x.Pack());
                    target.AddCoreTask(x => x.NugetPush("pathToPackage"));
               },
               when: c => !c.BuildSystems().Jenkins().IsRunningOnJenkins);
}
```

- Finally on group of tasks: onFinally acts just like finally in try/catch.

```C#
context.CreateTarget("Example")
		.AddCoreTask(x => x.Build())
         .Group(
              target =>
              {
				 target.AddCoreTask(x => x.Pack());
                 target.AddCoreTask(x => x.NugetPush("pathToPackage"));
              },
              onFinally: c =>
              {
				 c.Tasks().DeleteFilesTask("pathToNupkg", "*.*", true).Execute(c);
              });
```

- OnError on group of tasks:  You can perform some custom action when error occures in any of tasks that are in group.

```C#
context.CreateTarget("Example")
    .AddCoreTask(x => x.Build())
    .Group(
        target =>
        {
			target.AddCoreTask(x => x.Pack());
            target.AddCoreTask(x => x.NugetPush("pathToPackage"));
        },
        onError: (c, error) =>
        {
           //// some custom action when error occures in any of the task in group.
        });
```

<a name="Async-execution"></a>

### **Asynchronus or parallel execution of tasks, customCode and dependencies**

<ul>
<li>
Tasks can be executed asynchrounously or in parallel with AddTaskAsync or AddCoreTaskAsync method.

</li>
<li>
Custom code can be executed asynchrounosly with DoAsync method.

</li>
<li>
Dependencies can be executed asynchrounosly with DependsOnAsync method.

</li>
</ul>
Following target executes 3 tasks in parallel.

```C#
session.CreateTarget("run.tests")
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName3"));
```

Async and sync methods can also be mixed

```C#
session.CreateTarget("async.example")
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .Do(SomeCustomMethod)
    .DoAsync(SomeCustomAsyncMethod2)
    .DoAsync(SomeCustomAsyncMethod3);
```

The code above will first execute 2 nunit tasks asynchronously and wait for both tasks to finish. Then it will execute SomeCustomMethod synchrounosly. After it is finished code from SomeCustomAsyncMethod2 and SomeCustomAsyncMethod3 will be executed in parallel.

#### sequential logging in asynchronus executed tasks and targets 

Usually logs are not readable when executing more than 1 task asynchronously or in parallel. That's why FlubuCore offers sequential logging in asynchronus tasks. You can enable them with  ` .SequentialLogging(true)` on target. It has to be placed before asynchronus tasks/target dependencies otherwise logs will not be sequential.
```c#
context.CreateTarget("Test")
        .SetAsDefault()
        .SequentialLogging(true)
        .AddCoreTaskAsync(x => x.Pack())
        .AddCoreTaskAsync(x => x.Pack())
        .DependsOnAsync(test2, test3);
```
Target executed in parallel with FlubuCore runner have sequential logging on by default.

`flubu target1 target2 --parallel`

<a name="Other-features"></a>

### **Other features**

#### Target features
- SetAsDefault method: When applied to target that target is runned by default if no target is specified when running the script with runner.
- SetAsHidden method: When applied to target that target is not shown in help and it can only be run as other target dependency.
- Must method: Condition in must will have to be meet otherwise target execution will fail before any task get executed.
- Requires method: Parameter specified in required method must not be null otherwise target execution will fail before any task get executed.

#### Context features

- Log:`context.LogInfo("Some Text2", ConsoleColor.Blue);`
- GetVsSolution: Get's solution and it's projects information(such as full project path, target framework, runtimeidentifier..) `context.GetVsSolution();`
- GetFiles: Get Files from specified directory with option to filter files with glob pattern `context.GetFiles(OutputDirectory, "*.nupkg");`
- GetDirectories: Get Directories from specified directory with option to filter files with glob pattern `context.GetFiles(OutputDirectory, "*.nupkg");`
- GetEnviromentVariable method: Get's the enviroment variable by name  `context.GetEnvironmentVariable("someVariable");`

<a name="Run-any-program"></a>

#### Run any program or command in build script with RunProgramTask

```C#
protected override void ConfigureTargets(ITaskContext session)
{
	var runExternalProgramExample = session.CreateTarget("run.libz")
        .AddTask(x => x.RunProgramTask(@"packages\LibZ.Tool\1.2.0\tools\libz.exe")
            .WorkingFolder(@".\src")
            .WithArguments("add")
            .WithArguments("--libz", "Assemblies.libz"));
 }
```

Linux Example:

```C#
protected override void ConfigureTargets(ITaskContext session)
{
    var runExternalProgramExample = session.CreateTarget("systemctl.example")
        AddTask(x => x.RunProgramTask(@"systemctl")             
            .WithArguments("start")
            .WithArguments("nginx.service"));
}
```

<a name="Build-properties"></a>

### **Build properties**

You can define various build properties in ConfigureBuildProperties method to share them in different tasks and custom code.

Following example show how to share nunit console path across various nunit targets/tasks.

```C#
protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
{
	context.Properties.Set(BuildProps.NUnitConsolePath, @"packages\NUnit.ConsoleRunner.3.6.0\tools\nunit3-console.exe");
}

protected override void ConfigureTargets(ITaskContext session)
{
	session.CreateTarget("unit.tests1")
        .SetDescription("Runs unit tests")
        .AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests"));
		
    session.CreateTarget("unit.tests1")
         AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests2"));
}
```

If nunit console path would not be set in build properties you would have to set it in each task separately.

like so:
```C#
protected override void ConfigureTargets(ITaskContext session)
{
    session.CreateTarget("unit.tests1")
        .SetDescription("Runs unit tests")
        .AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests")
            .NunitConsolePath(@"packages\NUnit.ConsoleRunner.3.6.0\tools\nunit3-console.exe"));
			
    session.CreateTarget("unit.tests1")
		.AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests2").
			NunitConsolePath(@"packages\NUnit.ConsoleRunner.3.6.0\tools\nunit3-console.exe"));
}
```

<a name="Predefined-build-properties"></a>

#### Predefined build properties

 Some build properties are already defined. You can access them through interface:
  
` context.Properties.Get(PredefinedBuildProperties.OsPlatform);`

Available predefined build properties:

* OsPlatform
* PathToDotnetExecutable
* UserProfileFolder
* OutputDir 
* ProductRootDir

All of them can be overriden.

<a name="Script-arguments"></a>

## **Pass command line arguments, settings from json configuration file or environment variables to your build script properties.**

 You can pass command line arguments, settings from json configuration file or environment variables to your build script properties by adding FromArg attribute to property. 

```C#
public class SimpleScript : DefaultBuildScript
{
    [FromArg("sn", "If true app is deployed on second node. Otherwise not.")]
    public bool deployOnSecondNode { get; set; }        

    protected override void ConfigureTargets(ITaskContext context)
    {
        context.CreateTarget("Deploy.Exapmle")
            .AddTask(x => x.FlubuWebApiTasks().GetTokenTask("user", "pass").SetWebApiBaseUrl("noade1Url"))
            .AddTask(x => x.FlubuWebApiTasks().UploadPackageTask("packageDir", "*.zip"))
            .AddTask(x => x.FlubuWebApiTasks().ExecuteScriptTask("Deploy", "DeployScript.cs"))
            .Group(target =>
            {
                target.AddTask(x => x.FlubuWebApiTasks().GetTokenTask("user", "pass").SetWebApiBaseUrl("noade2Url"))
                      .AddTask(x => x.FlubuWebApiTasks().UploadPackageTask("packageDir", "*.zip"))
                      .AddTask(x => x.FlubuWebApiTasks().ExecuteScriptTask("Deploy", "DeployScript.cs"));
            },
            when: c => deployOnSecondNode);         
    }
}
```

First parameter in FromArg attribute is the argument key. Second is the help description of the property shown in flubu runner. You actually don't need to put attribute on property. If u dont then the key is the same as property name and help is not shown for property in build script runner.

Property types that are supported: string, boolean, int, long, decimal, double, DateTime.

<a name="Command-line-argument"></a>

### **Passing command line argument to build script property.**

 `Dotnet flubu Deploy.Example -sn=true`

<a name="json-configuration-file"></a>

### **Passing setting from json configuration file to build script property**

 * Create file FlubuSettings.json where Flubu runner is located.
 * Add argument key and value to file in json format.
 * For above example json file would look like this:
	```json
	 {
		"sn" : true,
		"SomeOtherKey" : "SomeOtherValue"
	 } 	
	```
* It's typical to have different configuration settings for different environments for example development, testing, and production. Just create different json files `FlubuSettings.{Environment}.Json` and [set enviroment variable](https://andrewlock.net/how-to-set-the-hosting-environment-in-asp-net-core/) 'ASPNETCORE_ENVIRONMENT' on desired machine 
* You can also create json configuration file by machine name `FlubuSettings.{MachineName}.Json`. If MachineName in file matches the machine name Flubu will automatically read settings from that file.

<a name="enviroment-variable"></a>

### **Passing enviroment variable to build script property**

You can also set script arguments through environment variables. environment variables must have prefix `flubu_`

For above example you would add environment variable from windows command line with the following command: `set flubu_sn=true`

<a name="Arguments-pass-through-to-tasks"></a>

## **Pass console arguments, settings from json configuration file, environment variables with ForMember to tasks.**

There is an alternative more sophisticated way to pass console arguments, settings and environment variables to tasks

```C#
protected override void ConfigureTargets(ITaskContext context)
{
   context.CreateTarget("compile")
       .AddTask(x => x.CompileSolutionTask()
           .ForMember(y => y.SolutionFileName("someSolution.sln"), "solution", "The solution to build."));
}
```

* First parameter is the method or property argument that will be passed through. values set in method parameters are default values if argument is not specified when running the build script.
* Second parameter is the argument key.
* Third optional parameter is help that will be displayed in detailed target help. If parameter is not set then default generated help will be displayed.

 `Dotnet flubu compile -solution=someothersolution.sln`

<a name="Referencing-other-assemblies-in-build-script"></a>



<a name="Build-system-providers"></a>

## **Build system providers** 

You can acces various build, commit... information for various build systems (such as Jenkins, TeamCity, AppVeyor, Travis...) 

```C#
protected override void ConfigureTargets(ITaskContext context)
{
    bool isLocalBuild = context.BuildSystems().IsLocalBuild;
    var gitCommitId = context.BuildSystems().Jenkins().GitCommitId;
}
```

<a name="Before-After"></a>

## **Build events**

- OnBuildFailed event:

```c#
public class BuildScript : DefaultBuildScript
{
    protected override void OnBuildFailed(ITaskSession session, Exception ex)
    {
    } 
}
```
 
- before and after target execution events:

```c#
protected override void BeforeTargetExecution(ITaskContext context)
{
}

protected override void AfterTargetExecution(ITaskContext context)
{
}
```    

- before and after build execution events:

```c#
protected override void BeforeBuildExecution(ITaskContext context)
{
}

protected override void AfterBuildExecution(ITaskSession session)
{
}
```
<a name="partial-class"></a>

## **Partial and base class in script**

Partial and base classes are loaded automatically if they are located in the same directory as buildscript. Otherwise they have to be added with [Include attribute](../referencing-external-assemblies#adding-other-cs-files-to-script). # Getting started with FlubuCore

## Getting started .NET core
-------
<a name="Requirements-.net-core"></a>

<a name="Installation-.net-core"></a>
#### Installation .NET core

-   Add new project to solution e.g. BuildScript
-   Add **[FlubuCore]** reference to project with NuGet

##### Or Install with FlubuCore template

- In console navigate where your solution is located.
- Run `dotnet new -i FlubuCore.Template`
- Run `dotnet new FlubuCore`
- This will add BuildScript.csproj with FlubuCore references and FlubuCore script template


<a name="Write-and-run-your-first-build-script-in-.net-core"></a>
#### Write and run your first build script in .NET core


Add BuildScript.cs file to buildscript projetct and add following code.

Following code adds compile target to flubu commands. Compile target compiles the solution.

```C#
public class MyBuildScript : DefaultBuildScript
{
	protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
    {
		context.Properties.Set(BuildProps.CompanyName, "Flubu");
        context.Properties.Set(BuildProps.CompanyCopyright, "Copyright (C) 2010-2016 Flubu");
        context.Properties.Set(BuildProps.ProductId, "FlubuCoreExample");
        context.Properties.Set(BuildProps.ProductName, "FlubuCoreExample");
    }
	
    protected override void ConfigureTargets(ITaskContext session)
    {
        var compile = context.CreateTarget("compile")
			.SetDescription("Compiles the solution.")
            .AddCoreTask(x => x.Build("FlubuExample.sln"));
    }
}
```

<a name="Run-build-script-Core"></a>
#### Run build script in .NET core with dotnet CLI tool

- Add [dotnet-flubu] as Dotnet tool to csproj or xproj(project.json). No need if u installed FlubuCore with template

csproj:
```xml
<ItemGroup>
    <DotNetCliToolReference Include="dotnet-flubu" Version="1.7.0" />
</ItemGroup>
```
project.json:
```json
"tools": {
        "dotnet-flubu": {
            "version": "1.7.0"          
        }
    }
```

- Run `dotnet restore`. This command will restore dotnet-flubu package and add it to dotnet tool commands.

- Run `dotnet flubu help`. There you will see besided default commands the compile command that we just added.

- Run `dotnet flubu compile` This command will compile your solution.

<a name="Run-build-script-core-with-global-tool"></a>
#### Run build script in .NET core with global tool

- .net core sdk 2.1.300 or greater must be installed.
- Install FlubuCore global tool: `dotnet tool install --global FlubuCore.GlobalTool`
- Run `flubu compile` where build script is located. It will compile your solution.

This is very basic build script just for you to see how simple it is to get you started. FlubuCore has to offer a lot of nice features. Read more about them at [Build script fundamentals] 
alternatively you can take a look at [.net core examples] and see most of main features in action. It is also recomended that you take a look at [FlubuCore interactive mode](build-script-runner-interactive.md) and [Override options in task through console](override-add-options.md) sections.

## Getting started .NET
-------
#### Requirements .NET

Build script project where FlubuCore is referenced must target .NET framework 4.62 or greater. If this is not possible you can use [Flubu] version 2.64 or less which only requires .NET Framework 4.0. To run build script with FlubuCore runner .net runtime 4.0 or greater is required.

<a name="Installation.net"></a>
#### Installation .NET

-   Add new project to solution e.g. BuildScript
-   Add **[FlubuCore.Runner]** reference to project with nuGet. This will add reference To FlubuCore.dll, add BuildScript.cs (build script template) to project and it will also add flubu.exe for running the buildscript.

<a name="write-and-run"></a>
#### Write and run your first build script in .NET

Modify BuildScript.cs with the following code. Change solution name to yours.

Following code adds compile target to flubu commands. Compile target compiles the solution.

```C#   
using FlubuCore.Context;
using FlubuCore.Scripting;

public class BuildScript : DefaultBuildScript
{
	protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
    {
		context.Properties.Set(BuildProps.ProductId, "FlubuExample");
        context.Properties.Set(BuildProps.ProductName, "FlubuExample");
        context.Properties.Set(BuildProps.SolutionFileName, "FlubuExample.sln");
        context.Properties.Set(BuildProps.BuildConfiguration, "Release");
    }

    protected override void ConfigureTargets(ITaskContext session)
    {
        var compile = session.CreateTarget("compile")
         .SetDescription("Compiles the solution.")
         .AddTask(x => x.CompileSolutionTask());
    }
}
```

<a name="run-build-script"></a>
#### Run build script 

- Open cmd and navigate to buildscript project directory.

- Run flubu.exe help. There you will see besides default commands the compile command that we just added.

- Run flubu.exe compile. It will compile your solution.

This is very basic build script just for you to see how simple it is to get you started. FlubuCore has to offer a lot of nice features. Read more about them at [Build script fundamentals] 
alternatively you can take a look at [.net examples] and see most of main features in action. 

<a name="Getting-started-.net-core"></a>


  [csproj.png]: https://bitbucket.org/repo/Bnjqgy/images/3977856142-csproj.png
  [projectjson.png]: https://bitbucket.org/repo/Bnjqgy/images/2485583270-projectjson.png
  [Flubu examples]: https://github.com/flubu-core/examples
  [Build script fundamentals]: buildscript-fundamentals.md
  [.net examples]: https://github.com/flubu-core/examples/blob/master/MVC_NET4.61/BuildScripts/BuildScript.cs
  [.net core examples]: https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScript.cs
  [Flubu]: https://www.nuget.org/packages/Flubu
  [FlubuCore]: https://www.nuget.org/packages/FlubuCore
  [FlubuCore.Runner]: https://www.nuget.org/packages/FlubuCore.Runner/
  [dotnet-flubu]: https://www.nuget.org/packages/dotnet-flubu/# FlubuCore
[![Windows Build](http://lucidlynx.comtrade.com:8080/buildStatus/icon?job=FlubuCore)](http://lucidlynx.comtrade.com:8080/login?from=%2F)
[![Travis](https://img.shields.io/travis/dotnetcore/FlubuCore.svg?branch=maste&?style=flat-square&label=linux-build)](https://travis-ci.org/dotnetcore/FlubuCore)
[![NuGet Badge](https://buildstats.info/nuget/flubucore)](https://www.nuget.org/packages/FlubuCore/)
[![Gitter](https://img.shields.io/gitter/room/FlubuCore/Lobby.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Twitter](https://img.shields.io/badge/twitter-flubucore-brightgreen.svg?logo=twitter)](https://twitter.com/FlubuC)
[![Member project of .NET Core Community](https://img.shields.io/badge/member%20project%20of-NCC-9e20c9.svg)](https://github.com/dotnetcore)
[![License](https://img.shields.io/github/license/dotnetcore/FlubuCore.svg)](https://github.com/dotnetcore/FlubuCore/blob/master/LICENSE)

## **Introduction**
"FlubuCore - Fluent Builder Core" is a cross platform build and deployment automation system. You can define your build and deployment scripts in C# using an intuitive fluent interface. This gives you code completion, IntelliSense, debugging, FlubuCore custom analyzers, and native access to the whole .NET ecosystem inside of your scripts.

![FlubuCore in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/demo.gif)

FlubuCore offers a .net (core) console application that uses power of roslyn to compile and execute scripts. Above example can be run from console with:

* FlubuCore runner  ``` flubu.exe Default ```
* FlubuCore dotnet cli tool ``` dotnet flubu Default ```
* FlubuCore global tool ``` flubu Default ```

## **Features and Advantages**

* Intuitive an easy to learn. C#, fluent interface, and IntelliSense make even most complex script creation a breeze.

```c#
context.CreateTarget("Example")
  .DependsOn(fetchBuildVersionTarget)
  .AddTask(x => x.CompileSolutionTask())
  .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
      .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);
```
          
* [Large number of often used built-in tasks](https://flubucore.dotnetcore.xyz/tasks/) like e.g. running tests, managing IIS, creating deployment packages, publishing NuGet packages, docker tasks, executing PowerShell scripts and many more.

```c#
context.CreateTarget("build")
   .AddTask(x => x.GitVersionTask())
   .AddTask(x => x.CompileSolutionTask("MySolution.sln").BuildConfiguration("Release");

context.CreateTarget("run.tests")
   .AddTask(x => x.XunitTaskByProjectName("MyProject").StopOnFail())
   .AddTask(x => x.NUnitTask(NunitCmdOptions.V3, "MyProject2").ExcludeCategory("Linux"))
   .AddCoreTask(x => x.CoverletTask("MyProject.dll"));
```

* [Execute your own custom C# code.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Custom-code)

```c#
context.CreateTarget("MyCustomBuildTarget")
     .AddTask(x => x.CompileSolutionTask())
     .Do(MyCustomMethod)
     .Do(NuGetPackageReferencingExample);
```

* [assembly references and nuget packages are loaded automatically](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Referencing-other-assemblies-in-build-script) when script is used together with project file. When script is executed alone (for example when deploying with FlubuCore script on production environment) references can be added with attributes.

```c#
[NugetPackage("Newtonsoft.json", "11.0.2")]
[Assembly(".\Lib\EntityFramework.dll")]
public class BuildScript : DefaultBuildScript
{
   public void NuGetPackageReferencingExample(ITaskContext context)
    {
        JsonConvert.SerializeObject("Example");
    }
}
```

* [Easily run any external program or console command in your script.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Run-any-program)

```c#
 public class SimpleScript : DefaultBuildScript
 {
	protected override void ConfigureTargets(ITaskContext context)
    {
		context.CreateTarget("Run.Libz")
		.AddTask(x => x.RunProgramTask(@"packages\LibZ.Tool\1.2.0\tools\libz.exe")
			.WorkingFolder(@".\src")
			.WithArguments("add")
			.WithArguments("--libz", "Assemblies.libz"));
	}
 }
```

* [Pass command line arguments, settings from json configuration file or environment variables to your script.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Script-arguments)

```c#
 public class SimpleScript : DefaultBuildScript
 {
    [FromArg("sn", "If true app is deployed on second node. Otherwise not.")]
    public bool deployOnSecondNode { get; set; }

 
     protected override void ConfigureTargets(ITaskContext context)
     {
         context.CreateTarget("compile")
            .AddTask(x => x.CompileSolutionTask()
                .ForMember(y => y.SolutionFileName("someSolution.sln"), "solution", "The solution to build.")); 
     }
 }
```
 
```
  flubu.exe compile -solution=someOtherSolution.sln -sn=true
```

* [Extending FlubuCore fluent interface by writing your own tasks within FlubuCore plugins.](https://flubucore.dotnetcore.xyz/write-plugins)

```c#
    public class ExampleFlubuPluginTask : TaskBase<int, ExampleFlubuPluginTask>
    {
        protected override int DoExecute(ITaskContextInternal context)
        {
            // Write your task logic here.
            return 0;
        }
    }
```

* [Growing list of FlubuCore plugins complements built in tasks.](https://flubucore.dotnetcore.xyz/AwesomePlugins/awesome-plugins/)

* [Asynchronous execution of tasks, target dependencies and custom code.](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Async-execution)

```c#
    context.CreateTarget("Run.Tests")
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName3"));
```

* [Override existing options or add additional options to tasks through console](https://flubucore.dotnetcore.xyz/override-add-options/)

   ```c#
  context.CreateTarget("Example")`
      .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 
   ``` 

  `flubu example --configuration=Debug`

   flubu would execute `dotnet build MySolution.sln --configuration Debug`
   
* [Full .NET Core support including the global CLI tool](https://flubucore.dotnetcore.xyz/getting-started#getting-started-net-core)

```
    dotnet tool install --global FlubuCore.GlobalTool
    flubu compile
```

* [Possibility to test and debug your build scripts.](https://flubucore.dotnetcore.xyz/Tests-debugging)

```c#
    context.WaitForDebugger();
```

* [Easily automate deployments remotely via the FlubuCore Web API.](https://flubucore.dotnetcore.xyz/WebApi/getting-started/)

* [Possibility to use FlubuCore tasks in any other .NET application.](https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs)

* [FlubuCore interactive mode](https://flubucore.dotnetcore.xyz/build-script-runner-interactive/) which offers target tab completition, options tab completition, toogle targets/options, executed commands history. It is also possible to execute external commands and operable programs. For some of them FlubuCore offers tab completion with help displayed at the bottom of console out of the box(such as dotnet, git..)  

![FlubuCore interactive mode](https://raw.githubusercontent.com/dotnetcore/flubu.core/master/assets/FlubuCore_Interactive_mode_full.gif)

* Improved developer experience with FlubuCore custom analyzers.

![FlubuCore analyzers in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCoreCustomAnalyzerDemo.png)

## **Getting Started**
Using FlubuCore is straightforward and very simple :-) It is also fully and throughly documented.

The [Getting Started](https://flubucore.dotnetcore.xyz/getting-started/) chapter in [Documentation](https://flubucore.dotnetcore.xyz) will help you set up your first FlubuCore build in no time.

A comprehensive list of features that FlubuCore has to offer with descriptions can be found in the [Build Script Fundamentals](https://flubucore.dotnetcore.xyz/buildscript-fundamentals) chapter.

Once you have your build and deployment scripts defined, the following Wiki chapters will explain how to run them:

* For .NET Framework projects use [FlubuCore.Runner](https://flubucore.dotnetcore.xyz/getting-started#Installation.net)

* For .NET Core projects use [FlubuCore CLI global tool](https://flubucore.dotnetcore.xyz/getting-started#Installation-.net-core)

## **Examples**
Aside from the detailed Wiki FlubuCore comes with example projects that reflect real-life situations. The examples can be found in the separate [Examples repository](https://github.com/flubu-core/examples/).

These examples will help you to get quickly start with FlubuCore:
* [.NET Framework build example](https://github.com/flubu-core/examples/blob/master/MVC_NET4.61/BuildScripts/BuildScript.cs
) - Example covers versioning, building the project, running tests, packaging application for deployment.

* [.NET Core build example](https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScript.cs
) - Example covers versioning, building the project, running tests, packaging application for deployment.

* [Deployment script example](https://github.com/flubu-core/examples/blob/master/DeployScriptExample/BuildScript/DeployScript.cs
) - Example shows how to write simple deployment script. 


* [Open source library example](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCoreOpenSource/Build/BuildScript.cs) - Example covers versioning, building the project, running tests and publishing nuget package. It also covers how to run build script on Appveyor and Travis CI.

## **Have a question?**

 [![Join the chat at https://gitter.im/FlubuCore/Lobby](https://badges.gitter.im/mbdavid/LiteDB.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## **Contributing**

Please see [CONTRIBUTING.md](https://github.com/dotnetcore/FlubuCore/blob/master/CONTRIBUTING.md).

## **Ways to Contribute**

* Spread the word about the project.
* If you like the project don't forget to give it a star so that the community get's bigger.
* Improve documentation.
* Report, fix a bug.
* Implement a new feature.
* Discuss potential ways to improve project.
* Improve existing implementation, performance, etc.

## Further Development
If you find FlubuCore useful (you feel it helps you on the daily basis) you can support further development by buying us a coffee (or become a backer or sponsor). Sometimes it's hard to stay awake till midnight implementing new features, coffee helps us with that. We would really appreciate your support. Money from sponsorship will also be used for the promotion of the project. If you are a backer or a sponsor you can also request for a new feature or ask for support. These issues will be handled with highest priority.

[![](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/NCOpMkt)

### Backers and Sponsors
[![OpenCollective](https://opencollective.com/flubucore/backers/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12502) 
[![OpenCollective](https://opencollective.com/flubucore/sponsors/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12503)


## **Changelog and Roadmap**

Changes with description and examples can be found in [Changelog.](https://github.com/flubu-core/flubu.core/blob/master/CHANGELOG.md) 
 
You can see FlubuCore roadmap by exploring opened [Milestones.](https://github.com/flubu-core/flubu.core/milestones)
FlubuCore offers you to add or override options in **all** tasks that run external processes. 

Let's say you have target
```c#
context.CreateTarget("Example")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 

```

and you wan't to build solution in debug configuration.
You could just write in console

`flubu example --configuration=Debug`

flubu would execute 

`dotnet build MySolution.sln --configuration Debug`

!!! info "Note"
	option keys are the same as in external processes. short versions of options keys also work. So in above example `-c=debug` would also work.
	
	FlubuCore also support tab completion for all options in tasks that run's external processes in [Interactive mode](build-script-runner-interactive.md)

<br/>

Tasks in FlubuCore plugins that does not support overriding of options out of the box can still be overriden with special prefix before option key `/o:`

`/o:{external_process_option={value}` 

With `/o:` FlubuCore adds specified option to all tasks in target's which can be a problem if target execute multiple tasks. So instead of `/o:`  you can use prefix by task name 

`/{taskName}:{external_process_option}={value}`  

Alternatively you can change default prefix on task

```c#
    context.CreateTarget("Publish")
        AddCoreTask(x => x.Publish()
            .ChangeDefaultAdditionalOptionPrefix("/p:"));
```

#### Example

Build task does support overriding of options out of the box but for the simplicity of the example build task is used.

```c#
context.CreateTarget("Example")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 
```

and you wan't to build solution in debug configuration.
You could just write in console

`flubu example /o:configuration=Debug`

or
`flubu example /o:c=Debug`

or
`flubu example /build:c=Debug`

flubu would execute 

`dotnet build MySolution.sln -c Debug`
## **Referencing external assemblies in build script**

FlubuCore loads all assemblies references and nuget packages automatically from build script csproj. Csproj must be at on of the location specified [here](https://github.com/flubu-core/flubu.core/blob/master/FlubuCore/Scripting/Analysis/ProjectFileAnalyzer.cs) If not assembly and nuget references will not be loaded automatically when executing script.

!!! Note
	You can also disable referencing assemblies and nuget packages from build script by adding attribute to build script.

	```C#
	[DisableLoadScriptReferencesAutomatically]
	public class BuildScript : DefaultBuildScript
	{
	}
	```

Alternatively when you are running scripts without csproj(for example deploy scripts) external references can be added  with directives in three ways:

<a name="By-assembly-relative-or-full-path"></a>

### **By assembly relative or full path**

On the build script class you have to add attribute:

```C#
[Assembly(@".\packages\Newtonsoft.Json.9.0.1\lib\net45\Newtonsoft.Json.dll")]
public class BuildScript : DefaultBuildScript
{
    public void ReferencedAssemlby(ITaskContext context)
    {
       JsonConvert.SerializeObject("Example");
    }
}
```
FlubuCore can also load all assemblies from specified directory and optionaly from it's subdirectories

```C#
[AssemblyFromDirectory(@".\Packages", true)]
public class BuildScript : DefaultBuildScript
{
}
```

<a name="Referencing-nuget-packages"></a>

### **Referencing nuget packages**

Flubu supports referencing nuget packages. .net core sdk or msbuild must be installed if u want to reference nuget packages otherwise they will not get restored.

You have to add NugetPackage attribute on the script class:

```C#
[NugetPackage("Newtonsoftjson", "11.0.2")]
public class BuildScript : DefaultBuildScript
{
    public void ReferencedNugetPackage(ITaskContext context)
    {
       JsonConvert.SerializeObject("Example");
    }
}
```

<a name="Load-assembly-by-assembly-full-name"></a>

### **Load assembly by assembly full name**

System assemblies can be loaded by fully qualifed assemlby name.

You have to add Reference attribute on the script class:

```C#
[Reference("System.Xml.XmlDocument, System.Xml, Version=4.0.0.0, Culture=neutral, publicKeyToken=b77a5c561934e089")]
public class BuildScript : DefaultBuildScript
{
    public void ReferencedAssemlby(ITaskContext context)
    {
		XmlDocument xml = new XmlDocument();
    }
}
```

One way to get fully qualifed assembly name:

    var fullQualifedAssemblyName = typeof(XmlDocument).Assembly.FullName;

<a name="Load-all-assemblies-from-directory"></a>

### **Load all assemblies from directory**
Even if you are not using your script together with csproj flubu can load all external assemblies for you automatically from directory (assemblies in subdirectories are also loaded ). 

By default flubu loads all assemblies from directory FlubuLib. Just create the directory at the flubu runner location and put assemblies in that directory. You can specify directory in flubu runner from where to load assemblyes also:

`flubu.exe -ass=somedirectory`

`dotnet flubu -ass=somedirectory`
alternatively you can put ass key into flubusettings.json file:

    {
      "ass" : "someDirectory",
      "SomeOtherKey" : "SomeOtherValue"
    }` 

<a name="Adding-other-cs-files-to-build-script"></a>

## **Adding other .cs files to script**

Other .cs files have to be added through attribute they are not automatically loaded from buildscript project file.
Exception are build script base classes and partial classes they are loaded automatically.

```C#
[Include(@".\BuildHelper.cs")]
public class BuildScript : DefaultBuildScript
{
    public void Example(ITaskContext context)
    {
        BuildHelper.SomeMethod();
    }
}    
```

FlubuCore can also load all .cs files to script from specified directory and optionaly from it's subfolders.

```C#
[IncludeFromDirectory(@".\Helpers", true)]
public class BuildScript : DefaultBuildScript
{
}
```Here you can find list of FlubuCore built in tasks with short description. Each task have fluent interface. See code documentation for detailed task documentation. If u have any questions about a task join us on gitter.

### **Tasks** 

| Task name | Description |
| --- | ----------- |
|RunProgramTask|Task runs specified external program|
|CompileSolutionTask|Task compiles specified solution.|
|PackageTask|Task Packages specified directories and files into specified directory or zip file..|
|FetchBuildVersionFromFileTask|Task fetches build version from file.|
|GitVersionTask| GitVersion is a tool to help you achieve Semantic Versioning on your project. [[ Documentation |https://gitversion.readthedocs.io/en/latest/]]
|FetchVersionFromExternalSourceTask|Task fetches build version from external source(Appveyor, travis, jenkins...).|
|GenerateCommonAssemlbyInfoTask|Task generates common assembly info for solution|
|NUnitTask|Task runs nunit tests with nunit.exe runner|
|XunitTask|Task runs xunit tests with xunit.exe runner|
|NUnitWithDotCoverTaskTask | runs nunit tests in combination with dotCover test coverage analysis|
|PublishNugetPackageTask|Task publishes nuget package to specified nuget server |
|NugetCmdLineTask| Manipulate nugets with nuget.exe  |
|UpdateXmlFileTask|Updates an XML file using the specified update commands. |
|UpdateJsonFileTask|Task updates an JSON file using the specified update commands.|
|CleanoutputTask|Task clean all projects outputs in solution.|
|ControlServiceTask|Control windows service with sc.exe command.|
|CreateWindowsServiceTask|Creates windows service with sc.exe command.|
|ExecutePowerShellScriptTask|Executes specified power shell script.|
|SqlCmdTask| Execute SQL script files with sqlcmd.exe |
|CreateAppPoolTask|Task creates new application pool in iis.|
|ControlAppPoolTask|Task can start/stop application pool.|
|DeleteAppPoolTask|Task deletes specified application pool.|
|CreateWebApplicationTask|Task creates new web application for specified web site in iis.|
|CreateWebSiteTask|Task creates new web site in iis.|
|AddWebSiteBindingTask|Task compiles specified solution.|
|GetLocalIisVersionTask|Task gets the version on iis on local machine.|
|ReplaceTokenTask|Task Replaces specified tokens in file.|
|ReplaceTextTask|Task Replaces specified texts in file.|
|CopyDirectoryStructureTask|Task copies files from one directory to another with specified filters. |
|CopyFileTask|Task copies file from from one directory to another.|
|CopyDirectoryStructureTask| Copies a directory tree from the source to the destination..|
|CreateDirectoryTask|Task creates directory at specified location.|
|DeleteDirectoryTask|Task deletes specified directory.|
|DeleteFilesTask|Task delete files from specified directory matching specified pattern.|
|UnzipFileTask|Task unzips specified zip file to specified location.|
|ZipFileTask|Task zips specified files.|
|OpenCoverTask|Task runs open cover tool.|
|OpenCoverToCoberturaTask|Task runs open cover to cobertuta tool.|
|CoverageReportTask|Task runs the coverage report generator tool.|
|LoadSolutionTask|Task load's solution information to the flubu session.|
|T4TemplateTask|Generate T4 template with TextTransform.exe utility..|
|GitTasks|Git Clone, Add, Commit, Pull, Push, Tag, RemoveFiles tasks.|
|DockerTasks|Build, Run, Stop Remove Container, Remove Image and all other tasks for coresponding docker cli commands. All tasks are genereated from offical docker documentation. |
|FlubuWebApiTasks|Various flubu web api client tasks.|

### **.net core Tasks** 
| Task name | Description |
| --- | ----------- |
|ExecuteDotnetTask|Executes specified dotnet command.
|DotnetRestoreTask|Restores the dependencies and tools for a given application / project..
|DotnetPublishTask|compiles the application, reads through its dependencies specified in the project file and publishes the resulting set of files to a directory.
|DotnetBuildTask|Builds a project and all of its dependencies.
|DotnetPackTask|command builds the project and creates NuGet packages. The result of this command is a NuGet package.
|DotnetNugetPushTask|Pushes the nuget package to the nuget server.
|DotnetTestTask|Runs tests using a test runner specified in the project.json / csproj.
|DotnetCleanTask| Cleans the output of a project.
|DotnetToolTask| All dotnet tool commands.
|DotnetEfTasks| Various entity framework tasks.
|UpdateNetCoreVersionTask| Updates the version in csproj / project.json file
|CoverletTask| Coverlet is a cross platform code coverage library for .NET Core, with support for line, branch and method coverage [[ Documentation |https://github.com/tonerdo/coverlet]].
|SshComandLinuxTask| Runs specified command on the remote host.
|SshCopyLinuxTask|Copy projects/files to the remote host.
|SystemCtlLinuxTask|Runs system ctl.

### **Writing build script tests and debuging build script through test**

Wiki coming soon. Meanwhile see simple test to get you started: https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs

If needed you can debug build script through test.

You can use flubu task in other .net applications just like in above test example.

### **Debugging build script by attaching to running process**
You can debug build script by attaching debuger to Flubu process. 

* Because Flubu alters build script slightly you have to disable option 'Require source code files to exactly match the original version' in visual studio.
Option can be found under Tools->Options->Debugging->General->Require source code files to exactly match the original version. Not sure for VS code if any settings have to be changed.
* It is advised to use  WaitForDebugger extension method on ITaskContext before first break point

        protected override void ConfigureTargets(ITaskContext context)
        {
            context.WaitForDebugger();
        }

* Run build script and attach debugger to FlubuCore process. FlubuCore process name vary depending on which FlubuCore "runner" you are using.

	* FlubuCore.Runner - You have to attach debugger to process named flubu.exe
    * dotnet-flubu Cli tool - You have to attach debugger to right process named dotnet
	* FlubuCore.GlobalTool - You have to attach debugger to process named FlubuYou can write your own tasks for flubu and extend flubu fluent interface with them.

When fluent interface will be extended with your custom task you could simply add it to the target or execute it with Do task with the following example code:

```c# 
public class BuildScript : DefaultBuildScript
{
    protected override void ConfigureTargets(ITaskContext context)
    {
        context.CreateTarget("FlubuPlugin.Example")
           .SetAsDefault()
           .Do(DoPluginExample);

       context.CreateTarget("FlubuPlugin.Example2")
           .AddTask(x => x.ExampleFlubuPluginTask());
    }

   private void DoPluginExample(ITaskContext context)
   {
       context.Tasks().ExampleFlubuPluginTask()
           .Message("some example message from plugin").Execute(context);
   }
}
```
### **How to create your own task plugin**
* Create new project in vs FlubuCore.{PluginName}
* Add FlubuCore nuget package to project.
* Add task and implement it. Following code shows implementation of example flubu plugin task.

```c#    
public class ExampleFlubuPluginTask : TaskBase<int, ExampleFlubuPluginTask>
{
    private string _message;

    protected override string Description { get; set; }

    public ExampleFlubuPluginTask Message(string message)
    {
        _message = message;
        return this;
    }

    protected override int DoExecute(ITaskContextInternal context)
    {
        //// write task logic here.
        context.LogInfo(!string.IsNullOrEmpty(_message) ? _message : "Just some dummy code");

        return 0;
    }
}
```

* Then you need to write an extension method to add the task to flubu fluent interface. Extension method for our example task:

```C#
using FlubuCore.PluginExample;

namespace FlubuCore.Context.FluentInterface.Interfaces
{
   public static class TaskFluentInterfaceExtension
    {
        public static ExampleFlubuPluginTask ExampleFlubuPluginTask(this ITaskFluentInterface flubu)
        {
            return new ExampleFlubuPluginTask();
        }
    }
}
```

* It is recommended that you add task to ICoreTaskFluentInterface or  ITaskFluentInterface

* We would be very glad if you add your plugin to the nuget repository. It would be great if the plugin name would start 
  with FlubuCore so others can find it.

* you can see whole example plugin code [here](https://github.com/flubu-core/examples/tree/master/FlubuCustomTaskPluginAndLoadAssembliesFromDirectoryExample)
 * [FlubuCore.CakePlugin](https://github.com/flubu-core/FlubuCore.CakePlugin) - Cake have quite alot of useful addins. This plugin allows you to use any Cake addins in FlubuCore.

* [FlubuCore.Azure](https://github.com/flubu-core/FlubuCore.Azure) - Plugin adds over 2000 generated tasks for Azure CLI commands. Tasks are generated from offical documentation.

* [FlubuCore.Diff](https://github.com/flubu-core/FlubuCore.Diff) - Plugin adds Diff task to FlubuCore task fluent interface. Diff task compares 2 specified files and generates html report with differences.

* [FlubuCore.Gitter](https://github.com/flubu-core/FlubuCore.Gitter) - Plugin for sending gitter messages in specified room. 

* FlubuCore.Kubernetes - Will not be implemented. Use [Kurernetes client](https://github.com/kubernetes-client/csharp) with FlubuCore instead.

* [FlubuCore.Npm](https://github.com/flubu-core/FlubuCore.Npm) - Plugin adds tasks for numerous npm CLI commands.

* [FlubuCore.Octopus](https://github.com/flubu-core/FlubuCore.Octopus) - Plugin adds tasks for numerous octopus CLI commands.

* [FlubuCore.Slack](https://github.com/flubu-core/FlubuCore.Slack) - Plugin for sending message to slack channels.

* [FlubuCore.Chocolatey](https://github.com/flubu-core/FlubuCore.Chocolatey) - Plugin adds tasks for numerous Chocolatey CLI commands. Chocolatey is a software management solution unlike anything else you've ever experienced on Windows. It focuses on simplicity, security, and scalability. You write a software deployment in PowerShell once for any software (not just installers), then you can deploy it everywhere you have Windows with any solution that can manage systems (configuration management, endpoint management, etc) and track and manage updates of that software over time.


## **About**
With FlubuCore web api you can execute FlubuCore scripts remotely. Mainly it is meant to automate deployment of .net or .net core applications from your build server to different environments but it can be used for any other FlubuCore script execution.

Web Api supports:

- Executing flubu scripts on the server where web api is deployed.
- Uploading (deploy or any other) packages to the server where web api is deployed.
- Deleting packages from server where web api is deployed.
- Sending reports back to client.
- Uploading FlubuCore scripts to the server where web api is deployed.
- Automatic updates
- Manual target execution through FlubuCore web app(deployed together with web api)

In this getting started tutorial we will:

- Deploy FlubuCore web api to the server.
- Write .net deployment script that will deploy mvc example application on the sever. You should go through this tutorial even if you want to use FlubuCore.WebApi for .net core application deployment. There are few small differences between using FlubuCore.WebApi for deploying .net core applications and .net applications. All differences are written in this tutorial.
- Write build script that will upload deployment package of the example application to the server and execute deployment script that we wrote.
- Run deployment script through build script remotely.

<a name="requirements"></a>
### **Requirements**

- .net 462+ runtime or .net core runtime installed on the server. Depending on which build of FlubuCore.WebApi you plan to use.

<a name="Web-api-deployment"></a>
### **Web api deployment**

- Get appropriate web api deploy package from https://github.com/flubu-core/flubu.core/releases.
- Copy web api deployment package to the server where you want to execute flubu script.
- Unzip the package.
- Set web api deployment configuration settings in the unzipped DeploymentConfig.json file. More about specific deployment config settings can be found in the configuration file.
- On windows server run deploy.bat to deploy the web api
- On linux/mac server run: dotnet restore and after that: dotnet flubu -s=deploymentscript.cs
- On deployed location run dotnet FlubuCore.WebApi.dll to selfhost web api. You can of course also host it for example on iis...

#### IIS deployment
 How to deploy asp .net core application see: https://docs.microsoft.com/en-us/aspnet/core/publishing/iis?tabs=aspnetcore2x

Some actions might need administration rights like starting / stoping the application pool. If that's the case u have to change identity on the application pool where you hosted the web api. Go to Application pools -> Web api app pool -> Advanced settings -> process model -> Identity and change to user which has admin rights.

<a name="Write-deploy-script"></a>
### **Write deploy script**
Example .net  deploy script can be found [Here](https://github.com/flubu-core/examples/blob/master/DeployScriptExample/BuildScript/DeployScript.cs). If u want to try the example the best way is to just clone the flubu core examples directory. Deploy script for .net core application would be of course slightly different.

Example deploy script for .net application will

 - Create iis application pool if it doesnt exists
 - Stop the application pool
 - Unzip package from /packages directory(which will be uploaded to web api with build script)
 - Copy unziped application to new folder where it is/will be hosted.
 - Create web site on iis for example web application
 - Start the application pool

When you finish writing your deploy script manually copy it to web api deployed location /scripts folder. Web api can also upload scripts but it is disabled by default for obvious security reason. It should stay disabled in most cases.

If needed modify Example DeployScript for your needs.

<a name="Write-build-script"></a>
### **Write build script**
   Example .net build script can be found [here](https://github.com/flubu-core/examples/blob/master/DeployScriptExample/BuildScript/BuildScript.cs)
   
Example .net build script will

 - Get the authentication token
 - Delete old packages from /packages folder on web api.
 - Upload package to web api /packages folder
 - Execute Deployment script in /scripts folder that we manually uploaded

If needed modify Example BuildScript for your needs.

<a name="Run-deploy-script"></a>
### **Run deploy script**
If u cloned example repository just execute at the root foolder:

 `dotnet restore buildscript.csproj ` and `dotnet flubu deploy -s=buildscript\buildscript.cs` in cmd from DeployScriptExample folder

In real case scenario you would probably deploy from your build server after sucesfull build, after merge to release branch, manually execute the job on build server...  

<a name="Security"></a>
### **Security** 
As attacker can do alot of damage if he gains access to web api next security measures should be implemented if possible:

* If possible Flubu web api should not be publicly accessible.
* Always host web api on https.
* Restrict access by ip(config).
* Restrict access by time frame(config). This security measure should be taken if you deploy your application always at same time e.g 11pm. Then time frame when api can be accessed should be set for example from 11pm to 11.15pm,
* Use very strong password(web api user creation).
* Do not disable feature "Restrict access on failed login"(config).
* Enable email notifications when GetToken/Script is executed on api(config).

For detailed description of security settings see appsettings.json file on web api.

<a name="Automatic-update"></a>
### **Automatic update**

You can automatically update FlubuCore web api if new version is available. Just navigate to /UpdateCenter (not /api/UpdateCenter)

<a name="manual-target-execution"></a>
### **Manual target execution remotely through FlubuCore web app**

You can manually execute target through FlubuCore web app. Just navigate to /Script挡在控制台中执行 FlubuCore 脚本或其他本地程序时，建议在 FlubuCore 交互模式下运行，它将带给你一些非常有意思的功能，这些功能已在[功能一节](#功能)中列明。只需要在你常用的卡侬值台程序中运行 `flubu -i` 便可进入 FlubuCore 交互模式。

## **演示**

![交互模式](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCore_Interactive_mode_full.gif)

 *在演示中[构建脚本](https://gist.github.com/mzorec/c2e0d0572ed023f1d3ebbe72cb5903fc)。*

## **功能**

交互模式下的功能

- 使用「tab 键」来完成 Target 选项卡
- 使用「tab 键」来完成 Option 选项卡
- Option's (parameter) value tab completition with tab key for enum types
- 在控制台底部显示 Target 帮助
- 在控制台底部显示 Option 帮助
- 执行外部命令。这意味着如果在 PowerShell 中运行 FlubuCore 交互模式，则所有 PowerShell 命令都可以在 FlubuCore 的交互模式中使用。
- 执行外部程序。对于其中部分程序，FlubuCore 交互模式提供 Tab 键自动补全（比如 dotnet、git 等，[查看完整列表](通过-Tab-键补全完成的外部程序列表)）
- 使用「↑ 键」和「↓ 键」来切换 Target 选项卡
- 使用「↑ 键」和「↓ 键」来切换 Option 选项卡
- Next / previos target or option with tab key
- 使用「↑ 键」和「↓ 键」来切换命令的历史记录
- 无需为每个命令加载脚本
- 重新加载当前脚本，或加载另一个脚本
- 在文件夹间切换

## **内部命令**

- `cd` 变更目录。
- `dir` 列出文件和目录。
- `l|load -s={script}` 加载另一个 FlubuCore 脚本。
- `r|reload` 重新加载当前脚本。
- `e|q|exit|quit` 退出 FlubuCore 交互模式。

## **热键**

FlubuCore 支持以下热键：

- 「回车键」执行命令
- 「Tab 键」提示用户完成 target/option 输入
- 「↑ 键」在历史记录中选择上一条命令
- 「↓ 键」在历史记录中选择下一条命令
- 「← 键」光标左移
- 「→ 键」光标右移
- 「Backspace 键」删除光标前的一个字符
- 「Delete 键」删除光标后的一个字符
- 「Home 键」光标跳转到用户输入的开头处
- 「End 键」光标跳转到用户输入的结尾处

## 通过 Tab 键补全完成的外部程序列表

在 FlubuCore 交互模式中通过 Tab 键来补全完成 options/switches 的外部程序列表。计划在近期添加对 docker、octopus、azure、npm 和 chocolatey 命令的支持。

- dotnet build
- dotnet test
- dotnet pack
- dotnet publish
- dotnet nuget push
- dotnet restore
- dotnet tool install
- dotnet tool update
- dotnet tool uniinstall
- git add
- git commit
- git push
- git checkout
- git clone
- git submodule
- git rm
- git tag
- gitversion
- coverlet
- sqlcmd.exe在 .NET 中，你可以通过控制台应用程序 flubu.exe 运行 flubu 构建脚本。可以通过 nuget 添加 Flubu.Runner 以便获取控制台应用程序。

在 .NET Core 中可以用 dotnet 命令或全局工具来运行 flubu 构建脚本。通过 nuget 添加 FlubuCore，将 dotnet-flubu 作为 dotnet cli 工具引入项目。至于如何将其添加为 dotnet cli 工具请移步**入门**一节。

### **如何使用**

.NET core 用法：`dotnet flubu {TargetToExecute} {Flubu options} {build script arguments}`

.NET core 全局工具的用法：`flubu {TargetToExecute} {Flubu options} {build script arguments}`

.NET 用法：flubu.exe `{TargetToExecute} {Flubu options} {build script arguments}`

#### 多目标执行

.NET core 用法：dotnet flubu {TargetToExecute} {TargetToExecute2} {TargetToExecute3...} {Options}

.NET 用法：flubu.exe {TargetToExecute} {TargetToExecute2} {TargetToExecute3...} {Options}

Target 可以和添加有 `-parallel` 选项的任务一同执行。

### **Flubu 选项**

![N/A](img/FlubuHelp.png "Flubu help")

### **帮助**

列出所有可用目标：

`flubu help`

`dotnet flubu help`

对特定目标的帮助：

`flubu {TargetName} help`

`dotnet flubu {TargetName} help`

这条命令将列出所有描述有执行目标的任务，以及哪些参数可以传递给目标（target）中的特定任务。

### Specifiying which script Flubu should run.

Easiest way is to put build script at one of the default locations (you can find list of default locations below). If it is located at one of the default locations FlubuCore will execute the script automatically `flubu {TargetName}`. 
Second option is to specify script location with -s option `flubu {TargetName} -s={pathToScriptFile}` Third option is to run `flubu setup` and specify script and csproj(optional) location in interactive mode.
 Flubu will store script and csproj location to `.flubu` file. if `.flubu` file is present FlubuCore will read location of the script and csproj file from that file. Additional benefit when storing location to `.flubu` file is 
 that you don't need to execute script at the root directory of the project. Meaning if your project is for example located at "c:\_git\myproject" you can execute script inside any subfolder of that location.

#### **默认构建脚本的位置***

- "Build.cs"

- “BuildScript.cs”

- “DeployScript.cs”

- "DeploymentScript.cs"

- "_Build/Build.cs"

- "_Build/BuildScript.cs"

- "Build/Build.cs"

- "Build/BuildScript.cs"

- "_BuildScript/BuildScript.cs"

- "_BuildScripts/BuildScript.cs"

- “BuildScript/BuildScript.cs”

- “buildscript/deployscript.cs”

- “buildscripts/buildscript.cs”

- “buildscripts/deployscript.cs”

- "BuildScript/DeploymentScript.cs"

- "BuildScripts/DeploymentScript.cs"
## **构建脚本**

每个构建脚本（build script）都继承自 DefaulBuildScript 类，因此必须实现 DefaulBuildScript 中的两个抽象方法（abstact method）。

- ConfigureTargets：用于创建将执行特定工作的新目标（targets）。

- ConfigureBuildProperties：用于设置可在多个任务和自定义 C# 代码间共享的各种构件属性（various build properties）。

空构建脚本示例：

```C#
public class BuildScript : DefaultBuildScript
{
	protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
    {
    }

    protected override void ConfigureTargets(ITaskContext session)
    {
    }
}
```

<a name="Targets"></a>

## **目标**

---

目标（target）用于按特定顺序执行特定工作。目标可执行诸如 FlubuCore 内置任务（如编译解决方案的任务）和一些自定义 C# 代码。目标也可以依赖于其他目标（other targets）。

### **创建新目标**

下例将创建在任务中执行一次构建的新目标。

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Compile")
		.SetDescription("Compiles the solution")
        .AddTask(x => x.CompileSolutionTask());
}
```

目标也可以通过方法上的特性来进行定义。

```C#
[Target("targetName", "a", "b")]
[Target("targetName2", "c", "d")]
[Target("targetName3", "e", "f")]
public void Example(ITarget target, string source, string destination)
{
	target.AddTask(x => x.CopyFileTask(source, destination, true));
}
```

你还可以通过控制台参数（console arguments）或 FlubuCore 配置文件向参数（parameter）传递值。

`Flubu targetName2 -destination=SomeOtherDestination`

<a name="Tasks"></a>

### **任务**

任务分为两种类型：（一般）任务（task）和 Core 任务。（一般）任务可以在 .NET 和 .NET Core 项目中执行，而 Core 任务只能在 .NET Core 项目中执行。

下例代码，在目标中执行了两个 Core 任务，执行顺序与代码中指定的顺序一致。

```C#
context.CreateTarget("Build")
    .AddCoreTask(x => x.Restore())
    .AddCoreTask(x => x.Build());
```

所有任务都有以下方法：

- `.OnError((c, ex) => { c.LogInfo("Example");}))` - onError 可在指定任务发生错误时执行一些自定义操作；

- `.Retry(5, 1000)` - 重试机制（Retry Mechanism）。可在该机制重试任务期间应用特定条件（specific condition）；

- `.Finally(c => { c.LogInfo("Example");}))` - Finally 就像 try-cache-finally 里的 finally 块；

- `.DoNotFailOnError()` - 脚本不会因发生异常而失败，你可为任务不失败时应用特定条件；

- `.NoLog()` - 任务日志将不会输出到控制台；
-
- `.SetDescription()` - 覆盖（overrides）任务的默认描述；

- `.ForMember()` - 将控制台参数传递给方法或属性，相关详细信息请查阅[向任务传递控制台参数、JSON 配置文件的设置，以及基于 ForMember 的环境变量](#Arguments-pass-through-to-tasks);

- 在单个任务上使用 When 从句（when cluase），使任务有条件地执行（参阅下面的任务组）：

```c#
context.CreateTarget("Example")
	.AddTask(x => x.CompileSolutionTask())
    .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
    .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);
```

- 当且仅当满足指定条件时设置任务参数：

```c#
 var compile = context
	.CreateTarget("compile")
    .SetDescription("Compiles the VS solution")
    .AddCoreTask(x => x.Build().Configuration("Release")
	.When(
		() =>
		{
	    	return context.BuildSystems().IsLocalBuild;
	    },
		task => { task.Configuration("Debug"); }));
```

- `.Interactive()` - 交互地将参数从控制台传递给任务的方法或参数。

<a name="Custom-code"></a>

### **自定义 C# 代码/任务**

下例将执行一些自定义代码。你可以在自定义代码中使用 FlubuCore 的内置任务：

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Example")
       .Do(CustomCodeExample);
}

private static void CustomCodeExample(ITaskContext context)
{
    //// You can put any c# code here and use any .net libraries.
    Console.WriteLine("Dummy custom code");
    context.Tasks().NUnitTaskForNunitV3("project name").Execute(context);
}
```

你也可以使用带参方法：

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Example")
		.Do(CustomCodeExample, "some value", 1);
}

private static void CustomCodeExample(ITaskContext context, string arg1, int arg2)
{
	Console.WriteLine("Dummy custom code");
    context.Tasks().NUnitTaskForNunitV3("project name").Execute(context);
}
```

<a name="Target-dependencies"></a>

### **目标依赖**

目标可依赖于其他目标。所有依赖项将按指定顺序在目标执行前执行。

当 targetC 执行时，目标的执行顺序将是：TargetB、TargetA 和 TargetC。

```C#
var targetA = context.CreateTarget("TargetA");
var targetB = context.CreateTarget("TargetB");
var targetC = context.CreateTarget("TargetC").DependsOn(targetB, targetA);
```

<a name="Reuse-set-of-tasks"></a>

### **在目标中添加目标**

通过 AddTarget，一个目标可在另一个目标内部执行。目标将按添加顺序执行。

示例：

```C#
    protected override void ConfigureTargets(ITaskContext context)
    {
       var exampleB = context.CreateTarget("TargetB")
            .Do(Something);

       context.CreateTarget("TargetA")
           .AddCoreTask(x => x.Build())
           .AddTarget(exampleB)
           .Do(JustAnExample);
    }

    public void JustAnExample(ITaskContext context)
    {
        ...
    }
```

TargetA 执行顺序为：

1. 构建任务；
2. TargetB 目标；
3. JustAnExample 方法。

### **在不同目标中复用任务集**

下例展示了如何在不同目标中复用任务集（reuse set of tasks）：

```C#
protected override void ConfigureTargets(ITaskContext session)
{
	session.CreateTarget("deploy.local").AddTasks(Deploy, "c:\\ExamplaApp").SetAsDefault();

    session.CreateTarget("deploy.test").AddTasks(Deploy, "d:\\ExamplaApp");

    session.CreateTarget("deploy.prod").AddTasks(Deploy, "e:\\ExamplaApp");
}

private void Deploy(ITarget target, string deployPath)
{
    target
        .AddTask(x => x.IisTasks().CreateAppPoolTask("Example app pool").Mode(CreateApplicationPoolMode.DoNothingIfExists))
        .AddTask(x => x.IisTasks().ControlAppPoolTask("Example app pool", ControlApplicationPoolAction.Stop).DoNotFailOnError())
        .Do(UnzipPackage)
        .AddTask(x => x.CopyDirectoryStructureTask(@"Packages\ExampleApp", @"C:\ExampleApp", true).Retry(20, 5000))
        .Do(CreateWebSite)
}
```

### **在 foreach 循环中为目标添加任务**

下例展示了如何在 foreach 循环中为目标添加多个任务：

```c#
  protected override void ConfigureTargets(ITaskContext context)
  {
         var solution = context.Properties.Get<VSSolution>(BuildProps.Solution);

         context.CreateTarget("Pack")
                .ForEach(solution.Projects, (item, target) =>
                {
                    target.AddCoreTask(x => x.Pack().Project(item.ProjectName))
                          .Do(JustAnExample, item);
                });
  }

  private void JustAnExample(ITaskContext context, VSProjectInfo vsProjectInfo)
  {
        //// Do something.
  }
```

例中，示例程序将为每个项目执行 Pack 任务。

<a name="Group-task"></a>

### **分组任务，并应用 When、OnError 和 Finally**

- 在任务组上使用 When 子句有条件地执行任务。

```C#
protected override void ConfigureTargets(ITaskContext context)
{
	context.CreateTarget("Example")
        .AddCoreTask(x => x.Build())
        .Group(
               target =>
               {
                    target.AddCoreTask(x => x.Pack());
                    target.AddCoreTask(x => x.NugetPush("pathToPackage"));
               },
               when: c => !c.BuildSystems().Jenkins().IsRunningOnJenkins);
}
```

- 在任务组中使用 Finally：onFinally 的行为与 try-catch-finally 中的 Finally 相同。

```C#
context.CreateTarget("Example")
		.AddCoreTask(x => x.Build())
         .Group(
              target =>
              {
				 target.AddCoreTask(x => x.Pack());
                 target.AddCoreTask(x => x.NugetPush("pathToPackage"));
              },
              onFinally: c =>
              {
				 c.Tasks().DeleteFilesTask("pathToNupkg", "*.*", true).Execute(c);
              });
```

- 在任务组中使用 OnError：可以在组中任意一个任务发生错误时执行一些自定义操作。

```C#
context.CreateTarget("Example")
    .AddCoreTask(x => x.Build())
    .Group(
        target =>
        {
			target.AddCoreTask(x => x.Pack());
            target.AddCoreTask(x => x.NugetPush("pathToPackage"));
        },
        onError: (c, error) =>
        {
           //// some custom action when error occures in any of the task in group.
        });
```

<a name="Async-execution"></a>

### **任务、自定义代码与依赖项的异步执行与并行执行**

<ul>
<li>
可通过 AddTaskAsync 或 AddCoreTaskAsync 方法异步执行任务。

</li>
<li>
可使用 DoAsync 方法异步执行自定义代码。

</li>
<li>
可通过 DependsOnAsync 方法异步执行依赖项。

</li>
</ul>
在下例目标中并行执行三个任务。

```C#
session.CreateTarget("run.tests")
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName3"));
```

异步方法和同步方法也可以混合使用。

```C#
session.CreateTarget("async.example")
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .Do(SomeCustomMethod)
    .DoAsync(SomeCustomAsyncMethod2)
    .DoAsync(SomeCustomAsyncMethod3);
```

上面代码中，将首先异步执行两个 nunit 任务，并等待两个任务完成；随后将同步执行 SOmeCustomMethod，执行完后再并行执行 SomeCustomAsyncMethod2 和 SomeCustomAsyncMethod3。

#### 在异步执行的任务和目标中顺序打日志

通常来讲，在异步或并行执行多个任务时，日志是不可读（not readable）的。这就是为啥 FlubuCore 在异步任务中提供顺序记录（sequential logging）的原因。你可以在目标上使用 `.SequentialLogging(true)` 来启用，且必须放在异步任务/目标依赖项之前，否则日志就不是顺序的了。

```c#
context.CreateTarget("Test")
        .SetAsDefault()
        .SequentialLogging(true)
        .AddCoreTaskAsync(x => x.Pack())
        .AddCoreTaskAsync(x => x.Pack())
        .DependsOnAsync(test2, test3);
```

在 FlubuCore runner 中并行执行的目标在默认情况下是顺序记录日志的。

`flubu target1 target2 --parallel`

<a name="Other-features"></a>

### **其它功能**

#### 目标功能

- SetAsDefault 方法：当应用于目标时，如果在使用 runner 运行脚本时没有指定目标，则默认运行该目标；
- SetAsHidden 方法：当应用于目标时，目标将不会被显示在帮助信息中，并且它只能作为其它目标的依赖项来运行；
- Must 方法：设置必要条件，该条件必须满足，不然在任务执行之前目标就会执行失败。
- Requires method: Parameter specified in required method must not be null otherwise target execution will fail before any task get executed. 

#### 上下文功能


- Log：`context.LogInfo("Some Text2", ConsoleColor.Blue);`；
- GetVsSolution：获取解决方案和项目信息 `context.GetVsSolution();`。
- GetFiles: Get Files from specified directory with option to filter files with glob pattern `context.GetFiles(OutputDirectory, "*.nupkg");`
- GetDirectories: Get Directories from specified directory with option to filter files with glob pattern `context.GetFiles(OutputDirectory, "*.nupkg");`
- GetEnviromentVariable 方法：根据名称（name）获取环境变量 `context.GetEnvironmentVariable("someVariable");`；

<a name="Run-any-program"></a>

#### 使用 RunProgramTask 在构建脚本中运行程序或命令

```C#
protected override void ConfigureTargets(ITaskContext session)
{
	var runExternalProgramExample = session.CreateTarget("run.libz")
        .AddTask(x => x.RunProgramTask(@"packages\LibZ.Tool\1.2.0\tools\libz.exe")
            .WorkingFolder(@".\src")
            .WithArguments("add")
            .WithArguments("--libz", "Assemblies.libz"));
 }
```

Linux 的例子：

```C#
protected override void ConfigureTargets(ITaskContext session)
{
    var runExternalProgramExample = session.CreateTarget("systemctl.example")
        AddTask(x => x.RunProgramTask(@"systemctl")
            .WithArguments("start")
            .WithArguments("nginx.service"));
}
```

<a name="Build-properties"></a>

### **构建属性**

你可以在 ConfigureBuildProperties 方法中定义多种构件属性，用以在不同任务和自定义代码间共享。

下例将演示如何跨越各种 nunit 目标/任务（nunit targets/tasks）共享 nunit 控制台路径：

```C#
protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
{
	context.Properties.Set(BuildProps.NUnitConsolePath, @"packages\NUnit.ConsoleRunner.3.6.0\tools\nunit3-console.exe");
}

protected override void ConfigureTargets(ITaskContext session)
{
	session.CreateTarget("unit.tests1")
        .SetDescription("Runs unit tests")
        .AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests"));

    session.CreateTarget("unit.tests1")
         AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests2"));
}
```

如果不在构件属性中设置 nunit 控制台路径，则必须单独在每个任务中设置。

如：

```C#
protected override void ConfigureTargets(ITaskContext session)
{
    session.CreateTarget("unit.tests1")
        .SetDescription("Runs unit tests")
        .AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests")
            .NunitConsolePath(@"packages\NUnit.ConsoleRunner.3.6.0\tools\nunit3-console.exe"));

    session.CreateTarget("unit.tests1")
		.AddTask(x => x.NUnitTaskForNunitV3("FlubuExample.Tests2").
			NunitConsolePath(@"packages\NUnit.ConsoleRunner.3.6.0\tools\nunit3-console.exe"));
}
```

<a name="Predefined-build-properties"></a>

#### 预定义的构建属性

一些构件属性已被预定义，可以通过接口获取：

`context.Properties.Get(PredefinedBuildProperties.OsPlatform);`

可用的预定义构件属性有：

- OsPlatform
- PathToDotnetExecutable
- UserProfileFolder
- OutputDir
- ProductRootDir

所有这些构建参数都可被覆盖。

<a name="Script-arguments"></a>

## **向构建脚本属性传递命令行参数、JSON 配置文件设置或环境变量**

可通过在属性上打 FromArg 特性的方式向构建脚本属性传递命令行参数、JSON 配置文件的设置或环境变量。

```C#
public class SimpleScript : DefaultBuildScript
{
    [FromArg("sn", "If true app is deployed on second node. Otherwise not.")]
    public bool deployOnSecondNode { get; set; }

    protected override void ConfigureTargets(ITaskContext context)
    {
        context.CreateTarget("Deploy.Exapmle")
            .AddTask(x => x.FlubuWebApiTasks().GetTokenTask("user", "pass").SetWebApiBaseUrl("noade1Url"))
            .AddTask(x => x.FlubuWebApiTasks().UploadPackageTask("packageDir", "*.zip"))
            .AddTask(x => x.FlubuWebApiTasks().ExecuteScriptTask("Deploy", "DeployScript.cs"))
            .Group(target =>
            {
                target.AddTask(x => x.FlubuWebApiTasks().GetTokenTask("user", "pass").SetWebApiBaseUrl("noade2Url"))
                      .AddTask(x => x.FlubuWebApiTasks().UploadPackageTask("packageDir", "*.zip"))
                      .AddTask(x => x.FlubuWebApiTasks().ExecuteScriptTask("Deploy", "DeployScript.cs"));
            },
            when: c => deployOnSecondNode);
    }
}
```

FromArg 特性第一个参数（parameter）是参数键（argument key）。第二个参数用于在 flubu runner 中显示属性的帮助描述。实际上在属性上打特性并不是必须的，如果你没有添加这个特性，那么参数键（第一个参数）会与属性同名，属性的帮助信息不会显示在构建脚本的 runner 上。

支持的属性类型有：string、boolean、int、long、decimal、double 和 DateTime。

<a name="Command-line-argument"></a>

### **向构建脚本参数传递命令行参数。**

`Dotnet flubu Deploy.Example -sn=true`

<a name="json-configuration-file"></a>

### **向构建脚本传递 JSON 配置文件的设置**

- 在 FLubu runner 所在的目录下创建 FlubuSettings.json 文件；
- 以 JSON 格式的方式向文件中添加参数的键和值；
- 对于上面的例子，JSON 文件将看上去是这样子的：
  `json {“sn”：true，“SomeOtherKey”：“SomeOtherValue”}`
- 对于不同的环境（如开发、测试和生产环境），通常有不同的配置。只需创建不同的 JSON 文件 `FlubuSettings.{Environment}.Json`，并在需要的机器上[设置环境变量](https://andrewlock.net/how-to-set-the-hosting-environment-in-asp-net-core/) 'ASPNETCORE_ENVIRONMENT' 即可；
- 还可以按机器名 `FlubuSettings.{MachineName}.Json` 创建 JSON 配置文件，如果文件中的 MachineName 与本机机器名匹配，Flubu 将自动从该文件中读取设置。

<a name="enviroment-variable"></a>

### **向构建脚本传递环境变量**

还可以通过环境变量设置脚本参数。环境变量前必须有前缀 `flubu_`。

对于上面的例子，你可以通过 Windows 命令行工具添加系统环境变量： `set flubu_sn = true`。

<a name="Arguments-pass-through-to-tasks"></a>

## **向任务传递控制台参数、JSON 配置文件的设置，以及基于 ForMember 的环境变量。**

还有一种更为复杂的方法来给任务传递控制台参数、设置和环境变量：

```C#
protected override void ConfigureTargets(ITaskContext context)
{
   context.CreateTarget("compile")
       .AddTask(x => x.CompileSolutionTask()
           .ForMember(y => y.SolutionFileName("someSolution.sln"), "solution", "The solution to build."));
}
```

- 第一个参数是需要传递的方法或属性的参数，如果在运行构建脚本时没有指定参数，则使用默认值；
- 第二个参数是参数键（argument key）；
- 第三个参数是可选的，在目标的帮助中显式帮助信息。如果参数没有设置，则显示默认生成的帮助。

`Dotnet flubu compile -solution=someothersolution.sln`

<a name="Referencing-other-assemblies-in-build-script"></a>

<a name="Build-system-providers"></a>

## **构建系统提供者程序**

你可以获取不同的构建系统（如 Jenkins、TeamCity、AppVeyor、Travis 等）的多种信息，如构建。提交等。

```C#
protected override void ConfigureTargets(ITaskContext context)
{
    bool isLocalBuild = context.BuildSystems().IsLocalBuild;
    var gitCommitId = context.BuildSystems().Jenkins().GitCommitId;
}
```

<a name="Before-After"></a>

## **构建事件**

- OnBuildFailed 事件：

```c#
public class BuildScript : DefaultBuildScript
{
    protected override void OnBuildFailed(ITaskSession session, Exception ex)
    {
    }
}
```

- 在目标执行前后执行的事件：

```c#
protected override void BeforeTargetExecution(ITaskContext context)
{
}

protected override void AfterTargetExecution(ITaskContext context)
{
}
```

- 在构建执行前后执行的事件：

```c#
protected override void BeforeBuildExecution(ITaskContext context)
{
}

protected override void AfterBuildExecution(ITaskSession session)
{
}
```

<a name="partial-class"></a>

## **脚本中的部分类和基类**

如果部分类（partial classes）和基类（base classes）位于同一个目录下，则会自动加载它们；否则，必须使用 [Include 特性](../referencing-external-assemblies#adding-other-cs-files-to-script)来添加。
# FlubuCore 入门

## .NET core 篇

---

<a name="Requirements-.net-core"></a>

<a name="Installation-.net-core"></a>

#### 安装

- 添加新项目到解决方案，比如：BuildScript；
- 在项目中用 NuGet 添加对 **[FlubuCore]** 的引用。

##### 或从 FlubuCore 模板安装

- 在控制台中将当前目录切换到解决方案所在之处。
- 运行 `dotnet new -i FlubuCore.Template`
- 运行 `dotnet new FlubuCore`
- 这一步将从 FlubuCore 引用和 FlubuCore 脚本模板中添加 BuildScript.csproj

<a name="Write-and-run-your-first-build-script-in-.net-core"></a>

#### 用 .NET Core 编写并运行第一个构建脚本

将 BuildScript.cs 文件添加到构建脚本项目之中，并添加以下代码。

以下代码将编译目标（compile target）添加到 flubu 命令中，编译目标将编译解决方案。

```C#
public class MyBuildScript : DefaultBuildScript
{
	protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
    {
		context.Properties.Set(BuildProps.CompanyName, "Flubu");
        context.Properties.Set(BuildProps.CompanyCopyright, "Copyright (C) 2010-2016 Flubu");
        context.Properties.Set(BuildProps.ProductId, "FlubuCoreExample");
        context.Properties.Set(BuildProps.ProductName, "FlubuCoreExample");
    }

    protected override void ConfigureTargets(ITaskContext session)
    {
        var compile = context.CreateTarget("compile")
			.SetDescription("Compiles the solution.")
            .AddCoreTask(x => x.Build("FlubuExample.sln"));
    }
}
```

<a name="Run-build-script-Core"></a>

#### 用 dotnet CLI 工具运行构建脚本

- 将 [dotnet-flubu] 作为 dotnet 工具添加到 csproj 文件或 xproj（project.json）文件中。如果你是从模板安装的 FlubuCore，则不需要这个步骤。

csproj:

```xml
<ItemGroup>
    <DotNetCliToolReference Include="dotnet-flubu" Version="1.7.0" />
</ItemGroup>
```

project.json:

```json
"tools": {
        "dotnet-flubu": {
            "version": "1.7.0"
        }
    }
```

- 运行 `dotnet restore`。这条命令将还原（restore） dotnet-flubu 包，并将其添加到 dotnet 工具命令中。

- 运行 `dotnet flubu help`。除了默认命令外，你还能看到刚才我们添加进去的编译命令。

- 运行 `dotnet flubu compile`，这条命令将编译你的解决方案。

<a name="Run-build-script-core-with-global-tool"></a>

#### 在全局工具中运行构建脚本

- 必须先安装 .net core sdk 2.1.300 或更高版本；
- 安装 FlubuCore 全局工具：`dotnet tool install --global FlubuCore.GlobalTool`；
- 在构建脚本所在的目录下运行 `flubu compile`，本命令将编译你的解决方案。

这是个非常基础的构建脚本，目的是帮你快速入门。FlubuCore 已为你提供了许多棒极了的功能。你可以到 [Build script fundamentals] 阅读更多，或者移步 [.net core examples] 查看大多数主要功能的用法。同时建议你查看 [FlubuCore 交互模式](build-script-runner-interactive.md)和[覆盖现有选项或通过控制台向任务添加其他选项](override-add-options.md)一节。


## .NET 篇

---

#### 要求

引用 FlubuCore 的构建脚本项目必须是 .NET Framework 4.6.2 或更高。如果这一点无法做到，那么可以使用低于 [Flubu] 2.64 的版本，只要你安装了 .NET Framework 4.0 环境。为了运行 FlubuCore Runner，你需要安装 .NET 运行时 4.0 或更高的版本。

<a name="Installation.net"></a>

#### 安装

- 添加新项目到解决方案，比如：BuildScript；
- 在项目中用 NuGet 添加对 **[FlubuCore.Runner]** 的引用。这一步将会引用 FlubuCore.dll 并会将 BuildScript.cs 文件（构建脚本模板）添加到项目之中，为运行脚本添加 flubu.exe。

<a name="write-and-run"></a>

#### 用 .NET 编写并运行第一个构建脚本

使用以下代码修改 BuildScript.cs 文件，将解决方案的名字换成你的。

以下代码将编译目标（compile target）添加到 flubu 密令中，编译目标将编译解决方案。

```C#
using FlubuCore.Context;
using FlubuCore.Scripting;

public class BuildScript : DefaultBuildScript
{
	protected override void ConfigureBuildProperties(IBuildPropertiesContext context)
    {
		context.Properties.Set(BuildProps.ProductId, "FlubuExample");
        context.Properties.Set(BuildProps.ProductName, "FlubuExample");
        context.Properties.Set(BuildProps.SolutionFileName, "FlubuExample.sln");
        context.Properties.Set(BuildProps.BuildConfiguration, "Release");
    }

    protected override void ConfigureTargets(ITaskContext session)
    {
        var compile = session.CreateTarget("compile")
         .SetDescription("Compiles the solution.")
         .AddTask(x => x.CompileSolutionTask());
    }
}
```

<a name="run-build-script"></a>

#### 运行构建脚本

- 打开控制台程序（cmd）并将当前目录导航到构建脚本项目所在之处；

- 运行 flubu.exe help。除了默认命令外，你还能看到刚才我们添加进去的编译命令。

- 运行 flubu.exe compile，该命令将编译你的解决方案。

这是个非常基础的构建脚本，目的是帮你快速入门。FlubuCore 已为你提供了许多棒极了的功能。你可以到 [Build script fundamentals] 阅读更多，或者移步 [.net examples] 查看大多数主要功能的用法。

<a name="Getting-started-.net-core"></a>

[csproj.png]: https://bitbucket.org/repo/Bnjqgy/images/3977856142-csproj.png
[projectjson.png]: https://bitbucket.org/repo/Bnjqgy/images/2485583270-projectjson.png
[flubu examples]: https://github.com/flubu-core/examples
[build script fundamentals]: buildscript-fundamentals.md
[.net examples]: https://github.com/flubu-core/examples/blob/master/MVC_NET4.61/BuildScripts/BuildScript.cs
[.net core examples]: https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScript.cs
[flubu]: https://www.nuget.org/packages/Flubu
[flubucore]: https://www.nuget.org/packages/FlubuCore
[flubucore.runner]: https://www.nuget.org/packages/FlubuCore.Runner/
[dotnet-flubu]: https://www.nuget.org/packages/dotnet-flubu/
# FlubuCore

[![Windows Build](http://lucidlynx.comtrade.com:8080/buildStatus/icon?job=FlubuCore)](http://lucidlynx.comtrade.com:8080/login?from=%2F)
[![Travis](https://img.shields.io/travis/dotnetcore/FlubuCore.svg?branch=maste&?style=flat-square&label=linux-build)](https://travis-ci.org/dotnetcore/FlubuCore)
[![NuGet Badge](https://buildstats.info/nuget/flubucore)](https://www.nuget.org/packages/FlubuCore/)
[![Gitter](https://img.shields.io/gitter/room/FlubuCore/Lobby.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Twitter](https://img.shields.io/badge/twitter-flubucore-brightgreen.svg?logo=twitter)](https://twitter.com/FlubuC)
[![Member project of .NET Core Community](https://img.shields.io/badge/member%20project%20of-NCC-9e20c9.svg)](https://github.com/dotnetcore)
[![License](https://img.shields.io/github/license/dotnetcore/FlubuCore.svg)](https://github.com/dotnetcore/FlubuCore/blob/master/LICENSE)

## **概述**

“FlubuCore - Fluent Builder Core”，跨平台的构建与部署自动化系统，通过直观的 Fluent 接口，使用 C# 定义构建和部署脚本。这使你的代码获得自动完成、IntelliSense、调试、FlubuCore 自定义分析器，以及在脚本中对整个 .NET 生态的原生性访问。

![FlubuCore in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/demo.gif)

通过 roslyn 的强大赋能，FlubuCore 提供有 .NET/.NET Core 控制台应用程序用于编译和执行脚本。以上示例均可从控制台运行：

- FlubuCore runner `flubu.exe Default`
- FlubuCore dotnet cli tool `dotnet flubu Default`
- FlubuCore global tool `flubu Default`

## 功能与优势

- 直观，易学。C#、流畅的 API 设计和 IntelliSense，使复杂脚本的构建变得举重若轻。

```c#
context.CreateTarget("Example")
  .DependsOn(fetchBuildVersionTarget)
  .AddTask(x => x.CompileSolutionTask())
  .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
      .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);
```

- [内置大量常用任务](https://flubucore.dotnetcore.xyz/tasks/)，如运行测试、管理 ISS、创建部署包（deployment packages）、发布 NuGet 包、docker 任务、执行 PowerShell 脚本等。

```c#
context.CreateTarget("build")
   .AddTask(x => x.GitVersionTask())
   .AddTask(x => x.CompileSolutionTask("MySolution.sln").BuildConfiguration("Release");

context.CreateTarget("run.tests")
   .AddTask(x => x.XunitTaskByProjectName("MyProject").StopOnFail())
   .AddTask(x => x.NUnitTask(NunitCmdOptions.V3, "MyProject2").ExcludeCategory("Linux"))
   .AddCoreTask(x => x.CoverletTask("MyProject.dll"));
```

- [执行自义定代码](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Custom-code)。

```c#
context.CreateTarget("MyCustomBuildTarget")
     .AddTask(x => x.CompileSolutionTask())
     .Do(MyCustomMethod)
     .Do(NuGetPackageReferencingExample);
```

- 当脚本与项目文件一起使用时[会自动加载程序集引用和 NuGet 包](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Referencing-other-assemblies-in-build-script)。当脚本单独执行（譬如在生产环境中使用 FlubuCore 脚本进行部署）时，可在特性（attributes）中添加引用（references）。

```c#
[NugetPackage("Newtonsoft.json", "11.0.2")]
[Assembly(".\Lib\EntityFramework.dll")]
public class BuildScript : DefaultBuildScript
{
   public void NuGetPackageReferencingExample(ITaskContext context)
    {
        JsonConvert.SerializeObject("Example");
    }
}
```

- [在脚本中轻松运行任何外部程序（external program）或控制台命令（console command）](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Run-any-program)。

```c#
 public class SimpleScript : DefaultBuildScript
 {
	protected override void ConfigureTargets(ITaskContext context)
    {
		context.CreateTarget("Run.Libz")
		.AddTask(x => x.RunProgramTask(@"packages\LibZ.Tool\1.2.0\tools\libz.exe")
			.WorkingFolder(@".\src")
			.WithArguments("add")
			.WithArguments("--libz", "Assemblies.libz"));
	}
 }
```

- [将命令行参数（command line arguments）、json 配置文件或环境变量（environment variables）的设置传入脚本](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Script-arguments)。

```c#
 public class SimpleScript : DefaultBuildScript
 {
    [FromArg("sn", "If true app is deployed on second node. Otherwise not.")]
    public bool deployOnSecondNode { get; set; }


     protected override void ConfigureTargets(ITaskContext context)
     {
         context.CreateTarget("compile")
            .AddTask(x => x.CompileSolutionTask()
                .ForMember(y => y.SolutionFileName("someSolution.sln"), "solution", "The solution to build."));
     }
 }
```

```
  flubu.exe compile -solution=someOtherSolution.sln -sn=true
```

- [通过在 FlubuCore 插件中编写自己的任务来扩展 FlubuCore Fluent Api](https://flubucore.dotnetcore.xyz/write-plugins)。

```c#
    public class ExampleFlubuPluginTask : TaskBase<int, ExampleFlubuPluginTask>
    {
        protected override int DoExecute(ITaskContextInternal context)
        {
            // Write your task logic here.
            return 0;
        }
    }
```

- [不断丰富中的 FlubuCore 插件补充着内置任务](https://flubucore.dotnetcore.xyz/AwesomePlugins/awesome-plugins/)。

- [异步执行任务、目标依赖与自定义代码](https://flubucore.dotnetcore.xyz/buildscript-fundamentals#Async-execution)。

```c#
    context.CreateTarget("Run.Tests")
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
        .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName3"));
```

- [通过控制台程序为任务添加额外配置项（additional options），或对现有的配置项进行重写（override）](https://flubucore.dotnetcore.xyz/override-add-options/)

```c#
context.CreateTarget("Example")`
   .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release");
```

`flubu example --configuration=Debug`

flubu 将执行 `dotnet build MySolution.sln --configuration Debug`

- [完整的 .NET Core 支持，包括全局 CLI 工具](https://flubucore.dotnetcore.xyz/getting-started#getting-started-net-core)

```
    dotnet tool install --global FlubuCore.GlobalTool
    flubu compile
```

- [可对构建脚本测试和调试](https://flubucore.dotnetcore.xyz/Tests-debugging)

```c#
    context.WaitForDebugger();
```

- [透过 FlubuCore Web API 轻松实现远程部署自动化](https://flubucore.dotnetcore.xyz/WebApi/getting-started/)

- [可在其他 .NET 应用程序中使用 FlubuCore 任务](https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs)。

- [FlubuCore 交互模式（interactive mode）](https://flubucore.dotnetcore.xyz/build-script-runner-interactive/) 提供有 target 标签自动完成、选项标签自动完成、切换 target/options，以及命令执行历史。还可以执行外部命令和可操作程序。对于其中的一部分，FlubuCore 还提供了 Tab 键自动补全的功能（比如 dotnet、git 等）

![FlubuCore 交互模式](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCore_Interactive_mode_full.gif)

- 使用 FlubuCore 自定义分析器（FlubuCore custom analyzers）增强开发体验。

![执行中的 FlubuCore 分析器](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCoreCustomAnalyzerDemo.png)

## **入门**

FlubuCore 用起来非常简单:-) 而且她的文档也非常完整。

[FlubuCore 文档](https://flubucore.dotnetcore.xyz) 中的[入门](https://flubucore.dotnetcore.xyz/getting-started/)一章将帮助你立即设置你的第一个 FlubuCore 构建。

可在[构建脚本的原理](https://flubucore.dotnetcore.xyz/buildscript-fundamentals) 一章中查阅 FlubuCore 提供的完整功能列表。

一旦你定义了构建与部署脚本（build and deployment scripts），以下 Wiki 张杰将解释如何运行它们：

- 针对 .NET Framework 项目，请使用 [FlubuCore.Runner](https://flubucore.dotnetcore.xyz/getting-started#Installation.net)
- 针对 .NET Core 项目，请使用 [FlubuCore CLI global tool](https://flubucore.dotnetcore.xyz/getting-started#Installation-.net-core)

## **范例**

除了 Wiki 的详细介绍外，FlubuCore 还提供了大量与真实情况相若的范例。这些例子可以在独立仓库 [Examples repository](https://github.com/dotnetcore/FlubuCore.Examples/) 中找到。

这些示例有助于你快速入门 FlubuCore：

这些示例有助于你快速入门 FlubuCore：

- [.NET Framework 构建示例](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/MVC_NET4.61/BuildScripts/BuildScript.cs) - Example covers versioning, building the project, running tests, packaging application for deployment.

- [.NET Core 构建示例](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCore_csproj/BuildScript/BuildScript.cs) - Example covers versioning, building the project, running tests, packaging application for deployment.
 
- [部署脚本示例](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/DeployScriptExample/BuildScript/DeployScript.cs) - Example shows how to write simple deployment script. 

- [Open source library example](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCoreOpenSource/Build/BuildScript.cs) - Example covers versioning, building the project, running tests and publishing nuget package. It also covers how to run build script on Appveyor and Travis CI.

## **疑惑？**

[![Join the chat at https://gitter.im/FlubuCore/Lobby](https://badges.gitter.im/mbdavid/LiteDB.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## **贡献**

请移步阅读 [CONTRIBUTING.md](https://github.com/dotnetcore/FlubuCore/blob/master/CONTRIBUTING.md).

### **如何作出贡献**

- 为本项目做推广。
- 如果你对本项目感兴趣，请在右上角点击 star，以便壮大我们的社区。
- 改进文档
- 反馈、修正 Bug。
- 实现新功能。
- 讨论如何进一步改进项目。
- 改善项目的现有实现、性能等。

## Further Development
If you find FlubuCore useful (you feel it helps you on the daily basis) you can support further development by buying us a coffee (or become a backer or sponsor). Sometimes it's hard to stay awake till midnight implementing new features, coffee helps us with that. We would really appreciate your support. Money from sponsorship will also be used for the promotion of the project. If you are a backer or a sponsor you can also request for a new feature or ask for support. These issues will be handled with highest priority.

[![](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/NCOpMkt)

### Backers and Sponsors
[![OpenCollective](https://opencollective.com/flubucore/backers/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12502) 
[![OpenCollective](https://opencollective.com/flubucore/sponsors/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12503)

## **更新日志与路线图**

详细变更记录与示例请参阅[变更日志](https://github.com/dotnetcore/FlubuCore/blob/master/CHANGELOG.md)。

FlubuCore 路线图请翻阅项目[里程碑](https://github.com/dotnetcore/FlubuCore/milestones)。
FlubuCore 允许在运行外部程序（external processes）的**所有**任务中添加或覆盖选项。

假设你有一个 target
```c#
context.CreateTarget("Example")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release"); 

```

并且你不想在调试配置中构建解决方案。

你可以直接在控制台中输入：

`flubu example --configuration=Debug`

FlubuCore 将执行： 

`dotnet build MySolution.sln --configuration Debug`

!!! info "Note"
	如果选项的 key 与外部程序的一样，那么可以使用对应的简短版本的 key。因此在上例中，`-c = debug` 也是可以的。

    FlubuCore 还支持在[交互模式](build-script-runner-interactive.md)中通过 Tab 键来自动补全信息。

<br/>

Tasks in FlubuCore plugins that does not support overriding of options out of the box can still be overriden with special prefix before option key `/o:`

`/o:{external_process_option}={value}`

`/o:` 会为 FlubuCore 目标中所有任务添加置顶选项。如果目标执行多个任务，那么这可能是个问题，所以

`/{taskName}:{external_process_option}={value}`

你也可以修改任务的默认前缀（default prefix）：

```c#
    context.CreateTarget("Publish")
        AddCoreTask(x => x.Publish()
            .ChangeDefaultAdditionalOptionPrefix("/p:"));
```

## **示例**

假设创建了目标（target）：

```c#
context.CreateTarget("Example")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release");

```

你不想在调试配置（debug configuration）中构建解决方案,

你可以在控制台中写

`flubu build /o:configuration=Debug`

或

`flubu build /o:c=Debug`

或

`flubu build /build:c=Debug`

flubu 将执行

`dotnet build MySolution.sln -c Debug`
## **在构建脚本中引用外部程序集**

FlubuCore 会自动从构建脚本的 csproj 文件中加载所有程序集引用（assemblies references）和 nuget 包。csproj 文件必须位于[指定位置](https://github.com/dotnetcore/FlubuCore/blob/master/src/FlubuCore/Scripting/Analysis/ProjectFileAnalyzer.cs)。如果不是程序集引用和 nuget 引用的话，FlubuCore 就不会在执行时自动加载它们。

!!! Note
	你可以在构建脚本中通过添加特性（attribute）的方式禁用引用程序集和 nuget 包。

	```C#
	[DisableLoadScriptReferencesAutomatically]
	public class BuildScript : DefaultBuildScript
	{
	}
	```

或者，当你运行无 csproj 的脚本（比如部署脚本）时，外部引用（external references）可以通过三种方式用指令来添加：

<a name="By-assembly-relative-or-full-path"></a>

### **通过程序集的相对路径或完整路径**

在构建脚本类上，你得添加特性（attribute）：

```C#
[Assembly(@".\packages\Newtonsoft.Json.9.0.1\lib\net45\Newtonsoft.Json.dll")]
public class BuildScript : DefaultBuildScript
{
    public void ReferencedAssemlby(ITaskContext context)
    {
       JsonConvert.SerializeObject("Example");
    }
}
```

FlubuCore 还可以从指定的目录价在所有程序集，也可以从其子目录（subdirectories）中加载

```C#
[AssemblyFromDirectory(@".\Packages", true)]
public class BuildScript : DefaultBuildScript
{
}
```

<a name="Referencing-nuget-packages"></a>

### **引用 NuGet 包**

Flubu 支持引用 NuGet 包。如果你想引用 NuGet 包，你必须先安装 .NET Core SDK 或 msbuild，否则它们（NuGet 包）将无法还原（restore）。

你必须在脚本的类上添加 NuGetPackage 特性：

```C#
[NugetPackage("Newtonsoftjson", "11.0.2")]
public class BuildScript : DefaultBuildScript
{
    public void ReferencedNugetPackage(ITaskContext context)
    {
       JsonConvert.SerializeObject("Example");
    }
}
```

<a name="Load-assembly-by-assembly-full-name"></a>

### **按程序集名称加载**

FlubuCore 可以通过完全限定程序集名（fully qualifed assemlby name）的方式加载系统程序集（system assemblies）。

逆序比在脚本类上添加 Reference 特性（attribute）：

```C#
[Reference("System.Xml.XmlDocument, System.Xml, Version=4.0.0.0, Culture=neutral, publicKeyToken=b77a5c561934e089")]
public class BuildScript : DefaultBuildScript
{
    public void ReferencedAssemlby(ITaskContext context)
    {
		XmlDocument xml = new XmlDocument();
    }
}
```

获取完全限定程序集名（fully qualifed assembly name）的一种方式：

    var fullQualifedAssemblyName = typeof(XmlDocument).Assembly.FullName;

<a name="Load-all-assemblies-from-directory"></a>

### **从目录中加载所有程序集**

即便你没有将脚本与 csproj 一道使用，FlubuCore 也可以从目录中自动加载所有外部程序集（external assemblies）（子目录（subdirectories）中的程序集也可以选择一并被加载）。

默认情况下，FlubuCore 会从 FlubuLib 目录下加载所有程序集。只要在 flubu runner 所在的位置下创建目录，并将程序集刚在该目录之中。你也可以在 flubu runner 中指明从那个目录加载程序集：

`flubu.exe -ass=somedirectory`

`dotnet flubu -ass=somedirectory`

或者你可以通过给 flubusettings.json 文件的 ass 设置一个值：

    {
      "ass" : "someDirectory",
      "SomeOtherKey" : "SomeOtherValue"
    }`

<a name="Adding-other-cs-files-to-build-script"></a>

## **将其它 .cs 文件加到脚本中**

其它 .cs 文件必须先添加特性（attribute），它们不会被自动地从构建脚本的项目文件中加载。除非已经自动加载过构建脚本的基类或部分类。

```C#
[Include(@".\BuildHelper.cs")]
public class BuildScript : DefaultBuildScript
{
    public void Example(ITaskContext context)
    {
        BuildHelper.SomeMethod();
    }
}
```

FlubuCore 还可以从指定的目录中加载所有的 .cs 文件到脚本中（也可以选择将该目录下的子文件夹中的 .cs 文件一并加载）。

```C#
[IncludeFromDirectory(@".\Helpers", true)]
public class BuildScript : DefaultBuildScript
{
}
```
本页面罗列了 FlubuCore 的内置任务及其简单描述。每个任务都支持流畅接口（fluent interface），更详细的任务文档请查阅代码文档。如果你有任何疑问，请加入我们的 gitter。

### **任务**

| 名称                               | 描述                                                                                                                          |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| RunProgramTask                     | 运行指定的外部程序                                                                                                            |
| CompileSolutionTask                | 编译指定的解决方案                                                                                                            |
| PackageTask                        | 将指定的目录和文件打包（package）到特定的目录或 zip 文件中                                                                    |
| FetchBuildVersionFromFileTask      | 从文件中获取构建版本（build version）                                                                                         |
| GitVersionTask                     | GitVersion 工具可帮助你在项目中实现语义版本控制（Semantic Versioning）[更多...](https://gitversion.readthedocs.io/en/latest/) |
| FetchVersionFromExternalSourceTask | 从外部源（Appveyor、travis、jenkins 等）获取构建版本（build version）                                                         |
| GenerateCommonAssemlbyInfoTask     | 为解决方案生成通用程序集信息（common assembly info）                                                                          |
| NUnitTask                          | 使用 nunit.exe runner 运行 nunit 测试                                                                                         |
| XunitTask                          | 使用 xunit.exe runner 运行 xunit 测试                                                                                         |
| NUnitWithDotCoverTaskTask          | 结合 dotCover 测试覆盖率分析（test coverage analysis）运行 nunit 测试                                                         |
| PublishNugetPackageTask            | 将 nuget 包发布到指定的 nuget 服务器上                                                                                        |
| NugetCmdLineTask                   | 通过 nuget.exe 操作 nuget                                                                                                     |
| UpdateXmlFileTask                  | 通过指定的更新命令更新 XML 文件                                                                                               |
| UpdateJsonFileTask                 | 通过指定的更新命令更新 JSON 文件                                                                                              |
| CleanoutputTask                    | 清理解决方案中所有项目的输出                                                                                                  |
| ControlServiceTask                 | 通过 sc.exe 命令控制 Windows 服务                                                                                             |
| CreateWindowsServiceTask           | 通过 sc.exe 命令创建 Winding 服务                                                                                             |
| ExecutePowerShellScriptTask        | 执行指定的 PowerShell 脚本                                                                                                    |
| SqlCmdTask                         | 通过 sqlcmd.exe 执行指定的 SQL 脚本文件                                                                                       |
| CreateAppPoolTask                  | 在 IIS 中创建新的应用程序池（application pool）                                                                               |
| ControlAppPoolTask                 | 启动/停止应用程序池                                                                                                           |
| DeleteAppPoolTask                  | 删除特定的应用程序池                                                                                                          |
| CreateWebApplicationTask           | 在 IIS 中为指定的 Web 站点创建新 Web 应用程序（web application）                                                              |
| CreateWebSiteTask                  | 在 IIS 中创建新站点（web site）                                                                                               |
| AddWebSiteBindingTask              | 编译（compile）指定的解决方案                                                                                                 |
| GetLocalIisVersionTask             | 获取本地机器上 IIS 的版本                                                                                                     |
| ReplaceTokenTask                   | 替换文件中指定的标记（token）                                                                                                 |
| ReplaceTextTask                    | 替换文件中指定的文本（text）                                                                                                  |
| CopyDirectoryStructureTask         | 使用指定的过滤器（filter）将文件从一个目录（directory）复制到另一个目录                                                       |
| CopyFileTask                       | 将文件从一个目录（directory）复制到另一个目录                                                                                 |
| CopyDirectoryStructureTask         | 将目录树（directory tree）从一处复制到另一处（from the source to the destination)                                             |
| CreateDirectoryTask                | 在指定路径下创建目录                                                                                                          |
| DeleteDirectoryTask                | 删除指定的目录                                                                                                                |
| DeleteFilesTask                    | 根据指定的模式（pattern）在指定的目录下删除文件                                                                               |
| UnzipFileTask                      | 将 zip 文件解压缩到指定的路径下                                                                                               |
| ZipFileTask                        | 压缩指定的数个文件                                                                                                            |
| OpenCoverTask                      | 运行 OpenCover                                                                                                                |
| OpenCoverToCoberturaTask           | 运行 OpenCover 至 Cobertuta                                                                                                   |
| CoverageReportTask                 | 运行覆盖率报告生成器                                                                                                          |
| LoadSolutionTask                   | 在 flubu 会话中加载解决方案信息                                                                                               |
| T4TemplateTask                     | 使用 TextTransform.exe 工具生成 T4 模板                                                                                       |
| GitTasks                           | 围绕 Git 克隆、添加、提交、拉取、推送、标签和移除文件的任务                                                                   |
| DockerTasks                        | 构建、运行、停止与移除容器，移除镜像以及其它相应的 docker cli 命令。所有任务均来自 docker 官方文档。                          |
| FlubuWebApiTasks                   | 各种 flubu web api 客户端任务                                                                                                 |

### **.NET Core 任务**

| 名称                     | 描述                                                                                                                                          |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ExecuteDotnetTask        | 执行指定的 dotnet 命令                                                                                                                        |
| DotnetRestoreTask        | 为指定应用程序或项目恢复（restore）依赖项（dependencies）和工具（tools）                                                                      |
| DotnetPublishTask        | 编译应用程序，读取项目文件中指定的依赖项，并将生成的文件集（set of files）发布到目录（directory）中                                           |
| DotnetBuildTask          | 构建（build）项目及其所有依赖项                                                                                                               |
| DotnetPackTask           | 通过命令构建项目并创建 nuget 包，该命令将生成一个 nuget 包                                                                                    |
| DotnetNugetPushTask      | 推送 nuget 包至 nuget 服务器                                                                                                                  |
| DotnetTestTask           | 根据 project.json / csproj 所配置的 test runner，运行测试                                                                                     |
| DotnetCleanTask          | 清理项目输出                                                                                                                                  |
| DotnetEfTasks            | 包含了多种实体框架（entity framework）任务                                                                                                    |
| UpdateNetCoreVersionTask | 在 csproj / project.json 文件中更新版本                                                                                                       |
| CoverletTask             | Coverlet 是 .NET Cire 下跨平台代码覆盖库，支持行（lines）、分支（branch）和方法（methods）覆盖 [更多...](https://github.com/tonerdo/coverlet) |
| SshComandLinuxTask       | 向远程主机运行指定的命令                                                                                                                      |
| SshCopyLinuxTask         | 将项目或文件复制到远程主机                                                                                                                    |
| SystemCtlLinuxTask       | 运行 systemctl 命令                                                                                                                           |
### **编写测试构建脚本与通过测试调试构建脚本**

Wiki 文档即将推出。先通过简单的测试来上手：https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs

如有需要，你可以通过测试调试构建脚本。

你也可以在其它 .NET 应用程序中使用 flub 任务，就像上面的测试示例一样。

### **通过附加到运行中的进程来调试构建脚本**

你可以通过调试器（debugger）附加到 Flubu 进程来调试构建脚本。

- 由于 Flubu 会稍微改变构建脚本，所以你必须将 Visual Studio 的「要求源文件与原始版本完全匹配」的选项禁用掉。
  这个选项的位置在「工具」→「选项」→「调试」→「常规」→「要求源文件与原始版本完全匹配」。对于 VS Code 来说则不能确定。
- 建议在第一个断点（break point）之前，在 ITaskContext 上使用 WaitForDebugger 扩展方法：

        protected override void ConfigureTargets(ITaskContext context)
        {
            context.WaitForDebugger();
        }

- 运行构建脚本，并将调试器（debugger）附加到 FlubuCore 进程。FlubuCore 进程名取决于你所使用 FlubuCore Runner。
  - FlubuCore.Runner - 你需要将调试器附加到名为 flubu.exe 的进程
  - dotnet-flubu Cli 工具 - 你需要将调试器附加到名为 dotnet 的确切的进程中
  - FlubuCore.GlobalTool - 你需要将调试器附加到名为 Flubu 的进程中
你可以通过编写自己的 flubu 任务来扩展 flubu 的流畅接口（fluent interface）。

当你通过自定义任务扩展 FlubuCore 时，只需要将其添加到目标（target）或通过 Do 来调用它即可，以下是例子：

```c#
public class BuildScript : DefaultBuildScript
{
    protected override void ConfigureTargets(ITaskContext context)
    {
        context.CreateTarget("FlubuPlugin.Example")
           .SetAsDefault()
           .Do(DoPluginExample);

       context.CreateTarget("FlubuPlugin.Example2")
           .AddTask(x => x.ExampleFlubuPluginTask());
    }

   private void DoPluginExample(ITaskContext context)
   {
       context.Tasks().ExampleFlubuPluginTask()
           .Message("some example message from plugin").Execute(context);
   }
}
```

### **如何创建任务插件**

- 在 VS 中创建新项目，项目名 FlubuCore.{PluginName}
- 在项目中引入 FlubuCore nuget 包
- 添加任务并实现之。以下代码演示了示例插件任务的实现：

```c#
public class ExampleFlubuPluginTask : TaskBase<int, ExampleFlubuPluginTask>
{
    private string _message;

    protected override string Description { get; set; }

    public ExampleFlubuPluginTask Message(string message)
    {
        _message = message;
        return this;
    }

    protected override int DoExecute(ITaskContextInternal context)
    {
        //// write task logic here.
        context.LogInfo(!string.IsNullOrEmpty(_message) ? _message : "Just some dummy code");

        return 0;
    }
}
```

- 然后，你需要编写一个扩展方法将任务添加对 flubu 流畅接口的支持。在本例中我们的扩展方法如下：

```C#
using FlubuCore.PluginExample;

namespace FlubuCore.Context.FluentInterface.Interfaces
{
   public static class TaskFluentInterfaceExtension
    {
        public static ExampleFlubuPluginTask ExampleFlubuPluginTask(this ITaskFluentInterface flubu)
        {
            return new ExampleFlubuPluginTask();
        }
    }
}
```

- 建议你将任务添加到对 ICoreTaskFluentInterface 或 ITaskFluentInterface 的扩展支持。

- 如果你将插件添加到 nuget 仓库中为佳。如果插件名以 FlubuCore 开头则更佳，因为这样大家都能很容易找到这个插件。

- 你可以在[这里](https://github.com/flubu-core/examples/tree/master/FlubuCustomTaskPluginAndLoadAssembliesFromDirectoryExample)查看示例插件的完整代码。
- [FlubuCore.CakePlugin](https://github.com/flubu-core/FlubuCore.CakePlugin) - Cake 有很多实用插件（addins）。CakePlugin 插件允许你在 FlubuCore 中使用任何 Cake 插件（addins）。

- [FlubuCore.Azure](https://github.com/flubu-core/FlubuCore.Azure) - 本插件为 Azure CLI 增加了超过 2000 个生成的任务，任务都是从官方文档生成的。

- [FlubuCore.Diff](https://github.com/flubu-core/FlubuCore.Diff) - 本插件将 Diff 任务添加到 FlubuCore 流畅接口（fluent interface）内。Diff 任务会比较两个指定文件，并生成 HTML 格式的差异报告。

- [FlubuCore.Gitter](https://github.com/flubu-core/FlubuCore.Gitter) - 本插件用于在指定的 Gitter room 内发送消息。

- FlubuCore.Kubernetes - 未被实现。请结合 FlubuCore 使用 [Kurernetes client](https://github.com/kubernetes-client/csharp)。

- [FlubuCore.Npm](https://github.com/flubu-core/FlubuCore.Npm) - 本插件为 npm CLI 命令添加了大量任务。

- [FlubuCore.Octopus](https://github.com/flubu-core/FlubuCore.Octopus) - 本插件为 octopus CLI 命令添加了大量任务。

- [FlubuCore.Slack](https://github.com/flubu-core/FlubuCore.Slack) - 本插件用于向 slack 频道（channels）发送消息。

- [FlubuCore.Chocolatey](https://github.com/flubu-core/FlubuCore.Chocolatey) - Plugin adds tasks for numerous Chocolatey CLI commands. Chocolatey is a software management solution unlike anything else you've ever experienced on Windows. It focuses on simplicity, security, and scalability. You write a software deployment in PowerShell once for any software (not just installers), then you can deploy it everywhere you have Windows with any solution that can manage systems (configuration management, endpoint management, etc) and track and manage updates of that software over time.
## **关于**

你可以通过使用 FlubuCore Web Api 远程执行 FlubuCore 脚本。这主要是为了让 .NET 或 .NET Core 应用程序从构建服务器（build server）部署到不同环境的自动化部署可以通过任意 FLubuCore 脚本来执行。

Web Api 支持：

- 在部署有 FlubuCore Web Api 的服务器上执行 flubu 脚本；
- 在部署有 FlubuCore Web Api 的服务器上上传（发布或其它操作）包（package）；
- 在部署有 FlubuCore Web Api 的服务器上删除包；
- 向客户端发送报告；
- 在部署有 FlubuCore Web Api 的服务器上上传 FlubuCore 脚本；
- 自动更新；
- 通过 FlubuCore Web App（与 Web Api 一同部署）手动执行目标（target）。

本指南将包含以下内容：

- 将 FlubuCore Web Api 部署到服务器
- 编写用于部署 MVC 示例应用程序于服务器的 .NET 部署脚本。如果你想通过 FlubuCore.WebApi 部署 .NET Core 应用程序，你应当阅读一下本指南。使用 FlubuCore.WebApi 部署 .NET Core 或 .NET 应用程序是没什么很大的差别的，所有差异都会写在本指南中。
- 编写构建脚本，将示例应用程序的部署包（deployment package）上传到服务器，并执行我们编写的部署脚本。
- 通过构建脚本（build script）远程运行部署脚本（deployment script）。

<a name="requirements"></a>

### **要求**

- .NET 运行时 4.6.2 或更高，或在服务器上安装 .NET Core Runtime，这取决于你打算使用的 FlubuCore.WebApi 构建哪一种应用。

<a name="Web-api-deployment"></a>

### **Web Api 开发**

- 从 https://github.com/dotnetcore/FlubuCore/releases 获取适当的 Web Api 部署包；
- 将 Web Api 部署包复制到需要执行 flubu 脚本的服务器上；
- 解压缩包；
- 在解压缩的 DeploymentConfig.json 文件中设置 Web Api 部署配置设置。有关特定部署设置的更多信息可见配置文件；
- 在 Windows 服务器上运行 deploy.bat 部署 Web Api；
- 在 Linux/macOS 服务器上依次运行 `dotnet restore`、`dotnet flubu -s=deploymentscript.cs`
- 在部署位置运行 `dotnet FlubuCore.WebApi.dll`，启动自托管（selfhost）的 Web Api。你当然也可以在 IIS 上托管它……

#### IIS 开发

如何部署 ASP.NET Core 应用程序，请查阅：https://docs.microsoft.com/en-us/aspnet/core/publishing/iis?tabs=aspnetcore2x

某些操作可能需要管理员权限（administration rights），比如启动/停止应用程序池（application pool）。如果是这种情况，你必须在托管 Web Api 的应用程序池中修改身份。切换到「应用程序池」→「Web Api 应用程序池」→「高级设置...」→「进程模型」→「标识」，并更改为具有管理员权限的账户。

<a name="Write-deploy-script"></a>

### **编写部署脚本**

用于示例的 .NET 部署脚本可以在[这里](https://github.com/flubu-core/examples/blob/master/DeployScriptExample/BuildScript/DeployScript.cs)查看。如果你想尝试该示例，最好的方法是复制 flubu core 的目录。.NET Core 应用程序的部署脚本会略有不同。

.NET 应用程序的示例部署脚本将：

- 如果不存在，创建 IIS 应用程序池；
- 停止应用程序池；
- 从 /packages 目录下解压缩包（将使用构建脚本上传到 Web Api）；
- 复制解压缩的应用程序到托管它的新文件夹；
- 在 IIS 上创建站点，如 Web 应用程序；
- 启动应用程序池。

完成部署脚本的编写之后，手动将其复制到 Web Api 部署位置的 /scripts 文件夹下。Web Api 也可以上传脚本，但出于安全考虑，这个功能默认是禁用的。在大多数情况下应保持禁用状态。

如果需要，你可以根据具体情况修改示例 DeployScript。

<a name="Write-build-script"></a>

### **编写构建脚本**

用于示例的 .NET 构建脚本可以在[这里](https://github.com/flubu-core/examples/blob/master/DeployScriptExample/BuildScript/BuildScript.cs)查看。

.NET 示例构建脚本将：

- 获取身份验证令牌（authentication token）
- 在 Web Api 上删除 /packages 目录下的旧的包
- 上传包（package）到 Web Api 的 /packages 文件夹下
- 执行 /scripts 文件夹下我们手动上传的部署脚本

如果需要，你可以根据具体情况修改示例 BuildScript。

<a name="Run-deploy-script"></a>

### **运行部署脚本**

如果你克隆（clone）了示例代码仓库，只需要在根目录（DeployScriptExample folder）下执行：

- `dotnet restore buildscript.csproj`，以及
- `dotnet flubu deploy -s=buildscript\buildscript.cs`

实际上你可能在成功构建之后从构建服务器部署。在合并到发布分支之后，在构建服务器上手动执行作业（job）……

<a name="Security"></a>

### **安全**

如果攻击者能获取 Web Api 的访问权限，那么他可能会进行大量破坏（do alot of damage）。如有可能，应实施以下安全举措（security measures）：

- 如有可能，FLubu Web Api 不应具有对外公开访问的权限；
- 始终通过 https 托管 Web Api；
- 通过 ip（通过配置）限制访问；
- 通过时间范围（通过配置）限制访问。如果你的应用程序在固定时间（如晚上 11 点）部署则应采用本安全策略，然后设置文档 api 的时间范围（如晚上 11 时至 11 时 15 分）；
- 使用强密码（Web Api 用户创建）
- 不要禁用「在登录失败时限制访问」的功能（通过配置）；
- 在 api 上执行 GetToken/Script 时启用电子邮件通知（通过配置）。

关于安全设置（security settings）的详细说明，请参阅 Web Api 的 appsettings.json 文件。

<a name="Automatic-update"></a>

### **自动更新**

如果存在可用的新版本，你可以自动更新 FlubuCore Web Api。只需要导航到 /UpdateCenter（不是 /api/UpdateCenter）

<a name="manual-target-execution"></a>

### **通过 FlubuCore Web App 远程手动执行目标**

你可以通过 FlubuCore Web App 手工执行目标（target），只需要导航到 /Script
<p align="center">
  <a href="https://github.com/dotnetcore/FlubuCore">English</a> | 
  <span>中文</span>  
</p>

# FlubuCore

[![Windows Build](http://lucidlynx.comtrade.com:8080/buildStatus/icon?job=FlubuCore)](http://lucidlynx.comtrade.com:8080/login?from=%2F)
[![Travis](https://img.shields.io/travis/dotnetcore/FlubuCore.svg?branch=maste&?style=flat-square&label=linux-build)](https://travis-ci.org/dotnetcore/FlubuCore)
[![NuGet Badge](https://buildstats.info/nuget/flubucore)](https://www.nuget.org/packages/FlubuCore/)
[![Gitter](https://img.shields.io/gitter/room/FlubuCore/Lobby.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Twitter](https://img.shields.io/badge/twitter-flubucore-brightgreen.svg?logo=twitter)](https://twitter.com/FlubuC)
[![Member project of .NET Core Community](https://img.shields.io/badge/member%20project%20of-NCC-9e20c9.svg)](https://github.com/dotnetcore)
[![License](https://img.shields.io/github/license/dotnetcore/FlubuCore.svg)](https://github.com/dotnetcore/FlubuCore/blob/master/LICENSE)

- [Introduction](#Introduction)
- [功能与优势](#功能与优势)
- [入门](#入门)
- [范例](#范例)
- [贡献](#贡献)
- [Backers and Sponsors](#Further-Development)
- [致谢](#致谢)

## Introduction

“FlubuCore - Fluent Builder Core”，跨平台的构建与部署自动化系统，通过直观的 Fluent 接口，使用 C# 定义构建和部署脚本。这使你的代码获得自动完成、IntelliSense、调试、FlubuCore 自定义分析器，以及在脚本中对整个 .NET 生态的原生性访问。

![FlubuCore in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/demo.gif)

通过 roslyn 的强大赋能，FlubuCore 提供有 .NET/.NET Core 控制台应用程序用于编译和执行脚本。以上示例均可从控制台运行：

- FlubuCore runner (.NET 4.62+)  `flubu.exe Default`
- FlubuCore dotnet cli tool (.NET Core 1.0+)  `dotnet flubu Default`
- FlubuCore global tool (.NET Core 2.1+) `flubu Default`

## 功能与优势

- 直观，易学。C#、流畅的 API 设计和 IntelliSense，使复杂脚本的构建变得举重若轻。

```cs
context.CreateTarget("Example")
  .DependsOn(fetchBuildVersionTarget)
  .AddTask(x => x.CompileSolutionTask())
  .AddTask(x => x.PublishNuGetPackageTask("packageId", "pathToNuspec"))
      .When(c => c.BuildSystems().Jenkins().IsRunningOnJenkins);
```

- [内置大量常用任务](https://flubucore-zh.dotnetcore.xyz/tasks/)，如运行测试、管理 ISS、创建部署包（deployment packages）、发布 NuGet 包、docker 任务、执行 PowerShell 脚本等。

```cs
context.CreateTarget("build")
   .AddTask(x => x.GitVersionTask())
   .AddTask(x => x.CompileSolutionTask("MySolution.sln").BuildConfiguration("Release");

context.CreateTarget("run.tests")
   .AddTask(x => x.XunitTaskByProjectName("MyProject").StopOnFail())
   .AddTask(x => x.NUnitTask(NunitCmdOptions.V3, "MyProject2").ExcludeCategory("Linux"))
   .AddCoreTask(x => x.CoverletTask("MyProject.dll"));
```

- [执行自义定代码](https://flubucore-zh.dotnetcore.xyz/buildscript-fundamentals#Custom-code)。

```cs
context.CreateTarget("MyCustomBuildTarget")
     .AddTask(x => x.CompileSolutionTask())
     .Do(MyCustomMethod)
     .Do(NuGetPackageReferencingExample);
```

- 当脚本与项目文件一起使用时[会自动加载程序集引用和 NuGet 包](https://flubucore-zh.dotnetcore.xyz/referencing-external-assemblies/)。当脚本单独执行（譬如在生产环境中使用 FlubuCore 脚本进行部署）时，可在特性（attributes）中添加引用（references）。

```cs
[NugetPackage("Newtonsoft.json", "11.0.2")]
[Assembly(".\Lib\EntityFramework.dll")]
public class BuildScript : DefaultBuildScript
{
   public void NuGetPackageReferencingExample(ITaskContext context)
    {
        JsonConvert.SerializeObject("Example");
    }
}
```

- [在脚本中轻松运行任何外部程序（external program）或控制台命令（console command）](https://flubucore-zh.dotnetcore.xyz/buildscript-fundamentals#Run-any-program)。

```cs
context.CreateTarget("Run.Libz")
    .AddTask(x => x.RunProgramTask(@"packages\LibZ.Tool\1.2.0\tools\libz.exe")
        .WorkingFolder(@".\src")
        .WithArguments("add")
        .WithArguments("--libz", "Assemblies.libz"));
```

- [将命令行参数（command line arguments）、json 配置文件或环境变量（environment variables）的设置传入脚本](https://flubucore-zh.dotnetcore.xyz/buildscript-fundamentals#Script-arguments)。

```cs
public class SimpleScript : DefaultBuildScript
{
    [FromArg("sn", "If true app is deployed on second node. Otherwise not.")]
    public bool deployOnSecondNode { get; set; }

    protected override void ConfigureTargets(ITaskContext context)
    {
        context.CreateTarget("compile")
           .AddTask(x => x.CompileSolutionTask()
               .ForMember(y => y.SolutionFileName("someSolution.sln"), "solution", "The solution to build."));
    }
}
```

```
flubu.exe compile -solution=someOtherSolution.sln -sn=true
```

- [通过在 FlubuCore 插件中编写自己的任务来扩展 FlubuCore Fluent Api](https://flubucore-zh.dotnetcore.xyz/write-plugins)。

```cs
public class ExampleFlubuPluginTask : TaskBase<int, ExampleFlubuPluginTask>
{
    protected override int DoExecute(ITaskContextInternal context)
    {
        // Write your task logic here.
        return 0;
    }
}
```

- [不断丰富中的 FlubuCore 插件补充着内置任务](https://flubucore-zh.dotnetcore.xyz/AwesomePlugins/awesome-plugins/)。

- [异步执行任务、目标依赖与自定义代码](https://flubucore-zh.dotnetcore.xyz/buildscript-fundamentals#Async-execution)。

```cs
context.CreateTarget("Run.Tests")
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName1"))
    .AddTaskAsync(x => x.NUnitTaskForNunitV3("TestProjectName3"));
```

- [通过控制台程序为任务添加额外配置项（additional options），或对现有的配置项进行重写（override）](https://flubucore-zh.dotnetcore.xyz/override-add-options/)

```c#
context.CreateTarget("Example")`
    .AddCoreTask(x => x.Build("MySolution.sln").Configuration("Release");
```

`flubu example --configuration=Debug`

flubu 将执行 `dotnet build MySolution.sln -c Debug`

- [完整的 .NET Core 支持，包括全局 CLI 工具](https://flubucore-zh.dotnetcore.xyz/getting-started#getting-started-net-core)

```
dotnet tool install --global FlubuCore.GlobalTool
flubu compile
```

- [可对构建脚本测试和调试](https://flubucore-zh.dotnetcore.xyz/Tests-debugging)

```cs
context.WaitForDebugger();
```

- [透过 FlubuCore Web API 轻松实现远程部署自动化](https://flubucore-zh.dotnetcore.xyz/WebApi/getting-started/)

- [可在其他 .NET 应用程序中使用 FlubuCore 任务](https://github.com/flubu-core/examples/blob/master/NetCore_csproj/BuildScript/BuildScriptTests.cs)。

- [FlubuCore 交互模式（interactive mode）](https://flubucore-zh.dotnetcore.xyz/build-script-runner-interactive/) 提供有 target 标签自动完成、选项标签自动完成、切换 target 和选项，以及命令执行历史等。

![FlubuCore 交互模式](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCore_Interactive_mode_full.gif)

- 使用 FlubuCore 自定义分析器（FlubuCore custom analyzers）增强开发体验。

![执行中的 FlubuCore 分析器](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/FlubuCoreCustomAnalyzerDemo.png)

## 入门

FlubuCore 用起来非常简单:-) 而且她的文档也非常完整。

[FlubuCore 文档](https://flubucore-zh.dotnetcore.xyz) 中的[入门](https://flubucore.dotnetcore.xyz/getting-started/)一章将帮助你立即设置你的第一个 FlubuCore 构建。

可在[构建脚本的原理](https://flubucore-zh.dotnetcore.xyz/buildscript-fundamentals) 一章中查阅 FlubuCore 提供的完整功能列表。

一旦你定义了构建与部署脚本（build and deployment scripts），以下 Wiki 张杰将解释如何运行它们：

- 针对 .NET Framework 项目，请使用 [FlubuCore.Runner](https://flubucore-zh.dotnetcore.xyz/getting-started#Installation.net)
- 针对 .NET Core 项目，请使用 [FlubuCore CLI global tool](https://flubucore-zh.dotnetcore.xyz/getting-started#Installation-.net-core)

## 范例

除了 Wiki 的详细介绍外，FlubuCore 还提供了大量与真实情况相若的范例。这些例子可以在独立仓库 [Examples repository](https://github.com/dotnetcore/FlubuCore.Examples/) 中找到。

这些示例有助于你快速入门 FlubuCore：

- [.NET Framework 构建示例](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/MVC_NET4.61/BuildScripts/BuildScript.cs) - Example covers versioning, building the project, running tests, packaging application for deployment and some other basic use cases.

- [.NET Core 构建示例](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCore_csproj/BuildScript/BuildScript.cs) - Example covers versioning, building the project, running tests, packaging application for deployment and some other basic use cases.
 
- [部署脚本示例](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/DeployScriptExample/BuildScript/DeployScript.cs) - Example shows how to write simple deployment script. 

* [Open source library example](https://github.com/dotnetcore/FlubuCore.Examples/blob/master/NetCoreOpenSource/Build/BuildScript.cs) - Example covers versioning, building the project, running tests and publishing nuget package. It also covers how to run build script on Appveyor and Travis CI.
## 疑惑？

[![Join the chat at https://gitter.im/FlubuCore/Lobby](https://badges.gitter.im/mbdavid/LiteDB.svg)](https://gitter.im/FlubuCore/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## 贡献

请移步阅读 [CONTRIBUTING.md](./CONTRIBUTING.md).

### 如何作出贡献

- 为本项目做推广。
- 如果你对本项目感兴趣，请在右上角点击 star，以便壮大我们的社区。
- 改进文档
- 反馈、修正 Bug。
- 实现新功能。
- 讨论如何进一步改进项目。
- 改善项目的现有实现、性能等。

## 更新日志与路线图

详细变更记录与示例请参阅[变更日志](https://github.com/dotnetcore/FlubuCore/blob/master/CHANGELOG.md)。

FlubuCore 路线图请翻阅项目[里程碑](https://github.com/dotnetcore/FlubuCore/milestones)。

## Further Development
If you find FlubuCore useful (you feel it helps you on the daily basis) you can support further development by buying us a coffee (or become a backer or sponsor). Sometimes it's hard to stay awake till midnight implementing new features, coffee helps us with that. We would really appreciate your support. Money from sponsorship will also be used for the promotion of the project. If you are a backer or a sponsor you can also request for a new feature or ask for support. These issues will be handled with highest priority.

[![](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/NCOpMkt)

### Backers and Sponsors
[![OpenCollective](https://opencollective.com/flubucore/backers/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12502) 
[![OpenCollective](https://opencollective.com/flubucore/sponsors/badge.svg?style=for-the-badge)](https://opencollective.com/flubucore/order/12503)

## 使用与支持

感谢 Comtrade 对我们的支持。

[![FlubuCore analyzers in action](https://raw.githubusercontent.com/flubu-core/flubu.core/master/assets/Svg/COMTRADE_logo.PNG)](https://www.comtrade.com)

## 致谢

特别感谢 [@ironcev](https://github.com/ironcev) 对 readme 文件做了大量改进并提供了一系列富有价值的建议。
特别感谢 [@alexinea](https://github.com/https://github.com/alexinea) 将整个文档翻译成中文。
OBSOLETE see CHANGELOG.md

3.2.0.0
- Added coverlet task
- Adds flubu setup where you can set location of the build script and project file.
- Added When condition to all tasks.
- Fixed bug where nuget and assemlby references were not loaded if csproj didnt have both of them
- Adds OnBuildFailed event.
- Adds before and after build execution events.
- Improved nunit tasks fluent intefaces.
- Added skipped target dependencies and tasks logging.
- Publicly exposed task name.
- fixed one of the default build script csproj location.

3.1.2.0
- Fixes Must on target fluent interface.
- Fixes script when using partial classes. Script failed in some scenarios.
- script allows includes of other cs files in partial classes.
- System.Drawing.Primitives assembly reference doesn't need to be referenced exlicitly anymore in script uses collored logging (issue was only present when target .net core framework)
- Improved some script error messages.

3.1.1.0
- Fixes loading of nuget packages that don't have target framework specified.
- FetchBuildVersionFromFileTask: Improves fetching of version from file by allowing version to be in any line not just first.
- FetchBuildVersionFromFileTask: Adds default project version file locations.
- FetchBuildVersionFromFileTask: Adds option to remove prefix from version.
- FetchBuildVersionFromFileTask: Adds option to allow any suffix. 
- Improves error messages when cs files that are used in script are not included.
- Improves error messages when script assembly references are not loaded.
- Added Null and empty target name validation.

3.1.0.0
- Added IncludeFromDirectoryAttribute: Attribute adds all .cs files from specified directory. With second optional parameter you can include subdirectories. 
- AssemblyFromDirectoryAttribute: When added on script class FlubuCore should add all assemblies from specified directory to script.
- Load base script class automatically.
- Improved collored console logging by wrapping strings of the output in ANSI codes that instruct the terminal to color the string based on the interpreted code.
- Allow namespaces in included cs files. Executing script does not fail anymore if included cs file contain namespace.
- Disable collored logging with attribute or script argument. 

3.0.2.0
- Fixed attribute "directives"

3.0.1.0
- Fixes restoring and loading of nuget packages with old csproj
- Stylecop nuget packages are not loaded anymore
- build status is now logged with color.
- Target and task information is now logged with color.

3.0.0.0
- Resolve nuget packages from build script csproj file automatically. No need for directives in build script anymore.
- Load referenced libraries from build csproj file automatically. No need for directives in build script anymore.
- All nuget dependencies are loaded automatically.
- Added GitVersionTask: GitVersion is a tool to help you achieve Semantic Versioning on your project. [Documentation](https://gitversion.readthedocs.io/en/latest/)
- Automatic load of build script partial classes. Partial classes have to be in same directory as build script.
- Automatic update of FlubuCore web api to new version. Just navigate to /UpdateCenter
- Added small web app to FlubuCore web api for executing scripts. Navigate to /Script
- load assembly references, nuget references through script class attributes
- Added Must method to target fluent interface. Condition in must will have to be meet otherwise target execution will fail before any task get executed.
- Option to execute custom code before each target execution. Just override following methods:
- Colored console logging
- FetchVersionFromExternalSourceTask now supports following build systems : Bamboo, Bitrise, ContinousCl, Jenkins, TFS, TeamCity, TravisCI.
- CompileSolutionTask: support for VS2019 
- Restoring of nuget packages has fallback to msbuild now if dotnet core sdk is not installed
- New Config attribute: Disable load of script references from csproj
- New Config Attribute: Always recompile build script
- Expose the output of ExternalProcessTaskBase
- Fix: Specifing flubu script path in config file does not work
- Fix: BuildScript assembly is not recompiled when included cs files are changed
- Fix: Added interactive method to task fluent interface.
- Fixed switched capture output and capture error output
- Fixed GetRemoveFileTask base methods (null reference exception)
- Fixed GitPushFileTask base methods (null reference excetpion).
- Fixed GitAddTask base methods (null reference excetpion).
- External process task return type is now generic
- script key is now case insensitive in file configuration.
- switched from Microsoft.Extensions.CommandLineUtils to McMaster.Extensions.CommadLineUtils
- Minor visual improvements when displaying help.
- Added Net462 Web api deploy package for x86
- Added some more default build script locations.

2.14.0.0
- Adds support for Interactive task members.
- Option to add clean up task when hitting ctrl + c with Finalize method on tasks or Finalize method on Group of tasks.
- Improves logging on web api client tasks.
- (Possible breaking change)Removed obsolete methods from some tasks
- Adds option to set destination package folder in CreateZipPackageFromProjcet tasks. Currently only default destination folder could be used.

2.13.0.0
- Added docker generated tasks
- (Breaking changes) Old Docker task's that were previously manually implemented were overwriten with generated task.
  - Docker tasks that used property of type List<> were replaced with params. 
  - Some method names in docker tasks were renamed to the same name as it is option name in the docker command.
- Improved target fluent interface intelisense by adding methods from base interface.
- GitBranch information can be readed for jenkins build system. context.BuildSystems().Jenkins().GitBranch;
- WebApi increased max size limit of uploaded content

2.12.11.0
- Fixed solution loading with duplicate properties.

2.12.10.0
- Added GIT checkout task.

2.12.9.0
- Fixed T4 TextTransform finder.

2.12.8.0
- Fixed T4 template task.

2.12.7.0
- Fixed git submodule update.

2.12.6.0
- Added touch file task.
- Added T4 transform task.

2.12.5.0
- Fixed git submodule task registration.

2.12.4.0
- Added Git submodule support.

2.12.3.0
- RunProgramTask: Fixed WithArguments.

2.12.2.0
- Added dotnet template for flubu.
- Sensible data is now masked in logs.
- Added option to mask sensible parameters in WithArgument method.
- Fixed Git add task. 
- CompileSolutionTask: Fixed resolution of msbuild 15 when only build tools are installed.
- Improved target detailed help visually.


2.12.1.0
- Added git add task.
- Added git clone task.
- Added git commit task.
- Added git pull task.
- Added git push task.
- Added git remove files task.
- Added git tag task.
- Added docker build task.
- Added docker run task.
- Added docker stop task.
- Added docker remove container task.
- Added docker remove image task.
- Improved validation in alot of tasks.
- Fixed log message in control app poll task.
- WebApi: Packaging reports sub directiores is not recursive anymore as it failed in some scenrarios sending reports.

2.11.2.0
- Fixed install.ps1 as build.exe was renamed to flubu.exe

2.11.1.0
- When specifing target's with Target attribute methods don't need to be public anymore.
- Fixed error handling for .net core when missing assembly directive in build script.
- Added System.Private.Uri assembly to default loaded assemblies.
- Fixed some analyzer issues.
- Improved some analyzers. 

2.11.0.0
- Added FlubuCore specific code analyzers. Added target parameter analyzers when specifing target's with Target attribute. Added FromArg attribute analyzer.
- Greatly improved performance for .net core.
- Improved nuget package resolving performance.
- Build script arguments keys are now case insensitive.
- (Possible breaking change) Renamed (obsoleted) method for reusing set of tasks in target. Do -> AddTasks.
- (Possible breaking change) Renamed Flubu runner Build.exe -> Flubu.exe
- (Possible breaking change) action parameter in Do method is now of type ITaskContext insted of ITaskContextInternal 
- Added addition clean options to DotnetCleanTask. You can now clean specified directory, output dir, build dir.
- FromArg for passing arguments to build script properties now support list of string.
- Validation for when build property getter is called in ConfigureTargets
- Validation that task was not executed already when adding it to the target.
- Added TaskExecuted property on tasks.
- Improved session build properties validation in tasks:LoadSolutionTask, CompileSolutionTask, NunitTask, XunitTask
- DotnetNugetTask: Added SkipPushOnLocalBuild.
- PublishNugetTask: Fixed SkipPushOnLocalBuild.
- Fixed order of target's end execution report.
- Improved error message when missing assembly directive in build script.

2.10.0.0
- Json configuration file can now be specified by machine name. FlubuSettings.{MachineName}.Json
- Option to retry a task only when specified condition is meet.
- Do tasks have method name by default.
- Tasks: DoNotFail only when specified condition is meet.
- Added WaitingForDebugger task context extension.
- FlubuRunner: Option to perform a dry run.
- FlubuRunner: Added end execution report.
- FlubuRunner: Fixed -nodeps option.
- FlubuRunner: Fixed build script global arguments help.
- improved assembly directive error handling.
- Added target name validation.
- Improved target help by adding Flubu options to help.
- Improved Task name logging for DoTasks in start of task execution task.
- Added DoTasks as task extensions to task fluent interface.
- Added option to log duration of tasks.
- Fixed MergeConfigurationTask when multiple source files were applied.
- Fixed async SleepTask.

2.9.1.0
- Added support to control IIS application pool on remote computer

2.9.0.0
- Added support for referencing a nuget package.
- Added support for debugging the script by attaching to the debuget.

2.8.2.0
- Fixed issue with global tool breaking dotnet cli tool.

2.8.1.0
- Fixed reference issues.

2.8.0.0
- FlubuCore is now available as .net core global tool.
- Console arguments, configuration properties, enviroment variables can now be passed to script properties.
- Target's can now be defined with attribute on method.
- Flubu dotnet cli tool is now available for .net core 2.1.
- (BreakingChange) Renamed(obsoleted) ITargetFluentInterface to ITarget.
- LoadSolutionTask: display detailed info in case project loading fails.

2.7.2.0
- (BREAKING CHANGE from version 2.7.0.0) When clause interface changed on target. When has no single parameter which applies condition to last target fluent interface action
- Group task on target has no when parameter to apply conditions to group of tasks.

2.7.0.0
- Added Xunit task - For running xunit tasks with xunit console runner
- Added Build system providers - You can acces various build, commit... information for various build systems (such as Jenkins, TeamCity, AppVeyor, Travis...) 
- Targets: Added conditonal task execution with When clause.
- Targets: Added option to group tasks.
- Targets: Added OnError block - Group tasks in target and specify action to be taken on error. 
- Targets: Added OnFinally block - Group tasks in target and specify action to be taken when all jobs finishes successfully or with error.
- Added task OnError action.
- Added task Finally action.
- (BREAKING CHANGE) Target: Removed TaskExtensions from target fluent interface. Use AddTask task or extension equivalent instead. See 2.6.0 breaking changes
- (BREAKING CHANGE) Target: Removed CoreTaskExtensions from target fluent interface. Use AddCoreTask task or extension equivalent instead. See 2.6.0 breaking changes
- WebApi: Option to include logs into ExecuteScript response.
- WebApi: Option to include StackTrace to error response.
- WebApi ExecuteTask: Fixed missing option to add script arguments. 
- Fixed Execute target without dependencies
- Fixed netcore publish task mismatched default values for build configuration. 
- CleanupOutputTask: Improve error message when load solution task was not executed before Cleanoutput task execution
- NunitTask: Improve error message when load solution task was not executed before NunitTask execution
- Updated varios nuget packages.

2.6.0.0
- Added option to add multiple tasks, dependencies With (anonimous) method to target with Do method.
- (BREAKING CHANGE)Migrated CoreTaskExtensions fluent interface to CoreTasks fluent interface. All extensions method have same name so update should be very simple.
- (BREAKING CHANGE)Migreated TaskExtensions fluent interface to Tasks fluent interface. All extensions method have same name so update should be very simple.
- When target is not found result is now not anymore success status code. 
- WebApi: Increased request timeout to 10 minutes.
- WebApi Increased keep alive timeout to 10 minutes.
- Updated some nuget packages.

2.5.1.0
- IIS control application poll task doesnt fail anymore if application poll is in same state as specified in control application pool task
- WebApi: Added option to upload packages to specified subdirectory in packages folder.
- WebApi: Added option to delete packages from specified subdirectory in packages folder.
- FlubuCore: Fixed set timeout on web api tasks.
- FlubuCore: When DoNotFail is applied on task exception is now logged. 

2.5.0.0
- Added create HttpClient task.
- WebApi for .net 462 framework
- (Breaking change) Renamed BuildScriptEngine -> FlubuEngine
- RunProgramTask - Fixed Switched Stdout and Stderr 
- GetToken task and client now add / at the end of base url if not provided
- Fixed web api DeletePackages - sometimes all directories were not deleted and taks failed.
- WebApi deploy script improved config validation
- Added web api for windows os specific deploy script. 
- Package task doesnt log directories anymore when DissableLogging is applied 
- Improved build script locator help text when build script is not found.

2.4.0.0
- Added BuildScriptEngine for writing build script tests, build script debuging and executing flubu tasks in other .net (core) applications.
- Flubu web api tasks now support sending requests to multiple flubu web api servers.
- (Breaking Change)Improved Flubu web api tasks fluent interface. Web api base url and timeout can now be set in GetToken task. Token is now set implicitly.
- Introduced HttpClientFactory which supports sending requests to different endpoints
- WebApi: Added ping controller
- WebApi: UploadPackage now logs which packages are uploaded.
- WebApi: Increased upload size limit for iis to 200mb(web config)
- WebApi client: Fixed error handling when response is not json.
- Switched to DoLogInfo in TaskBase whichs improves NoLog
- Added exception to DoNotFailOnError action.

Updated Packages:
FlubuCore
- Microsoft.Web.Administration 11.0.0 -> 11.1.0

2.3.5.0
- Fixed CleanoOutputTask for new csprojs

2.3.4.0
- Tasks: fixed all tasks to check for NoLog flag when logging
- Tasks: DoNotFailOnError For ExecuteAsync added
- Tasks: Added option to Add action to DoNotFailOnError

2.3.3.0
- Project loading: Added support for new project type - fixes cleanup task for new project types.
- Improved CleanupOutputTask: Added some new fluent interface options
- WebApi BREAKING CHANGE: Switched from db from json file storage to LiteDb
- WebApi deployment script improvements
- Added Web api request logging
- Updated nuget packages
- documentation updates

Updated Packages:
FlubuCore:
Microsoft.CodeAnalysis.Common 2.4.0 -> 2.6.1
Microsoft.CodeAnalysis.CSharp 2.4.0 -> 2.6.1
Microsoft.CodeAnalysis.CSharp.Scripting 2.4.0 -> 2.6.1

WebApi:
Aspnetcore 1.1.2 - > 1.1.5
Aspnetcore 2.0.0 -> 2.0.1
Aspnetcore.mvc 1.1.3 -> 1.1.5
Aspnetcore mvc 2.0.0 -> 2.0.2
Microsoft.AspNetCore.Authentication.JwtBearer 1.1.2 -> 1.1.3
Microsoft.AspNetCore.Authentication.JwtBearer 2.0.0 -> 2.0.1


2.3.2.0
- Added symbols to flubu nuget packages
- Added xml documentation files to nuget where they were missing
- Added release notes link to nuget packages.
- Improved default for member help
- Breaking change: DoTask: Renamed taskAction -> doOptions
- DoTask: Fixed set task description.
- Breaking change: renamed action parameters on ITaskCoreExtesionsFluentInterface to taskAction or taskOptions.
- Investigated and added example for writing flubu plugins. See wiki - Flubu Tasks plugins and flubu examples.   
2.3.1.0
- Fixed load assembly from directory (See wiki - build script fundamentals)
- Fixed DoTask with one parameter TaskAction is now invoked.
- Updated target help info
- FlubuCore.Runner - Skip copying build script template if it already exists
- readme for FlubuCore and dotnet-flubu nuget package.
- Fixed some targets description.

2.3.0.0
- Explicit configuration pass through to tasks (See wiki - build script fundamentals)
- Explicit enviroment variables pass through to tasks. (See wiki - build script fundamentals)
- Implicitly add references to assemblies from default or specified directory (See wiki - build script fundamentals)
- Default target is now supported on multiple targets.
- Improved error handling when build script file is not csharp code file.
- Improved error handling when build script file has compilation errors.
- Improved error handling when build script does not inherit DefaultBuildScript or implement interface IBuildScript
- Flubu runner: removed obsolete command options.

2.2.2.0
- Fixed ForMember when multiple ForMembers are applied on method.

2.2.1.0
- Added some more options to dotnet commands.

2.2.0.0
- DoAsyncTask can now call true async method.
- ForMember now supports argument pass through to Properties.
- Param Properties in DoTask and DoTaskAsync are now public so they can be used for argument pass through in ForMember.
- Fixed build properties Set and Remove - property name is now lower cased.
2.1.6.0
- Fixed error handling when build script is not found.
- FetchVersionFromFile has no option to skip saving version to session.
- FetchVersionFromExternalSourceTask keeps existing version fields.
- GenerateCommonAssemblyInfoTask uses BuildProps.ProductVersionFieldCount.

2.1.5.0
- Added support for adding more Env. variables for version.
- Added support for revision number in FetchVersionFromExternalSourceTask.

2.1.4.0
- TaskBase: Added support for multiple ForMembers with same argument key
- TaskBase: Retry now logs exception message
- Target description is now shown in target help. Bug was created in version 2.1.0.0

2.1.3.0
- Fixed resolve dotnet.exe if not installed.

2.1.2.0
- Fixed Issue #38. CommonAssemblyInfo autogenerated tag.

2.1.1.0
- Added dependency targets to target help.

2.1.0.0
- Added support for explicit argument pass-through to targets and tasks(ForMember method on tasks) (See wiki - build script fundamentals).
- Added Target help.
- Extended Do with base task actions(second optional parameter in Do).
- CompileSolutionTask have now completly fluent interface.

2.0.6.0 
- Fixed PublishNugetPackageTask when using newer version of nuget.exe.

2.0.5.0
- Fixed BuildScript template for Flubu.Runner.

2.0.4.0
- added -debug option for detailed logging.

2.0.3.0
- Fixed NUnit Categories option.
- DoNotFailOnError is now declared in ITaskOfT interface instead in ITask.

2.0.2.0
- Fixed PublishNuGetPackageTask (NugetCmdLineTask).

2.0.1.0
- Fixed DotnetNugetPushTask.
- All dotnet core tasks that have Project argument can now be mixed with WithArgument fluent interface and BuildPropertie SolutionFileName.
- All dotnet core tasks that have Configuration argument can now be mixed with WithArgument fluent interface and BuildPropertie Configuration.
- .Project() fluent interface in net core tasks can now be used at any place and not anymore only at the begining.

2.0.0.0
- dotnet flubu cli tool now also runs on .net core app 2.0.
- FlubuCore now supports .net standard 2.0.
- Flubu web api now also runs on .net core app 2.0.
- Added support for multiple target execution in script runner.
- Added task for executing powershell scripts.
- Added NunitWithDotCover task.
- Added Get predefined build properties in IBuildPropertiesSession.  
- Added standard console logger parameters and standard verbosity level parameters to compile solution task.
- Updated nuget packages.
- Some other minor improvements.

1.9.0.0
- add support for setting verbosity and other logging properties for msbuild (Compile Task).  
- Improved ServiceControlTask inteface.
- Added CreateService task.
- All Task that uses external program now implements external process tasks interface(Improved usability).

1.8.1.0
- dotnet-flubu is now also build in .netcoreapp 1.0 target framework to support older versions.  

1.8.0.0
- added support for finding and using MSBuild 15.0 in builds.
- All tasks that uses external programs have now fluent interface to add custom arguments.
- Improved dotnet core task fluent interface.
- Added GetEnviromentVariable extension method to TaskContext.

1.7.3.0
- if not target specified and not default target, display help.

1.7.2.0
- added SleepTask.
- added Sc.exe task.
- added generic interface for external process tasks.

1.7.1.0
- Fixed script arguments pass through on flubu runner and dotnet-flubu cli tool.

1.7.0.5
- Fixed NoLog ITask interface.

1.7.0.4
- Option to disable task logging.

1.7.0.3
- Updated SqlCmdTask (do not escape args).

1.7.0.2
- merged replaceToken and replaceText tasks.

1.7.0.1
- added standard sqlcmd params.

1.7.0.0
- Added SqlCmd task with output capture support.
- Added capture output support for RunProgramTask.

1.6.9.1
- fixed compile task (correctly pass arguments to msbuild).

1.6.9.0
- updated compile task to support workingFolder and any params for msbuild.
- fixed il merge generation with libz container.

1.6.8.0
- Fixed references to system assemblies in .net 462 which caused stackoverflow exception in flubu.runner in atleast package task.

1.6.7.1
- Fixed PackageTask logging.

1.6.7.0
- Fixed retry on tasks.

1.6.6.1
- Fixed binding redirect for System.Security.Cryptography.Algorithms.
- Display flubu version info.

1.6.6.0
- Flubu is now build with .net core sdk 2.0 on build serve.

1.6.5.0
- fixed flubuCore runner binding redirects.

1.6.4.0
- Dotnet-flubu now targets netcoreapp1.1.

1.6.3.1
- Added SqlCmd task for executing MS SQL scripts.
1.6.3.0
- FlubuCore: Fixed generic parameters in Do Task.
- FlubuCore: Removed verbose switch for default NUnit 3 task. Issues with nunit 3.7.

1.6.2.0
- FlubuCore: Fixed web api set of base url when doing more that one request in one target.
- FlubuCore: Added option to add generic parameters to Do task. 

1.6.1.0
- FlubCore: All tasks have now retry mechanism option.
- FlubuCore: All tasks have now do not fail option.

1.6.0.0
- FlubuCore, WebApi: Added option to pasthrough arguments to targets and custom tasks.
- FlubuCore: Added upload script task.
- FlubuCore: Added delete packages task.
- FlubuCore: Fixed web api base url set through build propertis.
- WebApi: Added option to upload scripts to web api through web api method.
- WebApi: Fixed CommandArguments lifestyle.
- WebApi: Only scripts in script directory can now be executed.

1.5.2.0
- Fixed UploadPackageTask.
- web api ip white list access restriction.

1.5.1.0
- Added flubu web api GetToken task.
- Improved flubu web api UploadPackageTask and ExecuteScriptTask.
- Added web api documentation.

1.5.0.0
- Added FlubuCore web api for remote script execution.
- Added FlubuCore web api client.
- Added Flubu web api tasks to FlubuCore.

1.4.13.0
- Removed Client from FlubuCore.

1.4.12.0
- Upgraded nuget packages.

1.4.11.0
- Added generic DoNotFailOnError setting for tasks.

1.4.10.0
- Updated nuget packages.
- Fixed ControlAppPoolTask missing dependencie.

1.4.8.0
- Fixed version information in GenerateCommonAssemblyInfo task extension.
- GenerateCommonAssemblyInfo task extension has now GenerateCommonAssemblyInfo task action parameter.
- BREAKING CHANGE: Improved core pacakge extension tasks.
- Improved some others task extensions with task action parameter.

1.4.6.0
- Added do not fail option to run program task.

1.4.5.0
- Fixed dotnet core fluent interface for dotnet restore build and publish.

1.4.4.0
- Fixed dotnet core tasks (build, restore, clean, publish,) when no project name is defined. 

1.4.3.0
- BREAKING CHANGE updated flubu.core and flubu.runner .net framework from .net4.6 to .net.462.

1.4.2.0
- Added support for including other .cs files into buildscript with //#imp {PathToCsFile}.
- Added dotnet nuget push task.
- Added dotnet entity framework task.
- CompileSolutionTask: Improved Msbuild path locator Using Microsoft tool location helper now. Registry locator is now used as fallback .
- Solution name and configuration are now added form build props in DotNet specific tasks if not specified explicitly.
- PackageTask: Added option to disable logging of which files were filtered and copied.
- Updated flubu dependencies. No release candidates are referenced anymore. See https://bitbucket.org/zoroz/flubu.core/commits/cfeaec842a83dfd06f62c13aadd2b74496e47fa7 for more info.

1.3.11.0
- Updated Microsoft.Web.Administration from 10.0.0-rc1 to 10.0.0 used for iis tasks.
1.3.10.0
- CompileSolution task now supports specifing your own paths to Msbuild. If msbuild path is not specified or not found MsBuild is still searched at default locations. 
1.3.9.0
- SSH command capture output stream directly.
1.3.8.0
- SSH command task fixes.
1.3.7.0
- Added SSH support for entering password.
- Added support for executing multiple commands in one session.
1.3.6.0
- Added support for SSH. SshCommand and SshCopy tasks.
1.3.5.0
- CreateApplicationPool iis task: .Net clr version can now be set.
- All iis tasks have now fluent interface.
1.3.4.0
- Fixed iis task interfaces. They now contain Execute and ExecuteVoid methods.
- PackageTask - fixed issue when output zip file name contains more than one dot.
1.3.3.0
- Added support for external assembly loading by assembly relative path
- Target names are case insensitve now
- If target to be run does not exist help is now shown instead of default target being run.
- Build script can now contain namespace
1.3.2.0
- Added support for external reference based on type loading.
- Added support for external assembly loading by assembly full path.
- Do in Target is now a task.
- BREAKING CHANGE: Do is now executed in the order specified in build script and not anymore before all tasks.
- Added DoAsync to target: For asynchronus custom code execution.
- Added AddTaskAsync to target: For asynchronus task execution.
- Added DependsOnAsync to Target: For asynchronus target dependencies execution.
- All tasks have now ExecuteAsync method.
1.2.3.0
- Added explicit System.IO reference to Roslyn scripting engine.
1.2.2.0
- Added LogInfo and LogError to TaskContext.
- Added fluent interface to PublishNugetPackageTask.
- Added fluent interface to CopyDirectoryStructureTask.
- Added fluent interface to FetchBuildVersionFromFileTask.
- Added fluent interface to UpdateXmlFileTask.
- Added fluent interface to ReplaceTokensTask.
- moved packaging filters to it's own namespace.
- Added FlubuCore and dotnet-flubu nuget metadata.
1.2.1.0
- Minor fixes.
1.2.0.0
- Flubu.Runner now works without any manual config modifications. 
- Task fluent interface documentation.
- Added Dotnet specific tasks and extensions.
- BREAKING CHANGE: Splited TaskExtensions into CoreTaskExtensions and TaskExtensions.
1.1.10.0
- Updated nuget packages to latest version.
1.1.9.0
- Removed dotnet test -xml output parameter. It won't work under VS2017 RC.
1.1.8.0
- BREAKING CHANGE: Removed DependsOn by TaskExtensionsFluentInterface from TargetFluentInterface. Use BackToTarget instead on TaskExtensionFluentInterface.
1.1.7.0
- System tests.
1.1.6.0
- CompileSolutionTask - specific platform can be set now. Default is still AnyCPU.
- CompileSolutionTask - Custom arguments can be added now. 

1.1.5.0
- Added FlubuCore.Runner for .net 4.6.
1.1.4.0
N/A
- To get you started read documentation at: https://github.com/flubu-core/flubu.core
- If u like flubu give it a star at https://github.com/flubu-core/flubu.core and upvote on https://stackoverflow.com/questions/40890522/choice-for-build-tool-msbuild-nant-or-something-else/46776658#46776658
  so that the community get's bigger.
- You can find detailed examples of how flubu is used at https://github.com/flubu-core/examples
- You can find list of major changes of new version at: https://github.com/flubu-core/flubu.core/wiki/9-What's-New
- You can find all release notes at: https://github.com/flubu-core/flubu.core/blob/master/FlubuCore.ProjectVersion.txt
- Have a question? Create a new issue at: https://github.com/flubu-core/flubu.core/issues
- If u find a bug please report it :)
- If u have any improvement or feature proposal's we would be glad to hear from you. Add new issue as proposal on github and we will discuss it with you.
- If u want to fix a bug yourself, improve or add new feature to flubu.. Fork, Pull request but first add new issue on github so we discuss it.
- If u like flubu give it a star at https://github.com/dotnetcore/FlubuCore/ 
  so that the community get's bigger.
- You can find flubu core documentation at https://github.com/dotnetcore/FlubuCore/
- You can find detailed examples of how flubu is used at https://github.com/dotnetcore/FlubuCore.Examples
- You can find changelog at: https://github.com/flubu-core/flubu.core/blob/master/CHANGELOG.md
- Have a question? Create a new issue at: https://github.com/dotnetcore/FlubuCore/issues
- If u find a bug please report it :)
- If u have any improvement or feature proposal's we would be glad to hear from you. Add new issue as proposal on github and we will discuss it with you.
- If u want to fix a bug yourself, improve or add new feature to flubu.. Fork, Pull request but first add new issue on github so we discuss it.
- If u like flubu give it a star at https://github.com/dotnetcore/FlubuCore/ 
  so that the community get's bigger.
- You can find flubu core documentation at https://github.com/dotnetcore/FlubuCore/
- You can find detailed examples of how flubu is used at https://github.com/dotnetcore/FlubuCore.Examples
- You can find changelog at: https://github.com/flubu-core/flubu.core/blob/master/CHANGELOG.md
- Have a question? Create a new issue at: https://github.com/dotnetcore/FlubuCore/issues
- If u find a bug please report it :)
- If u have any improvement or feature proposal's we would be glad to hear from you. Add new issue as proposal on github and we will discuss it with you.
- If u want to fix a bug yourself, improve or add new feature to flubu.. Fork, Pull request but first add new issue on github so we discuss it.
4.1.5.217.11.0.2-Beta20#Next version
- Some text
- Some text2

## 4.1.5.2 (21.2.2019)

- FSat

4.0.0.0The MIT License (MIT)

Copyright (c) 2011-2018 Twitter, Inc.
Copyright (c) 2011-2018 The Bootstrap Authors

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
Copyright JS Foundation and other contributors, https://js.foundation/

This software consists of voluntary contributions made by many
individuals. For exact contribution history, see the revision history
available at https://github.com/jquery/jquery

The following license applies to all parts of this software except as
documented below:

====

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

====

All files located in the node_modules and external directories are
externally maintained libraries used by this software which have their
own licenses; we recommend you read them, as their terms may differ from
the terms above.
The MIT License (MIT)
=====================

Copyright Jörn Zaefferer

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
Copyright (c) .NET Foundation. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
these files except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
- Buildscript project must target .net framework 4.62 or greater.
- update buildscript.cs as necesary.
- Create project version file(txt, md...) for solution e.g. YourSolutionName.ProjectVersion.txt and add version of your project to file e.g. 1.0.0.0 
- run "Build.exe" for default target or "Build.exe '{targetName}'" for specific build target. 
- optionaly you can copy Build.exe to root directory of the solution.
- If u like flubu give it a star at https://github.com/dotnetcore/FlubuCore/
  so that the community get's bigger.
- You can find flubu core documentation at https://github.com/dotnetcore/FlubuCore/
- You can find detailed examples of how flubu is used at https://github.com/dotnetcore/FlubuCore.Examples
- You can find all release notes at: https://github.com/dotnetcore/FlubuCore/blob/master/CHANGELOG.md
- Have a question? Create a new issue at: https://github.com/dotnetcore/FlubuCore/issues
- If u find a bug please report it :)
- If u have any improvement or feature proposal's we would be glad to hear from you. Add new issue as proposal on github and we will discuss it with you.
- If u want to fix a bug yourself, improve or add new feature to flubu.. Fork, Pull request but first add new issue on github so we discuss it.
The MIT License (MIT)

Copyright (c) 2007 James Newton-King

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
