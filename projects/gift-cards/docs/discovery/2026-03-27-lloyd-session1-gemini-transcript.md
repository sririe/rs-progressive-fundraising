---
title: "Gemini Notes & Transcript — Session 1: Digital Gift Card Fulfilment Technical Discovery (Lloyd)"
type: discovery
category: meeting-transcript
date: 2026-03-27
status: complete
format: gemini-notes-and-transcript
source: google-meet-gemini
participants:
  progressive:
    - Lloyd S. (Technical Contractor)
    - Doug B. (Owner)
    - Mario (Digital card operator)
  redstamp:
    - Spencer R.
    - Danny Norton (Tim L.)
tags: [knowledge-transfer, lloyd-handoff, gemini-transcript, digital-fulfillment, card-generation, esso, amazon, loblaws, systemone, blackhawk-api, python-scripts, validation-reference]
related:
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-transcript.md
---

﻿📝 Notes
Mar 27, 2026
Working Session - Redstamp + Progressive Fundraising (Digital Gift Card Fulfilment Technical Discovery) (Remote)
Invited lscrubb@progressivefundraising.ca gsmart@progiftcards.ca dbeers@progressivefundraising.ca Danny Norton Spencer Ririe mmanzano@progressivefundraising.ca
Attachments Working Session - Redstamp + Progressive Fundraising (Digital Gift Card Fulfilment Technical Discov 
Meeting records Transcript Recording 


Summary
Technical demonstration of digital order generation covered existing manual processes for inventory and card creation with updates on vendor API integration.

Technical Order Generation Demo
The technical demonstration focused on generating a complex digital order, Invoice 55, which included manually fulfilled ESO cards and system-generated Amazon cards. The process begins with running a Python script to read the invoice and generate folders for the specific merchants involved in the order.

Manual Inventory and Fulfillment
Fulfillment for ESO cards relies on a manual inventory process involving copying card details into a password-protected Excel file, which is then stored on Google Drive. Success of generation scripts is confirmed by the creation of the final zip file and a quick validation of the resultant PDF files.

Vendor API Integration Status
Progress on the Blackhawk API has halted due to undocumented cancel operation formats, which may only be resolvable in the production environment. The ESO integration is ready to proceed, confirmed by successful transactions in their test system and current pending review by the technical resource.


Details
* Initial Meeting Connection and Technical Setup: The meeting started with Danny Norton and Lloyd Scrubb attempting to establish audio connection. Lloyd Scrubb confirmed they could be heard, and the technical setup proceeded (00:00:00). The initial discussion focused on whether Lloyd Scrubb should share their screen from their machine or use Mario's, concluding that sharing Lloyd Scrubb's screen would be easiest for the technical demonstration (00:01:22).
* Goal of the Technical Demonstration: The purpose of the meeting was to allow the attendees to observe the technical process of generating orders, providing an "underneath the hood" look at how Lloyd Scrubb built certain systems. The intent was to see the technical side of the build to potentially understand and reverse engineer the process, contrasting with Mario's planned later demonstration of the workflow with different vendors (00:01:22).
* Selecting an Order for Demonstration: The team decided to proceed with demonstrating the creation of a digital order, a workflow Danny Norton wanted to see (00:02:18). Danny Norton presented several invoice options, including one that was Walmart-only and another that was Loblaw-only, but Lloyd Scrubb suggested a more complex order that included both generated and copied cards. They settled on using Invoice Number 55, which included ESO, Care, and Amazon (00:03:08) (00:06:25).
* Integrating Spencer Ririe into the Discussion: Spencer Ririe joined the meeting, and Danny Norton confirmed that the transcription and recording were active (00:03:56). Danny Norton explained that they would start by having Lloyd Scrubb demonstrate an order generation from their perspective, after which they could delve into any other specific technical questions Spencer Ririe had (00:04:49).
* Overview of the Order Generation Theory: Danny Norton inquired if Lloyd Scrubb could provide a high-level overview of the theory behind the process for the "Red Stamp guys," which Lloyd Scrubb suggested would be revealed naturally by going through the process itself (00:04:49). Lloyd Scrubb confirmed that the demonstration would essentially show what they taught Mario to do (00:05:44).
* Initial Step: Receiving and Processing the Invoice: Lloyd Scrubb explained that the process begins with receiving a digital order, typically in the form of an invoice, which they download to their downloads folder (00:06:25). Lloyd Scrubb noted they have a program written to read the invoice and generate the necessary files for the different cards that will be sent to the customer (00:07:23).
* Execution of the Invoice Reading Script: Lloyd Scrubb demonstrated running a Python script to read the invoice, which loads the different tools used by the program. This script brings up a dialogue box to load the invoice and generates a corresponding folder structure in the "orders" folder (00:09:55).
* Inventory and Generation Logic for Specific Merchants: The initial program generated folders for Amazon, Loblaw, and ESO (00:10:56). Lloyd Scrubb explained that for ESO, they use inventory by copying provided cards into a file and then encrypting it, as opposed to generating the cards themselves. For Amazon and Loblaw, generation programs are used (00:12:12).
* Inventory Management and Procurement Process: The team discussed the process of retrieving pre-purchased inventory (like ESO cards) from the orders folder (00:13:05). Lloyd Scrubb clarified that if inventory is insufficient, they would order and replenish it before starting the fulfillment process, which is now generally "just in time processing" rather than maintaining large stock (00:14:57).
* Triggering the Order Fulfillment Process: Danny Norton confirmed that payment of an invoice is the primary trigger for starting the fulfillment process. Procurement is managed by checking sales from a year prior, as sales are typically similar, though large, unanticipated orders require immediate replenishment before the invoice is considered paid and ready for processing (00:15:59).
* Manual Process of Inventory Transfer and Data Entry: Lloyd Scrubb detailed the manual process of transferring card information from the inventory file to the customer file for ESO cards, which involves copying the invoice number and card details and marking them as removed from inventory (00:16:56). This manual process is prone to being brittle if mistakes are made, though Danny Norton noted the team's diligence minimizes errors (00:19:48).
* Discussion on Script Version Control and Maintenance: Spencer Ririe inquired about version control for the Python and Apache scripts, noting that version control like Git is not used (00:25:34). Lloyd Scrubb confirmed they are the sole developer and track all work and updates via a Google Calendar, with copies of updated scripts stored (00:26:56).
* Addressing Script Errors and Debugging: Lloyd Scrubb confirmed that Mario has experienced issues with scripts not running successfully after installation on their machine, often necessitating updates to the Python version and subsequent debugging (00:27:53). When errors occur, output logs are generated on the screen, which Lloyd Scrubb uses to debug, particularly when encountering issues due to inconsistent invoice formats or different computer environments (00:28:48).
* Finalizing the Manual Inventory File for Delivery: After transferring the necessary information for ESO cards, Lloyd Scrubb saved the Excel file and added a password, which is based on the invoice number. This password-protected file is stored on Google Drive (00:22:03).
* The Amazon Generation Process: Lloyd Scrubb moved on to the Amazon order, which requires card generation (00:31:48) (00:33:42). The team reviewed the specific, complex order involving multiple denominations (00:34:42). Lloyd Scrubb demonstrated grabbing the cards from the inventory file, transferring the details, and freezing the top row of the spreadsheet to aid visibility (00:37:31).
* Executing the Amazon Card Generation Script: After successfully populating the inventory file for Amazon, Lloyd Scrubb ran the Amazon generation program, which prompted them to select the Excel file as input (00:47:11). This process generated a resultant folder containing PDFs for each denomination, which Lloyd Scrubb validated against the order (00:48:02).
* Customer Delivery Format Options and System Bind: The customer for this order requires URLs, which is one of two format options (the other being a zip file), available only for cards that they generate (00:48:02). This requires using the third-party service System Bind, where they upload the generated zip file to create web pages for each card (00:55:35).
* Zip File and Success Confirmation: Spencer Ririe asked about how Lloyd Scrubb confirms the generation script runs successfully, to which Lloyd Scrubb replied that the last step is the creation of the zip file, and a quick check of the generated PDF files confirms success (00:51:51). The zip file contains a gift card log file, an Excel file cataloging the contents, which is used by System Bind for matching and cataloging during the URL creation process (00:54:46).
* File Preparation and Encryption Demonstration: Lloyd Scrubb completed the export of a file and proceeded to rename it in the downloads folder, appending "encrypted" to the file name. They demonstrated adding an encryption password to the file, which contained URLs created for each card, using "password 44" as an example, and noted the importance of saving the changes (00:58:58). Lloyd Scrubb also mentioned that they should have verified the password on the original file to ensure accuracy before sending it, a step they perform to avoid errors (01:00:52).
* Discussion on Sending Encrypted Files and Outstanding Tasks: Lloyd Scrubb indicated that Mario could demonstrate how to send the encrypted files to the customer, which Spencer Ririe and Danny Norton agreed would be helpful. Lloyd Scrubb noted that they still needed to address the process for sending a zip file, which they sometimes utilize but had not yet covered in the current demonstration (01:00:52). They suggested they could demonstrate what happens if a zip file is needed as this part of the process was not previously seen (01:02:11).
* Review of Undocumented Workflow Knowledge: Spencer Ririe asked Lloyd Scrubb if there were any critical, undocumented elements of the workflow that were not captured, potentially creating a single point of failure if Lloyd Scrubb were unavailable. Lloyd Scrubb identified that Mario may not have experience with processing a Petro-Canada order using the old inventory system, a process they handled previously (01:03:00). However, they noted that this process is being phased out as the gift cards are now received as URLs, suggesting that worst case, the PDFs could be sent directly in a zip file without the option to add them as URLs (01:04:26).
* General System Operations and Non-Unique Vendor Processes: Lloyd Scrubb confirmed that processes for Amazon and Indigo, as well as Loblaws, are similar, with Loblaws also being phased out. They stated that Mario would be able to handle these, and mentioned that other vendors like Shoppers and Uber no longer use the process discussed, while Walmart still requires a specific process. They concluded that, assuming the system works as expected, there is nothing unique that Mario could not handle if a problem were to arise with the scripts, as the code is straightforward and any programmer could debug it (01:05:15).
* Status of Blackhawk API Integration Work: Spencer Ririe inquired about the ongoing Blackhawk API work, specifically the status of certification. Lloyd Scrubb reported that they have progressed as far as possible, having completed all requested transactions with the vendor Tim Hortons, though adding other vendors will likely require more work (01:06:34). Lloyd Scrubb detailed issues with documentation, noting that the required format for the cancel operation had to be guessed, and the testing response for a cancellation looked identical to a balance check (01:07:46).
* Testing and Production Concerns with Blackhawk API: Lloyd Scrubb communicated that the Blackhawk system's response for the cancel operation did not result in a status change in their test environment, and they were told that this functionality might only work correctly in the production system (01:07:46). Spencer Ririe summarized that they have been "guessing" at the API endpoints for the cancel operation, though Lloyd Scrubb clarified this was the only operation that lacked documentation. Danny Norton added that some merchants, like Loblaws, will not allow any backend integration, which impacts the overall vision for API integration (01:08:46).
* Progress on ESO API Integration Work: Lloyd Scrubb provided an update on the ESO integration, noting that unlike Blackhawk, ESO assigns a technical resource for support. They confirmed that all necessary transactions worked as expected in the ESO test system and that the integration is ready to proceed. They are currently waiting for the ESO technical resource to review the executed transactions on their system and confirm that they are ready to move forward (01:10:38).
* Final Technical Inquiries and Future Plans: Danny Norton thanked Lloyd Scrubb for the demo and asked if Spencer Ririe had any final questions. Spencer Ririe indicated that they may have follow-up questions but found the information helpful, especially before working with Mario on other vendors (01:11:28). Lloyd Scrubb mentioned that the notes sent cover script locations and tools, noting that the PDF tool, Inkscape, was the only non-Python library installation required, and suggested they might still need to demonstrate the unique Walmart process (01:12:29).
* Blackhawk Activation Process for Cold Stock Cards: Lloyd Scrubb brought up the Blackhawk digital card process, alerting Danny Norton that activating cold stock cards through their interface would require activating them one card at a time, rather than using a start-and-end range. Danny Norton responded that this individual activation process is acceptable for most merchants, as they do not sell a large volume of digital cards, with Walmart being the exception due to the high volume of physical card sales (01:13:34).


Suggested next steps
* Lloyd Scrubb will show what would happen if a zip file needs to be sent to a customer as part of the process, which has not been seen yet.
* Danny Norton and Spencer Ririe will digest and synthesize the information and regroup if there are any questions.
* Danny Norton and Spencer Ririe will shift over to a second session with Mario regarding the Walmart order.


You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes
Please provide feedback about using Gemini to take notes in a short survey.
📖 Transcript
Mar 27, 2026
Working Session - Redstamp + Progressive Fundraising (Digital Gift Card Fulfilment Technical Discov - Transcript
00:00:00
 
Danny Norton: Hey Lloyd. Hey there's Lloyd. Hey Lloyd. Can you hear us? Okay. You can hear us. Can you hear us, Lloyd? I think so. It's coming through or No, I think we can't hear you yet. How come is it just take some time to warm up? No, he might just be switching his inputs for his mic. Oh, I see. At least we got some IT guys that know what they're doing. So,
Lloyd Scrubb: as
Danny Norton: right, Marian, you're all ready to go. So, Oh, yeah. Yeah, you can pass that off. You can do that later. What is that? What are you doing? Oh, you're just doing that. Yeah, there we go.
Lloyd Scrubb: my mic is on.
Danny Norton: Yeah, it's We're good. We can hear you.
Lloyd Scrubb: Excellent.
Danny Norton: Hey, Lloyd, how's it going?
Lloyd Scrubb: Hey, not too bad. Thanks
Danny Norton: Good. Very good.
 
 
00:01:22
 
Danny Norton: All right.
Lloyd Scrubb: you.
Danny Norton: Do you have a preference in terms of using your machine and sharing that screen or is there any benefit of you logging into Mario's machine and and showing stuff from
Lloyd Scrubb: Okay.
Danny Norton: there?
Lloyd Scrubb: So, showing the scripts, like what are we showing? I thought there's a demo going on later. So, I'm trying to understand what
Danny Norton: Yeah. No. Great. Yeah.
Lloyd Scrubb: uh
Danny Norton: So what what our thought was that uh we wanted to be able to see what uh some of the the different ways of of you managing like how you kind of created certain things so that we could get an understanding underneath the hood on on what uh everything looks like. And uh later on today Mario is going to be going through the workflow that he does to generate things and and how that is managed with different vendors. So we don't need to necessarily cover that part. The goal is to see the more technical side of of how you've built certain things so that we can just get a sense of what that looks like and potentially reverse engineer and and just understand from from that side of things.
 
 
00:02:18
 
Danny Norton: And then when Spencer jumps on in a few minutes, he'll he'll he has a few more questions to kind of guide that as well. But that that was kind of the goal is just to see from your perspective how things are built out uh to then allow Mario to do what he does.
Lloyd Scrubb: Oh, okay. So, you want me to go through creating a digital order or something?
Danny Norton: That would that would definitely be one of the workflows we we want to see for sure.
Lloyd Scrubb: Okay. Okay. So, that's what I thought Mario was doing. So, I was Okay. So, that we can do that. No problem. I don't uh uh So, Doug, do you have an order that uh is
Danny Norton: Mario's got a few
Lloyd Scrubb: Okay.
Danny Norton: here.
Lloyd Scrubb: All righty. Can you Can you send me a an invoice?
Danny Norton: Yeah, Mario will do that.
Lloyd Scrubb: Okay, perfect. So, I guess then it's easier just for me to share my
Danny Norton: Yeah.
 
 
00:03:08
 
Danny Norton: Yeah, I think we could do that here.
Lloyd Scrubb: screen.
Danny Norton: I'll just make sure I got my max volume here. Should we do a simple one or more comp complicated with more Got
Lloyd Scrubb: doesn't doesn't matter to me.
Danny Norton: it.
Lloyd Scrubb: I don't I don't Well,
Danny Norton: What do you think, Danny? Like
Lloyd Scrubb: I don't I don't want to do a I don't want to do a uh So, maybe do one that has generated cards and uh ones that we're just going to copy like
Danny Norton: Okay. So, we got we got one that's uh a Walmart only and another one that's Loblas only.
Lloyd Scrubb: uh
Danny Norton: Does that fit the bill?
Lloyd Scrubb: No, but you want with So, Loblas and Walmart we generate, right?
Danny Norton: Oh, I see.
Lloyd Scrubb: But but maybe I mean it doesn't matter but
Danny Norton: Okay, Lloyd, we we we'll send you this one and then uh you can start it,
Lloyd Scrubb: it's
Danny Norton: Mario can finish it or whatever. This other one, it's got ESO, it's got Care, it's got Amazon.
 
 
00:03:56
 
Danny Norton: Um and then we got Yeah.
Lloyd Scrubb: perfect.
Danny Norton: Okay. So, send them that invoice and then if we need to,
Lloyd Scrubb: Okay.
Danny Norton: we'll send them these two invoices later. You just phone.
Lloyd Scrubb: Share screen. And this is this guy here, right?
Danny Norton: One moment there, Lloyd. I'm just going to make sure that Oh,
Lloyd Scrubb: Lord.
Danny Norton: nope. We got it all taken care of. We got Spence here. So, that's what I wanted to to make sure we had. It's a good looking picture of Spencer there. Oh, there.
Spencer Ririe: Oh,
Danny Norton: There he is.
Spencer Ririe: wrong camera
Danny Norton: That's a different angle.
Spencer Ririe: here.
Danny Norton: That's a good angle. I never seen that side of your profile. I don't know if I like that movie star.
Spencer Ririe: Yeah, hold on. Let me get this fixed because my uh I had to unplug my camera last night for some reason.
Danny Norton: Okay. So, Spence, um, we were just talking with Lloyd and just, uh, he's going to share his, uh, computer screen and we're going to kind of go through from there.
 
 
00:04:49
 
Danny Norton: I've got the the transcription going. I got the recording going for now. Um,
Spencer Ririe: Perfect.
Danny Norton: with Mario going to be going through some of the different flows uh, later on. My my thought was we're going to be going through a few more technical sides of things with with Lloyd. Is there anything specific that you want to see from him? He's We're going to just start with a uh a few line items of an order generation from his perspective. Um and then we can dive into anything else more technical. Uh but I know that you had some things that you you wanted to specifically
Lloyd Scrubb: Why
Danny Norton: see.
Spencer Ririe: Yeah, give me one second here just to get my camera sorted and then I can pull that
Danny Norton: Yeah, no problem. Lloyd,
Spencer Ririe: up.
Danny Norton: I was also wondering if maybe um it might be helpful for the Red Stamp guys if if you gave maybe give them an overview of what you needed to impart onto Mario so he could do this just sort of the theory behind it sort of thing.
 
 
00:05:44
 
Danny Norton: So they just have kind of a big picture sort of sort of uh you know overview of kind of you know you know you you built it.
Lloyd Scrubb: don't we why don't we go through the thing and that will be what I had to tell Mario to do,
Danny Norton: Okay.
Spencer Ririe: Yeah,
Lloyd Scrubb: right?
Spencer Ririe: that's
Danny Norton: Perfect. Okay. That's good. That's that's what I was getting at.
Lloyd Scrubb: Yeah.
Spencer Ririe: perfect.
Danny Norton: Perfect. Yeah.
Lloyd Scrubb: Well, well,
Danny Norton: That's awesome.
Lloyd Scrubb: going through is what you know is basically what I taught Mario to do,
Danny Norton: Yeah. Okay.
Lloyd Scrubb: but okay.
Danny Norton: Yeah.
Lloyd Scrubb: Sorry.
Danny Norton: Okay.
Lloyd Scrubb: I'm just uh I'm seeing a uh a weirdo thing here saying that there's picture and picture is open because you're screen sharing. I don't know what that means,
Danny Norton: Uh yeah.
Lloyd Scrubb: but I
Danny Norton: And if we just if like when you generate things, is that in a web browser window or is that going to be in uh like on your desktop?
 
 
00:06:25
 
Danny Norton: Because right now Okay.
Lloyd Scrubb: gonna be on my It's going to be on my desktop.
Danny Norton: So if you minimize the Google Meet,
Lloyd Scrubb: Yeah.
Danny Norton: then you'll be able to access your your desktop and we'll be able to see everything. So that's perfect.
Lloyd Scrubb: Ah,
Danny Norton: So we can see everything now.
Lloyd Scrubb: all right. Got it. There we go.
Danny Norton: All right.
Lloyd Scrubb: Upgrades to everything. Okay. So, uh so you sent me uh an invoice.
Danny Norton: Yeah,
Lloyd Scrubb: No worries.
Danny Norton: it's uh in it's invoice number 55.
Lloyd Scrubb: Okay.
Danny Norton: It's one of our matey groups. They got a bunch of different stuff on it.
Lloyd Scrubb: Can you see what I'm doing now? Oh, yeah.
Danny Norton: Yep.
Lloyd Scrubb: Okay, good. Okay.
Danny Norton: Here's
Lloyd Scrubb: So, um
Danny Norton: our
Lloyd Scrubb: basically the process starts with uh uh receiving a a digital order. So that would come in the form of a invoice. So basically uh we just download this to uh
 
 
00:07:23
 
Danny Norton: friend this not today. Not while we're
Lloyd Scrubb: here. Okay. Now, so it I've got my thing set up, browser set up for invoices to go into my uh downloads folder. That's the one there, Doug. PP11440 55 I don't I don't know I don't
Danny Norton: Yes. Yes. And Lloyd,
Lloyd Scrubb: know
Danny Norton: I just want to warn I want to warn you on one thing. There's a whole bunch of uh Amazon cards with one here,
Lloyd Scrubb: these
Danny Norton: one here, one here. So you know as an example they've ordered five 100s but they've got one one one and two sort of in so whatever whatever you are whatever you do here with explaining everything Mario will just take it over and finish it off if you know so you don't have
Lloyd Scrubb: Anyway,
Danny Norton: to go through this whole process of all these items sort of thing right so wherever you want to leave off Mario will take it from there sort of
Lloyd Scrubb: so we download the invoice and so basically um uh written a a program to read the invoice and generate all the uh the files for the different
 
 
00:08:30
 
Danny Norton: Oh, wow.
Lloyd Scrubb: uh cards that we and uh um that we'll send to the uh the customer. Um so I'll just go to the folder there. As I said in the email, everything is stored on my uh my Google Drive that both Doug and and Mario have access to. So that's how Mario
Danny Norton: Looks like we lost. Can you still hear Spencer?
Spencer Ririe: Yeah. Well, I don't think he's saying anything.
Danny Norton: Okay.
Lloyd Scrubb: You can't hear me?
Danny Norton: Oh,
Spencer Ririe: No, we
Danny Norton: now I can.
Lloyd Scrubb: Okay.
Spencer Ririe: can.
Lloyd Scrubb: No, Lord.
Danny Norton: This is what you do. You see all this stuff popping up code stuff. Yeah, but there
Lloyd Scrubb: just fill out.
Danny Norton: just following the process.
Lloyd Scrubb: Okay, so all the uh scripts that are used are in this folder. So, first thing we're going to do is uh uh read that invoice and basically generate a bunch of uh Wow, this feels like m I haven't done this for a while, man.
 
 
00:09:55
 
Lloyd Scrubb: I'm like, okay. Uh let's see. Python.
Danny Norton: mic hopefully.
Lloyd Scrubb: No, no. I I mean, I know what to do. It's usually I just I just recall commands on my thing.
Danny Norton: Yeah.
Lloyd Scrubb: So, now I'll just have to do it uh old school and and re uh that guy. Okay.
Danny Norton: This was
Lloyd Scrubb: So, that's the script. So, I I basically sent you basically these these steps here. So, this is a script that runs.
Spencer Ririe: Yeah.
Danny Norton: right.
Lloyd Scrubb: So, it's just a a Python program. It's going to bring up a dialogue and we're going to load the uh invoice into that. Okay. So, again, that will uh read the invoice and generate a bunch of folders. You'll see a bunch of stuff blow by on the screen here.
Danny Norton: That
Spencer Ririe: Okay.
Lloyd Scrubb: Since I haven't run this for a while, it's got to load all the different tools that it that it uh uses.
Danny Norton: way.
 
 
00:10:56
 
Lloyd Scrubb: So it'll complain for a bit and then it'll go through what it needs to do.
Spencer Ririe: Yeah,
Lloyd Scrubb: All this is uh built with stuff that's just freely available on the internet. So there's
Spencer Ririe: open source looks
Lloyd Scrubb: nothing.
Spencer Ririe: like.
Danny Norton: Yeah,
Lloyd Scrubb: Okay. So once that's done, so uh uh underneath this uh folder structure in my account here,
Danny Norton: heat.
Lloyd Scrubb: there's a orders folder. So that would have generated uh a bunch of uh things for each of the cars in the oldest folder orders folder.
Spencer Ririe: Okay.
Lloyd Scrubb: Um zooming on there. Let me just load the invoice so I can see what's um happening here. Just Amazon Loblas Esso. Oh, so they did it in multiple kind of.
Danny Norton: Yeah, I don't know why they did it that way, but um
Lloyd Scrubb: Okay. So anyway, so Amazon Loblas and Esso. So for Amazon,
Danny Norton: careful
Lloyd Scrubb: we generate those cards. So that will go through one program.
 
 
00:12:12
 
Lloyd Scrubb: If you can kind of see on the top lefthand corner here. So these are generation programs. So Mario must have those on his desktop too. Uh so we'll be running that. We'll be running one for Loblaws and we'll be running one for for ESO.
Danny Norton: Okay.
Lloyd Scrubb: So, um let's go to uh so the next step basically is to what what that program did was create folders with with uh so we'll go to the first one here. Let's just go to So okay. So it generated this folder here which basically has the invoice number plus just a tag which basically is the the time at which it generated that folder. Okay. So,
Spencer Ririe: Got it.
Lloyd Scrubb: when we're finished this process, we'll get rid of that and you'll just see folders like like here with no time stamp. But basically, uh so that allows me to run this many times and for whatever reason, it'll just keep different copies and you can get rid of or keep whichever ones you want.
 
 
00:13:05
 
Lloyd Scrubb: Um so, we'll go in here and in there should be an Excel file. U so ones that we just get inventory from. So, Doug orders cards and we keep inventory in the ESO folder. Um, and we're not going to generate these SO cards. We're just going to copy Earls that they provided us and then load them into to this this file here. And then we're going to save them and add an encryption pass add a password to that file.
Danny Norton: So just a a quick question on terms of logistics of that.
Lloyd Scrubb: Okay.
Danny Norton: That would be something if I'm not mistaken that you would go and pre- buy digitally from in this case ESO. Yes. And then you would have it in your inventory. Yes. Okay. So this is just the retrieval process of those except for Walmart which we generate ourselves. Okay.
Lloyd Scrubb: Uh well you still have to buy them but we anyway. So all the process are same.
Danny Norton: Right.
 
 
00:13:55
 
Lloyd Scrubb: It's just that what we do after. Okay.
Danny Norton: Okay.
Lloyd Scrubb: So um so we also have uh folders for uh with inventory. We have so cards and inventory that we can that we can use. So we would go to our inventory folder here and then find Sorry. See, this is how long I haven't done it. We' go to orders and under orders there'd be an inventory folder and uh we'd use we'd so and then inventory and there would be an inventory folder
Danny Norton: When you first started, you have a cheat sheet.
Lloyd Scrubb: there. The other folder I went to initially was basically if we're don't have any inventory here for the different denominations they need, then we'd go we had a process where we'd copy them there and then they'd get added into this location later. Okay. So, uh let's open up this file here.
Danny Norton: So, can I jump in with another question? Is that okay?
Lloyd Scrubb: Yeah.
Danny Norton: So in that in that situation where um you might not like do you always have inventory
 
 
00:14:57
 
Lloyd Scrubb: Yeah.
Danny Norton: ready readily available or is there potentially a circumstance where maybe a large order comes in depletes your stock and then you're in a situation where you need to replenish your inventory. Does that happen often? Yeah, we would replenish before we go through this process though. Okay. Like so if we don't if we don't have enough,
Lloyd Scrubb: Yeah.
Danny Norton: we would we would order it, get it there before we go through this process. Okay. Right.
Lloyd Scrubb: Yeah. So, so in the old days,
Danny Norton: All right.
Lloyd Scrubb: I think we used to have lots of inventory. So, basically when an order came in, I received it, then I would be able to just go and do it. But, so now it's kind of more order just in time processing like like the Japanese uh
Danny Norton: Makes sense.
Lloyd Scrubb: do. Okay. So,
Spencer Ririe: And is that is that triggered I guess Doug like when a a new order comes
Lloyd Scrubb: uh,
Spencer Ririe: in that that you've got in front of you and I guess I'm curious what the trigger is and who the person is that makes that determination.
 
 
00:15:59
 
Spencer Ririe: Oh, we just got a big order in. I don't think we have enough. And then who goes and
Danny Norton: uh I I would be responsible for that,
Spencer Ririe: checks?
Danny Norton: but Mario has now leared to do that. So that's what we call, you know, ordering our inventory, right? And basically what we're doing is we're tracking from a year ago because our sales are almost identical
Spencer Ririe: Yeah.
Danny Norton: from what they were a year ago in general terms.
Spencer Ririe: Right.
Danny Norton: So we're tracking and sometimes we we move out like a two week time span. Sometimes it's a whole month ahead, right? For grocery, we would never go a month out because we sell too much of the stuff, right? So, we're just every day Mario or I are checking a year
Spencer Ririe: Yeah.
Danny Norton: ago to see what we might need and we're ordering every day, but obviously we're going to get large orders that are unanticipated and then we have to order in get it in before we'll even, you know, let Lloyd know that the invoice is paid sort of
 
 
00:16:56
 
Spencer Ririe: Got it.
Danny Norton: thing.
Spencer Ririe: Okay.
Lloyd Scrubb: So yeah, so the trigger is a payment of an invoice. So they're not getting their cards until they
Danny Norton: Yes. Yeah. That's
Lloyd Scrubb: pay.
Danny Norton: it.
Lloyd Scrubb: And here we have uh 200s and 1250. Okay. So we just go to uh these uh inventory files that have uh will tell you what's stored inside of them. So, uh, but if we're if we're lucky, we have everything we need in this one file. Okay. So, 200s there. So, we would copy the um the invoice number and the uh stuff from inventory. we'd mark that it's been removed from there. So, I'm just going to
Danny Norton: It's a pretty manual process. It's a pretty manual process.
Lloyd Scrubb: Okay, so there's 200s that we're going to grab. So,
Danny Norton: Yeah.
Lloyd Scrubb: just date that the order was made. That's on the file 2026310. So, we'll add that in there as well.
 
 
00:18:52
 
Lloyd Scrubb: These guys did they change their uh do they have multiple customer number? These guys may nation of
Danny Norton: Yeah.
Lloyd Scrubb: Alberta.
Danny Norton: Yeah. And the the other thing too, Sloyd, if you're if you want to do like at the Amazon different denominations, we can tell you how many are uh you know, how many they ordered rather than you having to look up and down that whole invoice, right?
Lloyd Scrubb: All that information is in the file, right? They ordered. That's what this
Danny Norton: In the PDF,
Lloyd Scrubb: is.
Danny Norton: you mean on in what? Which files? Sorry. Or or you mean the invoice or
Lloyd Scrubb: That tells you here like we know that uh they'd ordered two. So hundreds and one Yeah. Yeah.
Danny Norton: Okay.
Lloyd Scrubb: So I don't I don't have to look in the voice. I just need to get information to put in here.
Danny Norton: Okay.
Lloyd Scrubb: Yeah.
Danny Norton: Okay.
Lloyd Scrubb: Yeah. We have a convention of uh of not having this guy u we just
 
 
00:19:48
 
Spencer Ririe: Right.
Lloyd Scrubb: alternate the color so it's easy to look in the file and see what was was ordered.
Danny Norton: Yeah. So,
Lloyd Scrubb: Oops.
Danny Norton: okay.
Lloyd Scrubb: So we got two of those guys. And here's the information that we need to transfer into the uh into the uh and this is what the customer is uh going to get. And then apparently a a date of when these cards were activated. Okay. So, basically we're just transferring information and then we need 1250.
Spencer Ririe: Right. And and this being sort of a fairly manual,
Lloyd Scrubb: Sorry.
Spencer Ririe: you know, select and edit is is kind of a process that could be somewhat
Danny Norton: I
Lloyd Scrubb: Correct.
Spencer Ririe: brittle if if mistakes are made. Now, is that common that that ever happens?
Danny Norton: would say no.
Lloyd Scrubb: Yeah,
Danny Norton: Not really.
Lloyd Scrubb: it's not. But but yeah,
Danny Norton: No. Well,
Lloyd Scrubb: I mean it's Yeah,
Danny Norton: we just I think it's I think it's because we have good people doing it,
 
 
00:21:00
 
Spencer Ririe: Yeah.
Danny Norton: right?
Lloyd Scrubb: sorry.
Danny Norton: So, if you if you went down the path and we were selling more and more cards,
Spencer Ririe: Yeah.
Danny Norton: we have multiple people doing it. There would be more mistakes. It's just that Lloyd is on top of it and he's trained Mario well to be on top of it.
Spencer Ririe: Yeah.
Danny Norton: So,
Spencer Ririe: Yeah. And I assume it it also uh means having to go a bit slower just just knowing that you don't want mistakes. Um so but yeah. Okay.
Lloyd Scrubb: Yeah. No. Yeah. If there Yeah. So I think I mentioned the thing if there's a if we come up with a a a standard format like so if we just kept a uh I don't know if it would be one growing anyway some procedure for just having the inventory uh whether it's full or not in a in a standard uh configuration then it could easily write the program to go into the inventory file grab those things and once the program has been tested then that could eliminate those types errors all together.
 
 
00:22:03
 
Lloyd Scrubb: Yeah,
Danny Norton: Yeah.
Spencer Ririe: Yeah.
Danny Norton: Wow.
Lloyd Scrubb: right now it's manual. Okay.
Spencer Ririe: Okay.
Lloyd Scrubb: And uh so the 250 we'll grab this guy here.
Danny Norton: Amazing. Ready?
Lloyd Scrubb: That's all we uh need for this file. So, we're going to save that. But then we uh need to processes, but I leave the cursor in the last nice uh guy. Oops. Sorry. Save. Hey. Oops. All right. So, this guy is good. We just save it now. Uh, so save. And then we're going to add an encryption
Danny Norton: And in this situation like that,
Lloyd Scrubb: password.
Danny Norton: is this a file that's shared across that you'll have access to as well? Yes, I can just access the Google Drive and uh it will be there. Perfect.
Spencer Ririe: And then when it comes to adding passwords here, is there a consistent password that gets used or how are you deciding what to use for this?
 
 
00:24:11
 
Lloyd Scrubb: is in the invoice.
Danny Norton: It's all the
Lloyd Scrubb: So these guys these these guys these guys without the uh
Danny Norton: voice
Spencer Ririe: Okay.
Lloyd Scrubb: dash
Spencer Ririe: Okay.
Danny Norton: and without the letters. No letters. There's no letters.
Lloyd Scrubb: Okay.
Danny Norton: No letters, no dashes.
Lloyd Scrubb: Okay.
Danny Norton: Okay.
Lloyd Scrubb: I mean, could be anything. We just have to tell the customer what what it is and we usually just describe what the know the password is and it doesn't doesn't change. Okay. Um saved. It should tell me if it didn't. Okay. So that would be that guys done. Nothing else for these types of ones. There's nothing else to be done. Uh so I basically just go here and remove the uh so now Amazon should start now. Okay.
Danny Norton: Spencer, are there any uh more behind the scenes technical questions that you had in mind to talk to Lloyd about specifically?
Spencer Ririe: Um I guess one yeah a few questions.
 
 
00:25:34
 
Spencer Ririe: Um because it seems like we'll likely be able to get more of this walk through like the tactical stuff with with Mario. Um so I'm curious when it comes to the
Danny Norton: Yeah.
Lloyd Scrubb: Okay.
Spencer Ririe: actual sort of scripts and programs. Is there anything that needs to be done?
Danny Norton: Heat.
Spencer Ririe: You know I I saw you know Python being involved, Apache. Is there any sort of um like ver you know version control that needs to happen with those scripts as far as if Python releases a new update that ends up being installed on the machine that's running the scripts. Does that, you know, impact any of the the scripts that you've run?
Lloyd Scrubb: Um, I imagine it would, but there's no unless there's something a new feature that's required by for I don't there's no auto download of the latest version of Python.
Spencer Ririe: Okay.
Lloyd Scrubb: Yeah. Oh, if that if that happened then there must have been a like in the generation of these scripts
Spencer Ririe: Um,
Lloyd Scrubb: then that would have done it would have been tested it would have been stored on this uh on this uh on that folder there.
 
 
00:26:56
 
Lloyd Scrubb: So we're not using like git or any version control. So there are other versions of the of the of the files being stored but so for instance if I had to make a change because something was broken then I would I would um attach that. So any any work that I'm doing for Doug I have to put I'm putting into a calendar like a Google calendar so which he has access to and any anything that I did is is noted there and then I would
Spencer Ririe: Yeah.
Lloyd Scrubb: have copied the version of the script that got updated with that last whatever work I did for for Doug. So there's different copies there so he could go back in the calendar as long as Google doesn't lose
Spencer Ririe: Okay.
Lloyd Scrubb: its disc drive and get any any previous versions of stuff. But yeah, so that's yeah,
Spencer Ririe: Yeah.
Lloyd Scrubb: I'm no I'm the only person doing any development or doing anything.
Danny Norton: There.
Lloyd Scrubb: So in terms of uh you know,
Spencer Ririe: Okay.
Lloyd Scrubb: so it's well it's not like a multi-user development environment for at least for this sort of stuff for this
 
 
00:27:53
 
Spencer Ririe: Got it.
Lloyd Scrubb: stuff.
Danny Norton: Are there situations where Mario like tries to go and and run something and then all of a sudden not something's
Spencer Ririe: And
Danny Norton: broken, it doesn't generate? Like, have you experienced any
Lloyd Scrubb: Yes. So,
Danny Norton: errors?
Lloyd Scrubb: so when we went to um so up until like this year, I always did this and you know we we we purchased a laptop and all the development was done from this
Danny Norton: Okay.
Lloyd Scrubb: laptop. All the generational cards was done from this laptop. Then when uh I I installed the different software that had to be got installed on Mario's computer, the scripts are common, but there were issues with things not not running. So, I guess it was probably related to then I had to install the latest version of Python on Mario's computer. So, I'd never have any problems on my computer, but Mario run it, it wouldn't run. So, then I'd have to go debug, find out what happened, update the scripts, and then and then republish it there.
 
 
00:28:48
 
Lloyd Scrubb: So as as far as I know, so there are some things like uh uh lines in Python that when run on Mario's things generate some kind of a output to the console, but it still generates the the f produces the file. So uh and Mario lets me know when uh for instance things I think he's worked around some things, but I think he lets me know when like if this if it doesn't work at all, you know, doesn't generate the scripts that he expects.
Spencer Ririe: Okay. And when that happens, does it post like any sort of error message or log to the console?
Lloyd Scrubb: Oh, anything like well for this one if uh um you know so for instance one of the things that happened was uh uh we read the uh the uh invoice and you can see on this screen here it's put in the it's populated the customer here. Um, so when Mario ran it, there were instances where it wouldn't populate the customer in these these files here. And so he would know that. So I guess if he saw that, he would say, "Oh, there's no customer." And he would type it in
 
 
00:30:00
 
Lloyd Scrubb: manually. So it would, you know, and when these scripts are run, it's generate, you know, so for me, you know, I don't care. I put everything that's happening on the screen. So this is all stuff that nobody cares about. But it's basically I can go through this and read okay it identified you know all these things. So if something does happen I can go back here and say why didn't it? So there have been instances where invoices have had weird formats or whatever the uh different people running on different computers. They it runs on computer X they generates the invoice was created on one computer and the
Spencer Ririe: Right.
Lloyd Scrubb: output of that invoice behave differently than the output of an invoice created on a different computer
Spencer Ririe: Are we
Lloyd Scrubb: in Doug's office. So th we've run into lots of those types of things where we've had to I've had to go in and figure out why is it
Danny Norton: Yeah.
Lloyd Scrubb: work when it's generated on this one and just put it around.
 
 
00:30:53
 
Lloyd Scrubb: So I've over time fix it so that it try and eliminates all the different inconsistencies on the on what's happening on on the different computers.
Danny Norton: It's reversed.
Lloyd Scrubb: But yeah, so there's output here. So if you're reading the output, you should be able to see whatever is put here should end up exactly in the file. If that's not working, you would you would see an error.
Spencer Ririe: Got it.
Lloyd Scrubb: Or if something actually broke, it would the program would crash and you would see it here and we'd be able to figure out. So if I was doing it, I'd just be I'd go and debug and figure it out and then run it
Danny Norton: Makes
Lloyd Scrubb: again.
Danny Norton: sense.
Lloyd Scrubb: You'd have to but you'd have to notice,
Spencer Ririe: Um,
Lloyd Scrubb: you know, these things.
Danny Norton: Absolutely.
Lloyd Scrubb: So what would happen if uh if the if uh you know so then if this didn't put a customer name in
Spencer Ririe: yeah.
Lloyd Scrubb: here and then we went to run one of the generation programs then uh um it would it would complain that there's no customer in the thing.
 
 
00:31:48
 
Lloyd Scrubb: So then he would say what he's done he said oh it didn't this isn't running and then it was because there was no customer there. So we've identified that issue and solved that type of invoice where we don't do generation then there'd be no damage. If information is not put here then for these ones we don't put the customer name in those files that are generated. So it wouldn't really it's more when we run our program to to create that screw up here would would uh affect the output but Amazon. So that's well uh the process is slightly different there but uh um so you
Danny Norton: Why should I just do the 10? Why don't you just do the one $10 one,
Lloyd Scrubb: see
Danny Norton: Lloyd? Then you don't have to go through all the different denominations or whatever. Does that work or are you
Lloyd Scrubb: I can do I can I can do laws is less cards.
Danny Norton: just whatever
Lloyd Scrubb: I don't care. Isn't it actually?
Danny Norton: whatever you need to show them what you want to show them.
 
 
00:32:53
 
Danny Norton: So you
Lloyd Scrubb: Well, maybe. Well, okay, let's go through let's go through the amalite. Yeah, I think uh the laws depends on whether we'll do generation depends on whether we're using old inventory or new inventory because now they're giving us cards that we don't generate. Right.
Danny Norton: Right. Right. Right.
Lloyd Scrubb: Okay.
Danny Norton: Okay.
Lloyd Scrubb: So,
Danny Norton: So,
Lloyd Scrubb: let's go here.
Danny Norton: does that mean the procurement process is different or it's changed? No. Basically, what was happening is there was a field that I thought it was mandatory to fill in when we were ordered and it had from Progressive or whatever and then Lloyd had delete that out because it was going to a client. They didn't want to say the card was from Progressive. So, then we figured out that it wasn't a mandatory field. So now that's no longer there, but some of that old stock Lloyd has to or Mario has to delete things and fix those before they can send it
 
 
00:33:42
 
Lloyd Scrubb: Okay. So, let's do uh let's do this guy.
Danny Norton: out.
Lloyd Scrubb: Um
Danny Norton: So Lloyd Lloyd what I what I did on this invoice is I I I
Lloyd Scrubb: that's like No, it doesn't. It it doesn't matter. You don't have to explain. It's just funny. Say because usually I I'm thinking that uh yeah,
Danny Norton: add
Lloyd Scrubb: it just does it in the order of that we we get it. Like if they were all done together, then it would produce done. But it it doesn't matter. It's this this this should this will this will be fine. So, let's go to inventory for uh for um
Danny Norton: this is the only voice I've ever seen.
Lloyd Scrubb: uh do we have every everything
Danny Norton: Someone does. We need
Lloyd Scrubb: from for Amazon here? There's inventory Amazon.
Danny Norton: 10.
Lloyd Scrubb: Okay, good. And uh so if we look at this quickly, we need uh 25s, 50s, hundreds, and 250s. Okay, let's start 25s,
 
 
00:34:42
 
Danny Norton: And T.
Lloyd Scrubb: 25 and 10.
Danny Norton: He did one.
Lloyd Scrubb: Okay, that's still here. This has the most guys on it.
Danny Norton: Yeah.
Lloyd Scrubb: and then we'll go for 250 at the end. Are there any 25s in here? Yes. So,
Danny Norton: I see help them with Yeah.
Lloyd Scrubb: one two 25s. I'll just I'll just speak out out loud and then you can tell me.
Danny Norton: 22.
Lloyd Scrubb: Uh, okay.
Danny Norton: Yeah.
Lloyd Scrubb: So, 225. So, let's grab that guy.
Danny Norton: You You're in
Lloyd Scrubb: Let's just put one here.
Danny Norton: charge
Lloyd Scrubb: I'm going to change the color of this guy or I'll just leave it like that for now. And I'm going to copy
Danny Norton: in ever.
Lloyd Scrubb: this.
Danny Norton: I've never seen an order like that. We chose the hardest order there.
Lloyd Scrubb: Yeah, it doesn't matter. So 225. Is that what we said? Oh my god.
Danny Norton: That's a good example though.
Lloyd Scrubb: Why is it
 
 
00:35:30
 
Danny Norton: That's a actually good to see. Yeah. Usual
Lloyd Scrubb: okay?
Danny Norton: one.
Lloyd Scrubb: So, 225s.
Danny Norton: So Danny, this is not typical. These are March is a busy time for us,
Lloyd Scrubb: Okay.
Danny Norton: right? Yeah.
Lloyd Scrubb: How many uh
Danny Norton: So this two 50s.
Lloyd Scrubb: 50s?
Danny Norton: This one wants five and five and 10, right? This one wants This is a good size one. This is our most hassle order because this is a group that doesn't order that much, but they always order a whole bunch of different denominations. Takes to do this this client and every time we see it,
Lloyd Scrubb: is Oh,
Danny Norton: we go,
Lloyd Scrubb: come on.
Danny Norton: right? So yeah. So that's,
Lloyd Scrubb: God.
Danny Norton: you know, everybody. I'll show you another one. That's a
Lloyd Scrubb: Okay. 250s. Excellent.
Danny Norton: 250s.
Lloyd Scrubb: Yeah. Okay. Nice. All right.
Danny Norton: So that's uh
 
 
00:36:30
 
Lloyd Scrubb: And more on that. How many hundreds?
Danny Norton: 5100s.
Lloyd Scrubb: 5100s. Oh, it's probably going to make me copy it again. Okay, I understand how it works. Okay, 5100s. Hopefully, we have five. Nice. Okay. Okay. And I think that's it for this file, right?
Danny Norton: Oh yeah, there's two 250s as well.
Lloyd Scrubb: Yeah.
Danny Norton: I'm not sure if there is
Lloyd Scrubb: I don't think those are in this I don't think those are in this file.
Danny Norton: So So that's more This is one of our regular sort of Yeah. digital people that are once a month and this is a
Lloyd Scrubb: Oh, there's tens here, too. Okay. So, uh you're probably wondering why I did this, Mario. So, this is the reason. So, I uh whenever I create these files,
Danny Norton: Yeah.
Lloyd Scrubb: I just freeze the top uh column there so that when we're scrolling up, I can see what the column things are and what the way is freeze panes.
 
 
00:37:31
 
Lloyd Scrubb: And then we freeze the top row. That way when we're scrolling then it keeps there and I can see what what's in there. Okay.
Danny Norton: Yeah.
Lloyd Scrubb: So we did 2550s and hundreds, right?
Danny Norton: Yeah.
Lloyd Scrubb: Okay. Perfect. So there's no more there's no tens in this file. So when uh when I do that, I would remove tens off of the uh which maybe you did. I didn't I can't off of the file name so that to go into the file if there's no tens. Okay. 25s. All right. So, we need to grab these guys.
Danny Norton: So the 250s, there's none in that file. He has to go get it in the other file. No, the 25 cities.
Lloyd Scrubb: Oh,
Danny Norton: Oh,
Lloyd Scrubb: it's only great. It's one at a time because uh so this is this is more complicated than the usual.
Danny Norton: yeah.
Lloyd Scrubb: Okay. So, 125 here.
Danny Norton: How come one at a time Amazon?
 
 
00:38:25
 
Danny Norton: You have to do one at a time. You have Yeah, you have to do like one um denomination at a time. So like you copy the 25 first and then when Yeah.
Lloyd Scrubb: 25 here. Sorry. Yeah.
Danny Norton: So
Lloyd Scrubb: So, this is this is likely introducing potential for more errors.
Danny Norton: for
Lloyd Scrubb: 125 here like the way that this file is. Okay. And the other 25 here. Guys, we have uh four people looking here. So,
Danny Norton: No pressure, Lloyd.
Lloyd Scrubb: yeah, but you should be you should be reviewing my work. Okay, so then 50s. Okay, so those guys are done. So, we would do this. All right. Yeah, it's not great to have to sit here sit here and watch this, but Okay.
Danny Norton: He should be make sure he's properly
Lloyd Scrubb: Okay. Now, the 50s. Okay. 250s. Nope. Okay. So, we grabbed this guy. Okay.
 
 
00:39:47
 
Lloyd Scrubb: Go down to the 50. That's all. put 50 in there. Okay. And then let's do
Danny Norton: thing left is the car and the
Lloyd Scrubb: Okay, perfect.
Danny Norton: right
Lloyd Scrubb: And then hundreds guys don't have nothing has to happen there. Okay, then uh hundreds here. So, oh, we're in the hundreds. Okay. Okay. So, we have two together, one together, two together. Perfect. Hundreds. Okay. So, grab these two. these two.
Danny Norton: So mate of Alberta that's a previous order they took a bunch of this right so they they
Lloyd Scrubb: So then there's a whole
Danny Norton: would invoice to order this this nomination
Lloyd Scrubb: Okay.
Danny Norton: could be like on the on the Excel sheet there's like all the cars that we use. I think like the previous one was Native Child Toronto. So we always keep track of like which car.
Lloyd Scrubb: Okay. And then there's two there.
Danny Norton: Yeah. Also the yellow there is the he's working on right now.
 
 
00:41:33
 
Danny Norton: Yes. We we just like this color coded. Yeah. Sure. Yeah. I remember that from seeing this stuff before. he does it different each time, right? We discuss each each of those. So, while Lloyd's doing that part, um when you deliver and fulfill the order to the client, the like the customer gets individual Excel spreadsheets based on the different uh merchants. Okay? And then they disseminate that to their customers, they whatever they want to their their own people that they're sending it to. For this one, there's uh one, two, three, four different merchants. They did four different Excel files. Yes. Okay. Think it's called a zip file. Excel or zip file depending on which form of it.
Lloyd Scrubb: Right.
Danny Norton: Zip is PDF stuff.
Lloyd Scrubb: Okay. And now we need two 50s. And you said tens. Oh,
Danny Norton: 110.
Lloyd Scrubb: 110. There it is. Wow.
Danny Norton: They got everything lighter.
 
 
00:42:47
 
Lloyd Scrubb: So there's no more tens in here,
Danny Norton: I think that's good.
Lloyd Scrubb: right, Mario?
Danny Norton: No, I think we use all of those for best
Lloyd Scrubb: So I'm gonna Yeah. Yeah. So I would just So you I mean it doesn't matter if it says none in there,
Danny Norton: life.
Lloyd Scrubb: but so 250 and uh Okay, now let's go with 250.
Danny Norton: and explain to Danny what is the what we call Lloyd's files and your files you know what I mean how they got that backup and when it switches and
Lloyd Scrubb: Okay. 250. So, there's just one and Oh, no.
Danny Norton: something.
Lloyd Scrubb: There's two 250s. Okay. Perfect. Okay. Oh, and this is an empty file. Wow. Beautiful. Okay.
Danny Norton: So that means no one there's not not anything been ordered from that specific one. Means we just ordered them a few days ago and they've not been no client
Lloyd Scrubb: Yeah. Okay.
Danny Norton: yet.
Lloyd Scrubb: Sorry if I'm messing up your system there, Mariel.
 
 
00:43:49
 
Lloyd Scrubb: Okay. And these guys because you maybe may have used a different file than I'm using now. I doesn't matter, but may matter to my Okay.
Danny Norton: Mario's leaving us anyway,
Lloyd Scrubb: Okay.
Danny Norton: so it's okay.
Spencer Ririe: Mhm.
Danny Norton: It's
Lloyd Scrubb: Okay. So, 250. So,
Danny Norton: files.
Lloyd Scrubb: we'll go to the top guy here. Goodness, this guy here. Okay. Perfect. Then the famous 10. All right. Let you do what you like there, man. Oh, yeah. It doesn't matter. Good. Save.
Danny Norton: There's
Spencer Ririe: And what does that 38 number represent on that inventory
Danny Norton: another
Lloyd Scrubb: How many f How many cards are left in that file?
Spencer Ririe: sheet?
Lloyd Scrubb: Okay. Uh 10. It just counts down. Yeah. Okay. So, um 10 famous 10. Okay. 33 left. Okay.
Danny Norton: blow. I send it to Mario. He puts it into a file.
 
 
00:45:22
 
Lloyd Scrubb: May
Danny Norton: So, he'll he'll that part. Okay. Well, well, basically what what I'm getting at is let's say it's well those 250s, right? And let's say we've got we noticed we're low and we have two 250s that are still left. There'll be only 10 more, but those have not been used yet. So, or that's in English that needs one of them. Yeah. He'll take that one. It won't even know that this file is there yet. And then the next order, let's say they need two, so we only got one left. Then at that time, he takes this file and he moves it into this. Okay. So, can you explain this? We I call it your file and Lloyd's file. But can you explain to them what what the that process is or what? So, it's like grocery report. So, as soon as we get more cards, we order it and then um when whenever the cards are ready, the merchants send to us or let us know.
 
 
00:46:19
 
Danny Norton: download it and then I move that to like to the general inventory which is like what we call like my Mario's folder. Yeah. And then whenever we are filling an order and then we see we need more card that we don't have enough and then we go from there grab from there and then put on the on the merchants inventory individually as we Okay. So it's sort of like a holding tank that sits there until we need to go to it and we go to it. It's no different than this. Yeah. When we need to fill an order we go and grab it.
Lloyd Scrubb: Okay.
Danny Norton: That looks
Lloyd Scrubb: Good. Okay. So, uh so we're finished with with this guy. Uh so,
Danny Norton: good.
Lloyd Scrubb: Amazon needs to be uh so that's all Amazon gives us. That's why we have to generate the cards. They don't give us a Earl or or anything. So, uh, we'd save that guy and then run this program up here in the top right.
 
 
00:47:11
 
Lloyd Scrubb: So, they're all kind of listed.
Spencer Ririe: Okay.
Lloyd Scrubb: I think you can see. So, you don't see this. I guess you can see my whole desktop, right?
Spencer Ririe: Yeah.
Danny Norton: We can see the like the the means covering but I can see the the Amazon one.
Lloyd Scrubb: Okay. Oh, this. Okay. So, yeah. So,
Danny Norton: Yeah.
Lloyd Scrubb: there's just a list of all the the ones there. Okay. Um, so, uh, double click on that guy. It's going to prompt for an Excel file.
Danny Norton: Same time.
Lloyd Scrubb: Um, okay.
Danny Norton: Yeah.
Lloyd Scrubb: So, you go search for it on the disk, which is uh, no, not there
Danny Norton: Did you click it? Is it open? No,
Lloyd Scrubb: orders. Whoops.
Danny Norton: you can't open.
Lloyd Scrubb: Amazon number and then takes that
Danny Norton: I can't. Oh, I see. We're gonna have Don't do that.
Lloyd Scrubb: as input. Okay. Uh,
 
 
00:48:02
 
Danny Norton: Okay.
Lloyd Scrubb: so when we run that guy, it's going to
Danny Norton: So what is this? What's doing right now? It's generating the for the Amazon.
Lloyd Scrubb: Okay. So, uh those files that got generated This uh folder here is what's generated or as a result of running the Amazon. So any of these programs that we run on the white side there, we'll put the resultant folder here. So we will copy this guy, paste it in the uh in the folder here. Mario, these guys, do they take uh do they want uh zip files or do they want uh URLs?
Danny Norton: Let me check over here.
Lloyd Scrubb: I'm thinking they're zip file or URL guys, but uh I'll let you check. So, what would happen is I'd have my calendar there and I would before creating their thing, I would have pulled up a previous order and then uh I would see what they would expect for their their gift cards and then I' I'd know what to name URLs.
Danny Norton: There have been
 
 
00:49:57
 
Lloyd Scrubb: Okay. So
Danny Norton: URLs.
Spencer Ririe: And are those the only two like customer preference options is a zip file or
Lloyd Scrubb: because
Spencer Ririe: URLs.
Lloyd Scrubb: yes, but they only have that option for cards that we generate. Otherwise,
Spencer Ririe: Got it.
Lloyd Scrubb: they just get whatever the uh the uh vendor provides. Okay. So for URLs, we need to um uh so what I would do is next would be go in here. I would just check that everything uh got generated uh properly. So there are the folders for each of the uh the types.
Danny Norton: from
Lloyd Scrubb: So uh in the old days I'd be able to remember I believe there were five 100s,
Danny Norton: merchant.
Lloyd Scrubb: right?
Danny Norton: 5100s.
Lloyd Scrubb: Yeah.
Danny Norton: Uh, yeah,
Lloyd Scrubb: So I go I go check that there were five in there PDF files
Danny Norton: that's correct.
Lloyd Scrubb: and 220. No.
Danny Norton: 25 when we generate.
Lloyd Scrubb: Okay. So 225s.
Danny Norton: Yes.
Lloyd Scrubb: Okay.
Danny Norton: Right.
 
 
00:50:55
 
Danny Norton: So,
Lloyd Scrubb: Five 250s.
Danny Norton: Amazon 550.
Lloyd Scrubb: No, two 250s. Okay.
Danny Norton: Oh, yeah. 250.
Lloyd Scrubb: 250s.
Danny Norton: Sorry.
Lloyd Scrubb: How many 50s?
Danny Norton: 50.
Lloyd Scrubb: Two.
Danny Norton: Yeah. We're doing loss now. No,
Lloyd Scrubb: Okay.
Danny Norton: no, we're just validating. Oh, I see.
Lloyd Scrubb: Yeah.
Danny Norton: And then
Lloyd Scrubb: And then 110. So that's what I would do.
Danny Norton: one
Lloyd Scrubb: So that would be Thanks. So I'd be, you know, uh you would just go through quickly verify. So, so if that's good,
Danny Norton: Q.
Lloyd Scrubb: then we are pretty sure that this zip file grabbed those things and put it in there. So, the next thing we would do is then uh uh go to uh system bind.
Danny Norton: What do those uh PDFs look like?
Lloyd Scrubb: Okay.
Danny Norton: Oh, well.
Lloyd Scrubb: So, that's what they information we
Danny Norton: Okay, sounds
Lloyd Scrubb: just created that anybody who's an artist could go in there and make them uh look better if they
 
 
00:51:51
 
Danny Norton: good.
Lloyd Scrubb: want. But nobody nobody's complained.
Spencer Ririe: One other one other question for you, Lloyd. Um, when you initially ran that Amazon program there that's on the desktop,
Lloyd Scrubb: Yeah.
Spencer Ririe: you know, obviously we saw it pulling and doing some work, but then it just like closed. you know,
Lloyd Scrubb: Yeah.
Spencer Ririe: I didn't see is there a success message or is there anything that lets you know who whoever the operator is know that it completed successfully? Is there ever a you know an op a chance that that script doesn't run to the end to generate all of the PDFs?
Lloyd Scrubb: Um there's a well so the last thing that you would you may not have noticed orever. So basically what happened at the end there was uh it went through it and generated all the cards. So usually it counts. So you would be able to see that it generated whatever number of cards and so you would be able to say oh there's x number of cards should be generated.
Spencer Ririe: Yeah.
 
 
00:53:01
 
Lloyd Scrubb: The last thing it does is it creates the zip file. So you would have seen go through the screen it would have been saying would have been showing you know 500s go all the files going into a zip file. So that's that's so so you knew it was going through that process.
Spencer Ririe: Yeah,
Lloyd Scrubb: And then the final thing for me is just to go through and and make sure that they in fact did generate.
Spencer Ririe: got it.
Lloyd Scrubb: So So to me it it looked so to me it looked like it was successful because it went through the process
Spencer Ririe: Okay.
Lloyd Scrubb: of generating all the individual cards. If if a card failed so sometimes what happens especially when we're doing laws because it seems that they their site goes down sometimes or it takes a long time. So you will see retries. Okay. So, but then if you see a retry, but then it comes back with the same number that should have been it would have attempted number 20 and it says 20, then you would know.
 
 
00:53:52
 
Lloyd Scrubb: So, those are those types of things happen. So, this is what I'm doing. Here's a final check. But if you see it go through the creating the zip file, then you know 99% it completed successfully. So, this is just me going to check that anything. I mean, I could put a delay there for it to hold so that you could see and you know, but um I just go here and check that all the cards were were a thing. And I you don't have to count the cards. You just go and look at the the thing there and you you and that kind of
Spencer Ririe: Yeah.
Lloyd Scrubb: gives you the the idea.
Spencer Ririe: And I see the desktop configuration settings file that is in the fold folder
Danny Norton: Yep.
Spencer Ririe: here. And then there's that same files in each of the individual denominations. Is that what is that file
Lloyd Scrubb: Sorry.
Spencer Ririe: for?
Lloyd Scrubb: Which that Oh, that file. That's a Windows thing. I I have no idea.
 
 
00:54:46
 
Spencer Ririe: Okay. So that's just something that Windows is creating. And then
Lloyd Scrubb: Yeah. And I'm going to guess I'm going to guess that everybody has it,
Spencer Ririe: the
Lloyd Scrubb: but it's typically hidden and some and somehow I did something to make it
Spencer Ririe: hidden correct.
Danny Norton: Yeah,
Spencer Ririe: Okay. To show them.
Lloyd Scrubb: unhidden.
Danny Norton: probably have like those.
Spencer Ririe: Yeah.
Lloyd Scrubb: Yeah.
Danny Norton: Yeah, that makes sense to
Lloyd Scrubb: Yeah. Yeah. Okay. But anyway,
Danny Norton: me.
Lloyd Scrubb: yes.
Spencer Ririe: And then the the gift card log file.
Lloyd Scrubb: So that's
Spencer Ririe: That's also there.
Lloyd Scrubb: Yeah.
Spencer Ririe: What is that file?
Lloyd Scrubb: So basically that's a an Excel file that's put inside of the the zip file that basically has a catalog of all these uh of all the what's in Okay, I can go in there and show you.
Spencer Ririe: Got
Lloyd Scrubb: So basically it has a inventory of what file and what's denomination for the
Spencer Ririe: it.
 
 
00:55:35
 
Lloyd Scrubb: file.
Spencer Ririe: And is that is that something that's generated by that Amazon um script
Lloyd Scrubb: Correct.
Spencer Ririe: that you ran?
Lloyd Scrubb: Correct. And and that's required for when we upload this.
Spencer Ririe: Okay.
Lloyd Scrubb: So that's embedded in that that zip file that when we upload it to systembind and they're going to create web pages for each of these cards, they use that as kind of a catalog and then they could sort of coincide that. So inside the zip file, there's going to be folders just like the folders we went into and they'll be able to use this as a backup to match to make sure everything kind of
Danny Norton: Sorry,
Lloyd Scrubb: matches.
Danny Norton: I missed that part. The websites created. Sorry, what was that?
Lloyd Scrubb: We're about to get there.
Danny Norton: Okay.
Lloyd Scrubb: I haven't done that yet because we've been talking about this yet.
Danny Norton: Okay, jump the gun.
Spencer Ririe: Okay.
Lloyd Scrubb: Not yet. No, no worries. But yeah, I I left I put that in the notes, too.
 
 
00:56:25
 
Lloyd Scrubb: I sent you. Okay. So, uh so if if you need uh um if if we
Spencer Ririe: Hey
Lloyd Scrubb: were going to send them a a zip file, then we would just encrypt this guy and then we're kind of done. But customers who need URLs, then we have to get them to generate them and then they're going to give us an Excel file with all the URL Earls. So I'll go through that process now. So that's uh we go to system bind. Uh that's that that's uh that's the company that's done that for us. You can see this I assume. Okay.
Danny Norton: Yep.
Spencer Ririe: Yeah.
Lloyd Scrubb: Um so we have to go here and uh Oh, come on. You better remember the
Danny Norton: big fraud about three years ago and one of our top clients digital recommended this
Lloyd Scrubb: There we
Danny Norton: company our security.
Lloyd Scrubb: go.
Danny Norton: Yeah, they're a secure company security company.
Lloyd Scrubb: Are you kidding
Danny Norton: So,
Lloyd Scrubb: me?
 
 
00:57:34
 
Danny Norton: do you have to do you go into system?
Lloyd Scrubb: All right. So they provide this this functionality here where we can uh choose a uh a zip
Danny Norton: Yes.
Spencer Ririe: And
Lloyd Scrubb: file. Uh basically the only uh checking it has is that if you try and upload a zip file with the same name then uh it's going to reject you.
Danny Norton: Okay.
Lloyd Scrubb: Okay. Okay. So, this is the zip file. We upload that and then uh you hit this upload
Danny Norton: Well, I
Lloyd Scrubb: uh the button here and it's going to show you that it
Danny Norton: need
Lloyd Scrubb: uploaded everything into their system. Then the next process we do is export. Okay. And that will download a a zip file.
Spencer Ririe: I can't see the rest of the text on that button.
Lloyd Scrubb: All sorry you can't see. Wait.
Spencer Ririe: Uh,
Lloyd Scrubb: Sorry.
Spencer Ririe: your Google Meet little window is covering export report. Okay. I just wanted to see the
 
 
00:58:58
 
Lloyd Scrubb: Yeah.
Spencer Ririe: text.
Lloyd Scrubb: Yeah. Okay. Uh and yeah, we just basically this stuff here. So we're done with that guy. So then we can uh that gets put into the downloads folder. Before we go there, let me go back here.
Danny Norton: from system. Yes.
Lloyd Scrubb: And we're going to go to downloads.
Danny Norton: URLs.
Lloyd Scrubb: If we refresh, that's the file that was exported. Uh we're just going to rename it that and then we're just going to give it encrypted at the end. Okay. And we're going to go in here. That's going to add an encryption password here. Okay. So, these are the earls that were created for each of those cards. Um, and it's going to get this this file. So, we're just going to password 44. One thing I missed from the other thing since I'm I've been doing this for a while, which we'll do here. Save uh save there. So, we're going to close that guy.
 
 
01:00:52
 
Lloyd Scrubb: Right. Then we're going to copy that to our So what I should have done also with the uh so file was uh just verify
Spencer Ririe: That's
Lloyd Scrubb: that I didn't mess up the password. So I would open this guy and okay I would redo it and put the appropriate password in there. Okay.
Spencer Ririe: just to validate that you keyed in the correct um password
Lloyd Scrubb: Yeah.
Danny Norton: password.
Spencer Ririe: before sending it.
Lloyd Scrubb: Yeah. No, I mean there's always a chance that uh you know I made the mistake like I
Spencer Ririe: Okay.
Lloyd Scrubb: guess three times, but uh I mean yeah, I don't think that that's ever happened. So anyway, so that's that's what what I do. Um okay, so I guess Mario could show you how to send these.
Danny Norton: Yeah.
Lloyd Scrubb: I guess like how do they send the customer?
Spencer Ririe: Yeah.
Danny Norton: Yeah, that makes sense.
Lloyd Scrubb: still have to do the other file. Um,
Danny Norton: Cara. Cara and Loblas.
 
 
01:02:11
 
Lloyd Scrubb: so
Danny Norton: Right. Cara and Loblas.
Lloyd Scrubb: yeah, but they look they look just like they look just like that.
Danny Norton: Oh,
Lloyd Scrubb: So,
Danny Norton: yeah.
Lloyd Scrubb: so I I guess what I could do here for this one is show what would happen if So, the only thing that we haven't seen is that uh is what we would do for um zip file.
Danny Norton: What does that file you
Lloyd Scrubb: Um
Danny Norton: said?
Spencer Ririe: Your audio cut out there,
Lloyd Scrubb: sorry,
Danny Norton: Yeah, you for one second
Spencer Ririe: Lloyd.
Lloyd Scrubb: if we need to send a zip file,
Danny Norton: there.
Lloyd Scrubb: we didn't see that as part of the process. That's something else that we we We we do sometimes.
Danny Norton: And I'm happy to Mario show us that as well,
Lloyd Scrubb: Wait,
Danny Norton: like that if that's something that he typically does, then we can we can go through that process and fulfill that part of the order.
Lloyd Scrubb: you
Danny Norton: Um, but uh yeah, Spence, do you have any other uh technical questions for
 
 
01:03:00
 
Lloyd Scrubb: okay?
Spencer Ririe: Yeah,
Danny Norton: Lloyd?
Spencer Ririe: I guess I'm I'm curious if there is any, you know, because ultimately what we're trying to wrap our heads around is is um you know, is there anything I guess undocumented anywhere in the workflow that sort of still lives in your head? you know, let's say you win the lottery tomorrow and all of a sudden you're no longer available to to support Mario. Um, is there anything critical that that he might not fully know or that's not captured somewhere?
Lloyd Scrubb: Um, yeah. I mean, I think we've uh Mar, did we ever go over doing a uh a um
Spencer Ririe: You might be covering your mic on your computer. Can't hear you.
Lloyd Scrubb: I'm not touching my computer.
Spencer Ririe: There we go.
Lloyd Scrubb: I wasn't touching my computer.
Spencer Ririe: That's better.
Lloyd Scrubb: Anyway, um uh Mario, have we ever uh um have you ever done a Petro Canada order where we were using the old inventory or did I just do that?
Danny Norton: No, I think you did it.
 
 
01:04:26
 
Danny Norton: I I remember one time I need it because uh whereas to the old one,
Lloyd Scrubb: Yeah.
Danny Norton: but you you just did it for me and I I don't know how
Lloyd Scrubb: Yeah.
Danny Norton: to
Lloyd Scrubb: I I guess Doug there's no I mean I guess worst case with the old inventory you could just use
Danny Norton: Yeah.
Lloyd Scrubb: it like because it's not something that is going to happen anymore because we get those
Danny Norton: Yeah. Yeah.
Lloyd Scrubb: as URLs now right so so that's that's something
Danny Norton: Yeah. Yeah. Yeah.
Lloyd Scrubb: that you know and and worse worst case you just send the gift cards as is to the right what they the PDFs to them as is you just put them in a zip file and just send them they don't have to and don't give the option to add them as earl. Right. So, so that's not something that So, that's Spencer.
Danny Norton: Yeah.
Lloyd Scrubb: That's something that that we've had to do but is kind of being phased out anyway.
 
 
01:05:15
 
Spencer Ririe: Got it.
Lloyd Scrubb: Um,
Danny Norton: Those are
Lloyd Scrubb: I mean,
Danny Norton: all
Lloyd Scrubb: I guess if you know if I wasn't available and something bug happened with a script, well, any program would be able to to do that, but you'd have to get something to go through them.
Spencer Ririe: Yeah.
Lloyd Scrubb: It's not I mean it's not not rocket science. It's like you know the code is pretty straightforward.
Spencer Ririe: Yeah.
Lloyd Scrubb: You just identify the error and debug it. Um so uh so Amazon Amazon is the same as uh same as Indigo same laws is being phased out. So probably worst case you could get customers to accept. Well, anyway, it doesn't matter. Amazon Loblaws acts just like Amazon. So, Mario would be able to do that. So, that's nothing unique. Shoppers Uber is not that anymore. Walmart is uh so there's nothing that uh um like assuming that it works as as expected that uh he couldn't just if if problems came up for some reason that uh where the scripts didn't
 
 
01:06:34
 
Spencer Ririe: Okay. And I guess my other questions and I'm just aware of time.
Danny Norton: Okay.
Spencer Ririe: I don't know how much longer we we have you for, but on the ESO and Blackhawk API work. I know that's something that it sounds like is ongoing and you've submitted I'm just trying to refresh my memory from from the notes that you had sent. You're waiting on certification. Is that right?
Lloyd Scrubb: Um, yeah. So, um, basically I've moved as far as I can. Uh, so Black Blackhawk, I mean, we've done all the transactions that, uh, Doug wanted. We've only worked with one vendor, Tim Hortons. presumably that the adding other vendors uh there'll be more work need to be done but it should be
Spencer Ririe: Right.
Lloyd Scrubb: straightforward once we get that done. Um there were some things we couldn't uh or at least to my satisfaction couldn't you know. So, so sometimes we would run stuff and it wouldn't work and then they'd say, "Oh, try adding a uh a slash after the earl for these the restful interface." And sometimes that work or they said,
 
 
01:07:46
 
Lloyd Scrubb: you know, there was no documentation like so for instance for the cancel operation there was no documentation. So like I I kind of guessed the format based on the what other things were there. So at the end of the earl like they cancel or like say for the reload early you reload they cancel say oh no it's not cancelled it's just it's just um uh you for the cancel operation you don't put anything at the end and you submit the arrow. So I tried that and it returned the response but I told them that the response looked exactly like as if I did a balance code and it didn't change it.
Spencer Ririe: Right.
Lloyd Scrubb: It didn't change any of the you know if we did a cancel then I would expect the status to go from active to you know so then it was like oh well it doesn't happen in our it may it may not it didn't say it may not happen in our our test system but it should work properly in the production system. So we'll have to wait till we get to production to see if that's in fact the case.
 
 
01:08:46
 
Spencer Ririe: Got it.
Lloyd Scrubb: So there's still some questions.
Spencer Ririe: Okay. So,
Lloyd Scrubb: So you know
Spencer Ririe: essentially you've been sort of guessing at how their API endpoint and calls and and
Lloyd Scrubb: Well,
Spencer Ririe: what's
Lloyd Scrubb: not well for that that's the only one I guess we were guessing the other ones they there was documented API and they did it and they work that one is the only one that's kind of they source said well when you can you can test it once on the and we'll we'll we'll give you some production cards which we won't judge you so that you can test that the council actually works.
Spencer Ririe: Right.
Lloyd Scrubb: Yeah. So
Spencer Ririe: Okay.
Danny Norton: So also on the on the a API come I'm going like
Lloyd Scrubb: no
Danny Norton: crazy. Um some of some of the the the merchants don't allow that, right? Like um I know Fundstream is kind of I would say like 10 years ahead of us with this sort of
Lloyd Scrubb: heat.
Danny Norton: stuff is like Lobos as an example won't allow any integration with their their backend or whatever.
 
 
01:09:44
 
Danny Norton: Right? So even if we wanted to sort of be integrated with as many processors and merchants as we can, some of the merchants just won't allow it. Right? So, so my my vision was to to get started on some so Lloyd could see kind of what the process was. Was it is it worthwhile? Is it going to help us a lot? And so S and Castar are the two that we started with. So um yeah, so that's that's kind of my vision of the big picture of why we're doing it. And I think you know Amazon's probably maybe the next one and there also might be some added integration work to do with with Walmart. So, that's kind of my short-term vision, but the long term is I just wanted to get into it, see what it was like, see if is it beneficial for us. And uh but I know some of the merchants and we can't we can't get to because they don't allow it. So,
Lloyd Scrubb: Yeah.
 
 
01:10:38
 
Spencer Ririe: Got
Lloyd Scrubb: So for uh and for for ESO um so they they actually with their process
Danny Norton: yeah.
Spencer Ririe: it.
Lloyd Scrubb: they actually and that was the same for Viceerve as well. They actually assign you like a resource that is a technical resource who you can go through. So with them I think we we're just waiting now for so anyway. So, we've tested everything we wanted to test. Worked as expected in their test system. Um, the last thing,
Spencer Ririe: Got
Lloyd Scrubb: and I just hadn't followed up or Doug hasn't followed up. The last thing was uh uh we executed all the transactions we had to. They worked as expected. He was going to the resource was going to review them on their system, get back to us. So, I haven't pushed it. So, we're ready to go. basically when they can assign a resource and say that they're ready to go. We initially had said that we were would be ready in the first week of March and we're here now.
 
 
01:11:28
 
Spencer Ririe: it.
Danny Norton: Okay. Okay.
Lloyd Scrubb: So
Danny Norton: Okay. That was a good demo. Thank you, Lloyd. Uh, Spence, anything else that you have on your
Spencer Ririe: Uh, I don't think so.
Danny Norton: end?
Spencer Ririe: Um, you know, certainly we may have some follow-up questions. You know, obviously it it it covers a lot. We'll we'll get more sort of as as we probably do a few of the other vendors with Mario, but no, that was super helpful.
Lloyd Scrubb: Um okay.
Danny Norton: All righty.
Lloyd Scrubb: So um
Danny Norton: Is there anything else that you wanted to share, Lloyd?
Lloyd Scrubb: no unless you have have questions. I was just sort of thinking if there was something that uh um I need to share. So, so basically in terms of how things are set up, like I think I've captured as much as possible on the uh in the notes I sent you in terms of where the scripts are and I think uh you know there's only one tool that had to be
 
 
01:12:29
 
Spencer Ririe: Yeah.
Lloyd Scrubb: installed that does the PDFs is this Inkscape. I think everything else is just Python libraries and that kind of stuff. So um uh yeah so I think it's not uh it's not full and and the same for the other integrations. They're also just oh sorry the the only different thing would be the Walmart which we didn't show. I don't know if you need to see that where we go and we uh I don't know if you have a Walmart order that's ready to be done Doug or if Mara could also show that as
Danny Norton: We got one right here.
Lloyd Scrubb: well.
Danny Norton: So, yeah. Yeah, Mario can show us that one. That's perfect.
Lloyd Scrubb: Yeah. So
Danny Norton: Yeah, we'll we'll digest and syn synthesize and if there's any questions,
Lloyd Scrubb: anyway,
Danny Norton: we know uh we know where to find you. Um and so we can definitely uh regroup if if that does happen. Um but yeah, let's let's call it on this meeting and then we can shift over Spence to the other in like I'll get a Google Meet um going for the second session with Mario and we can kind of go
 
 
01:13:34
 
Lloyd Scrubb: Okay. Okay.
Danny Norton: from there.
Lloyd Scrubb: So, Okay. Thanks, B. So, Doug, just one last thing, whatever. So,
Danny Norton: Yeah.
Lloyd Scrubb: with with uh with uh Blackhawk and their uh you know, the digital card thing. So, you're going to have the cold stock and you're going to want to activate those cards if you're going to plan to do it through their interface. So, it's going to be it's going to be like what you didn't want to do.
Danny Norton: Right.
Lloyd Scrubb: It's not start and end, right? You have to do one card at a
Danny Norton: Yeah. Well,
Lloyd Scrubb: time.
Danny Norton: that I think that's okay with um all the other merchants except for Walmart. Like the digitals, we don't sell that much, right? So, I think that's okay.
Lloyd Scrubb: Okay.
Danny Norton: The only the only problem is Walmart because we we the physical ones we sell
Lloyd Scrubb: Okay.
Danny Norton: so much of it, right?
Lloyd Scrubb: Yeah.
Danny Norton: All the ones individual is fine because we we don't sell enough of it to to really be a
Lloyd Scrubb: Okay.
Danny Norton: problem yet.
Lloyd Scrubb: Okay.
Danny Norton: Yeah.
Lloyd Scrubb: Sounds good.
Danny Norton: Perfect. Thanks, Lloyd. All right. Thanks, Lloyd.
Spencer Ririe: Thank
Danny Norton: Thank you. Take care.
Spencer Ririe: you.
Danny Norton: Thanks. That was helpful.
 
 
Transcription ended after 01:15:05


This editable transcript was computer generated and might contain errors. People can also change the text after it was created.