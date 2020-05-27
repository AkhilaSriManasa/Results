# Change Log

## [3.4.0-20190418](https://github.com/internetarchive/heritrix3/tree/3.4.0-20190418) (2019-04-18)
[Full Changelog](https://github.com/internetarchive/heritrix3/compare/3.4.0-20190207...3.4.0-20190418)

**Fixed bugs:**

- Invalid format exception in scanJobLog [\#239](https://github.com/internetarchive/heritrix3/issues/239)
- Domain name lookup failures get cached forever [\#234](https://github.com/internetarchive/heritrix3/issues/234)
- Allow failed lookups to expire, for \#234. [\#235](https://github.com/internetarchive/heritrix3/pull/235) ([anjackson](https://github.com/anjackson))

**Closed issues:**

- Failed DNS requests remain enqueued [\#252](https://github.com/internetarchive/heritrix3/issues/252)
- SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder" [\#236](https://github.com/internetarchive/heritrix3/issues/236)
- Make FetchHistoryProcessor 304 handler more robust [\#229](https://github.com/internetarchive/heritrix3/issues/229)
- ToeThread death when using HighestUriPrecedenceProvider [\#221](https://github.com/internetarchive/heritrix3/issues/221)
- Google Drive robots.txt broken [\#193](https://github.com/internetarchive/heritrix3/issues/193)

**Merged pull requests:**

- set of frontier management changes to support CrawlHQ module [\#253](https://github.com/internetarchive/heritrix3/pull/253) ([dvanduzer](https://github.com/dvanduzer))
- fix some trough dedup bugs [\#251](https://github.com/internetarchive/heritrix3/pull/251) ([nlevitt](https://github.com/nlevitt))
- Remove suffix from warcWriter since it is no longer used. [\#249](https://github.com/internetarchive/heritrix3/pull/249) ([ruebot](https://github.com/ruebot))
- Revert "Upgrade httpclient to 4.5.7 and handle cookies more compliantly" [\#248](https://github.com/internetarchive/heritrix3/pull/248) ([ato](https://github.com/ato))
- Upgrade httpclient to 4.5.7 and handle cookies more compliantly [\#246](https://github.com/internetarchive/heritrix3/pull/246) ([anjackson](https://github.com/anjackson))
- Update README.md [\#244](https://github.com/internetarchive/heritrix3/pull/244) ([mikeizbicki](https://github.com/mikeizbicki))
- Handle commas more compliantly when parsing srcset [\#243](https://github.com/internetarchive/heritrix3/pull/243) ([ato](https://github.com/ato))
- Trough dedup [\#242](https://github.com/internetarchive/heritrix3/pull/242) ([nlevitt](https://github.com/nlevitt))
- Ensure we start parsing full lines, for \#239. [\#240](https://github.com/internetarchive/heritrix3/pull/240) ([anjackson](https://github.com/anjackson))
- Add CHANGELOG; address \#233. [\#238](https://github.com/internetarchive/heritrix3/pull/238) ([ruebot](https://github.com/ruebot))

## [3.4.0-20190207](https://github.com/internetarchive/heritrix3/tree/3.4.0-20190207) (2019-02-07)
[Full Changelog](https://github.com/internetarchive/heritrix3/compare/3.4.0-20190205...3.4.0-20190207)

**Fixed bugs:**

- Add checks to guard against server sending 304 in error [\#230](https://github.com/internetarchive/heritrix3/pull/230) ([anjackson](https://github.com/anjackson))

**Merged pull requests:**

- Add synchronized statements for internetarchive/heritrix3\#221. [\#231](https://github.com/internetarchive/heritrix3/pull/231) ([anjackson](https://github.com/anjackson))

## [3.4.0-20190205](https://github.com/internetarchive/heritrix3/tree/3.4.0-20190205) (2019-02-05)
[Full Changelog](https://github.com/internetarchive/heritrix3/compare/3.2.0...3.4.0-20190205)

**Fixed bugs:**

- HTML extractor does not handle the base href correctly when it's relative [\#208](https://github.com/internetarchive/heritrix3/issues/208)
- Heritrix3 \(including pre-built binaries\) Fails to Bootstrap with Java8 due to Changes in Java stdlib [\#176](https://github.com/internetarchive/heritrix3/issues/176)
- Heritrix3 Fails to Build from Source [\#175](https://github.com/internetarchive/heritrix3/issues/175)
- Missing OneLineSimpleLayout class file [\#173](https://github.com/internetarchive/heritrix3/issues/173)

**Closed issues:**

- BdbFrontier thread safety [\#212](https://github.com/internetarchive/heritrix3/issues/212)
- HTTP response only results in garbage bytes [\#206](https://github.com/internetarchive/heritrix3/issues/206)
- Possibly stalled crawl [\#203](https://github.com/internetarchive/heritrix3/issues/203)
- Where do i find the crawled information \(Contents\) after crawling is completed  [\#199](https://github.com/internetarchive/heritrix3/issues/199)
- `-j` option can'not handle spaces in directory names? [\#182](https://github.com/internetarchive/heritrix3/issues/182)
- heritrix doesn't scrape rewrite srcset urls correctly [\#177](https://github.com/internetarchive/heritrix3/issues/177)
- Possible race-condition when first using the WARC writers? [\#167](https://github.com/internetarchive/heritrix3/issues/167)
- can you integration with spring boot [\#162](https://github.com/internetarchive/heritrix3/issues/162)
- Noisy alerts about 401s without auth challenge  [\#158](https://github.com/internetarchive/heritrix3/issues/158)
- Can't see all beans in scripts [\#157](https://github.com/internetarchive/heritrix3/issues/157)
- How to configure warcWriter with MirrorWriter?  [\#156](https://github.com/internetarchive/heritrix3/issues/156)
- Requesting inaccurate paths from js causes routing errors [\#155](https://github.com/internetarchive/heritrix3/issues/155)

**Merged pull requests:**

- do not checkpoint if crawl job has not started [\#227](https://github.com/internetarchive/heritrix3/pull/227) ([nlevitt](https://github.com/nlevitt))
- namespace scope log logger to crawl job [\#226](https://github.com/internetarchive/heritrix3/pull/226) ([nlevitt](https://github.com/nlevitt))
- un-threadlocal the HConnection [\#224](https://github.com/internetarchive/heritrix3/pull/224) ([nlevitt](https://github.com/nlevitt))
- reset HBaseAdmin on error [\#223](https://github.com/internetarchive/heritrix3/pull/223) ([nlevitt](https://github.com/nlevitt))
- keep trying to start up hbase dedup forever [\#222](https://github.com/internetarchive/heritrix3/pull/222) ([nlevitt](https://github.com/nlevitt))
- implement PredicatedDecideRule.onlyDecision\(\) [\#220](https://github.com/internetarchive/heritrix3/pull/220) ([nlevitt](https://github.com/nlevitt))
- use non-deprecated hbase api [\#219](https://github.com/internetarchive/heritrix3/pull/219) ([nlevitt](https://github.com/nlevitt))
- Correct spelling mistakes. [\#218](https://github.com/internetarchive/heritrix3/pull/218) ([EdwardBetts](https://github.com/EdwardBetts))
- Update API with note about checkpoint launching. [\#217](https://github.com/internetarchive/heritrix3/pull/217) ([anjackson](https://github.com/anjackson))
- Extend API to simplify using the latest checkpoint [\#215](https://github.com/internetarchive/heritrix3/pull/215) ([anjackson](https://github.com/anjackson))
- Ensure frontier work queues are updated safely across threads. [\#213](https://github.com/internetarchive/heritrix3/pull/213) ([anjackson](https://github.com/anjackson))
- fix exception starting DecideRuleSequence logging [\#210](https://github.com/internetarchive/heritrix3/pull/210) ([nlevitt](https://github.com/nlevitt))
- HtmlExtractor: allow relative hrefs in the base element [\#209](https://github.com/internetarchive/heritrix3/pull/209) ([anjackson](https://github.com/anjackson))
- Fix link to User Guide [\#207](https://github.com/internetarchive/heritrix3/pull/207) ([maurice-schleussinger](https://github.com/maurice-schleussinger))
- Add parameter to allow even distribution for parallel queues. [\#205](https://github.com/internetarchive/heritrix3/pull/205) ([adam-miller](https://github.com/adam-miller))
- catch exceptions scoping outlinks to stop them from derailing process… [\#197](https://github.com/internetarchive/heritrix3/pull/197) ([nlevitt](https://github.com/nlevitt))
- fix for test failures in a workspace on NFS-mounted filesystem [\#196](https://github.com/internetarchive/heritrix3/pull/196) ([kngenie](https://github.com/kngenie))
- limit max size of form input [\#194](https://github.com/internetarchive/heritrix3/pull/194) ([galgeek](https://github.com/galgeek))
- Enforce robots.txt character limit per char not per line [\#192](https://github.com/internetarchive/heritrix3/pull/192) ([ato](https://github.com/ato))
- Allow JavaDNS to be disabled as part of resolving outstanding build and test issues [\#190](https://github.com/internetarchive/heritrix3/pull/190) ([anjackson](https://github.com/anjackson))
- WARCLimitEnforcer.java - Add support for multiple warc writers. [\#189](https://github.com/internetarchive/heritrix3/pull/189) ([adam-miller](https://github.com/adam-miller))
- treat a failed fetch \(e.g. socket timeout\) of robots.txt the same way… [\#187](https://github.com/internetarchive/heritrix3/pull/187) ([nlevitt](https://github.com/nlevitt))
- reduce batch size to 400 and avoid ridiculously long log lines [\#186](https://github.com/internetarchive/heritrix3/pull/186) ([nlevitt](https://github.com/nlevitt))
- escape strings in sql posted to trough [\#185](https://github.com/internetarchive/heritrix3/pull/185) ([nlevitt](https://github.com/nlevitt))
- trough feed [\#180](https://github.com/internetarchive/heritrix3/pull/180) ([nlevitt](https://github.com/nlevitt))
- Add parsing for srcset attributes [\#179](https://github.com/internetarchive/heritrix3/pull/179) ([BitBaron](https://github.com/BitBaron))
- KafkaCrawlLogFeed had been using lots of heap because each callback i… [\#178](https://github.com/internetarchive/heritrix3/pull/178) ([nlevitt](https://github.com/nlevitt))
- AMQP fine control [\#171](https://github.com/internetarchive/heritrix3/pull/171) ([anjackson](https://github.com/anjackson))
- fix for race-condition when first using the WARC writers https://gith… [\#168](https://github.com/internetarchive/heritrix3/pull/168) ([nlevitt](https://github.com/nlevitt))
- Don't wait to receive Umbra urls if Heritrix sends no url to Umbra [\#166](https://github.com/internetarchive/heritrix3/pull/166) ([galgeek](https://github.com/galgeek))
- AMQP URL Waiter [\#165](https://github.com/internetarchive/heritrix3/pull/165) ([galgeek](https://github.com/galgeek))
- Fixes for apparent build errors \(extends \#154\) [\#164](https://github.com/internetarchive/heritrix3/pull/164) ([nlevitt](https://github.com/nlevitt))
- Kafka 0.9 [\#163](https://github.com/internetarchive/heritrix3/pull/163) ([nlevitt](https://github.com/nlevitt))
- No link extraction on URI not successfully downloaded [\#161](https://github.com/internetarchive/heritrix3/pull/161) ([kris-sigur](https://github.com/kris-sigur))
- Fixes issue \#158 : Noisy alerts about 401s without auth challenge [\#159](https://github.com/internetarchive/heritrix3/pull/159) ([kris-sigur](https://github.com/kris-sigur))
- Fixes for apparent build errors [\#154](https://github.com/internetarchive/heritrix3/pull/154) ([anjackson](https://github.com/anjackson))
- Switch to Java 7 [\#152](https://github.com/internetarchive/heritrix3/pull/152) ([anjackson](https://github.com/anjackson))
- Make Content-Location header url INFERRED not REFFER hop type since C… [\#151](https://github.com/internetarchive/heritrix3/pull/151) ([vonrosen](https://github.com/vonrosen))
- various changes to amqp publish and receive [\#150](https://github.com/internetarchive/heritrix3/pull/150) ([nlevitt](https://github.com/nlevitt))
- Update to ExtractorHTML.java for cond. comments [\#149](https://github.com/internetarchive/heritrix3/pull/149) ([eleclerc](https://github.com/eleclerc))
- Don't canonicalize source tag so that SourceSeedDecideRule will work.… [\#148](https://github.com/internetarchive/heritrix3/pull/148) ([vonrosen](https://github.com/vonrosen))
- More fixes for mutlipart form submission [\#146](https://github.com/internetarchive/heritrix3/pull/146) ([vonrosen](https://github.com/vonrosen))
- Make some urls with whitespace acceptable to JavaScript extractor. [\#145](https://github.com/internetarchive/heritrix3/pull/145) ([vonrosen](https://github.com/vonrosen))
- run received urls through the candidates processor, to check scope an… [\#144](https://github.com/internetarchive/heritrix3/pull/144) ([nlevitt](https://github.com/nlevitt))
- handle login forms with \<input type="text"\> fields in addition to use… [\#143](https://github.com/internetarchive/heritrix3/pull/143) ([nlevitt](https://github.com/nlevitt))
- Form login multipart [\#142](https://github.com/internetarchive/heritrix3/pull/142) ([nlevitt](https://github.com/nlevitt))
- Disable SNI for a request if that request failed due to an SNI error … [\#141](https://github.com/internetarchive/heritrix3/pull/141) ([vonrosen](https://github.com/vonrosen))
- handle multiple clauses for same user agent in robots.txt [\#139](https://github.com/internetarchive/heritrix3/pull/139) ([nlevitt](https://github.com/nlevitt))
- crawl level and host level limits on \*novel\* \(not deduplicated\) bytes and urls [\#138](https://github.com/internetarchive/heritrix3/pull/138) ([nlevitt](https://github.com/nlevitt))
- SourceSeedDecideRule, SeedLimitsEnforcer [\#137](https://github.com/internetarchive/heritrix3/pull/137) ([nlevitt](https://github.com/nlevitt))
- Register seeds send in via AMQP [\#136](https://github.com/internetarchive/heritrix3/pull/136) ([anjackson](https://github.com/anjackson))
- Allow KnowledgableExtractorJS to parse out youtube watch from youtube… [\#135](https://github.com/internetarchive/heritrix3/pull/135) ([vonrosen](https://github.com/vonrosen))
- Add maximum to number of cookies to store for domain to BdbCookieStore [\#133](https://github.com/internetarchive/heritrix3/pull/133) ([vonrosen](https://github.com/vonrosen))
- try very hard to start url consumer, and therefore bind the queue to … [\#132](https://github.com/internetarchive/heritrix3/pull/132) ([nlevitt](https://github.com/nlevitt))
- set isRunning=true so that stop\(\) gets called to avoid leaking connec… [\#131](https://github.com/internetarchive/heritrix3/pull/131) ([nlevitt](https://github.com/nlevitt))
- catch exceptions and log error in StatisticsTracker.run\(\), to make su… [\#130](https://github.com/internetarchive/heritrix3/pull/130) ([nlevitt](https://github.com/nlevitt))
- load keytool utility main class dynamically, trying both the old and … [\#129](https://github.com/internetarchive/heritrix3/pull/129) ([nlevitt](https://github.com/nlevitt))
- AMQPUrlReceiver changes to support RabbitMQ \>= 3.3 [\#128](https://github.com/internetarchive/heritrix3/pull/128) ([anjackson](https://github.com/anjackson))
- 'build.plugins.plugin.version' for org.apache.maven.plugins:maven-compiler-plugin is missing [\#126](https://github.com/internetarchive/heritrix3/pull/126) ([caofangkun](https://github.com/caofangkun))
- Amqp declarations fix [\#125](https://github.com/internetarchive/heritrix3/pull/125) ([ldko](https://github.com/ldko))
- Allow realm to be set by server for basic auth. [\#124](https://github.com/internetarchive/heritrix3/pull/124) ([vonrosen](https://github.com/vonrosen))
- Hosts report [\#123](https://github.com/internetarchive/heritrix3/pull/123) ([kris-sigur](https://github.com/kris-sigur))
- only submit checkbox and radio button form fields if they are on by d… [\#122](https://github.com/internetarchive/heritrix3/pull/122) ([nlevitt](https://github.com/nlevitt))
- new contrib module KnowledgableExtractorJS, a subclass of ExtractorJS th... [\#121](https://github.com/internetarchive/heritrix3/pull/121) ([nlevitt](https://github.com/nlevitt))
- for ARI-4267 accept possible uris with two dots in the filename part if ... [\#120](https://github.com/internetarchive/heritrix3/pull/120) ([nlevitt](https://github.com/nlevitt))
- Fix for HER-2082 [\#119](https://github.com/internetarchive/heritrix3/pull/119) ([adam-miller](https://github.com/adam-miller))
- Fix for ServerNotModified WARC revisit records incorrectly record WARC-Payload-Digest [\#118](https://github.com/internetarchive/heritrix3/pull/118) ([kris-sigur](https://github.com/kris-sigur))
- avoid java.lang.NullPointerException at org.archive.modules.writer.Write... [\#117](https://github.com/internetarchive/heritrix3/pull/117) ([nlevitt](https://github.com/nlevitt))
- make sure log4j is configured when running unit tests, to avoid log4j er... [\#116](https://github.com/internetarchive/heritrix3/pull/116) ([nlevitt](https://github.com/nlevitt))
- Set character set to UTF-8 when passing through files. [\#115](https://github.com/internetarchive/heritrix3/pull/115) ([kris-sigur](https://github.com/kris-sigur))
- remove RecordingOutputStreamTest.java \(moving to webarchive-commons\) [\#114](https://github.com/internetarchive/heritrix3/pull/114) ([nlevitt](https://github.com/nlevitt))
- Amqp receiver deadlock [\#112](https://github.com/internetarchive/heritrix3/pull/112) ([nlevitt](https://github.com/nlevitt))
- somewhat ugly fix to handle exceptions from the bean browser like java.l... [\#111](https://github.com/internetarchive/heritrix3/pull/111) ([nlevitt](https://github.com/nlevitt))
- Upgrade to HttpClient 4.3.6 [\#110](https://github.com/internetarchive/heritrix3/pull/110) ([kris-sigur](https://github.com/kris-sigur))
- so that it can appear in the crawl log, add contentSize to CrawlURI extr... [\#109](https://github.com/internetarchive/heritrix3/pull/109) ([nlevitt](https://github.com/nlevitt))
- kafka crawl log feed [\#108](https://github.com/internetarchive/heritrix3/pull/108) ([nlevitt](https://github.com/nlevitt))
- Handle case where form does not have an action defined. [\#107](https://github.com/internetarchive/heritrix3/pull/107) ([vonrosen](https://github.com/vonrosen))
- seriously, fix extraInfo handling in AMQPCrawlLogFeed [\#106](https://github.com/internetarchive/heritrix3/pull/106) ([nlevitt](https://github.com/nlevitt))
- fix extraInfo handling in AMQPCrawlLogFeed [\#105](https://github.com/internetarchive/heritrix3/pull/105) ([nlevitt](https://github.com/nlevitt))
- change field names to match new druid config [\#104](https://github.com/internetarchive/heritrix3/pull/104) ([nlevitt](https://github.com/nlevitt))
- CandidatesProcessor.java [\#103](https://github.com/internetarchive/heritrix3/pull/103) ([adam-miller](https://github.com/adam-miller))
- avoid deadlock in AMQPUrlReceiver hopefully [\#102](https://github.com/internetarchive/heritrix3/pull/102) ([nlevitt](https://github.com/nlevitt))
- Remove forcefetch for AMQP received urls so they don't get crawled twice... [\#101](https://github.com/internetarchive/heritrix3/pull/101) ([vonrosen](https://github.com/vonrosen))
- Allow discovery of urls in content attribute of meta tags. [\#100](https://github.com/internetarchive/heritrix3/pull/100) ([vonrosen](https://github.com/vonrosen))
- AMQPCrawlLogFeed, DecideRuleSequenceWithAMQPFeed, DecideRuleSequence.logExtraInfo [\#99](https://github.com/internetarchive/heritrix3/pull/99) ([nlevitt](https://github.com/nlevitt))
- Fix for HER-2074 [\#97](https://github.com/internetarchive/heritrix3/pull/97) ([kris-sigur](https://github.com/kris-sigur))
- new cookie store system to address HER-2070 "cookie monster" bug [\#96](https://github.com/internetarchive/heritrix3/pull/96) ([nlevitt](https://github.com/nlevitt))
- FIX corner-case of bean browser failing due to an exception from hashCode\(\) [\#95](https://github.com/internetarchive/heritrix3/pull/95) ([kngenie](https://github.com/kngenie))
- do not require "+" \(plus sign\) before @OPERATOR\_CONTACT\_URL@ in user-age... [\#94](https://github.com/internetarchive/heritrix3/pull/94) ([nlevitt](https://github.com/nlevitt))
- Allow urls in JavaScript between unicode quotes to be detected. [\#93](https://github.com/internetarchive/heritrix3/pull/93) ([vonrosen](https://github.com/vonrosen))
- remove more unused classes [\#92](https://github.com/internetarchive/heritrix3/pull/92) ([nlevitt](https://github.com/nlevitt))
- FetchHTTP.java [\#91](https://github.com/internetarchive/heritrix3/pull/91) ([adam-miller](https://github.com/adam-miller))
- Move Wayback-dedup module to heritrix-contrib [\#90](https://github.com/internetarchive/heritrix3/pull/90) ([kngenie](https://github.com/kngenie))
- Don’t let exception from property getter fail entire bean-browser. [\#89](https://github.com/internetarchive/heritrix3/pull/89) ([kngenie](https://github.com/kngenie))
- fix bug in CrawlURI.compare\(\) discovered by Kenji, add unit test CrawlUR... [\#88](https://github.com/internetarchive/heritrix3/pull/88) ([nlevitt](https://github.com/nlevitt))
- Allow xml extractor to handle urls in CDATA. [\#87](https://github.com/internetarchive/heritrix3/pull/87) ([vonrosen](https://github.com/vonrosen))
- remove unused Transform\* classes [\#86](https://github.com/internetarchive/heritrix3/pull/86) ([nlevitt](https://github.com/nlevitt))
- switch to mainline iipc webarchive-commons latest release [\#84](https://github.com/internetarchive/heritrix3/pull/84) ([nlevitt](https://github.com/nlevitt))
- oops! count novel urls/bytes for hosts report, etc [\#83](https://github.com/internetarchive/heritrix3/pull/83) ([nlevitt](https://github.com/nlevitt))
- Fix for HER-2071 [\#82](https://github.com/internetarchive/heritrix3/pull/82) ([kris-sigur](https://github.com/kris-sigur))
- Hbase cdh5 [\#81](https://github.com/internetarchive/heritrix3/pull/81) ([nlevitt](https://github.com/nlevitt))
- ExtractorHTML when a/@href links include the attribute data-remote="true... [\#80](https://github.com/internetarchive/heritrix3/pull/80) ([nlevitt](https://github.com/nlevitt))
- Revisit redux [\#79](https://github.com/internetarchive/heritrix3/pull/79) ([nlevitt](https://github.com/nlevitt))
- treat content as html and extract links if it looks like html, even if m... [\#78](https://github.com/internetarchive/heritrix3/pull/78) ([nlevitt](https://github.com/nlevitt))
- Force urls received from AMQP to be recrawled so custom http headers can... [\#77](https://github.com/internetarchive/heritrix3/pull/77) ([vonrosen](https://github.com/vonrosen))
- HER-2039 remove class Link, use CrawlURI [\#76](https://github.com/internetarchive/heritrix3/pull/76) ([nlevitt](https://github.com/nlevitt))
- in CrawlURI.createCrawlURI\(\), avoid clobbering inherited data with data ... [\#75](https://github.com/internetarchive/heritrix3/pull/75) ([nlevitt](https://github.com/nlevitt))
- Fix for https://webarchive.jira.com/browse/ARI-3943 [\#74](https://github.com/internetarchive/heritrix3/pull/74) ([vonrosen](https://github.com/vonrosen))
- Treat codebase as link hops, not embeds [\#73](https://github.com/internetarchive/heritrix3/pull/73) ([kris-sigur](https://github.com/kris-sigur))
- add A\_ANNOTATIONS to persistentKeys so that CrawlURI doesn't lose its an... [\#72](https://github.com/internetarchive/heritrix3/pull/72) ([nlevitt](https://github.com/nlevitt))
- avoid calling CheckpointService.hasAvailableCheckpoints\(\) when crawl not... [\#71](https://github.com/internetarchive/heritrix3/pull/71) ([nlevitt](https://github.com/nlevitt))
- for ARI-3712, add extracted links relative to both via and base, and annotate with "extractorSWFRelToVia", "extractorSWFRelToBase", or "extractorSWFRelToBoth" if resulting link is the same whether relative to base or via [\#70](https://github.com/internetarchive/heritrix3/pull/70) ([nlevitt](https://github.com/nlevitt))
- For https://webarchive.jira.com/browse/ARI-3865 [\#69](https://github.com/internetarchive/heritrix3/pull/69) ([vonrosen](https://github.com/vonrosen))
- handle exception determining whether to apply overlay [\#68](https://github.com/internetarchive/heritrix3/pull/68) ([nlevitt](https://github.com/nlevitt))
- don't log severe with stack trace on normal amqp shutdown [\#67](https://github.com/internetarchive/heritrix3/pull/67) ([nlevitt](https://github.com/nlevitt))
- oops, make "exit java process" button work again [\#66](https://github.com/internetarchive/heritrix3/pull/66) ([nlevitt](https://github.com/nlevitt))
- shut down the starter-restarter thread at crawl finish!! [\#65](https://github.com/internetarchive/heritrix3/pull/65) ([nlevitt](https://github.com/nlevitt))
- Via surt prefixed decide rule [\#64](https://github.com/internetarchive/heritrix3/pull/64) ([adam-miller](https://github.com/adam-miller))
- Contrib - ExtractorPDFContent [\#63](https://github.com/internetarchive/heritrix3/pull/63) ([adam-miller](https://github.com/adam-miller))
- Ari 3765 gracefully handle amqp server going up and down [\#62](https://github.com/internetarchive/heritrix3/pull/62) ([nlevitt](https://github.com/nlevitt))
- HER-2065 synchronize on inactiveQueuesByPrecedence inside of synchronize... [\#61](https://github.com/internetarchive/heritrix3/pull/61) ([nlevitt](https://github.com/nlevitt))
- Cosmetics [\#60](https://github.com/internetarchive/heritrix3/pull/60) ([nlevitt](https://github.com/nlevitt))
- fix unit test now that we accept speculative urls with query params with... [\#59](https://github.com/internetarchive/heritrix3/pull/59) ([nlevitt](https://github.com/nlevitt))
- for ARI-3723, accept speculative urls with query params with no value [\#58](https://github.com/internetarchive/heritrix3/pull/58) ([nlevitt](https://github.com/nlevitt))
- AMQPUrlReceiver - improve handling of case where rabbitmq is unreachable... [\#57](https://github.com/internetarchive/heritrix3/pull/57) ([nlevitt](https://github.com/nlevitt))
- fix FormLoginProcessor checkpointing [\#56](https://github.com/internetarchive/heritrix3/pull/56) ([nlevitt](https://github.com/nlevitt))
- oops, update test to expect post data as url-encoded query string [\#54](https://github.com/internetarchive/heritrix3/pull/54) ([nlevitt](https://github.com/nlevitt))
- Fix form login [\#53](https://github.com/internetarchive/heritrix3/pull/53) ([nlevitt](https://github.com/nlevitt))
- Implicitly add the ${} around groovyExpression. When cxml contains ${}, ... [\#52](https://github.com/internetarchive/heritrix3/pull/52) ([nlevitt](https://github.com/nlevitt))
- Expression deciderule [\#51](https://github.com/internetarchive/heritrix3/pull/51) ([nlevitt](https://github.com/nlevitt))
- Replace deprecated routines in guava [\#50](https://github.com/internetarchive/heritrix3/pull/50) ([shriphani](https://github.com/shriphani))
- Youtube march 2014 [\#49](https://github.com/internetarchive/heritrix3/pull/49) ([nlevitt](https://github.com/nlevitt))
- Umbra [\#48](https://github.com/internetarchive/heritrix3/pull/48) ([nlevitt](https://github.com/nlevitt))
- Adjusting Youtube itag priority [\#47](https://github.com/internetarchive/heritrix3/pull/47) ([adam-miller](https://github.com/adam-miller))
- switch dependency from ia-web-commons 1.1.1-SNAPSHOT to webarchive-commo... [\#46](https://github.com/internetarchive/heritrix3/pull/46) ([nlevitt](https://github.com/nlevitt))
- Update youtube itags [\#45](https://github.com/internetarchive/heritrix3/pull/45) ([nlevitt](https://github.com/nlevitt))
- update httpcomponents, should address NPE we've seen https://issues.apac... [\#44](https://github.com/internetarchive/heritrix3/pull/44) ([nlevitt](https://github.com/nlevitt))
- fix job.log file handler was left open when jobdir is removed [\#43](https://github.com/internetarchive/heritrix3/pull/43) ([martinsbalodis](https://github.com/martinsbalodis))
- Adding the queue declaration and binding to the UrlReceiver [\#42](https://github.com/internetarchive/heritrix3/pull/42) ([eldondev](https://github.com/eldondev))
- Fix slow cookies [\#41](https://github.com/internetarchive/heritrix3/pull/41) ([nlevitt](https://github.com/nlevitt))
- For https://webarchive.jira.com/browse/HER-2064 [\#40](https://github.com/internetarchive/heritrix3/pull/40) ([vonrosen](https://github.com/vonrosen))
- progress and formatting changes [\#39](https://github.com/internetarchive/heritrix3/pull/39) ([nlevitt](https://github.com/nlevitt))
- Umbra - AMQPUrlReceiver.java receive urls via amqp and add to frontier, related changes [\#38](https://github.com/internetarchive/heritrix3/pull/38) ([nlevitt](https://github.com/nlevitt))
- fix HER-2063 - omit port in Host request header when it is default for t... [\#37](https://github.com/internetarchive/heritrix3/pull/37) ([nlevitt](https://github.com/nlevitt))
- Avoid the exception below by handling bad charsets in FetchHTTP. Restore... [\#36](https://github.com/internetarchive/heritrix3/pull/36) ([nlevitt](https://github.com/nlevitt))
- whoops! send escaped path+query on http request line; had been sending r... [\#35](https://github.com/internetarchive/heritrix3/pull/35) ([nlevitt](https://github.com/nlevitt))
- fix NullPointerException in case of 401 with no auth challenge \(includes... [\#34](https://github.com/internetarchive/heritrix3/pull/34) ([nlevitt](https://github.com/nlevitt))
- First pass at a processor to publish crawluris to AMQP channels [\#33](https://github.com/internetarchive/heritrix3/pull/33) ([eldondev](https://github.com/eldondev))
- Switch to BasicHttpClientConnectionManager instead of [\#32](https://github.com/internetarchive/heritrix3/pull/32) ([nlevitt](https://github.com/nlevitt))
- make http proxy port configurable in cxml, avoiding this: org.springfram... [\#31](https://github.com/internetarchive/heritrix3/pull/31) ([nlevitt](https://github.com/nlevitt))
- Fix bdb cookie store [\#30](https://github.com/internetarchive/heritrix3/pull/30) ([nlevitt](https://github.com/nlevitt))
- HER-2062 Fix for WorkQueueFrontier.deleteURIs handling of retired queues [\#29](https://github.com/internetarchive/heritrix3/pull/29) ([kris-sigur](https://github.com/kris-sigur))
- switch to httpcomponents, get rid of archive-overlay-commons-httpclient [\#28](https://github.com/internetarchive/heritrix3/pull/28) ([nlevitt](https://github.com/nlevitt))
- rename dist/README.md to dist/README.txt so that maven bundles it in the... [\#27](https://github.com/internetarchive/heritrix3/pull/27) ([nlevitt](https://github.com/nlevitt))

## [3.2.0](https://github.com/internetarchive/heritrix3/tree/3.2.0) (2014-01-10)
[Full Changelog](https://github.com/internetarchive/heritrix3/compare/3.1.1...3.2.0)

**Merged pull requests:**

- update readme for 3.2.0 release [\#26](https://github.com/internetarchive/heritrix3/pull/26) ([nlevitt](https://github.com/nlevitt))
- bump version number to 3.2.0 for release [\#25](https://github.com/internetarchive/heritrix3/pull/25) ([nlevitt](https://github.com/nlevitt))
- for url-agnostic dedup, follow "Proposal for Standardizing the Recording... [\#24](https://github.com/internetarchive/heritrix3/pull/24) ([nlevitt](https://github.com/nlevitt))
- fix HER-1979 so heritrix can run on windows xp [\#23](https://github.com/internetarchive/heritrix3/pull/23) ([nlevitt](https://github.com/nlevitt))
- HER-1726: Templatize HTML [\#21](https://github.com/internetarchive/heritrix3/pull/21) ([adam-miller](https://github.com/adam-miller))
- Her 2031 - Improve login-form submission options [\#20](https://github.com/internetarchive/heritrix3/pull/20) ([gojomo](https://github.com/gojomo))
- BeanLookupBindings for simpler script access to beans [\#19](https://github.com/internetarchive/heritrix3/pull/19) ([travisfw](https://github.com/travisfw))
- Fix for HER-2018: XML representation for /engine/job/\<jobName\>/beans returns incorrect url for named beans [\#17](https://github.com/internetarchive/heritrix3/pull/17) ([adam-miller](https://github.com/adam-miller))
- Fix for HER-2017 XML representation of beans uses root node of type "script" [\#16](https://github.com/internetarchive/heritrix3/pull/16) ([adam-miller](https://github.com/adam-miller))
- Reuse htmllinkcontext [\#15](https://github.com/internetarchive/heritrix3/pull/15) ([kngenie](https://github.com/kngenie))
- suppress unused warnings for serialVersionUid [\#14](https://github.com/internetarchive/heritrix3/pull/14) ([travisfw](https://github.com/travisfw))
- have TooManyPathSegmentsDecideRule count path segments only [\#13](https://github.com/internetarchive/heritrix3/pull/13) ([travisfw](https://github.com/travisfw))
- generics warnings fixes [\#12](https://github.com/internetarchive/heritrix3/pull/12) ([travisfw](https://github.com/travisfw))
- New reports [\#11](https://github.com/internetarchive/heritrix3/pull/11) ([travisfw](https://github.com/travisfw))
- ScriptedDecideRule\#getEngine\(\) rewrite for better synchronization and thread local mgmt [\#10](https://github.com/internetarchive/heritrix3/pull/10) ([travisfw](https://github.com/travisfw))

## [3.1.1](https://github.com/internetarchive/heritrix3/tree/3.1.1) (2012-05-02)
[Full Changelog](https://github.com/internetarchive/heritrix3/compare/3.0.0...3.1.1)

**Merged pull requests:**

- Publicsuffixes2 [\#9](https://github.com/internetarchive/heritrix3/pull/9) ([kngenie](https://github.com/kngenie))
- Ip address set decide rule [\#7](https://github.com/internetarchive/heritrix3/pull/7) ([travisfw](https://github.com/travisfw))
- HER-2001: Use the CodeMirror editor for crawl config and script console [\#6](https://github.com/internetarchive/heritrix3/pull/6) ([ato](https://github.com/ato))
- HER-1998 [\#5](https://github.com/internetarchive/heritrix3/pull/5) ([adam-miller](https://github.com/adam-miller))
- sort script engines in script console [\#4](https://github.com/internetarchive/heritrix3/pull/4) ([travisfw](https://github.com/travisfw))

## [3.0.0](https://github.com/internetarchive/heritrix3/tree/3.0.0) (2009-12-05)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# Heritrix
[![Build Status](https://travis-ci.org/internetarchive/heritrix3.svg?branch=master)](https://travis-ci.org/internetarchive/heritrix3)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.archive/heritrix/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.archive/heritrix)
[![Javadoc](https://javadoc-badge.appspot.com/org.archive/heritrix.svg?label=javadoc)](https://www.javadoc.io/doc/org.archive.heritrix/heritrix-engine)
[![LICENSE](https://img.shields.io/badge/license-Apache-blue.svg?style=flat-square)](./LICENSE)

## Introduction

Heritrix is the Internet Archive's open-source, extensible, web-scale, archival-quality web crawler project. Heritrix (sometimes spelled heretrix, or misspelled or missaid as heratrix/heritix/heretix/heratix) is an archaic word for heiress (woman who inherits). Since our crawler seeks to collect and preserve the digital artifacts of our culture for the benefit of future researchers and generations, this name seemed apt.

## Crawl Operators!

Heritrix is designed to respect the [`robots.txt`](http://www.robotstxt.org/wc/robots.html) exclusion directives and [META robots tags](http://www.robotstxt.org/wc/exclusion.html#meta). Please consider the
load your crawl will place on seed sites and set politeness policies accordingly. Also, always identify your crawl with contact information in the `User-Agent` so sites that may be adversely affected by your crawl can contact you or adapt their server behavior accordingly.

## Getting Started

- [User Manual](https://github.com/internetarchive/heritrix3/wiki)

## Developer Documentation

- [Developer Manual](http://crawler.archive.org/articles/developer_manual/index.html)
- [REST API documentation](https://heritrix.readthedocs.io/en/latest/api.html)
- JavaDoc: [engine](https://www.javadoc.io/doc/org.archive.heritrix/heritrix-engine), [modules](https://www.javadoc.io/doc/org.archive.heritrix/heritrix-modules), [commons](https://www.javadoc.io/doc/org.archive.heritrix/heritrix-commons), [contrib](https://www.javadoc.io/doc/org.archive.heritrix/heritrix-contrib)


## Latest Releases

Information about releases can be found [here](https://github.com/internetarchive/heritrix3/wiki#latest-releases).

## License

Heritrix is free software; you can redistribute it and/or modify it under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Some individual source code files are subject to or offered under other licenses. See the included [`LICENSE.txt`](./LICENSE) file for more information.

Heritrix is distributed with the libraries it depends upon. The libraries can be found under the `lib` directory in the release distribution, and are used under the terms of their respective licenses, which are included alongside the libraries in the `lib` directory.
${build.timestamp}
${pom.version}
 
 P   R   E   F A   C   E . 
 T h i s   L i f e   o f   C o l u m b u s   i s   o n e   o f   a   s e r i e s   o f   b i o g r a p h i e s   p r e p a r e d   u n d e r   m y   s u p e r i n t e n d e n c e ,   a n d   f o r   t h e   m o s t   p a r t   t a k e n   v e r b a t i m   f r o m   m y   " H i s t o r y   o f   t h e   S p a n i s h   C o n q u e s t   i n   A m e r i c a . "   
 T h a t   w o r k   w a s   w r i t t e n   c h i e f l y   w i t h   a   v i e w   t o   i l l u s t r a t e   t h e   h i s t o r y   o f   s l a v e r y ,   a n d   n o t   t o   g i v e   f u l l   a c c o u n t s   o f   t h e   d e e d s   o f   t h e   d i s c o v e r e r s   a n d   c o n q u e r o r s   o f   t h e   N e w   W o r l d ,   m u c h   l e s s   t o   g i v e   a   c o n d e n s e d   m e m o i r   o f   e a c h   o f   t h e m .   
 I t   h a s ,   t h e r e f o r e ,   b e e n   n e c e s s a r y   t o   r e a r r a n g e   a n d   a d d   c o n s i d e r a b l y   t o   t h e s e   m a t e r i a l s ,   a n d   f o r   t h i s   a s s i s t a n c e   I   a m   i n d e b t e d   t o   t h e   s k i l l   a n d   r e s e a r c h   o f   M r .   H e r b e r t   P r e s t o n   T h o m a s .   
 P e r h a p s   t h e r e   a r e   f e w   o f   t h e   g r e a t   p e r s o n a g e s   
  v i i i   	 P R E F A C E .   
 i n   h i s t o r y   w h o   h a v e   b e e n   m o r e   t a l k e d   a b o u t   a n d   w r i t t e n   a b o u t   t h a n   C h r i s t o p h e r   C o l u m b u s ,   t h e   d i s c o v e r e r   o f   A m e r i c a .   I t   m i g h t   s e e m ,   t h e r e  f o r e ,   t h a t   t h e r e   i s   v e r y   l i t t l e   t h a t   i s   n e w   t o   b e   s a i d   a b o u t   h i m .   I   d o   n o t   t h i n k ,   h o w e v e r ,   t h a t   t h i s   i s   a l t o g e t h e r   t h e   c a s e .   A b s o r b e d   i n ,   a n d   t o   a   c e r t a i n   e x t e n t   o v e r c o m e   b y   t h e   c o n t e m p l a t i o n   o f   t h e   p r i n c i p a l   e v e n t ,   w e   h a v e   s o m e t i m e s ,   p e r  h a p s ,   b e e n   m i s t a k e n   a s   t o   t h e   c a u s e s   w h i c h   l e d   t o   i t .   W e   a r e   a p t   t o   l o o k   u p o n   C o l u m b u s   a s   a   p e r s o n   w h o   k n e w   t h a t   t h e r e   e x i s t e d   a   g r e a t   u n d i s c o v e r e d   c o n t i n e n t ,   a n d   w h o   m a d e   h i s   w a y   d i r e c t l y   t o   t h e   d i s c o v e r y   o f   t h a t   c o n t i n e n t - - s p r i n g i n g   a t   o n e   b o u n d   f r o m   t h e   k n o w n   t o   t h e   u n k n o w n .   W h e r e a s ,   t h e   d r e a m   o f   C o l u m b u s ' s   l i f e   w a s   t o   m a k e   h i s   w a y   b y   a n   u n k n o w n   r o u t e   t o   w h a t   w a s   k n o w n ,   o r   t o   w h a t   h e   c o n s i d e r e d   t o   b e   k n o w n .   H e   w i s h e d   t o   f i n d   o u t   a n   e a s y   p a t h w a y   t o   t h e   t e r r i t o r i e s   o f   K u b l a i   K h a n ,   o r   P r e s t e r  - J o h n .   
 N e i t h e r   w e r e   h i s   m o t i v e s   s u c h   a s   h a v e   b e e n   g e n e r a l l y   s u p p o s e d .   T h e y   w e r e ,   f o r   t h e   m o s t   p a r t ,   p u r e l y   r e l i g i o u s .   W i t h   t h e   g o l d   g a i n e d   f r o m   p o t e n t a t e s   s u c h   a s   K u b l a i   K h a n ,   t h e   H o l y   S e p u l c h r e   w a s   t o   b e   r e b u i l t ,   a n d   t h e   C a t h o l i c   
  	 P R E F A C E . 	 i x   
 F a i t h   w a s   t o   b e   s p r e a d   o v e r   t h e   r e m o t e s t   p a r t s   o f   t h e   e a r t h .   
 C o l u m b u s   h a d   a l l   t h e   s p i r i t   o f   a   c r u s a d e r ,   a n d ,   a t   t h e   s a m e   t i m e ,   t h e   i n v e s t i g a t i n g   n a t u r e   o f   a   m o d e r n   m a n   o f   s c i e n c e .   T h e   A r a b s   h a v e   a   p r o  v e r b   t h a t   a   m a n   i s   m o r e   t h e   s o n   o f   t h e   a g e   i n   w h i c h   h e   l i v e s   t h a n   o f   h i s   o w n   f a t h e r .   T h i s   w a s   n o t   s o   w i t h   C o l u m b u s ;   h e   h a r d l y   s e e m s   t o   b e l o n g   a t   a l l   t o   h i s   a g e .   A t   a   t i m e   w h e n   t h e r e   w a s   n e v e r   m o r e   o f   w o r l d l i n e s s   a n d   s e l f - s e e k i n g ;   w h e n   A l e x a n d e r   B o r g i a   w a s   P o p e ;   w h e n   L o u i s   t h e   E l e v e n t h   r e i g n e d   i n   F r a n c e ,   H e n r y   t h e   S e  v e n t h   i n   E n g l a n d ,   a n d   F e r d i n a n d   t h e   C a t h o l i c   i n   A r r a g o n   a n d   C a s t i l l e - - a b o u t   t h e   t h r e e   l a s t   m e n   i n   t h e   w o r l d   t o   b e c o m e   c r u s a d e r s - - C o l u m  b u s   w a s   p e n e t r a t e d   w i t h   t h e   i d e a s   o f   t h e   t w e l f t h   c e n t u r y ,   a n d   w o u l d   h a v e   b e e n   a   w o r t h y   c o m  p a n i o n   o f   S a i n t   L o u i s   i n   t h a t   p i o u s   k i n g ' s   c r u  s a d e .   
 A g a i n ,   a t   a   t i m e   w h e n   A r i s t o t l e   a n d   " t h e   A n g e l i c   D o c t o r "   r u l e d   t h e   m i n d s   o f   m e n   w i t h   a n   a l m o s t   u n e x a m p l e d   t y r a n n y :   w h e n   s c i e n c e   w a s   m o r e   d o g m a t i c   t h a n   t h e o l o g y ;   w h e n   i t   w a s   t h o u g h t   a   s u f f i c i e n t   a n d   s a t i s f a c t o r y   e x p l a n a t i o n   t o   s a y   t h a t   b o d i e s   f a l l i n g   t o   t h e   e a r t h   d e s c e n d e d   b e c a u s e   i t   i s    x   	 P R E F A C E   
 t h e i r   n a t u r e   t o   d e s c e n d - - C o l u m b u s   r e g a r d e d   n a t u r a l   p h e n o m e n a   w i t h   t h e   s p i r i t   o f   i n d u c t i v e   p h i l o s o p h y   t h a t   w o u l d   b e l o n g   t o   a   f o l l o w e r   o f   L o r d   B a c o n .   
 P e r h a p s   i t   w i l l   b e   f o u n d   t h a t   a   v e r y   g r e a t   m a n   s e l d o m   d o e s   b e l o n g   t o   h i s   p e r i o d ,   a s   o t h e r   m e n   d o   t o   t h e i r s .   M a c h i a v e l l i *   s a y s   t h a t   t h e   w a y   t o   r e n o v a t e   s t a t e s   i s   a l w a y s   t o   g o   b a c k   t o   f i r s t   p r i n c i p l e s ,   e s p e c i a l l y   t o   t h e   f i r s t   p r i n c i p l e s   u p o n   w h i c h   t h o s e   s t a t e s   w e r e   f o u n d e d .   T h e   s a m e   l a w ,   i f   l a w   i t   b e ,   m a y   h o l d   g o o d   a s   r e g a r d s   t h e   r e n o v a t i o n   o f   a n y   s c i e n c e ,   a r t ,   o r   m o d e   o f   h u m a n   a c t i o n .   T h e   m a n   w h o   i s   t o o   c l o s e l y   u n i t e d   i n   t h o u g h t   a n d   f e e l i n g   w i t h   h i s   o w n   a g e ,   i s   s e l d o m   t h e   m a n   i n c l i n e d   t o   g o   b a c k   t o   t h e s e   f i r s t   p r i n c i p l e s .   
 I t   i s   v e r y   n o t i c e a b l e   i n   C o l u m b u s   t h a t   h e   w a s   i t   m o s t   d u t i f u l ,   u n s w e r v i n g ,   a n d   u n - i n q u i r i n g   s o n   o f   t h e   C h u r c h .   T h e   s a m e   m a n   w h o   w o u l d   h a v e   t a k e n   n o t h i n g   f o r   g r a n t e d   i n   s c i e n t i f i c   r e s e a r c h ,   a n d   w o u l d   n o t   h a v e   h e l d   h i m s e l f   b o u n d   b y   t h e   a u t h o r i t y   o f   t h e   g r e a t e s t   n a m e s   i n   s c i e n c e ,   n e v e r   
 
 *   M a c h i a v e l l i   w a s   c o n t e m p o r a r y   w i t h   C o l u m b u s .   N o   t w o   m e n   c o u l d   h a v e   b e e n   m o r e   d i s s i m i l a r ;   a n d   M a c h i a  v e l l i   w a s   t h o r o u g h l y   a   p r o d u c t   o f   h i s   a g e ,   a n d   a   m a n   w h o   e n t i r e l y   b e l o n g e d   t o   i t . 
  	 P R E F A C E .   	 x i 
 v e n t u r e d   f o r   a   m o m e n t   t o   t r u s t   h i m s e l f   a s   a   d i s c o v e r e r   o n   t h e   p e r i l o u s   s e a   o f   t h e o l o g i c a l   i n v e s  t i g a t i o n .   
 I n   t h i s   r e s p e c t   L a s   C a s a s ,   t h o u g h   a   c h u r c h m a n ,   w a s   v e r y   d i f f e r e n t   f r o m   C o l u m b u s .   S u c h   d o c t r i n e s   a s   t h a t   t h e   I n d i a n s   s h o u l d   b e   s o m e w h a t   c i v i l i z e d   b e f o r e   b e i n g   c o n v e r t e d ,   a n d   t h a t   e v e n   b a p t i s m   m i g h t   b e   p o s t p o n e d   t o   i n s t r u c t i o n , - - d o c t r i n e s   t h a t   w o u l d   h a v e   f o u n d   a   r e a d y   a c c e p t  a n c e   f r o m   t h e   g o o d   b i s h o p - - w o u l d   h a v e   m e t   w i t h   s m a l l   r e s p o n s e   f r o m   t h e   s o l d i e r l y   t h e o l o g y   o f   C o l u m b u s .   
 T h e   w h o l e   l i f e   o f   C o l u m b u s   s h o w s   h o w   r a r e l y   m e n   o f   t h e   g r e a t e s t   i n s i g h t   a n d   f o r e s i g h t ,   a n d   a l s o   o f   t h e   g r e a t e s t   p e r s e v e r a n c e ,   a t t a i n   t h e   e x a c t   e n d s   t h e y   a i m   a t .   I n   t h i s   r e s p e c t   a l l   s u c h   m e n   p a r t a k e   t h e   c a r e e r   o f   t h e   a l c h e m i s t s ,   w h o   d i d   n o t   t r a n s m u t e   o t h e r   m e t a l s   i n t o   g o l d ,   b u t   m a d e   v a l u a b l e   d i s c o v e r i e s   i n   c h e m i s t r y .   S o ,   w i t h   C o l u m b u s .   H e   d i d   n o t   r e b u i l d   t h e   H o l y   S e p u l c h r e ;   h e   d i d   n o t   l e a d   a   n e w   c r u s a d e ;   h e   d i d   n o t   f i n d   h i s   K u b l a i   K h a n ,   o r   h i s   P r e s t e r   J o h n ;   b u t   h e   b r o u g h t   i n t o   r e l a t i o n   t h e   N e w   W o r l d   a n d   t h e   O l d .   
 I t   i s   i m p o s s i b l e   t o   r e a d   w i t h o u t   t h e   d e e p e s t   
  x i i   	 P R E F A C E .   
 i n t e r e s t   t h e   a c c o u n t   f r o m   d a y   t o   d a y   o f   h i s   v o y  a g e s .   I t   h a s   a l w a y s   b e e n   a   f a v o u r i t e   s p e c u l a t i o n   w i t h   h i s t o r i a n s ,   a n d ,   i n d e e d ,   w i t h   a l l   t h i n k i n g   m e n ,   t o   c o n s i d e r   w h a t   w o u l d   h a v e   h a p p e n e d   f r o m   a   s l i g h t   c h a n g e   o f   c i r c u m s t a n c e s   i n   t h e   c o u r s e   o f   t h i n g s   w h i c h   l e d   t o   g r e a t   e v e n t s .   T h i s   m a y   b e   a n   i d l e   a n d   a   u s e l e s s   s p e c u l a t i o n ,   b u t   i t   i s   a n   i n e v i t a b l e   o n e .   N e v e r   w a s   t h e r e   s u c h   a   f i e l d   f o r   t h i s   k i n d   o f   s p e c u l a t i o n   a s   i n   t h e   v o y a g e s ,   e s p e c i a l l y   t h e   f i r s t   o n e ,   o f   C o l u m b u s .   T h e   f i r s t   p o i n t   o f   l a n d   t h a t   h e   s a w ,   a n d   l a n d e d   a t ,   i s   a s   n e a r l y   a s   p o s s i b l e   t h e   c e n t r a l   p o i n t   o f   w h a t   m u s t   o n c e   h a v e   b e e n   t h e   U n i t e d   C o n t i n e n t   o f   N o r t h   a n d   S o u t h   A m e r i c a .   T h e   l e a s t   c h a n g e   o f   c i r c u m s t a n c e   m i g h t   h a v e   m a d e   a n   i m m e n s e   d i f f e r e n c e   i n   t h e   r e s u l t .   T h e   g o i n g   t o   s l e e p   o f   t h e   h e l m s m a n ,   t h e   u n s h i p p i n g   o f   t h e   r u d d e r ,   ( w h i c h   d i d   o c c u r   i n   t h e   c a s e   o f   " T h e   P i n z o n , " )   t h e   s l i g h t e s t   m i s t a k e   i n   t a k i n g   a n   o b  s e r v a t i o n ,   m i g h t   h a v e   m a d e ,   a n d   p r o b a b l y   d i d   m a k e ,   c o n s i d e r a b l e   c h a n g e   i n   t h e   e v e n t .   D u r i n g   t h a t   m e m o r a b l e   f i r s t   v o y a g e   o f   C o l u m b u s ,   t h e   g e n t l e s t   b r e e z e   c a r r i e d   w i t h   i t   t h e   d e s t i n i e s   o f   f u t u r e   e m p i r e s .   H a d   h e   m a d e   h i s   f i r s t   d i s c o v e r y   o f   l a n d   a t   a   p o i n t   m u c h   s o u t h w a r d   o f   t h a t   w h i c h   h e   d i d   d i s c o v e r ,   S o u t h   A m e r i c a   m i g h t   h a v e   b e e n   
  	 P R E F A C E .   	 x i i i   
 c o l o n i z e d   b y   t h e   S p a n i a r d s   w i t h   a l l   t h e   v i g o u r   t h a t   b e l o n g e d   t o   t h e i r   f i r s t   e f f o r t s   a t   c o l o n i z a t i o n ;   a n d ,   b e i n g   a   c o n t i n e n t ,   m i g h t   n o t   a f t e r w a r d s   h a v e   b e e n   s o   e a s i l y   w r e s t e d   f r o m   t h e i r   s w a y   b y   t h e   m a r i t i m e   n a t i o n s .   
 O n   t h e   o t h e r   h a n d ,   h a d   s o m e   b r e e z e ,   b i g   w i t h   t h e   f a t e   o f   n a t i o n s ,   c a r r i e d   C o l u m b u s   n o r t h w a r d s ,   i t   w o u l d   h a r d l y   h a v e   b e e n   l e f t   f o r   t h e   E n g l i s h ,   m o r e   t h a n   a   c e n t u r y   a f t e r w a r d s ,   t o   f o u n d   t h o s e   C o l o n i e s   w h i c h   h a v e   p r o v e d   t o   b e   t h e   s e e d s   o f   t h e   g r e a t e s t   n a t i o n   t h a t   t h e   w o r l d   i s   l i k e l y   t o   b e h o l d .   
 I t   w a s ,   h u m a n l y   s p e a k i n g ,   s i n g u l a r l y   u n f o r  t u n a t e   f o r   S p a n i s h   d o m i n i o n   i n   A m e r i c a ,   t h a t   t h e   e a r l i e s t   d i s c o v e r i e s   o f   t h e   S p a n i a r d s   w e r e   t h o s e   o f   t h e   W e s t   I n d i a   I s l a n d s .   A   m u l t i p l i c i t y   o f   g o  v e r n o r s   i n t r o d u c e d   c o n f u s i o n ,   f e e b l e n e s s ,   a n d   w a n t   o f   s y s t e m ,   i n t o   c o l o n i a l   g o v e r n m e n t .   T h e   n u m b e r s ,   c o m p a r a t i v e l y   f e w ,   o f   t h e   o r i g i n a l   i n h a  b i t a n t s   i n   e a c h   i s l a n d ,   w e r e   r a p i d l y   r e m o v e d   f r o m   t h e   s c e n e   o f   a c t i o n ;   a n d   t h e   S p a n i a r d s   l a c k e d ,   a t   t h e   b e g i n n i n g ,   t h a t   c o m p r e s s i n g   f o r c e   w h i c h   w o u l d   h a v e   b e e n   f o u n d   i n   t h e   e x i s t e n c e   o f   a   b o d y   o f   n a t i v e s   w h o   c o u l d   n o t   h a v e   b e e n    x i v   	 P R E F A C E . 
 r e m o v e d   b y   t h e   o u t r a g e s   o f   S p a n i s h   c r u e l t y ,   t h e   s t r e n g t h   o f   S p a n i s h   l i q u o r s ,   o r   t h e   v i r u l e n c e   o f   S p a n i s h   d i s e a s e s . *   
 T h e   M o n a r c h s   o f   S p a i n ,   t o o ,   w o u l d   h a v e   b e e n   c o m p e l l e d   t o   t r e a t   t h e i r   n e w   d i s c o v e r i e s   a n d   c o n  q u e s t s   m o r e   s e r i o u s l y .   T o   h a v e   h e l d   t h e   c o u n t r y   a t   a l l ,   t h e y   m u s t   h a v e   h e l d   i t   w e l l .   I t   w o u l d   n o t   h a v e   b e e n   O v a n d o s ,   B o b a d i l l a s ,   N i c u e s a s   a n d   O j e d a s   w h o   c o u l d   h a v e   b e e n   e m p l o y e d   t o   g o  v e r n ,   d i s c o v e r ,   c o n q u e r ,   c o l o n i z e - - a n d   r u i n   b y   t h e i r   f o l l y - - t h e   S p a n i s h   p o s s e s s i o n s   i n   t h e   I n d i e s .   T h e   w o r k   o f   d i s c o v e r y   a n d   c o n q u e s t ,   b e g u n   b y   C o l u m b u s ,   m u s t   t h e n   h a v e   b e e n   e n t r u s t e d   t o   m e n   l i k e   C o r t e s ,   t h e   P i z a r r o s ,   V a s c o   N u n e z ,   o r   t h e   P r e s i d e n t   G a s c a ;   a n d   a   c o l o n y   o r   a   k i n g d o m   f o u n d e d   b y   a n y   o f   t h e s e   m e n   m i g h t   w e l l   h a v e   r e m a i n e d   a   g r e a t   c o l o n y ,   o r   a   g r e a t   k i n g d o m ,   t o   t h e   p r e s e n t   d a y .   
 A R T H U R   H E L P S .   
 L o n d o n ,   O c t o b e r ,   1 8 6 8 . 
 *   T h e   s m a l l p o x ,   f o r   i n s t a n c e ,   w a s   a   d i s e a s e   i n t r o d u c e d   b y   t h e   S p a n i a r d s ,   w h i c h   t h e   c o m p a r a t i v e l y   f e e b l e   c o n s t i t u t i o n   o f   t h e   I n d i a n s   c o u l d   n o t   w i t h s t a n d . 
 
 
 X 
anonymous,o1|root=map, java.lang.Object
anonymous,global|root:first=object, org.archive.settings.path.Foo
default|root:first:eight=biginteger, 8
default|root:first:eleven=pattern, ^11$
default|root:first:five=int, 5
default|root:first:four=float, 4.0
default|root:first:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:first:nine=bigdecimal, 9.0
default|root:first:one=byte, 1
default|root:first:seven=short, 7
default|root:first:six=long, 6
o1|root:first:ten=string, three plus seven
default|root:first:three=double, 3.0
default|root:first:twelve=file, /12
default|root:first:two=char, 2
default|root:first:zero=boolean, false
anonymous,global|root:primary=primary, org.archive.settings.path.Foo
default|root:primary:eight=biginteger, 8
default|root:primary:eleven=pattern, ^11$
default|root:primary:five=int, 5
default|root:primary:four=float, 4.0
default|root:primary:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:primary:nine=bigdecimal, 9.0
default|root:primary:one=byte, 1
default|root:primary:seven=short, 7
default|root:primary:six=long, 6
default|root:primary:ten=string, ten
default|root:primary:three=double, 3.0
default|root:primary:twelve=file, /12
default|root:primary:two=char, 2
default|root:primary:zero=boolean, false
anonymous,o1|root:second=object, org.archive.settings.path.Foo
default|root:second:eight=biginteger, 8
default|root:second:eleven=pattern, ^11$
default|root:second:five=int, 5
default|root:second:four=float, 4.0
default|root:second:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:second:nine=bigdecimal, 9.0
default|root:second:one=byte, 1
default|root:second:seven=short, 7
default|root:second:six=long, 6
default|root:second:ten=string, ten
default|root:second:three=double, 3.0
default|root:second:twelve=file, /12
default|root:second:two=char, 2
default|root:second:zero=boolean, false
anonymous,global|root:bar=object, org.archive.settings.path.Bar
global|root:bar:foo=object, org.archive.settings.path.Foo
default|root:bar:foo:eight=biginteger, 8
default|root:bar:foo:eleven=pattern, ^11$
default|root:bar:foo:five=int, 5
default|root:bar:foo:four=float, 4.0
default|root:bar:foo:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:foo:nine=bigdecimal, 9.0
default|root:bar:foo:one=byte, 1
default|root:bar:foo:seven=short, 7
default|root:bar:foo:six=long, 6
default|root:bar:foo:ten=string, ten
default|root:bar:foo:three=double, 3.0
default|root:bar:foo:twelve=file, /12
default|root:bar:foo:two=char, 2
default|root:bar:foo:zero=boolean, false
default|root:bar:foo-auto=auto, root:primary
anonymous,global|root:bar:list=list, org.archive.settings.path.Foo
anonymous,global|root:bar:list:0=object, org.archive.settings.path.Foo
default|root:bar:list:0:eight=biginteger, 8
default|root:bar:list:0:eleven=pattern, ^11$
default|root:bar:list:0:five=int, 5
default|root:bar:list:0:four=float, 4.0
default|root:bar:list:0:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:0:nine=bigdecimal, 9.0
default|root:bar:list:0:one=byte, 1
default|root:bar:list:0:seven=short, 7
default|root:bar:list:0:six=long, 6
default|root:bar:list:0:ten=string, ten
default|root:bar:list:0:three=double, 3.0
default|root:bar:list:0:twelve=file, /12
default|root:bar:list:0:two=char, 2
default|root:bar:list:0:zero=boolean, false
anonymous,global|root:bar:list:1=object, org.archive.settings.path.Foo
default|root:bar:list:1:eight=biginteger, 8
default|root:bar:list:1:eleven=pattern, ^11$
default|root:bar:list:1:five=int, 5
default|root:bar:list:1:four=float, 4.0
default|root:bar:list:1:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:1:nine=bigdecimal, 9.0
default|root:bar:list:1:one=byte, 1
default|root:bar:list:1:seven=short, 7
default|root:bar:list:1:six=long, 6
default|root:bar:list:1:ten=string, ten
default|root:bar:list:1:three=double, 3.0
default|root:bar:list:1:twelve=file, /12
default|root:bar:list:1:two=char, 2
default|root:bar:list:1:zero=boolean, false
anonymous,global|root:bar:list:2=object, org.archive.settings.path.Foo
default|root:bar:list:2:eight=biginteger, 8
default|root:bar:list:2:eleven=pattern, ^11$
default|root:bar:list:2:five=int, 5
default|root:bar:list:2:four=float, 4.0
default|root:bar:list:2:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:2:nine=bigdecimal, 9.0
default|root:bar:list:2:one=byte, 1
default|root:bar:list:2:seven=short, 7
default|root:bar:list:2:six=long, 6
default|root:bar:list:2:ten=string, ten
default|root:bar:list:2:three=double, 3.0
default|root:bar:list:2:twelve=file, /12
default|root:bar:list:2:two=char, 2
default|root:bar:list:2:zero=boolean, false
anonymous,o1|root:bar:list:3=object, org.archive.settings.path.Foo
default|root:bar:list:3:eight=biginteger, 8
default|root:bar:list:3:eleven=pattern, ^11$
default|root:bar:list:3:five=int, 5
default|root:bar:list:3:four=float, 4.0
default|root:bar:list:3:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:3:nine=bigdecimal, 9.0
default|root:bar:list:3:one=byte, 1
default|root:bar:list:3:seven=short, 7
default|root:bar:list:3:six=long, 6
default|root:bar:list:3:ten=string, ten
default|root:bar:list:3:three=double, 3.0
default|root:bar:list:3:twelve=file, /12
default|root:bar:list:3:two=char, 2
default|root:bar:list:3:zero=boolean, false
anonymous,o1|root:bar:list:4=object, org.archive.settings.path.Foo
default|root:bar:list:4:eight=biginteger, 8
default|root:bar:list:4:eleven=pattern, ^11$
default|root:bar:list:4:five=int, 5
default|root:bar:list:4:four=float, 4.0
default|root:bar:list:4:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:4:nine=bigdecimal, 9.0
default|root:bar:list:4:one=byte, 1
default|root:bar:list:4:seven=short, 7
default|root:bar:list:4:six=long, 6
default|root:bar:list:4:ten=string, ten
default|root:bar:list:4:three=double, 3.0
default|root:bar:list:4:twelve=file, /12
default|root:bar:list:4:two=char, 2
default|root:bar:list:4:zero=boolean, false
anonymous,o2|root:bar:list:5=object, org.archive.settings.path.Foo
default|root:bar:list:5:eight=biginteger, 8
default|root:bar:list:5:eleven=pattern, ^11$
default|root:bar:list:5:five=int, 5
default|root:bar:list:5:four=float, 4.0
default|root:bar:list:5:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:5:nine=bigdecimal, 9.0
default|root:bar:list:5:one=byte, 1
default|root:bar:list:5:seven=short, 7
default|root:bar:list:5:six=long, 6
default|root:bar:list:5:ten=string, ten
default|root:bar:list:5:three=double, 3.0
default|root:bar:list:5:twelve=file, /12
default|root:bar:list:5:two=char, 2
default|root:bar:list:5:zero=boolean, false
anonymous,o2|root:bar:list:6=object, org.archive.settings.path.Foo
default|root:bar:list:6:eight=biginteger, 8
default|root:bar:list:6:eleven=pattern, ^11$
default|root:bar:list:6:five=int, 5
default|root:bar:list:6:four=float, 4.0
default|root:bar:list:6:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:6:nine=bigdecimal, 9.0
default|root:bar:list:6:one=byte, 1
default|root:bar:list:6:seven=short, 7
default|root:bar:list:6:six=long, 6
default|root:bar:list:6:ten=string, ten
default|root:bar:list:6:three=double, 3.0
default|root:bar:list:6:twelve=file, /12
default|root:bar:list:6:two=char, 2
default|root:bar:list:6:zero=boolean, false
anonymous,o1|root:bar:map=map, org.archive.settings.path.Foo
anonymous,global|root:bar:map:a=object, org.archive.settings.path.Foo
default|root:bar:map:a:eight=biginteger, 8
default|root:bar:map:a:eleven=pattern, ^11$
default|root:bar:map:a:five=int, 5
default|root:bar:map:a:four=float, 4.0
default|root:bar:map:a:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:a:nine=bigdecimal, 9.0
default|root:bar:map:a:one=byte, 1
default|root:bar:map:a:seven=short, 7
default|root:bar:map:a:six=long, 6
default|root:bar:map:a:ten=string, ten
default|root:bar:map:a:three=double, 3.0
default|root:bar:map:a:twelve=file, /12
default|root:bar:map:a:two=char, 2
default|root:bar:map:a:zero=boolean, false
anonymous,o1|root:bar:map:b=object, org.archive.settings.path.Baz
default|root:bar:map:b:eight=biginteger, 8
default|root:bar:map:b:eleven=pattern, ^11$
default|root:bar:map:b:five=int, 5
default|root:bar:map:b:four=float, 4.0
default|root:bar:map:b:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:b:nine=bigdecimal, 9.0
default|root:bar:map:b:one=byte, 1
default|root:bar:map:b:seven=short, 7
default|root:bar:map:b:six=long, 6
default|root:bar:map:b:ten=string, ten
default|root:bar:map:b:three=double, 3.0
default|root:bar:map:b:twelve=file, /12
default|root:bar:map:b:two=char, 2
default|root:bar:map:b:zero=boolean, false
anonymous,global|root:bar:map:c=object, org.archive.settings.path.Foo
default|root:bar:map:c:eight=biginteger, 8
default|root:bar:map:c:eleven=pattern, ^11$
default|root:bar:map:c:five=int, 5
default|root:bar:map:c:four=float, 4.0
default|root:bar:map:c:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:c:nine=bigdecimal, 9.0
default|root:bar:map:c:one=byte, 1
default|root:bar:map:c:seven=short, 7
default|root:bar:map:c:six=long, 6
default|root:bar:map:c:ten=string, ten
default|root:bar:map:c:three=double, 3.0
default|root:bar:map:c:twelve=file, /12
default|root:bar:map:c:two=char, 2
default|root:bar:map:c:zero=boolean, false
anonymous,o2|root:bar:map:e=object, org.archive.settings.path.Foo
default|root:bar:map:e:eight=biginteger, 8
default|root:bar:map:e:eleven=pattern, ^11$
default|root:bar:map:e:five=int, 5
default|root:bar:map:e:four=float, 4.0
default|root:bar:map:e:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:e:nine=bigdecimal, 9.0
default|root:bar:map:e:one=byte, 1
default|root:bar:map:e:seven=short, 7
default|root:bar:map:e:six=long, 6
default|root:bar:map:e:ten=string, ten
default|root:bar:map:e:three=double, 3.0
default|root:bar:map:e:twelve=file, /12
default|root:bar:map:e:two=char, 2
default|root:bar:map:e:zero=boolean, false
anonymous,o1|root:bar:map:d=object, org.archive.settings.path.Foo
default|root:bar:map:d:eight=biginteger, 8
default|root:bar:map:d:eleven=pattern, ^11$
default|root:bar:map:d:five=int, 5
default|root:bar:map:d:four=float, 4.0
default|root:bar:map:d:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:d:nine=bigdecimal, 9.0
default|root:bar:map:d:one=byte, 1
default|root:bar:map:d:seven=short, 7
default|root:bar:map:d:six=long, 6
default|root:bar:map:d:ten=string, ten
default|root:bar:map:d:three=double, 3.0
default|root:bar:map:d:twelve=file, /12
default|root:bar:map:d:two=char, 2
default|root:bar:map:d:zero=boolean, false
anonymous,global|root:bar:slist=list, java.lang.String
anonymous,global|root:bar:slist:0=string, zero
anonymous,global|root:bar:slist:1=string, one
anonymous,global|root:bar:slist:2=string, two
anonymous,o1|root:bar:slist:3=string, three
anonymous,o1|root:bar:slist:4=string, four
anonymous,o2|root:bar:slist:5=string, three o2
anonymous,o2|root:bar:slist:6=string, four o2
anonymous,global|root:bar:smap=map, java.lang.String
anonymous,global|root:bar:smap:a=string, 65
anonymous,global|root:bar:smap:b=string, 66
anonymous,global|root:bar:smap:c=string, 67global|root=map, java.lang.Object
global|root:first=object, org.archive.settings.path.Foo
global|root:primary=primary, org.archive.settings.path.Foo
global|root:second=object, org.archive.settings.path.Foo
global|root:bar=object, org.archive.settings.path.Bar
global|root:bar:foo=object, org.archive.settings.path.Foo
global|root:bar:list=list, org.archive.settings.path.Foo
global|root:bar:list:0=object, org.archive.settings.path.Foo
global|root:bar:list:1=object, org.archive.settings.path.Foo
global|root:bar:list:2=object, org.archive.settings.path.Foo
global|root:bar:map=map, org.archive.settings.path.Foo
global|root:bar:map:a=object, org.archive.settings.path.Foo
global|root:bar:map:b=object, org.archive.settings.path.Foo
global|root:bar:map:b:five=int, 50000
global|root:bar:map:c=object, org.archive.settings.path.Foo
global|root:bar:slist=list, java.lang.String
global|root:bar:slist:0=string, zero
global|root:bar:slist:1=string, one
global|root:bar:slist:2=string, two
global|root:bar:smap=map, java.lang.String
global|root:bar:smap:a=string, 65
global|root:bar:smap:b=string, 66
global|root:bar:smap:c=string, 67global|root=map, java.lang.Object
global|root:first=object, org.archive.settings.path.Foo
default|root:first:eight=biginteger, 8
default|root:first:eleven=pattern, ^11$
default|root:first:five=int, 5
default|root:first:four=float, 4.0
default|root:first:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:first:nine=bigdecimal, 9.0
default|root:first:one=byte, 1
default|root:first:seven=short, 7
default|root:first:six=long, 6
default|root:first:ten=string, ten
default|root:first:three=double, 3.0
default|root:first:twelve=file, /12
default|root:first:two=char, 2
default|root:first:zero=boolean, false
global|root:primary=primary, org.archive.settings.path.Foo
default|root:primary:eight=biginteger, 8
default|root:primary:eleven=pattern, ^11$
default|root:primary:five=int, 5
default|root:primary:four=float, 4.0
default|root:primary:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:primary:nine=bigdecimal, 9.0
default|root:primary:one=byte, 1
default|root:primary:seven=short, 7
default|root:primary:six=long, 6
default|root:primary:ten=string, ten
default|root:primary:three=double, 3.0
default|root:primary:twelve=file, /12
default|root:primary:two=char, 2
default|root:primary:zero=boolean, false
global|root:second=object, org.archive.settings.path.Foo
default|root:second:eight=biginteger, 8
default|root:second:eleven=pattern, ^11$
default|root:second:five=int, 5
default|root:second:four=float, 4.0
default|root:second:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:second:nine=bigdecimal, 9.0
default|root:second:one=byte, 1
default|root:second:seven=short, 7
default|root:second:six=long, 6
default|root:second:ten=string, ten
default|root:second:three=double, 3.0
default|root:second:twelve=file, /12
default|root:second:two=char, 2
default|root:second:zero=boolean, false
global|root:bar=object, org.archive.settings.path.Bar
global|root:bar:foo=object, org.archive.settings.path.Foo
default|root:bar:foo:eight=biginteger, 8
default|root:bar:foo:eleven=pattern, ^11$
default|root:bar:foo:five=int, 5
default|root:bar:foo:four=float, 4.0
default|root:bar:foo:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:foo:nine=bigdecimal, 9.0
default|root:bar:foo:one=byte, 1
default|root:bar:foo:seven=short, 7
default|root:bar:foo:six=long, 6
default|root:bar:foo:ten=string, ten
default|root:bar:foo:three=double, 3.0
default|root:bar:foo:twelve=file, /12
default|root:bar:foo:two=char, 2
default|root:bar:foo:zero=boolean, false
default|root:bar:foo-auto=auto, root:primary
global|root:bar:list=list, org.archive.settings.path.Foo
global|root:bar:list:0=object, org.archive.settings.path.Foo
default|root:bar:list:0:eight=biginteger, 8
default|root:bar:list:0:eleven=pattern, ^11$
default|root:bar:list:0:five=int, 5
default|root:bar:list:0:four=float, 4.0
default|root:bar:list:0:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:0:nine=bigdecimal, 9.0
default|root:bar:list:0:one=byte, 1
default|root:bar:list:0:seven=short, 7
default|root:bar:list:0:six=long, 6
default|root:bar:list:0:ten=string, ten
default|root:bar:list:0:three=double, 3.0
default|root:bar:list:0:twelve=file, /12
default|root:bar:list:0:two=char, 2
default|root:bar:list:0:zero=boolean, false
global|root:bar:list:1=object, org.archive.settings.path.Foo
default|root:bar:list:1:eight=biginteger, 8
default|root:bar:list:1:eleven=pattern, ^11$
default|root:bar:list:1:five=int, 5
default|root:bar:list:1:four=float, 4.0
default|root:bar:list:1:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:1:nine=bigdecimal, 9.0
default|root:bar:list:1:one=byte, 1
default|root:bar:list:1:seven=short, 7
default|root:bar:list:1:six=long, 6
default|root:bar:list:1:ten=string, ten
default|root:bar:list:1:three=double, 3.0
default|root:bar:list:1:twelve=file, /12
default|root:bar:list:1:two=char, 2
default|root:bar:list:1:zero=boolean, false
global|root:bar:list:2=object, org.archive.settings.path.Foo
default|root:bar:list:2:eight=biginteger, 8
default|root:bar:list:2:eleven=pattern, ^11$
default|root:bar:list:2:five=int, 5
default|root:bar:list:2:four=float, 4.0
default|root:bar:list:2:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:2:nine=bigdecimal, 9.0
default|root:bar:list:2:one=byte, 1
default|root:bar:list:2:seven=short, 7
default|root:bar:list:2:six=long, 6
default|root:bar:list:2:ten=string, ten
default|root:bar:list:2:three=double, 3.0
default|root:bar:list:2:twelve=file, /12
default|root:bar:list:2:two=char, 2
default|root:bar:list:2:zero=boolean, false
global|root:bar:map=map, org.archive.settings.path.Foo
global|root:bar:map:a=object, org.archive.settings.path.Foo
default|root:bar:map:a:eight=biginteger, 8
default|root:bar:map:a:eleven=pattern, ^11$
default|root:bar:map:a:five=int, 5
default|root:bar:map:a:four=float, 4.0
default|root:bar:map:a:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:a:nine=bigdecimal, 9.0
default|root:bar:map:a:one=byte, 1
default|root:bar:map:a:seven=short, 7
default|root:bar:map:a:six=long, 6
default|root:bar:map:a:ten=string, ten
default|root:bar:map:a:three=double, 3.0
default|root:bar:map:a:twelve=file, /12
default|root:bar:map:a:two=char, 2
default|root:bar:map:a:zero=boolean, false
global|root:bar:map:b=object, org.archive.settings.path.Foo
default|root:bar:map:b:eight=biginteger, 8
default|root:bar:map:b:eleven=pattern, ^11$
global|root:bar:map:b:five=int, 50000
default|root:bar:map:b:four=float, 4.0
default|root:bar:map:b:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:b:nine=bigdecimal, 9.0
default|root:bar:map:b:one=byte, 1
default|root:bar:map:b:seven=short, 7
default|root:bar:map:b:six=long, 6
default|root:bar:map:b:ten=string, ten
default|root:bar:map:b:three=double, 3.0
default|root:bar:map:b:twelve=file, /12
default|root:bar:map:b:two=char, 2
default|root:bar:map:b:zero=boolean, false
global|root:bar:map:c=object, org.archive.settings.path.Foo
default|root:bar:map:c:eight=biginteger, 8
default|root:bar:map:c:eleven=pattern, ^11$
default|root:bar:map:c:five=int, 5
default|root:bar:map:c:four=float, 4.0
default|root:bar:map:c:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:c:nine=bigdecimal, 9.0
default|root:bar:map:c:one=byte, 1
default|root:bar:map:c:seven=short, 7
default|root:bar:map:c:six=long, 6
default|root:bar:map:c:ten=string, ten
default|root:bar:map:c:three=double, 3.0
default|root:bar:map:c:twelve=file, /12
default|root:bar:map:c:two=char, 2
default|root:bar:map:c:zero=boolean, false
global|root:bar:slist=list, java.lang.String
global|root:bar:slist:0=string, zero
global|root:bar:slist:1=string, one
global|root:bar:slist:2=string, two
global|root:bar:smap=map, java.lang.String
global|root:bar:smap:a=string, 65
global|root:bar:smap:b=string, 66
global|root:bar:smap:c=string, 67o1,global|root=map, java.lang.Object
o1|root:first:ten=string, three plus seven
o1|root:second=object, org.archive.settings.path.Foo
o1,global|root:bar:list=list, org.archive.settings.path.Foo
o1|root:bar:list:3=object, org.archive.settings.path.Foo
o1|root:bar:list:4=object, org.archive.settings.path.Foo
o1,global|root:bar:map=map, org.archive.settings.path.Foo
o1|root:bar:map:b=object, org.archive.settings.path.Baz
o1|root:bar:map:d=object, org.archive.settings.path.Foo
o1,global|root:bar:slist=list, java.lang.String
o1|root:bar:slist:3=string, three
o1|root:bar:slist:4=string, fouro1,global|root=map, java.lang.Object
global|root:first=object, org.archive.settings.path.Foo
default|root:first:eight=biginteger, 8
default|root:first:eleven=pattern, ^11$
default|root:first:five=int, 5
default|root:first:four=float, 4.0
default|root:first:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:first:nine=bigdecimal, 9.0
default|root:first:one=byte, 1
default|root:first:seven=short, 7
default|root:first:six=long, 6
o1|root:first:ten=string, three plus seven
default|root:first:three=double, 3.0
default|root:first:twelve=file, /12
default|root:first:two=char, 2
default|root:first:zero=boolean, false
global|root:primary=primary, org.archive.settings.path.Foo
default|root:primary:eight=biginteger, 8
default|root:primary:eleven=pattern, ^11$
default|root:primary:five=int, 5
default|root:primary:four=float, 4.0
default|root:primary:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:primary:nine=bigdecimal, 9.0
default|root:primary:one=byte, 1
default|root:primary:seven=short, 7
default|root:primary:six=long, 6
default|root:primary:ten=string, ten
default|root:primary:three=double, 3.0
default|root:primary:twelve=file, /12
default|root:primary:two=char, 2
default|root:primary:zero=boolean, false
o1|root:second=object, org.archive.settings.path.Foo
default|root:second:eight=biginteger, 8
default|root:second:eleven=pattern, ^11$
default|root:second:five=int, 5
default|root:second:four=float, 4.0
default|root:second:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:second:nine=bigdecimal, 9.0
default|root:second:one=byte, 1
default|root:second:seven=short, 7
default|root:second:six=long, 6
default|root:second:ten=string, ten
default|root:second:three=double, 3.0
default|root:second:twelve=file, /12
default|root:second:two=char, 2
default|root:second:zero=boolean, false
global|root:bar=object, org.archive.settings.path.Bar
global|root:bar:foo=object, org.archive.settings.path.Foo
default|root:bar:foo:eight=biginteger, 8
default|root:bar:foo:eleven=pattern, ^11$
default|root:bar:foo:five=int, 5
default|root:bar:foo:four=float, 4.0
default|root:bar:foo:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:foo:nine=bigdecimal, 9.0
default|root:bar:foo:one=byte, 1
default|root:bar:foo:seven=short, 7
default|root:bar:foo:six=long, 6
default|root:bar:foo:ten=string, ten
default|root:bar:foo:three=double, 3.0
default|root:bar:foo:twelve=file, /12
default|root:bar:foo:two=char, 2
default|root:bar:foo:zero=boolean, false
default|root:bar:foo-auto=auto, root:primary
o1,global|root:bar:list=list, org.archive.settings.path.Foo
global|root:bar:list:0=object, org.archive.settings.path.Foo
default|root:bar:list:0:eight=biginteger, 8
default|root:bar:list:0:eleven=pattern, ^11$
default|root:bar:list:0:five=int, 5
default|root:bar:list:0:four=float, 4.0
default|root:bar:list:0:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:0:nine=bigdecimal, 9.0
default|root:bar:list:0:one=byte, 1
default|root:bar:list:0:seven=short, 7
default|root:bar:list:0:six=long, 6
default|root:bar:list:0:ten=string, ten
default|root:bar:list:0:three=double, 3.0
default|root:bar:list:0:twelve=file, /12
default|root:bar:list:0:two=char, 2
default|root:bar:list:0:zero=boolean, false
global|root:bar:list:1=object, org.archive.settings.path.Foo
default|root:bar:list:1:eight=biginteger, 8
default|root:bar:list:1:eleven=pattern, ^11$
default|root:bar:list:1:five=int, 5
default|root:bar:list:1:four=float, 4.0
default|root:bar:list:1:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:1:nine=bigdecimal, 9.0
default|root:bar:list:1:one=byte, 1
default|root:bar:list:1:seven=short, 7
default|root:bar:list:1:six=long, 6
default|root:bar:list:1:ten=string, ten
default|root:bar:list:1:three=double, 3.0
default|root:bar:list:1:twelve=file, /12
default|root:bar:list:1:two=char, 2
default|root:bar:list:1:zero=boolean, false
global|root:bar:list:2=object, org.archive.settings.path.Foo
default|root:bar:list:2:eight=biginteger, 8
default|root:bar:list:2:eleven=pattern, ^11$
default|root:bar:list:2:five=int, 5
default|root:bar:list:2:four=float, 4.0
default|root:bar:list:2:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:2:nine=bigdecimal, 9.0
default|root:bar:list:2:one=byte, 1
default|root:bar:list:2:seven=short, 7
default|root:bar:list:2:six=long, 6
default|root:bar:list:2:ten=string, ten
default|root:bar:list:2:three=double, 3.0
default|root:bar:list:2:twelve=file, /12
default|root:bar:list:2:two=char, 2
default|root:bar:list:2:zero=boolean, false
o1|root:bar:list:3=object, org.archive.settings.path.Foo
default|root:bar:list:3:eight=biginteger, 8
default|root:bar:list:3:eleven=pattern, ^11$
default|root:bar:list:3:five=int, 5
default|root:bar:list:3:four=float, 4.0
default|root:bar:list:3:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:3:nine=bigdecimal, 9.0
default|root:bar:list:3:one=byte, 1
default|root:bar:list:3:seven=short, 7
default|root:bar:list:3:six=long, 6
default|root:bar:list:3:ten=string, ten
default|root:bar:list:3:three=double, 3.0
default|root:bar:list:3:twelve=file, /12
default|root:bar:list:3:two=char, 2
default|root:bar:list:3:zero=boolean, false
o1|root:bar:list:4=object, org.archive.settings.path.Foo
default|root:bar:list:4:eight=biginteger, 8
default|root:bar:list:4:eleven=pattern, ^11$
default|root:bar:list:4:five=int, 5
default|root:bar:list:4:four=float, 4.0
default|root:bar:list:4:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:list:4:nine=bigdecimal, 9.0
default|root:bar:list:4:one=byte, 1
default|root:bar:list:4:seven=short, 7
default|root:bar:list:4:six=long, 6
default|root:bar:list:4:ten=string, ten
default|root:bar:list:4:three=double, 3.0
default|root:bar:list:4:twelve=file, /12
default|root:bar:list:4:two=char, 2
default|root:bar:list:4:zero=boolean, false
o1,global|root:bar:map=map, org.archive.settings.path.Foo
global|root:bar:map:a=object, org.archive.settings.path.Foo
default|root:bar:map:a:eight=biginteger, 8
default|root:bar:map:a:eleven=pattern, ^11$
default|root:bar:map:a:five=int, 5
default|root:bar:map:a:four=float, 4.0
default|root:bar:map:a:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:a:nine=bigdecimal, 9.0
default|root:bar:map:a:one=byte, 1
default|root:bar:map:a:seven=short, 7
default|root:bar:map:a:six=long, 6
default|root:bar:map:a:ten=string, ten
default|root:bar:map:a:three=double, 3.0
default|root:bar:map:a:twelve=file, /12
default|root:bar:map:a:two=char, 2
default|root:bar:map:a:zero=boolean, false
o1|root:bar:map:b=object, org.archive.settings.path.Baz
default|root:bar:map:b:eight=biginteger, 8
default|root:bar:map:b:eleven=pattern, ^11$
default|root:bar:map:b:five=int, 5
default|root:bar:map:b:four=float, 4.0
default|root:bar:map:b:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:b:nine=bigdecimal, 9.0
default|root:bar:map:b:one=byte, 1
default|root:bar:map:b:seven=short, 7
default|root:bar:map:b:six=long, 6
default|root:bar:map:b:ten=string, ten
default|root:bar:map:b:three=double, 3.0
default|root:bar:map:b:twelve=file, /12
default|root:bar:map:b:two=char, 2
default|root:bar:map:b:zero=boolean, false
global|root:bar:map:c=object, org.archive.settings.path.Foo
default|root:bar:map:c:eight=biginteger, 8
default|root:bar:map:c:eleven=pattern, ^11$
default|root:bar:map:c:five=int, 5
default|root:bar:map:c:four=float, 4.0
default|root:bar:map:c:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:c:nine=bigdecimal, 9.0
default|root:bar:map:c:one=byte, 1
default|root:bar:map:c:seven=short, 7
default|root:bar:map:c:six=long, 6
default|root:bar:map:c:ten=string, ten
default|root:bar:map:c:three=double, 3.0
default|root:bar:map:c:twelve=file, /12
default|root:bar:map:c:two=char, 2
default|root:bar:map:c:zero=boolean, false
o1|root:bar:map:d=object, org.archive.settings.path.Foo
default|root:bar:map:d:eight=biginteger, 8
default|root:bar:map:d:eleven=pattern, ^11$
default|root:bar:map:d:five=int, 5
default|root:bar:map:d:four=float, 4.0
default|root:bar:map:d:moose=enum, org.archive.settings.path.Foo$Zoo-MOOSE
default|root:bar:map:d:nine=bigdecimal, 9.0
default|root:bar:map:d:one=byte, 1
default|root:bar:map:d:seven=short, 7
default|root:bar:map:d:six=long, 6
default|root:bar:map:d:ten=string, ten
default|root:bar:map:d:three=double, 3.0
default|root:bar:map:d:twelve=file, /12
default|root:bar:map:d:two=char, 2
default|root:bar:map:d:zero=boolean, false
o1,global|root:bar:slist=list, java.lang.String
global|root:bar:slist:0=string, zero
global|root:bar:slist:1=string, one
global|root:bar:slist:2=string, two
o1|root:bar:slist:3=string, three
o1|root:bar:slist:4=string, four
global|root:bar:smap=map, java.lang.String
global|root:bar:smap:a=string, 65
global|root:bar:smap:b=string, 66
global|root:bar:smap:c=string, 67
    <!DOCTYPE html><html lang="en" data-cast-api-enabled="true"><head><script>var ytcsi = {gt: function(n) {n = (n || '') + 'data_';return ytcsi[n] || (ytcsi[n] = {tick: {},span: {},info: {}});},tick: function(l, t, n) {ytcsi.gt(n).tick[l] = t || +new Date();},span: function(l, s, n) {ytcsi.gt(n).span[l] = (typeof s == 'number') ? s :+new Date() - ytcsi.data_.tick[l];},info: function(k, v, n) {ytcsi.gt(n).info[k] = v;}};(function() {var perf = window['performance'] || window['mozPerformance'] ||window['msPerformance'] || window['webkitPerformance'];ytcsi.tick('_start', perf ? perf['timing']['responseStart'] : null);})();if (document.webkitVisibilityState == 'prerender') {ytcsi.info('prerender', 1);document.addEventListener('webkitvisibilitychange', function() {ytcsi.tick('_start');}, false);}try {ytcsi.pt_ = (window.chrome && chrome.csi().pageT ||window.gtbExternal && gtbExternal.pageT() ||window.external && external.pageT);if (ytcsi.pt_) {ytcsi.info('pt', Math.floor(ytcsi.pt_));}} catch(e) {}</script>  <script>
    try {window.ytbuffer = {};ytbuffer.handleClick = function(e) {var element = e.target || e.srcElement;while (element.parentElement) {if (element.className.match(/(^| )yt-can-buffer( |$)/)) {window.ytbuffer = {bufferedClick: e};element.className += ' yt-is-buffered';break;}element = element.parentElement;}};if (document.addEventListener) {document.addEventListener('click', ytbuffer.handleClick);} else {document.attachEvent('onclick', ytbuffer.handleClick);}} catch(e) {}
    (function(){var a=!1;function b(d,m,e,f){a=f;f=document.getElementsByTagName("html")[0];var g=[f.className];d&&1251<=(window.innerWidth||document.documentElement.clientWidth)&&(g.push("guide-pinned"),m&&g.push("show-guide"));if(e){a?(d=951,e=1136):(d=1056,e=1262);var h=(window.innerWidth||document.documentElement.clientWidth)-21-50;1251<=(window.innerWidth||document.documentElement.clientWidth)&&m&&(h-=230);g.push(" ",h>=e?"content-snap-width-3":h>=d?"content-snap-width-2":"content-snap-width-1")}f.className=g.join(" ")}
var c=["yt","www","masthead","sizing","init"],k=this;c[0]in k||!k.execScript||k.execScript("var "+c[0]);for(var l;c.length&&(l=c.shift());)c.length||void 0===b?k[l]?k=k[l]:k=k[l]={}:k[l]=b;})();
yt.www.masthead.sizing.init(true,true,true,false);
  </script>



        <script src="//s.ytimg.com/yts/jsbin/www-scheduler-vflKNUgKf.js" name="www-scheduler"></script>


  
  <link rel="stylesheet" href="//s.ytimg.com/yts/cssbin/www-core-vflmPuKLi.css" name="www-core">
<script>if (window.ytcsi) {window.ytcsi.tick("ce", null, '');}</script>  

    
<title>BCCentralStudentLife - YouTube</title><link rel="search" type="application/opensearchdescription+xml" href="http://www.youtube.com/opensearch?locale=en_US" title="YouTube Video Search"><link rel="shortcut icon" href="https://s.ytimg.com/yts/img/favicon-vfldLzJxy.ico" type="image/x-icon">     <link rel="icon" href="//s.ytimg.com/yts/img/favicon_32-vflWoMFGx.png" sizes="32x32"><link rel="canonical" href="http://www.youtube.com/user/BCCentralStudentLife"><link rel="alternate" media="handheld" href="https://m.youtube.com/user/BCCentralStudentLife?"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.youtube.com/user/BCCentralStudentLife?">    <meta name="title" content="BCCentralStudentLife">

    <meta name="description" content="Check out what Student Life at Broward College Central Campus is up to!">

<meta name="keywords" content="Broward College Central Campus Willis Holcombe Center School Student Life Learning Education Davie">    <link rel="image_src" href="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s48-c-k-no/photo.jpg">
    <link rel="alternate" type="application/rss+xml" title="RSS" href="http://gdata.youtube.com/feeds/base/users/BCCentralStudentLife/uploads?alt=rss&amp;v=2&amp;orderby=published&amp;client=ytapi-youtube-profile">
          <meta property="og:site_name" content="YouTube">
    <meta property="og:url" content="http://www.youtube.com/user/BCCentralStudentLife">
    <meta property="og:title" content="BCCentralStudentLife">
    <meta property="og:image" content="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s900-c-k-no/photo.jpg">

      <meta property="og:description" content="Check out what Student Life at Broward College Central Campus is up to!">

      <meta property="og:type" content="profile">

    <meta property="fb:app_id" content="87741124305">
      <meta property="fb:profile_id" content="145913712216063">

      <meta name="twitter:card" content="summary">
    <meta name="twitter:site" content="@youtube">
    <meta name="twitter:url" content="http://www.youtube.com/user/BCCentralStudentLife">
    <meta name="twitter:title" content="BCCentralStudentLife">
    <meta name="twitter:description" content="Check out what Student Life at Broward College Central Campus is up to!">
    <meta name="twitter:image" content="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s900-c-k-no/photo.jpg">
    <meta name="twitter:app:name:iphone" content="YouTube">
    <meta name="twitter:app:id:iphone" content="544007664">
    <meta name="twitter:app:name:ipad" content="YouTube">
    <meta name="twitter:app:id:ipad" content="544007664">
      <meta name="twitter:app:url:iphone" content="vnd.youtube://user/UCo50hV2EIx4YHc58L0RZDDQ">
      <meta name="twitter:app:url:ipad" content="vnd.youtube://user/UCo50hV2EIx4YHc58L0RZDDQ">
    <meta name="twitter:app:name:googleplay" content="YouTube">
    <meta name="twitter:app:id:googleplay" content="com.google.android.youtube">
    <meta name="twitter:app:url:googleplay" content="http://www.youtube.com/user/BCCentralStudentLife">

      <link itemprop="url" href="http://www.youtube.com/user/BCCentralStudentLife">
    <meta itemprop="name" content="BCCentralStudentLife">
    <meta itemprop="description" content="Check out what Student Life at Broward College Central Campus is up to!">
    <meta itemprop="paid" content="False">

      <meta itemprop="channelId" content="UCo50hV2EIx4YHc58L0RZDDQ">


        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="http://www.youtube.com/user/BCCentralStudentLife">
        </span>
        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="https://plus.google.com/111446941772299840849">
        </span>

    <link itemprop="thumbnailUrl" href="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s900-c-k-no/photo.jpg">
    <span itemprop="thumbnail" itemscope itemtype="http://schema.org/ImageObject">
      <link itemprop="url" href="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s900-c-k-no/photo.jpg">
      <meta itemprop="width" content="900">
      <meta itemprop="height" content="900">
    </span>


      <meta itemprop="isFamilyFriendly" content="True">
      <meta itemprop="regionsAllowed" content="AD,AE,AF,AG,AI,AL,AM,AO,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BL,BM,BN,BO,BQ,BR,BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CW,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MF,MG,MH,MK,ML,MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,SS,ST,SV,SX,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,TM,TN,TO,TR,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW">

  <div id="watch-container" itemid="" itemscope itemtype="http://schema.org/YoutubeChannelV2">
        <link itemprop="url" href="http://www.youtube.com/user/BCCentralStudentLife">
    <meta itemprop="name" content="BCCentralStudentLife">
    <meta itemprop="description" content="Check out what Student Life at Broward College Central Campus is up to!">
    <meta itemprop="paid" content="False">

      <meta itemprop="channelId" content="UCo50hV2EIx4YHc58L0RZDDQ">


        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="http://www.youtube.com/user/BCCentralStudentLife">
        </span>
        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="https://plus.google.com/111446941772299840849">
        </span>

    <link itemprop="thumbnailUrl" href="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s900-c-k-no/photo.jpg">
    <span itemprop="thumbnail" itemscope itemtype="http://schema.org/ImageObject">
      <link itemprop="url" href="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s900-c-k-no/photo.jpg">
      <meta itemprop="width" content="900">
      <meta itemprop="height" content="900">
    </span>


      <meta itemprop="isFamilyFriendly" content="True">
      <meta itemprop="regionsAllowed" content="AD,AE,AF,AG,AI,AL,AM,AO,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BL,BM,BN,BO,BQ,BR,BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CW,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MF,MG,MH,MK,ML,MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,SS,ST,SV,SX,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,TM,TN,TO,TR,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW">

  </div>

      <div class="cmt_iframe_holder" data-href="http://www.youtube.com/user/BCCentralStudentLife" data-viewtype="FILTERED" style="display: none;"></div>


  <link rel="stylesheet" href="//s.ytimg.com/yts/cssbin/www-pageframe-vflGQahlM.css" name="www-pageframe">
  <link rel="stylesheet" href="//s.ytimg.com/yts/cssbin/www-guide-vflNTDUTm.css" name="www-guide">
    <link rel="stylesheet" href="//s.ytimg.com/yts/cssbin/www-home-c4-vfldrNW9U.css" name="www-home-c4">



  
<script>if (window.ytcsi) {window.ytcsi.tick("cl", null, '');}</script></head>

      <body dir="ltr" class="  ltr  gecko gecko-28     site-center-aligned site-as-giant-card guide-pinning-enabled appbar-hidden     not-nirvana-dogfood  hitchhiker-enabled    flex-width-enabled      flex-width-enabled-snap    delayed-frame-styles-not-in  " id="body">

  <div id="body-container"><form name="logoutForm" method="POST" action="/logout"><input type="hidden" name="action_logout" value="1"></form><div id="masthead-positioner">      <div id="sb-wrapper">
    <div id="sb-container" class="sb-card sb-off">
      <div class="sb-card-arrow"></div>
      <div class="sb-card-border">
        <div class="sb-card-body-arrow"></div>
        <div class="sb-card-content" id="sb-target"></div>
      </div>
    </div>
    <div id="sb-onepick-target" class="sb-off"></div>
  </div>

  
  <div id="yt-masthead-container" class="yt-grid-box yt-base-gutter"><div id="yt-masthead" class=""><div class="yt-masthead-logo-container ">    <a id="logo-container" href="/" title="YouTube home" class=""><img id="logo" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="YouTube home"></a>
<div id="appbar-guide-button-container"><button onclick=";return false;" id="appbar-guide-button" type="button" class="appbar-guide-toggle appbar-guide-clickable-ancestor yt-uix-button yt-uix-button-text yt-uix-button-size-default yt-uix-button-has-icon yt-uix-button-empty"  role="button" aria-label="Guide"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-appbar-guide"></span><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-arrow"></button><div id="appbar-guide-button-notification-check" class="yt-valign"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="appbar-guide-notification-icon yt-valign-content"></div></div><div id="appbar-main-guide-notification-container"></div></div><div id="yt-masthead-user" class="yt-uix-clickcard"><span id="appbar-onebar-upload-group" class="yt-uix-button-group"><a href="#" class="yt-uix-button   create-channel-lightbox yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=mhsb" id="upload-btn" data-upsell="upload"><span class="yt-uix-button-content">Upload </span></a><button aria-haspopup="true" id="appbar-settings-button" type="button" class="flip  yt-uix-button yt-uix-button-default yt-uix-button-size-default yt-uix-button-has-icon yt-uix-button-empty" onclick=";return false;" data-button-menu-fixed="True" data-button-menu-action="yt.www.masthead.appbar.toggleMenu" data-button-menu-id="appbar-settings-menu" role="button" aria-label="Settings"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-appbar-settings"></span><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-arrow"></button><ul id="appbar-settings-menu" class="appbar-menu yt-uix-button-menu yt-uix-button-menu-default" role="menu" aria-haspopup="true" style="display: none">  <li role="menuitem" >
    <a href="/dashboard" class="yt-uix-button-menu-item upload-menu-item">
        <span class="yt-valign icon-container">
          <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="upload-menu-dashboard-icon yt-valign-container">
        </span>
      Dashboard
    </a>
  </li>
  <li role="menuitem" >
    <a href="/my_videos" class="yt-uix-button-menu-item upload-menu-item">
        <span class="yt-valign icon-container">
          <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="upload-menu-vm-icon yt-valign-container">
        </span>
      Video Manager
    </a>
  </li>
  <li role="menuitem" >
    <a href="https://www.youtube.com/analytics" class="yt-uix-button-menu-item upload-menu-item">
        <span class="yt-valign icon-container">
          <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="upload-menu-analytics-icon yt-valign-container">
        </span>
      Analytics
    </a>
  </li>
  <li role="menuitem" class="yt-uix-button-menu-new-section-separator">
    <a href="/account" class="yt-uix-button-menu-item upload-menu-item">
      YouTube settings
    </a>
  </li>
<li role="menuitem">    <button data-ghelp-anchor="appbar-settings-button" id="appbar-help" class="yt-uix-button-reverse yt-google-help-link inq-no-click yt-uix-button-menu-item upload-menu-item yt-uix-button yt-uix-button-google-help yt-uix-button-size-default" data-ghelp-tracking-param="appbar" onclick=";return false;" type="button"  role="button"><span class="yt-uix-button-content">Help
 </span></button>
</li></ul></span>  <span id="yt-masthead-user-displayname" dir="ltr" class="yt-valign-container yt-masthead-toggle-expanded" >
    Hunter Stern
  </span>

    <button onclick=";return false;" id="sb-button-notify" type="button" class="sb-notif-off yt-uix-button yt-uix-button-default yt-uix-button-size-default yt-uix-button-has-icon"  role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-bell"></span><span class="yt-uix-button-content">  </span></button>

      <button onclick=";return false;" type="button" class="yt-masthead-user-icon yt-masthead-toggle-expanded yt-uix-button yt-uix-button-default yt-uix-button-size-default" data-orientation="vertical" role="button"><span class="yt-uix-button-content">    <span class="video-thumb  yt-thumb yt-thumb-27"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" src="https://yt3.ggpht.com/-tABzqFZ-Q7Y/AAAAAAAAAAI/AAAAAAAAAAA/DK-o5fBilz0/s88-c-k-no/photo.jpg" width="27"  height="27" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
 </span></button>

</div><div id="yt-masthead-content"><form id="masthead-search" class="search-form consolidated-form" action="/results" onsubmit="if (_gel(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false;"><button class="search-btn-component search-button yt-uix-button yt-uix-button-default yt-uix-button-size-default" type="submit" id="search-btn" tabindex="2" dir="ltr" onclick="if (_gel(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false; _gel(&#39;masthead-search&#39;).submit(); return false;;return true;"  role="button"><span class="yt-uix-button-content">Search </span></button><div id="masthead-search-terms" class="masthead-search-terms-border" dir="ltr"><label><input id="masthead-search-term" autocomplete="off"  class="search-term yt-uix-form-input-bidi" name="search_query" value="" type="text" tabindex="1" title="Search"></label></div></form></div></div></div>
            <div id="masthead-expanded" class="collapsed">
    <div id="masthead-expanded-container" class="with-sandbar">
      <div id="masthead-expanded-menus-container">


        <span id="masthead-expanded-menu-shade"></span>
          <div id="masthead-expanded-menu">
    <span class="masthead-expanded-menu-header">
YouTube
    </span>
    <ul id="masthead-expanded-menu-list">
      <li class="masthead-expanded-menu-item">
        <a href="/create_channel" class="yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=mhee">
My Channel
        </a>
      </li>
      <li class="masthead-expanded-menu-item">
        <a href="/my_videos" class="yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=mhee">
Video Manager
        </a>
      </li>
      <li class="masthead-expanded-menu-item">
        <a href="/feed/subscriptions" class="yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=mhee">Subscriptions</a>
      </li>
      <li class="masthead-expanded-menu-item">
        <a href="/account" class="yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=mhee">
YouTube settings
        </a>
      </li>
    </ul>
  </div>

          <div id="masthead-expanded-google-menu">
    <span class="masthead-expanded-menu-header">
Google Account
    </span>
    <div id="masthead-expanded-menu-google-container">
      <div id="masthead-expanded-menu-google-column1">
        <ul>
          <li class="masthead-expanded-menu-item">
            <a href="https://plus.google.com/u/0/103249394226247435087">Profile</a>
          </li>
          <li class="masthead-expanded-menu-item"><a href="https://plus.google.com/u/0/stream">Google+</a></li>
            <li class="masthead-expanded-menu-item"><a href="https://www.google.com/intl/en/policies/">Privacy</a></li>
          <li class="masthead-expanded-menu-item">
            <a href="https://plus.google.com/u/0/settings">
Settings
            </a>
          </li>
        </ul>
      </div>
      <div id="masthead-expanded-menu-google-column2">
        <div id="masthead-expanded-menu-account-container">
              <img id="masthead-expanded-menu-gaia-photo" alt="" data-src="https://yt3.ggpht.com/-tABzqFZ-Q7Y/AAAAAAAAAAI/AAAAAAAAAAA/DK-o5fBilz0/s88-c-k-no/photo.jpg" width="28" height="28">
  <div id="masthead-expanded-menu-account-info"  class="email-only">
      <p>Hunter Stern</p>
    <p id="masthead-expanded-menu-email">hunter@archive.org</p>
  </div>

        </div>
        <ul>
          <li class="masthead-expanded-menu-item">
            <a class="end" href="#" onclick="document.logoutForm.submit(); return false;">
Sign out
            </a>
          </li>
            <li class="masthead-expanded-menu-item">
                <div class="yt-uix-clickcard masthead-expanded-menu-switch" data-card-class="masthead-card-switch-account">
    <button onclick=";return false;" type="button" class="yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-button-size-default" data-position="rightbottom" data-orientation="vertical" role="button"><span class="yt-uix-button-content">Switch account </span></button>
    <div class="yt-uix-clickcard-content">
        <ul id="yt-masthead-multilogin">
              <li>
    <a class="yt-masthead-multilogin-user yt-valign" href="/signin?next=%2Fuser%2FBCCentralStudentLife&amp;action_handle_signin=true&amp;skip_identity_prompt=True&amp;authuser=0">
          <span class="video-thumb yt-masthead-multilogin-user-icon yt-thumb yt-thumb-46"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Hunter Stern" src="https://yt3.ggpht.com/-tABzqFZ-Q7Y/AAAAAAAAAAI/AAAAAAAAAAA/DK-o5fBilz0/s88-c-k-no/photo.jpg" width="46"  height="46" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>

      <span class="yt-masthead-multilogin-user-content yt-valign-container">
        <span class="yt-masthead-multilogin-user-link" dir="ltr">Hunter Stern</span><br>
        hunter@archive.org
      </span>
          <div class="yt-alert yt-alert-naked yt-alert-success">
      <div class="yt-alert-icon">
    <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>

  </div>

    </a>
  </li>

        </ul>
        <div id="yt-masthead-multilogin-actions" class="yt-grid-box">
          <button onclick="document.logoutForm.submit();return false;" id="yt-masthead-multilogin-sign-out" type="button" class=" yt-uix-button yt-uix-button-link yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">Sign out </span></button>

            <a href="https://accounts.google.com/AddSession?continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252Fuser%252FBCCentralStudentLife&amp;passive=false&amp;service=youtube&amp;uilel=0&amp;hl=en">Add account</a>
        </div>
    </div>
  </div>

            </li>
        </ul>
      </div>
    </div>
  </div>

      </div>
      <div id="masthead-expanded-sandbar" class="">
        <div id="masthead-expanded-lists-container">
          <div id="masthead-expanded-loading-message">Loading...</div>
        </div>
      </div>
      <div class="clear"></div>
    </div>
  </div>


    <div id="masthead-appbar-container" class="clearfix"><div id="masthead-appbar"><div id="appbar-content" class="    appbar-content-hidden">      <div id="appbar-nav" class="appbar-content-hidable">
  <a href="/user/BCCentralStudentLife">
    <img class="appbar-nav-avatar" src="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s100-c-k-no/photo.jpg" title="BCCentralStudentLife" alt="BCCentralStudentLife">
  </a>
<ul class="appbar-nav-menu"><li>    <h2 class="epic-nav-item-heading ">
      BCCentralStudentLife
    </h2>
</li><li>    <a href="/user/BCCentralStudentLife/videos" class="yt-uix-button   spf-nolink yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJQCEMMtKAE"><span class="yt-uix-button-content">Videos </span></a>
</li><li>    <a href="/user/BCCentralStudentLife/playlists" class="yt-uix-button   spf-nolink yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJUCEMMtKAI"><span class="yt-uix-button-content">Playlists </span></a>
</li><li>    <a href="/user/BCCentralStudentLife/channels" class="yt-uix-button   spf-nolink yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJYCEMMtKAM"><span class="yt-uix-button-content">Channels </span></a>
</li><li>    <a href="/user/BCCentralStudentLife/discussion" class="yt-uix-button   spf-nolink yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJcCEMMtKAQ"><span class="yt-uix-button-content">Discussion </span></a>
</li><li>    <a href="/user/BCCentralStudentLife/about" class="yt-uix-button   spf-nolink yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJgCEMMtKAU"><span class="yt-uix-button-content">About </span></a>
</li><li>    <a href="/user/BCCentralStudentLife/search" class="yt-uix-button   spf-nolink yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default yt-uix-button-empty" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJkCEMMtKAY"></a>
</li></ul>  </div>

</div></div></div>

</div><div id="masthead-positioner-height-offset"></div><div id="page-container"><div id="page" class="  channel    not-fixed-width-tab-widescreen clearfix"><div id="guide" class="yt-scrollbar">      <div id="appbar-guide-menu" class="appbar-menu appbar-guide-menu-layout appbar-guide-clickable-ancestor yt-uix-scroller">
    <div id="guide-container" class="vve-check" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CAEQ_h4">
        <div class="guide-module-content yt-scrollbar">
    <ul class="guide-toplevel">
            <li class="guide-section vve-check"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CAIQ5isoAA"
    data-visibility-tracking="">
    <div class="guide-item-container personal-item">
      
      <ul class="guide-user-links yt-uix-tdl yt-box">
              <li class="vve-check guide-channel overflowable-list-item " id="what_to_watch-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/"
    title="What to Watch"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-personal&amp;ved=CAMQtSwoAA"
    data-visibility-tracking=""
    data-external-id="what_to_watch"
    data-serialized-endpoint="0qDduQEREg9GRXdoYXRfdG9fd2F0Y2g%3D"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-what-to-watch-icon">
        <span class="display-name  no-count">
          <span>
            What to Watch
          </span>
        </span>
    </span>
  </a>

  </li>

              <li class="vve-check guide-channel overflowable-list-item " id="create_channel-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/create_channel"
    title="My Channel"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-personal&amp;ved=CAQQtSwoAQ"
    data-visibility-tracking=""
    data-external-id="create_channel"
    data-serialized-endpoint="8qHduQECCAE%3D"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-my-channel-icon">
        <span class="display-name  no-count">
          <span>
            My Channel
          </span>
        </span>
    </span>
  </a>

  </li>

              <li class="vve-check guide-channel overflowable-list-item " id="subscriptions-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/feed/subscriptions"
    title="My Subscriptions"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-personal&amp;ved=CAUQtSwoAg"
    data-visibility-tracking=""
    data-external-id="subscriptions"
    data-serialized-endpoint="0qDduQEREg9GRXN1YnNjcmlwdGlvbnM%3D"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-my-subscriptions-icon">
        <span class="display-name  no-count">
          <span>
            My Subscriptions
          </span>
        </span>
    </span>
  </a>

  </li>

              <li class="vve-check guide-channel overflowable-list-item " id="history-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/feed/history"
    title="History"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-personal&amp;ved=CAYQtSwoAw"
    data-visibility-tracking=""
    data-external-id="history"
    data-serialized-endpoint="0qDduQELEglGRWhpc3Rvcnk%3D"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-history-icon">
        <span class="display-name  no-count">
          <span>
            History
          </span>
        </span>
    </span>
  </a>

  </li>

              <li class="vve-check guide-channel overflowable-list-item " id="VLWL-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/playlist?list=WL"
    title="Watch Later"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-personal&amp;ved=CAcQtSwoBA"
    data-visibility-tracking=""
    data-external-id="VLWL"
    data-serialized-endpoint="0qDduQEGEgRWTFdM"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-watch-later-icon">
        <span class="display-name  no-count">
          <span>
            Watch Later
          </span>
        </span>
    </span>
  </a>

  </li>

      </ul>
    </div>
      <hr class="guide-section-separator">
  </li>

            <li id="guide-subscriptions-section"
    class="guide-section without-filter vve-check"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CAgQ_x4oAQ"
    data-visibility-tracking=""
    >
        <h3>
      <a href="/subscription_manager" class=" yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-channel">Subscriptions</a>
    </h3>

    <div id="guide-subs-footer-container">
      <div id="guide-subscriptions-promo" class="default-promo">
        <a href="    /channels
" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-plus"></span><span class="yt-uix-button-content">Add channels </span></a>
        <div class="subscriptions-wrapper">
            <div class="guide-channels-content yt-scrollbar">
    <ul id="guide-channels" class="guide-channels-list guide-item-container parent-list guide-infinite-list yt-uix-scroller filter-has-matches yt-uix-tdl">
          <li class="vve-check guide-channel overflowable-list-item " id="UCF0pVplsI8R5kcAqgtoRqoA-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/channel/UCF0pVplsI8R5kcAqgtoRqoA"
    title="Popular on YouTube"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-channel&amp;ved=CAkQtSwoAA"
    data-visibility-tracking=""
    data-external-id="UCF0pVplsI8R5kcAqgtoRqoA"
    data-serialized-endpoint="0qDduQEaEhhVQ0YwcFZwbHNJOFI1a2NBcWd0b1Jxb0E%3D"
  >
    <span class="yt-valign-container">
        <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-20"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/i/F0pVplsI8R5kcAqgtoRqoA/1.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="20"  height="20" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</span>
        <span class="display-name  no-count">
          <span>
            Popular on YouTube
          </span>
        </span>
    </span>
  </a>

  </li>

          <li class="vve-check guide-channel overflowable-list-item " id="UC-9-kyTW8ZkZNDHQJ6FgpwQ-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
    title="Music"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-channel&amp;ved=CAoQtSwoAQ"
    data-visibility-tracking=""
    data-external-id="UC-9-kyTW8ZkZNDHQJ6FgpwQ"
    data-serialized-endpoint="0qDduQEaEhhVQy05LWt5VFc4WmtaTkRIUUo2Rmdwd1E%3D"
  >
    <span class="yt-valign-container">
        <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-20"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/i/-9-kyTW8ZkZNDHQJ6FgpwQ/1.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="20"  height="20" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</span>
        <span class="display-name  no-count">
          <span>
            Music
          </span>
        </span>
    </span>
  </a>

  </li>

          <li class="vve-check guide-channel overflowable-list-item " id="UCEgdi0XIXXZ-qJOFPf4JSKw-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/channel/UCEgdi0XIXXZ-qJOFPf4JSKw"
    title="Sports"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-channel&amp;ved=CAsQtSwoAg"
    data-visibility-tracking=""
    data-external-id="UCEgdi0XIXXZ-qJOFPf4JSKw"
    data-serialized-endpoint="0qDduQEaEhhVQ0VnZGkwWElYWFotcUpPRlBmNEpTS3c%3D"
  >
    <span class="yt-valign-container">
        <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-20"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/i/Egdi0XIXXZ-qJOFPf4JSKw/1.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="20"  height="20" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</span>
        <span class="display-name  no-count">
          <span>
            Sports
          </span>
        </span>
    </span>
  </a>

  </li>

          <li class="vve-check guide-channel overflowable-list-item " id="UCOpNcN46UbXVtpKMrmU4Abg-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/channel/UCOpNcN46UbXVtpKMrmU4Abg"
    title="Gaming"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-channel&amp;ved=CAwQtSwoAw"
    data-visibility-tracking=""
    data-external-id="UCOpNcN46UbXVtpKMrmU4Abg"
    data-serialized-endpoint="0qDduQEaEhhVQ09wTmNONDZVYlhWdHBLTXJtVTRBYmc%3D"
  >
    <span class="yt-valign-container">
        <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-20"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/i/OpNcN46UbXVtpKMrmU4Abg/1.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="20"  height="20" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</span>
        <span class="display-name  no-count">
          <span>
            Gaming
          </span>
        </span>
    </span>
  </a>

  </li>

    </ul>
  </div>

          <a class="guide-subscriptions-promo-tooltip" href="    /channels
">
            <p>
              <span class="" >Your subscriptions will show up here. Browse some channels to get started.</span>
            </p>
          </a>
        </div>
      </div>
    </div>
      <hr class="guide-section-separator">
  </li>

            <li class="guide-section vve-check"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CA0Q5isoAg"
    data-visibility-tracking="">
    <div class="guide-item-container personal-item">
      
      <ul class="guide-user-links yt-uix-tdl yt-box">
              <li class="vve-check guide-channel overflowable-list-item " id="guide_builder-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/channels"
    title="Browse channels"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-manage&amp;ved=CA4QtSwoAA"
    data-visibility-tracking=""
    data-external-id="guide_builder"
    data-serialized-endpoint="0qPduQECCAE%3D"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-builder-icon">
        <span class="display-name  no-count">
          <span>
            Browse channels
          </span>
        </span>
    </span>
  </a>

  </li>

              <li class="vve-check guide-channel overflowable-list-item " id="subscription_manager-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="/subscription_manager"
    title="Manage subscriptions"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-manage&amp;ved=CA8QtSwoAQ"
    data-visibility-tracking=""
    data-external-id="subscription_manager"
    data-serialized-endpoint="oqjduQECCAE%3D"
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-subscription-manager-icon">
        <span class="display-name  no-count">
          <span>
            Manage subscriptions
          </span>
        </span>
    </span>
  </a>

  </li>

      </ul>
    </div>
  </li>

    </ul>
  </div>

    </div>
  </div>
  <div id="appbar-guide-notifications" class="hid">
        <div id="appbar-guide-notification-watch-later-video-added">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Added to Watch Later</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-watch-later-video-removed">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Removed from Watch Later</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-subscription">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Subscription added</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-unsubscription">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Subscription removed</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-playlist-like">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Playlist added</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-playlist-unlike">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Playlist removed</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-video-like">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Added to Liked videos</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-video-unlike">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Removed from Liked videos</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-event-reminder-set">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">You&#39;ll be reminded about this event</span></span></div>    -->
  </div>


    <div id="appbar-guide-notification-event-reminder-removed">
    <!--
<div class="appbar-guide-notification"><span class="appbar-guide-notification-content-wrapper yt-valign"><img class="appbar-guide-notification-icon" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif"><span class="appbar-guide-notification-text-content">Event reminder removed</span></span></div>    -->
  </div>


  </div>
  <div id="appbar-guide-item-templates" class="hid">
        <div id="appbar-guide-item-template-playlist">
      <!--
          <li class="vve-check guide-channel overflowable-list-item " id="__ID__-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="__URL__"
    title="__TITLE__"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-playlists"
    data-visibility-tracking=""
    data-external-id="__ID__"
    data-serialized-endpoint=""
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-playlists-icon">
        <span class="display-name  no-count">
          <span>
            __TITLE__
          </span>
        </span>
    </span>
  </a>

  </li>

      -->
    </div>
    <div id="appbar-guide-item-template-mix">
      <!--
          <li class="vve-check guide-channel overflowable-list-item " id="__ID__-guide-item"
      data-visibility-tracking="">
      
  <a class="guide-item yt-uix-sessionlink yt-valign spf-nolink   "
    href="__URL__"
    title="__TITLE__"
    data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=g-playlists"
    data-visibility-tracking=""
    data-external-id="__ID__"
    data-serialized-endpoint=""
  >
    <span class="yt-valign-container">
        <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="thumb guide-mix-icon">
        <span class="display-name  no-count">
          <span>
            __TITLE__
          </span>
        </span>
    </span>
  </a>

  </li>

      -->
    </div>

  </div>
  <iframe id="appbar-guide-iframe-mask" class="appbar-guide-menu-layout"></iframe>

</div><div id="alerts" class="content-alignment">  
</div><div id="header"></div><div id="player" class="  off-screen  ">  <div id="player-mole-container">

    <div id="playlist" class="playlist">
      
    </div>

    <div id="player-unavailable" class="  hid  ">
      
    </div>

      <div id="player-api" class="player-width player-height off-screen-target  player-api"></div>

          <script>if (window.ytcsi) {window.ytcsi.tick("cfg", null, '');}</script>
        <div id="html5-player-messages" style="display:none">
    <!--
    -->
  </div>

<script>var ytplayer = ytplayer || {};ytplayer.config = {"min_version": "8.0.0", "sts": 16200, "html5": false, "args": {"cr": "US", "autoplay": "0", "enablejsapi": 1, "ssl": "1", "fexp": "927606,935705,941404,940908,936120,913434,939940,939944,936923,945044", "hl": "en_US"}, "assets": {"js": "\/\/s.ytimg.com\/yts\/jsbin\/html5player-en_US-vflzEDYyE.js", "html": "\/html5_player_template", "css": "\/\/s.ytimg.com\/yts\/cssbin\/www-player-vflbzCGhL.css"}, "params": {"allowscriptaccess": "always", "allowfullscreen": "true", "bgcolor": "#000000"}, "attrs": {"id": "movie_player"}, "url_v9as2": "https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflr2PFkb\/cps.swf", "url_v8": "https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflr2PFkb\/cps.swf", "url": "https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflr2PFkb\/watch_as3.swf"};</script>


  </div>

  <div class="clear"></div>
</div>
<div id="content" class="  content-alignment">  




  <div class="branded-page-v2-container branded-page-base-bold-titles branded-page-v2-container-flex-width branded-page-v2-has-top-row" id="c4-overview-tab">
      <div class="branded-page-v2-top-row">
        




    <div class="branded-page-v2-header channel-header yt-card">
    <div id="gh-banner">
          <style>
      #c4-header-bg-container {
      background-image: url(//i1.ytimg.com/u/o50hV2EIx4YHc58L0RZDDQ/channels4_banner.jpg?v=52f3a92e);
  }


  @media screen and (-webkit-min-device-pixel-ratio: 1.5),
         screen and (min-resolution: 1.5dppx) {
#c4-header-bg-container {
        background-image: url(//i1.ytimg.com/u/o50hV2EIx4YHc58L0RZDDQ/channels4_banner_hd.jpg?v=52f3a92e);
    }
  }

#c4-header-bg-container .hd-banner-image {
      background-image: url(//i1.ytimg.com/u/o50hV2EIx4YHc58L0RZDDQ/channels4_banner_hd.jpg?v=52f3a92e);
  }

    </style>
  <div id="c4-header-bg-container" class=" has-custom-banner">
    <div class="hd-banner">
      <div class="hd-banner-image"></div>
    </div>
          <div id="header-links">
      <ul class="about-network-links">
            <li class="channel-links-item">
    <a href="https://plus.google.com/u/0/111446941772299840849" rel="me nofollow" target="_blank" title="" class="about-channel-link yt-uix-redirect-link about-channel-link-with-icon">
        <img src="//s2.googleusercontent.com/s2/favicons?domain=plus.google.com&amp;feature=youtube_channel" class="about-channel-link-favicon" alt="" width="16" height="16">
    </a>
  </li>

            <li class="channel-links-item">
    <a href="http://www.facebook.com/pages/Broward-College-Student-Life-Central-Campus/145913712216063" rel="me nofollow" target="_blank" title="" class="about-channel-link yt-uix-redirect-link about-channel-link-with-icon">
        <img src="//s2.googleusercontent.com/s2/favicons?domain=www.facebook.com&amp;feature=youtube_channel" class="about-channel-link-favicon" alt="" width="16" height="16">
    </a>
  </li>

            <li class="channel-links-item">
    <a href="https://twitter.com/BrowardCollege" rel="me nofollow" target="_blank" title="" class="about-channel-link yt-uix-redirect-link about-channel-link-with-icon">
        <img src="//s2.googleusercontent.com/s2/favicons?domain=twitter.com&amp;feature=youtube_channel" class="about-channel-link-favicon" alt="" width="16" height="16">
    </a>
  </li>

      </ul>

  </div>



          <a class="channel-header-profile-image-container spf-link" href="/user/BCCentralStudentLife">
      <img class="channel-header-profile-image" src="https://yt3.ggpht.com/-dvEVPjaMpQg/AAAAAAAAAAI/AAAAAAAAAAA/ss98kBE_830/s100-c-k-no/photo.jpg" title="BCCentralStudentLife" alt="BCCentralStudentLife">
    </a>

  </div>

    </div>
      
  <div class="">
    <div class="primary-header-contents" id="c4-primary-header-contents">
      <div class="primary-header-actions clearfix">
                <span class="channel-header-subscription-button-container yt-uix-button-subscription-container with-preferences" ><button class="yt-uix-subscription-button yt-can-buffer yt-uix-button yt-uix-button-subscribe-branded yt-uix-button-size-default yt-uix-button-has-icon" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-channel-external-id="UCo50hV2EIx4YHc58L0RZDDQ" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=channels4&amp;ved=CJECEJsr" data-style-type="branded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button><button onclick=";return false;" type="button" class="yt-uix-subscription-preferences-button yt-uix-button yt-uix-button-default yt-uix-button-size-default yt-uix-button-has-icon yt-uix-button-empty" data-channel-external-id="UCo50hV2EIx4YHc58L0RZDDQ" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-subscription-preferences"></span></button><span class="yt-subscription-button-subscriber-count-branded-horizontal subscribed" >41</span>  <span class="yt-subscription-button-disabled-mask" title=""></span>
  
  <div class="yt-uix-overlay " data-overlay-style="primary"data-overlay-shape="tiny">
    
        <div class="yt-dialog hid ">
    <div class="yt-dialog-base">
      <span class="yt-dialog-align"></span>
      <div class="yt-dialog-fg">
        <div class="yt-dialog-fg-content">
            <div class="yt-dialog-header">
                <h2 class="yt-dialog-title">
                        Subscription preferences


                </h2>
            </div>
          <div class="yt-dialog-loading">
              <div class="yt-dialog-waiting-content">
    <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Loading...</div>
  </div>

          </div>
          <div class="yt-dialog-content">
              <div class="subscription-preferences-overlay-content-container">
    <div class="subscription-preferences-overlay-loading ">
        <p class="yt-spinner">
      <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Loading icon" class="yt-spinner-img">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
    <div class="subscription-preferences-overlay-content">
    </div>
  </div>

          </div>
          <div class="yt-dialog-working">
              <div class="yt-dialog-working-overlay"></div>
  <div class="yt-dialog-working-bubble">
    <div class="yt-dialog-waiting-content">
      <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Working...</div>
    </div>
  </div>

          </div>
        </div>
      </div>
    </div>
  </div>


  </div>

</span>

              
      </div>
      <h1 class="branded-page-header-title">
        <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text" ><a dir="ltr" href="/user/BCCentralStudentLife" class="spf-link branded-page-header-title-link yt-uix-sessionlink" title="BCCentralStudentLife" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"      >BCCentralStudentLife</a></span></span></span>
        </a>
      </h1>
    </div>
      <div id="channel-subheader" class="clearfix branded-page-gutter-padding appbar-content-trigger">
    <ul id="channel-navigation-menu" class="clearfix">
        <li>
          <h2 class="epic-nav-item-heading ">Home</h2>
        </li>
        <li>
          <a href="/user/BCCentralStudentLife/videos" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-content">Videos </span></a>
        </li>
        <li>
          <a href="/user/BCCentralStudentLife/playlists" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-content">Playlists </span></a>
        </li>
        <li>
          <a href="/user/BCCentralStudentLife/channels" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-content">Channels </span></a>
        </li>
        <li>
          <a href="/user/BCCentralStudentLife/discussion" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-content">Discussion </span></a>
        </li>
        <li>
          <a href="/user/BCCentralStudentLife/about" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-content">About </span></a>
        </li>
        <li>
            <div id="channel-search" ><label class="show-search epic-nav-item secondary-nav" for="channels-search-field"><img class="epic-nav-item-heading-icon" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Search Channel"></label><form class="search-form epic-nav-item secondary-nav"action="/user/BCCentralStudentLife/search"method="get"><span class=" yt-uix-form-input-container yt-uix-form-input-text-container ">    <input class="yt-uix-form-input-text search-field" name="query" id="channels-search-field" type="text" placeholder="Search Channel" maxlength="100" autocomplete="off">
</span></form></div>
        </li>
    </ul>
  </div>

  </div>

  </div>


      </div>

    <div class="branded-page-v2-col-container">
      <div class="branded-page-v2-col-container-inner">
        <div class="branded-page-v2-primary-col">
          <div class="   yt-card  clearfix">
              <div class="branded-page-v2-body branded-page-v2-primary-column-content" id="gh-overviewtab">
          

      <div class="c4-spotlight-module  yt-section-hover-container">
      <div class="c4-spotlight-module-component upsell">
          
  <div class="upsell-video-container yt-section-hover-container">
          <div class="video-player-view-component branded-page-box">
    <div class="video-content clearfix ">
        <div class="c4-player-container  c4-flexible-player-container">
      <div class="c4-flexible-height-setter"></div>
      <div id="upsell-video" class="c4-flexible-player-box" data-video-id="f6MV89_80Wc" data-swf-config="{&amp;quot;min_version&amp;quot;: &amp;quot;8.0.0&amp;quot;, &amp;quot;sts&amp;quot;: 16200, &amp;quot;html5&amp;quot;: false, &amp;quot;args&amp;quot;: {&amp;quot;view_count&amp;quot;: 38, &amp;quot;cr&amp;quot;: &amp;quot;US&amp;quot;, &amp;quot;token&amp;quot;: &amp;quot;vjVQa1PpcFPTHm5_nHTsHT17UfEV__KRtEtCAo8buAQ=&amp;quot;, &amp;quot;autoplay&amp;quot;: &amp;quot;1&amp;quot;, &amp;quot;el&amp;quot;: &amp;quot;profilepage&amp;quot;, &amp;quot;keywords&amp;quot;: &amp;quot;Broward Community College (Organization),broward college,central,campus,i heart bc song,i heart bc,happy at broward college,happy,Pharrell Williams (Musical Artist),Vevo (Website),Acoustic Guitar (Musical Instrument),acoustic set,acoustic&amp;quot;, &amp;quot;ssl&amp;quot;: &amp;quot;1&amp;quot;, &amp;quot;use_cipher_signature&amp;quot;: false, &amp;quot;width&amp;quot;: &amp;quot;360&amp;quot;, &amp;quot;rel&amp;quot;: 0, &amp;quot;user_age&amp;quot;: 41, &amp;quot;sendtmp&amp;quot;: &amp;quot;1&amp;quot;, &amp;quot;author&amp;quot;: &amp;quot;BCCentralStudentLife&amp;quot;, &amp;quot;autohide&amp;quot;: &amp;quot;1&amp;quot;, &amp;quot;height&amp;quot;: &amp;quot;203&amp;quot;, &amp;quot;idpj&amp;quot;: &amp;quot;-6&amp;quot;, &amp;quot;delay&amp;quot;: &amp;quot;9&amp;quot;, &amp;quot;iurlsd&amp;quot;: &amp;quot;https:\/\/i1.ytimg.com\/vi\/f6MV89_80Wc\/sddefault.jpg&amp;quot;, &amp;quot;allow_embed&amp;quot;: 1, &amp;quot;muted&amp;quot;: &amp;quot;0&amp;quot;, &amp;quot;status&amp;quot;: &amp;quot;ok&amp;quot;, &amp;quot;fexp&amp;quot;: &amp;quot;927606,935705,941404,940908,936120,913434,939940,939944,936923,945044&amp;quot;, &amp;quot;eurl&amp;quot;: &amp;quot;http:\/\/www.youtube.com\/user\/BCCentralStudentLife&amp;quot;, &amp;quot;ps&amp;quot;: &amp;quot;default&amp;quot;, &amp;quot;logwatch&amp;quot;: &amp;quot;1&amp;quot;, &amp;quot;iurlmaxres&amp;quot;: &amp;quot;https:\/\/i1.ytimg.com\/vi\/f6MV89_80Wc\/maxresdefault.jpg&amp;quot;, &amp;quot;vq&amp;quot;: &amp;quot;auto&amp;quot;, &amp;quot;iurl&amp;quot;: &amp;quot;https:\/\/i1.ytimg.com\/vi\/f6MV89_80Wc\/hqdefault.jpg&amp;quot;, &amp;quot;showinfo&amp;quot;: &amp;quot;0&amp;quot;, &amp;quot;hl&amp;quot;: &amp;quot;en_US&amp;quot;, &amp;quot;quality_cap&amp;quot;: &amp;quot;highres&amp;quot;, &amp;quot;eventid&amp;quot;: &amp;quot;xk51U7XzONKj-QP9tYGgDQ&amp;quot;, &amp;quot;is_purchased&amp;quot;: false, &amp;quot;watch_ajax_token&amp;quot;: &amp;quot;QUFFLUhqbUx5WEprWjN3dUxHMWJTbFo2aUJiWFBaY1ZRZ3xBQ3Jtc0tubTh1anNQV1FrX0FwZ21FY1lrQ2lXeFBFUldiemRmTzltbFAzRksyWFBSaDNtYkc1aU00cWFTVWRMaWsyeG9ReWd6czl3Wk5wLXBROHJiN0VxUDNYajdYcWVWM0NPbFhmZWpCWk1UUmtYM0xZQjVnWQ==&amp;quot;, &amp;quot;allow_ratings&amp;quot;: 1, &amp;quot;user_gender&amp;quot;: &amp;quot;m&amp;quot;, &amp;quot;track_embed&amp;quot;: 0, &amp;quot;watermark&amp;quot;: &amp;quot;,https:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_watermark-vflHX6b6E.png,https:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_hd_watermark-vflAzLcD6.png&amp;quot;, &amp;quot;plid&amp;quot;: &amp;quot;AAT5eLlUnx0wN-EY&amp;quot;, &amp;quot;thumbnail_url&amp;quot;: &amp;quot;https:\/\/i1.ytimg.com\/vi\/f6MV89_80Wc\/default.jpg&amp;quot;, &amp;quot;sentiment&amp;quot;: 2, &amp;quot;video_id&amp;quot;: &amp;quot;f6MV89_80Wc&amp;quot;, &amp;quot;avg_rating&amp;quot;: 5.0, &amp;quot;referrer&amp;quot;: null, &amp;quot;dashmpd&amp;quot;: &amp;quot;https:\/\/manifest.googlevideo.com\/api\/manifest\/dash\/ip\/208.70.27.190\/key\/yt5\/sver\/3\/fexp\/927606%2C935705%2C941404%2C940908%2C936120%2C913434%2C939940%2C939944%2C936923%2C945044\/itag\/0\/source\/youtube\/playback_host\/r17---sn-nwj7kne6.googlevideo.com\/as\/fmp4_audio_clear%2Cwebm_audio_clear%2Cfmp4_sd_hd_clear%2Cwebm_sd_hd_clear\/ms\/au\/sparams\/as%2Cid%2Cip%2Cipbits%2Citag%2Cplayback_host%2Crequiressl%2Csource%2Cexpire\/requiressl\/yes\/mws\/yes\/ipbits\/0\/expire\/1400218541\/mt\/1400196716\/id\/o-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj\/upn\/9C7_5ah03XI\/signature\/B9BA23F2AB43EF6C48FF95995A1139D1D6331916.4B15CBCF582F2FBE9EC1FD4D1E3DEE4B048A9899\/mv\/m&amp;quot;, &amp;quot;ldpj&amp;quot;: &amp;quot;-12&amp;quot;, &amp;quot;length_seconds&amp;quot;: 343, &amp;quot;url_encoded_fmt_stream_map&amp;quot;: &amp;quot;fallback_host=tc.v18.cache3.googlevideo.com\u0026quality=hd720\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.64001F%2C+mp4a.40.2%22\u0026itag=22\u0026url=https%3A%2F%2Fr17---sn-nwj7kne6.googlevideo.com%2Fvideoplayback%3Fip%3D208.70.27.190%26key%3Dyt5%26mws%3Dyes%26fexp%3D927606%252C935705%252C941404%252C940908%252C936120%252C913434%252C939940%252C939944%252C936923%252C945044%26itag%3D22%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ratebypass%3Dyes%26uinitcwndbps%3D5992000%26sparams%3Did%252Cip%252Cipbits%252Citag%252Cratebypass%252Crequiressl%252Csource%252Cuinitcwndbps%252Cupn%252Cexpire%26requiressl%3Dyes%26ipbits%3D0%26ms%3Dau%26expire%3D1400218541%26mt%3D1400196716%26id%3Do-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj%26upn%3D4W79d7Gu5Jw%26signature%3D9B7488918FC278EA29F659960BEE055AE821F903.38AA7828850805FC4F612A6A17E72ABF18C38FCA,fallback_host=tc.v10.cache3.googlevideo.com\u0026quality=medium\u0026type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22\u0026itag=43\u0026url=https%3A%2F%2Fr17---sn-nwj7kne6.googlevideo.com%2Fvideoplayback%3Fip%3D208.70.27.190%26key%3Dyt5%26mws%3Dyes%26fexp%3D927606%252C935705%252C941404%252C940908%252C936120%252C913434%252C939940%252C939944%252C936923%252C945044%26itag%3D43%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ratebypass%3Dyes%26uinitcwndbps%3D5992000%26sparams%3Did%252Cip%252Cipbits%252Citag%252Cratebypass%252Crequiressl%252Csource%252Cuinitcwndbps%252Cupn%252Cexpire%26requiressl%3Dyes%26ipbits%3D0%26ms%3Dau%26expire%3D1400218541%26mt%3D1400196716%26id%3Do-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj%26upn%3D4W79d7Gu5Jw%26signature%3D6C00C9CCA86DFC1DCF67082BC696A0E48D7ADF08.776ACA7E0FAC4CC64E2AD1B00477D0F056F163,fallback_host=tc.v10.cache2.googlevideo.com\u0026quality=medium\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.42001E%2C+mp4a.40.2%22\u0026itag=18\u0026url=https%3A%2F%2Fr17---sn-nwj7kne6.googlevideo.com%2Fvideoplayback%3Fip%3D208.70.27.190%26key%3Dyt5%26mws%3Dyes%26fexp%3D927606%252C935705%252C941404%252C940908%252C936120%252C913434%252C939940%252C939944%252C936923%252C945044%26itag%3D18%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ratebypass%3Dyes%26uinitcwndbps%3D5992000%26sparams%3Did%252Cip%252Cipbits%252Citag%252Cratebypass%252Crequiressl%252Csource%252Cuinitcwndbps%252Cupn%252Cexpire%26requiressl%3Dyes%26ipbits%3D0%26ms%3Dau%26expire%3D1400218541%26mt%3D1400196716%26id%3Do-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj%26upn%3D4W79d7Gu5Jw%26signature%3D3AEF59C4FBF2A84C5BBEB310442D1C4138453FB3.2DEE85DB8A4BF31BCE92ADA41D59666845103CCB,fallback_host=tc.v12.cache4.googlevideo.com\u0026quality=small\u0026type=video%2Fx-flv\u0026itag=5\u0026url=https%3A%2F%2Fr17---sn-nwj7kne6.googlevideo.com%2Fvideoplayback%3Fip%3D208.70.27.190%26key%3Dyt5%26mws%3Dyes%26fexp%3D927606%252C935705%252C941404%252C940908%252C936120%252C913434%252C939940%252C939944%252C936923%252C945044%26itag%3D5%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26uinitcwndbps%3D5992000%26ms%3Dau%26sparams%3Did%252Cip%252Cipbits%252Citag%252Crequiressl%252Csource%252Cuinitcwndbps%252Cupn%252Cexpire%26requiressl%3Dyes%26ipbits%3D0%26expire%3D1400218541%26mt%3D1400196716%26id%3Do-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj%26upn%3D4W79d7Gu5Jw%26signature%3D4266B17038E8DDB18CAAA72257E87393EB502038.B3FBA8B5CA4BFE829BB79CC09E29BEDA4F23B712,fallback_host=tc.v2.cache2.googlevideo.com\u0026quality=small\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026itag=36\u0026url=https%3A%2F%2Fr17---sn-nwj7kne6.googlevideo.com%2Fvideoplayback%3Fip%3D208.70.27.190%26key%3Dyt5%26mws%3Dyes%26fexp%3D927606%252C935705%252C941404%252C940908%252C936120%252C913434%252C939940%252C939944%252C936923%252C945044%26itag%3D36%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26uinitcwndbps%3D5992000%26ms%3Dau%26sparams%3Did%252Cip%252Cipbits%252Citag%252Crequiressl%252Csource%252Cuinitcwndbps%252Cupn%252Cexpire%26requiressl%3Dyes%26ipbits%3D0%26expire%3D1400218541%26mt%3D1400196716%26id%3Do-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj%26upn%3D4W79d7Gu5Jw%26signature%3D458D350E6794E3E0D5227442A16E46E95E60DDFC.5D80AC2247DCA6C325358881BDD7E8F3B62D2BCA,fallback_host=tc.v15.cache6.googlevideo.com\u0026quality=small\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026itag=17\u0026url=https%3A%2F%2Fr17---sn-nwj7kne6.googlevideo.com%2Fvideoplayback%3Fip%3D208.70.27.190%26key%3Dyt5%26mws%3Dyes%26fexp%3D927606%252C935705%252C941404%252C940908%252C936120%252C913434%252C939940%252C939944%252C936923%252C945044%26itag%3D17%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26uinitcwndbps%3D5992000%26ms%3Dau%26sparams%3Did%252Cip%252Cipbits%252Citag%252Crequiressl%252Csource%252Cuinitcwndbps%252Cupn%252Cexpire%26requiressl%3Dyes%26ipbits%3D0%26expire%3D1400218541%26mt%3D1400196716%26id%3Do-ABd1wtC7lMy8Izs7zy3FECKHB29kJNKVWfwxMlLt2eqj%26upn%3D4W79d7Gu5Jw%26signature%3D5301503384BBDFA72C02A6D6479CBFA8E06BDF85.326A10A482D488E4A58E704F6803E0AB99529F42&amp;quot;, &amp;quot;dash&amp;quot;: &amp;quot;1&amp;quot;, &amp;quot;has_cc&amp;quot;: false, &amp;quot;enablejsapi&amp;quot;: 1, &amp;quot;ftoken&amp;quot;: &amp;quot;QUFFLUhqa25MTEl0ODFNaTZaLTNNNnd5VXl6X00wVk9fQXxBQ3Jtc0ttVjV6d2QzMFBPNjFRWWpBNy1rZkVJSmU1RnJVZ2JVczJWNlRtWVFPTXpYOXFkaHozR3o2U2tfY0FKX2Y4UnBjRGR0dzRKcUI5WElOM3h4eG1XdTlSSGRKeUFHMGw2QnZ1bWpLcjBwWm5kN0xFYzJ3aw==&amp;quot;, &amp;quot;pltype&amp;quot;: &amp;quot;contentugc&amp;quot;, &amp;quot;fmt_list&amp;quot;: &amp;quot;22\/1280x720\/9\/0\/115,43\/640x360\/99\/0\/0,18\/640x360\/9\/0\/115,5\/320x240\/7\/0\/0,36\/320x240\/99\/1\/0,17\/176x144\/99\/1\/0&amp;quot;, &amp;quot;timestamp&amp;quot;: 1400196807, &amp;quot;is_video_preview&amp;quot;: false, &amp;quot;account_playback_token&amp;quot;: &amp;quot;QUFFLUhqay02aFdkbU5sSXQ1Zkl4UDFNaHdRbmxFU3pjZ3xBQ3Jtc0tuaklYV2c5ZkxPRDZ3VVhrSmU2bWxkYzlyaUVfNDBtcWRsRjBwZmFzNC0zNzBiX25nSlhjTnFLSGxTMDF5WUFZMjZZT0d0aWdyV21CYXBZSkVYa1pJTml1dGR3QV9vUVR0YTZwb2Mxd3YxajJiUjZRaw==&amp;quot;, &amp;quot;ptk&amp;quot;: &amp;quot;youtube_none&amp;quot;}, &amp;quot;assets&amp;quot;: {&amp;quot;js&amp;quot;: &amp;quot;\/\/s.ytimg.com\/yts\/jsbin\/html5player-en_US-vflzEDYyE.js&amp;quot;, &amp;quot;html&amp;quot;: &amp;quot;\/html5_player_template&amp;quot;, &amp;quot;css&amp;quot;: &amp;quot;\/\/s.ytimg.com\/yts\/cssbin\/www-player-vflbzCGhL.css&amp;quot;}, &amp;quot;params&amp;quot;: {&amp;quot;allowscriptaccess&amp;quot;: &amp;quot;always&amp;quot;, &amp;quot;allowfullscreen&amp;quot;: &amp;quot;true&amp;quot;, &amp;quot;bgcolor&amp;quot;: &amp;quot;#000000&amp;quot;}, &amp;quot;attrs&amp;quot;: {&amp;quot;id&amp;quot;: &amp;quot;c4-player&amp;quot;}, &amp;quot;url_v9as2&amp;quot;: &amp;quot;https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflr2PFkb\/cps.swf&amp;quot;, &amp;quot;url_v8&amp;quot;: &amp;quot;https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflr2PFkb\/cps.swf&amp;quot;, &amp;quot;url&amp;quot;: &amp;quot;https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflr2PFkb\/watch_as3.swf&amp;quot;}">
  </div>

  </div>

        <div class="video-detail">
      <h3 class="title">
        <a href="/watch?v=f6MV89_80Wc" title="&quot;I Heart BC&quot; Song (We Are) - Broward College" class="yt-uix-sessionlink yt-ui-ellipsis yt-ui-ellipsis-2 spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview">
          &quot;I Heart BC&quot; Song (We Are) - Broward College
        </a>
      </h3>
      <div class="view-count">
        <span class="count">
          38 views
        </span>
          <span class="content-item-time-created">
            1 week ago
          </span>
      </div>
      <div class="description yt-uix-expander yt-uix-expander-ellipsis yt-ui-ellipsis-10 yt-uix-expander-collapsed">
        <div class="yt-ui-ellipsis yt-ui-ellipsis-10" >
          A song by the students expressing our love of Broward College!<br /><br />Like us on Facebook! <a href="https://www.facebook.com/BCCentralStudentLife" target="_blank" title="https://www.facebook.com/BCCentralStudentLife" rel="nofollow" dir="ltr" class="yt-uix-redirect-link">https://www.facebook.com/BC...</a> <br />Check us on Instagram! <a href="http://instagram.com/bccentralstudentlife" target="_blank" title="http://instagram.com/bccentralstudentlife" rel="nofollow" dir="ltr" class="yt-uix-redirect-link">http://instagram.com/bccent...</a> <br />Subscribe! <a href="http://www.youtube.com/user/BCCentralStudentLife?feature=watch" target="_blank" title="http://www.youtube.com/user/BCCentralStudentLife?feature=watch" rel="nofollow" dir="ltr" class="yt-uix-redirect-link">http://www.youtube.com/user...</a> <br />Visit Broward College&#39;s website! <a href="http://www.broward.edu/Pages/home.aspx" target="_blank" title="http://www.broward.edu/Pages/home.aspx" rel="nofollow" dir="ltr" class="yt-uix-redirect-link">http://www.broward.edu/Page...</a><br /><br />The Student Life department at Broward College Central Campus (A. Hugh Adams Central Campus) is dedicated to student engagement on and off campus. We promote student leadership, cultural diversity, and enhance the college experience through different activities and events.<br /><br />No copyright infringement intended.
          <a class="yt-uix-expander-head">
Show less
          </a>
        </div>
        <a class="yt-uix-expander-head">
Read more
        </a>
      </div>
  </div>

      <div class="video-content-info">
      </div>
    </div>
  </div>

  </div>

      </div>
  </div>

      <div id="c4-shelves-container">
        
          <div class="compact-shelf shelf-item yt-uix-shelfslider yt-uix-shelfslider-at-head yt-uix-shelfslider-at-tail vve-check clearfix branded-page-box yt-section-hover-container fluid-shelf yt-uix-tdl"  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CBYQ3BwoAA">
            <h2 class="branded-page-module-title">
      <a href="/user/BCCentralStudentLife/videos?sort=dd&amp;view=0&amp;shelf_id=1" class="yt-uix-sessionlink branded-page-module-title-link spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">
            <span class="branded-page-module-title-text">
      <span class="" >Uploads</span>
    </span>

      </a>
        <a href="/watch?v=LqK_az3E55g&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="yt-uix-button  shelves-play yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-play-all"></span><span class="yt-uix-button-content">Play </span></a>

  </h2>


    

    <div class="compact-shelf-content-container">
        <div class="yt-uix-shelfslider-body">
    <ul class="yt-uix-shelfslider-list">
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=LqK_az3E55g&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CBkQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/LqK_az3E55g/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="LqK_az3E55g" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">10:40</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Student Life Awards Cold Open 2014" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CBgQvxs" href="/watch?v=LqK_az3E55g&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Student Life Awards Cold Open 2014</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>35 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 day ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=f6MV89_80Wc&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink watched yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CBwQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/f6MV89_80Wc/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
<div class="watched-badge">WATCHED</div>

  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="f6MV89_80Wc" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">5:43</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="&quot;I Heart BC&quot; Song (We Are) - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CBsQvxs" href="/watch?v=f6MV89_80Wc&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">&quot;I Heart BC&quot; Song (We Are) - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>38 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 week ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=Suw3vLbyt1I&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink watched yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CB8QwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/Suw3vLbyt1I/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
<div class="watched-badge">WATCHED</div>

  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="Suw3vLbyt1I" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">5:43</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="&quot;I Heart BC&quot; Song (We Are) - Student Life Awards Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CB4Qvxs" href="/watch?v=Suw3vLbyt1I&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">&quot;I Heart BC&quot; Song (We Are) - Student Life Awards Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>143 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 week ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=VBTVaT6F0HA&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCIQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/VBTVaT6F0HA/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="VBTVaT6F0HA" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:31</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="I ♥ BC Festival! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCEQvxs" href="/watch?v=VBTVaT6F0HA&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">I ♥ BC Festival! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>78 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 month ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=DdsdjuGHo-I&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCUQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/DdsdjuGHo-I/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="DdsdjuGHo-I" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:56</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Thank You! - Student Government" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCQQvxs" href="/watch?v=DdsdjuGHo-I&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Thank You! - Student Government</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>15 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 month ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=fnwm1USZmFo&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCgQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/fnwm1USZmFo/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="fnwm1USZmFo" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:19</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="I Heart BC Campaign" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCcQvxs" href="/watch?v=fnwm1USZmFo&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">I Heart BC Campaign</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>37 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 month ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=nroBeHlLkcY&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCsQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/nroBeHlLkcY/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="nroBeHlLkcY" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">8:19</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Embracing Inner Beauty - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CCoQvxs" href="/watch?v=nroBeHlLkcY&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Embracing Inner Beauty - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>111 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 month ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=cdGyyL-cIzY&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CC4QwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/cdGyyL-cIzY/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="cdGyyL-cIzY" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:01</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Finals Week! - Broward College Central Campus" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CC0Qvxs" href="/watch?v=cdGyyL-cIzY&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Finals Week! - Broward College Central Campus</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>62 views</li>
        <li class="yt-lockup-deemphasized-text">
            3 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=R90JNQHXmAk&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDEQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/R90JNQHXmAk/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="R90JNQHXmAk" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:55</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Hair Culture!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDAQvxs" href="/watch?v=R90JNQHXmAk&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Hair Culture!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>84 views</li>
        <li class="yt-lockup-deemphasized-text">
            3 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=1YgxvqCyfIc&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDQQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/1YgxvqCyfIc/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="1YgxvqCyfIc" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:48</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Club Rush 2014! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDMQvxs" href="/watch?v=1YgxvqCyfIc&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Club Rush 2014! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>101 views</li>
        <li class="yt-lockup-deemphasized-text">
            3 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=aGwLLe0kVCs&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDcQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/aGwLLe0kVCs/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="aGwLLe0kVCs" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:44</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Club Rush 2014 Promo! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDYQvxs" href="/watch?v=aGwLLe0kVCs&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Club Rush 2014 Promo! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>88 views</li>
        <li class="yt-lockup-deemphasized-text">
            3 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=3Pc3Z10lZco&amp;list=UUo50hV2EIx4YHc58L0RZDDQ" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDoQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/3Pc3Z10lZco/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="3Pc3Z10lZco" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:43</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Chili Cook-off 2013! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CDkQvxs" href="/watch?v=3Pc3Z10lZco&amp;list=UUo50hV2EIx4YHc58L0RZDDQ">Chili Cook-off 2013! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>91 views</li>
        <li class="yt-lockup-deemphasized-text">
            4 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item compact-shelf-view-all-card yt-valign">
          <h4 class="compact-shelf-view-all-card-link yt-valign-container">
            <a href="/user/BCCentralStudentLife/videos?sort=dd&view=0&shelf_id=1" class=" yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">30+ more</a>
          </h4>
        </li>
    </ul>
  </div>


      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-prev yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-prev-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Previous">
 </span></button>
      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-next yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-next-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Next">
 </span></button>
    </div>

  </div>

  


        
          <div class="compact-shelf shelf-item yt-uix-shelfslider yt-uix-shelfslider-at-head yt-uix-shelfslider-at-tail vve-check clearfix branded-page-box yt-section-hover-container fluid-shelf yt-uix-tdl"  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CDsQ3BwoAQ">
            <h2 class="branded-page-module-title">
      <a href="/user/BCCentralStudentLife/videos?sort=p&amp;view=0&amp;shelf_id=2" class="yt-uix-sessionlink branded-page-module-title-link spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">
            <span class="branded-page-module-title-text">
      <span class="" >Popular uploads</span>
    </span>

      </a>
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;title=Popular+uploads&amp;more_url=&amp;type=0&amp;feature=c4-overview-u" class="yt-uix-button  shelves-play yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-play-all"></span><span class="yt-uix-button-content">Play </span></a>

  </h2>


    

    <div class="compact-shelf-content-container">
        <div class="yt-uix-shelfslider-body">
    <ul class="yt-uix-shelfslider-list">
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;title=Popular+uploads&amp;more_url=&amp;type=0&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CD4QwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/fAtCDE9WjRA/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="fAtCDE9WjRA" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:30</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Question Every Possibility - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CD0Qvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;title=Popular+uploads&amp;more_url=&amp;type=0&amp;feature=c4-overview-u">Question Every Possibility - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>1,872 views</li>
        <li class="yt-lockup-deemphasized-text">
            8 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=1&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEEQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/5NxZIa6nZ6Y/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="5NxZIa6nZ6Y" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:02</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Welcome to Student Life! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEAQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=1&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Welcome to Student Life! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>733 views</li>
        <li class="yt-lockup-deemphasized-text">
            11 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=2&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEQQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/jAoch-yjcs8/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="jAoch-yjcs8" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">11:41</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Award Ceremony Almost Goes Wrong! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEMQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=2&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Award Ceremony Almost Goes Wrong! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>271 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=3&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEcQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/dgfkTFBTjbk/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="dgfkTFBTjbk" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:56</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Thank You" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEYQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=3&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Thank You</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>208 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=4&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEoQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/9L04sSZbytU/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="9L04sSZbytU" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">10:53</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Student Life - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEkQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=4&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Student Life - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>193 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=5&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CE0QwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/7TJFUMsb_PI/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="7TJFUMsb_PI" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:26</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Spring Welcome Back 2012 - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CEwQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=5&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Spring Welcome Back 2012 - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>174 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=6&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFAQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/Ab0P66ELadg/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="Ab0P66ELadg" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:46</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Board Of Trustees Surveys! - Student Government" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CE8Qvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=6&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Board Of Trustees Surveys! - Student Government</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>166 views</li>
        <li class="yt-lockup-deemphasized-text">
            5 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=7&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFMQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/wm0ijyhYySI/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="wm0ijyhYySI" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">5:06</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Karaoke Highlights! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFIQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=7&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Karaoke Highlights! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>141 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=8&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFYQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/Nu-Su1YR05M/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="Nu-Su1YR05M" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:01</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Finals Week! - Broward College Central Campus" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFUQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=8&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Finals Week! - Broward College Central Campus</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>148 views</li>
        <li class="yt-lockup-deemphasized-text">
            5 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=9&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFkQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/TRsr-LP8Iqg/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="TRsr-LP8Iqg" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:33</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Dance Central Tournament" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFgQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=9&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Dance Central Tournament</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>118 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=10&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFwQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/2BChJXW9cXo/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="2BChJXW9cXo" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:03</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="CAB Office" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CFsQvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=10&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">CAB Office</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>118 views</li>
        <li class="yt-lockup-deemphasized-text">
            10 months ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=11&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CF8QwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/z27_S2XKM30/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="z27_S2XKM30" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:06</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Welcome Back Week! (Part 1) - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-u&amp;ved=CF4Qvxs" href="/watch_videos?video_ids=fAtCDE9WjRA%2C5NxZIa6nZ6Y%2CjAoch-yjcs8%2CdgfkTFBTjbk%2C9L04sSZbytU%2C7TJFUMsb_PI%2CAb0P66ELadg%2Cwm0ijyhYySI%2CNu-Su1YR05M%2CTRsr-LP8Iqg%2C2BChJXW9cXo%2Cz27_S2XKM30&amp;index=11&amp;type=0&amp;title=Popular+uploads&amp;more_url=&amp;feature=c4-overview-u">Welcome Back Week! (Part 1) - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
      <li>112 views</li>
        <li class="yt-lockup-deemphasized-text">
            1 year ago
        </li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item compact-shelf-view-all-card yt-valign">
          <h4 class="compact-shelf-view-all-card-link yt-valign-container">
            <a href="/user/BCCentralStudentLife/videos?sort=p&view=0&shelf_id=2" class=" yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">30+ more</a>
          </h4>
        </li>
    </ul>
  </div>


      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-prev yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-prev-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Previous">
 </span></button>
      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-next yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-next-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Next">
 </span></button>
    </div>

  </div>

  


        
          <div class="compact-shelf shelf-item yt-uix-shelfslider yt-uix-shelfslider-at-head yt-uix-shelfslider-at-tail vve-check clearfix branded-page-box yt-section-hover-container fluid-shelf yt-uix-tdl"  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CGAQ3BwoAg">
            <h2 class="branded-page-module-title">
      <a href="/playlist?list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="yt-uix-sessionlink branded-page-module-title-link spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">
            <span class="branded-page-module-title-text">
      <span class="" >Student Life</span>
    </span>

      </a>
        <a href="/watch?v=dgfkTFBTjbk&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="yt-uix-button  shelves-play yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-play-all"></span><span class="yt-uix-button-content">Play </span></a>

  </h2>


    

    <div class="compact-shelf-content-container">
        <div class="yt-uix-shelfslider-body">
    <ul class="yt-uix-shelfslider-list">
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=dgfkTFBTjbk&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGQQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/dgfkTFBTjbk/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="dgfkTFBTjbk" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:56</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Thank You" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGIQvxs" href="/watch?v=dgfkTFBTjbk&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Thank You</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGMQwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>208 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=dbOyqFwm7uY&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGgQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/dbOyqFwm7uY/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="dbOyqFwm7uY" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">4:28</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="September 11 Commemoration Ceremony - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGYQvxs" href="/watch?v=dbOyqFwm7uY&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">September 11 Commemoration Ceremony - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGcQwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>81 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=9L04sSZbytU&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGwQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/9L04sSZbytU/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="9L04sSZbytU" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">10:53</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Student Life - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGoQvxs" href="/watch?v=9L04sSZbytU&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Student Life - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CGsQwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>193 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=eyu8aPJ5ABA&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHAQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/eyu8aPJ5ABA/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="eyu8aPJ5ABA" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:01</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Student Government 2012 - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CG4Qvxs" href="/watch?v=eyu8aPJ5ABA&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Student Government 2012 - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
              <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" title="Unlisted" alt="Unlisted" class="video-unlisted-icon">

        </li>
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CG8QwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>26 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=nKL5KSm6-3Q&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHQQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/nKL5KSm6-3Q/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="nKL5KSm6-3Q" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:22</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Ambassadors Assemble!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHIQvxs" href="/watch?v=nKL5KSm6-3Q&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Ambassadors Assemble!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHMQwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>83 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=5NxZIa6nZ6Y&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHgQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/5NxZIa6nZ6Y/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="5NxZIa6nZ6Y" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:02</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Welcome to Student Life! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHYQvxs" href="/watch?v=5NxZIa6nZ6Y&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Welcome to Student Life! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHcQwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>733 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=QFtsE3acVho&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHwQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/QFtsE3acVho/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="QFtsE3acVho" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:46</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Student Life Pool Party (Recap)" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHoQvxs" href="/watch?v=QFtsE3acVho&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Student Life Pool Party (Recap)</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CHsQwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>123 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=fAtCDE9WjRA&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIABEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/fAtCDE9WjRA/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="fAtCDE9WjRA" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:30</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Question Every Possibility - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CH4Qvxs" href="/watch?v=fAtCDE9WjRA&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Question Every Possibility - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CH8QwRs" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>1,872 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=NpaPFV6iP14&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIQBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/NpaPFV6iP14/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="NpaPFV6iP14" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">8:56</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Behind The Scenes! - Award Ceremony Almost Goes Wrong! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIIBEL8b" href="/watch?v=NpaPFV6iP14&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Behind The Scenes! - Award Ceremony Almost Goes Wrong! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIMBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>94 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=gC_fVWgDS9k&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIgBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/gC_fVWgDS9k/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="gC_fVWgDS9k" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:41</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Win A Free Kindle Fire HD! - I &#39;Heart&#39; BC Campaign" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIYBEL8b" href="/watch?v=gC_fVWgDS9k&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Win A Free Kindle Fire HD! - I &#39;Heart&#39; BC Campaign</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIcBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>98 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=vnoanT3HVJs&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIwBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/vnoanT3HVJs/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="vnoanT3HVJs" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:06</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Hispanic Heritage Festival! - Broward College Student Life" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIoBEL8b" href="/watch?v=vnoanT3HVJs&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Hispanic Heritage Festival! - Broward College Student Life</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CIsBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>77 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=wbNEeW6SU1s&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJABEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/wbNEeW6SU1s/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="wbNEeW6SU1s" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:55</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Ribbon Cutting Ceremony" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CI4BEL8b" href="/watch?v=wbNEeW6SU1s&amp;list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt">Ribbon Cutting Ceremony</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CI8BEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>52 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item compact-shelf-view-all-card yt-valign">
          <h4 class="compact-shelf-view-all-card-link yt-valign-container">
            <a href="/playlist?list=PLClm8SGlN5rYjBF6PDYuhG45JAUd6IPLt" class=" yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">5 more</a>
          </h4>
        </li>
    </ul>
  </div>


      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-prev yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-prev-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Previous">
 </span></button>
      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-next yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-next-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Next">
 </span></button>
    </div>

  </div>

  


        
          <div class="compact-shelf shelf-item yt-uix-shelfslider yt-uix-shelfslider-at-head yt-uix-shelfslider-at-tail vve-check clearfix branded-page-box yt-section-hover-container fluid-shelf yt-uix-tdl"  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CJEBENwcKAM">
            <h2 class="branded-page-module-title">
      <a href="/playlist?list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="yt-uix-sessionlink branded-page-module-title-link spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">
            <span class="branded-page-module-title-text">
      <span class="" >Office of Volunteering and Leadership (OVAL)</span>
    </span>

      </a>
        <a href="/watch?v=DqaHXwaNlCc&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="yt-uix-button  shelves-play yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-play-all"></span><span class="yt-uix-button-content">Play </span></a>

  </h2>


    

    <div class="compact-shelf-content-container">
        <div class="yt-uix-shelfslider-body">
    <ul class="yt-uix-shelfslider-list">
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=DqaHXwaNlCc&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJUBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/DqaHXwaNlCc/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="DqaHXwaNlCc" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:27</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Miami Zoo - OVAL" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJMBEL8b" href="/watch?v=DqaHXwaNlCc&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Miami Zoo - OVAL</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJQBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>107 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=nnG0DpgAsZI&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJkBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/nnG0DpgAsZI/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="nnG0DpgAsZI" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:45</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Park Cleanup! - (Video Recap)" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJcBEL8b" href="/watch?v=nnG0DpgAsZI&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Park Cleanup! - (Video Recap)</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJgBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>52 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=CIP52DDYm_s&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJ0BEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/CIP52DDYm_s/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="CIP52DDYm_s" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:57</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Veteran&#39;s Day!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJsBEL8b" href="/watch?v=CIP52DDYm_s&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Veteran&#39;s Day!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJwBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>45 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=Zu6FxfspNxI&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKEBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/Zu6FxfspNxI/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="Zu6FxfspNxI" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:30</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Gumbo Limbo! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CJ8BEL8b" href="/watch?v=Zu6FxfspNxI&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Gumbo Limbo! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKABEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>25 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=hAuW_YxxfiA&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKUBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/hAuW_YxxfiA/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="hAuW_YxxfiA" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:12</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Flamingo Gardens!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKMBEL8b" href="/watch?v=hAuW_YxxfiA&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Flamingo Gardens!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKQBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>20 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=lmjoQLbQmSo&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKkBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/lmjoQLbQmSo/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="lmjoQLbQmSo" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:34</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Cross Road Food Bank" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKcBEL8b" href="/watch?v=lmjoQLbQmSo&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Cross Road Food Bank</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKgBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>50 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=ApqFqv1jn4A&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CK0BEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/ApqFqv1jn4A/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="ApqFqv1jn4A" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:26</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Veteran&#39;s Day" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKsBEL8b" href="/watch?v=ApqFqv1jn4A&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Veteran&#39;s Day</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CKwBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>22 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=ZqmqOwlwE-A&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLEBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/ZqmqOwlwE-A/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="ZqmqOwlwE-A" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:57</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Earth Day!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CK8BEL8b" href="/watch?v=ZqmqOwlwE-A&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Earth Day!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLABEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>31 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=a_AxVXdsD0M&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLUBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/a_AxVXdsD0M/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="a_AxVXdsD0M" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:19</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Veteran&#39;s Appreciation Day! 2013 - Broward College Central Campus" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLMBEL8b" href="/watch?v=a_AxVXdsD0M&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Veteran&#39;s Appreciation Day! 2013 - Broward College Central Campus</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLQBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>51 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=mOCRNcjYszE&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLkBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/mOCRNcjYszE/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="mOCRNcjYszE" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:30</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Recycling Day! - Broward College Central Campus" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLcBEL8b" href="/watch?v=mOCRNcjYszE&amp;list=PLClm8SGlN5rbN6zjXJG-o3YlAUJIzubBs">Recycling Day! - Broward College Central Campus</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLgBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>71 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
    </ul>
  </div>


      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-prev yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-prev-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Previous">
 </span></button>
      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-next yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-next-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Next">
 </span></button>
    </div>

  </div>

  


        
          <div class="compact-shelf shelf-item yt-uix-shelfslider yt-uix-shelfslider-at-head yt-uix-shelfslider-at-tail vve-check clearfix branded-page-box yt-section-hover-container fluid-shelf yt-uix-tdl"  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=CLoBENwcKAQ">
            <h2 class="branded-page-module-title">
      <a href="/playlist?list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="yt-uix-sessionlink branded-page-module-title-link spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">
            <span class="branded-page-module-title-text">
      <span class="" >Campus Activities Board (CAB)</span>
    </span>

      </a>
        <a href="/watch?v=tiJ9-qbPI94&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="yt-uix-button  shelves-play yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-play-all"></span><span class="yt-uix-button-content">Play </span></a>

  </h2>


    

    <div class="compact-shelf-content-container">
        <div class="yt-uix-shelfslider-body">
    <ul class="yt-uix-shelfslider-list">
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=tiJ9-qbPI94&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CL4BEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/tiJ9-qbPI94/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="tiJ9-qbPI94" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">0:45</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Welcome Back BBQ 2013 (Recap)" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CLwBEL8b" href="/watch?v=tiJ9-qbPI94&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Welcome Back BBQ 2013 (Recap)</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CL0BEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>68 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=zbYNk8yq8cs&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMIBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/zbYNk8yq8cs/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="zbYNk8yq8cs" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">4:14</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Fall Fest 2012! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMABEL8b" href="/watch?v=zbYNk8yq8cs&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Fall Fest 2012! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMEBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>92 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=KU-vo4nHdzY&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMYBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/KU-vo4nHdzY/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="KU-vo4nHdzY" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:22</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Welcome Week and Club Rush!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMQBEL8b" href="/watch?v=KU-vo4nHdzY&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Welcome Week and Club Rush!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMUBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>72 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=owoBrhJSC4c&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMoBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/owoBrhJSC4c/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="owoBrhJSC4c" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:07</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Chili Cookoff 2012!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMgBEL8b" href="/watch?v=owoBrhJSC4c&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Chili Cookoff 2012!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMkBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>71 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=pDVf2BLaLcU&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CM4BEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/pDVf2BLaLcU/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="pDVf2BLaLcU" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:00</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Fall Fest 2012 Promo" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CMwBEL8b" href="/watch?v=pDVf2BLaLcU&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Fall Fest 2012 Promo</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CM0BEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>56 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=eUwpZoVnbxc&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNIBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/eUwpZoVnbxc/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="eUwpZoVnbxc" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:46</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Hispanic Heritage Festival!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNABEL8b" href="/watch?v=eUwpZoVnbxc&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Hispanic Heritage Festival!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNEBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>28 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=7TJFUMsb_PI&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNYBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/7TJFUMsb_PI/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="7TJFUMsb_PI" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:26</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Spring Welcome Back 2012 - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNQBEL8b" href="/watch?v=7TJFUMsb_PI&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Spring Welcome Back 2012 - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNUBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>174 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=PZeWQbP1Uj0&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNoBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/PZeWQbP1Uj0/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="PZeWQbP1Uj0" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:46</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Fall Fest 2011! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNgBEL8b" href="/watch?v=PZeWQbP1Uj0&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Fall Fest 2011! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNkBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>31 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=RX52fXIO-hQ&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CN4BEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/RX52fXIO-hQ/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="RX52fXIO-hQ" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">3:06</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Chili Cookoff! - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CNwBEL8b" href="/watch?v=RX52fXIO-hQ&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Chili Cookoff! - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CN0BEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>24 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=5JYRlbvtUs8&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COIBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/5JYRlbvtUs8/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="5JYRlbvtUs8" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:45</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Hispanic Heritage - Day 3" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COABEL8b" href="/watch?v=5JYRlbvtUs8&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Hispanic Heritage - Day 3</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COEBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>31 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=1Cl8_xEWdzE&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COYBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/1Cl8_xEWdzE/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="1Cl8_xEWdzE" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:21</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Hispanic Heritage (Day 2) - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COQBEL8b" href="/watch?v=1Cl8_xEWdzE&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Hispanic Heritage (Day 2) - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COUBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>64 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=4vDCc418XUw&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COoBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/4vDCc418XUw/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="4vDCc418XUw" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">2:49</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Hispanic Heritage (Day 1) - Broward College" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COgBEL8b" href="/watch?v=4vDCc418XUw&amp;list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt">Hispanic Heritage (Day 1) - Broward College</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=COkBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>53 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item compact-shelf-view-all-card yt-valign">
          <h4 class="compact-shelf-view-all-card-link yt-valign-container">
            <a href="/playlist?list=PLClm8SGlN5raGhDFox55zVjbyrEL68CTt" class=" yt-uix-sessionlink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">8 more</a>
          </h4>
        </li>
    </ul>
  </div>


      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-prev yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-prev-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Previous">
 </span></button>
      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-next yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-next-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Next">
 </span></button>
    </div>

  </div>

  


        
          <div class="compact-shelf shelf-item yt-uix-shelfslider yt-uix-shelfslider-at-head yt-uix-shelfslider-at-tail vve-check clearfix branded-page-box yt-section-hover-container fluid-shelf yt-uix-tdl"  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;ved=COsBENwcKAU">
            <h2 class="branded-page-module-title">
      <a href="/playlist?list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c" class="yt-uix-sessionlink branded-page-module-title-link spf-nolink" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ">
            <span class="branded-page-module-title-text">
      <span class="" >Health and Wellness Knowledge (HAWK)</span>
    </span>

      </a>
        <a href="/watch?v=u4dMRcMKq2w&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c" class="yt-uix-button  shelves-play yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-small" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-play-all"></span><span class="yt-uix-button-content">Play </span></a>

  </h2>


    

    <div class="compact-shelf-content-container">
        <div class="yt-uix-shelfslider-body">
    <ul class="yt-uix-shelfslider-list">
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=u4dMRcMKq2w&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CO8BEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/u4dMRcMKq2w/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="u4dMRcMKq2w" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:57</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Minute to Win It!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CO0BEL8b" href="/watch?v=u4dMRcMKq2w&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c">Minute to Win It!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CO4BEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>74 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=TRsr-LP8Iqg&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CPMBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/TRsr-LP8Iqg/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="TRsr-LP8Iqg" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:33</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Dance Central Tournament" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CPEBEL8b" href="/watch?v=TRsr-LP8Iqg&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c">Dance Central Tournament</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CPIBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>118 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
        <li class="channels-content-item yt-shelf-grid-item yt-uix-shelfslider-item ">
            



    <div class="yt-lockup clearfix  yt-lockup-video yt-lockup-grid"
  >
    <div class="yt-lockup-thumbnail"
    >
        <a href="/watch?v=K1ddteHHBHs&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c" class="ux-thumb-wrap yt-uix-sessionlink yt-fluid-thumb-link contains-addto "  data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CPcBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-185 yt-thumb-fluid"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="//i1.ytimg.com/vi/K1ddteHHBHs/mqdefault.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="185"  >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>


  <button title="Watch Later" onclick=";return false;" type="button" class="addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-button yt-uix-button-default yt-uix-button-size-small yt-uix-tooltip" data-video-ids="K1ddteHHBHs" role="button"><span class="yt-uix-button-content">  <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span></button>
    <span class="video-time">1:07</span>
</a>

    </div>
    <div class="yt-lockup-content">
          <h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="HAWK Event!" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CPUBEL8b" href="/watch?v=K1ddteHHBHs&amp;list=PLClm8SGlN5rY1mwj9pHrPFstJgUAohP_c">HAWK Event!</a></h3>

  <div class="yt-lockup-meta">
    <ul class="yt-lockup-meta-info">
        <li>
          
by <a href="/user/BCCentralStudentLife" class="g-hovercard yt-uix-sessionlink yt-user-name " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=c4-overview-vl&amp;ved=CPYBEMEb" dir="ltr" data-ytid="UCo50hV2EIx4YHc58L0RZDDQ" data-name="c4-overview-vl">BCCentralStudentLife</a>
        </li>
      <li>40 views</li>
    </ul>
  </div>
  
  
  

    </div>
    
  </div>



        </li>
    </ul>
  </div>


      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-prev yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-prev-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Previous">
 </span></button>
      <button onclick=";return false;" type="button" class="yt-uix-shelfslider-next yt-uix-button yt-uix-button-shelf-slider-pager yt-uix-button-size-default"  role="button"><span class="yt-uix-button-content">  <img class="yt-uix-shelfslider-next-arrow" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Next">
 </span></button>
    </div>

  </div>

  


    </div>





  

        


  <div id="ad_creative_1" class="ad-div hid" style="z-index: 1">
    <div id="ad_creative_div_1"></div>
    <script>(function() {function tagMpuIframe() {var containerEl = document.getElementById('ad_creative_div_1');if (!containerEl) {return;}var iframeEl = document.createElement('iframe');var iframeSrc = 'https://ad.doubleclick.net/N4061/adi/com.ytbc/BCCentralStudentLife;sz=1x1;tile=1;ssl=1;dc_yt=1;k18=1;k21=1;kage=41;kar=5;kauth=1;kga=1003;kgender=m;kgg=1;klg=en;kmyd=ad_creative_1;ytexp=927606,935705,941404,940908,936120;ord=' +Math.floor(Math.random() * 10000000000000000) +'?';iframeEl.id = 'ad_creative_iframe_1';iframeEl.width = '1';iframeEl.height = '1';iframeEl.style.cssText = 'z-index:1;';iframeEl.scrolling = 'no';iframeEl.frameBorder = '0';containerEl.appendChild(iframeEl);iframeEl.src = iframeSrc;}tagMpuIframe();})();</script>
  </div>



  </div>

          </div>
        </div>
          <div class="branded-page-v2-secondary-col">
            

    

        <div class="branded-page-related-channels branded-page-box  yt-card" >
            <h2 class="branded-page-module-title yt-uix-tooltip" data-tooltip-text="These recommendations have been automatically generated by YouTube." dir="ltr">
        Popular channels on YouTube
    </h2>

          <ul class="branded-page-related-channels-list">
        <li class="branded-page-related-channels-item spf-nolink clearfix" data-external-id="UCrAb_x80PtTiN3lCkQOSFPg">
    




    <span class="yt-lockup clearfix  yt-lockup-channel yt-lockup-mini"
  >
    <div class="yt-lockup-thumbnail"
        style="width: 34px;"
    >
        <a href="/user/portaltvperu" class="ux-thumb-wrap yt-uix-sessionlink " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CPwBEMAb">    <span class="video-thumb  yt-thumb yt-thumb-34 g-hovercard"
        data-ytid="UCrAb_x80PtTiN3lCkQOSFPg"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="https://yt3.ggpht.com/-cKWAs8vVghI/AAAAAAAAAAI/AAAAAAAAAAA/Jlft1Nw58Dw/s176-c-k-no/photo.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="34"  height="34" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</a>

    </div>
    <div class="yt-lockup-content">
          <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text g-hovercard" data-ytid="UCrAb_x80PtTiN3lCkQOSFPg" data-name="rc-rel"             ><h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link " dir="ltr" title="TVPerú Televisión Peruana" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CPoBEL8b" href="/user/portaltvperu">TVPerú Televisión Peruana</a></h3></span></span></span>


  <div class="yt-lockup-meta spf-nolink">
      <span class=" yt-uix-button-subscription-container" ><button title="13,723 subscribers" class="yt-uix-subscription-button yt-can-buffer yt-uix-hovercard yt-uix-button yt-uix-button-subscribe-unbranded yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-subscriber-count-tooltip="True" data-channel-external-id="UCrAb_x80PtTiN3lCkQOSFPg" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CPsBEJsr" data-subscriber-count-title="13,723 subscribers" data-style-type="unbranded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="13,723 subscribers" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span>
  </div>

    </div>
    
  </span>


  </li>

        <li class="branded-page-related-channels-item spf-nolink clearfix" data-external-id="UCwEJn0YxvgO2vKV5txlU3FQ">
    




    <span class="yt-lockup clearfix  yt-lockup-channel yt-lockup-mini"
  >
    <div class="yt-lockup-thumbnail"
        style="width: 34px;"
    >
        <a href="/user/Fujiboi" class="ux-thumb-wrap yt-uix-sessionlink " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIACEMAb">    <span class="video-thumb  yt-thumb yt-thumb-34 g-hovercard"
        data-ytid="UCwEJn0YxvgO2vKV5txlU3FQ"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="https://yt3.ggpht.com/-To58HPiI20g/AAAAAAAAAAI/AAAAAAAAAAA/pjHVovuC7wc/s176-c-k-no/photo.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="34"  height="34" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</a>

    </div>
    <div class="yt-lockup-content">
          <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text g-hovercard" data-ytid="UCwEJn0YxvgO2vKV5txlU3FQ" data-name="rc-rel"             ><h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link " dir="ltr" title="Fujiboi" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CP4BEL8b" href="/user/Fujiboi">Fujiboi</a></h3></span></span></span>


  <div class="yt-lockup-meta spf-nolink">
      <span class=" yt-uix-button-subscription-container" ><button title="11,555 subscribers" class="yt-uix-subscription-button yt-can-buffer yt-uix-hovercard yt-uix-button yt-uix-button-subscribe-unbranded yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-subscriber-count-tooltip="True" data-channel-external-id="UCwEJn0YxvgO2vKV5txlU3FQ" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CP8BEJsr" data-subscriber-count-title="11,555 subscribers" data-style-type="unbranded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="11,555 subscribers" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span>
  </div>

    </div>
    
  </span>


  </li>

        <li class="branded-page-related-channels-item spf-nolink clearfix" data-external-id="UCTtHA5e1zLaqUdU_LrI53IA">
    




    <span class="yt-lockup clearfix  yt-lockup-channel yt-lockup-mini"
  >
    <div class="yt-lockup-thumbnail"
        style="width: 34px;"
    >
        <a href="/user/CivilDigital" class="ux-thumb-wrap yt-uix-sessionlink " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIQCEMAb">    <span class="video-thumb  yt-thumb yt-thumb-34 g-hovercard"
        data-ytid="UCTtHA5e1zLaqUdU_LrI53IA"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="https://yt3.ggpht.com/-dQxkQBaaQ_M/AAAAAAAAAAI/AAAAAAAAAAA/gh7MKVdMulg/s176-c-k-no/photo.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="34"  height="34" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</a>

    </div>
    <div class="yt-lockup-content">
          <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text g-hovercard" data-ytid="UCTtHA5e1zLaqUdU_LrI53IA" data-name="rc-rel"             ><h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link " dir="ltr" title="Civil Digital" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIICEL8b" href="/user/CivilDigital">Civil Digital</a></h3></span></span></span>


  <div class="yt-lockup-meta spf-nolink">
      <span class=" yt-uix-button-subscription-container" ><button title="10,050 subscribers" class="yt-uix-subscription-button yt-can-buffer yt-uix-hovercard yt-uix-button yt-uix-button-subscribe-unbranded yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-subscriber-count-tooltip="True" data-channel-external-id="UCTtHA5e1zLaqUdU_LrI53IA" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIMCEJsr" data-subscriber-count-title="10,050 subscribers" data-style-type="unbranded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="10,050 subscribers" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span>
  </div>

    </div>
    
  </span>


  </li>

        <li class="branded-page-related-channels-item spf-nolink clearfix" data-external-id="UClQuD8W4UNatz7huHPx2frg">
    




    <span class="yt-lockup clearfix  yt-lockup-channel yt-lockup-mini"
  >
    <div class="yt-lockup-thumbnail"
        style="width: 34px;"
    >
        <a href="/user/MzeroAFlightTraining" class="ux-thumb-wrap yt-uix-sessionlink " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIgCEMAb">    <span class="video-thumb  yt-thumb yt-thumb-34 g-hovercard"
        data-ytid="UClQuD8W4UNatz7huHPx2frg"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="https://yt3.ggpht.com/-hl_d9xnR7M4/AAAAAAAAAAI/AAAAAAAAAAA/o2P6YrUja5w/s176-c-k-no/photo.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="34"  height="34" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</a>

    </div>
    <div class="yt-lockup-content">
          <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text g-hovercard" data-ytid="UClQuD8W4UNatz7huHPx2frg" data-name="rc-rel"             ><h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link " dir="ltr" title="MzeroA Flight Training" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIYCEL8b" href="/user/MzeroAFlightTraining">MzeroA Flight Training</a></h3></span></span></span>


  <div class="yt-lockup-meta spf-nolink">
      <span class=" yt-uix-button-subscription-container" ><button title="9,832 subscribers" class="yt-uix-subscription-button yt-can-buffer yt-uix-hovercard yt-uix-button yt-uix-button-subscribe-unbranded yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-subscriber-count-tooltip="True" data-channel-external-id="UClQuD8W4UNatz7huHPx2frg" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIcCEJsr" data-subscriber-count-title="9,832 subscribers" data-style-type="unbranded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="9,832 subscribers" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span>
  </div>

    </div>
    
  </span>


  </li>

        <li class="branded-page-related-channels-item spf-nolink clearfix" data-external-id="UC4HSOhd9ds3-dbyBJKvZgOQ">
    




    <span class="yt-lockup clearfix  yt-lockup-channel yt-lockup-mini"
  >
    <div class="yt-lockup-thumbnail"
        style="width: 34px;"
    >
        <a href="/channel/UC4HSOhd9ds3-dbyBJKvZgOQ" class="ux-thumb-wrap yt-uix-sessionlink " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIwCEMAb">    <span class="video-thumb  yt-thumb yt-thumb-34 g-hovercard"
        data-ytid="UC4HSOhd9ds3-dbyBJKvZgOQ"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="https://yt3.ggpht.com/-Ba94qAslh_s/AAAAAAAAAAI/AAAAAAAAAAA/O8lokM0pOQw/s176-c-k-no/photo.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="34"  height="34" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</a>

    </div>
    <div class="yt-lockup-content">
          <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text g-hovercard" data-ytid="UC4HSOhd9ds3-dbyBJKvZgOQ" data-name="rc-rel"             ><h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link " dir="ltr" title="Om Brewok" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIoCEL8b" href="/channel/UC4HSOhd9ds3-dbyBJKvZgOQ">Om Brewok</a></h3></span></span></span>


  <div class="yt-lockup-meta spf-nolink">
      <span class=" yt-uix-button-subscription-container" ><button title="8,161 subscribers" class="yt-uix-subscription-button yt-can-buffer yt-uix-hovercard yt-uix-button yt-uix-button-subscribe-unbranded yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-subscriber-count-tooltip="True" data-channel-external-id="UC4HSOhd9ds3-dbyBJKvZgOQ" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CIsCEJsr" data-subscriber-count-title="8,161 subscribers" data-style-type="unbranded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="8,161 subscribers" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span>
  </div>

    </div>
    
  </span>


  </li>

        <li class="branded-page-related-channels-item spf-nolink clearfix" data-external-id="UCf_8ZTFvJeS8U60W8C8PGhA">
    




    <span class="yt-lockup clearfix  yt-lockup-channel yt-lockup-mini"
  >
    <div class="yt-lockup-thumbnail"
        style="width: 34px;"
    >
        <a href="/user/barefootbooks" class="ux-thumb-wrap yt-uix-sessionlink " data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CJACEMAb">    <span class="video-thumb  yt-thumb yt-thumb-34 g-hovercard"
        data-ytid="UCf_8ZTFvJeS8U60W8C8PGhA"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <img alt="Thumbnail" data-thumb="https://yt3.ggpht.com/-wPko5JghuDc/AAAAAAAAAAI/AAAAAAAAAAA/2h9N8152kog/s176-c-k-no/photo.jpg" src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="34"  height="34" >
          <span class="vertical-align"></span>
        </span>
      </span>
    </span>
</a>

    </div>
    <div class="yt-lockup-content">
          <span class="qualified-channel-title ellipsized"><span class="qualified-channel-title-wrapper"><span dir="ltr" class="qualified-channel-title-text g-hovercard" data-ytid="UCf_8ZTFvJeS8U60W8C8PGhA" data-name="rc-rel"             ><h3 class="yt-lockup-title"><a class="yt-uix-sessionlink yt-uix-tile-link " dir="ltr" title="Barefoot Books" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CI4CEL8b" href="/user/barefootbooks">Barefoot Books</a></h3></span></span></span>


  <div class="yt-lockup-meta spf-nolink">
      <span class=" yt-uix-button-subscription-container" ><button title="26,663 subscribers" class="yt-uix-subscription-button yt-can-buffer yt-uix-hovercard yt-uix-button yt-uix-button-subscribe-unbranded yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-subscriber-count-tooltip="True" data-channel-external-id="UCf_8ZTFvJeS8U60W8C8PGhA" data-sessionlink="ei=xk51U7XzONKj-QP9tYGgDQ&amp;feature=rc-rel&amp;ved=CI8CEJsr" data-subscriber-count-title="26,663 subscribers" data-style-type="unbranded" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="26,663 subscribers" class="yt-uix-button-icon yt-uix-button-icon-subscribe"></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span>
  </div>

    </div>
    
  </span>


  </li>

  </ul>

    </div>


          </div>
      </div>
    </div>
  </div>
</div></div></div></div>  <div id="footer-container" class="yt-base-gutter"><div id="footer"><div id="footer-main"><div id="footer-logo"><a href="/" title="YouTube home"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="YouTube home"></a></div>  <ul class="pickers yt-uix-button-group" data-button-toggle-group="optional">
      <li>
            <button onclick=";return false;" id="yt-picker-language-button" type="button" class=" yt-uix-button yt-uix-button-default yt-uix-button-size-default yt-uix-button-has-icon" data-button-action="yt.www.picker.load" data-picker-position="footer" data-picker-key="language" data-button-menu-id="arrow-display" data-button-toggle="true" role="button"><span class="yt-uix-button-icon-wrapper"><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-icon yt-uix-button-icon-footer-language"></span><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Language:
  </span>
  English
 </span><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-arrow"></button>


      </li>
      <li>
            <button onclick=";return false;" id="yt-picker-country-button" type="button" class=" yt-uix-button yt-uix-button-default yt-uix-button-size-default" data-button-action="yt.www.picker.load" data-picker-position="footer" data-picker-key="country" data-button-menu-id="arrow-display" data-button-toggle="true" role="button"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Country:
  </span>
  Worldwide
 </span><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-arrow"></button>


      </li>
      <li>
            <button onclick=";return false;" id="yt-picker-safetymode-button" type="button" class=" yt-uix-button yt-uix-button-default yt-uix-button-size-default" data-button-action="yt.www.picker.load" data-picker-position="footer" data-picker-key="safetymode" data-button-menu-id="arrow-display" data-button-toggle="true" role="button"><span class="yt-uix-button-content">    <span class="yt-picker-button-label">
Safety:
    </span>
Off
 </span><img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-uix-button-arrow"></button>


      </li>
  </ul>
    <button data-ghelp-anchor="google-help" id="google-help" class="yt-uix-button-reverse yt-google-help-link inq-no-click  yt-uix-button yt-uix-button-default yt-uix-button-size-default" data-ghelp-tracking-param="" onclick=";return false;" type="button"  role="button"><span class="yt-uix-button-content">    <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="questionmark">
Help
 </span></button>
      <div id="yt-picker-language-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Loading icon" class="yt-spinner-img">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

      <div id="yt-picker-country-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Loading icon" class="yt-spinner-img">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

      <div id="yt-picker-safetymode-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="https://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Loading icon" class="yt-spinner-img">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

</div><div id="footer-links"><ul id="footer-links-primary">  <li><a href="//www.youtube.com/yt/about/">About</a></li>
  <li><a href="//www.youtube.com/yt/press/">Press &amp; Blogs</a></li>
  <li><a href="//www.youtube.com/yt/copyright/">Copyright</a></li>
  <li><a href="//www.youtube.com/yt/creators/">Creators &amp; Partners</a></li>
  <li><a href="//www.youtube.com/yt/advertise/">Advertising</a></li>
  <li><a href="//www.youtube.com/yt/dev/">Developers</a></li>
  <li><a href="https://plus.google.com/+youtube" dir="ltr">+YouTube</a></li>
</ul><ul id="footer-links-secondary">  <li><a href="/t/terms">Terms</a></li>
  <li><a href="https://www.google.com/intl/en/policies/privacy/">Privacy</a></li>
  <li><a href="//www.youtube.com/yt/policyandsafety/">
Policy &amp; Safety
  </a></li>
  <li><a href="//support.google.com/youtube/?hl=en" onclick="return yt.www.feedback.start(59);" class="reportbug">Send feedback</a></li>
  <li><a href="/testtube">Try something new!</a></li>
  <li></li>
</ul></div></div></div>
        <div class="yt-dialog hid " id="create-channel-identity-lb">
    <div class="yt-dialog-base">
      <span class="yt-dialog-align"></span>
      <div class="yt-dialog-fg">
        <div class="yt-dialog-fg-content">
            <div class="yt-dialog-header">
                  <button onclick=";return false;" type="button" class="  yt-dialog-dismiss yt-dialog-close yt-uix-button yt-uix-button-default yt-uix-button-size-default" data-action="close" role="button"><span class="yt-uix-button-content">Close </span></button>

                <h2 class="yt-dialog-title">
                        __title__


                </h2>
            </div>
          <div class="yt-dialog-loading">
              <div class="yt-dialog-waiting-content">
    <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Loading...</div>
  </div>

          </div>
          <div class="yt-dialog-content">
              <div id="create-channel-identity-dialog">
  </div>

          </div>
          <div class="yt-dialog-working">
              <div class="yt-dialog-working-overlay"></div>
  <div class="yt-dialog-working-bubble">
    <div class="yt-dialog-waiting-content">
      <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Working...</div>
    </div>
  </div>

          </div>
        </div>
      </div>
    </div>
  </div>




      <div class="yt-dialog hid " id="feed-privacy-lb">
    <div class="yt-dialog-base">
      <span class="yt-dialog-align"></span>
      <div class="yt-dialog-fg">
        <div class="yt-dialog-fg-content">
          <div class="yt-dialog-loading">
              <div class="yt-dialog-waiting-content">
    <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Loading...</div>
  </div>

          </div>
          <div class="yt-dialog-content">
              <div id="feed-privacy-dialog">
  </div>

          </div>
          <div class="yt-dialog-working">
              <div class="yt-dialog-working-overlay"></div>
  <div class="yt-dialog-working-bubble">
    <div class="yt-dialog-waiting-content">
      <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Working...</div>
    </div>
  </div>

          </div>
        </div>
      </div>
    </div>
  </div>


<div class="hid">  <div id="yt-uix-videoactionmenu-menu">
    <div class="hide-on-create-pl-panel">
      <h3>
Add to
      </h3>
    </div>
    <div class="add-to-widget">
    </div>
  </div>
</div><script>if (window.ytcsi) {window.ytcsi.tick("hr", null, '');}</script><script>var ytspf = ytspf || {};ytspf.enabled = false;</script>  <script src="//s.ytimg.com/yts/jsbin/spf-vfl5Y9Kzu.js" name="spf"></script>
  <script src="//s.ytimg.com/yts/jsbin/www-en_US-vflJXR0ms/base.js" name="www/base"></script>
<script>spf.script.path({'www/': '//s.ytimg.com/yts/jsbin/www-en_US-vflJXR0ms/'});var ytdepmap = {"www/base": null, "www/common": "www/base", "www/watch": "www/common", "www/videomanager": "www/common", "www/subscriptionmanager": "www/common", "www/results_starwars": "www/common", "www/results_star_trek": "www/common", "www/results": "www/common", "www/results_harlemshake": "www/common", "www/results_fibonacci": "www/common", "www/promo_join_network": "www/common", "www/legomap": "www/common", "www/feed": "www/common", "www/experiments": "www/common", "www/downloadreports": "www/common", "www/dashboard": "www/common", "www/channels": "www/common", "www/channels_accountupload": "www/common", "www/watch_videoshelf": "www/watch", "www/watch_twobillion": "www/watch", "www/watch_transcript": "www/watch", "www/watch_speedyg": "www/watch", "www/watch_promos": "www/watch", "www/watch_missilecommand": "www/watch", "www/watch_live": "www/watch", "www/watch_editor": "www/watch", "www/watch_edit": "www/watch", "www/watch_commentsrealtime": "www/watch", "www/watch_commentsmoderation": "www/watch", "www/channels_edit": "www/channels"};spf.script.declare(ytdepmap);</script><script>if (window.ytcsi) {window.ytcsi.tick("je", null, '');}</script>  

  <script>
    
      (function() {
      var channelHeaderEl = document.querySelector('.channel-header');

      if (!/channel-header-auto-hide/.test(channelHeaderEl.className)) {
        return;
      }

      var brandedPageContainer = document.querySelector('.branded-page-v2-container');
      var originalHeight = brandedPageContainer.clientHeight;
      channelHeaderEl.className = channelHeaderEl.className.replace(/\bhid\b/);
      var height = brandedPageContainer.clientHeight;
      var scrollDistance = height - originalHeight;

      document.body.style.minHeight = 0;

      var bodyScrollHeight = document.body.scrollHeight;
      var bodyClientHeight = document.body.clientHeight;
      var heightToIncrease = scrollDistance - (bodyScrollHeight - bodyClientHeight);
      if (heightToIncrease > 0) {
        document.body.style.minHeight = bodyScrollHeight + heightToIncrease + 'px';
      }

      document.body.scrollTop = document.documentElement.scrollTop = scrollDistance;
    }());

      yt.setConfig('CHANNEL_TAB', 'featured');
        



    
    yt.setConfig('CHANNEL_ID', "UCo50hV2EIx4YHc58L0RZDDQ");
    yt.setConfig('JS_PAGE_MODULES', [
      'www/channels',
      ''
    ]);
    yt.setConfig('CHANNEL_EDITABLE', false);



      yt.setConfig({
        'GUIDE_SELECTED_ITEM': "0qDduQEaEhhVQ281MGhWMkVJeDRZSGM1OEwwUlpERFE%3D"
      });

      yt.setConfig({
    'GUIDED_HELP_LOCALE': "en_US",
    'GUIDED_HELP_ENVIRONMENT': "prod"
  });

  </script>
<script>yt.setConfig({'EVENT_ID': "xk51U7XzONKj-QP9tYGgDQ",'PAGE_NAME': "channel",'LOGGED_IN': true,'SESSION_INDEX': 0,'FORMATS_FILE_SIZE_JS': ["%s B", "%s KB", "%s MB", "%s GB", "%s TB"],'DELEGATED_SESSION_ID': null,'GAPI_HOST': "https:\/\/apis.google.com",'GAPI_HINT_PARAMS': "m;\/_\/scs\/abc-static\/_\/js\/k=gapi.gapi.en.RIXl5bUHOTM.O\/m=__features__\/rt=j\/d=1\/rs=AItRSTMEDqSOskXzfRGcYnvBrDh5RTKEFQ",'GAPI_LOCALE': "en_US",'UNIVERSAL_HOVERCARDS': true,'VISITOR_DATA': "CgtwZlVMM3JybGhJcw%3D%3D",'APIARY_HOST': "",'APIARY_HOST_FIRSTPARTY': "",'INNERTUBE_CONTEXT_HL': "en",'INNERTUBE_CONTEXT_GL': "US",'INNERTUBE_CONTEXT_CLIENT_VERSION': "20140512",'INNERTUBE_API_KEY': "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",'GOOGLEPLUS_HOST': "https:\/\/plus.google.com",'PAGEFRAME_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-pageframe-vflp3m8iT.js",'JS_COMMON_MODULE': "\/\/s.ytimg.com\/yts\/jsbin\/www-en_US-vflJXR0ms\/common.js",'PAGE_FRAME_DELAYLOADED_CSS': "\/\/s.ytimg.com\/yts\/cssbin\/www-pageframedelayloaded-vflfYB34o.css",'PREFETCH_CSS_RESOURCES' : ["\/\/s.ytimg.com\/yts\/cssbin\/www-player-vflbzCGhL.css",''         ],'PREFETCH_JS_RESOURCES': ["\/\/s.ytimg.com\/yts\/jsbin\/html5player-en_US-vflzEDYyE.js",''         ],'SAFETY_MODE_PENDING': false,'LOCAL_DATE_TIME_CONFIG': {"formatLongDate": "MMMM d, yyyy h:mm a", "formatWeekdayShortTime": "EE h:mm a", "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "weekdays": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "formatShortDate": "MMM d, yyyy", "formatLongDateOnly": "MMMM d, yyyy", "shortMonths": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], "amPms": ["AM", "PM"], "shortWeekdays": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]},'PAGE_CL': 66897810,'PAGE_BUILD_TIMESTAMP': "Tue May 13 12:13:57 2014 (1400008437)",'PLAYER_PERSISTENCE_REFACTOR': true,'SANDBAR_ENABLED': true,'SANDBAR_LOCALE': "en-US",'FEEDBACK_BUCKET_ID': "Channels 4",'FEEDBACK_LOCALE_LANGUAGE': "en",'FEEDBACK_LOCALE_EXTRAS': {"experiments": "927606,935705,941404,940908,936120,921905,927906,943405,920605,937003,931943,921410,937105,922804,911507,913434,944702,931950,906957,939940,939944,946801,931970,901812,927616,919389,919393,934003,934004,938626,938632,927006,918119,918121,934113,930819,933218,936923,945044,941414,931967,947204,914948,938006,939201,901604,912714,929237,944309,935707,945815,931978,937803,927881,906001,902022", "guide_subs": "NA", "is_partner": false, "logged_in": true, "accept_language": "en-US,en;q=0.5", "is_branded": false}});yt.setMsg({'ADDTO_WATCH_LATER': "Watch Later",'ADDTO_WATCH_LATER_ADDED': "Added",'ADDTO_WATCH_LATER_ERROR': "Error",'ADDTO_WATCH_QUEUE': "Watch Queue",'ADDTO_WATCH_QUEUE_ADDED': "Added",'ADDTO_WATCH_QUEUE_ERROR': "Error",'ADDTO_TV_QUEUE': "TV Queue"});    yt.setConfig({
    'XSRF_TOKEN': "QUFFLUhqbFFyVUdfdVpTMjdjOVNuQTJfX1ZmUVFnRmtmUXxBQ3Jtc0tsSmpiSEpkcHV1RDJ6MS1Qdm9jSmhRRE82dEp3enNoeWdUTUZXMWo4bDN2NVdVcXBWU21FZ2E0cWRSZXpzbDZORzBjcU1HVUNaOV93ZzlwQVpHWmFHaTNJajF5Skd6R1ZCXzNIYnFqZ2Y5YkRyWUJjZ2poR1VuT3pLeDZFYThRRlNxNEUtSm4xM2ZvbUtEZ3hIZXI2aVNiUzZ1MkE=",
    'XSRF_REDIRECT_TOKEN': "PES0V7r277psa77HRQZIvIAsRZ58MTQwMDI4MzIwN0AxNDAwMTk2ODA3",
    'XSRF_FIELD_NAME': "session_token"
  });

  yt.setConfig('CREATE_CHANNEL_JS_URL', "\/\/s.ytimg.com\/yts\/jsbin\/www-createchanneldialog-vflrrCFXh.js");
  yt.setConfig('CREATE_CHANNEL_CSS_URL', "\/\/s.ytimg.com\/yts\/cssbin\/www-createchannel-vflyALfBj.css");
  yt.setMsg({
      'CREATE_CHANNEL_AJAX_ERROR_MSG': "An error has occurred while sending data over the network.",
      'CREATE_CHANNEL_NO_USERNAME_MSG': "Please enter a username"
  });
  yt.setConfig({
      'CREATE_CHANNEL_NEXT_URL_UPLOAD': "\/upload",
      'CREATE_CHANNEL_NEXT_URL_GUIDE': "\/feed\/?feature=guide",
      'CREATE_CHANNEL_DIALOG_TITLE_UPLOAD_USERNAME': "Upload your first video",
      'CREATE_CHANNEL_DIALOG_TITLE_PLAYLIST_USERNAME': "Create your first playlist",
      'CREATE_CHANNEL_DIALOG_TITLE_COMMENT_USERNAME': "Leave your first comment",
      'CREATE_CHANNEL_DIALOG_TITLE_DEFAULT_USERNAME': "Create your YouTube channel",
      'CREATE_CHANNEL_DIALOG_TITLE_UPLOAD_PROFILE': "Upload as...",
      'CREATE_CHANNEL_DIALOG_TITLE_PLAYLIST_PROFILE': "Create playlist for...",
      'CREATE_CHANNEL_DIALOG_TITLE_COMMENT_PROFILE': "Comment as...",
      'CREATE_CHANNEL_DIALOG_TITLE_DEFAULT_PROFILE': "Use YouTube as...",
  });
  yt.setConfig('HL_LOCALE', "en-US");

  yt.setMsg({
    'USERNAME_AVAILABLE': "Username available!",
    'USERNAME_TAKEN': "Username unavailable",
    'USERNAME_TAKEN_SUGGEST': "Sorry, $username was taken. The following usernames are available:",
    'USERNAME_INVALID': "Username invalid"
  });

  yt.setConfig('CREATE_CHANNEL_LIGHTBOX', true);
  yt.setConfig('FEED_PRIVACY_CSS_URL', "\/\/s.ytimg.com\/yts\/cssbin\/www-feedprivacydialog-vflrBbybR.css");

  yt.setConfig('FEED_PRIVACY_LIGHTBOX_ENABLED', true);
yt.setConfig({'SBOX_JS_URL': "\/\/s.ytimg.com\/yts\/jsbin\/www-searchbox-vflkAkFTq.js",'SBOX_SETTINGS': {"REQUEST_DOMAIN": "us", "REQUEST_LANGUAGE": "en", "SESSION_INDEX": 0, "HAS_ON_SCREEN_KEYBOARD": false, "PSUGGEST_TOKEN": "9wsTUOfx88gKQq7D9bLXRg", "EXPERIMENT_ID": -1},'SBOX_LABELS': {"SUGGESTION_DISMISSED_LABEL": "Suggestion dismissed", "SUGGESTION_DISMISS_LABEL": "Dismiss"}});  yt.setConfig({
    'YPC_LOADER_ENABLED': true,
    'YPC_LOADER_CONFIGS': "\/ypc_config_ajax",
    'YPC_LOADER_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-ypc-vflDF_Exr.js",
    'YPC_LOADER_CSS': "\/\/s.ytimg.com\/yts\/cssbin\/www-ypc-vfl8HSUWi.css",
    'YPC_LOADER_CALLBACKS': ['yt.www.ypc.checkout.init', 'yt.www.ypc.subscription.init']
  });
  yt.setConfig('GOOGLE_HELP_CONTEXT', "default");
ytcsi.span('st', 659);yt.setConfig({'TIMING_ACTION': "channels4",'TIMING_INFO': {"yt_spf": 0, "yt_li": 1, "yt_lt": "cold", "ei": "xk51U7XzONKj-QP9tYGgDQ", "e": "927606,935705,941404,940908,936120,913434,939940,939944,936923,945044"}});  yt.setConfig({
    'XSRF_TOKEN': "QUFFLUhqbFFyVUdfdVpTMjdjOVNuQTJfX1ZmUVFnRmtmUXxBQ3Jtc0tsSmpiSEpkcHV1RDJ6MS1Qdm9jSmhRRE82dEp3enNoeWdUTUZXMWo4bDN2NVdVcXBWU21FZ2E0cWRSZXpzbDZORzBjcU1HVUNaOV93ZzlwQVpHWmFHaTNJajF5Skd6R1ZCXzNIYnFqZ2Y5YkRyWUJjZ2poR1VuT3pLeDZFYThRRlNxNEUtSm4xM2ZvbUtEZ3hIZXI2aVNiUzZ1MkE=",
    'XSRF_REDIRECT_TOKEN': "PES0V7r277psa77HRQZIvIAsRZ58MTQwMDI4MzIwN0AxNDAwMTk2ODA3",
    'XSRF_FIELD_NAME': "session_token"
  });
  yt.setConfig('THUMB_DELAY_LOAD_BUFFER', 0);
if (window.ytcsi) {window.ytcsi.tick("jl", null, '');}</script>
</body></html>


    <!DOCTYPE html><html lang="en" data-cast-api-enabled="true"><head>  <script>var ytcsi = {data_: {tick: {},span: {},info: {}},tick: function(l, t) {ytcsi.data_.tick[l] = t || +new Date();},span: function(l, s) {ytcsi.data_.span[l] = (typeof s == 'number') ? s :+new Date() - ytcsi.data_.tick[l];},info: function(k, v) {ytcsi.data_.info[k] = v;}};ytcsi.tick('_start');if (document.webkitVisibilityState == 'prerender') {ytcsi.info('prerender', 1);document.addEventListener('webkitvisibilitychange', function() {ytcsi.tick('_start');}, false);}try {ytcsi.pt_ = (window.chrome && chrome.csi().pageT ||window.gtbExternal && gtbExternal.pageT() ||window.external && external.pageT);if (ytcsi.pt_) {ytcsi.info('pt', Math.floor(ytcsi.pt_));}} catch(e) {}</script>
<script>var ytdns = {};ytdns.ping = function(src, num) {var img = new Image();ytdns[num] = img;img.onload = img.onerror = function() {delete ytdns[num];};img.src = src;};ytdns.ping("http:\/\/r3---sn-a5m7znek.c.youtube.com\/crossdomain.xml", 2);ytdns.ping("http:\/\/r3---sn-a5m7znek.c.youtube.com\/generate_204", 3);</script>  <link id="css-982818953" rel="stylesheet" href="http://s.ytimg.com/yts/cssbin/www-core-vflScjXzY.css">

  <title>Bill&#39;s Design Talks: Graphic Design— Now in Production - YouTube</title><link rel="search" type="application/opensearchdescription+xml" href="http://www.youtube.com/opensearch?locale=en_US" title="YouTube Video Search"><link rel="shortcut icon" href="http://s.ytimg.com/yts/img/favicon-vfldLzJxy.ico" type="image/x-icon">     <link rel="icon" href="//s.ytimg.com/yts/img/favicon_32-vflWoMFGx.png" sizes="32x32"><link rel="canonical" href="http://www.youtube.com/watch?v=_BFJN62hZp0"><link rel="alternate" media="handheld" href="http://m.youtube.com/watch?v=_BFJN62hZp0"><link rel="alternate" media="only screen and (max-width: 640px)" href="http://m.youtube.com/watch?v=_BFJN62hZp0"><link rel="shortlink" href="http://youtu.be/_BFJN62hZp0">      <meta name="title" content="Bill&#39;s Design Talks: Graphic Design— Now in Production">

      <meta name="description" content="Find out how designers today are rethinking the aesthetics, process, and public of graphic design by creating their own software and systems. Join Cooper-Hew...">

      <meta name="keywords" content="graphic design, contemporary, exhibition, software, diy, tech, governors island, blauvelt, moggridge, lupton, cooper-hewitt, smithsonian, posterwall, lust, n...">

      <link rel="alternate" type="application/json+oembed" href="http://www.youtube.com/oembed?format=json&amp;url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D_BFJN62hZp0" title="Bill&#39;s Design Talks: Graphic Design— Now in Production">
  <link rel="alternate" type="text/xml+oembed" href="http://www.youtube.com/oembed?format=xml&amp;url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D_BFJN62hZp0" title="Bill&#39;s Design Talks: Graphic Design— Now in Production">

        <meta property="og:site_name" content="YouTube">
    <meta property="og:url" content="http://www.youtube.com/watch?v=_BFJN62hZp0">
    <meta property="og:title" content="Bill&#39;s Design Talks: Graphic Design— Now in Production">
    <meta property="og:type" content="video">
    <meta property="og:image" content="http://i4.ytimg.com/vi/_BFJN62hZp0/hqdefault.jpg?feature=og">

      <meta property="og:description" content="Find out how designers today are rethinking the aesthetics, process, and public of graphic design by creating their own software and systems. Join Cooper-Hew...">

      <meta property="og:video" content="http://www.youtube.com/v/_BFJN62hZp0?autohide=1&amp;version=3">
      <meta property="og:video:type" content="application/x-shockwave-flash">
      <meta property="og:video:width" content="640">
      <meta property="og:video:height" content="480">

    <meta property="fb:app_id" content="87741124305">

        <meta name="twitter:card" content="player">
    <meta name="twitter:site" content="@youtube">
    <meta name="twitter:url" content="http://www.youtube.com/watch?v=_BFJN62hZp0">
    <meta name="twitter:title" content="Bill&#39;s Design Talks: Graphic Design— Now in Production">
    <meta name="twitter:description" content="Find out how designers today are rethinking the aesthetics, process, and public of graphic design by creating their own software and systems. Join Cooper-Hew...">
    <meta name="twitter:image" content="http://i4.ytimg.com/vi/_BFJN62hZp0/hqdefault.jpg">
      <meta name="twitter:player" content="https://www.youtube.com/embed/_BFJN62hZp0">
      <meta name="twitter:player:width" content="640">
      <meta name="twitter:player:height" content="480">

  
      <link id="css-1181818654" rel="stylesheet" href="http://s.ytimg.com/yts/cssbin/www-watch-transcript-vfl-zKZyz.css">

<script>if (window.ytcsi) {ytcsi.tick("ct");}</script></head><!-- machid: pRXk1eHo5X0t6MXRsWjFKc242WGVWcUpqVXE1SExUQ0hzdXNIVUdzYXdKRm1jejlONmNfNVZn -->

      <body dir="ltr" class="  ltr      site-left-aligned  exp-new-site-width  exp-watch7-comment-ui  hitchhiker-enabled      guide-enabled guide-collapsed sidebar-expanded   ">

  <div id="body-container"><form name="logoutForm" method="POST" action="/logout"><input type="hidden" name="action_logout" value="1"></form>    
    
    <div id="yt-masthead-container" class="yt-grid-box"><div id="yt-masthead" class="">    <a id="logo-container" href="/" title="YouTube home" class=" "><img id="logo" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="YouTube home"></a>
<div id="yt-masthead-signin"><button onclick=";window.location.href=this.getAttribute(&#39;href&#39;);return false;" href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dsign_in_button%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" type="button" class=" yt-uix-button yt-uix-button-primary"  role="button"><span class="yt-uix-button-content">Sign in </span></button></div><div id="yt-masthead-content"><span id="masthead-upload-button-group"><a href="//www.youtube.com/upload" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-default" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=mhsb"><span class="yt-uix-button-content">Upload</span></a></span><form id="masthead-search" class="search-form consolidated-form" action="/results" onsubmit="if (_gel(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false;"><button class="search-btn-component search-button yt-uix-button yt-uix-button-default" type="submit" id="search-btn" tabindex="2" dir="ltr" onclick="if (_gel(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false; _gel(&#39;masthead-search&#39;).submit(); return false;;return true;"  role="button"><span class="yt-uix-button-content">Search </span></button><div id="masthead-search-terms" class="masthead-search-terms-border" dir="ltr"><label><input id="masthead-search-term"  class="search-term yt-uix-form-input-bidi" name="search_query" value="" type="text" tabindex="1" title="Search"></label></div></form></div></div></div>
    
<div id="alerts">  



</div><div id="header"></div><div id="page-container"><div id="page" class="  watch   clearfix"><div id="guide" >        <div id="guide-container" class="    collapsible-guide ">
      <div id="guide-main" class="    guide-module collapsed     spf-nolink ">
    <div class="guide-module-toggle">
      <span class="guide-module-toggle-icon">
        <span class="guide-module-toggle-arrow"></span>
        <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="">
        <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" id="collapsed-notification-icon">
      </span>
      <div class="guide-module-toggle-label">
        <h3>
          <span>
Guide
          </span>
        </h3>
      </div>
    </div>
      <div class="guide-module-content yt-scrollbar">
    <ul class="guide-toplevel">
      <li id="guide-subscriptions-section" class="guide-section without-filter guide-section-no-counts">
        <div id="guide-subs-footer-container">
            <div id="guide-subscriptions-container">
              
  <div class="guide-channels-content yt-scrollbar">
      <ul  id="guide-channels" class="guide-channels-list guide-item-container yt-uix-scroller filter-has-matches">
          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/"
        title="Popular on YouTube"
      data-channel-id="youtube"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CBoQgB8oAA"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/tnHdj3df7iM/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Popular on YouTube</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/music"
        title="Music"
      data-channel-id="HCp-Rdqh3z4Uc"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CBsQgB8oAQ"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/p-Rdqh3z4Uc/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Music</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/sports"
        title="Sports"
      data-channel-id="HC7Dr1BKwqctY"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CBwQgB8oAg"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i4.ytimg.com/li/7Dr1BKwqctY/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Sports</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/gaming"
        title="Gaming"
      data-channel-id="HChfZhJdhTqX8"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CB0QgB8oAw"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/hfZhJdhTqX8/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Gaming</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/movies"
        title="Movies"
      data-channel-id="UCczhp4wznQWonO7Pb8HQ2MQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CB4QgB8oBA"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i4.ytimg.com/i/czhp4wznQWonO7Pb8HQ2MQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Movies</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/YouTubeShowsUS"
        title="TV Shows"
      data-channel-id="UCl8dMTqDrJQ0c8y23UBu4kQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CB8QgB8oBQ"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/i/l8dMTqDrJQ0c8y23UBu4kQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>TV Shows</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/news"
        title="News"
      data-channel-id="HCPvDBPPFfuaM"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CCAQgB8oBg"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/PvDBPPFfuaM/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>News</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCBR8-60-B28hp2BmDPdntcQ"
        title="Spotlight"
      data-channel-id="UCBR8-60-B28hp2BmDPdntcQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-channel&amp;ved=CCEQgB8oBw"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/BR8-60-B28hp2BmDPdntcQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Spotlight</span>
          </span>
      </span>

    </a>
  </li>

        <li id="guide-filter-no-results">
No channels found
        </li>
        <li id="guide-filter-loading-results">
            <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
        Loading subscriptions
    </span>
  </p>

        </li>
      </ul>
  </div>

            </div>
            <hr class="guide-section-separator">
        </div>
      </li>
        <li id="guide-subscription-suggestions-section" class="guide-section guide-section-no-counts">
            <h3>
Channels for you
            </h3>
            <div class="guide-recommendations-list">
              
  <div class="guide-channels-content yt-scrollbar">
      <ul  class="guide-channels-list guide-item-container yt-uix-scroller filter-has-matches">
          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCry7B7DGVgUIa6k4Tis_DJQ"
        title="The Ricky Gervais Channel"
      data-channel-id="UCry7B7DGVgUIa6k4Tis_DJQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-chrec&amp;ved=CCMQgB8oAA"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/ry7B7DGVgUIa6k4Tis_DJQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>The Ricky Gervais Channel</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCHF66aWLOxBW4l6VkSrS3cQ"
        title="coachella"
      data-channel-id="UCHF66aWLOxBW4l6VkSrS3cQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-chrec&amp;ved=CCQQgB8oAQ"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/i/HF66aWLOxBW4l6VkSrS3cQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>coachella</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCdOm7WpPkqW6FPh23JA2mag"
        title="euronews knowledge"
      data-channel-id="UCdOm7WpPkqW6FPh23JA2mag"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-chrec&amp;ved=CCUQgB8oAg"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i1.ytimg.com/i/dOm7WpPkqW6FPh23JA2mag/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>euronews knowledge</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCkzRDjtq4ngMADh45j2KsJQ"
        title="MachinimaPrime&#39;s channel"
      data-channel-id="UCkzRDjtq4ngMADh45j2KsJQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-chrec&amp;ved=CCYQgB8oAw"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i4.ytimg.com/i/kzRDjtq4ngMADh45j2KsJQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>MachinimaPrime&#39;s channel</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCBR8-60-B28hp2BmDPdntcQ"
        title="YouTube Spotlight"
      data-channel-id="UCBR8-60-B28hp2BmDPdntcQ"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-chrec&amp;ved=CCcQgB8oBA"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="Thumbnail" data-group-key="guide-channel-thumbs" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/BR8-60-B28hp2BmDPdntcQ/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>YouTube Spotlight</span>
          </span>
      </span>

    </a>
  </li>

        <li id="guide-filter-no-results">
No channels found
        </li>
        <li id="guide-filter-loading-results">
            <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
        Loading subscriptions
    </span>
  </p>

        </li>
      </ul>
  </div>

            </div>
            <hr class="guide-section-separator">
            <ul id="gh-management" class="guide-item-container">
        



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/channels"
        title="Browse channels"
      data-channel-id="guide_builder"
      data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=g-manage&amp;ved=CCkQhx8oAA"
    >
      <span class="" >
          <span class="thumb guide-management-plus-icon">
            <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="">
          </span>
          <span>Browse channels</span>
      </span>

    </a>
  </li>

  </ul>

        </li>
    </ul>
        <div class="guide-section guide-header signup-promo guided-help-box">
    <p>
Sign in to add channels to your guide and for great recommendations!
    </p>
    <div id="guide-builder-promo-buttons" class="signed-out clearfix">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dsign_in_promo%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in &#8250;</span></a>
    </div>
  </div>

  </div>

  </div>

      <div id="watch-context-container" class="guide-module collapsed hid"></div>

  </div>

</div><div id="content" class="">  <div id="watch7-container" class="  transition-content  " itemscope itemid="" itemtype="http://schema.org/VideoObject">
        <link itemprop="url" href="http://www.youtube.com/watch?v=_BFJN62hZp0">
    <meta itemprop="name" content="Bill&#39;s Design Talks: Graphic Design— Now in Production">
    <meta itemprop="description" content="Find out how designers today are rethinking the aesthetics, process, and public of graphic design by creating their own software and systems. Join Cooper-Hew...">
    <meta itemprop="paid" content="False">

      <meta itemprop="duration" content="PT90M20S">
      <meta itemprop="unlisted" content="False">

        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="http://www.youtube.com/user/cooperhewitt">
        </span>

    <link itemprop="thumbnailUrl" href="http://i4.ytimg.com/vi/_BFJN62hZp0/hqdefault.jpg">
    <span itemprop="thumbnail" itemscope itemtype="http://schema.org/ImageObject">
      <link itemprop="url" href="http://i4.ytimg.com/vi/_BFJN62hZp0/hqdefault.jpg">
      <meta itemprop="width" content="320">
      <meta itemprop="height" content="180">
    </span>

      <link itemprop="embedURL" href="http://www.youtube.com/v/_BFJN62hZp0?autohide=1&amp;version=3">
      <meta itemprop="playerType" content="Flash">
      <meta itemprop="width" content="640">
      <meta itemprop="height" content="480">

      <meta itemprop="isFamilyFriendly" content="True">
      <meta itemprop="regionsAllowed" content="AD,AE,AF,AG,AI,AL,AM,AO,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BL,BM,BN,BO,BQ,BR,BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CW,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MF,MG,MH,MK,ML,MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,SS,ST,SV,SX,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,TM,TN,TO,TR,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW">


      <div id="player" class="">
        
  <div id="playlist">
    
  </div>
  <div id="player-unavailable" class="    hid  ">
            <img class="icon meh" src="//s.ytimg.com/yts/img/meh7-vflGevej7.png" alt="">
  <div class="content">
    <h1 id="unavailable-message" class="message">
            This video is unavailable.
    </h1>
    <div class="submessage">
    </div>
  </div>


  </div>

  <script>if (window.ytcsi) {ytcsi.tick("bf");}</script>

      <div id="player-api" class="player-width player-height off-screen-target"></div>


    <script>var ytplayer = ytplayer || {};ytplayer.config = {"min_version": "8.0.0", "sts": 1585, "html5": false, "args": {"showpopout": 1, "ucid": "UCBCaO28GYGr7IoKVjT4Jx5A", "cc3_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/subtitles3_module-vflBhj28W.swf", "rvs": "view_count=2%2C428\u0026length_seconds=3183\u0026author=bigthink\u0026featured=1\u0026title=Big+Think+Interview+With+George+Lois\u0026id=-92PkAXJIqQ\u0026feature_type=fvwp,title=Bill%27s+Design+Talks%3A+Nonobject-+A+Radical+New+Approach+to+Design\u0026length_seconds=3873\u0026author=cooperhewitt\u0026id=iQzYRC9fGE8\u0026view_count=1%2C376,title=Bill%27s+Design+Talks%3A+Pentagram\u0026length_seconds=2878\u0026author=cooperhewitt\u0026id=Jtqi0F3cDaU\u0026view_count=8%2C721,title=Bill%27s+Design+Talks%3A+Emily+Oberman\u0026length_seconds=4183\u0026author=cooperhewitt\u0026id=WwA1qGubdHU\u0026view_count=848,title=Bill%27s+Design+Talks%3A+Robert+Wong%2C+Google+CreativeLab\u0026length_seconds=4143\u0026author=cooperhewitt\u0026id=6vIPk6vIwv0\u0026view_count=3%2C987,title=History+of+Industrial+Design+Lecture+%235%3A+Efficiency\u0026length_seconds=3225\u0026author=HistoryofID\u0026id=z8MhAm-FwX4\u0026view_count=1%2C881,title=Designing+Logos+-+Graphic+Design+for+Everyone\u0026length_seconds=5260\u0026author=creativelive\u0026id=d_mDEv8fMug\u0026view_count=4%2C507,title=Academy+of+Art+University+%7C+School+of+Graphic+Design+%7C+Hybrid+Design%3A+Work+%26+Play+Panel\u0026length_seconds=5318\u0026author=academyofartu\u0026id=ErrmZ_xQ5hs\u0026view_count=1%2C998,title=Designing+Graphic+Design+History\u0026length_seconds=873\u0026author=RockPaperInk\u0026id=vkFkb1ghwWo\u0026view_count=5%2C878,title=Bill%27s+Design+Talks%3A+Annabelle+Selldorf\u0026length_seconds=4232\u0026author=cooperhewitt\u0026id=87nH6T01Zz4\u0026view_count=635,title=Graphic+Design+Tutorial%3A+Typography+and+Design\u0026length_seconds=965\u0026author=UltramanToronto\u0026id=mBoVoj5jLfc\u0026view_count=4%2C816,title=3.+Mobile+User+Experience+Design\u0026length_seconds=3847\u0026author=StanfordUniversity\u0026id=SEwCRpTEgA0\u0026view_count=29%2C591", "watermark": ",http:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_watermark-vflHX6b6E.png,http:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_hd_watermark-vflAzLcD6.png", "plid": "AATeb8ZpNJ3ziaPz", "video_id": "_BFJN62hZp0", "referrer": null, "allow_embed": 1, "ldpj": "-27", "length_seconds": 5420, "url_encoded_fmt_stream_map": "fallback_host=tc.v23.cache7.c.youtube.com\u0026sig=98D0AC4D1B545DE6D5C531A5DB7902877511632A.5700D588C7659DE8A8621EC5110CB638D0EF4A39\u0026itag=44\u0026type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22\u0026quality=large\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D44%26mt%3D1370471490%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ratebypass%3Dyes%26ms%3Dau%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire%26ipbits%3D8%26expire%3D1370493270%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26id%3Dfc114937ada1669d%26upn%3Dt-LMF5MC9BA,fallback_host=tc.v2.cache1.c.youtube.com\u0026sig=A23283ED964AA8EF061249CCA6199EDDA6543FF2.89798F8181F2250FCFF24F19B2E59D880D054703\u0026itag=35\u0026type=video%2Fx-flv\u0026quality=large\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26factor%3D1.25%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D35%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26ms%3Dau%26algorithm%3Dthrottle-factor%26id%3Dfc114937ada1669d%26expire%3D1370493270%26burst%3D40%26ipbits%3D8%26upn%3Dt-LMF5MC9BA%26mt%3D1370471490,fallback_host=tc.v22.cache3.c.youtube.com\u0026sig=2E2A7F8D5A61497159C2A2CFBB07F62B98062500.33826449E77B3A5F5FE40D028857064D7313D60A\u0026itag=43\u0026type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22\u0026quality=medium\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D43%26mt%3D1370471490%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ratebypass%3Dyes%26ms%3Dau%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire%26ipbits%3D8%26expire%3D1370493270%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26id%3Dfc114937ada1669d%26upn%3Dt-LMF5MC9BA,fallback_host=tc.v11.cache4.c.youtube.com\u0026sig=78D14935180C9DA87E1C562719525D0BB6BE21F9.9BC13425338E5DD6C255EA77136CC424830BCD21\u0026itag=34\u0026type=video%2Fx-flv\u0026quality=medium\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26factor%3D1.25%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D34%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26ms%3Dau%26algorithm%3Dthrottle-factor%26id%3Dfc114937ada1669d%26expire%3D1370493270%26burst%3D40%26ipbits%3D8%26upn%3Dt-LMF5MC9BA%26mt%3D1370471490,fallback_host=tc.v17.cache2.c.youtube.com\u0026sig=9534F06E230AFD98894138B4A5D6DF75D11BC316.A488BE98A3EADBE84BA4A8BDA61E12EB6CA7BB85\u0026itag=18\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.42001E%2C+mp4a.40.2%22\u0026quality=medium\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D18%26mt%3D1370471490%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ratebypass%3Dyes%26ms%3Dau%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire%26ipbits%3D8%26expire%3D1370493270%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26id%3Dfc114937ada1669d%26upn%3Dt-LMF5MC9BA,fallback_host=tc.v19.cache3.c.youtube.com\u0026sig=CA92F947487449BAB3D360E565331F5BE50D2134.8EC1CB03A41B459227D84F34D2C2AB7BC2BA95A0\u0026itag=5\u0026type=video%2Fx-flv\u0026quality=small\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26factor%3D1.25%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D5%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26ms%3Dau%26algorithm%3Dthrottle-factor%26id%3Dfc114937ada1669d%26expire%3D1370493270%26burst%3D40%26ipbits%3D8%26upn%3Dt-LMF5MC9BA%26mt%3D1370471490,fallback_host=tc.v19.cache4.c.youtube.com\u0026sig=793FD335B7B7EE9B77B457DA951DAED704FFC363.1B6AC609D71AB3EE17BDA911E2761A87C79A080F\u0026itag=36\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026quality=small\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26factor%3D1.25%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D36%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26ms%3Dau%26algorithm%3Dthrottle-factor%26id%3Dfc114937ada1669d%26expire%3D1370493270%26burst%3D40%26ipbits%3D8%26upn%3Dt-LMF5MC9BA%26mt%3D1370471490,fallback_host=tc.v3.cache3.c.youtube.com\u0026sig=06294DA91D0E1FE3C7DF7AD9D133EC95939B8D70.731CE14A56E9C61E4ABE43110CE7515C5F42C66B\u0026itag=17\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026quality=small\u0026url=http%3A%2F%2Fr3---sn-a5m7znek.c.youtube.com%2Fvideoplayback%3Fip%3D208.70.31.237%26key%3Dyt1%26factor%3D1.25%26newshard%3Dyes%26cp%3DU0hWRVRUUV9MSkNONl9MTlVDOjRtUl9JQzM2NENr%26itag%3D17%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26fexp%3D900352%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912518%252C906906%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C912711%252C929606%252C910075%26ms%3Dau%26algorithm%3Dthrottle-factor%26id%3Dfc114937ada1669d%26expire%3D1370493270%26burst%3D40%26ipbits%3D8%26upn%3Dt-LMF5MC9BA%26mt%3D1370471490", "tmi": "1", "c": "WEB", "enablejsapi": 1, "enablecsi": "1", "abd": "1", "autohide": "2", "sk": "3uBvvY7XTQkHQGc4IrN--8EFoMgpwOwOC", "timestamp": 1370471558, "account_playback_token": "lAYP7OghuiA-v2jAjxH1rc0hmBh8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4", "is_html5_mobile_device": false, "cr": "US", "sendtmp": "1", "keywords": "graphic design,contemporary,exhibition,software,diy,tech,governors island,blauvelt,moggridge,lupton,cooper-hewitt,smithsonian,posterwall,lust,nieuwenhuizen,talk,panel,bill's design talks,greene space,nyc", "endscreen_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/endscreen-vflKOX8EP.swf", "share_icons": "http:\/\/s.ytimg.com\/yts\/swfbin\/sharing-vflF4tO1T.swf", "title": "Bill's Design Talks: Graphic Design\u2014 Now in Production", "csi_page_type": "watch,watch7", "cc_asr": 1, "playlist_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/playlist_module-vfl1txF_X.swf", "ttsurl": "http:\/\/www.youtube.com\/api\/timedtext?expire=1370496758\u0026sparams=asr_langs%2Ccaps%2Cv%2Cexpire\u0026hl=en_US\u0026caps=asr\u0026v=_BFJN62hZp0\u0026asr_langs=ru%2Ces%2Cpt%2Cnl%2Cit%2Cko%2Cde%2Cfr%2Cja%2Cen\u0026signature=15734FC6C76E16600EBF59ADFDA56FB5D843BFDC.A8A6932FC7DA352FFA67C1649D4312EC94AFEFAA\u0026key=yttt1", "cc_font": "Arial Unicode MS, arial, verdana, _sans", "tk": "1", "no_get_video_log": "1", "t": "vjVQa1PpcFO1erBqBpYW0UNBhUhSIpvGrJO2yd46WNc=", "idpj": "-6", "storyboard_spec": "http:\/\/i4.ytimg.com\/sb\/_BFJN62hZp0\/storyboard3_L$L\/$N.jpg|48#27#100#10#10#0#default#-gk1SKNrHE-Tmy9iS7nuPTvFQuA|67#45#543#10#10#10000#M$M#xhaAoys0tYIQZ5-72FPCgETNlio|135#90#543#5#5#10000#M$M#86YKPK4UMPTNtqZalcHO0ika8yA", "cc_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/subtitle_module-vflFOqSms.swf", "pltype": "contentugc", "fexp": "900352,924605,928201,901208,929123,929121,929915,929906,925714,929919,929119,931202,928017,912512,912518,906906,904830,930807,919373,906836,933701,900816,912711,929606,910075", "ptk": "youtube_none", "vq": "auto", "fmt_list": "44\/854x480\/99\/0\/0,35\/854x480\/9\/0\/115,43\/640x360\/99\/0\/0,34\/640x360\/9\/0\/115,18\/640x360\/9\/0\/115,5\/320x240\/7\/0\/0,36\/320x240\/99\/0\/0,17\/176x144\/99\/0\/0", "hl": "en_US"}, "assets": {"js": "http:\/\/s.ytimg.com\/yts\/jsbin\/html5player-vflnYJM6b.js", "html": "\/html5_player_template", "css": "http:\/\/s.ytimg.com\/yts\/cssbin\/www-player-vflgp4Cz9.css"}, "params": {"allowscriptaccess": "always", "allowfullscreen": "true", "bgcolor": "#000000"}, "attrs": {"id": "movie_player"}, "url_v9as2": "http:\/\/s.ytimg.com\/yts\/swfbin\/cps-vflbmXkSz.swf", "url_v8": "http:\/\/s.ytimg.com\/yts\/swfbin\/cps-vflbmXkSz.swf", "url": "http:\/\/s.ytimg.com\/yts\/swfbin\/watch_as3-vflmOp4Pg.swf"};</script>    <script>
      (function() {
        ytplayer.config.loaded = true;
        var encoded = [];
        for (var key in ytplayer.config.args) {
          encoded.push(encodeURIComponent(key) + '=' + encodeURIComponent(ytplayer.config.args[key]));
        }
        var swf = "      \u003cembed type=\"application\/x-shockwave-flash\"     s\u0072c=\"http:\/\/s.ytimg.com\/yts\/swfbin\/watch_as3-vflmOp4Pg.swf\"     id=\"movie_player\"    flashvars=\"__flashvars__\"     allowscriptaccess=\"always\" allowfullscreen=\"true\" bgcolor=\"#000000\"\u003e\n  \u003cnoembed\u003e\u003cdiv class=\"yt-alert yt-alert-default yt-alert-error  yt-alert-player\"\u003e  \u003cdiv class=\"yt-alert-icon\"\u003e\n    \u003cimg s\u0072c=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" class=\"icon master-sprite\" alt=\"Alert icon\"\u003e\n  \u003c\/div\u003e\n\u003cdiv class=\"yt-alert-buttons\"\u003e\u003c\/div\u003e\u003cdiv class=\"yt-alert-content\" role=\"alert\"\u003e    \u003cspan class=\"yt-alert-vertical-trick\"\u003e\u003c\/span\u003e\n    \u003cdiv class=\"yt-alert-message\"\u003e\n            You need Adobe Flash Player to watch this video. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eDownload it from Adobe.\u003c\/a\u003e\n    \u003c\/div\u003e\n\u003c\/div\u003e\u003c\/div\u003e\u003c\/noembed\u003e\n\n";
        swf = swf.replace('__flashvars__', encoded.join('&'));
        document.getElementById("player-api").innerHTML = swf;
      })();
    </script>


  

  <div id="player-branded-banner">
    
  </div>

      </div>

    <div id="watch7-main-container">
      <div id="watch7-main" class="clearfix">
        <div id="watch7-content" class="watch-content">
              <div class="yt-uix-button-panel">
      <div id="watch7-headline" class="clearfix  yt-uix-expander yt-uix-expander-collapsed">
    <h1 id="watch-headline-title">
      


  


  <span id="eow-title" class="watch-title long-title yt-uix-expander-head" dir="ltr" title="Bill&#39;s Design Talks: Graphic Design— Now in Production">
    Bill&#39;s Design Talks: Graphic Design— Now in Production
  </span>

    </h1>
  </div>

    <div id="watch7-user-header" ><a href="/user/cooperhewitt?feature=watch" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="cooperhewitt" src="//i3.ytimg.com/i/BCaO28GYGr7IoKVjT4Jx5A/1.jpg?v=da8003" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a><a href="/user/cooperhewitt?feature=watch" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=watch" dir="ltr">cooperhewitt</a><span class="yt-user-separator">&middot;</span><a class="yt-uix-sessionlink yt-user-videos"href="/user/cooperhewitt/videos"data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=watch">427 videos</a><br><span id="watch7-subscription-container"><span class=" yt-uix-button-subscription-container" ><button class="yt-uix-subscription-button yt-uix-button yt-uix-button-subscribe-branded" aria-role="button" onclick=";return false;" aria-live="polite" aria-busy="false" type="button" data-href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26continue_action%3DQUFFLUhqbE9OeldYQlBMRXNzMDM4c2xJWVFjdVh2dFZsQXxBQ3Jtc0ttUDdKME0tQUdDUTM4a2xsZ2ZNNmFFMDhPMFM5S2pULTFRTE5CSUp6d3VZeURVNTRsZUZ1SU84NmVxM2w5UF9zUzVZdy1MWFJIaEtvUjNUUW5SMzI4QU1EeHRuLUZ6ZVZjRmUwS2RUVHR5akNCeko1RFk5c3Nsc0pGeXBYT0FBY1dBXzhLUm9VMXJvTC1Gb3Fpa25tXzFJbFNYM1lMdkl6OTEtTWdKRjloVlBlNkFKRzFIbWcxWUFrWmh5TlM4SVNMbV9fYnc%253D%26feature%3Dsubscribe%26hl%3Den_US%26next%3D%252Fchannel%252FUCBCaO28GYGr7IoKVjT4Jx5A%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" data-channel-external-id="UCBCaO28GYGr7IoKVjT4Jx5A" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&amp;feature=watch" data-style-type="branded" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-subscribe" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button><span class="yt-subscription-button-subscriber-count-branded-horizontal" >2,688</span>  <span class="yt-subscription-button-disabled-mask" title=""></span>
</span></span><div id="watch7-views-info">      <span class="watch-view-count " >
    1,200
  </span>

    <div class="video-extras-sparkbars">
    <div class="video-extras-sparkbar-likes" style="width: 100.0%"></div>
    <div class="video-extras-sparkbar-dislikes" style="width: 0.0%"></div>
  </div>
  <span class="video-extras-likes-dislikes">
      <img class="icon-watch-stats-like" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Like">
  <span class="likes-count">10</span>
 &nbsp;&nbsp;&nbsp;   <img class="icon-watch-stats-dislike" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Dislike">
  <span class="dislikes-count">0</span>

  </span>

</div></div>
      <div id="watch7-action-buttons" class="clearfix">
    <div id="watch7-sentiment-actions">
      <span id="watch-like-dislike-buttons" class="yt-uix-button-group " data-vote-state="2" data-button-toggle-group="optional"><span class="yt-uix-clickcard"><button title="" id="watch-like" class="yt-uix-clickcard-target yt-uix-button yt-uix-button-text yt-uix-tooltip" onclick=";return false;" type="button" data-force-position="true" data-position="bottomright" data-orientation="vertical" data-button-toggle="true" data-unlike-tooltip="Unlike" data-like-tooltip="I like this" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-like" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><span class="yt-uix-button-content">Like </span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your Google Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to like <span class="yt-user-name " dir="ltr">cooperhewitt</span>'s video.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button title="I dislike this" id="watch-dislike" class="yt-uix-clickcard-target yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" type="button" data-force-position="true" data-position="bottomright" data-button-toggle="true" data-orientation="vertical" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-dislike" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="I dislike this" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your Google Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to dislike <span class="yt-user-name " dir="ltr">cooperhewitt</span>'s video.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span></span>
    </div>
    <div id="watch7-secondary-actions"  class="yt-uix-button-group" data-button-toggle-group="required">
        <span >
    <button title="" onclick=";return false;" type="button" class="action-panel-trigger  yt-uix-button-toggled yt-uix-button yt-uix-button-text yt-uix-tooltip" data-button-toggle="true" data-trigger-for="action-panel-details" role="button"><span class="yt-uix-button-content">About </span></button>
  </span>

          <span >
    <button title="" onclick=";return false;" type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip" data-button-toggle="true" data-trigger-for="action-panel-share" role="button"><span class="yt-uix-button-content">Share </span></button>
  </span>

          <span class="yt-uix-clickcard">
    <button title="" onclick=";return false;" type="button" class="action-panel-trigger   yt-uix-clickcard-target yt-uix-button yt-uix-button-text yt-uix-tooltip" data-position="bottomleft" data-button-toggle="true" data-upsell="playlist" data-orientation="vertical" data-trigger-for="action-panel-none" role="button"><span class="yt-uix-button-content">Add to </span></button>
        <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your Google Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to add <span class="yt-user-name " dir="ltr">cooperhewitt</span>'s video to your playlist.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>

  </span>

          <span >
    <button title="Transcript" onclick=";return false;" type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" data-button-toggle="true" data-trigger-for="action-panel-transcript" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-action-panel-transcript" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Transcript" title=""><span class="yt-uix-button-valign"></span></span></button>
  </span>

          <span >
    <button title="Statistics" onclick=";return false;" type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" data-button-toggle="true" data-trigger-for="action-panel-stats" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-action-panel-stats" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Statistics" title=""><span class="yt-uix-button-valign"></span></span></button>
  </span>


        <span >
    <button title="Report" onclick=";return false;" type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" data-button-toggle="true" data-trigger-for="action-panel-report" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-action-panel-report" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Report" title=""><span class="yt-uix-button-valign"></span></span></button>
  </span>

    </div>
  </div>

      <div id="watch7-action-panels" class="yt-uix-button-panel">
      <div id="action-panel-details" class="action-panel-content ">
    <div id="watch-description" class="yt-uix-expander yt-uix-expander-collapsed yt-uix-button-panel">
      <div id="watch-description-content" >
        <div id="watch-description-clip">
          <p id="watch-uploader-info">
            <strong>Published on <span id="eow-date" class="watch-video-date" >Jun 28, 2012</span>
</strong>
          </p>
          <div id="watch-description-text">
            <p id="eow-description" >Find out how designers today are rethinking the aesthetics, process, and public of graphic design by creating their own software and systems. Join Cooper-Hewitt Director Bill Moggridge, Walker Art Center Curator Andrew Blauvelt and interaction designer Dimitri Nieuwenhuizen in a lively discussion. Dimitri is a member of Lust, the innovative Dutch design collective that created the large-scale interactive project Posterwall for the Twenty-first Century, on view in Cooper-Hewitt&#39;s new exhibition Graphic Design—Now In Production, on view every weekend through Labor Day on Governors Island, New York City. The exhibition was co-organized by Cooper-Hewitt and Walker Art Center.</p>
          </div>
            <div id="watch-description-extras">
    <ul class="watch-extras-section">
      <li>
        <h4 class="title">
Category
        </h4>
        <div class="content">
              <p id="eow-category"><a href="/education">Education</a></p>

        </div>
      </li>


        <li>
          <h4 class="title">License</h4>
          <div class="content">
              <p id="eow-reuse">
Standard YouTube License
  </p>

          </li>
        </li>
    </ul>
  </div>

        </div>
        <ul id="watch-description-extra-info">
          
        </ul>
      </div>

      <div id="watch-description-toggle" class="yt-uix-expander-head yt-uix-button-panel">
        <div id="watch-description-expand" class="expand">
          <button onclick=";return false;" type="button" class="metadata-inline yt-uix-button yt-uix-button-text"  role="button"><span class="yt-uix-button-content">Show more </span></button>
        </div>
        <div id="watch-description-collapse" class="collapse">
          <button onclick=";return false;" type="button" class="metadata-inline yt-uix-button yt-uix-button-text"  role="button"><span class="yt-uix-button-content">Show less </span></button>
        </div>
      </div>
    </div>
  </div>

      <div id="action-panel-share" class="action-panel-content hid">
      <div id="watch-actions-share-loading">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>
  <div id="watch-actions-share-panel"></div>

  </div>

      <div id="action-panel-addto" class="action-panel-content hid" data-auth-required="true">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>

        <div id="action-panel-transcript" class="action-panel-content hid">
    <div id="watch-actions-transcript-loading">
      <div class="action-panel-loading">
          <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

      </div>
    </div>
      <div id="watch-actions-transcript" class="watch-actions-panel hid">
      <div id="caption-line-template" class="hid">
    <!--
    <div class="caption-line-time">
      <div class="caption-line-start">__start__</div>
    </div>
    <div class="editable-line-text">
      <span class="editable-line-text-original">__original__</span>
      <label class="editable-line-text-current hid">__current__</label>
      <textarea class="editable-line-text-input hid">__input__</textarea>
    </div>
    -->
  </div>




    <div id="watch-transcript-container" >
      <div id="watch-transcript-not-found" class="hid">
The interactive transcript could not be loaded.
      </div>


      
    </div>
  </div>

  </div>

      <div id="action-panel-stats" class="action-panel-content hid">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>

      <div id="action-panel-report" class="action-panel-content hid" data-auth-required="true">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>

      <div id="action-panel-login" class="action-panel-content hid">
    <div class="action-panel-login">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-default" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>

  <div id="action-panel-ratings-disabled" class="action-panel-content hid">
      <div id="watch-actions-ratings-disabled" class="watch-actions-panel">
    <em>Ratings have been disabled for this video.</em>
  </div>

  </div>

  <div id="action-panel-rental-required" class="action-panel-content hid">
      <div id="watch-actions-rental-required" class="watch-actions-panel">
    <strong>Rating is available when the video has been rented.</strong>
  </div>

  </div>

  <div id="action-panel-error" class="action-panel-content hid">
    <div class="action-panel-error">
      This feature is not available right now. Please try again later.
    </div>
  </div>

    <div id="watch7-action-panel-footer">
        <hr class="yt-horizontal-rule ">

    </div>
  </div>

  </div>
    <div id="watch-discussion">
      <div style="display: none"><iframe src="https://apis.google.com/_/im/_/s/c?first_party_property=YOUTUBE&amp;view_type=FILTERED_POSTMOD&amp;yt_owner_id=BCaO28GYGr7IoKVjT4Jx5A&amp;href=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D_BFJN62hZp0&amp;query=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D_BFJN62hZp0"></iframe></div>

        
        <div id="comments-view" data-type="highlights" class="">

                <div >
      <h4>
      <a href="/all_comments?v=_BFJN62hZp0">
            <strong>All Comments</strong> (1)

      </a>
  </h4>


          <div class="comments-post-alert comments-post">
        <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dcomments%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3">Sign in</a> now to post a comment!

      </div>


      <ul id="all-comments">
      


  <li class="comment"
    data-author-id="l4umkS8O2YbhPKd5C4iv5A"
    data-id="Vw2N4wFzJ0D6WVoU4sB-tMc-CMILLaLRhrgxBjjdAvo"
    >
    <button onclick=";return false;" type="button" class="flip close yt-uix-button yt-uix-button-link yt-uix-button-empty" data-button-has-sibling-menu="true" role="button" aria-pressed="false" aria-expanded="false" aria-haspopup="true" aria-activedescendant=""><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-comment-close" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><div class=" yt-uix-button-menu yt-uix-button-menu-link" style="display: none;"><ul><li class="comment-action-remove comment-action" data-action="remove"><span class="yt-uix-button-menu-item">Remove</span></li><li class="comment-action" data-action="flag-profile-pic"><span class="yt-uix-button-menu-item">Report profile image</span></li><li class="comment-action" data-action="flag"><span class="yt-uix-button-menu-item">Flag for spam</span></li><li class="comment-action-block comment-action" data-action="block"><span class="yt-uix-button-menu-item">Block User</span></li><li class="comment-action-unblock comment-action" data-action="unblock"><span class="yt-uix-button-menu-item">Unblock User</span></li></ul></div></button>
      <a href="/user/GraphicDesignStuff" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="GraphicDesignStuff" data-thumb="//i1.ytimg.com/i/l4umkS8O2YbhPKd5C4iv5A/1.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a>

    

  <div class="content">
      <p class="metadata">
        <span class="author ">
          <a href="/user/GraphicDesignStuff" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ" dir="ltr">GraphicDesignStuff</a>
        </span>
          <span class="time" dir="ltr">
            <a dir="ltr" href="http://www.youtube.com/comment?lc=Vw2N4wFzJ0D6WVoU4sB-tMc-CMILLaLRhrgxBjjdAvo">
              2 weeks ago
            </a>
          </span>
      </p>


      <div class="comment-text" dir="ltr">
          <p>Excellent video!</p>
<p>Had to shared on our Graphic Design Page on FaceBook.</p>
<p>facebook(dot)com/GraphicDesign<wbr>&shy;Stuff</p>
<p>﻿</p>

      </div>
      
  <div class="comment-actions">
    <button onclick=";return false;" type="button" class="start comment-action yt-uix-button yt-uix-button-link" data-action="reply" role="button"><span class="yt-uix-button-content">Reply </span></button>
    <span class="separator">&middot;</span>


    <span class="yt-uix-clickcard"><button title="" onclick=";return false;" type="button" class="start comment-action-vote-up comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" data-tooltip-show-delay="300" data-action="" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-up" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">GraphicDesignStuff</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button title="" onclick=";return false;" type="button" class="end comment-action-vote-down comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" data-tooltip-show-delay="300" data-action="" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-down" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">GraphicDesignStuff</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&amp;passive=true&amp;service=youtube&amp;uilel=3" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span>
  </div>

  </div>


  </li>

  </ul>

  </div>




    <ul>
      <li class="hid" id="parent-comment-loading">Loading comment...</li>
    </ul>
  </div>
  <div id="comments-loading" class="hid">Loading...</div>
    


  </div>



        </div>
        <div id="watch7-sidebar" class="watch-sidebar ">
            



          <div class="watch-sidebar-section">

    <div class="watch-sidebar-body">
      <ul id="watch-related" class="video-list">
          <li class="video-list-item related-list-item">
            <a href="/watch?v=-92PkAXJIqQ" class="related-video yt-uix-contextlink  related-video-featured hid yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=fvwrel&ved=CAMQzRooAA"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/-92PkAXJIqQ/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">53:03</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="-92PkAXJIqQ" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Big Think Interview With George Lois">Big Think Interview With George Lois</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">bigthink</span></span><span class="stat alt badge"><span class="yt-badge ">Featured</span></span>    <span class="stat view-count">
        2,428
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=iQzYRC9fGE8" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CAQQzRooAQ"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/iQzYRC9fGE8/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:04:33</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="iQzYRC9fGE8" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Bill&#39;s Design Talks: Nonobject- A Radical New Approach to Design">Bill&#39;s Design Talks: Nonobject- A Radical New Approach to Design</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        1,376 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=Jtqi0F3cDaU" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CAUQzRooAg"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i3.ytimg.com/vi/Jtqi0F3cDaU/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">47:58</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="Jtqi0F3cDaU" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Bill&#39;s Design Talks: Pentagram">Bill&#39;s Design Talks: Pentagram</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        8,721 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=WwA1qGubdHU" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CAYQzRooAw"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i4.ytimg.com/vi/WwA1qGubdHU/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:09:43</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="WwA1qGubdHU" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Bill&#39;s Design Talks: Emily Oberman">Bill&#39;s Design Talks: Emily Oberman</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        848 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=6vIPk6vIwv0" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CAcQzRooBA"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i3.ytimg.com/vi/6vIPk6vIwv0/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:09:03</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="6vIPk6vIwv0" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Bill&#39;s Design Talks: Robert Wong, Google CreativeLab">Bill&#39;s Design Talks: Robert Wong, Google CreativeLab</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        3,987 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=z8MhAm-FwX4" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CAgQzRooBQ"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i3.ytimg.com/vi/z8MhAm-FwX4/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">53:45</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="z8MhAm-FwX4" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="History of Industrial Design Lecture #5: Efficiency">History of Industrial Design Lecture #5: Efficiency</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">HistoryofID</span></span>    <span class="stat view-count">
        1,881 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=d_mDEv8fMug" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CAkQzRooBg"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i1.ytimg.com/vi/d_mDEv8fMug/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:27:40</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="d_mDEv8fMug" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Designing Logos - Graphic Design for Everyone">Designing Logos - Graphic Design for Everyone</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">creativelive</span></span>    <span class="stat view-count">
        4,507 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=ErrmZ_xQ5hs" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CAoQzRooBw"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/ErrmZ_xQ5hs/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:28:38</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="ErrmZ_xQ5hs" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Academy of Art University | School of Graphic Design | Hybrid Design: Work &amp; Play Panel">Academy of Art University | School of Graphic Design | Hybrid Design: Work &amp; Play Panel</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">academyofartu</span></span>    <span class="stat view-count">
        1,998 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=vkFkb1ghwWo" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CAsQzRooCA"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i3.ytimg.com/vi/vkFkb1ghwWo/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">14:33</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="vkFkb1ghwWo" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Designing Graphic Design History">Designing Graphic Design History</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">RockPaperInk</span></span>    <span class="stat view-count">
        5,878 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=87nH6T01Zz4" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CAwQzRooCQ"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i1.ytimg.com/vi/87nH6T01Zz4/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:10:32</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="87nH6T01Zz4" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Bill&#39;s Design Talks: Annabelle Selldorf">Bill&#39;s Design Talks: Annabelle Selldorf</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        635 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=mBoVoj5jLfc" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CA0QzRooCg"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/mBoVoj5jLfc/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">16:05</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="mBoVoj5jLfc" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Graphic Design Tutorial: Typography and Design">Graphic Design Tutorial: Typography and Design</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">UltramanToronto</span></span>    <span class="stat view-count">
        4,816 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=SEwCRpTEgA0" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CA4QzRooCw"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i4.ytimg.com/vi/SEwCRpTEgA0/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:04:07</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="SEwCRpTEgA0" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="3. Mobile User Experience Design">3. Mobile User Experience Design</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">StanfordUniversity</span></span>    <span class="stat view-count">
        29,591 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=l5MrbukjA3Q" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CA8QzRooDA"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i1.ytimg.com/vi/l5MrbukjA3Q/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:14:03</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="l5MrbukjA3Q" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Design Lecture: Anthony Burrill">Design Lecture: Anthony Burrill</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">walkerartcenter</span></span>    <span class="stat view-count">
        7,611 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=h4wuHplQO58" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CBAQzRooDQ"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i1.ytimg.com/vi/h4wuHplQO58/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">10:06</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="h4wuHplQO58" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Curator&#39;s Tour of Graphic Design—Now in Production">Curator&#39;s Tour of Graphic Design—Now in Production</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        5,869 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=atn22-bmTPU" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CBEQzRooDg"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/atn22-bmTPU/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">21:57</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="atn22-bmTPU" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Paula Scher: Great design is serious (not solemn)">Paula Scher: Great design is serious (not solemn)</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">TEDtalksDirector</span></span>    <span class="stat view-count">
        59,170 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=tTKcPJVYvbI" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CBIQzRooDw"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i1.ytimg.com/vi/tTKcPJVYvbI/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">48:43</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="tTKcPJVYvbI" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Poster Design Workshop">Poster Design Workshop</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Gangplank HQ Video Central</span></span>    <span class="stat view-count">
        12,560 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=9H6Qu5BCpyc" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CBMQzRooEA"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/9H6Qu5BCpyc/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">10:28</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="9H6Qu5BCpyc" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Create a Logo Without Photoshop - FREE!">Create a Logo Without Photoshop - FREE!</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Tyler Moore</span></span>    <span class="stat view-count">
        48,283 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=6u0_K6t8wUE" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CBQQzRooEQ"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i3.ytimg.com/vi/6u0_K6t8wUE/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:05:46</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="6u0_K6t8wUE" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Ellen Lupton">Ellen Lupton</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">walkerartcenter</span></span>    <span class="stat view-count">
        5,334 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=owZvImgo57s" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=related&ved=CBUQzRooEg"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i4.ytimg.com/vi/owZvImgo57s/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">13:24</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="owZvImgo57s" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Graphic Design Tutorial: Relationships on the page">Graphic Design Tutorial: Relationships on the page</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">UltramanToronto</span></span>    <span class="stat view-count">
        7,334 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=mnkGhdcSkgE" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ei=hryvUcbTFeeNkAL4p4HQBQ&feature=relmfu&ved=CBYQzRooEw"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img alt="" data-thumb="//i2.ytimg.com/vi/mnkGhdcSkgE/default.jpg" src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">59:42</span>

  <button title="Watch Later" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" onclick=";return false;" type="button" data-video-ids="mnkGhdcSkgE" data-button-menu-id="shared-addto-watch-later-login" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Graphic Design- The Final Hours">Graphic Design- The Final Hours</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">cooperhewitt</span></span>    <span class="stat view-count">
        624 views
    </span>
</a>
          </li>
            <div id="watch-more-related" class="hid">
    <li id="watch-more-related-loading">
Loading more suggestions...
    </li>
  </div>
  <button onclick=";return false;" id="watch-more-related-button" type="button" class=" yt-uix-button yt-uix-button-default" data-button-action="yt.www.watch.related.loadMore" role="button"><span class="yt-uix-button-content">Load more suggestions </span></button>

      </ul>
    </div>   </div> 


        </div>
      </div>
    </div>

      <div style="visibility: hidden; height: 0px; padding: 0px; overflow: hidden;">
  </div>

  </div>
</div></div></div></div><div id="footer-container"><div id="footer"><div id="footer-main"><div id="footer-logo"><a href="/" title="YouTube home"><img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="YouTube home"></a></div>  <ul class="pickers yt-uix-button-group" data-button-toggle-group="optional">
      <li>
          
  <button onclick=";return false;" id="yt-picker-language-button" type="button" class=" yt-uix-button yt-uix-button-default" data-button-action="yt.www.picker.load" data-picker-position="footer" data-picker-key="language" data-button-toggle="true" data-button-menu-id="arrow-display" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-footer-language" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Language:
  </span>
  English
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>


      </li>
      <li>
          
  <button onclick=";return false;" id="yt-picker-country-button" type="button" class=" yt-uix-button yt-uix-button-default" data-button-action="yt.www.picker.load" data-picker-position="footer" data-picker-key="country" data-button-toggle="true" data-button-menu-id="arrow-display" role="button"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Country:
  </span>
  Worldwide
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>


      </li>
      <li>
          
  <button onclick=";return false;" id="yt-picker-safetymode-button" type="button" class=" yt-uix-button yt-uix-button-default" data-button-action="yt.www.picker.load" data-picker-position="footer" data-picker-key="safetymode" data-button-toggle="true" data-button-menu-id="arrow-display" role="button"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Safety:
  </span>
Off
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>


      </li>
  </ul>
  <button id="google-help" class="yt-uix-button-reverse yt-uix-button yt-uix-button-default" onclick="yt.www.feedback.startHelp(this, null, &quot;watch&quot;);return false;" type="button"  role="button"><span class="yt-uix-button-content">  <img class="questionmark" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
  <span>Help</span>
    <img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
 </span></button>
      <div id="yt-picker-language-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

      <div id="yt-picker-country-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

      <div id="yt-picker-safetymode-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

</div><div id="footer-links"><ul id="footer-links-primary">  <li><a href="//www.youtube.com/yt/about/">About</a></li>
  <li><a href="//www.youtube.com/yt/press/">Press &amp; Blogs</a></li>
  <li><a href="//www.youtube.com/yt/copyright/">Copyright</a></li>
  <li><a href="//www.youtube.com/yt/creators/">Creators &amp; Partners</a></li>
  <li><a href="//www.youtube.com/yt/advertise/">Advertising</a></li>
  <li><a href="//www.youtube.com/yt/dev/">Developers</a></li>
</ul><ul id="footer-links-secondary">  <li><a href="/t/terms">Terms</a></li>
  <li><a href="http://www.google.com/intl/en/policies/privacy/">Privacy</a></li>
  <li><a href="//www.youtube.com/yt/policyandsafety/">
Policy &amp; Safety
  </a></li>
  <li><a href="//www.google.com/tools/feedback/intl/en/error.html" onclick="return yt.www.feedback.start();" id="reportbug">Send feedback</a></li>
  <li><a href="/testtube">Try something new!</a></li>
  <li></li>
</ul></div></div></div>

      <div class="yt-dialog hid" id="feed-privacy-lb">
    <div class="yt-dialog-base">
      <span class="yt-dialog-align"></span>
      <div class="yt-dialog-fg">
        <div class="yt-dialog-fg-content">
          <div class="yt-dialog-loading">
              <div class="yt-dialog-waiting-content">
    <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Loading...</div>
  </div>

          </div>
          <div class="yt-dialog-content">
              <div id="feed-privacy-dialog">
  </div>

          </div>
          <div class="yt-dialog-working">
              <div id="yt-dialog-working-overlay">
  </div>
  <div id="yt-dialog-working-bubble">
    <div class="yt-dialog-waiting-content">
      <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Working...</div>
    </div>
  </div>

          </div>
        </div>
      </div>
    </div>
  </div>



    <div id="shared-addto-watch-later-login" class="hid">
      <a href="https://accounts.google.com/ServiceLogin?hl=en_US&continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dplaylist%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&passive=true&service=youtube&uilel=3" class="sign-in-link">Sign in</a> to add this to Watch Later

    </div>

  <div id="shared-addto-menu" style="display: none;" class="hid sign-in">
      <div class="addto-menu">
        <div id="addto-list-panel" class="menu-panel active-panel">
        <span class="yt-uix-button-menu-item yt-uix-tooltip sign-in"data-possible-tooltip=""data-tooltip-show-delay="750"><a href="https://accounts.google.com/ServiceLogin?hl=en_US&continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dplaylist%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1&passive=true&service=youtube&uilel=3" class="sign-in-link">Sign in</a> to add this to Watch Later
</span>

  </div>
  <div id="addto-list-saved-panel" class="menu-panel">
    <div class="panel-content">
      <div class="yt-alert yt-alert-naked yt-alert-success  ">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
            
  <span class="message">Added to <span class="addto-title yt-uix-tooltip yt-uix-tooltip-reverse" title="More information about this playlist" data-tooltip-show-delay="750"></span></span>

    </div>
</div></div>
        <div class="yt-alert yt-alert-naked yt-alert-warn  private-video-warning hid">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
            Private videos will be skipped if viewers don&#39;t have access, but playlist notes are publicly visible.
    </div>
</div></div>

    </div>
  </div>
  <div id="addto-list-error-panel" class="menu-panel">
    <div class="panel-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span class="error-details"></span>
      <a class="show-menu-link">Back to list</a>
    </div>
  </div>

        <div id="addto-note-input-panel" class="menu-panel">
    <div class="panel-content">
      <div class="yt-alert yt-alert-naked yt-alert-success  ">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
              <span class="message">Added to playlist:</span>
  <span class="addto-title yt-uix-tooltip" title="More information about this playlist" data-tooltip-show-delay="750"></span>

    </div>
</div></div>
        <div class="yt-alert yt-alert-naked yt-alert-warn  private-video-warning hid">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
            Private videos will be skipped if viewers don&#39;t have access, but playlist notes are publicly visible.
    </div>
</div></div>

    </div>
<div class="yt-uix-char-counter" data-char-limit="150"><div class="addto-note-box addto-text-box"><textarea id="addto-note" class="addto-note yt-uix-char-counter-input" maxlength="150"></textarea><label for="addto-note" class="addto-note-label">Add an optional note</label></div><span class="yt-uix-char-counter-remaining">150</span></div>    <button disabled="disabled" type="button" class="playlist-save-note yt-uix-button yt-uix-button-default" onclick=";return false;"  role="button"><span class="yt-uix-button-content">Add note </span></button>
  </div>
  <div id="addto-note-saving-panel" class="menu-panel">
    <div class="panel-content loading-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span>Saving note...</span>
    </div>
  </div>
  <div id="addto-note-saved-panel" class="menu-panel">
    <div class="panel-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span class="message">Note added to:</span>
    </div>
  </div>
  <div id="addto-note-error-panel" class="menu-panel">
    <div class="panel-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span class="message">Error adding note:</span>
      <ul class="error-details"></ul>
      <a class="add-note-link">Click to add a new note</a>
    </div>
  </div>
  <div class="close-note hid">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="close-button">
  </div>

  </div>

  </div>
<script>if (window.ytcsi) {ytcsi.tick("js_head");}</script>    <script id="js-4250492157" class="www_base_mod" src="//s.ytimg.com/yts/jsbin/www_base_mod-vfllOxUSK.js" data-loaded="true"></script>
  <script>
    yt.setConfig({
      'JS_DELAY_LOAD': 0,
      'WATCH_GUIDE_CSS': "http:\/\/s.ytimg.com\/yts\/cssbin\/www-guide-vflsMUwZf.css",
      'WATCH_CONTEXT_CONTAINER_TEMPLATE': "    \u003cdiv id=\"context-source-container\"data-context-source=\"__source__\"data-context-image=\"__image__\"style=\"display:none;\"\u003e\u003c\/div\u003e\u003cdiv class=\"__container_classes__\"\u003e\u003cdiv class=\"guide-module-toggle context-header\"\u003e\u003cspan class=\"guide-module-toggle-icon\"\u003e\u003cspan class=\"guide-module-toggle-arrow\"\u003e\u003c\/span\u003e\u003cimg src=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\"\u003e\u003c\/span\u003e\u003ca class=\"context-back-link yt-uix-sessionlink\" href=\"__back_link__\" data-sessionlink=\"ei=hryvUcbTFeeNkAL4p4HQBQ\u0026amp;feature=__feature__\"\u003e\u003cspan class=\"guide-context-image-link\"\u003e\u003cspan class=\"thumb guide-context-image\"\u003e\u003cimg id=\"context-image\" src=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\" data-context-image=\"__image__\"\u003e\u003c\/span\u003e\u003c\/span\u003e\u003cdiv class=\"guide-module-toggle-label\"\u003e\u003ch3 class=\"context-title\"\u003e\u003cspan\u003e__headline__\u003c\/span\u003e\u003c\/h3\u003e\u003cspan class=\"placeholder\" title=\"__more_from__\" dir=\"__title_dir__\"\u003e__more_from__\u003c\/span\u003e\u003c\/div\u003e\u003c\/a\u003e\u003c\/div\u003e\u003cdiv class=\"guide-module-content yt-scrollbar\"\u003e\u003chr class=\"guide-section-separator guide-context-separator-top\"\u003e\u003cul id=\"watch-context-item-list\" class=\"guide-context-item-container context-data-container yt-uix-scroller guide-context-body\" data-context-playing=\"__click_index__\" data-context-open=\"true\" data-context-subsource=\"__subsource__\" data-scroll-action=\"yt.www.watch.context.loadThumbnails\"\u003e__item_list__\u003c\/ul\u003e\u003chr class=\"guide-section-separator guide-context-separator-bottom\"\u003e\u003c\/div\u003e\u003c\/div\u003e\n",
      'WATCH_CONTEXT_VIDEO_TEMPLATE': "    \u003cli class=\"guide-context-item context-data-item context-video yt-uix-scroller-scroll-unit __item_classes__\" data-context-item-time=\"__video_time__\" data-context-item-actionverb=\"__action_verb__\" data-context-item-actionuser=\"__action_username__\" data-context-item-type=\"video\" data-context-item-views=\"__view_count__\" data-context-item-id=\"__video_id__\" data-context-item-title=\"__video_title__\" data-context-item-user=\"__user_name__\"\u003e\u003ca href=\"\/watch?v=__video_id__\" class=\"yt-uix-contextlink yt-uix-sessionlink \" data-sessionlink=\"ei=hryvUcbTFeeNkAL4p4HQBQ\u0026amp;feature=__feature__\"\u003e    \u003cspan class=\"video-thumb context-video-thumb yt-thumb yt-thumb-40\"\n      \u003e\n      \u003cspan class=\"yt-thumb-default\"\u003e\n        \u003cspan class=\"yt-thumb-clip\"\u003e\n          \u003cspan class=\"yt-thumb-clip-inner\"\u003e\n            \u003cimg alt=\"\" data-group-key=\"guide-context-thumbs\" data-thumb-manual=\"1\" data-thumb=\"\/\/i4.ytimg.com\/vi\/__video_id__\/default.jpg\" src=\"http:\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" width=\"40\" \u003e\n            \u003cspan class=\"vertical-align\"\u003e\u003c\/span\u003e\n          \u003c\/span\u003e\n        \u003c\/span\u003e\n      \u003c\/span\u003e\n    \u003c\/span\u003e\n\u003cspan class=\"title\"\u003e__video_title__\u003c\/span\u003e\u003cspan class=\"username\"\u003eby __user_name__\n\u003c\/span\u003e\u003cspan class=\"viewcount\"\u003e__view_count__\u003c\/span\u003e\u003cspan class=\"action\"\u003e__action_username__ __action_verb__\u003c\/span\u003e\u003c\/a\u003e\u003c\/li\u003e\n",
      'WATCH_CONTEXT_PLAYLIST_TEMPLATE': "    \u003cli class=\"guide-context-item context-data-item context-playlist yt-uix-scroller-scroll-unit __item_classes__\" data-context-item-videos=\"[\u0026quot;__playlist_video_id__\u0026quot;]\" data-context-item-count-label=\"__video_count_label__\" data-context-item-actionuser=\"__action_username__\" data-context-item-type=\"playlist\" data-context-item-actionverb=\"__action_verb__\" data-context-item-count=\"__video_count__\" data-context-item-id=\"__playlist_id__\" data-context-item-title=\"__playlist_title__\" data-context-item-user=\"\u0026quot;__user_name__\u0026quot;\"\u003e\u003ca href=\"\/watch?v=__playlist_video_id__\u0026amp;list=__playlist_id__\" class=\"yt-uix-contextlink yt-uix-sessionlink \" data-sessionlink=\"ei=hryvUcbTFeeNkAL4p4HQBQ\u0026amp;feature=__feature__\"\u003e\u003cspan class=\"context-video-thumb yt-pl-thumb\"\u003e    \u003cspan class=\"video-thumb  yt-thumb yt-thumb-40\"\n      \u003e\n      \u003cspan class=\"yt-thumb-default\"\u003e\n        \u003cspan class=\"yt-thumb-clip\"\u003e\n          \u003cspan class=\"yt-thumb-clip-inner\"\u003e\n            \u003cimg alt=\"\" data-group-key=\"guide-context-thumbs\" data-thumb-manual=\"1\" data-thumb=\"\/\/i4.ytimg.com\/vi\/__playlist_video_id__\/default.jpg\" src=\"http:\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" width=\"40\" \u003e\n            \u003cspan class=\"vertical-align\"\u003e\u003c\/span\u003e\n          \u003c\/span\u003e\n        \u003c\/span\u003e\n      \u003c\/span\u003e\n    \u003c\/span\u003e\n  \u003cspan class=\"video-count-wrapper\"\u003e\n    \u003cspan class=\"video-count-block\"\u003e\n      \u003cspan class=\"count-label\"\u003e__video_count__\u003c\/span\u003e\n      \u003cspan class=\"text-label\"\u003e__video_count_label__\u003c\/span\u003e\n    \u003c\/span\u003e\n  \u003c\/span\u003e\n\u003c\/span\u003e\u003cspan class=\"title\"\u003e__playlist_title__\u003c\/span\u003e\u003cspan class=\"username\"\u003eby __user_name__\n\u003c\/span\u003e\u003cspan class=\"action\"\u003e__action_username__ __action_verb__\u003c\/span\u003e\u003c\/a\u003e\u003c\/li\u003e\n",
      'WATCH_CONTEXT_APPBAR_TEMPLATE': "  \u003cli  id=\"appbar-item-context\" class=\"appbar-item\"\u003e\u003cbutton onclick=\";return false;\" type=\"button\" class=\" yt-uix-button yt-uix-button-appbar\" data-button-menu-action=\"yt.www.masthead.appbar.toggleMenu\" data-button-menu-id=\"appbar-context-menu\" role=\"button\"\u003e\u003cspan class=\"yt-uix-button-content\"\u003e\u003cspan class=\"appbar-notification-count\"\u003e__item_count__\u003c\/span\u003e__headline__\u0026nbsp;\u003cspan title=\"__more_from__\" dir=\"__title_dir__\"\u003e__more_from__\u003c\/span\u003e \u003c\/span\u003e\u003cimg class=\"yt-uix-button-arrow\" src=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\" title=\"\"\u003e\u003c\/button\u003e\u003c\/li\u003e\n",
      'WATCH_CONTEXT_GEN204': true,
      'SPF_PREFETCH': false,
      'SPF_PREFETCH_MAX': null,
      'GUIDE_ENABLED': true,
      'TIMING_WFF': true      });

    yt.setAjaxToken('watch_fragments_ajax', "MJS_RTe5NsRQxrJyXpslz0Z9KQ98MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");
    yt.setAjaxToken('guide_ajax', "XI1L9wkM6vNKHNl78ykW4hwYATd8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");
    yt.setAjaxToken('promo_ajax_token', "-RMEa3tQKG6yXxQO7rQyVn_p3ux8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");


    yt.setMsg({
      'WATCH_CONTEXT_MORE_FROM': "More from",
      'WATCH_CONTEXT_MORE_RESULTS': "More results"
    });

    
  </script>

    <script>
    yt.setConfig({
      'VIDEO_ID': "_BFJN62hZp0",

      'JS_PAGE_MODULES': {
        "\/\/s.ytimg.com\/yts\/jsbin\/www_watch_mod-vflTAa4vT.js": [
            "\/\/s.ytimg.com\/yts\/jsbin\/www_watch_transcript_mod-vflJ-zo7_.js",
            "\/\/s.ytimg.com\/yts\/jsbin\/www_watch_live_mod-vfleDv6X3.js",
          ''         ]
      },


      'REPORTVIDEO_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-reportvideo-vfl6CW3Ab.js",
      'REPORTVIDEO_CSS': "http:\/\/s.ytimg.com\/yts\/cssbin\/www-watch-reportvideo-vflzqn8VY.css",

        'IS_RESUMABLE_PLAYBACK': true,

      'ENABLE_AUTO_LARGE': true    });

    yt.setAjaxToken('insight_ajax', "s_Gf-8KDL-gWxaOm1cHD8hTIwoF8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");

      yt.setConfig({
    'EMBED_HTML_TEMPLATE': "\u003ciframe width=\"__width__\" height=\"__height__\" src=\"__url__\" frameborder=\"0\" allowfullscreen\u003e\u003c\/iframe\u003e",
    'EMBED_HTML_URL': "http:\/\/www.youtube.com\/embed\/__videoid__"
  });
    yt.setMsg('FLASH_UPGRADE', "\u003cdiv class=\"yt-alert yt-alert-default yt-alert-error  yt-alert-player\"\u003e  \u003cdiv class=\"yt-alert-icon\"\u003e\n    \u003cimg s\u0072c=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" class=\"icon master-sprite\" alt=\"Alert icon\"\u003e\n  \u003c\/div\u003e\n\u003cdiv class=\"yt-alert-buttons\"\u003e\u003c\/div\u003e\u003cdiv class=\"yt-alert-content\" role=\"alert\"\u003e    \u003cspan class=\"yt-alert-vertical-trick\"\u003e\u003c\/span\u003e\n    \u003cdiv class=\"yt-alert-message\"\u003e\n            You need to upgrade your Adobe Flash Player to watch this video. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eDownload it from Adobe.\u003c\/a\u003e\n    \u003c\/div\u003e\n\u003c\/div\u003e\u003c\/div\u003e");
  yt.setMsg('PLAYER_FALLBACK', "The Adobe Flash Player or an HTML5 supported browser is required for video playback. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eGet the latest Flash Player\u003c\/a\u003e \u003cbr\u003e \u003ca href=\"\/html5\"\u003eLearn more about upgrading to an HTML5 browser\u003c\/a\u003e");
  yt.setMsg('QUICKTIME_FALLBACK', "The Adobe Flash Player or QuickTime is required for video playback. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eGet the latest Flash Player\u003c\/a\u003e \u003cbr\u003e \u003ca href=\"http:\/\/www.apple.com\/quicktime\/download\/\"\u003eGet the latest version of QuickTime\u003c\/a\u003e");



    yt.setConfig({
      'IS_OWNER_VIEWING': null,
      'IS_WIDESCREEN': false,
      'PREFER_LOW_QUALITY': false,
      'ALLOW_EMBED': true,
      'ALLOW_RATINGS': true,
      'YPC_CAN_RATE_VIDEO': true,
      'YPC_SHOW_VPPA_CONFIRM_RATING': false,

        'TTS_URL': "http:\/\/www.youtube.com\/api\/timedtext?expire=1370496758\u0026sparams=asr_langs%2Ccaps%2Cv%2Cexpire\u0026hl=en_US\u0026caps=asr\u0026v=_BFJN62hZp0\u0026asr_langs=ru%2Ces%2Cpt%2Cnl%2Cit%2Cko%2Cde%2Cfr%2Cja%2Cen\u0026signature=15734FC6C76E16600EBF59ADFDA56FB5D843BFDC.A8A6932FC7DA352FFA67C1649D4312EC94AFEFAA\u0026key=yttt1",











      'ADS_DATA': {"use_gut": false, "show_afv": false, "show_afc": false, "show_companion": false, "show_instream": false, "show_pyv": false},
      'PLAYBACK_ID': "AATeb8ZpNJ3ziaPz",
      'PLAY_ALL_MAX': 480,
      'IN_SIGNED_OUT_ACTION_PROMO_1': false,
      'IN_SIGNED_OUT_ACTION_PROMO_2': false    });




    yt.setMsg({
        'HTML5_SUBS_ASR': "automatic captions",
      'LOADING': "Loading..."    });

      yt.setMsg({
    'UNBLOCK_USER': "Are you sure you want to unblock this user?",
    'BLOCK_USER': "Are you sure you want to block this user?"
  });
  yt.setConfig('BLOCK_USER_AJAX_XSRF', 'session_token=7HHrHd2U7qW2MissueBg2L5MqTx8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4');


      

  yt.setConfig({
    'COMMENTS_CHANNEL_CREATE_URL': null,
    'COMMENTS_SIGNIN_URL': "https:\/\/accounts.google.com\/ServiceLogin?hl=en_US\u0026continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dcomments%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253D_BFJN62hZp0%26nomobiletemp%3D1\u0026passive=true\u0026service=youtube\u0026uilel=3",
    'COMMENTS_THRESHHOLD': -5,
    'COMMENTS_PAGE_SIZE': 10,
    'COMMENTS_COUNT': 1,
    'COMMENTS_YPC_CAN_POST_OR_REACT_TO_COMMENT': true,
    'COMMENT_SOURCE': "w",
    'COMMENT_OPEN_REPLY_BOX' : false
  });

  yt.setAjaxToken('link_ajax', "7HHrHd2U7qW2MissueBg2L5MqTx8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");
  yt.setAjaxToken('comment_servlet', "3b6tL98u1vW4goibGmnf807zyYx8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");
  yt.setAjaxToken('comment_voting', "4W_NlsvTGhV6mXAPTtNCys6NWNd8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");




  yt.setMsg({
    'CHARACTERS_REMAINING': {"case0": "No characters remaining", "case1": "1 character remaining", "other": "# characters remaining"},
    'COMMENT_OK': "OK",
    'COMMENT_BLOCKED': "You have been blocked by the owner of this video.",
    'COMMENT_CAPTCHAFAIL': "The response to the letters on the image was not correct, please try again.",
    'COMMENT_PENDING': "Comment Pending Approval!",
    'COMMENT_ERROR_EMAIL': "Error, account unverified (see email)",
    'COMMENT_ERROR': "Error, try again",
    'COMMENT_FAILED_MAINTENANCE': "We're currently performing site maintenace, please try later.",
    'COMMENT_OWNER_LINKING': "Comments can't contain links. Please put the link in your video description and refer to it in the comment.",
    'FAILED_HASLINK': "Oops! Remove any web addresses and try again.",
    'FAILED_HASTAGS': "Oops! Remove the HTML tags and try again.",
    'FAILED_ASCIIART': "Oops! Remove the character (ascii) art and try again.",
    'FAILED_TOOSHORT': "Oops! Your comment is too short.",
    'FAILED_TOOLONG': "Oops! Your comment is too long.",
    'FAILED_BADPARENT': "Oops! You cannot respond to a deleted comment.",
    'SECONDS_REMAINING': {"case0": "You can post again", "case1": "1 second remaining before you can post", "other": "# seconds remaining before you can post"}
  });





    







          yt.setConfig({
        'LIVESTREAMING_CARDIO_ENABLED': true,
        'LIVESTREAMING_CARDIO_POLLING_INTERVAL': 30000      });




  </script>


<script>yt.setConfig({'EVENT_ID': "hryvUcbTFeeNkAL4p4HQBQ",'PAGE_NAME': "watch",'LOGGED_IN': false,'SESSION_INDEX': null,'CURRENT_URL': "http:\/\/www.youtube.com\/watch?v=_BFJN62hZp0",'MASTHEAD_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-masthead-vflvU_tXo.js",'JS_COMMON_MODULE': "\/\/s.ytimg.com\/yts\/jsbin\/www_common_mod-vflq05hub.js",'SAFETY_MODE_PENDING': false,'LOCAL_DATE_TIME_CONFIG': {"formatLongDate": "MMMM d, yyyy h:mm a", "formatWeekdayShortTime": "EE h:mm a", "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "weekdays": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "formatShortDate": "MMM d, yyyy", "formatLongDateOnly": "MMMM d, yyyy", "shortMonths": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], "amPms": ["AM", "PM"], "shortWeekdays": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]},'FEEDBACK_BUCKET_ID': "Watch",'FEEDBACK_LOCALE_LANGUAGE': "en",'FEEDBACK_LOCALE_EXTRAS': {"experiments": "900352,924605,928201,901208,929123,929121,929915,929906,925714,929919,929119,931202,928017,912512,912518,906906,904830,930807,919373,906836,933701,900816,912711,929606,910075", "guide_subs": "NA", "is_partner": "", "logged_in": false, "accept_language": null, "is_branded": ""}});yt.setMsg({'ADDTO_WATCH_LATER': "Watch Later",'ADDTO_WATCH_LATER_ADDED': "Added",'ADDTO_WATCH_LATER_ERROR': "Error"});yt.setAjaxToken('addto_ajax_logged_out', "ExhjRbReQDc38nCNVXaKXk7KtUZ8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");  yt.setConfig('FEED_PRIVACY_CSS_URL', "http:\/\/s.ytimg.com\/yts\/cssbin\/www-feedprivacydialog-vflmpM6y2.css");
  yt.setAjaxToken('feed_privacy_ajax', "OZ5MY0WAVs9YdBW9s7BbQnGqZzJ8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4");
    yt.setConfig('FEED_PRIVACY_LIGHTBOX_ENABLED', true);
yt.setConfig({'SBOX_JS_URL': "\/\/s.ytimg.com\/yts\/jsbin\/www-searchbox-vfl5XnjkO.js",'SBOX_SETTINGS': {"REQUEST_DOMAIN": "us", "REQUEST_LANGUAGE": "en", "CHIP_PARAMETERS": {}, "SESSION_INDEX": null, "HAS_ON_SCREEN_KEYBOARD": false, "PSUGGEST_TOKEN": null, "USE_HTTPS": false, "CLOSE_ICON_URL": "\/\/s.ytimg.com\/yts\/img\/icons\/close-vflrEJzIW.png", "SHOW_CHIP": false, "EXPERIMENT_ID": -1},'SBOX_LABELS': {"SUGGESTION_DISMISSED_LABEL": "Suggestion dismissed", "SUGGESTION_DISMISS_LABEL": "Dismiss", "WATCH_NOW_LABEL": "Watch now", "VIEW_CHANNEL_LABEL": "View channel"}});  yt.setConfig({
    'YPC_LOADER_ENABLED': true,
    'YPC_LOADER_CONFIGS': "\/ypc_config_ajax",
    'YPC_LOADER_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-ypc-vflmtgBB2.js",
    'YPC_LOADER_CSS': "http:\/\/s.ytimg.com\/yts\/cssbin\/www-ypc-vflRGdYjt.css",
    'YPC_LOADER_CALLBACKS': ['yt.www.ypc.checkout.init', 'yt.www.ypc.subscription.init']
  });
</script>    <script>
ytcsi.span('st', 141);yt.setConfig({'TIMING_ACTION': "watch,watch7",'TIMING_INFO': {"yt_pt": "flash", "yt_ad": 0, "yt_lt": "cold", "e": "", "yt_spf": 0, "yt_li": 0, "ei": "hryvUcbTFeeNkAL4p4HQBQ"}});    </script>
<script>yt.setConfig({'XSRF_TOKEN': "d09ypn0XRsI8VONBzDuZOv5pZFh8MTM3MDU1Nzk1OEAxMzcwNDcxNTU4",'XSRF_REDIRECT_TOKEN': "6Pe_v6cdd8afrWk3pCgm1CUQxm18MTM3MDU1Nzk1OEAxMzcwNDcxNTU4",'XSRF_FIELD_NAME': "session_token"});</script><script>yt.setConfig('THUMB_DELAY_LOAD_BUFFER', 0);</script><script>if (window.ytcsi) {ytcsi.tick("js_foot");}</script><div id="debug"></div></body></html>

    <!DOCTYPE html><html lang="en" data-cast-api-enabled="true"><head>  <script>var ytcsi = {data_: {tick: {},span: {},info: {}},tick: function(l, t) {ytcsi.data_.tick[l] = t || +new Date();},span: function(l, s) {ytcsi.data_.span[l] = (typeof s == 'number') ? s :+new Date() - ytcsi.data_.tick[l];},info: function(k, v) {ytcsi.data_.info[k] = v;}};ytcsi.tick('_start');if (document.webkitVisibilityState == 'prerender') {ytcsi.info('prerender', 1);document.addEventListener('webkitvisibilitychange', function() {ytcsi.tick('_start');}, false);}try {ytcsi.pt_ = (window.chrome && chrome.csi().pageT ||window.gtbExternal && gtbExternal.pageT() ||window.external && external.pageT);if (ytcsi.pt_) {ytcsi.info('pt', Math.floor(ytcsi.pt_));}} catch(e) {}</script>
<script>var ytdns = {};ytdns.ping = function(src, num) {var img = new Image();ytdns[num] = img;img.onload = img.onerror = function() {delete ytdns[num];};img.src = src;};ytdns.ping("http:\/\/r13---sn-qxo7sn7l.c.youtube.com\/crossdomain.xml", 2);ytdns.ping("http:\/\/r13---sn-qxo7sn7l.c.youtube.com\/generate_204", 3);</script>  <link id="css-982818953" rel="stylesheet" href="http://s.ytimg.com/yts/cssbin/www-core-vflScjXzY.css">

  <title>Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland - YouTube</title><link rel="search" type="application/opensearchdescription+xml" href="http://www.youtube.com/opensearch?locale=en_US" title="YouTube Video Search"><link rel="shortcut icon" href="http://s.ytimg.com/yts/img/favicon-vfldLzJxy.ico" type="image/x-icon">     <link rel="icon" href="//s.ytimg.com/yts/img/favicon_32-vflWoMFGx.png" sizes="32x32"><link rel="canonical" href="http://www.youtube.com/watch?v=OyJ3CafAM1Q"><link rel="alternate" media="handheld" href="http://m.youtube.com/watch?v=OyJ3CafAM1Q"><link rel="alternate" media="only screen and (max-width: 640px)" href="http://m.youtube.com/watch?v=OyJ3CafAM1Q"><link rel="shortlink" href="http://youtu.be/OyJ3CafAM1Q">      <meta name="title" content="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">

      <meta name="description" content="Lake Region Audubon Society has nominated Circle B Bar Reserve in Lakeland as one of Florida&#39;s Special Places. You can nominate your favorite natural Florida...">

      <meta name="keywords" content="Audubon, Florida, Lakeland, Circle B Bar, Lake Region, birds, Florida&#39;s Special Places, conservation, politics, bird, nature, wildlife">

      <link rel="alternate" type="application/json+oembed" href="http://www.youtube.com/oembed?url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DOyJ3CafAM1Q&amp;format=json" title="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">
  <link rel="alternate" type="text/xml+oembed" href="http://www.youtube.com/oembed?url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DOyJ3CafAM1Q&amp;format=xml" title="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">

        <meta property="og:site_name" content="YouTube">
    <meta property="og:url" content="http://www.youtube.com/watch?v=OyJ3CafAM1Q">
    <meta property="og:title" content="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">
    <meta property="og:type" content="video">
    <meta property="og:image" content="http://i4.ytimg.com/vi/OyJ3CafAM1Q/hqdefault.jpg?feature=og">

      <meta property="og:description" content="Lake Region Audubon Society has nominated Circle B Bar Reserve in Lakeland as one of Florida&#39;s Special Places. You can nominate your favorite natural Florida...">

      <meta property="og:video" content="http://www.youtube.com/v/OyJ3CafAM1Q?version=3&amp;autohide=1">
      <meta property="og:video:type" content="application/x-shockwave-flash">
      <meta property="og:video:width" content="480">
      <meta property="og:video:height" content="360">

    <meta property="fb:app_id" content="87741124305">

        <meta name="twitter:card" content="player">
    <meta name="twitter:site" content="@youtube">
    <meta name="twitter:url" content="http://www.youtube.com/watch?v=OyJ3CafAM1Q">
    <meta name="twitter:title" content="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">
    <meta name="twitter:description" content="Lake Region Audubon Society has nominated Circle B Bar Reserve in Lakeland as one of Florida&#39;s Special Places. You can nominate your favorite natural Florida...">
    <meta name="twitter:image" content="http://i4.ytimg.com/vi/OyJ3CafAM1Q/hqdefault.jpg">
      <meta name="twitter:player" content="https://www.youtube.com/embed/OyJ3CafAM1Q">
      <meta name="twitter:player:width" content="480">
      <meta name="twitter:player:height" content="360">

  
<script>if (window.ytcsi) {ytcsi.tick("ct");}</script></head><!-- machid: pQkVLQURfd1pHaE8wYlNKWGZaSjlHOE12N1UtWllzU1FSUW1laXpHaE4xeWFsRlhjc3hxeVBn -->

      <body dir="ltr" class="  ltr    exp-grouped-results  site-left-aligned  exp-new-site-width  exp-watch7-comment-ui  hitchhiker-enabled      guide-enabled guide-collapsed sidebar-expanded   ">

  <div id="body-container"><form name="logoutForm" method="POST" action="/logout"><input type="hidden" name="action_logout" value="1"></form>    
    
    <div id="yt-masthead-container" class="yt-grid-box"><div id="yt-masthead" class="">    <a id="logo-container" href="/" title="YouTube home" class=" "><img id="logo" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="YouTube home"></a>
<div id="yt-masthead-signin"><button href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dsign_in_button%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" type="button" class=" yt-uix-button yt-uix-button-primary" onclick=";window.location.href=this.getAttribute(&#39;href&#39;);return false;"  role="button"><span class="yt-uix-button-content">Sign in </span></button></div><div id="yt-masthead-content"><span id="masthead-upload-button-group"><a href="//www.youtube.com/upload" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-default" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=mhsb"><span class="yt-uix-button-content">Upload</span></a></span><form id="masthead-search" class="search-form consolidated-form" action="/results" onsubmit="if (_gel(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false;"><button onclick="if (_gel(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false; _gel(&#39;masthead-search&#39;).submit(); return false;;return true;" class="search-btn-component search-button yt-uix-button yt-uix-button-default" dir="ltr" tabindex="2" type="submit" id="search-btn"  role="button"><span class="yt-uix-button-content">Search </span></button><div id="masthead-search-terms" class="masthead-search-terms-border" dir="ltr"><label><input id="masthead-search-term"  class="search-term yt-uix-form-input-bidi" name="search_query" value="" type="text" tabindex="1" title="Search"></label></div></form></div></div></div>
    
<div id="alerts">  



</div><div id="header"></div><div id="page-container"><div id="page" class="  watch   clearfix"><div id="guide" >        <div id="guide-container" class="    collapsible-guide ">
      <div id="guide-main" class="    guide-module collapsed     spf-nolink ">
    <div class="guide-module-toggle">
      <span class="guide-module-toggle-icon">
        <span class="guide-module-toggle-arrow"></span>
        <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="">
        <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" id="collapsed-notification-icon">
      </span>
      <div class="guide-module-toggle-label">
        <h3>
          <span>
Guide
          </span>
        </h3>
      </div>
    </div>
      <div class="guide-module-content yt-scrollbar">
    <ul class="guide-toplevel">
      <li id="guide-subscriptions-section" class="guide-section without-filter guide-section-no-counts">
        <div id="guide-subs-footer-container">
            <div id="guide-subscriptions-container">
              
  <div class="guide-channels-content yt-scrollbar">
      <ul  id="guide-channels" class="guide-channels-list guide-item-container yt-uix-scroller filter-has-matches">
          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/"
        title="Popular on YouTube"
      data-channel-id="youtube"
      data-sessionlink="ved=CAMQgB8oAA&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/tnHdj3df7iM/default.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Popular on YouTube</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/music"
        title="Music"
      data-channel-id="HCp-Rdqh3z4Uc"
      data-sessionlink="ved=CAQQgB8oAQ&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/p-Rdqh3z4Uc/default.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Music</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/sports"
        title="Sports"
      data-channel-id="HC7Dr1BKwqctY"
      data-sessionlink="ved=CAUQgB8oAg&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i4.ytimg.com/li/7Dr1BKwqctY/default.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Sports</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/gaming"
        title="Gaming"
      data-channel-id="HChfZhJdhTqX8"
      data-sessionlink="ved=CAYQgB8oAw&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/hfZhJdhTqX8/default.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Gaming</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/movies"
        title="Movies"
      data-channel-id="UCczhp4wznQWonO7Pb8HQ2MQ"
      data-sessionlink="ved=CAcQgB8oBA&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i4.ytimg.com/i/czhp4wznQWonO7Pb8HQ2MQ/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Movies</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/YouTubeShowsUS"
        title="TV Shows"
      data-channel-id="UCl8dMTqDrJQ0c8y23UBu4kQ"
      data-sessionlink="ved=CAgQgB8oBQ&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i1.ytimg.com/i/l8dMTqDrJQ0c8y23UBu4kQ/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>TV Shows</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/news"
        title="News"
      data-channel-id="HCPvDBPPFfuaM"
      data-sessionlink="ved=CAkQgB8oBg&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i1.ytimg.com/li/PvDBPPFfuaM/default.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>News</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCBR8-60-B28hp2BmDPdntcQ"
        title="Spotlight"
      data-channel-id="UCBR8-60-B28hp2BmDPdntcQ"
      data-sessionlink="ved=CAoQgB8oBw&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-channel"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/BR8-60-B28hp2BmDPdntcQ/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Spotlight</span>
          </span>
      </span>

    </a>
  </li>

        <li id="guide-filter-no-results">
No channels found
        </li>
        <li id="guide-filter-loading-results">
            <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
        Loading subscriptions
    </span>
  </p>

        </li>
      </ul>
  </div>

            </div>
            <hr class="guide-section-separator">
        </div>
      </li>
        <li id="guide-subscription-suggestions-section" class="guide-section guide-section-no-counts">
            <h3>
Channels for you
            </h3>
            <div class="guide-recommendations-list">
              
  <div class="guide-channels-content yt-scrollbar">
      <ul  class="guide-channels-list guide-item-container yt-uix-scroller filter-has-matches">
          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCBR8-60-B28hp2BmDPdntcQ"
        title="YouTube Spotlight"
      data-channel-id="UCBR8-60-B28hp2BmDPdntcQ"
      data-sessionlink="ved=CAwQgB8oAA&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-chrec"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/BR8-60-B28hp2BmDPdntcQ/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>YouTube Spotlight</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCry7B7DGVgUIa6k4Tis_DJQ"
        title="The Ricky Gervais Channel"
      data-channel-id="UCry7B7DGVgUIa6k4Tis_DJQ"
      data-sessionlink="ved=CA0QgB8oAQ&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-chrec"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/ry7B7DGVgUIa6k4Tis_DJQ/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>The Ricky Gervais Channel</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCHX5-wIWTaClDu6uTKXKItg"
        title="Truthloader"
      data-channel-id="UCHX5-wIWTaClDu6uTKXKItg"
      data-sessionlink="ved=CA4QgB8oAg&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-chrec"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i1.ytimg.com/i/HX5-wIWTaClDu6uTKXKItg/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>Truthloader</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UCuw8B6Uv0cMWtV5vbNpeH_A"
        title="DigitalRev TV"
      data-channel-id="UCuw8B6Uv0cMWtV5vbNpeH_A"
      data-sessionlink="ved=CA8QgB8oAw&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-chrec"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i2.ytimg.com/i/uw8B6Uv0cMWtV5vbNpeH_A/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>DigitalRev TV</span>
          </span>
      </span>

    </a>
  </li>

          



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/feed/UC2C_jShtL725hvbm1arSV9w"
        title="C. G. P. Grey"
      data-channel-id="UC2C_jShtL725hvbm1arSV9w"
      data-sessionlink="ved=CBAQgB8oBA&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-chrec"
    >
      <span class="" >
          <span class="thumb">    <span class="video-thumb  yt-thumb yt-thumb-18"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thumbnail" data-thumb-manual="1" data-thumb="//i3.ytimg.com/i/2C_jShtL725hvbm1arSV9w/1.jpg" data-group-key="guide-channel-thumbs" width="18" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</span>
          <span class="display-name">
            <span>C. G. P. Grey</span>
          </span>
      </span>

    </a>
  </li>

        <li id="guide-filter-no-results">
No channels found
        </li>
        <li id="guide-filter-loading-results">
            <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
        Loading subscriptions
    </span>
  </p>

        </li>
      </ul>
  </div>

            </div>
            <hr class="guide-section-separator">
            <ul id="gh-management" class="guide-item-container">
        



  <li class="guide-channel" >
    <a class="guide-item yt-uix-sessionlink  "
      href="/channels"
        title="Browse channels"
      data-channel-id="guide_builder"
      data-sessionlink="ved=CBIQhx8oAA&amp;ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=g-manage"
    >
      <span class="" >
          <span class="thumb guide-management-plus-icon">
            <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="">
          </span>
          <span>Browse channels</span>
      </span>

    </a>
  </li>

  </ul>

        </li>
    </ul>
        <div class="guide-section guide-header signup-promo guided-help-box">
    <p>
Sign in to add channels to your guide and for great recommendations!
    </p>
    <div id="guide-builder-promo-buttons" class="signed-out clearfix">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dsign_in_promo%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in &#8250;</span></a>
    </div>
  </div>

  </div>

  </div>

      <div id="watch-context-container" class="guide-module collapsed hid"></div>

  </div>

</div><div id="content" class="">  <div id="watch7-container" class="  transition-content  " itemscope itemid="" itemtype="http://schema.org/VideoObject">
        <link itemprop="url" href="http://www.youtube.com/watch?v=OyJ3CafAM1Q">
    <meta itemprop="name" content="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">
    <meta itemprop="description" content="Lake Region Audubon Society has nominated Circle B Bar Reserve in Lakeland as one of Florida&#39;s Special Places. You can nominate your favorite natural Florida...">
    <meta itemprop="paid" content="False">

      <meta itemprop="duration" content="PT2M27S">
      <meta itemprop="unlisted" content="False">

        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="http://www.youtube.com/user/AudubonFL">
        </span>
        <span itemprop="author" itemscope itemtype="http://schema.org/Person">
          <link itemprop="url" href="https://plus.google.com/100086430334922344272">
        </span>

    <link itemprop="thumbnailUrl" href="http://i4.ytimg.com/vi/OyJ3CafAM1Q/hqdefault.jpg">
    <span itemprop="thumbnail" itemscope itemtype="http://schema.org/ImageObject">
      <link itemprop="url" href="http://i4.ytimg.com/vi/OyJ3CafAM1Q/hqdefault.jpg">
      <meta itemprop="width" content="320">
      <meta itemprop="height" content="180">
    </span>

      <link itemprop="embedURL" href="http://www.youtube.com/v/OyJ3CafAM1Q?version=3&amp;autohide=1">
      <meta itemprop="playerType" content="Flash">
      <meta itemprop="width" content="480">
      <meta itemprop="height" content="360">

      <meta itemprop="isFamilyFriendly" content="True">
      <meta itemprop="regionsAllowed" content="AD,AE,AF,AG,AI,AL,AM,AO,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BL,BM,BN,BO,BQ,BR,BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CW,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MF,MG,MH,MK,ML,MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,SS,ST,SV,SX,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,TM,TN,TO,TR,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW">


      <div id="player" class="">
        
  <div id="playlist">
    
  </div>
  <div id="player-unavailable" class="    hid  ">
            <img class="icon meh" src="//s.ytimg.com/yts/img/meh7-vflGevej7.png" alt="">
  <div class="content">
    <h1 id="unavailable-message" class="message">
            This video is unavailable.
    </h1>
    <div class="submessage">
    </div>
  </div>


  </div>

  <script>if (window.ytcsi) {ytcsi.tick("bf");}</script>

      <div id="player-api" class="player-width player-height off-screen-target"></div>


    <script>var ytplayer = ytplayer || {};ytplayer.config = {"url_v9as2": "http:\/\/s.ytimg.com\/yts\/swfbin\/cps-vfltj6hEE.swf", "url_v8": "http:\/\/s.ytimg.com\/yts\/swfbin\/cps-vfltj6hEE.swf", "assets": {"html": "\/html5_player_template", "css": "http:\/\/s.ytimg.com\/yts\/cssbin\/www-player-vflgp4Cz9.css", "js": "http:\/\/s.ytimg.com\/yts\/jsbin\/html5player-vflDG7-a-.js"}, "min_version": "8.0.0", "html5": false, "url": "http:\/\/s.ytimg.com\/yts\/swfbin\/watch_as3-vflrdHchm.swf", "args": {"ad_video_pub_id": "ca-pub-6219811747049371", "cafe_experiment_id": "", "idpj": "0", "c": "WEB", "yt_pt": "AL4CsgEH_AC3KNPqCT_ToQSkqO8EbV6vGQWZl7pha_Q4x0MH4y_lDEWtVOzpl5cKKdj_fPnT7HQ81xmXA_JJ9kxjgRcPtji-0mmPb1q9yTjB3QJ1Sx6AA0axDTkmdG5FtFh0h0u0MqQv_smWdPSJ", "prefetch_ad_live_stream": true, "autohide": "2", "as_launched_in_country": "1", "endscreen_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/endscreen-vflKOX8EP.swf", "mpu": true, "ptk": "youtube_multi", "gut_tag": "\/4061\/ytpwatch\/main_2569964", "ad_flags": 1, "afv_ad_tag": "http:\/\/googleads.g.doubleclick.net\/pagead\/ads?ytdevice=1\u0026host=ca-host-pub-1800120140230655\u0026description_url=http%3A%2F%2Fwww.youtube.com%2Fvideo%2FOyJ3CafAM1Q\u0026loeid=917000%2C923002%2C929201%2C916626\u0026client=ca-pub-6219811747049371\u0026hl=en\u0026ht_id=389538\u0026ad_type=text_image_flash\u0026channel=invideo_overlay_480x70_cat29%2Bafv_overlay%2BVertical_65%2BVertical_66%2BVertical_119%2BVertical_563%2BVertical_884%2Bafv_ugc%2Byt_mpvid_AATe6HfXIJQ-D5j2%2Byt_cid_2569964%2Bytdevice_1%2Bytps_default%2Bytel_detailpage", "ucid": "UCZwNj6gw95JMmeczpcNRiQg", "adsense_video_doc_id": "yt_OyJ3CafAM1Q", "invideo": true, "ad3_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/ad3-vfliDqBOd.swf", "dclk": true, "share_icons": "http:\/\/s.ytimg.com\/yts\/swfbin\/sharing-vflF4tO1T.swf", "pyv_in_related_cafe_experiment_id": "", "referrer": null, "sendtmp": "1", "cid": 2569964, "account_playback_token": "_cTMgljoLNK95C808UpmqOgmVj98MTM3MTA3NjMzMUAxMzcwOTg5OTMx", "mpvid": "AATe6HfXIJQ-D5j2", "ad_device": 1, "showpopout": 1, "no_get_video_log": "1", "ad_host": "ca-host-pub-1800120140230655", "fmt_list": "43\/640x360\/99\/0\/0,34\/640x360\/9\/0\/115,18\/640x360\/9\/0\/115,5\/320x240\/7\/0\/0,36\/320x240\/99\/0\/0,17\/176x144\/99\/0\/0", "vq": "auto", "sk": "I01cEMXv7aU4m_U6WXeuchcbYFBCjiSDC", "ad_logging_flag": 1, "url_encoded_fmt_stream_map": "sig=630933CA5B491434DDDCD129ED8C43A1B512C552.33CF18D6911B36247D49EE3C4498361A73E655F5\u0026quality=medium\u0026url=http%3A%2F%2Fr13---sn-qxo7sn7l.c.youtube.com%2Fvideoplayback%3Fexpire%3D1371014388%26fexp%3D917000%252C923002%252C929201%252C916626%252C900352%252C921047%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C929907%252C929125%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912515%252C912521%252C906906%252C904488%252C931910%252C931913%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C926403%252C912711%252C930618%252C930621%252C929606%252C910075%26newshard%3Dyes%26mt%3D1370989896%26ip%3D97.114.104.96%26itag%3D43%26ratebypass%3Dyes%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ms%3Dau%26ipbits%3D8%26upn%3D1ndc1Jz1vQ0%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire%26cp%3DU0hWRlBMUl9NUkNONl9IRlZEOnZvbEplRDhNMDBR%26id%3D3b227709a7c03354%26key%3Dyt1\u0026itag=43\u0026fallback_host=tc.v3.cache1.c.youtube.com\u0026type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22,sig=2B93DBF5BDA9AE5F0A0EABC254D43A227B06A3A3.6A5B86A949927A19BEF62F04A84A120CA680024C\u0026quality=medium\u0026url=http%3A%2F%2Fr13---sn-qxo7sn7l.c.youtube.com%2Fvideoplayback%3Fexpire%3D1371014388%26ip%3D97.114.104.96%26newshard%3Dyes%26mt%3D1370989896%26ipbits%3D8%26fexp%3D917000%252C923002%252C929201%252C916626%252C900352%252C921047%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C929907%252C929125%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912515%252C912521%252C906906%252C904488%252C931910%252C931913%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C926403%252C912711%252C930618%252C930621%252C929606%252C910075%26sver%3D3%26factor%3D1.25%26source%3Dyoutube%26mv%3Dm%26key%3Dyt1%26ms%3Dau%26itag%3D34%26upn%3D1ndc1Jz1vQ0%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26cp%3DU0hWRlBMUl9NUkNONl9IRlZEOnZvbEplRDhNMDBR%26id%3D3b227709a7c03354%26algorithm%3Dthrottle-factor%26burst%3D40\u0026itag=34\u0026fallback_host=tc.v24.cache3.c.youtube.com\u0026type=video%2Fx-flv,sig=A4EC1D4A8DCFD7AECEFC97AB3C7D0DAF20394543.5219DBEF71929AB069A744FCA99E8C6833F60225\u0026quality=medium\u0026url=http%3A%2F%2Fr13---sn-qxo7sn7l.c.youtube.com%2Fvideoplayback%3Fexpire%3D1371014388%26fexp%3D917000%252C923002%252C929201%252C916626%252C900352%252C921047%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C929907%252C929125%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912515%252C912521%252C906906%252C904488%252C931910%252C931913%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C926403%252C912711%252C930618%252C930621%252C929606%252C910075%26newshard%3Dyes%26mt%3D1370989896%26ip%3D97.114.104.96%26itag%3D18%26ratebypass%3Dyes%26source%3Dyoutube%26mv%3Dm%26sver%3D3%26ms%3Dau%26ipbits%3D8%26upn%3D1ndc1Jz1vQ0%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire%26cp%3DU0hWRlBMUl9NUkNONl9IRlZEOnZvbEplRDhNMDBR%26id%3D3b227709a7c03354%26key%3Dyt1\u0026itag=18\u0026fallback_host=tc.v17.cache4.c.youtube.com\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.42001E%2C+mp4a.40.2%22,sig=C780F3C8674B61C8D0D16762A88296000E166628.0127EEC12E4C0DF24C40A75F06D4792AEA828298\u0026quality=small\u0026url=http%3A%2F%2Fr13---sn-qxo7sn7l.c.youtube.com%2Fvideoplayback%3Fexpire%3D1371014388%26ip%3D97.114.104.96%26newshard%3Dyes%26mt%3D1370989896%26ipbits%3D8%26fexp%3D917000%252C923002%252C929201%252C916626%252C900352%252C921047%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C929907%252C929125%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912515%252C912521%252C906906%252C904488%252C931910%252C931913%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C926403%252C912711%252C930618%252C930621%252C929606%252C910075%26sver%3D3%26factor%3D1.25%26source%3Dyoutube%26mv%3Dm%26key%3Dyt1%26ms%3Dau%26itag%3D5%26upn%3D1ndc1Jz1vQ0%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26cp%3DU0hWRlBMUl9NUkNONl9IRlZEOnZvbEplRDhNMDBR%26id%3D3b227709a7c03354%26algorithm%3Dthrottle-factor%26burst%3D40\u0026itag=5\u0026fallback_host=tc.v3.cache5.c.youtube.com\u0026type=video%2Fx-flv,sig=5DE72A38BA27E0155EB573051BFF335092B06C7A.A817EA105EF2D5078AAB22C2840B4E86325AA2E2\u0026quality=small\u0026url=http%3A%2F%2Fr13---sn-qxo7sn7l.c.youtube.com%2Fvideoplayback%3Fexpire%3D1371014388%26ip%3D97.114.104.96%26newshard%3Dyes%26mt%3D1370989896%26ipbits%3D8%26fexp%3D917000%252C923002%252C929201%252C916626%252C900352%252C921047%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C929907%252C929125%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912515%252C912521%252C906906%252C904488%252C931910%252C931913%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C926403%252C912711%252C930618%252C930621%252C929606%252C910075%26sver%3D3%26factor%3D1.25%26source%3Dyoutube%26mv%3Dm%26key%3Dyt1%26ms%3Dau%26itag%3D36%26upn%3D1ndc1Jz1vQ0%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26cp%3DU0hWRlBMUl9NUkNONl9IRlZEOnZvbEplRDhNMDBR%26id%3D3b227709a7c03354%26algorithm%3Dthrottle-factor%26burst%3D40\u0026itag=36\u0026fallback_host=tc.v10.cache5.c.youtube.com\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22,sig=5CCCED64E0B162B126CDE6F73892FB843664A4CE.D6CE3E151BC7E42D2C359E056CA659CF5A92DC33\u0026quality=small\u0026url=http%3A%2F%2Fr13---sn-qxo7sn7l.c.youtube.com%2Fvideoplayback%3Fexpire%3D1371014388%26ip%3D97.114.104.96%26newshard%3Dyes%26mt%3D1370989896%26ipbits%3D8%26fexp%3D917000%252C923002%252C929201%252C916626%252C900352%252C921047%252C924605%252C928201%252C901208%252C929123%252C929121%252C929915%252C929906%252C929907%252C929125%252C925714%252C929919%252C929119%252C931202%252C928017%252C912512%252C912515%252C912521%252C906906%252C904488%252C931910%252C931913%252C904830%252C930807%252C919373%252C906836%252C933701%252C900816%252C926403%252C912711%252C930618%252C930621%252C929606%252C910075%26sver%3D3%26factor%3D1.25%26source%3Dyoutube%26mv%3Dm%26key%3Dyt1%26ms%3Dau%26itag%3D17%26upn%3D1ndc1Jz1vQ0%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire%26cp%3DU0hWRlBMUl9NUkNONl9IRlZEOnZvbEplRDhNMDBR%26id%3D3b227709a7c03354%26algorithm%3Dthrottle-factor%26burst%3D40\u0026itag=17\u0026fallback_host=tc.v17.cache2.c.youtube.com\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22", "ad_host_tier": 389538, "length_seconds": 147, "afv_inslate_ad_tag": "http:\/\/googleads.g.doubleclick.net\/pagead\/ads?ytdevice=1\u0026host=ca-host-pub-1800120140230655\u0026description_url=http%3A%2F%2Fwww.youtube.com%2Fvideo%2FOyJ3CafAM1Q\u0026loeid=917000%2C923002%2C929201%2C916626\u0026client=ca-pub-6219811747049371\u0026ht_id=389538\u0026ad_type=userchoice\u0026hl=en", "sffb": true, "t": "vjVQa1PpcFPfJboBdFyjjvilc9Odb3OvcfOyR__MVYk=", "title": "Florida's Special Places: Circle B Bar Reserve in Lakeland", "ad_channel_code_overlay": "invideo_overlay_480x70_cat29,afv_overlay,Vertical_65,Vertical_66,Vertical_119,Vertical_563,Vertical_884,afv_ugc,yt_mpvid_AATe6HfXIJQ-D5j2,yt_cid_2569964,ytdevice_1,ytps_default,ytel_detailpage", "fexp": "917000,923002,929201,916626,900352,921047,924605,928201,901208,929123,929121,929915,929906,929907,929125,925714,929919,929119,931202,928017,912512,912515,912521,906906,904488,931910,931913,904830,930807,919373,906836,933701,900816,926403,912711,930618,930621,929606,910075", "enablejsapi": 1, "tmi": "1", "watermark": ",http:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_watermark-vflHX6b6E.png,http:\/\/s.ytimg.com\/yts\/img\/watermark\/youtube_hd_watermark-vflAzLcD6.png", "timestamp": 1370989931, "disable_non_adsense_ssl_companions": true, "allow_embed": 1, "ad_eurl": "http:\/\/www.youtube.com\/video\/OyJ3CafAM1Q", "cr": "US", "abd": "1", "csi_page_type": "watch,watch7ad", "is_html5_mobile_device": false, "tk": "1", "loeid": "917000,923002,929201,916626", "host_language": "en", "afv": true, "no_afv_instream": "1", "hl": "en_US", "oid": "LtuniTgT0PFayH9n3PW4_A.ZP6trPnP707Uw7I8kjT4Eg", "keywords": "Audubon,Florida,Lakeland,Circle B Bar,Lake Region,birds,Florida's Special Places,conservation,politics,bird,nature,wildlife", "playlist_module": "http:\/\/s.ytimg.com\/yts\/swfbin\/playlist_module-vfl1txF_X.swf", "shortform": true, "rvs": "featured=1\u0026feature_type=fvwp\u0026title=Circle+B+Bar+Reserve\u0026view_count=2%2C515\u0026length_seconds=150\u0026id=sA8uJ54IpDI\u0026author=kwilli75,view_count=1%2C374\u0026author=mflynn2009\u0026length_seconds=407\u0026id=CDoNiT_2RVE\u0026title=Circle+B+Bar+Reserve+-+Lakeland+Area,view_count=5%2C268\u0026author=yourboypaulie\u0026length_seconds=388\u0026id=zZXUi8noht8\u0026title=Wildlife+at+Circle+B+Bar+Ranch%2C+Lakeland%2C+FL,view_count=7%2C872\u0026author=Audubon+Florida\u0026length_seconds=166\u0026id=3507Wkj3_yE\u0026title=Florida%27s+Special+Places%3A+Corkscrew+Swamp+Sanctuary+-+The+Heart+of+the+Western+Everglades,view_count=437\u0026author=Kesh+Butler\u0026length_seconds=448\u0026id=dJOLObQyhdY\u0026title=A+hike+at+the+Circle+B+Bar+Reserve+in+Lakeland%2C+Florida%2C+January+9%2C+2011,view_count=272\u0026author=Tanyia48\u0026length_seconds=338\u0026id=ziIMB8fcX8Q\u0026title=Circle+B+Bar+Reserve+1-14-2011,view_count=1%2C748\u0026author=Audubon+Florida\u0026length_seconds=44\u0026id=ZY06eqdCfw4\u0026title=A+Florida+Panther+Cruises+the+Boardwalk+at+Audubon%27s+Corkscrew+Swamp+Sanctuary,view_count=471\u0026author=Polk+Government\u0026length_seconds=170\u0026id=hyt6wnFpU0o\u0026title=Circle+B+Bar+Reserve+Introduction,view_count=5%2C193\u0026author=SandieM0731\u0026length_seconds=148\u0026id=BRe-eDY46aQ\u0026title=Identification+of+Bird+of+Prey%2C+The+Osprey+Devouring+%26+Eating+Live+Fish+at+Circle+B+Bar+Reserve,view_count=1%2C357\u0026author=Robert+Beaudreault\u0026length_seconds=322\u0026id=8kvQWXGG9Sw\u0026title=Lakeland%2C+FL+OFFICIAL+World%27s+Largest+Simultaneous+Flashmob,view_count=10%2C783\u0026author=TpindellTV\u0026length_seconds=526\u0026id=VMLQoSjbz14\u0026title=Kickin%27+it+with+Tpindell+6+%23FiestaMovement,view_count=1%2C842\u0026author=tpwellman\u0026length_seconds=377\u0026id=rhAkLyJESgE\u0026title=Peace+River+Kayak+Trip+-+105+miles%2F3+days", "pltype": "contentugc", "inactive_skippable_threshold": 600000, "plid": "AATe6HfWuA-RXscK", "ad_slots": "0", "video_id": "OyJ3CafAM1Q", "ad_tag": "http:\/\/ad.doubleclick.net\/N4061\/pfadx\/com.ytpwatch.nonprofit\/main_2569964;sz=WIDTHxHEIGHT;kvid=OyJ3CafAM1Q;kpu=AudubonFL;kpeid=ZwNj6gw95JMmeczpcNRiQg;kpid=2569964;u=OyJ3CafAM1Q|2569964;mpvid=AATe6HfXIJQ-D5j2;plat=pc;afct=site_content;afv=1;dc_dedup=1;k5=65_66_119_563_884;kclg=1;kclt=1;kcr=us;kga=-1;kgg=-1;klg=en;ko=c;kpco=582411;kr=H;kvz=203;nlfb=1;shortform=1;tves=1;ytcat=29;ytdevice=1;ytexp=917000,923002,929201,916626;ytps=default;ytvt=w;!c=2569964;k2=65;k2=66;k2=119;k2=563;k2=884;kvlg=en;", "ldpj": "-6", "enablecsi": "1"}, "params": {"allowscriptaccess": "always", "allowfullscreen": "true", "bgcolor": "#000000"}, "attrs": {"id": "movie_player"}, "sts": 1586};</script>    <script>
      (function() {
        ytplayer.config.loaded = true;
        var encoded = [];
        for (var key in ytplayer.config.args) {
          encoded.push(encodeURIComponent(key) + '=' + encodeURIComponent(ytplayer.config.args[key]));
        }
        var swf = "      \u003cembed type=\"application\/x-shockwave-flash\"     s\u0072c=\"http:\/\/s.ytimg.com\/yts\/swfbin\/watch_as3-vflrdHchm.swf\"     id=\"movie_player\"    flashvars=\"__flashvars__\"     allowscriptaccess=\"always\" allowfullscreen=\"true\" bgcolor=\"#000000\"\u003e\n  \u003cnoembed\u003e\u003cdiv class=\"yt-alert yt-alert-default yt-alert-error  yt-alert-player\"\u003e  \u003cdiv class=\"yt-alert-icon\"\u003e\n    \u003cimg s\u0072c=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" class=\"icon master-sprite\" alt=\"Alert icon\"\u003e\n  \u003c\/div\u003e\n\u003cdiv class=\"yt-alert-buttons\"\u003e\u003c\/div\u003e\u003cdiv class=\"yt-alert-content\" role=\"alert\"\u003e    \u003cspan class=\"yt-alert-vertical-trick\"\u003e\u003c\/span\u003e\n    \u003cdiv class=\"yt-alert-message\"\u003e\n            You need Adobe Flash Player to watch this video. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eDownload it from Adobe.\u003c\/a\u003e\n    \u003c\/div\u003e\n\u003c\/div\u003e\u003c\/div\u003e\u003c\/noembed\u003e\n\n";
        swf = swf.replace('__flashvars__', encoded.join('&'));
        document.getElementById("player-api").innerHTML = swf;
      })();
    </script>


  

  <div id="player-branded-banner">
    
  </div>

      </div>

    <div id="watch7-main-container">
      <div id="watch7-main" class="clearfix">
        <div id="watch7-content" class="watch-content">
              <div class="yt-uix-button-panel">
      <div id="watch7-headline" class="clearfix  yt-uix-expander yt-uix-expander-collapsed">
    <h1 id="watch-headline-title">
      


  


  <span id="eow-title" class="watch-title long-title yt-uix-expander-head" dir="ltr" title="Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland">
    Florida&#39;s Special Places: Circle B Bar Reserve in Lakeland
  </span>

    </h1>
  </div>

    <div id="watch7-user-header" ><a href="/user/AudubonFL?feature=watch" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="https://lh4.googleusercontent.com/-SNKXAYWLalg/AAAAAAAAAAI/AAAAAAAAAAA/Rw31onzZxAk/s48-c-k/photo.jpg" alt="Audubon Florida" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a><a href="/user/AudubonFL?feature=watch" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=watch" dir="ltr">Audubon Florida</a><span class="yt-user-separator">&middot;</span><a class="yt-uix-sessionlink yt-user-videos"href="/user/AudubonFL/videos"data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=watch">34 videos</a><br><span id="watch7-subscription-container"><span class=" yt-uix-button-subscription-container with-preferences" ><button aria-role="button" onclick=";return false;" type="button" class="yt-uix-subscription-button yt-uix-button yt-uix-button-subscribe-branded" aria-busy="false" aria-live="polite" data-channel-external-id="UCZwNj6gw95JMmeczpcNRiQg" data-style-type="branded" data-href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26continue_action%3DQUFFLUhqbUFJZmtzQjc3dWRwLTctRy0zTmFxZ0JreFdMUXxBQ3Jtc0ttRlFvUklIVEpKMXNkb0I1Q0RWeHJJbWtoTWlOdk9jVHJlTU9JcENva21vd2otT1lsanRUZnFOWVE1UzFBZ0VTVWR1QUo5Mm9xUjYxVEtKQTBrUG9ITDh4SFByd0ticmcyWXRGZzJyT3h4V2ZUZUJmVExELXNaekp0dF9ieVNmcGhyUUtVZ0t2aElpRk01ekhsMGtZYTFTeDlfT3hpVVJBZktoSFhPNmtsV3ByNm9zZmxVZU02RzBkVmJmemlJSEhlNFNBV3c%253D%26feature%3Dsubscribe%26hl%3Den_US%26next%3D%252Fchannel%252FUCZwNj6gw95JMmeczpcNRiQg%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg&amp;feature=watch" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-subscribe" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span> </span></button><button type="button" class="yt-uix-subscription-preferences-button yt-uix-button yt-uix-button-default yt-uix-button-empty" onclick=";return false;" data-channel-external-id="UCZwNj6gw95JMmeczpcNRiQg" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-subscription-preferences" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button><span class="yt-subscription-button-subscriber-count-branded-horizontal" >92</span>  <span class="yt-subscription-button-disabled-mask" title=""></span>
  
  <div class="yt-uix-overlay " data-overlay-style="primary"data-overlay-shape="tiny">
    
        <div class="yt-dialog hid" >
    <div class="yt-dialog-base">
      <span class="yt-dialog-align"></span>
      <div class="yt-dialog-fg">
        <div class="yt-dialog-fg-content">
            <div class="yt-dialog-header">
              <h2 class="yt-dialog-title">
                      Subscription preferences


              </h2>
            </div>
          <div class="yt-dialog-loading">
              <div class="yt-dialog-waiting-content">
    <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Loading...</div>
  </div>

          </div>
          <div class="yt-dialog-content">
              <div class="subscription-preferences-overlay-content-container">
    <div class="subscription-preferences-overlay-loading ">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
    <div class="subscription-preferences-overlay-content">
    </div>
  </div>

          </div>
          <div class="yt-dialog-working">
              <div id="yt-dialog-working-overlay">
  </div>
  <div id="yt-dialog-working-bubble">
    <div class="yt-dialog-waiting-content">
      <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Working...</div>
    </div>
  </div>

          </div>
        </div>
      </div>
    </div>
  </div>


  </div>

</span></span><div id="watch7-views-info">      <span class="watch-view-count " >
    1,184
  </span>

    <div class="video-extras-sparkbars">
    <div class="video-extras-sparkbar-likes" style="width: 100.0%"></div>
    <div class="video-extras-sparkbar-dislikes" style="width: 0.0%"></div>
  </div>
  <span class="video-extras-likes-dislikes">
      <img class="icon-watch-stats-like" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Like">
  <span class="likes-count">18</span>
 &nbsp;&nbsp;&nbsp;   <img class="icon-watch-stats-dislike" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Dislike">
  <span class="dislikes-count">0</span>

  </span>

</div></div>
      <div id="watch7-action-buttons" class="clearfix">
    <div id="watch7-sentiment-actions">
      <span id="watch-like-dislike-buttons" class="yt-uix-button-group " data-vote-state="2" data-button-toggle-group="optional"><span class="yt-uix-clickcard"><button onclick=";return false;" type="button" id="watch-like" class="yt-uix-clickcard-target yt-uix-button yt-uix-button-text yt-uix-tooltip" title="" data-force-position="true" data-like-tooltip="I like this" data-button-toggle="true" data-position="bottomright" data-unlike-tooltip="Unlike" data-orientation="vertical" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-like" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><span class="yt-uix-button-content">Like </span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your Google Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to like <span class="yt-user-name " dir="ltr">Audubon Florida</span>'s video.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button onclick=";return false;" type="button" id="watch-dislike" class="yt-uix-clickcard-target yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" title="I dislike this" data-button-toggle="true" data-force-position="true" data-orientation="vertical" data-position="bottomright" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-dislike" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="I dislike this" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your Google Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to dislike <span class="yt-user-name " dir="ltr">Audubon Florida</span>'s video.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span></span>
    </div>
    <div id="watch7-secondary-actions"  class="yt-uix-button-group" data-button-toggle-group="required">
        <span >
    <button type="button" class="action-panel-trigger  yt-uix-button-toggled yt-uix-button yt-uix-button-text yt-uix-tooltip" onclick=";return false;" title="" data-button-toggle="true" data-trigger-for="action-panel-details" role="button"><span class="yt-uix-button-content">About </span></button>
  </span>

          <span >
    <button type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip" onclick=";return false;" title="" data-button-toggle="true" data-trigger-for="action-panel-share" role="button"><span class="yt-uix-button-content">Share </span></button>
  </span>

          <span class="yt-uix-clickcard">
    <button type="button" class="action-panel-trigger   yt-uix-clickcard-target yt-uix-button yt-uix-button-text yt-uix-tooltip" onclick=";return false;" title="" data-button-toggle="true" data-trigger-for="action-panel-none" data-orientation="vertical" data-position="bottomleft" data-upsell="playlist" role="button"><span class="yt-uix-button-content">Add to </span></button>
        <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your Google Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to add <span class="yt-user-name " dir="ltr">Audubon Florida</span>'s video to your playlist.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>

  </span>

            
  <span >
    <button disabled="True" onclick=";return false;" type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" title="Stats have been disabled for this video" data-button-toggle="true" data-trigger-for="action-panel-stats" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-action-panel-stats" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Stats have been disabled for this video" title=""><span class="yt-uix-button-valign"></span></span></button>
  </span>


        <span >
    <button type="button" class="action-panel-trigger   yt-uix-button yt-uix-button-text yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="Report" data-button-toggle="true" data-trigger-for="action-panel-report" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-action-panel-report" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Report" title=""><span class="yt-uix-button-valign"></span></span></button>
  </span>

    </div>
  </div>

      <div id="watch7-action-panels" class="yt-uix-button-panel">
      <div id="action-panel-details" class="action-panel-content ">
    <div id="watch-description" class="yt-uix-expander yt-uix-expander-collapsed yt-uix-button-panel">
      <div id="watch-description-content" >
        <div id="watch-description-clip">
          <p id="watch-uploader-info">
            <strong>Uploaded on <span id="eow-date" class="watch-video-date" >Dec  9, 2011</span>
</strong>
          </p>
          <div id="watch-description-text">
            <p id="eow-description" >Lake Region Audubon Society has nominated Circle B Bar Reserve in Lakeland as one of Florida&#39;s Special Places. You can nominate your favorite natural Florida spots: <a href="http://www.FloridasSpecialPlaces.org" target="_blank" title="http://www.FloridasSpecialPlaces.org" rel="nofollow" dir="ltr" class="yt-uix-redirect-link">http://www.FloridasSpecialPlaces.org</a></p>
          </div>
            <div id="watch-description-extras">
    <ul class="watch-extras-section">
      <li>
        <h4 class="title">
Category
        </h4>
        <div class="content">
              <p id="eow-category"><a href="/activism">Nonprofits &amp; Activism</a></p>

        </div>
      </li>


        <li>
          <h4 class="title">License</h4>
          <div class="content">
              <p id="eow-reuse">
Standard YouTube License
  </p>

          </li>
        </li>
    </ul>
  </div>

        </div>
        <ul id="watch-description-extra-info">
          
        </ul>
      </div>

      <div id="watch-description-toggle" class="yt-uix-expander-head yt-uix-button-panel">
        <div id="watch-description-expand" class="expand">
          <button type="button" class="metadata-inline yt-uix-button yt-uix-button-text" onclick=";return false;"  role="button"><span class="yt-uix-button-content">Show more </span></button>
        </div>
        <div id="watch-description-collapse" class="collapse">
          <button type="button" class="metadata-inline yt-uix-button yt-uix-button-text" onclick=";return false;"  role="button"><span class="yt-uix-button-content">Show less </span></button>
        </div>
      </div>
    </div>
  </div>

      <div id="action-panel-share" class="action-panel-content hid">
      <div id="watch-actions-share-loading">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>
  <div id="watch-actions-share-panel"></div>

  </div>

      <div id="action-panel-addto" class="action-panel-content hid" data-auth-required="true">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>

      <div id="action-panel-stats" class="action-panel-content hid">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>

      <div id="action-panel-report" class="action-panel-content hid" data-auth-required="true">
    <div class="action-panel-loading">
        <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

    </div>
  </div>

      <div id="action-panel-login" class="action-panel-content hid">
    <div class="action-panel-login">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-default" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>

  <div id="action-panel-ratings-disabled" class="action-panel-content hid">
      <div id="watch-actions-ratings-disabled" class="watch-actions-panel">
    <em>Ratings have been disabled for this video.</em>
  </div>

  </div>

  <div id="action-panel-rental-required" class="action-panel-content hid">
      <div id="watch-actions-rental-required" class="watch-actions-panel">
    <strong>Rating is available when the video has been rented.</strong>
  </div>

  </div>

  <div id="action-panel-error" class="action-panel-content hid">
    <div class="action-panel-error">
      This feature is not available right now. Please try again later.
    </div>
  </div>

    <div id="watch7-action-panel-footer">
        <hr class="yt-horizontal-rule ">

    </div>
  </div>

  </div>
    <div id="watch-discussion">
      <div style="display: none"><iframe src="https://apis.google.com/_/im/_/s/c?first_party_property=YOUTUBE&amp;query=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DOyJ3CafAM1Q&amp;href=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DOyJ3CafAM1Q&amp;yt_owner_id=ZwNj6gw95JMmeczpcNRiQg&amp;view_type=FILTERED_POSTMOD"></iframe></div>

        
        <div id="comments-view" data-type="highlights" class="">

                <div >
      <h4>
      <a href="/all_comments?v=OyJ3CafAM1Q">
            <strong>All Comments</strong> (5)

      </a>
  </h4>


          <div class="comments-post-alert comments-post">
        <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dcomments%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube">Sign in</a> now to post a comment!

      </div>


      <ul id="all-comments">
      


  <li class="comment"
    data-author-id="Mug0dDuKd21pE_Dpt3uiJQ"
    data-id="eOqnzHZe6cf4kG6QePvq-9-n91moJ9FoIV1-SFDjhVE"
    >
    <button type="button" class="flip close yt-uix-button yt-uix-button-link yt-uix-button-empty" onclick=";return false;" data-button-has-sibling-menu="true" role="button" aria-pressed="false" aria-expanded="false" aria-haspopup="true" aria-activedescendant=""><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-comment-close" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><div class=" yt-uix-button-menu yt-uix-button-menu-link" style="display: none;"><ul><li class="comment-action-remove comment-action" data-action="remove"><span class="yt-uix-button-menu-item">Remove</span></li><li class="comment-action" data-action="flag-profile-pic"><span class="yt-uix-button-menu-item">Report profile image</span></li><li class="comment-action" data-action="flag"><span class="yt-uix-button-menu-item">Flag for spam</span></li><li class="comment-action-block comment-action" data-action="block"><span class="yt-uix-button-menu-item">Block User</span></li><li class="comment-action-unblock comment-action" data-action="unblock"><span class="yt-uix-button-menu-item">Unblock User</span></li></ul></div></button>
      <a href="/user/KazokuMugiwara" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="KazokuMugiwara" data-thumb="//i2.ytimg.com/i/Mug0dDuKd21pE_Dpt3uiJQ/1.jpg" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a>

    

  <div class="content">
      <p class="metadata">
        <span class="author ">
          <a href="/user/KazokuMugiwara" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg" dir="ltr">KazokuMugiwara</a>
        </span>
          <span class="time" dir="ltr">
            <a dir="ltr" href="http://www.youtube.com/comment?lc=eOqnzHZe6cf4kG6QePvq-9-n91moJ9FoIV1-SFDjhVE">
              2 months ago
            </a>
          </span>
      </p>


      <div class="comment-text" dir="ltr">
          <p>Woodstock!!</p>
<p>I&#39;m sooo excited.﻿</p>

      </div>
      
  <div class="comment-actions">
    <button type="button" class="start comment-action yt-uix-button yt-uix-button-link" onclick=";return false;" data-action="reply" role="button"><span class="yt-uix-button-content">Reply </span></button>
    <span class="separator">&middot;</span>


    <span class="yt-uix-clickcard"><button type="button" class="start comment-action-vote-up comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-up" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">KazokuMugiwara</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button type="button" class="end comment-action-vote-down comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-down" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">KazokuMugiwara</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span>
  </div>

  </div>


  </li>

      


  <li class="comment"
    data-author-id="Odfs6PK7AZq-9432_wI2mw"
    data-id="eOqnzHZe6ccUXn1nwgw1sgVG-4e7pWMWaYAo57Qva6U"
    >
    <button type="button" class="flip close yt-uix-button yt-uix-button-link yt-uix-button-empty" onclick=";return false;" data-button-has-sibling-menu="true" role="button" aria-pressed="false" aria-expanded="false" aria-haspopup="true" aria-activedescendant=""><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-comment-close" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><div class=" yt-uix-button-menu yt-uix-button-menu-link" style="display: none;"><ul><li class="comment-action-remove comment-action" data-action="remove"><span class="yt-uix-button-menu-item">Remove</span></li><li class="comment-action" data-action="flag-profile-pic"><span class="yt-uix-button-menu-item">Report profile image</span></li><li class="comment-action" data-action="flag"><span class="yt-uix-button-menu-item">Flag for spam</span></li><li class="comment-action-block comment-action" data-action="block"><span class="yt-uix-button-menu-item">Block User</span></li><li class="comment-action-unblock comment-action" data-action="unblock"><span class="yt-uix-button-menu-item">Unblock User</span></li></ul></div></button>
      <a href="/user/Sticks364" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Thomas Bussell" data-thumb="https://gp5.googleusercontent.com/-zRs7cC4AOt4/AAAAAAAAAAI/AAAAAAAAAAA/iVscWtMibh0/s48-c-k/photo.jpg" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a>

    

  <div class="content">
      <p class="metadata">
        <span class="author ">
          <a href="/user/Sticks364" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg" dir="ltr">Thomas Bussell</a>
        </span>
          <span class="time" dir="ltr">
            <a dir="ltr" href="http://www.youtube.com/comment?lc=eOqnzHZe6ccUXn1nwgw1sgVG-4e7pWMWaYAo57Qva6U">
              4 months ago
            </a>
          </span>
      </p>


      <div class="comment-text" dir="ltr">
          <p>Nice!!</p>
<p>﻿</p>

      </div>
      
  <div class="comment-actions">
    <button type="button" class="start comment-action yt-uix-button yt-uix-button-link" onclick=";return false;" data-action="reply" role="button"><span class="yt-uix-button-content">Reply </span></button>
    <span class="separator">&middot;</span>


    <span class="yt-uix-clickcard"><button type="button" class="start comment-action-vote-up comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-up" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">Thomas Bussell</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button type="button" class="end comment-action-vote-down comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-down" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">Thomas Bussell</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span>
  </div>

  </div>


  </li>

      


  <li class="comment"
    data-author-id="V9tZc_fZIb45GCaVsw_ndw"
    data-id="eOqnzHZe6cdfsY5sDi24mJyYBPSUozQhEe2hrFs8riU"
    >
    <button type="button" class="flip close yt-uix-button yt-uix-button-link yt-uix-button-empty" onclick=";return false;" data-button-has-sibling-menu="true" role="button" aria-pressed="false" aria-expanded="false" aria-haspopup="true" aria-activedescendant=""><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-comment-close" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><div class=" yt-uix-button-menu yt-uix-button-menu-link" style="display: none;"><ul><li class="comment-action-remove comment-action" data-action="remove"><span class="yt-uix-button-menu-item">Remove</span></li><li class="comment-action" data-action="flag-profile-pic"><span class="yt-uix-button-menu-item">Report profile image</span></li><li class="comment-action" data-action="flag"><span class="yt-uix-button-menu-item">Flag for spam</span></li><li class="comment-action-block comment-action" data-action="block"><span class="yt-uix-button-menu-item">Block User</span></li><li class="comment-action-unblock comment-action" data-action="unblock"><span class="yt-uix-button-menu-item">Unblock User</span></li></ul></div></button>
      <a href="/user/l67swap1" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="l67swap1" data-thumb="//i3.ytimg.com/i/V9tZc_fZIb45GCaVsw_ndw/1.jpg" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a>

    

  <div class="content">
      <p class="metadata">
        <span class="author ">
          <a href="/user/l67swap1" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg" dir="ltr">l67swap1</a>
        </span>
          <span class="time" dir="ltr">
            <a dir="ltr" href="http://www.youtube.com/comment?lc=eOqnzHZe6cdfsY5sDi24mJyYBPSUozQhEe2hrFs8riU">
              10 months ago
            </a>
          </span>
      </p>


      <div class="comment-text" dir="ltr">
          <p>Love this place﻿ ... amazing video</p>

      </div>
      
  <div class="comment-actions">
    <button type="button" class="start comment-action yt-uix-button yt-uix-button-link" onclick=";return false;" data-action="reply" role="button"><span class="yt-uix-button-content">Reply </span></button>
    <span class="separator">&middot;</span>


    <span class="yt-uix-clickcard"><button type="button" class="start comment-action-vote-up comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-up" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">l67swap1</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button type="button" class="end comment-action-vote-down comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-down" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">l67swap1</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span>
  </div>

  </div>


  </li>

      


  <li class="comment"
    data-author-id="FrMWTn1RuIggpoxD7zi02w"
    data-id="eOqnzHZe6ceYiDnkIO1TJEKYWaVu8WI3xMjDhXQZpXI"
    >
    <button type="button" class="flip close yt-uix-button yt-uix-button-link yt-uix-button-empty" onclick=";return false;" data-button-has-sibling-menu="true" role="button" aria-pressed="false" aria-expanded="false" aria-haspopup="true" aria-activedescendant=""><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-comment-close" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><div class=" yt-uix-button-menu yt-uix-button-menu-link" style="display: none;"><ul><li class="comment-action-remove comment-action" data-action="remove"><span class="yt-uix-button-menu-item">Remove</span></li><li class="comment-action" data-action="flag-profile-pic"><span class="yt-uix-button-menu-item">Report profile image</span></li><li class="comment-action" data-action="flag"><span class="yt-uix-button-menu-item">Flag for spam</span></li><li class="comment-action-block comment-action" data-action="block"><span class="yt-uix-button-menu-item">Block User</span></li><li class="comment-action-unblock comment-action" data-action="unblock"><span class="yt-uix-button-menu-item">Unblock User</span></li></ul></div></button>
      <a href="/user/mflynn2009" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="mflynn2009" data-thumb="//i3.ytimg.com/i/FrMWTn1RuIggpoxD7zi02w/1.jpg" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a>

    

  <div class="content">
      <p class="metadata">
        <span class="author ">
          <a href="/user/mflynn2009" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg" dir="ltr">mflynn2009</a>
        </span>
          <span class="time" dir="ltr">
            <a dir="ltr" href="http://www.youtube.com/comment?lc=eOqnzHZe6ceYiDnkIO1TJEKYWaVu8WI3xMjDhXQZpXI">
              1 year ago
            </a>
          </span>
      </p>


      <div class="comment-text" dir="ltr">
          <p>You﻿ captured it perfect!!</p>

      </div>
      
  <div class="comment-actions">
    <button type="button" class="start comment-action yt-uix-button yt-uix-button-link" onclick=";return false;" data-action="reply" role="button"><span class="yt-uix-button-content">Reply </span></button>
    <span class="separator">&middot;</span>


    <span class="yt-uix-clickcard"><button type="button" class="start comment-action-vote-up comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-up" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">mflynn2009</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button type="button" class="end comment-action-vote-down comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-down" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">mflynn2009</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span>
  </div>

  </div>


  </li>

      


  <li class="comment"
    data-author-id="nVlDQPrztpONEs4hjq7_Kw"
    data-id="eOqnzHZe6cfmTwznut1e2R4dne2WEZwSBOvXNDhJWi4"
    >
    <button type="button" class="flip close yt-uix-button yt-uix-button-link yt-uix-button-empty" onclick=";return false;" data-button-has-sibling-menu="true" role="button" aria-pressed="false" aria-expanded="false" aria-haspopup="true" aria-activedescendant=""><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-comment-close" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><div class=" yt-uix-button-menu yt-uix-button-menu-link" style="display: none;"><ul><li class="comment-action-remove comment-action" data-action="remove"><span class="yt-uix-button-menu-item">Remove</span></li><li class="comment-action" data-action="flag-profile-pic"><span class="yt-uix-button-menu-item">Report profile image</span></li><li class="comment-action" data-action="flag"><span class="yt-uix-button-menu-item">Flag for spam</span></li><li class="comment-action-block comment-action" data-action="block"><span class="yt-uix-button-menu-item">Block User</span></li><li class="comment-action-unblock comment-action" data-action="unblock"><span class="yt-uix-button-menu-item">Unblock User</span></li></ul></div></button>
      <a href="/user/MattUNI2005" class="yt-user-photo " >    <span class="video-thumb  yt-thumb yt-thumb-48"
      >
      <span class="yt-thumb-square">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="MattUNI2005" data-thumb="//i3.ytimg.com/i/nVlDQPrztpONEs4hjq7_Kw/1.jpg" width="48" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
</a>

    

  <div class="content">
      <p class="metadata">
        <span class="author ">
          <a href="/user/MattUNI2005" class="yt-uix-sessionlink yt-user-name " data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg" dir="ltr">MattUNI2005</a>
        </span>
          <span class="time" dir="ltr">
            <a dir="ltr" href="http://www.youtube.com/comment?lc=eOqnzHZe6cfmTwznut1e2R4dne2WEZwSBOvXNDhJWi4">
              1 year ago
            </a>
          </span>
      </p>


      <div class="comment-text" dir="ltr">
          <p>One of my all-time favorite spots in the world - Circle B Bar is simply﻿ amazing - great video!</p>

      </div>
      
  <div class="comment-actions">
    <button type="button" class="start comment-action yt-uix-button yt-uix-button-link" onclick=";return false;" data-action="reply" role="button"><span class="yt-uix-button-content">Reply </span></button>
    <span class="separator">&middot;</span>


    <span class="yt-uix-clickcard"><button type="button" class="start comment-action-vote-up comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-up" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">MattUNI2005</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span><span class="yt-uix-clickcard"><button type="button" class="end comment-action-vote-down comment-action yt-uix-clickcard-target yt-uix-button yt-uix-button-link yt-uix-tooltip yt-uix-button-empty" onclick=";return false;" title="" data-action="" data-tooltip-show-delay="300" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-watch-comment-vote-down" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span></button>  <div class="watch7-hovercard yt-uix-clickcard-content">
    <h3 class="watch7-hovercard-header">Sign in to YouTube</h3>
    <div class="watch7-hovercard-message">
      Sign in with your YouTube Account (YouTube, Google+, Gmail, Orkut, Picasa, or Chrome) to rate <span class="yt-user-name " dir="ltr">MattUNI2005</span>'s comment.

    </div>
    <ul class="watch7-hovercard-icon-strip clearfix">
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-youtube-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gplus-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-gmail-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-picasa-icon"></div>
      </li>
      <li class="watch7-hovercard-icon">
        <div class="watch7-hovercard-chrome-icon"></div>
      </li>
    </ul>
    <div class="watch7-hovercard-account-line">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3D__FEATURE__%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&amp;uilel=3&amp;hl=en_US&amp;service=youtube" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary" data-sessionlink="ei=a6W3UcTyCqXMiQLYr4HQBg"><span class="yt-uix-button-content">Sign in</span></a>
    </div>
  </div>
</span>
  </div>

  </div>


  </li>

  </ul>

  </div>




    <ul>
      <li class="hid" id="parent-comment-loading">Loading comment...</li>
    </ul>
  </div>
  <div id="comments-loading" class="hid">Loading...</div>
    


  </div>



        </div>
        <div id="watch7-sidebar" class="watch-sidebar ">
            


        <div id="watch-channel-brand-div" class="" >
    <div id="watch-channel-brand-div-text">
Advertisement
    </div>
    <div id="google_companion_ad_div">
    </div>
  </div>


          <div class="watch-sidebar-section">

    <div class="watch-sidebar-body">
      <ul id="watch-related" class="video-list">
          <li class="video-list-item related-list-item">
            <a href="/watch?v=sA8uJ54IpDI" class="related-video yt-uix-contextlink  related-video-featured hid yt-uix-sessionlink" data-sessionlink="ved=CBUQzRooAA&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=fvwrel"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i4.ytimg.com/vi/sA8uJ54IpDI/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">2:30</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="sA8uJ54IpDI" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Circle B Bar Reserve">Circle B Bar Reserve</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">kwilli75</span></span><span class="stat alt badge"><span class="yt-badge ">Featured</span></span>    <span class="stat view-count">
        2,515
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=CDoNiT_2RVE" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBYQzRooAQ&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i4.ytimg.com/vi/CDoNiT_2RVE/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">6:47</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="CDoNiT_2RVE" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Circle B Bar Reserve - Lakeland Area">Circle B Bar Reserve - Lakeland Area</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">mflynn2009</span></span>    <span class="stat view-count">
        1,374 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=zZXUi8noht8" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBcQzRooAg&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/zZXUi8noht8/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">6:28</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="zZXUi8noht8" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Wildlife at Circle B Bar Ranch, Lakeland, FL">Wildlife at Circle B Bar Ranch, Lakeland, FL</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">yourboypaulie</span></span>    <span class="stat view-count">
        5,268 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=3507Wkj3_yE" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBgQzRooAw&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=relmfu"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i4.ytimg.com/vi/3507Wkj3_yE/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">2:46</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="3507Wkj3_yE" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Florida&#39;s Special Places: Corkscrew Swamp Sanctuary - The Heart of the Western Everglades">Florida&#39;s Special Places: Corkscrew Swamp Sanctuary - The Heart of the Western Everglades</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Audubon Florida</span></span>    <span class="stat view-count">
        7,872 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=dJOLObQyhdY" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBkQzRooBA&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i1.ytimg.com/vi/dJOLObQyhdY/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">7:28</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="dJOLObQyhdY" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="A hike at the Circle B Bar Reserve in Lakeland, Florida, January 9, 2011">A hike at the Circle B Bar Reserve in Lakeland, Florida, January 9, 2011</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Kesh Butler</span></span>    <span class="stat view-count">
        437 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=ziIMB8fcX8Q" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBoQzRooBQ&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/ziIMB8fcX8Q/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">5:38</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="ziIMB8fcX8Q" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Circle B Bar Reserve 1-14-2011">Circle B Bar Reserve 1-14-2011</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Tanyia48</span></span>    <span class="stat view-count">
        272 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=ZY06eqdCfw4" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBsQzRooBg&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=relmfu"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/ZY06eqdCfw4/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">0:44</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="ZY06eqdCfw4" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="A Florida Panther Cruises the Boardwalk at Audubon&#39;s Corkscrew Swamp Sanctuary">A Florida Panther Cruises the Boardwalk at Audubon&#39;s Corkscrew Swamp Sanctuary</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Audubon Florida</span></span>    <span class="stat view-count">
        1,748 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=hyt6wnFpU0o" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CBwQzRooBw&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i1.ytimg.com/vi/hyt6wnFpU0o/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">2:50</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="hyt6wnFpU0o" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Circle B Bar Reserve Introduction">Circle B Bar Reserve Introduction</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Polk Government</span></span>    <span class="stat view-count">
        471 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=BRe-eDY46aQ" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CB0QzRooCA&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/BRe-eDY46aQ/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">2:28</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="BRe-eDY46aQ" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Identification of Bird of Prey, The Osprey Devouring &amp; Eating Live Fish at Circle B Bar Reserve">Identification of Bird of Prey, The Osprey Devouring &amp; Eating Live Fish at Circle B Bar Reserve</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">SandieM0731</span></span>    <span class="stat view-count">
        5,193 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=8kvQWXGG9Sw" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CB4QzRooCQ&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i1.ytimg.com/vi/8kvQWXGG9Sw/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">5:22</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="8kvQWXGG9Sw" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Lakeland, FL OFFICIAL World&#39;s Largest Simultaneous Flashmob">Lakeland, FL OFFICIAL World&#39;s Largest Simultaneous Flashmob</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Robert Beaudreault</span></span>    <span class="stat view-count">
        1,357 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=VMLQoSjbz14" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CB8QzRooCg&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/VMLQoSjbz14/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">8:46</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="VMLQoSjbz14" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Kickin&#39; it with Tpindell 6 #FiestaMovement">Kickin&#39; it with Tpindell 6 #FiestaMovement</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">TpindellTV</span></span>    <span class="stat view-count">
        10,783 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=rhAkLyJESgE" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCAQzRooCw&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/rhAkLyJESgE/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">6:17</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="rhAkLyJESgE" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Peace River Kayak Trip - 105 miles/3 days">Peace River Kayak Trip - 105 miles/3 days</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">tpwellman</span></span>    <span class="stat view-count">
        1,842 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=G0tQnRWCrEI" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCEQzRooDA&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i4.ytimg.com/vi/G0tQnRWCrEI/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">15:18</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="G0tQnRWCrEI" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="7 Functions of the Pyramid">7 Functions of the Pyramid</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">TranscendentalProdco</span></span>    <span class="stat view-count">
        173,193 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=ZTnUr8Ztu48" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCIQzRooDQ&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/ZTnUr8Ztu48/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:12</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="ZTnUr8Ztu48" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="How to Identify Black-bellied Whistling Ducks of Central Florida at Circle B Bar Reserve">How to Identify Black-bellied Whistling Ducks of Central Florida at Circle B Bar Reserve</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">SandieM0731</span></span>    <span class="stat view-count">
        2,955 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=X5Y6jRXkoD4" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCMQzRooDg&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i1.ytimg.com/vi/X5Y6jRXkoD4/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">3:28</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="X5Y6jRXkoD4" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="The Cranes of Japan">The Cranes of Japan</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">artwolfe8</span></span>    <span class="stat view-count">
        1,954 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=0Sh4tu5Xfhw" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCQQzRooDw&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i1.ytimg.com/vi/0Sh4tu5Xfhw/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">1:23</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="0Sh4tu5Xfhw" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Sand Cat Kittens-Cincinnati Zoo">Sand Cat Kittens-Cincinnati Zoo</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">CincinnatiZooTube</span></span>    <span class="stat view-count">
        626,033 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=gP55cCmTwEk" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCUQzRooEA&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i4.ytimg.com/vi/gP55cCmTwEk/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">5:58</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="gP55cCmTwEk" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Driving in Tornado Lakeland FLorida March 2011 Sun N Fun">Driving in Tornado Lakeland FLorida March 2011 Sun N Fun</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">kitfoxflyer</span></span>    <span class="stat view-count">
        19,432 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=YpcNW01que8" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCYQzRooEQ&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i2.ytimg.com/vi/YpcNW01que8/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">44:29</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="YpcNW01que8" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="The Pyramid Code: The Band of Peace">The Pyramid Code: The Band of Peace</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">VidTruth</span></span>    <span class="stat view-count">
        180,181 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=O9ytloon7TI" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCcQzRooEg&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i4.ytimg.com/vi/O9ytloon7TI/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">5:56</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="O9ytloon7TI" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="MAX - Rescued &quot;Pet&quot; Bobcat...">MAX - Rescued &quot;Pet&quot; Bobcat...</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">Big Cat Rescue</span></span>    <span class="stat view-count">
        392,187 views
    </span>
</a>
          </li>
          <li class="video-list-item related-list-item">
            <a href="/watch?v=FrAShtolieg" class="related-video yt-uix-contextlink  yt-uix-sessionlink" data-sessionlink="ved=CCgQzRooEw&ei=a6W3UcTyCqXMiQLYr4HQBg&feature=related"><span class="ux-thumb-wrap contains-addto ">    <span class="video-thumb  yt-thumb yt-thumb-120"
      >
      <span class="yt-thumb-default">
        <span class="yt-thumb-clip">
          <span class="yt-thumb-clip-inner">
            <img src="http://s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" data-thumb="//i3.ytimg.com/vi/FrAShtolieg/default.jpg" width="120" >
            <span class="vertical-align"></span>
          </span>
        </span>
      </span>
    </span>
<span class="video-time">7:21</span>

  <button onclick=";return false;" type="button" class="addto-button video-actions spf-nolink addto-watch-later-button-sign-in yt-uix-button yt-uix-button-default yt-uix-button-short yt-uix-tooltip" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="FrAShtolieg" role="button"><span class="yt-uix-button-content">  <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="Watch Later">
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>
</span><span dir="ltr" class="title" title="Charles Moore: Sailing the Great Pacific Garbage Patch">Charles Moore: Sailing the Great Pacific Garbage Patch</span><span class="stat attribution">by <span class="yt-user-name " dir="ltr">theonlytruecate</span></span>    <span class="stat view-count">
        610,843 views
    </span>
</a>
          </li>
            <div id="watch-more-related" class="hid">
    <li id="watch-more-related-loading">
Loading more suggestions...
    </li>
  </div>
  <button type="button" id="watch-more-related-button" onclick=";return false;" class=" yt-uix-button yt-uix-button-default" data-button-action="yt.www.watch.related.loadMore" role="button"><span class="yt-uix-button-content">Load more suggestions </span></button>

      </ul>
    </div>   </div> 


        </div>
      </div>
    </div>

      <div style="visibility: hidden; height: 0px; padding: 0px; overflow: hidden;">
  </div>

  </div>
</div></div></div></div><div id="footer-container"><div id="footer"><div id="footer-main"><div id="footer-logo"><a href="/" title="YouTube home"><img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="YouTube home"></a></div>  <ul class="pickers yt-uix-button-group" data-button-toggle-group="optional">
      <li>
          
  <button type="button" id="yt-picker-language-button" onclick=";return false;" class=" yt-uix-button yt-uix-button-default" data-button-toggle="true" data-picker-position="footer" data-button-menu-id="arrow-display" data-picker-key="language" data-button-action="yt.www.picker.load" role="button"><span class="yt-uix-button-icon-wrapper"><img class="yt-uix-button-icon yt-uix-button-icon-footer-language" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""><span class="yt-uix-button-valign"></span></span><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Language:
  </span>
  English
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>


      </li>
      <li>
          
  <button type="button" id="yt-picker-country-button" onclick=";return false;" class=" yt-uix-button yt-uix-button-default" data-button-toggle="true" data-picker-position="footer" data-button-menu-id="arrow-display" data-picker-key="country" data-button-action="yt.www.picker.load" role="button"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Country:
  </span>
  Worldwide
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>


      </li>
      <li>
          
  <button type="button" id="yt-picker-safetymode-button" onclick=";return false;" class=" yt-uix-button yt-uix-button-default" data-button-toggle="true" data-picker-position="footer" data-button-menu-id="arrow-display" data-picker-key="safetymode" data-button-action="yt.www.picker.load" role="button"><span class="yt-uix-button-content">  <span class="yt-picker-button-label">
Safety:
  </span>
Off
 </span><img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" alt="" title=""></button>


      </li>
  </ul>
  <button onclick="yt.www.feedback.startHelp(this, null, &quot;watch&quot;);return false;" type="button" id="google-help" class="yt-uix-button-reverse yt-uix-button yt-uix-button-default"  role="button"><span class="yt-uix-button-content">  <img class="questionmark" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
  <span>Help</span>
    <img class="yt-uix-button-arrow" src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
 </span></button>
      <div id="yt-picker-language-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

      <div id="yt-picker-country-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

      <div id="yt-picker-safetymode-footer"
      class="yt-picker"
      style="display: none"
>
      <p class="yt-spinner">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="yt-spinner-img" alt="Loading icon">

    <span class="yt-spinner-message">
Loading...
    </span>
  </p>

  </div>

</div><div id="footer-links"><ul id="footer-links-primary">  <li><a href="//www.youtube.com/yt/about/">About</a></li>
  <li><a href="//www.youtube.com/yt/press/">Press &amp; Blogs</a></li>
  <li><a href="//www.youtube.com/yt/copyright/">Copyright</a></li>
  <li><a href="//www.youtube.com/yt/creators/">Creators &amp; Partners</a></li>
  <li><a href="//www.youtube.com/yt/advertise/">Advertising</a></li>
  <li><a href="//www.youtube.com/yt/dev/">Developers</a></li>
</ul><ul id="footer-links-secondary">  <li><a href="/t/terms">Terms</a></li>
  <li><a href="http://www.google.com/intl/en/policies/privacy/">Privacy</a></li>
  <li><a href="//www.youtube.com/yt/policyandsafety/">
Policy &amp; Safety
  </a></li>
  <li><a href="//www.google.com/tools/feedback/intl/en/error.html" onclick="return yt.www.feedback.start();" id="reportbug">Send feedback</a></li>
  <li><a href="/testtube">Try something new!</a></li>
  <li></li>
</ul></div></div></div>

      <div class="yt-dialog hid" id="feed-privacy-lb">
    <div class="yt-dialog-base">
      <span class="yt-dialog-align"></span>
      <div class="yt-dialog-fg">
        <div class="yt-dialog-fg-content">
          <div class="yt-dialog-loading">
              <div class="yt-dialog-waiting-content">
    <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Loading...</div>
  </div>

          </div>
          <div class="yt-dialog-content">
              <div id="feed-privacy-dialog">
  </div>

          </div>
          <div class="yt-dialog-working">
              <div id="yt-dialog-working-overlay">
  </div>
  <div id="yt-dialog-working-bubble">
    <div class="yt-dialog-waiting-content">
      <div class="yt-spinner-img"></div><div class="yt-dialog-waiting-text">Working...</div>
    </div>
  </div>

          </div>
        </div>
      </div>
    </div>
  </div>



    <div id="shared-addto-watch-later-login" class="hid">
      <a href="https://accounts.google.com/ServiceLogin?passive=true&continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dplaylist%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&uilel=3&hl=en_US&service=youtube" class="sign-in-link">Sign in</a> to add this to Watch Later

    </div>

  <div id="shared-addto-menu" style="display: none;" class="hid sign-in">
      <div class="addto-menu">
        <div id="addto-list-panel" class="menu-panel active-panel">
        <span class="yt-uix-button-menu-item yt-uix-tooltip sign-in"data-possible-tooltip=""data-tooltip-show-delay="750"><a href="https://accounts.google.com/ServiceLogin?passive=true&continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dplaylist%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1&uilel=3&hl=en_US&service=youtube" class="sign-in-link">Sign in</a> to add this to Watch Later
</span>

  </div>
  <div id="addto-list-saved-panel" class="menu-panel">
    <div class="panel-content">
      <div class="yt-alert yt-alert-naked yt-alert-success  ">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
            
  <span class="message">Added to <span class="addto-title yt-uix-tooltip yt-uix-tooltip-reverse" title="More information about this playlist" data-tooltip-show-delay="750"></span></span>

    </div>
</div></div>
        <div class="yt-alert yt-alert-naked yt-alert-warn  private-video-warning hid">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
            Private videos will be skipped if viewers don&#39;t have access, but playlist notes are publicly visible.
    </div>
</div></div>

    </div>
  </div>
  <div id="addto-list-error-panel" class="menu-panel">
    <div class="panel-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span class="error-details"></span>
      <a class="show-menu-link">Back to list</a>
    </div>
  </div>

        <div id="addto-note-input-panel" class="menu-panel">
    <div class="panel-content">
      <div class="yt-alert yt-alert-naked yt-alert-success  ">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
              <span class="message">Added to playlist:</span>
  <span class="addto-title yt-uix-tooltip" title="More information about this playlist" data-tooltip-show-delay="750"></span>

    </div>
</div></div>
        <div class="yt-alert yt-alert-naked yt-alert-warn  private-video-warning hid">  <div class="yt-alert-icon">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="icon master-sprite" alt="Alert icon">
  </div>
<div class="yt-alert-content" role="alert">    <span class="yt-alert-vertical-trick"></span>
    <div class="yt-alert-message">
            Private videos will be skipped if viewers don&#39;t have access, but playlist notes are publicly visible.
    </div>
</div></div>

    </div>
<div class="yt-uix-char-counter" data-char-limit="150"><div class="addto-note-box addto-text-box"><textarea id="addto-note" class="addto-note yt-uix-char-counter-input" maxlength="150"></textarea><label for="addto-note" class="addto-note-label">Add an optional note</label></div><span class="yt-uix-char-counter-remaining">150</span></div>    <button disabled="disabled" type="button" class="playlist-save-note yt-uix-button yt-uix-button-default" onclick=";return false;"  role="button"><span class="yt-uix-button-content">Add note </span></button>
  </div>
  <div id="addto-note-saving-panel" class="menu-panel">
    <div class="panel-content loading-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span>Saving note...</span>
    </div>
  </div>
  <div id="addto-note-saved-panel" class="menu-panel">
    <div class="panel-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span class="message">Note added to:</span>
    </div>
  </div>
  <div id="addto-note-error-panel" class="menu-panel">
    <div class="panel-content">
      <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif">
      <span class="message">Error adding note:</span>
      <ul class="error-details"></ul>
      <a class="add-note-link">Click to add a new note</a>
    </div>
  </div>
  <div class="close-note hid">
    <img src="//s.ytimg.com/yts/img/pixel-vfl3z5WfW.gif" class="close-button">
  </div>

  </div>

  </div>
<script>if (window.ytcsi) {ytcsi.tick("js_head");}</script>    <script id="js-4250492157" class="www_base_mod" src="//s.ytimg.com/yts/jsbin/www_base_mod-vfllOxUSK.js" data-loaded="true"></script>
  <script>
    yt.setConfig({
      'JS_DELAY_LOAD': 0,
      'WATCH_GUIDE_CSS': "http:\/\/s.ytimg.com\/yts\/cssbin\/www-guide-vflsMUwZf.css",
      'WATCH_CONTEXT_CONTAINER_TEMPLATE': "    \u003cdiv id=\"context-source-container\"data-context-source=\"__source__\"data-context-image=\"__image__\"style=\"display:none;\"\u003e\u003c\/div\u003e\u003cdiv class=\"__container_classes__\"\u003e\u003cdiv class=\"guide-module-toggle context-header\"\u003e\u003cspan class=\"guide-module-toggle-icon\"\u003e\u003cspan class=\"guide-module-toggle-arrow\"\u003e\u003c\/span\u003e\u003cimg src=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\"\u003e\u003c\/span\u003e\u003ca class=\"context-back-link yt-uix-sessionlink\" href=\"__back_link__\" data-sessionlink=\"ei=a6W3UcTyCqXMiQLYr4HQBg\u0026amp;feature=__feature__\"\u003e\u003cspan class=\"guide-context-image-link\"\u003e\u003cspan class=\"thumb guide-context-image\"\u003e\u003cimg id=\"context-image\" src=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\" data-context-image=\"__image__\"\u003e\u003c\/span\u003e\u003c\/span\u003e\u003cdiv class=\"guide-module-toggle-label\"\u003e\u003ch3 class=\"context-title\"\u003e\u003cspan\u003e__headline__\u003c\/span\u003e\u003c\/h3\u003e\u003cspan class=\"placeholder\" title=\"__more_from__\" dir=\"__title_dir__\"\u003e__more_from__\u003c\/span\u003e\u003c\/div\u003e\u003c\/a\u003e\u003c\/div\u003e\u003cdiv class=\"guide-module-content yt-scrollbar\"\u003e\u003chr class=\"guide-section-separator guide-context-separator-top\"\u003e\u003cul id=\"watch-context-item-list\" class=\"guide-context-item-container context-data-container yt-uix-scroller guide-context-body\" data-context-playing=\"__click_index__\" data-context-open=\"true\" data-context-subsource=\"__subsource__\" data-scroll-action=\"yt.www.watch.context.loadThumbnails\"\u003e__item_list__\u003c\/ul\u003e\u003chr class=\"guide-section-separator guide-context-separator-bottom\"\u003e\u003c\/div\u003e\u003c\/div\u003e\n",
      'WATCH_CONTEXT_VIDEO_TEMPLATE': "    \u003cli class=\"guide-context-item context-data-item context-video yt-uix-scroller-scroll-unit __item_classes__\" data-context-item-user=\"__user_name__\" data-context-item-views=\"__view_count__\" data-context-item-actionuser=\"__action_username__\" data-context-item-type=\"video\" data-context-item-title=\"__video_title__\" data-context-item-actionverb=\"__action_verb__\" data-context-item-id=\"__video_id__\" data-context-item-time=\"__video_time__\"\u003e\u003ca href=\"\/watch?v=__video_id__\" class=\"yt-uix-contextlink yt-uix-sessionlink \" data-sessionlink=\"ei=a6W3UcTyCqXMiQLYr4HQBg\u0026amp;feature=__feature__\"\u003e    \u003cspan class=\"video-thumb context-video-thumb yt-thumb yt-thumb-40\"\n      \u003e\n      \u003cspan class=\"yt-thumb-default\"\u003e\n        \u003cspan class=\"yt-thumb-clip\"\u003e\n          \u003cspan class=\"yt-thumb-clip-inner\"\u003e\n            \u003cimg src=\"http:\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\" data-thumb-manual=\"1\" data-thumb=\"\/\/i4.ytimg.com\/vi\/__video_id__\/default.jpg\" data-group-key=\"guide-context-thumbs\" width=\"40\" \u003e\n            \u003cspan class=\"vertical-align\"\u003e\u003c\/span\u003e\n          \u003c\/span\u003e\n        \u003c\/span\u003e\n      \u003c\/span\u003e\n    \u003c\/span\u003e\n\u003cspan class=\"title\"\u003e__video_title__\u003c\/span\u003e\u003cspan class=\"username\"\u003eby __user_name__\n\u003c\/span\u003e\u003cspan class=\"viewcount\"\u003e__view_count__\u003c\/span\u003e\u003cspan class=\"action\"\u003e__action_username__ __action_verb__\u003c\/span\u003e\u003c\/a\u003e\u003c\/li\u003e\n",
      'WATCH_CONTEXT_PLAYLIST_TEMPLATE': "    \u003cli class=\"guide-context-item context-data-item context-playlist yt-uix-scroller-scroll-unit __item_classes__\" data-context-item-count-label=\"__video_count_label__\" data-context-item-actionuser=\"__action_username__\" data-context-item-type=\"playlist\" data-context-item-user=\"\u0026quot;__user_name__\u0026quot;\" data-context-item-title=\"__playlist_title__\" data-context-item-actionverb=\"__action_verb__\" data-context-item-count=\"__video_count__\" data-context-item-id=\"__playlist_id__\" data-context-item-videos=\"[\u0026quot;__playlist_video_id__\u0026quot;]\"\u003e\u003ca href=\"\/watch?v=__playlist_video_id__\u0026amp;list=__playlist_id__\" class=\"yt-uix-contextlink yt-uix-sessionlink \" data-sessionlink=\"ei=a6W3UcTyCqXMiQLYr4HQBg\u0026amp;feature=__feature__\"\u003e\u003cspan class=\"context-video-thumb yt-pl-thumb\"\u003e    \u003cspan class=\"video-thumb  yt-thumb yt-thumb-40\"\n      \u003e\n      \u003cspan class=\"yt-thumb-default\"\u003e\n        \u003cspan class=\"yt-thumb-clip\"\u003e\n          \u003cspan class=\"yt-thumb-clip-inner\"\u003e\n            \u003cimg src=\"http:\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\" data-thumb-manual=\"1\" data-thumb=\"\/\/i4.ytimg.com\/vi\/__playlist_video_id__\/default.jpg\" data-group-key=\"guide-context-thumbs\" width=\"40\" \u003e\n            \u003cspan class=\"vertical-align\"\u003e\u003c\/span\u003e\n          \u003c\/span\u003e\n        \u003c\/span\u003e\n      \u003c\/span\u003e\n    \u003c\/span\u003e\n  \u003cspan class=\"video-count-wrapper\"\u003e\n    \u003cspan class=\"video-count-block\"\u003e\n      \u003cspan class=\"count-label\"\u003e__video_count__\u003c\/span\u003e\n      \u003cspan class=\"text-label\"\u003e__video_count_label__\u003c\/span\u003e\n    \u003c\/span\u003e\n  \u003c\/span\u003e\n\u003c\/span\u003e\u003cspan class=\"title\"\u003e__playlist_title__\u003c\/span\u003e\u003cspan class=\"username\"\u003eby __user_name__\n\u003c\/span\u003e\u003cspan class=\"action\"\u003e__action_username__ __action_verb__\u003c\/span\u003e\u003c\/a\u003e\u003c\/li\u003e\n",
      'WATCH_CONTEXT_APPBAR_TEMPLATE': "  \u003cli  id=\"appbar-item-context\" class=\"appbar-item\"\u003e\u003cbutton type=\"button\" class=\" yt-uix-button yt-uix-button-appbar\" onclick=\";return false;\" data-button-menu-action=\"yt.www.masthead.appbar.toggleMenu\" data-button-menu-id=\"appbar-context-menu\" role=\"button\"\u003e\u003cspan class=\"yt-uix-button-content\"\u003e\u003cspan class=\"appbar-notification-count\"\u003e__item_count__\u003c\/span\u003e__headline__\u0026nbsp;\u003cspan title=\"__more_from__\" dir=\"__title_dir__\"\u003e__more_from__\u003c\/span\u003e \u003c\/span\u003e\u003cimg class=\"yt-uix-button-arrow\" src=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" alt=\"\" title=\"\"\u003e\u003c\/button\u003e\u003c\/li\u003e\n",
      'WATCH_CONTEXT_GEN204': true,
      'SPF_PREFETCH': false,
      'SPF_PREFETCH_MAX': null,
      'GUIDE_ENABLED': true,
      'TIMING_WFF': true      });

    yt.setAjaxToken('watch_fragments_ajax', "cr6GIKBj68r2TeJ8ICQH43MTZcF8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");
    yt.setAjaxToken('guide_ajax', "y3zpEBlrRPNUWMj2t54Uwxlntht8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");
    yt.setAjaxToken('promo_ajax_token', "oW19M4JimbfXy0vN8PES2BcC0sh8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");


    yt.setMsg({
      'WATCH_CONTEXT_MORE_FROM': "More from",
      'WATCH_CONTEXT_MORE_RESULTS': "More results"
    });

    
  </script>

    <script>
    yt.setConfig({
      'VIDEO_ID': "OyJ3CafAM1Q",

      'JS_PAGE_MODULES': {
        "\/\/s.ytimg.com\/yts\/jsbin\/www_watch_mod-vfleyg7dU.js": [
          ''         ]
      },


      'REPORTVIDEO_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-reportvideo-vfl6CW3Ab.js",
      'REPORTVIDEO_CSS': "http:\/\/s.ytimg.com\/yts\/cssbin\/www-watch-reportvideo-vflzqn8VY.css",


      'ENABLE_AUTO_LARGE': true    });

    yt.setAjaxToken('insight_ajax', "-B_IxTPrb5Eydy_UDGCu4XMIxGp8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");

      yt.setConfig({
    'EMBED_HTML_TEMPLATE': "\u003ciframe width=\"__width__\" height=\"__height__\" src=\"__url__\" frameborder=\"0\" allowfullscreen\u003e\u003c\/iframe\u003e",
    'EMBED_HTML_URL': "http:\/\/www.youtube.com\/embed\/__videoid__"
  });
    yt.setMsg('FLASH_UPGRADE', "\u003cdiv class=\"yt-alert yt-alert-default yt-alert-error  yt-alert-player\"\u003e  \u003cdiv class=\"yt-alert-icon\"\u003e\n    \u003cimg s\u0072c=\"\/\/s.ytimg.com\/yts\/img\/pixel-vfl3z5WfW.gif\" class=\"icon master-sprite\" alt=\"Alert icon\"\u003e\n  \u003c\/div\u003e\n\u003cdiv class=\"yt-alert-buttons\"\u003e\u003c\/div\u003e\u003cdiv class=\"yt-alert-content\" role=\"alert\"\u003e    \u003cspan class=\"yt-alert-vertical-trick\"\u003e\u003c\/span\u003e\n    \u003cdiv class=\"yt-alert-message\"\u003e\n            You need to upgrade your Adobe Flash Player to watch this video. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eDownload it from Adobe.\u003c\/a\u003e\n    \u003c\/div\u003e\n\u003c\/div\u003e\u003c\/div\u003e");
  yt.setMsg('PLAYER_FALLBACK', "The Adobe Flash Player or an HTML5 supported browser is required for video playback. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eGet the latest Flash Player\u003c\/a\u003e \u003cbr\u003e \u003ca href=\"\/html5\"\u003eLearn more about upgrading to an HTML5 browser\u003c\/a\u003e");
  yt.setMsg('QUICKTIME_FALLBACK', "The Adobe Flash Player or QuickTime is required for video playback. \u003cbr\u003e \u003ca href=\"http:\/\/get.adobe.com\/flashplayer\/\"\u003eGet the latest Flash Player\u003c\/a\u003e \u003cbr\u003e \u003ca href=\"http:\/\/www.apple.com\/quicktime\/download\/\"\u003eGet the latest version of QuickTime\u003c\/a\u003e");



    yt.setConfig({
      'IS_OWNER_VIEWING': null,
      'IS_WIDESCREEN': false,
      'PREFER_LOW_QUALITY': false,
      'ALLOW_EMBED': true,
      'ALLOW_RATINGS': true,
      'YPC_CAN_RATE_VIDEO': true,
      'YPC_SHOW_VPPA_CONFIRM_RATING': false,







        'RESOLUTION_TRACKING_ENABLED': true,





      'ADS_DATA': {"show_pyv": true, "afc_vars": {"ad_block": "2", "ad_host_tier_id": 389538, "ad_type": "image", "ad_client": "ca-pub-6219811747049371", "format": "300x250_as", "ad_channel": "3067994270+3067994272+3067994274+0854550287+afv_ugc+yt_mpvid_AATe6HfXIJQ-D5j2+yt_cid_2569964+ytdevice_1+Vertical_65+Vertical_66+Vertical_119+Vertical_563+Vertical_884+ytps_default+ytel_detailpage+afc_on_page", "video_doc_id": "yt_OyJ3CafAM1Q", "ad_host": "ca-host-pub-1800120140230655", "alternate_ad_url": "http:\/\/www.youtube.com\/ad_frame?id=watch-channel-brand-div", "language": "en"}, "show_companion": true, "show_afv": true, "afv_vars": {"google_video_doc_id": "yt_OyJ3CafAM1Q", "google_ad_block": "2", "google_language": "en", "google_ad_host_tier_id": 389538, "google_ad_host": "ca-host-pub-1800120140230655", "google_ad_client": "ca-pub-6219811747049371", "google_page_url": "http:\/\/www.youtube.com\/video\/OyJ3CafAM1Q", "google_ad_format": "300x250_as", "google_ad_channel": "3067994270+3067994272+3067994274+0854550288+afv_ugc+yt_mpvid_AATe6HfXIJQ-D5j2+yt_cid_2569964+ytdevice_1+Vertical_65+Vertical_66+Vertical_119+Vertical_563+Vertical_884+ytps_default+ytel_detailpage", "google_ad_type": "image", "google_loeid": "917000,923002,929201,916626", "google_yt_pt": "AL4CsgEH_AC3KNPqCT_ToQSkqO8EbV6vGQWZl7pha_Q4x0MH4y_lDEWtVOzpl5cKKdj_fPnT7HQ81xmXA_JJ9kxjgRcPtji-0mmPb1q9yTjB3QJ1Sx6AA0axDTkmdG5FtFh0h0u0MqQv_smWdPSJ", "google_alternate_ad_url": "http:\/\/www.youtube.com\/ad_frame?id=watch-channel-brand-div", "google_ad_height": "250"}, "gut_vars": {"tag": "\/4061\/ytpwatch\/main_2569964"}, "show_instream": false, "pyv_vars": {"iframe_json": "{\"google_ad_channel\": \"PyvWatchInRelated+PyvYTWatch+PyvWatchNoAdX+pw+cw+non_lpw+afv_ugc+yt_mpvid_AATe6HfXIJQ-D5j2+yt_cid_2569964+ytdevice_1\", \"google_video_doc_id\": \"yt_OyJ3CafAM1Q\", \"google_ad_block\": \"3\", \"google_language\": \"en\", \"google_ad_host_tier_id\": 389538, \"google_ad_type\": \"text\", \"google_max_num_ads\": 1, \"google_ad_client\": \"ca-pub-6219811747049371\", \"google_yt_pt\": \"AL4CsgEH_AC3KNPqCT_ToQSkqO8EbV6vGQWZl7pha_Q4x0MH4y_lDEWtVOzpl5cKKdj_fPnT7HQ81xmXA_JJ9kxjgRcPtji-0mmPb1q9yTjB3QJ1Sx6AA0axDTkmdG5FtFh0h0u0MqQv_smWdPSJ\", \"google_ad_host\": \"ca-host-pub-1800120140230655\", \"google_page_url\": \"http:\\\/\\\/www.youtube.com\\\/video\\\/OyJ3CafAM1Q\", \"google_loeid\": \"917000,923002,929201,916626\", \"google_only_pyv_ads\": true, \"google_ad_output\": \"js\"}", "measure_latency": false}, "show_afc": false, "use_gut": true},
      'PLAYBACK_ID': "AATe6HfWuA-RXscK",
      'PLAY_ALL_MAX': 480,
      'IN_SIGNED_OUT_ACTION_PROMO_1': false,
      'IN_SIGNED_OUT_ACTION_PROMO_2': false    });




    yt.setMsg({
      'LOADING': "Loading..."    });

      yt.setMsg({
    'UNBLOCK_USER': "Are you sure you want to unblock this user?",
    'BLOCK_USER': "Are you sure you want to block this user?"
  });
  yt.setConfig('BLOCK_USER_AJAX_XSRF', 'session_token=7T3dZHa6oaFAgZ7BOKXKoxJmui18MTM3MTA3NjMzMUAxMzcwOTg5OTMx');


      

  yt.setConfig({
    'COMMENTS_CHANNEL_CREATE_URL': null,
    'COMMENTS_SIGNIN_URL': "https:\/\/accounts.google.com\/ServiceLogin?passive=true\u0026continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26feature%3Dcomments%26hl%3Den_US%26next%3D%252Fwatch%253Fv%253DOyJ3CafAM1Q%26nomobiletemp%3D1\u0026uilel=3\u0026hl=en_US\u0026service=youtube",
    'COMMENTS_THRESHHOLD': -5,
    'COMMENTS_PAGE_SIZE': 10,
    'COMMENTS_COUNT': 5,
    'COMMENTS_YPC_CAN_POST_OR_REACT_TO_COMMENT': true,
    'COMMENT_SOURCE': "w",
    'COMMENT_OPEN_REPLY_BOX' : false
  });

  yt.setAjaxToken('link_ajax', "7T3dZHa6oaFAgZ7BOKXKoxJmui18MTM3MTA3NjMzMUAxMzcwOTg5OTMx");
  yt.setAjaxToken('comment_servlet', "LjVDANgl_xzRFGD4C7RJin1iz-d8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");
  yt.setAjaxToken('comment_voting', "akNZieKcAW7lhyu0I2Dk92NGmXB8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");




  yt.setMsg({
    'CHARACTERS_REMAINING': {"case1": "1 character remaining", "case0": "No characters remaining", "other": "# characters remaining"},
    'COMMENT_OK': "OK",
    'COMMENT_BLOCKED': "You have been blocked by the owner of this video.",
    'COMMENT_CAPTCHAFAIL': "The response to the letters on the image was not correct, please try again.",
    'COMMENT_PENDING': "Comment Pending Approval!",
    'COMMENT_ERROR_EMAIL': "Error, account unverified (see email)",
    'COMMENT_ERROR': "Error, try again",
    'COMMENT_FAILED_MAINTENANCE': "We're currently performing site maintenace, please try later.",
    'COMMENT_OWNER_LINKING': "Comments can't contain links. Please put the link in your video description and refer to it in the comment.",
    'FAILED_HASLINK': "Oops! Remove any web addresses and try again.",
    'FAILED_HASTAGS': "Oops! Remove the HTML tags and try again.",
    'FAILED_ASCIIART': "Oops! Remove the character (ascii) art and try again.",
    'FAILED_TOOSHORT': "Oops! Your comment is too short.",
    'FAILED_TOOLONG': "Oops! Your comment is too long.",
    'FAILED_BADPARENT': "Oops! You cannot respond to a deleted comment.",
    'SECONDS_REMAINING': {"case1": "1 second remaining before you can post", "case0": "You can post again", "other": "# seconds remaining before you can post"}
  });





    







    



  </script>


<script>yt.setConfig({'EVENT_ID': "a6W3UcTyCqXMiQLYr4HQBg",'PAGE_NAME': "watch",'LOGGED_IN': false,'SESSION_INDEX': null,'CURRENT_URL': "http:\/\/www.youtube.com\/watch?v=OyJ3CafAM1Q",'MASTHEAD_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-masthead-vflvU_tXo.js",'JS_COMMON_MODULE': "\/\/s.ytimg.com\/yts\/jsbin\/www_common_mod-vflq05hub.js",'SAFETY_MODE_PENDING': false,'LOCAL_DATE_TIME_CONFIG': {"shortWeekdays": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "weekdays": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "amPms": ["AM", "PM"], "formatWeekdayShortTime": "EE h:mm a", "formatShortDate": "MMM d, yyyy", "formatLongDateOnly": "MMMM d, yyyy", "shortMonths": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], "formatLongDate": "MMMM d, yyyy h:mm a"},'FEEDBACK_BUCKET_ID': "Watch",'FEEDBACK_LOCALE_LANGUAGE': "en",'FEEDBACK_LOCALE_EXTRAS': {"logged_in": false, "guide_subs": "NA", "accept_language": null, "is_branded": "", "experiments": "917000,923002,929201,916626,900352,921047,924605,928201,901208,929123,929121,929915,929906,929907,929125,925714,929919,929119,931202,928017,912512,912515,912521,906906,904488,931910,931913,904830,930807,919373,906836,933701,900816,926403,912711,930618,930621,929606,910075", "is_partner": ""}});yt.setMsg({'ADDTO_WATCH_LATER': "Watch Later",'ADDTO_WATCH_LATER_ADDED': "Added",'ADDTO_WATCH_LATER_ERROR': "Error"});yt.setAjaxToken('addto_ajax_logged_out', "N5R0ApS67sD6VlJQqWTWaFO0U7t8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");  yt.setConfig('FEED_PRIVACY_CSS_URL', "http:\/\/s.ytimg.com\/yts\/cssbin\/www-feedprivacydialog-vflmpM6y2.css");
  yt.setAjaxToken('feed_privacy_ajax', "1-rygmYOGjvd03er22cYiZ3fhZh8MTM3MTA3NjMzMUAxMzcwOTg5OTMx");
    yt.setConfig('FEED_PRIVACY_LIGHTBOX_ENABLED', true);
yt.setConfig({'SBOX_JS_URL': "\/\/s.ytimg.com\/yts\/jsbin\/www-searchbox-vfl5XnjkO.js",'SBOX_SETTINGS': {"SESSION_INDEX": null, "SHOW_CHIP": false, "CLOSE_ICON_URL": "\/\/s.ytimg.com\/yts\/img\/icons\/close-vflrEJzIW.png", "USE_HTTPS": false, "PSUGGEST_TOKEN": null, "HAS_ON_SCREEN_KEYBOARD": false, "REQUEST_DOMAIN": "us", "CHIP_PARAMETERS": {}, "EXPERIMENT_ID": -1, "REQUEST_LANGUAGE": "en"},'SBOX_LABELS': {"SUGGESTION_DISMISS_LABEL": "Dismiss", "SUGGESTION_DISMISSED_LABEL": "Suggestion dismissed", "WATCH_NOW_LABEL": "Watch now", "VIEW_CHANNEL_LABEL": "View channel"}});  yt.setConfig({
    'YPC_LOADER_ENABLED': true,
    'YPC_LOADER_CONFIGS': "\/ypc_config_ajax",
    'YPC_LOADER_JS': "\/\/s.ytimg.com\/yts\/jsbin\/www-ypc-vflmtgBB2.js",
    'YPC_LOADER_CSS': "http:\/\/s.ytimg.com\/yts\/cssbin\/www-ypc-vflRGdYjt.css",
    'YPC_LOADER_CALLBACKS': ['yt.www.ypc.checkout.init', 'yt.www.ypc.subscription.init']
  });
</script>    <script>
ytcsi.span('st', 65);yt.setConfig({'TIMING_ACTION': "watch,watch7ad",'TIMING_INFO': {"yt_ad_an": "afv,dclk", "yt_lt": "cold", "yt_ad_pr": 0, "ei": "a6W3UcTyCqXMiQLYr4HQBg", "yt_spf": 0, "yt_ad": 1, "yt_li": 0, "yt_pt": "flash", "e": "917000,923002,929201,916626"}});    </script>
<script>yt.setConfig({'XSRF_TOKEN': "6jIDB5iwwFGLYzfTdswJ0ZvPwWt8MTM3MTA3NjMzMUAxMzcwOTg5OTMx",'XSRF_REDIRECT_TOKEN': "E3jNJcT8WjS8QCBa_5wDLGWb4qp8MTM3MTA3NjMzMUAxMzcwOTg5OTMx",'XSRF_FIELD_NAME': "session_token"});</script><script>yt.setConfig('THUMB_DELAY_LOAD_BUFFER', 0);</script><script>if (window.ytcsi) {ytcsi.tick("js_foot");}</script><div id="debug"></div></body></html>

Heritrix is free software; you can redistribute it and/or modify it 
under the terms of the Apache License, Version 2.0:

  http://www.apache.org/licenses/LICENSE-2.0
  
Some individual source code files are subject to or offered under other
licenses. Here is a list of such files currently known:

 * commons/src/main/resources/effective_tld_names.dat
 * commons/src/main/java/org/archive/util/BenchmarkBlooms.java
 * commons/src/main/java/org/archive/util/BloomFilter32bit.java
 * commons/src/main/java/org/archive/util/BloomFilter32bitSplit.java
 * commons/src/main/java/org/archive/util/BloomFilter32bp2.java
 * commons/src/main/java/org/archive/util/BloomFilter32bp2Split.java
 * commons/src/main/java/org/archive/util/BloomFilter64bit.java
 * commons/src/main/java/org/archive/util/BloomFilter.java
 * engine/src/main/java/org/archive/crawler/frontier/BucketQueueAssignmentPolicy.java
 * engine/src/main/java/org/archive/crawler/util/RecoveryLogMapper.java
 * engine/src/main/java/org/archive/crawler/util/SeedUrlNotFoundException.java
 * modules/src/main/java/org/archive/modules/canonicalize/StripExtraSlashes.java
 * modules/src/main/java/org/archive/modules/extractor/JerichoExtractorHTML.java
 * modules/src/main/java/org/archive/modules/writer/Kw3Constants.java
 * modules/src/main/java/org/archive/modules/writer/Kw3WriterProcessor.java
 * modules/src/main/java/org/archive/modules/writer/MirrorWriterProcessor.java

Except as otherwise noted, always consult individual source files for most
accurate info.
 
Heritrix is distributed with the libraries it depends upon.  The 
libraries can be found under the 'lib' directory, and are used under 
the terms of their respective licenses, which are included alongside 
the libraries in the 'lib' directory. 

--
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

 
 
 
../README.mdThis directory contains utility classes and scripts which can be used, together 
with other tools like Hadoop, to perform an offline PageRank-calculation of a 
crawl's revealed link graph.

For more information, visit:
http://webteam.archive.org/confluence/display/Heritrix/Offline+PageRank+Analysis+Notes.

Note that the Java files in this directory are modifications of Hadoop 
example code, and are thus published under the Apache license./*
 *                                 Apache License
 *                           Version 2.0, January 2004
 *                        http://www.apache.org/licenses/
 *
 *   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
 *
 *   1. Definitions.
 *
 *      "License" shall mean the terms and conditions for use, reproduction,
 *      and distribution as defined by Sections 1 through 9 of this document.
 *
 *      "Licensor" shall mean the copyright owner or entity authorized by
 *      the copyright owner that is granting the License.
 *
 *      "Legal Entity" shall mean the union of the acting entity and all
 *      other entities that control, are controlled by, or are under common
 *      control with that entity. For the purposes of this definition,
 *      "control" means (i) the power, direct or indirect, to cause the
 *      direction or management of such entity, whether by contract or
 *      otherwise, or (ii) ownership of fifty percent (50%) or more of the
 *      outstanding shares, or (iii) beneficial ownership of such entity.
 *
 *      "You" (or "Your") shall mean an individual or Legal Entity
 *      exercising permissions granted by this License.
 *
 *      "Source" form shall mean the preferred form for making modifications,
 *      including but not limited to software source code, documentation
 *      source, and configuration files.
 *
 *      "Object" form shall mean any form resulting from mechanical
 *      transformation or translation of a Source form, including but
 *      not limited to compiled object code, generated documentation,
 *      and conversions to other media types.
 *
 *      "Work" shall mean the work of authorship, whether in Source or
 *      Object form, made available under the License, as indicated by a
 *      copyright notice that is included in or attached to the work
 *      (an example is provided in the Appendix below).
 *
 *      "Derivative Works" shall mean any work, whether in Source or Object
 *      form, that is based on (or derived from) the Work and for which the
 *      editorial revisions, annotations, elaborations, or other modifications
 *      represent, as a whole, an original work of authorship. For the purposes
 *      of this License, Derivative Works shall not include works that remain
 *      separable from, or merely link (or bind by name) to the interfaces of,
 *      the Work and Derivative Works thereof.
 *
 *      "Contribution" shall mean any work of authorship, including
 *      the original version of the Work and any modifications or additions
 *      to that Work or Derivative Works thereof, that is intentionally
 *      submitted to Licensor for inclusion in the Work by the copyright owner
 *      or by an individual or Legal Entity authorized to submit on behalf of
 *      the copyright owner. For the purposes of this definition, "submitted"
 *      means any form of electronic, verbal, or written communication sent
 *      to the Licensor or its representatives, including but not limited to
 *      communication on electronic mailing lists, source code control systems,
 *      and issue tracking systems that are managed by, or on behalf of, the
 *      Licensor for the purpose of discussing and improving the Work, but
 *      excluding communication that is conspicuously marked or otherwise
 *      designated in writing by the copyright owner as "Not a Contribution."
 *
 *      "Contributor" shall mean Licensor and any individual or Legal Entity
 *      on behalf of whom a Contribution has been received by Licensor and
 *      subsequently incorporated within the Work.
 *
 *   2. Grant of Copyright License. Subject to the terms and conditions of
 *      this License, each Contributor hereby grants to You a perpetual,
 *      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
 *      copyright license to reproduce, prepare Derivative Works of,
 *      publicly display, publicly perform, sublicense, and distribute the
 *      Work and such Derivative Works in Source or Object form.
 *
 *   3. Grant of Patent License. Subject to the terms and conditions of
 *      this License, each Contributor hereby grants to You a perpetual,
 *      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
 *      (except as stated in this section) patent license to make, have made,
 *      use, offer to sell, sell, import, and otherwise transfer the Work,
 *      where such license applies only to those patent claims licensable
 *      by such Contributor that are necessarily infringed by their
 *      Contribution(s) alone or by combination of their Contribution(s)
 *      with the Work to which such Contribution(s) was submitted. If You
 *      institute patent litigation against any entity (including a
 *      cross-claim or counterclaim in a lawsuit) alleging that the Work
 *      or a Contribution incorporated within the Work constitutes direct
 *      or contributory patent infringement, then any patent licenses
 *      granted to You under this License for that Work shall terminate
 *      as of the date such litigation is filed.
 *
 *   4. Redistribution. You may reproduce and distribute copies of the
 *      Work or Derivative Works thereof in any medium, with or without
 *      modifications, and in Source or Object form, provided that You
 *      meet the following conditions:
 *
 *      (a) You must give any other recipients of the Work or
 *          Derivative Works a copy of this License; and
 *
 *      (b) You must cause any modified files to carry prominent notices
 *          stating that You changed the files; and
 *
 *      (c) You must retain, in the Source form of any Derivative Works
 *          that You distribute, all copyright, patent, trademark, and
 *          attribution notices from the Source form of the Work,
 *          excluding those notices that do not pertain to any part of
 *          the Derivative Works; and
 *
 *      (d) If the Work includes a "NOTICE" text file as part of its
 *          distribution, then any Derivative Works that You distribute must
 *          include a readable copy of the attribution notices contained
 *          within such NOTICE file, excluding those notices that do not
 *          pertain to any part of the Derivative Works, in at least one
 *          of the following places: within a NOTICE text file distributed
 *          as part of the Derivative Works; within the Source form or
 *          documentation, if provided along with the Derivative Works; or,
 *          within a display generated by the Derivative Works, if and
 *          wherever such third-party notices normally appear. The contents
 *          of the NOTICE file are for informational purposes only and
 *          do not modify the License. You may add Your own attribution
 *          notices within Derivative Works that You distribute, alongside
 *          or as an addendum to the NOTICE text from the Work, provided
 *          that such additional attribution notices cannot be construed
 *          as modifying the License.
 *
 *      You may add Your own copyright statement to Your modifications and
 *      may provide additional or different license terms and conditions
 *      for use, reproduction, or distribution of Your modifications, or
 *      for any such Derivative Works as a whole, provided Your use,
 *      reproduction, and distribution of the Work otherwise complies with
 *      the conditions stated in this License.
 *
 *   5. Submission of Contributions. Unless You explicitly state otherwise,
 *      any Contribution intentionally submitted for inclusion in the Work
 *      by You to the Licensor shall be under the terms and conditions of
 *      this License, without any additional terms or conditions.
 *      Notwithstanding the above, nothing herein shall supersede or modify
 *      the terms of any separate license agreement you may have executed
 *      with Licensor regarding such Contributions.
 *
 *   6. Trademarks. This License does not grant permission to use the trade
 *      names, trademarks, service marks, or product names of the Licensor,
 *      except as required for reasonable and customary use in describing the
 *      origin of the Work and reproducing the content of the NOTICE file.
 *
 *   7. Disclaimer of Warranty. Unless required by applicable law or
 *      agreed to in writing, Licensor provides the Work (and each
 *      Contributor provides its Contributions) on an "AS IS" BASIS,
 *      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 *      implied, including, without limitation, any warranties or conditions
 *      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
 *      PARTICULAR PURPOSE. You are solely responsible for determining the
 *      appropriateness of using or redistributing the Work and assume any
 *      risks associated with Your exercise of permissions under this License.
 *
 *   8. Limitation of Liability. In no event and under no legal theory,
 *      whether in tort (including negligence), contract, or otherwise,
 *      unless required by applicable law (such as deliberate and grossly
 *      negligent acts) or agreed to in writing, shall any Contributor be
 *      liable to You for damages, including any direct, indirect, special,
 *      incidental, or consequential damages of any character arising as a
 *      result of this License or out of the use or inability to use the
 *      Work (including but not limited to damages for loss of goodwill,
 *      work stoppage, computer failure or malfunction, or any and all
 *      other commercial damages or losses), even if such Contributor
 *      has been advised of the possibility of such damages.
 *
 *   9. Accepting Warranty or Additional Liability. While redistributing
 *      the Work or Derivative Works thereof, You may choose to offer,
 *      and charge a fee for, acceptance of support, warranty, indemnity,
 *      or other liability obligations and/or rights consistent with this
 *      License. However, in accepting such obligations, You may act only
 *      on Your own behalf and on Your sole responsibility, not on behalf
 *      of any other Contributor, and only if You agree to indemnify,
 *      defend, and hold each Contributor harmless for any liability
 *      incurred by, or claims asserted against, such Contributor by reason
 *      of your accepting any such warranty or additional liability.
 *
 *   END OF TERMS AND CONDITIONS
 *
 *   APPENDIX: How to apply the Apache License to your work.
 *
 *      To apply the Apache License to your work, attach the following
 *      boilerplate notice, with the fields enclosed by brackets "[]"
 *      replaced with your own identifying information. (Don't include
 *      the brackets!)  The text should be enclosed in the appropriate
 *      comment syntax for the file format. We also recommend that a
 *      file or class name and description of purpose be included on the
 *      same "printed page" as the copyright notice for easier
 *      identification within third-party archives.
 *
 *   Copyright [yyyy] [name of copyright owner]
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */
From http://www.beanshell.org/license.html

Dual Licensing: Sun Public License / Gnu Lesser Public License

BeanShell is dual licensed under both the SPL and LGPL. You may use and 
develop BeanShell under either license.

Please see the Sun Public License 
[http://www.sun.com/developers/spl.html] for details.

About the LGPL

Note: the LGPL has become the "Lesser Gnu Public License" and BeanShell 
has adopted the new version...

A quick note about the LGPL:

The LGPL is less restrictive than the ordinary GNU Public License in 
that it does not force you to distribute your own applications under 
the terms of the GPL. It primarily requires that you include a notice 
that you are using the software in your documentation and provide 
access to the original source code. It also essentially requires that 
if you modify or extend BeanShell itself that you make those changes 
available separately, under the terms of either the LGPL or the GPL. 
I would ask that you accomodate this by simply sending me your bug 
fixes and improvement to allow me to incorporate them into the general 
BeanShell release. Please see the LGPL 
[http://www.gnu.org/copyleft/lesser.html] for the details.

If you have a more precise, brief explanation please let me know! 
Thanks! - Pat

Please also feel free to contact me: (Pat Niemeyer pat@pat.net) about 
other licensing arrangements.                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
dnsjava v2.0

http://www.xbill.org/dnsjava
http://www.dnsjava.org/

Author:

Brian Wellington (bwelling@xbill.org)
March 12, 2004

Overview:

dnsjava is an implementation of DNS in Java.  It supports all defined record
types (including the DNSSEC types), and unknown types.  It can be used for
queries, zone transfers, and dynamic updates.  It includes a cache which can be
used by clients, and an authoritative only server.  It supports TSIG
authenticated messages, partial DNSSEC verification, and EDNS0.  It is fully
thread safe.  It can be used to replace the native DNS support in Java.

dnsjava was started as an excuse to learn Java.  It was useful for testing new
features in BIND without rewriting the C resolver.  It was then cleaned up and
extended in order to be used as a testing framework for DNS interoperability
testing.  The high level API and caching resolver were added to make it useful
to a wider audience.  The authoritative only server was added as proof of
concept.


Getting started:

Run 'ant' from the toplevel directory to build dnsjava (a Makefile is also
provided, but does not have all of the features of the ant script).  JDK 1.4
or higher is required.

To compile name service provider support (org.xbill.DNS.spi), run 'ant spi'.


Replacing the standard Java DNS functionality:

Beginning with Java 1.4, service providers can be loaded at runtime.  To load
the dnsjava service provider, build it as explained above and set the system
property:

	sun.net.spi.nameservice.provider.1=dns,dnsjava

This instructs the JVM to use the dnsjava service provide for DNS at the
highest priority.


Testing dnsjava:

Matt Rutherford <rutherfo@cs.colorado.edu> contributed a number of unit
tests, which are in the tests subdirectory.  The hierarchy under tests
mirrors the org.xbill.DNS classes.  To build the unit tests, run
'ant compile_tests', and to run then, run 'ant run_tests'.  The tests require
JUnit (http://www.junit.org) to be installed.

Some high-level test programs are in org/xbill/DNS/tests.


Limitations:

There's no standard way to determine what the local nameserver or DNS search
path is at runtime from within the JVM.  dnsjava attempts several methods
until one succeeds.

 - The properties 'dns.server' and 'dns.search' (comma delimited lists) are
   checked.  The servers can either be IP addresses or hostnames (which are
   resolved using Java's built in DNS support).
 - The sun.net.dns.ResolverConfiguration class is queried.
 - On Unix, /etc/resolv.conf is parsed.
 - On Windows, ipconfig/winipcfg is called and its output parsed.  This may
   fail for non-English versions on Windows.
 - As a last resort, "localhost" is used as the nameserver, and the search
   path is empty.

The underlying platform must use an ASCII encoding of characters.  This means
that dnsjava will not work on OS/390, for example.


Additional documentation:

Javadoc documentation is provided in the doc/ subdirectory of binary
distributions, and can be built with 'ant docs'.


License:

dnsjava is placed under the BSD license.  Several files are also under
additional licenses; see the individual files for details.

Copyright (c) 1999-2005, Brian Wellington
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of the dnsjava project nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Final notes:

 - Thanks to Network Associates, Inc. for sponsoring some of the original
   dnsjava work in 1999-2000.

 - Thanks to Nominum, Inc. for sponsoring some work on dnsjava from 2000 to
   the present.
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
From http://www.lowagie.com/iText/download.html

iText: a Free Java-PDF library by Bruno Lowagie and Paulo Soares

License Agreement

iText is published under 2 different licenses: MPL and LGPL.

If you are a new user of iText, MPL is recommended (without the LGPL). 
MPL is less strict than LGPL. Please read the MPL license agreement 
[http://www.lowagie.com/iText/MPL-1.1.txt] before downloading and/or 
using iText.

LGPL is maintained for backward compatibility only. If you choose the 
LGPL, you need to mention the MPL as an alternative license. Please 
read the LGPL license agreement [http://www.lowagie.com/iText/lgpl.txt]
for more info.

This library is free and I want it to stay free: you can use it 
without paying a fee; you don't need to register anywhere. Only keep 
in mind that agreeing with the license is crucial to protect the 
software, its developers and its users. This library is distributed 
in the hope that it will be useful, but WITHOUT any warranty. If you 
don't like free software, don't (ab)use it!
jasper-compiler-5.5.15.jar and jasper-runtime-5.5.15.jar are part of Apache
Tomcat, available under the Apache License, Version 2.0. 

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
The JavaSWF2-BSD License

Copyright (c) 2001, David N. Main, All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. The name of the author may not be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

/*-
 * $Id: LICENSE,v 1.10.2.1 2007/02/01 14:49:28 cwl Exp $
 */

The following is the license that applies to this copy of the Berkeley
DB Java Edition software.  For a license to use the Berkeley DB Java
Edition software under conditions other than those described here, or
to purchase support for this software, please contact Oracle at
berkeleydb-info_us@oracle.com.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
/*
 * Copyright (c) 2002,2007 Oracle.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Redistributions in any form must be accompanied by information on
 *    how to obtain complete source code for the DB software and any
 *    accompanying software that uses the DB software.  The source code
 *    must either be included in the distribution or be available for no
 *    more than the cost of distribution plus a nominal fee, and must be
 *    freely redistributable under reasonable conditions.  For an
 *    executable file, complete source code means the source code for all
 *    modules it contains.  It does not include source code for modules or
 *    files that typically accompany the major components of the operating
 *    system on which the executable file runs.
 *
 * THIS SOFTWARE IS PROVIDED BY ORACLE ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR
 * NON-INFRINGEMENT, ARE DISCLAIMED.  IN NO EVENT SHALL ORACLE BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
 * BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
 * IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
/***
 * ASM: a very small and fast Java bytecode manipulation framework
 * Copyright (c) 2000-2005 INRIA, France Telecom
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the copyright holders nor the names of its
 *    contributors may be used to endorse or promote products derived from
 *    this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */
From http://jerichohtml.sourceforge.net/doc/index.html

Jericho HTML Parser

Jericho HTML Parser is a simple but powerful java library allowing 
analysis and manipulation of parts of an HTML document, including 
some common server-side tags, while reproducing verbatim any 
unrecognised or invalid HTML. It also provides high-level HTML form 
manipulation functions.

It is an open source library released under both the Eclipse Public 
License (EPL) [http://www.eclipse.org/legal/epl-v10.html] and GNU 
Lesser General Public License (LGPL) 
[http://www.gnu.org/copyleft/lesser.html]. You are therefore free to 
use it in commercial applications subject to the terms detailed in 
either one of these licence documents.                                  Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<HEAD>
<TITLE>Common Public License - v 1.0</TITLE>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</HEAD>

<BODY BGCOLOR="#FFFFFF" VLINK="#800000">


<P ALIGN="CENTER"><B>Common Public License - v 1.0</B>
<P><B></B><FONT SIZE="3"></FONT>
<P><FONT SIZE="3"></FONT><FONT SIZE="2">THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS COMMON PUBLIC LICENSE ("AGREEMENT").  ANY USE, REPRODUCTION OR DISTRIBUTION OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.</FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"><B>1.  DEFINITIONS</B></FONT>
<P><FONT SIZE="2">"Contribution" means:</FONT>

<UL><FONT SIZE="2">a) in the case of the initial Contributor, the initial code and documentation distributed under this Agreement, and<BR CLEAR="LEFT">
b) in the case of each subsequent Contributor:</FONT></UL>


<UL><FONT SIZE="2">i)	 	changes to the Program, and</FONT></UL>


<UL><FONT SIZE="2">ii)		additions to the Program;</FONT></UL>


<UL><FONT SIZE="2">where such changes and/or additions to the Program originate from and are distributed by that particular Contributor.  </FONT><FONT SIZE="2">A Contribution 'originates' from a Contributor if it was added to the Program by such Contributor itself or anyone acting on such Contributor's behalf.  </FONT><FONT SIZE="2">Contributions do not include additions to the Program which:  (i) are separate modules of software distributed in conjunction with the Program under their own license agreement, and (ii) are not derivative works of the Program.  </FONT></UL>

<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">"Contributor" means any person or entity that distributes the Program.</FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">"Licensed Patents " mean patent claims licensable by a Contributor which are necessarily infringed by the use or sale of its Contribution alone or when combined with the Program.  </FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2">"Program" means the Contributions distributed in accordance with this Agreement.</FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">"Recipient" means anyone who receives the Program under this Agreement, including all Contributors.</FONT>
<P><FONT SIZE="2"><B></B></FONT>
<P><FONT SIZE="2"><B>2.  GRANT OF RIGHTS</B></FONT>

<UL><FONT SIZE="2"></FONT><FONT SIZE="2">a)	</FONT><FONT SIZE="2">Subject to the terms of this Agreement, each Contributor hereby grants</FONT><FONT SIZE="2"> Recipient a non-exclusive, worldwide, royalty-free copyright license to</FONT><FONT SIZE="2" COLOR="#FF0000"> </FONT><FONT SIZE="2">reproduce, prepare derivative works of, publicly display, publicly perform, distribute and sublicense the Contribution of such Contributor, if any, and such derivative works, in source code and object code form.</FONT></UL>


<UL><FONT SIZE="2"></FONT></UL>


<UL><FONT SIZE="2"></FONT><FONT SIZE="2">b) 	Subject to the terms of this Agreement, each Contributor hereby grants </FONT><FONT SIZE="2">Recipient a non-exclusive, worldwide,</FONT><FONT SIZE="2" COLOR="#008000"> </FONT><FONT SIZE="2">royalty-free patent license under Licensed Patents to make, use, sell, offer to sell, import and otherwise transfer the Contribution of such Contributor, if any, in source code and object code form.  This patent license shall apply to the combination of the Contribution and the Program if, at the time the Contribution is added by the Contributor, such addition of the Contribution causes such combination to be covered by the Licensed Patents.  The patent license shall not apply to any other combinations which include the Contribution.  No hardware per se is licensed hereunder.   </FONT></UL>


<UL><FONT SIZE="2"></FONT></UL>


<UL><FONT SIZE="2">c)	Recipient understands that although each Contributor grants the licenses to its Contributions set forth herein, no assurances are provided by any Contributor that the Program does not infringe the patent or other intellectual property rights of any other entity.  Each Contributor disclaims any liability to Recipient for claims brought by any other entity based on infringement of intellectual property rights or otherwise.  As a condition to exercising the rights and licenses granted hereunder, each Recipient hereby assumes sole responsibility to secure any other intellectual property rights needed, if any.  For example, if a third party patent license is required to allow Recipient to distribute the Program, it is Recipient's responsibility to acquire that license before distributing the Program.</FONT></UL>


<UL><FONT SIZE="2"></FONT></UL>


<UL><FONT SIZE="2">d)	Each Contributor represents that to its knowledge it has sufficient copyright rights in its Contribution, if any, to grant the copyright license set forth in this Agreement. </FONT></UL>


<UL><FONT SIZE="2"></FONT></UL>

<P><FONT SIZE="2"><B>3.  REQUIREMENTS</B></FONT>
<P><FONT SIZE="2"><B></B>A Contributor may choose to distribute the Program in object code form under its own license agreement, provided that:</FONT>

<UL><FONT SIZE="2">a)	it complies with the terms and conditions of this Agreement; and</FONT></UL>


<UL><FONT SIZE="2">b)	its license agreement:</FONT></UL>


<UL><FONT SIZE="2">i)	effectively disclaims</FONT><FONT SIZE="2"> on behalf of all Contributors all warranties and conditions, express and implied, including warranties or conditions of title and non-infringement, and implied warranties or conditions of merchantability and fitness for a particular purpose; </FONT></UL>


<UL><FONT SIZE="2">ii) 	effectively excludes on behalf of all Contributors all liability for damages, including direct, indirect, special, incidental and consequential damages, such as lost profits; </FONT></UL>


<UL><FONT SIZE="2">iii)</FONT><FONT SIZE="2">	states that any provisions which differ from this Agreement are offered by that Contributor alone and not by any other party; and</FONT></UL>


<UL><FONT SIZE="2">iv)	states that source code for the Program is available from such Contributor, and informs licensees how to obtain it in a reasonable manner on or through a medium customarily used for software exchange.</FONT><FONT SIZE="2" COLOR="#0000FF"> </FONT><FONT SIZE="2" COLOR="#FF0000"></FONT></UL>


<UL><FONT SIZE="2" COLOR="#FF0000"></FONT><FONT SIZE="2"></FONT></UL>

<P><FONT SIZE="2">When the Program is made available in source code form:</FONT>

<UL><FONT SIZE="2">a)	it must be made available under this Agreement; and </FONT></UL>


<UL><FONT SIZE="2">b)	a copy of this Agreement must be included with each copy of the Program.  </FONT></UL>

<P><FONT SIZE="2"></FONT><FONT SIZE="2" COLOR="#0000FF"><STRIKE></STRIKE></FONT>
<P><FONT SIZE="2" COLOR="#0000FF"><STRIKE></STRIKE></FONT><FONT SIZE="2">Contributors may not remove or alter any copyright notices contained within the Program.  </FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">Each Contributor must identify itself as the originator of its Contribution, if any, in a manner that reasonably allows subsequent Recipients to identify the originator of the Contribution.  </FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"><B>4.  COMMERCIAL DISTRIBUTION</B></FONT>
<P><FONT SIZE="2">Commercial distributors of software may accept certain responsibilities with respect to end users, business partners and the like.  While this license is intended to facilitate the commercial use of the Program, the Contributor who includes the Program in a commercial product offering should do so in a manner which does not create potential liability for other Contributors.   Therefore, if a Contributor includes the Program in a commercial product offering, such Contributor ("Commercial Contributor") hereby agrees to defend and indemnify every other Contributor ("Indemnified Contributor") against any losses, damages and costs (collectively "Losses") arising from claims, lawsuits and other legal actions brought by a third party against the Indemnified Contributor to the extent caused by the acts or omissions of such Commercial Contributor in connection with its distribution of the Program in a commercial product offering.  The obligations in this section do not apply to any claims or Losses relating to any actual or alleged intellectual property infringement.  In order to qualify, an Indemnified Contributor must: a) promptly notify the Commercial Contributor in writing of such claim, and b) allow the Commercial Contributor to control, and cooperate with the Commercial Contributor in, the defense and any related settlement negotiations.  The Indemnified Contributor may participate in any such claim at its own expense.</FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">For example, a Contributor might include the Program in a commercial product offering, Product X.  That Contributor is then a Commercial Contributor.  If that Commercial Contributor then makes performance claims, or offers warranties related to Product X, those performance claims and warranties are such Commercial Contributor's responsibility alone.  Under this section, the Commercial Contributor would have to defend claims against the other Contributors related to those performance claims and warranties, and if a court requires any other Contributor to pay any damages as a result, the Commercial Contributor must pay those damages.</FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2" COLOR="#0000FF"></FONT>
<P><FONT SIZE="2" COLOR="#0000FF"></FONT><FONT SIZE="2"><B>5.  NO WARRANTY</B></FONT>
<P><FONT SIZE="2">EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, THE PROGRAM IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING, WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Each Recipient is</FONT><FONT SIZE="2"> solely responsible for determining the appropriateness of using and distributing </FONT><FONT SIZE="2">the Program</FONT><FONT SIZE="2"> and assumes all risks associated with its exercise of rights under this Agreement</FONT><FONT SIZE="2">, including but not limited to the risks and costs of program errors, compliance with applicable laws, damage to or loss of data, </FONT><FONT SIZE="2">programs or equipment, and unavailability or interruption of operations</FONT><FONT SIZE="2">.  </FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2"><B>6.  DISCLAIMER OF LIABILITY</B></FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2">EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, NEITHER RECIPIENT NOR ANY CONTRIBUTORS SHALL HAVE ANY LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES </FONT><FONT SIZE="2">(INCLUDING WITHOUT LIMITATION LOST PROFITS),</FONT><FONT SIZE="2"> HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE EXERCISE OF ANY RIGHTS GRANTED HEREUNDER, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"><B>7.  GENERAL</B></FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2">If any provision of this Agreement is invalid or unenforceable under applicable law, it shall not affect the validity or enforceability of the remainder of the terms of this Agreement, and without further action by the parties hereto, such provision shall be reformed to the minimum extent necessary to make such provision valid and enforceable.</FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">If Recipient institutes patent litigation against a Contributor with respect to a patent applicable to software (including a cross-claim or counterclaim in a lawsuit), then any patent licenses granted by that Contributor to such Recipient under this Agreement shall terminate as of the date such litigation is filed.  In addition, if Recipient institutes patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Program itself (excluding combinations of the Program with other software or hardware) infringes such Recipient's patent(s), then such Recipient's rights granted under Section 2(b) shall terminate as of the date such litigation is filed. </FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">All Recipient's rights under this Agreement shall terminate if it fails to comply with any of the material terms or conditions of this Agreement and does not cure such failure in a reasonable period of time after becoming aware of such noncompliance.  If all Recipient's rights under this Agreement terminate, Recipient agrees to cease use and distribution of the Program as soon as reasonably practicable.  However, Recipient's obligations under this Agreement and any licenses granted by Recipient relating to the Program shall continue and survive.  </FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2">Everyone is permitted to copy and distribute copies of this Agreement, but in order to avoid inconsistency the Agreement is copyrighted  and may only be modified in the following manner. The Agreement Steward reserves the right to </FONT><FONT SIZE="2">publish new versions (including revisions) of this Agreement from time to </FONT><FONT SIZE="2">time. No one other than the Agreement Steward has the right to modify this Agreement. IBM is the initial Agreement Steward.   IBM may assign the responsibility to serve as the Agreement Steward to a suitable separate entity.  </FONT><FONT SIZE="2">Each new version of the Agreement will be given a distinguishing version number.  The Program (including Contributions) may always be distributed subject to the version of the Agreement under which it was received. In addition, after a new version of the Agreement is published, Contributor may elect to distribute the Program (including its Contributions) under the new </FONT><FONT SIZE="2">version.  </FONT><FONT SIZE="2">Except as expressly stated in Sections 2(a) and 2(b) above, Recipient receives no rights or licenses to the intellectual property of any Contributor under this Agreement, whether expressly, </FONT><FONT SIZE="2">by implication, estoppel or otherwise</FONT><FONT SIZE="2">.</FONT><FONT SIZE="2">  All rights in the Program not expressly granted under this Agreement are reserved.</FONT>
<P><FONT SIZE="2"></FONT>
<P><FONT SIZE="2">This Agreement is governed by the laws of the State of New York and the intellectual property laws of the United States of America. No party to this Agreement will bring a legal action under this Agreement more than one year after the cause of action arose.  Each party waives its rights to a jury trial in any resulting litigation.</FONT>
<P><FONT SIZE="2"></FONT><FONT SIZE="2"></FONT>
<P><FONT SIZE="2"></FONT>

</BODY>

</HTML>		   GNU LESSER GENERAL PUBLIC LICENSE
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
/* ====================================================================
 * The Apache Software License, Version 1.1
 *
 * Copyright (c) 2000-2002 The Apache Software Foundation.  All rights
 * reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *
 * 3. The end-user documentation included with the redistribution,
 *    if any, must include the following acknowledgment:
 *       "This product includes software developed by the
 *        Apache Software Foundation (http://www.apache.org/)."
 *    Alternately, this acknowledgment may appear in the software itself,
 *    if and wherever such third-party acknowledgments normally appear.
 *
 * 4. The names "Apache" and "Apache Software Foundation", "Jakarta-Oro" 
 *    must not be used to endorse or promote products derived from this
 *    software without prior written permission. For written
 *    permission, please contact apache@apache.org.
 *
 * 5. Products derived from this software may not be called "Apache" 
 *    or "Jakarta-Oro", nor may "Apache" or "Jakarta-Oro" appear in their 
 *    name, without prior written permission of the Apache Software Foundation.
 *
 * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED.  IN NO EVENT SHALL THE APACHE SOFTWARE FOUNDATION OR
 * ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
 * USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 * ====================================================================
 *
 * This software consists of voluntary contributions made by many
 * individuals on behalf of the Apache Software Foundation.  For more
 * information on the Apache Software Foundation, please see
 * <http://www.apache.org/>.
 */
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
servlet-4.1.34.jar is part of Apache Tomcat, available under the Apache 
License, Version 2.0. 

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
Heritrix Documentation
======================

This directory contains structured documentation we're in the process of
migrating and reformatting. It can be [viewed online](https://heritrix.readthedocs.io/en/latest/).

The main bulk of Heritrix's documentation currently lives on the [Github wiki](https://github.com/internetarchive/heritrix3/wiki).
sphinxcontrib-httpdomain==1.7.0
Copyright (C) 2011 by Marijn Haverbeke <marijnh@gmail.com>

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

Please note that some subdirectories of the CodeMirror distribution
include their own LICENSE files, and are released under different
licences.
CodeMirror: an in-browser code editor

Provides a nicer editing experience for the crawl configuration and script
console.

We only include here the modes that Heritrix actually uses.

License: MIT-style
Website: http://codemirror.net/
# This robots.txt is used by the RobotsExclusion heritrix integration self test.
User-agent: heritrix_selftest(+http://localhost.localdomain)
Disallow: /RobotsExclusion/excluded.html
Disallow: /RobotsExclusion/excluded/
The robots.txt that is used in this test actually lives in the root webapp.
It has to be there to it shows at the root of our host.
This is a simple sample (say that three times fast).
http://127.0.0.1:7000/random/
http://127.0.0.1:7001/random/
http://127.0.0.1:7002/random/
http://127.0.0.1:7003/random/
http://127.0.0.1:7004/random/
http://127.0.0.1:7005/random/
http://127.0.0.1:7006/random/
http://127.0.0.1:7007/random/
http://127.0.0.1:7008/random/
http://127.0.0.1:7009/random/
http://127.0.0.1:7777/seed.html 1
http://127.0.0.1:7777/one/a.html 1
http://127.0.0.1:7777/one/b.html 1
http://127.0.0.1:7777/one/c.html 1
http://127.0.0.1:7777/five/a.html 5
http://127.0.0.1:7777/five/b.html 5
http://127.0.0.1:7777/five/c.html 5
http://127.0.0.1:7777/ten/a.html 10
http://127.0.0.1:7777/ten/b.html 10
http://127.0.0.1:7777/ten/c.html 10
