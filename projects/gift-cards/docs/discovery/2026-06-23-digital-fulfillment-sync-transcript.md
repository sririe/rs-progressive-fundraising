---
title: "Progressive Digital Fulfillment Sync — Transcript (SOW Amendment Walkthrough)"
type: discovery
category: meeting-transcript
date: 2026-06-23
status: complete
format: transcript
participants:
  progressive:
    - Doug Beers (dbeers@progressivefundraising.ca)
    - Lloyd Scrubb (lscrubb@progressivefundraising.ca)
  redstamp:
    - Spencer Ririe — "You"
    - Tim Lemke (tim@redstamp.com)
    - Stephanie Lamon (stephanie.lamon@redstamp.com)
speaker_key:
  "You": Spencer Ririe
  "Speaker 3": "Doug Beers — inferred from content (decision-maker; 'the big test on the vault is whether Doug Beers can do it'; asks timing/October-peak)"
  "Speaker 4": "Lloyd Scrubb — inferred from content (deep technical detail: Walmart activation, Starbucks columns, import mapping; 'I'm not writing that software')"
  "Speaker 1": "Redstamp (Tim Lemke or Stephanie Lamon) — unresolved; opening/closing small talk only"
  "Speaker 2": "Redstamp (Tim Lemke or Stephanie Lamon) — unresolved; small talk only"
  "system": "crosstalk / mislabeled continuation — unreliable (often continues the prior speaker)"
diarization_note: "Supernormal verified only 'You' (Spencer). Speaker 3=Doug and Speaker 4=Lloyd are inferred from content with high confidence; Speaker 1/2 (Redstamp small talk) remain unresolved between Tim and Stephanie. The 'system' label is unreliable and frequently continues whoever spoke last. Unlike the Gemini discovery transcripts (verified keys), treat all Speaker-N attributions as inferred."
referenced_not_present:
  - James (role unconfirmed)
  - Candace (Redstamp design)
  - Kaitlin Gordeyko (Redstamp design)
capture_tool: Supernormal
source_capture: "second-brain/Incoming/2026-06-29-1036-...-speaker-1-...md (manual web-UI copy, captured 2026-06-29)"
related:
  - projects/gift-cards/docs/discovery/2026-06-23-digital-fulfillment-sync-notes.md
  - projects/gift-cards/docs/plans/2026-05-27-progressive-secure-card-vault-sow-draft.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  - projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md
---

# Progressive Digital Fulfillment Sync — Transcript (2026-06-23)

