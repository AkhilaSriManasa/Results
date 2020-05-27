# Change Log

## [Unreleased](https://github.com/find-sec-bugs/find-sec-bugs/tree/HEAD)

[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.6.0...HEAD)

**Closed issues:**

- Run coveralls after each build [\#287](https://github.com/find-sec-bugs/find-sec-bugs/issues/287)

**Merged pull requests:**

- Version 1.6.0 to 1.7.0 [\#286](https://github.com/find-sec-bugs/find-sec-bugs/pull/286) ([h3xstream](https://github.com/h3xstream))

## [version-1.6.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.6.0) (2017-03-15)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.5.0...version-1.6.0)

**Implemented enhancements:**

- Unexpected deserialization with RestEasy/Jersey [\#198](https://github.com/find-sec-bugs/find-sec-bugs/issues/198)
- Turbine SQL Injection [\#238](https://github.com/find-sec-bugs/find-sec-bugs/issues/238)
- Detect hardcoded password in unknown API [\#231](https://github.com/find-sec-bugs/find-sec-bugs/issues/231)
- Malicious deserialization from LDAP entry [\#228](https://github.com/find-sec-bugs/find-sec-bugs/issues/228)
- \(Dev internal\) Validate the configuration files automatically [\#158](https://github.com/find-sec-bugs/find-sec-bugs/issues/158)
- Turbine SQL injections [\#253](https://github.com/find-sec-bugs/find-sec-bugs/pull/253) ([h3xstream](https://github.com/h3xstream))
- Adding overly permissive CORS policy detector [\#248](https://github.com/find-sec-bugs/find-sec-bugs/pull/248) ([plr0man](https://github.com/plr0man))
- LDAP improvements [\#278](https://github.com/find-sec-bugs/find-sec-bugs/pull/278) ([h3xstream](https://github.com/h3xstream))
- Add HTTP Parameter Pollution Injection Detector [\#267](https://github.com/find-sec-bugs/find-sec-bugs/pull/267) ([plr0man](https://github.com/plr0man))
- Add File Disclosure Injection detector [\#265](https://github.com/find-sec-bugs/find-sec-bugs/pull/265) ([plr0man](https://github.com/plr0man))
- Java source and target from 1.6 to 1.7 & API compatibility check [\#264](https://github.com/find-sec-bugs/find-sec-bugs/pull/264) ([ptamarit](https://github.com/ptamarit))
- Add JavaBeans Property Injection detector [\#263](https://github.com/find-sec-bugs/find-sec-bugs/pull/263) ([plr0man](https://github.com/plr0man))
- Add Insecure SMTP SSL detector [\#259](https://github.com/find-sec-bugs/find-sec-bugs/pull/259) ([plr0man](https://github.com/plr0man))
- SQL Injection \(CWE-89\) - Scala Slick & Scala Anorm injection detectors [\#254](https://github.com/find-sec-bugs/find-sec-bugs/pull/254) ([MaxNad](https://github.com/MaxNad))
- Add Url rewriting detector [\#252](https://github.com/find-sec-bugs/find-sec-bugs/pull/252) ([plr0man](https://github.com/plr0man))
- UNENCRYPTED\_SERVER\_SOCKET: use of java.net.ServerSocket [\#239](https://github.com/find-sec-bugs/find-sec-bugs/pull/239) ([edrdo](https://github.com/edrdo))
- Server Side Request Forgery \(CWE 918\) - Basic detector implementation [\#234](https://github.com/find-sec-bugs/find-sec-bugs/pull/234) ([MaxNad](https://github.com/MaxNad))

**Fixed bugs:**

- Out of bounds mutables in ... \(Assertion trigged\) [\#275](https://github.com/find-sec-bugs/find-sec-bugs/issues/275)
- Force encoding to UTF-8 on windows when generating micro-website [\#232](https://github.com/find-sec-bugs/find-sec-bugs/issues/232)
- Freemarker description fix [\#230](https://github.com/find-sec-bugs/find-sec-bugs/issues/230)
- Bug fix of detection of bad cipher modes of operation and minor improvements [\#271](https://github.com/find-sec-bugs/find-sec-bugs/pull/271) ([formanek](https://github.com/formanek))

**Closed issues:**

- Find-sec-bugs maven plugin failed to execute [\#274](https://github.com/find-sec-bugs/find-sec-bugs/issues/274)
- False negatives in detection of bad modes of operation [\#270](https://github.com/find-sec-bugs/find-sec-bugs/issues/270)
- findbugs not working with Sonarqube 6.1 [\#235](https://github.com/find-sec-bugs/find-sec-bugs/issues/235)
- Update JSP compiler  [\#279](https://github.com/find-sec-bugs/find-sec-bugs/issues/279)

**Merged pull requests:**

- Remove duplicated word in README [\#282](https://github.com/find-sec-bugs/find-sec-bugs/pull/282) ([jwilk](https://github.com/jwilk))
- Update JSP compiler [\#281](https://github.com/find-sec-bugs/find-sec-bugs/pull/281) ([h3xstream](https://github.com/h3xstream))
- Fix \#275 [\#277](https://github.com/find-sec-bugs/find-sec-bugs/pull/277) ([h3xstream](https://github.com/h3xstream))
- Add Format String Manipulation Injection Detector [\#266](https://github.com/find-sec-bugs/find-sec-bugs/pull/266) ([plr0man](https://github.com/plr0man))
- Travis improvements: batch mode and verify phase [\#262](https://github.com/find-sec-bugs/find-sec-bugs/pull/262) ([ptamarit](https://github.com/ptamarit))
- Add AWS Query Injection detector [\#260](https://github.com/find-sec-bugs/find-sec-bugs/pull/260) ([plr0man](https://github.com/plr0man))
- Fix false negatives in InsufficientKeySizeRsaDetector [\#257](https://github.com/find-sec-bugs/find-sec-bugs/pull/257) ([plr0man](https://github.com/plr0man))
- Fix false negative SHA in WeakMessageDigestDetector [\#255](https://github.com/find-sec-bugs/find-sec-bugs/pull/255) ([plr0man](https://github.com/plr0man))
- Persistent cookie detector [\#251](https://github.com/find-sec-bugs/find-sec-bugs/pull/251) ([plr0man](https://github.com/plr0man))
- Anonymous LDAP Bind detector [\#250](https://github.com/find-sec-bugs/find-sec-bugs/pull/250) ([plr0man](https://github.com/plr0man))
- Fix Maven warnings \(missing plugin version, relocation, proprietary API\) [\#247](https://github.com/find-sec-bugs/find-sec-bugs/pull/247) ([ptamarit](https://github.com/ptamarit))
- Adding ThreadLocalRandom detection [\#246](https://github.com/find-sec-bugs/find-sec-bugs/pull/246) ([plr0man](https://github.com/plr0man))
- Improve SpringMvcEndpointDetector by detecting new RequestMapping annotation shortcuts [\#244](https://github.com/find-sec-bugs/find-sec-bugs/pull/244) ([ptamarit](https://github.com/ptamarit))
- Update plugins \#279 [\#280](https://github.com/find-sec-bugs/find-sec-bugs/pull/280) ([h3xstream](https://github.com/h3xstream))
- Spring CSRF: Protection Disabled & Unrestricted RequestMapping [\#261](https://github.com/find-sec-bugs/find-sec-bugs/pull/261) ([ptamarit](https://github.com/ptamarit))
- \(internal\) Refactoring: Rename Summary to TaintConfig [\#258](https://github.com/find-sec-bugs/find-sec-bugs/pull/258) ([h3xstream](https://github.com/h3xstream))

## [version-1.5.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.5.0) (2016-10-06)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.6...version-1.5.0)

**Implemented enhancements:**

- Detect template usage \(template injection\) [\#227](https://github.com/find-sec-bugs/find-sec-bugs/issues/227)
- Reduce the number of FP related to Trust Boundary Violation [\#226](https://github.com/find-sec-bugs/find-sec-bugs/issues/226)
- XSS in Portlet [\#216](https://github.com/find-sec-bugs/find-sec-bugs/issues/216)
- How to set findsecbugs.taint.customconfigfile through gradle? [\#215](https://github.com/find-sec-bugs/find-sec-bugs/issues/215)
- Identify weak XML parser properties that could lead to XXE [\#209](https://github.com/find-sec-bugs/find-sec-bugs/issues/209)
- Scala : XSS in twirl template [\#207](https://github.com/find-sec-bugs/find-sec-bugs/issues/207)
- Scala: XSS in Play controller [\#206](https://github.com/find-sec-bugs/find-sec-bugs/issues/206)
- XML parsing vulnerable to XXE \(XMLReader\) shortage [\#191](https://github.com/find-sec-bugs/find-sec-bugs/issues/191)
- Path Traversal \(CWE 22\) - Scala Path Traversal injection sinks [\#223](https://github.com/find-sec-bugs/find-sec-bugs/pull/223) ([MaxNad](https://github.com/MaxNad))
- Sensitive data exposure \(CWE 200\) - Sensitive data exposure in cookies [\#221](https://github.com/find-sec-bugs/find-sec-bugs/pull/221) ([MaxNad](https://github.com/MaxNad))
- XSS \(CWE 79\) - Scala - The detector can be fooled when the .as\("text/html"\) is in uppercase [\#208](https://github.com/find-sec-bugs/find-sec-bugs/pull/208) ([MaxNad](https://github.com/MaxNad))
- Taint analysis bug fixes and improvements [\#214](https://github.com/find-sec-bugs/find-sec-bugs/pull/214) ([topolik](https://github.com/topolik))
- Potential fix for issue \#182 \(INSECURE\_COOKIE detector can be fooled by creating two or more cookies\) [\#204](https://github.com/find-sec-bugs/find-sec-bugs/pull/204) ([MaxNad](https://github.com/MaxNad))
- XSS \(CWE 79\) - Scala Play vulnerable code [\#203](https://github.com/find-sec-bugs/find-sec-bugs/pull/203) ([MaxNad](https://github.com/MaxNad))
- CWE 200 \(Information Exposure\) - Scala Play vulnerable code [\#202](https://github.com/find-sec-bugs/find-sec-bugs/pull/202) ([MaxNad](https://github.com/MaxNad))

**Fixed bugs:**

- FP: sending local broadcasts via LocalBroadcastManager [\#224](https://github.com/find-sec-bugs/find-sec-bugs/issues/224)
- False positive: ResourceBundle in JSP [\#213](https://github.com/find-sec-bugs/find-sec-bugs/issues/213)
- Out of bounds mutables in static myclass$.\<clinit\>\(\)V [\#199](https://github.com/find-sec-bugs/find-sec-bugs/issues/199)
- Issue \#224 - Added an exception for the LocalBroadcastManager in the detector. [\#225](https://github.com/find-sec-bugs/find-sec-bugs/pull/225) ([MaxNad](https://github.com/MaxNad))
- Potential fix for issue \\#182 \\(INSECURE\\_COOKIE detector can be fooled by creating two or more cookies\\) [\#204](https://github.com/find-sec-bugs/find-sec-bugs/pull/204) ([MaxNad](https://github.com/MaxNad))

**Closed issues:**

- not to report null-porter dereference if there is code already throws RuntimeError [\#197](https://github.com/find-sec-bugs/find-sec-bugs/issues/197)
- Release version 1.4.6 [\#195](https://github.com/find-sec-bugs/find-sec-bugs/issues/195)
- Release 1.4.5 [\#159](https://github.com/find-sec-bugs/find-sec-bugs/issues/159)
- Fix mix-content on micro-website [\#229](https://github.com/find-sec-bugs/find-sec-bugs/issues/229)

**Merged pull requests:**

- Custom config file method refactoring [\#218](https://github.com/find-sec-bugs/find-sec-bugs/pull/218) ([topolik](https://github.com/topolik))
- Accept environment variables spelled with underscores [\#217](https://github.com/find-sec-bugs/find-sec-bugs/pull/217) ([kuhnmi](https://github.com/kuhnmi))

## [version-1.4.6](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.6) (2016-06-02)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.5...version-1.4.6)

**Implemented enhancements:**

- Detect deserialization gadgets [\#189](https://github.com/find-sec-bugs/find-sec-bugs/issues/189)
- CustomInjection issues [\#172](https://github.com/find-sec-bugs/find-sec-bugs/issues/172)
- New Rule : XSLT processing detection [\#168](https://github.com/find-sec-bugs/find-sec-bugs/issues/168)
- Better sink confirmation mechanism, safe fields [\#173](https://github.com/find-sec-bugs/find-sec-bugs/pull/173) ([formanek](https://github.com/formanek))
- Credentials detector for Hashtable improved [\#155](https://github.com/find-sec-bugs/find-sec-bugs/pull/155) ([mcwww](https://github.com/mcwww))
- Update owasp.txt [\#188](https://github.com/find-sec-bugs/find-sec-bugs/pull/188) ([s-tikhomirov](https://github.com/s-tikhomirov))
- Correct japanese messages formatting [\#185](https://github.com/find-sec-bugs/find-sec-bugs/pull/185) ([marcosbento](https://github.com/marcosbento))
- Support for sanitization using replace methods in String [\#171](https://github.com/find-sec-bugs/find-sec-bugs/pull/171) ([formanek](https://github.com/formanek))
- Taint tags for injections, proper tag derivation, added and fixed summaries [\#169](https://github.com/find-sec-bugs/find-sec-bugs/pull/169) ([formanek](https://github.com/formanek))
- Taint tags - support for taint sanitization \(starting with XSS\) [\#166](https://github.com/find-sec-bugs/find-sec-bugs/pull/166) ([formanek](https://github.com/formanek))
- Fix typo in taint-config/java-lang.txt [\#157](https://github.com/find-sec-bugs/find-sec-bugs/pull/157) ([apasel422](https://github.com/apasel422))

**Fixed bugs:**

- find-sec-bugs always claims "The following classes needed for analysis were missing" for enums  [\#176](https://github.com/find-sec-bugs/find-sec-bugs/issues/176)
- Memory leak in the tests [\#193](https://github.com/find-sec-bugs/find-sec-bugs/issues/193)
- Test failure : Invalid VNA after location [\#192](https://github.com/find-sec-bugs/find-sec-bugs/issues/192)
- java.util.ConcurrentModificationException during analysis [\#184](https://github.com/find-sec-bugs/find-sec-bugs/issues/184)
- CustomInjection issues [\#172](https://github.com/find-sec-bugs/find-sec-bugs/issues/172)
- FindSecBugs plugin crash in Intellij [\#167](https://github.com/find-sec-bugs/find-sec-bugs/issues/167)
- Fixed exception, debug info to visitGETFIELD, formatting [\#156](https://github.com/find-sec-bugs/find-sec-bugs/pull/156) ([formanek](https://github.com/formanek))

**Closed issues:**

- No plugin support for findbugs4sbt [\#181](https://github.com/find-sec-bugs/find-sec-bugs/issues/181)
- Fixing the build [\#180](https://github.com/find-sec-bugs/find-sec-bugs/issues/180)
- Standalone execution [\#179](https://github.com/find-sec-bugs/find-sec-bugs/issues/179)
- AbstractInjectionDetector.checkTaintSink\(\) modifies Set\<TaintSink\> while iterating over it [\#177](https://github.com/find-sec-bugs/find-sec-bugs/issues/177)
- Make the test less verbose [\#194](https://github.com/find-sec-bugs/find-sec-bugs/issues/194)

**Merged pull requests:**

- Safe enums, dates, time and context path + javadoc [\#190](https://github.com/find-sec-bugs/find-sec-bugs/pull/190) ([formanek](https://github.com/formanek))
- New analysis parameters and extended taint config [\#187](https://github.com/find-sec-bugs/find-sec-bugs/pull/187) ([formanek](https://github.com/formanek))
- Add Struts DynaValidatorForm support in addition to ValidatorForm [\#178](https://github.com/find-sec-bugs/find-sec-bugs/pull/178) ([mkienenb](https://github.com/mkienenb))
- Fix URL shown for CUSTOM\_INJECTION bug warning [\#174](https://github.com/find-sec-bugs/find-sec-bugs/pull/174) ([mkienenb](https://github.com/mkienenb))

## [version-1.4.5](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.5) (2016-01-05)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.4...version-1.4.5)

**Implemented enhancements:**

- Play framework demo [\#154](https://github.com/find-sec-bugs/find-sec-bugs/issues/154)
- New Rule : Scala Command injection [\#153](https://github.com/find-sec-bugs/find-sec-bugs/issues/153)
- New Rule : Unvalidated redirect in Play Framework [\#152](https://github.com/find-sec-bugs/find-sec-bugs/issues/152)
- New Rule : Additional coverage for predictable random generator in Scala [\#151](https://github.com/find-sec-bugs/find-sec-bugs/issues/151)
- New Rule: Detect weak HostnameVerifier [\#150](https://github.com/find-sec-bugs/find-sec-bugs/issues/150)
- Migrate the old XSS detector to the new TaintDetector mecanism [\#149](https://github.com/find-sec-bugs/find-sec-bugs/issues/149)
- Support alternative bytecode for setEscapeXml="false" JSP \(Weblogic appc\) [\#148](https://github.com/find-sec-bugs/find-sec-bugs/issues/148)
- \(Dev internal\) DSL for more intuitive method matching [\#147](https://github.com/find-sec-bugs/find-sec-bugs/issues/147)
- New Rule : Missing HttpOnly flag on cookie [\#144](https://github.com/find-sec-bugs/find-sec-bugs/issues/144)
- New Rule : Trust Boundary Violation [\#133](https://github.com/find-sec-bugs/find-sec-bugs/issues/133)
- Taint analysis : Add taint parameters annotate \(RequestParam, PathVariable, ..\) [\#132](https://github.com/find-sec-bugs/find-sec-bugs/issues/132)
- New Rule : EL Expression Injection [\#130](https://github.com/find-sec-bugs/find-sec-bugs/issues/130)
- New Rule : XSS detector using the taint detector approach [\#129](https://github.com/find-sec-bugs/find-sec-bugs/issues/129)
- \(Dev internal\) Debug info for taint value to allow troubleshooting of the stack [\#81](https://github.com/find-sec-bugs/find-sec-bugs/issues/81)
- New Rule : Seam Logger usage could lead to remote code execution [\#56](https://github.com/find-sec-bugs/find-sec-bugs/issues/56)
- New Rule: Detect SSL disabler \(Java  + Scala implementation\) [\#34](https://github.com/find-sec-bugs/find-sec-bugs/issues/34)
- Change description of cryptography plus bad grammar [\#146](https://github.com/find-sec-bugs/find-sec-bugs/pull/146) ([mcwww](https://github.com/mcwww))
- Correct SonarQube product name [\#142](https://github.com/find-sec-bugs/find-sec-bugs/pull/142) ([agabrys](https://github.com/agabrys))
- Analysis of indirect subclasses of HttpServlet for XSS [\#137](https://github.com/find-sec-bugs/find-sec-bugs/pull/137) ([formanek](https://github.com/formanek))

**Fixed bugs:**

- Fix code bloc in description for multiples Bug Patterns : JSP\_INCLUDE, JSP\_SPRING\_EVAL and JSP\_JSTL\_OUT [\#131](https://github.com/find-sec-bugs/find-sec-bugs/issues/131)
- Hard coded keys false positive when loading bytes from FileInputStream [\#126](https://github.com/find-sec-bugs/find-sec-bugs/issues/126)
- Description for weak digest need an update [\#119](https://github.com/find-sec-bugs/find-sec-bugs/issues/119)
- Error scanning Scala code in IntelliJ [\#112](https://github.com/find-sec-bugs/find-sec-bugs/issues/112)

**Merged pull requests:**

- Change to description [\#145](https://github.com/find-sec-bugs/find-sec-bugs/pull/145) ([mcwww](https://github.com/mcwww))
- Properly handle paths to files [\#136](https://github.com/find-sec-bugs/find-sec-bugs/pull/136) ([jsotuyod](https://github.com/jsotuyod))
- Fixed hard coded keys detector and out-of-bounds index in TaintAnalysis [\#135](https://github.com/find-sec-bugs/find-sec-bugs/pull/135) ([formanek](https://github.com/formanek))

## [version-1.4.4](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.4) (2015-11-20)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.3...version-1.4.4)

**Implemented enhancements:**

- Path traversal and Xpath injection detectors should use taint analysis [\#97](https://github.com/find-sec-bugs/find-sec-bugs/issues/97)
- Detector for external control of configuration \(CWE-15\) [\#124](https://github.com/find-sec-bugs/find-sec-bugs/issues/124)
- Detector for CRLF injection in logs \(CWE-117\) [\#123](https://github.com/find-sec-bugs/find-sec-bugs/issues/123)
- Detector for HTTP response splitting [\#121](https://github.com/find-sec-bugs/find-sec-bugs/issues/121)
- New Rule : JSTL out escapeXml=false [\#114](https://github.com/find-sec-bugs/find-sec-bugs/issues/114)
- Improvements for JSP support [\#110](https://github.com/find-sec-bugs/find-sec-bugs/issues/110)
- Add taint sinks for XPath injection [\#108](https://github.com/find-sec-bugs/find-sec-bugs/issues/108)
- Missing taint sinks for LDAP Injection [\#105](https://github.com/find-sec-bugs/find-sec-bugs/issues/105)
- New rule : Detect dynamic JSP Includes [\#104](https://github.com/find-sec-bugs/find-sec-bugs/issues/104)
- Standalone command line tool to scan jars with or without the source [\#100](https://github.com/find-sec-bugs/find-sec-bugs/issues/100)
- Better support for collections [\#99](https://github.com/find-sec-bugs/find-sec-bugs/issues/99)
- Consider inheritance for method summaries [\#98](https://github.com/find-sec-bugs/find-sec-bugs/issues/98)
- Refactor injection detectors [\#96](https://github.com/find-sec-bugs/find-sec-bugs/issues/96)
- New Rule : Detect Spring Eval JSP taglib [\#55](https://github.com/find-sec-bugs/find-sec-bugs/issues/55)
- Add detector for java object deserialization [\#127](https://github.com/find-sec-bugs/find-sec-bugs/pull/127) ([minlex](https://github.com/minlex))

**Fixed bugs:**

- Path traversal false positives [\#113](https://github.com/find-sec-bugs/find-sec-bugs/issues/113)

**Closed issues:**

- mvn compile failing after adding findsecbugs-plugin [\#128](https://github.com/find-sec-bugs/find-sec-bugs/issues/128)
- Add methods for weak message digest [\#120](https://github.com/find-sec-bugs/find-sec-bugs/issues/120)
- How can I mark / exclude false positives? [\#116](https://github.com/find-sec-bugs/find-sec-bugs/issues/116)
- Missing taint sinks for Spring SQL injection [\#109](https://github.com/find-sec-bugs/find-sec-bugs/issues/109)
- Method arguments are not tainted if their derived summary is stored  [\#106](https://github.com/find-sec-bugs/find-sec-bugs/issues/106)
- Push release 1.4.3 to upstream projects [\#101](https://github.com/find-sec-bugs/find-sec-bugs/issues/101)

**Merged pull requests:**

- CRLF in loggers and taint analysis improvements [\#125](https://github.com/find-sec-bugs/find-sec-bugs/pull/125) ([formanek](https://github.com/formanek))
- Response splitting, hash functions and messages [\#122](https://github.com/find-sec-bugs/find-sec-bugs/pull/122) ([formanek](https://github.com/formanek))
- Refactored and fixed injection detectors [\#115](https://github.com/find-sec-bugs/find-sec-bugs/pull/115) ([formanek](https://github.com/formanek))
- Inheritance aware taint analysis, extended collections support [\#107](https://github.com/find-sec-bugs/find-sec-bugs/pull/107) ([formanek](https://github.com/formanek))
- Fix injection copy. [\#102](https://github.com/find-sec-bugs/find-sec-bugs/pull/102) ([mweiden](https://github.com/mweiden))

## [version-1.4.3](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.3) (2015-09-16)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.2...version-1.4.3)

**Implemented enhancements:**

- All Runtime.exec methods should be taint sinks [\#92](https://github.com/find-sec-bugs/find-sec-bugs/issues/92)
- Add coverage for LDAP injection [\#89](https://github.com/find-sec-bugs/find-sec-bugs/issues/89)
- Improve the detection of weak message digest [\#88](https://github.com/find-sec-bugs/find-sec-bugs/issues/88)
- Improve the detection in the use of old ciphers [\#87](https://github.com/find-sec-bugs/find-sec-bugs/issues/87)
- Insecure cookie [\#86](https://github.com/find-sec-bugs/find-sec-bugs/issues/86)
- Spring JDBC API [\#74](https://github.com/find-sec-bugs/find-sec-bugs/issues/74)
- JDBC api coverage [\#73](https://github.com/find-sec-bugs/find-sec-bugs/issues/73)
- False positive on Static IV when using Cipher.getIv\(\) [\#62](https://github.com/find-sec-bugs/find-sec-bugs/issues/62)
- Improved taint analysis \(several bugs fixed, refactoring\) [\#91](https://github.com/find-sec-bugs/find-sec-bugs/pull/91) ([formanek](https://github.com/formanek))

**Fixed bugs:**

- Parametric taint state not changed when used as an argument of an unknown method [\#90](https://github.com/find-sec-bugs/find-sec-bugs/issues/90)
- Bad method summaries derived for complex flow [\#85](https://github.com/find-sec-bugs/find-sec-bugs/issues/85)
- Invalid taint modifications of local variables, when loaded from method summary [\#84](https://github.com/find-sec-bugs/find-sec-bugs/issues/84)
- Taint not transfered in chained call of StringBuilder.append [\#83](https://github.com/find-sec-bugs/find-sec-bugs/issues/83)
- Too many iterations bug [\#82](https://github.com/find-sec-bugs/find-sec-bugs/issues/82)
- Issue with constructor with List and array as parameter \(Command injection detection\) [\#80](https://github.com/find-sec-bugs/find-sec-bugs/issues/80)
- Fix DES detection [\#79](https://github.com/find-sec-bugs/find-sec-bugs/issues/79)
- EntityManager createQuery trips SECSQLIJPA even with safe usage [\#76](https://github.com/find-sec-bugs/find-sec-bugs/issues/76)
- The IV generation should only be verified for the encryption mode [\#64](https://github.com/find-sec-bugs/find-sec-bugs/issues/64)

**Merged pull requests:**

- Fixed incomplete candidate method for LDAP injections [\#94](https://github.com/find-sec-bugs/find-sec-bugs/pull/94) ([formanek](https://github.com/formanek))
- Added command injection sinks and CWE identifiers [\#93](https://github.com/find-sec-bugs/find-sec-bugs/pull/93) ([formanek](https://github.com/formanek))
- Unknown methods made to modify taint state of their parameters to unknown [\#78](https://github.com/find-sec-bugs/find-sec-bugs/pull/78) ([formanek](https://github.com/formanek))
- Global taint analysis, improvements and bug fixes [\#75](https://github.com/find-sec-bugs/find-sec-bugs/pull/75) ([formanek](https://github.com/formanek))

## [version-1.4.2](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.2) (2015-08-18)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.1...version-1.4.2)

**Implemented enhancements:**

- Improve taint analysis to avoid SQL Injection detected when StringBuilder is used [\#14](https://github.com/find-sec-bugs/find-sec-bugs/issues/14)

**Fixed bugs:**

- Remove slash from XXE short message [\#68](https://github.com/find-sec-bugs/find-sec-bugs/issues/68)

**Merged pull requests:**

- Refactoring of classes for taint analysis [\#71](https://github.com/find-sec-bugs/find-sec-bugs/pull/71) ([formanek](https://github.com/formanek))
- Translate a message of HARD\_CODE\_KEY pattern. [\#70](https://github.com/find-sec-bugs/find-sec-bugs/pull/70) ([naokikimura](https://github.com/naokikimura))
- Taint sources locations added to bug reports [\#69](https://github.com/find-sec-bugs/find-sec-bugs/pull/69) ([formanek](https://github.com/formanek))
- Separated hard coded password and key reporting [\#67](https://github.com/find-sec-bugs/find-sec-bugs/pull/67) ([formanek](https://github.com/formanek))
- Taint sources and improved taint transfer [\#66](https://github.com/find-sec-bugs/find-sec-bugs/pull/66) ([formanek](https://github.com/formanek))
- Improved hardcoded passwords and key detector + taint analysis [\#63](https://github.com/find-sec-bugs/find-sec-bugs/pull/63) ([formanek](https://github.com/formanek))
- Allow analyze to set classpath entries [\#60](https://github.com/find-sec-bugs/find-sec-bugs/pull/60) ([mbmihura](https://github.com/mbmihura))
- website: corrected typos [\#59](https://github.com/find-sec-bugs/find-sec-bugs/pull/59) ([obilodeau](https://github.com/obilodeau))

## [version-1.4.1](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.1) (2015-05-30)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.4.0...version-1.4.1)

**Implemented enhancements:**

- Detector hard coded Spring OAuth secret key [\#57](https://github.com/find-sec-bugs/find-sec-bugs/issues/57)
- Add CWE references to messages \(few missing\) [\#52](https://github.com/find-sec-bugs/find-sec-bugs/issues/52)
- Create a tutorial for IntelliJ IDE [\#51](https://github.com/find-sec-bugs/find-sec-bugs/issues/51)
- Create a japanese page on the micro-website for the bug patterns [\#50](https://github.com/find-sec-bugs/find-sec-bugs/issues/50)
- NetBeans tutorial [\#45](https://github.com/find-sec-bugs/find-sec-bugs/issues/45)
- Update the documentation for Sonar Qube [\#44](https://github.com/find-sec-bugs/find-sec-bugs/issues/44)
- ECB and no integrity detection + tests [\#53](https://github.com/find-sec-bugs/find-sec-bugs/pull/53) ([formanek](https://github.com/formanek))
- Detector for hard coded passwords and cryptographic keys [\#46](https://github.com/find-sec-bugs/find-sec-bugs/pull/46) ([formanek](https://github.com/formanek))

**Fixed bugs:**

- XXE - reader False Positive [\#47](https://github.com/find-sec-bugs/find-sec-bugs/issues/47)
- Fix URLs in messages.xml [\#43](https://github.com/find-sec-bugs/find-sec-bugs/issues/43)
- CustomInjectionSource.properties not found [\#42](https://github.com/find-sec-bugs/find-sec-bugs/issues/42)

**Merged pull requests:**

- Update messages\_ja.xml [\#49](https://github.com/find-sec-bugs/find-sec-bugs/pull/49) ([naokikimura](https://github.com/naokikimura))

## [version-1.4.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.4.0) (2015-04-03)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.3.1...version-1.4.0)

**Implemented enhancements:**

- Support java 8 - upgrade to findbugs 3.0.0 or higher. [\#37](https://github.com/find-sec-bugs/find-sec-bugs/issues/37)
- New Android Security detectors [\#39](https://github.com/find-sec-bugs/find-sec-bugs/issues/39)
- Move command injection to the main injection detector mecanism [\#33](https://github.com/find-sec-bugs/find-sec-bugs/issues/33)
- Create messages\_ja.xml [\#38](https://github.com/find-sec-bugs/find-sec-bugs/pull/38) ([naokikimura](https://github.com/naokikimura))
- Enable additional signatures to detector of injection [\#36](https://github.com/find-sec-bugs/find-sec-bugs/pull/36) ([naokikimura](https://github.com/naokikimura))

## [version-1.3.1](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.3.1) (2015-02-23)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.3.0...version-1.3.1)

**Implemented enhancements:**

- Add supports for the new URL specification for bug reference [\#35](https://github.com/find-sec-bugs/find-sec-bugs/issues/35)
- Higher priority for injections [\#32](https://github.com/find-sec-bugs/find-sec-bugs/issues/32)
- Remove ESAPI references in messages [\#31](https://github.com/find-sec-bugs/find-sec-bugs/issues/31)
- XXE - Separate guidelines \(XMLReader/SaxParser/DocumentParser\) [\#27](https://github.com/find-sec-bugs/find-sec-bugs/issues/27)
- XXE - Avoid false positive when secure features are set. [\#26](https://github.com/find-sec-bugs/find-sec-bugs/issues/26)
- Fix links in the descriptions [\#25](https://github.com/find-sec-bugs/find-sec-bugs/issues/25)
- JDO Query - Potential Injections [\#23](https://github.com/find-sec-bugs/find-sec-bugs/issues/23)
- JDO PersistenceManager - Potential Injections [\#22](https://github.com/find-sec-bugs/find-sec-bugs/issues/22)
- Hibernate Restrictions API - Potential Injections [\#21](https://github.com/find-sec-bugs/find-sec-bugs/issues/21)

**Fixed bugs:**

- MethodUnprofitableException throwing could be suppressed [\#29](https://github.com/find-sec-bugs/find-sec-bugs/issues/29)
- Fix links in the descriptions [\#25](https://github.com/find-sec-bugs/find-sec-bugs/issues/25)
- CipherWithNoIntegrityDetector throws exception on algorithm-only cipher lookups [\#24](https://github.com/find-sec-bugs/find-sec-bugs/issues/24)
- Copy all files in metadata folder [\#30](https://github.com/find-sec-bugs/find-sec-bugs/pull/30) ([jsotuyod](https://github.com/jsotuyod))

## [version-1.3.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.3.0) (2015-01-02)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.2.1...version-1.3.0)

**Implemented enhancements:**

- Tag 1.2.1 release [\#18](https://github.com/find-sec-bugs/find-sec-bugs/issues/18)

## [version-1.2.1](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.2.1) (2014-10-03)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.2.0...version-1.2.1)

**Implemented enhancements:**

- SQL injection on JPA EntityManager.createNativeQuery\(\) is not checked [\#15](https://github.com/find-sec-bugs/find-sec-bugs/issues/15)
- Add scala.util.Random to PredictableRandomDetector [\#17](https://github.com/find-sec-bugs/find-sec-bugs/pull/17) ([HairyFotr](https://github.com/HairyFotr))

**Fixed bugs:**

- The BAD\_HEXA\_CONVERSION detector seems to have issues when UnconditionalValueDerefAnalysis is run later [\#12](https://github.com/find-sec-bugs/find-sec-bugs/issues/12)
- Parent POM referenced but not published to Maven Central [\#11](https://github.com/find-sec-bugs/find-sec-bugs/issues/11)

## [version-1.2.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.2.0) (2013-10-30)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.1.0...version-1.2.0)

**Fixed bugs:**

- Findbugs Security Plugin [\#5](https://github.com/find-sec-bugs/find-sec-bugs/issues/5)
- Clarify the test scope of test dependencies. [\#13](https://github.com/find-sec-bugs/find-sec-bugs/pull/13) ([dbaxa](https://github.com/dbaxa))

## [version-1.1.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.1.0) (2013-07-11)
[Full Changelog](https://github.com/find-sec-bugs/find-sec-bugs/compare/version-1.0.0...version-1.1.0)

**Implemented enhancements:**

- Various fixes for findbugs.xml, messages.xml and ECB detection [\#9](https://github.com/find-sec-bugs/find-sec-bugs/pull/9) ([samuelreed](https://github.com/samuelreed))

**Fixed bugs:**

- NullPointerException at BadHexadecimalConversionDetector.java:65 [\#3](https://github.com/find-sec-bugs/find-sec-bugs/issues/3)
- Bug fix for BadHexadecimalConversionDetector [\#4](https://github.com/find-sec-bugs/find-sec-bugs/pull/4) ([pcavezzan](https://github.com/pcavezzan))
- Removed duplicate entry of bug pattern SERVLET\_HEADER. [\#1](https://github.com/find-sec-bugs/find-sec-bugs/pull/1) ([uhafner](https://github.com/uhafner))

## [version-1.0.0](https://github.com/find-sec-bugs/find-sec-bugs/tree/version-1.0.0) (2012-10-20)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*# How to contribute

## Submitting an issue

If you are submitting an issue, here are key points to keep in mind.

### Fatal Error

 - Include stack trace
 - Code sample to reproduce
 - Configuration (if appropriate)

### False positive

 - Provide Java/Scala/Groovy code to reproduce the issue
 - Explain why the vulnerability should not have been triggered

### New detector idea

 - Make sure it can be applied to more than one application
 - Provide: Vulnerable code, False positive and Solution

## Creating a Pull Request

 - The build is still passing `mvn clean install`
 - You have created test cases for new detector or signatures
 - Your pull request will be link in the release notes. Make sure the description is clear for the **users** 

## Find Security Bugs internals

If you want to learn more about Find Security Bugs internals, you read the wiki pages under the section [Developers corner](https://github.com/find-sec-bugs/find-sec-bugs/wiki#wrench-developers-corner).
${project}
Copyright (c) ${owner}, All rights reserved.

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library.                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.
                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.
# OWASP Find Security Bugs 
[![Build Status](https://secure.travis-ci.org/find-sec-bugs/find-sec-bugs.png?branch=master)](http://travis-ci.org/find-sec-bugs/find-sec-bugs) [![codecov](https://codecov.io/gh/find-sec-bugs/find-sec-bugs/branch/master/graph/badge.svg)](https://codecov.io/gh/find-sec-bugs/find-sec-bugs) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.h3xstream.findsecbugs/findsecbugs-plugin/badge.svg)](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.h3xstream.findsecbugs%22%20a%3A%22findsecbugs-plugin%22) [![Slack Channel](https://img.shields.io/badge/slack-OWASP%2ffind--sec--bugs-orange?logo=slack)](https://app.slack.com/client/T04T40NHX/CN8G79Y6P)


Find Security Bugs is the [SpotBugs](https://spotbugs.github.io/) plugin for security audits of Java web applications.

Website : http://find-sec-bugs.github.io/

## Main developers

 - [Philippe Arteau](https://github.com/h3xstream) from [GoSecure](https://github.com/gosecure)
 - [David Formánek](https://github.com/formanek)
 - [Tomáš Polešovský](https://github.com/topolik) from [Liferay](https://github.com/liferay)

## Notable contributions

 - [David Formánek](https://github.com/formanek)
   - Major improvements and refactoring on the taint analysis for injections.
   - The creation of a detector for hard coded passwords and cryptographic keys.
 - [Tomáš Polešovský](https://github.com/topolik)
   - Improvements and bug fixes related to the taint analysis.
 - [Maxime Nadeau](https://github.com/MaxNad)
   - New detectors surrounding the Play Framework and improvements related to Scala.
 - [Naoki Kimura](https://github.com/naokikimura)
   - Detector for [injection in custom API](http://h3xstream.github.io/find-sec-bugs/bugs.htm#CUSTOM_INJECTION)
   - Translation of [messages in Japanese](http://h3xstream.github.io/find-sec-bugs/bugs_ja.htm)
 - [Dave Wichers](https://github.com/davewichers)
   - Improvement to vulnerability descriptions

## Project Sponsors

The development of Find Security Bugs is supported by [GoSecure](https://github.com/gosecure) since 2016. The support includes the development of new detectors and the research for new vulnerability classes.

![GoSecure Logo](website/out_web/images/gosecure.png)

## Screenshots

### Eclipse

![Eclipse](https://find-sec-bugs.github.io/images/screens/eclipse.png)

### IntelliJ / Android Studio

![IntelliJ](https://find-sec-bugs.github.io/images/screens/intellij.png)

### SonarQube

![SonarQube](https://find-sec-bugs.github.io/images/screens/sonar.png)

## License

This software is release under [LGPL](http://www.gnu.org/licenses/lgpl.html).
---
name: Bug report
about: The scanner is not working as expected

---

## Environment

<!-- The versions used: Gradle 4.5/4.6, Maven 3.5.X, Java 7/8/9, SpotBugs 3.1.6/..., FindSecBugs 1.8.0/.. -->

| Component          | Version |
| ------------------ | ------- |
| Maven              | ?????   |
| Gradle             | ?????   |
| Java               | ?????   |
| SpotBugs           | ?????   |
| FindSecBugs        | ?????   |

## Problem

<!-- Include the elements that applied:
     - Description of the expected behavior and the actual result.
     - Stacktrace
     - Maven/Gradle/Ant output
-->

## Code (If needed)

<!-- Include the Java code samples or ZIP files of a sample project that reproduce the given bug. -->

```java
public class BugSample1 {
  public static void hello(String message) {
       
    //Something
    Runnable r = () -> System.out.println(message);
   
    r.run();
  }
}
```
---
name: Feature request
about: New detector, new API to cover, new option, new anything

---

## Description

<!-- Include the elements that applied:
     - Description of the new vulnerability class
     - Link to the vulnerability class
     - API signature that need to be added
     - Link to Javadoc/Source of API
-->

## Code (If needed)

<!-- Include the Java code samples or ZIP files of a sample project that describe the new vulnerability. -->

```java
public class BugSample1 {
  public static void hello(String message) {
       
    //Something
    Runnable r = () -> System.out.println(message);
   
    r.run();
  }
}
```
---
name: Support
about: Questions for _existing_ features

---

<!--

If you have a question regarding existing features or if you need support,
please ask the question on StackOverflow :
https://stackoverflow.com/questions/ask?tags=find-sec-bugs,spotbugs,java

-->
# Find Security Bugs - Command Line Version

The latest package version is made available in the release section : https://github.com/find-sec-bugs/find-sec-bugs/releases

## Building the package

1. Update the version of the latest release of Find Security Bugs and SpotBugs in `gradle.properties`

2. Run the following command

```
gradle packageCli
```

This should produce a zip archive with a portable version of Find Security Bugs (`findsecbugs-cli-*.zip`).


The spotbugs dependencies and the latest FindSecurityBugs plugin will be place in the lib directory.
The lib directory need to be clear manually if the versions are changed from the gradle build file.
com/amazonaws/services/simpledb/model/SelectRequest.<init>(Ljava/lang/String;)V:0
com/amazonaws/services/simpledb/model/SelectRequest.<init>(Ljava/lang/String;Ljava/lang/Boolean;)V:1
com/amazonaws/services/simpledb/model/SelectRequest.withSelectExpression(Ljava/lang/String;)Lcom/amazonaws/services/simpledb/model/SelectRequest;:0org/apache/commons/beanutils/BeanUtils.populate(Ljava/lang/Object;Ljava/util/Map;)V:0
org/apache/commons/beanutils/BeanUtilsBean.populate(Ljava/lang/Object;Ljava/util/Map;)V:0scala/sys/process/Process$.apply(Ljava/lang/String;)Lscala/sys/process/ProcessBuilder;:0
scala/sys/process/Process$.apply(Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0
scala/sys/process/Process$.apply(Ljava/lang/String;Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0,1
scala/sys/process/Process$.apply(Ljava/lang/String;Ljava/io/File;Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0,2
scala/sys/process/Process$.apply(Lscala/collection/Seq;Ljava/io/File;Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0,2
scala/sys/process/Process$.apply(Ljava/lang/String;Lscala/Option;Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0,2
scala/sys/process/Process$.apply(Lscala/collection/Seq;Lscala/Option;Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0,2
scala/sys/process/Process$.apply(Ljava/lang/String;Lscala/Function0;)Lscala/sys/process/ProcessBuilder;:1
scala/sys/process/Process$.apply(Lscala/collection/Seq;Lscala/Function1;)Lscala/collection/Seq;:0,1

-stringToProcess is call when the bang operator (!) is apply to a string
scala/sys/process/package$.stringToProcess(Ljava/lang/String;)Lscala/sys/process/ProcessBuilder;:0
scala/sys/process/package$.stringSeqToProcess(Lscala/collection/Seq;)Lscala/sys/process/ProcessBuilder;:0
java/lang/Runtime.exec(Ljava/lang/String;)Ljava/lang/Process;:0
java/lang/Runtime.exec([Ljava/lang/String;)Ljava/lang/Process;:0
java/lang/Runtime.exec(Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/Process;:0,1
java/lang/Runtime.exec([Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/Process;:0,1
java/lang/Runtime.exec(Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)Ljava/lang/Process;:1,2
java/lang/Runtime.exec([Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)Ljava/lang/Process;:1,2

java/lang/ProcessBuilder.<init>([Ljava/lang/String;)V:0
java/lang/ProcessBuilder.<init>(Ljava/util/List;)V:0
java/lang/ProcessBuilder.command([Ljava/lang/String;)Ljava/lang/ProcessBuilder;:0
java/lang/ProcessBuilder.command(Ljava/util/List;)Ljava/lang/ProcessBuilder;:0
java/util/logging/Logger.config(Ljava/lang/String;)V:0
java/util/logging/Logger.entering(Ljava/lang/String;Ljava/lang/String;)V:0,1
java/util/logging/Logger.entering(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:0,1,2
java/util/logging/Logger.entering(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V:0,1,2
java/util/logging/Logger.exiting(Ljava/lang/String;Ljava/lang/String;)V:0,1
java/util/logging/Logger.exiting(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:0,1,2
java/util/logging/Logger.fine(Ljava/lang/String;)V:0
java/util/logging/Logger.finer(Ljava/lang/String;)V:0
java/util/logging/Logger.finest(Ljava/lang/String;)V:0
java/util/logging/Logger.info(Ljava/lang/String;)V:0
java/util/logging/Logger.log(Ljava/util/logging/Level;Ljava/lang/String;)V:0
java/util/logging/Logger.log(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/Object;)V:0,1
java/util/logging/Logger.log(Ljava/util/logging/Level;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
java/util/logging/Logger.log(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/Throwable;)V:1
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,1,2
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:0,1,2,3
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V:0,1,2,3
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V:1,2,3
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/util/function/Supplier;)V:1,2
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;Ljava/util/function/Supplier;)V:2,3
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/util/ResourceBundle;Ljava/lang/String;[Ljava/lang/Object;)V:0,1,3,4
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/util/ResourceBundle;Ljava/lang/String;Ljava/lang/Throwable;)V:1,3,4
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,2,3
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:0,1,3,4
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V:0,1,3,4
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V:1,3,4
java/util/logging/Logger.severe(Ljava/lang/String;)V:0
java/util/logging/Logger.throwing(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V:1,2
java/util/logging/Logger.warning(Ljava/lang/String;)V:0

org/apache/commons/logging/Log.debug(Ljava/lang/Object;)V:0
org/apache/commons/logging/Log.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/commons/logging/Log.error(Ljava/lang/Object;)V:0
org/apache/commons/logging/Log.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/commons/logging/Log.fatal(Ljava/lang/Object;)V:0
org/apache/commons/logging/Log.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/commons/logging/Log.info(Ljava/lang/Object;)V:0
org/apache/commons/logging/Log.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/commons/logging/Log.trace(Ljava/lang/Object;)V:0
org/apache/commons/logging/Log.trace(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/commons/logging/Log.warn(Ljava/lang/Object;)V:0
org/apache/commons/logging/Log.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:1

org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;)V:0
org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.debug(Ljava/lang/String;)V:0
org/slf4j/Logger.debug(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.debug(Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.debug(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.debug(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;)V:0
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.error(Ljava/lang/String;)V:0
org/slf4j/Logger.error(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.error(Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.error(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.error(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;)V:0
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.info(Ljava/lang/String;)V:0
org/slf4j/Logger.info(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.info(Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.info(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.info(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;)V:0
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.trace(Ljava/lang/String;)V:0
org/slf4j/Logger.trace(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.trace(Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.trace(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.trace(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;)V:0
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/slf4j/Logger.warn(Ljava/lang/String;)V:0
org/slf4j/Logger.warn(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/slf4j/Logger.warn(Ljava/lang/String;Ljava/lang/Object;)V:0,1
org/slf4j/Logger.warn(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:0,1,2
org/slf4j/Logger.warn(Ljava/lang/String;Ljava/lang/Throwable;)V:1

org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.debug(Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.debug(Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.debug(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.debug(Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.debug(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.entry([Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.error(Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.error(Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.error(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.error(Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.error(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.fatal(Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.fatal(Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.fatal(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.fatal(Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.fatal(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.info(Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.info(Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.info(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.info(Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.info(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/slf4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/slf4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.printf(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.printf(Lorg/apache/logging/log4j/Level;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.trace(Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.trace(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.trace(Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.trace(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.trace(Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.trace(Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.warn(Ljava/lang/Object;)V:0
org/apache/logging/log4j/Logger.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/logging/log4j/Logger.warn(Ljava/lang/String;)V:0
org/apache/logging/log4j/Logger.warn(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/apache/logging/log4j/Logger.warn(Ljava/lang/String;Lorg/apache/logging/log4j/util/Supplier;)V:1
org/apache/logging/log4j/Logger.warn(Ljava/lang/String;Ljava/lang/Throwable;)V:1

org/apache/log4j/Category.debug(Ljava/lang/Object;)V:0
org/apache/log4j/Category.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Category.error(Ljava/lang/Object;)V:0
org/apache/log4j/Category.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Category.fatal(Ljava/lang/Object;)V:0
org/apache/log4j/Category.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Category.info(Ljava/lang/Object;)V:0
org/apache/log4j/Category.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Category.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Throwable;)V:1,2
org/apache/log4j/Category.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/log4j/Category.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;)V:0
org/apache/log4j/Category.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Category.log(Ljava/lang/String;Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:1,3
org/apache/log4j/Category.warn(Ljava/lang/Object;)V:0
org/apache/log4j/Category.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.debug(Ljava/lang/Object;)V:0
org/apache/log4j/Logger.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.error(Ljava/lang/Object;)V:0
org/apache/log4j/Logger.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.fatal(Ljava/lang/Object;)V:0
org/apache/log4j/Logger.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.info(Ljava/lang/Object;)V:0
org/apache/log4j/Logger.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Throwable;)V:1,2
org/apache/log4j/Logger.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;)V:0
org/apache/log4j/Logger.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.log(Ljava/lang/String;Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:1,3
org/apache/log4j/Logger.warn(Ljava/lang/Object;)V:0
org/apache/log4j/Logger.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:1
org/apache/log4j/Logger.trace(Ljava/lang/Object;)V:0
org/apache/log4j/Logger.trace(Ljava/lang/Object;Ljava/lang/Throwable;)V:1

org/pmw/tinylog/Logger.debug(Ljava/lang/Object;)V:0
org/pmw/tinylog/Logger.debug(Ljava/lang/String;)V:0
org/pmw/tinylog/Logger.debug(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.debug(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.error(Ljava/lang/Object;)V:0
org/pmw/tinylog/Logger.error(Ljava/lang/String;)V:0
org/pmw/tinylog/Logger.error(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.error(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.info(Ljava/lang/Object;)V:0
org/pmw/tinylog/Logger.info(Ljava/lang/String;)V:0
org/pmw/tinylog/Logger.info(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.info(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.trace(Ljava/lang/Object;)V:0
org/pmw/tinylog/Logger.trace(Ljava/lang/String;)V:0
org/pmw/tinylog/Logger.trace(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.trace(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.warn(Ljava/lang/Object;)V:0
org/pmw/tinylog/Logger.warn(Ljava/lang/String;)V:0
org/pmw/tinylog/Logger.warn(Ljava/lang/String;[Ljava/lang/Object;)V:0,1
org/pmw/tinylog/Logger.warn(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:0,1
javax/el/ExpressionFactory.createValueExpression(Ljavax/el/ELContext;Ljava/lang/String;Ljava/lang/Class;)Ljavax/el/ValueExpression;:1
javax/el/ExpressionFactory.createMethodExpression(Ljavax/el/ELContext;Ljava/lang/String;Ljava/lang/Class;[Ljava/lang/Class;)Ljavax/el/MethodExpression;:2
java/util/Formatter.format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/Formatter;:1
java/util/Formatter.format(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/Formatter;:1

java/io/PrintStream.printf(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;:1
java/io/PrintStream.printf(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;:1

java/io/PrintStream.format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;:1
java/io/PrintStream.format(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintStream;:1

java/lang/String.format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;:1
java/lang/String.format(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;:1org/apache/commons/httpclient/methods/GetMethod.<init>(Ljava/lang/String;)V:0
org/apache/commons/httpclient/methods/GetMethod.setQueryString(Ljava/lang/String;)V:0

org/apache/http/client/methods/HttpGet.<init>(Ljava/lang/String;)V:0
kotlin/io/FilesKt.createTempFile$default(Ljava/lang/String;Ljava/lang/String;Ljava/io/File;ILjava/lang/Object;)Ljava/io/File;:3,4
kotlin/io/FilesKt.createTempFile(Ljava/lang/String;Ljava/lang/String;Ljava/io/File;)Ljava/io/File;:0,1,2
kotlin/io/FilesKt.createTempDir$default(Ljava/lang/String;Ljava/lang/String;Ljava/io/File;ILjava/lang/Object;)Ljava/io/File;:3,4
kotlin/io/FilesKt.createTempDir(Ljava/lang/String;Ljava/lang/String;Ljava/io/File;)Ljava/io/File;:0,1,2javax/naming/ldap/LdapName.<init>(Ljava/lang/String;)V:0

javax/naming/directory/Context.lookup(Ljava/lang/String;)Ljava/lang/Object;:0

javax/naming/directory/DirContext.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
javax/naming/directory/DirContext.search(Ljavax/naming/Name;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1
javax/naming/directory/DirContext.search(Ljavax/naming/Name;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2
javax/naming/directory/DirContext.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1,2
javax/naming/directory/DirContext.search(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2,3

javax/naming/directory/InitialDirContext.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
javax/naming/directory/InitialDirContext.search(Ljavax/naming/Name;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1
javax/naming/directory/InitialDirContext.search(Ljavax/naming/Name;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2
javax/naming/directory/InitialDirContext.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1,2
javax/naming/directory/InitialDirContext.search(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2,3

javax/naming/ldap/LdapContext.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
javax/naming/ldap/LdapContext.search(Ljavax/naming/Name;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1
javax/naming/ldap/LdapContext.search(Ljavax/naming/Name;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2
javax/naming/ldap/LdapContext.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1,2
javax/naming/ldap/LdapContext.search(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2,3

javax/naming/ldap/InitialLdapContext.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
javax/naming/ldap/InitialLdapContext.search(Ljavax/naming/Name;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1
javax/naming/ldap/InitialLdapContext.search(Ljavax/naming/Name;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2
javax/naming/ldap/InitialLdapContext.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1,2
javax/naming/ldap/InitialLdapContext.search(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2,3

javax/naming/event/EventDirContext.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
javax/naming/event/EventDirContext.search(Ljavax/naming/Name;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1
javax/naming/event/EventDirContext.search(Ljavax/naming/Name;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2
javax/naming/event/EventDirContext.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1,2
javax/naming/event/EventDirContext.search(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2,3

com/sun/jndi/ldap/LdapCtx.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
com/sun/jndi/ldap/LdapCtx.search(Ljavax/naming/Name;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1
com/sun/jndi/ldap/LdapCtx.search(Ljavax/naming/Name;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2
com/sun/jndi/ldap/LdapCtx.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:1,2
com/sun/jndi/ldap/LdapCtx.search(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;Ljavax/naming/directory/SearchControls;)Ljavax/naming/NamingEnumeration;:2,3

com/unboundid/ldap/sdk/LDAPConnection.search(Ljava/lang/String;Lcom/unboundid/ldap/sdk/SearchScope;Ljava/lang/String;[Ljava/lang/String;)Lcom/unboundid/ldap/sdk/SearchResult;:1,3

--

org/springframework/ldap/core/LdapTemplate.list(Ljava/lang/String;)Ljava/util/List;:0
org/springframework/ldap/core/LdapTemplate.list(Ljava/lang/String;Lorg/springframework/ldap/core/NameClassPairMapper;)Ljava/util/List;:1
org/springframework/ldap/core/LdapTemplate.list(Ljava/lang/String;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:1

org/springframework/ldap/core/LdapTemplate.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
org/springframework/ldap/core/LdapTemplate.lookup(Ljava/lang/String;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/lang/Object;:1
org/springframework/ldap/core/LdapTemplate.lookup(Ljava/lang/String;Lorg/springframework/ldap/core/ContextMapper;)Ljava/lang/Object;:1

org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:2,3
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/AttributesMapper;Lorg/springframework/ldap/core/DirContextProcessor;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/ContextMapper;Lorg/springframework/ldap/core/DirContextProcessor;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;Lorg/springframework/ldap/core/DirContextProcessor;)V:3,4
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;IZLorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:3,4
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:1,2
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;I[Ljava/lang/String;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;ILorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:2,3
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:1,2
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;I[Ljava/lang/String;Lorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;ILorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:2,3
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Lorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:1,2
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:2,3
org/springframework/ldap/core/LdapTemplate.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:2,3

--

org/springframework/ldap/core/LdapOperations.list(Ljava/lang/String;)Ljava/util/List;:0
org/springframework/ldap/core/LdapOperations.list(Ljava/lang/String;Lorg/springframework/ldap/core/NameClassPairMapper;)Ljava/util/List;:1
org/springframework/ldap/core/LdapOperations.list(Ljava/lang/String;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:1

org/springframework/ldap/core/LdapOperations.lookup(Ljava/lang/String;)Ljava/lang/Object;:0
org/springframework/ldap/core/LdapOperations.lookup(Ljava/lang/String;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/lang/Object;:1
org/springframework/ldap/core/LdapOperations.lookup(Ljava/lang/String;Lorg/springframework/ldap/core/ContextMapper;)Ljava/lang/Object;:1

org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:2,3
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/AttributesMapper;Lorg/springframework/ldap/core/DirContextProcessor;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/ContextMapper;Lorg/springframework/ldap/core/DirContextProcessor;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;Lorg/springframework/ldap/core/DirContextProcessor;)V:3,4
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;IZLorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:3,4
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Lorg/springframework/ldap/core/NameClassPairCallbackHandler;)V:1,2
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;I[Ljava/lang/String;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;ILorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:2,3
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:1,2
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;I[Ljava/lang/String;Lorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:3,4
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;ILorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:2,3
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Lorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:1,2
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/ContextMapper;)Ljava/util/List;:2,3
org/springframework/ldap/core/LdapOperations.search(Ljava/lang/String;Ljava/lang/String;Ljavax/naming/directory/SearchControls;Lorg/springframework/ldap/core/AttributesMapper;)Ljava/util/List;:2,3
java/io/File.<init>(Ljava/lang/String;)V:0
java/io/File.<init>(Ljava/lang/String;Ljava/lang/String;)V:0,1
java/io/File.<init>(Ljava/io/File;Ljava/lang/String;)V:0
java/io/File.<init>(Ljava/net/URI;)V:0
java/io/RandomAccessFile.<init>(Ljava/lang/String;Ljava/lang/String;)V:1

java/io/FileReader.<init>(Ljava/lang/String;)V:0
java/io/FileInputStream.<init>(Ljava/lang/String;)V:0

java/nio/file/Paths.get(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;:0,1

java/io/File.createTempFile(Ljava/lang/String;Ljava/lang/String;)Ljava/io/File;:0,1
java/io/File.createTempFile(Ljava/lang/String;Ljava/lang/String;Ljava/io/File;)Ljava/io/File;:0,1,2

javax/activation/FileDataSource.<init>(Ljava/lang/String;)V:0

java/nio/file/Files.createTempFile(Ljava/nio/file/Path;Ljava/lang/String;Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;:1,2
java/nio/file/Files.createTempFile(Ljava/lang/String;Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;:1,2
java/nio/file/Files.createTempDirectory(Ljava/nio/file/Path;Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;:1
java/nio/file/Files.createTempDirectory(Ljava/lang/String;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/file/Path;:1
java/io/FileWriter.<init>(Ljava/lang/String;)V:0
java/io/FileWriter.<init>(Ljava/lang/String;Z)V:1
java/io/FileOutputStream.<init>(Ljava/lang/String;)V:0
java/io/FileOutputStream.<init>(Ljava/lang/String;Z)V:1
javax/servlet/RequestDispatcher.forward(Ljavax/servlet/ServletRequest;Ljavax/servlet/ServletResponse;)V:2
javax/servlet/RequestDispatcher.include(Ljavax/servlet/ServletRequest;Ljavax/servlet/ServletResponse;)V:2javax/servlet/http/Cookie.<init>(Ljava/lang/String;Ljava/lang/String;)V:0,1
javax/servlet/http/Cookie.setValue(Ljava/lang/String;)V:0

javax/servlet/http/HttpServletResponse.addHeader(Ljava/lang/String;Ljava/lang/String;)V:0,1
javax/servlet/http/HttpServletResponse.setHeader(Ljava/lang/String;Ljava/lang/String;)V:0,1
javax/servlet/http/HttpServletResponseWrapper.addHeader(Ljava/lang/String;Ljava/lang/String;)V:0,1
javax/servlet/http/HttpServletResponseWrapper.setHeader(Ljava/lang/String;Ljava/lang/String;)V:0,1
scala/io/Source$.fromFile(Ljava/lang/String;Lscala/io/Codec;)Lscala/io/BufferedSource;:1
scala/io/Source$.fromFile(Ljava/lang/String;Ljava/lang/String;)Lscala/io/BufferedSource;:1
scala/io/Source$.fromFile(Ljava/net/URI;Lscala/io/Codec;)Lscala/io/BufferedSource;:1
scala/io/Source$.fromFile(Ljava/net/URI;Ljava/lang/String;)Lscala/io/BufferedSource;:1scala/reflect/io/File$.apply(Lscala/reflect/io/Path;Lscala/io/Codec;)Lscala/reflect/io/File;:1play/api/libs/ws/WSRequest.get()Lscala/concurrent/Future;:0
play/api/libs/ws/WSRequest.post(Ljava/lang/Object;Lplay/api/http/Writeable;)Lscala/concurrent/Future;:1,2javax/script/ScriptEngine.eval(Ljava/lang/String;)Ljava/lang/Object;:0
org/jboss/seam/log/Log.debug(Ljava/lang/Object;[Ljava/lang/Object;)V:1
org/jboss/seam/log/Log.debug(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:2
org/jboss/seam/log/Log.error(Ljava/lang/Object;[Ljava/lang/Object;)V:1
org/jboss/seam/log/Log.error(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:2
org/jboss/seam/log/Log.fatal(Ljava/lang/Object;[Ljava/lang/Object;)V:1
org/jboss/seam/log/Log.fatal(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:2
org/jboss/seam/log/Log.info(Ljava/lang/Object;[Ljava/lang/Object;)V:1
org/jboss/seam/log/Log.info(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:2
org/jboss/seam/log/Log.trace(Ljava/lang/Object;[Ljava/lang/Object;)V:1
org/jboss/seam/log/Log.trace(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:2
org/jboss/seam/log/Log.warn(Ljava/lang/Object;[Ljava/lang/Object;)V:1
org/jboss/seam/log/Log.warn(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:2play/api/mvc/Results$Status.apply(Ljava/lang/Object;Lplay/api/http/Writeable;)Lplay/api/mvc/Result;:1
play/api/mvc/Result.withCookies(Lscala/collection/Seq;)Lplay/api/mvc/Result;:0javax/mail/Message.setSubject(Ljava/lang/String;)V:0
javax/mail/Message.addHeader(Ljava/lang/String;Ljava/lang/String;)V:0,1
javax/mail/Message.setDescription(Ljava/lang/String;)V:0
javax/mail/Message.setDisposition(Ljava/lang/String;)V:0org/springframework/expression/ExpressionParser.parseExpression(Ljava/lang/String;)Lorg/springframework/expression/Expression;:0
org/springframework/expression/spel/standard/SpelExpressionParser.parseExpression(Ljava/lang/String;)Lorg/springframework/expression/Expression;:0
org/springframework/expression/common/TemplateAwareExpressionParser.parseExpression(Ljava/lang/String;)Lorg/springframework/expression/Expression;:0

org/springframework/expression/ExpressionParser.parseExpression(Ljava/lang/String;Lorg/springframework/expression/ParserContext;)Lorg/springframework/expression/Expression;:1
org/springframework/expression/spel/standard/SpelExpressionParser.parseExpression(Ljava/lang/String;Lorg/springframework/expression/ParserContext;)Lorg/springframework/expression/Expression;:1
org/springframework/expression/common/TemplateAwareExpressionParser.parseExpression(Ljava/lang/String;Lorg/springframework/expression/ParserContext;)Lorg/springframework/expression/Expression;:1
org/springframework/web/servlet/ModelAndView.<init>(Ljava/lang/String;)V:0
org/springframework/web/servlet/ModelAndView.<init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:2
org/springframework/web/servlet/ModelAndView.<init>(Ljava/lang/String;Ljava/util/Map;)V:1
org/springframework/web/servlet/ModelAndView.setViewName(Ljava/lang/String;)V:0--SQLiteDatabase

android/database/sqlite/SQLiteDatabase.compileStatement(Ljava/lang/String;)Landroid/database/sqlite/SQLiteStatement;:0

android/database/sqlite/SQLiteDatabase.query(ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,1,2,3,5,7
android/database/sqlite/SQLiteDatabase.query(ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;:1,2,3,4,6,8

android/database/sqlite/SQLiteDatabase.queryWithFactory(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,1,2,3,5,7
android/database/sqlite/SQLiteDatabase.queryWithFactory(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;:1,2,3,4,6,8

android/database/sqlite/SQLiteDatabase.query(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,1,2,4,6
android/database/sqlite/SQLiteDatabase.query(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,1,2,3,5,7

android/database/sqlite/SQLiteDatabase.rawQuery(Ljava/lang/String;[Ljava/lang/String;)Landroid/database/Cursor;:1
android/database/sqlite/SQLiteDatabase.rawQuery(Ljava/lang/String;[Ljava/lang/String;Landroid.os.CancellationSignal;)Landroid/database/Cursor;:2

android/database/sqlite/SQLiteDatabase.rawQueryWithFactory(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,2
android/database/sqlite/SQLiteDatabase.rawQueryWithFactory(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;:1,3

android/database/sqlite/SQLiteDatabase.delete(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)I:1,2
android/database/sqlite/SQLiteDatabase.update(Ljava/lang/String;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I:1,3
android/database/sqlite/SQLiteDatabase.updateWithOnConflict(Ljava/lang/String;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;I)I:2,4

android/database/sqlite/SQLiteDatabase.execSQL(Ljava/lang/String;)V:0
android/database/sqlite/SQLiteDatabase.execSQL(Ljava/lang/String;[Ljava/lang/Object;)V:1

--DatabaseUtils

android/database/DatabaseUtils.longForQuery(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;[Ljava/lang/String;)J:1
android/database/DatabaseUtils.stringForQuery(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/String;:1
android/database/DatabaseUtils.blobFileDescriptorForQuery(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;[Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;:1
android/database/DatabaseUtils.createDbFromSqlStatements(Landroid/content/Context;Ljava/lang/String;ILjava/lang/String;)V:0

--SQLiteQueryBuilder

android/database/sqlite/SQLiteQueryBuilder.appendWhere(Ljava/lang/CharSequence;)V:0

android/database/sqlite/SQLiteQueryBuilder.buildQueryString(ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,1,2,3,4,6

android/database/sqlite/SQLiteQueryBuilder.query(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,1,2,4
android/database/sqlite/SQLiteQueryBuilder.query(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:0,1,2,3,5
android/database/sqlite/SQLiteQueryBuilder.query(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;:1,2,3,4,6

android/database/sqlite/SQLiteQueryBuilder.buildQuery([Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,1,2,3,4
android/database/sqlite/SQLiteQueryBuilder.buildQuery([Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,1,2,3,5

android/database/sqlite/SQLiteQueryBuilder.buildUnionSubQuery(Ljava/lang/String;[Ljava/lang/String;Ljava/util/Set;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,1,2
android/database/sqlite/SQLiteQueryBuilder.buildUnionSubQuery(Ljava/lang/String;[Ljava/lang/String;Ljava/util/Set;ILjava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,1,3
android/database/sqlite/SQLiteQueryBuilder.buildUnionQuery([Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,1,2

--ContentProvider

android/content/ContentProvider.query(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;:2
android/content/ContentProvider.query(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;:3
android/content/ContentProvider.delete(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I:1
android/content/ContentProvider.update(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I:1
org/hibernate/criterion/Restrictions.sqlRestriction(Ljava/lang/String;)Lorg/hibernate/criterion/Criterion;:0
org/hibernate/criterion/Restrictions.sqlRestriction(Ljava/lang/String;Ljava/lang/Object;Lorg/hibernate/type/Type;)Lorg/hibernate/criterion/Criterion;:2
org/hibernate/criterion/Restrictions.sqlRestriction(Ljava/lang/String;[Ljava/lang/Object;[Lorg/hibernate/type/Type;)Lorg/hibernate/criterion/Criterion;:2

org/hibernate/Session.createQuery(Ljava/lang/String;)Lorg/hibernate/Query;:0
org/hibernate/Session.createQuery(Ljava/lang/String;)Lorg/hibernate/query/Query;:0
org/hibernate/Session.createSQLQuery(Ljava/lang/String;)Lorg/hibernate/SQLQuery;:0
java/sql/Statement.executeQuery(Ljava/lang/String;)Ljava/sql/ResultSet;:0
java/sql/Statement.execute(Ljava/lang/String;)Z:0
java/sql/Statement.execute(Ljava/lang/String;I)Z:1
java/sql/Statement.execute(Ljava/lang/String;[I)Z:1
java/sql/Statement.execute(Ljava/lang/String;[Ljava/lang/String;)Z:1
java/sql/Statement.executeUpdate(Ljava/lang/String;)I:0
java/sql/Statement.executeUpdate(Ljava/lang/String;I)I:1
java/sql/Statement.executeUpdate(Ljava/lang/String;[I)I:1
java/sql/Statement.executeUpdate(Ljava/lang/String;[Ljava/lang/String;)I:1
java/sql/Statement.executeLargeUpdate(Ljava/lang/String;)J:0
java/sql/Statement.executeLargeUpdate(Ljava/lang/String;I)J:1
java/sql/Statement.executeLargeUpdate(Ljava/lang/String;[I)J:1
java/sql/Statement.executeLargeUpdate(Ljava/lang/String;[Ljava/lang/String;)J:1
java/sql/Statement.addBatch(Ljava/lang/String;)V:0

java/sql/PreparedStatement.executeQuery(Ljava/lang/String;)Ljava/sql/ResultSet;:0
java/sql/PreparedStatement.execute(Ljava/lang/String;)Z:0
java/sql/PreparedStatement.execute(Ljava/lang/String;I)Z:1
java/sql/PreparedStatement.execute(Ljava/lang/String;[I)Z:1
java/sql/PreparedStatement.execute(Ljava/lang/String;[Ljava/lang/String;)Z:1
java/sql/PreparedStatement.executeUpdate(Ljava/lang/String;)I:0
java/sql/PreparedStatement.executeUpdate(Ljava/lang/String;I)I:1
java/sql/PreparedStatement.executeUpdate(Ljava/lang/String;[I)I:1
java/sql/PreparedStatement.executeUpdate(Ljava/lang/String;[Ljava/lang/String;)I:1
java/sql/PreparedStatement.executeLargeUpdate(Ljava/lang/String;)J:0
java/sql/PreparedStatement.executeLargeUpdate(Ljava/lang/String;I)J:1
java/sql/PreparedStatement.executeLargeUpdate(Ljava/lang/String;[I)J:1
java/sql/PreparedStatement.executeLargeUpdate(Ljava/lang/String;[Ljava/lang/String;)J:1
java/sql/PreparedStatement.addBatch(Ljava/lang/String;)V:0


java/sql/Connection.prepareCall(Ljava/lang/String;)Ljava/sql/CallableStatement;:0
java/sql/Connection.prepareCall(Ljava/lang/String;II)Ljava/sql/CallableStatement;:2
java/sql/Connection.prepareCall(Ljava/lang/String;III)Ljava/sql/CallableStatement;:3
java/sql/Connection.prepareStatement(Ljava/lang/String;)Ljava/sql/PreparedStatement;:0
java/sql/Connection.prepareStatement(Ljava/lang/String;I)Ljava/sql/PreparedStatement;:1
java/sql/Connection.prepareStatement(Ljava/lang/String;II)Ljava/sql/PreparedStatement;:2
java/sql/Connection.prepareStatement(Ljava/lang/String;III)Ljava/sql/PreparedStatement;:3
java/sql/Connection.prepareStatement(Ljava/lang/String;[I)Ljava/sql/PreparedStatement;:1
java/sql/Connection.prepareStatement(Ljava/lang/String;[Ljava/lang/String;)Ljava/sql/PreparedStatement;:1
java/sql/Connection.nativeSQL(Ljava/lang/String;)Ljava/lang/String;:0
- API reference: http://db.apache.org/jdo/index.html

javax/jdo/PersistenceManager.newQuery(Ljava/lang/String;)Ljavax/jdo/Query;:0
javax/jdo/PersistenceManager.newQuery(Ljava/lang/String;Ljava/lang/Object;)Ljavax/jdo/Query;:0
javax/jdo/PersistenceManager.newQuery(Ljava/lang/Class;Ljava/util/Collection;Ljava/lang/String;)Ljavax/jdo/Query;:0
javax/jdo/PersistenceManager.newQuery(Ljava/lang/Class;Ljava/lang/String;)Ljavax/jdo/Query;:0
javax/jdo/PersistenceManager.newQuery(Ljavax/jdo/Extent;Ljava/lang/String;)Ljavax/jdo/Query;:0

javax/jdo/Query.setFilter(Ljava/lang/String;)V:0
javax/jdo/Query.setGrouping(Ljava/lang/String;)V:0
- API reference:
- http://www.oracle.com/technetwork/articles/javaee/jpa-137156.html
- http://docs.oracle.com/javaee/6/api/javax/persistence/package-summary.html

javax/persistence/EntityManager.createQuery(Ljava/lang/String;)Ljavax/persistence/Query;:0
javax/persistence/EntityManager.createQuery(Ljava/lang/String;Ljava/lang/Class;)Ljavax/persistence/TypedQuery;:1
javax/persistence/EntityManager.createNativeQuery(Ljava/lang/String;)Ljavax/persistence/Query;:0
javax/persistence/EntityManager.createNativeQuery(Ljava/lang/String;Ljava/lang/String;)Ljavax/persistence/Query;:1
javax/persistence/EntityManager.createNativeQuery(Ljava/lang/String;Ljava/lang/Class;)Ljavax/persistence/Query;:1
- API reference:
- https://www.playframework.com/documentation/2.5.x/ScalaAnorm

anorm/SimpleSql.execute(Ljava/sql/Connection;)Z:1
anorm/SimpleSql.executeUpdate(Ljava/sql/Connection;)I:1
anorm/SimpleSql.executeQuery(Ljava/sql/Connection;)Lanorm/SqlQueryResult;:1
anorm/SimpleSql.executeInsert(Lanorm/ResultSetParser;Ljava/sql/Connection;)Ljava/lang/Object;:2
anorm/SimpleSql.as(Lanorm/ResultSetParser;Ljava/sql/Connection;)Ljava/lang/Object;:2

anorm/BatchSql$.apply(Ljava/lang/String;Lscala/collection/Seq;)Lanorm/BatchSql;:1
anorm/BatchSql$.apply(Ljava/lang/String;Lscala/collection/Seq;Lscala/collection/Seq;)Lanorm/BatchSql;:2- API reference:
- http://slick.lightbend.com/doc/3.0.0/sql.html
- http://slick.lightbend.com/doc/3.1.1/api/index.html#slick.jdbc.SQLActionBuilder

slick/jdbc/SQLActionBuilder.<init>(Lscala/collection/Seq;Lslick/jdbc/SetParameter;)V:1org/springframework/jdbc/core/PreparedStatementCreatorFactory.<init>(Ljava/lang/String;)V:0
org/springframework/jdbc/core/PreparedStatementCreatorFactory.<init>(Ljava/lang/String;[I)V:1
org/springframework/jdbc/core/PreparedStatementCreatorFactory.<init>(Ljava/lang/String;Ljava/util/List;)V:1
org/springframework/jdbc/core/PreparedStatementCreatorFactory.newPreparedStatementCreator(Ljava/lang/String;[Ljava/lang/Object;)Lorg/springframework/jdbc/core/PreparedStatementCreator;:1


org/springframework/jdbc/core/JdbcOperations.batchUpdate([Ljava/lang/String;)[I:0
org/springframework/jdbc/core/JdbcOperations.batchUpdate(Ljava/lang/String;Lorg/springframework/jdbc/core/BatchPreparedStatementSetter;)[I:1
org/springframework/jdbc/core/JdbcOperations.batchUpdate(Ljava/lang/String;Ljava/util/Collection;ILorg/springframework/jdbc/core/ParameterizedPreparedStatementSetter;)[[I:3
org/springframework/jdbc/core/JdbcOperations.batchUpdate(Ljava/lang/String;Ljava/util/List;)[I:1
org/springframework/jdbc/core/JdbcOperations.batchUpdate(Ljava/lang/String;Ljava/util/List;[I)[I:2

org/springframework/jdbc/core/JdbcOperations.execute(Ljava/lang/String;)V:0
org/springframework/jdbc/core/JdbcOperations.execute(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementCallback;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcOperations.execute(Ljava/lang/String;Lorg/springframework/jdbc/core/CallableStatementCallback;)Ljava/lang/Object;:1

org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/ResultSetExtractor;[Ljava/lang/Object;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowCallbackHandler;)V:1
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowCallbackHandler;[Ljava/lang/Object;)V:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:1
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;[Ljava/lang/Object;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;Lorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;Lorg/springframework/jdbc/core/RowCallbackHandler;)V:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;Lorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/RowCallbackHandler;)V:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:3
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:3
org/springframework/jdbc/core/JdbcOperations.query(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/RowCallbackHandler;)V:3

org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;)Ljava/util/List;:0
org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;Ljava/lang/Class;)Ljava/util/List;:1
org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;Ljava/lang/Class;[Ljava/lang/Object;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Class;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;[Ljava/lang/Object;[I)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;[Ljava/lang/Object;[ILjava/lang/Class;)Ljava/util/List;:3
org/springframework/jdbc/core/JdbcOperations.queryForList(Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/List;:1

org/springframework/jdbc/core/JdbcOperations.queryForMap(Ljava/lang/String;)Ljava/util/Map;:0
org/springframework/jdbc/core/JdbcOperations.queryForMap(Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/Map;:1
org/springframework/jdbc/core/JdbcOperations.queryForMap(Ljava/lang/String;[Ljava/lang/Object;[I)Ljava/util/Map;:2

org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;[Ljava/lang/Object;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;Ljava/lang/Class;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;[Ljava/lang/Object;[ILjava/lang/Class;)Ljava/lang/Object;:3
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/RowMapper;)Ljava/lang/Object;:3
org/springframework/jdbc/core/JdbcOperations.queryForObject(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/RowMapper;)Ljava/lang/Object;:2

org/springframework/jdbc/core/JdbcOperations.queryForRowSet(Ljava/lang/String;)Lorg/springframework/jdbc/support/rowset/SqlRowSet;:0
org/springframework/jdbc/core/JdbcOperations.queryForRowSet(Ljava/lang/String;[Ljava/lang/Object;)Lorg/springframework/jdbc/support/rowset/SqlRowSet;:1
org/springframework/jdbc/core/JdbcOperations.queryForRowSet(Ljava/lang/String;[Ljava/lang/Object;[I)Lorg/springframework/jdbc/support/rowset/SqlRowSet;:2

org/springframework/jdbc/core/JdbcOperations.queryForInt(Ljava/lang/String;)I:0
org/springframework/jdbc/core/JdbcOperations.queryForInt(Ljava/lang/String;[Ljava/lang/Object;)I:1
org/springframework/jdbc/core/JdbcOperations.queryForInt(Ljava/lang/String;[Ljava/lang/Object;[I)I:2

org/springframework/jdbc/core/JdbcOperations.queryForLong(Ljava/lang/String;)J:0
org/springframework/jdbc/core/JdbcOperations.queryForLong(Ljava/lang/String;[Ljava/lang/Object;)J:1
org/springframework/jdbc/core/JdbcOperations.queryForLong(Ljava/lang/String;[Ljava/lang/Object;[I)J:2

org/springframework/jdbc/core/JdbcOperations.update(Ljava/lang/String;)I:0
org/springframework/jdbc/core/JdbcOperations.update(Ljava/lang/String;[Ljava/lang/Object;)I:1
org/springframework/jdbc/core/JdbcOperations.update(Ljava/lang/String;[Ljava/lang/Object;[I)I:2
org/springframework/jdbc/core/JdbcOperations.update(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;)I:1

-JdbcTemplate is implementing JdbcOperations
org/springframework/jdbc/core/JdbcTemplate.batchUpdate([Ljava/lang/String;)[I:0
org/springframework/jdbc/core/JdbcTemplate.batchUpdate(Ljava/lang/String;Lorg/springframework/jdbc/core/BatchPreparedStatementSetter;)[I:1
org/springframework/jdbc/core/JdbcTemplate.batchUpdate(Ljava/lang/String;Ljava/util/Collection;ILorg/springframework/jdbc/core/ParameterizedPreparedStatementSetter;)[[I:3
org/springframework/jdbc/core/JdbcTemplate.batchUpdate(Ljava/lang/String;Ljava/util/List;)[I:1
org/springframework/jdbc/core/JdbcTemplate.batchUpdate(Ljava/lang/String;Ljava/util/List;[I)[I:2

org/springframework/jdbc/core/JdbcTemplate.execute(Ljava/lang/String;)V:0
org/springframework/jdbc/core/JdbcTemplate.execute(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementCallback;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcTemplate.execute(Ljava/lang/String;Lorg/springframework/jdbc/core/CallableStatementCallback;)Ljava/lang/Object;:1

org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/ResultSetExtractor;[Ljava/lang/Object;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowCallbackHandler;)V:1
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowCallbackHandler;[Ljava/lang/Object;)V:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:1
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;[Ljava/lang/Object;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;Lorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;Lorg/springframework/jdbc/core/RowCallbackHandler;)V:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;Lorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/RowCallbackHandler;)V:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/ResultSetExtractor;)Ljava/lang/Object;:3
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/RowMapper;)Ljava/util/List;:3
org/springframework/jdbc/core/JdbcTemplate.query(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/RowCallbackHandler;)V:3

org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;)Ljava/util/List;:0
org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;Ljava/lang/Class;)Ljava/util/List;:1
org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;Ljava/lang/Class;[Ljava/lang/Object;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Class;)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;[Ljava/lang/Object;[I)Ljava/util/List;:2
org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;[Ljava/lang/Object;[ILjava/lang/Class;)Ljava/util/List;:3
org/springframework/jdbc/core/JdbcTemplate.queryForList(Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/List;:1

org/springframework/jdbc/core/JdbcTemplate.queryForMap(Ljava/lang/String;)Ljava/util/Map;:0
org/springframework/jdbc/core/JdbcTemplate.queryForMap(Ljava/lang/String;[Ljava/lang/Object;)Ljava/util/Map;:1
org/springframework/jdbc/core/JdbcTemplate.queryForMap(Ljava/lang/String;[Ljava/lang/Object;[I)Ljava/util/Map;:2

org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;Lorg/springframework/jdbc/core/RowMapper;[Ljava/lang/Object;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;Ljava/lang/Class;)Ljava/lang/Object;:1
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;:2
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;[Ljava/lang/Object;[ILjava/lang/Class;)Ljava/lang/Object;:3
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;[Ljava/lang/Object;[ILorg/springframework/jdbc/core/RowMapper;)Ljava/lang/Object;:3
org/springframework/jdbc/core/JdbcTemplate.queryForObject(Ljava/lang/String;[Ljava/lang/Object;Lorg/springframework/jdbc/core/RowMapper;)Ljava/lang/Object;:2

org/springframework/jdbc/core/JdbcTemplate.queryForRowSet(Ljava/lang/String;)Lorg/springframework/jdbc/support/rowset/SqlRowSet;:0
org/springframework/jdbc/core/JdbcTemplate.queryForRowSet(Ljava/lang/String;[Ljava/lang/Object;)Lorg/springframework/jdbc/support/rowset/SqlRowSet;:1
org/springframework/jdbc/core/JdbcTemplate.queryForRowSet(Ljava/lang/String;[Ljava/lang/Object;[I)Lorg/springframework/jdbc/support/rowset/SqlRowSet;:2

org/springframework/jdbc/core/JdbcTemplate.queryForInt(Ljava/lang/String;)I:0
org/springframework/jdbc/core/JdbcTemplate.queryForInt(Ljava/lang/String;[Ljava/lang/Object;)I:1
org/springframework/jdbc/core/JdbcTemplate.queryForInt(Ljava/lang/String;[Ljava/lang/Object;[I)I:2

org/springframework/jdbc/core/JdbcTemplate.queryForLong(Ljava/lang/String;)J:0
org/springframework/jdbc/core/JdbcTemplate.queryForLong(Ljava/lang/String;[Ljava/lang/Object;)J:1
org/springframework/jdbc/core/JdbcTemplate.queryForLong(Ljava/lang/String;[Ljava/lang/Object;[I)J:2

org/springframework/jdbc/core/JdbcTemplate.update(Ljava/lang/String;)I:0
org/springframework/jdbc/core/JdbcTemplate.update(Ljava/lang/String;[Ljava/lang/Object;)I:1
org/springframework/jdbc/core/JdbcTemplate.update(Ljava/lang/String;[Ljava/lang/Object;[I)I:2
org/springframework/jdbc/core/JdbcTemplate.update(Ljava/lang/String;Lorg/springframework/jdbc/core/PreparedStatementSetter;)I:1
org/apache/turbine/om/peer/BasePeer.executeQuery(Ljava/lang/String;)Ljava/util/Vector;:0
org/apache/turbine/om/peer/BasePeer.executeQuery(Ljava/lang/String;Ljava/lang/String;)Ljava/util/Vector;:1
org/apache/turbine/om/peer/BasePeer.executeQuery(Ljava/lang/String;Ljava/lang/String;Z)Ljava/util/Vector;:2
org/apache/turbine/om/peer/BasePeer.executeQuery(Ljava/lang/String;ZLorg/apache/turbine/util/db/pool/DBConnection;)Ljava/util/Vector;:2
org/apache/turbine/om/peer/BasePeer.executeQuery(Ljava/lang/String;IIZLorg/apache/turbine/util/db/pool/DBConnection;)Ljava/util/Vector;:4
org/apache/turbine/om/peer/BasePeer.executeQuery(Ljava/lang/String;IILjava/lang/String;Z)Ljava/util/Vector;:4

org/apache/torque/util/BasePeer.executeQuery(Ljava/lang/String;)Ljava/util/Vector;:0
org/apache/torque/util/BasePeer.executeQuery(Ljava/lang/String;Ljava/lang/String;)Ljava/util/Vector;:1
org/apache/torque/util/BasePeer.executeQuery(Ljava/lang/String;Ljava/lang/String;Z)Ljava/util/Vector;:2
org/apache/torque/util/BasePeer.executeQuery(Ljava/lang/String;ZLorg/apache/turbine/util/db/pool/DBConnection;)Ljava/util/Vector;:2
org/apache/torque/util/BasePeer.executeQuery(Ljava/lang/String;IIZLorg/apache/turbine/util/db/pool/DBConnection;)Ljava/util/Vector;:4
org/apache/torque/util/BasePeer.executeQuery(Ljava/lang/String;IILjava/lang/String;Z)Ljava/util/Vector;:4
org/apache/struts/action/ActionForward.<init>(Ljava/lang/String;)V:0
org/apache/struts/action/ActionForward.<init>(Ljava/lang/String;Z)V:1
org/apache/struts/action/ActionForward.<init>(Ljava/lang/String;Ljava/lang/String;Z)V:1
org/apache/struts/action/ActionForward.<init>(Ljava/lang/String;Ljava/lang/String;ZZ)V:2
org/apache/struts/action/ActionForward.setPath(Ljava/lang/String;)V:0-- Struts2 and Ognl API

com/opensymphony/xwork2/util/TextParseUtil.translateVariables(Ljava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;)Ljava/lang/String;:1
com/opensymphony/xwork2/util/TextParseUtil.translateVariables(Ljava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;)Ljava/lang/String;:2
com/opensymphony/xwork2/util/TextParseUtil.translateVariables(CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;)Ljava/lang/String;:1
com/opensymphony/xwork2/util/TextParseUtil.translateVariables(CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;Ljava/lang/Class;)Ljava/lang/Object;:2
com/opensymphony/xwork2/util/TextParseUtil.translateVariables(CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;Ljava/lang/Class;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;)Ljava/lang/Object;:3
com/opensymphony/xwork2/util/TextParseUtil.translateVariables([CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;Ljava/lang/Class;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;)Ljava/lang/Object;:3
com/opensymphony/xwork2/util/TextParseUtil.translateVariables(CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;Ljava/lang/Class;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;I)Ljava/lang/Object;:4
com/opensymphony/xwork2/util/TextParseUtil.translateVariables([CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;Ljava/lang/Class;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;I)Ljava/lang/Object;:4
com/opensymphony/xwork2/util/TextParseUtil.translateVariablesCollection(Ljava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;ZLcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;)Lcom/opensymphony/xwork2/util/Collection;:3
com/opensymphony/xwork2/util/TextParseUtil.translateVariablesCollection([CLjava/lang/String;Lcom/opensymphony/xwork2/util/ValueStack;ZLcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;I)Lcom/opensymphony/xwork2/util/Collection;:4
com/opensymphony/xwork2/util/TextParseUtil.shallBeIncluded(Ljava/lang/String;Z)Z:1
com/opensymphony/xwork2/util/TextParseUtil.commaDelimitedStringToSet(Ljava/lang/String;)Lcom/opensymphony/xwork2/util/Set;:0

com/opensymphony/xwork2/util/TextParser.evaluate([CLjava/lang/String;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;I)Ljava/lang/Object;:2
com/opensymphony/xwork2/util/OgnlTextParser.evaluate([CLjava/lang/String;Lcom/opensymphony/xwork2/util/TextParseUtil$ParsedValueEvaluator;I)Ljava/lang/Object;:2

com/opensymphony/xwork2/ognl/OgnlReflectionProvider.getGetMethod(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/reflect/Method;:0
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.getSetMethod(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/reflect/Method;:0
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.getField(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/reflect/Field;:0
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.setProperties(Ljava/util/Map;Ljava/lang/Object;Ljava/util/Map;)V:2
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.setProperties(Ljava/util/Map;Ljava/lang/Object;Ljava/util/Map;Z)V:3
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.setProperties(Ljava/util/Map;Ljava/lang/Object;)V:1
--com/opensymphony/xwork2/ognl/OgnlReflectionProvider.getPropertyDescriptor(Ljava/lang/Class;Ljava/lang/String;)Ljava.beans.PropertyDescriptor;:0
--com/opensymphony/xwork2/ognl/OgnlReflectionProvider.getRealTarget(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;)Ljava/lang/Object;:2
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.setProperty(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;)V:3
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.setProperty(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;Z)V:4
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.getValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;)Ljava/lang/Object;:2
com/opensymphony/xwork2/ognl/OgnlReflectionProvider.setValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;Ljava/lang/Object;)V:3

com/opensymphony/xwork2/util/reflection/ReflectionProvider.getGetMethod(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/reflect/Method;:0
com/opensymphony/xwork2/util/reflection/ReflectionProvider.getSetMethod(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/reflect/Method;:0
com/opensymphony/xwork2/util/reflection/ReflectionProvider.getField(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/reflect/Field;:0
com/opensymphony/xwork2/util/reflection/ReflectionProvider.setProperties(Ljava/util/Map;Ljava/lang/Object;Ljava/util/Map;)V:2
com/opensymphony/xwork2/util/reflection/ReflectionProvider.setProperties(Ljava/util/Map;Ljava/lang/Object;Ljava/util/Map;Z)V:3
com/opensymphony/xwork2/util/reflection/ReflectionProvider.setProperties(Ljava/util/Map;Ljava/lang/Object;)V:1
--com/opensymphony/xwork2/util/reflection/ReflectionProvider.getPropertyDescriptor(Ljava/lang/Class;Ljava/lang/String;)Ljava.beans.PropertyDescriptor;:0
--com/opensymphony/xwork2/util/reflection/ReflectionProvider.copy(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;Ljava.util.Collection;Ljava.util.Collection;)V:
--com/opensymphony/xwork2/util/reflection/ReflectionProvider.getRealTarget(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;)Ljava/lang/Object;:2
com/opensymphony/xwork2/util/reflection/ReflectionProvider.setProperty(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;Z)V:4
com/opensymphony/xwork2/util/reflection/ReflectionProvider.setProperty(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;)V:3
--com/opensymphony/xwork2/util/reflection/ReflectionProvider.getBeanMap(Lcom/opensymphony/xwork2/util/reflection/Object;)Ljava/util/Map;:
com/opensymphony/xwork2/util/reflection/ReflectionProvider.getValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;)Ljava/lang/Object;:2
com/opensymphony/xwork2/util/reflection/ReflectionProvider.setValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;Ljava/lang/Object;)V:3
--com/opensymphony/xwork2/util/reflection/ReflectionProvider.getPropertyDescriptors(Ljava/lang/Object;)[Ljava.beans.PropertyDescriptor;:

com/opensymphony/xwork2/ognl/OgnlUtil.setProperties(Ljava/util/Map;Ljava/lang/Object;Ljava/util/Map;)V:2
com/opensymphony/xwork2/ognl/OgnlUtil.setProperties(Ljava/util/Map;Ljava/lang/Object;Ljava/util/Map;Z)V:3
com/opensymphony/xwork2/ognl/OgnlUtil.setProperties(Ljava/util/Map;Ljava/lang/Object;)V:1
com/opensymphony/xwork2/ognl/OgnlUtil.setProperties(Ljava/util/Map;Ljava/lang/Object;Z)V:2
com/opensymphony/xwork2/ognl/OgnlUtil.setProperty(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;)V:3
com/opensymphony/xwork2/ognl/OgnlUtil.setProperty(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Map;Z)V:4
com/opensymphony/xwork2/ognl/OgnlUtil.setValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;Ljava/lang/Object;)V:3
com/opensymphony/xwork2/ognl/OgnlUtil.getValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;)Ljava/lang/Object;:2
com/opensymphony/xwork2/ognl/OgnlUtil.callMethod(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;)Ljava/lang/Object;:2
com/opensymphony/xwork2/ognl/OgnlUtil.getValue(Ljava/lang/String;Ljava/util/Map;Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;:3

com/opensymphony/xwork2/ognl/OgnlUtil.compile(Ljava/lang/String;)Ljava/lang/Object;:0
--compileAndExecute method are private
--com/opensymphony/xwork2/ognl/OgnlUtil.compileAndExecute(Ljava/lang/String;Ljava/util/Map;Lcom/opensymphony/xwork2/ognl/OgnlTask;)Ljava/lang/Object;:2
--com/opensymphony/xwork2/ognl/OgnlUtil.compileAndExecuteMethod(Ljava/lang/String;Ljava/util/Map;Lcom/opensymphony/xwork2/ognl/OgnlTask;)Ljava/lang/Object;:2
com/opensymphony/xwork2/ognl/OgnlUtil.compile(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/Object;:1


org/apache/struts2/util/VelocityStrutsUtil.evaluate(Ljava/lang/String;)Ljava/lang/String;:0

--org/apache/struts2/util/StrutsUtil.bean(Lorg/apache/struts2/util/Object;)Lorg/apache/struts2/util/Object;:
org/apache/struts2/util/StrutsUtil.isTrue(Ljava/lang/String;)Z:0
org/apache/struts2/util/StrutsUtil.findString(Ljava/lang/String;)Lorg/apache/struts2/util/Object;:0
--org/apache/struts2/util/StrutsUtil.include(Lorg/apache/struts2/util/Object;)Ljava/lang/String;:
--org/apache/struts2/util/StrutsUtil.urlEncode(Ljava/lang/String;)Ljava/lang/String;:0
org/apache/struts2/util/StrutsUtil.findValue(Ljava/lang/String;Ljava/lang/String;)Lorg/apache/struts2/util/Object;:1
org/apache/struts2/util/StrutsUtil.getText(Ljava/lang/String;)Ljava/lang/String;:0
--org/apache/struts2/util/StrutsUtil.getContext()Ljava/lang/String;:
org/apache/struts2/util/StrutsUtil.translateVariables(Ljava/lang/String;)Ljava/lang/String;:0
org/apache/struts2/util/StrutsUtil.makeSelectList(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/apache/struts2/util/List;:0,1,2,3

org/apache/struts2/views/jsp/ui/OgnlTool.findValue(Ljava/lang/String;Lorg/apache/struts2/views/jsp/ui/Object;)Lorg/apache/struts2/views/jsp/ui/Object;:1


com/opensymphony/xwork2/util/ValueStack.findString(Ljava/lang/String;)Ljava/lang/String;:0
com/opensymphony/xwork2/util/ValueStack.findString(Ljava/lang/String;Z)Ljava/lang/String;:1
com/opensymphony/xwork2/util/ValueStack.findValue(Ljava/lang/String;)Ljava/lang/Object;:0
com/opensymphony/xwork2/util/ValueStack.findValue(Ljava/lang/String;Z)Ljava/lang/Object;:1
com/opensymphony/xwork2/util/ValueStack.findValue(Ljava/lang/String;Ljava/lang/Class;)Ljava/lang/Object;:1
com/opensymphony/xwork2/util/ValueStack.findValue(Ljava/lang/String;Ljava/lang/Class;Z)Ljava/lang/Object;:2
com/opensymphony/xwork2/util/ValueStack.setValue(Ljava/lang/String;Ljava/lang/Object;)V:1
com/opensymphony/xwork2/util/ValueStack.setValue(Ljava/lang/String;Ljava/lang/Object;Z)V:2
com/opensymphony/xwork2/util/ValueStack.setParameter(Ljava/lang/String;Ljava/lang/Object;)V:1
javax/servlet/http/HttpSession.setAttribute(Ljava/lang/String;Ljava/lang/Object;)V:1
javax/servlet/http/HttpSession.putValue(Ljava/lang/String;Ljava/lang/Object;)V:1javax/servlet/http/HttpSession.setAttribute(Ljava/lang/String;Ljava/lang/Object;)V:0
javax/servlet/http/HttpSession.putValue(Ljava/lang/String;Ljava/lang/Object;)V:0java/net/URL.openConnection()Ljava/net/URLConnection;:0
java/net/URL.openConnection(Ljava/net/Proxy;)Ljava/net/URLConnection;:0,1
java/net/URL.openStream()Ljava/io/InputStream;:0
java/net/URL.getContent()Ljava/lang/Object;:0
java/net/URL.getContent([Ljava/lang/Class;)Ljava/lang/Object;:1org/apache/xpath/XPathAPI.eval(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/apache/xpath/objects/XObject;:0
org/apache/xpath/XPathAPI.eval(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/apache/xpath/objects/XObject;:1
org/apache/xpath/XPathAPI.eval(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/apache/xml/utils/PrefixResolver;)Lorg/apache/xpath/objects/XObject;:1
org/apache/xpath/XPathAPI.selectNodeIterator(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/w3c/dom/traversal/NodeIterator;:0
org/apache/xpath/XPathAPI.selectNodeIterator(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/traversal/NodeIterator;:1
org/apache/xpath/XPathAPI.selectNodeList(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/w3c/dom/NodeList;:0
org/apache/xpath/XPathAPI.selectNodeList(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/NodeList;:1
org/apache/xpath/XPathAPI.selectSingleNode(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/w3c/dom/Node;:0
org/apache/xpath/XPathAPI.selectSingleNode(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/Node;:1

com/sun/org/apache/xpath/internal/XPathAPI.eval(Lorg/w3c/dom/Node;Ljava/lang/String;)Lcom/sun/org/apache/xpath/internal/objects/XObject;:0
com/sun/org/apache/xpath/internal/XPathAPI.eval(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lcom/sun/org/apache/xpath/internal/objects/XObject;:1
com/sun/org/apache/xpath/internal/XPathAPI.eval(Lorg/w3c/dom/Node;Ljava/lang/String;Lcom/sun/org/apache/xml/internal/utils/PrefixResolver;)Lcom/sun/org/apache/xpath/internal/objects/XObject;:1
com/sun/org/apache/xpath/internal/XPathAPI.selectNodeIterator(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/w3c/dom/traversal/NodeIterator;:0
com/sun/org/apache/xpath/internal/XPathAPI.selectNodeIterator(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/traversal/NodeIterator;:1
com/sun/org/apache/xpath/internal/XPathAPI.selectNodeList(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/w3c/dom/NodeList;:0
com/sun/org/apache/xpath/internal/XPathAPI.selectNodeList(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/NodeList;:1
com/sun/org/apache/xpath/internal/XPathAPI.selectSingleNode(Lorg/w3c/dom/Node;Ljava/lang/String;)Lorg/w3c/dom/Node;:0
com/sun/org/apache/xpath/internal/XPathAPI.selectSingleNode(Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/Node;:1

org/apache/xml/security/utils/XPathAPI.evaluate(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Z:1
org/apache/xml/security/utils/XPathAPI.selectNodeList(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/NodeList;:1

org/apache/xml/security/utils/JDKXPathAPI.evaluate(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Z:1
org/apache/xml/security/utils/JDKXPathAPI.selectNodeList(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/NodeList;:1

org/apache/xml/security/utils/XalanXPathAPI.evaluate(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Z:1
org/apache/xml/security/utils/XalanXPathAPI.selectNodeList(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;Lorg/w3c/dom/Node;)Lorg/w3c/dom/NodeList;:1
javax/xml/xpath/XPath.compile(Ljava/lang/String;)Ljavax/xml/xpath/XPathExpression;:0
javax/xml/xpath/XPath.evaluate(Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/String;:1
javax/xml/xpath/XPath.evaluate(Ljava/lang/String;Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;:2
javax/xml/xpath/XPath.evaluate(Ljava/lang/String;Lorg/xml/sax/InputSource;)Ljava/lang/String;:1
javax/xml/xpath/XPath.evaluate(Ljava/lang/String;Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;:2
javax/xml/transform/TransformerFactory.newTransformer(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Transformer;:0- Inherits from java.io.Writer
javax/servlet/jsp/JspWriter.write(Ljava/lang/String;)V:0
javax/servlet/jsp/JspWriter.write(Ljava/lang/String;II)V:2
javax/servlet/jsp/JspWriter.write([C)V:0
javax/servlet/jsp/JspWriter.write([CII)V:2
javax/servlet/jsp/JspWriter.append(Ljava/lang/CharSequence;)Ljava/io/PrintWriter;:0
javax/servlet/jsp/JspWriter.append(Ljava/lang/CharSequence;II)Ljava/io/PrintWriter;:2
javax/servlet/jsp/JspWriter.append(C)Ljava/io/PrintWriter;:0

- Sinks from javax.servlet.jsp.JspWriter
javax/servlet/jsp/JspWriter.print([C)V:0
javax/servlet/jsp/JspWriter.print(Ljava/lang/String;)V:0
javax/servlet/jsp/JspWriter.print(Ljava/lang/Object;)V:0
javax/servlet/jsp/JspWriter.print(C)V:0
javax/servlet/jsp/JspWriter.println([C)V:0
javax/servlet/jsp/JspWriter.println(Ljava/lang/String;)V:0
javax/servlet/jsp/JspWriter.println(Ljava/lang/Object;)V:0
javax/servlet/jsp/JspWriter.println(C)V:0

org/owasp/encoder/tag/ForHtmlTag.doTag()V:0play/api/mvc/Result.as(Ljava/lang/String;)Lplay/api/mvc/Result;:1- API reference:
- https://www.playframework.com/documentation/2.5.x/ScalaTemplates

play/twirl/api/Html$.apply(Ljava/lang/String;)Lplay/twirl/api/Html;:0java/io/PrintWriter.write(Ljava/lang/String;)V:0
java/io/PrintWriter.write(Ljava/lang/String;II)V:2
java/io/PrintWriter.write([C)V:0
java/io/PrintWriter.write([CII)V:2
java/io/PrintWriter.format(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;:0,1
java/io/PrintWriter.format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;:0,1
java/io/PrintWriter.print([C)V:0
java/io/PrintWriter.print(Ljava/lang/String;)V:0
java/io/PrintWriter.print(Ljava/lang/Object;)V:0
java/io/PrintWriter.print(C)V:0
java/io/PrintWriter.println([C)V:0
java/io/PrintWriter.println(Ljava/lang/String;)V:0
java/io/PrintWriter.println(Ljava/lang/Object;)V:0
java/io/PrintWriter.println(C)V:0
java/io/PrintWriter.printf(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;:0,1
java/io/PrintWriter.printf(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;:0,1
java/io/PrintWriter.append(Ljava/lang/CharSequence;)Ljava/io/PrintWriter;:0
java/io/PrintWriter.append(Ljava/lang/CharSequence;II)Ljava/io/PrintWriter;:2
java/io/PrintWriter.append(C)Ljava/io/PrintWriter;:0

javax/servlet/http/HttpServletResponse.sendError(ILjava/lang/String;)V:0
javax/servlet/http/HttpServletResponse.setStatus(ILjava/lang/String;)V:0
javax/servlet/http/HttpServletResponseWrapper.sendError(ILjava/lang/String;)V:0
javax/servlet/http/HttpServletResponseWrapper.setStatus(ILjava/lang/String;)V:0
javax/servlet/ServletOutputStream.print(Ljava/lang/String;)V:0
javax/servlet/ServletOutputStream.println(Ljava/lang/String;)V:0java/sql/DriverManager.getConnection(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/sql/Connection;#0
java/security/KeyStore$PasswordProtection.<init>([C)V#0
org/springframework/security/oauth2/config/annotation/builders/ClientDetailsServiceBuilder$ClientBuilder.secret(Ljava/lang/String;)Lorg/springframework/security/oauth2/config/annotation/builders/ClientDetailsServiceBuilder$ClientBuilder;#0

java/security/KeyStore.load(Ljava/io/InputStream;[C)V#0
javax/crypto/spec/PBEKeySpec.<init>([C)V#0
javax/crypto/spec/PBEKeySpec.<init>([C[BI)V#2
javax/crypto/spec/PBEKeySpec.<init>([C[BII)V#3
java/net/PasswordAuthentication.<init>(Ljava/lang/String;[C)V#0
javax/security/auth/callback/PasswordCallback.setPassword([C)V#0
java/security/KeyStore$PasswordProtection.<init>([C)V#0
javax/security/auth/kerberos/KerberosKey.<init>(Ljavax/security/auth/kerberos/KerberosPrincipal;[CLjava/lang/String;)V#1
javax/net/ssl/KeyManagerFactory.init(Ljava/security/KeyStore;[C)V#0

javax/crypto/spec/DESKeySpec.<init>([B)V#0
javax/crypto/spec/DESKeySpec.<init>([BI)V#1
javax/crypto/spec/DESedeKeySpec.<init>([B)V#0
javax/crypto/spec/DESedeKeySpec.<init>([BI)V#1
javax/crypto/spec/SecretKeySpec.<init>([BLjava/lang/String;)V#1
javax/crypto/spec/SecretKeySpec.<init>([BIILjava/lang/String;)V#3
java/security/spec/X509EncodedKeySpec.<init>([B)V#0
java/security/spec/PKCS8EncodedKeySpec.<init>([B)V#0
javax/security/auth/kerberos/KerberosKey.<init>(Ljavax/security/auth/kerberos/KerberosPrincipal;[BII)V#2
java/security/KeyRep.<init>(Ljava/security/KeyRep$Type;Ljava/lang/String;Ljava/lang/String;[B)V#0
javax/security/auth/kerberos/KerberosTicket.<init>([BLjavax/security/auth/kerberos/KerberosPrincipal;Ljavax/security/auth/kerberos/KerberosPrincipal;[BI[ZLjava/util/Date;Ljava/util/Date;Ljava/util/Date;Ljava/util/Date;[Ljava/net/InetAddress;)V#7
sun/security/provider/DSAPublicKeyImpl.<init>([B)V#0

java/security/spec/DSAPrivateKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1#2#3
java/security/spec/DSAPublicKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1#2#3
javax/crypto/spec/DHPrivateKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1#2
javax/crypto/spec/DHPublicKeySpec.<init> (Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1#2
java/security/spec/ECPrivateKeySpec.<init>(Ljava/math/BigInteger;Ljava/security/spec/ECParameterSpec;)V#0#1
java/security/spec/RSAPrivateKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1
java/security/spec/RSAMultiPrimePrivateCrtKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;[Ljava/security/spec/RSAOtherPrimeInfo;)V#1#2#3#4#5#6#7#8
java/security/spec/RSAPrivateCrtKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1#2#3#4#5#6#7
java/security/spec/RSAPublicKeySpec.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1
sun/security/provider/DSAPublicKeyImpl.<init>(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V#0#1#2#3
sun/security/provider/DSAPublicKeyImpl.<init>([B)V#0
--Apache Commons Lang 2
org/apache/commons/lang/StringEscapeUtils.escapeCsv(Ljava/lang/String;)Ljava/lang/String;:0
org/apache/commons/lang/StringEscapeUtils.unescapeCsv(Ljava/lang/String;)Ljava/lang/String;:0
org/apache/commons/lang/StringEscapeUtils.escapeHtml(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang/StringEscapeUtils.unescapeHtml(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang/StringEscapeUtils.escapeJava(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang/StringEscapeUtils.unescapeJava(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang/StringEscapeUtils.escapeJavaScript(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang/StringEscapeUtils.unescapeJavaScript(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang/StringEscapeUtils.escapeSql(Ljava/lang/String;)Ljava/lang/String;:0|+SQL_INJECTION_SAFE
org/apache/commons/lang/StringEscapeUtils.escapeXml(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/apache/commons/lang/StringEscapeUtils.unescapeXml(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE,-XPATH_INJECTION_SAFE

--Apache Commons Lang 3
org/apache/commons/lang3/StringEscapeUtils.escapeCsv(Ljava/lang/String;)Ljava/lang/String;:0
org/apache/commons/lang3/StringEscapeUtils.unescapeCsv(Ljava/lang/String;)Ljava/lang/String;:0
org/apache/commons/lang3/StringEscapeUtils.escapeEcmaScript(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.unescapeEcmaScript(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeHtml3(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.unescapeHtml3(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeHtml4(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.unescapeHtml4(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeJava(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.unescapeJava(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeJson(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.unescapeJson(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeXml(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/apache/commons/lang3/StringEscapeUtils.unescapeXml(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE,-XPATH_INJECTION_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeXml10(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/apache/commons/lang3/StringEscapeUtils.escapeXml11(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE

org/apache/commons/text/StringEscapeUtils.escapeHtml3(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/text/StringEscapeUtils.escapeHtml4(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/text/StringEscapeUtils.escapeEcmaScript(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/text/StringEscapeUtils.escapeXml10(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/apache/commons/text/StringEscapeUtils.escapeXml11(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE

org/apache/commons/io/FilenameUtils.getName(Ljava/lang/String;)Ljava/lang/String;:0|+PATH_TRAVERSAL_SAFE
org/apache/commons/io/FilenameUtils.getExtension(Ljava/lang/String;)Ljava/lang/String;:0|+PATH_TRAVERSAL_SAFE
org/apache/commons/io/FilenameUtils.getBaseName(Ljava/lang/String;)Ljava/lang/String;:0|+PATH_TRAVERSAL_SAFE
java/net/URLEncoder.encode(Ljava/lang/String;)Ljava/lang/String;:0|+URL_ENCODED,+XSS_SAFE
java/net/URLEncoder.encode(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1|+URL_ENCODED,+XSS_SAFE
java/net/URLDecoder.decode(Ljava/lang/String;)Ljava/lang/String;:0|-URL_ENCODED,-XSS_SAFE
java/net/URLDecoder.decode(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1|-URL_ENCODED,-XSS_SAFE

--Spring Framework
org/springframework/web/util/HtmlUtils.htmlEscape(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/springframework/web/util/HtmlUtils.htmlEscape(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1|+XSS_SAFE
org/springframework/web/util/HtmlUtils.htmlUnescape(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/springframework/web/util/HtmlUtils.htmlEscapeDecimal(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/springframework/web/util/HtmlUtils.htmlEscapeDecimal(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1|+XSS_SAFE
org/springframework/web/util/HtmlUtils.htmlEscapeHex(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/springframework/web/util/HtmlUtils.htmlEscapeHex(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1|+XSS_SAFE
org/springframework/web/util/JavaScriptUtils.javaScriptEscape(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE

org/springframework/util/StringUtils.getFilename(Ljava/lang/String;)Ljava/lang/String;:SAFE
org/springframework/util/StringUtils.getFilenameExtension(Ljava/lang/String;)Ljava/lang/String;:SAFE

--Safe date values
java/util/Calendar.getDisplayName(IILjava/util/Locale;)Ljava/lang/String;:SAFE
java/util/Calendar.getDisplayNames(IILjava/util/Locale;)Ljava/util/Map;:SAFE
java/util/UUID.randomUUID()Ljava/util/UUID;:SAFE

--Hash values should not be malicious even if the input is controlled by the user (exploitability is unlikely)
java/security/MessageDigest.digest([B)[B:SAFE

--Hexadecimal representation
javax/xml/bind/DatatypeConverter.printHexBinary([B)Ljava/lang/String;:SAFE
org/apache/commons/codec/binary/Hex.encodeHex([B)[C:SAFE
org/apache/commons/codec/binary/Hex.encodeHex([BZ)[C:SAFE
org/apache/commons/codec/binary/Hex.encodeHexString([B)Ljava/lang/String;:SAFE
org/apache/commons/codec/binary/Hex.encodeHexString([BZ)Ljava/lang/String;:SAFE

--Google Guava
com/google/common/escape/Escaper.escape(Ljava/lang/String;)Ljava/lang/String;:0|+URL_ENCODED,+XSS_SAFE--ESAPI
org/owasp/esapi/Encoder.canonicalize(Ljava/lang/String;)Ljava/lang/String;:0
org/owasp/esapi/Encoder.canonicalize(Ljava/lang/String;Z)Ljava/lang/String;:1
org/owasp/esapi/Encoder.canonicalize(Ljava/lang/String;ZZ)Ljava/lang/String;:2
org/owasp/esapi/Encoder.encodeForBase64([BZ)Ljava/lang/String;:SAFE
org/owasp/esapi/Encoder.encodeForCSS(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/esapi/Encoder.encodeForDN(Ljava/lang/String;)Ljava/lang/String;:0|+LDAP_INJECTION_SAFE
org/owasp/esapi/Encoder.encodeForHTML(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/esapi/Encoder.decodeForHTML(Ljava/lang/String;)Ljava/lang/String;:0|-XSS_SAFE
org/owasp/esapi/Encoder.encodeForHTMLAttribute(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/esapi/Encoder.encodeForJavaScript(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/esapi/Encoder.encodeForLDAP(Ljava/lang/String;)Ljava/lang/String;:0|+LDAP_INJECTION_SAFE
org/owasp/esapi/Encoder.encodeForOS(Lorg/owasp/esapi/codecs/Codec;Ljava/lang/String;)Ljava/lang/String;:0|+COMMAND_INJECTION_SAFE
org/owasp/esapi/Encoder.encodeForSQL(Lorg/owasp/esapi/codecs/Codec;Ljava/lang/String;)Ljava/lang/String;:0|+SQL_INJECTION_SAFE
org/owasp/esapi/Encoder.encodeForURL(Ljava/lang/String;)Ljava/lang/String;:0|+URL_ENCODED,+XSS_SAFE
org/owasp/esapi/Encoder.decodeFromURL(Ljava/lang/String;)Ljava/lang/String;:0|-URL_ENCODED,-XSS_SAFE
org/owasp/esapi/Encoder.encodeForVBScript(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/esapi/Encoder.encodeForXML(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/owasp/esapi/Encoder.encodeForXMLAttribute(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/owasp/esapi/Encoder.encodeForXPath(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE

--OWASP Encoder
org/owasp/encoder/Encode.forCDATA(Ljava/lang/String;)Ljava/lang/String;:0
org/owasp/encoder/Encode.forCssString(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forCssUrl(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forHtml(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forHtmlAttribute(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forHtmlContent(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forHtmlUnquotedAttribute(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forJava(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forJavaScript(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forJavaScriptAttribute(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forJavaScriptBlock(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forJavaScriptSource(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/encoder/Encode.forUri(Ljava/lang/String;)Ljava/lang/String;:0|+CR_ENCODED,+LF_ENCODED,+XSS_SAFE
org/owasp/encoder/Encode.forUriComponent(Ljava/lang/String;)Ljava/lang/String;:0|+URL_ENCODED,+XSS_SAFE
org/owasp/encoder/Encode.forXml(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/owasp/encoder/Encode.forXmlAttribute(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE,+XPATH_INJECTION_SAFE
org/owasp/encoder/Encode.forXmlComment(Ljava/lang/String;)Ljava/lang/String;:0
org/owasp/encoder/Encode.forXmlContent(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE

org/owasp/html/PolicyFactory.sanitize(Ljava/lang/String;)Ljava/lang/String;:0|+XSS_SAFE
org/owasp/html/PolicyFactory.sanitize(Ljava/lang/String;Lorg/owasp/html/HtmlChangeListener;Ljava/lang/Object;)Ljava/lang/String;:2|+XSS_SAFE
--DatabaseUtils

android/database/DatabaseUtils.concatenateWhere(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1#2

android/database/DatabaseUtils.appendEscapedSQLString(Ljava/lang/StringBuilder;Ljava/lang/String;)V:0|+SQL_INJECTION_SAFE
android/database/DatabaseUtils.sqlEscapeString(Ljava/lang/String;)Ljava/lang/String;:0|+SQL_INJECTION_SAFE
android/database/DatabaseUtils.appendValueToSql(Ljava/lang/StringBuilder;Ljava/lang/Object;)V:0|+SQL_INJECTION_SAFE

android/database/sqlite/SQLiteQueryBuilder.appendWhereEscapeString(Ljava/lang/String;)V:0|+SQL_INJECTION_SAFE
java/util/Collection.add(Ljava/lang/Object;)Z:0,1#1
java/util/Collection.addAll(Ljava/util/Collection;)Z:0,1#1
java/util/Collection.contains(Ljava/lang/Object;)Z:0#0
java/util/Collection.containsAll(Ljava/util/Collection;)Z:0#0
java/util/Collection.clear()V:SAFE#0
java/util/Collection.remove(Ljava/lang/Object;)Z:1
java/util/Collection.removeAll(Ljava/util/Collection;)Z:1
java/util/Collection.removeIf(Ljava/util/function/Predicate;)Z:1#1
java/util/Collection.retainAll(Ljava/util/Collection;)Z:1
java/util/Collection.toArray()[Ljava/lang/Object;:0
java/util/Collection.toArray([Ljava/lang/Object;)[Ljava/lang/Object;:1


java/util/Iterator.next()Ljava/lang/Object;:0


-- Lists, queues etc.

java/util/List.add(ILjava/lang/Object;)V:0,2#2
java/util/List.addAll(ILjava/util/Collection;)Z:0,2#2
java/util/List.get(I)Ljava/lang/Object;:1
java/util/List.indexOf(Ljava/lang/Object;)I:UNKNOWN
java/util/List.lastIndexOf(Ljava/lang/Object;)I:UNKNOWN
java/util/List.listIterator()Ljava/util/ListIterator;:0,UNKNOWN#0
java/util/List.listIterator(I)Ljava/util/ListIterator;:1,UNKNOWN#1
java/util/List.remove()Ljava/lang/Object;:0
java/util/List.remove(I)Ljava/lang/Object;:1
java/util/List.replaceAll(Ljava/util/function/UnaryOperator;)V:1#1
java/util/List.retainAll(Ljava/util/Collection;)Z:1
java/util/List.set(ILjava/lang/Object;)Ljava/lang/Object;:0,2#2
java/util/List.sort(Ljava/util/Comparator;)V:1
java/util/List.subList(II)Ljava/util/List;:2#2
java/util/List.toArray()[Ljava/lang/Object;:0
java/util/List.toArray([Ljava/lang/Object;)[Ljava/lang/Object;:1


- ListIterator is never SAFE, because it can modify the list and the taint is not propagated to it
java/util/ListIterator.add(Ljava/lang/Object;)V:0,1#1
java/util/ListIterator.previous()Ljava/lang/Object;:0
java/util/ListIterator.set(Ljava/lang/Object;)V:0,1#1


java/util/ArrayList.<init>()V:SAFE
java/util/ArrayList.<init>(I)V:SAFE
java/util/ArrayList.<init>(Ljava/util/Collection;)V:0#1,2

java/util/concurrent/CopyOnWriteArrayList.<init>()V:SAFE
java/util/concurrent/CopyOnWriteArrayList.<init>(Ljava/util/Collection;)V:0#1,2
java/util/concurrent/CopyOnWriteArrayList.<init>([Ljava/lang/Object;)V:0#1,2


java/util/Queue.element()Ljava/lang/Object;:0
java/util/Queue.offer(Ljava/lang/Object;)Z:0,1#1
java/util/Queue.peek()Ljava/lang/Object;:0
java/util/Queue.poll()Ljava/lang/Object;:0
java/util/Queue.remove()Ljava/lang/Object;:0


java/util/Deque.addFirst(Ljava/lang/Object;)V:0,1#1
java/util/Deque.addLast(Ljava/lang/Object;)V:0,1#1
java/util/Deque.descendingIterator()Ljava/util/Iterator;:0
java/util/Deque.getFirst()Ljava/lang/Object;:0
java/util/Deque.getLast()Ljava/lang/Object;:0
java/util/Deque.offerFirst(Ljava/lang/Object;)Z:0,1#1
java/util/Deque.offerLast(Ljava/lang/Object;)Z:0,1#1
java/util/Deque.peekFirst()Ljava/lang/Object;:0
java/util/Deque.peekLast()Ljava/lang/Object;:0
java/util/Deque.pollFirst()Ljava/lang/Object;:0
java/util/Deque.pollLast()Ljava/lang/Object;:0
java/util/Deque.pop()Ljava/lang/Object;:0
java/util/Deque.push(Ljava/lang/Object;)V:0,1#1
java/util/Deque.removeFirst()Ljava/lang/Object;:0
java/util/Deque.removeFirstOccurrence(Ljava/lang/Object;)Z:1
java/util/Deque.removeLast()Ljava/lang/Object;:0
java/util/Deque.removeLastOccurrence(Ljava/lang/Object;)Z:1


java/util/ArrayDeque.<init>()V:SAFE
java/util/ArrayDeque.<init>(Ljava/util/Collection;)V:0#1,2
java/util/ArrayDeque.<init>(I)V:SAFE

java/util/concurrent/ConcurrentLinkedDeque.<init>()V:SAFE
java/util/concurrent/ConcurrentLinkedDeque.<init>(Ljava/util/Collection;)V:0#1,2


java/util/LinkedList.<init>()V:SAFE
java/util/LinkedList.<init>(Ljava/util/Collection;)V:0#1,2
java/util/LinkedList.get(I)Ljava/lang/Object;:1
java/util/LinkedList.set(ILjava/lang/Object;)Ljava/lang/Object;:0,2#2


java/util/Vector.<init>()V:SAFE
java/util/Vector.<init>(Ljava/util/Collection;)V:0#1,2
java/util/Vector.<init>(I)V:SAFE
java/util/Vector.<init>(II)V:SAFE
java/util/Vector.add(ILjava/lang/Object;)V:0,2#2
java/util/Vector.addAll(ILjava/util/Collection;)Z:0,2#2
java/util/Vector.addElement(Ljava/lang/Object;)V:0,1#1
java/util/Vector.copyInto([Ljava/lang/Object;)V:1#0
java/util/Vector.elementAt(I)Ljava/lang/Object;:1
java/util/Vector.elements()Ljava/util/Enumeration;:0
java/util/Vector.firstElement()Ljava/lang/Object;:0
java/util/Vector.insertElementAt(Ljava/lang/Object;I)V:1,2#2
java/util/Vector.setElementAt(Ljava/lang/Object;I)V:1,2#2
java/util/Vector.sort(Ljava/util/Comparator;)V:UNKNOWN


java/util/Stack.<init>()V:SAFE
java/util/Stack.peek()Ljava/lang/Object;:0
java/util/Stack.pop()Ljava/lang/Object;:0
java/util/Stack.push(Ljava/lang/Object;)Ljava/lang/Object;:0,1#1
java/util/Stack.search(Ljava/lang/Object;)I:UNKNOWN


java/util/Enumeration.nextElement()Ljava/lang/Object;:0


java/util/Arrays.asList([Ljava/lang/Object;)Ljava/util/List;:0


-- Sets
- Set interface adds no new methods

java/util/HashSet.<init>()V:SAFE
java/util/HashSet.<init>(Ljava/util/Collection;)V:0#1,2
java/util/HashSet.<init>(I)V:SAFE
java/util/HashSet.<init>(IF)V:SAFE

java/util/LinkedHashSet.<init>()V:SAFE
java/util/LinkedHashSet.<init>(Ljava/util/Collection;)V:0#1,2
java/util/LinkedHashSet.<init>(I)V:SAFE
java/util/LinkedHashSet.<init>(IF)V:SAFE


java/util/SortedSet.first()Ljava/lang/Object;:0
java/util/SortedSet.headSet(Ljava/lang/Object;)Ljava/util/SortedSet;:0,1
java/util/SortedSet.last()Ljava/lang/Object;:0
java/util/SortedSet.tailSet(Ljava/lang/Object;)Ljava/util/SortedSet;:0,1
java/util/SortedSet.subSet(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;:0,1,2


java/util/NavigableSet.ceiling(Ljava/lang/Object;)Ljava/lang/Object;:0,1
java/util/NavigableSet.descendingIterator()Ljava/util/Iterator;:0
java/util/NavigableSet.descendingSet()Ljava/util/NavigableSet;:0
java/util/NavigableSet.floor(Ljava/lang/Object;)Ljava/lang/Object;:0,1
java/util/NavigableSet.headSet(Ljava/lang/Object;Z)Ljava/util/NavigableSet;:1,2
java/util/NavigableSet.higher(Ljava/lang/Object;)Ljava/lang/Object;:0,1
java/util/NavigableSet.lower(Ljava/lang/Object;)Ljava/lang/Object;:0,1
java/util/NavigableSet.pollFirst()Ljava/lang/Object;:0
java/util/NavigableSet.pollLast()Ljava/lang/Object;:0
java/util/NavigableSet.subSet(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableSet;:1,3,4
java/util/NavigableSet.tailSet(Ljava/lang/Object;Z)Ljava/util/NavigableSet;:1,2


java/util/TreeSet.<init>()V:SAFE
java/util/TreeSet.<init>(Ljava/util/Collection;)V:0#1,2
java/util/TreeSet.<init>(Ljava/util/Comparator;)V:SAFE
java/util/TreeSet.<init>(Ljava/util/SortedSet;)V:0#1,2


java/util/concurrent/ConcurrentSkipListSet.<init>()V:SAFE
java/util/concurrent/ConcurrentSkipListSet.<init>(Ljava/util/Collection;)V:0#1,2
java/util/concurrent/ConcurrentSkipListSet.<init>(Ljava/util/Comparator;)V:SAFE
java/util/concurrent/ConcurrentSkipListSet.<init>(Ljava/util/SortedSet;)V:0#1,2

java/util/concurrent/CopyOnWriteArraySet.<init>()V:SAFE
java/util/concurrent/CopyOnWriteArraySet.<init>(Ljava/util/Collection;)V:0#1,2


-- Maps

java/util/Map.clear()V:SAFE#0
java/util/Map.compute(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;:0,1,2#2
java/util/Map.computeIfAbsent(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;:1,2,UNKNOWN#2
java/util/Map.computeIfPresent(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;:1,2,UNKNOWN#2
java/util/Map.containsKey(Ljava/lang/Object;)Z:UNKNOWN
java/util/Map.containsValue(Ljava/lang/Object;)Z:UNKNOWN
java/util/Map.entrySet()Ljava/util/Set;:0
java/util/Map.forEach(Ljava/util/function/BiConsumer;)V:0,1#1
java/util/Map.get(Ljava/lang/Object;)Ljava/lang/Object;:1
java/util/Map.getOrDefault(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;:0,2
java/util/Map.keySet()Ljava/util/Set;:0
java/util/Map.merge(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;:0,1,2,3#3
java/util/Map.put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;:0,1,2#2
java/util/Map.putAll(Ljava/util/Map;)V:0,1#1
java/util/Map.putIfAbsent(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;:0,1,2#2
java/util/Map.remove(Ljava/lang/Object;)Ljava/lang/Object;:1
java/util/Map.remove(Ljava/lang/Object;Ljava/lang/Object;)Z:UNKNOWN
java/util/Map.replace(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;:0,1,2#2
java/util/Map.replace(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z:0,2,3#3
java/util/Map.replaceAll(Ljava/util/function/BiFunction;)V:0,1#1
java/util/Map.values()Ljava/util/Collection;:0

java/util/Map$Entry.getKey()Ljava/lang/Object;:0
java/util/Map$Entry.getValue()Ljava/lang/Object;:0
java/util/Map$Entry.setValue(Ljava/lang/Object;)Ljava/lang/Object;:0,1#1


java/util/HashMap.<init>()V:SAFE
java/util/HashMap.<init>(I)V:SAFE
java/util/HashMap.<init>(IF)V:SAFE
java/util/HashMap.<init>(Ljava/util/Map;)V:0#1,2

java/util/LinkedHashMap.<init>()V:SAFE
java/util/LinkedHashMap.<init>(I)V:SAFE
java/util/LinkedHashMap.<init>(IF)V:SAFE
java/util/LinkedHashMap.<init>(IFZ)V:SAFE
java/util/LinkedHashMap.<init>(Ljava/util/Map;)V:0#1,2

java/util/WeakHashMap.<init>()V:SAFE
java/util/WeakHashMap.<init>(I)V:SAFE
java/util/WeakHashMap.<init>(IF)V:SAFE
java/util/WeakHashMap.<init>(Ljava/util/Map;)V:0#1,2

java/util/IdentityHashMap.<init>()V:SAFE
java/util/IdentityHashMap.<init>(I)V:SAFE
java/util/IdentityHashMap.<init>(Ljava/util/Map;)V:0#1,2

- NavigableMap and SortedMap not supported yet

java/util/TreeMap.<init>()V:SAFE
java/util/TreeMap.<init>(Ljava/util/Comparator;)V:SAFE
java/util/TreeMap.<init>(Ljava/util/Map;)V:SAFE
java/util/TreeMap.<init>(Ljava/util/SortedMap;)V:SAFE


java/util/Dictionary.elements()Ljava/util/Enumeration;:0
java/util/Dictionary.get(Ljava/lang/Object;)Ljava/lang/Object;:1
java/util/Dictionary.keys()Ljava/util/Enumeration;:0
java/util/Dictionary.put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;:0,1,2#2
java/util/Dictionary.remove(Ljava/lang/Object;)Ljava/lang/Object;:1

java/util/Hashtable.<init>()V:SAFE
java/util/Hashtable.<init>(I)V:SAFE
java/util/Hashtable.<init>(IF)V:SAFE
java/util/Hashtable.<init>(Ljava/util/Map;)V:0#1,2


java/util/Properties.<init>()V:SAFE
java/util/Properties.<init>(Ljava/util/Properties;)V:0#1,2
java/util/Properties.getProperty(Ljava/lang/String;)Ljava/lang/String;:1
java/util/Properties.getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,2
java/util/Properties.load(Ljava/io/InputStream;)V:TAINTED#1
java/util/Properties.load(Ljava/io/Reader;)V:TAINTED#1
java/util/Properties.loadFromXML(Ljava/io/InputStream;)V:TAINTED#1
java/util/Properties.propertyNames()Ljava/util/Enumeration;:0
java/util/Properties.setProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;:0,1,2#2
java/util/Properties.stringPropertyNames()Ljava/util/Set;:0


-- Utility class Collections

java/util/Collections.addAll(Ljava/util/Collection;[Ljava/lang/Object;)Z:0,1#1
java/util/Collections.asLifoQueue(Ljava/util/Deque;)Ljava/util/Queue;:0
java/util/Collections.binarySearch(Ljava/util/List;Ljava/lang/Object;)I:UNKNOWN
java/util/Collections.binarySearch(Ljava/util/List;Ljava/lang/Object;Ljava/util/Comparator;)I:UNKNOWN
java/util/Collections.checkedCollection(Ljava/util/Collection;Ljava/lang/Class;)Ljava/util/Collection;:1
java/util/Collections.checkedList(Ljava/util/List;Ljava/lang/Class;)Ljava/util/List;:1
java/util/Collections.checkedMap(Ljava/util/Map;Ljava/lang/Class;Ljava/lang/Class;)Ljava/util/Map;:2
java/util/Collections.checkedNavigableMap(Ljava/util/NavigableMap;Ljava/lang/Class;Ljava/lang/Class;)Ljava/util/NavigableMap;:2
java/util/Collections.checkedNavigableSet(Ljava/util/NavigableSet;Ljava/lang/Class;)Ljava/util/NavigableSet;:1
java/util/Collections.checkedQueue(Ljava/util/Queue;Ljava/lang/Class;)Ljava/util/Queue;:1
java/util/Collections.checkedSet(Ljava/util/Set;Ljava/lang/Class;)Ljava/util/Set;:1
java/util/Collections.checkedSortedMap(Ljava/util/SortedMap;Ljava/lang/Class;Ljava/lang/Class;)Ljava/util/SortedMap;:2
java/util/Collections.checkedSortedSet(Ljava/util/SortedSet;Ljava/lang/Class;)Ljava/util/SortedSet;:1
java/util/Collections.copy(Ljava/util/List;Ljava/util/List;)V:0,1#1
java/util/Collections.disjoint(Ljava/util/Collection;Ljava/util/Collection;)Z:UNKNOWN
java/util/Collections.emptyEnumeration()Ljava/util/Enumeration;:SAFE
java/util/Collections.emptyIterator()Ljava/util/Iterator;:SAFE
java/util/Collections.emptyListIterator()Ljava/util/ListIterator;:SAFE
java/util/Collections.emptyMap()Ljava/util/Map;:SAFE
java/util/Collections.emptyNavigableMap()Ljava/util/NavigableMap;:SAFE
java/util/Collections.emptyNavigableSet()Ljava/util/NavigableSet;:SAFE
java/util/Collections.emptySet()Ljava/util/Set;:SAFE
java/util/Collections.emptySortedMap()Ljava/util/SortedMap;:SAFE
java/util/Collections.emptySortedSet()Ljava/util/SortedSet;:SAFE
java/util/Collections.enumeration(Ljava/util/Collection;)Ljava/util/Enumeration;:0
java/util/Collections.fill(Ljava/util/List;Ljava/lang/Object;)V:0#1
java/util/Collections.frequency(Ljava/util/Collection;Ljava/lang/Object;)I:UNKNOWN
java/util/Collections.indexOfSubList(Ljava/util/List;Ljava/util/List;)I:UNKNOWN
java/util/Collections.lastIndexOfSubList(Ljava/util/List;Ljava/util/List;)I:UNKNOWN
java/util/Collections.list(Ljava/util/Enumeration;)Ljava/util/ArrayList;:0
java/util/Collections.max(Ljava/util/Collection;)Ljava/lang/Object;:0
java/util/Collections.max(Ljava/util/Collection;Ljava/util/Comparator;)Ljava/lang/Object;:1
java/util/Collections.min(Ljava/util/Collection;)Ljava/lang/Object;:0
java/util/Collections.min(Ljava/util/Collection;Ljava/util/Comparator;)Ljava/lang/Object;:1
java/util/Collections.nCopies(ILjava/lang/Object;)Ljava/util/List;:0
java/util/Collections.newSetFromMap(Ljava/util/Map;)Ljava/util/Set;:0
java/util/Collections.replaceAll(Ljava/util/List;Ljava/lang/Object;Ljava/lang/Object;)Z:0,2#2
java/util/Collections.reverse(Ljava/util/List;)V:UNKNOWN
java/util/Collections.rotate(Ljava/util/List;I)V:UNKNOWN
java/util/Collections.shuffle(Ljava/util/List;)V:UNKNOWN
java/util/Collections.shuffle(Ljava/util/List;Ljava/util/Random;)V:UNKNOWN
java/util/Collections.singleton(Ljava/lang/Object;)Ljava/util/Set;:0
java/util/Collections.singletonList(Ljava/lang/Object;)Ljava/util/List;:0
java/util/Collections.singletonMap(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;:0,1
java/util/Collections.sort(Ljava/util/List;)V:UNKNOWN
java/util/Collections.sort(Ljava/util/List;Ljava/util/Comparator;)V:UNKNOWN
java/util/Collections.swap(Ljava/util/List;II)V:UNKNOWN
java/util/Collections.synchronizedCollection(Ljava/util/Collection;)Ljava/util/Collection;:0
java/util/Collections.synchronizedList(Ljava/util/List;)Ljava/util/List;:0
java/util/Collections.synchronizedMap(Ljava/util/Map;)Ljava/util/Map;:0
java/util/Collections.synchronizedNavigableMap(Ljava/util/NavigableMap;)Ljava/util/NavigableMap;:0
java/util/Collections.synchronizedNavigableSet(Ljava/util/NavigableSet;)Ljava/util/NavigableSet;:0
java/util/Collections.synchronizedSet(Ljava/util/Set;)Ljava/util/Set;:0
java/util/Collections.synchronizedSortedMap(Ljava/util/SortedMap;)Ljava/util/SortedMap;:0
java/util/Collections.synchronizedSortedSet(Ljava/util/SortedSet;)Ljava/util/SortedSet;:0
java/util/Collections.unmodifiableCollection(Ljava/util/Collection;)Ljava/util/Collection;:0
java/util/Collections.unmodifiableList(Ljava/util/List;)Ljava/util/List;:0
java/util/Collections.unmodifiableMap(Ljava/util/Map;)Ljava/util/Map;:0
java/util/Collections.unmodifiableNavigableMap(Ljava/util/NavigableMap;)Ljava/util/NavigableMap;:0
java/util/Collections.unmodifiableNavigableSet(Ljava/util/NavigableSet;)Ljava/util/NavigableSet;:0
java/util/Collections.unmodifiableSet(Ljava/util/Set;)Ljava/util/Set;:0
java/util/Collections.unmodifiableSortedMap(Ljava/util/SortedMap;)Ljava/util/SortedMap;:0
java/util/Collections.unmodifiableSortedSet(Ljava/util/SortedSet;)Ljava/util/SortedSet;:0
io/dropwizard/servlets/Servlets.getFullUrl(Ljavax/servlet/http/HttpServletRequest;)Ljava/lang/String;:TAINTED

--Avoid tainting argument
com/google/common/base/Optional.or(Ljava/lang/Object;)Ljava/lang/Object;:0,1#2
javax/servlet/ServletRequest.getAttributeNames()Ljava/util/Enumeration;:SAFE
javax/servlet/ServletRequest.getCharacterEncoding()Ljava/lang/String;:SAFE
javax/servlet/ServletRequest.getContentType()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequest.getLocalAddr()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequest.getLocalName()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequest.getParameter(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/servlet/ServletRequest.getParameterMap()Ljava/util/Map;:TAINTED
javax/servlet/ServletRequest.getParameterNames()Ljava/util/Enumeration;:TAINTED
javax/servlet/ServletRequest.getParameterValues(Ljava/lang/String;)[Ljava/lang/String;:TAINTED
javax/servlet/ServletRequest.getProtocol()Ljava/lang/String;:SAFE
javax/servlet/ServletRequest.getRealPath(Ljava/lang/String;)Ljava/lang/String;:0
javax/servlet/ServletRequest.getRemoteAddr()Ljava/lang/String;:SAFE
javax/servlet/ServletRequest.getRemoteHost()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequest.getRequestDispatcher(Ljava/lang/String;)Ljavax/servlet/RequestDispatcher;:0
javax/servlet/ServletRequest.getScheme()Ljava/lang/String;:SAFE
javax/servlet/ServletRequest.getServerName()Ljava/lang/String;:TAINTED

- better keep those, J2EE interfaces can be unavailable to analysis
javax/servlet/http/HttpServletRequest.getAttributeNames()Ljava/util/Enumeration;:SAFE
javax/servlet/http/HttpServletRequest.changeSessionId()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getAuthType()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getCharacterEncoding()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getContentType()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getContextPath()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getCookies()[Ljavax/servlet/http/Cookie;:TAINTED
javax/servlet/http/HttpServletRequest.getHeader(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getHeaderNames()Ljava/util/Enumeration;:TAINTED
javax/servlet/http/HttpServletRequest.getHeaders(Ljava/lang/String;)Ljava/util/Enumeration;:TAINTED
javax/servlet/http/HttpServletRequest.getLocalAddr()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getLocalName()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getMethod()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getParameter(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getParameterMap()Ljava/util/Map;:TAINTED
javax/servlet/http/HttpServletRequest.getParameterNames()Ljava/util/Enumeration;:TAINTED
javax/servlet/http/HttpServletRequest.getParameterValues(Ljava/lang/String;)[Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getProtocol()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getPathInfo()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getPathTranslated()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getQueryString()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getRealPath(Ljava/lang/String;)Ljava/lang/String;:0
javax/servlet/http/HttpServletRequest.getRemoteAddr()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getRemoteHost()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getRemoteUser()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getRequestDispatcher(Ljava/lang/String;)Ljavax/servlet/RequestDispatcher;:0
javax/servlet/http/HttpServletRequest.getRequestURI()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getRequestURL()Ljava/lang/StringBuffer;:TAINTED
javax/servlet/http/HttpServletRequest.getScheme()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequest.getServerName()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequest.getServletPath()Ljava/lang/String;:TAINTED

javax/servlet/http/HttpServletRequestWrapper.getAttributeNames()Ljava/util/Enumeration;:SAFE
javax/servlet/http/HttpServletRequestWrapper.changeSessionId()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getAuthType()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getCharacterEncoding()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getContentType()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getContextPath()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getCookies()[Ljavax/servlet/http/Cookie;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getHeader(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getHeaderNames()Ljava/util/Enumeration;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getHeaders(Ljava/lang/String;)Ljava/util/Enumeration;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getLocalAddr()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getLocalName()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getMethod()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getParameter(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getParameterMap()Ljava/util/Map;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getParameterNames()Ljava/util/Enumeration;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getParameterValues(Ljava/lang/String;)[Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getProtocol()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getPathInfo()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getPathTranslated()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getQueryString()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getRealPath(Ljava/lang/String;)Ljava/lang/String;:0
javax/servlet/http/HttpServletRequestWrapper.getRemoteAddr()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getRemoteHost()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getRemoteUser()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getRequestDispatcher(Ljava/lang/String;)Ljavax/servlet/RequestDispatcher;:0
javax/servlet/http/HttpServletRequestWrapper.getRequestURI()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getRequestURL()Ljava/lang/StringBuffer;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getScheme()Ljava/lang/String;:SAFE
javax/servlet/http/HttpServletRequestWrapper.getServerName()Ljava/lang/String;:TAINTED
javax/servlet/http/HttpServletRequestWrapper.getServletPath()Ljava/lang/String;:TAINTED

javax/servlet/ServletRequestWrapper.getAttributeNames()Ljava/util/Enumeration;:SAFE
javax/servlet/ServletRequestWrapper.getCharacterEncoding()Ljava/lang/String;:SAFE
javax/servlet/ServletRequestWrapper.getContentType()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequestWrapper.getLocalAddr()Ljava/lang/String;:SAFE
javax/servlet/ServletRequestWrapper.getLocalName()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequestWrapper.getParameter(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/servlet/ServletRequestWrapper.getParameterMap()Ljava/util/Map;:TAINTED
javax/servlet/ServletRequestWrapper.getParameterNames()Ljava/util/Enumeration;:TAINTED
javax/servlet/ServletRequestWrapper.getParameterValues(Ljava/lang/String;)[Ljava/lang/String;:TAINTED
javax/servlet/ServletRequestWrapper.getProtocol()Ljava/lang/String;:SAFE
javax/servlet/ServletRequestWrapper.getRealPath(Ljava/lang/String;)Ljava/lang/String;:0
javax/servlet/ServletRequestWrapper.getRemoteAddr()Ljava/lang/String;:SAFE
javax/servlet/ServletRequestWrapper.getRemoteHost()Ljava/lang/String;:TAINTED
javax/servlet/ServletRequestWrapper.getRequestDispatcher(Ljava/lang/String;)Ljavax/servlet/RequestDispatcher;:0
javax/servlet/ServletRequestWrapper.getScheme()Ljava/lang/String;:SAFE
javax/servlet/ServletRequestWrapper.getServerName()Ljava/lang/String;:TAINTED


javax/servlet/http/Cookie.getComment()Ljava/lang/String;:TAINTED
javax/servlet/http/Cookie.getDomain()Ljava/lang/String;:TAINTED
javax/servlet/http/Cookie.getName()Ljava/lang/String;:TAINTED
javax/servlet/http/Cookie.getPath()Ljava/lang/String;:TAINTED
javax/servlet/http/Cookie.getValue()Ljava/lang/String;:TAINTED


-javax/servlet/ServletConfig.getInitParameter(Ljava/lang/String;)Ljava/lang/String;:?
-javax/servlet/ServletConfig.getInitParameterNames()Ljava/util/Enumeration;:?
-javax/servlet/ServletConfig.getServletName()Ljava/lang/String;:SAFE


javax/servlet/ServletContext.getContextPath()Ljava/lang/String;:SAFE
-javax/servlet/ServletContext.getInitParameter(Ljava/lang/String;)Ljava/lang/String;:?
-javax/servlet/ServletContext.getInitParameterNames()Ljava/util/Enumeration;:?
javax/servlet/ServletContext.getNamedDispatcher(Ljava/lang/String;)Ljavax/servlet/RequestDispatcher;:0
javax/servlet/ServletContext.getRequestDispatcher(Ljava/lang/String;)Ljavax/servlet/RequestDispatcher;:0
javax/servlet/ServletContext.getRealPath(Ljava/lang/String;)Ljava/lang/String;:0
javax/servlet/ServletContext.getResource(Ljava/lang/String;)Ljava/net/URL;:0
javax/servlet/ServletContext.getResourceAsStream(Ljava/lang/String;)Ljava/io/InputStream;:0
javax/servlet/ServletContext.getResourcePaths(Ljava/lang/String;)Ljava/util/Set;:0

-- The following methods receive arguments but will not alter the objects received
-- (It avoids tainting the parameters that are not immutable)
javax/servlet/jsp/JspWriter.write([C)V:UNKNOWN
javax/servlet/jsp/JspWriter.write([CII)V:UNKNOWN
javax/servlet/jsp/JspWriter.print([C)V:UNKNOWN
javax/servlet/jsp/JspWriter.print(Ljava/lang/Object;)V:UNKNOWN
javax/servlet/jsp/JspWriter.println([C)V:UNKNOWN

org/apache/commons/fileupload/FileItem.getName()Ljava/lang/String;:TAINTED
javax/ws/rs/core/MultivaluedMap.getFirst(Ljava/lang/Object;)Ljava/lang/Object;:TAINTED
-- Following classes are immutable
Ljava/lang/String;:#IMMUTABLE
Ljava/io/File;:#IMMUTABLE
Ljava/util/Locale;:#IMMUTABLE
Ljava/net/Inet4Address;:#IMMUTABLE
Ljava/net/Inet6Address;:#IMMUTABLE
Ljava/net/InetSocketAddress;:#IMMUTABLE
Ljava/net/URI;:#IMMUTABLE
Ljava/net/URL;:#IMMUTABLE

-- Following classes are SAFE (and also immutable in sense of being tainted)
Ljava/lang/Boolean;:SAFE#IMMUTABLE
Ljava/lang/Character;:SAFE#IMMUTABLE
Ljava/lang/Double;:SAFE#IMMUTABLE
Ljava/lang/Float;:SAFE#IMMUTABLE
Ljava/lang/Integer;:SAFE#IMMUTABLE
Ljava/lang/Long;:SAFE#IMMUTABLE
Ljava/lang/Byte;:SAFE#IMMUTABLE
Ljava/lang/Short;:SAFE#IMMUTABLE
Ljava/math/BigInteger;:SAFE#IMMUTABLE
Ljava/math/BigDecimal;:SAFE#IMMUTABLE
Ljava/util/Date;:SAFE#IMMUTABLE
Ljava/sql/Time;:SAFE#IMMUTABLE
Ljava/time/Duration;:SAFE#IMMUTABLE
Ljava/time/Instant;:SAFE#IMMUTABLE
Ljava/time/LocalDate;:SAFE#IMMUTABLE
Ljava/time/LocalDateTime;:SAFE#IMMUTABLE
Ljava/time/LocalTime;:SAFE#IMMUTABLE
Ljava/time/MonthDay;:SAFE#IMMUTABLE
Ljava/time/OffsetDateTime;:SAFE#IMMUTABLE
Ljava/time/OffsetTime;:SAFE#IMMUTABLE
Ljava/time/Period;:SAFE#IMMUTABLE
Ljava/time/Year;:SAFE#IMMUTABLE
Ljava/time/YearMonth;:SAFE#IMMUTABLE
Ljava/time/ZonedDateTime;:SAFE#IMMUTABLE
Ljava/time/ZonedId;:SAFE#IMMUTABLE
Ljava/time/ZoneOffset;:SAFE#IMMUTABLE
Ljava/text/Format;:SAFE#IMMUTABLE
Ljava/text/DateFormat;:SAFE#IMMUTABLE
Ljava/text/SimpleDateFormat;:SAFE#IMMUTABLE
Ljava/text/MessageFormat;:SAFE#IMMUTABLE
Ljava/text/NumberFormat;:SAFE#IMMUTABLE
Ljava/text/ChoiceFormat;:SAFE#IMMUTABLE
Ljava/text/DecimalFormat;:SAFE#IMMUTABLE

java/text/MessageFormat.format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;:0,1

java/lang/Object.clone()Ljava/lang/Object;:0
java/lang/Object.equals(Ljava/lang/Object;)Z:UNKNOWN

- Not true, but allows analysis of methods calling toString on Object instances
java/lang/Object.toString()Ljava/lang/String;:0

java/lang/Enum.name()Ljava/lang/String;:SAFE
java/lang/Enum.toString()Ljava/lang/String;:SAFE

- Objects from Java 8 function package are UNKNOWN by default, some could be made SAFE or TAINTED in the future
java/lang/Iterable.forEach(Ljava/util/function/Consumer;)V:0,1#1
java/lang/Iterable.iterator()Ljava/util/Iterator;:0

- usually safe for web applications
java/lang/System.clearProperty(Ljava/lang/String;)Ljava/lang/String;:SAFE
java/lang/System.getenv()Ljava/util/Map;:SAFE
java/lang/System.getenv(Ljava/lang/String;)Ljava/lang/String;:SAFE
java/lang/System.getProperty(Ljava/lang/String;)Ljava/lang/String;:SAFE
java/lang/System.getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:SAFE
java/lang/System.lineSeparator()Ljava/lang/String;:SAFE
java/lang/System.setProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:SAFE


java/lang/Appendable.append(Ljava/lang/CharSequence;)Ljava/lang/Appendable;:0,1#1
java/lang/Appendable.append(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;:2,3#3


java/lang/StringBuilder.<init>()V:SAFE
java/lang/StringBuilder.<init>(Ljava/lang/CharSequence;)V:0#1,2
java/lang/StringBuilder.<init>(I)V:SAFE
java/lang/StringBuilder.<init>(Ljava/lang/String;)V:0#1,2

java/lang/StringBuilder.append(Ljava/lang/String;)Ljava/lang/StringBuilder;:0,1#1
java/lang/StringBuilder.append(Ljava/lang/StringBuffer;)Ljava/lang/StringBuilder;:0,1#1
java/lang/StringBuilder.append(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;:0,1#1
java/lang/StringBuilder.append(Ljava/lang/CharSequence;II)Ljava/lang/StringBuilder;:2,3#3
java/lang/StringBuilder.append(Z)Ljava/lang/StringBuilder;:1
java/lang/StringBuilder.append(C)Ljava/lang/StringBuilder;:1
java/lang/StringBuilder.append(D)Ljava/lang/StringBuilder;:2
java/lang/StringBuilder.append(F)Ljava/lang/StringBuilder;:1
java/lang/StringBuilder.append(I)Ljava/lang/StringBuilder;:1
java/lang/StringBuilder.append(J)Ljava/lang/StringBuilder;:2
java/lang/StringBuilder.append(Ljava/lang/Object;)Ljava/lang/StringBuilder;:0,1#1

java/lang/StringBuilder.insert(ILjava/lang/String;)Ljava/lang/StringBuilder;:0,2#2
java/lang/StringBuilder.insert(ILjava/lang/Object;)Ljava/lang/StringBuilder;:0,2#2
java/lang/StringBuilder.insert(ILjava/lang/CharSequence;)Ljava/lang/StringBuilder;:0,2#2
java/lang/StringBuilder.insert(ILjava/lang/CharSequence;II)Ljava/lang/StringBuilder;:2,4#4
java/lang/StringBuilder.insert(IZ)Ljava/lang/StringBuilder;:2
java/lang/StringBuilder.insert(IC)Ljava/lang/StringBuilder;:2
java/lang/StringBuilder.insert(ID)Ljava/lang/StringBuilder;:3
java/lang/StringBuilder.insert(IF)Ljava/lang/StringBuilder;:2
java/lang/StringBuilder.insert(II)Ljava/lang/StringBuilder;:2
java/lang/StringBuilder.insert(IJ)Ljava/lang/StringBuilder;:3

java/lang/StringBuilder.delete(II)Ljava/lang/StringBuilder;:2#2
java/lang/StringBuilder.deleteCharAt(I)Ljava/lang/StringBuilder;:1#1
java/lang/StringBuilder.ensureCapacity(I)Ljava/lang/StringBuilder;:1#1
java/lang/StringBuilder.replace(IILjava/lang/String;)Ljava/lang/StringBuilder;:0,3#3
java/lang/StringBuilder.reverse()Ljava/lang/StringBuilder;:0#0
java/lang/StringBuilder.substring(I)Ljava/lang/String;:1
java/lang/StringBuilder.substring(II)Ljava/lang/String;:2
java/lang/StringBuilder.subSequence(II)Ljava/lang/CharSequence;:2
java/lang/StringBuilder.trimToSize()V:0#0


java/lang/StringBuffer.<init>()V:SAFE
java/lang/StringBuffer.<init>(Ljava/lang/CharSequence;)V:0#1,2
java/lang/StringBuffer.<init>(I)V:SAFE
java/lang/StringBuffer.<init>(Ljava/lang/String;)V:0#1,2

java/lang/StringBuffer.append(Ljava/lang/String;)Ljava/lang/StringBuffer;:0,1#1
java/lang/StringBuffer.append(Ljava/lang/StringBuffer;)Ljava/lang/StringBuffer;:0,1#1
java/lang/StringBuffer.append(Ljava/lang/CharSequence;)Ljava/lang/StringBuffer;:0,1#1
java/lang/StringBuffer.append(Ljava/lang/CharSequence;II)Ljava/lang/StringBuffer;:2,3#3
java/lang/StringBuffer.append(Z)Ljava/lang/StringBuffer;:1
java/lang/StringBuffer.append(C)Ljava/lang/StringBuffer;:1
java/lang/StringBuffer.append(D)Ljava/lang/StringBuffer;:2
java/lang/StringBuffer.append(F)Ljava/lang/StringBuffer;:1
java/lang/StringBuffer.append(I)Ljava/lang/StringBuffer;:1
java/lang/StringBuffer.append(J)Ljava/lang/StringBuffer;:2
java/lang/StringBuffer.append(Ljava/lang/Object;)Ljava/lang/StringBuffer;:0,1#1

java/lang/StringBuffer.insert(ILjava/lang/String;)Ljava/lang/StringBuffer;:0,2#2
java/lang/StringBuffer.insert(ILjava/lang/Object;)Ljava/lang/StringBuffer;:0,2#2
java/lang/StringBuffer.insert(ILjava/lang/CharSequence;)Ljava/lang/StringBuffer;:0,2#2
java/lang/StringBuffer.insert(ILjava/lang/CharSequence;II)Ljava/lang/StringBuffer;:2,4#4
java/lang/StringBuffer.insert(IZ)Ljava/lang/StringBuffer;:2
java/lang/StringBuffer.insert(IC)Ljava/lang/StringBuffer;:2
java/lang/StringBuffer.insert(ID)Ljava/lang/StringBuffer;:3
java/lang/StringBuffer.insert(IF)Ljava/lang/StringBuffer;:2
java/lang/StringBuffer.insert(II)Ljava/lang/StringBuffer;:2
java/lang/StringBuffer.insert(IJ)Ljava/lang/StringBuffer;:3

java/lang/StringBuffer.delete(II)Ljava/lang/StringBuffer;:2#2
java/lang/StringBuffer.deleteCharAt(I)Ljava/lang/StringBuffer;:1#1
java/lang/StringBuffer.ensureCapacity(I)Ljava/lang/StringBuffer;:1#1
java/lang/StringBuffer.replace(IILjava/lang/String;)Ljava/lang/StringBuffer;:0,3#3
java/lang/StringBuffer.reverse()Ljava/lang/StringBuffer;:0#0
java/lang/StringBuffer.substring(I)Ljava/lang/String;:1
java/lang/StringBuffer.substring(II)Ljava/lang/String;:2
java/lang/StringBuffer.subSequence(II)Ljava/lang/CharSequence;:2
java/lang/StringBuffer.trimToSize()V:0#0

java/lang/Appendable.append(C)Ljava/lang/Appendable;:0,1#1

java/lang/String.<init>()V:SAFE
java/lang/String.<init>(Ljava/lang/String;)V:0#1,2
java/lang/String.<init>(Ljava/lang/StringBuilder;)V:0#1,2
java/lang/String.<init>(Ljava/lang/StringBuffer;)V:0#1,2

java/lang/String.concat(Ljava/lang/String;)Ljava/lang/String;:0,1
java/lang/String.intern()Ljava/lang/String;:0
java/lang/String.format(Ljava/util/Locale;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;:0
java/lang/String.format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;:0
java/lang/String.join(Ljava/lang/CharSequence;[Ljava/lang/CharSequence;)Ljava/lang/String;:0,1
java/lang/String.join(Ljava/lang/CharSequence;Ljava/lang/Iterable;)Ljava/lang/String;:0,1
java/lang/String.replace(CC)Ljava/lang/String;:2
java/lang/String.replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;:0,2
java/lang/String.replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,2
java/lang/String.replaceFirst(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,2
java/lang/String.split(Ljava/lang/String;)[Ljava/lang/String;:1
java/lang/String.split(Ljava/lang/String;I)[Ljava/lang/String;:2
java/lang/String.substring(I)Ljava/lang/String;:1
java/lang/String.substring(II)Ljava/lang/String;:2
java/lang/String.subSequence(II)Ljava/lang/CharSequence;:2
java/lang/String.toLowerCase()Ljava/lang/String;:0
java/lang/String.toLowerCase(Ljava/util/Locale;)Ljava/lang/String;:1
java/lang/String.toUpperCase()Ljava/lang/String;:0
java/lang/String.toUpperCase(Ljava/util/Locale;)Ljava/lang/String;:1
java/lang/String.trim()Ljava/lang/String;:0
java/lang/String.valueOf(Z)Ljava/lang/String;:SAFE
java/lang/String.valueOf(C)Ljava/lang/String;:SAFE
java/lang/String.valueOf(D)Ljava/lang/String;:SAFE
java/lang/String.valueOf(F)Ljava/lang/String;:SAFE
java/lang/String.valueOf(I)Ljava/lang/String;:SAFE
java/lang/String.valueOf(J)Ljava/lang/String;:SAFE
java/lang/String.valueOf(Ljava/lang/Object;)Ljava/lang/String;:0
java/lang/String.valueOf([C)Ljava/lang/String;:0

java/util/Arrays.toString([Ljava/lang/Object;)Ljava/lang/String;:0

java/lang/CharSequence.subSequence(II)Ljava/lang/CharSequence;:2


java/lang/Boolean.toString()Ljava/lang/String;:SAFE
java/lang/Boolean.toString(B)Ljava/lang/String;:SAFE
java/lang/Character.getName(I)Ljava/lang/String;:SAFE
java/lang/Character.toString()Ljava/lang/String;:SAFE
java/lang/Character.toString(C)Ljava/lang/String;:SAFE
java/lang/Double.toString()Ljava/lang/String;:SAFE
java/lang/Double.toString(D)Ljava/lang/String;:SAFE
java/lang/Float.toHexString(F)Ljava/lang/String;:SAFE
java/lang/Float.toString()Ljava/lang/String;:SAFE
java/lang/Float.toString(F)Ljava/lang/String;:SAFE
java/lang/Integer.toBinaryString(I)Ljava/lang/String;:SAFE
java/lang/Integer.toHexString(I)Ljava/lang/String;:SAFE
java/lang/Integer.toOctalString(I)Ljava/lang/String;:SAFE
java/lang/Integer.toString()Ljava/lang/String;:SAFE
java/lang/Integer.toString(I)Ljava/lang/String;:SAFE
java/lang/Integer.toString(II)Ljava/lang/String;:SAFE
java/lang/Long.toBinaryString(J)Ljava/lang/String;:SAFE
java/lang/Long.toHexString(J)Ljava/lang/String;:SAFE
java/lang/Long.toOctalString(J)Ljava/lang/String;:SAFE
java/lang/Long.toString()Ljava/lang/String;:SAFE
java/lang/Long.toString(J)Ljava/lang/String;:SAFE
java/lang/Long.toString(JI)Ljava/lang/String;:SAFE
java/lang/Byte.toString()Ljava/lang/String;:SAFE
java/lang/Byte.toString(B)Ljava/lang/String;:SAFE
java/lang/Short.toString()Ljava/lang/String;:SAFE
java/lang/Short.toString(S)Ljava/lang/String;:SAFE
java/math/BigDecimal.toEngineeringString()Ljava/lang/String;:SAFE
java/math/BigDecimal.toPlainString()Ljava/lang/String;:SAFE
java/math/BigDecimal.toString()Ljava/lang/String;:SAFE


java/lang/reflect/Type.getTypeName()Ljava/lang/String;:SAFE
java/lang/Class.getCanonicalName()Ljava/lang/String;:SAFE
java/lang/Class.getName()Ljava/lang/String;:SAFE
java/lang/Class.getResource(Ljava/lang/String;)Ljava/net/URL;:SAFE
java/lang/ClassLoader.getResource(Ljava/lang/String;)Ljava/net/URL;:SAFE
java/lang/ClassLoader.getResources(Ljava/lang/String;)Ljava/util/Enumeration;:SAFE
java/lang/ClassLoader.getSystemResource(Ljava/lang/String;)Ljava/net/URL;:SAFE
java/lang/ClassLoader.getSystemResources(Ljava/lang/String;)Ljava/util/Enumeration;:SAFE
java/lang/Class.getSimpleName()Ljava/lang/String;:SAFE
java/lang/Class.toGenericString()Ljava/lang/String;:SAFE
java/lang/Class.toString()Ljava/lang/String;:SAFE
java/lang/reflect/Member.getName()Ljava/lang/String;:SAFE
java/lang/reflect/Executable.toGenericString()Ljava/lang/String;:SAFE
java/lang/reflect/Method.toString()Ljava/lang/String;:SAFE
java/lang/reflect/Constructor.toString()Ljava/lang/String;:SAFE
java/lang/reflect/Field.toGenericString()Ljava/lang/String;:SAFE
java/lang/reflect/Field.toString()Ljava/lang/String;:SAFE
java/lang/Package.getName()Ljava/lang/String;:SAFE
java/lang/Package.toString()Ljava/lang/String;:SAFE

java/lang/Class.getResourceAsStream(Ljava/lang/String;)Ljava/io/InputStream;:0#1
javax/xml/transform/stream/StreamSource.<init>(Ljava/io/InputStream;)V:0#2

java/io/FileInputStream.<init>(Ljava/lang/String;)V:0#1,2
java/io/ByteArrayInputStream.<init>([B)V:0#1,2
java/lang/String.getBytes()[B:0#0

--ResourceBundle is typically locale strings that are loaded from static files
java/util/ResourceBundle.getString(Ljava/lang/String;)Ljava/lang/String;:SAFE
java/util/ResourceBundle.getStringArray(Ljava/lang/String;)[Ljava/lang/String;:SAFE
java/util/ResourceBundle.getObject(Ljava/lang/String;)Ljava/lang/Object;:SAFE

--Kotlin code that adds methods to String class in Java
kotlin/text/StringsKt.replace$default(Ljava/lang/String;CCZILjava/lang/Object;)Ljava/lang/String;:5
kotlin/text/StringsKt.replace$default(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ZILjava/lang/Object;)Ljava/lang/String;:5
kotlin/text/Regex.replace(Ljava/lang/CharSequence;Ljava/lang/String;)Ljava/lang/String;:1
kotlin/text/Regex.<init>(Ljava/lang/String;)V:SAFEjava/net/URI.<init>(Ljava/lang/String;)V:0#1,2
java/net/URI.<init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,1,2#3,4
java/net/URI.<init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,1,2,4,5,6#7,8
java/net/URI.<init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,1,2,3#4,5
java/net/URI.<init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,1,2,3,4#5,6
java/net/URI.create(Ljava/lang/String;)Ljava/net/URI;:0
java/net/URI.getAuthority()Ljava/lang/String;:0
java/net/URI.getFragment()Ljava/lang/String;:0
java/net/URI.getHost()Ljava/lang/String;:0
java/net/URI.getPath()Ljava/lang/String;:0
java/net/URI.getQuery()Ljava/lang/String;:0
java/net/URI.getRawAuthority()Ljava/lang/String;:0
java/net/URI.getRawFragment()Ljava/lang/String;:0
java/net/URI.getRawPath()Ljava/lang/String;:0
java/net/URI.getRawQuery()Ljava/lang/String;:0
java/net/URI.getRawSchemeSpecificPart()Ljava/lang/String;:0
java/net/URI.getRawUserInfo()Ljava/lang/String;:0
java/net/URI.getScheme()Ljava/lang/String;:0
java/net/URI.getSchemeSpecificPart()Ljava/lang/String;:0
java/net/URI.getUserInfo()Ljava/lang/String;:0
java/net/URI.normalize()Ljava/net/URI;:0
java/net/URI.parseServerAuthority()Ljava/net/URI;:0
java/net/URI.relativize(Ljava/net/URI;)Ljava/net/URI;:0,1
java/net/URI.resolve(Ljava/lang/String;)Ljava/net/URI;:0,1
java/net/URI.resolve(Ljava/net/URI;)Ljava/net/URI;:0,1
java/net/URI.toASCIIString()Ljava/lang/String;:0
java/net/URI.toString()Ljava/lang/String;:0
java/net/URI.toURL()Ljava/net/URL;:0


java/net/URL.<init>(Ljava/lang/String;)V:0#1,2
java/net/URL.<init>(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;)V:0,2,3#4,5
java/net/URL.<init>(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/net/URLStreamHandler;)V:1,3,4#5,6
java/net/URL.<init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V:0,1,2#3,4
java/net/URL.<init>(Ljava/net/URL;Ljava/lang/String;)V:0,1#2,3
java/net/URL.<init>(Ljava/net/URL;Ljava/lang/String;Ljava/net/URLStreamHandler;)V:1,2#3,4
java/net/URL.getAuthority()Ljava/lang/String;:0
java/net/URL.getContent()Ljava/lang/Object;:TAINTED
java/net/URL.getContent([Ljava/lang/Class;)Ljava/lang/Object;:TAINTED
java/net/URL.getFile()Ljava/lang/String;:0
java/net/URL.getHost()Ljava/lang/String;:0
java/net/URL.getPath()Ljava/lang/String;:0
java/net/URL.getProtocol()Ljava/lang/String;:0
java/net/URL.getQuery()Ljava/lang/String;:0
java/net/URL.getRef()Ljava/lang/String;:0
java/net/URL.getUserInfo()Ljava/lang/String;:0
java/net/URL.sameFile(Ljava/net/URL;)Z:UNKNOWN
java/net/URL.toExternalForm()Ljava/lang/String;:0
java/net/URL.toString()Ljava/lang/String;:0
java/net/URL.toURI()Ljava/net/URI;:0

java/io/File.createTempFile(Ljava/lang/String;Ljava/lang/String;)Ljava/io/File;:0,1
java/io/File.createTempFile(Ljava/lang/String;Ljava/lang/String;Ljava/io/File;)Ljava/io/File;:0,1,2
java/io/File.getCanonicalPath()Ljava/lang/String;:0

java/io/File.separator:SAFE
java/nio/file/FileSystem.getSeparator()Ljava/lang/String;:SAFE--Jetty API are rarely used by Web Application
--They are used by infrastructure application or framework

org/eclipse/jetty/http/HttpFields.getFieldNamesCollection()Ljava/util/Set;:TAINTED
org/eclipse/jetty/http/HttpFields.getFieldNames()Ljava/util/Enumeration;:TAINTED
org/eclipse/jetty/http/HttpFields.getStringField(Lorg/eclipse/jetty/http/HttpHeader;)Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpFields.get(Lorg/eclipse/jetty/http/HttpHeader;)Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpFields.getStringField(Ljava/lang/String;)Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpFields.get(Ljava/lang/String;)Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpFields.getCSV(Lorg/eclipse/jetty/http/HttpHeader;Z)Ljava/util/List;:TAINTED
org/eclipse/jetty/http/HttpFields.getCSV(Ljava/lang/String;Z)Ljava/util/List;:TAINTED
org/eclipse/jetty/http/HttpFields.getQualityCSV(Lorg/eclipse/jetty/http/HttpHeader;)Ljava/util/List;:TAINTED
org/eclipse/jetty/http/HttpFields.getQualityCSV(Ljava/lang/String;)Ljava/util/List;:TAINTED
org/eclipse/jetty/http/HttpFields.getValues(Ljava/lang/String;)Ljava/util/Enumeration;:TAINTED
org/eclipse/jetty/http/HttpFields.getValues(Ljava/lang/String;Ljava/lang/String;)Ljava/util/Enumeration;:TAINTED
org/eclipse/jetty/http/HttpFields.valueParameters(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String;:TAINTED

org/eclipse/jetty/http/HttpField.getName()Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpField.getValue()Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpField.getValues()[Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpField.toString()Ljava/lang/String;:TAINTED

org/eclipse/jetty/http/HttpCookie.getName()Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpCookie.getValue()Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpCookie.asString()Ljava/lang/String;:TAINTED

--org/eclipse/jetty/http/HttpHeader.getBytes()[B:TAINTED
--org/eclipse/jetty/http/HttpHeader.getBytesColonSpace()[B:TAINTED
--org/eclipse/jetty/http/HttpHeader.asString()Ljava/lang/String;:TAINTED
--org/eclipse/jetty/http/HttpHeader.toString()Ljava/lang/String;:TAINTED

--org/eclipse/jetty/http/HttpHeaderValue.toBuffer()Ljava/nio/ByteBuffer;:TAINTED
--org/eclipse/jetty/http/HttpHeaderValue.is(Ljava/lang/String;)Z:TAINTED
--org/eclipse/jetty/http/HttpHeaderValue.asString()Ljava/lang/String;:TAINTED
--org/eclipse/jetty/http/HttpHeaderValue.toString()Ljava/lang/String;:TAINTED

org/eclipse/jetty/http/HttpURI.getParam()Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpURI.getQuery()Ljava/lang/String;:TAINTED
org/eclipse/jetty/http/HttpURI.getHost()Ljava/lang/String;:TAINTED
-- Logging methods receive arguments but will not alter the objects received
-- (It avoids tainting the parameters that are not immutable)

java/util/logging/Logger.entering(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.entering(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.exiting(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.log(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.log(Ljava/util/logging/Level;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.logp(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
java/util/logging/Logger.logrb(Ljava/util/logging/Level;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN

org/apache/commons/logging/Log.debug(Ljava/lang/Object;)V:UNKNOWN
org/apache/commons/logging/Log.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/commons/logging/Log.error(Ljava/lang/Object;)V:UNKNOWN
org/apache/commons/logging/Log.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/commons/logging/Log.fatal(Ljava/lang/Object;)V:UNKNOWN
org/apache/commons/logging/Log.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/commons/logging/Log.info(Ljava/lang/Object;)V:UNKNOWN
org/apache/commons/logging/Log.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/commons/logging/Log.trace(Ljava/lang/Object;)V:UNKNOWN
org/apache/commons/logging/Log.trace(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/commons/logging/Log.warn(Ljava/lang/Object;)V:UNKNOWN
org/apache/commons/logging/Log.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN

org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.debug(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.debug(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.debug(Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.debug(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.error(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.error(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.error(Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.error(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.info(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.info(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.info(Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.info(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.trace(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.trace(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.trace(Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.trace(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.warn(Lorg/slf4j/Marker;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.warn(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.warn(Ljava/lang/String;Ljava/lang/Object;)V:UNKNOWN
org/slf4j/Logger.warn(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V:UNKNOWN

org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.debug(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.debug(Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.debug(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.entry([Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.error(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.error(Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.error(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.fatal(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.fatal(Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.fatal(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.info(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.info(Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.info(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/slf4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/slf4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.log(Lorg/apache/logging/log4j/Level;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.printf(Lorg/apache/logging/log4j/Level;Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.printf(Lorg/apache/logging/log4j/Level;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.trace(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.trace(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.trace(Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.trace(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.warn(Lorg/apache/logging/log4j/Marker;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/logging/log4j/Logger.warn(Ljava/lang/Object;)V:UNKNOWN
org/apache/logging/log4j/Logger.warn(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN

org/apache/log4j/Category.debug(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Category.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.error(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Category.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.fatal(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Category.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.info(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Category.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Category.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.log(Ljava/lang/String;Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Category.warn(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Category.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.debug(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.debug(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.error(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.error(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.fatal(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.fatal(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.info(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.info(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;[Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.l7dlog(Lorg/apache/log4j/Priority;Ljava/lang/String;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.log(Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.log(Ljava/lang/String;Lorg/apache/log4j/Priority;Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.warn(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.warn(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN
org/apache/log4j/Logger.trace(Ljava/lang/Object;)V:UNKNOWN
org/apache/log4j/Logger.trace(Ljava/lang/Object;Ljava/lang/Throwable;)V:UNKNOWN

org/pmw/tinylog/Logger.debug(Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.debug(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.debug(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.error(Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.error(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.error(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.info(Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.info(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.info(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.trace(Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.trace(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.trace(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.warn(Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.warn(Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN
org/pmw/tinylog/Logger.warn(Ljava/lang/Throwable;Ljava/lang/String;[Ljava/lang/Object;)V:UNKNOWN

org/jboss/seam/log/Log.debug(Ljava/lang/Object;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.debug(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.error(Ljava/lang/Object;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.error(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.fatal(Ljava/lang/Object;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.fatal(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.info(Ljava/lang/Object;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.info(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.trace(Ljava/lang/Object;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.trace(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.warn(Ljava/lang/Object;[Ljava/lang/Object;)V:UNKNOWN
org/jboss/seam/log/Log.warn(Ljava/lang/Object;Ljava/lang/Throwable;[Ljava/lang/Object;)V:UNKNOWN
java/io/BufferedReader.readLine()Ljava/lang/String;:TAINTED

java/io/Console.readLine()Ljava/lang/String;:TAINTED
java/io/Console.readLine(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;:TAINTED

java/io/DataInputStream.readLine()Ljava/lang/String;:TAINTED
java/io/DataInputStream.readUTF()Ljava/lang/String;:TAINTED
java/io/DataInputStream.readUTF(Ljava/io/DataInput;)Ljava/lang/String;:TAINTED

java/io/LineNumberReader.readLine()Ljava/lang/String;:TAINTED

java/util/Scanner.<init>(Ljava/io/File;)V:TAINTED#1,2
java/util/Scanner.<init>(Ljava/io/File;Ljava/lang/String;)V:TAINTED#2,3
java/util/Scanner.<init>(Ljava/io/InputStream;)V:TAINTED#1,2
java/util/Scanner.<init>(Ljava/io/InputStream;Ljava/lang/String;)V:TAINTED#2,3
java/util/Scanner.<init>(Ljava/nio/file/Path;)V:TAINTED#1,2
java/util/Scanner.<init>(Ljava/nio/file/Path;Ljava/lang/String;)V:TAINTED#2,3
java/util/Scanner.<init>(Ljava/lang/Readable;)V:TAINTED#1,2
java/util/Scanner.<init>(Ljava/nio/channels/ReadableByteChannel;)V:TAINTED#1,2
java/util/Scanner.<init>(Ljava/nio/channels/ReadableByteChannel;Ljava/lang/String;)V:TAINTED#2,3
java/util/Scanner.<init>(Ljava/lang/String;)V:0#1,2
java/util/Scanner.next()Ljava/lang/String;:0
java/util/Scanner.next(Ljava/util/regex/Pattern;)Ljava/lang/String;:1
java/util/Scanner.next(Ljava/lang/String;)Ljava/lang/String;:1
java/util/Scanner.nextLine()Ljava/lang/String;:0


java/sql/ResultSet.getNString(I)Ljava/lang/String;:TAINTED
java/sql/ResultSet.getNString(Ljava/lang/String;)Ljava/lang/String;:TAINTED
java/sql/ResultSet.getString(I)Ljava/lang/String;:TAINTED
java/sql/ResultSet.getString(Ljava/lang/String;)Ljava/lang/String;:TAINTED


java/util/StringTokenizer.<init>(Ljava/lang/String;)V:0#1,2
java/util/StringTokenizer.<init>(Ljava/lang/String;Ljava/lang/String;)V:1#2,3
java/util/StringTokenizer.<init>(Ljava/lang/String;Ljava/lang/String;B)V:2#3,4
java/util/StringTokenizer.nextToken()Ljava/lang/String;:0
java/util/StringTokenizer.nextToken(Ljava/lang/String;)Ljava/lang/String;:1


java/awt/TextComponent.getSelectedText()Ljava/lang/String;:TAINTED
java/awt/TextComponent.getText()Ljava/lang/String;:TAINTED

javax/swing/text/JTextComponent.getSelectedText()Ljava/lang/String;:TAINTED
javax/swing/text/JTextComponent.getText()Ljava/lang/String;:TAINTED
javax/swing/text/JTextComponent.getText(II)Ljava/lang/String;:TAINTED


flexjson/JSONSerializer.deepSerialize(Ljava/lang/Object;)Ljava/lang/String;:0
flexjson/JSONSerializer.deepSerialize(Ljava/lang/Object;Lflexjson/OutputHandler;)Ljava/lang/String;:1
flexjson/JSONSerializer.deepSerialize(Ljava/lang/Object;Ljava/lang/StringBuffer;)Ljava/lang/String;:1
flexjson/JSONSerializer.deepSerialize(Ljava/lang/Object;Ljava/lang/StringBuilder;)Ljava/lang/String;:1
flexjson/JSONSerializer.serialize(Ljava/lang/Object;)Ljava/lang/String;:0
flexjson/JSONSerializer.serialize(Ljava/lang/Object;Lflexjson/OutputHandler;)Ljava/lang/String;:1
flexjson/JSONSerializer.serialize(Ljava/lang/Object;Lflexjson/SerializationType;Lflexjson/OutputHandler;)Ljava/lang/String;:2
flexjson/JSONSerializer.serialize(Ljava/lang/Object;Ljava/lang/StringBuffer;)Ljava/lang/String;:1
flexjson/JSONSerializer.serialize(Ljava/lang/Object;Ljava/lang/StringBuilder;)Ljava/lang/String;:1


-- The following methods receive arguments but will not alter the objects received
-- (It avoids tainting the parameters that are not immutable)

javax/jdo/PersistenceManager.newQuery(Ljava/lang/Object;)Ljavax/jdo/Query;:UNKNOWN
javax/jdo/PersistenceManager.newQuery(Ljava/lang/String;Ljava/lang/Object;)Ljavax/jdo/Query;:UNKNOWN

javax/portlet/PortletRequest.getPortletMode()Ljavax/portlet/PortletMode;:TAINTED
javax/portlet/PortletRequest.getWindowState()Ljavax/portlet/WindowState;:TAINTED
javax/portlet/PortletRequest.getPreferences()Ljavax/portlet/PortletPreferences;:SAFE
javax/portlet/PortletRequest.getPortletSession()Ljavax/portlet/PortletSession;:SAFE
javax/portlet/PortletRequest.getPortletSession(Z)Ljavax/portlet/PortletSession;:SAFE
javax/portlet/PortletRequest.getPropertyNames()Ljava/util/Enumeration;:SAFE
javax/portlet/PortletRequest.getPortalContext()Ljavax/portlet/PortalContext;:SAFE
javax/portlet/PortletRequest.getAuthType()Ljava/lang/String;:SAFE
javax/portlet/PortletRequest.getContextPath()Ljava/lang/String;:SAFE
javax/portlet/PortletRequest.getRemoteUser()Ljava/lang/String;:TAINTED
javax/portlet/PortletRequest.getUserPrincipal()Ljava/security/Principal;:TAINTED
javax/portlet/PortletRequest.getAttributeNames()Ljava/util/Enumeration;:SAFE
javax/portlet/PortletRequest.getParameter(Ljava/lang/String;)Ljava/lang/String;:TAINTED
javax/portlet/PortletRequest.getParameterMap()Ljava/util/Map;:TAINTED
javax/portlet/PortletRequest.getParameterNames()Ljava/util/Enumeration;:TAINTED
javax/portlet/PortletRequest.getParameterValues(Ljava/lang/String;)[Ljava/lang/String;:TAINTED
javax/portlet/PortletRequest.getRequestedSessionId()Ljava/lang/String;:TAINTED
javax/portlet/PortletRequest.getResponseContentType()Ljava/util/Enumeration;:TAINTED
javax/portlet/PortletRequest.getResponseContentTypes()Ljava/util/Enumeration;:TAINTED
javax/portlet/PortletRequest.getLocale()Ljava/util/Locale;:TAINTED
javax/portlet/PortletRequest.getLocales()Ljava/util/Enumeration;:SAFE
javax/portlet/PortletRequest.getScheme()Ljava/lang/String;:SAFE
javax/portlet/PortletRequest.getServerName()Ljava/lang/String;:TAINTED
javax/portlet/PortletRequest.getWindowID()Ljava/lang/String;:TAINTED
javax/portlet/PortletRequest.getCookies()[Ljavax/portlet/http/Cookie;:TAINTED
javax/portlet/PortletRequest.getPrivateParameterMap()Ljava/util/Map;:TAINTED
javax/portlet/PortletRequest.getPublicParameterMap()Ljava/util/Map;:TAINTED

javax/portlet/ActionRequest.getReader()Ljava/io/BufferedReader;:TAINTED
javax/portlet/ActionRequest.getCharacterEncoding()Ljava/lang/String;:TAINTED
javax/portlet/ActionRequest.getContentType()Ljava/lang/String;:TAINTED

javax/portlet/ClientDataRequest.getPortletInputStream()Ljava/io/InputStream;:TAINTED
javax/portlet/ClientDataRequest.getReader()Ljava/io/BufferedReader;:TAINTED
javax/portlet/ClientDataRequest.getCharacterEncoding()Ljava/lang/String;:SAFE
javax/portlet/ClientDataRequest.getContentType()Ljava/lang/String;:TAINTED
javax/portlet/ClientDataRequest.getMethod()Ljava/lang/String;:SAFE

javax/portlet/RenderRequest.getETag()Ljava/lang/String;:TAINTED

javax/portlet/ResourceRequest.getETag()Ljava/lang/String;:TAINTED
javax/portlet/ResourceRequest.getResourceID()Ljava/lang/String;:TAINTED
javax/portlet/ResourceRequest.getPrivateRenderParameterMap()Ljava/util/Map;:TAINTED

javax/portlet/PortletResponse.encodeURL(Ljava/lang/String;)Ljava/lang/String;:0|+URL_ENCODED
javax/portlet/PortletResponse.getNamespace()Ljava/lang/String;:SAFE

javax/portlet/MimeResponse.createRenderURL()Ljavax/portlet/PortletURL;:SAFE
javax/portlet/MimeResponse.createActionURL()Ljavax/portlet/PortletURL;:SAFE
javax/portlet/MimeResponse.createResourceURL()Ljavax/portlet/PortletURL;:SAFE

javax/portlet/RenderResponse.createRenderURL()Ljavax/portlet/PortletURL;:SAFE
javax/portlet/RenderResponse.createActionURL()Ljavax/portlet/PortletURL;:SAFE
javax/portlet/RenderResponse.getNamespace()Ljava/lang/String;:SAFE

javax/portlet/ResourceResponse.createRenderURL()Ljavax/portlet/PortletURL;:SAFE
javax/portlet/ResourceResponse.createActionURL()Ljavax/portlet/PortletURL;:SAFE
javax/portlet/ResourceResponse.createResourceURL()Ljavax/portlet/PortletURL;:SAFE

javax/portlet/BaseURL.setParameter(Ljava/lang/String;Ljava/lang/String;)V:0,1#2
javax/portlet/BaseURL.setParameter(Ljava/lang/String;[Ljava/lang/String;)V:0,1#2
javax/portlet/BaseURL.setParameters(Ljava/util/Map;)V:0#1
javax/portlet/BaseURL.addProperty(Ljava/lang/String;Ljava/lang/String;)V:0,1#2
javax/portlet/BaseURL.setProperty(Ljava/lang/String;Ljava/lang/String;)V:0,1#2
javax/portlet/BaseURL.toString()Ljava/lang/String;:0|+CR_ENCODED,+LF_ENCODED,+QUOTE_ENCODED,+LT_ENCODED,+URL_ENCODED
- Scala collections and and Scala-lang

scala/Predef$.wrapRefArray([Ljava/lang/Object;)Lscala/collection/mutable/WrappedArray;:0

scala/collection/Seq$.apply(Lscala/collection/Seq;)Lscala/collection/GenTraversable;:0#0
scala/collection/immutable/Vector$.apply(Lscala/collection/Seq;)Lscala/collection/GenTraversable;:0#0

scala/StringContext.<init>(Lscala/collection/Seq;)V:0#1,2
scala/StringContext.s(Lscala/collection/Seq;)Ljava/lang/String;:0,1

scala/Tuple2.<init>(Ljava/lang/Object;Ljava/lang/Object;)V:0,1#3

scala/Option.get()Ljava/lang/Object;:0

scala/collection/mutable/StringBuilder.<init>()V:SAFE
scala/collection/mutable/StringBuilder.<init>(I)V:SAFE
scala/collection/mutable/StringBuilder.<init>(Ljava/lang/String;)V:0#1,2

scala/collection/mutable/StringBuilder.append(Ljava/lang/String;)Lscala/collection/mutable/StringBuilder;:0,1#1
scala/collection/mutable/StringBuilder.append(Z)Lscala/collection/mutable/StringBuilder;:1
scala/collection/mutable/StringBuilder.append(C)Lscala/collection/mutable/StringBuilder;:1
scala/collection/mutable/StringBuilder.append(D)Lscala/collection/mutable/StringBuilder;:2
scala/collection/mutable/StringBuilder.append(F)Lscala/collection/mutable/StringBuilder;:1
scala/collection/mutable/StringBuilder.append(I)Lscala/collection/mutable/StringBuilder;:1
scala/collection/mutable/StringBuilder.append(J)Lscala/collection/mutable/StringBuilder;:2
scala/collection/mutable/StringBuilder.append(Ljava/lang/Object;)Lscala/collection/mutable/StringBuilder;:0,1#1
scala/collection/mutable/StringBuilder.append(Lscala/collection/mutable/StringBuilder;)Lscala/collection/mutable/StringBuilder;:0,1#1

scala/collection/mutable/StringBuilder.appendAll(Ljava/lang/String;)Lscala/collection/mutable/StringBuilder;:0,1#1

scala/collection/mutable/StringBuilder.insert(ILjava/lang/String;)Lscala/collection/mutable/StringBuilder;:0,2#2
scala/collection/mutable/StringBuilder.insert(ILjava/lang/Object;)Lscala/collection/mutable/StringBuilder;:0,2#2
scala/collection/mutable/StringBuilder.insert(IZ)Ljava/lang/StringBuilder;:2
scala/collection/mutable/StringBuilder.insert(IC)Ljava/lang/StringBuilder;:2
scala/collection/mutable/StringBuilder.insert(ID)Ljava/lang/StringBuilder;:3
scala/collection/mutable/StringBuilder.insert(IF)Ljava/lang/StringBuilder;:2
scala/collection/mutable/StringBuilder.insert(II)Ljava/lang/StringBuilder;:2
scala/collection/mutable/StringBuilder.insert(IJ)Ljava/lang/StringBuilder;:3

scala/collection/mutable/StringBuilder.delete(II)Lscala/collection/mutable/StringBuilder;:2#2
scala/collection/mutable/StringBuilder.deleteCharAt(I)Lscala/collection/mutable/StringBuilder;:1#1
scala/collection/mutable/StringBuilder.ensureCapacity(I)V:1#1
scala/collection/mutable/StringBuilder.setCharAt(IC)V:0,1#1
scala/collection/mutable/StringBuilder.replace(IILjava/lang/String;)Lscala/collection/mutable/StringBuilder;:0,3#3
scala/collection/mutable/StringBuilder.replaceAllLiterally(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:0,2
scala/collection/mutable/StringBuilder.reverseContents()Lscala/collection/mutable/StringBuilder;:0#0
scala/collection/mutable/StringBuilder.substring(I)Ljava/lang/String;:1
scala/collection/mutable/StringBuilder.substring(II)Ljava/lang/String;:2
scala/collection/mutable/StringBuilder.subSequence(II)Ljava/lang/CharSequence;:2

scala/collection/mutable/StringBuilder.toString()Ljava/lang/String;:0

- Scala I/O
scala/reflect/io/Path$.string2path(Ljava/lang/String;)Lscala/reflect/io/Path;:0

- Scala Play framework MVC
play/api/mvc/Results$Status.apply(Ljava/lang/Object;Lplay/api/http/Writeable;)Lplay/api/mvc/Result;:1
play/api/mvc/Cookie.<init>(Ljava/lang/String;Ljava/lang/String;Lscala/Option;Ljava/lang/String;Lscala/Option;ZZ)V:5,6#7,8

- Anorm database framework
anorm/package$.SQL(Ljava/lang/String;)Lanorm/SqlQuery;:0#0
anorm/package$.sqlToSimple(Lanorm/SqlQuery;)Lanorm/SimpleSql;:0
anorm/package$.SqlStringInterpolation(Lscala/StringContext;)Lscala/StringContext;:0
anorm/package$SqlStringInterpolation$.SQL$extension(Lscala/StringContext;Lscala/collection/Seq;)Lanorm/SimpleSql;:1

- Scala WebService Library
play/api/libs/ws/WSClient.url(Ljava/lang/String;)Lplay/api/libs/ws/WSRequest;:0
play/api/libs/ws/WS$.url(Ljava/lang/String;Lplay/api/Application;)Lplay/api/libs/ws/WSRequest;:1

play/api/libs/ws/WSRequest.withAuth(Ljava/lang/String;Ljava/lang/String;Lplay/api/libs/ws/WSAuthScheme;)Lplay/api/libs/ws/WSRequest;:3
play/api/libs/ws/WSRequest.withBody(Lplay/api/libs/ws/WSBody;)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withFollowRedirects(Z)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withHeaders(Lscala/collection/Seq;)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withMethod(Ljava/lang/String;)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withQueryString(Lscala/collection/Seq;)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withRequestFilter(Lplay/api/libs/ws/WSRequestFilter;)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withRequestTimeout(Lscala/concurrent/duration/Duration;)Lplay/api/libs/ws/WSRequest;:1
play/api/libs/ws/WSRequest.withVirtualHost(Ljava/lang/String;)Lplay/api/libs/ws/WSRequest;:1
org/sonarqube/ws/client/Parameters.getValue(Ljava/lang/String;)Ljava/lang/String;:TAINTED
org/sonarqube/ws/client/Parameters.getValues(Ljava/lang/String;)Ljava/util/List;:TAINTED
org/sonarqube/ws/client/Parameters.getKeys()Ljava/util/Set;:TAINTED

org/sonarqube/ws/client/Headers.getValue(Ljava/lang/String;)Ljava/util/Optional;:TAINTED
org/sonarqube/ws/client/Headers.getNames()Ljava/util/Set;:TAINTED

org/sonarqube/ws/client/BaseRequest.getPath()Ljava/lang/String;:TAINTED
org/sonarqube/ws/client/BaseRequest.getMediaType()Ljava/lang/String;:TAINTED
org/sonarqube/ws/client/BaseRequest.getParams()Ljava/util/Map;:TAINTED

org/sonarqube/ws/client/WsRequest.getPath()Ljava/lang/String;:TAINTED
org/sonarqube/ws/client/WsRequest.getMediaType()Ljava/lang/String;:TAINTED
org/sonarqube/ws/client/WsRequest.getParams()Ljava/util/Map;:TAINTED
org/apache/struts2/dispatcher/Parameter.getValue()Ljava/lang/String;:TAINTED
org/apache/struts2/util/StrutsUtil.buildUrl(Ljava/lang/String;)Ljava/lang/String;:0|+URL_ENCODED,+XSS_SAFEorg/springframework/web/bind/annotation/PathVariable
org/springframework/web/bind/annotation/RequestParam
org/springframework/web/bind/annotation/RequestBody
org/springframework/web/bind/annotation/RequestHeader
org/springframework/web/bind/annotation/MatrixVariable
org/springframework/web/bind/annotation/RequestPart
org/springframework/ws/server/endpoint/annotation/RequestPayload
org/springframework/ws/server/endpoint/annotation/XPathParam
javax/ws/rs/PathParam
javax/ws/rs/HeaderParam
javax/ws/rs/MatrixParam
javax/ws/rs/CookieParam
javax/ws/rs/FormParam
javax/ws/rs/QueryParam- Sensitive data can be obtained if these get tainted

- Java Lang
java/lang/System.getenv(Ljava/lang/String;)Ljava/lang/String;:0|+SENSITIVE_DATA
java/lang/System.getProperty(Ljava/lang/String;)Ljava/lang/String;:0|+SENSITIVE_DATA
java/lang/System.getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:1|+SENSITIVE_DATA

- Scala Play
com/typesafe/config/Config.getString(Ljava/lang/String;)Ljava/lang/String;:0|+SENSITIVE_DATA
play/api/Configuration.getString(Ljava/lang/String;Lscala/Option;)Lscala/Option;:1|+SENSITIVE_DATA-- Rewrites safe variables for "findsecbugs.taint.taintedsystemvariables=true"
java/lang/System.clearProperty(Ljava/lang/String;)Ljava/lang/String;:TAINTED
java/lang/System.getenv()Ljava/util/Map;:TAINTED
java/lang/System.getenv(Ljava/lang/String;)Ljava/lang/String;:TAINTED
java/lang/System.getProperty(Ljava/lang/String;)Ljava/lang/String;:TAINTED
java/lang/System.getProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:TAINTED
java/lang/System.setProperty(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;:TAINTED
--Cover the API by tests

org/apache/wicket/protocol/http/request/WebClientInfo.getUserAgent()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/request/WebClientInfo.getUserAgentStringLc()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/request/WebClientInfo.getRemoteAddr(Lorg/apache/wicket/request/cycle/RequestCycle;)Ljava/lang/String;:TAINTED

org/apache/wicket/request/http/WebRequest.getHeaders(Ljava/lang/String;)Ljava/util/List;:TAINTED
org/apache/wicket/request/http/WebRequest.getHeader(Ljava/lang/String;)Ljava/lang/String;:TAINTED

org/apache/wicket/protocol/http/ClientProperties.getNavigatorAppCodeName()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getNavigatorAppName()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getNavigatorAppVersion()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getNavigatorLanguage()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getNavigatorPlatform()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getNavigatorUserAgent()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getRemoteAddress()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/ClientProperties.getHostname()Ljava/lang/String;:TAINTED

org/apache/wicket/request/IRequestParameters.getParameterNames()Ljava/util/Set;:TAINTED
org/apache/wicket/request/IRequestParameters.getParameterValue(Ljava/lang/String;)Lorg/apache/wicket/util/string/StringValue;:TAINTED
org/apache/wicket/request/IRequestParameters.getParameterValues(Ljava/lang/String;)Ljava/util/List;:TAINTED

org/apache/wicket/protocol/http/servlet/ServletPartFileItem.getName()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/servlet/ServletPartFileItem.getFileName(Ljavax/servlet/http/Part;)Ljava/lang/String;:TAINTED

org/apache/wicket/protocol/http/servlet/ServletPartFileItem.get()[B:TAINTED
org/apache/wicket/protocol/http/servlet/ServletPartFileItem.getString(Ljava/lang/String;)Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/servlet/ServletPartFileItem.getString()Ljava/lang/String;:TAINTED
org/apache/wicket/protocol/http/servlet/ServletPartFileItem.getInputStream()Ljava/io/InputStream;:TAINTED
testcode/sqli/MySqlWrapper.executeQuery(Ljava/lang/String;)Ljava/sql/ResultSet;:0
java/lang/Long.parseLong(Ljava/lang/String;)J:0|+SQL_INJECTION_SAFE#0
testcode/xpath/XPathSuperSecureUtil.encodeForXPath(Ljava/lang/String;)Ljava/lang/String;:0|+XPATH_INJECTION_SAFEtestcode/xpath/XPathBadApi.query(Ljava/lang/String;)Ljava/lang/String;:0javax/servlet/http/HttpServletRequest.getAttribute("safe"):SAFE@org/apache/jsp/xss/xss_005f8_005frequest_005fattribute_jsp
javax/servlet/http/HttpServletRequest.getAttribute("tainted"):TAINTED@org/apache/jsp/xss/xss_005f8_005frequest_005fattribute_jsp

javax/servlet/http/HttpSession.getAttribute(UNKNOWN):SAFE@org/apache/jsp/xss/xss_005f8_005frequest_005fattribute_jsp

org/apache/jsp/xss/xss_005f8_005frequest_005fattribute_jsp.suffix(TAINTED,SAFE,"_suffix"):SAFE@org/apache/jsp/xss/xss_005f8_005frequest_005fattribute_jspThis folder contains scripts to automate the generation of static files based on the messages.
This way the messages are visible on IDE but also available on the web on a publicly visible page.

```
> groovy BuildWebPage.groovy
[...]
Writing the template to out_web//index.htm
```

```
> groovy BuildSonarXmlFiles.groovy
Building ruleset findbugs (C:\Code\workspace-java\find-sec-bugs\website\out_sonar\rules-findbugs.xml)
Building ruleset jsp (C:\Code\workspace-java\find-sec-bugs\website\out_sonar\rules-jsp.xml)
Building profile findbugs-security-audit (C:\Code\workspace-java\find-sec-bugs\website\out_sonar\profiles-findbugs-security-audit.xml)
Building profile findbugs-security-minimal (C:\Code\workspace-java\find-sec-bugs\website\out_sonar\profiles-findbugs-security-minimal.xml)
Building profile findbugs-security-jsp (C:\Code\workspace-java\find-sec-bugs\website\out_sonar\profiles-findbugs-security-jsp.xml)
```CBC
CSRF
CORS
XXE
XSS
SSRF
XEE
JAX-RS
JAX-WS
XPath
ReDOS
JDBC
EL
SpEL
OGNL
CRLF
JNDI
PBKDF
HPP
JDO
JPQL
JDOQL
ESAPI
DTD
JEP
OAEP
JSP
JSTL
CAPEC
HMAC
OWASP
WASC
NISTreferer
untrusted
unvalidated
deserialization
geolocation
pseudorandom
servlet
hostname
sandboxing
classpath
filesystem
Eval
Parameterization
trigger
Cryptographic
cryptographic
RegEx
APIs
Cleartext
keystore
keystores
truststore
pentesters
ciphertext
plaintext
Cleartext
Keylength
cryptosystem
Redirector
Deserializing
Crypto
Pathname
sunsetting
deserializing
polymorphism
Unmarshaller
Stylesheet
templating

Stackoverflow
Cloudbees
Packtpub
Meterpreter
Qualys
Muñoz
Oleksandr
Mirosh
Suragch
Amodio
Dinis
Matias
Soler
Kubeck
Synactiv
Marlinspike
Grégoire
Acunetix
Securiteam

Blowfish
Hazelcast
Freemarker
Anorm
Xerces
Moustache
Logback
Restlet

SpEL
ReDOS

MODE_PRIVATE<div class="container">
    <div class="jumbotron jumbotron-ad hidden-print">

        <h1><i class="fa fa-copyright"></i>&nbsp; License</h1>

    </div>
</div>

<div class="container">

    <p>
        This software is released under <a href="http://www.gnu.org/licenses/lgpl.html">LGPL</a>.<br/>
        <br/><a href="http://www.gnu.org/licenses/lgpl.html"><img src="images/lgplv3.png" alt="LGPL"/></a>
        <br/>
    </p>

    <h2 class="page-header">Plugin use versus transformation</h2>

    <ul>
        <li>You can <b>use the plugin</b> to audit any kind of project (open source and proprietary).</li>
        <li>If you <b>modify the plugin</b>, you are required to publish the modifications.
            If you need custom detectors for your proprietary framework, it is suggested to create a separate
            plugin to avoid dependency to this plugin's code.
        </li>
    </ul>

    <h2 class="page-header">Other derived works</h2>

    <p>
        For reuse of the signatures and the descriptions in another project, please contact the <a href="https://github.com/h3xstream">author</a> to get an authorisation.
    </p>

</div>
