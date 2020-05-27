The MIT License

Copyright (c) 2016 Steven Robbins

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
THE SOFTWARE.## Welcome to TinyIoC

### Overview ###

Welcome to TinyIoC - an easy to use, hassle free, Inversion of Control Container. TinyIoC has been designed to fulfil a single key requirement - to lower the "level of entry" for using an IoC container; both for small projects, and developers who are new to IoC who might be "scared" of the "big boys"!

To that end, TinyIoC attempts to stick to the following core principals:

* **Simplfied Inclusion** - No assembly to reference, no binary to worry about, just a single cs file you can include in your project and you're good to go. It even works with both Mono and MonoTouch for iPhone development!
* **Simplified Setup** - With auto-resolving of concrete types and an "auto registration" option for interfaces setup is a piece of cake. It can be reduced to 0 lines for concrete types, or 1 line if you have any interface dependencies!
* **Simple, "Fluent" API** - Just because it's "Tiny", doesn't mean it has no features. A simple "fluent" API gives you access to the more advanced features, like specifying singleton/multi-instance, strong or weak references or forcing a particular constructor.

In addition to this, TinyIoC's "simplified inclusion" makes it useful for providing DI for internal library classes, or providing your library the ability to use DI without the consuming developer having to specify a container (although it's useful to provide the option to do so).

**Note** For ASP.Net per-request lifetime support you will need to also include TinyIoCAspNetExtensions.cs, and the TinyIoC namespace. This provides an extension method for supporting per-request registrations. It's an extra file, but it's preferable to taking a dependency on Asp.Net in the main file, which then requires users to setup #DEFINEs for non-asp.net platforms.

### Key Features ###

* Simple inclusion - just add the CS file (or VB file coming soon!) and off you go.
* Wide platform support - actively tested on Windows, Mono, MonoTouch, PocketPC and Windows Phone 7. Also works just fine on MonoDroid.
* Simple API for Register, Resolve, CanResolve and TryResolve.
* Supports constructor injection and property injection. Constructors are selected automatically but can be overridden using a "fluent" API.
* Lifetime management - including singletons, multi-instance and ASP.Net per-request singletons.
* Automatic lazy factories - a Func<T> dependency will automatically create a factory.
* RegisterMultiple/ResolveAll/IEnumerable<T> support - multiple implementations of an interface can be registered and resolved to an IEnumerable using ResolveAll, or taking a dependency on IEnumerable<T>.
* Child containers - lifetime can be managed using child containers, with automatic "bubbling" of resolving to parent containers where required.
The Common directory contains classes and XAML styles that simplify application development.

These are not merely convenient, but are required by most Visual Studio project and item templates.
If you need a variation on one of the styles in StandardStyles it is recommended that you make a
copy in your own resource dictionary.  When right-clicking on a styled control in the design
surface the context menu includes an option to Edit a Copy to simplify this process.

Classes in the Common directory form part of your project and may be further enhanced to meet your
needs.  Care should be taken when altering existing methods and properties as incompatible changes
will require corresponding changes to code included in a variety of Visual Studio templates.  For
example, additional pages added to your project are written assuming that the original methods and
properties in Common classes are still present and that the names of the types have not changed.