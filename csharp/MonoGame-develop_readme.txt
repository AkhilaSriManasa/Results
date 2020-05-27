# Change Log


## 3.7.1 Release - 12/8/2018

 - MGCB now generates content building statistics. [#6401](https://github.com/MonoGame/MonoGame/pull/6401)
 - Fixes to dependency loading in Pipeline Tool. [#6450](https://github.com/MonoGame/MonoGame/pull/6450)
 - Fixed crash when canceling choose folder dialog in Pipeline Tool. [#6449](https://github.com/MonoGame/MonoGame/pull/6449)
 - Fix add item dialog jumping around in Pipeline Tool. [#6451](https://github.com/MonoGame/MonoGame/pull/6451)
 - Fix OpenAL library loading on some Android phones. [#6454](https://github.com/MonoGame/MonoGame/pull/6454)
 - Fix Gamepad index tracking under UWP. [#6456](https://github.com/MonoGame/MonoGame/pull/6456)
 - Rename "Copy Asset Path" to "Copy Asset Name" for consistency with XNA in Pipeline Tool. [#6457](https://github.com/MonoGame/MonoGame/pull/6457)
 - Fix TextInput Keys argument for UWP. [#6455](https://github.com/MonoGame/MonoGame/pull/6455)
 - Add new GamePad.GetState() overloads to support different dead zone modes. [#6467](https://github.com/MonoGame/MonoGame/pull/6467)
 - Fixed incorrect offset DynamicSoundEffectInstance.SubmitBuffer under XAudio. [#6523](https://github.com/MonoGame/MonoGame/pull/6523)
 - Improved accuracy of fixed time step. [#6535](https://github.com/MonoGame/MonoGame/pull/6535)
 - Ensure intermediate output path exists before writing stats in Pipeline Tool. [#6503](https://github.com/MonoGame/MonoGame/pull/6503)
 - Fix for special window close case under SDL. [#6489](https://github.com/MonoGame/MonoGame/pull/6489)
 - Marshal microphone identifiers as UTF-8. [#6530](https://github.com/MonoGame/MonoGame/pull/6530)
 - Clear the current selections when excluding items in the Pipeline Tool. [#6549](https://github.com/MonoGame/MonoGame/pull/6549)
 - Enable standard derivatives extension for GLSL shaders. [#6501](https://github.com/MonoGame/MonoGame/pull/6501)
 - Fixed framebuffer object EXT loading under OpenGL. [#6562](https://github.com/MonoGame/MonoGame/pull/6562)
 - Fixed GL.RenderbufferStorage for devices that use the EXT entry points. [#6563](https://github.com/MonoGame/MonoGame/pull/6563)
 - Fix VS template installation when C# folder is missing. [#6544](https://github.com/MonoGame/MonoGame/pull/6544)
 - Fix for SDL loading when a '#' is in the directory path. [#6573](https://github.com/MonoGame/MonoGame/pull/6573)
 - Restored Buttons[] constructor in GamePadState fixing XNA compatibility. [#6572](https://github.com/MonoGame/MonoGame/pull/6572)


## 3.7 Release - 9/23/2018

 - Remove Scale and Rotation properties from Matrix. [#5584](https://github.com/MonoGame/MonoGame/pull/5584)
 - Added Switch as a platform. [#5596](https://github.com/MonoGame/MonoGame/pull/5596)
 - DirectX: Fixed multisample clamping logic. [#5477](https://github.com/MonoGame/MonoGame/pull/5477)
 - SDL Gamepad DB update. [#5605](https://github.com/MonoGame/MonoGame/pull/5605)
 - Add Missing method OpaqueDataDictionary.GetValue. [#5637](https://github.com/MonoGame/MonoGame/pull/5637)
 - Increase code coverage in Model* family. [#5632](https://github.com/MonoGame/MonoGame/pull/5632)
 - Fix scroll wheel events on Windows Universal. [#5631](https://github.com/MonoGame/MonoGame/pull/5631)
 - Implement GetHashCode on Vertex types. [#5654](https://github.com/MonoGame/MonoGame/pull/5654)
 - Implement GetHashCode and ToString methods for Joystick. [#5670](https://github.com/MonoGame/MonoGame/pull/5670)
 - Fixed Gamepad DPad on Android. [#5673](https://github.com/MonoGame/MonoGame/pull/5673)
 - Pipeline process not terminating on exit fix. [#5672](https://github.com/MonoGame/MonoGame/pull/5672)
 - Added Joystick.IsSupported property. [#5678](https://github.com/MonoGame/MonoGame/pull/5678)
 - Use GraphicsCapabilities.MaxTextureAnisotropy on SamplerState. [#5676](https://github.com/MonoGame/MonoGame/pull/5676)
 - Make SpriteBatch.End throw when Begin not called. [#5689](https://github.com/MonoGame/MonoGame/pull/5689)
 - Add Open Output Directory option to Pipeline Tool. [#5690](https://github.com/MonoGame/MonoGame/pull/5690)
 - Rename Exit to Quit on Pipeline Tool Linux Headerbar. [#5687](https://github.com/MonoGame/MonoGame/pull/5687)
 - Added minimum size to the Pipeline Tool window. [#5692](https://github.com/MonoGame/MonoGame/pull/5692)
 - Added Id and DisplayName properties to Gamepad. [#5625](https://github.com/MonoGame/MonoGame/pull/5625)
 - Improved GameController database loading for DesktopGL. [#5606](https://github.com/MonoGame/MonoGame/pull/5606)
 - RPC curves are now updated before Cue is played. [#5709](https://github.com/MonoGame/MonoGame/pull/5709)
 - Fixes to Texture2D.FromStream on Windows DirectX. [#5712](https://github.com/MonoGame/MonoGame/pull/5712)
 - Support DistanceScale and DopplerFactor under OpenAL. [#5718](https://github.com/MonoGame/MonoGame/pull/5718)
 - Implemented Microphone for OpenAL platforms. [#5651](https://github.com/MonoGame/MonoGame/pull/5651)
 - Implemented caching of staging resources used to copy data from a Texture2D under DirectX. [#5704](https://github.com/MonoGame/MonoGame/pull/5704)
 - Reusable function for raising events. [#5713](https://github.com/MonoGame/MonoGame/pull/5713)
 - Remove reference to SharpDX from project templates. [#5611](https://github.com/MonoGame/MonoGame/pull/5611)
 - Improvements to VideoPlayer for Desktop DirectX. [#5737](https://github.com/MonoGame/MonoGame/pull/5737)
 - Use SharpDX NuGet packages from our NuGet packages. [#5748](https://github.com/MonoGame/MonoGame/pull/5748)
 - Fixed leaks that affected shutting down and recreating GraphicsDevice under DirectX. [#5728](https://github.com/MonoGame/MonoGame/pull/5728)
 - Texture2D mipmap generation and population fixes. [#5614](https://github.com/MonoGame/MonoGame/pull/5614)
 - Remove SharpDX.RawInput.dll reference from DirectX graphics backend. [#5723](https://github.com/MonoGame/MonoGame/pull/5723)
 - New fast Texture2D.FromStream implementation for DesktopGL ported from STB. [#5630](https://github.com/MonoGame/MonoGame/pull/5630)
 - Added support DrawInstancedPrimitives on OpenGL platforms. [#4920](https://github.com/MonoGame/MonoGame/pull/4920)
 - Fixed mouse touch event to release when mouse moves outside the client area or we loses focus. [#5641](https://github.com/MonoGame/MonoGame/pull/5641)
 - Added GraphicsAdapter.UseDebugLayers to enable GPU debug features in release builds. [#5791](https://github.com/MonoGame/MonoGame/pull/5791)
 - Fixed DirectX back buffer update when multisampling changes. [#5617](https://github.com/MonoGame/MonoGame/pull/5617)
 - Adds Xbox One S controller support to Linux. [#5797](https://github.com/MonoGame/MonoGame/pull/5797)
 - Do not allow the Pipeline tool to delete files outside the content folder. [#5820](https://github.com/MonoGame/MonoGame/pull/5820)
 - OpenGL Mouse.SetCursor now works with alpha correctly. [#5829](https://github.com/MonoGame/MonoGame/pull/5829)
 - Implement Mouse.SetCursor() for Windows. [#5831](https://github.com/MonoGame/MonoGame/pull/5831)
 - Fix pre-emptive song finish in OggStreamer. [#5821](https://github.com/MonoGame/MonoGame/pull/5821)
 - UWP Templates use target version selected in wizard. [#5819](https://github.com/MonoGame/MonoGame/pull/5819)
 - Implement Mouse.WindowHandle under Windows DirectX. [#5816](https://github.com/MonoGame/MonoGame/pull/5816)
 - Improve shader error/warning parsing in Pipeline Tool. [#5849](https://github.com/MonoGame/MonoGame/pull/5849)
 - Fix crash on multi-editing bool values in Pipeline Tool. [#5859](https://github.com/MonoGame/MonoGame/pull/5859)
 - Fixes to XACT sound effect pooling. [#5832](https://github.com/MonoGame/MonoGame/pull/5832)
 - Improved disposal of OpenGL resources. [#5850](https://github.com/MonoGame/MonoGame/pull/5850)
 - Better support for WAV audio formats in content pipeline and FromStream. [#5750](https://github.com/MonoGame/MonoGame/pull/5750)
 - Fix for build hang with no mgcb file in project. [#5886](https://github.com/MonoGame/MonoGame/pull/5886)
 - Removed deprecated Rider settings from Linux installer. [#5881](https://github.com/MonoGame/MonoGame/pull/5881)
 - Improved performance of SpriteFont.MeasureString() & SpriteBatch.DrawString(). [#5874](https://github.com/MonoGame/MonoGame/pull/5874)
 - Sort content when saving MGCB files. [#5930](https://github.com/MonoGame/MonoGame/pull/5930)
 - Fix a crash when building content in xbuild. [#5897](https://github.com/MonoGame/MonoGame/pull/5897)
 - Fixed back button problems in UWP. [#5810](https://github.com/MonoGame/MonoGame/pull/5810)
 - Removed Windows 8.1 and Windows Phone 8.1 support. [#5809](https://github.com/MonoGame/MonoGame/pull/5809)
 - Upgrade to SharpDX 4.0.1. [#5949](https://github.com/MonoGame/MonoGame/pull/5949)
 - Update the UWP Template to use the Latest SDK. [#5931](https://github.com/MonoGame/MonoGame/pull/5931)
 - Fixed the Scissor rect calculation on DesktopGL and OpenGL platforms. [#5977](https://github.com/MonoGame/MonoGame/pull/5977)
 - Calculate the Client Bounds a bit later. [#5975](https://github.com/MonoGame/MonoGame/pull/5975)
 - Rework Android OpenGL Framebuffer Support. [#5993](https://github.com/MonoGame/MonoGame/pull/5993)
 - Implemented GraphicsDevice.GetBackBufferData. [#5114](https://github.com/MonoGame/MonoGame/pull/5114)
 - Optimizations to Length and Normalize in Vector3 and Vector4. [#6004](https://github.com/MonoGame/MonoGame/pull/6004)
 - Added MGCB man page for Linux. [#5987](https://github.com/MonoGame/MonoGame/pull/5987)
 - Included mgcb autocomplete for bash. [#5985](https://github.com/MonoGame/MonoGame/pull/5985)
 - Fixed GamePad.SetVibration crash. [#5965](https://github.com/MonoGame/MonoGame/pull/5965)
 - Fallback SurfaceFormat for RenderTargets. [#6170](https://github.com/MonoGame/MonoGame/pull/6170)
 - Added O(1) EffectParameter lookups by name. [#6146](https://github.com/MonoGame/MonoGame/pull/6146)
 - Reduce MouseState garbage in Desktop DirectX. [#6168](https://github.com/MonoGame/MonoGame/pull/6168)
 - Made SpriteFont constructor public. [#6126](https://github.com/MonoGame/MonoGame/pull/6126)
 - New Template System using Nuget. [#6135](https://github.com/MonoGame/MonoGame/pull/6135)
 - Use StbSharp for all Texture2D.FromStream. [#6008](https://github.com/MonoGame/MonoGame/pull/6008)
 - Dynamic reference loading in Pipeline Tool. [#6202](https://github.com/MonoGame/MonoGame/pull/6202)
 - Fix Pipeline tool to work regardless of Mono changes. [#6197](https://github.com/MonoGame/MonoGame/pull/6197)
 - Update Template Icons and Fix Mac Info.plist. [#6209](https://github.com/MonoGame/MonoGame/pull/6209)
 - Fix typo in VS2013 Shared Project Template. [#6216](https://github.com/MonoGame/MonoGame/pull/6216)
 - Fill up dotnet template info. [#6226](https://github.com/MonoGame/MonoGame/pull/6226)
 - Support Mac Unit Tests. [#5952](https://github.com/MonoGame/MonoGame/pull/5952)
 - Updated Assimp to latest version. [#6222](https://github.com/MonoGame/MonoGame/pull/6222)
 - Make sure that the window titlebar is within screen bounds on DesktopGL. [#6258](https://github.com/MonoGame/MonoGame/pull/6258)
 - Fixed trigger/dpad button state and reduced garbage in iOS Gamepad. [#6271](https://github.com/MonoGame/MonoGame/pull/6271)
 - Updated Windows Universal Min SDK Versions. [#6257](https://github.com/MonoGame/MonoGame/pull/6257)
 - Fix property content serialization detection when using a property named `Item`. [#5996](https://github.com/MonoGame/MonoGame/pull/5996)
 - Fix launcher default mimetype in Linux installer. [#6275](https://github.com/MonoGame/MonoGame/pull/6275)
 - Restore NVTT. [#6239](https://github.com/MonoGame/MonoGame/pull/6239)
 - Support unicode in window title under DesktopGL. [#6335](https://github.com/MonoGame/MonoGame/pull/6335)
 - Add crash report window to Pipeline Tool. [#6272](https://github.com/MonoGame/MonoGame/pull/6272)
 - Fix linking for copy action in Pipeline Tool. [#6398](https://github.com/MonoGame/MonoGame/pull/6398)
 - Implemented KeyboardInput and MessageBox for Windows DX. [#6410](https://github.com/MonoGame/MonoGame/pull/6410)
 - Fixed audio interruption bug on iOS. [#6433](https://github.com/MonoGame/MonoGame/pull/6433)


## 3.6 Release - 2/28/2017

 - Fixed XML deserialization of Curve type. [#5494](https://github.com/MonoGame/MonoGame/pull/5494)
 - Fix #5498 Pipeline Tool template loading on MacOS. [#5501](https://github.com/MonoGame/MonoGame/pull/5501)
 - Fix typo in the exclude.addins which cause warnings when installing the Addin in XS. [#5500](https://github.com/MonoGame/MonoGame/pull/5500)
 - Added support for arbitrary defines passed to the Effect compiler. [#5496](https://github.com/MonoGame/MonoGame/pull/5496)
 - Fixed GraphicsDevice.Present() to check for current render target. [#5389](https://github.com/MonoGame/MonoGame/pull/5389)
 - Custom texture compression for SpriteFonts. [#5299](https://github.com/MonoGame/MonoGame/pull/5299)
 - Performance improvements to SpriteBatch.DrawString(). [#5226](https://github.com/MonoGame/MonoGame/pull/5226)
 - Removed the OUYA platform [#5194](https://github.com/MonoGame/MonoGame/pull/5194)
 - Dispose of all graphical resources in unit tests. [#5133](https://github.com/MonoGame/MonoGame/pull/5133)
 - Throw NoSuitableGraphicsDeviceException if graphics device creation fails. [#5130](https://github.com/MonoGame/MonoGame/pull/5130)
 - Optimized and added additional constructors to Color. [#5117](https://github.com/MonoGame/MonoGame/pull/5117)
 - Added SamplerState.TextureFilterMode to correctly support comparison filtering. [#5112](https://github.com/MonoGame/MonoGame/pull/5112)
 - Fixed Apply3D() on stereo SoundEffect. [#5099](https://github.com/MonoGame/MonoGame/pull/5099)
 - Fixed Effect.OnApply to return void to match XNA. [#5090](https://github.com/MonoGame/MonoGame/pull/5090)
 - Fix crash when DynamicSoundEffectInstance not disposed. [#5075](https://github.com/MonoGame/MonoGame/pull/5075)
 - Texture2D.FromStream now correctly throws on null arguments. [#5050](https://github.com/MonoGame/MonoGame/pull/5050)
 - Implemented GraphicsAdapter for DirectX platforms. [#5024](https://github.com/MonoGame/MonoGame/pull/5024)
 - Fixed initialization of GameComponent when created within another GameComponent. [#5020](https://github.com/MonoGame/MonoGame/pull/5020)
 - Improved SoundEffect internal platform extendability. [#5006](https://github.com/MonoGame/MonoGame/pull/5006)
 - Refactored audio processing for platform extensibility. [#5001](https://github.com/MonoGame/MonoGame/pull/5001)
 - Refactored texture processing for platform extensibility. [#4996](https://github.com/MonoGame/MonoGame/pull/4996)
 - Refactor ShaderProfile to allow for pipeline extensibility. [#4992](https://github.com/MonoGame/MonoGame/pull/4992)
 - Removed unnessasary dictionary lookup for user index buffers for DirectX platforms. [#4988](https://github.com/MonoGame/MonoGame/pull/4988)
 - New SetRenderTargets() method which allows for variable target count. [#4987](https://github.com/MonoGame/MonoGame/pull/4987)
 - Added support for XACT reverb and filter effects. [#4974](https://github.com/MonoGame/MonoGame/pull/4974)
 - Remove array in GamePadDPad constructor. [#4970](https://github.com/MonoGame/MonoGame/pull/4970)
 - Updated to the latest version of Protobuild. [#4964](https://github.com/MonoGame/MonoGame/pull/4964)
 - Fixed static VBs and IBs on UWP on XB1. [#4955](https://github.com/MonoGame/MonoGame/pull/4955)
 - Updated to the latest version of Protobuild. [#4950](https://github.com/MonoGame/MonoGame/pull/4950)
 - Update Xamarin Studio addin for latest platform changes. [#4926](https://github.com/MonoGame/MonoGame/pull/4926)
 - Replace OpenTK with custom OpenGL bindings [#4874](https://github.com/MonoGame/MonoGame/pull/4874)
 - Fix Mouse updating when moving the Window. [#4924](https://github.com/MonoGame/MonoGame/pull/4924)
 - Fix incorrect use of startIndex in Texture2D.GetData DX. [#4833](https://github.com/MonoGame/MonoGame/pull/4833)
 - Cleanup of AssemblyInfo for framework assembly. [#4810](https://github.com/MonoGame/MonoGame/pull/4810)
 - New SDL2 backend for desktop GL platforms. [#4428](https://github.com/MonoGame/MonoGame/pull/4428)
 - Two MaterialProcessor properties fixed. [#4746](https://github.com/MonoGame/MonoGame/pull/4746)
 - Fixed thumbstick virtual buttons to always use independent axes. [#4742](https://github.com/MonoGame/MonoGame/pull/4742)
 - Fixed back buffer MSAA on DirectX platforms. [#4739](https://github.com/MonoGame/MonoGame/pull/4739)
 - Added new CHANGELOG.md to project. [#4732](https://github.com/MonoGame/MonoGame/pull/4732)
 - Added obsolete attribute and updated documentation. [#4731](https://github.com/MonoGame/MonoGame/pull/4731)
 - Fixed layout of UWP windows in VS template to ignore window chrome. [#4727](https://github.com/MonoGame/MonoGame/pull/4727)
 - Remove support for reading raw assets through ContentManager. [#4726](https://github.com/MonoGame/MonoGame/pull/4726)
 - Implemented DynamicSoundEffectInstance for DirectX and OpenAL platforms. [#4715](https://github.com/MonoGame/MonoGame/pull/4715)
 - Removed unused Yeti Mp3 compressor. [#4713](https://github.com/MonoGame/MonoGame/pull/4713)
 - MonoGame Portable Assemblies. [#4712](https://github.com/MonoGame/MonoGame/pull/4712)
 - Fixed RGBA64 packing and added unit tests. [#4683](https://github.com/MonoGame/MonoGame/pull/4683)
 - Fix Gamepad crash when platform doesn't support the amount. [#4677](https://github.com/MonoGame/MonoGame/pull/4677)
 - Fixed Song stopping before they are finished on Windows. [#4668](https://github.com/MonoGame/MonoGame/pull/4668)
 - Removed the Linux .deb installer. [#4665](https://github.com/MonoGame/MonoGame/pull/4665)
 - OpenAssetImporter is now automatically selected for all the formats it supports. [#4663](https://github.com/MonoGame/MonoGame/pull/4663)
 - Fixed broken unit tests under Linux. [#4614](https://github.com/MonoGame/MonoGame/pull/4614)
 - Split out Title Container into partial classes. [#4590](https://github.com/MonoGame/MonoGame/pull/4590)
 - Added Rider Support to Linux installer. [#4589](https://github.com/MonoGame/MonoGame/pull/4589)
 - Implement vertexStride in VertexBuffer.SetData for OpenGL. [#4568](https://github.com/MonoGame/MonoGame/pull/4568)
 - Performance improvement to SpriteBatch vertex generation. [#4547](https://github.com/MonoGame/MonoGame/pull/4547)
 - Optimization of indices initialization in SpriteBatcher. [#4546](https://github.com/MonoGame/MonoGame/pull/4546)
 - Optimized ContentReader to decode LZ4 compressed streams directly. [#4522](https://github.com/MonoGame/MonoGame/pull/4522)
 - TitleContainer partial class cleanup. [#4520](https://github.com/MonoGame/MonoGame/pull/4520)
 - Remove raw asset support from ContentManager. [#4489](https://github.com/MonoGame/MonoGame/pull/4489)
 - Initial implementation of RenderTargetCube for OpenGL. [#4488](https://github.com/MonoGame/MonoGame/pull/4488)
 - Removed unnecessary platform differences in MGFX. [#4486](https://github.com/MonoGame/MonoGame/pull/4486)
 - SoundEffect fixes and tests. [#4469](https://github.com/MonoGame/MonoGame/pull/4469)
 - Cleanup FX syntax for shader compiler. [#4462](https://github.com/MonoGame/MonoGame/pull/4462)
 - General Improvements to Pipeline Gtk implementation. [#4459](https://github.com/MonoGame/MonoGame/pull/4459)
 - ShaderProfile Refactor. [#4438](https://github.com/MonoGame/MonoGame/pull/4438)
 - GraphicsDeviceManager partial class refactor. [#4425](https://github.com/MonoGame/MonoGame/pull/4425)
 - Remove legacy Storage classes. [#4320](https://github.com/MonoGame/MonoGame/pull/4320)
 - Added mipmap generation for DirectX render targets. [#4189](https://github.com/MonoGame/MonoGame/pull/4189)
 

## 3.5.1 Release - 3/30/2016

 - Fixed negative values when pressing up on left thumbstick on Mac.
 - Removed exception and just return empty state when requesting an invalid GamePad index.
 - Fixed texture processing for 64bpp textures.
 - Fixed Texture2D.SaveAsPng on Mac.


## 3.5 Release - 3/17/2016

 - Content Pipeline Integration for Xamarin Studio and MonoDevleop on Mac and Linux.
 - Automatic inclusion of XNBs into your final project on Mac and Linux.
 - Improved Mac and Linux installers.
 - Assemblies are now installed locally on Mac and Linux just like they are on Windows.
 - New cross-platform Desktop project where same binary and content will work on Windows, Linux and Mac desktops.
 - Better Support for Xamarin.Mac and Xam.Mac.
 - Apple TV support (requires to be built from source at the moment).
 - Various sound system fixes.
 - New GraphicsMetrics API.
 - Optimizations to SpriteBatch performance and garbage generation.
 - Many improvements to the Pipeline tool: added toolbar, new filtered output view, new templates, drag and drop, and more.
 - New GamePad support for UWP.
 - Mac and Linux now support Vorbis compressed music.
 - Major refactor of texture support in content pipeline.
 - Added 151 new unit tests.
 - Big improvements to FBX and model content processing.
 - Various fixes to XML serialization.
 - MediaLibrary implementation for Windows platforms.
 - Removed PlayStation Mobile platform.
 - Added content pipeline extension template project.
 - Support for binding multiple vertex buffers in a draw call.
 - Fixed deadzone issues in GamePad support.
 - OcclusionQuery support for DX platforms.
 - Fixed incorrect z depth in SpriteBatch.
 - Lots of OpenTK backend fixes.
 - Much improved font processing.
 - Added new VertexPosition vertex format.
 - Better VS project template installation under Windows.


## 3.4 Release - 4/29/2015

 - Removed old XNA content pipeline extensions.
 - Added all missing PackedVector types.
 - Replacement of old SDL joystick path with OpenTK.
 - Added SamplerState.ComparisonFunction feature to DX and OGL platforms.
 - Fixed bug where content importers would not be autodetected on upper case file extensions.
 - Fixed compatibility with XNA sound effect XNBs.
 - Lots of reference doc improvements.
 - Added SamplerState.BorderColor feature to DX and OGL platforms.
 - Lots of improvements to the Mac, Linux and Windows versions of the Pipeline GUI tool.
 - Fixes for bad key mapping on Linux.
 - Support for texture arrays on DX platforms.
 - Fixed broken ModelMesh.Tag
 - VS templates will now only install if VS is detected on your system.
 - Added Color.MonoGameOrange.
 - Fixed Xact SoundBack loading bug on Android.
 - Added support for a bunch of missing render states to MGFX.
 - Added support for sRGB texture formats to DX and OGL platforms.
 - Added RasterizerState.DepthClipEnable support for DX and OGL platforms.
 - New support for the Windows 10 UAP plafform.
 - Fixed bug which caused the GamePad left thumbstick to not work correctly.
 - Preliminary base classed for future Joystick API.
 - Performance improvement on iOS by avoiding unnessasary GL context changes.
 - Fixed bug where MediaPlayer volume affected all sounds.
 - New XamarinStudio/MonoDevelop Addin for Mac.
 - New Mac installer packages.


## 3.3 Release - 3/16/2015

 - Support for vertex texture fetch on Windows.
 - New modern classes for KeyboardInput and MessageBox.
 - Added more validation to draw calls and render states.
 - Cleaned up usage of statics to support multiple GraphicsDevice instances.
 - Support Window.Position on WindowsGL platform.
 - Reduction of redundant OpenGL calls.
 - Fullscreen support for Windows DX platform.
 - Implemented Texture2D SaveAsPng and SaveAsJpeg for Android.
 - Improved GamePad deadzone calculations.
 - We now use FFmpeg for audio content building.
 - BoundingSphere fixes and optimizations.
 - Many improvements to Linux platform.
 - Various fixes to FontTextureProcessor.
 - New Windows Universal App template for Windows Store and Windows Phone support.
 - Many fixes to reduce garbage generation during runtime.
 - Adding support for TextureFormatOptions to FontDescriptionProcessor.
 - XNA compatibility improvements to FontDescriptionProcessor.
 - Resuscitated the unit test framework with 100s of additional unit tests.
 - BoundingFrustum fixes and optimizations.
 - Added VS2013 project templates.
 - Moved to new MonoGame logo.
 - Added MSAA render target support for OpenGL platforms.
 - Added optional content compression support to content pipeline and runtime.
 - TextureCube content reader and GetData fixes.
 - New OpenAL software implementation for Android.
 - Xact compatibility improvements.
 - Lots of Android fixes and improvements.
 - Added MediaLibrary implementation for Android, iOS, Windows Phone, and Windows Store.
 - Added ReflectiveWriter implementation to content pipeline.
 - Fixes to Texture2D.GetData on DirectX platforms.
 - SpriteFont rendering performance optimizations.
 - Huge refactor of ModelProcessor to be more compatible with XNA.
 - Moved NET and GamerServices into its own MonoGame.Framework.Net assembly.
 - Runtime support for ETC1 textures for Androud.
 - Improved compatibility for FBXImporter and XImporter.
 - Multiple SpritBatch compatibility fixes.
 - We now use FreeImage in TextureImporter to support many more input formats.
 - MGFX parsing and render state improvements.
 - New Pipeline GUI tool for managing content projects for Windows, Mac, and Linux desktops.
 - New implementation of content pipeline IntermediateSerializer.
 - All tools and content pipeline built for 64-bit.
 - New documentation system.
 - Implement web platform (JSIL) stubs.
 - Lots of fixes to PSM.
 - Added Protobuild support for project generation.
 - Major refactor of internals to better separate platform specific code.
 - Added MGCB command line tool to Windows installer.


## 3.2 Release - 4/7/2014

 - Implemented missing PackedVector types.
 - VS2013 support for MonoGame templates.
 - Big improvement to XInput performance on Windows/Windows8.
 - Added GameWindow.TextInput event enhancement.
 - Added Xamarin.Mac compatability.
 - Support for WPF interop under DirectX.
 - Enhancement to support multiple GameWindows on Windows under DirectX.
 - Various SpriteFont compatibility improvements.
 - OpenAL performance/memory/error handling improvements.
 - Reduction of Effect runtime memory usage.
 - Support for DXT/S3TC textures on Android.
 - Touch support on Windows desktop games.
 - Added new RenderTarget3D enhancement.
 - OUYA gamepad improvements.
 - Internal improvements to reduce garbage generation.
 - Various windowing fixes for OpenTK on Linux, Mac, and Windows.
 - Automatic support for content reloading on resume for Android.
 - Support for TextureCube, Texture3D, and RenderTargetCube on DirectX.
 - Added TitleContainer.SupportRetina enhancement for loading @2x content.
 - Lots of Android/Kindle compatibility fixes.
 - Added enhancement GameWindow.IsBorderless.
 - OpenGL now supports multiple render targets.
 - Game.IsRunningSlowly working accurately to XNA.
 - Game tick resolution improvements.
 - XACT compatibility improvements.
 - Various fixes and improvements to math types.
 - DrawUserIndexedPrimitives now works with 32bit indicies.
 - GamerServices fixes under iOS.
 - Various MonoGame FX improvements and fixes.
 - Render target fixes for Windows Phone.
 - MediaPlayer/MediaQueue/Song fixes on Windows Phone.
 - XNA accuracy fixes to TitleContainer.
 - Fixes to SpriteBatch performance and compatibility with XNA.
 - Threading fixes around SoundEffectInstance.
 - Support for Song.Duration.
 - Fixed disposal of OpenGL shader program cache.
 - Improved support of PoT textures in OpenGL.
 - Implemented missing EffectParameter SetValue/GetValue calls.
 - Touch fixes to Windows Phone.
 - Fixes to orientation support in iOS.
 - Lots of PSM fixes which make it usable for 2D games.
 - New Windows desktop platform using DirectX/XAudio.
 - Old Windows project renamed WindowsGL.
 - Fixed offsetInBytes parameter in IndexBuffer/VertexBuffer SetData.
 - Fixed subpixel offset when viewport is changed in OpenGL.
 - Tons of content pipeline improvements making it close to complete.


## 3.0.1 Release - 3/3/2013

 - Fix template error.
 - Fix offsetInBytes parameter in IndexBuffer/VertexBuffer SetData.
 - Fixes the scale applied on the origin in SpriteBatch.
 - Fixed render targets on WP8.
 - Removed minVertexIndex Exception.
 - Fixed some threading issues on iOS.
 - Use generic link for opening store on iOS.
 - Fix Matrix::Transpose.
 - Fixed vertexOffset in DrawUserIndexedPrimitives in GL.
 - Keys.RightControl/RightShift Support for WinRT.
 - Dispose in ShaderProgramCache.
 - IsRunningSlowly Fix.


## 3.0 Release - 1/21/2013

 - 3D (many thanks to Infinite Flight Studios for the code and Sickhead Games in taking the time to merge the code in).
 - New platforms: Windows 8, Windows Phone 8, OUYA, PlayStation Mobile (including Vita).
 - Custom Effects.
 - PVRTC support for iOS.
 - iOS supports compressed Songs.
 - Skinned Meshs.
 - VS2012 templates.
 - New Windows Installer.
 - New MonoDevelop Package/AddIn.
 - A LOT of bug fixes.
 - Closer XNA 4 compatibility.


## 2.5.1 Release - 6/18/2012

 - Updated android to use enumerations rather than hardocded ids as part of the Mono for Android 4.2 update.
 - Changed the Android video player to make use of the ViewView.
 - Corrected namespaces for SongReader and SoundEffectReader.
 - Updated the Keyboard mapping for android.
 - Added RectangleArrayReader.
 - Removed links to the third party GamePadBridge.
 - Added some missing mouseState operators.
 - Replaced all calls to DateTime.Now with DateTime.UtcNow.
 - Fixed SpriteFont rendering (again).
 - Added code to correclty dispose of Textures on all platforms.
 - Added some fixes for the sound on iOS.
 - Adding missing MediaQueue class.
 - Fixed Rectangle Intersect code.
 - Changed the way UserPrimitives work on windows.
 - Made sure the @2x file support on iOS works.
 - Updated project templates.
 - Added project templates for MacOS.
 - Fixed MonoDevelop.MonoGame AddIn so it works on Linux.
 

## 2.5 Release - 3/29/2012

### Fixes and Features
 - Minor fixes to the Networking stack to make it more reliable when looking for games.
 - SpriteBatch Fixes including making sure the matrix parameter is applied in both gles 1.1 and gles 2.0.
 - Updated IDrawable and IUpdatable interfaces to match XNA 4.0.
 - Fixed the Tick method.
 - Updated VideoPlayer constructor contract to match XNA 4.0.
 - Added Code to Lookup the Host Application Guid for Networking, the guid id is now pulled from the AssemblyInfo.cs if one is present.
 - Uses OpenAL on all platforms except Android.
 - Added Dxt5 decompression support.
 - Improves SpriteFont to conform more closely to XNA 4.0.
 - Moved DynamicVertexBuffer and DynamicIndexBuffer into its own files.

### iOS
 - Fixed Console.WriteLine problem.
 - Fixed loading of @2x Retina files.
 - Fixed Landscape Rendering.
 - Fixed Orientations changes correctly animate.
 - Fixed Guide.BeginShowKeyboardInput.
 - Fixed StorageDevice AOT compile problem.
 - Fixed SpriteBatch to respect matrices when drawn.
 - Fixed DoubleTap, improves touches in serial Game instances.
 - Fixed App startup in non-Portrait orientations.
 - Fixed UnauthorizedAccessException using TitleContainer.
 - Fixed a runtime JIT error that was occuring with List<AddJournalEntry<T>().
 - Guide.ShowKeyboard is not working.
 - App Backgrounding has regressed. A patch is already being tested in the develop branch and the fix will be rolled out as part of the v2.5.1.

### Android
 - Project Templates for MonoDevelop.
 - Fixed a few issues with Gestures.
 - Fixed the name of the assembly to be MonoGame.Framework.Android.
 - Fixed a Memory Leak in Texture Loading.
 - Force linear filter and clamp wrap on npot textures in ES2.0 on Android.
 - Added SetData and GetData support for Texture2D.
 - Guide.SignIn picks up the first email account on the phone.
 - CatapultWars does not render correctly under gles 1.1.

### MacOS X
 - SoundEffectInstance.Stop now works correctly.

### Linux
 - Project Templates for Visual Studio and MonoDevelop.
 - Fixed a bug when loading of Wav files.

### Windows
 - Project Templates for Visual Studio and MonoDevelop.
 - Fixed a bug when loading of Wav files.
 - Added Game.IsMouseVisible implementation for Windows.
 - Guide.SignIn picks up the logged in user.
 - Added a new Installer to install the MonoDevelop and / or Visual Studio Templates and binaries.


## 2.1 Release - 10/28/2011

### Features
 - Content Manager rewritten to use partial classes and implementation of cached assets that are loaded.  Greatly improves memory footprint.
 - Experimental support for GamePads and Joysticks.  Enhancements will be coming to integrate better for developers.
 - ContentReader improvements across the board.
 - Improved support for XACT audio.
 - StarterKits VectorRumble.

### iOS
 - Gesture support has been improved.
 - Better support for portrait to landscape rotations.
 - Fixed a rendering bug related to upsidedown portrait mode.
 - Better WaveBank support.
 - The Guide functionality is only available in iOS, for this release.

### Android
 - Updated to support Mono for Android 4.0.
 - Improvements to the Orientation Support.
 - Changed Sound system to use SoundPool.
 - Added Tap and DoubleTap Gesture Support.

### MacOS X
 - A lot of enhancements and fixes for Full Screen and Windowed control.
 - Cursor support fixed for IsMouseVisible.
 - Implementation of IsActive property and the events Activated and Deactivated.
 - First steps of DrawPrimitives, DrawUserPrimitives, DrawIndexedPrimitives.
 - Better WaveBank support.
 - Support for ApplyChanges() and setting the backbuffer and viewport sizes correctly.

### Linux
 - All new implementation which share quite a bit of code between MacOS X and Windows.
 - Added shader support via the Effects class.

### Windows
 - All new implementation which shares quite a bit of code between MacOS and Linux.


## 2.0 Release - 10/28/2011

 - Project renamed MonoGame.
 - Project moved to GitHub.
 - Support for Linux, Mac, Linux, and OpenGL on Windows.


## 0.7 Release - 12/2/2009

 - First stable release.
 - Originally named XnaTouch.
 - iPhone support only.
 - 2D rendering support.
 - Audio support.
 - Networking support.
 - Partial multitouch support.
 - Partial accelerometer support.
> #### NOTE: This code style standard for MonoGame is a work in progress and much of the code does not currently conform to these rules.  This is something that will be addressed by the core team.

# Introduction
As the MonoGame project gains more traction and becomes more widely used, we aim to provide a more professional and consistent look to the large amount of source now in the project.  It was a broadly supported decision by the core development team to follow the Microsoft coding guidelines (the default provided in Visual Studio's C# editor).  These coding guidelines listed below are based on a [MSDN blog post](http://blogs.msdn.com/b/brada/archive/2005/01/26/361363.aspx) from 2005 by Brad Abrams describing the internal coding guidelines at Microsoft, with some changes to suit our project.
# Coding Guidelines
## Tabs & Indenting
Tab characters (\0x09) should not be used in code. All indentation should be done with 4 space characters.
## Bracing
Open braces should always be at the beginning of the line after the statement that begins the block. Contents of the brace should be indented by 4 spaces. Single statements do not have braces. For example:
```
if (someExpression)
{
   DoSomething();
   DoAnotherThing();
}
else
   DoSomethingElse();
```

`case` statements should be indented from the switch statement like this:
```
switch (someExpression) 
{
   case 0:
      DoSomething();
      break;

   case 1:
      DoSomethingElse();
      break;

   case 2: 
      {
         int n = 1;
         DoAnotherThing(n);
      }
      break;
}
```

Braces are not used for single statement blocks immediately following a `for`, `foreach`, `if`, `do`, etc. The single statement block should always be on the following line and indented by four spaces. This increases code readability and maintainability.
```
for (int i = 0; i < 100; ++i)
    DoSomething(i);
```

## Single line property statements
Single line property statements can have braces that begin and end on the same line. This should only be used for simple property statements.  Add a single space before and after the braces.
```
public class Foo
{
   int bar;

   public int Bar
   {
      get { return bar; }
      set { bar = value; }
   }
}
```

## Commenting
Comments should be used to describe intention, algorithmic overview, and/or logical flow.  It would be ideal if, from reading the comments alone, someone other than the author could understand a function's intended behavior and general operation. While there are no minimum comment requirements (and certainly some very small routines need no commenting at all), it is best that most routines have comments reflecting the programmer's intent and approach.

Comments must provide added value or explanation to the code. Simply describing the code is not helpful or useful.
```
    // Wrong
    // Set count to 1
    count = 1;

    // Right
    // Set the initial reference count so it isn't cleaned up next frame
    count = 1;
```

### Copyright/License notice
Each file should start with a copyright notice. This is a short statement declaring the project name and copyright notice, and directing the reader to the license document elsewhere in the project. To avoid errors in doc comment builds, avoid using triple-slash doc comments.
```
// MonoGame - Copyright (C) The MonoGame Team
// This file is subject to the terms and conditions defined in
// file 'LICENSE.txt', which is part of this source code package.
```

### Documentation Comments
All methods should use XML doc comments. For internal dev comments, the `<devdoc>` tag should be used.
```
public class Foo 
{
    /// <summary>Public stuff about the method</summary>
    /// <param name="bar">What a neat parameter!</param>
    /// <devdoc>Cool internal stuff!</devdoc>
    public void MyMethod(int bar)
    {
        ...
    }
}
```

### Comment Style
The // (two slashes) style of comment tags should be used in most situations. Wherever possible, place comments above the code instead of beside it.  Here are some examples:
```
    // This is required for WebClient to work through the proxy
    GlobalProxySelection.Select = new WebProxy("http://itgproxy");

    // Create object to access Internet resources
    WebClient myClient = new WebClient();
```

## Spacing
Spaces improve readability by decreasing code density. Here are some guidelines for the use of space characters within code:

Do use a single space after a comma between function arguments.
```
Console.In.Read(myChar, 0, 1);  // Right
Console.In.Read(myChar,0,1);    // Wrong
```
Do not use a space after the parenthesis and function arguments.
```
CreateFoo(myChar, 0, 1)         // Right
CreateFoo( myChar, 0, 1 )       // Wrong
```
Do not use spaces between a function name and parentheses.
```
CreateFoo()                     // Right
CreateFoo ()                    // Wrong
```
Do not use spaces inside brackets.
```
x = dataArray[index];           // Right
x = dataArray[ index ];         // Wrong
```
Do use a single space before flow control statements.
```
while (x == y)                  // Right
while(x==y)                     // Wrong
```
Do use a single space before and after binary operators.
```
if (x == y)                     // Right
if (x==y)                       // Wrong
```
Do not use a space between a unary operator and the operand.
```
++i;                            // Right
++ i;                           // Wrong
```
Do not use a space before a semi-colon. Do use a space after a semi-colon if there is more on the same line.
```
for (int i = 0; i < 100; ++i)   // Right
for (int i=0 ; i<100 ; ++i)     // Wrong
```

## Naming
Follow all .NET Framework Design Guidelines for both internal and external members. Highlights of these include:
* Do not use Hungarian notation
* Do use an underscore prefix for member variables, e.g. "_foo"
* Do use camelCasing for member variables (first word all lowercase, subsequent words initial uppercase)
* Do use camelCasing for parameters
* Do use camelCasing for local variables
* Do use PascalCasing for function, property, event, and class names (all words initial uppercase)
* Do prefix interfaces names with "I"
* Do not prefix enums, classes, or delegates with any letter

The reasons to extend the public rules (no Hungarian, underscore prefix for member variables, etc.) is to produce a consistent source code appearance. In addition, the goal is to have clean, readable source. Code legibility should be a primary goal.

## File Organization
* Source files should contain only one public type, although multiple internal types are permitted if required
* Source files should be given the name of the public type in the file
* Directory names should follow the namespace for the class after `Framework`. For example, one would expect to find the public class `Microsoft.Xna.Framework.Graphics.GraphicsDevice` in **MonoGame.Framework\Graphics\GraphicsDevice.cs**
* Class members should be grouped logically, and encapsulated into regions (Fields, Constructors, Properties, Events, Methods, Private interface implementations, Nested types)
* Using statements should be before the namespace declaration.
```
using System;

namespace MyNamespace 
{
    public class MyClass : IFoo 
    {
        #region Fields
        int foo;
        #endregion

        #region Properties
        public int Foo { get { ... } set { ... } }
        #endregion

        #region Constructors
        public MyClass()
        {
            ...
        }
        #endregion

        #region Events
        public event EventHandler FooChanged { add { ... } remove { ... } }
        #endregion

        #region Methods
        void DoSomething()
        {
            ...
        }

        void FindSomething()
        {
            ...
        }
        #endregion

        #region Private interface implementations
        void IFoo.DoSomething()
        {
            DoSomething();
        }
        #endregion

        #region Nested types
        class NestedType
        {
            ...
        }
        #endregion
    }
}
```

# Useful Links
[C# Coding Conventions (MSDN)](http://msdn.microsoft.com/en-us/library/ff926074.aspx)
# Contributing to MonoGame

We're happy that you have chosen to contribute to the MonoGame project.

You are joining a group of hundreds of volunteers that have helped build MonoGame since 2009.  To organize these efforts, the MonoGame Team has written this simple guide to help you.

Please read this document completely before contributing.


## How To Contribute

MonoGame has a `master` branch for stable releases and a `develop` branch for daily development.  New features and fixes are always submitted to the `develop` branch.

If you are looking for ways to help, you should start by looking at the [Help Wanted tasks](https://github.com/mono/MonoGame/issues?q=is%3Aissue+is%3Aopen+label%3A%22Help+Wanted%22).  Please let us know if you plan to work on an issue so that others are not duplicating work.

The MonoGame project follows standard [GitHub flow](https://guides.github.com/introduction/flow/index.html).  You should learn and be familiar with how to [use Git](https://help.github.com/articles/set-up-git/), how to [create a fork of MonoGame](https://help.github.com/articles/fork-a-repo/), and how to [submit a Pull Request](https://help.github.com/articles/using-pull-requests/).

After you submit a PR, the [MonoGame build server](http://teamcity.monogame.net/?guest=1) will build your changes and verify all tests pass.  Project maintainers and contributors will review your changes and provide constructive feedback to improve your submission.

Once we are satisfied that your changes are good for MonoGame, we will merge it.


## Quick Guidelines

Here are a few simple rules and suggestions to remember when contributing to MonoGame.

* :bangbang: **NEVER** commit code that you didn't personally write.
* :bangbang: **NEVER** use decompiler tools to steal code and submit them as your own work.
* :bangbang: **NEVER** decompile XNA assemblies and steal Microsoft's copyrighted code.
* **PLEASE** try keep your PRs focused on a single topic and of a reasonable size or we may ask you to break it up.
* **PLEASE** be sure to write simple and descriptive commit messages.
* **DO NOT** surprise us with new APIs or big new features. Open an issue to discuss your ideas first.
* **DO NOT** reorder type members as it makes it difficult to compare code changes in a PR.
* **DO** try to follow our [coding style](CODESTYLE.md) for new code.
* **DO** give priority to the existing style of the file you're changing.
* **DO** try to add to our [unit tests](Test) when adding new features or fixing bugs.
* **DO NOT** send PRs for code style changes or make code changes just for the sake of style.
* **PLEASE** keep a civil and respectful tone when discussing and reviewing contributions.
* **PLEASE** tell others about MonoGame and your contributions via social media.


## Decompiler Tools

We prohibit the use of tools like dotPeek, ILSpy, JustDecompiler, or .NET Reflector which convert compiled assemblies into readable code.

There has been confusion on this point in the past, so we want to make this clear.  It is **NEVER ACCEPTABLE** to decompile copyrighted assemblies and submit that code to the MonoGame project.

* It **DOES NOT** matter how much you change the code.
* It **DOES NOT** matter what country you live in or what your local laws say.  
* It **DOES NOT** matter that XNA is discontinued.  
* It **DOES NOT** matter how small the bit of code you have stolen is.  
* It **DOES NOT** matter what your opinion is of stealing code.

If you did not write the code, you do not have ownership of the code and you shouldn't submit it to MonoGame.

If we find a contribution to be in violation of copyright, it will be immediately removed.  We will bar that contributor from the MonoGame project.


## Licensing

The MonoGame project is under the [Microsoft Public License](https://opensource.org/licenses/MS-PL) except for a few portions of the code.  See the [LICENSE.txt](LICENSE.txt) file for more details.  Third-party libraries used by MonoGame are under their own licenses.  Please refer to those libraries for details on the license they use.

We accept contributions in "good faith" that it isn't bound to a conflicting license.  By submitting a PR you agree to distribute your work under the MonoGame license and copyright.

To this end, when submitting new files, include the following in the header if appropriate:
```csharp
// MonoGame - Copyright (C) The MonoGame Team
// This file is subject to the terms and conditions defined in
// file 'LICENSE.txt', which is part of this source code package.
```

## Need More Help?

If you need help, please ask questions on our [community forums](http://community.monogame.net/) or come [chat on Gitter](https://gitter.im/mono/MonoGame).


Thanks for reading this guide and helping make MonoGame great!

 :heart: The MonoGame Team
<!--
# Please make sure that the issue is present in the
# develop branch of MonoGame before reporting
#
# You can download the development build installer from:
# http://www.monogame.net/downloads/
-->

<!-- Write your issue below -->





<!-- System stats -->

#### What version of MonoGame does the bug occur on:
- MonoGame 3.7

#### What operating system are you using:
- Windows

#### What MonoGame platform are you using:
<!-- e.g. DesktopGL, WindowsDX, WindowsUWP, Android -->
- DesktopGL
Microsoft Public License (Ms-PL)
MonoGame - Copyright © 2009-2020 The MonoGame Team

All rights reserved.

This license governs use of the accompanying software. If you use the software,
you accept this license. If you do not accept the license, do not use the
software.

1. Definitions

The terms "reproduce," "reproduction," "derivative works," and "distribution"
have the same meaning here as under U.S. copyright law.

A "contribution" is the original software, or any additions or changes to the
software.

A "contributor" is any person that distributes its contribution under this
license.

"Licensed patents" are a contributor's patent claims that read directly on its
contribution.

2. Grant of Rights

(A) Copyright Grant- Subject to the terms of this license, including the
license conditions and limitations in section 3, each contributor grants you a
non-exclusive, worldwide, royalty-free copyright license to reproduce its
contribution, prepare derivative works of its contribution, and distribute its
contribution or any derivative works that you create.

(B) Patent Grant- Subject to the terms of this license, including the license
conditions and limitations in section 3, each contributor grants you a
non-exclusive, worldwide, royalty-free license under its licensed patents to
make, have made, use, sell, offer for sale, import, and/or otherwise dispose of
its contribution in the software or derivative works of the contribution in the
software.

3. Conditions and Limitations

(A) No Trademark License- This license does not grant you rights to use any
contributors' name, logo, or trademarks.

(B) If you bring a patent claim against any contributor over patents that you
claim are infringed by the software, your patent license from such contributor
to the software ends automatically.

(C) If you distribute any portion of the software, you must retain all
copyright, patent, trademark, and attribution notices that are present in the
software.

(D) If you distribute any portion of the software in source code form, you may
do so only under this license by including a complete copy of this license with
your distribution. If you distribute any portion of the software in compiled or
object code form, you may only do so under a license that complies with this
license.

(E) The software is licensed "as-is." You bear the risk of using it. The
contributors give no express warranties, guarantees or conditions. You may have
additional consumer rights under your local laws which this license cannot
change. To the extent permitted under your local laws, the contributors exclude
the implied warranties of merchantability, fitness for a particular purpose and
non-infringement.

-------------------------------------------------------------------------------

The MIT License (MIT)
Portions Copyright © The Mono.Xna Team

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
# MonoGame

One framework for creating powerful cross-platform games.  The spiritual successor to XNA with thousands of titles shipped across desktop, mobile, and console platforms.  [MonoGame](http://www.monogame.net/) is a fully managed .NET open source game framework without any black boxes.  Create, develop and distribute your games your way.

[![Join the chat at https://discord.gg/tsuucV4](https://img.shields.io/discord/355231098122272778?color=%237289DA&label=MonoGame&logo=discord&logoColor=white)](https://discord.gg/tsuucV4) [![Join the chat at https://gitter.im/MonoGame/MonoGame](https://badges.gitter.im/MonoGame/MonoGame.svg)](https://gitter.im/MonoGame/MonoGame?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

 * [Build Status](#build-status)
 * [Supported Platforms](#supported-platforms)
 * [Support and Contributions](#support-and-contributions)
 * [Source Code](#source-code)
 * [Helpful Links](#helpful-links)
 * [License](#license)
 

## Build Status

Our [build server](http://teamcity.monogame.net/?guest=1) builds, tests, and packages the latest MonoGame changes.  The table below shows the current build status for the develop branch.

| Name  | Status |
|:---|--------|
| Build Windows, Web, and Android | [![Build Status](http://teamcity.monogame.net/app/rest/builds/buildType:MonoGame_DevelopWin/statusIcon)](http://teamcity.monogame.net/viewType.html?buildTypeId=MonoGame_DevelopWin&guest=1) |
| Build Mac, iOS, and Linux | [![Build Status](http://teamcity.monogame.net/app/rest/builds/buildType:MonoGame_DevelopMac/statusIcon)](http://teamcity.monogame.net/viewType.html?buildTypeId=MonoGame_DevelopMac&guest=1) |
| Windows Tests | [![Build Status](http://teamcity.monogame.net/app/rest/builds/buildType:MonoGame_TestWindows/statusIcon)](http://teamcity.monogame.net/viewType.html?buildTypeId=MonoGame_TestWindows&guest=1) |
| Mac Tests | [![Build Status](http://teamcity.monogame.net/app/rest/builds/buildType:MonoGame_TestMac/statusIcon)](http://teamcity.monogame.net/viewType.html?buildTypeId=MonoGame_TestMac&guest=1) |


## Supported Platforms

We support a growing list of platforms across the desktop, mobile, and console space.  If there is a platform we don't support, please [make a request](https://github.com/MonoGame/MonoGame/issues) or [come help us](CONTRIBUTING.md) add it.

 * Desktop PCs
   * Windows 10 Store Apps (UWP)
   * Windows Win32 (OpenGL & DirectX)
   * Linux (OpenGL)
   * Mac OS X (OpenGL)
 * Mobile/Tablet Devices
   * Android (OpenGL)
   * iPhone/iPad (OpenGL)
   * Windows Phone 10 (UWP)
 * Consoles (for registered developers)
   * PlayStation 4
   * PlayStation Vita
   * Xbox One (both UWP and XDK)
   * Nintendo Switch
   * Google Stadia
 * Other
   * tvOS (OpenGL)


## Support and Contributions

If you think you have found a bug or have a feature request, use our [issue tracker](https://github.com/MonoGame/MonoGame/issues). Before opening a new issue, please search to see if your problem has already been reported.  Try to be as detailed as possible in your issue reports.

If you need help using MonoGame or have other questions we suggest you post on our [community forums](http://community.monogame.net).  Please do not use the GitHub issue tracker for personal support requests.

If you are interested in contributing fixes or features to MonoGame, please read our [contributors guide](CONTRIBUTING.md) first.

### Subscription

If you'd like to help the project by supporting us financially, consider supporting us via a subscription for the price of a monthly coffee.

Money goes towards hosting, new hardware and if enough people subscribe a dedicated developer.

There are several options on our [Donation Page](http://www.monogame.net/donate/).


## Source Code

The full source code is available here from GitHub:

 * Clone the source: `git clone https://github.com/MonoGame/MonoGame.git`
 * Set up the submodules: `git submodule update --init`
 * Open the solution for your target platform to build the game framework.
 * Open the Tools solution for your development platform to build the pipeline and content tools.

For the prerequisites for building from source, please look at the [Requirements](REQUIREMENTS.md) file.

A high level breakdown of the components of the framework:

 * The game framework is found in [MonoGame.Framework](MonoGame.Framework).
 * The content pipeline is located in [MonoGame.Framework.Content.Pipeline](MonoGame.Framework.Content.Pipeline).
 * Project templates are in [Templates](Templates).
 * See [Tests](Tests) for the framework unit tests.
 * See [Tools/Tests](Tools/MonoGame.Tools.Tests) for the content pipeline and other tool tests.
 * [mgcb](Tools/MonoGame.Content.Builder) is the command line tool for content processing.
 * [mgfxc](Tools/MonoGame.Effect.Compiler) is the command line effect compiler tool.
 * The [mgcb-editor](Tools/MonoGame.Content.Builder.Editor) tool is a GUI frontend for content processing.


## Helpful Links

 * The official website is [monogame.net](http://www.monogame.net).
 * Our [issue tracker](https://github.com/MonoGame/MonoGame/issues) is on GitHub.
 * Use our [community forums](http://community.monogame.net/) for support questions.
 * You can [chat live](https://gitter.im/mono/MonoGame?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) with the core developers and other users.
 * The [official documentation](http://www.monogame.net/documentation/) is on our website.
 * Download release and development [installers and packages](http://www.monogame.net/downloads/).
 * Follow [@MonoGameTeam](https://twitter.com/monogameteam) on Twitter.

## License

The MonoGame project is under the [Microsoft Public License](https://opensource.org/licenses/MS-PL) except for a few portions of the code.  See the [LICENSE.txt](LICENSE.txt) file for more details.  Third-party libraries used by MonoGame are under their own licenses.  Please refer to those libraries for details on the license they use.
Windows Requirements
====================

Mac Requirements
================

Linux Requirements
==================

The following is the list of packages needed to compile MonoGame from Linux:
 * monodevelop
 * libopenal-dev
 * referenceassemblies-pcl
 * ttf-mscorefonts-installer
 * gtk-sharp3

If on Ubuntu, you can install the packages with the following commands:
```Shell
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list
sudo apt-get update
sudo apt-get install -y monodevelop libopenal-dev referenceassemblies-pcl ttf-mscorefonts-installer gtk-sharp3
```

If on Fedora, you can install the packages with the following commands:
```Shell
sudo rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
sudo dnf config-manager --add-repo http://download.mono-project.com/repo/centos/
sudo dnf update
sudo dnf install -y monodevelop referenceassemblies-pcl mscore-fonts gtk-sharp3
```
# TeamCity Settings

This folder contains settings for the MonoGame TeamCity build process.

You can edit the settings in IntelliJ Idea, open the pom.xml and select the 'Open as a project' option.

You can also edit this manually in any text editor in the settings.kts. The TeamCity server will validate the changes and give you build errors if something is incorrect.

The documentation to the Kotlin language for TeamCity is here:  https://www.jetbrains.com/help/teamcity/kotlin-dsl.html

Welcome to the MonoGame game library documentation hub.

This area of the site contains the documentation on the API of MonoGame as well as how to use it to create great games.
Note that this is a work in progress so there will be gaps in the documentation coverage. 

If you cannot find what you need here you can also look at the [Microsoft XNA documentation](https://msdn.microsoft.com/en-us/library/bb200104.aspx). MonoGame is API compatible
with [XNA](https://msdn.microsoft.com/en-us/library/bb203940.aspx) even down to the namespaces. So usually what works for XNA will work for MonoGame too. 

Note that this documentation hub is built from the source code on every commit to the development branch. As such 
it applies to the development builds available on the [Downloads](http://www.monogame.net/downloads) page. This may include new features which may
not be available in the current stable release 

### We Need Your Help!

Truly great open source projects require high quality documentation.  This is call for volunteers to help us make the MonoGame documentation truly great.  If you can help write tutorials, guides, code snippets, reference docs, video walkthroughs or just any improvement to our current documentation we could use your help!

Check out the [README on GitHub](https://github.com/mono/MonoGame/blob/develop/Documentation/README.md) or [talk with us on the community site](http://community.monogame.net/t/lets-improve-the-monogame-documentation/916) to learn how to help!
# External Links

Links to several useful reference sites related to MonoGame.

- [Microsoft XNA Documentation](http://msdn.microsoft.com/en-us/library/bb203940.aspx)
- [OpenGL 4.3 Reference Card](http://www.khronos.org/files/opengl43-quick-reference-card.pdf)
- [OpenGL ES 2.0 Reference Card](http://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf)
- [WebGL Reference Card](http://www.khronos.org/files/webgl/webgl-reference-card-1_0.pdf)
- [Collada Specification](http://www.khronos.org/collada/)
- [Valve's Guide to Porting to Linux](https://developer.nvidia.com/sites/default/files/akamai/gamedev/docs/Porting%20Source%20to%20Linux.pdf)
# Migrating to MonoGame 3.8

Previously MonoGame installed on your machine through an installer, but from 3.8 onwards everything is installed through NuGet packages.

## WindowsDX and DesktopGL

WindowsDX and DesktopGL templates now use SDK-style projects.
To migrate old projects we recommend creating a new project with the 3.8+ templates and
copying the csproj to your project folder. Make sure you back up your old project.
For more information about SDK-style projects see the [docs](https://docs.microsoft.com/en-us/dotnet/core/tools/csproj).

## Other Platforms

To migrate open up your project file in a text editor.
The reference to the MonoGame assembly looks like this:

```xml
</ItemGroup>
    <Reference Include="MonoGame.Framework">
        <HintPath>$(MonoGameInstallDirectory)\MonoGame\v3.0\Assemblies\{Platform}\MonoGame.Framework.dll</HintPath>
    </Reference>
</ItemGroup>
```

The task to build your content is imported at the end of the project file like this:

```xml
<Import Project="$(MSBuildExtensionsPath)\MonoGame\v3.0\MonoGame.Content.Builder.targets" />
```

You can remove these references and add a reference to the MonoGame NuGet packages instead.

```xml
<ItemGroup>
    <PackageReference Include="MonoGame.Framework.{Platform}" Version="3.8.0" />
    <PackageReference Include="MonoGame.Content.Builder.Task" Version="3.8.0" />
</ItemGroup>
```

## Tooling

MonoGame tools are now distributed as [.NET Core Tools](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).
You do not need the tools to build content for your games. The templates reference the `MonoGame.Content.Builder.Task`
NuGet package that automatically builds your content when building your game.

- [MonoGame Content Builder](tools/mgcb.md) (MGCB): `dotnet tool install -g dotnet-mgcb`
- [MonoGame Effect Compiler](tools/2mgfx.md) (MGFXC; previously 2MGFX): `dotnet tool install -g dotnet-mgfxc`
- [MGCB Editor](tools/pipeline.md) (Previously Pipeline Tool): `dotnet tool install -g dotnet-mgcb-editor`

After installing `mgcb-editor` run `dotnet mgcb-editor --register` to register MGCB Editor as the default app for mgcb
files. This currently does not work on Mac.
Once your game is ready to be published, it is recommended that you package it properly for consumption by players.

## Desktop games

To publish desktop games, it is recommended that you build your project as a [self-contained](https://docs.microsoft.com/en-us/dotnet/core/deploying/#publish-self-contained) .NET Core app. As such, your game will require absolutely no external dependencies and should run out-of-the-box as-is.

### Building and packaging for Windows

From the .NET Core CLI:

`dotnet publish -c Release -r win-x64 /p:PublishReadyToRun=false /p:TieredCompilation=false --self-contained`

You can then zip the content of the publish folder and distribute the archive as-is.

If you are targeting WindowsDX, note that players will need [the DirectX June 2010 runtime](https://www.microsoft.com/en-us/download/details.aspx?id=8109) to be installed on their machine for audio and gamepads to work properly.

### Building and packaging for Linux

From the .NET Core CLI:

`dotnet publish -c Release -r linux-x64 /p:PublishReadyToRun=false /p:TieredCompilation=false --self-contained`

You can then archive the content of the publish folder and distribute the archive as-is.

We recommend using the .tar.gz archiving format to preserve the execution permissions.

### Build and packaging for macOS

From the .NET Core CLI:

`dotnet publish -c Release -r osx-x64 /p:PublishReadyToRun=false /p:TieredCompilation=false --self-contained`

We recommend you distribute your game as an [application bundle](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html). Application bundles are directories with the following file structure:

```
YourGame.app                    (this is your root folder)
    - Contents
        - Resources
            - Content           (this is where all your content and XNB's should go)
            - YourGame.icns     (this is your app icon, in ICNS format)
        - MacOS                 (this is where your game belongs, except for content files)
    - Info.plist                (the metadata of your app)
```

The Info.plist file is a standard macOS file containing metadata about your game. Here's an example file with required and recommended values set:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>en</string>
    <key>CFBundleExecutable</key>
    <string>YourGame</string>
    <key>CFBundleIconFile</key>
    <string>YourGame</string>
    <key>CFBundleIdentifier</key>
    <string>com.your-domain.YourGame</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>YourGame</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleSignature</key>
    <string>FONV</string>
    <key>CFBundleVersion</key>
    <string>1</string>
    <key>LSApplicationCategoryType</key>
    <string>public.app-category.games</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
    <key>NSHumanReadableCopyright</key>
    <string>Copyright © 2020</string>
    <key>NSPrincipalClass</key>
    <string>NSApplication</string>
</dict>
</plist>
```

For more information about Info.plist files, see the [documentation](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html).

After completing these steps, your .app folder should appear as an executable application on macOS.

For archiving, we recommend using the .tar.gz format to preserve the execution permissions.

### Special notes about .NET Core parameters

.NET Core proposes several parameters when publishing apps that may sound helpful, but have many issues when it comes to games (because they were never meant for games in the first place, but for small lightweight applications).

**ReadyToRun (R2R)**

[ReadyToRun](https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-core-3-0#readytorun-images) is advertised as improving application startup time, but slightly increasing binary size. We recommend not using it for games, because it produces micro stutters when your game is running.

Ready2Run code is of low quality and makes the Just-In-Time compiler (JIT) trigger regularly to promote the code to a higher quality. Whenever the JIT runs, it produces potentially very visible stutters.

Disabling ReadyToRun solves this issue (at the cost of a slightly longer startup time, but typically very negligible).

ReadyToRun is disabled by default. You can configure it by setting the `PublishReadyToRun` property in your csproj file. MonoGame templates for .NET Core projects explicitly set this to `false`.

**Tiered compilation**

[Tiered compilation](https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-core-3-0#tiered-compilation) is a companion system to ReadyToRun and works on the same principle to enhance startup time. We suggest disabling it to avoid any stutter while your game is running.

Tiered compilation is **enabled by default**. To disable it set the `TieredCompilation` property to `false` in your csproj.
MonoGame templates for .NET Core projects disable tiered compilation.

**SingleFilePublish**

SingleFilePublish packages your game into a single executable file with all dependencies and content integrated.

While it sounds convenient, be aware that it's not magical and is in fact a hidden self-extracting zip archive. As such, it may make app startup take **a lot** longer if your game is large, and may fail to launch on systems where user permissions don't allow extracting files (or if there is not enough storage space available).

We recommend not using it for better compatibility across systems.

## Windows Store games

Please refer to the [Windows Store documentation](https://docs.microsoft.com/en-us/windows/uwp/publish/).

## Mobile games

Please refer to the Xamarin documentation:

- [Android](https://docs.microsoft.com/en-us/xamarin/android/deploy-test/publishing/)

- [iOS](https://docs.microsoft.com/en-us/xamarin/ios/deploy-test/app-distribution/app-store-distribution/publishing-to-the-app-store?tabs=windows)
# Porting from XNA to MonoGame

MonoGame implements the same [API](https://en.wikipedia.org/wiki/Application_programming_interface)
as XNA 4.0. That means you usually do not have to change your game code to port from XNA to
MonoGame. There are however some exceptions and some things to keep in mind when porting to MonoGame.

If your game targets XNA 3.1, you might want to use this archived migration cheatsheet to upgrade
to 4.0: [http://www.nelxon.com/blog/xna-3-1-to-xna-4-0-cheatsheet/](https://web.archive.org/web/20110217153321/http://www.nelxon.com/blog/xna-3-1-to-xna-4-0-cheatsheet/).

## Missing/removed API

- The Storage namespace was removed due to portability issues (short discussion [here](https://github.com/MonoGame/MonoGame/issues/4311)).
- GamerServices is not included in the main assembly. This part of MonoGame is not very well maintained due to low usage and difficulties
in providing the GamerServices API for different platforms.

## Effects

MonoGame does not use the legacy fxc compiler for effects that XNA used. Instead MonoGame uses the DX11 compiler.
The way MonoGame handles shaders imposes some restrictions and causes some caveats in what is and is not supported.
This is all documented in the [custom effects](content/custom_effects.md) documentation page.

## Half pixel offset

XNA uses the DirectX9 graphics API. MonoGame uses the newer DX11 API for DirectX platforms.
DirectX9 interprets UV coordinates differently from other graphics API's. This is typically
referred to as the half-pixel offset. 
MonoGame supports replicating XNA behavior (currently only on OpenGL platforms) by setting
the `PreferHalfPixelOffset` flag in `GraphicsDeviceManager` to `true`. This flag is
set to `false` by default to encourage users to use the modern style of pixel addressing.
DirectX platforms will ignore setting the `PreferHalfPixelOffset` flag and will
always render with a half pixel offset compared to XNA. This is usually not noticeable.

This value is passed to `UseHalfPixelOffset` in `GraphicsDevice`. If `UseHalfPixelOffset`
is `true`, you have to add half-pixel offset to a Projection matrix.

`SpriteBatch` rendering is not affected by the flag. Regardless of what value the flag has,
`SpriteBatch` will render things exactly the same as in XNA.

If you migrated your game from XNA and some things seem blurred out or very slightly offset,
you may want to try to enable the `PreferHalfPixelOffset` flag.
THIS IS A WORK IN PROGRESS!

# MonoGame Documentation
This is the source for the [documentation published on MonoGame.net](http://www.monogame.net/documentation/).  It is rebuilt when the code changes and is published nightly to the website.

## General Rules
The following rules must be observed at all times when contributing documentation to the MonoGame project.

 - Write in a neutral, technical tone.
 - Avoid humor, personal opinions, and colloquial language.
 - **Never** plagiarize any documentation from another source.
 - Do not use automatic documentation tools as they are ineffective. 

Breaking these rules can result in your contribution being rejected.

## Getting Started
You can create and edit documentation right from the web browser without needing to install Git or ever leave the GitHub site.

 - [Fork the MonoGame repo](https://help.github.com/articles/fork-a-repo/).
 - [Create a new branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/) from `develop` and make your changes only in that branch.
 - [Create a new file](https://help.github.com/articles/creating-new-files/) or [edit an existing one](https://help.github.com/articles/editing-files-in-your-repository/) using the GitHub markup editor.
 - [Submit pull requests](https://help.github.com/articles/creating-a-pull-request/) early and often to merge your documentation changes.

## Style Guide
Review the following expectations before contributing any documentation.

### Manuals, Guides, and Tutorials
TODO!

### API Reference 
The API reference documentation is a big part of the documentation effort for MonoGame.  The documentation is written in the [C# XML format](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/xmldoc/xml-documentation-comments) and is inline to the MonoGame source code. The final web pages with API documentation are generated using [SharpDoc](https://github.com/xoofx/SharpDoc).

#### Every Word Should Contain Value
Every word in the reference documentation should provide information beyond the API itself.  Documentation that only rehashes or rephrases what is already apparent in the class, method, parameter, or property name has zero value and wastes time for both the writer and reader.

#### The First Sentence Is the Most Important
There is no guarantee that the reader will read beyond the first sentence of the reference documentation.  This is why that first sentence is the most important and should convey the most key piece of information.  Take your time to write the most concise and clear first sentence possible.  This helps users tremendously and goes a long way towards having great documentation.

#### Surface Information Hidden in the Code
Being inline with the code allows you to easily look for critical information within it that the user might not know from looking at the API alone.  Take your time to explore inner method calls and platform specific sections of the code.  The time to write the documentation is once you feel you fully understand the code you are documenting.  If you don't feel you understand the code then leave the documentation for someone else to write.

#### Documentation Is Referenced Not Read
Remember that the user is searching for an answer for a specific question.  It is your job to predict these questions and provide them clear answers.


## License
All documentation contributed to the MonoGame project is subject to the [Creative Commons Attribution-NonCommercial-ShareAlike](http://creativecommons.org/licenses/by-nc-sa/4.0/) license.  By contributing you are agreeing to the terms of that license.

<p align="center"><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">MonoGame Documentation</span> by the <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.monogame.net" property="cc:attributionName" rel="cc:attributionURL">MonoGame Team</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike License</a>.</p>
# MonoGame Samples & Demos

Samples and Demos of MonoGame projects can be found at the following locations:

## [Official MonoGame Samples](https://github.com/MonoGame/MonoGame.Samples)

These are the official samples that contain the following:

- Platformer 2D
- SpaceWar
- NeonShooter

## [MonoGame.Extended Samples](https://github.com/craftworkgames/MonoGame.Extended)

MonoGame.Extended is an extension for MonoGame that makes it easier to make games.  They have [demos](https://github.com/craftworkgames/MonoGame.Extended/tree/develop/Source/Demos) and [games](https://github.com/craftworkgames/MonoGame.Extended/tree/develop/Source/Games) that can be tried out.

## [CartBlanche's Samples](https://github.com/CartBlanche/MonoGame-Samples)

This is a large library of MonoGame samples covering a large range of topics, including:

- Physics
- P2P Networking
- Textures
- Shaders
It also includes games such as:
- Tetris
- Pacman
- Role Playing Game

### Related

[Tutorials](tutorials.md)
# Tutorials

Links to various tutorials and articles to help you get started with MonoGame.

## RB Whitaker's MonoGame Tutorials

- [1 - C# Crash Course](http://rbwhitaker.wikidot.com/c-sharp-tutorials)
- [2 - Getting started](http://rbwhitaker.wikidot.com/monogame-getting-started-tutorials)
- [3 - 2D tutorials](http://rbwhitaker.wikidot.com/monogame-2d-tutorials)
- [4 - 3D tutorials](http://rbwhitaker.wikidot.com/monogame-3d-tutorials)
- [Extra - XNA tutorials](http://rbwhitaker.wikidot.com/xna-tutorials)

## Microsoft

Tara Walker's “Building a Shooter Game” tutorial series.

- [Part 1: Overview, Installation, MonoGame 3.0 Project Creation](https://docs.microsoft.com/en-us/archive/blogs/tarawalker/windows-8-game-development-using-c-xna-and-monogame-3-0-building-a-shooter-game-walkthrough-part-1-overview-installation-monogame-3-0-project-creation)
- [Part 2: Creating the Shooter/Player Asset of the Game](https://docs.microsoft.com/en-us/archive/blogs/tarawalker/windows-8-game-development-using-c-xna-and-monogame-3-0-building-a-shooter-game-walkthrough-part-2-creating-the-shooterplayer-asset-of-the-game)
- [Part 3: Updating Graphics using Content Pipeline with MonoGame](https://docs.microsoft.com/en-us/archive/blogs/tarawalker/windows-8-game-development-using-c-xna-and-monogame-3-0-building-a-shooter-game-walkthrough-part-3-updating-graphics-using-content-pipeline-with-monogame)
- [Part 4: Adding and Processing Player (User) Input](https://docs.microsoft.com/en-us/archive/blogs/tarawalker/windows-8-game-development-using-c-xna-and-monogame-3-0-building-a-shooter-game-walkthrough-part-4-adding-and-processing-player-user-input)
- [Part 5: Animating the Player/Ship and Creating a Parallaxing Background](https://docs.microsoft.com/en-us/archive/blogs/tarawalker/windows-8-game-development-using-c-xna-and-monogame-3-0-building-a-shooter-game-walkthrough-part-5-animating-the-playership-and-creating-a-parallaxing-background)
- [Part 6: Creating Enemies and Detecting Collisions](https://docs.microsoft.com/en-us/archive/blogs/tarawalker/windows-8-game-development-using-c-xna-and-monogame-3-0-building-a-shooter-game-walkthrough-part-6-creating-enemies-and-detecting-collisions)
- [Part 7: Creating Projectiles and Detecting Collisions](http://chrisongames.blogspot.com/2014/12/windows-8-game-development-using-c-xna.html)
- [Part 8: Creating Explosions using Sprite Animations](http://chrisongames.blogspot.com/2015/02/windows-8-game-development-using-c-xna.html)
- [Part 9: Adding Sound Effects and Game Music](http://chrisongames.blogspot.com/2015/12/windows-810-game-development-using-c.html)

## Neil Danson's F# series

- [Part 1 - MacOS](http://neildanson.wordpress.com/2013/07/30/f-and-monogame/)
- [Part 2 - Android](http://neildanson.wordpress.com/2013/07/31/f-and-monogame-part-2-android/)
- [Part 3 - iOS](http://neildanson.wordpress.com/2013/07/31/f-and-monogame-part-3-ios/)
- [Part 4 - Content Pipeline](http://neildanson.wordpress.com/2013/08/13/f-and-monogame-part-4-content-pipeline/)

## Others

- [A collection of tutorials, libraries and more, many of which are MonoGame related](https://github.com/UnterrainerInformatik/GameDevelopmentLinks)
- [How to create animations and sprite sheets for MonoGame](https://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-and-animations-with-monogame)
- [Making a platformer in F# with MonoGame](http://bruinbrown.wordpress.com/2013/10/06/making-a-platformer-in-f-with-monogame/)
- [XNA 4.0 Shader Programming / HLSL](http://digitalerr0r.wordpress.com/tutorials/)
- [Using Spine with MonoGame - by Randolph Burt (Randeroo)](http://randolphburt.co.uk/2013/03/30/dragons-and-dancing-crabs/)
- [Mac porting series](http://benkane.wordpress.com/2012/01/20/the-great-porting-adventure-day-8/)
- [Porting a Windows Phone 7 Game to Android](http://warrenburch.blogspot.co.uk/2011/12/porting-windows-phone-7-game-to-android.html)
- [A series on embedding MonoGame/WinGL into WinForms](http://jaquadro.com/2013/03/bringing-your-xna-winforms-controls-to-monogame-opengl/)
- [French articles about MonoGame on Linux, Windows and Windows 8](http://www.demonixis.net/blog/category/tutoriels/tuto-xna/)
- [Dark Genesis Blog](http://darkgenesis.zenithmoon.com/tag/monogame/)
- [MonoGame "Hello World" on Mac OS X and Xamarin Studio](http://jaquadro.com/2013/09/monogame-hello-world-on-mac-os-x-and-xamarin-studio/)
- [Solving Resolution Independent Rendering And 2D Camera Using Monogame](http://blog.roboblob.com/2013/07/27/solving-resolution-independent-rendering-and-2d-camera-using-monogame/)
- [XNA is Dead; Long Live the New XNA, MonoGame](http://www.codemag.com/Article/1411081)
- [Make Santa Jump - Making an endless runner game in F# using MonoGame](http://timjones.tw/blog/archive/2014/12/28/make-santa-jump-game-in-fsharp-using-monogame)
- [Running MonoGame on Android Wear](http://crossplatform.io/running-monogame-on-android-wear/)

## Video Tutorials

- [CodingMadeEasy RPG Tutorial](http://www.youtube.com/watch?feature=player_embedded&v=agt9-J9RPZ0)
- [Psuedo Games Tutorials](http://www.youtube.com/watch?feature=player_embedded&v=BwtQn02oy6A)
- [Desenvolvendo jogos multiplataforma em C# com MonoGame - Alexandre Chohfi (Portuguese)](http://channel9.msdn.com/Blogs/MSDN-Brasil-Cursos-de-Desenvolvimento/Desenvolvendo-jogos-multiplataforma-em-C-com-MonoGame)
- [Desenvolvimento de jogos para Windows 8 com XNA - Alexandre Chohfi (Portuguese)](https://www.youtube.com/watch?v=gM5pRnYV1tA)
- [Batholith Entertainment Game dev tutorials](https://www.youtube.com/playlist?list=PLZ6ofHM1rvK8lQSoKX1USZstM-ZXikFHp)
# TrueType fonts

MonoGame supports more than one method of using fonts, the following is an explanation of how to use TrueType fonts.

## Using TrueType Fonts with MonoGame

To be able to use a truetype font, MonoGame requires the truetype font file and a .spritefont file.
Truetype fonts may be installed on the system, or added to the project manually using your IDE in the same directory as the .spritefont file.

1. Create the .spritefont file.

  ![Adding TTF fonts step 1](~/images/adding_ttf_fonts_step_1.PNG)

  ![Adding TTF fonts step 2](~/images/adding_ttf_fonts_step_2.PNG)

2. Open the newly created .spritefont file in your text editor of choice, find this line and change it to your selected .ttf font.
If the font is installed on the system, just type the name of the font.

```xml
<FontName>Arial</FontName>
```

## Usage Example

Make a class variable of type Spritefont

```csharp
SpriteFont font;
```

Load the font in the LoadContent function

```csharp
font = myGame.Content.Load<SpriteFont>("Fonts/myFont")
```

Draw any text in the Draw function

```csharp
spriteBatch.Begin();
// Finds the center of the string in coordinates inside the text rectangle
Vector2 textMiddlePoint = font.MeasureString(text) / 2;
// Places text in center of the screen
Vector2 position = new Vector2(myGame.Window.ClientBounds.Width / 2, myGame.Window.ClientBounds.Height / 2);
spriteBatch.DrawString(font, "MonoGame Font Test", position, Color.White, 0, textMiddlePoint, 1.0f, SpriteEffects.None, 0.5f)
spriteBatch.End();
```

If you want to know more, please refer to the [API Documentation](xref:Microsoft.Xna.Framework).

# Adding Content

A big part of your game is your content.  This includes standard files like textures, sound effects, music, videos, and custom effects as well as custom content like level and enemy files.

MonoGame implements its own content pipeline for transforming your unoptimized assets into platform optimized content.  This is critical in building a game which runs as fast as possible under tight resource constraints.

This section will cover the following topics:

- What is Game Content
- [Using MGCB Editor](using_pipeline_tool.md)
- [Using TrueType Fonts](adding_ttf_fonts.md)
- [Custom Effects](custom_effects.md)
- Custom Content Types
# Effects

A core element of Microsoft XNA is the effect system which is used for all rendering.

For MonoGame we have the burden of supporting stock and custom effects for desktop GLSL, mobile GLSL, DirectX HLSL, and custom formats like that of the PlayStation Mobile.  There currently is no effect system or shader language that supports all the platforms we require, forcing us to build a new custom effect system.

## MGFX

MGFX is MonoGame's own "FX" runtime and tools which with the following core goals:

* Support a similar technique, passes, shaders structure as Microsoft FX files.
* Have a textual format for ease of editing.
* Have a compiled and optimized binary format for runtime use.
* Be cross-platform and support multiple shader languages and bytecodes.
* Easy to extend for future platforms and features.

## Stock Effects

MonoGame has the following effects built-in and fully supported on current platforms:

* SpriteEffect
* BasicEffect
* AlphaTestEffect
* DualTextureEffect
* EnvironmentMapEffect
* SkinnedEffect

Under the hood these effects use the same system and tools as one would for a custom Effect.  The source and pre-compiled versions of these effects can be found in the ['MonoGame.Framework\Graphics\Effect\Resources'](https://github.com/MonoGame/MonoGame/tree/develop/MonoGame.Framework/Graphics/Effect/Resources) folder.

If your game requires an extra little bit of performance you can easily hand edit the existing effects to remove unnecessary features or optimize for specific hardware and rebuild them with the MGFX tool.

## Custom Effects

To use a custom effect with MonoGame you must do one of the following (not both):

* Run the effect file through the [MonoGame Effect content processor](~/articles/tools/mgcb.md) for loading via the `ContentManager` (Recommended).
* Process your effect file with the [MGFXC tool](~/articles/tools/2mgfx.md) and load them yourself at runtime.

## Effect Writing Tips

These are some tips for writing or converting effects for use with MonoGame.

* The supported shader models when targeting DX are the following:
  * `vs_4_0_level_9_1` and `ps_4_0_level_9_1`
  * `vs_4_0_level_9_3` and `ps_4_0_level_9_3`
  * `vs_4_0` and `ps_4_0` (requires `HiDef` `GraphicsProfile` at runtime)
  * `vs_4_1` and `ps_4_1` (requires `HiDef` `GraphicsProfile` at runtime)
  * `vs_5_0` and `ps_5_0` (requires `HiDef` `GraphicsProfile` at runtime)
* When targeting GL platforms we automatically translate FX files to GLSL using a library called [MojoShader](http://icculus.org/mojoshader/).  The supported feature levels are the following:
  * `vs_2_0` and `ps_2_0`
  * `vs_3_0` and `ps_3_0`
* You can use preprocessor checks to add conditional code or compilation depending on defined symbols. MonoGame defines the following symbols when compiling effects:
  * `2MGFX`
  * `HLSL` and `SM4` for DirectX
  * `OpenGL` and `GLSL` for OpenGL
  
  As an example, you can conditionally set shader models depending on the platform with the following code:

  ```hlsl
  #if OPENGL
      #define VS_SHADERMODEL vs_3_0
      #define PS_SHADERMODEL ps_3_0
  #else
      #define VS_SHADERMODEL vs_4_0_level_9_1
      #define PS_SHADERMODEL ps_4_0_level_9_1
  #endif
  
  technique
  {
      pass
      {
          VertexShader = compile VS_SHADERMODEL MainVS();
          PixelShader = compile PS_SHADERMODEL MainPS();
      }
  };
  ```

Custom symbols can be defined from the [MGCB Editor](~/articles/tools/pipeline.md) or via [MGFXC](~/articles/tools/2mgfx.md).

* Make sure the pixel shaders inputs **exactly match** the vertex shader outputs so the parameters are passed in the correct registers. The parameters need to have the same size and order. Omitting parameters might not break compilation, but can cause unexpected results.
* Note that on GL platforms default values on Effect parameters do not work.  Either set the parameter from code or use a real constant like a #define.
* The effect compiler is aggressive about removing unused parameters, be sure the parameters you are setting are actually used.
* Preshaders are not supported.
* If you think you've found a bug porting a shader, [please let us know](https://github.com/MonoGame/MonoGame/issues).
# Localization

Localization is an important part of any game. While it can be possible to design a
game that is region independent, its quite hard. At some point you will need to
produce localized text and graphics.

MonoGame has a simple localization system built in. If you want to develop your own
system you are still able to do so. But the default system should be good enough for
most use cases.

## Creating resx files

MonoGame runs on .net/Mono on most platforms. Localization is handled by those platforms
via the use of resx files. There are walkthroughs on [MSDN](https://msdn.microsoft.com/en-us/library/aa992030(v=vs.100).aspx)
which walk you through the process. A simplified version is presented here.

Create a .resx file in the IDE e.g Foo.resx and add it to your game project. Note this needs to be added to the
main app projects. The Foo.resx file should have an Action of EmbeddedResouce and a Generator value of ResXFileCodeGenerator.
There is a snippet from the .csproj

```xml
<EmbeddedResource Include="Foo.resx">
  <Generator>ResXFileCodeGenerator</Generator>
  <LastGenOutput>Foo.Designer.cs</LastGenOutput>
</EmbeddedResource>
```

Add any string resources to that file. These are in the form of a Key/Value pair. You can use the built-in editor
or manually edit the .resx file by hand. It's an xml file so you can view the contents easily.

```xml
<data name="Wall_Style" xml:space="preserve">
  <value>Wall Style : {0}</value>
</data>
```

What happens when the resx is processed by the generator and produces a Foo.Designer.cs file which is then
included in your project. You can then access the "string" value by using code as follows:

```csharp
var s = MyProject.Foo.Wall_Style;
```

Note in the example we have a place holder ({0}) for additional text. You can still use te property of Foo.Wall_Style with
things like string.Format.

```csharp
int i = 1;
var s = string.Format (MyProject.Foo.Wall_Style, i);
```

All this means you don't need to hard the string directly. When accessing MyProject.Foo.Wall_Style the code will look up the value from
the embedded resx file.

You can add support for a new language by adding a new resx file which uses the language/region code e.g Foo.de-DE.resx.
This new file will contain the translations for that language/region. In the example we are targetting German.

### Universal Windows Platform (UWP) considerations

Unfortunately UWP does not support resx files anymore. They have a new file called resw. The format is similar but
incompatible. As a result, you will need to duplicate the data into a set of resw files to get the to work on UWP.
The process is like the standard resx process.

## Upgrading your SpriteFont files

By default, the SpriteFont processor uses a limited set of characters to generate the font. While this is fine for English
languages it would probably not include special characters needed for other languages (French, Arabic, Korean etc).

As a result MonoGame has a LocalizedFontProcessor which does something slightly different. The process looks at the resx
files you provide it with and generates an optimized spritefont which only contains the characters your game uses.

To make use of this functionality you ned to tell the spritefont which resx files to use. Open the .spritefont with a
xml/text editor and add lines like this inside the Asset node

```xml
<ResourceFiles>
  <Resx>..\Foo.resx</Resx>
  <Resx>..\Foo.de-DE.resx</Resx>
</ResourceFiles>
```

Note the paths are relative to the .spritefont directory. In the example above the resx files are in the directory
above the .spritefont.

You should end up with a .spritefont file like this

```xml
<?xml version="1.0" encoding="utf-8"?>
<XnaContent xmlns:Graphics="Microsoft.Xna.Framework.Content.Pipeline.Graphics">
  <Asset Type="Graphics:FontDescription">
    <FontName>Verdana</FontName>
    <Size>14</Size>
    <Spacing>1</Spacing>
    <Style>Regular</Style>
    <CharacterRegions>
      <CharacterRegion>
        <Start>&#32;</Start>
        <End>&#32;</End>
      </CharacterRegion>
    </CharacterRegions>
    <ResourceFiles>
      <Resx>..\Foo.resx</Resx>
      <Resx>..\Foo.de-DE.resx</Resx>
    </ResourceFiles>
  </Asset>
</XnaContent>
```

Once that is done you then need to change the .mgcb file so that the SpriteFontProcessor is replaced with
the LocalizedFontProcessor. This can be done by editing the .mgcb file or using the MGCB Editor. After
that you can just compile your content as normal. If the processor has any trouble resolving or reading the
resx files you will get an error.

## Loading the Font

Loading the font can be done in the normal way. The end result of the process is a .xnb file containing a normal
SpriteFont.

```csharp
var font = Content.Load<SpriteFont>("Foo");
```

### Other Localized assets

Not all localized assets will be fonts. In certain situations you might need to swap out an entire texture or spritesheet.
For these cases a new method has been added to the ContentManager, LoadLocalized. The idea behind this method is that it will
look for localized files BEFORE loading the default one.

So for example say you have an asset, MyCharacter. You have a MyCharacter.xnb file which contains the data for that item. You
can also has a MyCharacter.de-DE.xnb file which contains the German version of that asset. This asset could be a Texture, Audio
or any other game asset. You can then use LoadLocalized to load the localized version of the asset.

```csharp
var myCharacter = Content.LoadLocalized<Texture2D>("MyCharacter");
```

The decision on which localized asset to load is made by looking for a file with the following patterns

```xml
<AssetName>.<CurrentCulture.Name>
<AssetName>.<CurrentCulture.TwoLetterISOLanguageName>
```

These values are retrieved from

```csharp
CultureInfo.CurrentCulture.Name                        // eg. "en-US"
CultureInfo.CurrentCulture.TwoLetterISOLanguageName     // eg. "en"
```

which are part of the System.Globalization namespace. On a side note you can also use the `LoadLocalized` to load language
specific SpriteFonts. They just need to be named in the same way as we have described above.
# Using MGCB Editor

The [MGCB Editor](~/articles/tools/pipeline.md) is used to organize and build content for use with MonoGame. It is installed as part of the MonoGame SDK Installer or can be built [directly from source](https://github.com/mono/MonoGame/tree/develop/Tools/Pipeline) if needed.

## Create A Project

To start a new project just select “New...” from the “File” menu.  This will give you a new empty project to add content to.

If you are starting from an existing XNA project, the MGCB Editor supports importing your existing .contentproj. Again you can access this from the “File” menu:

![MGCB Editor import XNA](~/images/pipeline_import.png)

This creates a new project, adding all your content and content settings from the XNA project. If you happened to be using custom processors you may need to edit the assembly references to link to the correct paths which we discuss next.

## Project Settings

You can edit the content project settings directly from the property grid editor after selecting the project node in the tree view:

![Project settings](~/images/pipeline_project.png)

This is where you set up the folders for output, the platform to target, the assembly references for custom processors, etc.

Note that currently the MGCB Editor is not setup to support multiple target platforms. This means you may need to manage multiple content projects or manually change the target platform between builds. We are working on adding functionality to support multiple platforms and configurations within a single project.

## Adding Content Items

Once you have a project setup you can add content to it for building.  You can do this from the “Edit” menu:

![Edit menu](~/images/pipeline_items.png)

Selecting “New Item...” will bring up the New Item dialog which displays a list of new items that can be created:

![New item](~/images/pipeline_newitem.png)

When you select “Existing Item...”, you get to select an existing item from disk to add to the content project.

## Custom Content Processors

Just like XNA, the MonoGame content pipeline supports custom content processors.  To use them you need to rebuild them correctly to work against MonoGame.

The first step is removing all `Microsoft.Xna.Framework.XXX` references and replacing them with references to `MonoGame.Framework` and `MonoGame.Framework.Content.Pipeline`.  This is required as you will no longer be building against Microsoft XNA.

Once your references are working, you then need to change your assembly target platform.  MonoGame does not support x86 (aka 32bit) assemblies in the content pipeline.  This is mainly to allow of processing really big content as well as to simplify the number of configurations and native code dependencies.  For this reason you should try to target “Any CPU” with your custom content assembly.

After you have done these fixes, you should be able to add these new processors to the content project “References”.

## Building Content

The MGCB Editor has 3 actions related to building content: Build, Rebuild and Clean. Build will build all content that needs to be built and put the xnb's in the output directory (bin by default). Content will be skipped if it hasn't changed since the last build. The time source content was last edited is saved in the intermediate directory (obj by default) to determine if content changed since the last build. Clean will empty the output and intermediate directories. Rebuild will first Clean and then Build.

## Linking Content To Your Game

Once you have built your content, you have a few different ways to add the xnb's to your game project. They all have the same goal, to get the built xnb's in your project output folder so a ContentManager can easily find and load them.

### MonoGameContentReference

The simplest method is to set up your game project from one of the templates that come with the SDK. When you create a new project, it will include a Content.mgcb file with its Build Action set to MonoGameContentReference. This build action is defined in the .targets file [here](https://github.com/MonoGame/MonoGame/blob/develop/Tools/MonoGame.Content.Builder.Task/MonoGame.Content.Builder.Task.targets).
MonoGameContentReference is set up so that when the project is built, the mgcb will build any new/modified content and copy the resulting xnb's to the project output directory, so they can be used in the project. Note that this way you don't even have to manually build the content with the MGCB Editor. Just add your content to the .mgcb with the MGCB Editor and the rest will happen when you build your project. The content files do not need to be added to your project.

### Manual Copy

If you don't want to use the automated process, you can build the content project with the MGCB Editor and copy the xnb's to the output folder of your project manually.

### Add As Content

If you are using Visual Studio, you can simply add the xnb files to your C# game project.  Create a folder in the project called Content then right click on the folder and select Add > Existing Item.

![Add existing item](~/images/existing_item.png)

You will now see a file dialog from which you can add your content files.  Note that if you don't want Visual Studio to make a local copy of the files be sure to use “Add As Link”.

![Add as link](~/images/add_as_link.png)

Once the files are added you need to select them all and change their build action to “Content” and “Copy if newer”.

![Copy if newer](~/images/copy_if_newer.png)

### Add With Wildcard

The more automatic option is to hand edit your game .csproj and have it include you content using wildcards. To do this just open the .csproj with any text editor then add the following after any other `<ItemGroup>`:

```xml
<ItemGroup>
  <Content Include="Content\**\*.*">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </Content>
</ItemGroup>
```

Then any files you put in a Content folder within your game project will automatically be included in the build.

## Reporting Bugs

If you run into any problems with MGCB or the MGCB Editor, please ask for help on the [community site](http://community.monogame.net/) or submit a [bug report on GitHub](https://github.com/MonoGame/MonoGame/issues).
# Creating a New Project

Depending on the software you plan on using please follow either [Visual Studio](1_creating_a_new_project_vs.md), or [VS for Mac / MonoDevelop](1_creating_a_new_project_md.md) guide.
# Creating a Project with MonoDevelop

Start up MonoDevelop / Xamarin Studio and select **New...** in the upper left corner.

![New Solution](~/images/getting_started/1_new_soulution_md.png)

Now you should see a "New Project" dialog pop up. From here select **MonoGame > App** category, then select **MonoGame Cross Platform Desktop Project** and click **Next**.

![New Template](~/images/getting_started/1_template_dialog_md.png)

On the following dialog, type in the name that you wish to give your project. Do note that you should not use space character for it. For this tutorial, it will be named **ExampleGame**. After you've entered the name, click on the **Browse** button next to location text field, and select where you wish to save your project. Finally click **Create** to create a new project.

![New Project](~/images/getting_started/1_project_dialog_md.png)

If everything went correctly, you should see an **ExampleGame** project open up like in the picture bellow. To run your game simply press the big **Play Button** in the upper left corner or press **F5**.

![Run Game](~/images/getting_started/1_run_game_md.png)

You should now see your game window running.

![Game](~/images/getting_started/1_game_md.png)

Currently it's just clearing the surface with blue color. For further information on creating your game, please look at the [Understanding the Code](2_understanding_the_code.md).
# Creating a Project with Visual Studio

Start up Visual Studio and select **New Project...** in the upper left corner.

![New Solution](~/images/getting_started/1_new_soulution_vs.png)

Now you should see a "New Project" dialog pop up, from here select **Templates > Visual C# > MonoGame** category, and then select **MonoGame Cross Platform Desktop Project**. Next type in the name that you wish to give your project, for this tutorial let's just use **ExampleGame** (do note that you should not use space character for it). After you've entered the name, click on the **Browse** button next to the location text field, and select where you wish to save your project. Finally click **OK** to create a new project.

![New Template](~/images/getting_started/1_template_dialog_vs.png)

If everything went correctly, you should see an **ExampleGame** project open up like in the picture bellow. To run your game simply press the big **Play Button** in the toolbar or press **F5**.

![Run Game](~/images/getting_started/1_run_game_vs.png)

You should now see your game window running.

![Game](~/images/getting_started/1_game_vs.png)

Currently it's just clearing the surface with blue color. For further information on creating your game, please look at the [Understanding the Code](2_understanding_the_code.md).
# Understanding the Code

This file will go over the code that is getting created when you start a blank project. For help on creating a project please look at [Creating a New Project](1_creating_a_new_project.md).

## Using Statements

```csharp
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Storage;
using Microsoft.Xna.Framework.Input;
```

These using statements are required in order to use the code that MonoGame has to offer.

The reason why they start with Microsoft.Xna.Framework is because MonoGame is an open source implementation of Microsoft Xna framework, and in order to maintain compatibility with the XNA code, it is using the same namespaces.

## The Game1 Class

```csharp
public class Game1 : Game
```

The main Game1 class is inheriting from the Game class, which provides all the core methods for your game (ie. Load/Unload Content, Update, Draw etc.). You usually have only one Game class per game so its name isn't that important.

## Instanced Variables

```csharp
GraphicsDeviceManager graphics;
SpriteBatch spriteBatch;
```

The two default variables that the blank template starts with are GraphicsDeviceManager and SpriteBatch. Both of these variables are used for drawing stuff as you will see in a later tutorial.

## Constructor

```csharp
public Game1()
{
    graphics = new GraphicsDeviceManager(this);
    Content.RootDirectory = "Content";
}
```

The main game constructor is used to initialize the starting variables. In this case we are creating a new GraphicsDeviceManager from our game, and are setting the folder which the game will search for content.

## Initialize Method

```csharp
protected override void Initialize()
{
    // TODO: Add your initialization logic here

    base.Initialize();
}
```

This method is called after the constructor, but before the main game loop(Update/Draw). This is where you can query any required services and load any non-graphic related content.

## LoadContent Method

```csharp
protected override void LoadContent()
{
    // Create a new SpriteBatch, which can be used to draw textures.
    spriteBatch = new SpriteBatch(GraphicsDevice);

    // TODO: use this.Content to load your game content here
}
```

This method is used to load your game content. It is called only once per game, after Initialize method, but before the main game loop methods.

## Update Method

```csharp
protected override void Update(GameTime gameTime)
{
    if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
        Exit();

    // TODO: Add your update logic here

    base.Update(gameTime);
}
```

This method is called multiple times per second, and is used to update your game state (checking for collisions, gathering input, playing audio, etc.).

## Draw Method

```csharp
protected override void Draw(GameTime gameTime)
{
    graphics.GraphicsDevice.Clear(Color.CornflowerBlue);

    // TODO: Add your drawing code here

    base.Draw(gameTime);
}
```

Similar to the Update method, it is also called multiple times per second.

For the next part, look at [Adding Content](3_adding_content.md) page.
# Adding Content

This file will go over adding content to your game. For help on creating a project please look at [Creating a New Project](1_creating_a_new_project.md)

First, you are going to need some content for your game. For this tutorial use the following image of a ball:

![Open Content](~/images/getting_started/ball.png)

Do **right-click > Save Image As** and save it somewhere with the name “ball.png”.

Now open up your game project and look at the left. You should see a solution explorer window. Expand the **Content** folder and open up **Content.mgcb** file by double-clicking on it.

![Open Content](~/images/getting_started/3_open_content.png)

You should now see a MGCB Editor window open up. In case it didn't get opened, you can right-click on **Content.mgcb**, select **open with** and then select **MonoGame Pipeline**.

![MGCB Editor](~/images/getting_started/3_pipeline_tool.png)

Your game content is managed from this external tool. You can add content to your game in one of the following ways:

- **Add Existing Item** toolbar button
- **Edit > Add > Existing Item...** menu button
- **right-click > Add > Existing Item...** context menu

In our case let's use the **Add Existing Item** toolbar button.

![Add Content](~/images/getting_started/3_add_content.png)

You should now be prompted to select a file. Select the “ball.png” that you have downloaded a moment ago. After that you will be asked on what action you want to do for adding the file. Just leave it to default and click **OK**.

![Copy Content](~/images/getting_started/3_copy_content.png)

Now simply click **Save** toolbar button and close the tool.

![Save Content](~/images/getting_started/3_save_content.png)

Now that we have added the content, it's time to load it. First declare a new variable, so we can load the ball image into memory.

```csharp
public class Game1 : Game
{
    Texture2D ballTexture;

    GraphicsDeviceManager graphics;
```

Next find the LoadContent method and use it to initialize the ballTexture private variable:

```csharp
protected override void LoadContent()
{
    // Create a new SpriteBatch, which can be used to draw textures.
    spriteBatch = new SpriteBatch(GraphicsDevice);

    // TODO: use this.Content to load your game content here
    ballTexture = Content.Load<Texture2D>("ball");
}
```

And finally, find the Draw method, and let's draw the ball onto the screen:

```csharp
protected override void Draw(GameTime gameTime)
{
    graphics.GraphicsDevice.Clear(Color.CornflowerBlue);

    // TODO: Add your drawing code here
    spriteBatch.Begin();
    spriteBatch.Draw(ballTexture, new Vector2(0, 0), Color.White);
    spriteBatch.End();

    base.Draw(gameTime);
}
```

Now run the game and you should get the following:

![Game](~/images/getting_started/3_game.png)

For the next part, look at [Adding Basic Code](4_adding_basic_code.md) page.
# Adding Basic Code

This file will go over adding basic logic to your game. Do note that this file continues where [Adding Content](3_adding_content.md) tutorial left off.

First we need to add few new variables, one for position, and one for speed.

```csharp
public class Game1 : Game
{
    Texture2D ballTexture;
    Vector2 ballPosition;
    float ballSpeed;
```

Next let's initialize them. Find the **Initialize** method and add the following lines.

```csharp
// TODO: Add your initialization logic here
ballPosition = new Vector2(graphics.PreferredBackBufferWidth / 2,
    graphics.PreferredBackBufferHeight / 2);
ballSpeed = 100f;

base.Initialize();
```

With this we are putting our ball starting position to the center of the screen. Last thing we need to do is modify the position that the ball is getting drawn to. Find **Draw** method and modify the Draw call to:

```csharp
spriteBatch.Draw(ballTexture, ballPosition, Color.White);
```

Now run the game.

![Draw Ball 1](~/images/getting_started/4_ball_not_center.png)

As you can see the ball doesn't seem quite centered yet. This is happening because MonoGame uses (0, 0) as the origin point for drawing by default. We can modify this by doing the following:

```csharp
spriteBatch.Draw(
    ballTexture,
    ballPosition,
    null,
    Color.White,
    0f,
    new Vector2(ballTexture.Width / 2, ballTexture.Height / 2),
    Vector2.One,
    SpriteEffects.None,
    0f
);
```

With this we are setting the origin to the center of the image. Now the image will get drawn to the center of the screen.

![Draw Ball 2](~/images/getting_started/4_ball_center.png)

Next let's setup some movement. Find the **Update** method and add:

```csharp
// TODO: Add your update logic here
var kstate = Keyboard.GetState();

if (kstate.IsKeyDown(Keys.Up))
    ballPosition.Y -= ballSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;

if(kstate.IsKeyDown(Keys.Down))
    ballPosition.Y += ballSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;

if (kstate.IsKeyDown(Keys.Left))
    ballPosition.X -= ballSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;

if(kstate.IsKeyDown(Keys.Right))
    ballPosition.X += ballSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;

base.Update(gameTime);
```

Let's discuss the code a bit.

With this we are getting the current keyboard state and just putting it into a variable.

```csharp
var kstate = Keyboard.GetState();
```

Next is just a simple check to see if the Up arrow key is pressed.

```csharp
if (kstate.IsKeyDown(Keys.Up))
```

And last is a simple code for moving the ball by **ballSpeed**. The reason why **ballSpeed** is getting multiplied by **gameTime.ElapsedGameTime.TotalSeconds** is because Update is not usually fixed, that is the time between update calls is not the same, so in order to get smooth movement we multiply speed by the time since the last update method was called.

```csharp
    ballPosition.Y -= ballSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;
```

The last 2 code parts repeat for Down, Left and Right arrow keys.

Run the game and you should be able to move the ball with the arrow keys. You will probably notice that you can get out of the window, so let's make it so that the ball can't escape the window. We will do this by setting bounds onto the ballPosition after it has already been moved.

```csharp
if(kstate.IsKeyDown(Keys.Right))
    ballPosition.X += ballSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;

if(ballPosition.X > graphics.PreferredBackBufferWidth - ballTexture.Width / 2)
    ballPosition.X = graphics.PreferredBackBufferWidth - ballTexture.Width / 2;
else if(ballPosition.X < ballTexture.Width / 2)
    ballPosition.X = ballTexture.Width / 2;

if(ballPosition.Y > graphics.PreferredBackBufferHeight - ballTexture.Height / 2)
    ballPosition.Y = graphics.PreferredBackBufferHeight - ballTexture.Height / 2;
else if(ballPosition.Y < ballTexture.Height / 2)
    ballPosition.Y = ballTexture.Height / 2;

base.Update(gameTime);
```

Now run the game and the ball won't be able to escape window bounds anymore.

Happy Coding ^^
# Getting Started

This section walks you through the basics of MonoGame and help you create your first game.

- [Creating a New Project](1_creating_a_new_project.md)
  - [Visual Studio](1_creating_a_new_project_vs.md)
  - [MonoDevelop / Xamarin Studio](1_creating_a_new_project_md.md)
- [Understanding the Code](2_understanding_the_code.md)
- [Adding Content](3_adding_content.md)
- [Adding Basic Code](4_adding_basic_code.md)
MonoGame distributes templates for new projects in three ways:

- For [Visual Studio](https://visualstudio.microsoft.com/vs/)
- For [Visual Studio for Mac](https://visualstudio.microsoft.com/vs/mac/)
- For [.NET Core CLI](https://docs.microsoft.com/en-us/dotnet/core/tools/)

Once a project is created through any of these methods, it can be opened and built from any of the [compatible environments](requirements.md).

## Visual Studio

MonoGame templates can be installed as a Visual Studio extension.

- In Visual Studio go to Extensions > Manage Extensions...
- Make sure you have Online selected on the left pane.
- Search for MonoGame.
- Select the MonoGame Project Templates extension and click Download.
- Restart Visual Studio to install the extension.

When Visual Studio restarts, click Create a new project. The MonoGame templates should show up at the top, if not search for MonoGame in the search bar.

You'll see a few different templates were installed. To know which one to use, please refer to [Target Platforms](platforms.md).

## Visual Studio for Mac

MonoGame templates can be installed as a VS for Mac extension.

- Open VS for Mac and go to Visual Studio > Extensions...
- Open the Gallery tab and search for MonoGame.
- Select MonoGame Extension and click Install..., then Install again to confirm.

You've now installed the MonoGame templates. Go to File > New Solution... to open the New Project
dialog. You'll see the MonoGame templates in the list of templates.
To know which template to use, check out [Target Platforms](platforms.md).

## .NET Core CLI

You can set up a project using the .NET Core CLI (Command Line Interface).
If you don't have the .NET Core SDK installed, go get the latest version [here](https://dotnet.microsoft.com/download) (3.1 and up recommended).
After installation, you can run `dotnet --info` in a terminal to make sure the installation was successful.

MonoGame publishes templates for [dotnet new](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-new). To install the C# templates run `dotnet new -i MonoGame.Templates.CSharp`.

You can now create new projects. To do that, create a new directory for your project. Then, open a terminal and navigate to your project directory.
Run `dotnet new <TemplateID> -o <ProjectName>` to create your project, where `<TemplateID>` is a platform identifier, and `<ProjectName>` the name of your project.

For example: `dotnet new mgdesktopgl -o MyGame`.

To know which platform identifier to use for your project, please refer to [Target Platforms](platforms.md).
# Help and Support

This section will provide help and support for MonoGame.

## Help

If you wish to learn how to use MonoGame, please check out our [Tutorials page](~/articles/tutorials.md). If you want to find an answer to a more specific problem, you can ask it on our [Community page](https://community.monogame.net/).

## Bugs and new feature requests

If you find a bug or have a feature request, [please open a new issue](https://github.com/mono/monogame/issues). Before opening any issue, please search for existing issues and read the [Issue Guidelines](https://github.com/necolas/issue-guidelines).

Please note that the issue tracker is not for requesting help.
# Introduction

This section will give you an overview of MonoGame including, what it contains, development requirements, setup instructions, and additional links for help and support.

This section will cover the following topics:

- [What is MonoGame](what_is_monogame.md)
- [Development Requirements](requirements.md)
- [Create a MonoGame Project](create_project.md)
- [Target Platforms](platforms.md)
- [MonoGame FAQ](monogame_faq.md)
- [Help and Support](help_and_support.md)
# Frequently Asked Questions

This page contains a list of frequently asked questions.

## What software do I need to start?

Depending on the platform you wish to develop for the following things are needed:

- Android: [Xamarin.Android](https://docs.microsoft.com/en-us/xamarin/android/)
- iOS: [Xamarin.iOS](https://docs.microsoft.com/en-us/xamarin/ios/)

The linked pages will guide you through the setup process.
# Target Platforms

MonoGame supports the following systems:

- Windows
- Mac
- Linux
- Android
- iOS
- PlayStation 4
- PlayStation Vita
- Xbox One
- Nintendo Switch
- Google Stadia

There are different implementations of MonoGame that we call target platforms (or just platforms).
The platforms mostly correspond to the systems MonoGame supports but some platforms support multiple systems. Platforms for systems that require registration such as PlayStation and Xbox are not publicly available. To get access to those platforms, please contact your console account manager(s). MonoGame documentation for closed platforms is available in their respective repositories.

Below is a list of public platforms with the corresponding NuGet package, the `dotnet new` template identifier and an explanation of the platform.

- [WindowsDX](#windowsdx)
- [DesktopGL](#desktopgl)
- [Windows Universal](#windowsuniversal)
- [Android](#android)
- [iOS](#ios)

## WindowsDX

**Supported Systems**: Windows
**NuGet Package**: MonoGame.Framework.WindowsDX
**Template ID**: mgwindowsdx

WindowsDX uses WinForms to manage the game window, DirectX (9.0c or newer) is used for graphics, and XAudio is used for audio. You can target Windows Vista and up with this platform.

## DesktopGL

**Supported Systems**: Windows, macOS, Linux
**NuGet Package**: MonoGame.Framework.DesktopGL
**Template ID**: mgdesktopgl

DesktopGL uses SDL for windowing. OpenGL is used for graphics, and OpenAL-Soft for audio. DesktopGL supports Windows (Vista and up), macOS (High Sierra 10.13 and up) and Linux (64bit-only).

DesktopGL requires at least OpenGL 2.0 with the ARB_framebuffer_object extension (or alternatively at least OpenGL 3.0).

DesktopGL is a convenient way to publish builds for Windows, macOS, and Linux from a single project and source code. It also allows to cross-compile any build from any of these operating systems.

DesktopGL currently does not have a `VideoPlayer` implementation.

## WindowsUniversal

**Supported Systems**: Windows 10, Xbox One (UWP-only, not XDK)
**NuGet Package**: MonoGame.Framework.WindowsUniversal
**Template ID**: mguwpcore, mguwpxaml

The WindowsUniversal platform runs on [Universal Windows Platform (UWP)](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide).
WindowsUniversal uses DirectX for graphics, and XAudio for audio just like the WindowsDX platform.

This platform is meant to publish games on the Windows Store, for both Windows and Xbox One (through the [Xbox Live Creators Program](https://www.xbox.com/en-US/developers/creators-program)).

Note that UWP games running on Xbox One get [restricted access](https://docs.microsoft.com/en-us/windows/uwp/xbox-apps/system-resource-allocation) to the console capabilities. To unlock those restrictions, MonoGame has a dedicated Xbox One platform for registered [ID@Xbox](https://www.xbox.com/en-US/Developers/id) developers targeting the XDK (this platform is private and requires you to contact your ID@Xbox manager).

## Android

**Supported Systems**: Android
**NuGet Package**: MonoGame.Framework.Android
**Template ID**: mgandroid

The Android platform uses [Xamarin.Android](https://docs.microsoft.com/en-us/xamarin/android/).
OpenGL is used for graphics, and OpenAL for audio.

## iOS

**Supported Systems**: iOS
**NuGet Package**: MonoGame.Framework.iOS
**Template ID**: mgios

The iOS platform uses [Xamarin.iOS](https://docs.microsoft.com/en-us/xamarin/ios/).
OpenGL is used for graphics, and OpenAL for audio.
# Requirements

Depending on the [platform](platforms.md) that you are targeting, MonoGame has different sets of requirements.

## For desktop platforms

MonoGame requires a .NET Core SDK (3.1 or up) installation.
You can either install it [independently](https://dotnet.microsoft.com/download/dotnet-core), or by selecting the .NET Core payload when installing Visual Studio 2019 (version 15.4 and up required).

If you are targeting WindowsDX, you are also going to need [the DirectX June 2010 runtime](https://www.microsoft.com/en-us/download/details.aspx?id=8109) for audio and gamepads to work properly.

When it comes to IDE, Visual Studio 2019, Visual Studio Code, and Visual Studio 2019 for Mac are supported (alternatively, you can work directly from the CLI with your code editor of choice).

Desktop development is possible from any operating system.

## For UWP platforms

MonoGame requires the latest Windows 10 SDK.
You can install it by selecting the Universal App payload when installing Visual Studio 2019.
Building and publishing for UWP is only supported with Visual Studio 2019.

UWP development is not possible from macOS or Linux.

## For mobile platforms

MonoGame requires either Xamarin.iOS or Xamarin.Android depending on the target.

In Visual Studio you can install both by selecting the 'Mobile development with .NET' workload.
In Visual Studio for Mac you can install the iOS and Android workload separately.

Only Visual Studio 2019 or Visual Studio 2019 for Mac are supported in those contexts.

Mobile development is not possible from Linux.
# What is MonoGame

MonoGame is an Open Source implementation of the Microsoft XNA 4 Framework. Our goal is to allow people to make great games using a simple API.
The currently supported platforms are as follows.

* Desktop PCs
  * Windows 10 Store Apps (UWP)
  * Windows Win32 (OpenGL or DirectX)
  * Linux (OpenGL)
  * macOS (OpenGL)
* Mobile/Tablet Devices
  * Android (OpenGL)
  * iOS (OpenGL)
  * Windows Phone 10 (UWP)

Vulkan, DirectX 12, and Metal targets are planned but currently unavailable.

MonoGame also supports a number of Game Consoles. The templates and source for these platforms
are not publicly available. However, they are available to developers registered with the appropriate
developer programs.  

* Consoles (for registered developers)
  * PlayStation 4 (Sony)
  * PlayStation Vita (Sony)
  * Xbox One (both UWP and XDK) (ID@Xbox)
  * Nintendo Switch (Nintendo)
  * Stadia (Google)

To access the MonoGame version of these consoles, please contact your console account manager(s) directly (the MonoGame team can't give you access without contacting them first).
# Android

## Target Frameworks

Specifying the target Android versions can be confusing.  MonoGame is built to target Android 4.2 (API Level 17), but can run on lower Android versions.  If you build MonoGame from source, you will need the SDK Platform for API Level 17 installed in the Android SDK Manager.

Since MonoGame targets Android 4.2, the Target Framework in your Android project must be set to 4.2 or higher.  To allow your game to run on lower Android versions, set the Minimum Android version to the desired version in the project properties.

### Visual Studio

There are three settings in the Application tab of the project properties to set the target Android versions.

`Compile using Android version` must be set to a minimum of `Android 4.2`.  If you are using APIs available only in later Android versions, this must be set to the Android version that API became available or higher.

`Minimum Android to target` is set to the lowest Android version that you wish to support.

`Target Android version` is usually set to `Use Compile using SDK version`.  This means to use the same value that we set the app to be built with.  There is usually no reason to set this to any other value.

This is an example of a project set to build with the 4.4 SDK and target 4.0 as a minimum Android version.

![Android target frameworks](~/images/android_vs_target_frameworks.png)

### Xamarin Studio

Xamarin Studio has the same settings in the project options dialog. They are just in different places.

`Target framework` on the `General` page is the equivalent of Visual Studio's `Compile using Android version`.

![Android target framework](~/images/android_xs_target_framework.png)

On the `Android Application` page, you will find `Minimum Android version` (Visual Studio's `Minimum Android to target`) and `Target Android version` (same as Visual Studio).

![Android minimum framework](~/images/android_xs_minimum_framework.png)

## Android Manifest Requirements

### OpenGL ES 2.0 Support

MonoGame uses OpenGL ES 2.0. Google requires the following to be added to AndroidManifest.xml in order for the Market to hide the game from devices that do not have support for OpenGL ES 2.0.

```xml
<!-- Tell the system this app requires OpenGL ES 2.0. -->
<uses-feature android:glEsVersion="0x00020000" android:required="true" />
```

### Texture Compression

The Market can also filter games by the types of texture compression they support. Add a `<supports-gl-texture>` node for each type of texture compression used in your game. See the [Android documentation](http://developer.android.com/guide/topics/manifest/supports-gl-texture-element.html) for further details on this node.

## References

[Such Android API Levels, Much Confuse. Wow.](http://redth.codes/such-android-api-levels-much-confuse-wow/) is a blog post by Redth going into more detail about setting the Android versions in a Xamarin project.
# Platform specific Notes

While MonoGame aims to provide a platform-agnostic framework for developing games and apps, there are still some specific for each platform that need the developer needs to be aware of.  This section lists those specifics broken down by platform.

- [Android](android.md)
- [tvOS](tvOS.md)
- [Windows Universal Platform (UWP)](UWP.md)
## Menu Button Handling

The Menu button will map to the "Back" button on the GamePad. However on tvOS,
the Menu button requires some special processing. According to the Apple 
documentation the Menu Button

"*Pauses/resumes gameplay.
Returns to previous screen, exits to main game menu, and/or exits to Apple TV Home screen.*"

By default MonoGame will exit to the Apple TV Home screen when the Menu button is pressed, 
this is not alawys the desired behviour. When in gameplay the Menu button really should
Pause the game rather than Exiting to the Home screen.

Because MonoGame has no idea of the game state, it is down to the developer to inform
it when it can exit to the Home screen and when it should ignore the Menu event and allow
the developer to the event.

Some sample code.

```csharp

public class Game1 : Game, IPlaformBackButton
{

    private bool _isOnRootMenu = true;

    public bool Handled()
    {
        return !_isOnRootMenu;
    }

    public Game1()
    {
        Services.AddService<IPlaformBackButton>(this);
    }

    public override Update(GameTime gametime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed)
        {
            // do something in game
        }
    }
}
```

The key to this working is the `IPlatformBackButton` interface. By implementing
and registering this interface MonoGame can callback into your application to ask if it
should let you handle the Menu button or if it should pass it up to tvOS. So in this case if
the app is on the "Main menu" the developer will set *IsOnRootMenu* to true and when the Menu
button is pressed the game with Exit. However if IsOnRootMenu is false then the "Menu" button 
click will be routed to the GamePad Back button and the developer can check for the Back button
press and act accordingly.
# UWP

## Game class constructor

Due to some UWP implementation details, MonoGame has to construct your `Game` derived class by itself, using a static initializer `MonoGame.Framework.XamlGame<T>.Create(...)`.

In this situation, you have two main possibilities to create a `Game` derived class:

1. Let `XamlGame` initialize your `Game` derived class using the default constructor
2. Let `XamlGame` initialize your `Game` derived class using a custom constructor.

### 1. XamlGame uses the default constructor

With this logic, it isn't possible to inject dependencies through the constructor since the default constructor is called:
 `var game = new T();`

### 2. XamlGame uses a custom constructor

Why may you need this constructor?

Consider `Game1` needs some dependencies such as an `ISettingsRepository` to get some values from each *platform* settings store. You would then implement an `AndroidSettingsRepository` and a `UwpSettingsRepository`, but you cannot construct those dependencies in `Game1` itself, **because they are platform dependent**, so you'll have to inject them into its constructor.

For example, in a `MainActivity` on Android you would do:

```csharp
_game = new Game1(
    new AndroidTextFileImporter(Assets),
    new AndroidSettingsRepository(this));
```

With the UWP implementation using `XamlGame` static initializer, you could do this:

```csharp
_game = MonoGame.Framework.XamlGame<Game1>.Create(
    launchArguments,
    Window.Current.CoreWindow,
    swapChainPanel,
    () => new Game1(
        new UwpTextFileImporter(Assets),
        new UwpSettingsRepository(this)));
```

In this way, you tell the static initializer **how** you'd like to construct `Game1`.
# MGFXC

The MGFXC tool is used to compile [DirectX Effect files](https://docs.microsoft.com/en-us/windows/win32/direct3d9/writing-an-effect)
for usage with MonoGame.

The MGCB Editor uses MGFXC to compile effects and wraps them in an xnb file so they can be loaded using `ContentManager`.
If you compile effects directly with MGFXC you can load effects using the `Microsoft.Framework.Xna.Graphics.Effect` constructor
that takes a byte array with the effect code. Effects compiled directly are not xnb files and can not be loaded by `ContentManager`.

## Installation

MGFXC can be installed as a [.NET Core tool](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).
Make sure you have the .NET Core SDK installed. You can download it [here](https://dotnet.microsoft.com/download).

In a terminal run `dotnet tool install -g dotnet-mgfxc` to install MGFXC.

## Command Line

The command line options are:

```bat
mgfxc <SourceFile> <OutputFile> [/Debug] [/Profile:<DirectX_11,OpenGL,PlayStation4>]
```

### Source File

The input effect file in typical FX format with samplers, techniques, and passes defined.  This parameter is required.

### Output File

The path to write the compiled effect to.  This parameter is required.

NOTE: The generated file is not an XNB file for use with the ContentManager.

If the `/Debug` flag is passed the resulting compiled effect file will contain extra debug information and the fewest possible optimizations.

### Platform Profile

The `/Profile` option defines the platform we're targeting with this effect file.  It can be one of the following:

- DirectX_11
- OpenGL
- PlayStation4
- PSVita
- XboxOne
- Switch

NOTE: PlayStation 4, Xbox One, PS Vita, and Switch support is only available to licensed console developers.

### Help

If you use `/?`, `/help`, or simply pass no parameters to MGFXC you will get information about these command line options.

## Runtime Use

The resulting compiled effect file can be used from your game code like so:

```csharp
byte[] bytecode = File.ReadAllBytes("mycompiled.mgfx");
var effect = new Effect(bytecode);
```

This is how the stock effects (BasicEffect, DualTextureEffect, etc) are compiled and loaded.
# MGCB

The MonoGame Content Builder (MGCB.exe) is a command line tool for building XNB content on Windows, Mac, and Linux desktop systems.

Typically it is executed by the [MGCB Editor](pipeline.md) when editing content or by `MonoGame.Content.Builder.Task` during the build process
of a MonoGame project. Alternatively you can use it yourself from the command line for specialized build pipelines or for debugging content processing.

## Installation

MGCB can be installed as a [.NET Core tool](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).
Make sure you have the .NET Core SDK installed. You can download it [here](https://dotnet.microsoft.com/download).

In a terminal run `dotnet tool install -g dotnet-mgcb` to install MGCB.

## Command Line Options

The options are processed "left to right".  When an option is repeated the last option always wins.

### Output Directory

```
/outputDir:<directory_path>
```

It specifies the directory where all content is written.  If this option is omitted the output will be put into the current working directory.

### Intermediate Directory

```
/intermediateDir:<directory_path>
```

It specifies the directory where all intermediate files are written.  If this option is omitted the intermediate data will be put into the current working directory.

### Rebuild Content

```
/rebuild 
```

An optional parameter which forces a full rebuild of all content.

### Clean Content

```
/clean
```

Delete all previously built content and intermediate files.  Only the `/intermediateDir` and `/outputDir` need to be defined for clean to do its job.

### Incremental Build

```
/incremental
```

Skip cleaning files not included in the current build.  Useful for custom tools which only require a subset of the game content built.

### Assembly Reference

```
/reference:<assembly_path>
```

An optional parameter which adds an assembly reference which contains importers, processors, or writers needed during content building.

### Target Platform

```
/platform:<target_Platform>
```

Set the target platform for this build. It must be a member of the TargetPlatform enum:

* Windows
* iOS
* Android
* DesktopGL
* MacOSX
* WindowsStoreApp
* NativeClient
* PlayStation4
* WindowsPhone8
* RaspberryPi
* PSVita
* XboxOne
* Switch

If not set, it will default to Windows.

NOTE: PlayStation 4, Xbox One, PS Vita, and Switch support is only available to licensed console developers.

### Target Graphics Profile

```
/profile:<graphics_Profile>
```

Set the target graphics profile for this build. It must be a member of the GraphicsProfile enum:
* HiDef
* Reach

If not set, it will default to HiDef.

### Target Build Configuration

```
/config:<build_config>
```

The optional build configuration name from the build system.  This is sometimes used as a hint in content processors.

### Content Compression

```
/compress
```

Uses LZ4 compression to compress the contents of the XNB files.  Content build times will increase with this option enabled.  Compression is not recommended for platforms such as Android, Windows Phone 8 and Windows 8 as the app package is already compressed.  This is not compatible with LZX compression used in XNA content.

### Content Importer Name

```
/importer:<class_name>
```

An optional parameter which defines the class name of the content importer for reading source content.  If the option is omitted or used without a class name the default content importer for the source type is used.

### Content Processor Name

```
/processor:<class_name>
```

An optional parameter which defines the class name of the content processor for processing imported content.  If the option is omitted used without a class name the default content processor for the imported content is used.

Note that when you change the processor all previously defined `/processorParam` are cleared.

### Content Processor Parameter

```
/processorParam:<name>=<value>
```

An optional parameter which defines a parameter name and value to set on a content processor.

Note all defined processor parameters are cleared when the `/processor` is set.

### Build Content File

```
/build:<content_filepath>
/build:<content_filepath>;<destination_filepath>
```

Instructs the content builder to build the specified content file using the previously set switches and options. Optional destination path may be specified if you want to change the output filepath.

### Response File

```
/@:<response_filepath>
```

This defines a text response file (sometimes called a command file) that contains the same options and switches you would normally find on the command line.

Each switch is specified on a new line.  Comment lines are prefixed with #. These lines are removed by a preprocessor. You can specify multiple response files or mix normal command line switches with response files.

An example response file could look like this:

```
# Directories
/outputDir:bin/foo
/intermediateDir:obj/foo

/rebuild

# Build a texture
/importer:TextureImporter
/processor:TextureProcessor
/processorParam:ColorKeyEnabled=false
/build:Textures\wood.png
/build:Textures\metal.png
/build:Textures\plastic.png
```

### Launch Debugger

```
/launchdebugger
```

Allows a debugger to attach to the MGCB executable before content is built.

### Define Preprocessor Parameter

```
/define <name>=<value>
```

Sets or creates a preprocessor parameter with the given name and value.

### Preprocessor Macros

```
$if <name>=<value>
$endif
```

Preprocessor macros are intended to allow conditionals within a response file.

Preprocessor symbols can be defined from the command line with the `define` option or in a response file with the `$set` directive.

```
<example command line>
MGCB.exe /define:BuildEffects=No /@:example.mgcb

<example.mgcb file>
$if BuildEffects=Yes
   /importer:EffectImporter
   /processor:EffectProcessor
   /build:Effects\custom.fx
   # all other effects here....
$endif
```

```
$set BuildEffects=Yes

$if BuildEffects=Yes
    # ...
    # This is executed
$endif
```

For booleans you can omit a value to set a symbol and to check if it is set:

```
$set BuildEffects

$if BuildEffects
    # ...
    # This is executed
$endif
```

### Customizing your Build Process

When building content from your project via `msbuild`, there are a few ways to can hook into the build process. The `MonoGame.Content.Builder.targets` runs a target called
`BuildContent` just before your project builds. If you want to do any processing before or after this process you can use the `BeforeTargets` and `AfterTargets` mechanism provided
by `msbuild` to run your own targets.

```
<Target Name="MyBeforeTarget" BeforeTargets="BuildContent">
   <Message Text="MyBeforeTarget Ran"/>
</Target>
<Target Name="MyAfterTarget" AfterTargets="BuildContent">
   <Message Text="MyAfterTarget Ran"/>
</Target>
```

If you want to customise the arguements sent to the `MGCB.exe` as part of the build process you can use the `<MonoGameMGCBAdditionalArguments>` property to define those.
For example if you wanted to pass in the current project configuration you could define

```
<MonoGameMGCBAdditionalArguments>-config:$(Configuration)</MonoGameMGCBAdditionalArguments>
```
# MGCB Editor

MGCB Editor is the front-end GUI editor for MonoGame content builder projects.

[!MGCB Editor](~/images/pipeline.png)

MGCB Editor has the following features:

* Create, open, and save MGCB projects.
* Import existing XNA .contentproj.
* Tree view showing content of project.
* Property grid for editing content settings.
* Full undo/redo support.
* Build, rebuild, and clean the project.
* Rebuild selected items.
* Create new content like fonts and xml.
* Support for custom importers/processors/writers.
* Template format for adding new custom content types.

MGCB Editor can be installed as a [.NET Core tool](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).
Make sure you have the .NET Core SDK installed. You can download it [here](https://dotnet.microsoft.com/download).

In a terminal run `dotnet tool install -g dotnet-mgcb-editor` to install MGFXC.

After installing `mgcb-editor` run `dotnet mgcb-editor --register` to register MGCB Editor as the default app for .mgcb
files. This currently does not work on macOS.

[Read detailed documentation](~/articles/content/using_pipeline_tool.md).
# Tools

MonoGame distributes tooling to help manage and build content for your game.
These tools are available as [.NET Core Tools](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools).
Installation and usage instructions are on the following pages:

- [MonoGame Content Builder](mgcb.md) (MGCB): used to build content pipeline content.
- [MonoGame Effect Compiler](2mgfx.md) (MGFXC): used to compile stand alone effects (shaders).
- [MGCB Editor](pipeline.md): a graphical front end to edit mgcb files.
{\rtf1\adeflang1025\ansi\ansicpg1252\uc1\adeff1\deff0\stshfdbch0\stshfloch0\stshfhich0\stshfbi0\deflang1033\deflangfe1033\themelang1033\themelangfe0\themelangcs0{\fonttbl{\f0\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\f1\fbidi \fswiss\fcharset0\fprq2{\*\panose 020b0604020202020204}Arial;}
{\f34\fbidi \froman\fcharset1\fprq2{\*\panose 02040503050406030204}Cambria Math;}{\f36\fbidi \froman\fcharset0\fprq2{\*\panose 02040503050406030204}Cambria;}{\f38\fbidi \fswiss\fcharset0\fprq2{\*\panose 020b0604030504040204}Tahoma;}
{\f40\fbidi \fswiss\fcharset0\fprq2{\*\panose 020b0604030504040204}Verdana;}{\flomajor\f31500\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\fdbmajor\f31501\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\fhimajor\f31502\fbidi \froman\fcharset0\fprq2{\*\panose 02040503050406030204}Cambria;}
{\fbimajor\f31503\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\flominor\f31504\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\fdbminor\f31505\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\fhiminor\f31506\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0502020204030204}Calibri;}
{\fbiminor\f31507\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\f41\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\f42\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\f44\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\f45\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\f46\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\f47\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\f48\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\f49\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\f51\fbidi \fswiss\fcharset238\fprq2 Arial CE;}{\f52\fbidi \fswiss\fcharset204\fprq2 Arial Cyr;}
{\f54\fbidi \fswiss\fcharset161\fprq2 Arial Greek;}{\f55\fbidi \fswiss\fcharset162\fprq2 Arial Tur;}{\f56\fbidi \fswiss\fcharset177\fprq2 Arial (Hebrew);}{\f57\fbidi \fswiss\fcharset178\fprq2 Arial (Arabic);}
{\f58\fbidi \fswiss\fcharset186\fprq2 Arial Baltic;}{\f59\fbidi \fswiss\fcharset163\fprq2 Arial (Vietnamese);}{\f401\fbidi \froman\fcharset238\fprq2 Cambria CE;}{\f402\fbidi \froman\fcharset204\fprq2 Cambria Cyr;}
{\f404\fbidi \froman\fcharset161\fprq2 Cambria Greek;}{\f405\fbidi \froman\fcharset162\fprq2 Cambria Tur;}{\f408\fbidi \froman\fcharset186\fprq2 Cambria Baltic;}{\f421\fbidi \fswiss\fcharset238\fprq2 Tahoma CE;}
{\f422\fbidi \fswiss\fcharset204\fprq2 Tahoma Cyr;}{\f424\fbidi \fswiss\fcharset161\fprq2 Tahoma Greek;}{\f425\fbidi \fswiss\fcharset162\fprq2 Tahoma Tur;}{\f426\fbidi \fswiss\fcharset177\fprq2 Tahoma (Hebrew);}
{\f427\fbidi \fswiss\fcharset178\fprq2 Tahoma (Arabic);}{\f428\fbidi \fswiss\fcharset186\fprq2 Tahoma Baltic;}{\f429\fbidi \fswiss\fcharset163\fprq2 Tahoma (Vietnamese);}{\f430\fbidi \fswiss\fcharset222\fprq2 Tahoma (Thai);}
{\f441\fbidi \fswiss\fcharset238\fprq2 Verdana CE;}{\f442\fbidi \fswiss\fcharset204\fprq2 Verdana Cyr;}{\f444\fbidi \fswiss\fcharset161\fprq2 Verdana Greek;}{\f445\fbidi \fswiss\fcharset162\fprq2 Verdana Tur;}
{\f448\fbidi \fswiss\fcharset186\fprq2 Verdana Baltic;}{\f449\fbidi \fswiss\fcharset163\fprq2 Verdana (Vietnamese);}{\flomajor\f31508\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}
{\flomajor\f31509\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\flomajor\f31511\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\flomajor\f31512\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}
{\flomajor\f31513\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\flomajor\f31514\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\flomajor\f31515\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}
{\flomajor\f31516\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fdbmajor\f31518\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fdbmajor\f31519\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\fdbmajor\f31521\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fdbmajor\f31522\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fdbmajor\f31523\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\fdbmajor\f31524\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fdbmajor\f31525\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fdbmajor\f31526\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}
{\fhimajor\f31528\fbidi \froman\fcharset238\fprq2 Cambria CE;}{\fhimajor\f31529\fbidi \froman\fcharset204\fprq2 Cambria Cyr;}{\fhimajor\f31531\fbidi \froman\fcharset161\fprq2 Cambria Greek;}{\fhimajor\f31532\fbidi \froman\fcharset162\fprq2 Cambria Tur;}
{\fhimajor\f31535\fbidi \froman\fcharset186\fprq2 Cambria Baltic;}{\fbimajor\f31538\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fbimajor\f31539\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\fbimajor\f31541\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fbimajor\f31542\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fbimajor\f31543\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\fbimajor\f31544\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fbimajor\f31545\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fbimajor\f31546\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}
{\flominor\f31548\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\flominor\f31549\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\flominor\f31551\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}
{\flominor\f31552\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\flominor\f31553\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\flominor\f31554\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\flominor\f31555\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\flominor\f31556\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fdbminor\f31558\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}
{\fdbminor\f31559\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\fdbminor\f31561\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fdbminor\f31562\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}
{\fdbminor\f31563\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\fdbminor\f31564\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fdbminor\f31565\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}
{\fdbminor\f31566\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fhiminor\f31568\fbidi \fswiss\fcharset238\fprq2 Calibri CE;}{\fhiminor\f31569\fbidi \fswiss\fcharset204\fprq2 Calibri Cyr;}
{\fhiminor\f31571\fbidi \fswiss\fcharset161\fprq2 Calibri Greek;}{\fhiminor\f31572\fbidi \fswiss\fcharset162\fprq2 Calibri Tur;}{\fhiminor\f31575\fbidi \fswiss\fcharset186\fprq2 Calibri Baltic;}
{\fbiminor\f31578\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fbiminor\f31579\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\fbiminor\f31581\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}
{\fbiminor\f31582\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fbiminor\f31583\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\fbiminor\f31584\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\fbiminor\f31585\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fbiminor\f31586\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}}{\colortbl;\red0\green0\blue0;\red0\green0\blue255;\red0\green255\blue255;\red0\green255\blue0;
\red255\green0\blue255;\red255\green0\blue0;\red255\green255\blue0;\red255\green255\blue255;\red0\green0\blue128;\red0\green128\blue128;\red0\green128\blue0;\red128\green0\blue128;\red128\green0\blue0;\red128\green128\blue0;\red128\green128\blue128;
\red192\green192\blue192;}{\*\defchp }{\*\defpap \ql \li0\ri0\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 }\noqfpromote {\stylesheet{\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 
\ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 \snext0 \sqformat \spriority0 Normal;}{\s1\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\outlinelevel0\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 
\f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 \sbasedon0 \snext0 \slink15 \sqformat \spriority9 heading 1;}{\s2\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\outlinelevel1\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 
\f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 \sbasedon0 \snext0 \slink16 \sqformat \spriority9 heading 2;}{\*\cs10 \additive \ssemihidden Default Paragraph Font;}{\*
\ts11\tsrowd\trftsWidthB3\trpaddl108\trpaddr108\trpaddfl3\trpaddft3\trpaddfb3\trpaddfr3\trcbpat1\trcfpat1\tblind0\tblindtype3\tscellwidthfts0\tsvertalt\tsbrdrt\tsbrdrl\tsbrdrb\tsbrdrr\tsbrdrdgl\tsbrdrdgr\tsbrdrh\tsbrdrv 
\ql \li0\ri0\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 \rtlch\fcs1 \af0\afs20\alang1025 \ltrch\fcs0 \fs20\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 \snext11 \ssemihidden \sunhideused \sqformat Normal Table;}{\*\cs15 
\additive \rtlch\fcs1 \ab\af0\afs32 \ltrch\fcs0 \b\f36\fs32\kerning32 \sbasedon10 \slink1 \slocked \spriority9 Heading 1 Char;}{\*\cs16 \additive \rtlch\fcs1 \ab\ai\af0\afs28 \ltrch\fcs0 \b\i\f36\fs28 \sbasedon10 \slink2 \slocked \spriority9 
Heading 2 Char;}{\s17\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af38\afs16\alang1025 \ltrch\fcs0 \f38\fs16\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 
\sbasedon0 \snext17 \slink18 \ssemihidden \sunhideused \styrsid7424395 Balloon Text;}{\*\cs18 \additive \rtlch\fcs1 \af38\afs16 \ltrch\fcs0 \f38\fs16 \sbasedon10 \slink17 \slocked \ssemihidden \styrsid7424395 Balloon Text Char;}{\*\cs19 \additive 
\rtlch\fcs1 \af0\afs16 \ltrch\fcs0 \fs16 \sbasedon10 \ssemihidden \sunhideused \styrsid4538388 annotation reference;}{\s20\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs20\alang1025 \ltrch\fcs0 
\f1\fs20\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 \sbasedon0 \snext20 \slink21 \ssemihidden \sunhideused \styrsid4538388 annotation text;}{\*\cs21 \additive \rtlch\fcs1 \af1 \ltrch\fcs0 \f1 
\sbasedon10 \slink20 \slocked \ssemihidden \styrsid4538388 Comment Text Char;}{\s22\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \ab\af1\afs20\alang1025 \ltrch\fcs0 \b\f1\fs20\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 
\sbasedon20 \snext20 \slink23 \ssemihidden \sunhideused \styrsid4538388 annotation subject;}{\*\cs23 \additive \rtlch\fcs1 \ab\af1 \ltrch\fcs0 \b\f1 \sbasedon21 \slink22 \slocked \ssemihidden \styrsid4538388 Comment Subject Char;}}{\*\rsidtbl \rsid213160
\rsid284417\rsid417145\rsid481196\rsid551334\rsid723397\rsid786968\rsid1382437\rsid1390003\rsid1521043\rsid1530955\rsid1708989\rsid1783212\rsid1903779\rsid2431884\rsid3165084\rsid3416120\rsid3419781\rsid3754103\rsid3768194\rsid3831520\rsid4538130
\rsid4538388\rsid4552277\rsid4680449\rsid4729674\rsid4865270\rsid4987534\rsid5128131\rsid5186068\rsid5864350\rsid6186044\rsid6311778\rsid6384507\rsid6434687\rsid6561471\rsid6910344\rsid6947552\rsid7033180\rsid7424395\rsid7682010\rsid7690850\rsid7744081
\rsid8151618\rsid8196281\rsid8198206\rsid8342723\rsid8350925\rsid8722561\rsid8852349\rsid8934457\rsid8944153\rsid9573035\rsid9635349\rsid9638545\rsid9724918\rsid10044820\rsid10095979\rsid10228618\rsid10449644\rsid10494075\rsid11166278\rsid11166751
\rsid11285353\rsid11366513\rsid11494815\rsid11932529\rsid12061202\rsid12533699\rsid12536400\rsid12916885\rsid13264736\rsid13322831\rsid13440556\rsid13455614\rsid13597357\rsid13768671\rsid14097590\rsid14157399\rsid14229900\rsid14305025\rsid14314735
\rsid14436896\rsid14565916\rsid14572556\rsid14688892\rsid14752433\rsid14904394\rsid15086147\rsid15749945\rsid15814398\rsid15927751\rsid16071312\rsid16126175\rsid16279402\rsid16391569\rsid16404661\rsid16452939\rsid16537688\rsid16606866\rsid16674896}
{\mmathPr\mmathFont34\mbrkBin0\mbrkBinSub0\msmallFrac0\mdispDef1\mlMargin0\mrMargin0\mdefJc1\mwrapIndent1440\mintLim0\mnaryLim1}{\info{\title Microsoft Permissive License (Ms-PL)}{\author Jonr}{\operator Dean Johnson}{\creatim\yr2007\mo2\dy23\hr15\min10}
{\revtim\yr2007\mo2\dy23\hr15\min10}{\printim\yr2006\mo9\dy28\hr8\min46}{\version2}{\edmins1}{\nofpages1}{\nofwords404}{\nofchars2221}{\*\company Microsoft}{\nofcharsws2620}{\vern32859}{\*\saveprevpict}}{\*\userprops {\propname _NewReviewCycle}\proptype30
{\staticval }}{\*\xmlnstbl {\xmlns1 http://schemas.microsoft.com/office/word/2003/wordml}{\xmlns2 urn:schemas-microsoft-com:office:smarttags}}\paperw12240\paperh15840\margl1440\margr1440\margt1440\margb1440\gutter0\ltrsect 
\widowctrl\ftnbj\aenddoc\trackmoves0\trackformatting1\donotembedsysfont0\relyonvml0\donotembedlingdata1\grfdocevents0\validatexml0\showplaceholdtext0\ignoremixedcontent0\saveinvalidxml0\showxmlerrors0\hyphcaps0\horzdoc\dghspace120\dgvspace120
\dghorigin1701\dgvorigin1984\dghshow0\dgvshow3\jcompress\viewkind1\viewscale100\splytwnine\ftnlytwnine\htmautsp\useltbaln\alntblind\lytcalctblwd\lyttblrtgr\lnbrkrule\nobrkwrptbl\snaptogridincell\allowfieldendsel\wrppunct\asianbrkrule\rsidroot10494075
\newtblstyruls\nogrowautofit\utinl \fet0{\*\wgrffmtfilter 2450}\ilfomacatclnup0\ltrpar \sectd \ltrsect\linex0\sectdefaultcl\sftnbj {\*\pnseclvl1\pnucrm\pnstart1\pnindent720\pnhang {\pntxta .}}{\*\pnseclvl2\pnucltr\pnstart1\pnindent720\pnhang {\pntxta .}}
{\*\pnseclvl3\pndec\pnstart1\pnindent720\pnhang {\pntxta .}}{\*\pnseclvl4\pnlcltr\pnstart1\pnindent720\pnhang {\pntxta )}}{\*\pnseclvl5\pndec\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl6\pnlcltr\pnstart1\pnindent720\pnhang {\pntxtb (}
{\pntxta )}}{\*\pnseclvl7\pnlcrm\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl8\pnlcltr\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl9\pnlcrm\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}\pard\plain \ltrpar
\s1\ql \li0\ri0\sb180\nowidctlpar\wrapdefault\faauto\outlinelevel0\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \af1\afs31 \ltrch\fcs0 
\fs31\cf1\kerning36\insrsid10494075\charrsid14688892 Microsoft}{\rtlch\fcs1 \af1\afs31 \ltrch\fcs0 \fs31\cf1\kerning36\insrsid10494075  Permissive}{\rtlch\fcs1 \af1\afs31 \ltrch\fcs0 \fs31\cf1\kerning36\insrsid14688892  }{\rtlch\fcs1 \af1\afs31 
\ltrch\fcs0 \fs31\cf1\kerning36\insrsid10494075 License (Ms-PL}{\rtlch\fcs1 \af1\afs31 \ltrch\fcs0 \fs31\cf1\kerning36\insrsid4552277 )}{\rtlch\fcs1 \af1\afs31 \ltrch\fcs0 \fs31\cf1\kerning36\insrsid10494075 
\par }\pard\plain \ltrpar\ql \li0\ri0\sl336\slmult1\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \ab\af40\afs17 \ltrch\fcs0 
\b\f40\fs17\insrsid10494075 
\par This license governs use of the accompanying software. If you use the software, you accept this license. If you do not accept the license, do not use the software.
\par }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid6910344 
\par }\pard\plain \ltrpar\s2\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\outlinelevel1\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \ab\af40\afs23 \ltrch\fcs0 
\b\f40\fs23\insrsid10494075 1. Definitions
\par }\pard\plain \ltrpar\ql \li0\ri0\sl336\slmult1\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075 The terms \'93reproduce,\'94 \'93reproduction}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid7744081 ,}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 \'94 }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid551334 \'93derivative works,\'94}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid7744081\charrsid7744081  }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 and \'93distribution\'94 have the same meaning here as under 
{\*\xmlopen\xmlns2{\factoidname country-region}}{\*\xmlopen\xmlns2{\factoidname place}}U.S.{\*\xmlclose}{\*\xmlclose} copyright law.
\par }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400 A \'93contribution\'94 is the original software}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid4865270 ,}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400  }{\rtlch\fcs1 
\af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid11932529 or}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400  any additions or changes to the software.
\par }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid551334 A \'93c}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid551334\charrsid551334 ontributor\'94 }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400 is}{\rtlch\fcs1 \af40\afs17 
\ltrch\fcs0 \f40\fs17\insrsid12536400\charrsid551334  }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid551334\charrsid551334 any person that }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400 
distributes its contribution under this license.}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 
\par }\pard \ltrpar\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0\pararsid14229900 {\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid4729674\delrsid4729674  }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 \'93Licensed patents
\'94 }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400 are }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3831520 a contributor\rquote s }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 patent claims }{\rtlch\fcs1 
\af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3831520 that }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 read directly on }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3831520 its contribution.}{\rtlch\fcs1 \af1 \ltrch\fcs0 
\insrsid14229900\charrsid14229900 
\par }\pard\plain \ltrpar\s2\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\outlinelevel1\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \ab\af40\afs23 \ltrch\fcs0 
\b\f40\fs23\insrsid5186068 
\par }{\rtlch\fcs1 \ab\af40\afs23 \ltrch\fcs0 \b\f40\fs23\insrsid10494075 2. Grant of Rights
\par }\pard\plain \ltrpar\ql \li0\ri0\sl336\slmult1\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075 (A) Copyright Grant- Subject to the terms of this license, including the license conditions and limitations in section 3, }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3754103 each contributor }{\rtlch\fcs1 \af40\afs17 
\ltrch\fcs0 \f40\fs17\insrsid10494075 grants you a non-exclusive, worldwide, royalty-free copyright license to reproduce }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3754103 its contribution}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075 , prepare derivative works of }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3754103 its contribution}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid12536400 ,}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075  and distribute }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3754103 its contribution}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075  or any derivative works that you create.
\par (B) Patent Grant- Subject to the terms of this license, including the license conditions and limitations in section 3, }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid9724918 each contributor }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075 grants you a non-exclusive, worldwide, royalty-free license under }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid15814398 its }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 licensed patents
 to make, have made, use, sell, offer for sale, }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid1390003 import, }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 and/or otherwise dispose of }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid8944153 its contribution in }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 the software or derivative works of }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid8944153 the contribution in }{\rtlch\fcs1 \af40\afs17 
\ltrch\fcs0 \f40\fs17\insrsid10494075 the software.
\par }\pard\plain \ltrpar\s2\ql \li0\ri0\nowidctlpar\wrapdefault\faauto\outlinelevel1\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \ab\af40\afs23 \ltrch\fcs0 
\b\f40\fs23\insrsid5186068 
\par }{\rtlch\fcs1 \ab\af40\afs23 \ltrch\fcs0 \b\f40\fs23\insrsid10494075 3. Conditions and Limitations
\par }\pard\plain \ltrpar\ql \li0\ri0\sl336\slmult1\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0 \rtlch\fcs1 \af1\afs24\alang1025 \ltrch\fcs0 \f1\fs24\lang1033\langfe1033\cgrid\langnp1033\langfenp1033 {\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid1530955  }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 (A) No Trademark License- This license does not grant you rights to use }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid1708989 any contributors\rquote  }{
\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 name, logo, or trademarks.
\par (B) If you }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid8934457 bring a patent claim against }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10095979 any contributor}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 
 over patents that you }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid6947552 claim }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid7682010 are }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid6947552 infringe}{\rtlch\fcs1 
\af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid7682010 d by}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075  the software, your }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid7682010 patent }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075 license}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid7682010  from such contributor}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075  to the software ends automatically.
\par (C) If you distribute }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid3165084 any portion of }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 
the software, you must retain all copyright, patent, trademark, and attribution notices that are present in the software.
\par (D) If you distribute }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid15749945 any portion of the }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 software in source code form}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid14904394 ,}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075  you may do so only under this license}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid6384507  }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid14904394 by including }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 a complete copy of this license with your distribution}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid6384507 .}{\rtlch\fcs1 \af40\afs17 
\ltrch\fcs0 \f40\fs17\insrsid10494075  }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid6384507 I}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 f you distribute }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid15749945 
any portion of }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 the software in compiled or object code form}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid16452939 ,}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 
 you may only do so under a license that complies with this license.
\par }\pard \ltrpar\ql \li0\ri0\sl336\slmult1\nowidctlpar\wrapdefault\faauto\rin0\lin0\itap0\pararsid14572556 {\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 (E) The software is licensed \'93as-is.\'94 You bear the risk of using it. }{
\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid284417 The contributors }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 
give no express warranties, guarantees or conditions. You may have additional consumer rights under your local laws which this license cannot change. To the extent permitted under your local laws, }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid1783212 the contributors }{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 \f40\fs17\insrsid10494075 exclude the implied warranties of merchantability, fitness for a particular purpose and non-infringement.}{\rtlch\fcs1 \af40\afs17 \ltrch\fcs0 
\f40\fs17\insrsid10494075\charrsid14572556 
\par }{\*\themedata 504b030414000600080000002100828abc13fa0000001c020000130000005b436f6e74656e745f54797065735d2e786d6cac91cb6ac3301045f785fe83d0b6d8
72ba28a5d8cea249777d2cd20f18e4b12d6a8f843409c9df77ecb850ba082d74231062ce997b55ae8fe3a00e1893f354e9555e6885647de3a8abf4fbee29bbd7
2a3150038327acf409935ed7d757e5ee14302999a654e99e393c18936c8f23a4dc072479697d1c81e51a3b13c07e4087e6b628ee8cf5c4489cf1c4d075f92a0b
44d7a07a83c82f308ac7b0a0f0fbf90c2480980b58abc733615aa2d210c2e02cb04430076a7ee833dfb6ce62e3ed7e14693e8317d8cd0433bf5c60f53fea2fe7
065bd80facb647e9e25c7fc421fd2ddb526b2e9373fed4bb902e182e97b7b461e6bfad3f010000ffff0300504b030414000600080000002100a5d6a7e7c00000
00360100000b0000005f72656c732f2e72656c73848fcf6ac3300c87ef85bd83d17d51d2c31825762fa590432fa37d00e1287f68221bdb1bebdb4fc7060abb08
84a4eff7a93dfeae8bf9e194e720169aaa06c3e2433fcb68e1763dbf7f82c985a4a725085b787086a37bdbb55fbc50d1a33ccd311ba548b63095120f88d94fbc
52ae4264d1c910d24a45db3462247fa791715fd71f989e19e0364cd3f51652d73760ae8fa8c9ffb3c330cc9e4fc17faf2ce545046e37944c69e462a1a82fe353
bd90a865aad41ed0b5b8f9d6fd010000ffff0300504b0304140006000800000021006b799616830000008a0000001c0000007468656d652f7468656d652f7468
656d654d616e616765722e786d6c0ccc4d0ac3201040e17da17790d93763bb284562b2cbaebbf600439c1a41c7a0d29fdbd7e5e38337cedf14d59b4b0d592c9c
070d8a65cd2e88b7f07c2ca71ba8da481cc52c6ce1c715e6e97818c9b48d13df49c873517d23d59085adb5dd20d6b52bd521ef2cdd5eb9246a3d8b4757e8d3f7
29e245eb2b260a0238fd010000ffff0300504b03041400060008000000210096b5ade296060000501b0000160000007468656d652f7468656d652f7468656d65
312e786d6cec594f6fdb3614bf0fd87720746f6327761a07758ad8b19b2d4d1bc46e871e698996d850a240d2497d1bdae38001c3ba618715d86d87615b8116d8
a5fb34d93a6c1dd0afb0475292c5585e9236d88aad3e2412f9e3fbff1e1fa9abd7eec70c1d1221294fda5efd72cd4324f1794093b0eddd1ef62fad79482a9c04
98f184b4bd2991deb58df7dfbb8ad755446282607d22d771db8b944ad79796a40fc3585ee62949606ecc458c15bc8a702910f808e8c66c69b9565b5d8a314d3c
94e018c8de1a8fa94fd05093f43672e23d06af89927ac06762a049136785c10607758d9053d965021d62d6f6804fc08f86e4bef210c352c144dbab999fb7b471
7509af678b985ab0b6b4ae6f7ed9ba6c4170b06c788a705430adf71bad2b5b057d03606a1ed7ebf5babd7a41cf00b0ef83a6569632cd467faddec9699640f671
9e76b7d6ac355c7c89feca9cccad4ea7d36c65b258a206641f1b73f8b5da6a6373d9c11b90c537e7f08dce66b7bbeae00dc8e257e7f0fd2badd5868b37a088d1
e4600ead1ddaef67d40bc898b3ed4af81ac0d76a197c86826828a24bb318f3442d8ab518dfe3a20f000d6458d104a9694ac6d88728eee2782428d60cf03ac1a5
193be4cbb921cd0b495fd054b5bd0f530c1931a3f7eaf9f7af9e3f45c70f9e1d3ff8e9f8e1c3e3073f5a42ceaa6d9c84e5552fbffdeccfc71fa33f9e7ef3f2d1
17d57859c6fffac327bffcfc793510d26726ce8b2f9ffcf6ecc98baf3efdfdbb4715f04d814765f890c644a29be408edf3181433567125272371be15c308d3f2
8acd249438c19a4b05fd9e8a1cf4cd296699771c393ac4b5e01d01e5a30a787d72cf1178108989a2159c77a2d801ee72ce3a5c545a6147f32a99793849c26ae6
6252c6ed637c58c5bb8b13c7bfbd490a75330f4b47f16e441c31f7184e140e494214d273fc80900aedee52ead87597fa824b3e56e82e451d4c2b4d32a423279a
668bb6690c7e9956e90cfe766cb37b077538abd27a8b1cba48c80acc2a841f12e698f13a9e281c57911ce298950d7e03aba84ac8c154f8655c4f2af074481847
bd804859b5e696007d4b4edfc150b12addbecba6b18b148a1e54d1bc81392f23b7f84137c2715a851dd0242a633f900710a218ed715505dfe56e86e877f0034e
16bafb0e258ebb4faf06b769e888340b103d3311da9750aa9d0a1cd3e4efca31a3508f6d0c5c5c398602f8e2ebc71591f5b616e24dd893aa3261fb44f95d843b
5974bb5c04f4edafb95b7892ec1108f3f98de75dc97d5772bdff7cc95d94cf672db4b3da0a6557f70db629362d72bcb0431e53c6066acac80d699a6409fb44d0
8741bdce9c0e4971624a2378cceaba830b05366b90e0ea23aaa241845368b0eb9e2612ca8c742851ca251ceccc70256d8d87265dd96361531f186c3d9058edf2
c00eafe8e1fc5c509031bb4d680e9f39a3154de0accc56ae644441edd76156d7429d995bdd88664a9dc3ad50197c38af1a0c16d684060441db02565e85f3b966
0d0713cc48a0ed6ef7dedc2dc60b17e92219e180643ed27acffba86e9c94c78ab90980d8a9f0913ee49d62b512b79626fb06dccee2a432bbc60276b9f7dec44b
7904cfbca4f3f6443ab2a49c9c2c41476dafd55c6e7ac8c769db1bc399161ee314bc2e75cf8759081743be1236ec4f4d6693e5336fb672c5dc24a8c33585b5fb
9cc24e1d4885545b58463634cc5416022cd19cacfccb4d30eb45296023fd35a458598360f8d7a4003bbaae25e331f155d9d9a5116d3bfb9a95523e51440ca2e0
088dd844ec6370bf0e55d027a012ae264c45d02f708fa6ad6da6dce29c255df9f6cae0ec38666984b372ab5334cf640b37795cc860de4ae2816e95b21be5ceaf
8a49f90b52a51cc6ff3355f47e0237052b81f6800fd7b802239daf6d8f0b1571a8426944fdbe80c6c1d40e8816b88b8569082ab84c36ff0539d4ff6dce591a26
ade1c0a7f669880485fd484582903d284b26fa4e2156cff62e4b9265844c4495c495a9157b440e091bea1ab8aaf7760f4510eaa69a6465c0e04ec69ffb9e65d0
28d44d4e39df9c1a52ecbd3607fee9cec7263328e5d661d3d0e4f62f44acd855ed7ab33cdf7bcb8ae889599bd5c8b3029895b6825696f6af29c239b75a5bb1e6
345e6ee6c28117e73586c1a2214ae1be07e93fb0ff51e133fb65426fa843be0fb515c187064d0cc206a2fa926d3c902e907670048d931db4c1a44959d366ad93
b65abe595f70a75bf03d616c2dd959fc7d4e6317cd99cbcec9c58b34766661c7d6766ca1a9c1b327531486c6f941c638c67cd22a7f75e2a37be0e82db8df9f30
254d30c1372581a1f51c983c80e4b71ccdd28dbf000000ffff0300504b0304140006000800000021000dd1909fb60000001b010000270000007468656d652f74
68656d652f5f72656c732f7468656d654d616e616765722e786d6c2e72656c73848f4d0ac2301484f78277086f6fd3ba109126dd88d0add40384e4350d363f24
51eced0dae2c082e8761be9969bb979dc9136332de3168aa1a083ae995719ac16db8ec8e4052164e89d93b64b060828e6f37ed1567914b284d262452282e3198
720e274a939cd08a54f980ae38a38f56e422a3a641c8bbd048f7757da0f19b017cc524bd62107bd5001996509affb3fd381a89672f1f165dfe514173d9850528
a2c6cce0239baa4c04ca5bbabac4df000000ffff0300504b01022d0014000600080000002100828abc13fa0000001c0200001300000000000000000000000000
000000005b436f6e74656e745f54797065735d2e786d6c504b01022d0014000600080000002100a5d6a7e7c0000000360100000b000000000000000000000000
002b0100005f72656c732f2e72656c73504b01022d00140006000800000021006b799616830000008a0000001c00000000000000000000000000140200007468
656d652f7468656d652f7468656d654d616e616765722e786d6c504b01022d001400060008000000210096b5ade296060000501b000016000000000000000000
00000000d10200007468656d652f7468656d652f7468656d65312e786d6c504b01022d00140006000800000021000dd1909fb60000001b010000270000000000
00000000000000009b0900007468656d652f7468656d652f5f72656c732f7468656d654d616e616765722e786d6c2e72656c73504b050600000000050005005d010000960a00000000}
{\*\colorschememapping 3c3f786d6c2076657273696f6e3d22312e302220656e636f64696e673d225554462d3822207374616e64616c6f6e653d22796573223f3e0d0a3c613a636c724d
617020786d6c6e733a613d22687474703a2f2f736368656d61732e6f70656e786d6c666f726d6174732e6f72672f64726177696e676d6c2f323030362f6d6169
6e22206267313d226c743122207478313d22646b3122206267323d226c743222207478323d22646b322220616363656e74313d22616363656e74312220616363
656e74323d22616363656e74322220616363656e74333d22616363656e74332220616363656e74343d22616363656e74342220616363656e74353d22616363656e74352220616363656e74363d22616363656e74362220686c696e6b3d22686c696e6b2220666f6c486c696e6b3d22666f6c486c696e6b222f3e}
{\*\latentstyles\lsdstimax267\lsdlockeddef0\lsdsemihiddendef1\lsdunhideuseddef1\lsdqformatdef0\lsdprioritydef99{\lsdlockedexcept \lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority0 \lsdlocked0 Normal;
\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 1;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 2;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 3;
\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 4;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 5;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 6;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 7;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 8;
\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 9;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 1;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 2;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 3;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 4;
\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 5;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 6;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 7;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 8;\lsdqformat1 \lsdpriority39 \lsdlocked0 toc 9;
\lsdqformat1 \lsdpriority35 \lsdlocked0 caption;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority10 \lsdlocked0 Title;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority11 \lsdlocked0 Subtitle;
\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority22 \lsdlocked0 Strong;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority20 \lsdlocked0 Emphasis;\lsdsemihidden0 \lsdunhideused0 \lsdpriority59 \lsdlocked0 Table Grid;
\lsdunhideused0 \lsdlocked0 Placeholder Text;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority1 \lsdlocked0 No Spacing;\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List;\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid;\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List;\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading;\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid;\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List Accent 1;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 1;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1 Accent 1;\lsdunhideused0 \lsdlocked0 Revision;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority34 \lsdlocked0 List Paragraph;
\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority29 \lsdlocked0 Quote;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority30 \lsdlocked0 Intense Quote;\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2 Accent 1;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 1;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List Accent 1;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid Accent 1;\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List Accent 2;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 2;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1 Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2 Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 2;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List Accent 2;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List Accent 2;\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid Accent 2;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid Accent 3;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1 Accent 3;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2 Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 3;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading Accent 3;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid Accent 3;\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading Accent 4;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 4;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1 Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2 Accent 4;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 4;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List Accent 4;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid Accent 4;\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List Accent 5;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 5;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1 Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2 Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 5;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List Accent 5;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List Accent 5;\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid Accent 5;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority60 \lsdlocked0 Light Shading Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority61 \lsdlocked0 Light List Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority62 \lsdlocked0 Light Grid Accent 6;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority65 \lsdlocked0 Medium List 1 Accent 6;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority66 \lsdlocked0 Medium List 2 Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 6;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority70 \lsdlocked0 Dark List Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority71 \lsdlocked0 Colorful Shading Accent 6;
\lsdsemihidden0 \lsdunhideused0 \lsdpriority72 \lsdlocked0 Colorful List Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdpriority73 \lsdlocked0 Colorful Grid Accent 6;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority19 \lsdlocked0 Subtle Emphasis;
\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority21 \lsdlocked0 Intense Emphasis;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority31 \lsdlocked0 Subtle Reference;
\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority32 \lsdlocked0 Intense Reference;\lsdsemihidden0 \lsdunhideused0 \lsdqformat1 \lsdpriority33 \lsdlocked0 Book Title;\lsdpriority37 \lsdlocked0 Bibliography;
\lsdqformat1 \lsdpriority39 \lsdlocked0 TOC Heading;}}{\*\datastore 0105000002000000180000004d73786d6c322e534158584d4c5265616465722e352e3000000000000000000000060000
d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff090006000000000000000000000001000000010000000000000000100000feffffff00000000feffffff0000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffdfffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffffffffffffec69d9888b8b3d4c859eaf6cd158be0f000000000000000000000000d070
a7c59f57c701feffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000105000000000000}}Any raw assets you want to be deployed with your application can be placed in
this directory (and child directories) and given a Build Action of "AndroidAsset".

These files will be deployed with you package and will be accessible using Android's
AssetManager, like this:

public class ReadAsset : Activity
{
	protected override void OnCreate (Bundle bundle)
	{
		base.OnCreate (bundle);

		InputStream input = Assets.Open ("my_asset.txt");
	}
}

Additionally, some Android functions will automatically load asset files:

Typeface tf = Typeface.CreateFromAsset (Context.Assets, "fonts/samplefont.ttf");Images, layout descriptions, binary blobs and string dictionaries can be included 
in your application as resource files.  Various Android APIs are designed to 
operate on the resource IDs instead of dealing with images, strings or binary blobs 
directly.

For example, a sample Android app that contains a user interface layout (Main.xml),
an internationalization string table (Strings.xml) and some icons (drawable/Icon.png) 
would keep its resources in the "Resources" directory of the application:

Resources/
    Drawable/
        Icon.png

    Layout/
        Main.axml

    Values/
        Strings.xml

In order to get the build system to recognize Android resources, the build action should be set 
to "AndroidResource".  The native Android APIs do not operate directly with filenames, but 
instead operate on resource IDs.  When you compile an Android application that uses resources, 
the build system will package the resources for distribution and generate a class called
"Resource" that contains the tokens for each one of the resources included. For example, 
for the above Resources layout, this is what the Resource class would expose:

public class Resource {
    public class Drawable {
        public const int Icon = 0x123;
    }

    public class Layout {
        public const int Main = 0x456;
    }

    public class String {
        public const int FirstString = 0xabc;
        public const int SecondString = 0xbcd;
    }
}

You would then use Resource.Drawable.Icon to reference the Drawable/Icon.png file, or 
Resource.Layout.Main to reference the Layout/Main.axml file, or Resource.String.FirstString
to reference the first string in the dictionary file Values/Strings.xml.# MonoGame Tests

The MonoGame Tests run against XNA on Windows and MonoGame on Windows,
Mac OS X and Linux.  They serve as an assurance that MonoGame conforms
as closely as possible to XNA.

Simple unit tests make assertions about MonoGame's core class
properties, methods and behavior to guarantee compatibility with XNA in
those regards.  Additionally, visual tests verify via frame capture and
comparison that MonoGame renders equivalently to XNA.

Currently, on Windows, the tests can be run using NUnit and target
either XNA or MonoGame.  On Mac OS X and Linux, the tests target
MonoGame and are implemented in an executable assembly that can be run
and debugged directly.  After execution using the custom test runner,
and HTML report of the results will be loaded in your default browser,
and a log of stdout can be found in bin\$(Configuration)\stdout.txt.

*Note: Currently there is no way to skip or select certain tests to run
using the custom runner.  This functionality is coming soon.*

## Rendering Tests

Most rendering tests do not require a game loop, but just need a
GraphicsDevice to be able to render things. These tests can inherit from
GraphicsDeviceTestFixtureBase and use the supplied GraphicsDevice 'gd'
to render. Tests that require rendering were formerly implemented with
the VisualTestFixtureBase (we call these "visual tests"), but this is no
longer recommended unless the test requires an actual Game loop or tests
functionality of the Game class itself because these tests are slower
and harder to implement. When creating a new rendering test, the first
run will fail because there is no reference image. Running the test will
capture and save the result. Run the test with the XNA test project to
get a reference image that checks XNA compatibility, or with MG to make
sure no regression occurs. After adding the captured frame as a
reference image, the test should pass.


### GraphicsDeviceTestFixtureBase

There are 3 methods in GraphicsDeviceTestFixtureBase that can be used to
capture a frame and compare it to a reference image.

- `PrepareFrameCapture`: Call this before rendering, so a RenderTarget can be
prepared and set as the target for the GraphicsDevice. Optionally pass
in the amount of frames you expect to capture. This is used for naming
the captures when saving them (i.e. frame1.png or frame001.png) and
the amount of captured frames will also be checked explicitly unless
the ExactNumberSubmits flag is set to false.
- `SubmitFrame`: Store the content of the render target in a list of
submitted frames
- `CheckFrames`: Call this when all frames are submitted. Checks all
submitted frames against reference images if they can be found. Will
also write out the captured image and a diff of captured image vs
reference image if required by the WriteCapture and WriteDiffs settings.
Compared frames get a similarity score between 0 and 1. If this score is
higher than the set Similarity the test will pass.
For ease of use, when no frame was submitted but PrepareFrameCapture has
been called, this will submit a frame. Because of this tests that only
submit one frame just need to be wrapped in PrepareFrameCapture/CheckFrames
calls and can render as usual in between.


If you still think you need a visual test to properly test a feature,
read the paragraphs below to get a sense of how to get started.

MonoGame's visual tests are implemented as ```Game```s and
```GameComponent```s whose output is captured and compared to known-good
reference renderings.  Performance is ignored in these tests:  the focus
here is correct drawing.

### Workflow for Implementing a Visual Test

A good visual test, like any good test, should perform the minimum work
necessary to verify that the functionality under test is correct.  As
much as possible, drawing and test code should be made modular by
inheriting from ```GameComponent```, ```DrawableGameComponent```,
```VisualTestGameComponent```, or ```VisualTestDrawableGameComponent```
to encourage reuse, rather than duplication, in other tests.

Here is one possible workflow for implementing a visual test (assuming
the test fixture is already set up):

> Before you start:  
> Examine the existing visual tests to get a sense of how components
> are being composed into a test and what components may already
> satisfy part of the requirements of the new test.


1. Implement any new drawing logic needed in a new subclass of one of
   the \*Component base classes.

2. Compose your test Game in a new [Test] method.  As this stage, you
   can run the new test directly to visually verify the rendering.

3. Add a FrameCompareComponent to your test Game with at least one
   IFrameComparer implementation.  Use the ```FrameCompareComponent```'s
   predicate to capture and compare frames.

4. Pass the FrameCompareComponent.Results to the diffing, logging and
   assertion utility methods provided by ```VisualTestFixtureBase```

5. The first time a visual test is run, it will fail for lack of
   reference images to compare the captured images to.  However, it will
   write the captured frames to bin\$(Configuration)\CapturedFrames\{TestDir}.

6. Proof the images generated from the first run to ensure that they are
   correct, then add them to the test project in
   Assets\ReferenceImages\$TestDir.  **Be sure to add them in the
   projects for all platforms!**  These files should have their build
   actions set to "Compile" and "Copy if newer".

7. Rerun the visual test.  The reference images should be copied into
   place and the test should now pass.

8. XOR diffs between the reference images and captured frames are output
   into bin\$(Configuration)\Diffs\{TestDir} for debugging purposes.


### Notes For Implementing Correct Visual Tests

- **Visual tests must be marked as [RequiresSTA] to work correctly on
  all platforms**
- Try not to rely on ```GameComponent.Update```, since capturing frames
  can make the game run slowly and result in multiple Update calls per
  Draw.  Instead, inherit from ```VisualTestGameComponent``` or
  ```VisualTestDrawableGameComponent``` and override
  ```UpdateOncePerDraw```.
- For similarity thresholds, prefer Constants.StandardRequiredSimilarity
  unless there is a very good reason to choose another value.  This will
  allow the strictness of all the tests to be adjusted together in the
  future, as requirements change.
- Use the Paths static class to reduce typos in resource paths.

## Special Considerations

- For new test fixtures, call Paths.SetStandardWorkingDirectory() in
  [SetUp] \(VisualTestBase does this for you\) to ensure that the
  ```ContentManager``` can find your assets on all platforms.
- Note that all platforms are forced to run in Synchronous mode and
  that this doesn't always work perfectly on all platforms yet.

## NUnit Configuration

There are a few things to know about running these tests under NUnit:

- You must run the -x86 versions of NUnit, because XNA won't work with
  the 64-bit versions.
- You must disable shadow copying because having it enabled makes it
  impossible for the ContentManager to find any assets.
  - GUI: Tools > Settings > Test Loader > Advanced
  - CLI: /noshadow
- For debugger support, Run tests directly in the NUnit process, (note
  that this may cause a few-seconds-long hang when exiting NUnit after
  running a visual test) otherwise choose 'single separate process'
  - This setting can be found in:
    ```Tools > Settings > Test Loader > Assembly Isolation```
For XNA effects can be compiled using the .csproj in this folder.
Simply build the csproj using MSBuild to compile the effects using
XNA's content importer and processor. To add an effect, just
copy-paste an existing entry and replace the effect path and name.

For DirectX and OpenGL use the pipeline tool to build the effects.

These files can be used for commercial and non-commercial projects that makes use of MonoGame.

* The NetBuffer object is gone; instead there are NetOutgoingMessage and NetIncomingMessage objects

* No need to allocate a read buffer before calling ReadMessage






Improvements over last version of library:

* New delivery type: Reliable sequenced (Lost packets are resent but late arrivals are dropped)
* Disconnects and shutdown requests are now queued properly, so calling shutdown will still send any queued messages before shutting down
* All messages are pooled/recycled for zero garbage
* Reduced CPU usage and lower latencies (in the <1 ms range, but still) due to better socket polling
* All public members of NetPeer/NetConnection are completely thread safe
* Larger number of delivery channels
* More exact roundtrip measurement
* Method serialize entire objects via reflection
* Unique identifier now exists for all peers/connections
* More flexible peer discovery; filters possible and arbitrary data can be sent with response
* Much better protection against malformed messages crashing the app

API enhancements:
* NetPeerConfiguration immutable properties now locked once NetPeer is initialized
* Messages cannot be send twice by accident
* Impossible to confuse sending and receiving buffers since they're different classes
* No more confusion if user should create a buffer or preallocate and reuse



PER MESSAGE:
7 bits - NetMessageType
1 bit - Is a message fragment?

[8 bits NetMessageLibraryType, if NetMessageType == Library]

[16 bits sequence number, if NetMessageType >= UserSequenced]

8/16 bits - Payload length in bits (variable size ushort)

[16 bits fragments group id, if fragmented]
[16 bits fragments total count, if fragmented]
[16 bits fragment number, if fragmented]

[x - Payload] if length > 0


Completed features:
* Message coalescing
* Peer, connection statistics
* Lag, loss and duplication simulation for testing
* Connection approval
* Throttling
* Clock synchronization to detect jitter per packet (NetTime.RemoteNow)
* Peer discovery
* Message fragmentation

Missing features:
* Receipts 25% done, need design
* More realistic lag/loss (lumpy)
* Detect estimated packet loss
* More advanced ack packet

**This package only works if you are targeting .NET Core.** This package allows you to package up your MonoGame game into a flatpak installer for Linux.

## Requirements:
- netcoreapp as the target
- flatpak
  - org.freedesktop.Platform/x86_64/1.6
  - org.freedesktop.Sdk/x86_64/1.6

Flatpak install instructions: [https://flatpak.org/setup/](https://flatpak.org/setup/)

To install the required runtimes, simply do:
```sh
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.freedesktop.Platform/x86_64/1.6
flatpak install flathub org.freedesktop.Sdk/x86_64/1.6
```

## Usage:
Call the publish command as you normally would: `dotnet publish -r linux-x64`, the resulting flatpak should get generated in the output directory.

## Customization:
This nuget package offers the following properties for customizing the build of the flatpak. Simply set them in the csproj or pass them to msbuild to change their values:

```
| Variable Name            | Description / Default value            |
| ------------------------ | -------------------------------------- |
| MGFlatpakIntermediateDir | Folder for temporary files.            |
|                          | $(IntermediateOutputPath)              |
| ------------------------ | -------------------------------------- |
| MGFlatpakOutputPath      | The output folder for the flatpak.     |
|                          | $(OutputPath)                          |
| ------------------------ | -------------------------------------- |
| MGFlatpakProjectDir      | The current project directory.         |
|                          | $(ProjectDir)                          |
| ------------------------ | -------------------------------------- |
| MGFlatpakPublishDir      | The publish output folder.             |
|                          | $(PublishDir)                          |
| ------------------------ | -------------------------------------- |
| MGFlatpakAssemblyName    | The output assembly to run.            |
|                          | $(AssemblyName)                        |
| ------------------------ | -------------------------------------- |
| MGFlatpakTitle           | The game title.                        |
|                          | $(AssemblyTitle)                       |
| ------------------------ | -------------------------------------- |
| MGFlatpakId              | The game id.                           |
|                          | com.$(Company).$(AssemblyName)         |
| ------------------------ | -------------------------------------- |
| MGFlatpakIcon            | The icon file, needs to be png format. |
|                          | Icon.png                               |
```

