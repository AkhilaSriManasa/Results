The QuickFIX Software License, Version 1.0

Copyright (c) 2001-2005 quickfixengine.org  All rights
reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in
   the documentation and/or other materials provided with the
   distribution.

3. The end-user documentation included with the redistribution,
   if any, must include the following acknowledgment:
      "This product includes software developed by
       quickfixengine.org (http://www.quickfixengine.org/)."
   Alternately, this acknowledgment may appear in the software itself,
   if and wherever such third-party acknowledgments normally appear.

4. The names "QuickFIX" and "quickfixengine.org" must
   not be used to endorse or promote products derived from this
   software without prior written permission. For written
   permission, please contact ask@quickfixengine.org

5. Products derived from this software may not be called "QuickFIX",
   nor may "QuickFIX" appear in their name, without prior written
   permission of quickfixengine.org

THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL QUICKFIXENGINE.ORG OR
ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
QuickFIX/J
==========

[![Build Status](https://travis-ci.org/quickfix-j/quickfixj.svg?branch=master)](https://travis-ci.org/quickfix-j/quickfixj)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.quickfixj/quickfixj-core/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.quickfixj/quickfixj-core)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/quickfix-j/quickfixj.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/quickfix-j/quickfixj/alerts/)
[![Language grade: Java](https://img.shields.io/lgtm/grade/java/g/quickfix-j/quickfixj.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/quickfix-j/quickfixj/context:java)

This is the official QuickFIX/J project repository.

## intro
QuickFIX/J is a full featured messaging engine for the FIX protocol.
It is a 100% Java open source implementation of the popular C++ QuickFIX engine.

The Financial Information eXchange (FIX) protocol is a messaging standard developed
specifically for the real-time electronic exchange of securities transactions.
FIX is a public-domain specification owned and maintained by FIX Protocol, Ltd (FPL).

For more information see the project website at http://www.quickfixj.org.

## release notes

Check out the wiki: https://github.com/quickfix-j/quickfixj/wiki

## questions
For asking questions please use the mailing list: https://lists.sourceforge.net/lists/listinfo/quickfixj-users

## issues
Please report issues here: https://github.com/quickfix-j/quickfixj/issues

## security
QuickFIX/J welcomes and appreciates responsible disclosure. Contributors are given appropriate credit in release notes and Git logs.

For security issues in QuickFIX/J itself contact the project maintainer: christoph.john-at-macd.com

For security issues in libraries used by QuickFIX/J contact the relevant project team (e.g. for Apache MINA: https://www.apache.org/security/ ). If you feel they are particularly exploitable via QuickFIX/J also feel free to follow up with the project maintainer as above so that we upgrade to the new version in a timely fashion.

Once a security issue is fixed in QuickFIX/J it will be communicated via the user mailing list and other appropriate channels.

## contributions
Pull requests are always welcome! Best is if you added a unit test to show that a certain bug has been fixed or a new feature works as expected.

## build instructions

Fastest: clone the repo and issue the following command.
```
$ mvn clean package -Dmaven.javadoc.skip=true -DskipTests -PskipBundlePlugin
```

Slower: if you only want to skip the acceptance test suite:
```
$ mvn clean package -Dmaven.javadoc.skip=true -DskipAT=true -PskipBundlePlugin
```

Slow: if you want to run all tests:
```
$ mvn clean package -Dmaven.javadoc.skip=true -PskipBundlePlugin
```
NB: If you want to use the resulting JARs in an OSGi environment you'll have to omit the `-PskipBundlePlugin` option.

## configuration options
https://rawgit.com/quickfix-j/quickfixj/master/quickfixj-core/src/main/doc/usermanual/usage/configuration.html

## basics

### Creating a QuickFIX/J application

Implement the `quickfix.Application` interface.

By implementing these interface methods in your derived class, you are requesting to be notified of events that occur on the FIX engine. The function that you should be most aware of is `fromApp`.

Here are explanations of what these functions provide for you.

`onCreate` is called when QFJ creates a new session. A session comes into and remains in existence for the life of the application. Sessions exist whether or not a counter party is connected to it. As soon as a session is created, you can begin sending messages to it. If no one is logged on, the messages will be sent at the time a connection is established with the counterparty.

`onLogon` notifies you when a valid logon has been established with a counter party. This is called when a connection has been established and the FIX logon process has completed with both parties exchanging valid logon messages. 

`onLogout` notifies you when an FIX session is no longer online. This could happen during a normal logout exchange or because of a forced termination or a loss of network connection. 

`toAdmin` provides you with a peek at the administrative messages that are being sent from your FIX engine to the counter party. This is normally not useful for an application however it is provided for any logging you may wish to do. Notice that the `quickfix.Message` is mutable. This allows you to add fields before an adminstrative message before it is sent out. 

`toApp` is a callback for application messages that are being sent to a counterparty. If you throw a `DoNotSend` exception in this method, the application will not send the message. This is mostly useful if the application has been asked to resend a message such as an order that is no longer relevant for the current market. Messages that are being resent are marked with the `PossDupFlag` in the header set to true; If a `DoNotSend` exception is thrown and the flag is set to true, a sequence reset will be sent in place of the message. If it is set to false, the message will simply not be sent. Notice that the `quickfix.Message` is mutable. This allows you to add fields to an application message before it is sent out. 

`fromAdmin` notifies you when an administrative message is sent from a counterparty to your FIX engine. This can be useful for doing extra validation on `Logon` messages such as for checking passwords. Throwing a `RejectLogon` exception will disconnect the counterparty. 

`fromApp` is one of the core entry points for your FIX application. Every application level request will come through here. If, for example, your application is a sell-side OMS, this is where you will get your new order requests. If you were a buy side, you would get your execution reports here. If a `FieldNotFound` exception is thrown, the counterparty will receive a reject indicating a conditionally required field is missing. The `Message` class will throw this exception when trying to retrieve a missing field, so you will rarely need the throw this explicitly. You can also throw an `UnsupportedMessageType` exception. This will result in the counterparty getting a reject informing them your application cannot process those types of messages. An `IncorrectTagValue` can also be thrown if a field contains a value that is out of range or you do not support. 


The sample code below shows how you might start up a FIX acceptor which listens on a socket. If you wanted an initiator, you would simply replace the acceptor in this code fragment with a `SocketInitiator`. `ThreadedSocketInitiator` and `ThreadedSocketAcceptor` classes are also available. These will supply a thread to each session that is created. If you use these you must make sure your application is thread safe.

```Java
import quickfix.*;
import java.io.FileInputStream;

public class MyClass {

  public static void main(String args[]) throws Exception {
    if (args.length != 1) return;
    String fileName = args[0];

    // FooApplication is your class that implements the Application interface
    Application application = new FooApplication();

    SessionSettings settings = new SessionSettings(new FileInputStream(fileName));
    MessageStoreFactory storeFactory = new FileStoreFactory(settings);
    LogFactory logFactory = new FileLogFactory(settings);
    MessageFactory messageFactory = new DefaultMessageFactory();
    Acceptor acceptor = new SocketAcceptor
      (application, storeFactory, settings, logFactory, messageFactory);
    acceptor.start();
    // while(condition == true) { do something; }
    acceptor.stop();
  }
}
```

### Receiving messages

Most of the messages you will be interested in looking at will be arriving in your overloaded `fromApp` method of your application. You can get fields out of messages with different degrees of type safety. The type in question here is the FIX message type.

When the application passes you a `Message` class, the Java type checker has no idea what specific FIX message it is, you must determine that dynamically. There is, however, a way we can make Java aware of this type information.

Keep in mind that all messages have a header and a trailer. If you want to see fields in them, you must first call `getHeader()` or `getTrailer()` to get access to them. Otherwise you access them just like in the message body.

QuickFIX/J has message classes that correlate to all the messages defined in the spec. They are, just like the field classes, generated directly off of the FIX specifications. To take advantage of this, you must break the messages out with the supplied `MessageCracker`. 

```Java
import quickfix.*;
import quickfix.field.*;

public void fromApp(Message message, SessionID sessionID)
      throws FieldNotFound, UnsupportedMessageType, IncorrectTagValue {

  crack(message, sessionID);
}

public void onMessage(quickfix.fix42.NewOrderSingle message, SessionID sessionID)
      throws FieldNotFound, UnsupportedMessageType, IncorrectTagValue {

  ClOrdID clOrdID = new ClOrdID();
  message.get(clOrdID);

  ClearingAccount clearingAccount = new ClearingAccount();
  message.get(clearingAccount);
}

public void onMessage(quickfix.fix42.OrderCancelRequest message, SessionID sessionID)
      throws FieldNotFound, UnsupportedMessageType, IncorrectTagValue {

  ClOrdID clOrdID = new ClOrdID();
  message.get(clOrdID);

  // compile time error!! field not defined for OrderCancelRequest
  ClearingAccount clearingAccount = new ClearingAccount();
  message.get(clearingAccount);
}
```

In order to use this you must use the `MessageCracker` as a mixin to your application. This will provide you with the `crack` method and allow you to overload specific message functions.

Any function you do not overload will by default throw an `UnsupportedMessageType` exception


Define your application like this:

```Java
import quickfix.Application;
import quickfix.MessageCracker;

public class MyApplication extends MessageCracker implements quickfix.Application {
    public void fromApp(Message message, SessionID sessionID)
            throws FieldNotFound, UnsupportedMessageType, IncorrectTagValue {
        crack(message, sessionID);
    }

    // Using annotation
    @Handler
    public void myEmailHandler(quickfix.fix50.Email email, SessionID sessionID) {
        // handler implementation
    }

    // By convention (notice different version of FIX. It's an error to have two handlers for the same message)
    // Convention is "onMessage" method with message object as first argument and SessionID as second argument
    public void onMessage(quickfix.fix44.Email email, SessionID sessionID) {
        // handler implementation
    }
}
```

If you'd rather use composition rather than inheritance of the `MessageCracker` you can construct a message cracker with a delegate object. The delegate message handler methods will be automatically discovered.

Message crackers for each FIX version are still generated for backward compatibility but it's more efficient to define the specific handlers you need.

The generated classes define handlers for all messages defined by that version of FIX. This requires the JVM to load those classes when the cracker is loaded. Most applications only need to handle a small subset of the messages defined by a FIX version so loading all the messages classes is excessive overhead in those cases.

#### Functional interfaces for receiving messages

If you prefer using lambda expressions in handling received messages, then <code>ApplicationFunctionalAdapter</code> or <code>ApplicationExtendedFunctionalAdapter</code> can be used to register reactions to events the application is interested in.

They also allow registering the interests in a given message type in a type-safe manner.

```Java
import quickfix.ApplicationFunctionalAdapter;
import quickfix.SessionID;

public class EmailForwarder {
    public void init(ApplicationFunctionalAdapter adapter) {
        adapter.addOnLogonListener(this::captureUsername);
        adapter.addFromAppListener(quickfix.fix44.Email.class, (e , s) -> forward(e));
    }

    private void forward(quickfix.fix44.Email email) {
        // implementation
    }

    private void captureUsername(SessionID sessionID) {
        // implementation
    }
}
```
<code>ApplicationFunctionalAdapter</code> and <code>ApplicationExtendedFunctionalAdapter</code> support multiple registration to the same event, and the registered callbacks are invoked in the FIFO manner. 

However FIFO cannot be guaranteed between registration with specific message type (e.g. <code>quickfix.fix44.Email</code>) and that without specific message type. For example, there is no invocation order guarantee between the following two callbacks:

```Java
    adapter.addFromAppListener((e , s) -> handleGeneral(e));

    adapter.addFromAppListener(quickfix.fix44.Email.class, (e , s) -> handleSpecific(e));
```

### Sending messages

Messages can be sent to a counter party with one of the static `Session.sendToTarget` methods. This method has several signatures. They are:

```Java
package quickfix;

public static boolean sendToTarget(Message message)
  throws SessionNotFound

public static boolean sendToTarget(Message message, SessionID sessionID)
  throws SessionNotFound

public static boolean sendToTarget
  (Message message, String senderCompID, String targetCompID)
  throws SessionNotFound
```

The highly recommended method is to use the type safe message classes. This should typically be the only way you should ever have to create messages.

Here the constructor takes in all the required fields and adds the correct `MsgType` and `BeginString` for you. What's more, by using the `set` method instead of `setField`, the compiler will not let you add a field that is not a part of a `OrderCancelRequest` based on the FIX4.1 specs. Keep in mind that you can still use `setField` if you want to force any field you want into the message.

```Java
import quickfix.*;

void sendOrderCancelRequest() throws SessionNotFound {
  quickfix.fix41.OrderCancelRequest message = new quickfix.fix41.OrderCancelRequest(
	new OrigClOrdID("123"),
	new ClOrdID("321"),
	new Symbol("LNUX"),
	new Side(Side.BUY));

  message.set(new Text("Cancel My Order!"));

  Session.sendToTarget(message, "TW", "TARGET");
}
```
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.
Or even better, a unit test or reproducer.

**Expected behavior**
A clear and concise description of what you expected to happen.

**system information:**
 - OS: [e.g. Linux]
 - Java version [e.g. JDK8]
 - QFJ Version [e.g. 2.1.1]

**Additional context**
Add any other context about the problem here.
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<title>QuickFIX License</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<h1 id="title">QuickFIX License</h1>
<p> <font face="Courier New, Courier, mono">The <a href="http://quickfix.sourceforge.net">QuickFIX</a> Software License,
  Version 1.0</font></p>
<p><font face="Courier New, Courier, mono"> Copyright (c) 2001-2008 quickfixengine.org All rights reserved.</font></p>
<p><font face="Courier New, Courier, mono"> Redistribution and use in source and binary forms, with or without modification,
  are permitted provided that the following conditions are met:</font></p>
<ol>
  <li><font face="Courier New, Courier, mono"> Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.</font></li>
  <li><font face="Courier New, Courier, mono"> Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.</font></li>
  <li><font face="Courier New, Courier, mono"> The end-user documentation included
      with the redistribution, if any, must include the following acknowledgment: "This
      product includes software developed by quickfixengine.org <a href="http://www.quickfixengine.org/">http://www.quickfixengine.org/</a>".
    Alternately, this acknowledgment may appear in the software itself, if and
    wherever such third-party acknowledgments normally appear.</font></li>
  <li><font face="Courier New, Courier, mono"> The names "QuickFIX" and "quickfixengine.org" must
      not be used to endorse or promote products derived from this software without
      prior written permission.
    For written permission, please contact quickfix-users@lists.sourceforge.net.</font></li>
  <li><font face="Courier New, Courier, mono"> Products derived from this software
      may not be called "QuickFIX", nor
    may "QuickFIX" appear in their name, without prior written permission of
    quickfixengine.org</font></li>
</ol>
<p><font face="Courier New, Courier, mono"> THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED WARRANTIES,
  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL QUICKFIXENGINE.ORG
  OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
  OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
  WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
  SUCH DAMAGE.</font></p>
  <div class="footer">More information at <a href="http://www.quickfixj.org/">www.quickfixj.org</a></div>

</body>
</html>
The formatter.xml file can be imported into Eclipse and
implements the QuickFIX/J formatting guidelines.
