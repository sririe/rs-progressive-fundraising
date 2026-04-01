---
title: "Lloyd Knowledge Transfer — Session 1 Transcript: Digital Fulfillment Walkthrough"
type: discovery
category: meeting-transcript
date: 2026-03-27
status: complete
format: transcript
duration: "~1h 8m"
participants:
  progressive:
    - Lloyd S. (Technical Contractor) — Speaker 2
    - Doug B. (Owner) — Speaker 3
    - Mario (Digital card operator) — Speaker 6
    - Danny (Director of Operations) — Speaker 5
  redstamp:
    - Spencer R. — "You"
    - Tim L. — Speaker 1
speaker_key:
  "Speaker 1": Tim L.
  "Speaker 2": Lloyd S.
  "Speaker 3": Doug B.
  "Speaker 5": Danny
  "Speaker 6": Mario
  "You": Spencer R.
  "system Unknown": unidentified / crosstalk
tags: [knowledge-transfer, lloyd-handoff, digital-fulfillment, card-generation, transcript, esso, amazon, loblaws, walmart, systemone, inventory-management, blackhawk-api]
related:
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
---

[0:00] Speaker 2: It's going to be on my desktop, yeah.
[0:02] Speaker 1: Okay, so if you minimize the Google Meet, then you'll be able to access your your desktop and we'll be able to see everything.
[0:07] Speaker 1: So that's perfect.
[0:08] Speaker 1: So we can see everything now.
[0:10] Speaker 2: All right, done.
[0:11] Speaker 2: All right. Upgrades to everything.
[0:14] Speaker 2: Okay, so you sent me an invoice.
[0:19] Speaker 3: Yeah, it's uh, and it's invoice number 55.
[0:23] Speaker 3: It's one of our maté groups.
[0:26] Speaker 3: They got a bunch of different stuff on it.
[0:28] Speaker 2: And you see what I'm doing now?
[0:31] Speaker 2: Yep. Oh yeah.
[0:33] Speaker 2: Okay, good.
[0:34] Speaker 2: Okay.
[0:34] Speaker 2: So, um, Here's, Sarah.
[0:38] Speaker 3: You must know the ones who every week.
[0:41] Speaker 2: Basically, the process starts with, uh, uh, receiving, uh, a digital order.
[0:48] Speaker 2: So that would come in the form of a, uh, invoice.
[0:51] Speaker 2: So basically, uh, we just download this to, uh, Saying the princess.
[0:58] Speaker 3: Okay, I was here.
[1:00] Speaker 2: Okay, now.
[1:04] Speaker 2: Do it, I've got my things set up, browse each other for invoices to go into my, uh, downloads folder.
[1:15] Speaker 2: That's the one there, duck, CP 114-4055?
[1:20] Speaker 3: Yes, yes.
[1:21] Speaker 3: And well, I just want to warn you on one thing.
[1:25] Speaker 3: There a whole bunch of Amazon cards with one here, one here, one here.
[1:29] Speaker 3: So, you know, as an example, they've ordered 5 100s, but they've got one, one, one, and 2 sort of.
[1:39] Speaker 3: So whatever, whatever you are, whatever you do here with explaining everything, Mario will just take it over and finish it off if, you know, so you don't have to go through this whole process of all these items sort of thing, right?
[1:51] Speaker 3: So wherever you want to leave off, Mario will take it from there, sort of thing.
[1:55] Speaker 2: Anyways, so we download the invoice, and so basically, um, uh, written a program to read the invoice and generate all the, uh, the files for the different, uh, cards that we can, uh, um, that will send to the, uh, the customer. Um, so I'll just go to the folder there.
[2:18] Speaker 2: As I said in the email, everything is stored on my, uh, My Google Drive that, that, uh, both Doug and, and Mario have access to.
[2:27] Speaker 2: So that's how Mario.
[2:28] Speaker 1: It looks like we lost.
[2:35] You: Yeah. Yeah.
[2:36] Speaker 1: Can you still hear Liz Spencer?
[2:37] system Unknown: Okay.
[2:38] You: Well, I don't think you've seen anything.
[2:40] You: No, we can.
[2:41] system Unknown: You can't hear me?
[2:43] system Unknown: Oh, no, I can.
[2:44] system Unknown: Okay.
[2:46] system Unknown: Oh, Lord.
[2:56] Speaker 3: See all this stuff popping up in those code stuff.
[3:01] Speaker 3: Yeah, but I don't know.
[3:04] Speaker 2: Yeah. Yeah, just fill out.
[3:09] system Unknown: Just fall in the process.
[3:11] Speaker 2: Okay, so all the, uh, scripts that are used are in this folder. So the 1st thing we're gonna do is, uh, uh, read the invoice and basically generate a bunch of, uh, Wow, this feels like now, I haven't done this for a while, man.
[3:30] Speaker 2: I'm like, Okay, uh, let's see.
[3:33] Speaker 2: place it on.
[3:34] system Unknown: Like, hopefully.
[3:35] Speaker 2: No, no, I mean, I know what to do.
[3:39] Speaker 2: It's usually, I just, I just recall commands them, I think, so, uh, no, I'll just have to do it, uh, old school and and re, uh, it feels good.
[3:48] Speaker 2: I've got it.
[3:50] You: Yeah. Yeah.
[3:51] Speaker 2: Okay.
[3:52] Speaker 2: So that's the script.
[3:54] Speaker 2: So I basically sent you basically these steps here.
[3:57] Speaker 2: So this is the run, so it's just a Python program.
[4:01] Speaker 2: It's going to bring up a dialogue and we're going to load the invoice into that.
[4:05] system Unknown: Okay, yeah, yes, yes, yes.
[4:10] Speaker 2: So again, that will read the invoice and generate a bunch of folders.
[4:19] Speaker 2: You see a bunch of stuff.
[4:20] Speaker 2: Go by on the screen here.
[4:20] You: Okay.
[4:22] Speaker 2: Since I haven't run this for a while, it's got to load all the different tools that, that, uh, uses.
[4:30] Speaker 2: So, you know, complain for a bit and then it'll go through what it needs to do.
[4:34] Speaker 2: Well, this is built with stuff that's just freely available on the internet, so there's nothing.
[4:38] You: Yeah, open source.
[4:42] You: It looks like.
[4:43] system Unknown: Yeah.
[4:56] Speaker 2: So once that's done, so, uh, uh, underneath this, uh, longer structure in my account here, there's an order folder, so that would have generated, uh, a bunch of, uh, things for each of the cards in the oldest order, orders folder.
[5:14] Speaker 2: Um, Hang on there.
[5:20] Speaker 2: Let me just load the invoice.
[5:21] Speaker 2: Well, I can see what's, um, settling here, just about that.
[5:27] Speaker 2: Amazon, blah, blah, Esso.
[5:33] Speaker 2: Well, so they did it in multiple kind of...
[5:36] Speaker 3: Yeah, I don't know why they did it that way, but, um, okay, so anyway, so Amazon, Loblaws, and Hassle.
[5:42] Speaker 2: So for Amazon, we generate those cards, so that will go through one program.
[5:46] Speaker 2: If you can kind of see on the top left hand corner here.
[5:49] Speaker 2: So these are the generation programs.
[5:50] Speaker 2: So Mario must have those on his desktop too.
[5:52] Speaker 2: So we'll be running that.
[5:54] Speaker 2: We'll, we'll be running, wants the Loblaws, and we'll be running one for for SO.
[5:58] Speaker 2: So, um, let's go to, uh, so the next step basically is to what, what that program did was create folders with, with, uh, so we'll go to the 1st one here.
[6:09] Speaker 2: Let's go to Esso.
[6:10] system Unknown: Okay.
[6:13] Speaker 2: So, uh, generated this folder here, which basically has the invoice number plus just a tag, which basically is the, the time at which it generated that's older.
[6:17] You: Got it.
[6:23] Speaker 2: Okay, so when we're finished this process, we'll get rid of that and you'll just see folders like, like here with no timestamp, but basically, so that allows me to run this many times and for whatever reason, it'll just keep different copies and you can get rid of or keep whichever ones you want.
[6:39] Speaker 2: Um, so we'll go in here and there should be an Excel file.
[6:44] Speaker 2: Um, so, ones that we just get inventory from, so Doug orders cards and then we keep inventory in the SO folder, um, and we're not going to generate these SO cards.
[6:55] Speaker 2: We're just going to copy earls that they provided us and then load them into, to this, this file here and then we're going to save them and add an encryption pass, add a possible to that file.
[7:06] Speaker 1: Okay, quick question in terms of logistics of that.
[7:09] Speaker 1: That would be something, if I'm not mistaken, that you would go and pre-buy digitally from, in this case, SO.
[7:15] Speaker 1: Yes. And then you would have it in your inventory.
[7:17] Speaker 1: Yes.
[7:18] Speaker 1: Okay.
[7:18] Speaker 3: So this is just the retrieval process of those.
[7:21] Speaker 3: Except for Walmart, which we generate ourselves.
[7:23] Speaker 3: Okay.
[7:24] Speaker 2: Uh, well, you still have to buy them, but anyway, so all the persons are saying is just that what we do after.
[7:31] Speaker 2: Okay?
[7:32] Speaker 2: So, um, so we also have folders for, uh, with inventory.
[7:38] Speaker 2: We have, uh, Esso cards and inventory that we can, that we can use.
[7:43] Speaker 2: So we would go to our inventory folder here.
[7:46] Speaker 2: And then find that. So.
[7:50] Speaker 2: Sorry.
[7:53] Speaker 2: See, this is how long I haven't done it.
[7:55] Speaker 2: We would go to the orators, and under orders, there'd be an inventory folder.
[7:59] Speaker 2: And uh, we'd use, we'd cut.
[8:03] Speaker 2: So, and then inventory.
[8:06] Speaker 2: And there'll be inventory folder there.
[8:11] Speaker 2: The other folder I went to, initially, it was basically if we're don't have any inventory here for the different denominations they need, then we'd go, we had a process where we'd copy them there and then they'd get added into this location later.
[8:24] Speaker 2: Okay, so uh, let's open up this file here.
[8:27] Speaker 2: So can I jump in with another question?
[8:30] Speaker 1: Is that okay?
[8:31] Speaker 1: So in that in that situation where, um, you might not, like, do you always have inventory ready, readily available, or is there potentially a circumstance where maybe a large order comes in, depletes your stock, and then you're in a situation where you need to replenish your inventory?
[8:46] Speaker 1: Does that happen often?
[8:48] Speaker 3: Yeah, yeah, we would replenish before we go through this process though.
[8:51] Speaker 3: Okay.
[8:51] Speaker 3: Like, so if we, if we don't have enough, we would, we would order it, get it there before we go through this process.
[8:58] Speaker 3: Okay. Right?
[8:59] Speaker 2: Yeah. So in the old days, I think we used to have lots of inventory.
[9:03] Speaker 2: So basically when an order came in, I received it and I would be able to just go and do it, but so now it's kind of more order just in time processing.
[9:07] You: And is that, is that triggered, I guess, Doug, like, when a new order comes in that, that you've got in front of you?
[9:12] Speaker 2: Like the Japanese, uh, do.
[9:14] Speaker 2: Yeah, okay.
[9:16] Speaker 2: So uh,
[9:26] You: And I guess, I'm curious what the trigger is and who the person is that makes that determination, oh, we just got a big order in.
[9:35] You: I don't think we have enough.
[9:35] Speaker 3: I would be responsible for that, but Mario has now learnt to do that.
[9:37] You: And then who goes and checks?
[9:44] Speaker 3: So that's what we call, you know, ordering our inventory, right?
[9:45] You: Yeah.
[9:47] Speaker 3: And basically what we're doing is we're tracking from a year ago because our sales are almost identical from what they were a year ago.
[9:53] You: Right.
[9:54] Speaker 3: In general terms.
[9:56] Speaker 3: So we're tracking and sometimes we we move out like a 2 week time span.
[10:02] Speaker 3: Sometimes it's a whole month ahead, right? For grocery, we would never go a month out because we sell too much of the stuff.
[10:07] Speaker 3: Right?
[10:08] Speaker 3: So we're just every day, Mario or I are checking a year ago to see what we might need and we're ordering every day.
[10:17] Speaker 3: But obviously, we're going to get large orders that are unanticipated, and then we have to order in, get it in before we'll even, you know, let Lloyd know that the invoice is paid sort of thing.
[10:21] You: Yeah. Got it.
[10:29] You: Okay.
[10:29] Speaker 2: So, yeah, so the trigger is the payment of an invoice.
[10:35] Speaker 2: So they're not getting their cards until they pay.
[10:37] Speaker 2: Yeah. And here we have uh, 201, 250.
[10:42] You: Daddy? What?
[10:47] Speaker 2: Okay, so we just go to, uh, these uh, inventory files that have, uh, will tell you what's stored inside of them.
[10:52] You: Okay, you'll have to use the TV.
[10:53] You: I'm on a phone call.
[10:54] You: No. I don't want to. I'm just sure.
[10:54] Speaker 2: So, uh,
[10:56] Speaker 2: But it's where, if we're lucky, we have everything we need in this one style.
[11:05] Speaker 2: Okay.
[11:09] Speaker 2: So 200's there.
[11:12] Speaker 2: So we would copy the, um, The invoice number and the, uh, Yeah.
[11:21] Speaker 2: That's for inventory, we mark that it's been removed from there, so. It's gonna.
[11:33] Speaker 3: It's a pretty manual.
[11:39] Speaker 3: Yes, yeah.
[11:39] Speaker 2: Okay, so there's 200s that we're going to grab, so just...
[12:00] Speaker 2: Hey, that the order was made, that's on the slide of 20260310.
[12:08] Speaker 2: So we'll add that in there as well.
[12:21] Speaker 2: These guys. Did they change their, uh, do they have multiple customer number, these guys, maybe nation of Alberta?
[12:33] Speaker 3: Yeah, yeah.
[12:35] Speaker 3: And the other, the other thing too, Lloyd, if you're, if you want to do like the Amazon different denominations, we can tell you how many are, uh, you know, how many they ordered rather than you having to look up and down that whole invoice, right?
[12:47] Speaker 3: All that information is in the slough, right?
[12:51] system Unknown: Any order?
[12:55] Speaker 3: That's what this is?
[12:56] Speaker 2: The PDF?
[12:57] Speaker 3: You mean on, in what, which files or, or you mean the invoice or?
[13:03] Speaker 2: What tells you here?
[13:05] Speaker 2: Like, we know that they'd ordered 2 SO and 100s and one.
[13:09] Speaker 2: Yeah, yeah, yeah, so I don't have to look in the voice.
[13:11] Speaker 2: I just need to get information to put in here.
[13:13] system Unknown: Okay.
[13:14] Speaker 2: We have a convention as, uh, of not having this guy, uh, we just alternate the color, so it's easy to look in the file and see what was was ordered.
[13:27] You: Right.
[13:28] Speaker 2: Yeah, so...
[13:30] Speaker 2: So we got 2 of those guys.
[13:35] Speaker 2: And here's the information that we need to transfer into the, uh, into the, uh,
[13:42] system Unknown: Hundreds.
[13:44] Speaker 2: And this is what the customer is, uh, gonna get.
[13:55] Speaker 2: And then, apparently, uh, a date of when these cards were activated.
[14:03] You: Yeah. Right.
[14:04] Speaker 2: Okay, so basically we're just transferring information.
[14:10] Speaker 2: And then we need one, 250.
[14:11] You: And and this being sort of a fairly manual, you know, select and edit is is kind of a process that could be somewhat brittle if mistakes are made.
[14:13] system Unknown: Sorry?
[14:14] system Unknown: Correct.
[14:24] You: And is that common that that ever happens?
[14:25] Speaker 2: I would say no, not really. No, it's not, but no, but yeah.
[14:33] Speaker 2: Well, we just, I think it's because we have good people doing it, right?
[14:33] You: Yeah.
[14:33] You: Yeah Yeah.
[14:37] Speaker 3: So if you if you went down the path and we were selling more and more cards, we have multiple people doing it, there would be more mistakes.
[14:44] You: Yeah.
[14:44] Speaker 3: It's just a lawyer is on top of it and he's trained Mario well to be on top of it.
[14:46] You: Yeah, and I assume it, it also uh, means having to go a bit slower, just, just knowing that you don't want mistakes.
[14:50] Speaker 3: So.
[14:59] You: Um, so, but yeah, okay.
[15:03] system Unknown: Yeah, no.
[15:05] Speaker 2: Yeah, yeah, so I think I mentioned the thing, is there's a, if we come up with a, a standard format, like, so if we just kept a, I don't know if it would be one growing.
[15:17] Speaker 2: Anyway, some procedure for just having the inventory, uh, whether it's full or not, in a, in a standard, uh, configuration, then it could easily write the program to go into the inventory file, grab, grab those things, and once the program has been tested, then that could eliminate those types of errors altogether, yeah.
[15:35] You: Yeah.
[15:37] Speaker 2: Like, Right now it's man.
[15:38] You: Okay.
[15:41] Speaker 2: Okay, and uh, so 250, we'll grab this guy here.
[16:11] Speaker 2: That's all we need for this file.
[16:13] Speaker 2: So we're gonna save that, but then we, uh, need to.
[16:23] system Unknown: Hmm.
[16:30] Speaker 2: Sure, America's processes, but I leave the cursor in the last nice, uh,
[16:51] Speaker 2: Okay.
[16:54] Speaker 2: Okay, looks... So that is...
[16:58] Speaker 2: Hey.
[17:04] Speaker 2: Oops.
[17:06] Speaker 2: All right, so this guy is good.
[17:11] Speaker 2: We just save it now.
[17:12] Speaker 2: Uh, so we'll save.
[17:14] Speaker 2: And then we're gonna add an encryption password.
[17:16] Speaker 1: And in this situation, like, is this a file that's shared across that you'll have access to as well?
[17:23] Speaker 1: Yes, I can just access the Google Drive and it will be there.
[17:28] system Unknown: perfect.
[17:33] You: And then when it comes to adding passwords here, is there a consistent password that gets used or how are you deciding what to use for this?
[17:40] system Unknown: There's in the end list.
[17:47] Speaker 2: It's all the cheese guys, of course.
[17:49] You: Okay.
[17:50] Speaker 2: These guys without the dash.
[17:51] You: Okay.
[17:54] Speaker 2: Yeah, it's out to look, you know, letters.
[18:01] Speaker 3: No letters, no letters, no dashes.
[18:02] Speaker 3: Okay.
[18:03] Speaker 2: Okay.
[18:07] Speaker 2: I mean, could be anything.
[18:09] Speaker 2: We just have to tell the customer what, what it is and we usually just describe what the, you know, the password is.
[18:14] Speaker 2: And that doesn't doesn't change.
[18:16] Speaker 2: Okay.
[18:18] Speaker 2: Um.
[18:19] Speaker 2: Tell me, so I didn't.
[18:25] Speaker 2: okay?
[18:25] Speaker 2: So that would be that guy's done.
[18:27] Speaker 2: And that's so these types of ones, there's nothing else to be done.
[18:32] Speaker 2: So I basically just go here.
[18:34] Speaker 2: And uh, remove the uh,
[18:43] Speaker 2: So now Amazon.
[18:48] Speaker 2: Which is starting now.
[18:50] system Unknown: Okay.
[18:51] Speaker 1: Spencer, are there any more behind the scenes technical questions that you had in mind and talked to Lloyd about specifically?
[18:54] You: Um...
[19:02] You: I guess one, yeah, a few questions.
[19:08] You: Um, Because it seems like we'll likely be able to get more of this walkthrough, like the tactical stuff with Mario.
[19:18] system Unknown: Yeah.
[19:18] You: Um, So I'm curious, when it comes to the actual sort of scripts and programs, is there anything that needs to be done?
[19:31] You: You know, I saw, you know, Python being involved, Apache, is there any sort of, um, Like, Vert, you know, version control that needs to happen with those scripts as far as if Python releases a new update that ends up being installed on the machine that's running the scripts.
[19:52] You: Does that, you know, impact any of the scripts that you've run?
[20:01] Speaker 2: Um, I imagine it would, but There's no, unless there's something, a new feature that's required by, for down.
[20:08] Speaker 2: I don't, there's no auto download as the latest version of Python.
[20:11] You: Okay.
[20:11] Speaker 2: Yeah. Oh, it's not, it's not happened, and there must have been, uh, like in the generation of these scripts, then that was,
[20:12] You: Um.
[20:23] Speaker 2: None that would have been tested, it would have been stored on this, uh, on this, uh, on that shoulder there.
[20:30] Speaker 2: So we're not using like git or any version control.
[20:33] Speaker 2: So there are other versions of the, of the, of the files being stored, but so for instance, if I had to make a change because something was broken, then I would, I would, um, attach that.
[20:47] Speaker 2: So any work that I'm doing for Doug, I have to put, I'm putting into a calendar, like a Google calendar, so which he has access to.
[20:49] You: Yeah. Yeah.
[20:54] Speaker 2: And anything that I did is noted there.
[20:57] Speaker 2: And then I would have copied the version of the script that got updated with that last, whether the work I did for, for Doug. So there's different copies in it.
[21:00] You: Okay.
[21:06] Speaker 2: so he could go back in the calendar as long as Google doesn't move.
[21:10] Speaker 2: It's disk drive and get any, any previous versions of stuff, but yeah, so that's, yeah, I'm not, I'm the only person doing any development or doing anything, so, in terms of, uh, you know, so it's, it's not like a multi user development environment for, at least for this source stuff.
[21:10] You: Yeah. Yeah.
[21:14] You: Okay.
[21:24] You: Got it.
[21:26] Speaker 2: So this lesson.
[21:27] Speaker 1: Are there situations where Mario, like, tries to go and run something and then all of a sudden, not something broken, it doesn't generate?
[21:35] Speaker 1: Like, have you experienced any errors?
[21:37] Speaker 2: Yeah, yes.
[21:38] Speaker 2: So, so when we went to, um, so, up until, like, this year, I always did this and, you know, we, we purchased a laptop and all the development was done from this laptop, all the generation of cards was done from this laptop.
[21:50] You: Roan, what is it?
[21:53] Speaker 2: Then when I installed the different software that had to be installed on Mario's computer.
[21:55] You: What's that?
[22:01] Speaker 2: The scripts are common, but there were issues with things not running.
[22:06] Speaker 2: So I guess it was probably related to, then I had to install a latest version of Python on Mario's computer.
[22:13] Speaker 2: So I'd never have any problems on my computer, but if I would run, it wouldn't run.
[22:16] Speaker 2: So then I'd have to go debug, find out what happened, update the scripts, and then, and then republish it there.
[22:22] Speaker 2: So, as far as I know.
[22:24] Speaker 2: So there are some things like, uh, uh, lines and python that when run on Mario, those things generate some kind of, output to the console, but it still generates the, the, produces the file.
[22:36] Speaker 2: So, uh, and Mario lets me know when, uh, For instance, things.
[22:39] You: Okay. Okay.
[22:41] Speaker 2: I think he's worked around some things, but I think he lets me know when, like, he's just, if it doesn't work at all, you know, doesn't generate the scripts as an expense.
[22:50] You: And when that happens, does it post, like, any sort of error message or log to the console?
[22:55] Speaker 2: Oh, anything like, well, for this one, if, uh, Um, you know, so for instance, a lot of things that happened was, uh, uh, we read the, uh, the, uh, invoice, and you can see on this screen here, it's put in the, it's populated the customer here.
[23:15] Speaker 2: Um, so when Mario ran it, there were instances where it wouldn't populate the customer in these these flaws here.
[23:17] You: You're going to have to figure out something else to do.
[23:25] Speaker 2: And so, He would know that.
[23:29] Speaker 2: So I guess if he saw that, he would say, oh, there's no customer and he would.
[23:29] You: I can do it.
[23:30] You: right now.
[23:30] You: I'm sorry I'm on a call.
[23:33] Speaker 2: Type it in manually.
[23:36] Speaker 2: So, it would, you know, and when these scripts are run, it's gener- I just generate, you know, so for me, you know, I don't care.
[23:44] Speaker 2: I put everything that's happening on screen.
[23:46] Speaker 2: So this is all stuff that nobody cares about, but it's basically I can go through this and read, okay, identified, you know, all these things.
[23:52] Speaker 2: So if something does happen, I can go back here and say, why didn't that?
[23:56] Speaker 2: So there have been instances where invoices have had weird formats or whatever.
[24:01] Speaker 2: The, uh, different people running, running on different computers.
[24:01] You: Right.
[24:05] Speaker 2: They, it runs on computer X, they generate, the invoice was created on one computer, and the output of that invoice behave differently than the output of an invoice created on a different computer in Doug's office.
[24:12] You: Yeah. What?
[24:18] Speaker 2: So the run into lots of those types of things where we've had to
[24:21] You: That was nice.
[24:22] Speaker 2: I've had to go in and figure out, well, why is it work?
[24:24] Speaker 2: when they generate on this one and just put it around.
[24:27] Speaker 2: So I've, over time, fixed it so that it trying to eliminate all the different inconsistencies on the on what's happening on the, on the, the different computers.
[24:37] Speaker 2: But yeah, so there's output here, so if you're reading the output, you should be able to see whatever's put here should end up exactly in the file, is that's not working?
[24:42] You: Got it.
[24:46] Speaker 2: You would, you would see an air or if something actually broke, it would, the program would crash and you would see it here and we'd be able to figure out.
[24:52] You: Yeah. Um, Yeah.
[24:55] Speaker 2: So if I was doing it, I'd just be, I'd go and debug and figure it out and then run it again.
[24:59] Speaker 2: makes sense.
[25:00] Speaker 2: You'd have to, but you'd have to know this, you know, these things.
[25:06] Speaker 2: So what would happen if, uh, if the, if, uh, you also then, if this didn't for the customer name in here, and then we went to run one of the generation programs, then, uh, um, it would, it would complain that there's no customer in the thing, so then he would say, he's what he's done.
[25:25] Speaker 2: Oh, it didn't, this isn't running, and then it was because there was no customer there.
[25:29] Speaker 2: So we've identified that issue and solved that.
[25:31] Speaker 2: This type of invoice where we don't do generation, then there'd be no damages.
[25:38] Speaker 2: information is not put here.
[25:39] Speaker 2: And for these ones, we don't put the customer name in those files that are generated, so it wouldn't really, it's more when we run our program to to create.
[25:50] Speaker 2: Is that screw up here, what, what, uh, affect the output?
[25:56] Speaker 2: But. The Amazon, so that's, well, uh, the process is slightly different there, but, uh, um, so you see, just do the 10th.
[26:10] Speaker 3: Why don't you just do the one $10 one, Lloyd, that you don't have to go through all the different denominations or whatever?
[26:15] You: What is going on?
[26:15] Speaker 2: Does that work? or are you just... I can do, I can, I can do log laws.
[26:18] You: Come here.
[26:18] You: Come here. Neither.
[26:22] Speaker 2: It less cars, I don't care.
[26:23] Speaker 2: What is that?
[26:24] Speaker 3: Whatever, whatever you need to show them what you want to show them.
[26:25] You: Yeah, I had a home road.
[26:27] You: I am on a phone call.
[26:27] Speaker 3: So, you...
[26:28] Speaker 2: Well, maybe, well.
[26:29] Speaker 2: Okay, let's go through.
[26:30] You: Do not...
[26:31] Speaker 2: let's go through the avilad, because it, yeah, I think, uh, the blah blah, depends on whether we'll do generation, depends on whether we're using old inventory or new inventory because now they're giving us cards that we don't generate, right?
[26:45] Speaker 1: Right, right, right.
[26:46] Speaker 1: Okay.
[26:46] Speaker 2: So let's go here.
[26:47] Speaker 1: So does that mean the procurement process is different or it's changed?
[26:50] Speaker 3: No, basically what was happening is there was a field that I thought it was mandatory to fill in when we were ordered and it had from progressive or whatever.
[26:59] Speaker 3: And then Lloyd had to leave that out because it was going to a client.
[27:03] Speaker 3: didn't want to say the card was from aggressive.
[27:05] Speaker 3: So then we figured out that it wasn't a mandatory field.
[27:08] Speaker 3: So now that's no longer there.
[27:09] Speaker 3: But some of that old stock, Lloyd, has to, or Mario has to delete things, infection it off before they can send it off.
[27:15] Speaker 2: Okay, so let's do uh, let's do this guy.
[27:31] Speaker 3: So, Lloyd, what I, what I did on this invoice is I, I, I, no, it doesn't, it doesn't matter.
[27:37] Speaker 2: You don't have to, but it's just funny, because usually, I'm thinking that, uh,
[27:43] Speaker 2: Yeah, it just does it in the order of that we we get it, like if they were all done together, then it would produce them.
[27:50] Speaker 2: it doesn't matter.
[27:51] Speaker 2: This, this, this, this will be fine.
[27:54] Speaker 2: So let's go to the inventory for, uh, for, um, uh, This only one voice I've ever seen or someone does that.
[28:02] Speaker 3: you should go.
[28:02] Speaker 3: We need to.
[28:03] Speaker 2: And do we have everything for Amazon here?
[28:05] Speaker 2: There's inventory, Amazon.
[28:06] Speaker 2: Okay, good.
[28:07] Speaker 2: And so we look at this quickly, we need 25s, 50s, 100s, and 250s.
[28:14] Speaker 2: Okay, let's start 20 times.
[28:16] Speaker 2: And 10...
[28:17] Speaker 2: You need one. 10?
[28:19] system Unknown: Yeah.
[28:19] Speaker 2: Okay, let's do here.
[28:21] Speaker 2: This has the most guys on it, and then who goes to 250 at the end.
[28:25] Speaker 2: Are there any toilet slides in here?
[28:25] You: do anything!
[28:29] Speaker 2: Yes.
[28:29] Speaker 2: Okay, see, help them with, so one.
[28:34] Speaker 2: Two 25.
[28:37] Speaker 2: Yeah, I'll just speak out loud and then you can tell me...
[28:42] Speaker 2: So 225, so let's grab that guy.
[28:46] Speaker 2: Where are you interested one here?
[28:49] Speaker 2: I'm gonna change the color of this guy.
[28:51] Speaker 2: Oh, I'll just leave it like that for now, I'm gonna copy this.
[28:54] Speaker 3: And indeed, ever of our coming.
[28:56] Speaker 3: I never seen an order like that.
[28:57] Speaker 3: Oh, sweet just the hardest work.
[28:59] system Unknown: There.
[29:00] Speaker 2: It doesn't matter.
[29:02] Speaker 2: So 225, is that what you said?
[29:04] Speaker 1: That's a good call, though.
[29:05] Speaker 1: actually good to see.
[29:06] Speaker 1: Yeah.
[29:08] system Unknown: Okay.
[29:08] system Unknown: Usual one.
[29:16] Speaker 2: So 225s?
[29:19] Speaker 3: So canny, this is not typical, I think.
[29:23] Speaker 3: Merch is good.
[29:25] Speaker 3: busy time for us, right?
[29:26] Speaker 2: Yeah. So, how many uh, 60s?
[29:28] Speaker 2: 250s.
[29:30] Speaker 3: 5 and 10, right?
[29:32] Speaker 3: This one what?
[29:33] Speaker 3: This is a good size one.
[29:35] Speaker 3: This is our most hassle order because this is a different, it doesn't matter that much, but they always order a whole bunch of different denominations.
[29:42] Speaker 3: to do this, this client?
[29:45] Speaker 3: And every time you see me, oh, come on.
[29:47] Speaker 3: That's right.
[29:48] Speaker 3: So that's, you know, everybody, like, usually another one that's integrated.
[29:54] Speaker 2: Okay, 250s.
[29:57] Speaker 2: 250.
[29:59] system Unknown: Yeah.
[29:59] system Unknown: Okay.
[30:00] system Unknown: Nice.
[30:02] Speaker 2: That's right, and my lunch is out.
[30:06] Speaker 2: How many hundreds?
[30:07] Speaker 3: Uh, 5100. 5100.
[30:11] Speaker 2: Oh, it's probably gonna make me copy it again.
[30:13] Speaker 2: Okay.
[30:13] Speaker 2: You understand how it works.
[30:15] Speaker 2: Okay, 5100s. Hopefully we're flying nice.
[30:19] Speaker 2: Okay?
[30:27] Speaker 2: And I think that's it for this file, right?
[30:29] Speaker 6: Oh, yeah, there's true 250s as well.
[30:32] Speaker 2: I'm not sure if those are in this peltic those are in as well.
[30:36] Speaker 2: So, uh,
[30:37] Speaker 3: So that's more, this is one of our regular sort of digital people that were once a month, and this is a, oh, there's 10s here too.
[30:46] Speaker 2: Okay.
[30:47] Speaker 2: So, uh, You're probably wondering why I did this, Mario.
[30:51] Speaker 2: So this is the reason.
[30:52] Speaker 2: So I, uh, whenever I create these files, I just freeze the top, uh, column there so that when we're scrolling up, I can see what the column things are and what the, what is this?
[31:03] Speaker 2: Freeze pains, and then we freeze the top rope.
[31:07] Speaker 2: That way when we're scrolling, then it keeps in, I can see what what's in there.
[31:11] Speaker 2: Okay, so we did 2550s and hundreds, right?
[31:14] system Unknown: Yeah.
[31:14] Speaker 2: Okay, perfect.
[31:16] Speaker 2: So there's no more.
[31:16] Speaker 2: there's no tension this fun.
[31:18] Speaker 2: So when, uh, when I do that, I would move tans off of the, uh, which maybe you did.
[31:25] Speaker 2: I didn't, I couldn't remember.
[31:26] Speaker 2: Also, the file name so that, uh, You don't have to go into that files.
[31:33] Speaker 2: no tens.
[31:34] Speaker 2: Okay, 25s.
[31:35] Speaker 2: All right.
[31:36] Speaker 2: So we need to grab these guys.
[31:39] Speaker 3: So the 250s there's done in that file he has to go get any other time?
[31:45] Speaker 6: No, it's 25 cities in America.
[31:47] Speaker 3: Oh, totally.
[31:48] Speaker 3: Right.
[31:48] Speaker 2: So one at a time because uh, so this is, this is more complicated than the usual.
[31:53] Speaker 2: Okay, so 125 here.
[31:55] Speaker 2: Someone at a time.
[32:00] Speaker 3: Amazonia a few, but I'm kind.
[32:01] Speaker 6: You have.
[32:02] Speaker 6: Yeah, you have to do like one denomination at a time.
[32:05] Speaker 6: So like you copied the 21st and then... 25 here?
[32:09] Speaker 3: Sorry?
[32:09] Speaker 2: Yeah. Yeah.
[32:11] Speaker 2: So this is this is likely introducing potential for more errors.
[32:15] Speaker 2: 125 here?
[32:17] Speaker 2: Like the way that this file is.
[32:20] Speaker 2: Okay, and it's the other 25 here.
[32:26] Speaker 2: Nice, we have 4 people looking here, so. No pressure, Lloyd.
[32:33] Speaker 2: Well, you should be you should be reviewing my work.
[32:37] Speaker 2: Okay, so then 50s.
[32:38] Speaker 2: Okay, so those guys are done.
[32:39] Speaker 2: So we wouldn't do this.
[32:41] Speaker 2: Right?
[32:43] Speaker 2: Yeah, it's not great to have to sit here and watch this, but.
[32:47] Speaker 2: Okay, make sure he's doing it properly.
[32:50] system Unknown: Okay.
[32:52] Speaker 2: Now, the Sisties, okay.
[32:54] Speaker 2: 250s? Nope, okay.
[33:03] Speaker 2: So we grabbed this guy.
[33:12] system Unknown: Okay.
[33:18] Speaker 2: Okay. So then to the 50 man, that is it.
[33:30] Speaker 2: Just on there.
[33:31] Speaker 2: And
[33:37] Speaker 3: Let's do. Let's do Karen, right?
[33:42] Speaker 2: Perfect, and then 100s.
[33:51] Speaker 2: There's nothing nice to happen there.
[33:54] Speaker 2: Okay.
[33:54] Speaker 2: Then, uh, Hundreds.
[33:58] Speaker 2: So, oh, we're in 100s.
[34:03] Speaker 2: Okay.
[34:04] Speaker 2: Okay, so we have 2 together, one together, 2 together.
[34:09] Speaker 2: Perfect.
[34:09] Speaker 2: Hundreds, okay, so put on these two?
[34:20] Speaker 2: These two.
[34:30] Speaker 3: So... Oh, May tea or Alberta.
[34:33] Speaker 3: That's a previous order. They took a bunch of.
[34:36] Speaker 2: Oh, so then there's a 100?
[34:37] Speaker 3: Okay. So they they look okay.
[34:40] Speaker 3: Invoice to order this, this nomination for who, like on the, um, on the accent, she turns like, all the cars that we use, think like the previous one was native child, Toronto.
[34:55] Speaker 3: So we always keep track of it, which more than there's 2 where...
[35:00] system Unknown: Yeah.
[35:00] Speaker 3: And so basically yellow pairs, even though she's working on right now?
[35:07] Speaker 6: Yes, we just like... We just call our COVID?
[35:10] system Unknown: Yeah sure.
[35:11] Speaker 3: Yeah, I remember that from seeing this stuff before.
[35:14] Speaker 3: It does a different time, right?
[35:16] Speaker 3: each of us.
[35:18] Speaker 1: So while Lloyd's doing that part, um, When you deliver and to sell the order to the client, the, like the customer gets individual Excel spreadsheets based on the different, uh, merchants?
[35:34] Speaker 1: Okay.
[35:34] Speaker 5: And then they disseminate that to their customers, whatever they want to their their their own people that they're sending to.
[35:38] You: I'm on my phone call with my work.
[35:43] You: Is your iPad charge?
[35:44] Speaker 5: Okay.
[35:44] Speaker 3: For this one, there's, uh, one, two, three, 4 different options.
[35:50] You: Yeah. I'm gonna get you the other iPad, okay?
[35:50] Speaker 3: They'd get 4 different XL files.
[35:52] Speaker 3: Yes.
[35:52] system Unknown: Okay.
[35:53] Speaker 3: So I think it's called a zip point.
[35:56] You: I am.
[35:56] Speaker 3: X or zip file, depending on the term a bit.
[35:57] You: Why did you do that?
[35:59] You: Oh, yeah. Why?
[36:00] Speaker 3: Zip with CDM.
[36:01] You: Okay.
[36:07] Speaker 2: Okay, and now we need 250s.
[36:12] Speaker 2: And you said tens?
[36:14] system Unknown: 110.
[36:16] Speaker 2: Well, 110, there it is.
[36:17] Speaker 2: Wow.
[36:18] Speaker 2: They got everything lighter.
[36:21] Speaker 2: Oh, there's no more tans in here, right, Mario?
[36:23] Speaker 6: No, I think even there all of those for best life.
[36:27] Speaker 6: Yeah, yeah.
[36:28] Speaker 2: So, I would, so, uh, you, uh, I mean, it doesn't matter, so there's none of that, but, well.
[36:39] Speaker 2: Okay, so 250 and uh, Okay, no, it's going to the 250s.
[36:45] Speaker 3: To Danny, what is the, what do we call void styles in your files?
[36:50] Speaker 3: You know what I mean?
[36:51] Speaker 3: They got that backup and when it switches and stuff.
[36:53] Speaker 3: something important.
[36:55] Speaker 2: And 50 so.
[36:57] Speaker 2: So there's just one and 0 no, there's 2 250s, okay?
[37:00] Speaker 2: Okay.
[37:02] Speaker 2: Well, and this is an empty file.
[37:07] Speaker 2: Wow, beautiful.
[37:08] Speaker 2: Okay.
[37:09] Speaker 1: So that means no one, there's not, not anything we've ordered from that specific one.
[37:13] Speaker 3: Yeah, we basically just ordered them.
[37:16] Speaker 3: It is ago and they've not been... no client...
[37:20] Speaker 2: Sorry if I'm messing up your system there.
[37:22] Speaker 2: Mario.
[37:23] Speaker 2: Okay.
[37:24] Speaker 2: And these guys, because you may be able to use the difference all that I'm using now.
[37:28] Speaker 2: I mean, it doesn't matter, but...
[37:31] Speaker 2: Okay.
[37:33] Speaker 3: Mario's leaving us anyway, so it's okay.
[37:37] Speaker 3: It's fine.
[37:38] Speaker 2: Okay. So 250?
[37:40] Speaker 2: So we'll go the whole top guy here.
[37:42] Speaker 2: Goodness.
[37:43] Speaker 2: This guy.
[37:49] You: It just has coloring on it.
[37:50] Speaker 2: Yeah, okay.
[37:55] You: You have to plug in the other iPad if you want it.
[37:57] You: to watch a show.
[37:58] Speaker 2: Mm. People for you.
[38:04] You: Okay.
[38:10] Speaker 2: Perfect.
[38:20] Speaker 2: And then the same as 10.
[38:21] Speaker 2: All right.
[38:23] Speaker 2: Let you do it, you like that, right?
[38:26] Speaker 2: Oh yeah, it doesn't matter.
[38:26] system Unknown: Save.
[38:30] You: And what is that, 38 number represent on that inventory sheet?
[38:30] Speaker 2: That's another. How many, so how many cards are left in that phone?
[38:42] Speaker 2: Uh, 10.
[38:45] Speaker 2: It just counts down yet.
[38:47] Speaker 2: Okay, so, um, 10.
[38:52] Speaker 2: Same is 10.
[38:53] Speaker 2: Okay.
[38:53] Speaker 2: 33 left.
[38:56] Speaker 2: Okay.
[38:56] Speaker 2: Maybe too.
[38:57] Speaker 3: I sent it to Mario.
[38:59] Speaker 3: He puts it into a file.
[39:00] Speaker 3: So he'll, he'll...
[39:02] Speaker 3: Well, well, basically, whatever I'm getting is, let's say it's love those 250s.
[39:08] Speaker 3: Yeah, and let's say we've got, we noticed we're low and we have 250s, there are still left, but we only 10 more.
[39:14] Speaker 3: But those have not been used yet. So they, or area that's in the movies, that needs one of them.
[39:21] system Unknown: He'll take that one.
[39:22] Speaker 3: It won't even know that this file's there yet.
[39:25] Speaker 3: And then the next order, let's say, they need two.
[39:28] Speaker 3: So we only got one left.
[39:30] Speaker 3: And at that time, he takes this file and he moves it to this.
[39:34] Speaker 3: So can you explain this?
[39:36] Speaker 3: We, I call it your file in Lloyd's file, but can you explain from what, what, what the, that, that process is or what?
[39:43] Speaker 3: It's, like, race report, so what's something more cards you are? And then, um,
[39:49] Speaker 6: When, whenever the cards are ready, the merchant intros are let us know, we download it, and then I move that to, like, to the general inventory, which like, we call like my Mario's folder.
[40:02] Speaker 6: And then whenever we are filling an order and then we see we need more credit, we don't have enough, and then we go from there, prep from there, and then put on the, on the merchant's inventory individually as we.
[40:13] system Unknown: Okay.
[40:14] Speaker 3: So it's sort of like a whole new tech that's just there until we need to go to it and we go to it.
[40:18] Speaker 3: It's no different, man, for this.
[40:20] Speaker 3: Yeah. When we need to fill in order, we go and grab.
[40:22] Speaker 3: Yeah. Okay.
[40:25] Speaker 2: That looks good.
[40:27] Speaker 2: Okay, so we're finished with this guy.
[40:31] Speaker 2: Uh, so Amazon needs to be uh, so that's all Amazon gives us.
[40:35] Speaker 2: That's why we have to generate the cards.
[40:37] Speaker 2: They'll give us an Earl or anything.
[40:38] You: Okay
[40:39] Speaker 2: So, uh, We'd save that guy and then run this program up here in the top right, so they're all kind of listed.
[40:46] Speaker 2: Uh, And I think you can see.
[40:47] You: Yeah.
[40:49] Speaker 2: So you don't see this, I guess, you can see my whole desktop, right?
[40:52] Speaker 1: We can see the, like, the, the homemade's covering, but I can see the Amazon one, yeah.
[40:57] Speaker 2: Oh, this, okay, so, yeah, so there's just a list of all the, the, the ones there.
[41:03] Speaker 2: Okay.
[41:04] Speaker 2: So, uh, that's going to prompt for, uh, for excel soil.
[41:11] system Unknown: Same type.
[41:12] Speaker 2: Um, okay, so you go search for it on this, which is, uh, no, not there.
[41:20] system Unknown: Click it?
[41:22] Speaker 3: Is it open?
[41:23] Speaker 2: No.
[41:24] Speaker 2: Murders.
[41:25] Speaker 2: Oops.
[41:26] Speaker 2: You can't open Amazon.
[41:27] Speaker 2: I can't.
[41:28] Speaker 3: Oh, I see.
[41:29] system Unknown: I remember.
[41:30] Speaker 2: We're going to have to fix that.
[41:33] system Unknown: Don't do that.
[41:34] system Unknown: Okay?
[41:35] Speaker 2: So then we run that guy. It's gonna.
[41:47] Speaker 3: So it's just... What's in right now?
[41:53] Speaker 3: He's generating the above.
[41:55] Speaker 3: Or the Amazon.
[42:15] system Unknown: Okay.
[42:17] Speaker 2: So, uh, those files that got generated.
[42:30] Speaker 2: Of older hair is what's generated as a result of running an Amazon.
[42:40] Speaker 2: So any of these programs that we run on the white side there, we'll put the result in folder here.
[42:45] Speaker 2: So we copy this guy.
[42:46] Speaker 2: Is it in the, uh, in, uh, over here.
[42:56] Speaker 2: Mario, these guys, do they take, uh, do they want, uh, zip files or do they want, uh, URLs?
[43:06] Speaker 6: Let me check over here.
[43:09] Speaker 2: I'm thinking there's Zipzog, uh, URL guys, but uh, I'll let you check.
[43:15] Speaker 2: So what happened is I'd have my calendar there, and I would, before creating there, saying I would have pulled up a previous order, and then I would see what they would expect for their gift cards, and then I'd know what to.
[43:26] You: And are those the only 2 like customer preference options?
[43:28] Speaker 2: There have been URLs.
[43:30] system Unknown: URLs?
[43:31] system Unknown: Okay.
[43:31] Speaker 2: So, guys, Yes, but they only have that option for cards that we generate.
[43:35] You: Is the zip file or URL?
[43:43] Speaker 2: Otherwise, they just get whatever the uh, the uh, vendor provides.
[43:43] You: Got it.
[43:48] Speaker 2: Okay, so for URLs, we need to, um, Uh, so what I would do is next would be go in here.
[43:58] Speaker 2: I would just check that everything, uh, got generated, uh, properly, so they're the folders for each of the, uh, the types.
[44:06] Speaker 2: So, uh, and the old day they'd be able to remember, I believe there were 5 100s, right?
[44:12] Speaker 2: By 100s.
[44:15] Speaker 2: Yep, that's correct. We'll check that there were 5 in there.
[44:18] Speaker 2: PDF saws and 220?
[44:22] Speaker 2: No, 25?
[44:23] Speaker 3: When we generate it.
[44:24] Speaker 2: Okay, so 225?
[44:27] Speaker 2: Okay.
[44:27] Speaker 3: So right here, right?
[44:29] Speaker 2: So, Amazon. I'll have to say this.
[44:32] Speaker 2: Yeah, even 250s, okay.
[44:34] Speaker 2: Oh, yeah, 250, sorry.
[44:37] Speaker 2: How many 50s?
[44:38] Speaker 2: 50s. Yeah.
[44:42] Speaker 1: No, no, we're just validating.
[44:44] Speaker 1: Oh, I see.
[44:45] Speaker 2: And 110.
[44:48] Speaker 3: That's what I would do.
[44:49] Speaker 2: So that would be, thanks, I'd be, you know, uh, just go through quickly, verify.
[44:55] Speaker 2: So if that's good, then we are pretty sure that the zip file grabbed those things and put it in there.
[45:01] Speaker 2: So the next thing we would do is then, uh, uh, go to, uh, system one.
[45:06] Speaker 1: What are those PDFs look like?
[45:09] Speaker 1: Okay.
[45:17] system Unknown: Oh, wow.
[45:18] Speaker 2: So, that's what they. Okay, sounds good. Information, we just created that.
[45:23] You: One other, one other question for you, Lloyd, um, When you initially ran that Amazon program there that's on the desktop, you know, obviously we sought polling and doing some work, but then it just like closed.
[45:27] Speaker 2: Anybody who's an artist to go in there and make them, uh, look better if they want.
[45:32] Speaker 2: But nobody's complained.
[45:34] system Unknown: Where you...
[45:37] Speaker 3: What
[45:47] system Unknown: Yeah. Yeah.
[45:49] You: You know, I didn't see.
[45:51] You: Is there a success message or is there anything that lets, you know, whoever the operator is, know that it completed successfully.
[46:01] You: Is there ever a, you know, an a chance that that script doesn't run to the end to generate all of the PDFs?
[46:07] Speaker 2: Um. There's a, well, so the last thing that you and the, you may not have noticed or whatever.
[46:19] Speaker 2: So basically what happened at the end there was, uh, it went through a generator of the cards.
[46:23] You: Yeah. Yeah.
[46:24] Speaker 2: So usually it counts.
[46:25] Speaker 2: So you would be able to see that it generated whatever number of cards. And so you would be able to say, oh, there's X number cards should be generated.
[46:35] Speaker 2: The last thing it does is it creates a zip file.
[46:38] Speaker 2: So that you would have seen go through the screen.
[46:40] Speaker 2: It would have been saying, we've been showing, you know, 500, all the files going into a zip file.
[46:45] You: Yep.
[46:46] Speaker 2: So that's, that's also, so you knew it was going through that process.
[46:50] Speaker 2: And then the final thing for me is just to go through and make sure that they, in fact, did generate.
[46:52] You: Okay. Okay.
[46:55] Speaker 2: So, so to me, it looked, so to me, it looked like it was successful, because it went through the process of generating all the individual cards.
[47:04] Speaker 2: If a card failed.
[47:06] Speaker 2: So sometimes what happens, especially when we're doing blah blah, because it seems that they, their site goes down sometimes or it takes a long time.
[47:13] Speaker 2: So you will see retries.
[47:15] Speaker 2: Okay, so, but then, if you see a retry, but then it comes back with the same number that should have been, it would have attempted number 20 and it says 20, then you would know.
[47:26] Speaker 2: So those are those types of things happen.
[47:28] Speaker 2: So this is what I'm doing here is a final check, but if you see it go through the creating the zip file, then, you know, 99% it completed successfully.
[47:38] Speaker 2: So this is just me going to check that, anything.
[47:42] Speaker 2: I mean, I could put a delay there for it to hold so that you could see and, you know, but, um, I just go here and check that all the cards were, were saying, and I, you don't have to count the cards.
[47:46] You: Yeah. Yeah.
[47:55] Speaker 2: You just go and look at the, the thing there and you, you, Said, that kind of gives you the, the idea.
[48:02] Speaker 2: Yep
[48:02] You: And I see the desktop configuration settings file that is in the full folder here, and then there's that same file as in each of the individual denominations.
[48:12] You: Is that, what does that file for?
[48:15] You: Okay, so that's just something that Windows is creating.
[48:16] Speaker 2: Sorry, which that, oh, that well?
[48:18] Speaker 2: That's the Windows thing.
[48:19] Speaker 2: I have no idea.
[48:20] Speaker 2: Yeah, and I, I, I'm gonna guess.
[48:22] You: And then the
[48:26] Speaker 2: I'm gonna guess that everybody has it, but it's typically hidden. and somehow I did something to make it unhidden.
[48:29] You: Hidden, correct.
[48:30] You: Okay.
[48:31] You: To show them.
[48:33] You: Yeah.
[48:34] Speaker 2: Oh, yeah, like those.
[48:34] You: And then the the gift card log file that's also there.
[48:36] Speaker 2: That's me.
[48:37] Speaker 2: Okay.
[48:37] Speaker 2: But anyway, yes, no, that's. Yeah.
[48:41] You: What is that file?
[48:43] Speaker 2: So basically that's uh, an Excel file that's put inside of the, the zip file that basically has a catalog of all these, uh, of all the, what's in, okay, I can go in there and join.
[48:59] Speaker 2: So basically, it has an inventory of what file and what's denomination.
[49:07] You: Got it.
[49:08] system Unknown: For the file.
[49:10] You: And is that, is that something that's generated by that Amazon script that you ran?
[49:16] Speaker 2: Right.
[49:17] Speaker 2: Correct.
[49:19] Speaker 2: And, and that's required for when we upload this, so that's embedded in that, that Zimfla, that when we upload it to system bond, and they're going to create web pages for each of these cards.
[49:30] Speaker 2: They use that as kind of a catalog, and then they can serve coincide that.
[49:36] Speaker 2: So inside the zip file, there's going to be folders, just like the soldier we went into, and they'll be able to use this as a backup to match to make sure everything kind of matches.
[49:44] You: Okay. Okay.
[49:45] Speaker 1: Sorry, I missed that part.
[49:47] Speaker 1: The website's created, sorry?
[49:49] system Unknown: What was that?
[49:50] Speaker 2: We're about to get there.
[49:51] Speaker 2: We haven't done that yet.
[49:52] Speaker 2: Drop the gun.
[49:54] Speaker 2: No, no worries.
[49:56] Speaker 2: But yeah, I love, I put that in the notes too.
[49:59] You: Okay.
[49:59] Speaker 2: I sent you.
[50:00] Speaker 2: Okay, so, uh, so if if you need, uh, um, If if we were gonna send them a, a, a zip file, then we would just encrypt this guy and then we're kind of done.
[50:14] Speaker 2: But customers in need URLs, and we have to get them to generate them, and then they're going to give us an Excel file with all the URL earls.
[50:23] Speaker 2: So I'll go through that process now.
[50:25] Speaker 2: So that's, uh, we go to system behind.
[50:27] Speaker 2: Uh, that's that, uh, that's the company that's done that for us.
[50:28] You: Yeah. Yeah.
[50:33] Speaker 2: You can see this, I assume.
[50:35] Speaker 2: Yep.
[50:35] Speaker 2: Okay.
[50:37] Speaker 2: Um, so we have to go here and uh, Oh, come on, you better remember the, uh.
[50:51] Speaker 3: One of the top clients or digital recommended this company.
[50:54] Speaker 3: There we go.
[50:55] Speaker 3: Our security programs.
[50:57] Speaker 3: Yeah.
[50:57] Speaker 3: They're secure company, security company.
[51:00] Speaker 3: Are you kidding?
[51:01] system Unknown: No.
[51:04] Speaker 2: Yeah, you have to guess, you're going to say, yeah.
[51:12] Speaker 2: So they provide this this functionality here where we can choose a, uh, a zip file.
[51:20] Speaker 2: Uh, basically the only, uh, Checking it has is that they see you try and upload a zip file with the same name and uh, it's gonna reject you.
[51:32] system Unknown: Okay. Um. Okay.
[51:54] Speaker 2: Hey, so, does it soundly upload that?
[52:00] Speaker 2: And then uh, you hit this upload, uh,
[52:03] Speaker 2: Well, I think. But here?
[52:07] Speaker 2: And it's gonna show you that it uploaded everything into their system.
[52:10] You: And I can't see the rest of the text on that button.
[52:12] Speaker 2: Then the next process we do is export.
[52:14] Speaker 2: Okay, and that will download a zip file.
[52:20] Speaker 2: Or, sorry, you can't see what, sorry?
[52:23] You: Uh, your Google Meet little windows covering export report.
[52:30] You: Okay.
[52:30] You: I just wanted to see the text.
[52:31] system Unknown: Yeah, yeah.
[52:33] Speaker 2: Okay.
[52:34] Speaker 2: Uh, and yeah, but just, basically, into this discuss here.
[52:40] Speaker 2: So we're done with that guy.
[52:41] Speaker 2: So then we can, uh, Now that gets put into the download folder before we go there, and then we go back here.
[52:55] Speaker 3: I don't know. Some system up?
[52:58] Speaker 3: Yes.
[52:58] Speaker 2: So, so, so, it turns into anywhere else. You're going to go downloads, if we refresh.
[53:03] Speaker 2: That's the file that was exported.
[53:07] Speaker 2: We're just going to rename it.
[53:10] Speaker 2: That's when I'm just going to give it encrypted, in the end.
[53:15] Speaker 2: Hey, and we're going to go in here.
[53:37] Speaker 2: That's gonna add an encryption password.
[53:43] Speaker 2: Here.
[53:44] Speaker 2: Okay, so these are the earls that were created for each of those cards.
[53:47] Speaker 2: Um, Yeah, it's gonna get this file, so we're just gonna... Sword.
[54:07] Speaker 2: The one thing I missed from the other things, it's a, I've been doing this for a while, which we'll do here.
[54:18] Speaker 2: Says, uh, say there, so we're gonna close.
[54:22] Speaker 2: Uh, that guy?
[54:25] system Unknown: Right?
[54:27] Speaker 2: Then we're gonna copy that to our.
[54:41] Speaker 2: So what I should done also with the SO file?
[54:50] Speaker 2: Was, uh, just verify that they didn't mess up the password. So when I would open this guy.
[54:56] system Unknown: Yeah.
[54:58] system Unknown: Hey.
[55:03] Speaker 2: Yeah. I said, I would redo it and put the appropriate password in there.
[55:08] You: That's just to validate that you keyed in the correct, um, password before sending it.
[55:10] Speaker 2: Okay.
[55:12] system Unknown: That's right.
[55:17] Speaker 2: Yeah.
[55:18] Speaker 2: Yeah, no, I mean, there's always a chance that, uh, you know, I made the mistake, like, I guess 3 times.
[55:18] You: Okay.
[55:27] Speaker 2: But, uh, I mean, yeah, I don't think that that's ever happened.
[55:32] Speaker 2: So anyway, so that's that's what I do.
[55:34] Speaker 2: Um, Okay, so I guess Mario can show you how to send these, I guess.
[55:38] You: Yeah.
[55:40] Speaker 2: Yeah, that makes sense.
[55:42] Speaker 2: We still have to do the other file.
[55:44] Speaker 2: Um, Kira. Kira and Mavlas, right?
[55:47] Speaker 2: Karen Loblas.
[55:51] Speaker 2: Yeah, but they look they look just like, oh, yeah, just like SO.
[55:56] Speaker 2: So I guess what I could do here for this one is show what would happen this, uh, so the only thing that we haven't seen is, that, uh, is what we would do for, um, their fun.
[56:09] Speaker 3: Um, does that follow you said?
[56:10] You: Your audio cut out there, Lloyd.
[56:13] system Unknown: Sorry?
[56:15] Speaker 3: Yeah, you, for 12nd there.
[56:18] Speaker 2: If we need to send a zip file, we didn't see that as part of the process.
[56:22] Speaker 2: That's something else that we do sometimes.
[56:26] Speaker 1: Mario, show us that as well. Like that, if that's something that he typically does, then we can we can go through that process and fulfill that part of the order.
[56:35] Speaker 1: But, um, yeah, Spence, do you have any other uh, technical questions for Lloyd?
[56:40] You: Yeah, I guess I'm, I'm curious if there is anything, you know, because ultimately what we're trying to wrap our heads around is, is, um, you know, is there anything, I guess, undocumented anywhere in the workflow that sort of still lives in your head?
[57:00] You: You know, let's say you win the lottery tomorrow and all of a sudden you're no longer available to support Mario.
[57:08] You: Um, Is there anything critical that that he might not fully know or that's not captured somewhere?
[57:16] Speaker 2: Um.
[57:19] Speaker 2: Yeah, I mean, I think we've, uh, Married, did we ever go over doing a, uh,
[57:27] You: You might be covering your mic on your computer.
[57:29] Speaker 2: A, um.
[57:37] Speaker 2: I'm not touching my computer.
[57:39] You: Can't hear you.
[57:39] You: There we go.
[57:42] Speaker 2: I wasn't touching my computer.
[57:42] You: That's better.
[57:45] Speaker 2: Anyway, um, uh, Mario, have we ever, uh, Um,
[57:51] Speaker 2: Have you ever done a petro Canada order where we were using the old inventory?
[57:55] Speaker 2: Or did I just do that?
[57:57] Speaker 6: No, I think you did it.
[58:00] Speaker 6: I remember one time I needed because we're with the old one, but you just did it for me and I...
[58:07] Speaker 2: I guess that there's no...
[58:10] Speaker 2: I mean, I guess worst case, with the old inventory, you could just use it.
[58:14] Speaker 2: Yeah, yeah.
[58:15] Speaker 2: Yeah.
[58:16] Speaker 2: Like, because it's not something that is going to happen anymore because we get those as URLs now, right?
[58:20] Speaker 2: Yeah, yeah.
[58:22] Speaker 2: So, so that's, that's something that, you know, and, and worst, worst case, you just send the gift cards as is to the, the PBS to them as is.
[58:34] Speaker 2: You just put them in a zip file and just sign them.
[58:36] Speaker 2: don't have to be, and don't give the option to add them as herbal, right?
[58:40] Speaker 2: Yep.
[58:40] Speaker 2: So that's not something that, so that's, uh, that's something that, uh, we had to do, but it's kind of being phased out anyway.
[58:46] You: Got it.
[58:48] Speaker 2: Um.
[58:50] Speaker 3: Those are all calling all kinds.
[58:52] Speaker 2: I mean, I guess it's, you know, if I wasn't available and something, bug happened with the script, well, any program would be able to to do that, but you'd have to get something to go through them.
[59:03] You: Yeah.
[59:04] You: Yeah.
[59:05] Speaker 2: But it's not.
[59:06] Speaker 2: I mean, it's not, it's not rocket science.
[59:08] Speaker 2: It's like, you know, the code is pretty straightforward, you just identify the air and debug it.
[59:15] Speaker 2: Um, So, uh, so Amazon.
[59:21] Speaker 2: Amazon is the same as uh, Same as indigo, same as the law laws is being phased out.
[59:31] Speaker 2: So probably, Worst case, you could get customers to accept, well, anyway, it doesn't matter.
[59:39] Speaker 2: Amazon, uh, Loblaws acts just like Amazon, so Mario would be able to do that, so that's nothing uh, unique.
[59:44] Speaker 2: Shoppers, Ubers, not that anymore.
[59:47] Speaker 2: Walmart is, uh, So there's nothing that, uh, um,
[59:53] Speaker 2: Like assuming that it works as, as expected that, uh, he, he couldn't, It's just, his problems came out for some reason that, uh, where the scripts didn't work.
[1:00:03] You: Okay.
[1:00:06] system Unknown: Okay.
[1:00:08] You: And I guess my other questions that I'm just aware of time, I don't know how much longer we have you for.
[1:00:16] You: But on the SO and Blackhawk API work, I know that's something that sounds like is ongoing and you've submitted, I'm just trying to refresh my memory from the notes that you had sent. You're waiting on certification, is that right?
[1:00:35] Speaker 2: Um, yeah, so. Um, Basically, I've moved as far as I can.
[1:00:45] Speaker 2: So Black Hawk, I mean, we've done all the transactions that, uh, Doug Wad.
[1:00:50] Speaker 2: We only worked with one vendor, Tim Hortons.
[1:00:52] Speaker 2: Presumably the, the, adding other vendors.
[1:00:56] Speaker 2: There'll be more work need to be done, but it should be straight forward once we get that done.
[1:01:00] Speaker 2: Um, there were some things we couldn't, uh, or at least to my satisfaction, couldn't, you know, so every, so sometimes we would run stuff, and it wouldn't work, and then they'd say, oh, try adding a, uh, a slash after the earl, to these, the wrestle intervation.
[1:01:11] You: Yeah. Right.
[1:01:18] Speaker 2: Sometimes that, or they said, you know, there was no documentation, like, so for instance, for the cancel operation.
[1:01:25] Speaker 2: There was no documentation, so, like, I I kind of guess the format based on the, what other things were there.
[1:01:31] Speaker 2: So, at the end of the earl, like they, cancel or like, say, sir, the reload, the reload.
[1:01:37] Speaker 2: They can say, oh, no, it's not canceled.
[1:01:39] Speaker 2: just, it's just, um, uh, you, sort of kind of operation.
[1:01:45] Speaker 2: You don't put anything at the end, and you submit the URL.
[1:01:48] Speaker 2: So I tried that, and it returned the response, but I told him that, The response looked exactly like, is this what I did, a balance comb.
[1:01:48] You: Yeah. Right.
[1:01:57] Speaker 2: And it didn't change it.
[1:01:58] Speaker 2: It didn't change any of the, you know, as we did a cancel, then I would expect the status to go from active to,
[1:02:05] Speaker 2: You know, so then it was like, oh, well, it doesn't happen in our,
[1:02:10] You: Yeah, yeah, yeah. Got it.
[1:02:10] Speaker 2: It may it may not.
[1:02:12] Speaker 2: It didn't say, it may not happen in our, their test system, but it should work properly in the production system.
[1:02:16] Speaker 2: So we'll have to wait till we get to production to see if that's in fact the case.
[1:02:20] You: Okay.
[1:02:20] Speaker 2: So, There's still some questions.
[1:02:21] You: So essentially, you've been sort of guessing at how their API endpoint in calls and and what's...
[1:02:22] Speaker 2: So, yeah, so.
[1:02:30] Speaker 2: Yeah, well, well, for that, that's the only one, I guess, I was guessing.
[1:02:34] Speaker 2: The other ones, there was documented API, they did it, and they worked.
[1:02:38] Speaker 2: That one is the only one that's kind of, they source a, well, when you can, you can test it once on the, and we'll, we'll, we'll give you some production cards, which we won't judge you as far so that you can test that, the cancel actually works.
[1:02:44] You: Right.
[1:02:50] You: Okay.
[1:02:51] system Unknown: Yeah.
[1:02:51] Speaker 3: So. So, also on the, on the, A, API. No, come on, go on, like crazy.
[1:03:00] Speaker 3: Um, some some of the, the merchants don't allow that, right?
[1:03:05] Speaker 3: Like, um, I know Funstream is kind of, I would say, like 10 years ahead of us with this sort of stuff, is like Labaz is an example won't allow any integration with their their backend or whatever, right?
[1:03:18] Speaker 3: So even if we wanted to sort of be integrated with as many processors and merchants as we can, some of the merchants just won't allow it, right?
[1:03:26] Speaker 3: So, so my, my vision was to, to get started on some, so Lloyd could see kind of what the process was, wasn't, is it worthwhile?
[1:03:35] Speaker 3: Is it worthless a lot?
[1:03:37] Speaker 3: And so SLN cast are the 2 that we started with.
[1:03:38] You: You can do it a little bit later.
[1:03:40] Speaker 3: So, um, yeah, so that's that's kind of my vision of the big picture of why we're doing it.
[1:03:47] Speaker 3: And I think, you know, Amazon's probably maybe the next one and there also might be some added integration work to do with with Walmart.
[1:03:49] You: I know if I'm still in a meeting, okay?
[1:03:50] You: When I'm done with my meeting.
[1:03:53] You: But I need to just start...
[1:03:56] Speaker 3: So that's kind of my short term vision, but the long term is, I just wanted to get into it, see what it was like, see if is it beneficial for us? And, uh, But I know some of the merchants and we can't, we can't get to it because they don't allow it.
[1:04:02] You: Okay, let me get to our stopping point and then I'll come and move it, okay?
[1:04:10] You: Got it.
[1:04:10] system Unknown: So.
[1:04:10] system Unknown: Yeah.
[1:04:12] Speaker 2: So for, uh, and for, for Eso, um, so they, they actually, with their process, they actually, and that was the same for buy serve as well.
[1:04:21] Speaker 2: They actually assign you, like, a resource that is a technical resource who you can go through.
[1:04:28] Speaker 2: So, with them, I think we were just waiting now. So, anyway, so we've tested everything we want to test, worked as expected in their test system.
[1:04:36] Speaker 2: Um, The last thing, and I just hadn't sold it up or Doug hasn't sold out, the last thing was, uh, uh, we executed all the transaction we had to.
[1:04:45] Speaker 2: They worked as expected.
[1:04:46] Speaker 2: He was gonna, the resource was going to review them on their system.
[1:04:50] Speaker 2: Get back to us.
[1:04:53] Speaker 2: So I haven't pushed it, so we're ready to go basically when they can assign a resource and say that they're ready to go.
[1:05:01] Speaker 2: Uh, we initially said that we would be ready in the 1st week of March, and we're here now.
[1:05:01] You: Got it.
[1:05:07] Speaker 2: So.
[1:05:09] system Unknown: Okay.
[1:05:10] system Unknown: Okay. Okay.
[1:05:13] Speaker 1: I was a good demo.
[1:05:15] Speaker 1: Thank you, Lloyd.
[1:05:15] Speaker 1: Spence, anything else that you have on your end?
[1:05:15] You: Uh, I don't think so.
[1:05:19] You: Um, you know, certainly we may have some follow-up questions, you know, Obviously, it covers a lot.
[1:05:26] You: We'll get more sort of as we probably do a few of the other vendors with Mario, but no, that was super helpful.
[1:05:35] Speaker 3: Um okay.
[1:05:38] Speaker 3: All righty.
[1:05:40] Speaker 2: Is there anything else that you wanted to share, Lloyd?
[1:05:43] Speaker 2: Um, no, not unless you have questions.
[1:05:48] Speaker 2: I was just sort of thinking if there was something that, uh, Um, I need to share.
[1:05:53] Speaker 2: So, so basically in terms of how things are set up, like, I think I've captured as much as possible on the, uh, in the notes I sent you in terms of where the scripts are and, I think, uh, you know, there's only one tool that had to be installed that does the PDFs, it says Inkscape.
[1:05:57] You: Yeah. Yeah.
[1:06:10] Speaker 2: I think everything else is just play some libraries and that kind of stuff, so, um, yeah, so I think it's not, uh, you know, so.
[1:06:21] Speaker 2: And and the same for the other integrations.
[1:06:24] Speaker 2: They're also just, um, oh, sorry, the only different thing would be the Walmart, which we didn't show.
[1:06:30] Speaker 2: I don't know if you need to see that where we go and we, uh, I don't know if we have a Walmart order that's ready to be done, Doug, where it's, Mario could also show that.
[1:06:38] Speaker 3: I got one right here.
[1:06:39] Speaker 1: So, yeah.
[1:06:40] Speaker 1: Yeah, Mario can show us that one.
[1:06:42] Speaker 1: perfect.
[1:06:42] Speaker 2: Yeah.
[1:06:43] Speaker 2: So, anyway.
[1:06:45] Speaker 1: Yeah, well, we'll digest and synthesize and if there's any questions, we know, uh, we know where to find you.
[1:06:51] Speaker 1: Um, and so, you can definitely uh, recroup if that does happen.
[1:06:55] Speaker 1: Um, but yeah, let's let's call it on this meeting and then we can shift over Spence to the other in, like, I'll get a Google meet, um, going for the 2nd session with Mario, and we gotta go from there.
[1:07:09] Speaker 2: Okay, so, okay, thanks, guys.
[1:07:12] Speaker 2: So just one last thing, whatever, so with, with the Black Hawk in there, uh, you know, the digital card thing.
[1:07:21] Speaker 2: So you're going to have the polls thought.
[1:07:22] Speaker 2: And you're gonna want to activate those cards if you're gonna plan to do it through their interface.
[1:07:28] Speaker 2: So it's going to be, it's going to be like what you didn't want to do.
[1:07:31] Speaker 2: It's not start to end, right?
[1:07:32] Speaker 2: You have to do one card at a time.
[1:07:34] Speaker 3: Yeah.
[1:07:35] Speaker 3: Well, that, I think that's okay with, um, all the other merchants except for Walmart.
[1:07:40] Speaker 3: Like the digitals, we don't sell that much, right?
[1:07:42] Speaker 3: So I think that's...
[1:07:44] Speaker 3: Okay.
[1:07:44] Speaker 3: The only the only problem is Walmart because we, we, the physical ones, we sell so much of it, right?
[1:07:51] Speaker 3: All the ones individual is fine.
[1:07:54] Speaker 3: Okay, we don't sell enough of it to to really be a problem yet.
[1:07:58] Speaker 3: Yeah, okay, sounds good.
[1:08:01] Speaker 3: Perfect.
[1:08:02] Speaker 3: Thanks, Lloyd.
[1:08:03] Speaker 3: Alright, thanks, all right.
[1:08:04] Speaker 3: care.
[1:08:05] Speaker 3: You too.
[1:08:06] Speaker 3: Bye.
[1:08:06] Speaker 3: Thanks.
[1:08:07] system Unknown: That was helpful.
[1:08:11] Speaker 1: So, Spence, what we can do is we can, um, well, we can adjourn this one and then that, that will get the recording and and all the, the transcripts going.
[1:08:15] You: Okay, sounds good.
[1:08:20] Speaker 1: And then we can, in a couple minutes, jump on the other one.
[1:08:22] Speaker 1: Okay, sounds good.
[1:08:23] You: Okay, thanks.