[0:06] Speaker 1: I rode my bike last week around where they all started their parade and everything. There's just so many people down there.
[0:13] Speaker 1: It's crazy.
[0:14] Speaker 1: I know.
[0:15] system : It's a lot of fun for the city, so. Yeah, Mateo, my eldest son, he's been going down every day that he doesn't have soccer training and he's been going down to watch uh, watch the events and uh, yeah, just be part of the viewing parties and the ambiance.
[0:29] system : pretty neat.
[0:30] Speaker 2: Stuff happening all over the city.
[0:33] Speaker 2: It's really exciting.
[0:34] Speaker 2: Yeah, I love it.
[0:36] system : Hi guys.
[0:37] You: How's it going?
[0:39] Speaker 1: That's her, good.
[0:41] Speaker 1: Yeah, we're.
[0:42] Speaker 1: Yeah, ready to get out of here.
[0:44] Speaker 1: So, uh, yeah, it's uh, it's good.
[0:47] Speaker 2: We're, uh, Lots of back and forth on this, so I'm really interested here what, what you guys have to say and, uh, yeah, I wanna, try to get everything all nailed down if we can.
[0:58] You: Yeah, absolutely.
[0:58] system : So
[1:00] You: And I appreciate the, um, you know, the, The thoughtfulness and patience, obviously, um, There's always, you know, sort of the complexity and translating, you know, a very technical solution into, um, a statement of work can sometimes be a challenge.
[1:21] You: And so, um, I thought what would be helpful is, um, I have some kind of talking points to walk through, um, primarily related to some of the things that, um, both Lloyd and and James had sort of pointed out to kind of, um, I guess, better outline how we're thinking about the workflows. And I think we were already, I guess, directionally, uh, heading in the direction, and then once we received
[1:52] You: the additional set file, I think that, um, sort of confirmed what what Tim and I had had originally planned, but now we can probably put more concrete language around it so it doesn't feel ambiguous.
[1:56] system : Yeah.
[2:04] system : Okay.
[2:04] You: Um, And so, um, uh, I guess one big piece, uh, and Lloyd, this goes to the, uh, in in homogeneous by supplier and not merchant.
[2:17] You: Um, comment is, um, Right now there are, you know, I guess, 23 merchants, but that doesn't necessarily mean that there are 23 different formats that the vault would need to store.
[2:36] You: Um, and so our, like, intent here, once we were able to kind of analyze all of the the different, uh, files that you'd shared is, um, essentially, um, And I'm trying to think of the right language here to describe this, but, um, Essentially, when any card, um,
[3:04] You: or set of inventory would be ingested or pulled into the vault, we would be sort of normalizing the information that each spreadsheet has against our own sort of vault, um,
[3:23] You: And I guess in technical terms, like the canon, the canonical, um, card record.
[3:30] You: And so, What that looks like is for every card coming into the vault, regardless of its source.
[3:38] You: We would have fields for the merchant and brand, um, i.e. Tim Hortons.
[3:44] You: We would have a field for the supplier and source system.
[3:49] You: So this is mainly so we can track where that card actually came from.
[3:53] You: Um, and so was it from Cash Star?
[3:57] You: Was it from a fuel porter, portal?
[4:01] You: Was it from, um, I know you sometimes acquire cards from a competitor, so that's something that we would want to capture when we import the card information.
[4:13] You: Um, and then we would have a credential field, and the credential field, I'll expand on here in a minute.
[4:22] You: Um, I also noted that right now some of the, um, card import items also already included like a recipient name and a recipient email.
[4:34] You: Um, that isn't necessarily present on all of the the card formats, but it would be something we would be looking to normalize.
[4:43] You: Um, And then, um, we would have, uh, obviously associated with the belt, we would have the customer, the order reference, the invoice reference, and the date, as well as a status.
[4:57] You: So that would be, you know, available, allocated, fulfilled, um, plus quarantined, need replacement, or voided, and those would just be the data points that we would maintain.
[5:11] You: If, you know, an order is fulfilled and sent, but then something happens to a card, you know, we would need to be able to quarantine that, um, in a way that we would, uh, be able to then decide, okay, how do we handle that sort of edge case?
[5:27] You: Um, And then, um, for like being able to maintain the audit trail, obviously a source provenance sort of field.
[5:38] You: So what import batch was it, was that card a part of, what file, what row, uh, in the original ingestion, uh, process?
[5:48] You: And so the goal with this is to sort of simplify, um, that import to so that each merchant reduces to, um, You know, they either have a URL, they might have a card number or a pin.
[6:11] You: They might have, um, a redemption or a claim code, a challenge code.
[6:17] You: So we would essentially be capturing all of that, um, in that process.
[6:23] You: Um, and so what I have so far is it basically comes down to, um, like Amazon, um, the Amazon card family, they have a claim code secret, cash star, which is most merchants.
[6:40] You: They have a URL plus like a secret or a challenge.
[6:44] You: Uh, the Fairmont Winners URL, uh, the PC allocation would have URL plus secrets, which would be account number and pin.
[6:54] You: Um, et cetera, et cetera.
[6:57] You: So we, we would essentially set it up so that it's not that when you add a new merchant, we have to like add a new merchant necessarily, um, as like rebuilding a new, um, software function for it.
[7:13] You: We would just, the only caveat would be if down the road, a new merchant is added that has, um, let's say a new, um, credential that is different from the existing pattern, that would be something that would require a change order.
[7:32] You: But I would say from a maintenance, like standpoint, um, anytime a new vendor becomes available, that still is going to require, um, some work on our end to make sure that we have, like, the data field structured to recognize that vendor when we go to import it.
[7:55] You: Um, And I don't think it requires like a massive, you know, change order to do something like that, but it's basically like, in order for the system to work, we would need to account for a new vendor and then make sure we test that when we import from that vendor vendor's format that it works on how we structured it.
[8:19] You: Does that sort of make sense, Lloyd?
[8:21] Speaker 3: Um, I guess it just depends how you design your...
[8:27] Speaker 3: I mean, it makes sense.
[8:28] Speaker 4: Um, But it's, it seems that, uh, especially for those, uh, vendors where we're just essentially passing it through.
[8:37] Speaker 4: I mean, I think the things that from Doug's perspective, the things that we can't really do now well easily is like doing inventory and that kind of stuff, right?
[8:44] You: Yeah.
[8:47] Speaker 4: So I think that is like the big thing, but it's, if, uh, you know, basically we have to take what we receive.
[8:53] Speaker 4: doesn't matter what's in there.
[8:54] Speaker 4: You could actually send every field inside that file.
[8:57] Speaker 4: I think there's no harm in sending whatever they, and just put the password on it, put it into some format, password, and then, now with race or delivery.
[9:06] You: Yeah
[9:06] Speaker 4: So, if that, if that's a model, like for my, my brain, like, there's nothing that has to be done other than to record that it's in the system.
[9:16] Speaker 4: You know, I, like you said earlier, like you want to keep the vendor, you want to maybe keep all that other stuff, but, um, you know, but again, I'm not writing that software, so I don't know how you guys are doing that, but from, from outside, like if I was, uh, I would say, For, unless it's like something like, You know, a new, another Amazon, like if you took on Doug a card where you had to do generation, those are only ones that, that are outside of the,
[9:45] Speaker 4: The, the,
[9:48] Speaker 4: And you should, you should, you should be able to just, I think, just easily select.
[9:54] Speaker 4: So if you did, so if you designed it a certain way, you could probably get away with never doing a, and, and again, I don't know.
[10:01] Speaker 4: I mean, I'm not writing that, so I don't, I haven't put much thought into what needs to be done in order to do that.
[10:07] system : But, um, Yeah.
[10:09] system : Uh, uh, uh,
[10:14] You: Yeah, and the goal is to basically just standardize the process and how we store inventory in such a way that it doesn't matter where the inventory came from.
[10:22] system : Right.
[10:25] You: that every new, like, inventory batch that would go into the vault can basically be stored in the vault.
[10:34] You: Um, in such a way that we build everything.
[10:38] You: So that when we launch it, we account for your basically current offering, um, and everything there can be stored in the vault and we have sort of a, a common, um, naming convention for the different credentials that each format might require.
[10:57] You: And they're all actually fairly similar.
[11:01] You: Um, you know, um, when when you boil all of it down, the credentials are all fairly similar, and most of the outputs are are, for the most part, just passed through.
[11:14] You: Like as you've mentioned, um, Walmart is really the only edge case in that that's the one part of the vault that we would have a bidirectional flow, if you will.
[11:25] You: So with Walmart, when that, um, and just to confirm, to make sure I understood this correctly, today, when you acquire Walmart inventory, it is, um, You're provided card numbers, but they are inactive, and you acquire that before you fulfill orders.
[11:46] You: Is that correct?
[11:48] system : Um.
[11:50] Speaker 4: No, what, uh Walmart?
[11:53] Speaker 4: Oh sorry, you're talking about Loblaws, right?
[11:56] You: Walmart.
[11:56] Speaker 4: Oh, Walmart, sorry.
[11:58] Speaker 4: Yeah, we received, uh, uh, we don't receive anything, actually.
[12:02] Speaker 4: They're all virtual.
[12:03] Speaker 4: So basically we just say we want X number as these denominations.
[12:07] Speaker 4: So we send other requests and then they send back the garden.
[12:10] You: Okay, but but yeah, basically I was clarifying with Tim on just the mental model for that is we would then store those card numbers as, you know, inventory that has not been activated.
[12:26] You: And then when it comes time, when a Walmart order comes in, the fulfillment workflow for Walmart would be we allocate from that inventory list that is in the vault to the Walmart order.
[12:39] You: And and the vault prepares the activation file that then someone on the progressive team would take through the FISER, um, activation.
[12:50] Speaker 4: No, yeah.
[12:52] Speaker 4: So, so, sorry, so there's like, so we have, we have nothing.
[12:55] Speaker 4: we have no uh inventory.
[12:57] Speaker 4: And then that that operation is an activation operation.
[13:01] Speaker 4: So it creates cards and it activates them.
[13:03] Speaker 4: So then they're lying.
[13:04] You: Okay, so that does it all?
[13:04] Speaker 4: So there's no.
[13:06] Speaker 4: Yeah, so, so, so when we receive the, the cards back, those are live cards and then basically, uh, um, we could distribute them.
[13:16] Speaker 4: And right now we've basically been, we don't do that until the order has been paid for, once they pay it for, activate and then generate the cards and then we send them to the custom.
[13:27] You: Okay.
[13:27] system : So, yeah.
[13:28] You: Yeah, so that, I guess that's the part that I was still fuzzy on.
[13:34] You: Um, So then,
[13:35] system : So it's an activation, it's an activation and an inquiry, of course, at the same time.
[13:40] You: At the same time.
[13:41] You: Okay.
[13:41] You: So then that would simplify the fulfillment piece in that, um, we wouldn't need to upfront, like, let's say before anyone orders Walmart, we wouldn't need to have any stored Walmart card numbers in the vault.
[13:59] You: Is that?
[14:00] You: Is that do I understand that correctly?
[14:04] Speaker 4: Correct, yes.
[14:04] You: Okay.
[14:05] Speaker 4: Let's come into being, yeah.
[14:06] You: Or
[14:09] You: Order comes in, then we would need to, um, essentially just be ready for someone running the activation workflow.
[14:20] You: And then they would then take the output from that and and put it into the, uh, into the vault so that then it can be basically associated with the order because I assume there's instances where someone orders, let's say 50 Walmart cards, but then they're going to have cards for other vendors and we want to be able to package it up.
[14:38] You: you know, essentially together, um, to to normalize distribution.
[14:41] system : Right.
[14:45] system : So I guess, yeah, so for, um, Yeah, so the, for the generation step, I guess, and I don't know what you're doing for the generation for the other vendors, but um, whatever part from the generation, that's where the Walmart, the, the Walmart would flow into that same flow for as Amazon and I know the other music.
[15:08] You: Yeah.
[15:10] You: Okay, that makes sense.
[15:13] You: Um, Let me just scroll down here.
[15:19] Speaker 3: Can I, um, I'm just going to jump in with one thing.
[15:22] You: Yep.
[15:23] Speaker 3: It's mostly going to be listening today, but I just want to make sure that Lloyd's comfortable with what he, because he said this to me a few times about, you know, some of these merchants, we, we can just take it and we're just going to use it exactly like, like we have it.
[15:37] system : Now, Lloyd, are you, are you, um,
[15:40] Speaker 3: wanting to make sure we don't have to build too many things because it's all ready to go, and I just want to make sure that we're all aligned.
[15:48] Speaker 3: You know what I mean?
[15:49] Speaker 3: With Spencer, your answer to what?
[15:50] You: Yeah.
[15:51] Speaker 3: I want to make sure Lloyd's comfortable with what you're saying.
[15:53] Speaker 3: So, Lloyd, it, it, it, if you're not, I want you, I want you to tell Spencer because, uh, um, you know what I mean?
[16:01] Speaker 3: Like, you guys are building it, but I don't want to, if, if, if Lloyd feels that maybe it can be built quicker, easier, and faster because they're all ready to go.
[16:10] Speaker 3: I want to make sure that I just want to make sure we're all aligned because you guys are working at a different level than I am, but I want to make sure Lloyd's comfortable with your answer.
[16:13] You: Yeah.
[16:22] system : You know what I mean?
[16:22] You: Yeah.
[16:24] Speaker 4: Yeah, well, I, I, I don't know what, what's being, like how it's going to be built, right?
[16:31] Speaker 4: So, I, I just have, uh, like a use case, you know, for those, those vendors where we don't do anything where, you know, like, if, if it is, you know, because I think there are things that just generally import things and then can just send those out in a, right?
[16:48] Speaker 4: So it puts it into stock, and it could, it's, they're all coming in as CSV files, I guess.
[16:54] Speaker 4: I always know what the format is, right?
[16:56] You: Yeah.
[16:56] Speaker 4: So in my brain, I'm thinking, okay, it's a CSV flaw.
[16:58] Speaker 4: That's how you usually receive them, though. I say, CSV or XL Slaws.
[17:02] Speaker 4: And they could be imported.
[17:04] system : I know I can, you know, get a program just to figure out what the, the columns are in that thing and whatever it is, whatever the, the columns is, like handling an Express, spreadsheet is a pretty easy thing for, for a programmer, I think.
[17:18] Speaker 4: And so take it in and store it exactly in those units.
[17:23] Speaker 4: I guess the only thing that comes in.
[17:24] Speaker 4: So where I'm thinking that the disconnect would be is because some of your vendors, they do change their format, so winners will come in one day as these columns, then the next day they'll come in with, Additional columns, then you need to store in our current, like, uh, haphazard thing.
[17:42] Speaker 4: We store both of them.
[17:44] Speaker 4: We, as humans, we can go in.
[17:45] Speaker 4: So, but assuming that everything can be, doesn't change ever again, which maybe is not a good, is a sanction, then winners is always winners, it should just come in and, you know, or, or it actually doesn't matter what it is.
[18:00] Speaker 4: You can just take it in and send it out, actually.
[18:03] Speaker 4: And I'm going to change my thing.
[18:04] Speaker 4: Whatever it is, whatever format you store in inventory, you should just have these are the fields and these are the, maybe you have, you know, you can figure things that you say, okay, I want to send, this is what's in, and you, and there's an interface that says, like, click this, I want to, and these are what, the fields I need to pass the customer.
[18:20] Speaker 4: And then that defines your output thing, right?
[18:24] Speaker 4: From, from this thing and it just hides the rest and creates an excel spreadsheet. It's only the columns that are the export local.
[18:32] Speaker 4: And to me, that doesn't matter what, what it is.
[18:35] Speaker 4: It's just a, uh, uh, an object in your thing and you're telling it what in this object needs to be sent.
[18:43] system : So, I mean, it may be more effort upfront to, like I understand, it's more up for the front, maybe to design something that is adaptable like that, but in my brain, I still think that once you handle that flow, then there's no other real use cases you have, Doug, because if I was a human, I would just say, oh, I would just take the Excel file and I'd hand it to the person that's getting it, and I think.
[19:10] Speaker 4: A system, that should be a model that is handled by default in the system.
[19:16] Speaker 4: And then if there's something that Definitely breaks the paradigm, then that would be, in my brain, a change case, right?
[19:23] Speaker 4: where you have to, okay, we have to change the, the underlying engine, vault engine to handle this new particular thing because we didn't think of, uh, the thing, but, um, I, I don't know what that effort is, like from, from a program to basically handle that kind of a model, right?
[19:41] Speaker 4: I'm just gonna pop in for a 2nd.
[19:44] Speaker 4: And I see what you're saying.
[19:47] Speaker 4: It's like, you're saying that if, if something is pretty similar to what the end client was going to get anyway, why wouldn't you just store it like that and then pass it along?
[19:57] Speaker 4: But from an inventory management and kind of now like, If we're doing now across a number of vendors and kind of working on an improved kind of delivery of the kind of the information to a client.
[20:14] Speaker 4: I think personally, The way I would approach it is still the normalization approach.
[20:21] Speaker 4: Um, because If we build it in such a way that all of the the data we need, you can still import it.
[20:30] Speaker 4: However, it comes, basically.
[20:32] Speaker 4: So you're not necessarily changing a lot of the import process.
[20:36] system : It's just that the, the kind of the data within the vault is normalized in such a way that it gives us flexibility to basically kind of package the output how we want.
[20:49] Speaker 4: So in the sense that, so say, like your example, like say winners, so say winners, is a certain kind of gives you X format, and then there's Walmart X format.
[21:02] system : And then there's one other one that a client purchases at X format, and they're all slightly different, even though, you know, in this kind of example, say that the the end client needs the same info that was imported.
[21:18] Speaker 4: If we normalize things within the app, then we can choose how we present that to the end clients.
[21:24] system : We're not just, we're not just taking a CSV and saying, okay, here's the winner's CSV.
[21:29] Speaker 4: It's like, well, this is how we want you to see the CSV, so you can, you can kind of use it easily and it's, it's uniform to what we're showing for the other merchants.
[21:40] Speaker 4: So, I see what you're saying, Lloyd.
[21:42] Speaker 4: I just think that, um, Because then also, like you said, you'll have to account for if something changes, then you maybe have to.
[21:50] Speaker 4: And I think if we're storing kind of direct representations of an import that kind of represent the files themselves.
[21:58] Speaker 4: So say you say, oh, this is the CSV for this card, but this, this merchant has a different import format.
[22:06] Speaker 4: It's going to get really convoluted quickly, as opposed to from a kind of data standpoint, if we are able to normalize things.
[22:15] system : It'll allow things to scale and kind of have different, um, I think vendors coexisting more peacefully beside one another within kind of the data, the database and kind of the operational flow of the app.
[22:32] You: And I, I think, I think we're all, um, aligned on, we're not trying to add a needed complexity where we're building individual data models in the app for each different merchant.
[22:45] You: Not at all what we're suggesting.
[22:47] You: We just want to make sure that when we ingest any new inventory, That, regardless of what that vendor calls a column in the spreadsheet, We have a, we build the ingestion engine, if you will, to convert what a vendor calls a thing to what the card ball calls the thing.
[23:08] You: Um, so that regardless of vendors and new vendors down the road, we have sort of our own, you know, defined naming conventions for, um, you know, what a pin number is, et cetera.
[23:21] You: And so it doesn't, ultimately, it doesn't matter when it comes in.
[23:24] You: We normalize it and store it.
[23:25] You: Um, And we have the import log, so we know what came in, we know what it was called.
[23:33] You: And so that's something that, you know, likely is metadata associated with an import.
[23:38] You: And then when it comes time to generate, Because we've already normalized everything, we can then, like, Tim said, if an order has 7 different card merchants in it, we can present the generated output to the end user in a much more consistent, you know, format.
[23:58] You: Um, So I think we're all basically saying the same thing.
[24:03] You: Um, But it's really just to simplify how we store inventory so that regardless of some cards might have different data fields associated with them.
[24:14] You: We still just store everything in a normalized way so that it's really easy to understand.
[24:19] You: What's an inventory now, where it came from, you know, what was the acquisition source?
[24:25] You: Um, And then when it comes time to fulfill, um, That also just gives us flexity, flexibility moving forward when we move past our 1st launch and then we look at, okay, now we're going to build something to help.
[24:39] You: you know, your customers.
[24:41] You: you know, distribute the cards they bought to multiple individuals, that becomes much easier to do when we've normalized the format of everything.
[24:52] You: So it's, you know, it's basically like you drop off all your recycling at the depot and there's bottles from different breweries, you know, at the end of the day, like, the system sees a can and it doesn't matter which brewery it came from.
[25:07] You: Like, this is high level, right?
[25:09] You: But at the end of the day, it represents one can in, can goes into the system.
[25:15] You: Oh, this is an aluminum can.
[25:17] You: It has a label on it, which, you know, obviously is important to make sure that when someone orders an Amazon beer, they get an Amazon beer, not a Walmart beer, but at the end of the day, it's an aluminum can.
[25:28] You: 12 ounces.
[25:29] You: Um, Maybe one vendor includes the international bidder unit measure on the front of the can, but for our system, we would normalize each sort of vendor's own language to sort of a standard shared language in the vault so that, um, We just have, you know, our perspective on how everything is named and stored, and then it just makes, you know, ruining those cards once they're in the vault, you know, much easier.
[25:56] You: Um, that was probably a terrible analogy, but, um, uh, you know, just really trying to simplify the process.
[26:04] You: Um, and yeah, really the only time a, you know, any sort of infrastructure change would be needed, is if there's some form of new, you know, format that would need to be handled, that presents, you know, a data field that we currently don't have mapped.
[26:24] You: And I would say, there's likely very few cases where that would be the case.
[26:30] You: The only ad that we would need on our end is just to, um, you know, let's say you get, hey, we, there's this new, you know, new spin out from the Richards Group restaurants where they have these new gift cards we're going to start carrying.
[26:48] You: We would just, before the 1st import, we would make sure that we go into the system and add the new merchant info.
[26:57] You: We would look at, okay, what do they provide us?
[26:59] You: Okay, we've already we've already accounted for that.
[27:03] You: So then in the future, when this merchant, uh, you know, whatever you buy and whatever you receive from that merchant, when you have that in hand, we would just want to make sure when that goes into the vault that it normalizes properly.
[27:15] You: So it mainly just be, before we just blindly start feeding in new formats, we would want to make sure that, okay, we've got a new, um, you know, merchant data ID that we need to account for, and we're gonna do a test import to make sure that we normalize that, and it works, and then once we test it, then we're off to the races being able to fulfill it.
[27:40] You: So it's mainly just giving, you know, context to the vault as the brain, if you will, that, hey, just so you know, we got a new merchant, doesn't change anything about the system.
[27:49] You: This merchant typically is going to give us cards in this format, so the vault can normalize it, and then when it comes to sending them out to your customer,
[27:58] You: There's no new machinery needed there.
[28:02] You: So it's really just like, adding a new dropdown in a in an Excel spreadsheet for which vendor is this or merchant is this associated with?
[28:11] You: So, you know, fairly minor, but anytime you are dealing with cash instrument, we would just want to run some small QA testing when a new merchant shows up just to make sure that it, you know, works seamlessly.
[28:23] You: So, um, overall, relatively, you know, load up, but with anything software, uh, it always always appears on the outset to be simple, but, um, you know, over time, things can, uh, crop up that we don't plan for, but the the goal with the V one is to essentially account for, um, all of the card merchants that you have now.
[28:45] You: and have them normalized and mapped so that there's just no friction.
[28:50] You: Some of the cards will come in and they'll go right back out nearly and maybe the identical format.
[28:55] You: But they'll be allocated and tracked so that you have sort of full visibility on where the inventory came from and then which order did it get allocated to?
[29:03] You: Um, and at any point, you know, you can log in and you can see, you know, oh, we just shipped this, uh, this batch of cards out to the First Nations group in Saskatchewan.
[29:16] You: Pull that order up, you can see exactly which cards were alligated to them.
[29:20] You: Um, and sort of have the history and you could see who on the team fulfilled the order.
[29:26] You: Um, just so that you always have that history, Doug, if you're if you're off grid for a month and you come back and there was a question about an order, customer said, hey, I didn't get this.
[29:35] You: Um, you'd be able to go right to that screen, find the order, see who fulfilled it, see what cards were allocated, and if, you know, it was a mistake by someone who, um, you know, you'd be able to see, oh, well, the customer thinks they ordered this, but we actually have their order form.
[29:53] You: We see exactly what they ordered and that's what we fulfilled and we have the audit trail to sort of prove like, hey, no, this is what you ordered.
[30:00] You: So you might have missed clicked something on the website.
[30:03] You: Um, and then that would make it just easier for you to handle those like maybe those French cases where a customer might feel like, hey, you know, I'm pretty sure we ordered $50, $100 denominations and we only got 25 and it's like, well, here's the order.
[30:16] You: Here's here's what we process and allocated.
[30:19] You: Um, and so that just can, you know, make all that easier versus right now, or what I watched Mario do was he was having to go back in his email history to find, you know, the date that something happened and and just even trying to track like, you know, what day that order might have been processed on and how the cards were managed and, oh, and he didn't have enough to fulfill it, so he had to go to Doug's office and have Doug get on and get another batch, and then he had to pull from a spreadsheet to put him there.
[30:50] You: So like all of those pain, pain points just immediately go away because it's all handled in sort of that one central registry.
[30:57] Speaker 4: Uh, one thing I'll just jump in and say, too, is the way I was anticipating the import or part of the import process, work was that, Um, so in the import process, there would be a screen that would show what's being imported and what's being mapped to what?
[31:13] Speaker 4: so that it can be kind of accepted and verified prior to it even getting imported.
[31:18] Speaker 4: So, we do the work ahead of time to say, okay, when we import, uh, uh, winners, we were using that example.
[31:27] Speaker 4: So this field in the CSV maps to this in the vault.
[31:31] Speaker 4: And then, but even, even though we will have done that work ahead of time as part of the acceptance to the import steps, so you import, and you see what's mapping to what, and you could say, oh, that doesn't, that doesn't map, that shouldn't be mapping to that.
[31:45] system : I need to adjust my CSV file, maybe a header or whatever.
[31:50] Speaker 4: Um, That's kind of how I anticipated part of the import process working.
[31:54] Speaker 4: So that even before the cards get added to the vault, there's kind of a verification that things are where they should be.
[32:02] You: And that's just helpful because Just because we're being sophisticated with how we're doing this doesn't mean the merchants you are buying your cards from are like it, and it sounds like any given week, maybe it's a different, you know, it's sandy versus Tim that is exporting cards from, you know, the merchant and they're sending to you to Dr. Eubim, and one of them uses a different template.
[32:27] You: Like, We just want to make sure our system doesn't break if that happens.
[32:31] You: So that sort of import process allows you to to sort of adjust and calibrate, um, because it sounds like, you know, in a perfect world, everyone would just send you the cards in the exact same sort of agree upon format, but we want to make sure that, you know, we've got the flexibility there to to handle sort of those changes and and then not have to go back and say, like, ugh, we got to build some new infrastructure to handle the fact that these cards are coming in differently.
[32:58] You: Like, it's it's not meant to be brittle on our end.
[33:01] You: We want it to be fairly robust and be able to handle those edge cases.
[33:05] You: So that's really why we did spend quite a bit of time.
[33:08] You: you know, going through all of the the example files you have and and my confidence was pretty high after basically going through all of that to, yep, this this actually maps really well to our plan to sort of normalize power storing everything.
[33:27] Speaker 3: Well, from my perspective, it's good we have these conversations, right?
[33:31] You: Yeah.
[33:32] Speaker 3: So, I think we get to the heart of the real issues and that sort of thing.
[33:36] Speaker 3: So I'm, I'm happy with that I'm here and, um, I'll talk to Lloyd myself after and, uh, you know, I just want to make sure, Lloyd, I just want to make sure that you're, you're on, you're on board and you, you totally agree because, because, uh, you're, you're my biggest resource in making sure this is right for a long time for us.
[33:56] system : So.
[33:57] You: And what, what we can, uh, and I think this would just be helpful for all parties.
[34:03] You: I'm a pretty visual person when it comes to thinking about this.
[34:06] You: So, Tim and I can sync up and put together sort of just a visual, like, diagram that would basically, you know, we don't necessarily have to do it for every single merchant, but just saying, okay, here are, like, the 6 most common merchants, and this is typically what their CSV file includes.
[34:26] You: like when it would go into the vault.
[34:28] You: And then here's the vault, and then this is how we normalize that information in the vault so it's stored, just so you can sort of see how things would map.
[34:38] system : Yeah, I mean, I think from Doug's, or from, you know, say from Ducks perspective, he doesn't, the normalization stuff, that's, that's your programming stuff you're going to do.
[34:47] You: Yeah.
[34:49] Speaker 4: Like, uh, I, I, uh, want him to focus on that.
[34:52] Speaker 4: Okay, the input, you just need to put this in and then you're gonna, we want to deliver this, right?
[34:57] system : So you have, I think you have both sides of that.
[34:59] Speaker 4: You have what we typically deliver.
[35:02] Speaker 4: I mean, maybe if you would look at, and we, you know, so what we typically deliver was the minimum that they needed to basically use a card, right?
[35:11] system : So if there's a challenge code or if there's a, you know, for instance, Loblaws gives us Earl, and then they give us a pin and they give us, you know, so I guess that allows them maybe to go to a, or some kind of terminal and type in the code and put the pin in.
[35:29] You: Right.
[35:29] Speaker 4: I have no idea.
[35:30] Speaker 4: But, you know, um, so, so I think that from that, like, whatever you're doing, but I just, you know, again, from my, uh, simple viewing of the thing, it should just, it's just in and then out and, Oh, you store is fine.
[35:43] You: Yeah
[35:46] You: Okay.
[35:47] Speaker 4: I want Doug, you have to figure out whether the requirements, right?
[35:51] Speaker 4: So, you know, like, In the future, yes, so now as customers are asked for this, they want to be able to deliver.
[35:58] system : They don't want to deal with the cards.
[35:59] Speaker 4: They just want you to send them to, they're going to give you a list of URLs and, or, or email addresses or whatever, and you're gonna, want to, there's going to be some way to map that process, right?
[36:11] Speaker 4: Because that's not going to just be, you know, someone's going to have to input email addresses.
[36:15] system : Sorry, the customer's gonna have to send something where you say, okay, here's the cards and, you know, so that's a, a separate thing, but from the, Assuming that before that email goes out, um, There's just, it seems just very minimal information that needs to be stored there, so the, I understand your normalization that was going to go on, but I think from, it's just seems very simple from, from what needs to be done, right?
[36:36] You: Yep.
[36:37] You: Yeah, top level card info goes in.
[36:42] You: Only the needed information, um, the end customer for redemption goes out.
[36:45] system : Yeah.
[36:48] You: You know, they don't, they're not going to need any of our, uh, that that normalization data is all just sort of internal.
[36:55] You: They're gonna get, you know, the output format, very simple, streamlined only what they need.
[37:00] You: Um, and we can still account for PDF generation of cards, if and when required, and we would likely be running that server side, Lloyd, um, versus through, uh, like a, on desktop, on machine, um, like Inkscape type program.
[37:16] system : Right.
[37:18] You: Um, Um, so, Mainly because I know that, uh, in some cases, there's 200 cards that need PDFs generated if those are generated sequentially.
[37:31] You: Um, that can take a while.
[37:33] You: And so there's a, there's the option to do, you know, parallel generations if needed, but end of the day, the most simple output is having one output format versus, um, having to balance PDFs on top of, you know,
[37:51] You: So I, I know Doug mentioned he was willing to consider like moving away from the sort of PDF format, but, um, We've accounted for for that.
[37:52] system : All right.
[38:03] You: The PDF format, uh, if need be, but certainly it would be simpler to not have to do it because, um, it's, that's just one more link in the chain where, Something breaks and, um, that would be a scenario where someone on your team wouldn't be able to fix that if, if there's an issue that that we would have to jump in and help with.
[38:21] You: So if we were really looking to simplify things, we would probably just omit PDFX, you know, generation altogether and stick to just the numbered format.
[38:31] You: But, um, yeah.
[38:33] Speaker 4: And and that and that's just kind of one of the powerful things with just kind of building an app like this is we can have control over the format.
[38:41] Speaker 4: So it's like, what?
[38:43] Speaker 4: You know, some, if you're working with a 3rd party and you're kind of buying the card numbers and passing those along, you maybe have kind of some limitations there, but now with this app we can decide, it's like, is it PDFs?
[38:56] Speaker 4: Is it kind of a standard CSV format, whatever it may be?
[39:00] Speaker 4: We can kind of make those choices as we build it now and especially what works best for the business.
[39:08] Speaker 4: Yeah, so the, uh, the PDS is, uh, because we did the PDS, it gave, gave us the opportunity to, to send the Ziplo PDS, but, uh, there's, so for Amazon and Wawa, definitely, there's no existing card, right?
[39:25] Speaker 4: There's no formats, and that's the issue.
[39:28] system : At least in law, there's a format.
[39:29] You: Yeah, and we can make that format, and as an idea, like, we essentially make a, it could even be a pro-gift cards branded, you know, card that also has the vendor logo. Like, we can make, we can easily produce, like, fill gaps.
[39:30] Speaker 1: And...
[39:47] system : Hmm.
[39:49] You: So if you do like the idea of, you know, and maybe it's something on the customer end, they preserve, you know, sometimes getting just the number feels, you know.
[39:57] system : No, well, they never, they never get the number.
[40:00] Speaker 4: Right?
[40:01] Speaker 4: So they get a URL, which may have like blah blah, that they get a URL, which may have, uh, account number and a pin associated with it, in the in the slot.
[40:02] You: Oh right.
[40:10] You: Right.
[40:11] Speaker 4: But nobody ever gets that, that's why we had to do.
[40:15] Speaker 4: That's what Doug did in his very 1st Walmart customer was just sending the cards and they said, oh, what the heck is this?
[40:21] Speaker 4: So we had to, because, because, for Amazon, they didn't give us a card and so, uh, I mean, and Amazon is, that's what they deal with, but for the dogs and user, they don't like just receiving. Pins, you know?
[40:37] You: Yeah
[40:38] system : Uh, so we we generated uh, the cards for them, and that's why the PDS came in to think, so, um, but for, and then the other one would be, uh, uh, chapters.
[40:50] Speaker 4: Chapters is another one where they just give us numbers and you have to pass something that's presented to whether they get an earl or however they're going to receive it.
[40:58] Speaker 4: They needed some physical thing, which had the information, and it was more the, it's not the number, it's the barking.
[41:05] Speaker 4: We had to give them something with the barcos.
[41:07] system : That's a, that's, that's why we did the generation.
[41:07] You: Right.
[41:09] You: Got it.
[41:10] Speaker 4: And that just matters itself as a uh, as a PDS law.
[41:14] You: Got it.
[41:16] You: Okay.
[41:17] Speaker 3: So, so my little summary from layman's terms for my position, I say that, um, You know, um, I like the normalization.
[41:28] Speaker 3: I think I think it makes sense.
[41:30] Speaker 3: I think it just allows us to do lots of things.
[41:33] Speaker 3: Um, I hear Lloyd's message is pretty simple process.
[41:37] Speaker 3: We got this same thing that comes in that we're gonna probably just send to the client.
[41:41] Speaker 3: Right?
[41:42] Speaker 3: So, but I still, I still think the normalization is really important to kind of pull it all together, but I, I, I, I, I, I, I, like Floyd sort of challenging that, you know, some of it is pretty simple.
[41:58] Speaker 4: Just grabbing and we're going to be sending the same thing up.
[42:01] system : Well, Doug, the normalization is the stuff they have to do, they give you the features that you, like you want, inventory and all that kind of stuff, right?
[42:09] Speaker 4: So they need to put some stuff in place to basically, uh, say, you know, be able to have these objects in there and say, then, you know, you have to go to a screen or however it's going to be designed to say, how many success cards, right?
[42:22] Speaker 4: So they have to put it in a way that's going to be easy for them to do whatever programming they need to do, right?
[42:27] system : So, but, um, so it's not really, that's going to be done regardless of how simple the process is. If it's complicated or not, you know, so I, I, I, I don't want, uh, So, and and having said that, they, they, they're going to do when they write the program, they're going to do what they need to do to, to make sure that they give you what your requirements are.
[42:50] Speaker 4: But, we also need to make sure that it's, it, it's whatever is getting done does not take away from, you know, how, like, I would say a requirement is that it shouldn't matter what you, as long as they, they give you a format to put in.
[43:07] Speaker 4: So if it's a if it's a CSV, then whatever that CSV looks like.
[43:11] Speaker 4: It should be able to be put into the system and then normalize and then be able to, right, then you shouldn't need a change order to, to, to have that function.
[43:21] Speaker 4: That's a, that's what I would say is one of your requirements, right?
[43:25] Speaker 4: But maybe it's not as simple as I think, right?
[43:29] Speaker 4: So I'm just looking for what requirements, right?
[43:31] Speaker 4: So it shouldn't matter really in my brain.
[43:33] Speaker 4: That, uh, next day, uh, uh, one of the winners changes their format.
[43:40] Speaker 4: Well, it's coming in to into the vault as a CSV has different things.
[43:45] system : I'm pretty sure that they're gonna just say, oh, we've been giving you this.
[43:50] Speaker 4: Stuff in the file that is not really, we decide it's not really relevant, but in the end, the pieces of data that were always being sent through are still going to be there.
[44:01] Speaker 4: Right.
[44:02] Speaker 4: So, for instance, in in Starbucks, they had all this crap.
[44:08] Speaker 4: They had, uh, voided dates, this and this and then all this stuff in there.
[44:12] Speaker 4: Never, ever filled in.
[44:15] Speaker 4: Eso is the same.
[44:16] system : They have, uh, stuff that where you put in, um, uh, You know, I guess if you want to get the physical card, that has like, uh, I can't come up with a word, the art or whatever.
[44:29] Speaker 4: So something that's going to be an image on the part.
[44:31] system : There's a column there.
[44:33] Speaker 4: And they never.
[44:34] Speaker 4: There's never anything there, right?
[44:36] Speaker 4: So all of a sudden they, they decided that, oh, why are we sending this to Doug or whoever customers? Because it's never used, right?
[44:43] Speaker 4: So Starbucks took, but so they took out stuff.
[44:46] Speaker 4: But all this stuff that gets passed on the, to the customer is still in that style.
[44:51] Speaker 4: They just decide to eliminate stuff that they was never, I guess they figured this is in the feature we're private to the customer, which they never did anyway.
[44:59] Speaker 4: Right?
[45:00] Speaker 4: So that's the thing, right?
[45:01] Speaker 4: So I think if that happens, like it shouldn't really be a change.
[45:04] Speaker 4: Like start, they took away some columns.
[45:06] Speaker 4: But those columns were never really delivered.
[45:10] Speaker 4: Like, so that's why ours doesn't look the same as theirs.
[45:13] Speaker 4: So they said, well, why are we saying that?
[45:14] Speaker 4: There's no data in there.
[45:15] Speaker 4: So why are we putting a column with no data, right?
[45:18] Speaker 4: So I think the system should be able to handle that, but I don't know what cost.
[45:19] You: Yeah.
[45:21] You: No, absolutely.
[45:22] Speaker 4: And...
[45:23] You: And I would just say it's like, if you are, um, you know, you have your accounting system and you change your cleaning company, you don't have to go into your accounting system and build new software to allow you to change your cleaning company.
[45:42] You: You just have to log in and be able to say, okay, our cleaning company is now has a different name, and we just need to make sure that when payroll goes to pay our cleaning company, that it knows to look for a new company name.
[45:55] You: So we're basically just having data sets of merchants that we have to account for.
[46:00] You: But at the end of the day, the goal for anyone at Progressive who has to operate the workflow, they shouldn't have to think about any of this.
[46:09] You: It should really, it is, you know, simple as in inventory comes in, order comes in, we allocate from inventory to the order.
[46:18] You: Based on the type of merchants and cards in that order, we generate the output that matches. And then you take it and send it off.
[46:31] You: So, yeah, ultimately at the surface level, it's simple.
[46:34] You: The real complexity just comes from standardizing the format, maintaining audit history, ensuring that it's secure.
[46:44] You: Um, and then being able to plan for edge cases if there's ever an issue with uh, generation or anything, we just need a way to handle sort of the system errors.
[46:53] You: Um, um, but, you know, The goal is from an exterior standpoint is to probably make Doug think, Man, this is just so simple.
[47:04] You: How come we didn't do it this way before?
[47:06] You: Um, But the underlying build, in order for it to be that simple on the outside, it does require, you know, a lot of thinking about how that's done.
[47:17] You: Um, But, yeah, we definitely approached this in like, uh, If I had to solve this problem for Redsamp, this is what I would do.
[47:27] You: Because if your order volume doubles overnight, you can't have a system break.
[47:33] You: It has to be able to handle like growth, but we're also not building functionality because we anticipate that it's coming someday.
[47:41] You: We're just building for where you're at right now.
[47:44] You: Um, and then in such a way that we can easily add to it.
[47:48] You: Um, without breaking anything, without having to refactor the whole, you know, software architecture, but really just solving the main pain points.
[47:57] system : Okay
[47:58] You: Hopefully Lloyd doesn't have to get any more phone calls, you know, outside of, you know, at some point, maybe there's a way for us to get on with Walmart and figure out how to move that activation part.
[48:10] You: connection via API or something directly into the tool so that it doesn't have to have a separate piece, but that would be really the only, like, larger architecture change that I could anticipate in the next year would be, you know, at some point that would be awesome, but I don't know, um, feasibility on that.
[48:28] You: You know, but that's likely enough conversation.
[48:32] Speaker 4: So, okay, so, so I think it's a good idea that, um, to do like, pick specific vendors and do, um, like the, the work slow for those ones, right?
[48:41] You: Yeah.
[48:43] Speaker 4: I mean, I don't know, maybe Doug wants to, I don't need pictures. I just want to know what the, see what the, right?
[48:47] You: The data file.
[48:50] Speaker 4: Like, so the simple cases, like the pass through lines, and then I think then there's the generation ones, and then there's the generation, so these.
[48:58] system : I think it's Amazon.
[48:59] system : I think it's, uh, you know, uh, Walmart, and then,
[49:07] You: Oh, you went on mute there, like?
[49:10] Speaker 4: Yeah, I'm not touching anything.
[49:13] You: No, it's all good.
[49:13] Speaker 4: Doug was saying he couldn't hear me.
[49:14] You: Yeah.
[49:14] Speaker 4: So I think there's something wrong with why they have too much running on my computer.
[49:18] You: Oh, that's working now.
[49:18] Speaker 4: Um, Uh, so that, you know, I think that would, that would, uh, because when I was reading the, the documentation, it was just hard for me to map.
[49:28] You: Yeah.
[49:28] Speaker 4: Okay, well, I mean, I know what happened.
[49:31] Speaker 4: I just don't know how it maps into what I was reading, right, in the thing.
[49:34] You: Yeah, and, and there's.
[49:35] Speaker 4: I mean, at a high level, but then, but then, you know, so there is going to be, like you were talking about integration into Walmart.
[49:43] Speaker 4: Well, there's a, you know, basically it's an Excel file, and they just send, they have a proto, we send it to them, and they send back with, and then we just update the Excel file with what they said, that's right.
[49:53] Speaker 4: So, um, um, but that, you know, so, I know that they has to get into the system for, you know, then packaging and delivery, you know, but it's basically it's not going to be staying in inventory that, that long, right?
[50:08] You: Yeah
[50:09] Speaker 4: So that's what I'm thinking. And then it also needs the generation piece, right?
[50:13] Speaker 4: Send to the Walmart, get the cards, and put that in the Excel sign, we generate the cards, and then, so I think that's the point at which, after the generation, then it would go into, to, um, evolve.
[50:26] You: Yeah, yeah, exactly.
[50:29] You: Uh, and there's, there's a, I will definitely own the, uh, SW language in a few, uh, places when it comes to, like, the, the banner brands and system bind.
[50:42] You: I had I had a miss.
[50:44] You: I think I wrote system one or something in a few places.
[50:47] You: So a few areas where I had some errors in there that probably made it a little bit more confusing.
[50:53] You: Um, But I think we have a, you know, a better sense end to end and what we can follow up with as well is, um, kind of Tim has identified, like, uh, hosting and, you know, the security sort of layers that, um, we can also, you know, say, this is our current sort of recommendation.
[51:17] You: What I would say with software engineering is, um, We like to say this is what our current recommendation is, but oftentimes when we get into the actual build, there are some things we run into that we just had no way of planning for.
[51:30] You: So, we say, this is our recommendation being that we want to have a secure, stable, reliable host that never experiences, you know, and never is not the right word, that has like the 99.9% up time.
[51:45] You: Things happen, right?
[51:47] You: If Amazon servers go offline because of an infrastructure attack, not only is TD down, but, you know, everyone's down so that, you know, those are the French scenarios that do happen, not very often, but, um, Yeah.
[52:00] Speaker 4: Impressive, just AVTV, but not progressive.
[52:02] You: Yeah, um, so we'll include that.
[52:06] You: Um, and then, um, Yeah.
[52:07] Speaker 4: Is it going to be it's going to be on a server or something, which you guys are hosting?
[52:13] Speaker 4: Or you're using like an Amazon Services or something?
[52:13] You: Uh, So we would be using likely an AWS type equivalent.
[52:20] You: Um, like, um, Tim has has has won, uh, mapped out.
[52:26] You: So we'll share that with you, Lloyd, for you to check out and look at what we're what we're looking at there.
[52:34] You: Yeah.
[52:35] You: Um, but no, we wouldn't be managing the actual server infrastructure.
[52:40] You: It would be a managed, uh, you know, hosting hosted solution that is designed for this type of software application.
[52:48] You: Um, just, just because, uh, the last thing we want is to have a, a physical server sitting in, in your office that needs to be, uh, you know, physically maintained and have power back up and that sort of stuff.
[53:04] Speaker 4: So, so, um, and the cost for that server will be a monthly bill to that kind of thing or, okay.
[53:12] You: Yeah, yeah.
[53:13] You: And and nominal in in the scheme of things, yeah.
[53:13] system : So, so, yeah.
[53:16] Speaker 4: Yeah.
[53:18] Speaker 4: So, so, uh, and so I don't know who that is, but Doug, just for your, you know, when you're, um, you know, maybe, I don't know, Spencer, if you have an option for that, but Doug already has like system behind is doing stuff as well, right?
[53:33] Speaker 4: So it'd be good if, I don't know if they could do this service that, that you guys require through that, through their, their thing.
[53:40] Speaker 4: But, uh, For you, dog, they're supposed to getting bills from whatever, maybe.
[53:45] Speaker 4: Maybe a thing to see is, you can get Spencer in touch with them and see if that, if they provide a, uh, launch from it, that would work for.
[53:54] Speaker 4: They need to do for the, for, um, the adult.
[53:58] You: Yep.
[53:59] You: And and the likelihood is, is system buying would likely be just passing on the bill for the same company we would be picking, you know, at the end of the day.
[54:09] system : Okay. Okay.
[54:09] You: Um, You know, and I know that, um, Yeah, and we can talk about that.
[54:17] Speaker 4: Yeah, it's a, it's a, yeah, I'm just, because it's not my,
[54:17] You: We want to, you know, not add that.
[54:21] Speaker 4: not my area.
[54:22] Speaker 4: expectation right now.
[54:22] Speaker 3: That's why I don't know what makes sense, but I was just throwing that out there in terms of, uh, you know, if you're paying more costs for like infrastructure costs to, you know, the service thing, maybe it makes sense to use the same indolent. And is there, is there any way that what, what red stamp is doing, can replace what system buying is doing, or those is system binds totally needed?
[54:35] You: Yeah, yeah, we can certainly look at that.
[54:48] Speaker 3: Or whatever we're paying them to do.
[54:51] Speaker 4: I don't, you know, I mean, I know that. Well, they have the right system of mine had to write software to, uh, to manage, you know, do the uploads of the, of the, of the, of the, uh, Turn them into...
[55:08] Speaker 4: the zits allows to generate the or else, right?
[55:10] Speaker 4: So it's their, they, they have to do some work, right?
[55:14] Speaker 4: Other people can do that.
[55:14] You: Yeah.
[55:16] Speaker 4: That's that's true.
[55:17] You: Yeah, and, Yeah, I would say the, the system buying peace is probably the part that I'm least familiar with.
[55:17] Speaker 4: But then, but you'd have to, they'd have to write that something.
[55:25] You: Um, But I would say that if what I'm hearing it correctly is they're handling the sort of URL generation and ensuring that those URLs are basically up and accessible to customer, like, that is something that could easily be replaced likely, but I don't want to speak unless Tim and I chat about it a little bit more.
[55:27] system : No.
[55:50] You: I would say, like, for initial run, leave that piece in place until we get the vault working, and then, um, the likelihood is, is that is potentially something that could be folded in into, into one sort of software stack, vertical versus relying on another vendor, because that just, again, increases your risk of something changes there, and then all of a sudden all the, the, URL generation, we need to run all of a sudden stops, you know, working
[56:21] You: working.
[56:21] You: So they are in the dependency chain right now for you to successfully deliver to your customer.
[56:27] You: Yeah, didn't want to rock any more boats, uh, to start.
[56:33] You: We'd rather get the foundation in place and then, you know, potentially there's an opportunity to do a swap there needed.
[56:42] system : Sounds good.
[56:44] You: And I, So what I would propose, Doug, is, um, we will put together a modified statement of work.
[56:45] system : So what?
[56:56] You: And what I will do is make sure that we update in the new version you get, I'll highlight everything in yellow that has changed.
[57:09] system : Okay.
[57:09] You: Um, Just so that, um, You know, it makes sense, and then likely just, you know, as a companion to that, just a very simple, like, these are the questions that James had or that Lloyd had, you know, these are the ones we discussed on the call, and then just making sure there's a bit of commentary on how the SMW kind of addresses the questions that you had.
[57:37] You: Um, Because I think everything else, um, You know, most every question sort of sort of like falls under that normalization umbrella with, you know, just the brands and the merchants and whatnot.
[57:52] Speaker 3: Yeah, well, my feeling is I, as long as you get the message across and your meaning or requirements, I don't think you need to get into,
[58:02] Speaker 3: don't worry about dealing with every question, you know what I mean?
[58:04] You: Okay, yeah.
[58:05] Speaker 3: I think we're a little...
[58:07] Speaker 3: Don't worry about that.
[58:08] Speaker 3: Just give us the best modified statement of work.
[58:11] Speaker 3: You can yell highlight, which is, which is good.
[58:12] You: Yeah.
[58:14] system : Lloyd wants to see, obviously see the workflows and stuff, but don't don't worry about it.
[58:19] You: Okay.
[58:19] Speaker 3: Uh, you know, answering specific questions.
[58:23] Speaker 3: Let's just get on with that.
[58:24] system : Give us the best of what you think on this conversation and the back and forth we have by email.
[58:30] Speaker 3: Let's let's get on with it.
[58:32] Speaker 3: So.
[58:32] You: Okay, yeah.
[58:33] You: Loud and clear.
[58:35] You: And and thanks for your time.
[58:35] Speaker 3: Yeah, no, I, you know, I,
[58:38] You: I know it's complex and I turned off my air conditioning before the call so I could make sure I could hear everything and I'm sitting here like sweating like a pig under my long sleeve shirt.
[58:47] You: Getting into that.
[58:48] Speaker 2: One sleeve shirt.
[58:50] Speaker 2: Charlie, because you have air conditioning.
[58:50] You: Yeah, because I had I had it on earlier and then I got cold because I'm, you know, I'm scrawny.
[58:57] Speaker 3: Um, So why did we, did we cover everything that you think we needed to cover?
[58:58] You: First world problem.
[59:03] Speaker 3: Lloyd?
[59:03] Speaker 4: Do you think we covered everything or? Yeah, no, for sure, for sure.
[59:07] Speaker 4: I think, um, yeah, so my, I just, you know, from just doing software in the past, like, I just want to see like, okay, well, what's, what are the souls, right?
[59:16] system : So that you don't see, like, I think it's hard for, for you to see, like, and I think you need to, you know, be, you don't have to understand, like, how everything works, but you need to, uh, you're in the office there, you see how people work.
[59:29] Speaker 4: You need to understand how, you know, and there's it, and make sure that it's truly simplifying things that people that are, you're going to have in your office don't need to be computer scientists to, uh, which I don't think that they will be, but, um, you know, so that's why I just want to see what, what are the flows? Because, I mean, I know what needs to be done, and, and, uh, I, you know, I just want to be able to map for that, that, um, the flow process and sort of makes sense from, uh,
[59:42] You: Yeah
[59:45] You: Yeah.
[59:58] Speaker 4: You know, okay, well, what does that mean for the car generation and all that?
[1:00:02] Speaker 4: right?
[1:00:02] Speaker 4: How is that swelling into the vault?
[1:00:06] system : Well, the big test on the vault will be whether Doug Beers can actually do it.
[1:00:09] Speaker 3: So if I can do it, we're good.
[1:00:12] Speaker 3: That'll be the one.
[1:00:12] You: Chall Challenge accepted.
[1:00:13] Speaker 3: Yeah, that'll be the difference.
[1:00:14] You: And and we are, we are, um, part of this is, um, including, you know, Candace and Caitlin from our design practice side for, um, sort of making sure the user experience and the interface is is considered because obviously, Engineers go right to, you know,
[1:00:35] You: Acceptance criteria met, but we also want to make sure that when it comes to thinking about, you know, Doug having to use it and someone else, like, it making it as simple as possible so that, like, you log in and it's very obvious how you how you move through each step.
[1:00:52] You: I think that's important.
[1:00:53] You: Not that we're building, you know, Doesn't need to be overthought, but where it can be, you know, simple and clearly communicated visually on screen as you use a tool is always helpful.
[1:01:05] You: Nothing is worse than, you know, downloading a new tool and opening it up and just being like, okay, like there's literally no guide here for me that helps me understand how I need to use those tools.
[1:01:16] You: So that's something that we are factoring in just to make sure that it's, um, that it's easy and obvious.
[1:01:23] Speaker 3: And how about general timing?
[1:01:26] Speaker 3: Where are we still kind of at?
[1:01:28] Speaker 3: You know, kind of 8 weeks sort of like my vision is ready to go like for one kind of thing.
[1:01:35] Speaker 3: Are we still think we're on that timeline?
[1:01:38] You: Let, let me and Tim chat on timing again.
[1:01:43] You: I know he is on vacation next week.
[1:01:44] system : Sure.
[1:01:45] You: Um, But if we, yeah, our goal is to get everything sort of locked down and signed off.
[1:01:53] You: Um, you know, he's actually already put in a significant amount of work into how the architecture works.
[1:02:00] You: So, um, that that certainly gives us a boost.
[1:02:01] system : Yeah
[1:02:04] You: But yeah, let us just chat.
[1:02:06] You: I don't want to, I don't want to just pluck a number out of the sky, but, um, obviously our goal is to to deliver as quickly as we can while making sure the quality and the testing have been done.
[1:02:06] system : No.
[1:02:08] system : No.
[1:02:17] You: Um, just so that, you know, the last one you want is the, you know, you get a new Harley and you get out there for your 1st cruise during the World Cup and then the back wheel comes flying off and you're tossed into the crowd.
[1:02:17] system : Yeah.
[1:02:30] You: that doesn't go well for anyone.
[1:02:31] You: So, just want to make sure we, uh,
[1:02:31] Speaker 3: But, you know, of course, you know, our whole world kind of starts to begin to wrap up, you know, after black. You know, once we're in October, it's like, it's sort of too late.
[1:02:37] You: Yeah, absolutely.
[1:02:39] You: So also like, Yeah, no, yeah, very, very, that keeping that very front of mind.
[1:02:44] Speaker 3: You know what I mean?
[1:02:45] Speaker 3: It's just, yeah.
[1:02:49] You: So.
[1:02:49] Speaker 3: Okay, good.
[1:02:50] You: Yeah.
[1:02:51] Speaker 3: Okay.
[1:02:52] You: All right.
[1:02:53] system : Great.
[1:02:54] Speaker 3: Yeah, I really like this couple.
[1:02:56] Speaker 3: I think we got down to, you know, real meat and potato serious sort of thing.
[1:03:02] Speaker 3: So I'm really happy with, with, uh, with.
[1:03:04] You: Yeah, and again, thanks, Lloyd.
[1:03:04] Speaker 3: So...
[1:03:07] You: I know we've, you know, gleaned information from you originally during discovery and then follow up, just the little details really help. Just the last thing you want to do is, um, you know, get it, get it ready to go and then all of a sudden we missed one like critical thing.
[1:03:24] You: So that's why we kind of did, um, you know, really want to kick the tires here to make sure that that we've accounted for everything.
[1:03:31] You: And so I think those clothes will obviously help with that.
[1:03:34] You: But, um,
[1:03:36] You: Yeah.
[1:03:36] Speaker 1: Okay. That's good.
[1:03:38] You: Yeah.
[1:03:39] You: Okay, well, we'll, uh, check back in likely, um, uh, sometime, uh, at tomorrow or Thursday, and then, uh, we can get, uh, that, that SOW in front of you and then, uh, and then get kicked off and, um, Yeah, excited, excited to get started and get building.
[1:03:48] system : Okay.
[1:04:02] system : Yeah.
[1:04:03] Speaker 3: Sounds good.
[1:04:04] Speaker 3: Okay, thank you.
[1:04:05] You: Yep.
[1:04:05] Speaker 3: Thanks, everyone, and what's up, again, thought it was a good call.
[1:04:07] You: Okay, take care.
[1:04:08] Speaker 3: So.
[1:04:09] Speaker 1: Perfect, thank you.
[1:04:10] You: Bye.
[1:04:10] Speaker 1: Bye.
