The MIT License (MIT)

Copyright (c) 2014-2020 Omar Cornut

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
(Click "Preview" to turn any http URL into a clickable link)

1. PLEASE CAREFULLY READ: [FAQ](https://github.com/ocornut/imgui/blob/master/docs/FAQ.md)

2. PLEASE CAREFULLY READ: https://github.com/ocornut/imgui/issues/2261

2. FOR FIRST-TIME USERS ISSUES COMPILING/LINKING/RUNNING/LOADING FONTS,  please use the [Discord server](http://discord.dearimgui.org).

3. PLEASE MAKE SURE that you have: read the FAQ; explored the contents of `ShowDemoWindow()` including the Examples menu; searched among Issues; used your IDE to search for keywords in all sources and text files; and read the link provided in (1) (2).

4. Be mindful that messages are being sent to the e-mail box of "Watching" users. Try to proof-read your messages before sending them. Edits are not seen by those users.

5. Delete points 1-6 and PLEASE FILL THE TEMPLATE BELOW before submitting your issue.

Thank you!

----

_(you may also go to Demo>About Window, and click "Config/Build Information" to obtain a bunch of detailed information that you can paste here)_

**Version/Branch of Dear ImGui:**

Version: XXX
Branch: XXX _(master/viewport/docking/etc.)_

**Back-end/Renderer/Compiler/OS**

Back-ends: imgui_impl_XXX.cpp + imgui_impl_XXX.cpp _(or specify if using a custom engine/back-end)_
Compiler: XXX _(if the question is related to building or platform specific features)_
Operating System: XXX

**My Issue/Question:**

XXX _(please provide as much context as possible)_

**Screenshots/Video**

XXX _(you can drag files here)_

**Standalone, minimal, complete and verifiable example:** _(see https://github.com/ocornut/imgui/issues/2261)_
```
// Please do not forget this!
ImGui::Begin("Example Bug");
MoreCodeToExplainMyIssue();
ImGui::End();
```
(Click "Preview" to turn any http URL into a clickable link)

PLEASE CAREFULLY READ:
https://github.com/ocornut/imgui/issues/2261

(Clear this template before submitting your PR)
dear imgui
CHANGELOG

This document holds the user-facing changelog that we also use in release notes.
We generally fold multiple commits pertaining to the same topic as a single entry.
Changes to the examples/bindings are included within the individual .cpp files in the examples/ folder.

RELEASE NOTES:                  https://github.com/ocornut/imgui/releases
REPORT ISSUES, ASK QUESTIONS:   https://github.com/ocornut/imgui/issues
COMMITS HISTORY:                https://github.com/ocornut/imgui/commits/master

WHEN TO UPDATE?

- Keeping your copy of dear imgui updated once in a while is recommended.
- It is generally safe to sync to the latest commit in master.
  The library is fairly stable and regressions tends to be fixed fast when reported.

HOW TO UPDATE?

- Overwrite every file except imconfig.h (if you have modified it).
- You may also locally branch to modify imconfig.h and merge latest into your branch.
- Read the `Breaking Changes` section (in imgui.cpp or here in the Changelog).
- If you have a problem with a missing function/symbols, search for its name in the code, there will likely be a comment about it.
- If you are dropping this repository in your codebase, please leave the demo and text files in there, they will be useful.
- You may diff your previous Changelog with the one you just copied and read that diff.
- You may enable `IMGUI_DISABLE_OBSOLETE_FUNCTIONS` in imconfig.h to forcefully disable legacy names and symbols.
  Doing it every once in a while is a good way to make sure you are not using obsolete symbols. Dear ImGui is in active development,
  and API updates have been a little more frequent lately. They are documented below and in imgui.cpp and should not affect all users.
- Please report any issue!


-----------------------------------------------------------------------
 VERSION 1.75 WIP (In Progress)
-----------------------------------------------------------------------

Breaking Changes:
- Removed redirecting functions/enums names that were marked obsolete in 1.53 (December 2017):
  - ShowTestWindow()                    -> use ShowDemoWindow()
  - IsRootWindowFocused()               -> use IsWindowFocused(ImGuiFocusedFlags_RootWindow)
  - IsRootWindowOrAnyChildFocused()     -> use IsWindowFocused(ImGuiFocusedFlags_RootAndChildWindows)
  - SetNextWindowContentWidth(w)        -> use SetNextWindowContentSize(ImVec2(w, 0.0f)
  - GetItemsLineHeightWithSpacing()     -> use GetFrameHeightWithSpacing()
  - ImGuiCol_ChildWindowBg              -> use ImGuiCol_ChildBg
  - ImGuiStyleVar_ChildWindowRounding   -> use ImGuiStyleVar_ChildRounding
  - ImGuiTreeNodeFlags_AllowOverlapMode -> use ImGuiTreeNodeFlags_AllowItemOverlap
  - IMGUI_DISABLE_TEST_WINDOWS          -> use IMGUI_DISABLE_DEMO_WINDOWS
  If you were still using the old names, while you are cleaning up, considering enabling
  IMGUI_DISABLE_OBSOLETE_FUNCTIONS in imconfig.h even temporarily to have a pass at finding
  and removing up old API calls, if any remaining.
- Removed implicit default parameter to IsMouseDragging(int button = 0) to be consistent
  with other mouse functions (none of the other functions have it).
- Obsoleted calling ImDrawList::PrimReserve() with a negative count (which was vaguely
  documented and rarely if ever used). Instead we added an explicit PrimUnreserve() API
  which can be implemented faster. Also clarified pre-existing constraints which weren't
  documented (can only unreserve from the last reserve call). If you suspect you ever
  used that feature before, #define IMGUI_DEBUG_PARANOID in imconfig.h to catch existing
  calls. [@ShironekoBen]
- Limiting Columns()/BeginColumns() api to 64 columns with an assert. While the current code
  technically supports it, future code may not so we're putting the restriction ahead.
- imgui_internal.h: changed ImRect() default constructor initializes all fields to 0.0f instead
  of (FLT_MAX,FLT_MAX,-FLT_MAX,-FLT_MAX). If you used ImRect::Add() to create bounding boxes by
  adding multiple points into it, you may need to fix your initial value.

Other Changes:
- Inputs: Added ImGuiMouseButton enum for convenience (e.g. ImGuiMouseButton_Right=1).
  We forever guarantee that the existing value will not changes so existing code is free to use 0/1/2.
- ColorEdit: Fix label alignment when using ImGuiColorEditFlags_NoInputs. (#2955) [@rokups]
- ColorEdit: In HSV display of a RGB stored value, attempt to locally preserve Saturation
  when Value==0.0 (similar to changes done in 1.73 for Hue). Removed Hue editing lock since
  those improvements in 1.73 makes them unnecessary. (#2722, #2770). [@rokups]
- ColorEdit: "Copy As" context-menu tool shows hex values with a '#' prefix instead of '0x'.
- ColorEdit: "Copy As" content-menu tool shows hex values both with/without alpha when available.
- ImDrawList: Add AddNgon(), AddNgonFilled() API with a guarantee on the explicit segment count.
  In the current branch they are essentially the same as AddCircle(), AddCircleFilled() but as
  we will rework the circle rendering functions to use textures and automatic segment count
  selection, those new api can fill a gap. [@ShironekoBen]
- Misc: Added ImGuiMouseCursor_NotAllowed enum so it can be used by more shared widgets. [@rokups]
- Misc: Added misc/single_file/imgui_single_file.h, We use this to validate compiling all *.cpp
  files in a same compilation unit. Actual users of that technique (also called "Unity builds")
  can generally provide this themselves, so we don't really recommend you use this. [@rokups]
- Backends: GLFW, SDL, Win32, OSX, Allegro: Added support for ImGuiMouseCursor_NotAllowed. [@rokups]
- Backends: GLFW: Added support for the missing mouse cursors newly added in GLFW 3.4+. [@rokups]
- Backends: SDL: Wayland: use SDL_GetMouseState (because there is no global mouse state available
  on Wayland). (#2800, #2802) [@NeroBurner]
- Backends: Win32: Added support for #define IMGUI_IMPL_WIN32_DISABLE_GAMEPAD to disable all
  XInput using code, and IMGUI_IMPL_WIN32_DISABLE_LINKING_XINPUT to disable linking with XInput,
  the later may be problematic if compiling with recent Windows SDK and you want your app to run
  on Windows 7. You can instead try linking with Xinput9_1_0.lib instead. (#2716)
- CI: Added PVS-Studio static analysis on the continuous-integration server. [@rokups]
- Examples: Explicitly adding -DIMGUI_IMPL_OPENGL_LOADER_GL3W to Makefile to match linking
  settings (otherwise if another loader such as Glew is accessible, the OpenGL3 backend might
  automatically use it). (#2919, #2798)
- Examples: Metal: Wrapped main loop in @autoreleasepool block to ensure allocations get freed
  even if underlying system event loop gets paused due to app nap. (#2910, #2917) [@bear24rw]
- Examples: Added support for glbindings OpenGL loader. (#2870) [@rokups]


-----------------------------------------------------------------------
 VERSION 1.74 (Released 2019-11-25)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.74

Breaking Changes:
- Removed redirecting functions/enums names that were marked obsolete in 1.52 (October 2017):
  - Begin() [old 5 args version]     -> use Begin() [3 args], use SetNextWindowSize() SetNextWindowBgAlpha() if needed
  - IsRootWindowOrAnyChildHovered()  -> use IsWindowHovered(ImGuiHoveredFlags_RootAndChildWindows)
  - AlignFirstTextHeightToWidgets()  -> use AlignTextToFramePadding()
  - SetNextWindowPosCenter()         -> use SetNextWindowPos() with a pivot of (0.5f, 0.5f)
  - ImFont::Glyph                    -> use ImFontGlyph
  If you were still using the old names, read "API Breaking Changes" section of imgui.cpp to find out
  the new names or equivalent features, or see how they were implemented until 1.73.
- Inputs: Fixed a miscalculation in the keyboard/mouse "typematic" repeat delay/rate calculation, used
  by keys and e.g. repeating mouse buttons as well as the GetKeyPressedAmount() function.
  If you were using a non-default value for io.KeyRepeatRate (previous default was 0.250), you can
  add +io.KeyRepeatDelay to it to compensate for the fix.
  The function was triggering on: 0.0 and (delay+rate*N) where (N>=1). Fixed formula responds to (N>=0).
  Effectively it made io.KeyRepeatRate behave like it was set to (io.KeyRepeatRate + io.KeyRepeatDelay).
  Fixed the code and altered default io.KeyRepeatRate,Delay from 0.250,0.050 to 0.300,0.050 to compensate.
  If you never altered io.KeyRepeatRate nor used GetKeyPressedAmount() this won't affect you.
- Misc: Renamed IMGUI_DISABLE_FORMAT_STRING_FUNCTIONS to IMGUI_DISABLE_DEFAULT_FORMAT_FUNCTIONS. (#1038)
- Misc: Renamed IMGUI_DISABLE_MATH_FUNCTIONS to IMGUI_DISABLE_DEFAULT_MATH_FUNCTIONS.
- Fonts: ImFontAtlas::AddCustomRectRegular() now requires an ID larger than 0x110000 (instead of 0x10000) to
  conform with supporting Unicode planes 1-16 in a future update. ID below 0x110000 will now assert.
- Backends: DX12: Added extra ID3D12DescriptorHeap parameter to ImGui_ImplDX12_Init() function.
  The value is unused in master branch but will be used by the multi-viewport feature. (#2851) [@obfuscate]

Other Changes:
- InputText, Nav: Fixed Home/End key broken when activating Keyboard Navigation. (#787)
- InputText: Filter out ASCII 127 (DEL) emitted by low-level OSX layer, as we are using the Key value. (#2578)
- Layout: Fixed a couple of subtle bounding box vertical positioning issues relating to the handling of text
  baseline alignment. The issue would generally manifest when laying out multiple items on a same line,
  with varying heights and text baseline offsets.
  Some specific examples, e.g. a button with regular frame padding followed by another item with a
  multi-line label and no frame padding, such as: multi-line text, small button, tree node item, etc.
  The second item was correctly offset to match text baseline, and would interact/display correctly,
  but it wouldn't push the contents area boundary low enough.
- Scrollbar: Fixed an issue where scrollbars wouldn't display on the frame following a frame where
  all child window contents would be culled.
- ColorPicker: Fixed SV triangle gradient to block (broken in 1.73). (#2864, #2711). [@lewa-j]
- TreeNode: Fixed combination of ImGuiTreeNodeFlags_SpanFullWidth and ImGuiTreeNodeFlags_OpenOnArrow
  incorrectly locating the arrow hit position to the left of the frame. (#2451, #2438, #1897)
- TreeNode: The collapsing arrow accepts click even if modifier keys are being held, facilitating
  interactions with custom multi-selections patterns. (#2886, #1896, #1861)
- TreeNode: Added IsItemToggledOpen() to explicitly query if item was just open/closed, facilitating
  interactions with custom multi-selections patterns. (#1896, #1861)
- DragScalar, SliderScalar, InputScalar: Added p_ prefix to parameter that are pointers to the data
  to clarify how they are used, and more comments redirecting to the demo code. (#2844)
- Error handling: Assert if user mistakenly calls End() instead of EndChild() on a child window. (#1651)
- Misc: Optimized storage of window settings data (reducing allocation count).
- Misc: Windows: Do not use _wfopen() if IMGUI_DISABLE_WIN32_FUNCTIONS is defined. (#2815)
- Misc: Windows: Disabled win32 function by default when building with UWP. (#2892, #2895)
- Misc: Using static_assert() when using C++11, instead of our own construct (avoid zealous Clang warnings).
- Misc: Added IMGUI_DISABLE_FILE_FUNCTIONS/IMGUI_DISABLE_DEFAULT_FILE_FUNCTION to nullify or disable
  default implementation of ImFileXXX functions linking with fopen/fclose/fread/fwrite. (#2734)
- Docs: Improved and moved FAQ to docs/FAQ.md so it can be readable on the web. [@ButternCream, @ocornut]
- Docs: Moved misc/fonts/README.txt to docs/FONTS.txt.
- Docs: Added permanent redirect from https://www.dearimgui.org/faq to FAQ page.
- Demo: Added simple item reordering demo in Widgets -> Drag and Drop section. (#2823, #143) [@rokups]
- Metrics: Show wire-frame mesh and approximate surface area when hovering ImDrawCmd. [@ShironekoBen]
- Metrics: Expose basic details of each window key/value state storage.
- Examples: DX12: Using IDXGIDebug1::ReportLiveObjects() when DX12_ENABLE_DEBUG_LAYER is enabled.
- Examples: Emscripten: Removed BINARYEN_TRAP_MODE=clamp from Makefile which was removed in Emscripten 1.39.0
  but required prior to 1.39.0, making life easier for absolutely no-one. (#2877, #2878) [@podsvirov]
- Backends: OpenGL3: Fix building with pre-3.2 GL loaders which do not expose glDrawElementsBaseVertex(),
  using runtime GL version to decide if we set ImGuiBackendFlags_RendererHasVtxOffset. (#2866, #2852) [@dpilawa]
- Backends: OSX: Fix using Backspace key. (#2578, #2817, #2818) [@DiligentGraphics]
- Backends: GLFW: Previously installed user callbacks are now restored on shutdown. (#2836) [@malte-v]
- CI: Set up a bunch of continuous-integration tests using GitHub Actions. We now compile many of the example
  applications on Windows, Linux, MacOS, iOS, Emscripten. Removed Travis integration. (#2865) [@rokups]


-----------------------------------------------------------------------
 VERSION 1.73 (Released 2019-09-24)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.73

Other Changes:

- Nav, Scrolling: Added support for Home/End key. (#787)
- ColorEdit: Disable Hue edit when Saturation==0 instead of letting Hue values jump around.
- ColorEdit, ColorPicker: In HSV display of a RGB stored value, attempt to locally preserve Hue
  when Saturation==0, which reduces accidentally lossy interactions. (#2722, #2770) [@rokups]
- ColorPicker: Made rendering aware of global style alpha of the picker can be faded out. (#2711)
  Note that some elements won't accurately fade down with the same intensity, and the color wheel
  when enabled will have small overlap glitches with (style.Alpha < 1.0).
- TabBar: Fixed single-tab not shrinking their width down.
- TabBar: Fixed clicking on a tab larger than tab-bar width creating a bouncing feedback loop.
- TabBar: Feed desired width (sum of unclipped tabs width) into layout system to allow for auto-resize. (#2768)
  (before 1.71 tab bars fed the sum of current width which created feedback loops in certain situations).
- TabBar: Improved shrinking for large number of tabs to avoid leaving extraneous space on the right side.
  Individuals tabs are given integer-rounded width and remainder is spread between tabs left-to-right.
- Columns, Separator: Fixed a bug where non-visible separators within columns would alter the next row position
  differently than visible ones.
- SliderScalar: Improved assert when using U32 or U64 types with a large v_max value. (#2765) [@loicmouton]
- DragInt, DragFloat, DragScalar: Using (v_min > v_max) allows locking any edits to the value.
- DragScalar: Fixed dragging of unsigned values on ARM cpu (float to uint cast is undefined). (#2780) [@dBagrat]
- TreeNode: Added ImGuiTreeNodeFlags_SpanAvailWidth flag. (#2451, #2438, #1897) [@Melix19, @PathogenDavid]
  This extends the hit-box to the right-most edge, even if the node is not framed.
  (Note: this is not the default in order to allow adding other items on the same line. In the future we will
  aim toward refactoring the hit-system to be front-to-back, allowing more natural overlapping of items,
  and then we will be able to make this the default.)
- TreeNode: Added ImGuiTreeNodeFlags_SpanFullWidth flag. This extends the hit-box to both the left-most and
  right-most edge of the working area, bypassing indentation.
- CollapsingHeader: Added support for ImGuiTreeNodeFlags_Bullet and ImGuiTreeNodeFlags_Leaf on framed nodes,
  mostly for consistency. (#2159, #2160) [@goran-w]
- Selectable: Added ImGuiSelectableFlags_AllowItemOverlap flag in public api (was previously internal only).
- Style: Allow style.WindowMenuButtonPosition to be set to ImGuiDir_None to hide the collapse button. (#2634, #2639)
- Font: Better ellipsis ("...") drawing implementation. Instead of drawing three pixel-ey dots (which was glaringly
  unfitting with many types of fonts) we first attempt to find a standard ellipsis glyphs within the loaded set.
  Otherwise we render ellipsis using '.' from the font from where we trim excessive spacing to make it as narrow
  as possible. (#2775) [@rokups]
- ImDrawList: Clarified the name of many parameters so reading the code is a little easier. (#2740)
- ImDrawListSplitter: Fixed merging channels if the last submitted draw command used a different texture. (#2506)
- Using offsetof() when available in C++11. Avoids Clang sanitizer complaining about old-style macros. (#94)
- ImVector: Added find(), find_erase(), find_erase_unsorted() helpers.
- Added a mechanism to compact/free the larger allocations of unused windows (buffers are compacted when
  a window is unused for 60 seconds, as per io.ConfigWindowsMemoryCompactTimer = 60.0f). Note that memory
  usage has never been reported as a problem, so this is merely a touch of overzealous luxury. (#2636)
- Documentation: Various tweaks and improvements to the README page. [@ker0chan]
- Backends: OpenGL3: Tweaked initialization code allow application calling ImGui_ImplOpenGL3_CreateFontsTexture()
  before ImGui_ImplOpenGL3_NewFrame(), which sometimes can be convenient.
- Backends: OpenGL3: Attempt to automatically detect default GL loader by using __has_include. (#2798) [@o-micron]
- Backends: DX11: Fixed GSGetShader() call not passing an initialized instance count, which would
  generally make the DX11 debug layer complain (bug added in 1.72).
- Backends: Vulkan: Added support for specifying multisample count. Set 'ImGui_ImplVulkan_InitInfo::MSAASamples' to
   one of the VkSampleCountFlagBits values to use, default is non-multisampled as before. (#2705, #2706) [@vilya]
- Examples: OSX: Fix example_apple_opengl2/main.mm not forwarding mouse clicks and drags correctly. (#1961, #2710)
  [@intonarumori, @ElectricMagic]
- Misc: Updated stb_rect_pack.h from 0.99 to 1.00 (fixes by @rygorous: off-by-1 bug in best-fit heuristic,
  fix handling of rectangles too large to fit inside texture). (#2762) [@tido64]


-----------------------------------------------------------------------
 VERSION 1.72b (Released 2019-07-31)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.72b

Other Changes:

- Nav, Scrolling: Fixed programmatic scroll leading to a slightly incorrect scroll offset when
  the window has decorations or a menu-bar (broken in 1.71). This was mostly noticeable when
  a keyboard/gamepad movement led to scrolling the view, or using e.g. SetScrollHereY() function.
- Nav: Made hovering non-MenuItem Selectable not re-assign the source item for keyboard navigation.
- Nav: Fixed an issue with NavFlattened window flag (beta) where widgets not entirely fitting
  in child window (often selectables because of their protruding sides) would be not considered
  as entry points to to navigate toward the child window. (#787)


-----------------------------------------------------------------------
 VERSION 1.72 (Released 2019-07-27)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.72

Breaking Changes:
- Removed redirecting functions/enums names that were marked obsolete in 1.51 (June 2017):
  - ImGuiCol_Column*, ImGuiSetCond_* enums.
  - IsItemHoveredRect(), IsPosHoveringAnyWindow(), IsMouseHoveringAnyWindow(), IsMouseHoveringWindow() functions.
  - IMGUI_ONCE_UPON_A_FRAME macro.
  If you were still using the old names, read "API Breaking Changes" section of imgui.cpp to find out
  the new names or equivalent features.
- Renamed ImFontAtlas::CustomRect to ImFontAtlasCustomRect. Kept redirection typedef (will obsolete).
- Removed TreeAdvanceToLabelPos() which is rarely used and only does SetCursorPosX(GetCursorPosX() + GetTreeNodeToLabelSpacing()).
  Kept redirection function (will obsolete). (#581, #324)

Other Changes:
- Scrolling: Made mouse-wheel scrolling lock the underlying window until the mouse is moved again or
  until a short delay expires (~2 seconds). This allow uninterrupted scroll even if child windows are
  passing under the mouse cursor. (#2604)
- Scrolling: Made it possible for mouse wheel and navigation-triggered scrolling to override a call to
  SetScrollX()/SetScrollY(), making it possible to use a simpler stateless pattern for auto-scrolling:
     // (Submit items..)
     if (ImGui::GetScrollY() >= ImGui::GetScrollMaxY())  // If scrolling at the already at the bottom..
         ImGui::SetScrollHereY(1.0f);                    // ..make last item fully visible
- Scrolling: Added SetScrollHereX(), SetScrollFromPosX() for completeness. (#1580) [@kevreco]
- Scrolling: Mouse wheel scrolling while hovering a child window is automatically forwarded to parent window
  if ScrollMax is zero on the scrolling axis.
  Also still the case if ImGuiWindowFlags_NoScrollWithMouse is set (not new), but previously the forwarding
  would be disabled if ImGuiWindowFlags_NoScrollbar was set on the child window, which is not the case
  any more. Forwarding can still be disabled by setting ImGuiWindowFlags_NoInputs. (amend #1502, #1380).
- Window: Fixed InnerClipRect right-most coordinates using wrong padding setting (introduced in 1.71).
- Window: Fixed old SetWindowFontScale() api value from not being inherited by child window. Added
  comments about the right way to scale your UI (load a font at the right side, rebuild atlas, scale style).
- Scrollbar: Avoid overlapping the opposite side when window (often a child window) is forcibly too small.
- Combo: Hide arrow when there's not enough space even for the square button.
- InputText: Testing for newly added ImGuiKey_KeyPadEnter key. (#2677, #2005) [@amc522]
- TabBar: Fixed unfocused tab bar separator color (was using ImGuiCol_Tab, should use ImGuiCol_TabUnfocusedActive).
- Columns: Fixed a regression from 1.71 where the right-side of the contents rectangle within each column
  would wrongly use a WindowPadding.x instead of ItemSpacing.x like it always did. (#125, #2666)
- Columns: Made the right-most edge reaches up to the clipping rectangle (removing half of WindowPadding.x
  worth of asymmetrical/extraneous padding, note that there's another half that conservatively has to offset
  the right-most column, otherwise it's clipping width won't match the other columns). (#125, #2666)
- Columns: Improved honoring alignment with various values of ItemSpacing.x and WindowPadding.x. (#125, #2666)
- Columns: Made GetColumnOffset() and GetColumnWidth() behave when there's no column set, consistently with
  other column functions. (#2683)
- InputTextMultiline: Fixed vertical scrolling tracking glitch.
- Word-wrapping: Fixed overzealous word-wrapping when glyph edge lands exactly on the limit. Because
  of this, auto-fitting exactly unwrapped text would make it wrap. (fixes initial 1.15 commit, 78645a7d).
- Style: Attenuated default opacity of ImGuiCol_Separator in Classic and Light styles.
- Style: Added style.ColorButtonPosition (left/right, defaults to ImGuiDir_Right) to move the color button
  of ColorEdit3/ColorEdit4 functions to either side of the inputs.
- IO: Added ImGuiKey_KeyPadEnter and support in various back-ends (previously back-ends would need to
  specifically redirect key-pad keys to their regular counterpart). This is a temporary attenuating measure
  until we actually refactor and add whole sets of keys into the ImGuiKey enum. (#2677, #2005) [@amc522]
- Misc: Made Button(), ColorButton() not trigger an "edited" event leading to IsItemDeactivatedAfterEdit()
  returning true. This also effectively make ColorEdit4() not incorrect trigger IsItemDeactivatedAfterEdit()
  when clicking the color button to open the picker popup. (#1875)
- Misc: Added IMGUI_DISABLE_METRICS_WINDOW imconfig.h setting to explicitly compile out ShowMetricsWindow().
- Debug, Metrics: Added "Tools->Item Picker" tool which allow clicking on a widget to break in the debugger
  within the item code. The tool calls IM_DEBUG_BREAK() which can be redefined in imconfig.h if needed.
- ImDrawList: Fixed CloneOutput() helper crashing. (#1860) [@gviot]
- ImDrawList::ChannelsSplit(), ImDrawListSplitter: Fixed an issue with merging draw commands between
  channel 0 and 1. (#2624)
- ImDrawListSplitter: Fixed memory leak when using low-level split api (was not affecting ImDrawList api,
  also this type was added in 1.71 and not advertised as a public-facing feature).
- Fonts: binary_to_compressed_c.cpp: Display an error message if failing to open/read the input font file.
- Demo: Log, Console: Using a simpler stateless pattern for auto-scrolling.
- Demo: Widgets: Showing how to use the format parameter of Slider/Drag functions to display the name
  of an enum value instead of the underlying integer value.
- Demo: Renamed the "Help" menu to "Tools" (more accurate).
- Backends: DX10/DX11: Backup, clear and restore Geometry Shader is any is bound when calling renderer.
- Backends: DX11: Clear Hull Shader, Domain Shader, Compute Shader before rendering. Not backing/restoring them.
- Backends: OSX: Disabled default native Mac clipboard copy/paste implementation in core library (added in 1.71),
  because it needs application to be linked with '-framework ApplicationServices'. It can be explicitly
  enabled back by using '#define IMGUI_ENABLE_OSX_DEFAULT_CLIPBOARD_FUNCTIONS' in imconfig.h. Re-added
  equivalent using NSPasteboard api in the imgui_impl_osx.mm experimental back-end. (#2546)
- Backends: SDL2: Added dummy ImGui_ImplSDL2_InitForD3D() function to make D3D support more visible.
  (#2482, #2632) [@josiahmanson]
- Examples: Added SDL2+DirectX11 example application. (#2632, #2612, #2482) [@vincenthamm]


-----------------------------------------------------------------------
 VERSION 1.71 (Released 2019-06-12)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.71

Breaking Changes:
- IO: changed AddInputCharacter(unsigned short c) signature to AddInputCharacter(unsigned int c).
- Renamed SetNextTreeNodeOpen() to SetNextItemOpen(). Kept inline redirection function (will obsolete).
- Window: rendering of child windows outer decorations (e.g. bg color, border, scrollbars) is now
  performed as part of their parent window, avoiding the creation of an extraneous draw commands.
  If you have overlapping child windows with decorations, and relied on their relative z-order to be
  mapped to submission their order, this will affect your rendering. The optimization is disabled
  if the parent window has no visual output because it appears to be the most common situation leading
  to the creation of overlapping child windows. Please reach out if you are affected by this change!

Other Changes:
- Window: clarified behavior of SetNextWindowContentSize(). Content size is defined as the size available
  after removal of WindowPadding on each sides. So SetNextWindowContentSize(ImVec2(100,100)) + auto-resize
  will always allow submitting a 100x100 item without creating a scrollbar, regarding of WindowPadding.
  The exact meaning of ContentSize for decorated windows was previously ill-defined.
- Window: Fixed auto-resize with AlwaysVerticalScrollbar or AlwaysHorizontalScrollbar flags.
- Window: Fixed one case where auto-resize by double-clicking the resize grip would make either scrollbar
  appear for a single frame after the resize.
- Separator: Revert 1.70 "Declare its thickness (1.0f) to the layout" change. It's not incorrect
  but it breaks existing some layout patterns. Will return back to it when we expose Separator flags.
- Fixed InputScalar, InputScalarN, SliderScalarN, DragScalarN with non-visible label from inserting
  style.ItemInnerSpacing.x worth of trailing spacing.
- Fixed InputFloatX, SliderFloatX, DragFloatX functions erroneously reporting IsItemEdited() multiple
  times when the text input doesn't match the formatted output value (e.g. input "1" shows "1.000").
  It wasn't much of a problem because we typically use the return value instead of IsItemEdited() here.
- Fixed uses of IsItemDeactivated(), IsItemDeactivatedAfterEdit() on multi-components widgets and
  after EndGroup(). (#2550, #1875)
- Fixed crash when appending with BeginMainMenuBar() more than once and no other window are showing. (#2567)
- ColorEdit: Fixed the color picker popup only displaying inputs as HSV instead of showing multiple
  options. (#2587, broken in 1.69 by #2384).
- CollapsingHeader: Better clipping when a close button is enabled and it overlaps the label. (#600)
- Scrollbar: Minor bounding box adjustment to cope with various border size.
- Scrollbar, Style: Changed default style.ScrollbarSize from 16 to 14.
- Combo: Fixed rounding not applying with the ImGuiComboFlags_NoArrowButton flag. (#2607) [@DucaRii]
- Nav: Fixed gamepad/keyboard moving of window affecting contents size incorrectly, sometimes leading
  to scrollbars appearing during the movement.
- Nav: Fixed rare crash when e.g. releasing Alt-key while focusing a window with a menu at the same
  frame as clearing the focus. This was in most noticeable in back-ends such as Glfw and SDL which
  emits key release events when focusing another viewport, leading to Alt+clicking on void on another
  viewport triggering the issue. (#2609)
- TreeNode, CollapsingHeader: Fixed highlight frame not covering horizontal area fully when using
  horizontal scrolling. (#2211, #2579)
- TabBar: Fixed BeginTabBar() within a window with horizontal scrolling from creating a feedback
  loop with the horizontal contents size.
- Columns: Fixed Columns() within a window with horizontal scrolling from not covering the full
  horizontal area (previously only worked with an explicit contents size). (#125)
- Columns: Fixed Separator from creating an extraneous draw command. (#125)
- Columns: Fixed Selectable with SpanAllColumns flag from creating an extraneous draw command. (#125)
- Style: Added style.WindowMenuButtonPosition (left/right, defaults to ImGuiDir_Left) to move the
  collapsing/docking button to the other side of the title bar.
- Style: Made window close button cross slightly smaller.
- Log/Capture: Fixed BeginTabItem() label not being included in a text log/capture.
- ImDrawList: Added ImDrawCmd::VtxOffset value to support large meshes (64k+ vertices) using 16-bit indices.
  The renderer back-end needs to set 'io.BackendFlags |= ImGuiBackendFlags_RendererHasVtxOffset' to enable
  this, and honor the ImDrawCmd::VtxOffset field. Otherwise the value will always be zero.
  This has the advantage of preserving smaller index buffers and allowing to execute on hardware that do not
  support 32-bit indices. Most examples back-ends have been modified to support the VtxOffset field.
- ImDrawList: Added ImDrawCmd::IdxOffset value, equivalent to summing element count for each draw command.
  This is provided for convenience and consistency with VtxOffset.
- ImDrawCallback: Allow to override the signature of ImDrawCallback by #define-ing it. This is meant to
  facilitate custom rendering back-ends passing local render-specific data to the draw callback.
- ImFontAtlas: FreeType: Added RasterizerFlags::Monochrome flag to disable font anti-aliasing. Combine
  with RasterizerFlags::MonoHinting for best results. (#2545) [@HolyBlackCat]
- ImFontGlyphRangesBuilder: Fixed unnecessarily over-sized buffer, which incidentally was also not
  fully cleared. Fixed edge-case overflow when adding character 0xFFFF. (#2568). [@NIKE3500]
- Demo: Added full "Dear ImGui" prefix to the title of "Dear ImGui Demo" and "Dear ImGui Metrics" windows.
- Backends: Add native Mac clipboard copy/paste default implementation in core library to match what we are
  dealing with Win32, and to facilitate integration in custom engines. (#2546) [@andrewwillmott]
- Backends: OSX: imgui_impl_osx: Added mouse cursor support. (#2585, #1873) [@actboy168]
- Examples/Backends: DirectX9/10/11/12, Metal, Vulkan, OpenGL3 (Desktop GL only): Added support for large meshes
  (64k+ vertices) with 16-bit indices, enable 'ImGuiBackendFlags_RendererHasVtxOffset' in those back-ends.
- Examples/Backends: Don't filter characters under 0x10000 before calling io.AddInputCharacter(),
  the filtering is done in io.AddInputCharacter() itself. This is in prevision for fuller Unicode
  support. (#2538, #2541)


-----------------------------------------------------------------------
 VERSION 1.70 (Released 2019-05-06)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.70

Breaking Changes:
- ImDrawList: Improved algorithm for mitre joints on thick lines, preserving correct thickness
  up to 90 degrees angles (e.g. rectangles). If you have custom rendering using thick lines,
  they will appear a little thicker now. (#2518) [@rmitton]
- Obsoleted GetContentRegionAvailWidth(), use GetContentRegionAvail().x instead.
  Kept inline redirection function.
- Examples: Vulkan: Added MinImageCount/ImageCount fields in ImGui_ImplVulkan_InitInfo, required
  during initialization to specify the number of in-flight image requested by swap chains.
  (was previously a hard #define IMGUI_VK_QUEUED_FRAMES 2). (#2071, #1677) [@nathanvoglsam]
- Examples: Vulkan: Tidying up the demo/internals helpers (most engine/app should not rely
  on them but it is possible you have!).

Other Changes:
- ImDrawList: Added ImDrawCallback_ResetRenderState, a special ImDrawList::AddCallback() value
  to request the renderer back-end to reset its render state. (#2037, #1639, #2452)
  Examples: Added support for ImDrawCallback_ResetRenderState in all renderer back-ends. Each
  renderer code setting up initial render state has been moved to a function so it could be
  called at the start of rendering and when a ResetRenderState is requested. [@ocornut, @bear24rw]
- InputText: Fixed selection background rendering one frame after the cursor movement when
  first transitioning from no-selection to has-selection. (Bug in 1.69) (#2436) [@Nazg-Gul]
- InputText: Work-around for buggy standard libraries where isprint('\t') returns true. (#2467, #1336)
- InputText: Fixed ImGuiInputTextFlags_AllowTabInput leading to two tabs characters being inserted
  if the back-end provided both Key and Character input. (#2467, #1336)
- Layout: Added SetNextItemWidth() helper to avoid using PushItemWidth/PopItemWidth() for single items.
  Note that SetNextItemWidth() currently only affect the same subset of items as PushItemWidth(),
  generally referred to as the large framed+labeled items. Because the new SetNextItemWidth()
  function is explicit we may later extend its effect to more items.
- Layout: Fixed PushItemWidth(-width) for right-side alignment laying out some items (button, listbox, etc.)
  with negative sizes if the 'width' argument was smaller than the available width at the time of item
  submission.
- Window: Fixed window with the AlwaysAutoResize flag unnecessarily extending their hovering boundaries
  by a few pixels (this is used to facilitate resizing from borders when available for a given window).
  One of the noticeable minor side effect was that navigating menus would have had a tendency to disable
  highlight from parent menu items earlier than necessary while approaching the child menu.
- Window: Close button is horizontally aligned with style.FramePadding.x.
- Window: Fixed contents region being off by WindowBorderSize amount on the right when scrollbar is active.
- Window: Fixed SetNextWindowSizeConstraints() with non-rounded positions making windows drift. (#2067, #2530)
- Popups: Closing a popup restores the focused/nav window in place at the time of the popup opening,
  instead of restoring the window that was in the window stack at the time of the OpenPopup call. (#2517)
  Among other things, this allows opening a popup while no window are focused, and pressing Escape to
  clear the focus again.
- Popups: Fixed right-click from closing all popups instead of aiming at the hovered popup level
  (regression in 1.67).
- Selectable: With ImGuiSelectableFlags_AllowDoubleClick doesn't return true on the mouse button release
  following the double-click. Only first mouse release + second mouse down (double-click) returns true.
  Likewise for internal ButtonBehavior() with both _PressedOnClickRelease | _PressedOnDoubleClick. (#2503)
- GetMouseDragDelta(): also returns the delta on the mouse button released frame. (#2419)
- GetMouseDragDelta(): verify that mouse positions are valid otherwise returns zero.
- Inputs: Also add support for horizontal scroll with Shift+Mouse Wheel. (#2424, #1463) [@LucaRood]
- PlotLines, PlotHistogram: Ignore NaN values when calculating min/max bounds. (#2485)
- Columns: Fixed boundary of clipping being off by 1 pixel within the left column. (#125)
- Separator: Declare its thickness (1.0f) to the layout, making items around separator more symmetrical.
- Combo, Slider, Scrollbar: Improve rendering in situation when there's only a few pixels available (<3 pixels).
- Nav: Fixed Drag/Slider functions going into text input mode when keyboard CTRL is held while pressing NavActivate.
- Drag and Drop: Fixed drag source with ImGuiDragDropFlags_SourceAllowNullID and null ID from receiving click
  regardless of being covered by another window (it didn't honor correct hovering rules). (#2521)
- ImDrawList: Improved algorithm for mitre joints on thick lines, preserving correct thickness up to 90 degrees
  angles, also faster to output. (#2518) [@rmitton]
- Misc: Added IM_MALLOC/IM_FREE macros mimicking IM_NEW/IM_DELETE so user doesn't need to revert
  to using the ImGui::MemAlloc()/MemFree() calls directly.
- Misc: Made IMGUI_CHECKVERSION() macro also check for matching size of ImDrawIdx.
- Metrics: Added "Show windows rectangles" tool to visualize the different rectangles.
- Demo: Improved trees in columns demo.
- Examples: OpenGL: Added a dummy GL call + comments in ImGui_ImplOpenGL3_Init() to detect uninitialized
  GL function loaders early, and help users understand what they are missing. (#2421)
- Examples: SDL: Added support for SDL_GameController gamepads (enable with ImGuiConfigFlags_NavEnableGamepad). (#2509) [@DJLink]
- Examples: Emscripten: Added Emscripten+SDL+GLES2 example. (#2494, #2492, #2351, #336) [@nicolasnoble, @redblobgames]
- Examples: Metal: Added Glfw+Metal example. (#2527) [@bear24rw]
- Examples: OpenGL3: Minor tweaks + not calling glBindBuffer more than necessary in the render loop.
- Examples: Vulkan: Fixed in-flight buffers issues when using multi-viewports. (#2461, #2348, #2378, #2097)
- Examples: Vulkan: Added missing support for 32-bit indices (#define ImDrawIdx unsigned int).
- Examples: Vulkan: Avoid passing negative coordinates to vkCmdSetScissor, which debug validation layers do not like.
- Examples: Vulkan: Added ImGui_ImplVulkan_SetMinImageCount() to change min image count at runtime. (#2071) [@nathanvoglsam]
- Examples: DirectX9: Fixed erroneous assert in ImGui_ImplDX9_InvalidateDeviceObjects(). (#2454)
- Examples: DirectX10/11/12, Allegro, Marmalade: Render functions early out when display size is zero (minimized). (#2496)
- Examples: GLUT: Fixed existing FreeGLUT example to work with regular GLUT. (#2465) [@andrewwillmott]
- Examples: GLUT: Renamed imgui_impl_freeglut.cpp/.h to imgui_impl_glut.cpp/.h. (#2465) [@andrewwillmott]
- Examples: GLUT: Made io.DeltaTime always > 0. (#2430)
- Examples: Visual Studio: Updated default platform toolset+sdk in vcproj files from v100+sdk7 (vs2010)
  to v110+sdk8 (vs2012). This is mostly so we can remove reliance on DXSDK_DIR for the DX10/DX11 example,
  which if existing and when switching to recent SDK ends up conflicting and creating warnings.


-----------------------------------------------------------------------
 VERSION 1.69 (Released 2019-03-13)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.69

Breaking Changes:

- Renamed ColorEdit/ColorPicker's ImGuiColorEditFlags_RGB/_HSV/_HEX flags to respectively
  ImGuiColorEditFlags_DisplayRGB/_DisplayHSV/_DisplayHex. This is because the addition of
  new flag ImGuiColorEditFlags_InputHSV makes the earlier one ambiguous.
  Kept redirection enum values (will obsolete). (#2384) [@haldean]
- Renamed GetOverlayDrawList() to GetForegroundDrawList(). Kept redirection function (will obsolete). (#2391)

Other Changes:

- Added GetBackgroundDrawList() helper to quickly get access to a ImDrawList that will be rendered
  behind every other windows. (#2391, #545)
- DragScalar, InputScalar, SliderScalar: Added support for u8/s8/u16/s16 data types (ImGuiDataType_S8, etc.)
  We are reusing function instances of larger types to reduce code size. (#643, #320, #708, #1011)
- Added InputTextWithHint() to display a description/hint in the text box when no text
  has been entered. (#2400) [@Organic-Code, @ocornut]
- Nav: Fixed a tap on AltGR (e.g. German keyboard) from navigating to the menu layer.
- Nav: Fixed Ctrl+Tab keeping active InputText() of a previous window active after the switch. (#2380)
- Fixed IsItemDeactivated()/IsItemDeactivatedAfterEdit() from not correctly returning true
  when tabbing out of a focusable widget (Input/Slider/Drag) in most situations. (#2215, #1875)
- InputInt, InputFloat, InputScalar: Fix to keep the label of the +/- buttons centered when
  style.FramePadding.x is abnormally larger than style.FramePadding.y. Since the buttons are
  meant to be square (to align with e.g. color button) we always use FramePadding.y. (#2367)
- InputInt, InputScalar: +/- buttons now respects the natural type limits instead of
  overflowing or underflowing the value.
- InputText: Fixed an edge case crash that would happen if another widget sharing the same ID
  is being swapped with an InputText that has yet to be activated.
- InputText: Fixed various display corruption related to swapping the underlying buffer while
  a input widget is active (both for writable and read-only paths). Often they would manifest
  when manipulating the scrollbar of a multi-line input text.
- ColorEdit, ColorPicker, ColorButton: Added ImGuiColorEditFlags_InputHSV to manipulate color
  values encoded as HSV (in order to avoid HSV<>RGB round trips and associated singularities).
  (#2383, #2384) [@haldean]
- ColorPicker: Fixed a bug/assertion when displaying a color picker in a collapsed window
  while dragging its title bar. (#2389)
- ColorEdit: Fixed tooltip not honoring the ImGuiColorEditFlags_NoAlpha contract of never
  reading the 4th float in the array (value was read and discarded). (#2384) [@haldean]
- MenuItem, Selectable: Fixed disabled widget interfering with navigation (fix c2db7f63 in 1.67).
- TabBar: Fixed a crash when using many BeginTabBar() recursively (didn't affect docking). (#2371)
- TabBar: Added extra mis-usage error recovery. Past the assert, common mis-usage don't lead to
  hard crashes any more, facilitating integration with scripting languages. (#1651)
- TabBar: Fixed ImGuiTabItemFlags_SetSelected being ignored if the tab is not visible (with
  scrolling policy enabled) or if is currently appearing.
- TabBar: Fixed Tab tooltip code making drag and drop tooltip disappear during the frame where
  the drag payload activate a tab.
- TabBar: Reworked scrolling policy (when ImGuiTabBarFlags_FittingPolicyScroll is set) to
  teleport the view when aiming at a tab far away the visible section, and otherwise accelerate
  the scrolling speed to cap the scrolling time to 0.3 seconds.
- Text: Fixed large Text/TextUnformatted calls not feeding their size into layout when starting
  below the lower point of the current clipping rectangle. This bug has been there since v1.0!
  It was hardly noticeable but would affect the scrolling range, which in turn would affect
  some scrolling request functions when called during the appearing frame of a window.
- Plot: Fixed divide-by-zero in PlotLines() when passing a count of 1. (#2387) [@Lectem]
- Log/Capture: Fixed LogXXX functions emitting extraneous leading carriage return.
- Log/Capture: Fixed an issue when empty string on a new line would not emit a carriage return.
- Log/Capture: Fixed LogXXX functions 'auto_open_depth' parameter being treated as an absolute
  tree depth instead of a relative one.
- Log/Capture: Fixed CollapsingHeader trailing ascii representation being "#" instead of "##".
- ImFont: Added GetGlyphRangesVietnamese() helper. (#2403)
- Misc: Asserting in NewFrame() if style.WindowMinSize is zero or smaller than (1.0f,1.0f).
- Demo: Using GetBackgroundDrawList() and GetForegroundDrawList() in "Custom Rendering" demo.
- Demo: InputText: Demonstrating use of ImGuiInputTextFlags_CallbackResize. (#2006, #1443, #1008).
- Examples: GLFW, SDL: Preserve DisplayFramebufferScale when main viewport is minimized.
  (This is particularly useful for the viewport branch because we are not supporting per-viewport
  frame-buffer scale. It fixes windows not refreshing when main viewport is minimized.) (#2416)
- Examples: OpenGL: Fix to be able to run on ES 2.0 / WebGL 1.0. [@rmitton, @gabrielcuvillier]
- Examples: OpenGL: Fix for OSX not supporting OpenGL 4.5, we don't try to read GL_CLIP_ORIGIN
  even if the OpenGL headers/loader happens to define the value. (#2366, #2186)
- Examples: Allegro: Added support for touch events (emulating mouse). (#2219) [@dos1]
- Examples: DirectX9: Minor changes to match the other DirectX examples more closely. (#2394)


-----------------------------------------------------------------------
 VERSION 1.68 (Released 2019-02-19)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.68

Breaking Changes:

- Removed io.DisplayVisibleMin/DisplayVisibleMax (which were marked obsolete and removed from viewport/docking branch already).
- Made it illegal/assert when io.DisplayTime == 0.0f (with an exception for the first frame).
  If for some reason your time step calculation gives you a zero value, replace it with a dummy small value!

Other Changes:

- Added .editorconfig file for text editors to standardize using spaces. (#2038) [@kudaba]
- ImDrawData: Added FramebufferScale field (currently a copy of the value from io.DisplayFramebufferScale).
  This is to allow render functions being written without pulling any data from ImGuiIO, allowing incoming
  multi-viewport feature to behave on Retina display and with multiple displays.
  If you are not using a custom binding, please update your render function code ahead of time,
  and use draw_data->FramebufferScale instead of io.DisplayFramebufferScale. (#2306, #1676)
- Added IsItemActivated() as an extension to the IsItemDeactivated/IsItemDeactivatedAfterEdit functions
  which are useful to implement variety of undo patterns. (#820, #956, #1875)
- InputText: Fixed a bug where ESCAPE would not restore the initial value in all situations. (#2321) [@relick]
- InputText: Fixed a bug where ESCAPE would be first captured by the Keyboard Navigation code. (#2321, #787)
- InputText: Fixed redo buffer exhaustion handling (rare) which could corrupt the undo character buffer. (#2333)
  The way the redo/undo buffers work would have made it generally unnoticeable to the user.
- Fixed range-version of PushID() and GetID() not honoring the ### operator to restart from the seed value.
- Fixed CloseCurrentPopup() on a child-menu of a modal incorrectly closing the modal. (#2308)
- Tabs: Added ImGuiTabBarFlags_TabListPopupButton flag to show a popup button on manual tab bars. (#261, #351)
- Tabs: Removed ImGuiTabBarFlags_NoTabListPopupButton which was available in 1.67 but actually had zero use.
- Tabs: Fixed a minor clipping glitch when changing style's FramePadding from frame to frame.
- Tabs: Fixed border (when enabled) so it is aligned correctly mid-pixel and appears as bright as other borders.
- Style, Selectable: Added ImGuiStyle::SelectableTextAlign and ImGuiStyleVar_SelectableTextAlign. (#2347) [@haldean]
- Menus: Tweaked horizontal overlap between parent and child menu (to help convey relative depth)
  from using style.ItemSpacing.x to style.ItemInnerSpacing.x, the later being expected to be smaller. (#1086)
- RadioButton: Fixed label horizontal alignment to precisely match Checkbox().
- Window: When resizing from an edge, the border is more visible and better follow the rounded corners.
- Window: Fixed initial width of collapsed windows not taking account of contents width (broken in 1.67). (#2336, #176)
- Scrollbar: Fade out and disable interaction when too small, in order to facilitate using the resize grab on very
  small window, as well as reducing visual noise/overlap.
- ListBox: Better optimized when clipped / non-visible.
- InputTextMultiline: Better optimized when clipped / non-visible.
- Font: Fixed high-level ImGui::CalcTextSize() used by most widgets from erroneously subtracting 1.0f*scale to
  calculated text width. Among noticeable side-effects, it would make sequences of repeated Text/SameLine calls
  not align the same as a single call, and create mismatch between high-level size calculation and those performed
  with the lower-level ImDrawList api. (#792) [@SlNPacifist]
- Font: Fixed building atlas when specifying duplicate/overlapping ranges within a same font. (#2353, #2233)
- ImDrawList: Fixed AddCircle(), AddCircleFilled() angle step being off, which was visible when drawing a "circle"
  with a small number of segments (e.g. an hexagon). (#2287) [@baktery]
- ImGuiTextBuffer: Added append() function (unformatted).
- ImFontAtlas: Added 0x2000-0x206F general punctuation range to default ChineseFull/ChineseSimplifiedCommon ranges. (#2093)
- ImFontAtlas: FreeType: Added support for imgui allocators + custom FreeType only SetAllocatorFunctions. (#2285) [@Vuhdo]
- ImFontAtlas: FreeType: Fixed using imgui_freetype.cpp in unity builds. (#2302)
- Demo: Fixed "Log" demo not initializing properly, leading to the first line not showing before a Clear. (#2318) [@bluescan]
- Demo: Added "Auto-scroll" option in Log/Console demos. (#2300) [@nicolasnoble, @ocornut]
- Examples: Metal, OpenGL2, OpenGL3, Vulkan: Fixed offsetting of clipping rectangle with ImDrawData::DisplayPos != (0,0)
  when the display frame-buffer scale scale is not (1,1). While this doesn't make a difference when using master branch,
  this is effectively fixing support for multi-viewport with Mac Retina Displays on those examples. (#2306) [@rasky, @ocornut]
  Also using ImDrawData::FramebufferScale instead of io.DisplayFramebufferScale.
- Examples: Clarified the use the ImDrawData::DisplayPos to offset clipping rectangles.
- Examples: Win32: Using GetForegroundWindow()+IsChild() instead of GetActiveWindow() to be compatible with windows created
  in a different thread or parent. (#1951, #2087, #2156, #2232) [many people]
- Examples: SDL: Using the SDL_WINDOW_ALLOW_HIGHDPI flag. (#2306, #1676) [@rasky]
- Examples: Win32: Added support for XInput gamepads (if ImGuiConfigFlags_NavEnableGamepad is enabled).
- Examples: Win32: Added support for mouse buttons 4 and 5 via WM_XBUTTON* messages. (#2264)
- Examples: DirectX9: Explicitly disable fog (D3DRS_FOGENABLE) before drawing in case user state has it set. (#2288, #2230)
- Examples: OpenGL2: Added #define GL_SILENCE_DEPRECATION to cope with newer XCode warnings.
- Examples: OpenGL3: Using GLSL 4.10 shaders for any GLSL version over 410 (e.g. 430, 450). (#2329) [@BrutPitt]


-----------------------------------------------------------------------
 VERSION 1.67 (Released 2019-01-14)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.67

Breaking Changes:

- Made it illegal to call Begin("") with an empty string. This somehow half-worked before but had various undesirable
  side-effect because the window would have ID zero. In particular it is causing problems in viewport/docking branches.
- Renamed io.ConfigResizeWindowsFromEdges to io.ConfigWindowsResizeFromEdges and removed its [Beta] mark.
  The addition of new configuration options in the Docking branch is pushing for a little reorganization of those names.
- Renamed ImFontAtlas::GlyphRangesBuilder to ImFontGlyphRangesBuilder. Kept redirection typedef (will obsolete).

Other Changes:
- Added BETA api for Tab Bar/Tabs widgets: (#261, #351)
  - Added BeginTabBar(), EndTabBar(), BeginTabItem(), EndTabItem(), SetTabItemClosed() API.
  - Added ImGuiTabBarFlags flags for BeginTabBar().
  - Added ImGuiTabItemFlags flags for BeginTabItem().
  - Style: Added ImGuiCol_Tab, ImGuiCol_TabHovered, ImGuiCol_TabActive, ImGuiCol_TabUnfocused, ImGuiCol_TabUnfocusedActive colors.
  - Demo: Added Layout->Tabs demo code.
  - Demo: Added "Documents" example app showcasing possible use for tabs.
  This feature was merged from the Docking branch in order to allow the use of regular tabs in your code.
  (It does not provide the docking/splitting/merging of windows available in the Docking branch)
- Added ImGuiWindowFlags_UnsavedDocument window flag to append '*' to title without altering the ID, as a convenience
  to avoid using the ### operator. In the Docking branch this also has an effect on tab closing behavior.
- Window, Focus, Popup: Fixed an issue where closing a popup by clicking another window with the _NoMove flag would refocus
  the parent window of the popup instead of the newly clicked window.
- Window: Contents size is preserved while a window collapsed. Fix auto-resizing window losing their size for one frame when uncollapsed.
- Window: Contents size is preserved while a window contents is hidden (unless it is hidden for resizing purpose).
- Window: Resizing windows from edge is now enabled by default (io.ConfigWindowsResizeFromEdges=true). Note that
  it only works _if_ the back-end sets ImGuiBackendFlags_HasMouseCursors, which the standard back-ends do.
- Window: Added io.ConfigWindowsMoveFromTitleBarOnly option. This is ignored by window with no title bars (often popups).
  This affects clamping window within the visible area: with this option enabled title bars need to be visible. (#899)
- Window: Fixed using SetNextWindowPos() on a child window (which wasn't really documented) position the cursor as expected
  in the parent window, so there is no mismatch between the layout in parent and the position of the child window.
- InputFloat: When using ImGuiInputTextFlags_ReadOnly the step buttons are disabled. (#2257)
- DragFloat: Fixed broken mouse direction change with power!=1.0. (#2174, #2206) [@Joshhua5]
- Nav: Fixed an keyboard issue where holding Activate/Space for longer than two frames on a button would unnecessary
  keep the focus on the parent window, which could steal it from newly appearing windows. (#787)
- Nav: Fixed animated window titles from being updated when displayed in the CTRL+Tab list. (#787)
- Error recovery: Extraneous/undesired calls to End() are now being caught by an assert in the End() function closer
  to the user call site (instead of being reported in EndFrame). Past the assert, they don't lead to crashes any more. (#1651)
  Missing calls to End(), past the assert, should not lead to crashes or to the fallback Debug window appearing on screen.
  Those changes makes it easier to integrate dear imgui with a scripting language allowing, given asserts are redirected
  into e.g. an error log and stopping the script execution.
- ImFontAtlas: Stb and FreeType: Atlas width is now properly based on total surface rather than glyph count (unless overridden with TexDesiredWidth).
- ImFontAtlas: Stb and FreeType: Fixed atlas builder so missing glyphs won't influence the atlas texture width. (#2233)
- ImFontAtlas: Stb and FreeType: Fixed atlas builder so duplicate glyphs (when merging fonts) won't be included in the rasterized atlas.
- ImFontAtlas: FreeType: Fixed abnormally high atlas height.
- ImFontAtlas: FreeType: Fixed support for any values of TexGlyphPadding (not just only 1).
- ImDrawList: Optimized some of the functions for performance of debug builds where non-inline function call cost are non-negligible.
  (Our test UI scene on VS2015 Debug Win64 with /RTC1 went ~5.9 ms -> ~4.9 ms. In Release same scene stays at ~0.3 ms.)
- IO: Added BackendPlatformUserData, BackendRendererUserData, BackendLanguageUserData void* for storage use by back-ends.
- IO: Renamed InputCharacters[], marked internal as was always intended. Please don't access directly, and use AddInputCharacter() instead!
- IO: AddInputCharacter() goes into a queue which can receive as many characters as needed during the frame. This is useful
  for automation to not have an upper limit on typing speed. Will later transition key/mouse to use the event queue later.
- Style: Tweaked default value of style.DisplayWindowPadding from (20,20) to (19,19) so the default style as a value
  which is the same as the title bar height.
- Demo: "Simple Layout" and "Style Editor" are now using tabs.
- Demo: Added a few more things under "Child windows" (changing ImGuiCol_ChildBg, positioning child, using IsItemHovered after a child).
- Examples: DirectX10/11/12: Made imgui_impl_dx10/dx11/dx12.cpp link d3dcompiler.lib from the .cpp file to ease integration.
- Examples: Allegro 5: Properly destroy globals on shutdown to allow for restart. (#2262) [@DomRe]


-----------------------------------------------------------------------
 VERSION 1.66b (Released 2018-12-01)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.66b

Other Changes:

- Fixed a text rendering/clipping bug introduced in 1.66 (on 2018-10-12, commit ede3a3b9) that affect single ImDrawList::AddText()
  calls with single strings larger than 10k. Text/TextUnformatted() calls were not affected, but e.g. InputText() was. [@pdoane]
- When the focused window become inactive don't restore focus to a window with the ImGuiWindowFlags_NoInputs flag. (#2213) [@zzzyap]
- Separator: Fixed Separator() outputting an extraneous empty line when captured into clipboard/text/file.
- Demo: Added ShowAboutWindow() call, previously was only accessible from the demo window.
- Demo: ShowAboutWindow() now display various Build/Config Information (compiler, os, etc.) that can easily be copied into bug reports.
- Fixed build issue with osxcross and macOS. (#2218) [@dos1]
- Examples: Setting up 'io.BackendPlatformName'/'io.BackendRendererName' fields to the current back-end can be displayed in the About window.
- Examples: SDL: changed the signature of ImGui_ImplSDL2_ProcessEvent() to use a const SDL_Event*. (#2187)


-----------------------------------------------------------------------
 VERSION 1.66 (Released 2018-11-22)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.66

Breaking Changes:

- Renamed SetScrollHere() to SetScrollHereY(). Kept redirection function (will obsolete).
- Renamed misc/stl/imgui_stl.* to misc/cpp/imgui_stdlib.* in prevision for other C++ helper files. (#2035, #2096)

Other Changes:

- Fixed calling SetNextWindowSize()/SetWindowSize() with non-integer values leading to
  accidental alteration of window position. We now round the provided size. (#2067)
- Fixed calling DestroyContext() always saving .ini data with the current context instead
  of the supplied context pointer. (#2066)
- Nav, Focus: Fixed ImGuiWindowFlags_NoBringToFrontOnFocus windows not being restoring focus
  properly after the main menu bar or last focused window is deactivated.
- Nav: Fixed an assert in certain circumstance (mostly when using popups) when mouse positions stop being valid. (#2168)
- Nav: Fixed explicit directional input not re-highlighting current nav item if there is a single item in the window
  and highlight has been previously disabled by the mouse. (#787)
- DragFloat: Fixed a situation where dragging with value rounding enabled or with a power curve
  erroneously wrapped the value to one of the min/max edge. (#2024, #708, #320, #2075).
- DragFloat: Disabled using power curve when one edge is FLT_MAX (broken in 1.61). (#2024)
- DragFloat: Disabled setting a default drag speed when one edge is FLT_MAX. (#2024)
- SliderAngle: Added optional format argument to alter precision or localize the string. (#2150) [@podsvirov]
- Window: Resizing from edges (with io.ConfigResizeWindowsFromEdges Beta flag) extends the hit region
  of root floating windows outside the window, making it easier to resize windows. Resize grips are also
  extended accordingly so there are no discontinuity when hovering between borders and corners. (#1495, #822)
- Window: Added ImGuiWindowFlags_NoBackground flag to avoid rendering window background. This is mostly to allow
  the creation of new flag combinations, as we could already use SetNextWindowBgAlpha(0.0f). (#1660) [@biojppm, @ocornut]
- Window: Added ImGuiWindowFlags_NoDecoration helper flag which is essentially NoTitleBar+NoResize+NoScrollbar+NoCollapse.
- Window: Added ImGuiWindowFlags_NoMouseInputs which is basically the old ImGuiWindowFlags_NoInputs (essentially
  we have renamed ImGuiWindowFlags_NoInputs to ImGuiWindowFlags_NoMouseInputs). Made the new ImGuiWindowFlags_NoInputs
  encompass both NoMouseInputs+NoNav, which is consistent with its description. (#1660, #787)
- Window, Inputs: Fixed resizing from edges when io.MousePos is not pixel-rounded by rounding mouse position input. (#2110)
- BeginChild(): Fixed BeginChild(const char*, ...) variation erroneously not applying the ID stack
  to the provided string to uniquely identify the child window. This was undoing an intentional change
  introduced in 1.50 and broken in 1.60. (#1698, #894, #713).
- TextUnformatted(): Fixed a case where large-text path would read bytes past the text_end marker depending
  on the position of new lines in the buffer (it wasn't affecting the output but still not the right thing to do!)
- ListBox(): Fixed frame sizing when items_count==1 unnecessarily showing a scrollbar. (#2173) [@luk1337, @ocornut]
- ListBox(): Tweaked frame sizing so list boxes will look more consistent when FramePadding is far from ItemSpacing.
- RenderText(): Some optimization for very large text buffers, useful for non-optimized builds.
- BeginMenu(): Fixed menu popup horizontal offset being off the item in the menu bar when WindowPadding=0.0f.
- ArrowButton(): Fixed arrow shape being horizontally misaligned by (FramePadding.y-FramePadding.x) if they are different.
- Demo: Split the contents of ShowDemoWindow() into smaller functions as it appears to speed up link time with VS. (#2152)
- Drag and Drop: Added GetDragDropPayload() to peek directly into the payload (if any) from anywhere. (#143)
- ImGuiTextBuffer: Avoid heap allocation when empty.
- ImDrawList: Fixed AddConvexPolyFilled() undefined behavior when passing points_count smaller than 3,
  in particular, points_count==0 could lead to a memory stomp if the draw list was previously empty.
- Examples: DirectX10, DirectX11: Removed seemingly unnecessary calls to invalidate and recreate device objects
  in the WM_SIZE handler. (#2088) [@ice1000]
- Examples: GLFW: User previously installed GLFW callbacks are now saved and chain-called by the default callbacks. (#1759)
- Examples: OpenGL3: Added support for GL 4.5's glClipControl(GL_UPPER_LEFT). (#2186)
- Examples: OpenGL3+GLFW: Fixed error condition when using the GLAD loader. (#2157) [@blackball]
- Examples: OpenGL3+GLFW/SDL: Made main.cpp compile with IMGUI_IMPL_OPENGL_LOADER_CUSTOM (may be missing init). (#2178) [@doug-moen]
- Examples: SDL2+Vulkan: Fixed application shutdown which could deadlock on Linux + Xorg. (#2181) [@eRabbit0]


-----------------------------------------------------------------------
 VERSION 1.65 (Released 2018-09-06)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.65

Breaking Changes:

- Renamed stb_truetype.h to imstb_truetype.h, stb_textedit.h to imstb_textedit.h, and
  stb_rect_pack.h to imstb_rectpack.h. If you were conveniently using the imgui copy of those
  STB headers in your project, you will have to update your include paths. (#1718, #2036)
  The reason for this change is to avoid conflicts for projects that may also be importing
  their own copy of the STB libraries. Note that imgui's copy of stb_textedit.h is modified.
- Renamed io.ConfigCursorBlink to io.ConfigInputTextCursorBlink. (#1427)

Other Changes:

- This is a minor release following the 1.64 refactor, with a little more shuffling of code.
- Clarified and improved the source code sectioning in all files (easier to search or browse sections).
- Nav: Removed the [Beta] tag from various descriptions of the gamepad/keyboard navigation system.
  Although it is not perfect and will keep being improved, it is fairly functional and used by many. (#787)
- Fixed a build issue with non-Cygwin GCC under Windows.
- Demo: Added a "Configuration" block to make io.ConfigFlags/io.BackendFlags more prominent.
- Examples: OpenGL3+SDL2: Fixed error condition when using the GLAD loader. (#2059, #2002) [@jiri]


-----------------------------------------------------------------------
 VERSION 1.64 (Released 2018-08-31)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.64

Changes:

- Moved README, CHANGELOG and TODO files to the docs/ folder.
  If you are updating dear imgui by copying files, take the chance to delete the old files.
- Added imgui_widgets.cpp file, extracted and moved widgets code out of imgui.cpp into imgui_widgets.cpp.
  Re-ordered some of the code remaining in imgui.cpp.
  NONE OF THE FUNCTIONS HAVE CHANGED. THE CODE IS SEMANTICALLY 100% IDENTICAL, BUT _EVERY_ FUNCTIONS HAS BEEN MOVED.
  Because of this, any local modifications to imgui.cpp will likely conflict when you update.
  If you have any modifications to imgui.cpp, it is suggested that you first update to 1.63, then
  isolate your patches. You can peak at imgui_widgets.cpp from 1.64 to get a sense of what is included in it,
  then separate your changes into several patches that can more easily be applied to 1.64 on a per-file basis.
  What I found worked nicely for me, was to open the diff of the old patches in an interactive merge/diff tool,
  search for the corresponding function in the new code and apply the chunks manually.
- As a reminder, if you have any change to imgui.cpp it is a good habit to discuss them on the github,
  so a solution applicable on the Master branch can be found. If your company has changes that you cannot
  disclose you may also contact me privately.


-----------------------------------------------------------------------
 VERSION 1.63 (Released 2018-08-29)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.63

Breaking Changes:

- Style: Renamed ImGuiCol_ModalWindowDarkening to ImGuiCol_ModalWindowDimBg for consistency with other features.
  Kept redirection enum (will obsolete).
- Changed ImGui::GetTime() return value from float to double to avoid accumulating floating point imprecision over time.
- Removed per-window ImGuiWindowFlags_ResizeFromAnySide Beta flag in favor `io.ConfigResizeWindowsFromEdges=true` to
  enable the feature globally. (#1495)
  The feature is not currently enabled by default because it is not satisfying enough, but will eventually be.
- InputText: Renamed ImGuiTextEditCallback to ImGuiInputTextCallback, ImGuiTextEditCallbackData to ImGuiInputTextCallbackData
  for consistency. Kept redirection types (will obsolete).
- InputText: Removed ImGuiTextEditCallbackData::ReadOnly because it is a duplication of (::Flags & ImGuiInputTextFlags_ReadOnly).
- Renamed IsItemDeactivatedAfterChange() to IsItemDeactivatedAfterEdit() for consistency with new IsItemEdited() API.
  Kept redirection function (will obsolete soonish as IsItemDeactivatedAfterChange() is very recent).
- Renamed io.OptCursorBlink to io.ConfigCursorBlink [-> io.ConfigInputTextCursorBlink in 1.65], io.OptMacOSXBehaviors to
  io.ConfigMacOSXBehaviors for consistency. (#1427, #473)
- Removed obsolete redirection functions: CollapsingHeader() variation with 2 bools - marked obsolete in v1.49, May 2016.

Other Changes:

- ArrowButton: Fixed to honor PushButtonRepeat() setting (and internals' ImGuiItemFlags_ButtonRepeat).
- ArrowButton: Setup current line text baseline so that ArrowButton() + SameLine() + Text() are aligned properly.
- Nav: Added a CTRL+TAB window list and changed the highlight system accordingly. The change is motivated by upcoming
  Docking features. (#787)
- Nav: Made CTRL+TAB skip menus + skip the current navigation window if is has the ImGuiWindow_NoNavFocus set. (#787)
  While it was previously possible, you won't be able to CTRL-TAB out and immediately back in a window with the
  ImGuiWindow_NoNavFocus flag.
- Window: Allow menu and popups windows from ignoring the style.WindowMinSize values so short menus/popups are not padded. (#1909)
- Window: Added global io.ConfigResizeWindowsFromEdges option to enable resizing windows from their edges and from
  the lower-left corner. (#1495)
- Window: Collapse button shows hovering highlight + clicking and dragging on it allows to drag the window as well.
- Added IsItemEdited() to query if the last item modified its value (or was pressed). This is equivalent to the bool
  returned by most widgets.
  It is useful in some situation e.g. using InputText() with ImGuiInputTextFlags_EnterReturnsTrue. (#2034)
- InputText: Added support for buffer size/capacity changes via the ImGuiInputTextFlags_CallbackResize flag. (#2006, #1443, #1008).
- InputText: Fixed not tracking the cursor horizontally when modifying the text buffer through a callback.
- InputText: Fixed minor off-by-one issue when submitting a buffer size smaller than the initial zero-terminated buffer contents.
- InputText: Fixed a few pathological crash cases on single-line InputText widget with multiple millions characters worth of contents.
  Because the current text drawing function reserve for a worst-case amount of vertices and how we handle horizontal clipping,
  we currently just avoid displaying those single-line widgets when they are over a threshold of 2 millions characters,
  until a better solution is found.
- Drag and Drop: Fixed an incorrect assert when dropping a source that is submitted after the target (bug introduced with 1.62 changes
  related to the addition of IsItemDeactivated()). (#1875, #143)
- Drag and Drop: Fixed ImGuiDragDropFlags_SourceNoDisableHover to affect hovering state prior to calling IsItemHovered() + fixed description. (#143)
- Drag and Drop: Calling BeginTooltip() between a BeginDragSource()/EndDragSource() or BeginDropTarget()/EndDropTarget() uses adjusted tooltip
  settings matching the one created when calling BeginDragSource() without the ImGuiDragDropFlags_SourceNoPreviewTooltip flag. (#143)
- Drag and Drop: Payload stays available and under the mouse if the source stops being submitted, however the tooltip is replaced by "...". (#1725)
- Drag and Drop: Added ImGuiDragDropFlags_SourceAutoExpirePayload flag to force payload to expire if the source stops being submitted. (#1725, #143).
- IsItemHovered(): Added ImGuiHoveredFlags_AllowWhenDisabled flag to query hovered status on disabled items. (#1940, #211)
- Selectable: Added ImGuiSelectableFlags_Disabled flag in the public API. (#211)
- ColorEdit4: Fixed a bug when text input or drag and drop leading to unsaturated HSV values would erroneously alter the resulting color. (#2050)
- Misc: Added optional misc/stl/imgui_stl.h wrapper to use with STL types (e.g. InputText with std::string). (#2006, #1443, #1008)
  [*EDIT* renamed to misc/std/imgui_stdlib.h in 1.66]
- Misc: Added IMGUI_VERSION_NUM for easy compile-time testing. (#2025)
- Misc: Added ImGuiMouseCursor_Hand cursor enum + corresponding software cursor. (#1913, 1914) [@aiekick, @ocornut]
- Misc: Tweaked software mouse cursor offset to match the offset of the corresponding Windows 10 cursors.
- Made assertion more clear when trying to call Begin() outside of the NewFrame()..EndFrame() scope. (#1987)
- Fixed assertion when transitioning from an active ID to another within a group, affecting ColorPicker (broken in 1.62). (#2023, #820, #956, #1875).
- Fixed PushID() from keeping alive the new ID Stack top value (if a previously active widget shared the ID it would be erroneously kept alive).
- Fixed horizontal mouse wheel not forwarding the request to the parent window if ImGuiWindowFlags_NoScrollWithMouse is set. (#1463, #1380, #1502)
- Fixed a include build issue for Cygwin in non-POSIX (Win32) mode. (#1917, #1319, #276)
- ImDrawList: Improved handling for worst-case vertices reservation policy when large amount of text (e.g. 1+ million character strings)
  are being submitted in a single call. It would typically have crashed InputTextMultiline(). (#200)
- OS/Windows: Fixed missing ImmReleaseContext() call in the default Win32 IME handler. (#1932) [@vby]
- Metrics: Changed io.MetricsActiveWindows to reflect the number of active windows (!= from visible windows), which is useful
  for lazy/idle render mechanisms as new windows are typically not visible for one frame.
- Metrics: Added io.MetricsRenderWindow to reflect the number of visible windows.
- Metrics: Added io.MetricsActiveAllocations, moving away from the cross-context global counters than we previously used. (#1565, #1599, #586)
- Demo: Added basic Drag and Drop demo. (#143)
- Demo: Modified the Console example to use InsertChars() in the input text callback instead of poking directly into the buffer.
  Although this won't make a difference in the example itself, using InsertChars() will honor the resizing callback properly. (#2006, #1443, #1008).
- Demo: Clarified the use of IsItemHovered()/IsItemActive() right after being in the "Active, Focused, Hovered & Focused Tests" section.
- Examples: Tweaked the main.cpp of each example.
- Examples: Metal: Added Metal rendering backend. (#1929, #1873) [@warrenm]
- Examples: OSX: Added early raw OSX platform backend. (#1873) [@pagghiu, @itamago, @ocornut]
- Examples: Added mac OSX & iOS + Metal example in example_apple_metal/. (#1929, #1873) [@warrenm]
- Examples: Added mac OSX + OpenGL2 example in example_apple_opengl2/. (#1873)
- Examples: OpenGL3: Added shaders more versions of GLSL. (#1938, #1941, #1900, #1513, #1466, etc.)
- Examples: OpenGL3: Tweaked the imgui_impl_opengl3.cpp to work as-is with Emscripten + WebGL 2.0. (#1941). [@o-micron]
- Examples: OpenGL3: Made the example app default to GL 3.0 + GLSL 130 (instead of GL 3.2 + GLSL 150) unless on Mac.
- Examples: OpenGL3: Added error output when shaders fail to compile/link.
- Examples: OpenGL3: Added support for glew and glad OpenGL loaders out of the box. (#2001, #2002) [@jdumas]
- Examples: OpenGL2: Disabling/restoring GL_LIGHTING and GL_COLOR_MATERIAL to increase compatibility with legacy OpenGL applications. (#1996)
- Examples: DirectX10, DirectX11: Fixed unreleased resources in Init and Shutdown functions. (#1944)
- Examples: DirectX11: Querying for IDXGIFactory instead of IDXGIFactory1 to increase compatibility. (#1989) [@matt77hias]
- Examples: Vulkan: Fixed handling of VkSurfaceCapabilitiesKHR::maxImageCount = 0 case. Tweaked present mode selections.
- Examples: Win32, Glfw, SDL: Added support for the ImGuiMouseCursor_Hand cursor.


-----------------------------------------------------------------------
 VERSION 1.62 (Released 2018-06-22)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.62

Breaking Changes:

- TreeNodeEx(): The helper ImGuiTreeNodeFlags_CollapsingHeader flag now include ImGuiTreeNodeFlags_NoTreePushOnOpen.
  The flag was already set by CollapsingHeader().
  The only difference is if you were using TreeNodeEx() manually with ImGuiTreeNodeFlags_CollapsingHeader and without
  ImGuiTreeNodeFlags_NoTreePushOnOpen. In this case you can remove the ImGuiTreeNodeFlags_NoTreePushOnOpen flag from
  your call (ImGuiTreeNodeFlags_CollapsingHeader & ~ImGuiTreeNodeFlags_NoTreePushOnOpen). (#1864)
  This also apply if you were using internal's TreeNodeBehavior() with the ImGuiTreeNodeFlags_CollapsingHeader flag directly.
- ImFontAtlas: Renamed GetGlyphRangesChinese() to GetGlyphRangesChineseFull() to distinguish new smaller variants and
  discourage using the full set. (#1859)

Other Changes:

- Examples back-ends have been refactored to separate the platform code (e.g. Win32, Glfw, SDL2) from the renderer code (e.g. DirectX11, OpenGL3, Vulkan).
  The "Platform" bindings are in charge of: mouse/keyboard/gamepad inputs, cursor shape, timing, etc.
  The "Renderer" bindings are in charge of: creating the main font texture, rendering imgui draw data.
      before: imgui_impl_dx11.cpp        --> after: imgui_impl_win32.cpp + imgui_impl_dx11.cpp
      before: imgui_impl_dx12.cpp        --> after: imgui_impl_win32.cpp + imgui_impl_dx12.cpp
      before: imgui_impl_glfw_gl3.cpp    --> after: imgui_impl_glfw.cpp + imgui_impl_opengl2.cpp
      before: imgui_impl_glfw_vulkan.cpp --> after: imgui_impl_glfw.cpp + imgui_impl_vulkan.cpp
      before: imgui_impl_sdl_gl3.cpp     --> after: imgui_impl_sdl2.cpp + imgui_impl_opengl2.cpp
      before: imgui_impl_sdl_gl3.cpp     --> after: imgui_impl_sdl2.cpp + imgui_impl_opengl3.cpp etc.
  - The idea is what we can now easily combine and maintain back-ends and reduce code redundancy. Individual files are
    smaller and more reusable. Integration of imgui into a new/custom engine may also be easier as there is less overlap
    between "windowing / inputs" and "rendering" code, so you may study or grab one half of the code and not the other.
  - This change was motivated by the fact that adding support for the upcoming multi-viewport feature requires more work
    from the Platform and Renderer back-ends, and the amount of redundancy across files was becoming too difficult to
    maintain. If you use default back-ends, you'll benefit from an easy update path to support multi-viewports later
    (for future ImGui 1.7x).
  - This is not strictly a breaking change if you keep your old bindings, but when you'll want to fully update your bindings,
    expect to have to reshuffle a few things.
  - Each example still has its own main.cpp which you may refer you to understand how to initialize and glue everything together.
  - Some frameworks (such as the Allegro, Marmalade) handle both the "platform" and "rendering" part, and your custom engine may as well.
  - Read examples/README.txt for details.
- Added IsItemDeactivated() to query if the last item was active previously and isn't anymore. Useful for Undo/Redo patterns. (#820, #956, #1875)
- Added IsItemDeactivatedAfterChange() [*EDIT* renamed to IsItemDeactivatedAfterEdit() in 1.63] if the last item was active previously,
  is not anymore, and during its active state modified a value. Note that you may still get false positive (e.g. drag value and while
  holding return on the same value). (#820, #956, #1875)
- Nav: Added support for PageUp/PageDown (explorer-style: first aim at bottom/top most item, when scroll a page worth of contents). (#787)
- Nav: To keep the navigated item in view we also attempt to scroll the parent window as well as the current window. (#787)
- ColorEdit3, ColorEdit4, ColorButton: Added ImGuiColorEditFlags_NoDragDrop flag to disable ColorEditX as drag target and ColorButton as drag source. (#1826)
- BeginDragDropSource(): Offset tooltip position so it is off the mouse cursor, but also closer to it than regular tooltips,
  and not clamped by viewport. (#1739)
- BeginDragDropTarget(): Added ImGuiDragDropFlags_AcceptNoPreviewTooltip flag to request hiding the drag source tooltip
  from the target site. (#143)
- BeginCombo(), BeginMainMenuBar(), BeginChildFrame(): Temporary style modification are restored at the end of BeginXXX
  instead of EndXXX, to not affect tooltips and child windows.
- Popup: Improved handling of (erroneously) repeating calls to OpenPopup() to not close the popup's child popups. (#1497, #1533, #1865).
- InputTextMultiline(): Fixed double navigation highlight when scrollbar is active. (#787)
- InputText(): Fixed Undo corruption after pasting large amount of text (Redo will still fail when undo buffers are exhausted,
  but text won't be corrupted).
- SliderFloat(): When using keyboard/gamepad and a zero precision format string (e.g. "%.0f"), always step in integer units. (#1866)
- ImFontConfig: Added GlyphMinAdvanceX/GlyphMaxAdvanceX settings useful to make a font appears monospaced, particularly useful
  for icon fonts. (#1869)
- ImFontAtlas: Added GetGlyphRangesChineseSimplifiedCommon() helper that returns a list of ~2500 most common Simplified Chinese
  characters. (#1859) [@JX-Master, @ocornut]
- Examples: OSX: Added imgui_impl_osx.mm binding to be used along with e.g. imgui_impl_opengl2.cpp. (#281, #1870) [@pagghiu, @itamago, @ocornut]
- Examples: GLFW: Made it possible to Shutdown/Init the backend again (by reseting the time storage properly). (#1827) [@ice1000]
- Examples: Win32: Fixed handling of mouse wheel messages to support sub-unit scrolling messages (typically sent by track-pads). (#1874) [@zx64]
- Examples: SDL+Vulkan: Added SDL+Vulkan example.
- Examples: Allegro5: Added support for ImGuiConfigFlags_NoMouseCursorChange flag. Added clipboard support.
- Examples: Allegro5: Unindexing buffers ourselves as Allegro indexed drawing primitives are buggy in the DirectX9 back-end
  (will be fixed in Allegro 5.2.5+).
- Examples: DirectX12: Moved the ID3D12GraphicsCommandList* parameter from ImGui_ImplDX12_NewFrame() to ImGui_ImplDX12_RenderDrawData() which makes a lots more sense. (#301)
- Examples: Vulkan: Reordered parameters ImGui_ImplVulkan_RenderDrawData() to be consistent with other bindings,
  a good occasion since we refactored the code.
- Examples: FreeGLUT: Added FreeGLUT bindings. Added FreeGLUT+OpenGL2 example. (#801)
- Examples: The functions in imgui_impl_xxx.cpp are prefixed with IMGUI_IMPL_API (which defaults to IMGUI_API) to facilitate
  some uses. (#1888)
- Examples: Fixed bindings to use ImGuiMouseCursor_COUNT instead of old name ImGuiMouseCursor_Count_ so they can compile
  with IMGUI_DISABLE_OBSOLETE_FUNCTIONS. (#1887)
- Misc: Updated stb_textedit from 1.09 + patches to 1.12 + minor patches.
- Internals: PushItemFlag() flags are inherited by BeginChild().


-----------------------------------------------------------------------
 VERSION 1.61 (Released 2018-05-14)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.61

Breaking Changes:

- DragInt(): The default compile-time format string has been changed from "%.0f" to "%d", as we are not using integers internally
  any more. If you used DragInt() with custom format strings, make sure you change them to use %d or an integer-compatible format.
  To honor backward-compatibility, the DragInt() code will currently parse and modify format strings to replace %*f with %d,
  giving time to users to upgrade their code.
  If you have IMGUI_DISABLE_OBSOLETE_FUNCTIONS enabled, the code will instead assert! You may run a reg-exp search on your
  codebase for e.g. "DragInt.*%f" to you find them.
- InputFloat(): Obsoleted InputFloat() functions taking an optional "int decimal_precision" in favor of an equivalent and more
  flexible "const char* format", consistent with other functions. Kept redirection functions (will obsolete).
- Misc: IM_DELETE() helper function added in 1.60 doesn't set the input pointer to NULL, more consistent with standard
  expectation and allows passing r-values.

Other Changes:

- Added DragScalar, DragScalarN: supports signed/unsigned, 32/64 bits, float/double data types. (#643, #320, #708, #1011)
- Added InputScalar, InputScalarN: supports signed/unsigned, 32/64 bits, float/double data types. (#643, #320, #708, #1011)
- Added SliderScalar, SliderScalarN: supports signed/unsigned, 32/64 bits, float/double data types. (#643, #320, #708, #1011)
- Window: Fixed pop-ups/tooltips/menus not honoring style.DisplaySafeAreaPadding as well as it should have (part of menus
  displayed outside the safe area, etc.).
- Window: Fixed windows using the ImGuiWindowFlags_NoSavedSettings flag from not using the same default position as other windows. (#1760)
- Window: Relaxed the internal stack size checker to allow Push/Begin/Pop/.../End patterns to be used with PushStyleColor, PushStyleVar, PushFont without causing a false positive assert. (#1767)
- Window: Fixed the default proportional item width lagging by one frame on resize.
- Columns: Fixed a bug introduced in 1.51 where columns would affect the contents size of their container, often creating
  feedback loops when ImGuiWindowFlags_AlwaysAutoResize was used. (#1760)
- Settings: Fixed saving an empty .ini file if CreateContext/DestroyContext are called without a single call to NewFrame(). (#1741)
- Settings: Added LoadIniSettingsFromDisk(), LoadIniSettingsFromMemory(), SaveIniSettingsToDisk(), SaveIniSettingsToMemory()
  to manually load/save .ini settings. (#923, #993)
- Settings: Added io.WantSaveIniSettings flag, which is set to notify the application that e.g. SaveIniSettingsToMemory()
  should be called. (#923, #993)
- Scrolling: Fixed a case where using SetScrollHere(1.0f) at the bottom of a window on the same frame the window height
  has been growing would have the scroll clamped using the previous height. (#1804)
- MenuBar: Made BeginMainMenuBar() honor style.DisplaySafeAreaPadding so the text can be made visible on TV settings that
  don't display all pixels. (#1439) [@dougbinks]
- InputText: On Mac OS X, filter out characters when the CMD modifier is held. (#1747) [@sivu]
- InputText: On Mac OS X, support CMD+SHIFT+Z for Redo. CMD+Y is also supported as major apps seems to default to support both. (#1765) [@lfnoise]
- InputText: Fixed returning true when edition is cancelled with ESC and the current buffer matches the initial value.
- InputFloat,InputFloat2,InputFloat3,InputFloat4: Added variations taking a more flexible and consistent optional
  "const char* format" parameter instead of "int decimal_precision". This allow using custom formats to display values
  in scientific notation, and is generally more consistent with other API.
  Obsoleted functions using the optional "int decimal_precision" parameter. (#648, #712)
- DragFloat, DragInt: Cancel mouse tweak when current value is initially past the min/max boundaries and mouse is pushing
  in the same direction (keyboard/gamepad version already did this).
- DragFloat, DragInt: Honor natural type limits (e.g. INT_MAX, FLT_MAX) instead of wrapping around. (#708, #320)
- DragFloat, SliderFloat: Fixes to allow input of scientific notation numbers when using CTRL+Click to input the value. (~#648, #1011)
- DragFloat, SliderFloat: Rounding-on-write uses the provided format string instead of parsing the precision from the string,
  which allows for finer uses of %e %g etc. (#648, #642)
- DragFloat: Improved computation when using the power curve. Improved lost of input precision with very small steps.
  Added an assert than power-curve requires a min/max range. (~#642)
- DragFloat: The 'power' parameter is only honored if the min/max parameter are also setup.
- DragInt, SliderInt: Fixed handling of large integers (we previously passed data around internally as float, which reduced
  the range of valid integers).
- ColorEdit: Fixed not being able to pass the ImGuiColorEditFlags_NoAlpha or ImGuiColorEditFlags_HDR flags to SetColorEditOptions().
- Nav: Fixed hovering a Selectable() with the mouse so that it update the navigation cursor (as it happened in the pre-1.60 navigation branch). (#787)
- Style: Changed default style.DisplaySafeAreaPadding values from (4,4) to (3,3) so it is smaller than FramePadding and has no effect on main menu bar on a computer. (#1439)
- Fonts: When building font atlas, glyphs that are missing in the fonts are not using the glyph slot to render a dummy/default glyph. Saves space and allow merging fonts with
  overlapping font ranges such as FontAwesome5 which split out the Brands separately from the Solid fonts. (#1703, #1671)
- Misc: Added IMGUI_CHECKVERSION() macro to compare version string and data structure sizes in order to catch issues with mismatching compilation unit settings. (#1695, #1769)
- Misc: Added IMGUI_DISABLE_MATH_FUNCTIONS in imconfig.h to make it easier to redefine wrappers for std/crt math functions.
- Misc: Fix to allow compiling in unity builds where stb_rectpack/stb_truetype may be already included in the same compilation unit.
- Demo: Simple Overlay: Added a context menu item to enable freely moving the window.
- Demo: Added demo for DragScalar(), InputScalar(), SliderScalar(). (#643)
- Examples: Calling IMGUI_CHECKVERSION() in the main.cpp of every example application.
- Examples: Allegro 5: Added support for 32-bit indices setup via defining ImDrawIdx, to avoid an unnecessary conversion (Allegro 5 doesn't support 16-bit indices).
- Examples: Allegro 5: Renamed bindings from imgui_impl_a5.cpp to imgui_impl_allegro5.cpp.
- Examples: DirectX 9: Saving/restoring Transform because they don't seem to be included in the StateBlock. Setting shading mode to Gouraud. (#1790, #1687) [@sr-tream]
- Examples: SDL: Fixed clipboard paste memory leak in the SDL binding code. (#1803) [@eliasdaler]
- Various minor fixes, tweaks, refactoring, comments.


-----------------------------------------------------------------------
 VERSION 1.60 (Released 2018-04-07)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.60

The gamepad/keyboard navigation branch (which has been in the work since July 2016) has been merged.
Gamepad/keyboard navigation is still marked as Beta and has to be enabled explicitly.
Various internal refactoring have also been done, as part of the navigation work and as part of the upcoming viewport/docking work.

Breaking Changes:

- Obsoleted the io.RenderDrawListsFn callback, you can call your graphics engine render function after ImGui::Render().
  e.g. with example backends, call ImDrawData* draw_data = ImGui::GetDrawData(); ImGui_ImplXXXX_RenderDrawData(draw_data).
- Reorganized context handling to be more explicit: (#1599)
  - YOU NOW NEED TO CALL ImGui::CreateContext() AT THE BEGINNING OF YOUR APP, AND CALL ImGui::DestroyContext() AT THE END.
  - removed Shutdown() function, as DestroyContext() serve this purpose. If you are using an old backend from the examples/ folder, remove the line that calls Shutdown().
  - you may pass a ImFontAtlas* pointer to CreateContext() to share a font atlas between contexts. Otherwise CreateContext() will create its own font atlas instance.
  - removed allocator parameters from CreateContext(), they are now setup with SetAllocatorFunctions(), and shared by all contexts.
  - removed the default global context and font atlas instance, which were confusing for users of DLL reloading and users of multiple contexts.
- Renamed ImGuiStyleVar_Count_ to ImGuiStyleVar_COUNT and ImGuiMouseCursor_Count_ to ImGuiMouseCursor_COUNT for consistency with other public enums.
- Fonts: Moved sample TTF files from extra_fonts/ to misc/fonts/. If you loaded files directly from the imgui repo you may need to update your paths.
- Fonts: changed ImFont::DisplayOffset.y to defaults to 0 instead of +1. Fixed vertical rounding of Ascent/Descent to match TrueType renderer.
  If you were adding or subtracting (not assigning) to ImFont::DisplayOffset check if your fonts are correctly aligned vertically. (#1619)
- BeginDragDropSource(): temporarily removed the optional mouse_button=0 parameter because it is not really usable in many situations at the moment.
- Obsoleted IsAnyWindowHovered() in favor of IsWindowHovered(ImGuiHoveredFlags_AnyWindow). Kept redirection function (will obsolete).
- Obsoleted IsAnyWindowFocused() in favor of IsWindowFocused(ImGuiFocusedFlags_AnyWindow). Kept redirection function (will obsolete).
- Renamed io.WantMoveMouse to io.WantSetMousePos for consistency and ease of understanding (was added in 1.52, not used by core, and honored by some binding ahead of merging the Nav branch).
- Removed ImGuiCol_CloseButton, ImGuiCol_CloseButtonActive, ImGuiCol_CloseButtonHovered style colors as the closing cross uses regular button colors now.
- Renamed ImGuiSizeConstraintCallback to ImGuiSizeCallback, ImGuiSizeConstraintCallbackData to ImGuiSizeCallbackData.
- Removed CalcItemRectClosestPoint() which was weird and not really used by anyone except demo code. If you need it should be easy to replicate on your side (you can find the code in 1.53).
- [EDITED] Window: BeginChild() with an explicit name doesn't include the hash within the internal window name. (#1698)
  This change was erroneously introduced, undoing the change done for #894, #713, and not documented properly in the original
  1.60 release Changelog. It was fixed on 2018-09-28 (1.66) and I wrote this paragraph the same day.

Other Changes:

- Doc: Added a Changelog file in the repository to ease comparing versions (it goes back to dear imgui 1.48), until now it was only on GitHub.
- Navigation: merged in the gamepad/keyboard navigation (about a million changes!). (#787, #323)
  The initial focus was to support game controllers, but keyboard is becoming increasingly and decently usable.
- To use Gamepad Navigation:
  - Set io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad to enable.
  - Backend: Set io.BackendFlags |= ImGuiBackendFlags_HasGamepad + fill the io.NavInputs[] fields before calling NewFrame(). Read imgui.cpp for more details.
  - See https://github.com/ocornut/imgui/issues/1599 for recommended gamepad mapping or download PNG/PSD at http://goo.gl/9LgVZW
  - See 'enum ImGuiNavInput_' in imgui.h for a description of inputs. Read imgui.cpp for more details.
- To use Keyboard Navigation:
  - Set io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard to enable. NewFrame() will automatically fill io.NavInputs[] based on your io.KeysDown[] + io.KeyMap[] arrays.
  - Basic controls: arrows to navigate, Alt to enter menus, Space to activate item, Enter to edit text, Escape to cancel/close, Ctrl-Tab to focus windows, etc.
  - When keyboard navigation is active (io.NavActive + ImGuiConfigFlags_NavEnableKeyboard), the io.WantCaptureKeyboard flag will be set.
    For more advanced uses, you may want to read from io.NavActive or io.NavVisible. Read imgui.cpp for more details.
- Navigation: SetItemDefaultFocus() sets the navigation position in addition to scrolling. (#787)
- Navigation: Added IsItemFocused(), added IsAnyItemFocused(). (#787)
- Navigation: Added window flags: ImGuiWindowFlags_NoNav (== ImGuiWindowFlags_NoNavInputs | ImGuiWindowFlags_NoNavFocus).
- Navigation: Style: Added ImGuiCol_NavHighlight, ImGuiCol_NavWindowingHighlight colors. (#787)
- Navigation: TreeNode: Added ImGuiTreeNodeFlags_NavLeftJumpsBackHere flag to allow Nav Left direction to jump back to parent tree node from any of its child. (#1079)
- Navigation: IO: Added io.ConfigFlags (input), io.NavActive (output), io.NavVisible (output). (#787)
- Context: Removed the default global context and font atlas instances, which caused various problems to users of multiple contexts and DLL users. (#1565, #1599)
  YOU NOW NEED TO CALL ImGui::CreateContext() AT THE BEGINNING OF YOUR APP, AND CALL ImGui::DestroyContext() AT THE END. Existing apps will assert/crash without it.
- Context: Added SetAllocatorFunctions() to rewire memory allocators (as a replacement to previous parameters to CreateContext()). Allocators are shared by all contexts and imgui helpers. (#1565, #586, #992, #1007, #1558)
- Context: You may pass a ImFontAtlas to CreateContext() to specify a font atlas to share. Shared font atlas are not owned by the context and not destroyed along with it. (#1599)
- Context: Added IMGUI_DISABLE_DEFAULT_ALLOCATORS to disable linking with malloc/free. (#1565, #586, #992, #1007, #1558)
- IO: Added io.ConfigFlags for user application to store settings for imgui and for the backend:
  - ImGuiConfigFlags_NavEnableKeyboard: Enable keyboard navigation.
  - ImGuiConfigFlags_NavEnableGamepad: Enable gamepad navigation (provided ImGuiBackendFlags_HasGamepad is also set by backend).
  - ImGuiConfigFlags_NavEnableSetMousePos: Instruct navigation to move the mouse cursor. May be useful on TV/console systems where moving a virtual mouse is awkward.
  - ImGuiConfigFlags_NoMouseCursorChange: Instruct backend to not alter mouse cursor shape and visibility (by default the example backend use mouse cursor API of the platform when available)
  - ImGuiConfigFlags_NoMouse: Instruct imgui to clear mouse position/buttons in NewFrame(). This allows ignoring the mouse information passed by the backend.
  - ImGuiConfigFlags_IsSRGB, ImGuiConfigFlags_IsTouchScreen: Flags for general application use.
- IO: Added io.BackendFlags for backend to store its capabilities (currently: _HasGamepad, _HasMouseCursors, _HasSetMousePos). This will be used more in the next version.
- IO: Added ImGuiKey_Insert, ImGuiKey_Space keys. Setup in all example bindings. (#1541)
- IO: Added Horizontal Mouse Wheel support for horizontal scrolling. (#1463) [@tseeker]
- IO: Added IsAnyMouseDown() helper which is helpful for bindings to handle mouse capturing.
- Window: Clicking on a window with the ImGuiWIndowFlags_NoMove flags takes an ActiveId so we can't hover something else when dragging afterwards. (#1381, #1337)
- Window: IsWindowHovered(): Added ImGuiHoveredFlags_AnyWindow, ImGuiFocusedFlags_AnyWindow flags (See Breaking Changes). Added to demo. (#1382)
- Window: Added SetNextWindowBgAlpha() helper. Particularly helpful since the legacy 5-parameters version of Begin() has been marked as obsolete in 1.53. (#1567)
- Window: Fixed SetNextWindowContentSize() with 0.0f on Y axis (or SetNextWindowContentWidth()) overwriting the contents size. Got broken on Dec 10 (1.53). (#1363)
- ArrowButton: Added ArrowButton() given a cardinal direction (e.g. ImGuiDir_Left).
- InputText: Added alternative clipboard shortcuts: Shift+Delete (cut), CTRL+Insert (copy), Shift+Insert (paste). (#1541)
- InputText: Fixed losing Cursor X position when clicking outside on an item that's submitted after the InputText(). It was only noticeable when restoring focus programmatically. (#1418, #1554)
- InputText: Added ImGuiInputTextFlags_CharsScientific flag to also allow 'e'/'E' for input of values using scientific notation. Automatically used by InputFloat.
- Style: Default style is now StyleColorsDark(), instead of the old StyleColorsClassic(). (#707)
- Style: Enable window border by default. (#707)
- Style: Exposed ImGuiStyleVar_WindowTitleAlign, ImGuiStyleVar_ScrollbarSize, ImGuiStyleVar_ScrollbarRounding, ImGuiStyleVar_GrabRounding + added an assert to reduce accidental breakage. (#1181)
- Style: Added style.MouseCursorScale help when using the software mouse cursor facility. (#939).
- Style: Close button nows display a cross before hovering. Fixed cross positioning being a little off. Uses button colors for highlight when hovering. (#707)
- Popup: OpenPopup() Always reopen existing pop-ups. (Removed imgui_internal.h's OpenPopupEx() which was used for this.) (#1497, #1533).
- Popup: BeginPopupContextItem(), BeginPopupContextWindow(), BeginPopupContextVoid(), OpenPopupOnItemClick() all react on mouse release instead of mouse press. (~#439)
- Popup: Better handling of user mistakenly calling OpenPopup() every frame (with reopen_existing option). The error will now be more visible and easier to understand. (#1497)
- Popup: BeginPopup(): Exposed extra_flags parameter that are passed through to Begin(). (#1533)
- Popup: BeginPopupModal: fixed the conditional test for SetNextWindowPos() which was polling the wrong window, which in practice made the test succeed all the time.
- Tooltip: BeginTooltip() sets ImGuiWindowFlags_NoInputs flag.
- Scrollbar: Fixed ScrollbarY enable test after ScrollbarX has been enabled being a little off (small regression from Nov 2017). (#1574)
- Scrollbar: Fixed ScrollbarX enable test subtracting WindowPadding.x (this has been there since the addition of horizontal scroll bar!).
- Columns: Clear offsets data when columns count changed. (#1525)
- Columns: Fixed a memory leak of ImGuiColumnsSet's Columns vector. (#1529) [@unprompted]
- Columns: Fixed resizing a window very small breaking some columns positioning (broken in 1.53).
- Columns: The available column extent takes consideration of the right-most clipped pixel, so the right-most column may look a little wider but will contain the same amount of visible contents.
- MenuBar: Fixed menu bar pushing a clipping rect outside of its allocated bound (usually unnoticeable).
- TreeNode: nodes with the ImGuiTreeNodeFlags_Leaf flag correctly disable highlight when DragDrop is active. (#143, #581)
- Drag and Drop: Increased payload type string to 32 characters instead of 8. (#143)
- Drag and Drop: TreeNode as drop target displays rectangle over full frame. (#1597, #143)
- DragFloat: Fix/workaround for backends which do not preserve a valid mouse position when dragged out of bounds. (#1559)
- InputFloat: Allow inputing value using scientific notation e.g. "1e+10".
- InputDouble: Added InputDouble() function. We use a format string instead of a decimal_precision parameter to also for "%e" and variants. (#1011)
- Slider, Combo: Use ImGuiCol_FrameBgHovered color when hovered. (#1456) [@stfx]
- Combo: BeginCombo(): Added ImGuiComboFlags_NoArrowButton to disable the arrow button and only display the wide value preview box.
- Combo: BeginCombo(): Added ImGuiComboFlags_NoPreview to disable the preview and only display a square arrow button.
- Combo: Arrow button isn't displayed over frame background so its blended color matches other buttons. Left side of the button isn't rounded.
- PlotLines: plot a flat line if scale_min==scale_max. (#1621)
- Fonts: Changed DisplayOffset.y to defaults to 0 instead of +1. Fixed rounding of Ascent/Descent to match TrueType renderer.
  If you were adding or subtracting (not assigning) to ImFont::DisplayOffset check if your fonts are correctly aligned vertically. (#1619)
- Fonts: Updated stb_truetype from 1.14 to stb_truetype 1.19. (w/ include fix from some platforms #1622)
- Fonts: Added optional FreeType rasterizer in misc/freetype. Moved from imgui_club repo. (#618) [@Vuhdo, @mikesart, @ocornut]
- Fonts: Moved extra_fonts/ to misc/fonts/.
- ImFontAtlas: Fixed cfg.MergeMode not reusing existing glyphs if available (always overwrote).
- ImFontAtlas: Handle stb_truetype stbtt_InitFont() and stbtt_PackBegin() possible failures more gracefully, GetTexDataAsRGBA32() won't crash during conversion. (#1527)
- ImFontAtlas: Moved mouse cursor data out of ImGuiContext, fix drawing them with multiple contexts. Also remove the last remaining undesirable dependency on ImGui in imgui_draw.cpp. (#939)
- ImFontAtlas: Added ImFontAtlasFlags_NoPowerOfTwoHeight flag to disable padding font height to nearest power of two. (#1613)
- ImFontAtlas: Added ImFontAtlasFlags_NoMouseCursors flag to disable baking software mouse cursors, mostly to save texture memory on very low end hardware. (#1613)
- ImDrawList: Fixed AddRect() with anti-aliasing disabled (lower-right corner pixel was often missing, rounding looks a little better.) (#1646)
- ImDrawList: Added CloneOutput() helper to facilitate the cloning of ImDrawData or ImDrawList for multi-threaded rendering.
- Misc: Functions passed to libc qsort are explicitly marked cdecl to support compiling with vectorcall as the default calling convention. (#1230, #1611) [@RandyGaul]
- Misc: ImVec2: added [] operator. This is becoming desirable for some code working of either axes independently. Better adding it sooner than later.
- Misc: NewFrame(): Added an assert to detect incorrect filling of the io.KeyMap[] array earlier. (#1555)
- Misc: Added IM_OFFSETOF() helper in imgui.h (previously was in imgui_internal.h)
- Misc: Added IM_NEW(), IM_DELETE() helpers in imgui.h (previously were in imgui_internal.h)
- Misc: Added obsolete redirection function GetItemsLineHeightWithSpacing() (which redirects to GetFrameHeightWithSpacing()), as intended and stated in docs of 1.53.
- Misc: Added misc/natvis/imgui.natvis for visual studio debugger users to easily visualize imgui internal types. Added to examples projects.
- Misc: Added IMGUI_USER_CONFIG to define a custom configuration filename. (#255, #1573, #1144, #41)
- Misc: Added IMGUI_STB_TRUETYPE_FILENAME and IMGUI_STB_RECT_PACK_FILENAME compile time directives to use another version of the stb_ files.
- Misc: Updated stb_rect_pack from 0.10 to 0.11 (minor changes).
  (Those flags are not used by ImGui itself, they only exists to make it easy for the engine/backend to pass information to the application in a standard manner.)
- Metrics: Added display of Columns state.
- Demo: Improved Selectable() examples. (#1528)
- Demo: Tweaked the Child demos, added a menu bar to the second child to test some navigation functions.
- Demo: Console: Using ImGuiCol_Text to be more friendly to color changes.
- Demo: Using IM_COL32() instead of ImColor() in ImDrawList centric contexts. Trying to phase out use of the ImColor helper whenever possible.
- Examples: Files in examples/ now include their own changelog so it is easier to occasionally update your bindings if needed.
- Examples: Using Dark theme by default. (#707). Tweaked demo code.
- Examples: Added support for horizontal mouse wheel for API that allows it. (#1463) [@tseeker]
- Examples: All examples now setup the io.BackendFlags to signify they can honor mouse cursors, gamepad, etc.
- Examples: DirectX10: Fixed erroneous call to io.Fonts->ClearInputData() + ClearTexData() that was left in DX10 example but removed in 1.47 (Nov 2015) in every other backends. (#1733)
- Examples: DirectX12: Added DirectX 12 example. (#301) [@jdm3]
- Examples: OpenGL3+GLFW,SDL: Changed GLSL shader version from 330 to 150. (#1466, #1504)
- Examples: OpenGL3+GLFW,SDL: Added a way to override the GLSL version string in the Init function. (#1466, #1504).
- Examples: OpenGL3+GLFW,SDL: Creating VAO in the render function so it can be more easily used by multiple shared OpenGL contexts. (#1217)
- Examples: OpenGL3+GLFW: Using 3.2 context instead of 3.3. (#1466)
- Examples: OpenGL: Setting up glPixelStorei() explicitly before uploading texture.
- Examples: OpenGL: Calls to glPolygonMode() are casting parameters as GLEnum to not fail with more strict bindings. (#1628) [@ilia-glushchenko]
- Examples: Win32 (DirectX9,10,11,12): Added support for mouse cursor shapes. (#1495)
- Examples: Win32 (DirectX9,10,11,12: Support for windows using the CS_DBLCLKS class flag by handling the double-click messages (WM_LBUTTONDBLCLK etc.). (#1538, #754) [@ndandoulakis]
- Examples: Win32 (DirectX9,10,11,12): Made the Win32 proc handlers not assert if there is no active context yet, to be more flexible with creation order. (#1565)
- Examples: GLFW: Added support for mouse cursor shapes (the diagonal resize cursors are unfortunately not supported by GLFW at the moment. (#1495)
- Examples: GLFW: Don't attempt to change the mouse cursor input mode if it is set to GLFW_CURSOR_DISABLED by the application. (#1202) [@PhilCK]
- Examples: SDL: Added support for mouse cursor shapes. (#1626) [@olls]
- Examples: SDL: Using SDL_CaptureMouse() to retrieve coordinates outside of client area when dragging (SDL 2.0.4+ only, otherwise using SDL_WINDOW_INPUT_FOCUS instead of previously SDL_WINDOW_MOUSE_FOCUS). (#1559)
- Examples: SDL: Enabled vsync by default so people don't come at us when the examples are running at 2000 FPS and burning a CPU core.
- Examples: SDL: Using SDL_GetPerformanceCounter() / SDL_GetPerformanceFrequency() to handle frame-rate over 1000 FPS properly. (#996)
- Examples: SDL: Using scan-code exclusively instead of a confusing mixture of scan-codes and key-codes.
- Examples: SDL: Visual Studio: Added .vcxproj file. Using %SDL2_DIR% in the default .vcxproj and build files instead of %SDL_DIR%, the earlier being more standard.
- Examples: Vulkan: Visual Studio: Added .vcxproj file.
- Examples: Apple: Fixed filenames in OSX xcode project. Various other Mac friendly fixes. [@gerryhernandez etc.]
- Examples: Visual Studio: Disabled extraneous function-level check in Release build.
- Various fixes, tweaks, internal refactoring, optimizations, comments.


-----------------------------------------------------------------------
 VERSION 1.53 (Released 2017-12-25)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.53

Breaking Changes:

- Renamed the emblematic `ShowTestWindow()` function to `ShowDemoWindow()`. Kept redirection function (will obsolete).
- Renamed `GetItemsLineHeightWithSpacing()` to `GetFrameHeightWithSpacing()` for consistency. Kept redirection function (will obsolete).
- Renamed `ImGuiTreeNodeFlags_AllowOverlapMode` flag to `ImGuiTreeNodeFlags_AllowItemOverlap`. Kept redirection enum (will obsolete).
- Obsoleted `IsRootWindowFocused()` in favor of using `IsWindowFocused(ImGuiFocusedFlags_RootWindow)`. Kept redirection function (will obsolete). (#1382)
- Obsoleted `IsRootWindowOrAnyChildFocused()` in favor of using `IsWindowFocused(ImGuiFocusedFlags_RootAndChildWindows)`. Kept redirection function (will obsolete). (#1382)
- Obsoleted `IsRootWindowOrAnyChildHovered()` in favor of using `IsWindowHovered(ImGuiHoveredFlags_RootAndChildWindows)`. Kept redirection function (will obsolete). (#1382)
- Obsoleted `SetNextWindowContentWidth() in favor of using `SetNextWindowContentSize()`. Kept redirection function (will obsolete).
- Renamed `ImGuiTextBuffer::append()` helper to `appendf()`, and `appendv()` to `appendfv()` for consistency. If you copied the 'Log' demo in your code, it uses appendv() so that needs to be renamed.
- ImDrawList: Removed 'bool anti_aliased = true' final parameter of `ImDrawList::AddPolyline()` and `ImDrawList::AddConvexPolyFilled()`. Prefer manipulating ImDrawList::Flags if you need to toggle them during the frame.
- Style, ImDrawList: Renamed `style.AntiAliasedShapes` to `style.AntiAliasedFill` for consistency and as a way to explicitly break code that manipulate those flag at runtime. You can now manipulate ImDrawList::Flags.
- Style, Begin: Removed `ImGuiWindowFlags_ShowBorders` window flag. Borders are now fully set up in the ImGuiStyle structure (see e.g. `style.FrameBorderSize`, `style.WindowBorderSize`, `style.PopupBorderSize`).
  Use `ImGui::ShowStyleEditor()` to look them up.
  Please note that the style system will keep evolving (hopefully stabilizing in Q1 2018), and so custom styles will probably subtly break over time.
  It is recommended that you use the `StyleColorsClassic()`, `StyleColorsDark()`, `StyleColorsLight()` functions. Also see `ShowStyleSelector()`.
- Style: Removed `ImGuiCol_ComboBg` in favor of combo boxes using `ImGuiCol_PopupBg` for consistency. Combo are normal pop-ups.
- Style: Renamed `ImGuiCol_ChildWindowBg` to `ImGuiCol_ChildBg`.
- Style: Renamed `style.ChildWindowRounding` to `style.ChildRounding`, `ImGuiStyleVar_ChildWindowRounding` to `ImGuiStyleVar_ChildRounding`.
- Removed obsolete redirection functions: SetScrollPosHere() - marked obsolete in v1.42, July 2015.
- Removed obsolete redirection functions: GetWindowFont(), GetWindowFontSize() - marked obsolete in v1.48, March 2016.

Other Changes:

- Added `io.OptCursorBlink` option to allow disabling cursor blinking. (#1427) [renamed to io.ConfigCursorBlink in 1.63]
- Added `GetOverlayDrawList()` helper to quickly get access to a ImDrawList that will be rendered in front of every windows.
- Added `GetFrameHeight()` helper which returns `(FontSize + style.FramePadding.y * 2)`.
- Drag and Drop: Added Beta API to easily use drag and drop patterns between imgui widgets.
  - Setup a source on a widget with `BeginDragDropSource()`, `SetDragDropPayload()`, `EndDragDropSource()` functions.
  - Receive data with `BeginDragDropTarget()`, `AcceptDragDropPayload()`, `EndDragDropTarget()`.
  - See ImGuiDragDropFlags for various options.
  - The ColorEdit4() and ColorButton() widgets now support Drag and Drop.
  - The API is tagged as Beta as it still may be subject to small changes.
- Drag and Drop: When drag and drop is active, tree nodes and collapsing header can be opened by hovering on them for 0.7 seconds.
- Renamed io.OSXBehaviors to io.OptMacOSXBehaviors. Should not affect users as the compile-time default is usually enough. (#473, #650)
- Style: Added StyleColorsDark() style. (#707) [@dougbinks]
- Style: Added StyleColorsLight() style. Best used with frame borders + thicker font than the default font. (#707)
- Style: Added style.PopupRounding setting. (#1112)
- Style: Added style.FrameBorderSize, style.WindowBorderSize, style.PopupBorderSize. Removed ImGuiWindowFlags_ShowBorders window flag!
  Borders are now fully set up in the ImGuiStyle structure. Use ImGui::ShowStyleEditor() to look them up. (#707, fix #819, #1031)
- Style: Various small changes to the classic style (most noticeably, buttons are now using blue shades). (#707)
- Style: Renamed ImGuiCol_ChildWindowBg to ImGuiCol_ChildBg.
- Style: Renamed style.ChildWindowRounding to style.ChildRounding, ImGuiStyleVar_ChildWindowRounding to ImGuiStyleVar_ChildRounding.
- Style: Removed ImGuiCol_ComboBg in favor of combo boxes using ImGuiCol_PopupBg for consistency. (#707)
- Style: Made the ScaleAllSizes() helper rounds down every values so they are aligned on integers.
- Focus: Added SetItemDefaultFocus(), which in the current (master) branch behave the same as doing `if (IsWindowAppearing()) SetScrollHere()`.
  In the navigation branch this will also set the default focus. Prefer using this when creating combo boxes with `BeginCombo()` so your code will be forward-compatible with gamepad/keyboard navigation features. (#787)
- Combo: Pop-up grows horizontally to accommodate for contents that is larger then the parent combo button.
- Combo: Added BeginCombo()/EndCombo() API which allows use to submit content of any form and manage your selection state without relying on indices.
- Combo: Added ImGuiComboFlags_PopupAlignLeft flag to BeginCombo() to prioritize keeping the pop-up on the left side (for small-button-looking combos).
- Combo: Added ImGuiComboFlags_HeightSmall, ImGuiComboFlags_HeightLarge, ImGuiComboFlags_HeightLargest to easily provide desired pop-up height.
- Combo: You can use SetNextWindowSizeConstraints() before BeginCombo() to specify specific pop-up width/height constraints.
- Combo: Offset popup position by border size so that a double border isn't so visible. (#707)
- Combo: Recycling windows by using a stack number instead of a unique id, wasting less memory (like menus do).
- InputText: Added ImGuiInputTextFlags_NoUndoRedo flag. (#1506, #1508) [@ibachar]
- Window: Fixed auto-resize allocating too much space for scrollbar when SizeContents is bigger than maximum window size (fixes c0547d3). (#1417)
- Window: Child windows with MenuBar use regular WindowPadding.y so layout look consistent as child or as a regular window.
- Window: Begin(): Fixed appending into a child window with a second Begin() from a different window stack querying the wrong window for the window->Collapsed test.
- Window: Calling IsItemActive(), IsItemHovered() etc. after a call to Begin() provides item data for the title bar, so you can easily test if the title bar is being hovered, etc. (#823)
- Window: Made it possible to use SetNextWindowPos() on a child window.
- Window: Fixed a one frame glitch. When an appearing window claimed the focus themselves, the title bar wouldn't use the focused color for one frame.
- Window: Added ImGuiWindowFlags_ResizeFromAnySide flag to resize from any borders or from the lower-left corner of a window. This requires your backend to honor GetMouseCursor() requests for full usability. (#822)
- Window: Sizing fixes when using SetNextWindowSize() on individual axises.
- Window: Hide new window for one frame until they calculate their size. Also fixes SetNextWindowPos() given a non-zero pivot. (#1694)
- Window: Made mouse wheel scrolling accommodate better to windows that are smaller than the scroll step.
- Window: SetNextWindowContentSize() adjust for the size of decorations (title bar/menu bar), but _not_ for borders are we consistently make borders not affect layout.
  If you need a non-child window of an exact size with border enabled but zero window padding, you'll need to accommodate for the border size yourself.
- Window: Using the ImGuiWindowFlags_NoScrollWithMouse flag on a child window forwards the mouse wheel event to the parent window, unless either ImGuiWindowFlags_NoInputs or ImGuiWindowFlags_NoScrollbar are also set. (#1380, #1502)
- Window: Active Modal window always set the WantCaptureKeyboard flag. (#744)
- Window: Moving window doesn't use accumulating MouseDelta so straying out of imgui boundaries keeps moved imgui window at the same cursor-relative position.
- IsWindowFocused(): Added ImGuiFocusedFlags_ChildWindows flag to include child windows in the focused test. (#1382).
- IsWindowFocused(): Added ImGuiFocusedFlags_RootWindow flag to start focused test from the root (top-most) window. Obsolete IsRootWindowFocused(). (#1382)
- IsWindowHovered(): Added ImGuiHoveredFlags_ChildWindows flag to include child windows in the hovered test. (#1382).
- IsWindowHovered(): Added ImGuiHoveredFlags_RootWindow flag to start hovered test from the root (top-most) window. The combination of both flags obsoletes IsRootWindowOrAnyChildHovered(). (#1382)
- IsWindowHovered(): Fixed return value when an item is active to use the same logic as IsItemHovered(). (#1382, #1404)
- IsWindowHovered(): Always return true when current window is being moved. (#1382)
- Scrollbar: Fixed issues with vertical scrollbar flickering/appearing, typically when manually resizing and using a pattern of filling available height (e.g. full sized BeginChild).
- Scrollbar: Minor graphical fix for when scrollbar don't have enough visible space to display the full grab.
- Scrolling: Fixed padding and scrolling asymmetry where lower/right sides of a window wouldn't use WindowPadding properly + causing minor scrolling glitches.
- Tree: TreePush with zero arguments was ambiguous. Resolved by making it call TreePush(const void*). [@JasonWilkins]
- Tree: Renamed ImGuiTreeNodeFlags_AllowOverlapMode to ImGuiTreeNodeFlags_AllowItemOverlap. (#600, #1330)
- MenuBar: Fixed minor rendering issues on the right size when resizing a window very small and using rounded window corners.
- MenuBar: better software clipping to handle small windows, in particular child window don't have minimum constraints so we need to render clipped menus better.
- BeginMenu(): Tweaked the Arrow/Triangle displayed on child menu items.
- Columns: Clipping columns borders on Y axis on CPU because some Linux GPU drivers appears to be unhappy with triangle spanning large regions. (#125)
- Columns: Added ImGuiColumnsFlags_GrowParentContentsSize to internal API to restore old content sizes behavior (may be obsolete). (#1444, #125)
- Columns: Columns width is no longer lost when dragging a column to the right side of the window, until releasing the mouse button you have a chance to save them. (#1499, #125). [@ggtucker]
- Columns: Fixed dragging when using a same of columns multiple times in the frame. (#125)
- Indent(), Unindent(): Allow passing negative values.
- ColorEdit4(): Made IsItemActive() return true when picker pop-up is active. (#1489)
- ColorEdit4(): Tweaked tooltip so that the color button aligns more correctly with text.
- ColorEdit4(): Support drag and drop. Color buttons can be used as drag sources, and ColorEdit widgets as drag targets. (#143)
- ColorPicker4(): Fixed continuously returning true when holding mouse button on the sat/value/alpha locations. We only return true on value change. (#1489)
- NewFrame(): using literal strings in the most-frequently firing IM_ASSERT expressions to increase the odd of programmers seeing them (especially those who don't use a debugger).
- NewFrame() now asserts if neither Render or EndFrame have been called. Exposed EndFrame(). Made it legal to call EndFrame() more than one. (#1423)
- ImGuiStorage: Added BuildSortByKey() helper to rebuild storage from scratch.
- ImFont: Added GetDebugName() helper.
- ImFontAtlas: Added missing Thai punctuation in the GetGlyphRangesThai() ranges. (#1396) [@nProtect]
- ImDrawList: Removed 'bool anti_aliased = true' final parameter of ImDrawList::AddPolyline() and ImDrawList::AddConvexPolyFilled(). Anti-aliasing is controlled via the regular style.AntiAliased flags.
- ImDrawList: Added ImDrawList::AddImageRounded() helper. (#845) [@thedmd]
- ImDrawList: Refactored to make ImDrawList independent of ImGui. Removed static variable in PathArcToFast() which caused linking issues to some.
- ImDrawList: Exposed ImDrawCornerFlags, replaced occurrences of ~0 with an explicit ImDrawCornerFlags_All. NB: Inversed BotLeft (prev 1<<3, now 1<<2) and BotRight (prev 1<<2, now 1<<3).
- ImVector: Added ImVector::push_front() helper.
- ImVector: Added ImVector::contains() helper.
- ImVector: insert() uses grow_capacity() instead of using grow policy inconsistent with push_back().
- Internals: Remove requirement to define IMGUI_DEFINE_PLACEMENT_NEW to use the IM_PLACEMENT_NEW macro. (#1103)
- Internals: ButtonBehavior: Fixed ImGuiButtonFlags_NoHoldingActiveID flag from incorrectly setting the ActiveIdClickOffset field.
  This had no known effect within imgui code but could have affected custom drag and drop patterns. And it is more correct this way! (#1418)
- Internals: ButtonBehavior: Fixed ImGuiButtonFlags_AllowOverlapMode to avoid temporarily activating widgets on click before they have been correctly double-hovered. (#319, #600)
- Internals: Added SplitterBehavior() helper. (#319)
- Internals: Added IM_NEW(), IM_DELETE() helpers. (#484, #504, #1517)
- Internals: Basic refactor of the settings API which now allows external elements to be loaded/saved.
- Demo: Added ShowFontSelector() showing loaded fonts.
- Demo: Added ShowStyleSelector() to select among default styles. (#707)
- Demo: Renamed the emblematic ShowTestWindow() function to ShowDemoWindow().
- Demo: Style Editor: Added a "Simplified settings" sections with check-boxes for border size and frame rounding. (#707, #1019)
- Demo: Style Editor: Added combo box to select stock styles and select current font when multiple are loaded. (#707)
- Demo: Style Editor: Using local storage so Save/Revert button makes more sense without code passing its storage. Added horizontal scroll bar. Fixed Save/Revert button to be always accessible. (#1211)
- Demo: Console: Fixed context menu issue. (#1404)
- Demo: Console: Fixed incorrect positioning which was hidden by a minor scroll issue (this would affect people who copied the Console code as is).
- Demo: Constrained Resize: Added more test cases. (#1417)
- Demo: Custom Rendering: Fixed clipping rectangle extruding out of parent window.
- Demo: Layout: Removed unnecessary and misleading BeginChild/EndChild calls.
- Demo: The "Color Picker with Palette" demo supports drag and drop. (#143)
- Demo: Display better mouse cursor info for debugging backends.
- Demo: Stopped using rand() function in demo code.
- Examples: Added a handful of extra comments (about fonts, third-party libraries used in the examples, etc.).
- Examples: DirectX9: Handle loss of D3D9 device (D3DERR_DEVICELOST). (#1464)
- Examples: Added null_example/ which is helpful for quick testing on multiple compilers/settings without relying on graphics library.
- Fix for using alloca() in "Clang with Microsoft Codechain" mode.
- Various fixes, optimizations, comments.


-----------------------------------------------------------------------
 VERSION 1.52 (2017-10-27)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.52

Breaking Changes:

- IO: `io.MousePos` needs to be set to ImVec2(-FLT_MAX,-FLT_MAX) when mouse is unavailable/missing, instead of ImVec2(-1,-1) as previously) This is needed so we can clear `io.MouseDelta` field when the mouse is made available again.
- Renamed `AlignFirstTextHeightToWidgets()` to `AlignTextToFramePadding()`. Kept inline redirection function (will obsolete).
- Obsoleted the legacy 5 parameters version of Begin(). Please avoid using it. If you need a transparent window background, uses `PushStyleColor()`. The old size parameter there was also misleading and equivalent to calling `SetNextWindowSize(size, ImGuiCond_FirstTimeEver)`. Kept inline redirection function (will obsolete).
- Obsoleted `IsItemHoveredRect()`, `IsMouseHoveringWindow()` in favor of using the newly introduced flags of `IsItemHovered()` and `IsWindowHovered()`. Kept inline redirection function (will obsolete). (#1382)
- Obsoleted 'SetNextWindowPosCenter()' in favor of using 1SetNextWindowPos()` with a pivot value which allows to do the same and more. Keep inline redirection function.
- Removed `IsItemRectHovered()`, `IsWindowRectHovered()` recently introduced in 1.51 which were merely the more consistent/correct names for the above functions which are now obsolete anyway. (#1382)
- Changed `IsWindowHovered()` default parameters behavior to return false if an item is active in another window (e.g. click-dragging item from another window to this window). You can use the newly introduced IsWindowHovered() flags to requests this specific behavior if you need it. (#1382)
- Renamed imconfig.h's `IMGUI_DISABLE_WIN32_DEFAULT_CLIPBOARD_FUNCS`/`IMGUI_DISABLE_WIN32_DEFAULT_IME_FUNCS` to `IMGUI_DISABLE_WIN32_DEFAULT_CLIPBOARD_FUNCTIONS`/`IMGUI_DISABLE_WIN32_DEFAULT_IME_FUNCTIONS` for consistency.
- Renamed ImFont::Glyph to ImFontGlyph. Kept redirection typedef (will obsolete).

Other Changes:

- ProgressBar: fixed rendering when straddling rounded area. (#1296)
- SliderFloat, DragFloat: Using scientific notation e.g. "%.1e" in the displayed format string doesn't mistakenly trigger rounding of the value. [@MomentsInGraphics]
- Combo, InputFloat, InputInt: Made the small button on the right side align properly with the equivalent colored button of ColorEdit4().
- IO: Tweaked logic for `io.WantCaptureMouse` so it now outputs false when e.g. hovering over void while an InputText() is active. (#621) [@pdoane]
- IO: Fixed `io.WantTextInput` from mistakenly outputting true when an activated Drag or Slider was previously turned into an InputText(). (#1317)
- Misc: Added flags to `IsItemHovered()`, `IsWindowHovered()` to access advanced hovering-test behavior. Generally useful for pop-ups and drag and drop behaviors: (relates to ~#439, #1013, #143, #925)
  - `ImGuiHoveredFlags_AllowWhenBlockedByPopup`
  - `ImGuiHoveredFlags_AllowWhenBlockedByActiveItem`
  - `ImGuiHoveredFlags_AllowWhenOverlapped`
  - `ImGuiHoveredFlags_RectOnly`
- Input: Added `IsMousePosValid()` helper.
- Input: Added `GetKeyPressedAmount()` to easily measure press count when the repeat rate is faster than the frame rate.
- Input/Focus: Disabled TAB and Shift+TAB when CTRL key is held.
- CheckBox: Now rendering a tick mark instead of a full square.
- ColorEdit4: Added "Copy as..." option in context menu. (#346)
- ColorPicker: Improved ColorPicker hue wheel color interpolation. (#1313) [@thevaber]
- ColorButton: Reduced bordering artifact that would be particularly visible with an opaque Col_FrameBg and FrameRounding enabled.
- ColorButton: Fixed rendering color button with a checkerboard if the transparency comes from the global style.Alpha and not from the actual source color.
- TreeNode: Added `ImGuiTreeNodeFlags_FramePadding` flag to conveniently create a tree node with full padding at the beginning of a line, without having to call `AlignTextToFramePadding()`.
- Trees: Fixed calling `SetNextTreeNodeOpen()` on a collapsed window leaking to the first tree node item of the next frame.
- Layout: Horizontal layout is automatically enforced in a menu bar, so you can use non-MenuItem elements without calling SameLine().
- Separator: Output a vertical separator when used inside a menu bar (or in general when horizontal layout is active, but that isn't exposed yet!).
- Window: Added `IsWindowAppearing()` helper (helpful e.g. as a condition before initializing some of your own things.).
- Window: Added pivot parameter to `SetNextWindowPos()`, making it possible to center or right align a window. Obsoleted `SetNextWindowPosCenter()`.
- Window: Fixed title bar color of top-most window under a modal window.
- Window: Fixed not being able to move a window by clicking on one of its child window. (#1337, #635)
- Window: Fixed `Begin()` auto-fit calculation code that predict the presence of a scrollbar so it works better when window size constraints are used.
- Window: Fixed calling `Begin()` more than once per frame setting `window_just_activated_by_user` which in turn would set enable the Appearing condition for that frame.
- Window: The implicit "Debug" window now uses a "Debug##Default" identifier instead of "Debug" to allow user creating a window called "Debug" without losing their custom flags.
- Window: Made the `ImGuiWindowFlags_NoMove` flag properly inherited from parent to child. In a setup with ParentWindow (no flag) -> Child (NoMove) -> SubChild (no flag), the user won't be able to move the parent window by clicking on SubChild. (#1381)
- Popups: Pop-ups can be closed with a right-click anywhere, without altering focus under the pop-up. (~#439)
- Popups: `BeginPopupContextItem()`, `BeginPopupContextWindow()` are now setup to allow reopening a context menu by right-clicking again. (~#439)
- Popups: `BeginPopupContextItem()` now supports a NULL string identifier and uses the last item ID if available.
- Popups: Added `OpenPopupOnItemClick()` helper which mimic `BeginPopupContextItem()` but doesn't do the BeginPopup().
- MenuItem: Only activating on mouse release. [@Urmeli0815] (was already fixed in nav branch).
- MenuItem: Made tick mark thicker (thick mark?).
- MenuItem: Tweaks to be usable inside a menu bar (nb: it looks like a regular menu and thus is misleading, prefer using Button() and regular widgets in menu bar if you need to). (#1387)
- ImDrawList: Fixed a rare draw call merging bug which could lead to undisplayed triangles. (#1172, #1368)
- ImDrawList: Fixed a rare bug in `ChannelsMerge()` when all contents has been clipped, leading to an extraneous draw call being created. (#1172, #1368)
- ImFont: Added `AddGlyph()` building helper for use by custom atlas builders.
- ImFontAtlas: Added support for CustomRect API to submit custom rectangles to be packed into the atlas. You can map them as font glyphs, or use them for custom purposes.
  After the atlas is built you can query the position of your rectangles in the texture and then copy your data there. You can use this features to create e.g. full color font-mapped icons.
- ImFontAtlas: Fixed fall-back handling when merging fonts, if a glyph was missing from the second font input it could have used a glyph from the first one. (#1349) [@inolen]
- ImFontAtlas: Fixed memory leak on build failure case when stbtt_InitFont failed (generally due to incorrect or supported font type). (#1391) (@Moka42)
- ImFontConfig: Added `RasterizerMultiply` option to alter the brightness of individual fonts at rasterization time, which may help increasing readability for some.
- ImFontConfig: Added `RasterizerFlags` to pass options to custom rasterizer (e.g. the [imgui_freetype](https://github.com/ocornut/imgui_club/tree/master/imgui_freetype) rasterizer in imgui_club has such options).
- ImVector: added resize() variant with initialization value.
- Misc: Changed the internal name formatting of child windows identifier to use slashes (instead of dots) as separator, more readable.
- Misc: Fixed compilation with `IMGUI_DISABLE_OBSOLETE_FUNCTIONS` defined.
- Misc: Marked all format+va_list functions with format attribute so GCC/Clang can warn about misuses.
- Misc: Fixed compilation on NetBSD due to missing alloca.h (#1319) [@RyuKojiro]
- Misc: Improved warnings compilation for newer versions of Clang. (#1324) (@waywardmonkeys)
- Misc: Added `io.WantMoveMouse flags` (from Nav branch) and honored in Examples applications. Currently unused but trying to spread Examples applications code that supports it.
- Misc: Added `IMGUI_DISABLE_FORMAT_STRING_FUNCTIONS` support in imconfig.h to allow user reimplementing the `ImFormatString()` functions e.g. to use stb_printf(). (#1038)
- Misc: [Windows] Fixed default Win32 `SetClipboardText()` handler leaving the Win32 clipboard handler unclosed on failure. [@pdoane]
- Style: Added `ImGuiStyle::ScaleAllSizes(float)` helper to make it easier to have application transition e.g. from low to high DPI with a matching style.
- Metrics: Draw window bounding boxes when hovering Pos/Size; List all draw layers; Trimming empty commands like Render() does.
- Examples: OpenGL3: Save and restore sampler state. (#1145) [@nlguillemot]
- Examples: OpenGL2, OpenGL3: Save and restore polygon mode. (#1307) [@JJscott]
- Examples: DirectX11: Allow creating device with feature level 10 since we don't really need much for that example. (#1333)
- Examples: DirectX9/10/12: Using the Win32 SetCapture/ReleaseCapture API to read mouse coordinates when they are out of bounds. (#1375) [@Gargaj, @ocornut]
- Tools: Fixed binary_to_compressed_c tool to return 0 when successful. (#1350) [@benvanik]
- Internals: Exposed more helpers and unfinished features in imgui_internal.h. (use at your own risk!).
- Internals: A bunch of internal refactoring, hopefully haven't broken anything! Merged a bunch of internal changes from the upcoming Navigation branch.
- Various tweaks, fixes and documentation changes.

Beta Navigation Branch:
(Lots of work has been done toward merging the Beta Gamepad/Keyboard Navigation branch (#787) in master.)
(Please note that this branch is always kept up to date with master. If you are using the navigation branch, some of the changes include:)
- Nav: Added `#define IMGUI_HAS_NAV` in imgui.h to ease sharing code between both branches. (#787)
- Nav: MainMenuBar now releases focus when user gets out of the menu layer. (#787)
- Nav: When applying focus to a window with only menus, the menu layer is automatically activated. (#787)
- Nav: Added `ImGuiNavInput_KeyMenu` (~Alt key) aside from ImGuiNavInput_PadMenu input as it is one differentiator of pad vs keyboard that was detrimental to the keyboard experience. Although isn't officially supported, it makes the current experience better. (#787)
- Nav: Move requests now wrap vertically inside Menus and Pop-ups. (#787)
- Nav: Allow to collapse tree nodes with NavLeft and open them with NavRight. (#787, #1079).
- Nav: It's now possible to navigate sibling of a menu-bar while navigating inside one of their child. If a Left<>Right navigation request fails to find a match we forward the request to the root menu. (#787, #126)
- Nav: Fixed `SetItemDefaultFocus` from stealing default focus when we are initializing default focus for a menu bar layer. (#787)
- Nav: Support for fall-back horizontal scrolling with PadLeft/PadRight (nb: fall-back scrolling is only used to navigate windows that have no interactive items). (#787)
- Nav: Fixed tool-tip from being selectable in the window selection list. (#787)
- Nav: `CollapsingHeader(bool*)` variant: fixed for `IsItemHovered()` not working properly in the nav branch. (#600, #787)
- Nav: InputText: Fixed using Up/Down history callback feature when Nav is enabled. (#787)
- Nav: InputTextMultiline: Fixed navigation/selection. Disabled selecting all when activating a multi-line text editor. (#787)
- Nav: More consistently drawing a (thin) navigation rectangle hover filled frames such as tree nodes, collapsing header, menus. (#787)
- Nav: Various internal refactoring.


-----------------------------------------------------------------------
 VERSION 1.51 (2017-08-24)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.51

Breaking Changes:

Work on dear imgui has been gradually resuming. It means that fixes and new features should be tackled at a faster rate than last year. However, in order to move forward with the library and get rid of some cruft, I have taken the liberty to be a little bit more aggressive than usual with API breaking changes. Read the details below and search for those names in your code! In the grand scheme of things, those changes are small and should not affect everyone, but this is technically our most aggressive release so far in term of API breakage. If you want to be extra forward-facing, you can enable `#define IMGUI_DISABLE_OBSOLETE_FUNCTIONS` in your imconfig.h to disable the obsolete names/redirection.

- Renamed `IsItemHoveredRect()` to `IsItemRectHovered()`. Kept inline redirection function (will obsolete).
- Renamed `IsMouseHoveringWindow()` to `IsWindowRectHovered()` for consistency. Kept inline redirection function (will obsolete).
- Renamed `IsMouseHoveringAnyWindow()` to `IsAnyWindowHovered()` for consistency. Kept inline redirection function (will obsolete).
- Renamed `ImGuiCol_Columns***` enums to `ImGuiCol_Separator***`. Kept redirection enums (will obsolete).
- Renamed `ImGuiSetCond***` types and enums to `ImGuiCond***`. Kept redirection enums (will obsolete).
- Renamed `GetStyleColName()` to `GetStyleColorName()` for consistency. Unlikely to be used by end-user!
- Added `PushStyleColor(ImGuiCol idx, ImU32 col)` overload, which _might_ cause an "ambiguous call" compilation error if you are using ImColor() with implicit cast. Cast to ImU32 or ImVec4 explicitly to fix.
- Marked the weird `IMGUI_ONCE_UPON_A_FRAME` helper macro as obsolete. Prefer using the more explicit `ImGuiOnceUponAFrame`.
- Changed `ColorEdit4(const char* label, float col[4], bool show_alpha = true)` signature to `ColorEdit4(const char* label, float col[4], ImGuiColorEditFlags flags = 0)`, where flags 0x01 is a safe no-op (hello dodgy backward compatibility!). The new `ColorEdit4`/`ColorPicker4` functions have lots of available flags! Check and run the demo window, under "Color/Picker Widgets", to understand the various new options.
- Changed signature of `ColorButton(ImVec4 col, bool small_height = false, bool outline_border = true)` to `ColorButton(const char* desc_id, ImVec4 col, ImGuiColorEditFlags flags = 0, ImVec2 size = ImVec2(0,0))`. This function was rarely used and was very dodgy (no explicit ID!).
- Changed `BeginPopupContextWindow(bool also_over_items=true, const char* str_id=NULL, int mouse_button=1)` signature to `(const char* str_id=NULL, int mouse_button=1, bool also_over_items=true)`. This is perhaps the most aggressive change in this update, but note that the majority of users relied on default parameters completely, so this will affect only a fraction of users of this already rarely used function.
- Removed `IsPosHoveringAnyWindow()`, which was partly broken and misleading. In the vast majority of cases, people using that function wanted to use `io.WantCaptureMouse` flag. Replaced with IM_ASSERT + comment redirecting user to `io.WantCaptureMouse`. (#1237)
- Removed the old `ValueColor()` helpers, they are equivalent to calling `Text(label)` + `SameLine()` + `ColorButton()`.
- Removed `ColorEditMode()` and `ImGuiColorEditMode` type in favor of `ImGuiColorEditFlags` and parameters to the various Color*() functions. The `SetColorEditOptions()` function allows to initialize default but the user can still change them with right-click context menu. Commenting out your old call to `ColorEditMode()` may just be fine!

Other Changes:

- Added flags to `ColorEdit3()`, `ColorEdit4()`. The color edit widget now has a context-menu and access to the color picker. (#346)
- Added flags to `ColorButton()`. (#346)
- Added `ColorPicker3()`, `ColorPicker4()`. The API along with those of the updated `ColorEdit4()` was designed so you may use them in various situation and hopefully compose your own picker if required. There are a bunch of available flags, check the Demo window and comment for `ImGuiColorEditFlags_`. Some of the options it supports are: two color picker types (hue bar + sat/val rectangle, hue wheel + rotating sat/val triangle), display as u8 or float, lifting 0.0..1.0 constraints (currently rgba only), context menus, alpha bar, background checkerboard options, preview tooltip, basic revert. For simple use, calling the existing `ColorEdit4()` function as you did before will be enough, as you can now open the color picker from there. (#346) [@r-lyeh, @nem0, @thennequin, @dariomanesku and @ocornut]
- Added `SetColorEditOptions()` to set default color options (e.g. if you want HSV over RGBA, float over u8, select a default picker mode etc. at startup time without a user intervention. Note that the user can still change options with the context menu unless disabled with `ImGuiColorFlags_NoOptions` or explicitly enforcing a display type/picker mode etc.).
- Added user-facing `IsPopupOpen()` function. (#891) [@mkeeter]
- Added `GetColorU32(u32)` variant that perform the style alpha multiply without a floating-point round trip, and helps makes code more consistent when using ImDrawList APIs.
- Added `PushStyleColor(ImGuiCol idx, ImU32 col)` overload.
- Added `GetStyleColorVec4(ImGuiCol idx)` which is equivalent to accessing `ImGui::GetStyle().Colors[idx]` (aka return the raw style color without alpha alteration).
- ImFontAtlas: Added `GlyphRangesBuilder` helper class, which makes it easier to build custom glyph ranges from your app/game localization data, or add into existing glyph ranges.
- ImFontAtlas: Added `TexGlyphPadding` option. (#1282) [@jadwallis]
- ImFontAtlas: Made it possible to override size of AddFontDefault() (even if it isn't really recommended!).
- ImDrawList: Added `GetClipRectMin()`, `GetClipRectMax()` helpers.
- Fixed Ini saving crash if the ImGuiWindowFlags_NoSavedSettings gets removed from a window after its creation (unlikely!). (#1000)
- Fixed `PushID()`/`PopID()` from marking parent window as Accessed (which needlessly woke up the root "Debug" window when used outside of a regular window). (#747)
- Fixed an assert when calling `CloseCurrentPopup()` twice in a row. [@nem0]
- Window size can be loaded from .ini data even if ImGuiWindowFlags_NoResize flag is set. (#1048, #1056)
- Columns: Added `SetColumnWidth()`. (#913) [@ggtucker]
- Columns: Dragging a column preserve its width by default. (#913) [@ggtucker]
- Columns: Fixed first column appearing wider than others. (#1266)
- Columns: Fixed allocating space on the right-most side with the assumption of a vertical scrollbar. The space is only allocated when needed. (#125, #913, #893, #1138)
- Columns: Fixed the right-most column from registering its content width to the parent window, which led to various issues when using auto-resizing window or e.g. horizontal scrolling. (#519, #125, #913)
- Columns: Refactored some of the columns code internally toward a better API (not yet exposed) + minor optimizations. (#913) [@ggtucker, @ocornut]
- Popups: Most pop-ups windows can be moved by the user after appearing (if they don't have explicit positions provided by caller, or e.g. sub-menu pop-up). The previous restriction was totally arbitrary. (#1252)
- Tooltip: `SetTooltip()` is expanded immediately into a window, honoring current font / styling setting. Add internal mechanism to override tooltips. (#862)
- PlotHistogram: bars are drawn based on zero-line, so negative values are going under. (#828)
- Scrolling: Fixed return values of `GetScrollMaxX()`, `GetScrollMaxY()` when both scrollbars were enabled. Tweak demo to display more data. (#1271) [@degracode]
- Scrolling: Fixes for Vertical Scrollbar not automatically getting enabled if enabled Horizontal Scrollbar straddle the vertical limit. (#1271, #246)
- Scrolling: `SetScrollHere()`, `SetScrollFromPosY()`: Fixed Y scroll aiming when Horizontal Scrollbar is enabled. (#665).
- [Windows] Clipboard: Fixed not closing Win32 clipboard on early open failure path. (#1264)
- Removed an unnecessary dependency on int64_t which failed on some older compilers.
- Demo: Rearranged everything under Widgets in a more consistent way.
- Demo: Columns: Added Horizontal Scrolling demo. Tweaked another Columns demo. (#519, #125, #913)
- Examples: OpenGL: Various makefiles for MINGW, Linux. (#1209, #1229, #1209) [@fr500, @acda]
- Examples: Enabled vsync by default in example applications, so it doesn't confuse people that the sample run at 2000+ fps and waste an entire CPU. (#1213, #1151).
- Various other small fixes, tweaks, comments, optimizations.


-----------------------------------------------------------------------
 VERSION 1.50 (2017-06-02)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.50

Breaking Changes:

- Added a void* user_data parameter to Clipboard function handlers. (#875)
- SameLine(x) with x>0.0f is now relative to left of column/group if any, and not always to left of window. This was sort of always the intent and hopefully breakage should be minimal.
- Renamed ImDrawList::PathFill() - rarely used directly - to ImDrawList::PathFillConvex() for clarity and consistency.
- Removed ImFontConfig::MergeGlyphCenterV in favor of a more multipurpose ImFontConfig::GlyphOffset.
- Style: style.WindowTitleAlign is now a ImVec2 (ImGuiAlign enum was removed). set to (0.5f,0.5f) for horizontal+vertical centering, (0.0f,0.0f) for upper-left, etc.
- BeginChild(const char*) now applies the stack id to the provided label, consistently with other functions as it should always have been. It shouldn't affect you unless (extremely unlikely) you were appending multiple times to a same child from different locations of the stack id. If that's the case, generate an id with GetId() and use it instead of passing string to BeginChild().

Other Changes:

- InputText(): Added support for CTRL+Backspace (delete word).
- InputText(): OSX uses Super+Arrows for home/end. Add Shortcut+Backspace support. (#650) [@michaelbartnett]
- InputText(): Got rid of individual OSX-specific options in ImGuiIO, added a single io.OSXBehaviors flag. (#473, #650)
- InputText(): Fixed pressing home key on last character when it isn't a trailing \n (#588, #815)
- InputText(): Fixed state corruption/crash bug in stb_textedit.h redo logic when exhausting undo/redo char buffer. (#715. #681)
- InputTextMultiline(): Fixed CTRL+DownArrow moving scrolling out of bounds.
- InputTextMultiline(): Scrollbar fix for when input and latched internal buffers differs in a way that affects vertical scrollbar existence. (#725)
- ImFormatString(): Fixed an overflow handling bug with implementation of vsnprintf() that do not return -1. (#793)
- BeginChild(const char*) now applies stack id to provided label, consistent with other widgets. (#894, #713)
- SameLine() with explicit X position is relative to left of group/columns. (ref #746, #125, #630)
- SliderInt(), SliderFloat() supports reverse direction (where v_min > v_max). (#854)
- SliderInt(), SliderFloat() better support for when v_min==v_max. (#919)
- SliderInt(), SliderFloat() enforces writing back value when interacting, to be consistent with other widgets. (#919)
- SliderInt, SliderFloat(): Fixed edge case where style.GrabMinSize being bigger than slider width can lead to a division by zero. (#919)
- Added IsRectVisible() variation with explicit start-end positions. (#768) [@thedmd]
- Fixed TextUnformatted() clipping bug in the large-text path when horizontal scroll has been applied. (#692, #246)
- Fixed minor text clipping issue in window title when using font straying above usual line. (#699)
- Fixed SetCursorScreenPos() fixed not adjusting CursorMaxPos as well.
- Fixed scrolling offset when using SetScrollY(), SetScrollFromPosY(), SetScrollHere() with menu bar.
- Fixed using IsItemActive() after EndGroup() or any widget using groups. (#840, #479)
- Fixed IsItemActive() lagging by one frame on initial widget activation. (#840)
- Fixed Separator() zero-height bounding box resulting in clipping when laying exactly on top line of clipping rectangle (#860)
- Fixed PlotLines() PlotHistogram() calling with values_count == 0.
- Fixed clicking on a window's void while staying still overzealously marking .ini settings as dirty. (#923)
- Fixed assert triggering when a window has zero rendering but has a callback. (#810)
- Scrollbar: Fixed rendering when sizes are negative to reduce glitches (which can happen with certain style settings and zero WindowMinSize).
- EndGroup(): Made IsItemHovered() work when an item was activated within the group. (#849)
- BulletText(): Fixed stopping to display formatted string after the '##' mark.
- Closing the focused window restore focus to the first active root window in descending z-order .(part of #727)
- Word-wrapping: Fixed a bug where we never wrapped after a 1 character word. [@sronsse]
- Word-wrapping: Fixed TextWrapped() overriding wrap position if one is already set. (#690)
- Word-wrapping: Fixed incorrect testing for negative wrap coordinates, they are perfectly legal. (#706)
- ImGuiListClipper: Fixed automatic-height calc path dumbly having user display element 0 twice. (#661, #716)
- ImGuiListClipper: Fix to behave within column. (#661, #662, #716)
- ImDrawList: Renamed ImDrawList::PathFill() to ImDrawList::PathFillConvex() for clarity. (BREAKING API)
- Columns: End() avoid calling Columns(1) if no columns set is open, not sure why it wasn't the case already (pros: faster, cons: exercise less code).
- ColorButton(): Fix ColorButton showing wrong hex value for alpha. (#1068) [@codecat]
- ColorEdit4(): better preserve inputting value out of 0..255 range, display then clamped in Hexadecimal form.
- Shutdown() clear out some remaining pointers for sanity. (#836)
- Added IMGUI_USE_BGRA_PACKED_COLOR option in imconfig.h (#767, #844) [@thedmd]
- Style: Removed the inconsistent shadow under RenderCollapseTriangle() (~#707)
- Style: Added ButtonTextAlign, ImGuiStyleVar_ButtonTextAlign. (#842)
- ImFont: Allowing to use up to 0xFFFE glyphs in same font (increased from previous 0x8000).
- ImFont: Added GetGlyphRangesThai() helper. [@nProtect]
- ImFont: CalcWordWrapPositionA() fixed font scaling with fallback character.
- ImFont: Calculate and store the approximate texture surface to get an idea of how costly each source font is.
- ImFontConfig: Added GlyphOffset to explicitly offset glyphs at font build time, useful for merged fonts. Removed MergeGlyphCenterV. (BREAKING API)
- Clarified asserts in CheckStacksSize() when there is a stack mismatch.
- Context: Support for #define-ing GImGui and IMGUI_SET_CURRENT_CONTEXT_FUNC to enable custom thread-based hackery (#586)
- Updated stb_truetype.h to 1.14 (added OTF support, removed warnings). (#883, #976)
- Updated stb_rect_pack.h to 0.10 (removed warnings). (#883)
- Added ImGuiMouseCursor_None enum value for convenient usage by app/binding.
- Clipboard: Added a void* user_data parameter to Clipboard function handlers. (#875) (BREAKING API)
- Internals: Refactor internal text alignment options to use ImVec2, removed ImGuiAlign. (#842, #222)
- Internals: Renamed ImLoadFileToMemory to ImFileLoadToMemory to be consistent with ImFileOpen + fix mismatching .h name. (#917)
- OS/Windows: Fixed Windows default clipboard handler leaving its buffer unfreed on application's exit. (#714)
- OS/Windows: No default IME handler when compiling for Windows using GCC. (#738)
- OS/Windows: Now using _wfopen() instead of fopen() to allow passing in paths/filenames with UTF-8 characters. (#917)
- Tools: binary_to_compressed_c: Avoid ?? trigraphs sequences in string outputs which break some older compilers. (#839)
- Demo: Added an extra 3-way columns demo.
- Demo: ShowStyleEditor: show font character map / grid in more details.
- Demo: Console: Fixed a completion bug when multiple candidates are equals and match until the end.
- Demo: Fixed 1-byte off overflow in the ShowStyleEditor() combo usage. (#783) [@bear24rw]
- Examples: Accessing ImVector fields directly, feel less stl-ey. (#810)
- Examples: OpenGL*: Saving/restoring existing scissor rectangle for completeness. (#807)
- Examples: OpenGL*: Saving/restoring active texture number (the value modified by glActiveTexture). (#1087, #1088, #1116)
- Examples: OpenGL*: Saving/restoring separate color/alpha blend functions correctly. (#1120) [@greggman]
- Examples: OpenGL2: Uploading font texture as RGBA32 to increase compatibility with users shaders for beginners. (#824)
- Examples: Vulkan: Countless fixes and improvements. (#785, #804, #910, #1017, #1039, #1041, #1042, #1043, #1080) [@martty, @Loftilus, @ParticlePeter, @SaschaWillems]
- Examples: DirectX9/10/10: Only call SetCursor(NULL) is io.MouseDrawCursor is set. (#585, #909)
- Examples: DirectX9: Explicitly setting viewport to match that other examples are doing. (#937)
- Examples: GLFW+OpenGL3: Fixed Shutdown() calling GL functions with NULL parameters if NewFrame was never called. (#800)
- Examples: GLFW+OpenGL2: Renaming opengl_example/ to opengl2_example/ for clarity.
- Examples: SDL+OpenGL: explicitly setting GL_UNPACK_ROW_LENGTH to reduce issues because SDL changes it. (#752)
- Examples: SDL2: Added build .bat files for Win32.
- Added various links to language/engine bindings.
- Various other minor fixes, tweaks, comments, optimizations.


-----------------------------------------------------------------------
 VERSION 1.49 (2016-05-09)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.49

Breaking Changes:

- Renamed `SetNextTreeNodeOpened()` to `SetNextTreeNodeOpen()` for consistency, no redirection.
- Removed confusing set of `GetInternalState()`, `GetInternalStateSize()`, `SetInternalState()` functions. Now using `CreateContext()`, `DestroyContext()`, `GetCurrentContext()`, `SetCurrentContext()`. If you were using multiple contexts the change should be obvious and trivial.
- Obsoleted old signature of `CollapsingHeader(const char* label, const char* str_id = NULL, bool display_frame = true, bool default_open = false)`, as extra parameters were badly designed and rarely used. Most uses were using 1 parameter and shouldn't affect you. You can replace the "default_open = true" flag in new API with `CollapsingHeader(label, ImGuiTreeNodeFlags_DefaultOpen)`.
- Changed `ImDrawList::PushClipRect(ImVec4 rect)` to `ImDraw::PushClipRect(ImVec2 min,ImVec2 max,bool intersect_with_current_clip_rect=false)`. Note that higher-level `ImGui::PushClipRect()` is preferable because it will clip at logic/widget level, whereas `ImDrawList::PushClipRect()` only affect your renderer.
- Title bar (using ImGuiCol_TitleBg/ImGuiCol_TitleBgActive colors) isn't rendered over a window background (ImGuiCol_WindowBg color) anymore (see #655). If your TitleBg/TitleBgActive alpha was 1.0f or you are using the default theme it will not affect you. However if your TitleBg/TitleBgActive alpha was <1.0f you need to tweak your custom theme to readjust for the fact that we don't draw a WindowBg background behind the title bar.
  This helper function will convert an old TitleBg/TitleBgActive color into a new one with the same visual output, given the OLD color and the OLD WindowBg color. (Or If this is confusing, just pick the RGB value from title bar from an old screenshot and apply this as TitleBg/TitleBgActive. Or you may just create TitleBgActive from a tweaked TitleBg color.)

    ImVec4 ConvertTitleBgCol(const ImVec4& win_bg_col, const ImVec4& title_bg_col)
    {
       float new_a = 1.0f - ((1.0f - win_bg_col.w) * (1.0f - title_bg_col.w));
       float k = title_bg_col.w / new_a;
       return ImVec4((win_bg_col.x * win_bg_col.w + title_bg_col.x) * k, (win_bg_col.y * win_bg_col.w + title_bg_col.y) * k, (win_bg_col.z * win_bg_col.w + title_bg_col.z) * k, new_a);
    }

Other changes:

- New version of ImGuiListClipper helper calculates item height automatically. See comments and demo code. (#662, #661, #660)
- Added SetNextWindowSizeConstraints() to enable basic min/max and programmatic size constraints on window. Added demo. (#668)
- Added PushClipRect()/PopClipRect() (previously part of imgui_internal.h). Changed ImDrawList::PushClipRect() prototype. (#610)
- Added IsRootWindowOrAnyChildHovered() helper. (#615)
- Added TreeNodeEx() functions. (#581, #600, #190)
- Added ImGuiTreeNodeFlags_Selected flag to display TreeNode as "selected". (#581, #190)
- Added ImGuiTreeNodeFlags_AllowOverlapMode flag. (#600)
- Added ImGuiTreeNodeFlags_NoTreePushOnOpen flag (#590).
- Added ImGuiTreeNodeFlags_NoAutoOpenOnLog flag (previously private).
- Added ImGuiTreeNodeFlags_DefaultOpen flag (previously private).
- Added ImGuiTreeNodeFlags_OpenOnDoubleClick flag.
- Added ImGuiTreeNodeFlags_OpenOnArrow flag.
- Added ImGuiTreeNodeFlags_Leaf flag, always opened, no arrow, for convenience. For simple use case prefer using TreeAdvanceToLabelPos()+Text().
- Added ImGuiTreeNodeFlags_Bullet flag, to add a bullet to Leaf node or replace Arrow with a bullet.
- Added TreeAdvanceToLabelPos(), GetTreeNodeToLabelSpacing() helpers. (#581, #324)
- Added CreateContext()/DestroyContext()/GetCurrentContext()/SetCurrentContext(). Obsoleted nearly identical GetInternalState()/SetInternalState() functions. (#586, #269)
- Added NewLine() to undo a SameLine() and as a shy reminder that horizontal layout support hasn't been implemented yet.
- Added IsItemClicked() helper. (#581)
- Added CollapsingHeader() variant with close button. (#600)
- Fixed MenuBar missing lower border when borders are enabled.
- InputText(): Fixed clipping of cursor rendering in case it gets out of the box (which can be forced w/ ImGuiInputTextFlags_NoHorizontalScroll. (#601)
- Style: Changed default IndentSpacing from 22 to 21. (#581, #324)
- Style: Fixed TitleBg/TitleBgActive color being rendered above WindowBg color, which was inconsistent and causing visual artifact. (#655)
  This broke the meaning of TitleBg and TitleBgActive. Only affect values where Alpha<1.0f. Fixed default theme. Read comments in "API BREAKING CHANGES" section to convert.
- Relative rendering of order of Child windows creation is preserved, to allow more control with overlapping children. (#595)
- Fixed GetWindowContentRegionMax() being off by ScrollbarSize amount when explicit SizeContents is set.
- Indent(), Unindent(): optional non-default indenting width. (#324, #581)
- Bullet(), BulletText(): Slightly bigger. Less polygons.
- ButtonBehavior(): fixed subtle old bug when a repeating button would also return true on mouse release (barely noticeable unless RepeatRate is set to be very slow). (#656)
- BeginMenu(): a menu that becomes disabled while open gets closed down, facilitate user's code. (#126)
- BeginGroup(): fixed using within Columns set. (#630)
- Fixed a lag in reading the currently hovered window when dragging a window. (#635)
- Obsoleted 4 parameters version of CollapsingHeader(). Refactored code into TreeNodeBehavior. (#600, #579)
- Scrollbar: minor fix for top-right rounding of scrollbar background when window has menu bar but no title bar.
- MenuItem(): the check mark renders in disabled color when menu item is disabled.
- Fixed clipping rectangle floating point representation to ensure renderer-side float point operations yield correct results in typical DirectX/GL settings. (#582, 597)
- Fixed GetFrontMostModalRootWindow(), fixing missing fade-out when a combo pop was used stacked over a modal window. (#604)
- ImDrawList: Added AddQuad(), AddQuadFilled() helpers.
- ImDrawList: AddText() refactor, moving some code to ImFont, reserving less unused vertices when large vertical clipping occurs.
- ImFont: Added RenderChar() helper.
- ImFont: Added AddRemapChar() helper. (#609)
- ImFontConfig: Clarified persistence requirement of GlyphRanges array. (#651)
- ImGuiStorage: Added bool helper functions for completeness.
- AddFontFromMemoryCompressedTTF(): Fix ImFontConfig propagation. (#587)
- Renamed majority of use of the word "opened" to "open" for clarity. Renamed SetNextTreeNodeOpened() to SetNextTreeNodeOpen(). (#625, #579)
- Examples: OpenGL3: Saving/restoring glActiveTexture() state. (#602)
- Examples: DirectX9: save/restore all device state.
- Examples: DirectX9: Removed dependency on d3dx9.h, d3dx9.lib, dxguid.lib so it can be used in a DirectXMath.h only environment. (#611)
- Examples: DirectX10/X11: Apply depth-stencil state (no use of depth buffer). (#640, #636)
- Examples: DirectX11/X11: Added comments on removing dependency on D3DCompiler. (#638)
- Examples: SDL: Initialize video+timer subsystem only.
- Examples: Apple/iOS: lowered XCode project deployment target from 10.7 to 10.11. (#598, #575)


-----------------------------------------------------------------------
 VERSION 1.48 (2016-04-09)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.48

Breaking Changes:

- Consistently honoring exact width passed to PushItemWidth() (when positive), previously it would add extra FramePadding.x*2 over that width. Some hand-tuned layout may be affected slightly. (#346)
- Style: removed `style.WindowFillAlphaDefault` which was confusing and redundant, baked alpha into `ImGuiCol_WindowBg` color. If you had a custom WindowBg color but didn't change WindowFillAlphaDefault, multiply WindowBg alpha component by 0.7. Renamed `ImGuiCol_TooltipBg` to `ImGuiCol_PopupBG`, applies to other types of pop-ups. `bg_alpha` parameter of 5-parameters version of Begin() is an override. (#337)
- InputText(): Added BufTextLen field in ImGuiTextEditCallbackData. Requesting user to update it if the buffer is modified in the callback. Added a temporary length-check assert to minimize panic for the 3 people using the callback. (#541)
- Renamed GetWindowFont() to GetFont(), GetWindowFontSize() to GetFontSize(). Kept inline redirection function (will obsolete). (#340)

Other Changes:

- Consistently honoring exact width passed to PushItemWidth(), previously it would add extra FramePadding.x*2 over that width. Some hand-tuned layout may be affected slightly. (#346)
- Fixed clipping of child windows within parent not taking account of child outer clipping boundaries (including scrollbar, etc.). (#506)
- TextUnformatted(): Fixed rare crash bug with large blurb of text (2k+) not finished with a '\n' and fully above the clipping Y line. (#535)
- IO: Added 'KeySuper' field to hold CMD keyboard modifiers for OS X. Updated all examples accordingly. (#473)
- Added ImGuiWindowFlags_ForceVerticalScrollbar, ImGuiWindowFlags_ForceHorizontalScrollbar flags. (#476)
- Added IM_COL32 macros to generate a U32 packed color, convenient for direct use of ImDrawList api. (#346)
- Added GetFontTexUvWhitePixel() helper, convenient for direct use of ImDrawList api.
- Selectable(): Added ImGuiSelectableFlags_AllowDoubleClick flag to allow user reacting on double-click. (@zapolnov) (#516)
- Begin(): made the close button explicitly set the boolean to false instead of toggling it. (#499)
- BeginChild()/EndChild(): fixed incorrect layout to allow widgets submitted after an auto-fitted child window. (#540)
- BeginChild(): Added ImGuiWindowFlags_AlwaysUseWindowPadding flag to ensure non-bordered child window uses window padding. (#462)
- Fixed InputTextMultiLine(), ListBox(), BeginChildFrame(), ProgressBar(): outer frame not honoring bordering. (#462, #503)
- Fixed Image(), ImageButtion() rendering a rectangle 1 px too large on each axis. (#457)
- SetItemAllowOverlap(): Promoted from imgui_internal.h to public imgui.h api. (#517)
- Combo(): Right-most button stays highlighted when pop-up is open.
- Combo(): Display pop-up above if there's isn't enough space below / or select largest side. (#505)
- DragFloat(), SliderFloat(), InputFloat(): fixed cases of erroneously returning true repeatedly after a text input modification (e.g. "0.0" --> "0.000" would keep returning true). (#564)
- DragFloat(): Always apply value when mouse is held/widget active, so that an always-reseting variable (e.g. non saved local) can be passed.
- InputText(): OS X friendly behaviors: Word movement uses ALT key; Shortcuts uses CMD key; Double-clicking text select a single word; Jumping to next word sets cursor to end of current word instead of beginning of current word. (@zhiayang), (#473)
- InputText(): Added BufTextLen in ImGuiTextEditCallbackData. Requesting user to maintain it if buffer is modified. Zero-ing structure properly before use. (#541)
- CheckboxFlags(): Added support for testing/setting multiple flags at the same time. (@DMartinek) (#555)
- TreeNode(), CollapsingHeader() fixed not being able to use "##" sequence in a formatted label.
- ColorEdit4(): Empty label doesn't add InnerSpacing.x, matching behavior of other widgets. (#346)
- ColorEdit4(): Removed unnecessary calls to scanf() when idle in hexadecimal edit mode.
- BeginPopupContextItem(), BeginPopupContextWindow(): added early out optimization.
- CaptureKeyboardFromApp() / CaptureMouseFromApp(): added argument to allow clearing the capture flag. (#533)
- ImDrawList: Fixed index-overflow check broken by AddText() casting current index back to ImDrawIdx. (#514)
- ImDrawList: Fixed incorrect removal of trailing draw command if it is a callback command.
- ImDrawList: Allow windows with only a callback only to be functional. (#524)
- ImDrawList: Fixed ImDrawList::AddRect() which used to render a rectangle 1 px too large on each axis. (#457)
- ImDrawList: Fixed ImDrawList::AddCircle() to fit precisely within bounding box like AddCircleFilled() and AddRectFilled(). (#457)
- ImDrawList: AddCircle(), AddRect() takes optional thickness parameter.
- ImDrawList: Added AddTriangle().
- ImDrawList: Added PrimQuadUV() helper to ease custom rendering of textured quads (require primitive reserve).
- ImDrawList: Allow AddText(ImFont\* font, float font_size, ...) variant to take NULL/0.0f as default.
- ImFontAtlas: heuristic increase default texture width up for large number of glyphs. (#491)
- ImTextBuffer: Fixed empty() helper which was utterly broken.
- Metrics: allow to inspect individual triangles in draw calls.
- Demo: added more draw primitives in the Custom Rendering example. (#457)
- Demo: extra comments and example for PushItemWidth(-1) patterns.
- Demo: InputText password demo filters out blanks. (#515)
- Demo: Fixed malloc/free mismatch and leak when destructing demo console, if it has been used. (@fungos) (#536)
- Demo: plot code doesn't use ImVector to avoid heap allocation and be more friendly to custom allocator users. (#538)
- Fixed compilation on DragonFly BSD (@mneumann) (#563)
- Examples: Vulkan: Added a Vulkan example (@Loftilus) (#549)
- Examples: DX10, DX11: Saving/restoring most device state so dropping render function in your codebase shouldn't have DX device side-effects. (#570)
- Examples: DX10, DX11: Fixed ImGui_ImplDX??_NewFrame() from recreating device objects if render isn't called (g_pVB not set).
- Examples: OpenGL3: Fix BindVertexArray/BindBuffer order. (@nlguillemot) (#527)
- Examples: OpenGL: skip rendering and calling glViewport() if we have zero-fixed buffer. (#486)
- Examples: SDL2+OpenGL3: Fix context creation options. Made ImGui_ImplSdlGL3_NewFrame() signature match GL2 one. (#468, #463)
- Examples: SDL2+OpenGL2/3: Fix for high-dpi displays. (@nickgravelyn)
- Various extra comments and clarification in the code.
- Various other fixes and optimizations.


-----------------------------------------------------------------------
 VERSION 1.47 (2015-12-25)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.47

Changes:

- Rebranding "ImGui" -> "dear imgui" as an optional first name to reduce ambiguity with IMGUI term. (#21)
- Added ProgressBar(). (#333)
- InputText(): Added ImGuiInputTextFlags_Password mode: hide display, disable logging/copying to clipboard. (#237, #363, #374)
- Added GetColorU32() helper to retrieve color given enum with global alpha and extra applied.
- Added ImGuiIO::ClearInputCharacters() superfluous helper.
- Fixed ImDrawList draw command merging bug where using PopClipRect() along with PushTextureID()/PopTextureID() functions
  would occasionally restore an incorrect clipping rectangle.
- Fixed ImDrawList draw command merging so PushTextureID(XXX)/PopTextureID()/PushTextureID(XXX) sequence are now properly merged.
- Fixed large popups positioning issues when their contents on either axis is larger than DisplaySize,
  and WindowPadding < DisplaySafeAreaPadding.
- Fixed border rendering in various situations when using non-pixel aligned glyphs.
- Fixed border rendering of windows to always contain the border within the window.
- Fixed Shutdown() leaking font atlas data if NewFrame() was never called. (#396, #303)
- Fixed int>void\* warnings for 64-bit architectures with fancy warnings enabled.
- Renamed the dubious Color() helpers to ValueColor() - dangerously named, rarely used and probably to be made obsolete.
- InputText(): Fixed and better handling of using keyboard while mouse button if being held and dragging. (#429)
- InputText(): Replace OS IME (Input Method Editor) cursor on top-left when we are not text editing.
- TreeNode(), CollapsingHeader(), Bullet(), BulletText(): various sizing and layout fixes to better support laying out
  multiple item with different height on same line. (#414, #282)
- Begin(): Initial window creation with ImGuiWindowFlags_NoBringToFrontOnFocus flag pushes it at the front of global window list.
- BeginPopupContextWindow() and BeginPopupContextVoid() reopen window on subsequent click. (#439)
- ColorEdit4(): Fixed broken tooltip on hovering the color button. (actually fixes #373, #380)
- ImageButton(): uses FrameRounding up to a maximum of available framing size. (#394)
- Columns: Fixed bug with indentation within columns, also making code a bit shorter/faster. (#414, #125)
- Columns: Columns set with no implicit id include the columns count within the id to reduce collisions. (#125)
- Columns: Removed one unnecessary allocation when columns are not used by a window. (#125)
- ImFontAtlas: Tweaked GetGlyphRangesJapanese() so it is easier to modify.
- ImFontAtlas: Updated stb_rect_pack.h to 0.08.
- Metrics: Fixed computing ImDrawCmd bounding box when the draw buffer have been unindexed.
- Demo: Added a simple "Property Editor" demo applet. (#125, #414)
- Demo: Fixed assertion in "Custom Rendering" demo when holding both mouse buttons. (#393)
- Demo: Lots of extra comments, fixes.
- Demo: Tweaks to Style Editor.
- Examples: Not clearing input data/tex data in atlas (will be required for dynamic atlas anyway).
- Examples: Added /Zi (output debug information) to Win32 batch files.
- Examples: Various fixes for resizing window and recreating graphic context.
- Examples: OpenGL2/3: Save/restore viewport as part of default render function. (#392, #441).
- Examples; OpenGL3: Fixed gl3w.c for Linux when compiled with a C++ compiler. (#411)
- Examples: DirectX: Removed assumption about Unicode build in example main.cpp. (#399)
- Examples: DirectX10: Added DirectX10 example. (#424)
- Examples: DirectX11: Downgraded requirement from shader model 5.0 to 4.0. (#420)
- Examples: DirectX11: Removed Debug flag from graphics context. (#415)
- Examples: Added SDL+OpenGL3 example. (#356)


-----------------------------------------------------------------------
 VERSION 1.46 (2015-10-18)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.46

Changes:

- Begin*(): added ImGuiWindowFlags_NoFocusOnAppearing flag. (#314)
- Begin*(): added ImGuiWindowFlags_NoBringToFrontOnFocus flag.
- Added GetDrawData() alternative to setting a Render function pointer in ImGuiIO structure.
- Added SetClipboardText(), GetClipboardText() helper shortcuts that user code can call directly without reading
  from the ImGuiIO structure (to match MemAlloc/MemFree)
- Fixed handling of malformed UTF-8 at the end of a non-zero terminated string range.
- Fixed mouse click detection when passing DeltaTime 0.0. (#338)
- Fixed IsKeyReleased() and IsMouseReleased() returning true on the first frame.
- Fixed using SetNextWindow\* functions on Modal windows with a ImGuiSetCond_Appearing condition. (#377)
- IsMouseHoveringRect(): Added 'bool clip' parameter to disable clipping provided rectangle. (#316)
- InputText(): added ImGuiInputTextFlags_ReadOnly flag. (#211)
- InputText(): lose cursor/undo-stack when reactivating focus is buffer has changed size.
- InputText(): fixed ignoring text inputs when ALT or ALTGR are pressed. (#334)
- InputText(): fixed mouse-dragging not tracking the cursor when text doesn't fit. (#339)
- InputText(): fixed cursor pixel-perfect alignment when horizontally scrolling.
- InputText(): fixed crash when passing a buf_size==0 (which can be of use for read-only selectable text boxes). (#360)
- InputFloat() fixed explicit precision modifier, both display and input were broken.
- PlotHistogram(): improved rendering of histogram with a lot of values.
- Dummy(): creates an item so functions such as IsItemHovered() can be used.
- BeginChildFrame() helper: added the extra_flags parameter.
- Scrollbar: fixed rounding of background + child window consistenly have ChildWindowBg color under ScrollbarBg fill. (#355).
- Scrollbar: background color less translucent in default style so it works better when changing background color.
- Scrollbar: fixed minor rendering offset when borders are enabled. (#365)
- ImDrawList: fixed 1 leak per ImDrawList using the ChannelsSplit() API (via Columns). (#318)
- ImDrawList: fixed rectangle rendering glitches with width/height <= 1/2 and rounding enabled.
- ImDrawList: AddImage() uv parameters default to (0,0) and (1,1).
- ImFontAtlas: Added TexDesiredWidth and tweaked default cheapo best-width choice. (#327)
- ImFontAtlas: Added GetGlyphRangesKorean() helper to retrieve unicode ranges for Korean. (#348)
- ImGuiTextFilter::Draw() helper return bool and build when filter is modified.
- ImGuiTextBuffer: added c_str() helper.
- ColorEdit4(): fixed hovering the color button always showing 1.0 alpha. (#373)
- ColorConvertFloat4ToU32() round the floats instead of truncating them.
- Window: Fixed window lower-right clipping limit so it plays more friendly with both OpenGL and DirectX coordinates.
- Internal: Extracted a EndFrame() function out of Render() but kept it internal/private + clarified some asserts. (#335)
- Internal: Added missing IMGUI_API definitions in imgui_internal.h (#326)
- Internal: ImLoadFileToMemory() return void\* instead of taking void*\* + allow optional int\* file_size.
- Demo: Horizontal scrollbar demo allows to enable simultanaeous scrollbars on both axises.
- Tools: binary_to_compressed_c.cpp: added -nocompress option.
- Examples: Added example for the Marmalade platform.
- Examples: Added batch files to build Windows examples with VS.
- Examples: OpenGL3: Saving/restoring more GL state correctly. (#347)
- Examples: OpenGL2/3: Added msys2/mingw64 target to Makefiles.


-----------------------------------------------------------------------
 VERSION 1.45 (2015-09-01)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.45

Breaking Changes:

- With the addition of better horizontal scrolling primitives I had to make some consistency fixes.
  `GetCursorPos()` `SetCursorPos()` `GetContentRegionMax()` `GetWindowContentRegionMin()` `GetWindowContentRegionMax()`
  are now incorporating the scrolling amount. They were incorrectly not incorporating this amount previously.
  It PROBABLY shouldn't break anything, but that depends on how you used them. Namely:
  - If you always used SetCursorPos() with values relative to GetCursorPos() there shouldn't be a problem.
    However if you used absolute coordinates, note that SetCursorPosY(100.0f) will put you at +100 from the initial Y position (which may be scrolled out of the view), NOT at +100 from the window top border. Since there wasn't any official scrolling value on X axis (past just manually moving the cursor) this can only affect you if you used to set absolute coordinates on the Y axis which is hopefully rare/unlikely, and trivial to fix.
  - The value of GetWindowContentRegionMax() isn't necessarily close to GetWindowWidth() if horizontally scrolling.
    Previously they were roughly interchangeable (roughly because the content region exclude window padding).

Other Changes:

- Added Horizontal Scrollbar via ImGuiWindowFlags_HorizontalScroll (#246).
- Added GetScrollX(), GetScrollX(), GetScrollMaxX() apis (#246).
- Added SetNextWindowContentSize(), SetNextWindowContentWidth() to explicitly set the content size of a window, which
  define the range of scrollbar. When set explicitly it also define the base value from which widget width are derived.
- Added IO.WantTextInput telling when ImGui is expecting text input, so that e.g. OS on-screen keyboard can be enabled.
- Added printf attribute to printf-like text formatting functions (Clang/GCC).
- Added GetMousePosOnOpeningCurrentPopup() helper.
- Added GetContentRegionAvailWidth() helper.
- Malformed UTF-8 data don't terminate string, output 0xFFFD instead (#307).
- ImDrawList: Added AddBezierCurve(), PathBezierCurveTo() API for cubic bezier curves (#311).
- ImDrawList: Allow to override ImDrawIdx type (#292).
- ImDrawList: Added an assert on overflowing index value (#292).
- ImDrawList: Fixed issues with channels split/merge. Now functional without manually adding a draw cmd. Added comments.
- ImDrawData: Added ScaleClipRects() helper useful when rendering scaled. (#287).
- Fixed Bullet() inconsistent layout behaviour when clipped.
- Fixed IsWindowHovered() not taking account of window hoverability (may be disabled because of a popup).
- Fixed InvisibleButton() not honoring negative size consistently with other widgets that do so.
- Fixed OpenPopup() accessing current window, effectively opening "Debug" when called from an empty window stack.
- TreeNode(): Fixed IsItemHovered() result being inconsistent with interaction visuals (#282).
- TreeNode(): Fixed mouse interaction padding past the node label being accounted for in layout (#282).
- BeginChild(): Passing a ImGuiWindowFlags_NoMove inhibits moving parent window from this child.
- BeginChild() fixed missing rounding for child sizes which leaked into layout and have items misaligned.
- Begin(): Removed default name = "Debug" parameter. We already have a "Debug" window pushed to the stack in the first place so it's not really a useful default.
- Begin(): Minor fixes with windows main clipping rectangle (e.g. child window with border).
- Begin(): Window flags are only read on the first call of the frame. Subsequent calls ignore flags, which allows appending to a window without worryin about flags.
- InputText(): ignore character input when ctrl/alt are held. (Normally those text input are ignored by most wrappers.) (#279).
- Demo: Fixed incorrectly formed string passed to Combo (#298).
- Demo: Added simple Log demo.
- Demo: Added horizontal scrolling example + enabled in console, log and child examples (#246).
- Style: made scrollbars rounded by default. Because nice. Minor menu bar background alpha tweak. (#246)
- Metrics: display indices along with triangles count (#299) and some internal state.
- ImGuiTextFilter::PassFilter() supports string range. Added [] helper to ImGuiTextBuffer.
- ImGuiTextFilter::Draw() default parameter width=0.0f for no override, allow override with negative values.
- Examples: OpenGL2/OpenGL3: fix for retina displays. Default font current lack crispness.
- Examples: OpenGL2/OpenGL3: save/restore more GL state correctly.
- Examples: DirectX9/DirectX11: resizing buffers dynamically (#299).
- Examples: DirectX9/DirectX11: added missing middle mouse button to Windows event handler.
- Examples: DirectX11: fix for Visual Studio 2015 presumably shipping with an updated version of DX11.
- Examples: iOS: fixed missing files in project.


-----------------------------------------------------------------------
 VERSION 1.44 (2015-08-08)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.44

Breaking Changes:

- imgui.cpp has been split intro extra files: imgui_demo.cpp, imgui_draw.cpp, imgui_internal.h.
  Add the two extra .cpp to your project or #include them from another .cpp file. (#219)

Other Changes:

- Internal data structure and several useful functions are now exposed in imgui_internal.h. This should make it easier
  and more natural to extend ImGui. However please note that none of the content in imgui_internal.h is guaranteed
  for forward-compatibility and code using those types/functions may occasionally break. (#219)
- All sample code is in imgui_demo.cpp. Please keep this file in your project and consider allowing your code to call
  the ShowTestWindow() function as de-facto guide to ImGui features. It will be stripped out by the linker when unused.
- Added GetContentRegionAvail() helper (basically GetContentRegionMax() - GetCursorPos()).
- Added ImGuiWindowFlags_NoInputs for totally input-passthru window.
- Button(): honor negative size consistently with other widgets that do so (width -100 to align the button 100 pixels
  before the right-most position of the contents region).
- InputTextMultiline(): honor negative size consistently with other widgets that do so.
- Combo() clamp popup to lower edge of visible area.
- InputInt(): value doesn't pass through an int>float>int casting chain, fix handling lost of precision with "large" integer.
- InputInt() allow hexadecimal input (awkwardly via ImGuiInputTextFlags_CharsHexadecimal but we will allow format
  string in InputInt* later).
- Checkbox(), RadioButton(): fixed scaling of checkbox and radio button for the filling of "active" visual.
- Columns: never assume horizontal space for scrollbar if NoScrollbar flag is explicitly set.
- Slider: fixed using FramePadding between frame and grab visual. Scaling that spacing would look odd.
- Fixed lower-right resize grip hit box not scaling along with its rendered size (#287)
- ImDrawList: Fixed angles in ImDrawList::PathArcTo(), PathArcToFast() (v1.43) being off by an extra PI for no reason.
- ImDrawList: Added ImDrawList::AddText() shorthand helper.
- ImDrawList: Add missing support for anti-aliased thick-lines (#133, also ref #288)
- ImFontAtlas: Added AddFontFromMemoryCompressedBase85TTF() to load base85 encoded font string. Default font encoded
  as base85 saves ~100 lines / 26 KB of source code. Added base85 output to the binary_to_compressed_c tool.
- Build fix for MinGW (#276).
- Examples: OpenGL3: Fixed running on script core profiles for OSX (#277).
- Examples: OpenGL3: Simplified code using glBufferData for vertices as well (#277, #278)
- Examples: DirectX11: Clear font texture view to ensure Release() doesn't get called twice (#290).
- Updated to stb_truetype 1.07 (back to vanilla version as our minor changes are now in master & fix unlikely assert
  with odd fonts (#280)


-----------------------------------------------------------------------
 VERSION 1.43 (2015-07-17)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.43

Breaking Changes:

- This is a rather important release and we unfortunately had to break the rendering API.
  ImGui now requires you to render indexed vertices instead of non-indexed ones. The fix should be very easy.
  Sorry for that! This change is saving a fair amount of CPU/GPU and enables us to get anti-aliasing for a marginal cost.
  Each ImDrawList now contains both a vertex buffer and an index buffer. For each command, render ElemCount/3 triangles
  using indices from the index buffer.
- If you are using a vanilla copy of one of the imgui_impl_XXXX.cpp provided in the example, you just need to update
  your copy and you can ignore the rest.
- The signature of the io.RenderDrawListsFn handler has changed
  From:  ImGui_XXXX_RenderDrawLists(ImDrawList** const cmd_lists, int cmd_lists_count)
  To:    ImGui_XXXX_RenderDrawLists(ImDrawData* draw_data)
  With:  argument   'cmd_lists'        -> 'draw_data->CmdLists'
         argument   'cmd_lists_count'  -> 'draw_data->CmdListsCount'
         ImDrawList 'commands'         -> 'CmdBuffer'
         ImDrawList 'vtx_buffer'       -> 'VtxBuffer'
         ImDrawList  n/a               -> 'IdxBuffer' (new)
         ImDrawCmd  'vtx_count'        -> 'ElemCount'
         ImDrawCmd  'clip_rect'        -> 'ClipRect'
         ImDrawCmd  'user_callback'    -> 'UserCallback'
         ImDrawCmd  'texture_id'       -> 'TextureId'
- If you REALLY cannot render indexed primitives, you can call the draw_data->DeIndexAllBuffers() method to de-index
  the buffers. This is slow and a waste of CPU/GPU. Prefer using indexed rendering!
  Refer to code in the examples/ folder or ask on the GitHub if you are unsure of how to upgrade. Please upgrade!

Other Changes:

- Added anti-aliasing on lines and shapes based on primitives by @MikkoMononen (#133).
  Between the use of indexed-rendering and the fact that the entire rendering codebase has been optimized and massaged
  enough, with anti-aliasing enabled ImGui 1.43 is now running FASTER than 1.41.
  Made some extra effort in making the code run faster in your typical Debug build.
- Anti-aliasing can be disabled in the ImGuiStyle structure via the AntiAliasedLines/AntiAliasedShapes fields for further gains.
- ImDrawList: Added AddPolyline(), AddConvexPolyFilled() with optional anti-aliasing.
- ImDrawList: Added stateful path building and stroking API. PathLineTo(), PathArcTo(), PathRect(), PathFill(), PathStroke()
  with optional anti-aliasing.
- ImDrawList: Added AddRectFilledMultiColor() helper.
- ImDrawList: Added multi-channel rendering so out of order elements can be rendered in separate channels and then merged
  back together (used by columns).
- ImDrawList: Fixed merging draw commands when equal clip rectangles are in the two first commands.
- ImDrawList: Fixed window draw lists not destructed properly on Shutdown().
- ImDrawData: Added DeIndexAllBuffers() helper.
- Added lots of new font options ImFontAtlas::AddFont() and the new ImFontConfig structure.
  - Added support for oversampling (ImFontConfig: OversampleH, OversampleV) and sub-pixel positioning (ImFontConfig: PixelSnapH).
    Oversampling allows sub-pixel positioning but can also be used as a way to get some leeway with scaling fonts without re-rasterizing.
  - Added GlyphExtraSpacing option to add extra horizontal spacing between characters (#242).
  - Added MergeMode option to merge glyphs from different font inputs into a same font (#182, #232).
  - Added FontDataOwnedByAtlas option to keep ownership from the TTF data buffer and request the atlas to make a copy (#220).
- Updated to stb_truetype 1.06 (+ minor mods) with better font rasterization.
- InputText: Added ImGuiInputTextFlags_NoHorizontalScroll flag.
- InputText: Added ImGuiInputTextFlags_AlwaysInsertMode flag.
- InputText: Added HasSelection() helper in ImGuiTextEditCallbackData as a clarification.
- InputText: Fix for using END key on a multi-line text editor (#275)
- Columns: Dispatch render of each column in a sub-draw list and merge on closure, saving a lot of draw calls! (#125)
- Popups: Fixed Combo boxes inside menus. (#272)
- Style: Added GrabRounding setting to make the sliders etc. grabs rounded.
- Changed SameLine() parameters from int to float.
- Fixed incorrect assert triggering when code stole ActiveID from user moving a window by calling e.g. SetKeyboardFocusHere().
- Fixed CollapsingHeader() label rendering outside its frame in columns context where ClipRect max isn't aligned with the
  right-side of the header.
- Metrics window: calculate bounding box of actual vertices when hovering a draw list.
- Examples: Showing more information in the Fonts section.
- Examples: Added a gratuitous About window.
- Examples: Updated all examples code (OpenGL/DX9/DX11/SDL/Allegro/iOS) to use indexed rendering.
- Examples: Fixed the SDL2 example to support Unicode text input (#274).


-----------------------------------------------------------------------
 VERSION 1.42 (2015-07-08)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.42

Breaking Changes:

- Renamed SetScrollPosHere() to SetScrollHere(). Kept inline redirection function (will obsolete).
- Renamed GetScrollPosY() to GetScrollY(). Necessary to reduce confusion and make scrolling API consistent,
  because positions (e.g. cursor position) are not equivalent to scrolling amount.
- Removed obsolete GetDefaultFontData() function that would assert anyway.
  If you are updating from <1.30 you'll get a compile error instead of an assertion. (obsoleted 2015/01/11)

Other Changes:

- Added SDL2 example application (courtesy of @CedricGuillemet)
- Added iOS example application (courtesy of @joeld42)
- Added Allegro 5 example application (courtesy of @bggd)
- Added TitleBgActive color in style so focused window is made visible. (#253)
- Added CaptureKeyboardFromApp() / CaptureMouseFromApp() to manually enforce inputs capturing.
- Added DragFloatRange2() DragIntRange2() helpers. (#76)
- Added a Y centering ratio to SetScrollFromCursorPos() which can be used to aim the top or bottom of the window. (#150)
- Added SetScrollY(), SetScrollFromPos(), GetCursorStartPos() for manual scrolling manipulations. (#150).
- Added GetKeyIndex() helper for converting from ImGuiKey_\* enum to user's keycodes. Basically pulls from io.KeysMap[].
- Added missing ImGuiKey_PageUp, ImGuiKey_PageDown so more UI code can be written without referring to implementation-side keycodes.
- MenuItem() can be activated on release. (#245)
- Allowing NewFrame() with DeltaTime==0.0f to not assert.
- Fixed IsMouseDragging(). (#260)
- Fixed PlotLines(), PlotHistogram() using incorrect hovering test so they would show their tooltip even when there is
  a popup between mouse and the graph.
- Fixed window padding being reported incorrectly for child windows with borders when parent have no borders.
- Fixed a bug with TextUnformatted() clipping of long text blob when clipping y1 line sits on the first line of text. (#257)
- Fixed text baseline alignment of small button (no padding) after regular buttons.
- Fixed ListBoxHeader() not honoring negative sizes the same way as BeginChild() or BeginChildFrame(). (#263)
- Fixed warnings for more pedantic compiler settings (#258).
- ImVector<> cannot be re-defined anymore, cannot be replaced with std::vector<>. Allowed us to clean up and optimize
  lots of code. Yeah! (#262)
- ImDrawList: store pointer to their owner name for easier auditing/debugging.
- Examples: added scroll tracking example with SetScrollFromCursorPos().
- Examples: metrics windows render clip rectangle when hovering over a draw call.
- Lots of small optimization (particularly to run faster on unoptimized builds) and tidying up.
- Added font links in extra_fonts/ + instructions for using compressed fonts in C array.


-----------------------------------------------------------------------
 VERSION 1.41 (2015-06-26)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.41

Breaking Changes:

- Changed ImageButton() default bg_col parameter from (0,0,0,1) (black) to (0,0,0,0) (transparent).
  Only makes a difference when texture have transparency.
- Changed Selectable() API from (label, selected, size) to (label, selected, flags, size).
  Size override should be used very rarely so hopefully it doesn't affect many people. Sorry!

Other Changes:

- Added InputTextMultiline() multi-line text editor, vertical scrolling, selection, optimized enough to handle rather
  big chunks of text in stateless context (thousands of lines are ok), option for allowing Tab to be input, option
  for validating with Return or Ctrl+Return (#200).
- Added modal window API, BeginPopupModal(), follows the popup api scheme. Modal windows can be closed by clicking
  outside. By default the rest of the screen is dimmed (using ImGuiCol_ModalWindowDarkening). Modal windows can be stacked.
- Added GetGlyphRangesCyrillic() helper (#237).
- Added SetNextWindowPosCenter() to center a window prior to knowing its size. (#249)
- Added IsWindowHovered() helper.
- Added IsMouseReleased(), IsKeyReleased() helpers to allow to user to avoid tracking them. (#248)
- Allow Set*WindowSize() calls to be used with popups.
- Window: AutoFit can be triggered on each axis separately via SetNextWindowSize(), etc.
- Window: fixed scrolling with mouse wheel while window was collapsed.
- Window: fixed mouse wheel scroll issues.
- DragFloat(), SliderFloat(): Fixed rounding of negative numbers which sometime made the negative lower bound unreachable.
- InputText(): lifted character count limit.
- InputText(): fixes in case of using per-window font scaling.
- Selectable(), MenuItem(): do not use frame rounding for hovering/selection.
- Selectable(): Added flag ImGuiSelectableFlags_DontClosePopups.
- Selectable(): Added flag ImGuiSelectableFlags_SpanAllColumns (#125).
- Combo(): Fixed issue with activating a Combo() not taking active id (#241).
- ColorButton(), ColorEdit4(): fix to ensure that the colored square stays square when non-default padding settings are used.
- BeginChildFrame(): returns bool like BeginChild() for clipping.
- SetScrollPosHere(): takes account of item height + more accurate centering + fixed precision issue.
- ImFont: ignoring '\r'.
- ImFont: added GetCharAdvance() helper. Exposed font Ascent and font Descent.
- ImFont: additional rendering optimizations.
- Metrics windows display storage size.


-----------------------------------------------------------------------
 VERSION 1.40 (2015-05-31)
-----------------------------------------------------------------------

Decorated log: https://github.com/ocornut/imgui/releases/tag/v1.40

Breaking Changes:

- The BeginPopup() API (introduced in 1.37) had to be changed to allow for stacked popups and menus.
  Use OpenPopup() to toggle the opened state and BeginPopup() to append.**
- The third parameter of Button(), 'repeat_if_held' has been removed. While it's been very rarely used,
  some code will possibly break if you didn't rely on the default parameter.
  Use PushButtonRepeat()/PopButtonRepeat() to configure repeat.
- Renamed IsRectClipped() to !IsRectVisible() for consistency (opposite return value!). Kept inline redirection function (will obsolete)
- Renamed GetWindowCollapsed() to IsWindowCollapsed() for consistency. Kept inline indirection function (will obsolete).

Other Changes:

- Menus: Added a menu system! Menus are typically populated with menu items and sub-menus, but you can add any sort of
  widgets in them (buttons, text inputs, sliders, etc.). (#126)
- Menus: Added MenuItem() to append a menu item. Optional shortcut display, acts a button & toggle with checked/unchecked state,
  disabled mode. Menu items can be used in any window.
- Menus: Added BeginMenu() to append a sub-menu. Note that you generally want to add sub-menu inside a popup or a menu-bar.
  They will work inside a normal window but it will be a bit unusual.
- Menus: Added BeginMenuBar() to append to window menu-bar (set ImGuiWindowFlags_MenuBar to enable).
- Menus: Added BeginMainMenuBar() helper to append to a fullscreen main menu-bar.
- Popups: Support for stacked popups. Each popup level inhibit inputs to lower levels. The menus system is based on this. (#126).
- Popups: Added BeginPopupContextItem(), BeginPopupContextWindow(), BeginPopupContextVoid() to create a popup window on mouse-click.
- Popups: Popups have borders by default (#197), attenuated border alpha in default theme.
- Popups & Tooltip: Fit within display. Handling various positioning/sizing/scrolling edge cases. Better hysteresis when moving
  in corners. Tooltip always tries to stay away from mouse-cursor.
- Added ImGuiStorage::GetVoidPtrRef() for manipulating stored void*.
- Added IsKeyDown() IsMouseDown() as convenience and for consistency with existing functions (instead of reading them from IO structures).
- Added Dummy() helper to advance layout by a given size. Unlike InvisibleButton() this doesn't catch any click.
- Added configurable io.KeyRepeatDelay, io.KeyRepeatRate keyboard and mouse repeat rate.
- Added PushButtonRepeat() / PopButtonRepeat() to enable hold-button-to-repeat press on any button.
- Removed the third 'repeat' parameter of Button().
- Added IsAnyItemHovered() helper.
- Added GetItemsLineHeightWithSpacing() helper.
- Added ImGuiListClipper helper for clipping large list of evenly sized items, to avoid using CalcListClipping() directly.
- Separator: within group start on group horizontal offset. (#205)
- InputText: Fixed incorrect edit state after text buffer is appended to by user via the callback. (#206)
- InputText: CTRL+letter-key shortcuts (e.g. CTRL+C/V/X) makes sure only CTRL is pressed. (#214)
- InputText: Fixed cursor generating a zero-width wire-frame rectangle turning into a division by zero (would go unnoticed
  unless you trapped exceptions).
- InputFloatN/InputIntN: Flags parameter added to match scalar versions. (#218)
- Selectable: Horizontal filling not declared to ItemSize() so Selectable(),SameLine() works and we can better auto-fit the window.
- Selectable: Handling text baseline alignment for line that aren't of text height.
- Combo: Empty label doesn't add ItemInnerSpacing alignment, matching other widgets.
- EndGroup: Carries the text base offset from the last line of the group (sort of incorrect but better than nothing,
  should use the first line of the group, will implement in the future).
- Columns: distinguish columns-set ID from other widgets as a convenience, added asserts and sailors.
- ListBox: ListBox() function only use public API to encourage creating custom versions. ListBoxHeader() can return false.
- ListBox: Uses ImGuiListClipper and assume items of matching height, so large lists can be handled.
- Plot: overlay label clipped within frame when not fitting.
- Window: Added ImGuiSetCond_Appearing to test the hidden->visible transition in SetWindow***/SetNextWindow*** functions.
- Window: Auto-fitting cancel out one worth of vertical spacing for vertical symmetry (like what group and tooltip do).
- Window: Default item width for auto-resizing windows expressed as a factor of font height, scales better with different font.
- Window: Fixed auto-fit calculation mismatch of whether a scrollbar will be added by maximum height clamping. Also honor NoScrollBar in the case of height clamping, not adding extra horizontal space.
- Window: Hovering require to hover same child window. Reverted 860cf57 (December 3). Might break something if you have
  child overlapping items in parent window.
- Window: Fixed appending multiple times to an existing child via multiple BeginChild/EndChild calls to same child name.
  Allows a simple form of out-of-order appending.
- Window: Fixed auto-filling child window using WindowMinSize at their minimum size, irrelevant.
- Metrics: Added io.MetricsActiveWindows counter. (#213.
- Metrics: Added io.MetricsAllocs counter (number of active memory allocations).
- Metrics: ShowMetricsWindow() shows popups stack, allocations.
- Style: Added style.DisplayWindowPadding to prevent windows from reaching edges of display (similar to style.DisplaySafeAreaPadding which is still in effect and also affect popups/tooltips).
- Style: Removed style.AutoFitPadding, using style.WindowPadding makes more sense (the default values were already the same).
- Style: Added style.ScrollbarRounding. (#212)
- Style: Added ImGuiCol_TextDisabled for disabled text. Added TextDisabled() helper.
- Style: Added style.WindowTitleAlign alignment options, to e.g. center title on windows. (#222)
- ImVector: tweak growth strategy, matches vector from VS2010.
- ImFontAtlas: Added ClearFonts(), making the different clear funcs more explicit. (#224)
- ImFontAtlas: Fixed appending new fonts without clearing existing fonts. Clearing input data left to application. (#224)
- ImDrawList: Merge draw command better, cases of multiple Begin/End gets merged properly.
- Store common stacked settings contiguously in memory to avoid heap allocation for unused features, and reduce cache misses.
- Shutdown() tests for g.IO.Fonts not being NULL to ease use of multiple ImGui contexts. (#207)
- Added IMGUI_DISABLE_OBSOLETE_FUNCTIONS define to disable the functions that are meant to be removed.
- Examples: Added ? marks with tooltips next to various widgets. Added more comments in the demo window.
- Examples: Added Menu-bar example.
- Examples: Added Simple Layout example.
- Examples: AutoResize demo doesn't use TextWrapped().
- Examples: Console example uses standard malloc/free, makes more sense as a copy & pastable example.
- Examples: DirectX9/11: Fixed key mapping for down arrow.
- Examples: DirectX9/11: hide OS cursor if ImGui is drawing it. (#155)
- Examples: DirectX11: explicitly set rasterizer state.
- Examples: OpenGL3: Add conditional compilation of forward compat as required by glfw on OSX. (#229)
- Fixed build with Visual Studio 2008 (possibly earlier versions as well).
- Other fixes, comments, tweaks.


-----------------------------------------------------------------------

For older version, see https://github.com/ocornut/imgui/releases

# FAQ (Frequenty Asked Questions)

You may link to this document using short form:
  https://www.dearimgui.org/faq
or its real address:
  https://github.com/ocornut/imgui/blob/master/docs/FAQ.md
or view this file with any Markdown viewer.


## Index

| **Q&A: Basics** |
:---------------------------------------------------------- |
| [Where is the documentation?](#q-where-is-the-documentation) |
| [What is this library called?](#q-what-is-this-library-called) |
| [Which version should I get?](#q-which-version-should-i-get) |
| **Q&A: Integration** |
| **[How can I tell whether to dispatch mouse/keyboard to Dear ImGui or to my application?](#q-how-can-i-tell-whether-to-dispatch-mousekeyboard-to-dear-imgui-or-to-my-application)** |
| [How can I enable keyboard or gamepad controls?](#q-how-can-i-enable-keyboard-or-gamepad-controls) |
| [How can I use this on a machine without mouse, keyboard or screen? (input share, remote display)](#q-how-can-i-use-this-on-a-machine-without-mouse-keyboard-or-screen-input-share-remote-display) |
| [I integrated Dear ImGui in my engine and the text or lines are blurry..](#q-i-integrated-dear-imgui-in-my-engine-and-the-text-or-lines-are-blurry) |
| [I integrated Dear ImGui in my engine and some elements are clipping or disappearing when I move windows around..](#q-i-integrated-dear-imgui-in-my-engine-and-some-elements-are-clipping-or-disappearing-when-i-move-windows-around) |
| **Q&A: Usage** |
| **[Why are multiple widgets reacting when I interact with a single one?<br>How can I have multiple widgets with the same label or with an empty label?](#q-why-are-multiple-widgets-reacting-when-i-interact-with-a-single-one-q-how-can-i-have-multiple-widgets-with-the-same-label-or-with-an-empty-label)** |
| [How can I display an image? What is ImTextureID, how does it work?](#q-how-can-i-display-an-image-what-is-imtextureid-how-does-it-work)|
| [How can I use my own math types instead of ImVec2/ImVec4?](#q-how-can-i-use-my-own-math-types-instead-of-imvec2imvec4) |
| [How can I interact with standard C++ types (such as std::string and std::vector)?](#q-how-can-i-interact-with-standard-c-types-such-as-stdstring-and-stdvector) |
| [How can I display custom shapes? (using low-level ImDrawList API)](#q-how-can-i-display-custom-shapes-using-low-level-imdrawlist-api) |
| **Q&A: Fonts, Text** |
| [How can I load a different font than the default?](#q-how-can-i-load-a-different-font-than-the-default) |
| [How can I easily use icons in my application?](#q-how-can-i-easily-use-icons-in-my-application) |
| [How can I load multiple fonts?](#q-how-can-i-load-multiple-fonts) |
| [How can I display and input non-Latin characters such as Chinese, Japanese, Korean, Cyrillic?](#q-how-can-i-display-and-input-non-latin-characters-such-as-chinese-japanese-korean-cyrillic) |
| **Q&A: Concerns** |
| [Who uses Dear ImGui?](#q-who-uses-dear-imgui) |
| [Can you create elaborate/serious tools with Dear ImGui?](#q-can-you-create-elaborateserious-tools-with-dear-imgui)  |
| [Can you reskin the look of Dear ImGui?](#q-can-you-reskin-the-look-of-dear-imgui) |
| [Why using C++ (as opposed to C)?](#q-why-using-c-as-opposed-to-c) |
| **Q&A: Community** |
| [How can I help?](#q-how-can-i-help) |


# Q&A: Basics

### Q: Where is the documentation?

**This library is poorly documented at the moment and expects of the user to be acquainted with C/C++.**
- Dozens of standalone example applications using e.g. OpenGL/DirectX are provided in the [examples/](https://github.com/ocornut/imgui/blob/master/examples/) folder to explain how to integrate Dear ImGui with your own engine/application. You can run those applications and explore them.
- See demo code in [imgui_demo.cpp](https://github.com/ocornut/imgui/blob/master/imgui_demo.cpp) and particularly the `ImGui::ShowDemoWindow()` function. The demo covers most features of Dear ImGui, so you can read the code and see its output.
- See documentation and comments at the top of [imgui.cpp](https://github.com/ocornut/imgui/blob/master/imgui.cpp) + general API comments in [imgui.h](https://github.com/ocornut/imgui/blob/master/imgui.h).
- The [Wiki](https://github.com/ocornut/imgui/wiki) has many resources and links.
- The [Glossary](https://github.com/ocornut/imgui/wiki/Glossary) page may be useful.
- The [Issues](https://github.com/ocornut/imgui/issues) section can be searched for past questions and issues.
- Your programming IDE is your friend, find the type or function declaration to find comments associated to it.
- The `ImGui::ShowMetricsWindow()` function exposes lots of internal information and tools. Although it is primary designed as a debugging tool, having access to that information tends to help understands concepts.

---

### Q. What is this library called?

**This library is called Dear ImGui**. Please refer to it as Dear ImGui (not ImGui, not IMGUI).

(The library misleadingly started its life in 2014 as "ImGui" due to the fact that I didn't give it a proper name when when I released 1.0, and had no particular expectation that it would take off. However, the term IMGUI (immediate-mode graphical user interface) was coined before and is being used in variety of other situations e.g. Unity uses it own implementation of the IMGUI paradigm. To reduce the ambiguity without affecting existing code bases, I have decided in December 2015 a fully qualified name "Dear ImGui" for this library.

---

### Q: Which version should I get?
I occasionally tag [Releases](https://github.com/ocornut/imgui/releases) but it is generally safe and recommended to sync to master/latest. The library is fairly stable and regressions tend to be fixed fast when reported.

You may use the [docking](https://github.com/ocornut/imgui/tree/docking) branch which includes:
- [Docking features](https://github.com/ocornut/imgui/issues/2109)
- [Multi-viewport features](https://github.com/ocornut/imgui/issues/1542)

Many projects are using this branch and it is kept in sync with master regularly.

---

##### [Return to Index](#index)


# Q&A: Integration

### Q: How can I tell whether to dispatch mouse/keyboard to Dear ImGui or to my application?

You can read the `io.WantCaptureMouse`, `io.WantCaptureKeyboard` and `io.WantTextInput` flags from the ImGuiIO structure.

e.g. `if (ImGui::GetIO().WantCaptureMouse) { ... }`

- When `io.WantCaptureMouse` is set, imgui wants to use your mouse state, and you may want to discard/hide the inputs from the rest of your application.
- When `io.WantCaptureKeyboard` is set, imgui wants to use your keyboard state, and you may want to discard/hide the inputs from the rest of your application.
- When `io.WantTextInput` is set to may want to notify your OS to popup an on-screen keyboard, if available (e.g. on a mobile phone, or console OS).

**Note:** You should always pass your mouse/keyboard inputs to Dear ImGui, even when the io.WantCaptureXXX flag are set false.
 This is because imgui needs to detect that you clicked in the void to unfocus its own windows.

**Note:** The `io.WantCaptureMouse` is more accurate that any manual attempt to "check if the mouse is hovering a window" (don't do that!). It handle mouse dragging correctly (both dragging that started over your application or over an imgui window) and handle e.g. modal windows blocking inputs. Those flags are updated by `ImGui::NewFrame()`. Preferably read the flags after calling NewFrame() if you can afford it, but reading them before is also perfectly fine, as the bool toggle fairly rarely. If you have on a touch device, you might find use for an early call to `UpdateHoveredWindowAndCaptureFlags()`.

**Note:** Text input widget releases focus on "Return KeyDown", so the subsequent "Return KeyUp" event that your application receive will typically have `io.WantCaptureKeyboard == false`. Depending on your application logic it may or not be inconvenient. You might want to track which key-downs were targeted for Dear ImGui, e.g. with an array of bool, and filter out the corresponding key-ups.)

---

### Q: How can I enable keyboard or gamepad controls?
- The gamepad/keyboard navigation is fairly functional and keeps being improved. The initial focus was to support game controllers, but keyboard is becoming increasingly and decently usable. Gamepad support is particularly useful to use Dear ImGui on a game console (e.g. PS4, Switch, XB1) without a mouse connected!
- Keyboard: set `io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard` to enable.
- Gamepad: set `io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad` to enable (with a supporting back-end).
- See [Control Sheets for Gamepads](http://www.dearimgui.org/controls_sheets) (reference PNG/PSD for for PS4, XB1, Switch gamepads).
- See `USING GAMEPAD/KEYBOARD NAVIGATION CONTROLS` section of [imgui.cpp](https://github.com/ocornut/imgui/blob/master/imgui.cpp) for more details.

---

### Q: How can I use this on a machine without mouse, keyboard or screen? (input share, remote display)
- You can share your computer mouse seamlessly with your console/tablet/phone using solutions such as [Synergy](https://symless.com/synergy)
This is the preferred solution for developer productivity.
In particular, the [micro-synergy-client repository](https://github.com/symless/micro-synergy-client) has simple
and portable source code (uSynergy.c/.h) for a small embeddable client that you can use on any platform to connect
to your host computer, based on the Synergy 1.x protocol. Make sure you download the Synergy 1 server on your computer.
Console SDK also sometimes provide equivalent tooling or wrapper for Synergy-like protocols.
- Game console users: consider emulating a mouse cursor with DualShock4 touch pad or a spare analog stick as a mouse-emulation fallback.
- You may also use a third party solution such as [Remote ImGui](https://github.com/JordiRos/remoteimgui) or [imgui-ws](https://github.com/ggerganov/imgui-ws) which sends the vertices to render over the local network, allowing you to use Dear ImGui even on a screen-less machine. See [Wiki](https://github.com/ocornut/imgui/wiki) index for most details.
- For touch inputs, you can increase the hit box of widgets (via the `style.TouchPadding` setting) to accommodate
for the lack of precision of touch inputs, but it is recommended you use a mouse or gamepad to allow optimizing
for screen real-estate and precision.

---

### Q: I integrated Dear ImGui in my engine and the text or lines are blurry..
In your Render function, try translating your projection matrix by (0.5f,0.5f) or (0.375f,0.375f).
Also make sure your orthographic projection matrix and io.DisplaySize matches your actual framebuffer dimension.

---

### Q: I integrated Dear ImGui in my engine and some elements are clipping or disappearing when I move windows around..
You are probably mishandling the clipping rectangles in your render function.
Rectangles provided by ImGui are defined as
`(x1=left,y1=top,x2=right,y2=bottom)`
and **NOT** as
`(x1,y1,width,height)`

##### [Return to Index](#index)


# Q&A: Usage

### Q: Why are multiple widgets reacting when I interact with a single one? <br>Q: How can I have multiple widgets with the same label or with an empty label?

A primer on labels and the ID Stack...

Dear ImGui internally need to uniquely identify UI elements.
Elements that are typically not clickable (such as calls to the Text functions) don't need an ID.
Interactive widgets (such as calls to Button buttons) need a unique ID.
Unique ID are used internally to track active widgets and occasionally associate state to widgets.
Unique ID are implicitly built from the hash of multiple elements that identify the "path" to the UI element.

- Unique ID are often derived from a string label:
```c
Button("OK");          // Label = "OK",     ID = hash of (..., "OK")
Button("Cancel");      // Label = "Cancel", ID = hash of (..., "Cancel")
```
- ID are uniquely scoped within windows, tree nodes, etc. which all pushes to the ID stack. Having
two buttons labeled "OK" in different windows or different tree locations is fine.
We used "..." above to signify whatever was already pushed to the ID stack previously:
```c
Begin("MyWindow");
Button("OK");          // Label = "OK",     ID = hash of ("MyWindow", "OK")
End();
Begin("MyOtherWindow");
Button("OK");          // Label = "OK",     ID = hash of ("MyOtherWindow", "OK")
End();
```
- If you have a same ID twice in the same location, you'll have a conflict:
```c
Button("OK");
Button("OK");          // ID collision! Interacting with either button will trigger the first one.
```
Fear not! this is easy to solve and there are many ways to solve it!

- Solving ID conflict in a simple/local context:
When passing a label you can optionally specify extra ID information within string itself.
Use "##" to pass a complement to the ID that won't be visible to the end-user.
This helps solving the simple collision cases when you know e.g. at compilation time which items
are going to be created:
```c
Begin("MyWindow");
Button("Play");        // Label = "Play",   ID = hash of ("MyWindow", "Play")
Button("Play##foo1");  // Label = "Play",   ID = hash of ("MyWindow", "Play##foo1")  // Different from above
Button("Play##foo2");  // Label = "Play",   ID = hash of ("MyWindow", "Play##foo2")  // Different from above
End();
```
- If you want to completely hide the label, but still need an ID:
```c
Checkbox("##On", &b);  // Label = "",       ID = hash of (..., "##On")   // No visible label, just a checkbox!
```
- Occasionally/rarely you might want change a label while preserving a constant ID. This allows
you to animate labels. For example you may want to include varying information in a window title bar,
but windows are uniquely identified by their ID. Use "###" to pass a label that isn't part of ID:
```c
Button("Hello###ID");  // Label = "Hello",  ID = hash of (..., "###ID")
Button("World###ID");  // Label = "World",  ID = hash of (..., "###ID")  // Same as above, even if the label looks different

sprintf(buf, "My game (%f FPS)###MyGame", fps);
Begin(buf);            // Variable title,   ID = hash of "MyGame"
```
- Solving ID conflict in a more general manner:
Use PushID() / PopID() to create scopes and manipulate the ID stack, as to avoid ID conflicts
within the same window. This is the most convenient way of distinguishing ID when iterating and
creating many UI elements programmatically.
You can push a pointer, a string or an integer value into the ID stack.
Remember that ID are formed from the concatenation of _everything_ pushed into the ID stack.
At each level of the stack we store the seed used for items at this level of the ID stack.
```c
Begin("Window");
for (int i = 0; i < 100; i++)
{
  PushID(i);           // Push i to the id tack
  Button("Click");     // Label = "Click",  ID = hash of ("Window", i, "Click")
  PopID();
}
for (int i = 0; i < 100; i++)
{
  MyObject* obj = Objects[i];
  PushID(obj);
  Button("Click");     // Label = "Click",  ID = hash of ("Window", obj pointer, "Click")
  PopID();
}
for (int i = 0; i < 100; i++)
{
  MyObject* obj = Objects[i];
  PushID(obj->Name);
  Button("Click");     // Label = "Click",  ID = hash of ("Window", obj->Name, "Click")
  PopID();
}
End();
```
- You can stack multiple prefixes into the ID stack:
```c
Button("Click");       // Label = "Click",  ID = hash of (..., "Click")
PushID("node");
  Button("Click");     // Label = "Click",  ID = hash of (..., "node", "Click")
  PushID(my_ptr);
    Button("Click");   // Label = "Click",  ID = hash of (..., "node", my_ptr, "Click")
  PopID();
PopID();
```
- Tree nodes implicitly creates a scope for you by calling PushID().
```c
Button("Click");       // Label = "Click",  ID = hash of (..., "Click")
if (TreeNode("node"))  // <-- this function call will do a PushID() for you (unless instructed not to, with a special flag)
{
  Button("Click");     // Label = "Click",  ID = hash of (..., "node", "Click")
  TreePop();
}
```
- When working with trees, ID are used to preserve the open/close state of each tree node.
Depending on your use cases you may want to use strings, indices or pointers as ID.
e.g. when following a single pointer that may change over time, using a static string as ID
will preserve your node open/closed state when the targeted object change.
e.g. when displaying a list of objects, using indices or pointers as ID will preserve the
node open/closed state differently. See what makes more sense in your situation!

---

### Q: How can I display an image? What is ImTextureID, how does it work?

Short explanation:
- Refer to [Image Loading and Displaying Examples](https://github.com/ocornut/imgui/wiki/Image-Loading-and-Displaying-Examples) on the [Wiki](https://github.com/ocornut/imgui/wiki).
- You may use functions such as `ImGui::Image()`, `ImGui::ImageButton()` or lower-level `ImDrawList::AddImage()` to emit draw calls that will use your own textures.
- Actual textures are identified in a way that is up to the user/engine. Those identifiers are stored and passed as ImTextureID (void*) value.
- Loading image files from the disk and turning them into a texture is not within the scope of Dear ImGui (for a good reason).

**Please read documentations or tutorials on your graphics API to understand how to display textures on the screen before moving onward.**

Long explanation:
- Dear ImGui's job is to create "meshes", defined in a renderer-agnostic format made of draw commands and vertices. At the end of the frame those meshes (ImDrawList) will be displayed by your rendering function. They are made up of textured polygons and the code to render them is generally fairly short (a few dozen lines). In the examples/ folder we provide functions for popular graphics API (OpenGL, DirectX, etc.).
- Each rendering function decides on a data type to represent "textures". The concept of what is a "texture" is entirely tied to your underlying engine/graphics API.
 We carry the information to identify a "texture" in the ImTextureID type.
ImTextureID is nothing more that a void*, aka 4/8 bytes worth of data: just enough to store 1 pointer or 1 integer of your choice.
Dear ImGui doesn't know or understand what you are storing in ImTextureID, it merely pass ImTextureID values until they reach your rendering function.
- In the [examples/](https://github.com/ocornut/imgui/tree/master/examples) bindings, for each graphics API binding we decided on a type that is likely to be a good representation for specifying an image from the end-user perspective. This is what the _examples_ rendering functions are using:
```
OpenGL:
- ImTextureID = GLuint
- See ImGui_ImplOpenGL3_RenderDrawData() function in imgui_impl_opengl3.cpp
```
```
DirectX9:
- ImTextureID = LPDIRECT3DTEXTURE9
- See ImGui_ImplDX9_RenderDrawData() function in imgui_impl_dx9.cpp
```
```
DirectX11:
- ImTextureID = ID3D11ShaderResourceView*
- See ImGui_ImplDX11_RenderDrawData() function in imgui_impl_dx11.cpp
```
```
DirectX12:
- ImTextureID = D3D12_GPU_DESCRIPTOR_HANDLE
- See ImGui_ImplDX12_RenderDrawData() function in imgui_impl_dx12.cpp
```
For example, in the OpenGL example binding we store raw OpenGL texture identifier (GLuint) inside ImTextureID.
Whereas in the DirectX11 example binding we store a pointer to ID3D11ShaderResourceView inside ImTextureID, which is a higher-level structure tying together both the texture and information about its format and how to read it.

- If you have a custom engine built over e.g. OpenGL, instead of passing GLuint around you may decide to use a high-level data type to carry information about the texture as well as how to display it (shaders, etc.). The decision of what to use as ImTextureID can always be made better knowing how your codebase is designed. If your engine has high-level data types for "textures" and "material" then you may want to use them.
If you are starting with OpenGL or DirectX or Vulkan and haven't built much of a rendering engine over them, keeping the default ImTextureID representation suggested by the example bindings is probably the best choice.
(Advanced users may also decide to keep a low-level type in ImTextureID, and use ImDrawList callback and pass information to their renderer)

User code may do:
```cpp
// Cast our texture type to ImTextureID / void*
MyTexture* texture = g_CoffeeTableTexture;
ImGui::Image((void*)texture, ImVec2(texture->Width, texture->Height));
```
The renderer function called after ImGui::Render() will receive that same value that the user code passed:
```cpp
// Cast ImTextureID / void* stored in the draw command as our texture type
MyTexture* texture = (MyTexture*)pcmd->TextureId;
MyEngineBindTexture2D(texture);
```
Once you understand this design you will understand that loading image files and turning them into displayable textures is not within the scope of Dear ImGui.
This is by design and is actually a good thing, because it means your code has full control over your data types and how you display them.
If you want to display an image file (e.g. PNG file) into the screen, please refer to documentation and tutorials for the graphics API you are using.

Refer to [Image Loading and Displaying Examples](https://github.com/ocornut/imgui/wiki/Image-Loading-and-Displaying-Examples) on the [Wiki](https://github.com/ocornut/imgui/wiki) to find simplified examples for loading textures with OpenGL, DirectX9 and DirectX11.

C/C++ tip: a void* is pointer-sized storage. You may safely store any pointer or integer into it by casting your value to ImTextureID / void*, and vice-versa.
Because both end-points (user code and rendering function) are under your control, you know exactly what is stored inside the ImTextureID / void*.
Examples:
```cpp
GLuint my_tex = XXX;
void* my_void_ptr;
my_void_ptr = (void*)(intptr_t)my_tex;                  // cast a GLuint into a void* (we don't take its address! we literally store the value inside the pointer)
my_tex = (GLuint)(intptr_t)my_void_ptr;                 // cast a void* into a GLuint

ID3D11ShaderResourceView* my_dx11_srv = XXX;
void* my_void_ptr;
my_void_ptr = (void*)my_dx11_srv;                       // cast a ID3D11ShaderResourceView* into an opaque void*
my_dx11_srv = (ID3D11ShaderResourceView*)my_void_ptr;   // cast a void* into a ID3D11ShaderResourceView*
```
Finally, you may call `ImGui::ShowMetricsWindow()` to explore/visualize/understand how the ImDrawList are generated.

---

### Q: How can I use my own math types instead of ImVec2/ImVec4?

You can edit [imconfig.h](https://github.com/ocornut/imgui/blob/master/imconfig.h) and setup the `IM_VEC2_CLASS_EXTRA`/`IM_VEC4_CLASS_EXTRA` macros to add implicit type conversions.
This way you'll be able to use your own types everywhere, e.g. passing `MyVector2` or `glm::vec2` to ImGui functions instead of `ImVec2`.

---

### Q: How can I interact with standard C++ types (such as std::string and std::vector)?
- Being highly portable (bindings for several languages, frameworks, programming style, obscure or older platforms/compilers), and aiming for compatibility & performance suitable for every modern real-time game engines, dear imgui does not use any of std C++ types. We use raw types (e.g. char* instead of std::string) because they adapt to more use cases.
- To use ImGui::InputText() with a std::string or any resizable string class, see [misc/cpp/imgui_stdlib.h](https://github.com/ocornut/imgui/blob/master/misc/cpp/imgui_stdlib.h).
- To use combo boxes and list boxes with `std::vector` or any other data structure: the `BeginCombo()/EndCombo()` API
lets you iterate and submit items yourself, so does the `ListBoxHeader()/ListBoxFooter()` API.
Prefer using them over the old and awkward `Combo()/ListBox()` api.
- Generally for most high-level types you should be able to access the underlying data type.
You may write your own one-liner wrappers to facilitate user code (tip: add new functions in ImGui:: namespace from your code).
- Dear ImGui applications often need to make intensive use of strings. It is expected that many of the strings you will pass
to the API are raw literals (free in C/C++) or allocated in a manner that won't incur a large cost on your application.
Please bear in mind that using `std::string` on applications with large amount of UI may incur unsatisfactory performances.
Modern implementations of `std::string` often include small-string optimization (which is often a local buffer) but those
are not configurable and not the same across implementations.
- If you are finding your UI traversal cost to be too large, make sure your string usage is not leading to excessive amount
of heap allocations. Consider using literals, statically sized buffers and your own helper functions. A common pattern
is that you will need to build lots of strings on the fly, and their maximum length can be easily be scoped ahead.
One possible implementation of a helper to facilitate printf-style building of strings: https://github.com/ocornut/Str
This is a small helper where you can instance strings with configurable local buffers length. Many game engines will
provide similar or better string helpers.

---

### Q: How can I display custom shapes? (using low-level ImDrawList API)

- You can use the low-level `ImDrawList` api to render shapes within a window.

```
ImGui::Begin("My shapes");

ImDrawList* draw_list = ImGui::GetWindowDrawList();

// Get the current ImGui cursor position
ImVec2 p = ImGui::GetCursorScreenPos();

// Draw a red circle
draw_list->AddCircleFilled(ImVec2(p.x + 50, p.y + 50), 30.0f, IM_COL32(255, 0, 0, 255), 16);

// Draw a 3 pixel thick yellow line
draw_list->AddLine(ImVec2(p.x, p.y), ImVec2(p.x + 100.0f, p.y + 100.0f), IM_COL32(255, 255, 0, 255), 3.0f);

// Advance the ImGui cursor to claim space in the window (otherwise the window will appears small and needs to be resized)
ImGui::Dummy(ImVec2(200, 200));

ImGui::End();
```
![ImDrawList usage](https://raw.githubusercontent.com/wiki/ocornut/imgui/tutorials/CustomRendering01.png)

- Refer to "Demo > Examples > Custom Rendering" in the demo window and read the code of `ShowExampleAppCustomRendering()` in `imgui_demo.cpp` from more examples.
- To generate colors: you can use the macro `IM_COL32(255,255,255,255)` to generate them at compile time, or use `ImGui::GetColorU32(IM_COL32(255,255,255,255))` or `ImGui::GetColorU32(ImVec4(1.0f,1.0f,1.0f,1.0f))` to generate a color that is multiplied by the current value of `style.Alpha`.
- Math operators: if you have setup `IM_VEC2_CLASS_EXTRA` in `imconfig.h` to bind your own math types, you can use your own math types and their natural operators instead of ImVec2. ImVec2 by default doesn't export any math operators in the public API. You may use `#define IMGUI_DEFINE_MATH_OPERATORS` `#include "imgui_internal.h"` to use the internally defined math operators, but instead prefer using your own math library and set it up in `imconfig.h`.
- You can use `ImGui::GetBackgroundDrawList()` or `ImGui::GetForegroundDrawList()` to access draw lists which will be displayed behind and over every other dear imgui windows (one bg/fg drawlist per viewport). This is very convenient if you need to quickly display something on the screen that is not associated to a dear imgui window.
- You can also create your own dummy window and draw inside it. Call Begin() with the NoBackground | NoDecoration | NoSavedSettings | NoInputs flags (The `ImGuiWindowFlags_NoDecoration` flag itself is a shortcut for NoTitleBar | NoResize | NoScrollbar | NoCollapse). Then you can retrieve the ImDrawList* via GetWindowDrawList() and draw to it in any way you like.
- You can create your own ImDrawList instance. You'll need to initialize them with `ImGui::GetDrawListSharedData()`, or create your own instancing ImDrawListSharedData, and then call your renderer function with your own ImDrawList or ImDrawData data.

##### [Return to Index](#index)


# Q&A: Fonts, Text

### Q: How can I load a different font than the default?
Use the font atlas to load the TTF/OTF file you want:

```c
ImGuiIO& io = ImGui::GetIO();
io.Fonts->AddFontFromFileTTF("myfontfile.ttf", size_in_pixels);
io.Fonts->GetTexDataAsRGBA32() or GetTexDataAsAlpha8()
```

Default is ProggyClean.ttf, monospace, rendered at size 13, embedded in dear imgui's source code.

(Tip: monospace fonts are convenient because they allow to facilitate horizontal alignment directly at the string level.)

(Read the [docs/FONTS.txt](https://github.com/ocornut/imgui/blob/master/docs/FONTS.txt) file for more details about font loading.)

New programmers: remember that in C/C++ and most programming languages if you want to use a
backslash \ within a string literal, you need to write it double backslash "\\":

```c
io.Fonts->AddFontFromFileTTF("MyFolder\MyFont.ttf", size);  // WRONG (you are escaping the M here!)
io.Fonts->AddFontFromFileTTF("MyFolder\\MyFont.ttf", size;  // CORRECT
io.Fonts->AddFontFromFileTTF("MyFolder/MyFont.ttf", size);  // ALSO CORRECT
```

---

### Q: How can I easily use icons in my application?
The most convenient and practical way is to merge an icon font such as FontAwesome inside you
main font. Then you can refer to icons within your strings.
You may want to see `ImFontConfig::GlyphMinAdvanceX` to make your icon look monospace to facilitate alignment.
(Read the [docs/FONTS.txt](https://github.com/ocornut/imgui/blob/master/docs/FONTS.txt) file for more details about icons font loading.)
With some extra effort, you may use colorful icon by registering custom rectangle space inside the font atlas,
and copying your own graphics data into it. See docs/FONTS.txt about using the AddCustomRectFontGlyph API.

---

### Q: How can I load multiple fonts?
Use the font atlas to pack them into a single texture:
(Read the [docs/FONTS.txt](https://github.com/ocornut/imgui/blob/master/docs/FONTS.txt) file and the code in ImFontAtlas for more details.)

```cpp
ImGuiIO& io = ImGui::GetIO();
ImFont* font0 = io.Fonts->AddFontDefault();
ImFont* font1 = io.Fonts->AddFontFromFileTTF("myfontfile.ttf", size_in_pixels);
ImFont* font2 = io.Fonts->AddFontFromFileTTF("myfontfile2.ttf", size_in_pixels);
io.Fonts->GetTexDataAsRGBA32() or GetTexDataAsAlpha8()
// the first loaded font gets used by default
// use ImGui::PushFont()/ImGui::PopFont() to change the font at runtime

// Options
ImFontConfig config;
config.OversampleH = 2;
config.OversampleV = 1;
config.GlyphOffset.y -= 1.0f;      // Move everything by 1 pixels up
config.GlyphExtraSpacing.x = 1.0f; // Increase spacing between characters
io.Fonts->AddFontFromFileTTF("myfontfile.ttf", size_pixels, &config);

// Combine multiple fonts into one (e.g. for icon fonts)
static ImWchar ranges[] = { 0xf000, 0xf3ff, 0 };
ImFontConfig config;
config.MergeMode = true;
io.Fonts->AddFontDefault();
io.Fonts->AddFontFromFileTTF("fontawesome-webfont.ttf", 16.0f, &config, ranges); // Merge icon font
io.Fonts->AddFontFromFileTTF("myfontfile.ttf", size_pixels, NULL, &config, io.Fonts->GetGlyphRangesJapanese()); // Merge japanese glyphs
```

---

### Q: How can I display and input non-Latin characters such as Chinese, Japanese, Korean, Cyrillic?
When loading a font, pass custom Unicode ranges to specify the glyphs to load.

```cpp
// Add default Japanese ranges
io.Fonts->AddFontFromFileTTF("myfontfile.ttf", size_in_pixels, NULL, io.Fonts->GetGlyphRangesJapanese());

// Or create your own custom ranges (e.g. for a game you can feed your entire game script and only build the characters the game need)
ImVector<ImWchar> ranges;
ImFontGlyphRangesBuilder builder;
builder.AddText("Hello world");                        // Add a string (here "Hello world" contains 7 unique characters)
builder.AddChar(0x7262);                               // Add a specific character
builder.AddRanges(io.Fonts->GetGlyphRangesJapanese()); // Add one of the default ranges
builder.BuildRanges(&ranges);                          // Build the final result (ordered ranges with all the unique characters submitted)
io.Fonts->AddFontFromFileTTF("myfontfile.ttf", 16.0f, NULL, ranges.Data);
```

All your strings needs to use UTF-8 encoding. In C++11 you can encode a string literal in UTF-8
by using the u8"hello" syntax. Specifying literal in your source code using a local code page
(such as CP-923 for Japanese or CP-1251 for Cyrillic) will NOT work!
Otherwise you can convert yourself to UTF-8 or load text data from file already saved as UTF-8.

Text input: it is up to your application to pass the right character code by calling `io.AddInputCharacter()`.
The applications in examples/ are doing that.
Windows: you can use the WM_CHAR or WM_UNICHAR or WM_IME_CHAR message (depending if your app is built using Unicode or MultiByte mode).
You may also use MultiByteToWideChar() or ToUnicode() to retrieve Unicode codepoints from MultiByte characters or keyboard state.
Windows: if your language is relying on an Input Method Editor (IME), you copy the HWND of your window to io.ImeWindowHandle in order for
the default implementation of io.ImeSetInputScreenPosFn() to set your Microsoft IME position correctly.

##### [Return to Index](#index)


# Q&A: Concerns

### Q: Who uses Dear ImGui?

You may take a look at:

- [Quotes](https://github.com/ocornut/imgui/wiki/Quotes)
- [Software using Dear ImGui](https://github.com/ocornut/imgui/wiki/Software-using-dear-imgui)
- [Gallery](https://github.com/ocornut/imgui/issues/2847)

### Q: Can you create elaborate/serious tools with Dear ImGui?

Yes. People have written game editors, data browsers, debuggers, profilers and all sort of non-trivial tools with the library. In my experience the simplicity of the API is very empowering. Your UI runs close to your live data. Make the tools always-on and everybody in the team will be inclined to create new tools (as opposed to more "offline" UI toolkits where only a fraction of your team effectively creates tools). The list of sponsors below is also an indicator that serious game teams have been using the library.

Dear ImGui is very programmer centric and the immediate-mode GUI paradigm might require you to readjust some habits before you can realize its full potential. Dear ImGui is about making things that are simple, efficient and powerful.

Dear ImGui is built to be efficient and scalable toward the needs for AAA-quality applications running all day. The IMGUI paradigm offers different opportunities for optimization that the more typical RMGUI paradigm.

### Q: Can you reskin the look of Dear ImGui?

Somehow. You can alter the look of the interface to some degree: changing colors, sizes, padding, rounding, fonts. However, as Dear ImGui is designed and optimized to create debug tools, the amount of skinning you can apply is limited. There is only so much you can stray away from the default look and feel of the interface. Dear ImGui is NOT designed to create user interface for games, although with ingenious use of the low-level API you can do it.

A reasonably skinned application may look like (screenshot from [#2529](https://github.com/ocornut/imgui/issues/2529#issuecomment-524281119))
![minipars](https://user-images.githubusercontent.com/314805/63589441-d9794f00-c5b1-11e9-8d96-cfc1b93702f7.png)

### Q: Why using C++ (as opposed to C)?

Dear ImGui takes advantage of a few C++ languages features for convenience but nothing anywhere Boost insanity/quagmire. Dear ImGui does NOT require C++11 so it can be used with most old C++ compilers. Dear ImGui doesn't use any C++ header file. Language-wise, function overloading and default parameters are used to make the API easier to use and code more terse. Doing so I believe the API is sitting on a sweet spot and giving up on those features would make the API more cumbersome. Other features such as namespace, constructors and templates (in the case of the ImVector<> class) are also relied on as a convenience.

There is an auto-generated [c-api for Dear ImGui (cimgui)](https://github.com/cimgui/cimgui) by Sonoro1234 and Stephan Dilly. It is designed for creating binding to other languages. If possible, I would suggest using your target language functionalities to try replicating the function overloading and default parameters used in C++ else the API may be harder to use. Also see [Bindings](https://github.com/ocornut/imgui/wiki/Bindings) for various third-party bindings.

##### [Return to Index](#index)


# Q&A: Community

### Q: How can I help?
- Businesses: please reach out to `contact AT dearimgui.org` if you work in a place using Dear ImGui! We can discuss ways for your company to fund development via invoiced technical support, maintenance or sponsoring contacts. This is among the most useful thing you can do for Dear ImGui. With increased funding we can hire more people working on this project.
- Individuals: you can support continued maintenance and development via PayPal donations. See [README](https://github.com/ocornut/imgui/blob/master/docs/README.md).
- If you are experienced with Dear ImGui and C++, look at the [GitHub Issues](https://github.com/ocornut/imgui/issues), look at the [Wiki](https://github.com/ocornut/imgui/wiki), read [docs/TODO.txt](https://github.com/ocornut/imgui/blob/master/docs/TODO.txt) and see how you want to help and can help!
- Disclose your usage of Dear ImGui via a dev blog post, a tweet, a screenshot, a mention somewhere etc.
You may post screenshot or links in the [gallery threads](https://github.com/ocornut/imgui/issues/2847). Visuals are ideal as they inspire other programmers. Disclosing your use of dear imgui help the library grow credibility, and help other teams and programmers with taking decisions.
- If you have issues or if you need to hack into the library, even if you don't expect any support it is useful that you share your issues or sometimes incomplete PR.

##### [Return to Index](#index)

dear imgui
FONTS DOCUMENTATION

Also read https://www.dearimgui.org/faq for more fonts related infos.

The code in imgui.cpp embeds a copy of 'ProggyClean.ttf' (by Tristan Grimmer),
a 13 pixels high, pixel-perfect font used by default.
We embed it font in source code so you can use Dear ImGui without any file system access.

You may also load external .TTF/.OTF files.
The files in this folder are suggested fonts, provided as a convenience.

Please read the FAQ: https://www.dearimgui.org/faq
Please use the Discord server: http://discord.dearimgui.org and not the Github issue tracker for basic font loading questions.


---------------------------------------
 INDEX:
---------------------------------------

- Readme First / FAQ
- Fonts Loading Instructions
- Using Icons
- Using FreeType rasterizer
- Building Custom Glyph Ranges
- Using custom colorful icons
- Embedding Fonts in Source Code
- Credits/Licences for fonts included in repository
- Fonts Links


---------------------------------------
 README FIRST / FAQ
---------------------------------------

- You can use the style editor ImGui::ShowStyleEditor() in the "Fonts" section to browse your fonts
  and understand what's going on if you have an issue.
- Fonts are rasterized in a single texture at the time of calling either of io.Fonts->GetTexDataAsAlpha8()/GetTexDataAsRGBA32()/Build().
- Make sure your font ranges data are persistent and available at the time the font atlas is being built.
- Use C++11 u8"my text" syntax to encode literal strings as UTF-8. e.g.:
      u8"hello"
      u8"こんにちは"   // this will be encoded as UTF-8
- If you want to include a backslash \ character in your string literal, you need to double them e.g. "folder\\filename".
  Read FAQ for details.


---------------------------------------
 FONTS LOADING INSTRUCTIONS
---------------------------------------

Load default font:

  ImGuiIO& io = ImGui::GetIO();
  io.Fonts->AddFontDefault();

Load .TTF/.OTF file with:

  ImGuiIO& io = ImGui::GetIO();
  io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels);

Load multiple fonts:

  ImGuiIO& io = ImGui::GetIO();
  ImFont* font1 = io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels);
  ImFont* font2 = io.Fonts->AddFontFromFileTTF("anotherfont.otf", size_pixels);

  // Select font at runtime
  ImGui::Text("Hello");	// use the default font (which is the first loaded font)
  ImGui::PushFont(font2);
  ImGui::Text("Hello with another font");
  ImGui::PopFont();

For advanced options create a ImFontConfig structure and pass it to the AddFont function (it will be copied internally):

  ImFontConfig config;
  config.OversampleH = 2;
  config.OversampleV = 1;
  config.GlyphExtraSpacing.x = 1.0f;
  ImFont* font = io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels, &config);

Combine two fonts into one:

  // Load a first font
  ImFont* font = io.Fonts->AddFontDefault();

  // Add character ranges and merge into the previous font
  // The ranges array is not copied by the AddFont* functions and is used lazily
  // so ensure it is available at the time of building or calling GetTexDataAsRGBA32().
  static const ImWchar icons_ranges[] = { 0xf000, 0xf3ff, 0 }; // Will not be copied by AddFont* so keep in scope.
  ImFontConfig config;
  config.MergeMode = true;
  io.Fonts->AddFontFromFileTTF("DroidSans.ttf", 18.0f, &config, io.Fonts->GetGlyphRangesJapanese());
  io.Fonts->AddFontFromFileTTF("fontawesome-webfont.ttf", 18.0f, &config, icons_ranges);
  io.Fonts->Build();

Font atlas is too large?

- If you have very large number of glyphs or multiple fonts, the texture may become too big for your graphics API.
- The typical result of failing to upload a texture is if every glyphs appears as white rectangles.
- In particular, using a large range such as GetGlyphRangesChineseSimplifiedCommon() is not recommended
  unless you set OversampleH/OversampleV to 1 and use a small font size.
- Mind the fact that some graphics drivers have texture size limitation.
- If you are building a PC application, mind the fact that users may run on hardware with lower specs than yours.

Some solutions:

 - 1) Reduce glyphs ranges by calculating them from source localization data.
   You can use ImFontGlyphRangesBuilder for this purpose, this will be the biggest win!
 - 2) You may reduce oversampling, e.g. config.OversampleH = config.OversampleV = 1, this will largely reduce your texture size.
 - 3) Set io.Fonts.TexDesiredWidth to specify a texture width to minimize texture height (see comment in ImFontAtlas::Build function).
 - 4) Set io.Fonts.Flags |= ImFontAtlasFlags_NoPowerOfTwoHeight; to disable rounding the texture height to the next power of two.
 - Read about oversampling here: https://github.com/nothings/stb/blob/master/tests/oversample


Add a fourth parameter to bake specific font ranges only:

  // Basic Latin, Extended Latin
  io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels, NULL, io.Fonts->GetGlyphRangesDefault());

  // Default + Selection of 2500 Ideographs used by Simplified Chinese
  io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels, NULL, io.Fonts->GetGlyphRangesChineseSimplifiedCommon());

  // Default + Hiragana, Katakana, Half-Width, Selection of 1946 Ideographs
  io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels, NULL, io.Fonts->GetGlyphRangesJapanese());

See "BUILDING CUSTOM GLYPH RANGES" section to create your own ranges.
Offset font vertically by altering the io.Font->DisplayOffset value:

  ImFont* font = io.Fonts->AddFontFromFileTTF("font.ttf", size_pixels);
  font->DisplayOffset.y = 1;   // Render 1 pixel down


---------------------------------------
 USING ICONS
---------------------------------------

Using an icon font (such as FontAwesome: http://fontawesome.io or OpenFontIcons. https://github.com/traverseda/OpenFontIcons)
is an easy and practical way to use icons in your Dear ImGui application.
A common pattern is to merge the icon font within your main font, so you can embed icons directly from your strings without
having to change fonts back and forth.

To refer to the icon UTF-8 codepoints from your C++ code, you may use those headers files created by Juliette Foucaut:

  https://github.com/juliettef/IconFontCppHeaders

Those files contains a bunch of named #define which you can use to refer to specific icons of the font, e.g.:

  #define ICON_FA_MUSIC   "\xef\x80\x81"
  #define ICON_FA_SEARCH  "\xef\x80\x82"

Example Setup:

  // Merge icons into default tool font
  #include "IconsFontAwesome.h"
  ImGuiIO& io = ImGui::GetIO();
  io.Fonts->AddFontDefault();

  ImFontConfig config;
  config.MergeMode = true;
  config.GlyphMinAdvanceX = 13.0f; // Use if you want to make the icon monospaced
  static const ImWchar icon_ranges[] = { ICON_MIN_FA, ICON_MAX_FA, 0 };
  io.Fonts->AddFontFromFileTTF("fonts/fontawesome-webfont.ttf", 13.0f, &config, icon_ranges);

Example Usage:

  // Usage, e.g.
  ImGui::Text("%s among %d items", ICON_FA_SEARCH, count);
  ImGui::Button(ICON_FA_SEARCH " Search");

Important to understand: C string _literals_ can be concatenated at compilation time, e.g. "hello" " world"
ICON_FA_SEARCH is defined as a string literal so this is the same as "A" "B" becoming "AB"

See Links below for other icons fonts and related tools.


---------------------------------------
 FREETYPE RASTERIZER, SMALL FONT SIZES
---------------------------------------

Dear ImGui uses imstb_truetype.h to rasterize fonts (with optional oversampling).
This technique and its implementation are not ideal for fonts rendered at _small sizes_, which may appear a
little blurry or hard to read.

There is an implementation of the ImFontAtlas builder using FreeType that you can use in the misc/freetype/ folder.

FreeType supports auto-hinting which tends to improve the readability of small fonts.
Note that this code currently creates textures that are unoptimally too large (could be fixed with some work).
Also note that correct sRGB space blending will have an important effect on your font rendering quality.


---------------------------------------
 BUILDING CUSTOM GLYPH RANGES
---------------------------------------

You can use the ImFontGlyphRangesBuilder helper to create glyph ranges based on text input.
For example: for a game where your script is known, if you can feed your entire script to it and only build the characters the game needs.

  ImVector<ImWchar> ranges;
  ImFontGlyphRangesBuilder builder;
  builder.AddText("Hello world");                        // Add a string (here "Hello world" contains 7 unique characters)
  builder.AddChar(0x7262);                               // Add a specific character
  builder.AddRanges(io.Fonts->GetGlyphRangesJapanese()); // Add one of the default ranges
  builder.BuildRanges(&ranges);                          // Build the final result (ordered ranges with all the unique characters submitted)

  io.Fonts->AddFontFromFileTTF("myfontfile.ttf", size_in_pixels, NULL, ranges.Data);
  io.Fonts->Build();                                     // Build the atlas while 'ranges' is still in scope and not deleted.


---------------------------------------
 USING CUSTOM COLORFUL ICONS
---------------------------------------

(This is a BETA api, use if you are familiar with dear imgui and with your rendering back-end)

You can use the ImFontAtlas::AddCustomRect() and ImFontAtlas::AddCustomRectFontGlyph() api to register rectangles
that will be packed into the font atlas texture. Register them before building the atlas, then call Build().
You can then use ImFontAtlas::GetCustomRectByIndex(int) to query the position/size of your rectangle within the
texture, and blit/copy any graphics data of your choice into those rectangles.

Pseudo-code:

  // Add font, then register two custom 13x13 rectangles mapped to glyph 'a' and 'b' of this font
  ImFont* font = io.Fonts->AddFontDefault();
  int rect_ids[2];
  rect_ids[0] = io.Fonts->AddCustomRectFontGlyph(font, 'a', 13, 13, 13+1);
  rect_ids[1] = io.Fonts->AddCustomRectFontGlyph(font, 'b', 13, 13, 13+1);

  // Build atlas
  io.Fonts->Build();

  // Retrieve texture in RGBA format
  unsigned char* tex_pixels = NULL;
  int tex_width, tex_height;
  io.Fonts->GetTexDataAsRGBA32(&tex_pixels, &tex_width, &tex_height);

  for (int rect_n = 0; rect_n < IM_ARRAYSIZE(rect_ids); rect_n++)
  {
      int rect_id = rects_ids[rect_n];
      if (const ImFontAtlas::CustomRect* rect = io.Fonts->GetCustomRectByIndex(rect_id))
      {
          // Fill the custom rectangle with red pixels (in reality you would draw/copy your bitmap data here!)
          for (int y = 0; y < rect->Height; y++)
          {
              ImU32* p = (ImU32*)tex_pixels + (rect->Y + y) * tex_width + (rect->X);
              for (int x = rect->Width; x > 0; x--)
                  *p++ = IM_COL32(255, 0, 0, 255);
          }
      }
  }


---------------------------------------
 EMBEDDING FONTS IN SOURCE CODE
---------------------------------------

Compile and use 'binary_to_compressed_c.cpp' to create a compressed C style array that you can embed in source code.
See the documentation in binary_to_compressed_c.cpp for instruction on how to use the tool.
You may find a precompiled version binary_to_compressed_c.exe for Windows instead of demo binaries package (see README).
The tool can optionally output Base85 encoding to reduce the size of _source code_ but the read-only arrays in the
actual binary will be about 20% bigger.

Then load the font with:
  ImFont* font = io.Fonts->AddFontFromMemoryCompressedTTF(compressed_data, compressed_data_size, size_pixels, ...);
or:
  ImFont* font = io.Fonts->AddFontFromMemoryCompressedBase85TTF(compressed_data_base85, size_pixels, ...);


---------------------------------------
 CREDITS/LICENSES FOR FONTS INCLUDED IN REPOSITORY
---------------------------------------

Some fonts are available in the misc/fonts/ folder:

Roboto-Medium.ttf

  Apache License 2.0
  by Christian Robertson
  https://fonts.google.com/specimen/Roboto

Cousine-Regular.ttf

  by Steve Matteson
  Digitized data copyright (c) 2010 Google Corporation.
  Licensed under the SIL Open Font License, Version 1.1
  https://fonts.google.com/specimen/Cousine

DroidSans.ttf

  Copyright (c) Steve Matteson
  Apache License, version 2.0
  https://www.fontsquirrel.com/fonts/droid-sans

ProggyClean.ttf

  Copyright (c) 2004, 2005 Tristan Grimmer
  MIT License
  recommended loading setting: Size = 13.0, DisplayOffset.Y = +1
  http://www.proggyfonts.net/

ProggyTiny.ttf
  Copyright (c) 2004, 2005 Tristan Grimmer
  MIT License
  recommended loading setting: Size = 10.0, DisplayOffset.Y = +1
  http://www.proggyfonts.net/

Karla-Regular.ttf
  Copyright (c) 2012, Jonathan Pinhorn
  SIL OPEN FONT LICENSE Version 1.1


---------------------------------------
 FONTS LINKS
---------------------------------------

ICON FONTS

  C/C++ header for icon fonts (#define with code points to use in source code string literals)
  https://github.com/juliettef/IconFontCppHeaders

  FontAwesome
  https://fortawesome.github.io/Font-Awesome

  OpenFontIcons
  https://github.com/traverseda/OpenFontIcons

  Google Icon Fonts
  https://design.google.com/icons/

  Kenney Icon Font (Game Controller Icons)
  https://github.com/nicodinh/kenney-icon-font

  IcoMoon - Custom Icon font builder
  https://icomoon.io/app

REGULAR FONTS

  Google Noto Fonts (worldwide languages)
  https://www.google.com/get/noto/

  Open Sans Fonts
  https://fonts.google.com/specimen/Open+Sans

  (Japanese) M+ fonts by Coji Morishita are free
  http://mplus-fonts.sourceforge.jp/mplus-outline-fonts/index-en.html

MONOSPACE FONTS (PIXEL PERFECT)

  Proggy Fonts, by Tristan Grimmer
  http://www.proggyfonts.net or http://upperbounds.net

  Sweet16, Sweet16 Mono, by Martin Sedlak (Latin + Supplemental + Extended A)
  https://github.com/kmar/Sweet16Font
  Also include .inl file to use directly in dear imgui.

MONOSPACE FONTS (REGULAR)

  Google Noto Mono Fonts
  https://www.google.com/get/noto/

  Typefaces for source code beautification
  https://github.com/chrissimpkins/codeface

  Programmation fonts
  http://s9w.github.io/font_compare/

  Inconsolata
  http://www.levien.com/type/myfonts/inconsolata.html

  Adobe Source Code Pro: Monospaced font family for user interface and coding environments
  https://github.com/adobe-fonts/source-code-pro

  Monospace/Fixed Width Programmer's Fonts
  http://www.lowing.org/fonts/


 Or use Arial Unicode or other Unicode fonts provided with Windows for full characters coverage (not sure of their licensing).
dear imgui
=====
[![Build Status](https://github.com/ocornut/imgui/workflows/build/badge.svg)](https://github.com/ocornut/imgui/actions?workflow=build)

<sub>(This library is available under a free and permissive license, but needs financial support to sustain its continued improvements. In addition to maintenance and stability there are many desirable features yet to be added. If your company is using dear imgui, please consider reaching out.)</sub>

Businesses: support continued development via invoiced technical support, maintenance, sponsoring contracts:
<br>&nbsp;&nbsp;_E-mail: contact @ dearimgui dot org_

Individuals: support continued maintenance and development via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WGHNC6MBFLZ2S) donations.

----

Dear ImGui is a **bloat-free graphical user interface library for C++**. It outputs optimized vertex buffers that you can render anytime in your 3D-pipeline enabled application. It is fast, portable, renderer agnostic and self-contained (no external dependencies).

Dear ImGui is designed to **enable fast iterations** and to **empower programmers** to create **content creation tools and visualization / debug tools** (as opposed to UI for the average end-user). It favors simplicity and productivity toward this goal, and lacks certain features normally found in more high-level libraries.

Dear ImGui is particularly suited to integration in games engine (for tooling), real-time 3D applications, fullscreen applications, embedded applications, or any applications on consoles platforms where operating system features are non-standard.

| [Usage](#usage) - [How it works](#how-it-works) - [Demo](#demo) - [Integration](#integration) |
:----------------------------------------------------------: |
| [Upcoming changes](#upcoming-changes) - [Gallery](#gallery) - [Support, FAQ](#support-frequently-asked-questions-faq) -  [How to help](#how-to-help) - [Sponsors](#sponsors) - [Credits](#credits) - [License](#license) |
| [Wiki](https://github.com/ocornut/imgui/wiki) - [Language & frameworks bindings](https://github.com/ocornut/imgui/wiki/Bindings) - [Software using Dear ImGui](https://github.com/ocornut/imgui/wiki/Software-using-dear-imgui) - [User quotes](https://github.com/ocornut/imgui/wiki/Quotes) |

### Usage

**The core of Dear ImGui is self-contained within a few platform-agnostic files** which you can easily compile in your application/engine. They are all the files in the root folder of the repository (imgui.cpp, imgui.h, imgui_demo.cpp, imgui_draw.cpp etc.).

**No specific build process is required**. You can add the .cpp files to your existing project.

You will need a backend to integrate Dear ImGui in your app. The backend passes mouse/keyboard/gamepad inputs and variety of settings to Dear ImGui, and is in charge of rendering the resulting vertices.

**Backends for a variety of graphics api and rendering platforms** are provided in the [examples/](https://github.com/ocornut/imgui/tree/master/examples) folder, along with example applications. See the [Integration](#integration) section of this document for details. You may also create your own backend. Anywhere where you can render textured triangles, you can render Dear ImGui.

After Dear ImGui is setup in your application, you can use it from \_anywhere\_ in your program loop:

Code:
```cp
ImGui::Text("Hello, world %d", 123);
if (ImGui::Button("Save"))
    MySaveFunction();
ImGui::InputText("string", buf, IM_ARRAYSIZE(buf));
ImGui::SliderFloat("float", &f, 0.0f, 1.0f);
```
Result:
<br>![sample code output (dark)](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v175/capture_readme_styles_0001.png) ![sample code output (light)](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v175/capture_readme_styles_0002.png)
<br>_(settings: Dark style (left), Light style (right) / Font: Roboto-Medium, 16px / Rounding: 5)_

Code:
```cpp
// Create a window called "My First Tool", with a menu bar.
ImGui::Begin("My First Tool", &my_tool_active, ImGuiWindowFlags_MenuBar);
if (ImGui::BeginMenuBar())
{
    if (ImGui::BeginMenu("File"))
    {
        if (ImGui::MenuItem("Open..", "Ctrl+O")) { /* Do stuff */ }
        if (ImGui::MenuItem("Save", "Ctrl+S"))   { /* Do stuff */ }
        if (ImGui::MenuItem("Close", "Ctrl+W"))  { my_tool_active = false; }
        ImGui::EndMenu();
    }
    ImGui::EndMenuBar();
}

// Edit a color (stored as ~4 floats)
ImGui::ColorEdit4("Color", my_color);

// Plot some values
const float my_values[] = { 0.2f, 0.1f, 1.0f, 0.5f, 0.9f, 2.2f };
ImGui::PlotLines("Frame Times", my_values, IM_ARRAYSIZE(my_values));

// Display contents in a scrolling region
ImGui::TextColored(ImVec4(1,1,0,1), "Important Stuff");
ImGui::BeginChild("Scrolling");
for (int n = 0; n < 50; n++)
    ImGui::Text("%04d: Some text", n);
ImGui::EndChild();
ImGui::End();
```
Result:
<br>![sample code output](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v160/code_sample_03_color.gif)

Dear ImGui allows you **create elaborate tools** as well as very short-lived ones. On the extreme side of short-livedness: using the Edit&Continue (hot code reload) feature of modern compilers you can add a few widgets to tweaks variables while your application is running, and remove the code a minute later! Dear ImGui is not just for tweaking values. You can use it to trace a running algorithm by just emitting text commands. You can use it along with your own reflection data to browse your dataset live. You can use it to expose the internals of a subsystem in your engine, to create a logger, an inspection tool, a profiler, a debugger, an entire game making editor/framework, etc.

### How it works

Check out the Wiki's [About the IMGUI paradigm](https://github.com/ocornut/imgui/wiki#About-the-IMGUI-paradigm) section if you want to understand the core principles behind the IMGUI paradigm. An IMGUI tries to minimize superfluous state duplication, state synchronization and state retention from the user's point of view. It is less error prone (less code and less bugs) than traditional retained-mode interfaces, and lends itself to create dynamic user interfaces.

Dear ImGui outputs vertex buffers and command lists that you can easily render in your application. The number of draw calls and state changes required to render them is fairly small. Because Dear ImGui doesn't know or touch graphics state directly, you can call its functions  anywhere in your code (e.g. in the middle of a running algorithm, or in the middle of your own rendering process). Refer to the sample applications in the examples/ folder for instructions on how to integrate dear imgui with your existing codebase.

_A common misunderstanding is to mistake immediate mode gui for immediate mode rendering, which usually implies hammering your driver/GPU with a bunch of inefficient draw calls and state changes as the gui functions are called. This is NOT what Dear ImGui does. Dear ImGui outputs vertex buffers and a small list of draw calls batches. It never touches your GPU directly. The draw call batches are decently optimal and you can render them later, in your app or even remotely._

### Demo

Calling the `ImGui::ShowDemoWindow()` function will create a demo window showcasing variety of features and examples. The code is always available for reference in `imgui_demo.cpp`.

![screenshot demo](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v167/v167-misc.png)

You should be able to build the examples from sources (tested on Windows/Mac/Linux). If you don't, let me know! If you want to have a quick look at some Dear ImGui features, you can download Windows binaries of the demo app here:
- [imgui-demo-binaries-20190715.zip](http://www.dearimgui.org/binaries/imgui-demo-binaries-20190715.zip) (Windows binaries, 1.72 WIP, built 2019/07/15, master branch, 5 executables)

The demo applications are not DPI aware so expect some blurriness on a 4K screen. For DPI awareness in your application, you can load/reload your font at different scale, and scale your style with `style.ScaleAllSizes()`.

### Integration

On most platforms and when using C++, **you should be able to use a combination of the [imgui_impl_xxxx](https://github.com/ocornut/imgui/tree/master/examples) files without modification** (e.g. `imgui_impl_win32.cpp` + `imgui_impl_dx11.cpp`). If your engine supports multiple platforms, consider using more of the imgui_impl_xxxx files instead of rewriting them: this will be less work for you and you can get Dear ImGui running immediately. You can _later_ decide to rewrite a custom binding using your custom engine functions if you wish so.

Integrating Dear ImGui within your custom engine is a matter of 1) wiring mouse/keyboard/gamepad inputs 2) uploading one texture to your GPU/render engine 3) providing a render function that can bind textures and render textured triangles. The [examples/](https://github.com/ocornut/imgui/tree/master/examples) folder is populated with applications doing just that. If you are an experienced programmer at ease with those concepts, it should take you less than two hours to integrate Dear ImGui in your custom engine. **Make sure to spend time reading the [FAQ](https://www.dearimgui.org/faq), comments, and some of the examples/ application!**

Officially maintained bindings (in repository):
- Renderers: DirectX9, DirectX10, DirectX11, DirectX12, OpenGL (legacy), OpenGL3/ES/ES2 (modern), Vulkan, Metal.
- Platforms: GLFW, SDL2, Win32, Glut, OSX.
- Frameworks: Emscripten, Allegro5, Marmalade.

Third-party bindings (see [Bindings](https://github.com/ocornut/imgui/wiki/Bindings/) page):
- Languages: C, C#/.Net, ChaiScript, D, Go, Haskell, Haxe/hxcpp, Java, JavaScript, Julia, Lua, Odin, Pascal, PureBasic, Python, Ruby, Rust, Swift...
- Frameworks: Amethyst, bsf, Cinder, Cocos2d-x, Diligent Engine, Flexium, GML/GameMakerStudio2, Irrlicht, Ogre, OpenFrameworks, OpenSceneGraph/OSG, ORX, px_render, LÖVE+Lua, Magnum, NanoRT, Qt, QtDirect3D, SFML, Software Rasterizers, Unreal Engine 4...
- Note that C bindings ([cimgui](https://github.com/cimgui/cimgui)) are auto-generated, you can use its json/lua output to generate bindings for other languages.

Also see [Wiki](https://github.com/ocornut/imgui/wiki) for more links and ideas.

### Upcoming Changes

Some of the goals for 2019-2020 are:
- Finish work on docking, tabs. (see [#2109](https://github.com/ocornut/imgui/issues/2109), in public [docking](https://github.com/ocornut/imgui/tree/docking) branch looking for feedback)
- Finish work on multiple viewports / multiple OS windows. (see [#1542](https://github.com/ocornut/imgui/issues/1542), in public [docking](https://github.com/ocornut/imgui/tree/docking) branch looking for feedback)
- Finish work on gamepad/keyboard controls. (see [#787](https://github.com/ocornut/imgui/issues/787))
- Add an automation and testing system, both to test the library and end-user apps. (see [#435](https://github.com/ocornut/imgui/issues/435))
- Make Columns better. They are currently pretty terrible! New Tables API coming Q4 2019!
- Make the examples look better, improve styles, improve font support, make the examples hi-DPI and multi-DPI aware.

### Gallery

For more user-submitted screenshots of projects using Dear ImGui, check out the [Gallery Threads](https://github.com/ocornut/imgui/issues/2847)!

Custom engine
[![screenshot game](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v149/gallery_TheDragonsTrap-01-thumb.jpg)](https://cloud.githubusercontent.com/assets/8225057/20628927/33e14cac-b329-11e6-80f6-9524e93b048a.png)

Custom engine
[![screenshot tool](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v160/editor_white_preview.jpg)](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v160/editor_white.png)

[Tracy Profiler](https://bitbucket.org/wolfpld/tracy)
![tracy profiler](https://raw.githubusercontent.com/wiki/ocornut/imgui/web/v173/tracy_profiler.jpg)

### Support, Frequently Asked Questions (FAQ)

Most common questions will be answered by the [Frequently Asked Questions (FAQ)](https://github.com/ocornut/imgui/blob/master/docs/FAQ.md) page.

See: [Wiki](https://github.com/ocornut/imgui/wiki) for many links, references, articles.

See: [Articles about the IMGUI paradigm](https://github.com/ocornut/imgui/wiki#Articles-about-the-IMGUI-paradigm) to read/learn about the Immediate Mode GUI paradigm.

If you are new to Dear ImGui and have issues with: compiling, linking, adding fonts, wiring inputs, running or displaying Dear ImGui: you can use [Discord server](http://discord.dearimgui.org).

Otherwise, for any other questions, bug reports, requests, feedback, you may post on https://github.com/ocornut/imgui/issues. Please read and fill the New Issue template carefully.

Paid private support is available for business customers (E-mail: _contact @ dearimgui dot org_).

**Which version should I get?**

I occasionally tag [Releases](https://github.com/ocornut/imgui/releases) but it is generally safe and recommended to sync to master/latest. The library is fairly stable and regressions tend to be fixed fast when reported.

You may also peak at the [Multi-Viewport](https://github.com/ocornut/imgui/issues/1542) and [Docking](https://github.com/ocornut/imgui/issues/2109) features in the `docking` branch. Many projects are using this branch and it is kept in sync with master regularly.

**Who uses Dear ImGui?**

See the [Quotes](https://github.com/ocornut/imgui/wiki/Quotes) and [Software using dear imgui](https://github.com/ocornut/imgui/wiki/Software-using-dear-imgui) Wiki pages for a list of games/software which are publicly known to use dear imgui. Please add yours if you can! Also see the [Gallery Threads](https://github.com/ocornut/imgui/issues/2847)!

How to help
-----------

**How can I help?**

- You may participate in the [Discord server](http://discord.dearimgui.org), [GitHub forum/issues](https://github.com/ocornut/imgui/issues).
- You may help with development and submit pull requests! Please understand that by submitting a PR you are also submitting a request for the maintainer to review your code and then take over its maintenance forever. PR should be crafted both in the interest in the end-users and also to ease the maintainer into understanding and accepting it.
- See [Help wanted](https://github.com/ocornut/imgui/wiki/Help-Wanted) on the [Wiki](https://github.com/ocornut/imgui/wiki/) for some more ideas.
- Have your company financially support this project.

**How can I help financing further development of Dear ImGui?**

Your contributions are keeping this project alive. The library is available under a free and permissive license, but continued maintenance and development are a full-time endeavor and I would like to grow the team. In addition to maintenance and stability there are many desirable features yet to be added. If your company is using dear imgui, please consider reaching out for invoiced technical support and maintenance contracts. Thank you!

Businesses: support continued development via invoiced technical support, maintenance, sponsoring contracts:
<br>&nbsp;&nbsp;_E-mail: contact @ dearimgui dot org_

Individuals: support continued maintenance and development via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WGHNC6MBFLZ2S) donations.

### Sponsors

Ongoing Dear ImGui development is financially supported by users and private sponsors, recently:

*Platinum-chocolate sponsors*
- Blizzard Entertainment
- Google
- Ubisoft

*Double-chocolate sponsors*
- Media Molecule, Mobigame, Aras Pranckevičius, Greggman, DotEmu, Nadeo, Supercell, Aiden Koss, Kylotonn.

*Salty caramel supporters*
- Remedy Entertainment, Next Level Games, Recognition Robotics, ikrima, Geoffrey Evans, Mercury Labs, Singularity Demo Group, Lionel Landwerlin, Ron Gilbert, Brandon Townsend, G3DVu, Cort Stratton, drudru, Harfang 3D, Jeff Roberts, Rainway inc, Ondra Voves, Mesh Consultants, Unit 2 Games, Neil Bickford, Bill Six, Graham Manders.

*Caramel supporters*
- Jerome Lanquetot, Daniel Collin, Ctrl Alt Ninja, Neil Henning, Neil Blakey-Milner, Aleksei, NeiloGD, Eric, Game Atelier, Vincent Hamm, Morten Skaaning, Colin Riley, Sergio Gonzales, Andrew Berridge, Roy Eltham, Game Preservation Society, Josh Faust, Martin Donlon, Codecat, Doug McNabb, Emmanuel Julien, Guillaume Chereau, Jeffrey Slutter, Jeremiah Deckard, r-lyeh, Nekith, Joshua Fisher, Malte Hoffmann, Mustafa Karaalioglu, Merlyn Morgan-Graham, Per Vognsen, Fabian Giesen, Jan Staubach, Matt Hargett, John Shearer, Jesse Chounard, kingcoopa, Jonas Bernemann, Johan Andersson, Michael Labbe, Tomasz Golebiowski, Louis Schnellbach, Jimmy Andrews, Bojan Endrovski, Robin Berg Pettersen, Rachel Crawford, Andrew Johnson, Sean Hunter, Jordan Mellow, Nefarius Software Solutions, Laura Wieme, Robert Nix, Mick Honey, Steven Kah Hien Wong, Bartosz Bielecki, Oscar Penas, A M, Liam Moynihan, Artometa, Mark Lee, Dimitri Diakopoulos, Pete Goodwin, Johnathan Roatch, nyu lea, Oswald Hurlem, Semyon Smelyanskiy, Le Bach, Jeong MyeongSoo, Chris Matthews, Astrofra, Frederik De Bleser, Anticrisis, Matt Reyer.

And all other past and present supporters; THANK YOU!
(Please contact me if you would like to be added or removed from this list)

Dear ImGui is using software and services kindly provided free of charge for open source projects:
- [PVS-Studio](https://www.viva64.com/en/b/0570/) for static analysis.
- [GitHub actions](https://github.com/features/actions) for continuous integration systems.

Credits
-------

Developed by [Omar Cornut](http://www.miracleworld.net) and every direct or indirect contributors to the GitHub. The early version of this library was developed with the support of [Media Molecule](http://www.mediamolecule.com) and first used internally on the game [Tearaway](http://tearaway.mediamolecule.com) (Vita).

I first discovered the IMGUI paradigm at [Q-Games](http://www.q-games.com) where Atman Binstock had dropped his own simple implementation in the codebase, which I spent quite some time improving and thinking about. It turned out that Atman was exposed to the concept directly by working with Casey. When I moved to Media Molecule I rewrote a new library trying to overcome the flaws and limitations of the first one I've worked with. It became this library and since then I have spent an unreasonable amount of time iterating and improving it.

Embeds [ProggyClean.ttf](http://upperbounds.net) font by Tristan Grimmer (MIT license).

Embeds [stb_textedit.h, stb_truetype.h, stb_rect_pack.h](https://github.com/nothings/stb/) by Sean Barrett (public domain).

Inspiration, feedback, and testing for early versions: Casey Muratori, Atman Binstock, Mikko Mononen, Emmanuel Briney, Stefan Kamoda, Anton Mikhailov, Matt Willis. And everybody posting feedback, questions and patches on the GitHub.

License
-------

Dear ImGui is licensed under the MIT License, see [LICENSE.txt](https://github.com/ocornut/imgui/blob/master/LICENSE.txt) for more information.
dear imgui
ISSUES & TODO LIST

Issue numbers (#) refer to github issues listed at https://github.com/ocornut/imgui/issues/XXXX
The list below consist mostly of ideas noted down before they are requested/discussed by users (at which point they usually exist on the github issue tracker).
It's mostly a bunch of personal notes, probably incomplete. Feel free to query if you have any questions.

 - doc/test: add a proper documentation+regression testing system (#435)
 - doc/test: checklist app to verify binding/integration of imgui (test inputs, rendering, callback, etc.).
 - doc/tips: tips of the day: website? applet in imgui_club?
 - doc/wiki: work on the wiki https://github.com/ocornut/imgui/wiki

 - window: preserve/restore relative focus ordering (persistent or not) (#2304) -> also see docking reference to same #.
 - window: calling SetNextWindowSize() every frame with <= 0 doesn't do anything, may be useful to allow (particularly when used for a single axis). (#690)
 - window: add a way for very transient windows (non-saved, temporary overlay over hundreds of objects) to "clean" up from the global window list. perhaps a lightweight explicit cleanup pass.
 - window: auto-fit feedback loop when user relies on any dynamic layout (window width multiplier, column) appears weird to end-user. clarify.
 - window: allow resizing of child windows (possibly given min/max for each axis?.)
 - window: background options for child windows, border option (disable rounding).
 - window: begin with *p_open == false could return false.
 - window: get size/pos helpers given names (see discussion in #249)
 - window: a collapsed window can be stuck behind the main menu bar?
 - window: when window is very small, prioritize resize button over close button.
 - window: detect extra End() call that pop the "Debug" window out and assert at End() call site instead of at end of frame.
 - window: increase minimum size of a window with menus or fix the menu rendering so that it doesn't look odd.
 - window: double-clicking on title bar to minimize isn't consistent, perhaps move to single-click on left-most collapse icon?
 - window: expose contents size. (#1045)
 - window: using SetWindowPos() inside Begin() and moving the window with the mouse reacts a very ugly glitch. We should just defer the SetWindowPos() call.
 - window: GetWindowSize() returns (0,0) when not calculated? (#1045)
 - window: investigate better auto-positioning for new windows.
 - window: top most window flag? (#2574)
 - window: the size_on_first_use path of Begin() can probably be removed
 - window/size: manually triggered auto-fit (double-click on grip) shouldn't resize window down to viewport size?
 - window/opt: freeze window flag: if not focused/hovered, return false, render with previous ImDrawList. and/or reduce refresh rate. -> this may require enforcing that it is illegal to submit contents if Begin returns false.
 - window/child: the first draw command of a child window could be moved into the current draw command of the parent window (unless child+tooltip?).
 - window/child: border could be emitted in parent as well.
 - window/child: allow SetNextWindowContentSize() to work on child windows.
 - window/clipping: some form of clipping when DisplaySize (or corresponding viewport) is zero.
 - window/tab: add a way to signify that a window or docked window requires attention (e.g. blinking title bar).
 ! scrolling: exposing horizontal scrolling with Shift+Wheel even when scrollbar is disabled expose lots of issues (#2424, #1463)
 - scrolling: while holding down a scrollbar, try to keep the same contents visible (at least while not moving mouse)
 - scrolling: allow immediately effective change of scroll after Begin() if we haven't appended items yet.
 - scrolling: forward mouse wheel scrolling to parent window when at the edge of scrolling limits? (useful for listbox,tables?)
 - scrolling/clipping: separator on the initial position of a window is not visible (cursorpos.y <= clippos.y). (2017-08-20: can't repro)
 - scrolling/style: shadows on scrollable areas to denote that there is more contents

 - drawdata: make it easy to clone (or swap?) a full ImDrawData so user can easily save that data if they use threaded rendering. (e.g. #2646)
 ! drawlist: add calctextsize func to facilitate consistent code from user pov (currently need to use ImGui or ImFont alternatives!)
 - drawlist: end-user probably can't call Clear() directly because we expect a texture to be pushed in the stack.
 - drawlist: maintaining bounding box per command would allow to merge draw command when clipping isn't relied on (typical non-scrolling window or non-overflowing column would merge with previous command).
 - drawlist: primitives/helpers to manipulate vertices post submission, so e.g. a quad/rect can be resized to fit later submitted content, _without_ using the ChannelSplit api
 - drawlist: make it easier to toggle AA per primitive, so we can use e.g. non-AA fill + AA borders more naturally
 - drawlist: non-AA strokes have gaps between points (#593, #288), glitch especially on RenderCheckmark() and ColorPicker4().
 - drawlist: would be good to be able to deep copy of ImDrawData (we have a deep copy of ImDrawList now).
 - drawlist: rendering: provide a way for imgui to output to a single/global vertex buffer, re-order indices only at the end of the frame (ref: https://gist.github.com/floooh/10388a0afbe08fce9e617d8aefa7d302)
 - drawlist: callback: add an extra void* in ImDrawCallback to allow passing render-local data to the callback (would break API).
 - drawlist: AddRect vs AddLine position confusing (#2441)
 - drawlist: channel splitter should be external helper and not stored in ImDrawList.
 - drawlist/opt: store rounded corners in texture to use 1 quad per corner (filled and wireframe) to lower the cost of rounding. (#1962)
 - drawlist/opt: AddRect() axis aligned pixel aligned (no-aa) could use 8 triangles instead of 16 and no normal calculation.
 - drawlist/opt: thick AA line could be doable in same number of triangles as 1.0 AA line by storing gradient+full color in atlas.

 - main: find a way to preserve relative orders of multiple reappearing windows (so an app toggling between "modes" e.g. fullscreen vs all tools) won't lose relative ordering.
 - main: IsItemHovered() make it more consistent for various type of widgets, widgets with multiple components, etc. also effectively IsHovered() region sometimes differs from hot region, e.g tree nodes
 - main: IsItemHovered() info stored in a stack? so that 'if TreeNode() { Text; TreePop; } if IsHovered' return the hover state of the TreeNode?

 - widgets: display mode: widget-label, label-widget (aligned on column or using fixed size), label-newline-tab-widget etc. (#395)
 - widgets: clean up widgets internal toward exposing everything and stabilizing imgui_internals.h.
 - widgets: add visuals for Disabled/ReadOnly mode and expose publicly (#211)
 - widgets: add always-allow-overlap mode. This should perhaps be the default? one problem is that highlight after mouse-wheel scrolling gets deferred, makes scrolling more flickery.
 - widgets: start exposing PushItemFlag() and ImGuiItemFlags
 - widgets: alignment options in style (e.g. center Selectable, Right-Align within Button, etc.) #1260
 - widgets: activate by identifier (trigger button, focus given id)
 - widgets: a way to represent "mixed" values, so e.g. all values replaced with *, including check-boxes, colors, etc. with support for multi-components widgets (e.g. SliderFloat3, make only "Y" mixed) (#2644)
 - widgets: selectable: generic BeginSelectable()/EndSelectable() mechanism.
 - widgets: selectable: a way to visualize partial/mixed selection (e.g. parent tree node has children with mixed selection)
 - widgets: checkbox: checkbox with custom glyph inside frame.
 - widgets: coloredit: keep reporting as active when picker is on?
 - widgets: group/scalarn functions: expose more per-component information. e.g. store NextItemData.ComponentIdx set by scalarn function, groups can expose them back somehow.

 - input text: clean up the mess caused by converting UTF-8 <> wchar. the code is rather inefficient right now and super fragile.
 - input text: reorganize event handling, allow CharFilter to modify buffers, allow multiple events? (#541)
 - input text: expose CursorPos in char filter event (#816)
 - input text: access public fields via a non-callback API e.g. InputTextGetState("xxx") that may return NULL if not active.
 - input text: flag to disable live update of the user buffer (also applies to float/int text input) (#701)
 - input text: hover tooltip could show unclamped text
 - input text: option to Tab after an Enter validation.
 - input text: add ImGuiInputTextFlags_EnterToApply? (off #218)
 - input text: easier ways to update buffer (from source char*) while owned. preserve some sort of cursor position for multi-line text.
 - input text: add discard flag (e.g. ImGuiInputTextFlags_DiscardActiveBuffer) or make it easier to clear active focus for text replacement during edition (#725)
 - input text: display bug when clicking a drag/slider after an input text in a different window has all-selected text (order dependent). actually a very old bug but no one appears to have noticed it.
 - input text: allow centering/positioning text so that ctrl+clicking Drag or Slider keeps the textual value at the same pixel position.
 - input text: decorrelate layout from inputs - e.g. what's the easiest way to implement a nice IP/Mac address input editor?
 - input text: global callback system so user can plug in an expression evaluator easily. (#1691)
 - input text: force scroll to end or scroll to a given line/contents (so user can implement a log or a search feature)
 - input text: a way to preview completion (e.g. disabled text completing from the cursor)
 - input text: a side bar that could e.g. preview where errors are. probably left to the user to draw but we'd need to give them the info there.
 - input text: a way for the user to provide syntax coloring.
 - input text: Shift+TAB with ImGuiInputTextFlags_AllowTabInput could eat preceding blanks, up to tab_count.
 - input text: facilitate patterns like if (InputText(..., obj.get_string_ref()) { obj.set_string(...); } relying on internally held buffer.
 - input text multi-line: don't directly call AddText() which does an unnecessary vertex reserve for character count prior to clipping. and/or more line-based clipping to AddText(). and/or reorganize TextUnformatted/RenderText for more efficiency for large text (e.g TextUnformatted could clip and log separately, etc).
 - input text multi-line: support for cut/paste without selection (cut/paste the current line)
 - input text multi-line: line numbers? status bar? (follow up on #200)
 - input text multi-line: behave better when user changes input buffer while editing is active (even though it is illegal behavior). namely, the change of buffer can create a scrollbar glitch (#725)
 - input text multi-line: better horizontal scrolling support (#383, #1224)
 - input text multi-line: single call to AddText() should be coarse clipped on InputTextEx() end.
 - input number: optional range min/max for Input*() functions
 - input number: holding [-]/[+] buttons could increase the step speed non-linearly (or user-controlled)
 - input number: use mouse wheel to step up/down
 - input number: applying arithmetics ops (+,-,*,/) messes up with text edit undo stack.

 - layout: helper or a way to express ImGui::SameLine(ImGui::GetCursorStartPos().x + ImGui::CalcItemWidth() + ImGui::GetStyle().ItemInnerSpacing.x); in a simpler manner.
 - layout: generalization of the above: a concept equivalent to word processor ruler tab stop ~ mini columns (position in X, no clipping implied) (vaguely relate to #267, #395, also what is used internally for menu items)
 - layout: horizontal layout helper (#97)
 - layout: horizontal flow until no space left (#404)
 - layout: more generic alignment state (left/right/centered) for single items?
 - layout: clean up the InputFloatN/SliderFloatN/ColorEdit4 layout code. item width should include frame padding.
 - layout: vertical alignment of mixed height items (e.g. buttons) within a same line (#1284)
 - layout: null layout mode were items are not rendered but user can query GetItemRectMin()/Max/Size.
 - layout: (R&D) local multi-pass layout mode.
 - layout: (R&D) bind authored layout data (created by an off-line tool), items fetch their pos/size at submission, self-optimize data structures to stable linear access.

 - group: BeginGroup() needs a border option. (~#1496)
 - group: IsHovered() after EndGroup() covers whole aabb rather than the intersection of individual items. Is that desirable?
 - group: merge deactivation/activation within same group (fwd WasEdited flag). (#2550)

 - columns: sizing policy (e.g. for each column: fixed size, %, fill, distribute default size among fills) (#513, #125)
 - columns: add a conditional parameter to SetColumnOffset() (#513, #125)
 - columns: headers. re-orderable. (#513, #125)
 - columns: optional sorting modifiers (up/down), sort list so sorting can be done multi-criteria. notify user when sort order changed.
 - columns: option to alternate background colors on odd/even scanlines.
 - columns: allow columns to recurse.
 - columns: allow a same columns set to be interrupted by e.g. CollapsingHeader and resume with columns in sync when moving them.
 - columns: sizing is lossy when columns width is very small (default width may turn negative etc.)
 - columns: separator function or parameter that works within the column (currently Separator() bypass all columns) (#125)
 - columns: flag to add horizontal separator above/below?
 - columns/layout: setup minimum line height (equivalent of automatically calling AlignFirstTextHeightToWidgets)

!- color: the color conversion helpers/types are a mess and needs sorting out.
 - color: (api breaking) ImGui::ColorConvertXXX functions should be loose ImColorConvertXX to match imgui_internals.h

 - plot: full featured plot/graph api w/ scrolling, zooming etc. all bell & whistle. why not!
 - plot: PlotLines() should use the polygon-stroke facilities, less vertices (currently issues with averaging normals)
 - plot: make it easier for user to draw extra stuff into the graph (e.g: draw basis, highlight certain points, 2d plots, multiple plots)
 - plot: "smooth" automatic scale over time, user give an input 0.0(full user scale) 1.0(full derived from value)
 - plot: option/feature: draw the zero line
 - plot: option/feature: draw grid, vertical markers
 - plot: option/feature: draw unit
 - plot: add a helper e.g. Plot(char* label, float value, float time_span=2.0f) that stores values and Plot them for you - probably another function name. and/or automatically allow to plot ANY displayed value (more reliance on stable ID)

 - clipper: ability to force display 1 item in the list would be convenient (for patterns where we need to set active id etc.)
 - clipper: ability to disable the clipping through a simple flag/bool.
 - clipper: ability to run without knowing full count in advance.
 - clipper: horizontal clipping support. (#2580)

 - separator: expose flags (#759)
 - separator: width, thickness, centering (#1643)
 - splitter: formalize the splitter idiom into an official api (we want to handle n-way split) (#319)

 - dock: merge docking branch (#2109)
 - dock: dock out from a collapsing header? would work nicely but need emitting window to keep submitting the code.

 - tabs: make EndTabBar fail if users doesn't respect BeginTabBar return value, for consistency/future-proofing.
 - tabs: persistent order/focus in BeginTabBar() api (#261, #351)
 - tabs: TabItem could honor SetNextItemWidth()?

 - image/image button: misalignment on padded/bordered button?
 - image/image button: parameters are confusing, image() has tint_col,border_col whereas imagebutton() has bg_col/tint_col. Even thou they are different parameters ordering could be more consistent. can we fix that?
 - image button: not taking an explicit id can be problematic. (#2464, #1390)
 - button: provide a button that looks framed. (?)
 - slider/drag: ctrl+click when format doesn't include a % character.. disable? display underlying value in default format? (see TempInputTextScalar)
 - slider: allow using the [-]/[+] buttons used by InputFloat()/InputInt()
 - slider: initial absolute click is imprecise. change to relative movement slider (same as scrollbar). (#1946)
 - slider: add dragging-based widgets to edit values with mouse (on 2 axises), saving screen real-estate.
 - slider: tint background based on value (e.g. v_min -> v_max, or use 0.0f either side of the sign)
 - slider: relative dragging? + precision dragging
 - slider: step option (#1183)
 - slider style: fill % of the bar instead of positioning a drag.
 - knob: rotating knob widget (#942)
 - drag float: power/logarithmic slider and drags are weird. (#1316)
 - drag float: up/down axis
 - drag float: power != 0.0f with current value being outside the range keeps the value stuck.
 - drag float: added leeway on edge (e.g. a few invisible steps past the clamp limits)

 - combo: use clipper: make it easier to disable clipper with a single flag.
 - combo: flag for BeginCombo to not return true when unchanged (#1182)
 - combo: a way/helper to customize the combo preview (#1658)
 - combo/listbox: keyboard control. need InputText-like non-active focus + key handling. considering keyboard for custom listbox (pr #203)
 - listbox: refactor and clean the begin/end api
 - listbox: multiple selection.
 - listbox: unselect option (#1208)
 - listbox: make it easier/more natural to implement range-select (need some sort of info/ref about the last clicked/focused item that user can translate to an index?) (wip stash)
 - listbox: user may want to initial scroll to focus on the one selected value?
 - listbox: expose hovered item for a basic ListBox
 - listbox: keyboard navigation.
 - listbox: disable capturing mouse wheel if the listbox has no scrolling. (#1681)
 - listbox: scrolling should track modified selection.
 - listbox: future api should allow to enable horizontal scrolling (#2510)

!- popups/menus: clarify usage of popups id, how MenuItem/Selectable closing parent popups affects the ID, etc. this is quite fishy needs improvement! (#331, #402)
 - popups/modal: make modal title bar blink when trying to click outside the modal
 - popups: reopening context menu at new position should be the behavior by default? (equivalent to internal OpenPopupEx() with reopen_existing=true) (~#1497)
 - popups: if the popup functions took explicit ImGuiID it would allow the user to manage the scope of those ID. (#331)
 - popups: clicking outside (to close popup) and holding shouldn't drag window below.
 - popups: add variant using global identifier similar to Begin/End (#402)
 - popups: border options. richer api like BeginChild() perhaps? (#197)
 - tooltip: drag and drop with tooltip near monitor edges lose/changes its last direction instead of locking one. The drag and drop tooltip should always follow without changing direction.
 - tooltip: tooltip that doesn't fit in entire screen seems to lose their "last preferred direction" and may teleport when moving mouse.
 - tooltip: allow to set the width of a tooltip to allow TextWrapped() etc. while keeping the height automatic.
 - tooltip: tooltips with delay timers? or general timer policy? (instantaneous vs timed): IsItemHovered() with timer + implicit aabb-id for items with no ID. (#1485)

 - menus: calling BeginMenu() twice with a same name doesn't append as Begin() does for regular windows (#1207)
 - menus: menu bars inside modal windows are acting weird.
 - status-bar: add a per-window status bar helper similar to what menu-bar does.
 - shortcuts: local-style shortcut api, e.g. parse "&Save"
 - shortcuts,menus: global-style shortcut api e.g. "Save (CTRL+S)" -> explicit flag for recursing into closed menu
 - shortcuts: programmatically access shortcuts "Focus("&Save"))
 - menus: menu-bar: main menu-bar could affect clamping of windows position (~ akin to modifying DisplayMin)
 - menus: hovering from menu to menu on a menu-bar has 1 frame without any menu, which is a little annoying. ideally either 0 either longer.
 - menus: could merge draw call in most cases (how about storing an optional aabb in ImDrawCmd to move the burden of merging in a single spot).

 - text: selectable text (for copy) as a generic feature (ItemFlags?)
 - text: proper alignment options in imgui_internal.h
 - text: it's currently impossible to have a window title with "##". perhaps an official workaround would be nice. \ style inhibitor? non-visible ascii code to insert between #?
 - text: provided a framed text helper, e.g. https://pastebin.com/1Laxy8bT
 - text: refactor TextUnformatted (or underlying function) to more explicitly request if we need width measurement or not
 - text link/url button: underlined. should api expose an ID or use text contents as ID? which colors enum to use?
 - text/wrapped: should be a more first-class citizen, e.g. wrapped text within a Selectable with known width
 - text/wrapped: figure out better way to use TextWrapped() in an always auto-resize context (tooltip, etc.) (#249)

 - tree node: add treenode/treepush int variants? not there because (void*) cast from int warns on some platforms/settings?
 - tree node: try to apply scrolling at time of TreePop() if node was just opened and end of node is past scrolling limits?
 - tree node / selectable render mismatch which is visible if you use them both next to each other (e.g. cf. property viewer)
 - tree node: tweak color scheme to distinguish headers from selected tree node (#581)
 - tree node: leaf/non-leaf highlight mismatch.
 - tree node: _NoIndentOnOpen flag? would require to store a per-depth bit mask to store info for pop (or whatever is cheaper)
 - tree node/opt: could avoid formatting when clipped (flag assuming we don't care about width/height, assume single line height?)

 - settings: write more decent code to allow saving/loading new fields: columns, selected tree nodes?
 - settings: api for per-tool simple persistent data (bool,int,float,columns sizes,etc.) in .ini file (#437)
 - settings/persistence: helpers to make TreeNodeBehavior persist (even during dev!) - may need to store some semantic and/or data type in ImGuiStoragePair

 - style: better default styles. (#707)
 - style: add a highlighted text color (for headers, etc.)
 - style: border types: out-screen, in-screen, etc. (#447)
 - style: add window shadow (fading away from the window. Paint-style calculation of vertices alpha after drawlist would be easier)
 - style: a concept of "compact style" that the end-user can easily rely on (e.g. PushStyleCompact()?) that maps to other settings? avoid implementing duplicate helpers such as SmallCheckbox(), etc.
 - style: try to make PushStyleVar() more robust to incorrect parameters (to be more friendly to edit & continues situation).
 - style: global scale setting.
 - style: FramePadding could be different for up vs down (#584)
 - style: WindowPadding needs to be EVEN as the 0.5 multiplier used on this value probably have a subtle effect on clip rectangle
 - style: have a more global HSV setter (e.g. alter hue on all elements). consider replacing active/hovered by offset in HSV space? (#438, #707, #1223)
 - style: gradients fill (#1223) ~ 2 bg colors for each fill? tricky with rounded shapes and using textures for corners.
 - style editor: color child window height expressed in multiple of line height.

 - log: have more control over the log scope (e.g. stop logging when leaving current tree node scope)
 - log: be able to log anything (e.g. right-click on a window/tree-node, shows context menu? log into tty/file/clipboard)
 - log: let user copy any window content to clipboard easily (CTRL+C on windows? while moving it? context menu?). code is commented because it fails with multiple Begin/End pairs.
 - log: obsolete LogButtons() all together.
 - log: LogButtons() options for specifying depth and/or hiding depth slider

 - filters: set a current filter that tree node can automatically query to hide themselves
 - filters: handle wild-cards (with implicit leading/trailing *), reg-exprs
 - filters: fuzzy matches (may use code at blog.forrestthewoods.com/4cffeed33fdb)

 - drag and drop: drag tooltip hovering over source widget with IsItemHovered/SetTooltip flickers.
 - drag and drop: fix/support/options for overlapping drag sources.
 - drag and drop: releasing a drop shows the "..." tooltip for one frame - since e13e598 (#1725)
 - drag and drop: drag source on a group object (would need e.g. an invisible button covering group in EndGroup) https://twitter.com/paniq/status/1121446364909535233
 - drag and drop: have some way to know when a drag begin from BeginDragDropSource() pov. (see 2018/01/11 post in #143)
 - drag and drop: allow preview tooltip to be submitted from a different place than the drag source. (#1725)
 - drag and drop: allow using with other mouse buttons (where activeid won't be set). (#1637)
 - drag and drop: make it easier and provide a demo to have tooltip both are source and target site, with a more detailed one on target site (tooltip ordering problem)
 - drag and drop: demo with reordering nodes (in a list, or a tree node). (#143)
 - drag and drop: test integrating with os drag and drop (make it easy to do a naive WM_DROPFILE integration)
 - drag and drop: allow for multiple payload types. (#143)
 - drag and drop: make payload optional? payload promise? (see 2018/01/11 post in #143)
 - drag and drop: (#143) "both an in-process pointer and a promise to generate a serialized version, for whether the drag ends inside or outside the same process"
 - drag and drop: feedback when hovering a region blocked by modal (mouse cursor "NO"?)

 - node/graph editors (#306) (also see https://github.com/ocornut/imgui/wiki#node-editors)
 - pie menus patterns (#434)
 - markup: simple markup language for color change? (#902)

 - font: MergeMode: flags to select overwriting or not (this is now very easy with refactored ImFontAtlasBuildWithStbTruetype)
 - font: free the Alpha buffer if user only requested RGBA.
!- font: better CalcTextSizeA() API, at least for simple use cases. current one is horrible (perhaps have simple vs extended versions).
 - font: for the purpose of RenderTextEllipsis(), it might be useful that CalcTextSizeA() can ignore the trailing padding?
 - font: a CalcTextHeight() helper could run faster than CalcTextSize().y
 - font: enforce monospace through ImFontConfig (for icons?) + create dual ImFont output from same input, reusing rasterized data but with different glyphs/AdvanceX
 - font: finish CustomRectRegister() to allow mapping Unicode codepoint to custom texture data
 - font: make it easier to submit own bitmap font (same texture, another texture?). (#2127, #2575)
 - font: PushFontSize API (#1018)
 - font: MemoryTTF taking ownership confusing/not obvious, maybe default should be opposite?
 - font: storing MinAdvanceX per font would allow us to skip calculating line width (under a threshold of character count) in loops looking for block width
 - font/demo: add tools to show glyphs used by a text blob, display U16 value, list missing glyphs.
 - font/demo: demonstrate use of ImFontGlyphRangesBuilder.
 - font/atlas: add a missing Glyphs.reserve()
 - font/atlas: incremental updates
 - font/atlas: dynamic font atlas to avoid baking huge ranges into bitmap and make scaling easier.
 - font/draw: vertical and/or rotated text renderer (#705) - vertical is easier clipping wise
 - font/draw: need to be able to specify wrap start position.
 - font/draw: better reserve policy for large horizontal block of text (shouldn't reserve for all clipped lines)
 - font/draw: underline, squiggle line rendering helpers.
 - font: optimization: for monospace font (like the default one) we can trim IndexXAdvance as long as trailing value is == FallbackXAdvance (need to make sure TAB is still correct), would save on cache line.
 - font: add support for kerning, probably optional. A) perhaps default to (32..128)^2 matrix ~ 9K entries = 36KB, then hash for non-ascii?. B) or sparse lookup into per-char list?
 - font: add a simpler CalcTextSizeA() api? current one ok but not welcome if user needs to call it directly (without going through ImGui::CalcTextSize)
 - font: fix AddRemapChar() to work before atlas  has been built.
 - font: support for unicode codepoints higher than 0xFFFF? (pr #2815)
 - font: (api breaking) remove "TTF" from symbol names. also because it now supports OTF.
 - font/opt: Considering storing standalone AdvanceX table as 16-bit fixed point integer?
 - font/opt: Glyph currently 40 bytes (2+9*4). Consider storing UV as 16 bits integer? (->32 bytes). X0/Y0/X1/Y1 as 16 fixed-point integers? Or X0/Y0 as float and X1/Y1 as fixed8_8?

 - nav: some features such as PageUp/Down/Home/End should probably work without ImGuiConfigFlags_NavEnableKeyboard? (where do we draw the line?)
 ! nav: never clear NavId on some setup (e.g. gamepad centric)
 - nav: restore NavId on reappearing non-child window.
 - nav: code to focus child-window on restoring NavId appears to have issue (to investigate)
 - nav: configuration flag to disable global shortcuts (currently only CTRL-Tab) ?
 - nav: Home/End behavior when navigable item is not fully visible at the edge of scrolling? should be backtrack to keep item into view?
 - nav: NavScrollToBringItemIntoView() with item bigger than view should focus top-right? Repro: using Nav in "About Window"
 - nav: wrap around logic to allow e.g. grid based layout (pressing NavRight on the right-most element would go to the next row, etc.). see internal's NavMoveRequestTryWrapping().
 - nav: patterns to make it possible for arrows key to update selection
 - nav: restore/find nearest NavId when current one disappear (e.g. pressed a button that disappear, or perhaps auto restoring when current button change name)
 - nav: SetItemDefaultFocus() level of priority, so widget like Selectable when inside a popup could claim a low-priority default focus on the first selected iem
 - nav: ESC within a menu of a child window seems to exit the child window.
 - nav: NavFlattened: ESC on a flattened child should select something.
 - nav: NavFlattened: broken: in typical usage scenario, the items of a fully clipped child are currently not considered to enter into a NavFlattened child.
 - nav: NavFlattened: init request doesn't select items that are part of a NavFlattened child
 - nav: NavFlattened: cannot access menu-bar of a flattened child window with Alt/menu key (not a very common use case..).
 - nav: Left within a tree node block as a fallback (ImGuiTreeNodeFlags_NavLeftJumpsBackHere by default?)
 - nav/menus: pressing left-right on a vertically clipped menu bar tends to jump to the collapse/close buttons.
 - nav/menus: allow pressing Menu to leave a sub-menu.
 - nav/menus: a way to access the main menu bar with Alt? (currently needs CTRL+TAB)
 - nav/menus: when using the main menu bar, even though we restore focus after, the underlying window loses its title bar highlight during menu manipulation. could we prevent it?
 - nav/menus: main menu bar currently cannot restore a NULL focus. Could save NavWindow at the time of being focused, similarly to what popup do?
 - nav: simulate right-click or context activation? (SHIFT+F10)
 - nav: tabs should go through most/all widgets (in submission order?).
 - nav: when CTRL-Tab/windowing is active, the HoveredWindow detection doesn't take account of the window display re-ordering.
 - nav: esc/enter default behavior for popups, e.g. be able to mark an "ok" or "cancel" button that would get triggered by those keys.
 - nav: when activating a button that changes label (without a static ID) or disappear, can we somehow automatically recover into a nearest highlight item?
 - nav: there's currently no way to completely clear focus with the keyboard. depending on patterns used by the application to dispatch inputs, it may be desirable.
 - focus: preserve ActiveId/focus stack state, e.g. when opening a menu and close it, previously selected InputText() focus gets restored (#622)
 - focus: SetKeyboardFocusHere() on with >= 0 offset could be done on same frame (else latch and modulate on beginning of next frame)
 - focus: unable to use SetKeyboardFocusHere() on clipped widgets. (#787)

 - inputs: we need an explicit flag about whether the imgui window is focused, to be able to distinguish focused key releases vs alt-tabbing all release behaviors.
 - inputs: rework IO system to be able to pass actual ordered/timestamped events. use an event queue? (~#335, #71)
 - inputs: support track pad style scrolling & slider edit.
 - inputs/io: backspace and arrows in the context of a text input could use system repeat rate.
 - inputs/io: clarify/standardize/expose repeat rate and repeat delays (#1808)
 - inputs/scrolling: support for smooth scrolling (#2462, #2569)

 - misc: idle: expose "woken up" boolean (set by inputs) and/or animation time (for cursor blink) for back-end to be able stop refreshing easily.
 - misc: idle: if cursor blink if the _only_ visible animation, core imgui could rewrite vertex alpha to avoid CPU pass on ImGui:: calls.
 - misc: idle: if cursor blink if the _only_ visible animation, could even expose a dirty rectangle that optionally can be leverage by some app to render in a smaller viewport, getting rid of much pixel shading cost.
 - misc: no way to run a root-most GetID() with ImGui:: api since there's always a Debug window in the stack. (mentioned in #2960)
 - misc: make the ImGuiCond values linear (non-power-of-two). internal storage for ImGuiWindow can use integers to combine into flags (Why?)
 - misc: provide a way to compile out the entire implementation while providing a dummy API (e.g. #define IMGUI_DUMMY_IMPL)
 - misc: PushItemFlag(): add a flag to disable keyboard capture when used with mouse? (#1682)
 - misc: use more size_t in public api?
 - misc: possible compile-time support for string view/range instead of char* would e.g. facilitate usage with Rust (#683)
 - misc: possible compile-time support for wchar_t instead of char*?

 - remote: make a system like RemoteImGui first-class citizen/project (#75)

 - demo: find a way to demonstrate textures in the examples application, as it such a common issue for new users.
 - demo: demonstrate using PushStyleVar() in more details.
 - demo: add vertical separator demo
 - demo: add virtual scrolling example?
 - demo: demonstrate Plot offset
 - demo: window size constraint: square demo is broken when resizing from edges (#1975), would need to rework the callback system to solve this

 - examples: window minimize, maximize (#583)
 - examples: provide a zero frame-rate/idle example.
 - backends: apple: example_apple should be using modern GL3.
 - backends: glfw: could go idle when minimized? if (glfwGetWindowAttrib(window, GLFW_ICONIFIED)) { glfwWaitEvents(); continue; } // issue: DeltaTime will be super high on resume, perhaps provide a way to let impl know (#440)
 - backends: opengl: rename imgui_impl_opengl2 to impl_opengl_legacy and imgui_impl_opengl3 to imgui_impl_opengl? (#1900)
 - backends: opengl: could use a single vertex buffer and glBufferSubData for uploads?
 - backends: opengl: explicitly disable GL_STENCIL_TEST in bindings.
 - backends: opengl: consider gl_lite loader https://github.com/ApoorvaJ/Papaya/blob/3808e39b0f45d4ca4972621c847586e4060c042a/src/libs/gl_lite.h
 - backends: vulkan: viewport: support for synchronized swapping of multiple swap chains.
 - backends: bgfx: https://gist.github.com/RichardGale/6e2b74bc42b3005e08397236e4be0fd0
 - backends: mscriptem: with refactored examples, we could provide a direct imgui_impl_emscripten platform layer (see eg. https://github.com/floooh/sokol-samples/blob/master/html5/imgui-emsc.cc#L42)

 - optimization: replace vsnprintf with stb_printf? or enable the defines/infrastructure to allow it (#1038)
 - optimization: add clipping for multi-component widgets (SliderFloatX, ColorEditX, etc.). one problem is that nav branch can't easily clip parent group when there is a move request.
 - optimization: add a flag to disable most of rendering, for the case where the user expect to skip it (#335)
 - optimization: fully covered window (covered by another with non-translucent bg + WindowRounding worth of padding) may want to clip rendering.
 - optimization: use another hash function than crc32, e.g. FNV1a
 - optimization/render: merge command-lists with same clip-rect into one even if they aren't sequential? (as long as in-between clip rectangle don't overlap)?
 - optimization: turn some the various stack vectors into statically-sized arrays
-----------------------------------------------------------------------
 dear imgui, v1.75 WIP
-----------------------------------------------------------------------
 examples/README.txt
 (This is the README file for the examples/ folder. See docs/ for more documentation)
-----------------------------------------------------------------------

Dear ImGui is highly portable and only requires a few things to run and render:

 - Providing mouse/keyboard inputs
 - Uploading the font atlas texture into graphics memory
 - Providing a render function to render indexed textured triangles
 - Optional: clipboard support, mouse cursor supports, Windows IME support, etc.

This is essentially what the example bindings in this folder are providing + obligatory portability cruft.

It is important to understand the difference between the core Dear ImGui library (files in the root folder)
and examples bindings which we are describing here (examples/ folder).
You should be able to write bindings for pretty much any platform and any 3D graphics API. With some extra
effort you can even perform the rendering remotely, on a different machine than the one running the logic.

This folder contains two things:

 - Example bindings for popular platforms/graphics API, which you can use as is or adapt for your own use.
   They are the imgui_impl_XXXX files found in the examples/ folder.

 - Example applications (standalone, ready-to-build) using the aforementioned bindings.
   They are the in the XXXX_example/ sub-folders.

You can find binaries of some of those example applications at:
  http://www.dearimgui.org/binaries


---------------------------------------
 MISC COMMENTS AND SUGGESTIONS
---------------------------------------

 - Read FAQ at http://dearimgui.org/faq

 - Please read 'PROGRAMMER GUIDE' in imgui.cpp for notes on how to setup Dear ImGui in your codebase.
   Please read the comments and instruction at the top of each file.

 - If you are using of the backend provided here, so you can copy the imgui_impl_xxx.cpp/h files
   to your project and use them unmodified. Each imgui_impl_xxxx.cpp comes with its own individual
   ChangeLog at the top of the .cpp files, so if you want to update them later it will be easier to
   catch up with what changed.

 - Dear ImGui has 0 to 1 frame of lag for most behaviors, at 60 FPS your experience should be pleasant.
   However, consider that OS mouse cursors are typically drawn through a specific hardware accelerated path
   and will feel smoother than common GPU rendered contents (including Dear ImGui windows).
   You may experiment with the io.MouseDrawCursor flag to request Dear ImGui to draw a mouse cursor itself,
   to visualize the lag between a hardware cursor and a software cursor. However, rendering a mouse cursor
   at 60 FPS will feel slow. It might be beneficial to the user experience to switch to a software rendered
   cursor only when an interactive drag is in progress.
   Note that some setup or GPU drivers are likely to be causing extra lag depending on their settings.
   If you feel that dragging windows feels laggy and you are not sure who to blame: try to build an
   application drawing a shape directly under the mouse cursor.


---------------------------------------
 EXAMPLE BINDINGS
---------------------------------------

Most the example bindings are split in 2 parts:

 - The "Platform" bindings, in charge of: mouse/keyboard/gamepad inputs, cursor shape, timing, windowing.
   Examples: Windows (imgui_impl_win32.cpp), GLFW (imgui_impl_glfw.cpp), SDL2 (imgui_impl_sdl.cpp), etc.

 - The "Renderer" bindings, in charge of: creating the main font texture, rendering imgui draw data.
   Examples: DirectX11 (imgui_impl_dx11.cpp), GL3 (imgui_impl_opengl3.cpp), Vulkan (imgui_impl_vulkan.cpp), etc.

 - The example _applications_ usually combine 1 platform + 1 renderer binding to create a working program.
   Examples: the example_win32_directx11/ application combines imgui_impl_win32.cpp + imgui_impl_dx11.cpp.

 - Some bindings for higher level frameworks carry both "Platform" and "Renderer" parts in one file.
   This is the case for Allegro 5 (imgui_impl_allegro5.cpp), Marmalade (imgui_impl_marmalade5.cpp).

 - If you use your own engine, you may decide to use some of existing bindings and/or rewrite some using
   your own API. As a recommendation, if you are new to Dear ImGui, try using the existing binding as-is
   first, before moving on to rewrite some of the code. Although it is tempting to rewrite both of the
   imgui_impl_xxxx files to fit under your coding style, consider that it is not necessary!
   In fact, if you are new to Dear ImGui, rewriting them will almost always be harder.

   Example: your engine is built over Windows + DirectX11 but you have your own high-level rendering
   system layered over DirectX11.
     Suggestion: step 1: try using imgui_impl_win32.cpp + imgui_impl_dx11.cpp first.
     Once this work, _if_ you want you can replace the imgui_impl_dx11.cpp code with a custom renderer
     using your own functions, etc.
     Please consider using the bindings to the lower-level platform/graphics API as-is.

   Example: your engine is multi-platform (consoles, phones, etc.), you have high-level systems everywhere.
     Suggestion: step 1: try using a non-portable binding first (e.g. win32 + underlying graphics API)!
     This is counter-intuitive, but this will get you running faster! Once you better understand how imgui
     works and is bound, you can rewrite the code using your own systems.

 - Road-map: Dear ImGui 1.80 (WIP currently in the "docking" branch) will allows imgui windows to be
   seamlessly detached from the main application window. This is achieved using an extra layer to the
   platform and renderer bindings, which allows Dear ImGui to communicate platform-specific requests.
   If you decide to use unmodified imgui_impl_xxxx.cpp files, you will automatically benefit from
   improvements and fixes related to viewports and platform windows without extra work on your side.


List of Platforms Bindings in this repository:

    imgui_impl_glfw.cpp       ; GLFW (Windows, macOS, Linux, etc.) http://www.glfw.org/
    imgui_impl_osx.mm         ; macOS native API (not as feature complete as glfw/sdl back-ends)
    imgui_impl_sdl.cpp        ; SDL2 (Windows, macOS, Linux, iOS, Android) https://www.libsdl.org
    imgui_impl_win32.cpp      ; Win32 native API (Windows)
    imgui_impl_glut.cpp       ; GLUT/FreeGLUT (absolutely not recommended in 2019)

List of Renderer Bindings in this repository:

    imgui_impl_dx9.cpp        ; DirectX9
    imgui_impl_dx10.cpp       ; DirectX10
    imgui_impl_dx11.cpp       ; DirectX11
    imgui_impl_dx12.cpp       ; DirectX12
    imgui_impl_metal.mm       ; Metal (with ObjC)
    imgui_impl_opengl2.cpp    ; OpenGL 2 (legacy, fixed pipeline <- don't use with modern OpenGL context)
    imgui_impl_opengl3.cpp    ; OpenGL 3/4, OpenGL ES 2, OpenGL ES 3 (modern programmable pipeline)
    imgui_impl_vulkan.cpp     ; Vulkan

List of high-level Frameworks Bindings in this repository: (combine Platform + Renderer)

    imgui_impl_allegro5.cpp
    imgui_impl_marmalade.cpp

Note that Dear ImGui works with Emscripten. The examples_emscripten/ app uses imgui_impl_sdl.cpp and
imgui_impl_opengl3.cpp, but other combinations are possible.

Third-party framework, graphics API and languages bindings are listed at:

    https://github.com/ocornut/imgui/wiki/Bindings

    Languages:
     C, C#, ChaiScript, CovScript, D, Go, Haxe/hxcpp, Java, JavaScript, Julia, Lua, Nim,
     Odin, Pascal, PureBasic, Python, Ruby, Rust, Swift...

    Frameworks:
     Amethyst, bsf, Cinder, Cocoa2d-x, Diligent Engine, Flexium, GML/GameMaker Studio,
     GTK3 + OpenGL, Irrlicht, Ogre, OpenSceneGraph/OSG, openFrameworks, Orx, LÖVE+LUA,
     Magnum, NanoRT, Nim Game Lib, px_render, Qt, Qt3d, SFML, Sokol, Unreal Engine 4, vtk...

    Miscellaneous: Software Renderer, RemoteImgui, imgui-ws, etc.

Not sure which to use?
Recommended platform/frameworks:

    GLFW    https://github.com/glfw/glfw        Use imgui_impl_glfw.cpp
    SDL2    https://www.libsdl.org              Use imgui_impl_sdl.cp
    Sokol   https://github.com/floooh/sokol     Use util/sokol_imgui.h in Sokol repository.

Those will allow you to create portable applications and will solve and abstract away many issues.


---------------------------------------
 EXAMPLE APPLICATIONS
---------------------------------------

Building:
  Unfortunately in 2018 it is still tedious to create and maintain portable build files using external
  libraries (the kind we're using here to create a window and render 3D triangles) without relying on
  third party software. For most examples here I choose to provide:
   - Makefiles for Linux/OSX
   - Batch files for Visual Studio 2008+
   - A .sln project file for Visual Studio 2010+
   - Xcode project files for the Apple examples
  Please let me know if they don't work with your setup!
  You can probably just import the imgui_impl_xxx.cpp/.h files into your own codebase or compile those
  directly with a command-line compiler.


example_allegro5/
    Allegro 5 example.
    = main.cpp + imgui_impl_allegro5.cpp

example_apple_metal/
    OSX & iOS + Metal.
    = main.m + imgui_impl_osx.mm + imgui_impl_metal.mm
    It is based on the "cross-platform" game template provided with Xcode as of Xcode 9.
    (NB: imgui_impl_osx.mm is currently not as feature complete as other platforms back-ends.
    You may prefer to use the GLFW Or SDL back-ends, which will also support Windows and Linux.)

example_apple_opengl2/
    OSX + OpenGL2.
    = main.mm + imgui_impl_osx.mm + imgui_impl_opengl2.cpp
    (NB: imgui_impl_osx.mm is currently not as feature complete as other platforms back-ends.
    You may prefer to use the GLFW Or SDL back-ends, which will also support Windows and Linux.)

example_empscripten:
    Emcripten + SDL2 + OpenGL3+/ES2/ES3 example.
    = main.cpp + imgui_impl_sdl.cpp + imgui_impl_opengl3.cpp
    Note that other examples based on SDL or GLFW + OpenGL could easily be modified to work with Emscripten.
    We provide this to make the Emscripten differences obvious, and have them not pollute all other examples.

example_glfw_metal/
    GLFW (Mac) + Metal example.
    = main.mm + imgui_impl_glfw.cpp + imgui_impl_metal.mm.

example_glfw_opengl2/
    GLFW + OpenGL2 example (legacy, fixed pipeline).
    = main.cpp + imgui_impl_glfw.cpp + imgui_impl_opengl2.cpp
    **DO NOT USE OPENGL2 CODE IF YOUR CODE/ENGINE IS USING MODERN OPENGL (SHADERS, VBO, VAO, etc.)**
    **Prefer using OPENGL3 code (with gl3w/glew/glad/glbindings, you can replace the OpenGL function loader)**
    This code is mostly provided as a reference to learn about Dear ImGui integration, because it is shorter.
    If your code is using GL3+ context or any semi modern OpenGL calls, using this renderer is likely to
    make things more complicated, will require your code to reset many OpenGL attributes to their initial
    state, and might confuse your GPU driver. One star, not recommended.

example_glfw_opengl3/
    GLFW (Win32, Mac, Linux) + OpenGL3+/ES2/ES3 example (programmable pipeline).
    = main.cpp + imgui_impl_glfw.cpp + imgui_impl_opengl3.cpp
    This uses more modern OpenGL calls and custom shaders.
    Prefer using that if you are using modern OpenGL in your application (anything with shaders).
    (Please be mindful that accessing OpenGL3+ functions requires a function loader, which are a frequent
    source for confusion for new users. We use a loader in imgui_impl_opengl3.cpp which may be different
    from the one your app normally use. Read imgui_impl_opengl3.h for details and how to change it.)

example_glfw_vulkan/
    GLFW (Win32, Mac, Linux) + Vulkan example.
    = main.cpp + imgui_impl_glfw.cpp + imgui_impl_vulkan.cpp
    This is quite long and tedious, because: Vulkan.
    For this example, the main.cpp file exceptionally use helpers function from imgui_impl_vulkan.h/cpp.

example_glut_opengl2/
    GLUT (e.g., FreeGLUT on Linux/Windows, GLUT framework on OSX) + OpenGL2.
    = main.cpp + imgui_impl_glut.cpp + imgui_impl_opengl2.cpp
    Note that GLUT/FreeGLUT is largely obsolete software, prefer using GLFW or SDL.

example_marmalade/
    Marmalade example using IwGx.
    = main.cpp + imgui_impl_marmalade.cpp

example_null
    Null example, compile and link imgui, create context, run headless with no inputs and no graphics output.
    = main.cpp
    This is used to quickly test compilation of core imgui files in as many setups as possible.
    Because this application doesn't create a window nor a graphic context, there's no graphics output.

example_sdl_directx11/
    SDL2 + DirectX11 example, Windows only.
    = main.cpp + imgui_impl_sdl.cpp + imgui_impl_dx11.cpp
    This to demonstrate usage of DirectX with SDL.

example_sdl_opengl2/
    SDL2 (Win32, Mac, Linux etc.) + OpenGL example (legacy, fixed pipeline).
    = main.cpp + imgui_impl_sdl.cpp + imgui_impl_opengl2.cpp
    **DO NOT USE OPENGL2 CODE IF YOUR CODE/ENGINE IS USING MODERN OPENGL (SHADERS, VBO, VAO, etc.)**
    **Prefer using OPENGL3 code (with gl3w/glew/glad/glbindings, you can replace the OpenGL function loader)**
    This code is mostly provided as a reference to learn about Dear ImGui integration, because it is shorter.
    If your code is using GL3+ context or any semi modern OpenGL calls, using this renderer is likely to
    make things more complicated, will require your code to reset many OpenGL attributes to their initial
    state, and might confuse your GPU driver. One star, not recommended.

example_sdl_opengl3/
    SDL2 (Win32, Mac, Linux, etc.) + OpenGL3+/ES2/ES3 example.
    = main.cpp + imgui_impl_sdl.cpp + imgui_impl_opengl3.cpp
    This uses more modern OpenGL calls and custom shaders.
    Prefer using that if you are using modern OpenGL in your application (anything with shaders).
    (Please be mindful that accessing OpenGL3+ functions requires a function loader, which are a frequent
    source for confusion for new users. We use a loader in imgui_impl_opengl3.cpp which may be different
    from the one your app normally use. Read imgui_impl_opengl3.h for details and how to change it.)

example_sdl_vulkan/
    SDL2 (Win32, Mac, Linux, etc.) + Vulkan example.
    = main.cpp + imgui_impl_sdl.cpp + imgui_impl_vulkan.cpp
    This is quite long and tedious, because: Vulkan.
    For this example, the main.cpp file exceptionally use helpers function from imgui_impl_vulkan.h/cpp.

example_win32_directx9/
    DirectX9 example, Windows only.
    = main.cpp + imgui_impl_win32.cpp + imgui_impl_dx9.cpp

example_win32_directx10/
    DirectX10 example, Windows only.
    = main.cpp + imgui_impl_win32.cpp + imgui_impl_dx10.cpp

example_win32_directx11/
    DirectX11 example, Windows only.
    = main.cpp + imgui_impl_win32.cpp + imgui_impl_dx11.cpp

example_win32_directx12/
    DirectX12 example, Windows only.
    = main.cpp + imgui_impl_win32.cpp + imgui_impl_dx12.cpp
    This is quite long and tedious, because: DirectX12.

# Configuration

Dear ImGui outputs 16-bit vertex indices by default.
Allegro doesn't support them natively, so we have two solutions: convert the indices manually in imgui_impl_allegro5.cpp, or compile dear imgui with 32-bit indices.
You can either modify imconfig.h that comes with Dear ImGui (easier), or set a C++ preprocessor option IMGUI_USER_CONFIG to find to a filename.
We are providing `imconfig_allegro5.h` that enables 32-bit indices.
Note that the back-end supports _BOTH_ 16-bit and 32-bit indices, but 32-bit indices will be slightly faster as they won't require a manual conversion.

# How to Build

### On Ubuntu 14.04+ and macOS

```bash
g++ -DIMGUI_USER_CONFIG=\"examples/example_allegro5/imconfig_allegro5.h\" -I .. -I ../.. main.cpp ../imgui_impl_allegro5.cpp ../../imgui*.cpp -lallegro -lallegro_main -lallegro_primitives -o allegro5_example
```

On macOS, install Allegro with homebrew: `brew install allegro`.

### On Windows with Visual Studio's CLI

You may install Allegro using vcpkg:
```
git clone https://github.com/Microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
.\vcpkg install allegro5
.\vcpkg integrate install    ; optional, automatically register include/libs in Visual Studio
```

Build:
```
set ALLEGRODIR=path_to_your_allegro5_folder
cl /Zi /MD /I %ALLEGRODIR%\include /DIMGUI_USER_CONFIG=\"examples/example_allegro5/imconfig_allegro5.h\" /I .. /I ..\.. main.cpp ..\imgui_impl_allegro5.cpp ..\..\imgui*.cpp /link /LIBPATH:%ALLEGRODIR%\lib allegro-5.0.10-monolith-md.lib user32.lib
```
# iOS / OSX Metal example

## Introduction

This example shows how to integrate Dear ImGui with Metal. It is based on the "cross-platform" game template provided with Xcode as of Xcode 9.

(NB: you may still want to use GLFW or SDL which will also support Windows, Linux along with OSX.)


# How to Build

- You need to install Emscripten from https://emscripten.org/docs/getting_started/downloads.html, and have the environment variables set, as described in https://emscripten.org/docs/getting_started/downloads.html#installation-instructions

- Depending on your configuration, in Windows you may need to run `emsdk/emsdk_env.bat` in your console to access the Emscripten command-line tools.

- Then build using `make` while in the `example_emscripten/` directory.

- Note that Emscripten 1.39.0 (October 2019) obsoleted the `BINARYEN_TRAP_MODE=clamp` compilation flag which was required with version older than 1.39.0 to avoid rendering artefacts. See [#2877](https://github.com/ocornut/imgui/issues/2877) for details. If you use an older version, uncomment this line in the Makefile:

`#EMS += -s BINARYEN_TRAP_MODE=clamp`
# Example usage:
#  mkdir build
#  cd build
#  cmake -g "Visual Studio 14 2015" ..

cmake_minimum_required(VERSION 2.8)
project(imgui_example_glfw_vulkan C CXX)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug CACHE STRING "" FORCE)
endif()

set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DVK_PROTOTYPES")
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DVK_PROTOTYPES")

# GLFW
set(GLFW_DIR ../../../glfw) # Set this to point to an up-to-date GLFW repo
option(GLFW_BUILD_EXAMPLES "Build the GLFW example programs" OFF)
option(GLFW_BUILD_TESTS "Build the GLFW test programs" OFF)
option(GLFW_BUILD_DOCS "Build the GLFW documentation" OFF)
option(GLFW_INSTALL "Generate installation target" OFF)
option(GLFW_DOCUMENT_INTERNALS "Include internals in documentation" OFF)
add_subdirectory(${GLFW_DIR} binary_dir EXCLUDE_FROM_ALL)
include_directories(${GLFW_DIR}/include)

# Dear ImGui
set(IMGUI_DIR ../../)
include_directories(${IMGUI_DIR} ..)

# Libraries
find_library(VULKAN_LIBRARY
  NAMES vulkan vulkan-1)
set(LIBRARIES "glfw;${VULKAN_LIBRARY}")

# Use vulkan headers from glfw:
include_directories(${GLFW_DIR}/deps)

file(GLOB sources *.cpp)

add_executable(example_glfw_vulkan ${sources} ${IMGUI_DIR}/examples/imgui_impl_glfw.cpp ${IMGUI_DIR}/examples/imgui_impl_vulkan.cpp ${IMGUI_DIR}/imgui.cpp ${IMGUI_DIR}/imgui_draw.cpp ${IMGUI_DIR}/imgui_demo.cpp ${IMGUI_DIR}/imgui_widgets.cpp)
target_link_libraries(example_glfw_vulkan ${LIBRARIES})

# How to Build

- On Windows with Visual Studio's CLI

```
set SDL2_DIR=path_to_your_sdl2_folder
cl /Zi /MD /I.. /I..\.. /I%SDL2_DIR%\include main.cpp ..\imgui_impl_sdl.cpp ..\imgui_impl_opengl2.cpp ..\..\imgui*.cpp /FeDebug/example_sdl_opengl2.exe /FoDebug/ /link /libpath:%SDL2_DIR%\lib\x86 SDL2.lib SDL2main.lib opengl32.lib /subsystem:console
#          ^^ include paths                  ^^ source files                                                           ^^ output exe                    ^^ output dir   ^^ libraries
# or for 64-bit:
cl /Zi /MD /I.. /I..\.. /I%SDL2_DIR%\include main.cpp ..\imgui_impl_sdl.cpp ..\imgui_impl_opengl2.cpp ..\..\imgui*.cpp /FeDebug/example_sdl_opengl2.exe /FoDebug/ /link /libpath:%SDL2_DIR%\lib\x64 SDL2.lib SDL2main.lib opengl32.lib /subsystem:console
```

- On Linux and similar Unixes

```
c++ `sdl2-config --cflags` -I .. -I ../.. main.cpp ../imgui_impl_sdl.cpp ../imgui_impl_opengl2.cpp ../../imgui*.cpp `sdl2-config --libs` -lGL
```

- On Mac OS X

```
brew install sdl2
c++ `sdl2-config --cflags` -I .. -I ../.. main.cpp ../imgui_impl_sdl.cpp ../imgui_impl_opengl2.cpp ../../imgui*.cpp `sdl2-config --libs` -framework OpenGl
```

# How to Build

- On Windows with Visual Studio's CLI

```
set SDL2_DIR=path_to_your_sdl2_folder
cl /Zi /MD /I.. /I..\.. /I%SDL2_DIR%\include /I..\libs\gl3w main.cpp ..\imgui_impl_sdl.cpp ..\imgui_impl_opengl3.cpp ..\..\imgui*.cpp ..\libs\gl3w\GL\gl3w.c /FeDebug/example_sdl_opengl3.exe /FoDebug/ /link /libpath:%SDL2_DIR%\lib\x86 SDL2.lib SDL2main.lib opengl32.lib /subsystem:console
#          ^^ include paths                                 ^^ source files                                                                                  ^^ output exe                    ^^ output dir   ^^ libraries
# or for 64-bit:
cl /Zi /MD /I.. /I..\.. /I%SDL2_DIR%\include /I..\libs\gl3w main.cpp ..\imgui_impl_sdl.cpp ..\imgui_impl_opengl3.cpp ..\..\imgui*.cpp ..\libs\gl3w\GL\gl3w.c /FeDebug/example_sdl_opengl3.exe /FoDebug/ /link /libpath:%SDL2_DIR%\lib\x64 SDL2.lib SDL2main.lib opengl32.lib /subsystem:console
```

- On Linux and similar Unixes

```
c++ `sdl2-config --cflags` -I .. -I ../.. -I ../libs/gl3w main.cpp ../imgui_impl_sdl.cpp ../imgui_impl_opengl3.cpp ../../imgui*.cpp ../libs/gl3w/GL/gl3w.c `sdl2-config --libs` -lGL -ldl
```

- On Mac OS X

```
brew install sdl2
c++ `sdl2-config --cflags` -I .. -I ../.. -I ../libs/gl3w main.cpp ../imgui_impl_sdl.cpp ../imgui_impl_opengl3.cpp ../../imgui*.cpp ../libs/gl3w/GL/gl3w.c `sdl2-config --libs` -framework OpenGl -framework CoreFoundation
```
Copyright (c) 2002-2006 Marcus Geelnard
Copyright (c) 2006-2010 Camilla Berglund <elmindreda@elmindreda.org>

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would
   be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and must not
   be misrepresented as being the original software.

3. This notice may not be removed or altered from any source
   distribution.


uSynergy client -- Implementation for the embedded Synergy client library
version 1.0.0, July 7th, 2012
Copyright (c) 2012 Alex Evans

This is a copy of the files once found at:
  https://github.com/symless/synergy-core/tree/790d108a56ada9caad8e56ff777d444485a69da9/src/micro


misc/cpp/
  InputText() wrappers for C++ standard library (STL) type: std::string.
  This is also an example of how you may wrap your own similar types.

misc/fonts/
  Fonts loading/merging instructions (e.g. How to handle glyph ranges, how to merge icons fonts).
  Command line tool "binary_to_compressed_c" to create compressed arrays to embed data in source code.
  Suggested fonts and links.

misc/freetype/
  Font atlas builder/rasterizer using FreeType instead of stb_truetype.
  Benefit from better FreeType rasterization, in particular for small fonts.

misc/natvis/
  Natvis file to describe dear imgui types in the Visual Studio debugger.
  With this, types like ImVector<> will be displayed nicely in the debugger.
  You can include this file a Visual Studio project file, or install it in Visual Studio folder.

misc/single_file/
  Single-file header stub.
  We use this to validate compiling all *.cpp files in a same compilation unit.
  Users of that technique (also called "Unity builds") can generally provide this themselves,
  so we don't really recommend you use this in your projects.

imgui_stdlib.h + imgui_stdlib.cpp
  InputText() wrappers for C++ standard library (STL) type: std::string.
  This is also an example of how you may wrap your own similar types.

imgui_scoped.h
  [Experimental, not currently in main repository]
  Additional header file with some RAII-style wrappers for common Dear ImGui functions.
  Try by merging: https://github.com/ocornut/imgui/pull/2197
  Discuss at: https://github.com/ocornut/imgui/issues/2096
# imgui_freetype

Build font atlases using FreeType instead of stb_truetype (which is the default font rasterizer in Dear ImGui).
<br>by @vuhdo, @mikesart, @ocornut.

### Usage

1. Get latest FreeType binaries or build yourself (under Windows you may use vcpkg with `vcpkg install freetype`).
2. Add imgui_freetype.h/cpp alongside your imgui sources.
3. Include imgui_freetype.h after imgui.h.
4. Call `ImGuiFreeType::BuildFontAtlas()` *BEFORE* calling `ImFontAtlas::GetTexDataAsRGBA32()` or `ImFontAtlas::Build()` (so normal Build() won't be called):

```cpp
// See ImGuiFreeType::RasterizationFlags
unsigned int flags = ImGuiFreeType::NoHinting;
ImGuiFreeType::BuildFontAtlas(io.Fonts, flags);
io.Fonts->GetTexDataAsRGBA32(&pixels, &width, &height);
```

### Gamma Correct Blending

FreeType assumes blending in linear space rather than gamma space.
See FreeType note for [FT_Render_Glyph](https://www.freetype.org/freetype2/docs/reference/ft2-base_interface.html#FT_Render_Glyph).
For correct results you need to be using sRGB and convert to linear space in the pixel shader output.
The default Dear ImGui styles will be impacted by this change (alpha values will need tweaking).

### Test code Usage
```cpp
#include "misc/freetype/imgui_freetype.h"
#include "misc/freetype/imgui_freetype.cpp"

// Load various small fonts
ImGuiIO& io = ImGui::GetIO();
io.Fonts->AddFontFromFileTTF("../../misc/fonts/Roboto-Medium.ttf", 13.0f);
io.Fonts->AddFontFromFileTTF("../../misc/fonts/Cousine-Regular.ttf", 13.0f);
io.Fonts->AddFontDefault();

FreeTypeTest freetype_test;

// Main Loop
while (true)
{
   if (freetype_test.UpdateRebuild())
   {
      // REUPLOAD FONT TEXTURE TO GPU
      ImGui_ImplXXX_DestroyDeviceObjects();
      ImGui_ImplXXX_CreateDeviceObjects();
   }
   ImGui::NewFrame();
   freetype_test.ShowFreetypeOptionsWindow();
   ...
}
```

### Test code
```cpp
#include "misc/freetype/imgui_freetype.h"
#include "misc/freetype/imgui_freetype.cpp"

struct FreeTypeTest
{
    enum FontBuildMode
    {
        FontBuildMode_FreeType,
        FontBuildMode_Stb
    };

    FontBuildMode BuildMode;
    bool          WantRebuild;
    float         FontsMultiply;
    int           FontsPadding;
    unsigned int  FontsFlags;

    FreeTypeTest()
    {
        BuildMode = FontBuildMode_FreeType;
        WantRebuild = true;
        FontsMultiply = 1.0f;
        FontsPadding = 1;
        FontsFlags = 0;
    }

    // Call _BEFORE_ NewFrame()
    bool UpdateRebuild()
    {
        if (!WantRebuild)
            return false;
        ImGuiIO& io = ImGui::GetIO();
        io.Fonts->TexGlyphPadding = FontsPadding;
        for (int n = 0; n < io.Fonts->ConfigData.Size; n++)
        {
            ImFontConfig* font_config = (ImFontConfig*)&io.Fonts->ConfigData[n];
            font_config->RasterizerMultiply = FontsMultiply;
            font_config->RasterizerFlags = (BuildMode == FontBuildMode_FreeType) ? FontsFlags : 0x00;
        }
        if (BuildMode == FontBuildMode_FreeType)
            ImGuiFreeType::BuildFontAtlas(io.Fonts, FontsFlags);
        else if (BuildMode == FontBuildMode_Stb)
            io.Fonts->Build();
        WantRebuild = false;
        return true;
    }

    // Call to draw interface
    void ShowFreetypeOptionsWindow()
    {
        ImGui::Begin("FreeType Options");
        ImGui::ShowFontSelector("Fonts");
        WantRebuild |= ImGui::RadioButton("FreeType", (int*)&BuildMode, FontBuildMode_FreeType);
        ImGui::SameLine();
        WantRebuild |= ImGui::RadioButton("Stb (Default)", (int*)&BuildMode, FontBuildMode_Stb);
        WantRebuild |= ImGui::DragFloat("Multiply", &FontsMultiply, 0.001f, 0.0f, 2.0f);
        WantRebuild |= ImGui::DragInt("Padding", &FontsPadding, 0.1f, 0, 16);
        if (BuildMode == FontBuildMode_FreeType)
        {
            WantRebuild |= ImGui::CheckboxFlags("NoHinting",     &FontsFlags, ImGuiFreeType::NoHinting);
            WantRebuild |= ImGui::CheckboxFlags("NoAutoHint",    &FontsFlags, ImGuiFreeType::NoAutoHint);
            WantRebuild |= ImGui::CheckboxFlags("ForceAutoHint", &FontsFlags, ImGuiFreeType::ForceAutoHint);
            WantRebuild |= ImGui::CheckboxFlags("LightHinting",  &FontsFlags, ImGuiFreeType::LightHinting);
            WantRebuild |= ImGui::CheckboxFlags("MonoHinting",   &FontsFlags, ImGuiFreeType::MonoHinting);
            WantRebuild |= ImGui::CheckboxFlags("Bold",          &FontsFlags, ImGuiFreeType::Bold);
            WantRebuild |= ImGui::CheckboxFlags("Oblique",       &FontsFlags, ImGuiFreeType::Oblique);
            WantRebuild |= ImGui::CheckboxFlags("Monochrome",    &FontsFlags, ImGuiFreeType::Monochrome);
        }
        ImGui::End();
    }
};
```

### Known issues
- `cfg.OversampleH`, `OversampleV` are ignored (but perhaps not so necessary with this rasterizer).


Natvis file to describe dear imgui types in the Visual Studio debugger.
With this, types like ImVector<> will be displayed nicely in the debugger.
You can include this file a Visual Studio project file, or install it in Visual Studio folder.
